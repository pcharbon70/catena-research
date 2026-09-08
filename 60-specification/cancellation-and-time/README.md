---
title: "Cancellation and Time"
kind: map
created: "2026-09-08"
tags:
  - specification
  - actors
aliases: []
---

# Cancellation and Time (`60-specification/cancellation-and-time`)

## Purpose

This area defines the normative C088 cancellation and time contract at exact
`0.1.53`.

The [authority policy](../../SPECIFICATION-AUTHORITY.md),
[conformance vocabulary](../../CONFORMANCE-VOCABULARY.md), and
[implementation limits](../../IMPLEMENTATION-LIMITS.md) govern this area.

## What belongs here

Exact durations, opaque local deadlines, sleep, total timed receive, safe-point
cancellation and their interactions with bounded lifetime cleanup.

## Index

### Subdirectories

None yet.

### Documents

- [Deadlines, Waits and Cancellation](deadlines-waits-and-cancellation.md) — normative
  time-target semantics and the eight conformance obligations.

## Variability register

No new implementation-defined choice, presentation allowance or implementation
limit is introduced. Durations are input; scheduler and deadline races are
specified nondeterminism. The fixed native wait interval does not cap language
durations. Standing capacity and evidence bounds retain their classifications.

## Maintaining this index

Inventory every direct child. Change authority, evidence, traceability and
version-selection records together when changing the contract.
