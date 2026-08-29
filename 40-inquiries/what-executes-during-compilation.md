---
title: "What Executes During Compilation?"
kind: inquiry
created: "2026-08-26"
status: resolved
tags:
  - catena
  - compile-time-evaluation
  - derivations
  - totality
  - language-design
aliases:
  - "G038 compile-time evaluation inquiry"
---

# What Executes During Compilation?

## Purpose

G038 asks the checklist question: "Decide whether constants,
attributes, generated derivations, or macros execute code during
compilation and under which totality and determinism restrictions."
C034's gate already binds the answer — any compile-time evaluation
must ship total-or-bounded in its admitting slice. This inquiry
makes the decision: what executes today, what never will without a
gated slice, and what the complete restriction set is.

## Operational definitions

- **Compile-time execution** — evaluating user-authored expressions
  during compilation, beyond checking and generation.
- **Meta-level evaluator** — a bounded machine that runs during
  compilation (condition normalization, specification-example
  checking, law checking).
- **Compiler-internal generation** — template-driven emission of
  definitions, executing no user code.
- **The gate** — C034's rule: total-or-bounded in the admitting
  slice, no unbounded arrival, ever.

## Hypotheses

1. A new area `compile-time-evaluation` at `0.1.34` (code `CE`)
   carries the contract, inheriting C034's gate as its own normative
   rule. *(Recommended: one-version-per-area; the gate's consumer
   becomes its owner.)*
2. **Absence + gate** for the three nonexistent forms: no constants
   execute code (definitions compile, never run), no attribute
   system exists, no macro system exists — each arriving, if ever,
   through its own gated slice. *(Recommended: the checklist's
   "decide whether" is answered with a decision, not a design.)*
3. **Generated derivations classify as compiler-internal
   generation**: folds and capabilities are template-driven, execute
   no user code, carry `compiler_derived` provenance, are
   deterministic and total by construction, and their output is
   ordinary checked definitions. *(Recommended: the one existing
   sub-item, classified as non-execution.)*
4. The restrictions are **one cited table**: C034's gate plus the
   three shipped budgets (conditions' acyclic normalization, the
   20,000-step specification checker, bounded law samples) as the
   complete set at 0.1.34.
5. The deliverable is witnesses with zero new diagnostic families:
   the derivation provenance regression with byte-identical
   recompilation, the three budget regressions, the absence matrix,
   and determinism.

## Paths explored

- **Design a const-eval fragment now** — rejected: nothing demands
  it; no constant form exists to consume it (P109's spelling era).
- **Design a macro system now** — rejected: macros are syntax;
  squarely P109-era surface work.
- **Treat derivations as gated execution** — rejected: mislabels
  template generation as execution — the derivation engine never
  evaluates user expressions.
- **Defer derivation classification to G040** — rejected: leaves an
  existing mechanism unclassified after the slice named to classify
  it.
- **Gate citation without the budget table** — rejected: loses the
  one-place answer G038 explicitly asks for.
- **Evaluator skeleton / normative-only** — rejected patterns.

## Findings

All five hypotheses held; the developer chose the recommended option
on every fork (five of five, no overrides). Planning-time
verification confirmed the witness vocabulary: derived folds are
declared via a datatype's `derivations: ["fold"]` and appear in the
typed core as definitions with `generated?: true` and
`provenance: :compiler_derived` (the C002 shape), and capability
plans (`CollectingMapper`, `Equatable`, `Orderable`) arrive through
the C004 declaration vocabulary — all existing test territory,
reasserted rather than invented.

## Outcome

Resolved as C038 at revision `0.1.34`: the contract lives in the
[Compile-Time Evaluation Specification](../60-specification/compile-time-evaluation/README.md),
the reasoning in
[Catena Compile-Time Evaluation](../20-notes/catena-compile-time-evaluation.md),
and the forks in the [design decision
register](../20-notes/design-decision-register.md). P109 spellings
for any future const/macro/attribute surface and G040's deriving
extensions remain open with their owners.
