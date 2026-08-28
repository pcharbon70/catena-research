---
title: "Resource Observability Specification"
kind: map
created: "2026-08-26"
tags:
  - archive-navigation
  - directory-index
  - observability
  - specification
aliases:
  - "Catena 0.1.33 observability specification"
---

# Resource Observability Specification (`60-specification/resource-observability`)

## Purpose

This directory contains the Catena 0.1.33 contract for resource and
allocation observability: the six-way classification of program
observability, semantic identity, the two-clause identity rule, the
finalization declared absence with its gate, the debugging-channel
distinction, the abstract boundaries, and executable conformance
obligations.

The repository-level [Specification Authority](../../SPECIFICATION-AUTHORITY.md)
controls status, applicability, rendered labels, and conflicts. The
[Catena Conformance Vocabulary](../../CONFORMANCE-VOCABULARY.md) controls
requirement force, invalidity, and variability. The
[Catena Implementation Limits and Portability](../../IMPLEMENTATION-LIMITS.md)
policy governs resource disclosure; this area adds no new dimension.

## What belongs here

Put the observability classification, semantic identity, the identity
rule, the finalization absence, and C037 conformance obligations
here. The kernel calculus remains C010's, frozen at 0.1.8. The tail
guarantee remains C032/C034's. Comparison exclusions remain C035's,
now permanent. Handle operations remain C010's and G084's. Resource
scopes and cleanup remain the G080s era's. Message-copy details remain
G085's. Foreign finalization remains G095's. Debugging tools remain
G124's.

## Variability register

This area introduces no implementation-defined choice, recommendation,
bounded unspecified presentation, or implementation limit beyond the
one it elevates: representation is a non-observable, so implementors
retain every representation freedom. The classification is
deterministic; no registry or tooling behavior may vary.

## Index

### Subdirectories

- None yet.

### Documents

- [The Observability Model](the-observability-model.md) — the
  kernel-verbatim elevation with the six-way classification and the
  semantic-identity statement.
- [Identity and Finalization](identity-and-finalization.md) — the
  two-clause identity rule, the finalization declared absence with
  its gate, and the debugging-channel distinction.
- [Diagnostics and Conformance](diagnostics-and-conformance.md) — the
  zero-new-families contract, the witness boundaries,
  `RO-OBL-001`–`RO-OBL-008`, evidence sets, and persistence
  separation.

## Maintaining this index

Keep all chapters at one lifecycle status and version. A
classification, identity, or absence change requires an explicit later
semantic revision. Cleanup arrives only through its gated eras. Keep
the traceability map, sibling compiler tests, source-language guides,
and this inventory synchronized.
