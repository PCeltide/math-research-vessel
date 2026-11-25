# Computation

A computation is evidence at its stated scope. A program that runs successfully does not prove its mathematical interpretation. This covers scripts in any system, such as Python with SymPy or NumPy, SageMath, Macaulay2, GAP, PARI/GP, Magma, Mathematica or Maple.

## Record

For each computation that supports a claim, record:
- the exact inputs and their identities;
- the algorithm, parameters and domain;
- the environment and pinned versions, including the system's own version;
- the command, exit status, outputs and output hashes;
- an interpretation bounded by the claim it supports.

Keep scripts in Git. Large outputs and caches stay outside Git, bound by hashes. A worksheet or notebook that supports a claim is exported to a script, or kept with its exact cell outputs.

## Kinds of computational evidence

Label each kind, because the article and reports treat them differently:
- **used in a proof:** a premise of the argument; it must be reproducible and reviewed;
- **independent corroboration:** an independent check of a result proved otherwise;
- **exploratory:** a search or experiment that guides the work. It stays exploratory until the dictionary to the mathematics and an independent check are complete, and it is never a premise.

A finite search never proves a universal statement or a nonexistence claim. State the coverage it actually had.

## Article computation ledger

When several computations bear on a paper, keep a short ledger keyed to its statements or examples. For each row give the quantity tested, script and inputs, a control capable of revealing a wrong sign or index, range, replay command, output identity, and the geometric or theoretical premise the code assumes. Mark a proposed check, an author replay and an independent replay separately. A second implementation that works from defining equations can distinguish two arguments whose output tables agree. Print only the checks whose interpretation helps the reader. An ordinary script is enough when it answers the question.

Added 2026-11-25 to connect reproducible computations to the article claims they test.

## Checks

Replay in a clean environment before claiming reproducibility. An independent reviewer reruns the prescribed computations, keeping frozen inputs separate from regenerated outputs. Include negative controls, or a comparison by an independent method or a second system, wherever an error could pass unnoticed. Record the numerical precision, and any mathematical interpretation of the output that has not been verified. Check the runtime actually available; this guide installs nothing.
