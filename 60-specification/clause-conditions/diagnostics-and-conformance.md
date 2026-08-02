---
title: "Clause Condition Diagnostics and Conformance"
kind: specification
created: "2026-08-02"
status: normative
spec_version: "0.3"
tags:
  - diagnostics
  - pattern-matching
  - specification
aliases:
  - "C003 conformance contract"
---

# Clause Condition Diagnostics and Conformance

## Stable diagnostics

The version 0.3 diagnostic family is:

| ID | Meaning |
| --- | --- |
| `CND001` | Malformed condition declaration, AST-version use, operator, signature shape, or lowering selection |
| `CND002` | A condition or declared predicate does not return `Bool`, has a nonempty effect, or violates the first-order `Bool`/`Int` signature boundary |
| `CND003` | Disallowed ordinary, partial, higher-order, local-match, construction, foreign, effectful, or trait-dispatched expression |
| `CND004` | Recursive or mutually recursive condition dependency |
| `CND005` | Missing, malformed, nonportable, or digest-inconsistent imported condition evidence |
| `CND006` | Selective-receive message type, pattern, or native-lowerability restriction |
| `CND007` | Deterministic condition normalization, expansion, or safety budget exhausted |

The 0.2 `M001`, `M002`, and `M004` diagnostics remain the non-exhaustive,
redundant, and structural-budget reports. A fact checker MUST NOT use `M001` or
`M002` merely because a proposition is unsupported or times out.

Diagnostics include the JSON path or eventual source span when available.
`CND007` includes the supported minimum budget. Task-facing text SHOULD say
“clause condition” before explaining the compiler term “guard.”

## Required positive cases

A conforming implementation MUST check and execute:

- Boolean literals and variables;
- lazy negation, conjunction, and disjunction;
- exact Boolean and integer equality and inequality;
- all four integer order operations, unary negation, addition, subtraction,
  and multiplication;
- direct fully applied local and explicitly imported condition predicates;
- forward acyclic predicate dependencies;
- ordinary matches and signed multi-clause functions;
- negative, zero, and positive integer partitions proved exhaustive by the
  difference-constraint checker;
- a condition false falling through to exactly the next clause;
- overlapping or-pattern lowering with one shared condition continuation;
- version 0.2 interfaces consumed without condition evidence;
- version 0.3 interface round trips with canonical evidence; and
- typed receive-harness clauses over an explicit closed message type.

## Required negative cases

The suite MUST reject:

- a condition declaration without a signature or with malformed signature
  syntax;
- a non-Boolean clause condition or predicate result;
- a nonempty condition effect;
- an ordinary call, lambda, partial application, local binding, local match,
  construction, foreign call, effect, handler, or trait-dispatched operation;
- division, remainder, and another unchecked partial primitive;
- a recursive predicate dependency;
- a missing, implicit, duplicate, or tampered condition import;
- use of 0.3 condition syntax in an earlier AST version;
- a proved-false or fact-shadowed redundant clause;
- a nonlinear arithmetic partition claimed exhaustive without a fallback;
- a condition or fact budget below the required minimum; and
- a receive harness using a free message type, nonnative condition, or expanded
  or-pattern.

## Differential evidence

For representative ordinary matches and functions, the suite compares:

1. the pure reference evaluator;
2. forced native BEAM lowering; and
3. forced ordinary BEAM lowering.

All paths MUST select the same clause and return the same typed result for the
same input. Generated BEAM and interface output MUST be deterministic for
identical inputs and options. Native and ordinary bytes need not be identical.

The suite also independently corrupts condition evidence and asks the
typed-core or interface verifier to reject it. A compiler that only trusts the
inference path is not conforming.

## Promotion evidence

Published Catena compiler commit
[`165fc4837f101d01016248e62479ef4caa0f20ce`](https://github.com/pcharbon70/catena/commit/165fc4837f101d01016248e62479ef4caa0f20ce),
merged by [compiler PR #65](https://github.com/pcharbon70/catena/pull/65),
passes 46 tests on Elixir 1.20.2 and Erlang/OTP 29.0.4, including the required
0.3 core cases. The exact commands and observations are in
[C003 Executable Clause Condition Conformance](../../50-journal/2026-08-02-c003-executable-clause-condition-conformance.md).

The conformance suite was rerun with that commit checked out before normative
promotion. This chapter, its eight sibling chapters, and checklist item C003
therefore share one immutable implementation identity.

## Connections

The diagnostic vocabulary follows the usability direction in
[Clause Guards](../../20-notes/clause-guards.md). The formal claims and limits
are in [Clause Condition Metatheory](metatheory.md).
