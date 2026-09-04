---
title: "Exception Boundary Specification"
kind: map
created: "2026-09-01"
tags:
  - archive-navigation
  - directory-index
  - failure
  - specification
aliases:
  - "Catena 0.1.47 exception boundary specification"
---

# Exception Boundary Specification (`60-specification/exception-boundary`)

## Purpose

This directory contains the Catena 0.1.47 contract for the
exception boundary: the three-way mechanism partition, the blessed
effect pattern, the panic classification, the routing table, and
the conformance obligations.

The repository-level [Specification Authority](../../SPECIFICATION-AUTHORITY.md)
controls status, applicability, rendered labels, and conflicts. The
[Catena Conformance Vocabulary](../../CONFORMANCE-VOCABULARY.md) controls
requirement force, invalidity, and variability. The
[Catena Implementation Limits and Portability](../../IMPLEMENTATION-LIMITS.md)
policy governs resource disclosure; this area adds no new dimension.

## What belongs here

Put the partition, the pattern blessing, the panic classification,
the routing table, and C081 conformance obligations here. The
failure taxonomy remains C036's, the exception-clause exclusion
C044's, the resumption discipline C005's, the process-local trap
evidence C010's, and the foreign visibility requirement C067's —
restated here as routing rows, not amended. Outcome-type contents
remain G103's, library faults G105's, cancellation G088's, process
death G084's, and foreign typing G095/G096's.

## Variability register

This area introduces no implementation-defined choice,
recommendation, bounded unspecified presentation, or implementation
limit. The partition and the routing bind every conforming
implementation identically; no registry or tooling behavior may
vary.

## Index

### Subdirectories

- None yet.

### Documents

- [The Mechanism Partition](the-mechanism-partition.md)
  — values, the effect pattern, and the terminal trap; the
  blessed pattern, panic-as-kind, and the routing table.
- [Exception Boundary Diagnostics and Conformance](diagnostics-and-conformance.md)
  — zero new families, abstract boundaries, and the `XB-OBL-*`
  obligations with evidence sets.

## Maintaining this index

Update this README when a chapter is added, renamed, or archived.
Every direct child belongs in the index. If a language exception
form ever arrives through the reopening door, link the discharging
revision here.
