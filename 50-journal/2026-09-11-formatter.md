---
title: "2026-09-11 Formatter"
kind: journal
created: "2026-09-11"
tags: [specification, formatting, tooling, source-text]
aliases: []
---

# 2026-09-11 Formatter

## Scope

Execute G118's grammar-independent portion at `0.1.94` while retaining the
P109 public-source hold. CP-118-1..3 select a lossless-tree destination,
version-coupled canonical defaults, and exact comment and literal
preservation. This slice implements the document and preview boundary that is
valid before the tree builder and production layouts exist.

## Implementation decisions

| Decision | Four alternatives | Recommended and selected |
| --- | --- | --- |
| FM-I01 Input | A token stream; B syntax-independent document; C source regexes; D host AST | B: callers express layout without defining Catena productions. |
| FM-I02 Algebra | A arbitrary callbacks; B closed text/line/concat/nest/group/verbatim forms; C HTML; D host formatter docs | B: a small validated algebra is deterministic and auditable. |
| FM-I03 Break choice | A random best fit; B flatten a group only when it fits; C always flatten; D always break | B: width-sensitive output has one reproducible rule. |
| FM-I04 Hard breaks | A treat as spaces; B always newline; C caller setting; D platform newline | B: structural mandatory breaks remain invariant. |
| FM-I05 Width unit | A bytes; B Unicode scalars; C graphemes; D terminal cells | B: C013 supplies a stable platform-independent unit. |
| FM-I06 Default width | A 80; B 100; C 120; D unbounded | B: 100 is fixed, practical, and leaves narrow-width evidence meaningful. |
| FM-I07 Width options | A arbitrary style profile; B width only, bounded at 240; C host config; D per-node settings | B: one presentation parameter avoids premature style policy. |
| FM-I08 Indentation | A tabs; B ASCII spaces from explicit nest nodes; C copy host indentation; D infer from source | B: output remains platform-independent and grammar-neutral. |
| FM-I09 Origin authority | A caller strings; B exact tokenizer token identity; C line numbers; D regenerated lexemes | B: C013/C017 byte spans reject forged preservation claims. |
| FM-I10 Comment handling | A normalize bodies; B exact bytes plus attachment identity; C discard; D move to line end | B: C016 attachment remains intact. |
| FM-I11 Literal handling | A decode and re-encode; B exact token bytes; C choose shortest delimiters; D host escaping | B: no delimiter or payload decision is introduced. |
| FM-I12 Source map | A none; B exact half-open source/output byte spans; C line-only map; D token ordinal | B: consumers can verify every copied origin exactly. |
| FM-I13 Preview bytes | A prose diff; B exact Base64 preimage/result; C result only; D filesystem temporary | B: review and digest verification recover every byte. |
| FM-I14 Preview identity | A timestamp; B canonical full-record digest; C random identifier; D filename | B: equivalent inputs produce equivalent evidence. |
| FM-I15 Applicability | A immediately applicable; B explicitly gated after P109; C unspecified; D editor-only | B: the preview cannot claim a public tree or grammar that does not exist. |
| FM-I16 Application | A overwrite now; B validate authorization/preimage then refuse at P109 gate; C silent no-op; D shell patch | B: safety properties are exercised without implying source completeness. |
| FM-I17 Idempotence | A claim full formatter idempotence; B claim deterministic document rendering only; C no repeat check; D normalize source blindly | B: evidence matches the implemented boundary. |
| FM-I18 Bounds | A host memory; B fixed node/depth/input/output/attachment bounds; C timeout only; D truncate output | B: resource exhaustion is finite and never produces partial output. |
| FM-I19 Exhaustion | A generic invalidity; B distinct format-limit outcome; C crash; D partial preview | B: callers can distinguish finite capacity from malformed input. |
| FM-I20 Trust placement | A unclassified utility; B reviewed tools-profile component; C source frontend authority; D runtime service | B: the tool and its dependency calls remain visible without making it grammar authority. |

Every recommendation was selected under the user's delegated decision
authority. No recommendation was overridden.

## Executed evidence

Compiler [PR 186](https://github.com/pcharbon70/catena/pull/186) merged feature
commit `305ba9b` as merge commit
`99922cf126f29f4081d0ba3853e76e6841613c36` into `rewrite`. Six focused cases
exercise wide and narrow groups, nesting, Unicode scalar width, exact block
and trailing comments, raw literals, attachments, source maps, repeatability,
forged origins, altered previews, width and depth exhaustion, authorization,
stale preimages, lifecycle selection, and the P109 hold.

The complete 1,166-test suite passes. Production compilation with warnings as
errors, escript construction, reviewed trust-inventory verification, and
`git diff --check` pass. The approved trust update classifies
`lib/catena/tool/formatter.ex` in `tools-profile` and binds its final source
digest.

Corrective compiler [PR 187](https://github.com/pcharbon70/catena/pull/187)
merged feature commit `d1a2b53` as merge commit
`9aaaedaaa18389658c7f3389f65ef9d621e60b4d` into `rewrite`. It publishes the
256-byte attachment bound, gives its exhaustion the distinct formatter-limit
outcome, and directly exercises attachment and 16,777,216-byte output limits.
The focused and complete suites, production build, escript, trust audit, and
diff check pass again.

The [normative contract](../60-specification/formatter/syntax-independent-document-algebra.md)
makes the implemented boundary durable. G118 stays partial because lossless
public parsing, canonical layouts for every production, semantic round trips,
whole-formatter idempotence, and atomic source edits require P109.
