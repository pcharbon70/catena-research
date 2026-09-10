---
title: "Compatibility Suite"
kind: map
created: "2026-09-10"
tags: [specification, compatibility, conformance, testing]
aliases: []
---

# Compatibility Suite (`60-specification/compatibility-suite`)

## Purpose

Bounded, machine-readable compatibility evidence across language revisions,
semantic interfaces, dependency graphs, persistent data, supported toolchains,
historical signatures, and runtime upgrades under
[authority](../../SPECIFICATION-AUTHORITY.md),
[conformance vocabulary](../../CONFORMANCE-VOCABULARY.md), and
[implementation limits](../../IMPLEMENTATION-LIMITS.md).

## What belongs here

Rules for compatibility matrices, their layer-specific oracles, coverage bounds,
result classes, and the limits of claims drawn from finite fixtures.

## Index

### Subdirectories

None yet.

### Documents

- [Layered Matrix and Edition Policy](layered-matrix-and-edition-policy.md) — C136's exact matrix format, oracle separation, retained coverage, and bounded-claim contract.

## Variability register

Implementations publish the retained revisions, interface formats, artifact
formats, toolchain fingerprints, graph dimensions, and runtime-upgrade paths
covered by a matrix. Unlisted combinations have the `unsupported` result and do
not silently become failures or compatibility promises.

## Maintaining this index

Keep edition lifecycle, API compatibility, package locks, artifact migration,
toolchain support, hot upgrades, compiler fixtures, traceability, and the
completion checklist synchronized with this matrix contract.
