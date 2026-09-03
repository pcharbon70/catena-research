---
title: "Selective Receive Specification"
kind: map
created: "2026-09-01"
tags:
  - archive-navigation
  - directory-index
  - receive
  - specification
aliases:
  - "Catena 0.1.46 selective receive specification"
---

# Selective Receive Specification (`60-specification/selective-receive`)

## Purpose

This directory contains the Catena 0.1.46 contract for selective
receive: the fixed rule set (scan order, preservation, removal,
typing, conditions, starvation cost), the four routed interfaces,
and the conformance obligations.

The repository-level [Specification Authority](../../SPECIFICATION-AUTHORITY.md)
controls status, applicability, rendered labels, and conflicts. The
[Catena Conformance Vocabulary](../../CONFORMANCE-VOCABULARY.md) controls
requirement force, invalidity, and variability. The
[Catena Implementation Limits and Portability](../../IMPLEMENTATION-LIMITS.md)
policy governs resource disclosure; this area adds no new dimension.

## What belongs here

Put the receive rule set, the routed interfaces, and C086
conformance obligations here. The lowering harness and its
conditions remain C003's, restated here at the language level, not
amended. The public-receive reservation remains C044's, consumed
here by the timeout-fallback naming. Mailbox preservation remains
C010's. Send-side message semantics remain G085's, typed protocols
G087's, and cancellation and time G088's to ship. Public tokens
remain P109's.

## Variability register

This area introduces no implementation-defined choice,
recommendation, bounded unspecified presentation, or implementation
limit. Scan order, preservation, and the cost statement bind every
conforming implementation identically; no registry or tooling
behavior may vary.

## Index

### Subdirectories

- None yet.

### Documents

- [The Receive Rule Set](the-receive-rule-set.md)
  — scan order, preservation, removal, typing, conditions, and
  starvation cost.
- [The Routed Interfaces](the-routed-interfaces.md)
  — the obligations on P109, G088, G087, and G085.
- [Selective Receive Diagnostics and Conformance](diagnostics-and-conformance.md)
  — zero new families, abstract boundaries, and the `SR-OBL-*`
  obligations with evidence sets.

## Maintaining this index

Update this README when a chapter is added, renamed, or archived.
Every direct child belongs in the index. When an interface's owner
ships its slice, link the discharging revision here.
