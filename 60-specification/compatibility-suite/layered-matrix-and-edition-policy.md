---
title: "Layered Matrix and Edition Policy"
kind: specification
created: "2026-09-10"
status: normative
spec_version: "0.1.82"
tags: [specification, compatibility, conformance, testing]
aliases: []
---

# Layered Matrix and Edition Policy

## Status and authority

C136 defines revision `0.1.82` under [authority](../../SPECIFICATION-AUTHORITY.md),
[conformance vocabulary](../../CONFORMANCE-VOCABULARY.md), and
[implementation limits](../../IMPLEMENTATION-LIMITS.md). It completes the
[P136 plan](../../20-notes/language-completion-plan-delivery.md#item-136-compatibility-suite)
by composing C008 editions, C025 dependency locks, C028 compatibility layers,
C092 checked upgrades, C099 toolchain profiles, C116 historical migration, C121
builds, and C128 reproducible artifacts. It introduces no public language
vocabulary (`CS-OBL-001`).

## Matrix identity and scope

A compatibility matrix binds an exact format revision, a nonempty human-readable
scope, a finite ordered set of cases, and a canonical digest over those fields.
Every case has a unique stable identifier, one layer, one expected observation,
and a canonical input object (`CS-OBL-002`).

The layers are `source`, `interface`, `dependency`, `data`, `toolchain`,
`historical-signature`, and `runtime-upgrade`. A matrix cannot combine them into
one undifferentiated compatibility verdict (`CS-OBL-003`).

A report binds the source matrix digest and repeats its scope. It records the
case digest, expectation, observed class, outcome, and evidence for every case;
its own canonical digest covers the complete report (`CS-OBL-004`).

## Observations and outcomes

Each layer-specific oracle observes `compatible`, `incompatible`, or
`unsupported`. An expected compatible or incompatible observation is `pass`; a
contradicting supported observation is `fail`. `unsupported` remains distinct
regardless of expectation and cannot be relabelled as either success or
regression (`CS-OBL-005`).

An unavailable adapter yields `unsupported`. A malformed adapter result or
invalid matrix yields explicit refusal rather than an omitted row or inferred
success (`CS-OBL-006`).

## Layer authorities

Source cases use exact edition and language-revision selection. The suite tests
the earliest retained selection, the current selection, invalid selections, and
future editions without treating acceptance by a newer frontend as proof of
unchanged meaning (`CS-OBL-007`).

Interface cases use decoded semantic interfaces and C028's change classifier.
They distinguish source acceptance, semantic interface compatibility, artifact
rebuild, and runtime replacement. Byte inequality alone is not a breaking change
and byte equality alone is not a semantic proof (`CS-OBL-008`).

Dependency cases resolve complete graphs and replay exact lock records with
content verification. They cover diamonds plus explicit wide and deep graph
bounds; malformed locks, missing nodes, cycles, and digest mismatches refuse the
case (`CS-OBL-009`).

Data cases dispatch exact historical artifact interpreters or declared adjacent
migrations. Historical source bytes and signatures remain immutable; derived
artifacts have separate identity and cannot rewrite old signatures
(`CS-OBL-010`).

Toolchain cases use published exact host fingerprints and required facilities.
The oldest and newest supported rows are explicit even when one retained
fingerprint currently occupies both positions. An unlisted host is
`unsupported`, and an artifact for a different fingerprint requires a rebuild
from retained source (`CS-OBL-011`).

Historical-signature cases verify the original canonical signing domain with the
applicable historical trust material. Successful cryptographic verification
authenticates bytes and does not establish semantic compatibility
(`CS-OBL-012`).

Runtime-upgrade cases use C092 preflight, quiescence, migration, activation, and
rollback rules. Source or interface compatibility cannot substitute for a
successful admitted upgrade path (`CS-OBL-013`).

## Coverage and edition policy

The suite combines curated retained applications with generated dependency
families. Generated cases preserve explicit seeds or construction parameters,
and failures retain the smallest available reproducible counterexample
(`CS-OBL-014`).

A compatible language revision or edition claim requires every matrix row named
by that claim to pass. Unsupported or omitted rows remain disclosed limitations.
Revision `0.1.82` retains edition `0.1`; it does not select a future `1.0`
versioning convention (`CS-OBL-015`).

Finite fixtures establish compatibility only for their published matrix scope.
A project cannot infer ecosystem-wide, future-host, or unbounded-graph
compatibility from a passing bounded report (`CS-OBL-016`).

## Variability and limits

> **Implementation-defined choice.** An implementation publishes maximum case
> count and encoded bytes per case, the exact retained matrix rows, supported
> toolchain fingerprints, graph width and depth, and available upgrade adapters.
> Exhaustion or absent coverage produces explicit refusal or `unsupported`
> without deleting other case results (`CS-OBL-017`).

## Diagnostics and conformance

Tests MUST cover deterministic matrix and report digests; duplicate, malformed,
oversized, and tampered cases; expectation mismatches; missing adapters; pass,
fail, and unsupported outcomes; oldest and current source selections; interface
additions and breaking changes; wide and deep exact lock replay; historical data
and signatures; oldest and newest supported host rows; admitted and refused hot
upgrades; lifecycle registration; conformance reporting; and trust
classification (`CS-OBL-018`).

## Rationale and evidence (non-normative)

The [implementation journal](../../50-journal/2026-09-10-compatibility-suite.md)
records the planned forks, additional four-way decisions, and executable results.
The [API compatibility map](../../10-maps/api-and-abi-compatibility.md) connects
this evidence layer to semantic versions, editions, package identity, historical
artifacts, toolchains, and upgrades. The bounded claim follows the archive's
[Erlang/OTP compatibility evidence](../../30-sources/erlang-otp-compatibility-and-upgrading.md)
rather than extrapolating beyond tested hosts.
