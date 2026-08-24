---
title: "Resolution and Lockfile"
kind: specification
created: "2026-08-24"
status: candidate
spec_version: "0.1.21"
tags:
  - packages
  - specification
  - versioning
aliases:
  - "Catena resolution and lockfile"
---

# Resolution and Lockfile

## Status and authority

This chapter is the normative Catena 0.1.21 resolution, lockfile, and
identity contract. It is governed by
[Specification Authority](../../SPECIFICATION-AUTHORITY.md),
[Catena Conformance Vocabulary](../../CONFORMANCE-VOCABULARY.md), and
[Catena Implementation Limits and Portability](../../IMPLEMENTATION-LIMITS.md).
It applies [Manifest Dependencies and Versions](manifest-dependencies-and-versions.md)
over the unchanged C008 manifest and reuses the C006 canonicalization
machinery.

The rules apply only to source-language revision `0.1.21`.

## The resolution environment

Resolution runs against a package environment: a mapping from package
name to the set of available versions with their metadata. How an
environment is populated — local files, a registry mirror, a vendor
directory — is G121's build-tooling question; this chapter defines the
deterministic function from manifest plus environment to outcome
(`PK-OBL-006`).

## The dependency graph is a DAG

Package dependencies MUST form a directed acyclic graph. A package that
transitively depends on itself is static invalidity reported as `PKG002`
naming the cycle's path (`PK-OBL-007`). This is distinct from C024
*module* cycles inside one package, which remain admitted: the package
graph itself never loops.

## Single-version resolution

For each package name reachable from the root manifest's `dependencies`,
the resolved version is the highest available version that satisfies
every requirement on that name gathered from the root and from every
resolved dependency's own `dependencies` (`PK-OBL-008`). Build metadata
never participates in the choice: of versions equal up to build, at most
one may be present in an environment, otherwise `PKG005`.

If no available version satisfies every gathered requirement, resolution
fails as `PKG003` static invalidity listing the package name and every
requirer with its requirement (`PK-OBL-009`). If a declared name is
absent from the environment, resolution fails as `PKG004` naming the
requirer (`PK-OBL-009`).

Resolution is a pure function of manifest and environment
(`PK-OBL-008`): traversal order, environment map ordering, and insertion
order of requirements never change the resolved set, the chosen versions,
or the failure.

## The lockfile

`catena.lock` is a generated, never-hand-edited canonical-JCS JSON record
(`PK-OBL-010`). For each resolved package it records: the package name;
the exact resolved version; the requirement that admitted it from the
root or its requirers; the list of requirers; the SHA-256 bundle digest;
the sorted member interface digests; and the sorted component joint
digests of its C024 strongly-connected components. It also records the
resolved edition, language revision, and preview selection per package
and for the root.

Replay: when a lockfile is present, each recorded exact version is used
as an exact pin — resolution is not recomputed — provided every recorded
requirement-against-version pair still satisfies the grammar and every
recorded digest matches the present content (`PK-OBL-011`). A lockfile
whose recorded versions or requirements no longer match the manifest is
stale and fails as `PKG005` re-lock invalidity; a bundle-digest mismatch
against present content is tamper and also fails as `PKG005`, with the
reason distinguishing the two.

Regeneration: generating a lockfile twice from the same manifest and
environment yields byte-identical output (`PK-OBL-012`). Hand edits are
never repaired; a malformed lockfile is `PKG001`.

## Bundle-digest identity

Package identity is the triple (name, version, bundle digest)
(`PK-OBL-006`). The bundle digest is SHA-256 over the canonical JCS of:

1. the manifest's semantic fields — name, version, dependencies,
   selection, modules, interfaces, roots, output — with irrelevant
   presentation excluded;
2. the sorted member interface digests; and
3. the sorted component joint digests.

Identical package content yields an identical digest regardless of file
order, key order, or transport. No two distinct contents may share a
digest; a collision is treated as an implementation failure, not a
semantic event.

## The Hex transport profile

hex.pm is the bootstrap transport profile (`PK-OBL-006`): a Catena
package published there carries the same name and SemVer version, and
the registry tarball checksum recorded at install MUST equal the package's
bundle digest for the install to be valid. Registry retirement, signing,
and mirrors remain G130's layers; the identity above stays
registry-neutral so a second transport changes nothing.

## Deliberately separate work

Build and fetch tools (G121), reproducible-build consumption (G128),
signing and threat modeling (G130), compatibility meanings of versions
(G028), and re-export facades — re-owned from C022's deferral to the
G028 compatibility era by this area — stay outside.

## Rationale and evidence (non-normative)

The [package synthesis](../../20-notes/catena-package-identity-and-dependencies.md)
records why one-version-per-name is mandated by C010 nominal identity and
what the lockfile trades for reproducibility.
