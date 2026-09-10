---
title: "Build System and Package Manager"
kind: map
created: "2026-09-10"
tags: [specification, packages, tooling, reproducibility]
aliases: []
---

# Build System and Package Manager (`60-specification/build-system`)

## Purpose

Project discovery, workspace planning, verified acquisition, offline execution,
cache identity, and output publication under
[authority](../../SPECIFICATION-AUTHORITY.md),
[conformance vocabulary](../../CONFORMANCE-VOCABULARY.md), and
[implementation limits](../../IMPLEMENTATION-LIMITS.md).

## What belongs here

Rules that compose retained manifests, dependency locks, registry acquisition,
reproducible compiler plans, and governed artifacts into a complete build path.

## Index

### Subdirectories

None yet.

### Documents

- [Project Graphs, Acquisition, and Offline Builds](project-graphs-acquisition-and-offline-builds.md) — C121's exact workspace, cache, generator, and publication contract.

## Variability register

Implementations publish their supported named profiles and finite workspace,
dependency, generator, path, acquisition, and artifact bounds. Build execution
does not admit ambient network access or undeclared generator authority.

## Maintaining this index

Keep package identity, locks, registry policy, reproducible inputs, build
orchestration, trust inventory, traceability, and the completion checklist in
sync.
