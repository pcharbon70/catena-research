---
title: "Binding Structure and Scope"
kind: specification
created: "2026-08-25"
status: candidate
spec_version: "0.1.27"
tags:
  - bindings
  - specification
aliases:
  - "Catena binding structure"
---

# Binding Structure and Scope

## Status and authority

This chapter is the normative Catena 0.1.27 binding-structure and
scope contract. It is governed by
[Specification Authority](../../SPECIFICATION-AUTHORITY.md),
[Catena Conformance Vocabulary](../../CONFORMANCE-VOCABULARY.md), and
[Catena Implementation Limits and Portability](../../IMPLEMENTATION-LIMITS.md).
It elevates, without amending, the binding rules of
[Sequential Dynamics](../formal-semantic-kernel/sequential-dynamics.md),
the precedence of
[Shadowing and Ambiguity](../namespaces-and-shadowing/shadowing-and-ambiguity.md),
and the mutual-recursion admission of
[SCC Admission and Resolution](../module-dependency-cycles/scc-admission-and-resolution.md),
under the schedules of
[Ordered Forms and Entry Rule](../evaluation-order/ordered-forms-and-entry-rule.md).

The rules apply only to source-language revision `0.1.27`. They do not
reinterpret retained manifests, interfaces, artifacts, or signed formats,
and they change no 0.1.8 kernel rule.

## Local binding structure

> **Normative definition.**

```text
let name = rhs ; body
```

- `name` is one value name under the identifier spelling of
  [Identifier Syntax and Equivalence](../identifiers/identifier-syntax-and-equivalence.md).
- `rhs` evaluates in the environment **without** `name` — local
  bindings are strictly non-recursive (`BS-OBL-002`). A right-hand
  side that references its own binder is `T001` unbound, exactly as
  the existing environment rules fix.
- Substitution of `name` in `body` happens only after `rhs` is a
  value — the kernel's substitute-after-value rule, elevated.
- The binder is a plain value name; pattern binding is not a `let`
  form at this revision (its match-based spelling remains
  C002/P109 surface work).

## Scope and shadowing

Scope is **sequential-lexical** (`BS-OBL-003`): a binding extends the
environment for its body alone, and an inner binding extends it
further for its own body. A local binding MAY silently shadow anything
in scope — an outer binding of the same name, a module definition, an
imported name, a prelude-origin name — per
[Shadowing and Ambiguity](../namespaces-and-shadowing/shadowing-and-ambiguity.md):
the innermost binding of a name always wins, without diagnostic. This
restates C021's rule at the binding level; no new collision
diagnostics exist here, and `NSP004` remains an import-versus-import
phenomenon.

## The recursion boundary

**Recursion is definitions-only** (`BS-OBL-004`):

- A named definition may call itself through the kernel's signed
  definition environment; general recursion may reduce forever
  (termination remains P034's).
- **Mutual recursion among named definitions is** the
  strongly-connected-component admission of
  [SCC Admission and Resolution](../module-dependency-cycles/scc-admission-and-resolution.md)
  — C024's statement, elevated as the language answer.
- No local recursive or mutually-recursive binding form exists at
  0.1.27. Local recursive *functions* — a named local binding whose
  value closes over itself — are G032's named-local-function question,
  and any such form lands in its own slice.

## Deliberately separate work

Functions, arity, currying as typing, partial application, closure
capture, tail-call guarantees, and named local functions remain
G032's. Branch forms remain G033's. Termination and recursive-total
fragments remain P034's. Pattern-binding surface forms remain
C002/P109's. Cancellation mid-sequence remains G088's.

## Rationale and evidence (non-normative)

The [bindings synthesis](../../20-notes/catena-bindings-and-sequencing.md)
records why non-recursion is an elevation of the kernel's rule rather
than a choice, why mutual recursion resolves to C024's SCC, and why
the plain-name binder keeps the retained AST's shape. The [resolved
inquiry](../../40-inquiries/how-should-catena-define-bindings-and-sequencing.md)
and [topic map](../../10-maps/bindings-and-sequencing.md) preserve the
decision route.
