---
title: "Package Diagnostics and Conformance"
kind: specification
created: "2026-08-24"
status: normative
spec_version: "0.1.21"
tags:
  - conformance
  - diagnostics
  - packages
  - specification
  - testing
aliases:
  - "Catena 0.1.21 package conformance"
---

# Package Diagnostics and Conformance

## Status and authority

This chapter is the normative Catena 0.1.21 package diagnostic, abstract
frontend, and conformance contract. It is governed by
[Specification Authority](../../SPECIFICATION-AUTHORITY.md),
[Catena Conformance Vocabulary](../../CONFORMANCE-VOCABULARY.md), and
[Catena Implementation Limits and Portability](../../IMPLEMENTATION-LIMITS.md).
It applies [Manifest Dependencies and Versions](manifest-dependencies-and-versions.md)
and [Resolution and Lockfile](resolution-and-lockfile.md).

## Stable diagnostics

| ID | Required meaning |
| --- | --- |
| `PKG001` | a malformed version, requirement, package name, or lockfile |
| `PKG002` | the package dependency graph contains a cycle |
| `PKG003` | no available version satisfies every gathered requirement on a name |
| `PKG004` | a declared dependency name is absent from the environment |
| `PKG005` | a lockfile is stale, tampered, or the environment duplicates a version up to build metadata |

An exact-selection mismatch remains `EDN001`. Failure is transactional:
no resolution result, lockfile bytes, or artifact is published for the
affected action. Diagnostics carry the offending names, versions,
requirements, and — for `PKG003` — every requirer with its requirement.
Diagnostic prose can improve only within the bounded presentation rules.

## Abstract public boundary

A conforming implementation exposes a dependency engine with these
operations (`PK-OBL-001`):

- **Requirement parsing** — version and requirement strings to parsed
  forms, or `PKG001`;
- **Satisfaction** — parsed version against parsed requirement;
- **Resolution** — root manifest plus environment to the resolved set
  (name → exact version, admitting requirement, requirers, digests), or
  one diagnostic; a pure, order-independent function;
- **Lockfile generation** — resolution to canonical `catena.lock` bytes,
  byte-deterministic for identical inputs;
- **Lockfile replay** — manifest, lockfile, and content digests to an
  exact-pin resolution or `PKG005`;
- **Bundle digest** — package semantic content to its SHA-256 identity.

The engine does not fetch, cache, build, sign, or run registry
protocols; implementations MUST NOT use this boundary to claim those
G121/G130 phases (`PK-OBL-012`).

The bootstrap evidence names these `Catena.Package.Deps.parse_version/1`,
`parse_requirement/1`, `satisfies?/2`, `resolve/2`,
`generate_lockfile/2`, `replay_lockfile/3`, and `bundle_digest/1`. These
Elixir names are evidence API names, not required names for every
implementation.

## Determinism

Equal inputs produce equal parsed forms, resolutions, lockfile bytes, or
diagnostics on every conforming implementation (`PK-OBL-012`). Bundle
digests are stable under reordering of manifest keys, environment maps,
member lists, and component lists.

## Conformance obligations

| ID | Obligation | Required executable evidence |
| --- | --- | --- |
| `PK-OBL-001` | apply package behavior only at exact 0.1.21 and register the stable lifecycle addition | exact selection, registry, and lifecycle tests |
| `PK-OBL-002` | validate the `dependencies` field: names, single requirement strings, absence means free | field matrix and malformed-rejection tests |
| `PK-OBL-003` | enforce the SemVer grammar and precedence including pre-release ordering and build exclusion | grammar matrix and ordering tests |
| `PK-OBL-004` | enforce the three-form requirement grammar, rejecting other operators, compounds, and operand build metadata | requirement matrix tests |
| `PK-OBL-005` | enforce exact/caret/tilde satisfaction with the Cargo 0.x rule and the pre-release operand restriction | boundary tables including `^0.1.2`, `^0.0.3`, `~1.2.3` |
| `PK-OBL-006` | compute registry-neutral bundle digests as SHA-256 over canonical JCS of semantic fields plus member and component digests | digest stability under reordering |
| `PK-OBL-007` | reject cyclic package graphs as `PKG002` with the cycle path | cycle tests |
| `PK-OBL-008` | resolve single-version highest-satisfying per name, order-independently | diamond resolution and permutation tests |
| `PK-OBL-009` | reject unsatisfiable sets as `PKG003` with every requirer and absent names as `PKG004` | conflict and unknown-name tests |
| `PK-OBL-010` | generate canonical byte-deterministic `catena.lock` records | double-generation byte-equality tests |
| `PK-OBL-011` | replay a matching lockfile as exact pins and reject stale or tampered locks as `PKG005` | replay, re-lock, and tamper tests |
| `PK-OBL-012` | keep the engine deterministic, source-only, and outside G121/G130 phases | repeated-result and absent-phase tests |

Every obligation has at least one tagged passing test. The sibling
compiler gates the complete `PK-OBL-*` set against unknown and uncovered
identifiers before C025 conformance is claimed.

## Required evidence sets

Positive evidence includes valid version and requirement matrices; the
pre-release ordering cases; boundary satisfaction tables; diamond
resolution; deep multi-level graphs; lockfile generation, replay, and
double-generation byte-equality; bundle digests stable under key, list,
and environment reordering; and integration with the existing manifest
decoder carrying `dependencies` and with C024 joint digests embedded in
locks.

Negative evidence includes malformed versions (leading zeros, partial,
empty, build in operands), bad operators and compounds, invalid package
names, cyclic graphs with path evidence, unsatisfiable intersections
naming all requirers, unknown names, stale and tampered lockfiles, and
duplicate-up-to-build environments.

Exclusion evidence demonstrates that dependency-free manifests are
byte-unchanged, that the engine fetches nothing and runs no registry
protocol, and that predecessor APIs retain their exact selections and
defaults.

## Re-export re-ownership

C022 deferred re-exports to "G025 package assembly." This area completes
without them, and the deferral is re-owned: facade-style forwarding now
awaits the C028 compatibility era, where a package's public surface
evolution and digest chains are designed. No spelling is reserved.

## Revision and persistence separation

Revision `0.1.21` adds the dependency grammar, resolution, lockfile, and
identity layers; it adds no JSON AST version, kernel S-expression
version, interface version, artifact version, signature domain, typing
rule, runtime behavior, or BEAM representation (`PK-OBL-001`,
`PK-OBL-012`). The manifest's `dependencies` field is optional and
backward-compatible: every previously valid manifest remains valid.

The source-text decoder accepts cumulative revisions `0.1.9` through
`0.1.21`; every predecessor API retains its exact selection. The next
unused semantic patch is `0.1.22`.

## Rationale and evidence (non-normative)

The design route is preserved in the
[package synthesis](../../20-notes/catena-package-identity-and-dependencies.md),
the [resolved inquiry](../../40-inquiries/how-should-catena-define-package-identity-and-dependency-resolution.md),
and the [topic map](../../10-maps/package-identity-and-dependencies.md).
The C025 evidence record will preserve the sibling-compiler commands and
archive validation.
