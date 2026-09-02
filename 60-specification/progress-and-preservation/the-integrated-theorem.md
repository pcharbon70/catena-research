---
title: "The Integrated Theorem"
kind: specification
created: "2026-09-01"
status: candidate
spec_version: "0.1.45"
tags:
  - metatheory
  - specification
aliases:
  - "Catena composed safety theorem"
---

# The Integrated Theorem

## Status and authority

This chapter is the normative Catena 0.1.45 integrated-theorem
statement. It is governed by
[Specification Authority](../../SPECIFICATION-AUTHORITY.md),
[Catena Conformance Vocabulary](../../CONFORMANCE-VOCABULARY.md), and
[Catena Implementation Limits and Portability](../../IMPLEMENTATION-LIMITS.md).
It composes the standing component targets —
[Metatheory](../data-and-patterns/metatheory.md) (C002),
C003's [metatheory](../clause-conditions/metatheory.md), the
kernel [metatheory](../formal-semantic-kernel/metatheory.md) (C010),
and [The Effects and Failure Targets](the-effects-and-failure-targets.md)
— without amending any of them.

The rules apply only to source-language revision `0.1.45`.

## The composed statement

> **Normative definition.**

The integrated theorem is the following composed claim
(`PP-OBL-005`): **if** each component target holds as stated —
data (C002), conditions (C003), kernel sequential and mailbox
(C010), effects and failure (0.1.45) — **and** the composition
lemma below is discharged, **then** every closed, well-typed
edition-0.1 program evaluates to a value, traps with a kinded
reason, or diverges — the three-way partition — with each step
preserving types and each observable trace agreeing across
conforming targets (`PP-OBL-005`).

## The composition lemma

> **Normative definition.**

The composition lemma — that the components' typing and step
relations combine without interference across their boundaries
(patterns into conditions, conditions into effects, effects into
failure, all over the kernel calculus) — is a **named proof
obligation**, owned by the formal-validation program (the open
type-system inquiry and Section 16's gates), and is NOT claimed
here (`PP-OBL-006`). Until discharged, the honest summary is:
every component target is stated with evidence, and no known
composition counterexample exists (`PP-OBL-005`).

## Conditional extensions

> **Normative definition.**

- **Public processes.** The kernel mailbox targets (C010) stand
  as stated. The extension to public process creation and lifetime
  holds **iff** the owning slice (G084/G085) ships with its own
  preservation statement; this chapter claims nothing about
  machinery that does not exist (`PP-OBL-007`).
- **Foreign values.** Foreign values enter only through the
  visible, typed, failure-classified boundary C067 requires
  (G095/G096); entering values are therefore already-typed, and
  preservation holds **by construction of the boundary** — the
  condition being precisely that no other entry path exists,
  which the C067 exclusions enforce (`PP-OBL-007`).

## Rationale and evidence (non-normative)

The [synthesis](../../20-notes/catena-progress-and-preservation.md)
argues the composed statement's honest middle — strictly more
than "each part works," strictly less than "the whole is proven" —
and why the conditionals cost nothing unprovable.
