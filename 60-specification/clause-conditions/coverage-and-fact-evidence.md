---
title: "Coverage and Fact Evidence"
kind: specification
created: "2026-08-02"
status: normative
spec_version: "0.3"
tags:
  - compilers
  - pattern-matching
  - program-semantics
  - specification
aliases:
  - "Catena guarded coverage facts"
---

# Coverage and Fact Evidence

## Structural baseline

The 0.2 typed-pattern usefulness relation remains authoritative for structural
coverage. Conditions add a precision layer; they do not replace constructor,
literal, tuple, abstraction, inhabitation, or GADT reasoning.

A compiler MUST accept a guarded set as exhaustive only when:

- structural analysis and proved-true conditions close the domain; or
- the 0.3 fact checker proves that the disjunction of applicable conditions is
  true for every value remaining in that structural region.

Unsupported propositions, an exhausted budget, or incomplete binding
translation are `unknown`. Unknown MUST NOT close an exhaustiveness gap or make
a clause redundant.

## Condition classification

For coverage, a condition is:

- **proved true** when its negation is unsatisfiable in the supported theory;
- **proved false** when it is unsatisfiable;
- **unknown** otherwise.

A proved-false clause is redundant. A later clause is redundant when the fact
checker proves that its condition has no satisfying input outside the union of
earlier applicable conditions. Structural shadowing remains independently
redundant under 0.2 rules.

## Supported fact theory

The 0.3 checker supports Boolean formulas built from `not`, `and`, and `or`
whose integer atoms normalize exactly to difference constraints:

```text
x - y <= c
```

`x` and `y` may include a distinguished constant-zero variable, and `c` is an
integer. The translation includes:

- strict and non-strict integer comparisons;
- integer equality as two non-strict inequalities;
- integer inequality as a disjunction of two strict inequalities;
- addition, subtraction, and unary negation when normalization yields a
  difference constraint; and
- multiplication only by constants `-1`, `0`, or `1` when it remains in the
  same theory.

General multiplication such as `x * y`, nonlinear arithmetic, trait calls,
and opaque ordinary values are unknown for coverage even though total integer
multiplication is valid at runtime inside a condition.

Strict integer comparison is normalized exactly, for example:

```text
x < y  ≡  x - y <= -1
```

The checker operates over mathematical integers, so this rewrite has no
overflow case.

## Deterministic decision procedure

The implementation converts supported Boolean formulas to a bounded
disjunction of conjunctions. Each conjunction records propositional literals
and difference-constraint edges. Contradictory Boolean assignments or a
negative-weight cycle prove the conjunction unsatisfiable. Exhaustiveness is
checked by proving the negation of the accumulated condition union
unsatisfiable.

An implementation may use another algorithm only if it is deterministic,
sound for the same theory, conservative for unsupported terms, and produces
evidence the typed-core verifier can recheck without trusting an external
solver. Version 0.3 does not invoke an external SMT solver.

## Evidence and rechecking

Each checked clause carries its normalized formula, classification, and theory
identifier. The ordered decision representation carries the checked clauses.
The independent verifier recomputes condition-evidence integrity, clause
typing, structural usefulness, and fact classification before BEAM lowering.

These records are compiler evidence and may be erased from executable code
after verification. They are not runtime values and do not authorize an
optimizer to assume facts outside the selected clause.

## Budgets and diagnostics

The structural `M004` minimum of 20,000 usefulness steps remains. Condition
normalization and expansion separately guarantee at least 20,000 nodes and use
`CND007` when that safety budget is unavailable or exceeded. A fact-analysis
implementation limit MUST be reported as an implementation limit or treated as
unknown; it MUST NOT be mislabeled as a semantic proof.

## Connections

The structural baseline is defined by the
[0.2 coverage chapter](../data-and-patterns/match-semantics-and-coverage.md).
The evidence requirements become executable cases in
[Clause Condition Diagnostics and Conformance](diagnostics-and-conformance.md).
