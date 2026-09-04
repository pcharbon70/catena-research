---
title: "Top-Level Effects Specification"
kind: map
created: "2026-09-01"
tags:
  - archive-navigation
  - directory-index
  - effects
  - specification
aliases:
  - "Catena 0.1.48 top-level effects specification"
---

# Top-Level Effects Specification (`60-specification/top-level-effects`)

## Purpose

This directory contains the Catena 0.1.48 contract for top-level
effects: the boundary statement (nothing unhandled, nobody
interpreting), the capability interface G106 must satisfy, the
supervision routing, and the conformance obligations.

The repository-level [Specification Authority](../../SPECIFICATION-AUTHORITY.md)
controls status, applicability, rendered labels, and conflicts. The
[Catena Conformance Vocabulary](../../CONFORMANCE-VOCABULARY.md) controls
requirement force, invalidity, and variability. The
[Catena Implementation Limits and Portability](../../IMPLEMENTATION-LIMITS.md)
policy governs resource disclosure; this area adds no new dimension.

## What belongs here

Put the boundary statement, the capability interface, the
supervision routing, and C082 conformance obligations here. Entry
declaration and validity remain C027's, restated here as routing
rows, not amended. Launch semantics remain C027's. The prelude's
zero-implicit-names rule remains C026's. The foreign visibility
requirement remains C067's. The capability channel's design
remains G106's, failure interpretation G084's, and entry-form
tokens P109's.

## Variability register

This area introduces no implementation-defined choice,
recommendation, bounded unspecified presentation, or implementation
limit. The boundary and the interface bind every conforming
implementation identically; no registry or tooling behavior may
vary.

## Index

### Subdirectories

- None yet.

### Documents

- [The Top-Level Boundary](the-top-level-boundary.md)
  — nothing unhandled, nobody interpreting, the capability
  interface, and the door.
- [Top-Level Effects Diagnostics and Conformance](diagnostics-and-conformance.md)
  — zero new families, abstract boundaries, and the `TL-OBL-*`
  obligations with evidence sets.

## Maintaining this index

Update this README when a chapter is added, renamed, or archived.
Every direct child belongs in the index. When G106's channel or
any entry-form widening arrives, link the discharging revision
here.
