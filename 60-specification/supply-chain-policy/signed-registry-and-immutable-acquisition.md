---
title: "Signed Registry and Immutable Acquisition"
kind: specification
created: "2026-09-10"
status: normative
spec_version: "0.1.74"
tags: [specification, conformance, security, supply-chain-security]
aliases: []
---

# Signed Registry and Immutable Acquisition

## Status and authority

C130 defines revision `0.1.74` under [authority](../../SPECIFICATION-AUTHORITY.md),
[conformance vocabulary](../../CONFORMANCE-VOCABULARY.md), and
[implementation limits](../../IMPLEMENTATION-LIMITS.md). It executes the
[reviewed supply-chain plan](../../20-notes/language-completion-plan-delivery.md#item-130-supply-chain-policy).
The protocol authenticates registry state and exact package bytes. It does not
prove source semantics, native safety, publisher honesty, mirror availability,
or correctness of the trusted host (`RG-OBL-001`).

This is a separate package protocol. It introduces no public language vocabulary,
source frontend, interface version, or assurance-manifest version. Registry
signatures do not satisfy C006 governance policies, and governance signatures do
not become registry authority. C025 owns package identity and dependency
resolution; C127 owns trusted obligations; C128 owns reproducible builds.

## Trust roots and rotation

A client begins from an out-of-band canonical root. The root contains an exact
format and version, positive sequence, expiry in Unix seconds, Ed25519 public keys,
root/snapshot/recovery roles, and package-scoped publisher delegations. Every key
identifier is the lowercase SHA-256 digest of its lowercase hexadecimal public
key. Principals are sorted, unique, present in the key map, and paired with a
positive threshold no greater than the role size. Unknown fields, noncanonical
bytes, malformed keys, duplicate delegations, and expired roots are invalid
(`RG-OBL-002`).

Signing uses canonical JSON prefixed by the exact domain
`catena:registry:<kind>:1` and a newline, where `<kind>` is `root`, `snapshot`, or
`release`. Duplicate signatures from one principal count once. A normal root
rotation increments sequence by exactly one, binds the prior root digest, and
meets both the old and new root thresholds. Recovery increments and binds the
same fields but meets the old root's separately declared recovery threshold.
Self-signing alone, a stale prior digest, skipped sequence, expired successor, or
forged loaded-root digest is refused (`RG-OBL-003`).

## Signed snapshots and history

A snapshot envelope contains exact format/version, a canonical signed snapshot,
and registry signatures. The snapshot binds a positive monotonic sequence, exact
root sequence, Unix expiry, and a complete sorted unique release list. Its
snapshot-role threshold MUST verify. Opening records the exact envelope,
observation time, snapshot digest, and decoded state; every later use reopens and
compares that complete record before trusting it (`RG-OBL-004`).

Opening a later snapshot against prior state MUST reject a lower sequence and a
different body at the same sequence. Every previously observed package/version
identity remains present with the identical artifact. Its status sequence never
decreases and increases when status changes. Once observed as `compromised`, that
identity remains `compromised`. A status sequence cannot exceed its containing
snapshot sequence (`RG-OBL-005`).

## Publisher authority and immutable releases

Each release contains an immutable artifact, publisher signatures, one status,
and a positive status sequence. The artifact binds package and semantic version,
kind, byte size, SHA-256 content digest, C025 bundle digest, and provenance.
Signatures over the artifact MUST meet the exact package delegation threshold.
The registry snapshot separately authenticates `active`, `yanked`, or
`compromised` status. Thus a publisher cannot change availability and a registry
cannot replace signed content under an existing identity (`RG-OBL-006`).

Source provenance binds the C025 dependency requirements, exact edition/revision/
preview selection, module/interface/root/output paths, interface/component
digests, and C128 reproducible-input digest. The artifact bundle digest MUST equal
C025's digest of those semantic fields. Requirements and versions MUST parse under
C025. Registry acquisition does not waive later source checking or reproducible
envelope verification (`RG-OBL-007`).

Native provenance binds exact content as the native-package digest, target
platform, supported toolchain digest, reproducible-input digest, and sorted unsafe
obligations. Acquisition MUST match platform and toolchain and acknowledge every
obligation. These checks preserve C098 and C127 admission; authentic native bytes
remain trusted code capable of VM failure (`RG-OBL-008`).

## Acquisition, mirrors, and status

For new acquisition, the caller supplies an observation time no earlier than the
snapshot's verified time. Both root and snapshot MUST remain unexpired at that
time, and the release MUST be `active`. Missing time, future use of expired
metadata, yanked content, compromised content, unknown identity, and unsupported
options are refused before a successful result (`RG-OBL-009`).

Mirrors supply bytes without authority. The client examines at most the declared
mirror ceiling and accepts the first copy whose size and SHA-256 digest exactly
match the signed artifact. A transport name, order, cache path, or version label
cannot redefine content. No matching copy yields explicit acquisition refusal and
no partial package result (`RG-OBL-010`).

Active source releases form the only environment for new C025 resolution. Exact
C025 lock replay can address active, yanked, or compromised metadata, but content
is returned only for active or yanked status. The replay check binds package,
version, C025 bundle digest, and the exact verified snapshot digest. It then
re-verifies mirror bytes. A changed lock field, replacement byte, or compromised
status fails the entire replay (`RG-OBL-011`).

## Offline and compromise semantics

Offline replay uses a previously verified persisted client, exact lock, and local
mirror bytes. It deliberately makes no current-freshness claim. Expired metadata
can reproduce the frozen decision because every client field is reverified and no
new dependency choice is made. A later yank does not erase a historically locked
identity. If the verified snapshot used for replay marks an identity compromised,
the client MUST deny it even when exact locked bytes remain available
(`RG-OBL-012`).

An offline client cannot know a status published after its frozen snapshot.
Deployment policy owns refresh requirements and emergency distribution of new
roots or compromise metadata. This residual does not authorize an online client
to ignore observed compromise or to revert a terminal compromised history.

## Limits, refusal, and host trust

The protocol admits at most 32 keys, 256 delegations, 4,096 releases, 32 signatures
per signature list, eight mirrors, 16 MiB of snapshot metadata, and 64 MiB per
artifact. Root metadata is capped at 1 MiB. Sequences and expiry values lie in the
canonical safe-integer range. Package/platform strings and every nested list or map
must satisfy its exact shape. Excess, malformed metadata, failed signatures,
unavailable content, and incompatible native provenance produce refusal without
truncation or a partial success (`RG-OBL-013`).

The machine-readable compiler profile publishes these ceilings and the offline,
yanked, and compromised dispositions. Root delivery, observation-clock integrity,
private-key custody, cryptographic provider correctness, mirror availability,
local storage, and the execution of admitted native code remain host trust. Every
registry outcome has the meaning fixed here; silent byte replacement is forbidden
(`RG-OBL-014`).

## Rationale and evidence (non-normative)

The [implementation journal](../../50-journal/2026-09-10-signed-package-registry.md)
records sixteen four-way decisions and the local attack fixtures. The
[TUF source note](../../30-sources/the-update-framework-specification.md) supports
separated roles, threshold keys, delegation, rollback resistance, and
dual-authority root rotation. Catena adapts those principles to its own canonical
documents and existing C025/C127/C128 boundaries; this chapter does not claim TUF
protocol compatibility.
