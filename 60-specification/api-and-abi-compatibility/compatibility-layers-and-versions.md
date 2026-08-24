---
title: "Compatibility Layers and Versions"
kind: specification
created: "2026-08-24"
status: normative
spec_version: "0.1.24"
tags:
  - compatibility
  - specification
  - api
aliases:
  - "Catena compatibility layers"
---

# Compatibility Layers and Versions

## Status and authority

This chapter is the normative Catena 0.1.24 compatibility-layer and
version-meaning contract. It is governed by
[Specification Authority](../../SPECIFICATION-AUTHORITY.md),
[Catena Conformance Vocabulary](../../CONFORMANCE-VOCABULARY.md), and
[Catena Implementation Limits and Portability](../../IMPLEMENTATION-LIMITS.md).
It extends, without amending, the change classification of
[Feature Lifecycle and Compatibility](../editions-and-feature-lifecycle/feature-lifecycle-and-compatibility.md),
the interfaces of
[Interfaces and Representation](../data-and-patterns/interfaces-and-representation.md),
and the version machinery of
[Manifest Dependencies and Versions](../package-identity-and-dependencies/manifest-dependencies-and-versions.md).

The rules apply only to source-language revision `0.1.24`. They do not
reinterpret retained manifests, interfaces, artifacts, or signed formats.

## The four layers

Compatibility is layered; each layer has exactly one stance
(`CP-OBL-002`):

> **Normative definition.**

| Layer | Stance |
| --- | --- |
| Source | Real rules: retained revisions are immutable |
| Type/interface | Real rules: the strict diff matrix |
| Behavior | Declared absence: the kernel is the contract |
| BEAM ABI | Declared absence: representation is not a surface |

**Source.** A retained language revision is immutable: a source file
that checked under an exact revision keeps checking under that exact
revision, byte for byte (`CP-OBL-003`). Acceptance is cumulative
forward — each revision adds acceptance and never removes it, per
C008's registered classification. A package upgrade that selects a new
revision rechecks under that revision's rules; nothing in this chapter
migrates source, which remains G116/P121 tooling.

**Type/interface.** A consumer validates against a producer's later
interface if and only if no breaking change defined by
[Breaking Change Matrix](breaking-change-matrix.md) occurred
(`CP-OBL-004`). Interfaces are the only cross-package contract this
chapter recognizes; source text, build outputs, and diagnostics of the
producer are not.

**Behavior (declared absence).** The deterministic kernel of
[Canonical Kernel Syntax](../formal-semantic-kernel/canonical-kernel-syntax.md)
and [Sequential Dynamics](../formal-semantic-kernel/sequential-dynamics.md)
*is* the behavior contract. There is no separate
behavioral-compatibility promise, no observational equivalence claim
across producer versions, and no bug compatibility: a corrected kernel
rule applies from its introducing revision, and a change to dynamic
behavior is classified by C008's registry, not excused here
(`CP-OBL-010`). Implementations MUST NOT use this chapter to claim
behavioral guarantees the kernel does not already fix.

**BEAM ABI (declared absence).** No stable BEAM ABI, wire, or
serialization contract exists at 0.1.24 (`CP-OBL-010`). Compiled
companion binaries are deterministic outputs of a compiler build; they
are not compatibility surfaces, and loading them on any other build or
release is outside every Catena guarantee, exactly as
[Authority and Representation Exclusions](../abstraction-boundaries/authority-and-representation-exclusions.md)
fixed for representation. A representation or layout change therefore
never requires a version increment by itself. Any future
layout-stability or calling-convention contract belongs to P093, G094,
G095, and G092 through an explicit later revision; until such an owner
delivers, every appearance of a stable-ABI promise in any frontend is
invalid input, not a semantics.

## Version-increment meanings

Version numbers use the SemVer 2.0.0 grammar and precedence C025
fixed; this chapter fixes what increments *mean* (`CP-OBL-005`):

> **Normative definition.**

- **1.0.0 and above:** a breaking interface change under the matrix
  MUST increment the major version; additive-only changes increment
  minor; corrections with no interface content change increment patch.
- **Below 1.0.0 (the 0.x convention):** a breaking interface change
  MUST increment the minor version; additive-only changes increment
  patch. This is the Cargo-style rule C025 already fixed for the
  caret and tilde operators; this chapter fixes its meaning side.
- **Editions:** a language-level breaking change travels as a new
  edition (0.1 → 0.2) through the C008 lifecycle record that names the
  change, migration, and retirement — never as a revision within an
  edition. Edition mechanics remain C008's.

A claimed increment below the required class is `CMP001` under
[Diagnostics and Conformance](diagnostics-and-conformance.md). The
1.0-era switch of the 0.x convention is itself an edition-record
decision reserved to the G136 era; no revision within edition 0.1
changes it.

## What versions do not carry

Digest values — bundle digests, joint component digests, interface
digests — are identity and cache keys, never compatibility classes: a
digest change says content differs, not that anything broke. Build
metadata, compile timestamps the compiler does not emit, and artifact
byte differences caused by toolchain version are not compatibility
facts. Diagnostics may improve within bounded presentation; a new
warning is never a breaking change, matching C008's classification.

## Deliberately separate work

Migration engines and conservative source edits remain G116/P125.
Registry retirement, yanks, compromised-version policy, and
dependency graphs spanning editions remain G130. Hot upgrade remains
G092. Representation, calling-convention, and foreign-term contracts
remain P093/G094/G095. Tooling automation of claim validation remains
G121. The G136 edition policy owns the 1.0-era conventions.

## Rationale and evidence (non-normative)

The [compatibility synthesis](../../20-notes/catena-api-and-abi-compatibility.md)
records why layered stances were selected over uniform promises, and
the [OTP strategy analysis](../../30-sources/erlang-otp-compatibility-and-upgrading.md)
shows the target runtime itself tiers its surfaces and declines
bug-compatibility. The [resolved
inquiry](../../40-inquiries/how-should-catena-define-api-and-abi-compatibility.md)
and [topic map](../../10-maps/api-and-abi-compatibility.md) preserve
the decision route.
