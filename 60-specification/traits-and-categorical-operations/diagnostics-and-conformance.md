---
title: "Trait Diagnostics and Conformance"
kind: specification
created: "2026-08-02"
status: normative
spec_version: "0.1.4"
tags:
  - category-theory
  - compilers
  - specification
  - trait-constraints
aliases:
  - "Catena 0.1.4 trait conformance"
---

# Trait Diagnostics and Conformance

## Stable diagnostics

Version 0.1.4 reserves these families:

| ID | Meaning |
| --- | --- |
| `TRT001` | malformed, duplicate, missing, or unknown declaration/method |
| `TRT002` | kind, arity, parent-cycle, or functional-dependency shape error |
| `TRT003` | ownership, overlap, context-decrease, or dependency consistency error |
| `TRT004` | missing, recursive, ambiguous, or incoherent evidence |
| `TRT005` | invalid law schema or evidence tier |
| `TRT006` | malformed template or incomplete/ambiguous helper closure |
| `TRT007` | specialization budget or polymorphic-recursion failure |
| `TRT008` | resolution budget or standard/interface digest mismatch |
| `DRV001` | unsupported or ill-shaped structural derivation |
| `LNK001` | malformed package manifest or package link input/output failure |

Older AST profiles retain their published diagnostic identifiers. A 0.1.4
implementation MUST NOT relabel an older valid or invalid program merely
because its internal registry is shared.

## Positive corpus

Conformance requires:

- all seventeen traits alone and every direct parent edge;
- the `Workflow` and `CollectingMapper` diamonds with shared ancestor evidence;
- value-, unary-constructor-, and binary-constructor-kinded heads;
- parameterized instances, functional dependencies, and associated types;
- two useful examples for each unitless capability:
  `Combiner` (nonempty aggregation and validation errors), `MultiMapper`
  (zipped optional values and accumulating validation), `Chainable` (optional
  and result workflows), `Composable` (function and parser pipelines), and
  `ContextualMapper` (nonempty zippers and annotated trees);
- the six explicit structural derivations, including two independent
  `TwoSlotMapper` targets;
- promised, tested, and derived law evidence;
- explicit `Equatable` law checks and bounded extensional function samples;
- callback count and order observations;
- resolution and execution of standard `List` `Mapper` and `Reducible` on at
  least 250,000 elements without stack exhaustion;
- deterministic interface round trips and package specialization; and
- reference-evaluator/BEAM agreement for generated operations.

## Negative corpus

Conformance also requires wrong kinds, undeclared variables, parent cycles,
foreign ownership, overlapping and dependency-inconsistent instances,
nondecreasing contexts, missing and extra methods, unresolved and ambiguous
goals, reserved law tiers, invalid derivation positions, tampered interfaces,
missing template helpers, recursive specialization, and exhausted budgets.

## Erasure and compatibility checks

Generated forms and BEAM behavior MUST demonstrate direct calls and absence of
dictionary parameters or reflective instance identity. AST 0.1.1 through 0.1.3
and interfaces 0.1.2 through 0.1.3 remain green. The full suite runs with compiler
warnings treated as errors and includes deterministic repeat builds.

## Conformance identity (non-normative)

The C004 semantic boundary was historically bound to sibling-compiler commit
[`b69f6f7e3da6015bf9b3385152ca3f3687422472`](https://github.com/pcharbon70/catena/commit/b69f6f7e3da6015bf9b3385152ca3f3687422472),
published through [compiler PR #66](https://github.com/pcharbon70/catena/pull/66)
and incorporated by merge commit
[`1b6b902b146a5539fc1a24f4303f9182fbe431fc`](https://github.com/pcharbon70/catena/commit/1b6b902b146a5539fc1a24f4303f9182fbe431fc).
The following sequence passed from the immutable implementation commit:

> **Non-normative evidence.**

```bash
mix format --check-formatted
mix clean
mix compile --warnings-as-errors
mix test
mix escript.build
git diff --check
```

The [C004 conformance journal](../../50-journal/2026-08-02-c004-executable-trait-conformance.md)
records the observed output, deterministic repeat specialization, direct-call
artifact inspection, standard collection stress case, and compatibility
results. P107 remains partial until the public vocabulary has independent
usability evidence.

That immutable commit used the retired `0.1` through `0.4` protocol
identifiers. It does not establish the exact `0.1.1` through `0.1.4` strings.
The [prototype-slice renumbering record](../../50-journal/2026-08-04-prototype-slice-renumbering.md)
requires fresh cross-slice evidence before the renumbered executable identity
is published.

## Connections (non-normative)

The promotion rule follows the archive's
[language specification lifecycle](../README.md) and keeps prototype behavior
subordinate to an explicit immutable contract.
