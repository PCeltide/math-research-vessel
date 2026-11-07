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
"""Query TheoremSearch (theoremsearch.com) without credentials. Standard library only.

Usage: python tools/theorem_search.py "query" [--limit N] [--transport mcp|rest] [--out FILE]

Prints {query, endpoint, retrieved_utc, results} as JSON; --out also saves it as
evidence. Exit 1 on network or API failure. Hits are leads for retrieval: read
the primary source before relying on any result.
"""
import argparse
from datetime import datetime, timezone
import json
from pathlib import Path
import sys
import urllib.request

BASE = "https://api.theoremsearch.com"


def search(query, limit=5, transport="mcp"):
    if transport == "rest":
        endpoint, payload = BASE + "/search", {"query": query, "n_results": limit}
    else:
        endpoint = BASE + "/mcp"
        payload = {"jsonrpc": "2.0", "id": 1, "method": "tools/call",
                   "params": {"name": "theorem_search", "arguments": {"query": query, "n_results": limit}}}
    request = urllib.request.Request(endpoint, data=json.dumps(payload).encode(), headers={
        "Content-Type": "application/json", "Accept": "application/json, text/event-stream"})
    with urllib.request.urlopen(request, timeout=45) as response:
        result = json.load(response)
    if not isinstance(result, dict):
        return {"query": query, "endpoint": endpoint,
                "retrieved_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"), "results": result}
    if "error" in result or result.get("result", {}).get("isError"):
        raise RuntimeError(json.dumps(result))
    if transport == "mcp":
        answer = result["result"]
        result = answer.get("structuredContent")
        if result is None:
            result = json.loads(next(c["text"] for c in answer["content"] if c.get("type") == "text"))
    return {"query": query, "endpoint": endpoint,
            "retrieved_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"), "results": result}


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("query")
    parser.add_argument("--limit", type=int, default=5, help="number of hits (positive)")
    parser.add_argument("--transport", choices=["mcp", "rest"], default="mcp")
    parser.add_argument("--out", type=Path)
    args = parser.parse_args()
    if not args.query.strip() or args.limit < 1:
        parser.error("a nonempty query and a positive limit are required")
    try:
        record = search(args.query, args.limit, args.transport)
    except (OSError, RuntimeError, KeyError, ValueError, StopIteration) as error:  # OSError covers URLError and timeouts
        print(f"TheoremSearch unavailable: {error}", file=sys.stderr)
        raise SystemExit(1)
    text = json.dumps(record, ensure_ascii=False, indent=1)
    print(text)  # printed first, so a failed save never loses the result
    if args.out:
        try:
            args.out.parent.mkdir(parents=True, exist_ok=True)
            args.out.write_bytes((text + "\n").encode("utf-8"))
        except OSError as error:
            print(f"Could not save to {args.out}: {error}", file=sys.stderr)
            raise SystemExit(1)


if __name__ == "__main__":
    main()
