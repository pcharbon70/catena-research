---
title: "Checked Migration and Activation"
kind: specification
created: "2026-09-10"
status: normative
spec_version: "0.1.79"
tags: [specification, concurrency, runtime, compatibility]
aliases: []
---

# Checked Migration and Activation

## Status and authority

C092 defines revision `0.1.79` under [authority](../../SPECIFICATION-AUTHORITY.md),
[conformance vocabulary](../../CONFORMANCE-VOCABULARY.md), and
[implementation limits](../../IMPLEMENTATION-LIMITS.md). It completes
[G092](../../20-notes/language-completion-plan-semantics.md#item-092-hot-code-upgrade-g092)
through checked internal descriptors and runtime APIs without selecting public
source vocabulary (`HU-OBL-001`).

## Upgrade descriptor and preflight

An upgrade descriptor binds exact old and new artifact digests, old and new
state-schema identities, the new semantic interface, migration code, evidence
digest, participating node versions, and positive state-byte and execution-time
limits. Missing, malformed, mutable-tag, or mismatched identity is refused
before state changes (`HU-OBL-002`).

The old interface and proposed interface MUST have the same module identity.
The C028 semantic-interface classifier MUST classify the change as identical,
patch, or minor. A breaking interface, incompatible protocol or capability
identity, wrong artifact, or unvalidated evidence is refused (`HU-OBL-003`).

Every coordinated node reports either the exact old or exact new artifact.
Any third version or unreported node is refused. Coordination does not promise
an atomic network-wide instant and does not turn G091 delivery uncertainty into
exactly-once behavior (`HU-OBL-004`).

## Quiescence and coexistence

Migration begins only at an explicit quiescent upgrade point. A live
incompatible capability, unconsumed affine resumption, unsupported active
frame, unfinished owned child, or owned resource blocks the transition. The
implementation reports the blocker and preserves the active generation
(`HU-OBL-005`).

Exactly one generation is active and at most one older generation drains.
While a generation drains, another preflight is refused. Existing closures and
frames retain their generation; they are never rewritten to new code. A third
resident version cannot be admitted by purging live work (`HU-OBL-006`).

Messages arriving during drain are retained in order and delivered only after
successful activation under the checked new boundary. Failure before commit
discards the upgrade attempt, not messages already admitted to the old
generation before quiescence (`HU-OBL-007`).

## Migration and activation

Migration is a declared pure state transformation executed with explicit time
and serialized-state byte limits. Its result MUST validate against the new
state schema before activation. Timeout, trap, malformed result, schema failure,
or size exhaustion aborts activation with a classified failure (`HU-OBL-008`).

The pre-migration state remains an immutable snapshot until activation commits.
Precommit failure restores that snapshot and the old artifact. Migration cannot
perform environmental effects, move capabilities across scopes, serialize
resumptions, or claim to reverse external history (`HU-OBL-009`).

Activation commits the exact new artifact, interface, schema, migrated state,
and immutable evidence, then releases queued messages. No new code is visible
through the upgrade unit before this transition (`HU-OBL-010`).

Postcommit rollback requires a separately declared, bounded, schema-checked
reverse migration and exact reverse artifact identities. In its absence the
runtime refuses rollback. External effects remain historical facts and are
never automatically undone (`HU-OBL-011`).

## OTP realization

The admitted OTP adapter suspends a managed system process, invokes the checked
code-change callback, and resumes it. Failure attempts to resume the old process
and reports the adapter error. Raw module loading, force purge, `.appup`,
`relup`, and release distribution are deployment machinery and cannot bypass
the Catena descriptor or evidence checks (`HU-OBL-012`).

OTP's current/old two-version mechanism witnesses the coexistence ceiling; it
does not define Catena closure meaning. Distributed release handlers act per
node, so Catena performs its version-set preflight before local activation
(`HU-OBL-013`).

## Variability and limits

> **Implementation-defined choice.** The bootstrap accepts positive migration
> limits up to 5,000 milliseconds and 16,777,216 serialized state bytes. The
> machine profile discloses both ceilings. Exhaustion aborts before activation
> and restores the old snapshot (`HU-OBL-014`).

## Diagnostics and conformance

Conformance evidence MUST cover successful migration, quiescence blockers,
wrong artifact and interface identity, mixed unsupported node versions, message
arrival during drain, concurrent-upgrade refusal, migration failure and
exhaustion, precommit restoration, reverse migration, missing reverse
migration, actual OTP suspend/change/resume, lifecycle registration, and trust
inventory classification (`HU-OBL-015`).

## Rationale and evidence (non-normative)

The [implementation journal](../../50-journal/2026-09-10-hot-code-upgrade.md)
records the four-way decisions and executable results. The
[OTP upgrade source note](../../30-sources/erlang-otp-29-code-loading-and-release-handling.md)
documents the two-version code server, process suspension, release workflow,
and per-node coordination that bound the adapter.
