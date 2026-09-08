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

The `0.1.49` [waiting and scan cost amendment](../selective-receive-correction/waiting-and-scan-cost-amendment.md)
repairs the rejected-prefix contradiction in the retained `0.1.46` rule set.
The historical chapter remains available; the amendment explicitly identifies
which rules it replaces and adopts.

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
C010's. Send-side message semantics remain P085's, typed protocols
P087's, and cancellation and time G088's to ship. Public tokens
remain P109's.

## Variability register

The amendment permits internal scan caching only within the visibly declared
unobservable strategy equivalence class in
[Scan work](../selective-receive-correction/waiting-and-scan-cost-amendment.md#scan-work). Selected messages,
residual mailbox and effects remain fixed. No new implementation-defined
choice or implementation limit is introduced.

## Index

### Subdirectories

- None yet.

### Documents


- [The Receive Rule Set](the-receive-rule-set.md)
  — scan order, preservation, removal, typing, conditions, and
  starvation cost.
- [The Routed Interfaces](the-routed-interfaces.md)
  — the obligations on P109, G088, P087, and P085.
- [Selective Receive Diagnostics and Conformance](diagnostics-and-conformance.md)
  — zero new families, abstract boundaries, and the `RC-OBL-*`
  obligations with evidence sets.

## Maintaining this index

Update this README when a chapter is added, renamed, or archived.
Every direct child belongs in the index. When an interface's owner
ships its slice, link the discharging revision here.
