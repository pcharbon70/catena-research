---
title: "2026-09-10 Compatibility Suite"
kind: journal
created: "2026-09-10"
tags: [specification, compatibility, conformance, testing]
aliases: []
---

# 2026-09-10 Compatibility Suite

## Scope

Execute [P136](../20-notes/language-completion-plan-delivery.md#item-136-compatibility-suite)
after C092, C116, and C121. Revision `0.1.82` is covered by the user's
session-wide approval. CP-136-1..3 retain their recommended selections, and the
work does not choose public language vocabulary or a `1.0` convention.

## Implementation decisions

| Decision | Four alternatives | Recommended and selected |
| --- | --- | --- |
| CS-I01 Representation | A prose checklist; B canonical machine-readable matrix; C test names only; D CI logs | B: stable inputs and digests make evidence replayable. |
| CS-I02 Layers | A one verdict; B seven separate layers; C source plus binary only; D product version strings | B: each authority answers a different compatibility question. |
| CS-I03 Outcomes | A Boolean; B pass/fail/unsupported; C skip means pass; D unsupported means fail | B: absence of coverage stays visible without inventing a regression. |
| CS-I04 Expectations | A infer after execution; B bind compatible/incompatible before execution; C compare bytes; D accept adapter labels | B: the oracle detects contradictory supported observations. |
| CS-I05 Scope | A ecosystem-wide claim; B explicit bounded scope; C no scope; D latest release only | B: finite evidence supports only the named matrix. |
| CS-I06 Source coverage | A newest only; B earliest retained and current exact selections plus refusals; C parse success; D future editions accepted | B: retention and forward refusal are both exercised. |
| CS-I07 Interfaces | A file hashes; B C028 semantic classifier; C package versions; D manual review | B: interface meaning is the applicable authority. |
| CS-I08 Dependency fixtures | A pairs; B generated wide/deep graphs and exact replay; C registry popularity; D random unseeded graphs | B: graph interactions remain broad, bounded, and reproducible. |
| CS-I09 Historical data | A rewrite in place; B exact interpreter or adjacent migration retaining source; C newest decoder; D discard old formats | B: historical meaning and provenance remain reviewable. |
| CS-I10 Signatures | A resign migrated bytes as history; B verify the original domain; C omit signatures; D trust filenames | B: migration cannot manufacture historical authenticity. |
| CS-I11 Toolchains | A promise all OTP releases; B exact published fingerprints with explicit endpoints; C major version; D observed host only | B: supported hosts are exact and unlisted hosts remain unsupported. |
| CS-I12 Runtime upgrades | A infer from source; B invoke C092 preflight; C restart silently; D byte equality | B: runtime replacement has its own state and coexistence obligations. |
| CS-I13 Report identity | A mutable log; B digest matrix, cases, evidence, and report; C timestamp only; D CI URL | B: changes to the claim or evidence change identity. |
| CS-I14 Invalid adapters | A omit; B explicit failed protocol result; C coerce to unsupported; D crash | B: a broken oracle cannot masquerade as missing coverage. |
| CS-I15 Bounds | A unlimited; B 4,096 cases and 1 MiB per case; C two cases; D implementation silence | B: useful generated coverage has published finite ceilings. |
| CS-I16 Trust classification | A outside trust model; B classify matrix authority and residual adapter trust; C treat tests as proof; D trust CI | B: evidence dependencies and remaining assumptions are explicit. |

## Results

Compiler [PR 164](https://github.com/pcharbon70/catena/pull/164) merged feature
commit `12c9d5d7fd3f64d32a2a706d8b25fe00430bb943` into `rewrite` as merge commit
`2538427a8c5316ea46217a511044f7b6f510662e`. The matrix implementation separates seven layers and canonicalizes
both inputs and reports. Integrated fixtures call retained edition selection,
semantic interface classification, dependency lock replay, artifact migration,
OTP fingerprint validation, Ed25519 verification, and hot-upgrade preflight.
Generated graphs cover width 64 and depth 48.

Follow-up compiler [PR 165](https://github.com/pcharbon70/catena/pull/165)
merged feature commit `e92fca1b7b2c64a38ebfa09672a186706de766a3` as
`50d1bdc5f5a0d572d4403fc81db045132bc9644a`, adding the direct regression that
distinguishes an unavailable adapter from an adapter that violates the result
protocol.

The complete suite passes 1,083 tests. Production compilation with warnings as
errors, production escript construction, trust inventory audit, and diff checks
pass; the final focused matrix suite passes seven tests. The [normative contract](../60-specification/compatibility-suite/layered-matrix-and-edition-policy.md)
promotes P136 to C136 while limiting every conclusion to the published bounded
matrix.
