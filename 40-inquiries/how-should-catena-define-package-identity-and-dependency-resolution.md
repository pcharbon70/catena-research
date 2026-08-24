---
title: "How Should Catena Define Package Identity and Dependency Resolution?"
kind: inquiry
created: "2026-08-24"
status: open
tags:
  - catena
  - language-design
  - packages
  - versioning
aliases:
  - "Catena package identity inquiry"
---

# How Should Catena Define Package Identity and Dependency Resolution?

## Why this matters

C008 gave Catena a package manifest with an exact language selection, and
C024 gave modules components with joint digests — but a package cannot yet
declare a dependency, no version grammar exists, nothing resolves
conflicting transitive requirements, and no lockfile or integrity rule
makes a build reproducible. Until G025 closes, multi-package programs are
only a manifest shape: two packages that depend on a third have no defined
way to agree on which version of it they see, and every one of those
disagreements would leak into G027's entry points, G028's compatibility
policy, G121's build tooling, and G130's supply-chain rules.

## Operational question

Choose a bounded 0.1.21 boundary in which independent implementations agree
on:

- how a package declares dependencies and what absence means;
- the version grammar and the exact/caret/tilde requirement operators,
  including their pre-1.0 semantics;
- how conflicting transitive requirements resolve and when they reject;
- the lockfile: shape, generation, replay, and determinism;
- package source identity and integrity, independent of any registry; and
- the transport profile under which hex.pm publishing works.

The answer must compose with the C008 manifest's selection semantics, the
C024 component joint digests, and the C006 canonicalization machinery
without deciding G121 build tooling, G130 supply-chain signing, G028
compatibility policy, G026 prelude contents, or G027 entry points.

## Working hypotheses

- The manifest gains an optional `dependencies` object: package name →
  requirement string; absence means dependency-free.
- Versions are SemVer 2.0.0 with parsed pre-release and build metadata;
  requirements are exact pins, caret (`^`, Cargo-style 0.x rule), and
  tilde (`~`, same-patch step).
- Resolution picks one version per package name per build — the highest
  satisfying every requirement — with empty intersections rejected and
  every conflicting requirer named.
- A generated, never-hand-edited `catena.lock` records resolved versions,
  admitting requirements, requirers, digests, and selections; a matching
  lockfile replays as exact pins; regeneration is byte-deterministic.
- Package identity is (name, version, SHA-256 bundle digest) over canonical
  JCS of manifest semantic fields plus member interface digests plus C024
  component joint digests; hex.pm is the bootstrap transport profile whose
  tarball checksum must equal the bundle digest.
- Re-exports remain excluded, with their C022 deferral re-owned by the
  G028 compatibility era.

## Paths to explore

- [Semantic Versioning 2.0.0 grammar and precedence](../30-sources/preston-werner-2013-semantic-versioning.md)
  fix the version ordering.
- [Hex version requirements](../30-sources/hex-project-2026-packages.md)
  fix the transport profile's operators and pre-release matching.
- [The Hex publishing hypothesis](../00-inbox/package-publishing-hypothesis-hex.md)
  fixes the registry direction this slice profiles.
- [Edition selection](../60-specification/editions-and-feature-lifecycle/edition-selection-and-applicability.md)
  fixes the manifest that gains the dependencies field.
- [SCC admission](../60-specification/module-dependency-cycles/scc-admission-and-resolution.md)
  fixes the component joint digests the lockfile records.
- [Canonicalization](../60-specification/specifications-and-governance/claims-examples-and-checking.md)
  fixes the JCS and SHA-256 machinery identity reuses.

## Findings

- SemVer 2.0.0's sections 9–11 give a complete grammar and precedence —
  including pre-release ordering and build-metadata exclusion — that
  Catena can vendor without modification; the specification defines no
  requirement syntax, so the operator set is a genuine fork.
- Hex's `~>` and its `:allow_pre false` default supply the transport
  profile's conventions; neither Hex nor npm defines caret semantics in
  the pre-1.0 region, so Catena's Cargo-style `^0.1.2`-admits-`0.1.x` rule
  is an explicit recorded choice rather than an inheritance.
- One-version-per-name is not merely a taste: C010 nominal identity is
  `origin::module::name`, so two simultaneously present versions of one
  package would fork every type identity unless origins were versioned —
  machinery nothing supports and no evidence requests.
- The existing manifest decoder already validates strict shapes, and the
  linker already compiles multi-module packages; both extend rather than
  change.
- The synthesis
  [Catena Package Identity and Dependencies](../20-notes/catena-package-identity-and-dependencies.md)
  develops the full model and falsification criteria; the
  [topic map](../10-maps/package-identity-and-dependencies.md) routes the
  evidence.

## Outcome

Open. Resolution requires candidate normative chapters covering
dependencies and versions, resolution and the lockfile, and diagnostics; a
sibling compiler dependency engine with requirement parsing, deterministic
resolution, lockfile generation and replay, and bundle digests, with
tagged executable evidence; and the C013–C024 promotion workflow.
