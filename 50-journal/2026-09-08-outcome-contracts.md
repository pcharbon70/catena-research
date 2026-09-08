---
title: "Outcome Contract Implementation"
kind: journal
created: "2026-09-08"
tags:
  - language-design
  - algebraic-data-types
aliases: []
---

# Outcome Contract Implementation

## Starting point and scope

After C088, compiler `rewrite` at `67aad5700282a7612666b0639e2c0d00c401eccd`
and research `main` at `bf0e210c3f57d0c0017e966964b4e400e1092c75` were synchronized
before feature-branch deletion. P103 is an independent prerequisite of P087;
P085's remote facet continues to await G091. No scheduled continuation is used.

This slice implements the [outcome contract](../60-specification/outcome-contracts/values-sequencing-and-validation.md).
The original [CP-103 forks](../20-notes/language-completion-plan-delivery.md#item-103-outcome-types)
retain their recorded recommendations. Public vocabulary remains held. The
compiler package uses internal role labels and explicit C004 library evidence.

## Implementation decisions

| Decision | Four alternatives explored | Recommended and selected |
| --- | --- | --- |
| OV-I01 | A: ordinary distinct nominal ADTs; B: compiler-reserved nullable values; C: one universal dynamic failure tuple; D: implicit effect escape. | **A.** C042/C081 and the plan already distinguish expected values from terminal and effect mechanisms. |
| OV-I02 | A: invalid validation requires a head plus finite tail; B: allow an empty invalid error sequence; C: silently turn empty errors into success; D: invent a default error. | **A.** An explicit optional conversion handles empty input without inventing success data or errors. Dependent errors remain arbitrary typed values. |
| OV-I03 | A: separate independent accumulation from dependent Workflow; B: give both the same fail-fast chain; C: accumulate during dependent callbacks after failure; D: decide the strategy at runtime. | **A.** Only optional and dependent families provide coherent Workflow evidence. |
| OV-I04 | A: preserve left-to-right error order and duplicates; B: sort errors; C: deduplicate errors; D: use task completion order. | **A.** It matches eager argument evaluation and makes the validation result reproducible without adding ordering constraints to error types. |
| OV-I05 | A: explicit content-digest-bound ordinary package extending existing hierarchy evidence; B: mutate the frozen C004 hierarchy; C: auto-import outcome names; D: add a new core outcome construct. | **A.** The existing standard hierarchy digest remains unchanged. The package supplies its own declarations, APIs and instances. Its internal names do not select source vocabulary. |
| OV-I06 | A: compile ordinary polymorphic equations and specialize host library dictionaries using C004; B: widen old JSON syntax to add recursion or qualified calls; C: implement only untyped host tuples; D: present metadata as execution evidence. | **A.** Mapping/conversions have checked ordinary definitions; independent accumulation additionally has a checked combiner-parameterized equation compared with the actual linked library implementation. No old frontend admission is widened. |
| OV-I07 | A: stop coverage when an entire existing row is wildcard; B: increase the analysis budget; C: disable coverage for outcomes; D: unfold recursive fields indefinitely. | **A.** A fully covering row proves non-usefulness without unfolding recursive tails. The initial ordinary package exposed this unnecessary expansion. |
| OV-I08 | A: instantiate flexible constructor variables to rigid scrutinee parameters; B: refine rigid parameters to fresh clause-local variables; C: relax typed-core verification; D: monomorphize all library definitions manually. | **A.** The initial polymorphic mapping exposed a verifier mismatch caused by B. The inference repair preserves the verifier and existing GADT tests. |
| OV-I09 | A: linear stack-safe error concatenation with explicit cost; B: unrestricted recursive host stack growth; C: truncate long errors; D: promise constant cost without a representation supporting it. | **A.** The witness covers 50,001 errors and retains every element. Repeated growing-left concatenation is not advertised as globally linear. |
| OV-I10 | A: keep absence/result/validation adapters explicit; B: catch every exception as failure; C: convert process death to absence; D: flatten nested outcomes automatically. | **A.** C081 and the plan require named boundaries and preservation of distinct mechanisms. No foreign frame is admitted here. |

## Executable evidence

The compiler owns `lib/catena/standard/outcomes.ex`, the explicit
`priv/stdlib/catena-outcomes-0.1.54.json` package, and
`test/catena/outcome_contract_test.exs`. The package uses retained `0.1.4`
ordinary type and interface encoding with uniform layout; `0.1.54` records the
library contract rather than a new executable frontend. The existing standard
hierarchy digest is retained.

The focused suite checks deterministic source and specialized companion
artifacts; typed constructor rejection; coherent parent dictionaries;
reference/BEAM agreement for polymorphic maps and all four validation input
combinations; callback multiplicity; empty and nested outcomes; explicit error
conversions; bounded identity/composition/associativity; trap/exit propagation;
and large ordered error concatenation. Independent error observations are
reconstructed structurally rather than by calling the host concatenation
implementation.

The first full run passed 778 of 783 tests. Its five failures were stale
current-revision assertions and an incorrectly broadened expected executable
version list. The fixes retain the old executable list and update only current
metadata expectations. Final publication requires the fresh run below.

## Publication gate

Compiler commit
[`427fdcfc79384ef9d7d81a5a007daaa7bc530ca8`](https://github.com/pcharbon70/catena/commit/427fdcfc79384ef9d7d81a5a007daaa7bc530ca8)
passes **784 tests**, including twelve outcome tests. Verification used
`mix test`, `MIX_ENV=prod mix compile --warnings-as-errors`,
`MIX_ENV=prod mix escript.build`, `mix format --check-formatted` and
`git diff --check`, on Elixir 1.20.2 / OTP 29.0.4. Test-only existing warnings
and expected actor-trap log output remain; production compilation is clean.
Package corruption, wrong layout/contract and incompatible hierarchy tests
were added after the initial run and are included in the final 784.

Archive validation passes with 599 documents, 66 directories, 6,821 local
links, 119 sources, 180 specification chapters and 759 traceability obligations
(664 traced, 74 partial, 21 untraced). The eight new obligations are indexed
in the [traceability map](../10-maps/conformance-traceability.md#outcome-contract-registry-ov-0154).
No new external source claim was introduced; this slice implements the
existing plan and synthesis. C103 closes the bounded ordinary-library
contract. Foreign admission, general collection protocols and final vocabulary
remain with their existing owners. The next unused semantic patch is `0.1.55`.
