---
title: "2026-09-10 Long-Term Evolution"
kind: journal
created: "2026-09-10"
tags: [specification, governance, compatibility, artifacts]
aliases: []
---

# 2026-09-10 Long-Term Evolution

## Scope

Execute [P116](../20-notes/language-completion-plan-delivery.md#item-116-long-term-evolution)
from C092 merge `7ee602f815f92bd05591987519be7597b7ef66b1`.
Revision `0.1.80` is covered by the user's session-wide approval. CP-116-1..3
retain their recommended selections.

## Implementation decisions

| Decision | Four alternatives | Recommended and selected |
| --- | --- | --- |
| EV-I01 Interpreter dispatch | A latest decoder; B exact version; C filename; D timestamp | B: historical meaning stays bound to its format. |
| EV-I02 Supported ledger | A all versions; B explicit 0.1.6–0.1.8; C latest only; D dynamic registry | B: every support claim has executable evidence. |
| EV-I03 Migration shape | A direct arbitrary hops; B deterministic adjacent hops; C manual edit; D no evolution | B: small transformations compose with a visible path. |
| EV-I04 Semantic loss | A warn and continue; B refuse; C fill defaults; D erase field | B: migration cannot invent a prior decision. |
| EV-I05 Original storage | A replace; B exact embedded bytes plus digest; C parsed map only; D external URL | B: provenance remains independently verifiable. |
| EV-I06 Old signatures | A rewrite; B retain only as historical bytes; C discard; D relabel | B: signer authority is never fabricated. |
| EV-I07 Derived identity | A inherit old digest; B canonical new envelope; C timestamp; D mutable tag | B: the derivation is a distinct reproducible artifact. |
| EV-I08 Revoked root | A reject history; B archived root for historical replay only; C reactivate; D ignore | B: past validity stays separate from new authority. |
| EV-I09 Missing tool | A latest fallback; B explicit nonportable outcome; C download ambiently; D assume | B: replay limits remain honest. |
| EV-I10 Missing dependency | A registry fallback; B explicit nonportable outcome; C omit; D substitute | B: decisions remain tied to exact inputs. |
| EV-I11 Future format | A best effort; B refuse; C strip fields; D host decode | B: unknown semantics cannot be inferred safely. |
| EV-I12 Archive set | A source only; B source/formats/tools/deps/roots/decisions; C BEAM only; D registry link | B: it preserves interpretive context. |

## Results

Compiler [PR 162](https://github.com/pcharbon70/catena/pull/162) merged feature
commit `71281e2` as `1b7623fb7e4eff2a37866af41a9b764afd723967`
into `rewrite`. The complete suite passes 1,068 tests; production compilation,
escript construction, trust audit, and diff checks pass. The
[normative contract](../60-specification/long-term-evolution/historical-replay-and-migration.md)
promotes P116 to C116 without claiming support for unknown future formats.
