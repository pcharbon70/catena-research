---
title: "2026-09-10 Optimizer Validity"
kind: journal
created: "2026-09-10"
tags: [specification, optimization, semantics, conformance]
aliases: []
---

# 2026-09-10 Optimizer Validity

## Scope

Execute [P135](../20-notes/language-completion-plan-delivery.md#item-135-optimizer-validity)
at revision `0.1.86`. CP-135-1..3 retain their recommended selections. The
slice inventories existing transformation owners and adds a small checked
optimizer whose enabled rules have locally replayable premises. It does not
generalize C004's sampled law evidence or select public syntax.

## Implementation decisions

| Decision | Four alternatives | Recommended and selected |
| --- | --- | --- |
| OP-I01 Default mode | A always optimize; B disabled unless checked selected; C release-only; D host-dependent | B: retained compilation behavior stays explicit. |
| OP-I02 Initial domain | A every feature; B verified kernel expressions; C BEAM peepholes; D source tokens | B: transformations begin after checking and before lowering. |
| OP-I03 Rule inventory | A implicit patterns; B closed named list; C plugin callbacks; D compiler heuristics | B: conformance can identify every enabled semantic rewrite. |
| OP-I04 First rules | A annihilation; B literal arithmetic and right identities; C inlining; D fusion | B: the removed work is a checked total literal. |
| OP-I05 Existing transforms | A call all optimizer rules; B classify by current owner and contract; C ignore; D disable compiler | B: specialization, layouts, conditions, comprehensions, and lowering keep their existing authority. |
| OP-I06 Input authority | A trust annotations; B independent core verification; C backend acceptance; D tests only | B: malformed evidence cannot enter rewriting. |
| OP-I07 Output authority | A trust construction; B independently reverify; C compare types only; D BEAM compile | B: every transformed core must satisfy the full verifier. |
| OP-I08 Certificate shape | A rule name; B rule/path/digests/premises/digest; C text log; D none | B: each local step is attributable and tamper-evident. |
| OP-I09 Certificate checking | A inspect fields; B replay from original core; C trust optimizer; D sample output | B: certificate order and applicability are machine checked. |
| OP-I10 Traversal | A hash order; B stable child-before-parent order; C parallel race; D random | B: nested rewrites and evidence reproduce exactly. |
| OP-I11 Law evidence | A tested laws authorize; B require stronger checked premises; C promised laws authorize; D names imply laws | B: sampled equality cannot establish contextual equivalence. |
| OP-I12 Annihilation | A always rewrite; B refuse nonliteral removed work; C assume purity; D retry tests | B: traps, divergence, effects, and calls remain observable. |
| OP-I13 Call multiplicity | A ignore; B preserve exact count and order; C permit duplication; D compare final value | B: strict evaluation makes calls externally relevant. |
| OP-I14 Provenance | A use child span; B retain transformed whole-expression observation; C delete spans; D synthetic user spans | B: diagnostics remain attributable without fabricated source. |
| OP-I15 Compiler metadata | A omit optimizer; B preserve mode, rules, digests, certificates, refusals; C print log; D timestamp | B: build evidence explains what ran. |
| OP-I16 Invalid requests | A ignore; B reject unknown and duplicate rules; C enable nearest name; D warn | B: the selected optimizer is exact. |
| OP-I17 Large trees | A special semantics; B identical stable semantics under host bounds; C truncate; D skip certificates | B: size does not weaken correctness conditions. |
| OP-I18 Proof wording | A tests prove optimizer; B finite-evidence disclaimer; C imply preservation; D omit scope | B: C134 comparisons remain empirical evidence. |

## Results

Compiler [PR 169](https://github.com/pcharbon70/catena/pull/169) merged feature
commit `7c1e12d` as merge commit
`047d6f129b71e70c9a4b72408bf3b30fc3bf73b4` into `rewrite`.
`Catena.Optimizer` verifies and digests input, applies the two-rule closed
inventory in stable postorder, emits and replays certificates, verifies output,
and records unsafe annihilation as a refusal. `Catena.compile_kernel/2` exposes
explicit disabled and checked modes and binds evidence into metadata.
Compiler [PR 170](https://github.com/pcharbon70/catena/pull/170) then corrected
the focused tags to the unique `OZ-OBL-*` namespace at merge commit
`8492cdf5f4cf6fb88be537058ccf2cab7d9000ad`; its nine focused tests passed.

Nine focused cases cover inventory, positive rules, certificate tampering,
disabled/checked reference and BEAM agreement, annihilation refusal, trap
preservation, exact-once calls, 128-level deterministic trees, lifecycle and
invalid requests. The complete suite has 1,115 tests; 1,114 passed in the full
gate immediately before the final focused witness, which also passed.
Production compilation with warnings as errors, escript construction, trust
inventory audit, and diff checks pass. The
[normative contract](../60-specification/optimizer-validity/checked-rewrites-and-observation-preservation.md)
promotes P135 to C135 without claiming a general optimizer proof.
