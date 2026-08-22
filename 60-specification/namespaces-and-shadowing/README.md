---
title: "Namespaces and Shadowing Specification"
kind: map
created: "2026-08-22"
tags:
  - archive-navigation
  - directory-index
  - namespaces
  - specification
aliases:
  - "Catena 0.1.17 namespace specification"
---

# Namespaces and Shadowing Specification (`60-specification/namespaces-and-shadowing`)

## Purpose

This directory contains the Catena 0.1.17 contract for namespaces and
shadowing: the namespace category inventory with its spelling-class
partition, uniqueness domains, the scope and shadowing model, type-variable
scoping, local-over-imported precedence with collision rejection, governed
identity separation, two-segment qualification, stable diagnostics, the
abstract scope-event resolver boundary, and executable conformance
obligations.

The repository-level [Specification Authority](../../SPECIFICATION-AUTHORITY.md)
controls status, applicability, rendered labels, and conflicts. The
[Catena Conformance Vocabulary](../../CONFORMANCE-VOCABULARY.md) controls
requirement force, invalidity, diagnostic presentation, and variability. The
[Catena Implementation Limits and Portability](../../IMPLEMENTATION-LIMITS.md)
policy governs aggregate-input disclosure; this area adds no new resource
dimension.

## What belongs here

Put namespace categories and their spelling classes, uniqueness domains,
scope structure, shadowing and duplicate rules, type-variable interaction
with type and trait namespaces, cross-origin precedence and collision
rejection, governed-identity separation, qualification depth, and C021
conformance obligations here. Import and export syntax, visibility
defaults, renaming, wildcard exclusion, and unused-import diagnostics
remain G022. Module cycles remain G024. Package-level module uniqueness
remains G025. Prelude contents remain G026. Type-directed resolution
remains G066. The declaration grammar that emits scope events remains
P109.

## Variability register

This area introduces no implementation-defined choice, recommendation, or
bounded unspecified presentation. It introduces no implementation limit.
Scope-event streams remain subject to the aggregate-input policy of the
G129 owner.

## Index

### Subdirectories

- None yet.

### Documents

- [Namespace Inventory and Spelling](namespace-inventory-and-spelling.md)
  — the category inventory, the two spelling classes as a hard partition,
  uniqueness domains, the flat constructor namespace, and governed
  identity separation.
- [Shadowing and Ambiguity](shadowing-and-ambiguity.md) — the scope
  model, deterministic silent shadowing, same-scope duplicate invalidity,
  type-variable quantifier scoping, local-over-imported precedence, and
  collision rejection.
- [Diagnostics and Conformance](diagnostics-and-conformance.md) — stable
  `NSP001`–`NSP005`, the abstract scope-event resolver boundary,
  two-segment qualification, `NS-OBL-001`–`NS-OBL-014`, evidence sets,
  and persistence separation.

## Maintaining this index

Keep all chapters at one lifecycle status and version. A category,
spelling-class binding, uniqueness domain, shadowing rule, precedence
rule, or qualification-depth change requires an explicit later semantic
revision. Keep the traceability map, sibling compiler tests,
source-language guides, and this inventory synchronized.
