---
title: "Project Graphs, Acquisition, and Offline Builds"
kind: specification
created: "2026-09-10"
status: normative
spec_version: "0.1.81"
tags: [specification, packages, tooling, reproducibility]
aliases: []
---

# Project Graphs, Acquisition, and Offline Builds

## Status and authority

C121 defines revision `0.1.81` under [authority](../../SPECIFICATION-AUTHORITY.md),
[conformance vocabulary](../../CONFORMANCE-VOCABULARY.md), and
[implementation limits](../../IMPLEMENTATION-LIMITS.md). It completes the
[P121 plan](../../20-notes/language-completion-plan-delivery.md#item-121-build-system-and-package-manager)
over C025 locks, C128 reproducible inputs, C130 verified acquisition, and C116
artifact evolution. It selects no public project or language vocabulary
(`BG-OBL-001`).

## Project discovery and profiles

An explicit project path has precedence and must identify an available regular
project input. Without one, a project file at the workspace root has precedence.
Otherwise exactly one nested project file is discoverable; zero or several
candidates produce an explicit discovery failure (`BG-OBL-002`).

A build selects one exact named profile before planning. The profile is part of
build identity and cannot silently inherit ambient host settings. The bootstrap
profiles are `development`, `test`, and `release` (`BG-OBL-003`).

## Workspace graph

A workspace contains uniquely named packages and explicit workspace or locked
external dependency edges. Every workspace edge resolves inside that workspace.
The graph is finite and acyclic; cycles, missing vertices, duplicate identities,
or malformed edges refuse the whole plan (`BG-OBL-004`).

Planning computes one stable topological order. A dependency is built before
each dependent and a shared diamond dependency is built at most once for one
plan (`BG-OBL-005`).

Each package binds a retained reproducible input digest, exact toolchain digest,
capability-set digest, selected profile, declared generators, and dependency
identities. A workspace dependency contributes its recursively computed cache
key, so any changed dependency invalidates every transitive dependent
(`BG-OBL-006`).

## Acquisition and offline execution

External content is identified by its locked package, version, and SHA-256
digest. Acquisition completes before build execution and verifies size and bytes
against that digest (`BG-OBL-007`).

Acquisition is transactional for a plan. If any download is interrupted,
missing, oversized, or has the wrong digest, no newly acquired item becomes
visible in the returned cache (`BG-OBL-008`).

Build execution performs no network operation. Missing locked content or a
corrupt cache entry refuses the offline build before package output publication
(`BG-OBL-009`).

## Generators and cache identity

A generator declares a finite nonempty set of normalized relative inputs and
one normalized relative output. Parent traversal, output/input aliasing,
undeclared inputs, undeclared outputs, and ambient shell authority are refused
(`BG-OBL-010`).

Generator declarations, their retained reproducible input bytes, the exact
environment admitted by C128, and their capability-set digest contribute to the
package cache key. A generated file has the same provenance and hashing duties
as another build input (`BG-OBL-011`).

A cached package archive is accepted only when it is canonical, validates under
C128, and names the expected package input digest. A valid archive stored under
another package's key is not a cache hit (`BG-OBL-012`).

## Output publication

The retained compiler builds each cache miss in a fresh package root and emits a
canonical complete-output archive. Clean, cached, and offline execution of one
exact plan produce byte-identical declared outputs (`BG-OBL-013`).

Publication stages and verifies the complete archive before an atomic rename.
A staging, verification, or replacement failure preserves the previously
published destination bytes (`BG-OBL-014`).

## Variability and limits

> **Implementation-defined choice.** An implementation publishes supported
> profile names and configured maxima for workspace packages, dependencies per
> package, generators per package, acquisition bytes, path bytes, reproducible
> inputs, and output archives. Exhaustion refuses the affected plan or
> transaction without partial acquisition or publication (`BG-OBL-015`).

## Diagnostics and conformance

Tests MUST cover discovery precedence and ambiguity, cycles, missing workspace
dependencies, diamond graphs, profile switches, transitive cache invalidation,
declared generator confinement, missing and corrupt cache content, interrupted
and wrong-digest acquisition, clean/cached/offline equivalence through the real
retained compiler, output rollback, lifecycle registration, conformance
reporting, and trust classification (`BG-OBL-016`).

## Rationale and evidence (non-normative)

The [implementation journal](../../50-journal/2026-09-10-build-system.md)
records the four planned forks, additional four-way implementation decisions,
and executable evidence. The
[package map](../../10-maps/package-identity-and-dependencies.md) connects this
orchestration layer to its identity, compatibility, reproducibility, registry,
and governance foundations.
