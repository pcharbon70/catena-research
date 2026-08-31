---
title: "Numeric Relationships Specification"
kind: map
created: "2026-08-31"
tags:
  - archive-navigation
  - directory-index
  - numerics
  - specification
aliases:
  - "Catena 0.1.40 numeric relationships specification"
---

# Numeric Relationships Specification (`60-specification/numeric-relationships`)

## Purpose

This directory contains the Catena 0.1.40 contract for how `Int`
and `Float` relate across operators: the closed-set instantiation
rule, the dispatch exclusion, float arithmetic, and the G105
routings, with the conformance obligations.

The repository-level [Specification Authority](../../SPECIFICATION-AUTHORITY.md)
controls status, applicability, rendered labels, and conflicts. The
[Catena Conformance Vocabulary](../../CONFORMANCE-VOCABULARY.md) controls
requirement force, invalidity, and variability. The
[Catena Implementation Limits and Portability](../../IMPLEMENTATION-LIMITS.md)
policy governs resource disclosure; this area adds no new dimension.

## What belongs here

Put the instantiation rule, the overloadability exclusion, and
C061 conformance obligations here. Literal spelling and conversion
remain C018's. Operator tokens, precedence, and fixity remain
C019's. The comparable set remains C035's. The numeric runtime
types remain C040's. Division, remainder, checked and decimal
arithmetic, explicit conversions, and the numeric library remain
G105's.

## Variability register

This area introduces no implementation-defined choice,
recommendation, bounded unspecified presentation, or implementation
limit. The closed set, the same-type rule, and the exclusions bind
every conforming implementation identically; no registry or tooling
behavior may vary.

## Index

### Subdirectories

- None yet.

### Documents

- [The Closed-Set Instantiation Rule](the-closed-set-instantiation-rule.md)
  — the typing mechanism and float arithmetic.
- [Exclusions and Routings](exclusions-and-routings.md)
  — no dispatch, no defaulting, no coercion, no literal
  constraints; division and remainder to G105.
- [Numeric Relationships Diagnostics and Conformance](diagnostics-and-conformance.md)
  — zero new families, abstract boundaries, and the `NR-OBL-*`
  obligations with evidence sets.

## Maintaining this index

Update this README when a chapter is added, renamed, or archived.
Every direct child belongs in the index. When a future numeric
type amends the closed set, link that revision here.
