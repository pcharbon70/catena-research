---
title: "Text and Binary Model Implementation"
kind: journal
created: "2026-09-09"
tags: [language-design, unicode, conformance]
aliases: []
---

# Text and Binary Model Implementation

## Starting point and scope

C102 merged through [compiler PR 147](https://github.com/pcharbon70/catena/pull/147)
and [research PR 97](https://github.com/pcharbon70/catena-research/pull/97).
Compiler `rewrite` was `14cbf00a1c515259abdab57790efe5dfc7968295`;
research `main` was `8fa26b5f5b896dc55b4a392d2b209dbfd29b9590`.
Integration branches were synchronized before deleting feature branches.
This slice uses `codex/text-binary-model`; session-wide approval covers semantic
revision `0.1.66`. No continuation is scheduled.

The [CP-104 plan](../20-notes/language-completion-plan-delivery.md#item-104-text-and-binary-model)
selects distinct units, pinned explicit Unicode algorithms and semantic formatting
before public syntax. The [contract](../60-specification/text-binary-model/units-unicode-and-checked-binary-operations.md)
completes that bounded library gate. P105 still owns Float/decimal formatting and
P109 owns interpolation/binary-pattern spelling.

## Implementation decisions

All choices retain the original CP-104 recommendations. These additional forks
record four alternatives each and the agent's selected recommendation.

| Decision | Four alternatives explored | Recommended and selected |
| --- | --- | --- |
| TB-I01 | A byte offsets everywhere; B distinct byte/scalar/grapheme indices; C universal grapheme Int; D implicit host index. | **B**, recommended and selected: preserve CP-104-1 and reject mixed units. |
| TB-I02 | A silently normalize Text; B explicit NFC/NFD/NFKC/NFKD at Unicode 17.0.0; C ASCII only; D host-current algorithms. | **B**, recommended and selected: retain scalar equality and CP-104-2. |
| TB-I03 | A legacy graphemes; B default extended grapheme clusters UAX29 revision47; C locale tailoring; D host String segmentation. | **B**, recommended and selected: complete pinned conformance vectors with no unstated tailoring. |
| TB-I04 | A modify frozen identifier tables; B separate deterministic text table from pinned inputs; C network lookup per call; D embed incomplete handpicked properties. | **B**, recommended and selected: new algorithms without changing C014 source manifests. |
| TB-I05 | A rescan every prefix; B one scalar pass with bounded segmentation state and sorted range lookup; C quadratic suffix regexes; D fixed-size grapheme assumptions. | **B**, recommended and selected: handles long combining/emoji/Indic runs without guessed cluster limits. |
| TB-I06 | A implicit BOM stripping; B explicit endian codecs with BOM retained as data; C guess encoding; D replacement decoding. | **B**, recommended and selected: deterministic strict conversion and exact malformed offset. |
| TB-I07 | A clamped slices; B checked half-open bounds with typed failures; C negative wraparound; D host exceptions. | **B**, recommended and selected: huge and reversed bounds never silently change meaning. |
| TB-I08 | A split UTF-8 scalars in Text; B byte slicing Text requires scalar endpoints while Bytes permit all byte offsets; C silently repair split text; D pretend bytes are scalars. | **B**, recommended and selected: preserve C040 valid Text and distinct units. |
| TB-I09 | A arbitrary inspect interpolation; B explicit typed text/scalar/integer/byte-hex fragments; C executable interpolation strings; D choose public punctuation now. | **B**, recommended and selected: pure formatting without syntax adoption; Float formatting remains P105. |
| TB-I10 | A unrestricted host bit syntax; B checked sequential binary segment descriptors with explicit widths/endian/signedness and typed captures; C regex-only byte matching; D freeze public binary patterns. | **B**, recommended and selected: executable binary semantics without new grammar. |
| TB-I11 | A malformed binary is a trap; B optional mismatch versus typed encoding/bounds failure and separate descriptor refusal; C erase failure distinctions; D retry decoding with other encodings. | **B**, recommended and selected: retain C103/C095 distinctions. |
| TB-I12 | A publish O(1) text indexing; B linear scans with explicit conversion costs and no implicit constant-time cache; C hide preprocessing cost; D forbid large text. | **B**, recommended and selected: honest complexity and full input/output bounds. |
| TB-I13 | A use native Unicode normalization; B deterministic table-based decomposition/order/composition; C normalize with locale libraries; D support only ASCII normalization. | **B**, recommended and selected: all four forms against official vectors, independent of host Unicode version. |
| TB-I14 | A public API freeze; B ordinary nominal index roles and checked retained-input runtime adoption; C native helper tests alone; D new general frontend. | **B**, recommended and selected: existing language code must execute the selected contract while public names remain held. |
| TB-I15: Historical parser boundary | A: teach the old kernel Text spelling silently; B: retain parsed structure and use C093 checked value trees; C: rename Text to Int; D: bypass the verifier. | **B**, recommended and selected: The explicit 0.1.58 profile already admits these carriers and preserves the source-vocabulary hold. |
| TB-I16: Compiled adoption | A: native helper tests only; B: exact 0.1.66 artifact combining verified source entry with a typed fixed pipeline; C: reinterpret strings as code; D: widen historical artifact identity. | **B**, recommended and selected: Actual source computation executes before checked library steps on both backend owners. |
| TB-I17: Failure payloads | A: opaque arbitrary error atoms; B: closed structural variant carried by C103 dependent failure; C: host exceptions; D: silently return empty Text. | **B**, recommended and selected: Unit mismatch, bounds, split scalar and malformed encoding have distinct typed payloads. |
| TB-I18: Binary captures | A: allocate arbitrary capture-name atoms; B: derived positional tuple schema; C: untyped host maps; D: partial bitstring ingress. | **B**, recommended and selected: Captures remain closed typed data and unsupported partial-bit remainders mismatch. |
| TB-I19: Binary integer width | A: host-native size/endian; B: explicit 1–4096 bits, byte-aligned little endian; C: only signed machine words; D: unbounded inferred width. | **B**, recommended and selected: Bit extraction and two’s-complement meaning are deterministic and bounded. |
| TB-I20: Loaded code | A: overwrite an existing same-name module; B: serialize load, reuse identical bytes and refuse conflicts; C: load without checking provenance; D: purge unrelated old code. | **B**, recommended and selected: Verified text identity does not authorize silent replacement of another loaded program. |
| TB-I21: Artifact/source limits | A: verify types but skip old literal limits; B: reuse full calling-artifact validation before text lowering; C: disable large literals in the parser; D: rely on an eventual VM crash. | **B**, recommended and selected: Retains literal, arity and toolchain obligations while the new wrapper stays explicit. |
| TB-I22: Unicode conformance extent | A: selected examples; B: every official vector equation plus all scalars outside Part 1; C: compare only to host Unicode; D: infer correctness from table names. | **B**, recommended and selected: Covers supplementary normalization requirements and separates pinned semantics from host versions. |
| TB-I23: Index caching | A: hidden cache with O(1) claims; B: explicit linear scans and boundary construction; C: trust caller-supplied cached offsets; D: silently change index units. | **B**, recommended and selected: No reusable cache is promised by this initial contract; physical sharing remains unobservable. |

## Pinned algorithms and provenance

The existing identifier Unicode table remains byte-for-byte unchanged. New
`catena-text.etf` is generated deterministically by `scripts/build_text_tables.exs`
from local pinned files, with no network operation in the generator. The table
has 61,401 bytes and SHA-256
`efae9bbdcd4c9c56d820d5f96e31c7a0f055ae55778507a6daee3147c0920252`.
A second generation produced the same digest.

The source manifest binds UnicodeData, DerivedNormalizationProps,
NormalizationTest, DerivedCoreProperties and three added official Unicode 17
files. Their retrieved SHA-256 identities are:

| File | SHA-256 |
| --- | --- |
| GraphemeBreakProperty.txt | `d6b51d1d2ae5c33b451b7ed994b48f1f4dc62b2272a5831e7fd418514a6bae89` |
| GraphemeBreakTest.txt | `e2d134d2c52919bace503ebb6a551c1855fe1a1faec18478c78fff254a1793ec` |
| emoji-data.txt | `2cb2bb9455cda83e8481541ecf5b6dfda66a3bb89efa3fa7c5297eccf607b72b` |

Upstream files retain copyright/license headers; the compiler data README records
the generation boundary. [UAX #29](../30-sources/hadley-2025-unicode-text-segmentation.md),
[UAX #15](../30-sources/whistler-2025-unicode-normalization-forms.md) and
[Unicode encoding](../30-sources/unicode-consortium-2025-unicode-standard-17.md)
were checked as primary sources. They supply algorithm/encoding definitions;
Catena index, failure, formatting and artifact rules are local design choices.

`Standard.Text.Graphemes` uses sorted property ranges and a single forward pass
with finite contextual state, including regional-indicator parity.
`Normalization` uses table-based recursive decomposition, stable combining-order
sorting and linear structural composition without repeated prefix append.
`Encoding` explicitly decodes UTF-8/16/32, preserving BOM data and first malformed
scalar offsets. The existing `UnicodeData` and `Text` owners expose delegates to
the new contract; no new built-in value kind is needed in `Values`.

## Checked library and compiled adoption

`Standard.Text` separates descriptor units, typed checked slices, explicit
normalization/conversion, concatenation and formatting roles. Error payloads are
a closed structural variant carried through ordinary C103 outcomes. Complete
outcome wrappers and index descriptors consume C095 budgets. Non-finite Float
formatting is not smuggled into this text slice; the numeric contract remains P105.

`Standard.Binary.Pattern` derives a positional capture tuple schema from explicit
segments and requires whole-input matching. Integer fields have declared
signedness, width and endian; remaining Bytes excludes partial-bit values.
Input mismatch, descriptor refusal and malformed text decoding remain distinct.

`Standard.Text.Indices` embeds a separate canonical package with three ordinary
nominal index roles and six constructor/eliminator functions, compiled through
retained 0.1.4. An explicit bridge preserves units when turning nominal results
into checked descriptors. An ordinary type error rejects a constructor belonging
to the wrong index result type.

`Standard.Text.Program` independently checks retained core and a fixed typed
pipeline before emitting a new 0.1.66 BEAM wrapper. It reuses full C094 source
validation so retained literal limits are not accidentally skipped. The wrapper
executes the real compiled source entry, then the fixed library operations.
A closed failure variant terminates dependent sequencing; optional binary
mismatch stays nested instead of being coerced to a decoding failure.

Verification rebuilds core/step/profile/compiler/forms/binary identity, and the
invocation boundary validates its argument. Loaded modules are serialized,
identical code is reused and conflicting same-name code is refused. This preserves
explicit artifact provenance without introducing a new public source grammar.

An initial fixture incorrectly treated Text as a type already parsed by kernel
0.1.8. Its A002 refusal confirmed the historical boundary; the actual witness now
uses C093's checked pure value-tree input. An ordinary JSON fixture was corrected
to its retained operator schema, supported 0.1.3 revision and required exported
signature. These were fixture repairs, not permission to widen historical syntax.

## Executed evidence

- `text_unicode_contract_test.exs` checks all **766** pinned extended-grapheme
  vectors and every normalization equation for all **20,034** vector rows. It
  additionally checks all four forms for **1,094,978** scalars outside the
  **17,086** Part 1 source scalars, a stronger domain than assigned scalars alone.
  Long combining runs contain **50,000** marks; regional-indicator parity and
  exact source-manifest digests are checked separately.
- `text_binary_contract_test.exs` checks non-BMP and combining content, empty and
  enormous slices, mixed units, scalar splitting versus arbitrary Bytes,
  UTF-8/16/32 round trips, NUL/BOM/noncharacters, malformed offsets, explicit
  formatting and bounded complete results. Binary-field values agree with
  independent integer arithmetic for all 256 byte values and wider signed words.
- `text_program_test.exs` executes value-tree normalization/encoding/slicing,
  typed formatting and binary matching, repeated exact-code reuse, incompatible
  sidecar/loaded-code refusal, static unit failures and dependent encoding failure.
  An ordinary JSON add-one function executes before integer formatting and scalar
  counting. Ordinary nominal index code and a wrong-constructor type refusal
  demonstrate the distinction before runtime.

## Verification

Reproducible commands are `elixir scripts/build_text_tables.exs`, `mix test`,
`MIX_ENV=prod mix compile --warnings-as-errors`, `MIX_ENV=prod mix escript.build`,
`python3 validate_archive.py` and `git diff --check`.

The complete compiler suite passed **933 tests**. The production compiler passed
with warnings treated as errors, and the production escript built successfully.
The archive validator passed **638 documents, 78 directories, 122 sources and
192 normative chapters**, with **874 obligations**: 779 traced, 74 partial and
21 untraced. Both repositories passed whitespace validation. The checklist now
records **104 complete, 23 partial, 12 gaps and 2 deferred** items.

Additional compiled witnesses preserve an actual source trap and exercise the
253/254-operation admission boundary. Table regeneration reproduced the recorded
SHA-256 exactly. Implementation commit and merged PR provenance follow below.

Compiler implementation: commit `64e7fdf957b47ec892bc9f06e7ad74e721895e6e`,
merged through [compiler PR 148](https://github.com/pcharbon70/catena/pull/148)
as `ae36b3ee24b556a79de7a36cabee43b4ec0a7acc`. The compiler `rewrite` branch
was synchronized with origin before its feature branch was deleted.
