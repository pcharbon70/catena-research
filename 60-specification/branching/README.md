---
title: "Branching Specification"
kind: map
created: "2026-08-25"
tags:
  - archive-navigation
  - directory-index
  - branching
  - specification
aliases:
  - "Catena 0.1.29 branching specification"
---

# Branching Specification (`60-specification/branching`)

## Purpose

This directory contains the Catena 0.1.29 contract for conditionals
and general branching: match as the single branch form, the
conditional sugar promise, the consolidated branch rules with their
cited homes, the declared absence of statement-like control forms, the
abstract boundaries, and executable conformance obligations.

The repository-level [Specification Authority](../../SPECIFICATION-AUTHORITY.md)
controls status, applicability, rendered labels, and conflicts. The
[Catena Conformance Vocabulary](../../CONFORMANCE-VOCABULARY.md) controls
requirement force, invalidity, and variability. The
[Catena Implementation Limits and Portability](../../IMPLEMENTATION-LIMITS.md)
policy governs resource disclosure; this area adds no new dimension.

## What belongs here

Put the branch-form statement, the sugar promise, the consolidated
rule table, the statement-form absence, and C033 conformance
obligations here. Match typing, coverage, and redundancy remain
C002's; the condition fragment remains C003's; commitment dynamics
remain C010's; the strictness skips remain C029's; scrutinee and
clause schedules remain C030's; tail calls after selection remain
C032's. Termination remains P034's. The failure taxonomy remains
G036's. Future scrutinee types' coverage entries remain G040's.
Surface spellings remain P109's. Cancellation mid-branch remains
G088's.

## Variability register

This area introduces no implementation-defined choice, recommendation,
bounded unspecified presentation, or implementation limit. Branching
semantics are deterministic; no registry or tooling behavior may
vary.

## Index

### Subdirectories

- None yet.

### Documents

- [The Branch Form and Its Desugaring](the-branch-form-and-its-desugaring.md)
  — match as the only branch form, the conditional sugar promise, and
  Boolean-pattern dispatch.
- [Branch Rules Consolidated](branch-rules-consolidated.md) — the
  cited elevation of scrutinee-once, clause order, conditions,
  fallthrough, commitment, branch typing, missing alternatives, and
  tail-position clause calls.
- [Diagnostics and Conformance](diagnostics-and-conformance.md) — the
  zero-new-families contract, the statement-form declared absence, the
  witness boundaries, `BR-OBL-001`–`BR-OBL-008`, evidence sets, and
  persistence separation.

## Maintaining this index

Keep all chapters at one lifecycle status and version. A branch-form,
promise, or absence change requires an explicit later semantic
revision. G040 enters each new scrutinee type with its coverage entry;
P109 consumes the sugar promise. Keep the traceability map, sibling
compiler tests, source-language guides, and this inventory
synchronized.
