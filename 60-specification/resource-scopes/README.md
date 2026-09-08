---
title: "Resource Scopes"
kind: map
created: "2026-09-08"
tags:
  - specification
  - algebraic-effects
aliases: []
---

# Resource Scopes (`60-specification/resource-scopes`)

## Purpose

This area defines local owned resource lifetime at the explicit `0.1.51`
compound-tree boundary. Public vocabulary and general foreign ownership remain
separate admission work.

The [authority policy](../../SPECIFICATION-AUTHORITY.md),
[conformance vocabulary](../../CONFORMANCE-VOCABULARY.md) and
[implementation limits](../../IMPLEMENTATION-LIMITS.md) govern this area.

## What belongs here

Rules for acquisition, scoped handles, reverse cleanup, abandonment, terminal
outcomes and the local cancellation/deadline interface.

## Index

### Subdirectories

None yet.

### Documents

- [Owned Lifetime and Mandatory Cleanup](owned-lifetime-and-mandatory-cleanup.md)
  — specifies the checked local scope boundary, outcome precedence and
  reference/BEAM obligations.

## Variability register

This area introduces no implementation-defined choice, presentation allowance
or implementation-limit dimension. Release grace is an explicit input;
whole-millisecond rounding is fixed by the contract. Clock-event scheduling
is defined nondeterminism, not unspecified presentation. Standing runtime
capacity and reference-evidence budgets retain their classifications.

## Maintaining this index

Inventory every direct child and update authority, traceability and evidence
links in the same change as a chapter's status or applicability.
