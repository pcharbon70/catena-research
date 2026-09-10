---
title: "2026-09-10 Release Readiness"
kind: journal
created: "2026-09-10"
tags: [specification, conformance, release, evidence]
aliases: []
---

# 2026-09-10 Release Readiness

## Scope

Execute [G139](../20-notes/language-completion-plan-delivery.md#item-139-release-readiness-definition)
at revision `0.1.90`. CP-139-1..5 retain their recommendations: three explicit
claim classes, an exact proof ledger, a machine-readable evidence manifest,
mechanized core lemmas, and a pinned Rocq checker. Defining the gate does not
claim that held P107/P109, human G137, or the integrated theorem has passed.

## Implementation decisions

| Decision | Four alternatives | Recommended and selected |
| --- | --- | --- |
| RR-I01 Manifest encoding | A prose only; B canonical JCS map with digest; C host term; D unsigned YAML | B: canonical bytes make evidence identity portable. |
| RR-I02 Class model | A Boolean ready; B experimental/complete/stable; C maturity percentage; D marketing labels | B: each claim has an explicit evidence boundary. |
| RR-I03 Experimental gaps | A forbid all; B allow only disclosed ledgers; C ignore gaps; D auto-promote | B: useful prototype releases remain honest. |
| RR-I04 Obligation accounting | A total only; B total/traced/partial/untraced arithmetic; C checkboxes only; D inferred counts | B: incomplete coverage remains visible and checkable. |
| RR-I05 Platform identity | A OS name; B exact supported fingerprint and digest; C latest host; D any BEAM | B: retained evidence supports only its tested row. |
| RR-I06 Evidence domains | A one pass bit; B separate compatibility/performance/source-tooling/usability; C tests only; D testimonials | B: one kind of evidence cannot stand in for another. |
| RR-I07 Limitation ledger | A omit when green; B nonempty stable IDs and dispositions; C free prose; D hidden issue tracker | B: finite scope remains part of every claim. |
| RR-I08 Proof admission | A trust manifest text; B closed exact registry; C theorem name only; D test count | B: evidence cannot self-authorize. |
| RR-I09 Checker | A Rocq 9.2 pinned image; B ambient Rocq; C custom checker; D no checker | A: exact version and container digest make the run repeatable. |
| RR-I10 Initial calculus | A all Catena immediately; B minimal Nat core; C arithmetic benchmark; D copy production AST | B: an independent small relation supports sound first lemmas without overstating scope. |
| RR-I11 Substitution | A axiom; B inductive lookup and typed substitution proof; C examples; D omit variables | B: the kernel checks the structural lemma without assumptions. |
| RR-I12 Composition | A name theorem only; B prove bounded interaction after progress/preservation; C use tests; D admit | B: actual composition is checked while its limited scope is explicit. |
| RR-I13 Integrated claim | A accept asserted record; B keep registry empty until reviewed real proof; C infer from bounded proof; D drop goal | B: complete and stable remain blocked honestly. |
| RR-I14 Contradiction handling | A ignore examples; B exact audit IDs and dispositions; C let compiler decide; D delete history | B: corrections preserve authority and an auditable outcome. |
| RR-I15 Publication | A publish on pass; B report only with explicit later action; C push tags automatically; D silently upgrade | B: assessment has no external side effect. |
| RR-I16 Trust placement | A outside inventory; B tools-profile plus proof identity in manifest; C claim checker removes host trust; D bundle generated proof artifacts | B: executable assessment stays audited and proof outputs remain reproducible, not source inputs. |

## Executed evidence

Compiler [PR 175](https://github.com/pcharbon70/catena/pull/175) merged feature
commit `dc2d920` as merge commit
`60e9ada7855b86522cd89f271e1e3a5f559d63ab` into `rewrite`.
Hardening [PR 176](https://github.com/pcharbon70/catena/pull/176) then merged
feature commit `e5287a6` as merge commit
`afa267b870cedb912a419d3f667ae5acf028ff41`, requiring canonical ordering,
unique row identities, and an empty open-item ledger for complete claims.
`Catena.Release.Readiness` builds and verifies canonical digest-bound manifests,
checks exact platform and proof registries, reports class-specific blockers and
claims, and performs no publication or automatic upgrade. Negative cases cover
digest tampering, invalid obligation arithmetic, missing audits, forged proof
identity, unsupported hosts, unresolved contradictions, and a self-asserted
integrated proof.

The pinned `rocq/rocq-prover:9.2.0` image at digest
`sha256:33926fb3757b2b560c3844157bd64173a26b6d338a256be1ae5eec8df2019025`
checks `CatenaKernel.v` at source digest
`107a74da9b8e8a963a282f23bfb485f240259d00ef493b66e4d6aad098211024`.
The proof uses no admitted axiom. Its Nat-only calculus is independent evidence
for six named lemmas and is not the integrated Catena theorem.

The complete compiler suite passes with 1,137 tests. Production compilation
with warnings as errors, escript construction, trust-inventory verification,
the pinned proof check, and `git diff --check` pass. The
[normative contract](../60-specification/release-readiness/evidence-gates-and-release-claims.md)
completes G139's definition while its own result continues to block complete
and stable language claims on the held and unproved gates.
