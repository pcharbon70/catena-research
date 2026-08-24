---
title: "Package Publishing Hypothesis: Hex Registry"
kind: note
created: "2026-08-22"
maturity: seed
tags:
  - catena
  - packages
  - tooling
aliases:
  - "Catena Hex hypothesis"
---

# Package Publishing Hypothesis: Hex Registry

> Temporary inbox capture. This is a working assumption for future package
> research, not a decision: it binds no language revision and commits no
> tooling until the owning checklist items are planned.

## Capture

Working hypothesis (2026-08-22, author decision): Catena should adopt the
Hex package ecosystem as its default publishing and dependency-transport
substrate, following the Gleam precedent — a new BEAM language publishing
to hex.pm, consuming Erlang and Elixir packages as dependencies, and riding
the existing registry, version resolution, retirement, checksum, and docs
hosting machinery rather than building a bespoke registry.

## Why this hypothesis

- It directly serves the BEAM-participation goal of the interoperability
  program: existing Erlang/Elixir/OTP libraries become dependencies instead
  of a rebuild burden, before Catena's own standard library exists.
- A bespoke registry adds operational cost and no language-research value;
  Hex already answers parts of the supply-chain questions (yanks/retirement,
  checksums, semver resolution) that G130 would otherwise have to invent.
- Gleam demonstrates the interop path works for a non-Erlang-syntax BEAM
  language, including emitting Hex-format packages from its own build tool.

## What it does not decide

- Hex is transport, not authority. C006's Ed25519-signed assurance
  manifests and C008's exact-revision pins remain Catena-side trust inside
  package tarballs; Hex does not validate them. The G130 supply-chain
  policy must state this boundary explicitly rather than letting registry
  presence imply assurance.
- Hex requires semver package versions; that is the package axis only.
  Language revisions (`0.1.x`), interface versions, and artifact formats
  stay separate version axes under C008.
- Consuming Erlang/Elixir packages needs the foreign-term boundary (G095)
  and foreign-call syntax (G096), which are open; Catena packages consumed
  from Erlang/Elixir need calling conventions (G094). Registry access
  without those boundaries yields dependencies the language cannot call.
- The package manifest shape (a `catena.toml`-style file or extension of
  existing formats), directory layout, and build-tool behavior remain G025
  and G121 design work shaped toward Hex-compatible output.

## Owners

- G025 package identity, manifests, dependency resolution, lockfiles
- G028 API/ABI compatibility policy
- G094/G095/G096 calling conventions and foreign-term entry
- G121 build system and package manager
- G130 supply-chain policy

## Promotion path

**Executed.** C025 (`0.1.21`) adopted this hypothesis as the normative
transport profile: bundle digests must equal the registry tarball
checksum at install, and identity itself stays registry-neutral. See the
[package specification](../60-specification/package-identity-and-dependencies/README.md)
and the
[C025 evidence record](../50-journal/2026-08-24-c025-package-identity.md).
Remaining owners: G121 (fetch/publish tooling), G130 (signing and
threat model), G094–G096 (cross-language calls). This note may be
archived once those slices land.

## Connections

- [Remaining Catena Research Areas](remaining-catena-research-areas.md)
  names the package program and its G025/G121/G130 owners.
- [Language-Integrated Specifications and Governance](../20-notes/language-integrated-specifications-and-governance.md)
  defines the signed-artifact authority that must remain distinct from
  registry trust.
- [Language Editions and Feature Lifecycle](../20-notes/language-editions-and-feature-lifecycle.md)
  fixes the version-axis separation Hex's semver must not disturb.
