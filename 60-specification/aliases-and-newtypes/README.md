---
title: "Aliases and Newtypes Specification"
kind: map
created: "2026-09-01"
tags:
  - archive-navigation
  - directory-index
  - type-system
  - specification
aliases:
  - "Catena 0.1.41 aliases and newtypes specification"
---

# Aliases and Newtypes Specification (`60-specification/aliases-and-newtypes`)

## Purpose

This directory contains the Catena 0.1.41 contract for aliases,
opaque types, and newtypes: the alias exclusion with its arrival
conditions, the newtype form with its identity, representation,
access, coercion, deriving, and error-message rules, the routing of
opaque types to the abstraction contract, and the conformance
obligations.

The repository-level [Specification Authority](../../SPECIFICATION-AUTHORITY.md)
controls status, applicability, rendered labels, and conflicts. The
[Catena Conformance Vocabulary](../../CONFORMANCE-VOCABULARY.md) controls
requirement force, invalidity, and variability. The
[Catena Implementation Limits and Portability](../../IMPLEMENTATION-LIMITS.md)
policy governs resource disclosure; this area adds no new dimension.

## What belongs here

Put the alias exclusion, the newtype rules, and C062 conformance
obligations here. Export transparency modes and their validation
remain C022's. The constructor-authority vocabulary and the
smart-constructor idiom remain C023's. Nominal identity remains
C002's. Comparability remains C035's. Derivation remains C073's.
Representation invisibility remains C023/C037's. Explicit
conversions remain G105's library territory. Surface spellings
remain P109's.

## Variability register

This area introduces no implementation-defined choice,
recommendation, bounded unspecified presentation, or implementation
limit. The exclusion and the rules bind every conforming
implementation identically; no registry or tooling behavior may
vary.

## Index

### Subdirectories

- None yet.

### Documents

- [The Alias Exclusion](the-alias-exclusion.md)
  — transparent synonyms excluded, with recorded arrival
  conditions.
- [The Newtype Form](the-newtype-form.md)
  — the newtype as the nominal single-field ADT: identity,
  representation, access, coercion, deriving, diagnostics, and the
  opaque routing.
- [Aliases and Newtypes Diagnostics and Conformance](diagnostics-and-conformance.md)
  — zero new families, abstract boundaries, and the `AN-OBL-*`
  obligations with evidence sets.

## Maintaining this index

Update this README when a chapter is added, renamed, or archived.
Every direct child belongs in the index. If an alias form ever
arrives, link the slice that discharged the arrival conditions
here.
