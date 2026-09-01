---
title: "The Foreign Visibility Routing"
kind: specification
created: "2026-09-01"
status: candidate
spec_version: "0.1.43"
tags:
  - type-system
  - safety
  - foreign-boundary
  - specification
aliases:
  - "Catena foreign visibility routing"
---

# The Foreign Visibility Routing

## Status and authority

This chapter is the normative Catena 0.1.43 foreign visibility
requirement. It is governed by
[Specification Authority](../../SPECIFICATION-AUTHORITY.md),
[Catena Conformance Vocabulary](../../CONFORMANCE-VOCABULARY.md), and
[Catena Implementation Limits and Portability](../../IMPLEMENTATION-LIMITS.md).
It applies
[The Intralanguage Exclusions](the-intralanguage-exclusions.md) to
the only edges where dynamic or unsafe values can enter, routing
implementation to the foreign gaps' owning slices.

The rules apply only to source-language revision `0.1.43`.

## The cross-edge requirement

> **Normative definition.**

Any dynamic or unsafe value entering Catena MUST pass a **visible,
typed, failure-classified boundary owned by its arriving slice**
(`DU-OBL-004`): Erlang terms arrive through G095's boundary,
foreign calls through G096's, and NIFs and ports through G098's.
Each owning slice MUST declare its boundary's checks, the types it
admits, and the failure classification of what it refuses or that
fails — before any value crosses (`DU-OBL-004`). This area adds no
mechanism and reserves no spelling; it binds the foreign slices'
designs (`DU-OBL-005`).

## Standing precedents

> **Normative definition.**

Two rules already in force are precedents for the requirement
(`DU-OBL-005`): the failure taxonomy's mapping of a foreign raise
to `trap(reason)` (C036 — foreign failure already has a named,
visible classification), and the guard fragment's rejection of
foreign calls inside conditions (C003 — the boundary is visible
by exclusion where evidence matters most). The host's own term
format — which refuses non-finite float payloads rather than
coercing them (the probes journal) — demonstrates refusal as
visibility in kind (`DU-OBL-005`).

## No silent widening

> **Normative definition.**

An implementation MUST NOT admit a dynamic or unsafe value by any
path other than a boundary discharging this requirement, and MUST
NOT treat host permissiveness as permission: where the host
accepts what the language excludes, the boundary refuses
(`DU-OBL-004`).

## Rationale and evidence (non-normative)

The [synthesis](../../20-notes/catena-dynamic-and-unsafe-boundaries.md)
records why the requirement is stated rather than mechanized: the
foreign edges are undesigned, and C036's mapping plus the
term-format refusal show the discipline the edges must inherit.
