---
title: "Data and Pattern Diagnostics and Conformance"
kind: specification
created: "2026-08-02"
status: normative
spec_version: "0.1.2"
tags:
  - algebraic-data-types
  - diagnostics
  - pattern-matching
  - specification
aliases:
  - "C002 conformance contract"
---

# Data and Pattern Diagnostics and Conformance

## Stable diagnostics

The 0.1.2 diagnostic families are:

| ID | Meaning |
| --- | --- |
| `A001` | Malformed or ill-kinded datatype declaration, import, or derivation |
| `A002` | Duplicate type, constructor, field, or imported constructor alias |
| `A003` | Invalid constructor payload, result, arity, field style, or fold eligibility |
| `A004` | Unknown, hidden, or inaccessible constructor |
| `A005` | Nominal interface identity or integrity mismatch |
| `M001` | Non-exhaustive match, with a missing witness |
| `M002` | Redundant match clause |
| `M003` | Invalid pattern type, arity, field, binding, or `or` agreement |
| `M004` | Deterministic coverage implementation limit exhausted |
| `M005` | Unsupported 0.1.2 pattern form |
| `L001` | Invalid layout selection or verified typed-layout invariant |

C001 `T009` remains the rigid existential or equality escape diagnostic.
C001 `T010` remains the missing annotation or unsupported advanced-boundary
diagnostic. Malformed JSON structure continues to use `T012` before semantic
datatype checking.

Diagnostics MUST include the JSON path or eventual source span when one is
available. `M001` MUST include a machine-readable witness. `M004` MUST state
the supported minimum budget and MUST NOT masquerade as `M001` or `M002`.

## Required positive cases

A conforming implementation MUST accept and check:

- unit, empty, phantom, nested, mutually recursive, positive, and negative
  ordinary datatype declarations;
- positional and named construction, including named fields written out of
  declaration order;
- every pattern form enumerated by 0.1.2, including nested `as` and `or` forms;
- exhaustive Boolean, tuple, constructor, and proven-empty matches;
- unknown guarded clauses followed by an unguarded exhaustive fallback;
- transparent imported constructors and abstract values used opaquely;
- annotated GADT matches with impossible alternatives removed;
- nonescaping existential unpacking;
- explicit eligible folds; and
- the same observable results under uniform and compact layouts.

## Required negative cases

The suite MUST reject:

- duplicate declarations, constructors, fields, binders, and aliases;
- unknown kinds, unsaturated named types, invalid constructor results, and
  existential result escape;
- construction or patterns with the wrong arity or field style;
- hidden imported constructors;
- mismatched `or` bindings or refinements;
- non-exhaustive and redundant clauses;
- a `false` guarded clause as redundant;
- an empty match over an unknown or inhabited type;
- a GADT match without its enclosing signature;
- a GADT or existential fold derivation;
- a corrupted interface digest; and
- corrupted typed-core constructor or decision evidence.

## Differential and deterministic evidence

The reference evaluator represents ADTs by semantic nominal constructor IDs,
independent of BEAM layout. A conformance fixture MUST run through:

1. the reference evaluator;
2. uniform-layout BEAM; and
3. compact-layout BEAM.

Comparison is by typed source observation, not raw Erlang term equality.
Generated BEAM and `.cati.json` output MUST be byte-for-byte deterministic for
identical compiler inputs and options.

The suite MUST include a deterministic bounded pattern corpus independent of
the inference and coverage implementation. Bounded enumeration is evidence,
not proof.

## Promotion evidence (non-normative)

The executable evidence is published in the sibling compiler repository on
`rewrite` as commit `ae311604ef587a022ce2b7b46599200fcb96a7ab`. That historical
commit used the retired `0.1` and `0.2` protocol identifiers. It is the
immutable semantic evidence originally used to promote C002, but it is not an
implementation identity for the exact `0.1.1` and `0.1.2` strings.

Commands and observed results are recorded in
[C002 Executable Data and Pattern Conformance](../../50-journal/2026-08-02-c002-executable-data-and-pattern-conformance.md).
The [prototype-slice renumbering record](../../50-journal/2026-08-04-prototype-slice-renumbering.md)
requires a fresh cross-slice identity before the renumbered executable claim
is published.
