---
title: "Immutable Retained-Input Language Service"
kind: specification
created: "2026-09-12"
status: normative
spec_version: "0.1.96"
tags: [specification, tooling, diagnostics]
aliases: []
---

# Immutable Retained-Input Language Service

## Status and authority

G123 defines its preparatory language-service core at revision `0.1.96` under
[authority](../../SPECIFICATION-AUTHORITY.md),
[conformance vocabulary](../../CONFORMANCE-VOCABULARY.md), and
[implementation limits](../../IMPLEMENTATION-LIMITS.md). It executes the
[G123 plan](../../20-notes/language-completion-plan-delivery.md#item-123-editor-protocol)
without choosing Catena's public vocabulary or grammar. Public source parsing,
incremental recovery, source-coordinate edits, formatting behavior, and editor
transport remain held for P109, so G123 remains partial (`LS-OBL-001`).

## Snapshots and semantic authority

An admitted document MUST be a retained JSON AST with a nonempty URI, a
nonnegative integer version, and no more than 16,777,216 exact input bytes. A
snapshot MUST retain those bytes, their SHA-256 digest, and the result of the
shared compiler check. The service MUST NOT substitute a separate editor type
checker or treat public source as admitted input at this revision
(`LS-OBL-002`).

A changed document MUST use a version strictly greater than its predecessor.
The resulting snapshot MUST be immutable and MUST retain the predecessor's
exact digest. A request MUST identify its snapshot by exact URI, version, and
digest; any mismatch MUST produce the stale-request outcome before semantic
dispatch (`LS-OBL-003`).

The service MUST retain a syntactically malformed JSON input as a snapshot with
the shared compiler diagnostic when the input is within the byte bound. It MUST
make diagnostics available for that partial input and MUST reject semantic
queries whose checked analysis is unavailable (`LS-OBL-004`).

## Requests, cancellation, and diagnostics

Every request MUST have a nonempty identity and one recognized method. A
cancelled request identity MUST produce a snapshot-bound cancelled result
before method dispatch. One snapshot MUST retain no more than 256 cancelled
request identities; attempting to exceed that bound MUST produce the distinct
language-service-limit outcome (`LS-OBL-005`).

Every successful or cancelled response MUST identify the exact snapshot. Each
diagnostic MUST retain the compiler diagnostic identity, message, path,
severity, URI, snapshot version, and snapshot digest. Its stable identity MUST
be the canonical digest of those fields, so repeated observation of the same
diagnostic on the same snapshot is stable and a changed snapshot cannot
silently reuse that identity (`LS-OBL-006`).

## Semantic operations

The service MUST derive symbols from checked compiler definitions. Each symbol
MUST have a canonical identity derived from module, definition kind, and name,
and MUST retain its visibility, retained-JSON definition path, presented type,
and verified capability uses (`LS-OBL-007`).

Completion MUST expose public exported symbols only. Prefix selection MUST use
valid Unicode text of no more than 256 bytes and MUST preserve the canonical
symbol identity (`LS-OBL-008`).

Hover MUST report the selected symbol's identity, name, kind, visibility,
presented type, and verified uses. Definition navigation MUST report the exact
snapshot URI, retained-JSON path, and symbol identity. Semantic-token results
MUST report symbol identity, retained-JSON path, kind, and visibility, and MUST
state that public-source coordinates remain held for P109 (`LS-OBL-009`).

## Rename previews

A rename request MUST select an existing canonical symbol identity and a name
accepted by the current identifier rules. It MUST reject a collision with
another top-level symbol (`LS-OBL-010`).

Until resolved public-source occurrences exist, the service MUST reject rename
when any checked top-level expression contains a variable occurrence with the
old name. An admitted rename MUST cover only the selected retained-JSON
definition name and matching export entries. It MUST NOT use textual global
replacement or claim unresolved occurrence safety (`LS-OBL-011`).

A rename preview MUST contain normalized machine-applicable JSON edits, the
exact preimage identity, selected symbol identity, old and new names, Base64
encoded exact result bytes, result digest, format and language-service version,
and a canonical digest over the complete plan body. Applying a preview MUST
recompute the expected plan from the selected snapshot and require exact
equality before creating a strictly newer immutable snapshot
(`LS-OBL-012`).

## Limits and variability

One snapshot is limited to 4,096 symbols, one completion prefix to 256 bytes,
one rename plan to 1,024 edits, and one result to 16,777,216 bytes, in addition
to the input and cancellation bounds above. Exceeding any bound MUST produce
the distinct language-service-limit outcome before publishing an oversized
result (`LS-OBL-013`).

This preparatory service has zero variability dispositions. An implementation
MUST NOT substitute ambient editor state, stale results, mutable snapshots,
unbounded queues, textual rename, or an unverified analysis engine and describe
the result as this contract (`LS-OBL-014`).

## Conformance

The conformance profile MUST publish revision, admitted input, public-source
and transport holds, snapshot identity, analysis authority, freshness,
cancellation, diagnostic identity, coordinate space, completion visibility,
rename behavior, formatting hold, method set, and every fixed limit
(`LS-OBL-015`).

An implementation claiming this revision MUST exercise valid and malformed
retained input, immutable changes, stale requests, stable diagnostics,
request-specific cancellation and its bound, exported completion, hover,
definition navigation, semantic tokens, exact rename preview and application,
stale and forged plans, collisions, unresolved occurrences, formatting and
transport holds, lifecycle selection, production compilation, trust-inventory
verification, and its complete regression suite (`LS-OBL-016`).

## Rationale and evidence (non-normative)

The [implementation journal](../../50-journal/2026-09-12-editor-protocol.md)
records twenty-two four-way implementation decisions and compiler
[PR 192](https://github.com/pcharbon70/catena/pull/192). The retained-input
boundary supplies useful editor semantics through the compiler's existing
identities while leaving public productions, recovery, coordinates, formatting,
and transport for joint design at P109.
