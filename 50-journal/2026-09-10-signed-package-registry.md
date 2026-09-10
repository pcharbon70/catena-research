---
title: "2026-09-10 Signed Package Registry"
kind: journal
created: "2026-09-10"
tags: [specification, conformance, security, supply-chain-security]
aliases: []
---

# 2026-09-10 Signed Package Registry

## Scope

Execute [P130](../20-notes/language-completion-plan-delivery.md#item-130-supply-chain-policy)
from compiler C128 merge `e872a922ef12a6a25e61dc71673bc9c9efc4bc7c`.
Revision 0.1.74 is covered by the user's session-wide approval. Compiler PR
[156](https://github.com/pcharbon70/catena/pull/156) merged as
`e3a2e98bc5949511ec4aadd6e7dc6094a2a3cb33` into `rewrite`.

## Implementation decisions

CP-130-1..3 retain their recommendations. Each implementation fork below
compares four alternatives and selects the recommendation.

| Decision | Four alternatives | Recommended and selected |
| --- | --- | --- |
| RG-I01 Trust bootstrap | A TLS identity; B canonical out-of-band root with exact keys/roles; C package names; D governance approval | B: registry trust begins from an explicit independent root. |
| RG-I02 Root rotation | A new root self-signs; B old-plus-new thresholds with recovery role; C replace on expiry; D mirror majority | B: normal continuity requires both authorities; declared recovery handles compromised old root. |
| RG-I03 Repository state | A unsigned listing; B threshold-signed complete snapshots with sequence and expiry; C per-mirror state; D filesystem mtime | B: clients can detect stale or equivocal metadata. |
| RG-I04 Publisher authority | A any root key; B package-scoped delegated publisher threshold; C TLS certificate; D governance signer | B: publisher authority is narrow and distinct from registry and language governance. |
| RG-I05 Release identity | A mutable version URL; B immutable content/bundle/provenance tuple; C package and version only; D latest tag | B: a version cannot silently change bytes or semantic identity. |
| RG-I06 Status | A delete yanks; B registry-signed active/yanked/compromised state with monotonic compromise; C publisher-only status; D ignore compromise | B: availability and identity remain separate, and compromise cannot be undone by a later snapshot. |
| RG-I07 Yank replay | A deny all old builds; B admit only an exact snapshot-bound lock; C admit by version string; D silently fetch replacement | B: historical replay survives a yank without widening new acquisition. |
| RG-I08 Compromise | A allow exact locks; B deny every acquisition and replay; C warn only; D delete metadata | B: known compromised content never re-enters through offline history. |
| RG-I09 Mirrors | A first mirror wins; B accept the first size-and-digest exact copy; C quorum bytes; D trust transport | B: mirrors are availability sources and cannot redefine identity. |
| RG-I10 Offline mode | A ignore all metadata; B replay a previously verified snapshot with its exact digest-bound lock; C refresh over network; D trust local filename | B: offline replay uses frozen verified evidence and cannot claim current freshness. |
| RG-I11 Dependency integration | A bypass C025; B derive its environment and replay its lock through acquired content; C invent another solver; D trust registry resolution | B: registry policy supplies bytes while retained dependency semantics remain authoritative. |
| RG-I12 Reproducibility | A omit acquisition; B return exact bundle bytes under logical paths for C128 inputs; C cache paths as identity; D rebuild remote state | B: acquired bytes enter the existing reproducibility envelope explicitly. |
| RG-I13 Native provenance | A source rules only; B require content/package digest, platform, toolchain, reproducible input and unsafe obligations; C signature means safe; D forbid native | B: authenticity does not erase C098/C127 trust. |
| RG-I14 Time | A host clock implicit; B caller-supplied observation checked against signed expiry; C no freshness; D timestamp files | B: the decision is testable and leaves clock correctness as explicit host trust. |
| RG-I15 History | A permit disappearance/replacement; B retain every prior identity and make compromise terminal; C compare sequence only; D retain latest only | B: a higher sequence cannot hide or rewrite accepted history. |
| RG-I16 Limits | A unlimited metadata; B finite keys/delegations/releases/signatures/mirrors/bytes; C timeout only; D truncate | B: malformed or excessive input is wholly refused. |

## Verification route

Use generated test-only Ed25519 keys and local in-memory mirror fixtures. Exercise
authentic resolution/acquisition, publisher forgery, replacement, wrong mirror,
expiry, rollback, same-sequence equivocation, root rotation and recovery, yanked
locked replay, terminal compromise, wrong native platform and missing obligation
acknowledgements. No network service or production signing key is involved.

The [TUF source note](../30-sources/the-update-framework-specification.md) supports
the use of distinct metadata roles, thresholds, delegated scopes, rollback
protection and dual-authority root rotation. Catena adapts those ideas to its own
canonical documents and C025/C127/C128 boundaries; it does not claim TUF protocol
compatibility.

## Results

The compiler adds an exact signed registry root and rotation protocol, persisted
client reverification, monotonic threshold snapshots, package-scoped publisher
signatures, exact mirror acquisition, separate active/yanked/compromised status,
C025 resolution and lock replay, C128 reproducible source builds, and C127-aware
native provenance. Revision and machine-profile discovery expose `0.1.74` without
adding a source form or changing retained artifact formats.

The seven registry tests cover authentic source resolution/acquisition/build,
forged publisher metadata, replaced bytes, missing mirrors, stale metadata,
rollback, same-sequence equivocation, terminal compromise, yanked locked replay,
dual-threshold rotation, recovery, native platform/toolchain/obligations, exact
metadata shapes, persisted-client forgery, and reported limits. The full compiler
suite passed 1,032 tests. Production compilation with warnings as errors, escript
construction, and the trusted-boundary audit also passed. The
[normative contract](../60-specification/supply-chain-policy/signed-registry-and-immutable-acquisition.md)
promotes P130 to C130.
