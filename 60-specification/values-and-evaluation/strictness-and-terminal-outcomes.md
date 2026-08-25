---
title: "Strictness and Terminal Outcomes"
kind: specification
created: "2026-08-24"
status: candidate
spec_version: "0.1.25"
tags:
  - values
  - evaluation
  - strictness
  - specification
aliases:
  - "Catena strictness invariant"
---

# Strictness and Terminal Outcomes

## Status and authority

This chapter is the normative Catena 0.1.25 strictness and
terminal-outcome contract. It is governed by
[Specification Authority](../../SPECIFICATION-AUTHORITY.md),
[Catena Conformance Vocabulary](../../CONFORMANCE-VOCABULARY.md), and
[Catena Implementation Limits and Portability](../../IMPLEMENTATION-LIMITS.md).
It elevates, without amending, the evaluation rules of
[Sequential Dynamics](../formal-semantic-kernel/sequential-dynamics.md)
and the trap taxonomy of
[Actors, Messages, and Failures](../formal-semantic-kernel/actors-messages-and-failures.md).

The rules apply only to source-language revision `0.1.25`. They do not
reinterpret retained manifests, interfaces, artifacts, or signed formats,
and they change no 0.1.8 kernel rule.

## The strictness invariant

The Catena language is strict (`VA-OBL-006`):

> **Normative definition.**

```text
Every subexpression evaluates at most once,
to a value or a terminal trap,
before it is used.
```

- **At most once** — no subexpression is re-evaluated by the
  evaluation itself; C005's affine resumption rule enforces the same
  discipline for continuations.
- **To a value or a terminal trap** — the two outcomes of
  [Terminal outcomes](#terminal-outcomes); a diverging evaluation
  reduces forever, which is non-termination, not an exception to
  strictness.
- **Before it is used** — no form consumes an unevaluated subexpression.

## Named exceptions

Exactly two forms skip an operand's evaluation
(`VA-OBL-006`), fixed by
[Sequential Dynamics](../formal-semantic-kernel/sequential-dynamics.md)
and unchanged here:

- `and` skips its right operand when the left value is false;
- `or` skips its right operand when the left value is true.

Both still evaluate their left operand exactly once, and the skipped
case is the one whose result is already determined.

## The edition-record gate

Any future form that would evaluate lazily, skip evaluation outside
the two named exceptions, or evaluate more than once MUST be
introduced by a lifecycle record under
[Feature Lifecycle and Compatibility](../editions-and-feature-lifecycle/feature-lifecycle-and-compatibility.md)
naming the form, its evaluation regime, and its migration
(`VA-OBL-007`). No such form exists at 0.1.25, and implementations
MUST NOT use this chapter's boundary to claim one.

## Terminal outcomes

A completed evaluation has exactly two terminal outcomes
(`VA-OBL-006`):

> **Normative definition.**

```text
outcome ::= value | trap ( reason ) ;
```

A **trap** is an explicit terminal failure under the kernel taxonomy of
[Actors, Messages, and Failures](../formal-semantic-kernel/actors-messages-and-failures.md);
there is no third terminal outcome at this revision. A suspended
algebraic request `e -> request(c, op, values, E)` is **not** a
terminal outcome: it is a pending continuation owned by the handler
calculus, and under the C010 completion rule no process entry returns
with one live.

## Determinism

For a closed expression without process operations, at most one
ordinary sequential step applies at any point, exactly as the kernel
fixes (`VA-OBL-006`); equal inputs produce equal terminal outcomes.

## Deliberately separate work

Which form evaluates first in each compound — the per-form order
details beyond the invariant — remains P030's. Bindings and sequencing
remain G031's. Tail-call guarantees remain G032's. The failure
taxonomy beyond traps remains G036's. Time, cancellation, and deadlines
remain G088's.

## Rationale and evidence (non-normative)

The [values synthesis](../../20-notes/catena-values-and-evaluation.md)
records why the invariant needs an explicit gate (a silent lazy form
would be a compatible addition by default classification, weakening
every evaluate-before-use reasoning tool) and reuses the prelude
guarantee's edition-record mechanism. The [topic
map](../../10-maps/values-and-evaluation.md) routes the decision.
