# MIT License. Copyright (c) 2026 Pratik Apshinge (Math Research Vessel,
# https://github.com/PCeltide/math-research-vessel).
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
"""Citation-use map and statement fingerprints for a LaTeX document.

Usage: python cite_map.py ENTRY.tex --out NEW.json [--previous OLD.json]

Follows \\input/\\include from ENTRY, ignores comments, handles multi-line
citations. With --previous, carries stable IDs (K001...) forward and classifies
each use as unchanged / changed-locator / changed-context / new / removed;
IDs are never reused (the map keeps a high-water mark). Fingerprints every
statement environment declared with \\newtheorem plus the common defaults, and
reports statements changed, relabelled, added or removed. Proofs are not
fingerprinted. Standard library only.
A map locates uses; it never checks that a source supports them.
"""
import argparse
import bisect
import hashlib
import json
import os
from pathlib import Path
import re

# \nocite and \citestyle are not uses; \citeauthor and friends are.
CITE = re.compile(r"\\(?:[Cc]ite(?:t|p|alt|alp|author|year|yearpar|num)?|[Pp]arencite|[Tt]extcite|[Aa]utocite|"
                  r"[Ff]ootcite|[Ss]martcite|supercite)(?![A-Za-z])\*?\s*((?:\[[^\]]*\]\s*){0,2})\{([^}]*)\}")
INPUT = re.compile(r"\\(?:input|include)\s*\{([^}]*)\}")
NEWTHEOREM = re.compile(r"\\(newtheorem\*?|spnewtheorem\*?|declaretheorem)\s*(?:\[([^\]]*)\]\s*)?\{([^}]*)\}")
FORMAT = 2  # bump when fingerprints change meaning; older maps are not compared
DEFAULT_ENVS = {"theorem", "proposition", "lemma", "corollary", "definition", "example",
                "remark", "conjecture", "question"}
LABEL = re.compile(r"\\label\{([^}]*)\}")
BOUNDARY = re.compile(r"(?<=[.!?])\s+(?=[A-Z\\$])|\n\s*\n|\\(?:begin|end)\{[^}]*\}")
CODE = re.compile(r"(?:[^\\%]|\\.)*")  # text up to the first unescaped %


def strip_comments(text):
    """Drop % comments (an even run of backslashes before % leaves it a comment)."""
    return "\n".join(CODE.match(line).group(0) for line in text.split("\n"))


def collect(entry):
    root, order, warnings, seen = entry.resolve().parent, [], [], set()

    def show(path):
        return Path(os.path.relpath(path, root)).as_posix()

    def walk(path):
        if path in seen:
            return
        seen.add(path)
        if not path.is_file():
            warnings.append(f"missing input: {show(path)}")
            return
        raw = path.read_bytes()
        try:
            text = raw.decode("utf-8-sig")
        except UnicodeDecodeError:
            text = raw.decode("utf-8", errors="replace")
            warnings.append(f"not UTF-8, undecodable bytes replaced: {show(path)}")
        text = strip_comments(text)
        order.append((show(path), text))
        for name in INPUT.findall(text):
            name = name.strip()
            walk((root / (name if name.endswith(".tex") else name + ".tex")).resolve())

    walk(entry.resolve())
    return order, warnings


def normalize(text):
    return " ".join(CITE.sub(lambda m: r"\cite{" + re.sub(r"\s", "", m.group(2)) + "}", text).split())


def extract(entry):
    order, warnings = collect(Path(entry))
    envs, unnumbered = set(DEFAULT_ENVS), set()
    for _, text in order:
        for command, options, names in NEWTHEOREM.findall(text):
            found = {n.strip() for n in names.split(",") if n.strip()}
            envs |= found
            if command.endswith("*") or "numbered=no" in options.replace(" ", ""):
                unnumbered |= found
    statement = re.compile(r"\\begin\{(%s)(\*?)\}(.*?)\\end\{\1\*?\}" % "|".join(map(re.escape, sorted(envs))), re.S)
    uses, statements = [], []
    for name, text in order:
        starts = [0] + [m.end() for m in re.finditer("\n", text)]
        bounds = [0] + [m.end() for m in BOUNDARY.finditer(text)] + [len(text)]
        for m in CITE.finditer(text):
            i = bisect.bisect_right(bounds, m.start()) - 1
            sentence = normalize(text[bounds[i]:bounds[i + 1]])
            optional = re.findall(r"\[([^\]]*)\]", m.group(1))
            locator = " ".join(optional[-1].split()) if optional else ""
            for key in filter(None, (k.strip() for k in m.group(2).split(","))):
                uses.append({"key": key, "file": name, "line": bisect.bisect_right(starts, m.start()),
                             "locator": locator, "sentence": sentence})
        for n, m in enumerate(statement.finditer(text), 1):
            body = m.group(3)
            label = LABEL.search(body)
            statements.append({"id": label.group(1) if label else f"{name}:{m.group(1)}#{n}",
                               "env": m.group(1), "numbered": not m.group(2) and m.group(1) not in unnumbered, "file": name,
                               "line": bisect.bisect_right(starts, m.start()),
                               # Environment included (conjecture -> theorem is a change); labels excluded,
                               # so a pure relabelling keeps its fingerprint.
                               "sha256": hashlib.sha256((m.group(1) + "\x00" + " ".join(LABEL.sub("", body).split())).encode()).hexdigest()})
    if not statements:
        warnings.append("no statements fingerprinted; environments searched: " + ", ".join(sorted(envs)))
    commands = sum(len(CITE.findall(text)) for _, text in order)
    return {"format": FORMAT, "entry": Path(entry).name, "files": [n for n, _ in order], "uses": uses, "commands": commands,
            "statements": statements, "statement_envs": sorted(envs), "warnings": warnings}


def compare_statements(before, after):
    """Match identical text first (so moved or relabelled statements pair up), then IDs."""
    pending = list(before)
    unchanged, relabelled, changed, added = [], [], [], []
    rest = []
    for s in after:
        same = [b for b in pending if b["sha256"] == s["sha256"]]
        if same:
            b = next((b for b in same if b["id"] == s["id"]), same[0])
            pending.remove(b)
            if b["id"] == s["id"]:
                unchanged.append(s["id"])
            else:
                relabelled.append([b["id"], s["id"]])
        else:
            rest.append(s)
    for s in rest:
        b = next((b for b in pending if b["id"] == s["id"]), None)
        if b:
            pending.remove(b)
            changed.append(s["id"])
        else:
            added.append(s["id"])
    return {"changed": sorted(changed), "relabelled": relabelled, "added": sorted(added),
            "removed": sorted(b["id"] for b in pending), "unchanged": len(unchanged)}


def classify(current, previous):
    """Carry IDs forward. Passes run from strictest match to loosest."""
    old = list(previous["uses"])
    taken, result = set(), {}
    passes = (("unchanged", ("key", "file", "sentence", "locator")),
              ("changed-locator", ("key", "file", "sentence")),
              ("changed-context", ("key", "file", "locator")))
    for label, fields in passes:
        for i, use in enumerate(current["uses"]):
            if i in result:
                continue
            matches = [j for j, o in enumerate(old) if j not in taken and all(o[f] == use[f] for f in fields)]
            if matches:
                taken.add(matches[0])
                result[i] = (label, old[matches[0]]["id"], len(matches) > 1)
    # High-water mark: never reuse an ID, including IDs retired in any earlier map.
    seen_ids = [o["id"] for o in old + previous.get("removed", [])]
    number = max([int(i[1:]) for i in seen_ids] + [previous.get("max_id", 0)])
    for i, use in enumerate(current["uses"]):
        if i not in result:
            number += 1
            result[i] = ("new", f"K{number:03d}", False)
        use["class"], use["id"], ambiguous = result[i]
        if ambiguous:
            use["ambiguous"] = True
    current["removed"] = [o for j, o in enumerate(old) if j not in taken]
    current["max_id"] = number
    if previous.get("format") == FORMAT:
        current["statement_changes"] = compare_statements(previous.get("statements", []), current["statements"])
    else:
        current["statement_changes"] = None
        current["warnings"].append("previous map has an older format; statements not compared, rerun the gate on a fresh pair of maps")
    return current


def number(result):
    """IDs for a first map."""
    for n, use in enumerate(result["uses"], 1):
        use["id"], use["class"] = f"K{n:03d}", "new"
    result["max_id"] = len(result["uses"])
    return result


def summary(result):
    counts = {}
    for use in result["uses"]:
        counts[use["class"]] = counts.get(use["class"], 0) + 1
    if "removed" in result:
        counts["removed"] = len(result["removed"])
    return {"uses": len(result["uses"]), "commands": result["commands"], "classes": counts,
            "statements": len(result["statements"]),
            "numbered": sum(s["numbered"] for s in result["statements"]),
            "statement_changes": result.get("statement_changes"),
            "ambiguous": [u["id"] for u in result["uses"] if u.get("ambiguous")],
            "warnings": result["warnings"]}


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("entry", type=Path)
    parser.add_argument("--out", type=Path, required=True)
    parser.add_argument("--previous", type=Path)
    args = parser.parse_args()
    if args.out.exists():  # earlier maps stay frozen; write each map to a new versioned name
        parser.error(f"{args.out} exists; choose a new name such as cite-map-vN.json")
    result = extract(args.entry)
    if args.previous:
        try:
            previous = json.loads(args.previous.read_bytes().decode("utf-8"))
        except (OSError, ValueError) as error:
            parser.error(f"cannot read --previous {args.previous}: {error}")
        if not isinstance(previous, dict) or not isinstance(previous.get("uses"), list):
            parser.error(f"--previous {args.previous} is not a citation-use map")
        if previous.get("entry") != result["entry"]:
            result["warnings"].append(f"previous map is for {previous.get('entry')!r}, not {result['entry']!r}; check the argument order")
        result = classify(result, previous)
    else:
        result = number(result)
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(result, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
    print(json.dumps(summary(result), indent=1))


if __name__ == "__main__":
    main()
