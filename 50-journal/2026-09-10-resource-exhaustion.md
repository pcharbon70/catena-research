---
title: "2026-09-10 Resource Exhaustion"
kind: journal
created: "2026-09-10"
tags: [specification, conformance, implementation-limits, runtime]
aliases: []
---

# 2026-09-10 Resource Exhaustion

## Scope

Execute [P129](../20-notes/language-completion-plan-delivery.md#item-129-resource-exhaustion)
from compiler C130 merge `e3a2e98bc5949511ec4aadd6e7dc6094a2a3cb33`.
Revision `0.1.75` is covered by the user's session-wide approval.
Compiler PR [157](https://github.com/pcharbon70/catena/pull/157) merged feature
commit `a144e951e23ab09dcae4d0bb6cf1c4a3c07a2d2e` as
`af912f4282031e0c52041fd08a5e5ec6be6d0e09` into `rewrite`.

## Implementation decisions

CP-129-1..3 retain their recommendations. Each implementation fork below
compares four alternatives and selects the recommendation.

| Decision | Four alternatives | Recommended and selected |
| --- | --- | --- |
| RX-I01 Aggregate dimensions | A only per-file limits; B files, source bytes, decoded nodes, and publication bytes; C wall-clock timeout; D resident memory only | B: the four deterministic dimensions cover compiler-wide amplification without making host measurements semantic. |
| RX-I02 Portable floors | A no floors; B 128 files, 16 MiB source, 100,000 nodes, and 16 MiB output; C bootstrap maxima as floors; D platform-derived values | B: meaningful cross-implementation minima leave room for a larger bootstrap profile. |
| RX-I03 Source measurement | A characters; B exact bytes across the complete de-duplicated input set; C compressed bytes; D largest file only | B: exact input bytes are stable and aggregate many small files. |
| RX-I04 Tree measurement | A AST leaves only; B recursive maps/lists/tuples/structures, keys, and leaves; C allocator words; D parser tokens only | B: one representation-independent traversal covers decoded JSON and kernel structures. |
| RX-I05 Entry integration | A CLI only; B public JSON/kernel/SCC and package boundaries; C tests call the budget directly; D backend only | B: every retained compiler transaction crosses the shared budget. |
| RX-I06 Package inputs | A modules only; B manifest, modules, interfaces, governance, and trust root; C manifest only; D directory total | B: all semantic package inputs count while unrelated directory files do not. |
| RX-I07 Publication | A write then measure; B prepare all outputs, measure, then commit transactionally; C truncate; D publish modules independently | B: exhaustion cannot create a partial successful package. |
| RX-I08 Runtime layer | A redefine raw send; B explicit bounded queue above raw send; C poll mailbox length; D silent drop | B: capacity-sensitive code opts into observable admission without changing C010. |
| RX-I09 Capacity dimensions | A messages only; B messages plus deterministic external-size bytes; C resident heap only; D reductions | B: count and logical byte pressure are exact while physical memory remains a deployment fact. |
| RX-I10 Overload | A silent drop; B explicit reject or terminal exhaustion selected at creation; C block forever; D retry automatically | B: both outcomes are visible and preserve producer intent. |
| RX-I11 Ownership | A every holder consumes; B shared offer authority with creator-only take/stats/close; C global name; D implicit transfer | B: several producers compose while lifecycle and consumption remain unambiguous. |
| RX-I12 Cancellation | A abandon the process; B owner death cancels and close reports discarded count/bytes; C drain forever; D transfer to supervisor | B: cleanup is bounded and the unprocessed state is observable. |
| RX-I13 Host failure | A promise recovery; B declare VM/OS fatal exhaustion outside recoverable semantics; C map all failure to a value; D ignore it | B: the guarantee matches what the BEAM and host can support. |
| RX-I14 Diagnostics/profile | A prose errors; B stable LIM006–LIM009 details plus complete machine disclosure; C exceptions; D one generic limit | B: exact thresholds, repair information, and residual limits are auditable. |

## Verification route

Exercise every aggregate threshold and next unit, many small sources, a retained
public compiler path, FIFO rejection with no loss, cleanup of a full queue after
rejection, multiple producers, owner-only operations, forged handles, terminal
overload, owner notification, owner-death cancellation, and the conformance
profile. Run the complete compiler suite, production warnings-as-errors build,
escript construction, trusted-boundary audit, and archive validator.

## Results

The compiler adds one shared aggregate budget to JSON, kernel, SCC, and package
transactions; it budgets complete package outputs before publication. An opaque
bounded runtime queue enforces positive message and external-size byte capacities,
explicit rejection or termination, FIFO admission, owner-only consumption and
bounded cancellation. Raw send remains unchanged and host-fatal exhaustion is
disclosed rather than converted into a false language result.

Six focused resource tests pass as part of 1,038 compiler tests. Production
compilation with warnings as errors, escript construction, and the reviewed trust
inventory audit pass. The
[normative contract](../60-specification/resource-exhaustion/aggregate-budgets-and-runtime-admission.md)
promotes P129 to C129.
