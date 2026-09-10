---
title: "Historical Replay and Migration"
kind: specification
created: "2026-09-10"
status: normative
spec_version: "0.1.80"
tags: [specification, governance, compatibility, artifacts]
aliases: []
---

# Historical Replay and Migration

## Status and authority

C116 defines revision `0.1.80` under [authority](../../SPECIFICATION-AUTHORITY.md),
[conformance vocabulary](../../CONFORMANCE-VOCABULARY.md), and
[implementation limits](../../IMPLEMENTATION-LIMITS.md). It completes the
[P116 plan](../../20-notes/language-completion-plan-delivery.md#item-116-long-term-evolution)
without changing public vocabulary (`LE-OBL-001`).

## Interpretation ledger

Every supported historical artifact format maps to one exact-version
interpreter. The bootstrap supports governance-era formats `0.1.6`, `0.1.7`,
and `0.1.8`. Replay dispatches by the recorded format, never by the latest
decoder, filename, timestamp, or mutable release tag (`LE-OBL-002`).

An unknown future or retired-unarchived format is refused as unsupported. A
new compiler cannot infer the meaning of an unknown format (`LE-OBL-003`).

Historical replay uses the trust-root state, policy interpreter, tool identity,
dependencies, and decision context applicable to the original record. A root
revoked for new actions can remain valid historical evidence only through an
archived historical-root record (`LE-OBL-004`).

Missing interpreters, tools, dependencies, or historical roots produce distinct
nonportable-evidence outcomes. They do not silently convert denial to allowance
or make an unverifiable decision current (`LE-OBL-005`).

## Adjacent migration

Schema migration is a deterministic chain of adjacent supported versions. Each
hop validates its exact input and output versions and records the ordered path.
A missing or malformed hop refuses the whole migration (`LE-OBL-006`).

A migration reporting semantic loss is refused. Loss cannot be hidden by a
default, warning, or higher version number. A transformation that requires a
policy choice must become a separately governed derived action (`LE-OBL-007`).

The original bytes are embedded unchanged in the derived envelope with their
SHA-256 digest and source version. Original signatures remain historical data;
the migration MUST NOT rewrite or represent them as signatures over the new
document (`LE-OBL-008`).

The derived envelope records its format, target version, source version,
source digest, exact source bytes, ordered migration path, and migrated
document. Canonical encoding is deterministic (`LE-OBL-009`).

Verification recomputes the source digest and decodes the retained source to
confirm its version. Tampering with bytes, digest, source version, or envelope
shape is refused (`LE-OBL-010`).

## Archive portability

A replayable archive contains source artifacts, exact format and tool
identities, dependencies, historical trust-root records, policy inputs, and
decisions. Source alone, BEAM alone, or dependence on a mutable live registry
does not establish replayability (`LE-OBL-011`).

Migration creates new derived evidence and never modifies the historical
record. Normal governance and signatures apply if the derived artifact is used
for a new build, publication, or activation decision (`LE-OBL-012`).

## Variability and limits

> **Implementation-defined choice.** An implementation publishes its supported
> historical format ledger and archive requirements. Support can expand only
> with exact interpreters and adjacent migrations; absence is reported rather
> than guessed (`LE-OBL-013`).

## Diagnostics and conformance

Tests MUST cover every supported exact interpreter, deterministic multi-hop
migration, immutable original bytes and signatures, path recording, unknown
versions, semantic loss, missing hops, revoked roots with and without historical
records, missing tools and dependencies, derived-envelope tampering, lifecycle
registration, and trust classification (`LE-OBL-014`).

## Rationale and evidence (non-normative)

The [implementation journal](../../50-journal/2026-09-10-long-term-evolution.md)
records the four-way decisions and executable evidence. C006 governance identity,
C008 lifecycle selection, C114 artifact formats, and C115 historical trust-root
replay supply the retained foundations.
