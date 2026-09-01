---
title: "Name Resolution Specification"
kind: map
created: "2026-09-01"
tags:
  - archive-navigation
  - directory-index
  - name-resolution
  - specification
aliases:
  - "Catena 0.1.42 name resolution specification"
---

# Name Resolution Specification (`60-specification/name-resolution`)

## Purpose

This directory contains the Catena 0.1.42 contract for name
resolution: the type-independence invariant, the five-way
classification table, the evidence-selection carve-out, the
exclusions with their arrival conditions, and the conformance
obligations.

The repository-level [Specification Authority](../../SPECIFICATION-AUTHORITY.md)
controls status, applicability, rendered labels, and conflicts. The
[Catena Conformance Vocabulary](../../CONFORMANCE-VOCABULARY.md) controls
requirement force, invalidity, and variability. The
[Catena Implementation Limits and Portability](../../IMPLEMENTATION-LIMITS.md)
policy governs resource disclosure; this area adds no new dimension.

## What belongs here

Put the resolution invariant, the classification table, and C066
conformance obligations here. The scope-structural resolution
model remains C021's. Literal spelling remains C017/C018's.
Instance evidence and coherence remain C065/C004's. Constructor
visibility remains C002/C023's. Operator instantiation remains
C061's. Record operations remain C041's. Surface spellings remain
P109's.

## Variability register

This area introduces no implementation-defined choice,
recommendation, bounded unspecified presentation, or implementation
limit. The invariant binds every conforming implementation
identically; no registry or tooling behavior may vary.

## Index

### Subdirectories

- None yet.

### Documents

- [The Resolution Invariant](the-resolution-invariant.md)
  — type independence, the five-way table, and the evidence
  carve-out.
- [Boundaries and Reservations](boundaries-and-reservations.md)
  — the exclusions and their arrival conditions.
- [Name Resolution Diagnostics and Conformance](diagnostics-and-conformance.md)
  — zero new families, abstract boundaries, and the `NMR-OBL-*`
  obligations with evidence sets.

## Maintaining this index

Update this README when a chapter is added, renamed, or archived.
Every direct child belongs in the index. If any excluded form ever
arrives, link the revision that amended the classification table
here.
