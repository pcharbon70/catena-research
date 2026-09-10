---
title: "Transactional Retained-JSON Edits"
kind: specification
created: "2026-09-10"
status: normative
spec_version: "0.1.93"
tags: [specification, migration, tooling, diagnostics]
aliases: []
---

# Transactional Retained-JSON Edits

## Status and authority

P125 defines its retained-input migration tool at revision `0.1.93` under
[authority](../../SPECIFICATION-AUTHORITY.md),
[conformance vocabulary](../../CONFORMANCE-VOCABULARY.md), and
[implementation limits](../../IMPLEMENTATION-LIMITS.md). It executes the
[P125 plan](../../20-notes/language-completion-plan-delivery.md#item-125-migration-tools)
over C008 and P117 `json-edit` repairs while preserving the C008 compiler's
report-only behavior. Public-source, API, and deprecated-syntax rewrites remain
held for P109, so P125 remains partial (`MT-OBL-001`).

## Plans and exact previews

The compiler MUST continue to report migration suggestions without applying
them. A separate migration action MUST consume an explicit nonempty request and
MUST accept only `json-edit` records whose applicability is
`machine-applicable` and whose operation is `add`, `replace`, or `remove`
(`MT-OBL-002`).

Every planned file MUST identify a regular file beneath one exact root, its
document kind, normalized edits, exact preimage and proposed result, and a
SHA-256 digest for each byte sequence. Plans MUST have a canonical digest over
their complete unsigned content. Duplicate paths, duplicate edits, ancestor
and descendant edit overlap, unsupported paths, malformed plans, and altered
plan content MUST be rejected before mutation (`MT-OBL-003`).

A preview MUST reproduce the plan's exact preimage bytes, proposed result
bytes, digests, paths, and edits. Previewing MUST NOT authorize or mutate a
file. Application MUST require a separate explicit authorization for that
exact verified plan (`MT-OBL-004`).

## Filesystem transaction and rollback

The root and every source path MUST be revalidated at application time. An
absolute path, parent traversal, path outside the root, nonregular source,
source symlink, or symlinked backup base MUST be rejected without changing an
input (`MT-OBL-005`).

Before replacing any input, the tool MUST validate every current preimage
against both its recorded bytes and digest, verify every proposed result, copy
every preimage to a retained plan-specific backup, and stage every result in
the destination filesystem. A stale preimage or staging failure MUST leave all
input paths unchanged (`MT-OBL-006`).

The commit phase MUST replace only the files in the authorized plan. If any
replacement fails or the transaction is interrupted, the tool MUST attempt to
restore every input already entered into the commit phase from its exact local
rollback copy. A successful rollback MUST report the initiating commit or
interruption outcome; an incomplete rollback MUST report a distinct rollback
failure and identify each affected path (`MT-OBL-007`).

Successful application MUST retain the immutable preimage backups. A repeated
application with an occupied backup identity MUST be rejected rather than
overwriting earlier evidence (`MT-OBL-008`).

## Semantic checks and authority

A retained module result MUST pass the selected Catena checker, and its
verified public interface digest MUST equal the preimage interface digest. A
retained package-manifest result MUST pass manifest decoding, and its language
selection MUST equal the preimage language selection. A rejected result or
unresolved behavioral change MUST leave every input unchanged
(`MT-OBL-009`).

Migration creates new bytes and new evidence. It MUST NOT copy, regenerate,
or imply a governance approval, signature, compatibility decision, or proof
for the result. Such authority requires its normal independent procedure
(`MT-OBL-010`).

A successful audit MUST bind the plan digest, status, each path, preimage and
result digests, retained backup path, verification result, and the explicit
fact that governance approval was not inherited. The audit MUST carry a
canonical digest over all preceding fields (`MT-OBL-011`).

## Variability and limits

One plan is limited to 32 files, 16,777,216 aggregate decoded preimage octets,
16,777,216 aggregate decoded result octets, and 1,024 edits. The same bounds
MUST be checked when a plan is created and when a supplied plan is verified.
Exhaustion MUST produce the distinct `migration-limit-exceeded` implementation
limit outcome and MUST NOT mutate an input (`MT-OBL-012`).

This retained-input profile has zero variability dispositions
(`MT-OBL-013`).

## Diagnostics and conformance

The conformance profile MUST publish revision, retained input kind, edit kind,
applicability, authorization, preview, transaction, backup, rollback,
verification, governance-inheritance, public-source status, and every finite
limit (`MT-OBL-014`).

An implementation claiming this P125 slice MUST exercise a successful module
migration and manifest migration; exact preview and backup bytes; explicit
authorization; stale, ambiguous, overlapping, unsupported, malformed,
semantically rejected, and behavior-changing requests; path escape and
symlink refusal; interrupted multi-file rollback; failure after moving an
original; distinct rollback failure; plan tampering; limit exhaustion;
lifecycle selection; production compilation; trust inventory; and the complete
suite (`MT-OBL-015`).

P125 MUST remain partial until P109 supplies the public parser and identity
needed for source rewrites, API refactors, and deprecated-syntax handling.
Retained JSON paths and edit operations are tooling protocol and MUST NOT
establish Catena's public vocabulary or grammar (`MT-OBL-016`).

## Rationale and evidence (non-normative)

The [implementation journal](../../50-journal/2026-09-10-migration-tool.md)
records twenty four-way decisions and compiler PRs 183–185. Exact byte
identity, verification before mutation, and conservative authority boundaries
make the migration reviewable while the held grammar remains untouched.
