---
title: "2026-09-10 Migration Tool"
kind: journal
created: "2026-09-10"
tags: [specification, migration, tooling, diagnostics]
aliases: []
---

# 2026-09-10 Migration Tool

## Scope

Execute P125's retained-JSON portion at `0.1.93` while retaining the P109
public-source hold. CP-125-1..3 select a separate explicit tool, preimage-bound
transaction, and semantic recheck without inherited governance authority.

## Implementation decisions

| Decision | Four alternatives | Recommended and selected |
| --- | --- | --- |
| MT-I01 Entry point | A silent compiler mutation; B separate explicit tool action; C manual edits only; D text replacement | B: C008 remains report-only while migration is reviewable. |
| MT-I02 Input scope | A public syntax; B retained JSON first; C BEAM rewriting; D arbitrary files | B: useful work proceeds without deciding P109 grammar. |
| MT-I03 Edit admission | A every hint; B machine-applicable JSON edits only; C probable edits; D raw patches | B: applicability is explicit and structurally checkable. |
| MT-I04 Plan identity | A filename; B canonical digest of complete plan; C timestamp; D random token | B: authorization binds exact content. |
| MT-I05 Byte binding | A line offsets; B exact bytes plus SHA-256; C modification time; D file size | B: stale or substituted inputs fail reliably. |
| MT-I06 Edit overlap | A apply in arrival order; B normalize and reject ancestor overlap; C last wins; D merge guesses | B: the result is independent of caller order. |
| MT-I07 Preview | A prose summary; B exact Base64 preimage and result; C diff only; D no preview | B: every proposed byte is independently recoverable. |
| MT-I08 Authorization | A preview implies consent; B separate explicit apply authorization; C environment variable; D repository write bit | B: inspection and mutation stay distinct. |
| MT-I09 Root boundary | A trust strings; B exact root with traversal and symlink rejection; C current directory only; D resolve after write | B: migration cannot redirect writes outside its transaction. |
| MT-I10 Staging | A mutate one file at a time; B stage every result before commit; C edit in memory then stream; D temporary remote store | B: preparation failure leaves inputs unchanged. |
| MT-I11 Backups | A none; B retained plan-specific exact preimages; C one rotating backup; D result-only log | B: recovery and review retain original evidence. |
| MT-I12 Commit | A truncate then write; B same-filesystem rename sequence; C shell editor; D asynchronous writes | B: each replacement has a local rollback point. |
| MT-I13 Interruption | A leave partial state; B restore every entered path; C retry blindly; D delete outputs | B: the transaction attempts exact restoration. |
| MT-I14 Rollback failure | A hide it; B distinct outcome with paths; C call it success; D discard backups | B: operators can identify unresolved filesystem state. |
| MT-I15 Module verification | A syntax only; B checker plus equal interface digest; C execute arbitrary program; D trust edits | B: public behavior changes require review. |
| MT-I16 Manifest verification | A JSON parse only; B manifest decoder plus equal language selection; C accept revision drift; D regenerate lock | B: migrations cannot silently change selected semantics. |
| MT-I17 Governance | A inherit approvals; B explicitly inherit none; C auto-sign; D infer from author | B: new bytes require independent authority. |
| MT-I18 Audit | A console line; B canonical plan/file/backup/verification record; C mutable log; D no evidence | B: the committed transaction remains inspectable. |
| MT-I19 Bounds | A host memory; B fixed aggregate byte, file, result, and edit limits; C truncate edits; D per-file only | B: planning and application remain finite without partial output. |
| MT-I20 Exhaustion | A generic invalidity; B distinct implementation-limit outcome; C crash; D partial migration | B: the cross-cutting limit policy requires an observable nonmutation outcome. |

## Executed evidence

Compiler [PR 183](https://github.com/pcharbon70/catena/pull/183) merged feature
commit `72f6a18c2f6e54e342eb46c392d1512301d731b3` as merge commit
`a41920d9656bf1677d3065da7111f7e5276124da` into `rewrite`. Nine focused cases
cover successful module and manifest migrations, exact previews, authorization,
retained backups, stale and overlapping edits, rejected semantic changes, path
and symlink defenses, interruption rollback, rollback failure, tampered plans,
lifecycle selection, and the P109 hold. The complete 1,158-test suite passes,
as do production warnings-as-errors compilation, escript construction, trust
inventory verification, and `git diff --check`.

Corrective compiler [PR 184](https://github.com/pcharbon70/catena/pull/184)
merged feature commit `1adb20f3b0981356e5aa493bd957dad84d12ff63` as merge commit
`45c6509ca1d208a16dbe0c5980363f4221aab3ae` into `rewrite`. It separates empty
invalid requests from file-count, byte, result, and edit exhaustion and adds a
direct distinct-outcome witness. The complete suite passes 1,159 tests; the
production build and trust audit pass.

Evidence compiler [PR 185](https://github.com/pcharbon70/catena/pull/185)
merged feature commit `7a3dc22d4f0c994ab6b3fe6810253e58811d6601` as merge commit
`cc0ea8882c685d4e6c3262502059421f58e5a3ef` into `rewrite`. It directly covers
occupied backup identity refusal plus file-count, preimage-byte, result-byte,
and edit-count exhaustion. Eleven focused cases and the complete 1,160-test
suite pass.

The [normative contract](../60-specification/migration-tool/transactional-retained-json-edits.md)
makes the retained-input work durable. P125 stays partial because source/API
rewrites and deprecated-syntax handling require the P109 public parser and
identity model.
