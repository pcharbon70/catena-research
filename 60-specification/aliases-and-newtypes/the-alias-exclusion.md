---
title: "The Alias Exclusion"
kind: specification
created: "2026-09-01"
status: normative
spec_version: "0.1.41"
tags:
  - type-system
  - aliases
  - specification
aliases:
  - "Catena alias exclusion"
---

# The Alias Exclusion

## Status and authority

This chapter is the normative Catena 0.1.41 alias rule. It is
governed by
[Specification Authority](../../SPECIFICATION-AUTHORITY.md),
[Catena Conformance Vocabulary](../../CONFORMANCE-VOCABULARY.md), and
[Catena Implementation Limits and Portability](../../IMPLEMENTATION-LIMITS.md).
It extends the complete authority vocabulary of
[Authority and Representation Exclusions](../abstraction-boundaries/authority-and-representation-exclusions.md)
and defends the nominal identity of
[Declarations and Nominal Identity](../data-and-patterns/declarations-and-nominal-identity.md).

The rules apply only to source-language revision `0.1.41`. They do
not reinterpret retained manifests, interfaces, artifacts, or
signed formats.

## The exclusion

> **Normative definition.**

Transparent type aliases — declarations under which a second name
denotes exactly the type another name denotes, erasably and
silently — do not exist in edition `0.1` (`AN-OBL-002`). No
frontend, interface, or artifact form introduces one. Every type
name is a nominal declaration with its own identity (`AN-OBL-002`).
When two names must denote one type, the source uses one type.

The exclusion extends the constructor-authority vocabulary's
completeness (C023) from export modes to naming itself: there is no
third kind of type visibility, and no erasable synonym beside
declaration and reference (`AN-OBL-002`).

## Arrival conditions

> **Normative definition.**

A slice that admits an alias form MUST first state, in its own
normative revision (`AN-OBL-008`):

1. **identity-sharing** — whether aliased names denote one nominal
   identity, and what that means for C002's declaration-anchored
   identity;
2. **the comparability interaction** — whether aliases are
   transparent to C035's comparable set and what witnesses decide;
3. **the compatibility treatment** — under C028's rules, whether
   introducing, changing, or removing an alias is a breaking
   change; and
4. **error-message naming** — which of the aliased spellings
   diagnostics carry, consistently with C002's
   declaration-naming discipline.

Until all four are stated with witnesses, this exclusion binds.

## Rationale and evidence (non-normative)

The [aliases-and-newtypes synthesis](../../20-notes/catena-aliases-and-newtypes.md)
argues the three pillars behind the exclusion: nominal identity as
the corpus spine, a complete authority vocabulary with no back
door, and the nothing-implicit guarantee. The [resolved
inquiry](../../40-inquiries/should-catena-admit-type-aliases-and-newtypes.md)
preserves the decision route.
