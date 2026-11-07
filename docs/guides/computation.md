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

## Checks

Replay in a clean environment before claiming reproducibility. An independent reviewer reruns the prescribed computations, keeping frozen inputs separate from regenerated outputs. Include negative controls, or a comparison by an independent method or a second system, wherever an error could pass unnoticed. Record the numerical precision, and any mathematical interpretation of the output that has not been verified. Check the runtime actually available; this guide installs nothing.
