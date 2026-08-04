---
title: "Clause Condition Metatheory"
kind: specification
created: "2026-08-02"
status: normative
spec_version: "0.3"
tags:
  - formal-methods
  - pattern-matching
  - program-semantics
  - specification
aliases:
  - "C003 metatheory targets"
---

# Clause Condition Metatheory

## Judgment boundary

Version 0.3 adds these judgment families:

> **Normative definition.**

```text
K ; Γ ; P ⊢condition e : Bool ⇒ c ; deps
K ⊢ predicates acyclic
F ⊢ c satisfiable ⇒ yes | no | unknown
Δ ; F ⊢ guarded-matrix useful(pattern, c) ⇒ result
Σ ⊢ guard-tree ok
Σ ; mode ⊢ guard-tree ⇒ ErlangForms
```

`K` contains checked predicate signatures and normalized bodies. `P` contains
row-local pattern bindings. `F` is the supported Boolean and integer
difference-constraint theory. `Σ` contains typed clauses, condition evidence,
coverage facts, and ordered continuation metadata. `mode` is native or
ordinary for normal matches and native only for the receive harness.

## Required claims

The version 0.3 design targets:

1. **Condition typing.** Normalization preserves the source condition's exact
   `Bool` type.
2. **Closed safety.** Evaluating accepted normalized condition core terminates,
   performs no effect, and returns one Boolean for every typed input.
3. **Predicate expansion.** Acyclic inlining preserves predicate result and
   introduces no free variable after parameter substitution.
4. **Short-circuit equivalence.** Source and core `and`/`or` evaluate the same
   operands in the same left-to-right conditional order.
5. **Selection determinism.** One scrutinee and ordered clause set select at
   most one committed body.
6. **Fallthrough correctness.** A false condition continues to exactly the
   next source clause with no row-local binding escape.
7. **Commitment.** Evaluation after a true condition cannot resume the guard
   tree because of body failure.
8. **Or-pattern sharing.** One successful source or-pattern attempt evaluates
   its shared condition once.
9. **Fact soundness.** A proved-unsatisfiable formula has no mathematical
   integer valuation; unknown never establishes exhaustiveness or redundancy.
10. **Guarded exhaustive progress.** An accepted exhaustive ordinary guard
    tree over a well-typed value reaches one committed body.
11. **Interface integrity.** Rechecked canonical evidence denotes the same
    condition body and dependency identities used by the consumer.
12. **Lowering equivalence.** Native and ordinary lowering select the same body
    and produce the same typed observation.
13. **Receive preservation.** A native rejected receive candidate remains in
    the mailbox, while a selected candidate is consumed once.
14. **Evidence erasure.** Removing analysis-only condition and fact evidence
    from `.beam` does not change runtime selection.

## Proof and evidence status (non-normative)

These are written proof targets, not machine-checked theorems. Current local
evidence consists of:

- a closed normalizer and acyclic predicate checker;
- an independently invoked typed-core verifier;
- a deterministic difference-constraint satisfiability checker;
- positive and negative coverage cases, including conservative nonlinear
  unknowns;
- a pure reference evaluator;
- forced native and ordinary BEAM lowering;
- interface round-trip and tamper tests;
- a typed native receive lowering harness; and
- 46 passing compiler tests on the pinned OTP 29 toolchain.

The prototype does not prove the claims for all programs. It also does not yet
measure compile-time growth, runtime overhead, mailbox scan behavior, or human
diagnostic comprehension.

## Falsification criteria

The specification MUST be revised if a counterexample shows:

- an accepted condition can diverge, fail, perform an effect, or return a
  non-Boolean value;
- predicate inlining changes capture, evaluation order, or result;
- the fact checker accepts a non-exhaustive match or rejects a reachable row;
- unsupported arithmetic is treated as a proof;
- an or-pattern evaluates its shared condition more than once;
- body failure falls through;
- native and ordinary lowering disagree for a typed input;
- imported evidence can be changed without detection;
- receive lowering consumes or reorders a rejected message; or
- a supported input within the required minimum budget reports an
  implementation-limit diagnostic.

## Deferred proof extensions

An integrated theorem still needs effects, handlers, traits, process typing,
public receive syntax, foreign values, failures, and optimizer validity. A
future proof-producing solver or recursive total predicate language requires a
new trusted boundary and cannot be inferred from these claims.

## Connections (non-normative)

The inherited type claims are in the
[0.1 metatheory](../type-system/metatheory.md), and the structural pattern
claims are in the [0.2 metatheory](../data-and-patterns/metatheory.md).
