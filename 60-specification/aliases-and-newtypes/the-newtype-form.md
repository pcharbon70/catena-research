---
title: "The Newtype Form"
kind: specification
created: "2026-09-01"
status: normative
spec_version: "0.1.41"
tags:
  - type-system
  - newtypes
  - specification
aliases:
  - "Catena newtype form"
---

# The Newtype Form

## Status and authority

This chapter is the normative Catena 0.1.41 newtype and
opaque-type rule set. It is governed by
[Specification Authority](../../SPECIFICATION-AUTHORITY.md),
[Catena Conformance Vocabulary](../../CONFORMANCE-VOCABULARY.md), and
[Catena Implementation Limits and Portability](../../IMPLEMENTATION-LIMITS.md).
It changes no rule of
[Declarations and Nominal Identity](../data-and-patterns/declarations-and-nominal-identity.md),
[Export Declarations and Visibility](../imports-and-exports/export-declarations-and-visibility.md),
or
[Authority and Representation Exclusions](../abstraction-boundaries/authority-and-representation-exclusions.md).

The rules apply only to source-language revision `0.1.41`.

## The newtype is a declared form

> **Normative definition.**

A newtype is a nominal datatype with exactly one constructor of
exactly one field (`AN-OBL-003`). The declaration is the ordinary
C002 data declaration; no dedicated surface exists or is required.
The wrapper's identity is its own: distinct from the wrapped type,
distinct from every other wrapper, anchored in its declaration
(`AN-OBL-003`).

## Representation and cost

> **Normative definition.**

A newtype's representation is invisible and both layouts conform
(C023, unchanged) (`AN-OBL-004`). No cost, layout, or erasure
promise attaches to a newtype: "zero-cost" is unstateable under
representation invisibility, exactly as complexity is excluded for
collections (C042), and any future cost contract follows C028's
declared-absence route (`AN-OBL-004`).

## Constructor access and the opaque routing

> **Normative definition.**

Constructor access follows the complete binary vocabulary (C023,
unchanged): a `transparent` export exposes the constructor for
construction and matching; an `abstract` export hides both
(`AN-OBL-005`). **An opaque type is a nominal datatype exported
`abstract`** — routed to C022's export modes and C023's authority
rules, which this chapter restates as routing rows and does not
amend (`AN-OBL-005`). The smart-constructor idiom over an abstract
type remains the sanctioned invariant-bearing interface. No
per-constructor, construction-only, matching-only, or selective
exposure exists (C023 exclusion, unchanged).

## Coercion

> **Normative definition.**

No coercion between a newtype and its wrapped type is implicit in
either direction (`AN-OBL-006`): the constructor wraps, a pattern
unwraps, and explicit named conversions are library territory
(G105). An implementation MUST NOT insert, elide, or optimize a
wrapping without source justification (`AN-OBL-006`).

## Deriving

> **Normative definition.**

Trait instances attach to a newtype only through explicit-target
derivation (C073, unchanged) (`AN-OBL-007`). Instances never flow
implicitly through the wrapper: the newtype is a fresh nominal type
in every respect, carries no instance of the wrapped type, and
derives only what its declaration names (`AN-OBL-007`).

## Error messages

> **Normative definition.**

Diagnostics that mention a newtype carry its declared nominal
spelling (C002's source-vocabulary discipline, unchanged)
(`AN-OBL-005`). A failing program against an abstract newtype names
the type, never the hidden constructor surface.

## Rationale and evidence (non-normative)

The [synthesis](../../20-notes/catena-aliases-and-newtypes.md)
records what the wrapper gets and never gets, and why the
cost-promise refusal follows C042's precedent. The C023 test
corpus's `Email`-style declarations are the form's standing
witnesses.
