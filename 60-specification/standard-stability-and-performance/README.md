---
title: "Standard Stability and Performance"
kind: map
created: "2026-09-10"
tags: [specification, standard-library, compatibility, performance]
aliases: []
---

# Standard Stability and Performance (`60-specification/standard-stability-and-performance`)

## Purpose

The normative operation-contract policy under
[Specification Authority](../../SPECIFICATION-AUTHORITY.md),
[Catena Conformance Vocabulary](../../CONFORMANCE-VOCABULARY.md), and
[Catena Implementation Limits and Portability](../../IMPLEMENTATION-LIMITS.md).

## What belongs here

Rules for library law and behavior stability, per-operation complexity and
stack contracts, replacement classification, representation exclusions, and
toolchain-bound performance observations.

## Index

### Subdirectories

None yet.

### Documents

- [Versioned Operation Contracts](versioned-operation-contracts.md) — P108's revision 0.1.87 library stability, complexity, replacement, and evidence policy.

## Variability register

Implementations may improve an asymptotic bound without breaking compatibility
and may publish toolchain-specific measurements. They may not weaken a
published semantic or complexity contract, infer a portable timing guarantee,
or expose an unversioned representation promise.

## Maintaining this index

Keep the standard package catalog, compatibility classifier, measurement
evidence, lifecycle metadata, and traceability obligations synchronized.
