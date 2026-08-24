---
title: "Breaking Change Matrix"
kind: specification
created: "2026-08-24"
status: normative
spec_version: "0.1.24"
tags:
  - compatibility
  - specification
  - api
aliases:
  - "Catena breaking change matrix"
---

# Breaking Change Matrix

## Status and authority

This chapter is the normative Catena 0.1.24 breaking-change matrix. It
is governed by
[Specification Authority](../../SPECIFICATION-AUTHORITY.md),
[Catena Conformance Vocabulary](../../CONFORMANCE-VOCABULARY.md), and
[Catena Implementation Limits and Portability](../../IMPLEMENTATION-LIMITS.md).
It applies the layer stances of
[Compatibility Layers and Versions](compatibility-layers-and-versions.md)
over the interface content of
[Interfaces and Representation](../data-and-patterns/interfaces-and-representation.md),
the entry declarations of
[Entry Declarations](../entry-points/entry-declarations.md), and the
package machinery of
[Resolution and Lockfile](../package-identity-and-dependencies/resolution-and-lockfile.md).

The rules apply only to source-language revision `0.1.24`. They do not
reinterpret retained manifests, interfaces, artifacts, or signed formats.

## The matrix

Compatibility between a producer's earlier and later decoded semantic
interfaces is decided by the complete ordered diff of interface
content (`CP-OBL-004`):

> **Normative definition.**

| # | Change | Class |
| --- | --- | --- |
| 1 | Remove an export | breaking |
| 2 | Rename an export (remove plus add) | breaking |
| 3 | Change an export's type scheme, including its quantifier list | breaking |
| 4 | Widen an export's recorded effect row — new requests | breaking |
| 5 | Narrow an export's recorded effect row | minor |
| 6 | Add an export | minor |
| 7 | Remove, rename, or change the kind/arity of a datatype constructor | breaking |
| 8 | Add a datatype constructor | minor |
| 9 | Change a datatype's nominal identity, visibility, or transparency mode | breaking |
| 10 | Remove or change a trait, handler, or instance signature | breaking |
| 11 | Add a trait, handler, or instance | minor |
| 12 | Change a representation or layout of any type | never breaking alone |
| 13 | Add an entry | minor |
| 14 | Remove an entry or change its declared result | breaking |
| 15 | Change the launch marker between entries | minor |

A diff is classified **breaking** when any row of class breaking
occurs; otherwise **minor** when any minor row occurs; otherwise
**patch** when the interfaces differ without any matrix row matching;
otherwise **identical**. Drift a conforming classifier cannot assign —
unknown or malformed interface content — is `CMP003`, never a guess
(`CP-OBL-006`).

Names compare by their full interface identity: an export by name, a
datatype by its nominal `origin::module::name` identity, constructors
by their declaring datatype and name. Effect rows compare by their
recorded entries under C005's row equality: widening means the later
row contains every earlier request and at least one more.

## Deferral resolutions

This section closes the deferrals six shipped slices left here
(`CP-OBL-007`):

- **Re-export facades (from C022, re-owned by C025):** a facade
  mechanism is **formally excluded**. An ordinary forwarding definition
  — a function whose body applies another module's export — is already
  expressible and transparent, and is itself classified under the
  matrix like any export. Any identity-preserving facade — a rule
  admitting another package's exports under a local qualifier without a
  forwarding definition — would contradict C002's transparency modes
  and C021's `NSP004` collision model and MUST NOT exist at this
  revision; if a future edition admits one, it does so through a C008
  lifecycle record that names its identity semantics.
- **Joint component digests (from C024):** a joint digest is identity
  for cache and signature domains, never a compatibility class. A
  component whose joint digest changed is rebuilt and rechecked; the
  compatibility verdict comes from the matrix over its members'
  interfaces alone.
- **Version skew (from C025):** consumers observe one resolved version
  per package name, pinned and replayed by `catena.lock` exactly as
  C025 fixed. Skew between builds is resolved by replaying the lock,
  not by compatibility rules; this chapter adds no coexistence
  semantics.
- **Prelude bumps (from C026):** a prelude selection's version bump is
  an ordinary dependency bump. Its compatibility class is the matrix
  applied between the old and new prelude package interfaces; the
  manifest's `prelude` requirement changes are themselves additive
  metadata.
- **Entry sets (from C027):** rows 13–15. An entry addition is
  minor-compatible; an entry removal or result-type change is
  breaking. The launch marker is metadata and its movement is minor.

## Claim validation

A **version claim** is the (old version, new version) pair a producer
asserts for an interface change (`CP-OBL-005`). Validation compares
the claim's allowance under
[Compatibility Layers and Versions](compatibility-layers-and-versions.md)
with the matrix classification: a breaking diff claimed as minor or
patch, or a minor diff claimed as patch, is `CMP001`. A claim at or
above the required class is valid — over-signaling (claiming major for
an additive change) is permitted and unclassified. Validation consumes
decoded interfaces and claimed versions only; it never parses source
and never claims behavior (`CP-OBL-010`).

## Deliberately separate work

Behavioral equivalence and performance are outside the matrix. Data
evolution and serialization are outside until P093/G095 deliver
contracts. Migration edits remain G116/P125. Registry retirement and
yanks remain G130. Tooling automation remains G121.

## Rationale and evidence (non-normative)

The [compatibility synthesis](../../20-notes/catena-api-and-abi-compatibility.md)
records why effect-row widening is breaking (a consumer that handles
nothing cannot type-check against new requests), why additions are
minor, and why the facade exclusion closes the C022/C025 deferral. The
[topic map](../../10-maps/api-and-abi-compatibility.md) routes the
decision.
