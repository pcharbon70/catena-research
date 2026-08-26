---
title: "Unused Bindings and Sequencing"
kind: specification
created: "2026-08-25"
status: candidate
spec_version: "0.1.27"
tags:
  - bindings
  - sequencing
  - specification
aliases:
  - "Catena unused bindings and sequencing"
---

# Unused Bindings and Sequencing

## Status and authority

This chapter is the normative Catena 0.1.27 unused-binding and
sequencing contract. It is governed by
[Specification Authority](../../SPECIFICATION-AUTHORITY.md),
[Catena Conformance Vocabulary](../../CONFORMANCE-VOCABULARY.md), and
[Catena Implementation Limits and Portability](../../IMPLEMENTATION-LIMITS.md).
It elevates, without amending, the unused-binding rule of
[Sequential Dynamics](../formal-semantic-kernel/sequential-dynamics.md),
applies the schedule of
[Ordered Forms and Entry Rule](../evaluation-order/ordered-forms-and-entry-rule.md),
and copies the deny-able-warning pattern of
[Import Declarations and Admission](../imports-and-exports/import-declarations-and-admission.md).

The rules apply only to source-language revision `0.1.27`. They do not
reinterpret retained manifests, interfaces, artifacts, or signed formats.

## Unused bindings are valid

A binding whose name never occurs in its body **remains valid** and
**preserves evaluation of its right-hand side** (`BS-OBL-005`) — the
kernel's rule, elevated verbatim: the RHS evaluates to a value under
the C030 schedule, its effects are observable, and only the value is
discarded. An implementation MUST NOT eliminate the RHS evaluation.

## The BS001 warning

Because an unused binder usually signals an omission, a conforming
frontend SHOULD emit a `BS001` warning for each binding whose name
never occurs in its body and whose name is not `_`-prefixed
(`BS-OBL-006`):

> **Normative definition.**

| ID | Severity | Meaning |
| --- | --- | --- |
| `BS001` | warning (deny-able) | a non-`_`-prefixed binder never occurs in its binding's body |

- **Deny-ability** follows the IMP001 pattern: the manifest's
  `diagnostics.deny` list may name `BS001`, promoting the warning to
  an error carrying `promoted_from_warning`.
- **The `_`-prefix exemption** marks deliberate discard: a binder
  whose name begins with `_` never warns. The exemption exists because
  the normative sequencing idiom (below) uses exactly such a binder.
- The warning is advisory to validity: a program with unused bindings
  checks, compiles, and runs identically with or without it.

## The sequencing idiom

Sequencing of effectful expressions **is** the let-with-unused-binder
idiom (`BS-OBL-007`):

> **Normative definition.**

```text
let _ = e1 ; e2
```

evaluates `e1` to a value — its effects observable, per the C030
first-to-value schedule — discards the value, then evaluates `e2`,
whose value is the sequence's value. This is the only sequencing form
the retained JSON AST expresses; the kernel's bare sequence form
remains kernel-calculus; any dedicated surface punctuation is P109's,
with this chapter as its semantics.

## Deliberately separate work

Whether G032's local-function forms introduce their own discard
conventions remains G032's. Cancellation between `e1` and `e2` remains
G088's. Lint refinements to the exemption rule remain future patch
work.

## Rationale and evidence (non-normative)

The [bindings synthesis](../../20-notes/catena-bindings-and-sequencing.md)
records why the warning needs an exemption (a form that flags the
normative sequencing idiom would be self-defeating) and why the idiom
elevates rather than inventing a form. The [topic
map](../../10-maps/bindings-and-sequencing.md) routes the decision.
