---
title: "Catena Language Specification Completeness Checklist"
kind: note
created: "2026-08-01"
maturity: seed
tags:
  - catena
  - language-design
  - specification
aliases:
  - "Catena missing specification checklist"
---

# Catena Language Specification Completeness Checklist

> Temporary inbox capture. This is an audit and planning checklist, not a
> normative specification or a commitment to implement every feature listed.

Catena's research establishes a coherent architectural direction, but it does
not yet constitute a complete language specification. Completeness does not
mean including every familiar language feature. It means that every relevant
boundary is either defined precisely or explicitly excluded, with the
consequences of that exclusion recorded.

This checklist tracks the work needed to turn the current research into an
implementable, testable, and versioned language definition.

## How to use this checklist

Status labels describe the archive at this document's current Git revision:

- **Gap** — no focused research currently specifies the area.
- **Partial** — related research constrains the answer, but normative behavior
  remains undecided or scattered.
- **Deferred** — the research deliberately leaves the feature outside the
  initial core; the specification must still state that boundary explicitly.
- **Complete** — a versioned normative boundary and its required evidence are
  present for this item. Complete does not mean that neighboring items are
  complete.

Every checkbox has a unique reference identifier. `G` identifies a gap, `P`
identifies a partial specification, `D` identifies a deferred feature, and `C`
identifies a completed item. The
three-digit suffix records the item's position in this audit and is never
reused. When an item's status changes, preserve its numeric suffix, change the
prefix, and update every reference to its former identifier in the same
change.

An item is complete only when the language reference states, as applicable:

1. accepted syntax and name-resolution rules;
2. static typing, effect, and coverage rules;
3. dynamic semantics, including order and failure;
4. observable cost or resource guarantees where programmers rely on them;
5. lowering and BEAM interoperability constraints;
6. required diagnostics and representative examples; and
7. executable conformance tests or another verification method.

Checking an item may therefore mean either specifying the feature or recording
that Catena does not support it in the relevant language version.

### Prototype numbering note

C001 through C006 now designate language slices `0.1.1` through `0.1.6`.
Their cited immutable commits remain evidence for the same bounded semantics,
but those commits emitted the retired two-component protocol identifiers. They
do not establish the new wire strings, canonical bytes, or signatures. The
[prototype-slice renumbering record](../50-journal/2026-08-04-prototype-slice-renumbering.md)
tracks the hard cutover and fresh cross-slice executable-evidence gate. This
identifier migration does not reopen the completed semantic checklist items.
Normative C008 uses `0.1.7` for editions and feature lifecycle. Its explicitly
authorized immutable compiler commit and promotion evidence are recorded in
the [C008 conformance journal](../50-journal/2026-08-05-c008-edition-conformance.md).
Normative C010 uses `0.1.8` for the formal semantic kernel. Its explicitly
authorized immutable compiler commit and promotion evidence are recorded in
the [C010 conformance journal](../50-journal/2026-08-06-c010-formal-semantic-kernel.md).
Normative C013 uses `0.1.9` for the strict source-text envelope. Its decoder,
diagnostics, location model, and verification are recorded in the
[C013 conformance journal](../50-journal/2026-08-17-c013-source-text-encoding-and-normalization.md).
Normative C018 uses `0.1.14` for numeric literal semantics. Its domains,
conversion, diagnostics, limits, and verification are recorded in the
[C018 conformance journal](../50-journal/2026-08-21-c018-numeric-literal-semantics.md).
Normative C019 uses `0.1.15` for operators and punctuation. Its inventory,
capabilities and frames, ladder, diagnostics, and verification are recorded
in the
[C019 conformance journal](../50-journal/2026-08-21-c019-operators-and-punctuation.md).
Normative C020 uses `0.1.16` for the file-to-module relationship. Its file
units, module binding, generated markers, diagnostics, and verification
are recorded in the
[C020 conformance journal](../50-journal/2026-08-22-c020-files-and-modules.md).

## Existing research that needs normative consolidation

These areas already have substantial research. They still need to be rewritten
as small normative rules rather than copied wholesale into a specification.

- [x] **C001 — Complete — Hindley–Milner inference and the advanced typing boundary.**
  The [version 0.1.1 type-system specification](../60-specification/type-system/README.md)
  consolidates the principal core, advanced checking, rows, traits, effects,
  elaboration, metatheory, diagnostics, and executable conformance boundary.
- [x] **C002 — Complete — algebraic data types and pattern matching.** The
  [version 0.1.2 normative specification](../60-specification/data-and-patterns/README.md)
  covers nominal declarations, recursive groups,
  visibility, construction, the initial pattern grammar, ordered matching,
  coverage, GADT scope, generated folds, interfaces, and representation
  independence. Historical compiler commit
  `ae311604ef587a022ce2b7b46599200fcb96a7ab` supplies semantic evidence under
  the retired identifiers.
- [x] **C003 — Complete — clause conditions.** The
  [version 0.1.3 normative specification](../60-specification/clause-conditions/README.md)
  and historical compiler commit
  [`165fc4837f101d01016248e62479ef4caa0f20ce`](https://github.com/pcharbon70/catena/commit/165fc4837f101d01016248e62479ef4caa0f20ce)
  together define and exercise the exact `Bool`/`Int`
  fragment, acyclic signed predicates, difference-constraint coverage,
  ordered guard trees, interface evidence, dual BEAM lowering, and a typed
  native receive harness. Public parser syntax, usability, performance, traits,
  recursive totality, and full receive semantics remain separately identified
  later work.
- [x] **C004 — Complete — traits and category-inspired operations.** The
  [normative 0.1.4 specification](../60-specification/traits-and-categorical-operations/README.md),
  [executable conformance record](../50-journal/2026-08-02-c004-executable-trait-conformance.md),
  and published compiler commit
  [`b69f6f7e3da6015bf9b3385152ca3f3687422472`](https://github.com/pcharbon70/catena/commit/b69f6f7e3da6015bf9b3385152ca3f3687422472)
  define and exercise the initial hierarchy, behavior-first ABI, coherence, law evidence,
  derivation, operational contracts, specialization, and erasure.
- [x] **C005 — Complete — algebraic effects and handlers.** The
  [normative 0.1.5 specification](../60-specification/effects-and-handlers/README.md),
  [executable conformance record](../50-journal/2026-08-03-c005-executable-effect-conformance.md),
  [compiler PR #67](https://github.com/pcharbon70/catena/pull/67), and
  immutable compiler commit
  [`b24e58d587c830dbb9d8c87770105714745fcd1b`](https://github.com/pcharbon70/catena/commit/b24e58d587c830dbb9d8c87770105714745fcd1b)
  define and exercise nominal first-order requests, identity-aware rows, lexical
  capabilities, named deep handlers, affine resumptions, explicit typed core,
  effect-directed CPS, cross-module handlers, and differential reference/BEAM
  traces. Cleanup, exceptions, host effects, scoped control, performance, and
  usability remain separately identified work rather than incompleteness in
  the bounded 0.1.5 feature.
- [x] **C006 — Complete — language-integrated specifications and governance.**
  The
  [normative 0.1.6 specification](../60-specification/specifications-and-governance/README.md),
  [executable conformance record](../50-journal/2026-08-03-c006-executable-specification-governance-conformance.md),
  and historical authorized immutable compiler commit
  `2f6805e166a086f7d67c2cc0f3023e9e34fe2cec` define and exercise the bounded claim forms,
  evidence semantics, governed scopes, authorization, erasure, artifact
  binding, and transition rules. Public source punctuation and long-term
  protocol evolution remain separately identified work rather than
  incompleteness in the bounded 0.1.6 feature.

## 1. Specification form and conformance

- [x] **C007 — Complete — normative document structure.** The repository-level
  [Specification Authority](../SPECIFICATION-AUTHORITY.md), enforced template
  and validator, complete 0.1.1–0.1.6 chapter migration, aligned compiler-facing
  guides, and [C007 validation record](../50-journal/2026-08-03-c007-normative-document-authority.md)
  define which documents are normative, visibly distinguish definitions,
  examples, rationale, and evidence, require document-and-heading citations,
  and make normative text the sole authority when reference paths, compiler
  behavior, and tests disagree. This governance completion creates no Catena
  0.1.7 slice or immutable compiler commit.
- [x] **C008 — Complete — language editions and feature lifecycle.** The
  [normative 0.1.7 specification](../60-specification/editions-and-feature-lifecycle/README.md),
  [synthesis](../20-notes/language-editions-and-feature-lifecycle.md), and
  [resolved inquiry](../40-inquiries/how-should-catena-version-editions-and-language-features.md)
  define edition `0.1`, exact retained revisions, package-local selection,
  named previews, lifecycle transitions, pre-1.0 and post-1.0 compatibility,
  deprecation, migration records, selection-bound interfaces and artifacts,
  versioned signatures, optional governance constraints, and structured
  diagnostics. The sibling compiler implements the contract with focused
  positive and adversarial evidence. The
  [C008 conformance record](../50-journal/2026-08-05-c008-edition-conformance.md)
  records the authorized immutable compiler commit
  [`8ef7835d1d7f9b2ab14843ac7817798d58eb2bd4`](https://github.com/pcharbon70/catena/commit/8ef7835d1d7f9b2ab14843ac7817798d58eb2bd4),
  its parent and tree, the post-commit suites, artifact hashes, and the known
  non-reproducible escript-packaging limitation.
- [x] **C009 — Complete — conformance vocabulary.** The repository-level
  [Catena Conformance Vocabulary](../CONFORMANCE-VOCABULARY.md),
  [synthesis](../20-notes/catena-conformance-vocabulary-and-behavior-classes.md),
  [resolved inquiry](../40-inquiries/how-should-catena-classify-conformance-behavior.md),
  area variability registers, enforced validator, and bootstrap compiler
  profile define the five canonical requirement words; required, invalid,
  implementation-defined, bounded unspecified-presentation,
  implementation-limit, and explicit-trap classes; and Catena's prohibition
  on undefined behavior. The
  [C009 record](../50-journal/2026-08-05-c009-conformance-vocabulary.md)
  records the complete `MAY`, `SHOULD`, and invalidity audit. This
  repository-governance completion creates no language revision `0.1.8`,
  compiler semantic change, or immutable promotion commit.
- [x] **C010 — Complete — formal semantic kernel.** The normative
  [0.1.8 specification](../60-specification/formal-semantic-kernel/README.md)
  integrates a closed S-expression conformance input, regular data, structural
  value rows, duplicate ordinary effect rows, bounded traits, deep affine
  handlers, explicit traps, typed public process entries, a small-step actor
  machine, independent core verification, and fixed BEAM lowering. The
  [resolved inquiry](../40-inquiries/how-should-catena-integrate-its-formal-semantic-kernel.md),
  [conformance journal](../50-journal/2026-08-06-c010-formal-semantic-kernel.md),
  and immutable compiler commit
  [`ef8bcf85adde84fed4a7cab3a533eb8399fbe67a`](https://github.com/pcharbon70/catena/commit/ef8bcf85adde84fed4a7cab3a533eb8399fbe67a)
  record the atomic promotion and post-commit executable evidence.
- [x] **C011 — Complete — executable conformance suite.** At C011 completion,
  every `MUST`/`MUST NOT` obligation across the original eight normative areas
  carried a permanent
  area-scoped identifier (`AREA-OBL-NNN`), a resolved normative anchor, and,
  where it has a focused executable unit, at least one tagged passing compiler
  test enforced by a per-area coverage gate. The non-normative
  [traceability registry](../10-maps/conformance-traceability.md) held 318
  obligations at that milestone and now also holds C012's 12 governance
  obligations and C013's 10 fully traced source-text obligations. The
  [resolved inquiry](../40-inquiries/how-should-catena-achieve-exhaustive-rule-to-test-traceability.md)
  and [C011 record](../50-journal/2026-08-12-c011-executable-conformance-suite.md)
  record the coordinated compiler PRs (#76–#87) and the immutable compiler
  identity. Twenty architectural, future-version, and P117/G095 diagnostic
  obligations remain explicitly allow-listed and carried by their owner items.
  This repository-governance completion creates no language revision and no
  compiler semantic change.
- [x] **C012 — Complete — implementation limits.** The repository-level
  [Catena Implementation Limits and Portability](../IMPLEMENTATION-LIMITS.md),
  [synthesis](../20-notes/catena-implementation-limits-and-portability.md),
  [resolved inquiry](../40-inquiries/how-should-catena-bound-implementation-limits.md),
  [topic map](../10-maps/implementation-limits-and-portability.md), and
  [C012 record](../50-journal/2026-08-17-c012-implementation-limits.md) define
  portable floors of 253 explicit callable arguments, 4,096 integer digits,
  a reserved 65,536-byte decoded literal payload, and a 1,048,576-byte
  generated BEAM module; centralize the existing 20,000-step and 1,024-depth
  bounds; separate compiler refusals from inconclusive evidence and runtime
  capacity; require structured transactional diagnostics; and require
  deterministic machine-readable reporting. The sibling compiler implements
  the contract at immutable commit
  [`841af5ee342a31ff4769749bbdaa18a675b1bb21`](https://github.com/pcharbon70/catena/commit/841af5ee342a31ff4769749bbdaa18a675b1bb21)
  on draft PR [#88](https://github.com/pcharbon70/catena/pull/88), with 179
  passing tests and `IL-OBL-001`–`IL-OBL-012` traceability. Mailbox capacity
  remains deployment-defined under G068/G129 without permitting silent
  per-sender reordering, retargeting, or live-target message loss. This
  repository-governance milestone creates no language revision.

## 2. Lexical grammar and source files

- [x] **C013 — Complete — source encoding and normalization.** The normative
  [0.1.9 source-text specification](../60-specification/source-text/README.md),
  [synthesis](../20-notes/catena-source-text-encoding-and-normalization.md),
  [resolved inquiry](../40-inquiries/how-should-catena-decode-and-normalize-source-text.md),
  [topic map](../10-maps/source-text-encoding-and-normalization.md), and
  [C013 record](../50-journal/2026-08-17-c013-source-text-encoding-and-normalization.md)
  define strict UTF-8, reject leading BOMs, alternate encoding signatures,
  malformed sequences, and lone CR, map LF and CRLF to one logical LF,
  preserve every other scalar without whole-file normalization, and assign
  original-byte spans with scalar-based lines and columns. The sibling
  compiler implements `Catena.decode_source_text/2`, source units,
  `check-source-text`, `SRC001`–`SRC003`, exact frontend/persistence
  separation, and complete `ST-OBL-001`–`ST-OBL-010` executable coverage at
  immutable commit
  [`d4e8e5c0ad41f47ebe86d59047cdabe017762f38`](https://github.com/pcharbon70/catena/commit/d4e8e5c0ad41f47ebe86d59047cdabe017762f38)
  on draft compiler PR [#89](https://github.com/pcharbon70/catena/pull/89).
  C014 now defines standalone identifiers, C015 defines layout events, C016
  defines comments, C017 defines atomic literals, C018 defines numeric
  literal meaning, and C019 defines operators and the whole-source token
  stream; C020 defines the file-to-module relationship and P109 retains the
  declaration grammar; P117 and G118 retain complete diagnostics and
  formatting.
- [x] **C014 — Complete — identifiers.** The normative
  [0.1.10 identifier specification](../60-specification/identifiers/README.md),
  [synthesis](../20-notes/catena-identifiers-and-name-security.md),
  [resolved inquiry](../40-inquiries/how-should-catena-define-and-secure-identifiers.md),
  [topic map](../10-maps/identifier-and-name-security.md), and
  [C014 record](../50-journal/2026-08-17-c014-identifiers-and-name-security.md)
  pin Unicode 17 XID, require NFC source spelling, make case significant but
  role-neutral, apply the General Security and Highly Restrictive profiles,
  freeze hard keywords with backtick escapes, define ASCII-dot qualification,
  and emit deny-able confusable warnings over supplied comparison domains. The
  sibling compiler branch `agent/c014-identifiers` vendors exact Unicode data,
  implements standalone identifier/qualified-name/audit APIs and
  `check-identifiers`, and supplies complete `ID-OBL-001`–`ID-OBL-013`
  executable coverage. C015 now defines whitespace/layout, C016 defines
  comments/documentation, C017 defines atomic literals, C018 defines numeric
  literal meaning, and C019 defines the whole-source token stream; C020
  fixes the file-to-module relationship; G021–G022 retain namespaces,
  resolution, imports, and exports.
- [x] **C015 — Complete — whitespace and layout.** The normative
  [0.1.11 whitespace and layout specification](../60-specification/whitespace-and-layout/README.md),
  [synthesis](../20-notes/catena-whitespace-layout-and-line-continuation.md),
  [resolved inquiry](../40-inquiries/how-should-catena-treat-whitespace-and-line-breaks.md),
  [topic map](../10-maps/whitespace-layout-and-line-continuation.md), and
  [C015 record](../50-journal/2026-08-17-c015-whitespace-and-layout.md)
  make indentation non-semantic, admit only ASCII space, tab, and C013 logical
  LF as layout whitespace, use hard LF and semicolon separators, and classify
  continuation from lexer-supplied before/after token capabilities plus
  continued or block delimiter frames. The sibling compiler branch
  `agent/c015-whitespace-layout` implements a lossless
  `Catena.resolve_layout/2` token-event engine, `LAY001`–`LAY003`, exact spans,
  revision/persistence separation, and complete `LY-OBL-001`–`LY-OBL-011`
  coverage at immutable compiler commit
  [`5d08925ce92f57e78018e0ab81c008a7d917dfbc`](https://github.com/pcharbon70/catena/commit/5d08925ce92f57e78018e0ab81c008a7d917dfbc)
  on draft compiler PR [#91](https://github.com/pcharbon70/catena/pull/91).
  C016 now defines comment integration, C017 defines literal-contained line
  ownership, and C019 assigns the concrete token capabilities and delimiter
  frames; P109 retains the complete surface grammar.
- [x] **C016 — Complete — comments and documentation comments.** The normative
  [0.1.12 comments specification](../60-specification/comments-and-documentation-comments/README.md),
  [synthesis](../20-notes/catena-comments-and-documentation-comments.md),
  [resolved inquiry](../40-inquiries/how-should-catena-handle-comments-and-documentation-comments.md),
  [topic map](../10-maps/comments-and-documentation-comments.md), and
  [C016 record](../50-journal/2026-08-18-c016-comments-and-documentation-comments.md)
  define `//`, nested `/* ... */`, forward outer documentation comments,
  lossless C015 classification for every comment-internal LF, exact body
  normalization and declaration attachment, CommonMark 0.31.2, inert raw HTML,
  and explicit-only future `catena doctest` fences. The sibling compiler branch
  `agent/c016-comments-documentation` implements `Catena.scan_comment/2` and
  `Catena.resolve_comments/2`, exact `CMT001`, `CMT002`, and `DOC001`
  diagnostics, source-only revision/persistence separation, and complete
  `CM-OBL-001`–`CM-OBL-012` executable coverage. C019 now supplies the complete token stream and
  C020 the file-to-module relationship; P109
  retains declaration grammar; G110/G118
  retain rendering/formatting; G119 retains actual doctest execution.
- [x] **C017 — Complete — atomic literal grammar.** The normative
  [0.1.13 literal specification](../60-specification/literal-grammar/README.md),
  [synthesis](../20-notes/catena-literal-grammar.md),
  [resolved inquiry](../40-inquiries/how-should-catena-spell-and-decode-literals.md),
  [topic map](../10-maps/literal-grammar.md), and
  [C017 record](../50-journal/2026-08-18-c017-literal-grammar.md) define exact
  Boolean keywords; unsigned binary/octal/decimal/hexadecimal integers;
  decimal dotted or exponent floats; strict separators and leading zeros;
  cooked text, one-scalar characters, and bytes; exact arbitrary-hash raw text
  and bytes; a closed escape set; no normalization; literal-owned raw LF;
  lossless source pieces; `LIT001`–`LIT003`; and active `LIM002`/`LIM004`
  boundaries. Sibling compiler commit
  [`d51b3079c87f84b560e009ac9fc00e0077d11b05`](https://github.com/pcharbon70/catena/commit/d51b3079c87f84b560e009ac9fc00e0077d11b05)
  on compiler PR [#93](https://github.com/pcharbon70/catena/pull/93)
  implements `Catena.scan_literal/2`, exact numeric metadata, provenance,
  source-only lifecycle/persistence separation, and complete
  `LT-OBL-001`–`LT-OBL-012` coverage with 233 passing tests. Compound lists,
  tuples, records, maps, and binary construction remain G040/G042/P093/G097;
  atoms/symbols remain G040/P093/G097; negation spelling and the token
  inventory are complete as C019 while P109 retains declaration grammar;
  numeric meaning is complete as C018; and any future interpolation requires
  a new opt-in prefix.
- [x] **C018 — Complete — numeric literal semantics.** The normative
  [0.1.14 numeric specification](../60-specification/numeric-literal-semantics/README.md),
  [synthesis](../20-notes/catena-numeric-literal-semantics.md),
  [resolved inquiry](../40-inquiries/how-should-catena-define-numeric-literal-semantics.md),
  [topic map](../10-maps/numeric-literal-semantics.md), and
  [C018 record](../50-journal/2026-08-21-c018-numeric-literal-semantics.md)
  fix `Int` as the unbounded mathematical integers and `Float` as finite
  binary64 with signed zero and no infinities or NaN; type integer and
  decimal literals monomorphically without defaulting, constraints, or
  implicit coercions; convert decimal components through one exact correctly
  rounded `roundTiesToEven` step with valid subnormal and underflow-to-zero
  results; refuse magnitudes at or above 2¹⁰²⁴ − 2⁹⁷⁰ statically as
  `NUM001`; elaborate numeric negation totally including `-0.0` with its
  spelling and precedence fixed by C019; keep patterns unsigned; and bound decimal
  component digits with the 4,096-digit `LIM005` floor. Sibling compiler
  commit
  [`6fb2ad89a5cc5518528106f73d60b5adc9387d74`](https://github.com/pcharbon70/catena/commit/6fb2ad89a5cc5518528106f73d60b5adc9387d74)
  supplies complete `NM-OBL-001`–`NM-OBL-014` coverage with 246 passing
  tests. Numeric traits remain G061, explicit conversions and the numeric
  library remain G105, primitive equality remains P035, and arithmetic
  failures remain G036.
- [x] **C019 — Complete — operators and punctuation.** The normative
  [0.1.15 operators specification](../60-specification/operators-and-punctuation/README.md),
  [synthesis](../20-notes/catena-operators-and-punctuation.md),
  [resolved inquiry](../40-inquiries/how-should-catena-fix-operators-and-punctuation.md),
  [topic map](../10-maps/operators-and-punctuation.md), and
  [C019 record](../50-journal/2026-08-21-c019-operators-and-punctuation.md)
  fix the closed semantic-mapped operator and punctuation inventory
  (`+ - *`, comparisons, equalities, `! && ||`, `-> |> . , ; ( ) [ ] { }`)
  with ASCII-only maximal munch against every C014–C018 atom and `OPR001`
  reserved-spelling rejection; assign every token its C015
  `join_before`/`join_after` capabilities with `paren`/`bracket` continued
  frames and a `brace` block frame; fix one precedence ladder with
  per-level associativity, no fixity declarations, non-associative
  comparisons whose chains are rejected as `OPR002`, prefix `-` and `!`
  tightest, and the loosest left-associative `|>` pipe; tokenize `->` while
  excluding it from expression rules; keep `.` qualification-only; and
  deliver the whole-source token stream and operator-expression layer with
  transactional rejection and no recovery. Sibling compiler commit
  [`6e13bdf72547c4b363d794461c3f875fd0a16119`](https://github.com/pcharbon70/catena/commit/6e13bdf72547c4b363d794461c3f875fd0a16119)
  supplies complete `OP-OBL-001`–`OP-OBL-016` coverage with 260 passing
  tests. Application and declaration grammar remain P109; file-to-module
  file-to-module relations are complete as C020; qualification resolution
  remains G021/G022; field-like access remains G040; operator dispatch
  remains G061; editor recovery remains G123.
- [x] **C020 — Complete — file-to-module relationship.** The normative
  [0.1.16 files specification](../60-specification/files-and-modules/README.md),
  [synthesis](../20-notes/catena-files-and-modules.md),
  [resolved inquiry](../40-inquiries/how-should-catena-relate-files-to-modules.md),
  [topic map](../10-maps/files-and-modules.md), and
  [C020 record](../50-journal/2026-08-22-c020-files-and-modules.md) fix the
  `.cat` extension; at most one module per file with empty and comment-only
  files as valid no-module units; ASCII uppercase-initial module-name
  spelling aligned with both semantic frontends; declared-name basename
  verification whose mismatch is `FIL004` static invalidity; and one exact
  first-line `// catena:generated by <tool>` marker that is inert anywhere
  else with malformed near-misses rejected as `FIL005`. Sibling compiler
  commit
  [`677a8f4a91f047d3ee97f197992b24401cff9a41`](https://github.com/pcharbon70/catena/commit/677a8f4a91f047d3ee97f197992b24401cff9a41)
  supplies complete `FU-OBL-001`–`FU-OBL-012` coverage with 271 passing
  tests through the abstract file-unit resolver. The concrete module-header
  syntax remains P109; module-name resolution remains G021/G022; package
  assembly remains G025; entry modules remain G027.

## 3. Names, modules, packages, and separate compilation

- [ ] **G021 — Gap — namespaces and shadowing.** Define namespaces for values, types,
  constructors, traits, effects, specifications, and modules, plus ambiguity
  and shadowing rules.
- [ ] **G022 — Gap — imports and exports.** Define qualification, renaming, wildcard
  imports or their exclusion, re-exports, unused-import diagnostics, and
  visibility defaults.
- [ ] **P023 — Partial — abstraction boundaries.** C002 completes transparent
  constructor export versus fully abstract type export and layout-free module
  interfaces. Stable layout opt-in and any separate construction versus
  matching authority remain open.
- [ ] **G024 — Gap — dependency cycles.** Define whether module recursion exists and
  how initialization, inference, and separate compilation behave across cycles.
- [ ] **G025 — Gap — package identity and dependency resolution.** Define manifests,
  semantic versioning expectations, lockfiles, source identity, integrity, and
  conflicting transitive versions.
- [ ] **G026 — Gap — prelude policy.** Define automatic imports, opt-out behavior,
  shadowing, and what is guaranteed by every language edition.
- [ ] **G027 — Gap — entry points and application structure.** Define executable and
  library roots, top-level effects, application startup, and shutdown results.
- [ ] **G028 — Gap — API and ABI compatibility.** Define source, type, behavior, and
  BEAM-level compatibility, including what changes require a major version.

## 4. Core expressions and evaluation

- [ ] **P029 — Partial — value and evaluation definition.** State precisely that the
  language is strict and define which forms are values.
- [ ] **P030 — Partial — evaluation order.** C002 defines single scrutinee
  evaluation and source-order constructor fields. C003 adds
  pattern-before-condition order, exactly one condition evaluation, lazy
  left-to-right Boolean composition, false fallthrough, irreversible body
  commitment, and shared or-pattern continuations. General function and
  operator arguments, collections, traits, interpolation, and other forms
  remain open.
- [ ] **G031 — Gap — bindings and sequencing.** Define `let`-like syntax, scope,
  recursive bindings, mutual recursion, unused values, and sequencing of
  effectful expressions.
- [ ] **G032 — Gap — functions and calls.** Define currying or fixed arity, partial
  application, closure capture, named functions, anonymous functions, local
  functions, and tail-call guarantees.
- [ ] **G033 — Gap — conditionals and general branching.** Specify Boolean conditions,
  match expressions, branch typing, missing alternatives, and whether any
  statement-like control forms exist.
- [ ] **P034 — Partial — recursion and termination.** C003 excludes
  recursive condition predicates and verifies an acyclic first-order fragment.
  Separate unrestricted program recursion from future recursive total
  fragments used by conditions, specifications, laws, and compile-time
  evaluation.
- [ ] **P035 — Partial — equality and ordering of primitive values.** C003
  defines exact equality for `Bool` and mathematical `Int`, plus integer
  order, only inside the closed condition fragment. Define their general
  expression forms and floats including NaN, strings, binaries, functions,
  references, processes, mixed numeric types, traits, and coercions.
- [ ] **G036 — Gap — runtime failure taxonomy.** Distinguish typed failure, explicit
  panic or crash, arithmetic faults, failed assertions, foreign exceptions,
  and VM termination.
- [ ] **G037 — Gap — resource and allocation observability.** State which allocation,
  sharing, object identity, garbage collection, stack use, and finalization
  behaviors programs may observe.
- [ ] **G038 — Gap — compile-time evaluation.** Decide whether constants, attributes,
  generated derivations, or macros execute code during compilation and under
  which totality and determinism restrictions.

## 5. Data, collections, and patterns

- [x] **C039 — Complete — algebraic data declaration syntax.** The 0.1.2 normative specification
  specifies kinded parameters, nullary, positional, and named-product
  constructors, atomic recursive groups, explicit existentials and refined
  results, `derives fold`, and transparent or abstract export.
- [ ] **G040 — Gap — built-in data model.** Define unit, Boolean, numeric, string,
  binary, tuple, list, map, set, process, reference, and function types, or
  explicitly exclude each nonessential built-in.
- [ ] **P041 — Partial — structural records and variants.** Specify literal, selection,
  update, extension, restriction, row-polymorphic typing, duplicate labels, and
  runtime representation.
- [ ] **G042 — Gap — collection construction and update.** Define persistent update,
  duplicate map keys, ordering, key equality, bounds failures, and complexity
  promises.
- [x] **C043 — Complete — initial pattern grammar.** The 0.1.2 normative specification supports
  wildcard, binder, integer and Boolean literal, tuple, positional and named
  constructor, `as`, `or`, and nested patterns; it explicitly excludes list,
  structural-record, row-variant, binary, range, and programmable forms.
- [ ] **P044 — Partial — refutability by context.** C002 defines all supported
  pattern forms in exhaustive matches. C003 makes multi-clause
  functions exhaustive and gives the typed receive harness selective
  nonconsuming rejection. Local bindings, generators, public receives,
  handlers, and exception clauses still need their own admissibility and
  failure rules.
- [x] **C045 — Complete — initial coverage and redundancy.** The 0.1.2 normative specification
  uses one usefulness relation for closed nominal data, Booleans, tuples,
  integer literals, abstract types, three-valued inhabitation, guards, `or`
  patterns, and GADT refinements, with witnesses and deterministic limits.
- [ ] **D046 — Deferred — programmable patterns.** Explicitly exclude or separately
  specify view patterns, pattern synonyms, active patterns, and their effects,
  totality, coverage, evaluation count, and cost. C002 explicitly excludes
  these forms without reserving hidden conversion semantics.

## 6. List comprehensions, generators, and iteration

The [list-comprehension synthesis](../20-notes/list-comprehensions.md) now
proposes a coherent initial answer. Every item remains unchecked because the
proposal still needs normative grammar, formalization, implementation, and
validation.

- [ ] **P047 — Partial — list-comprehension surface syntax.** Validate the proposed
  result-producing `for ... yield` shape and specify total generator,
  filtering generator, Boolean filter, binding, and nested qualifier grammar.
- [ ] **P048 — Partial — generator protocol.** Confirm the proposed initial `List A`
  source; keep iterators, streams, effectful producers, and generic foldable
  sources explicitly outside that version.
- [ ] **P049 — Partial — multiple-generator meaning.** Formalize the proposed
  left-to-right, depth-first Cartesian traversal, dependency, source-evaluation
  count, and empty-input behavior.
- [ ] **P050 — Partial — filter semantics.** Validate ordinary typed `Bool` filters
  with visible effects, false-as-skip, and propagation of all other failures.
- [ ] **P051 — Partial — pattern-generator failure.** Formalize exhaustive ordinary
  generators and explicitly marked filtering generators whose pattern mismatch
  alone skips an element.
- [ ] **P052 — Partial — qualifier bindings and scope.** Validate left-to-right
  visibility, non-recursive exhaustive bindings, no escaping names, and the
  proposed same-comprehension rebinding error.
- [ ] **P053 — Partial — evaluation and effect order.** Specify and test exact source
  traversal, qualifier order, multiplicity, short-circuiting, failure timing,
  and effect-row inference.
- [ ] **P054 — Partial — eager versus lazy production.** Confirm eager ordered list
  results; keep lazy streams and infinite inputs under a separate resource and
  cancellation contract.
- [ ] **P055 — Partial — elaboration contract.** Formalize the typed qualifier-tree
  target, pure extensional equations with `map` and `flat_map`, and the fused
  worker behavior that must preserve effects and failures.
- [ ] **P056 — Partial — result type.** Confirm initial `List B` output and explicitly
  exclude maps, sets, binaries, streams, validation values, and arbitrary
  `Applicative` or `Monad` targets.
- [ ] **P057 — Partial — sequential versus parallel execution.** Make sequential
  source-order behavior normative and require separate syntax, effects, and
  structured-concurrency rules for any future parallel form.
- [ ] **P058 — Partial — termination and cost.** Verify tail-recursive workers, linear
  output allocation, no intermediate map/filter lists, Cartesian cost
  explanations, and debugger/profiler source fidelity.
- [ ] **D059 — Deferred — neighboring iteration syntax.** Research ranges,
  effect-only loops, generator functions, async streams, binary and map
  comprehensions, zip qualifiers, and generic collectors independently.

## 7. Type-system surface and advanced boundaries

- [x] **C060 — Complete — type syntax.** Version 0.1.1 freezes function, tuple,
  constructor, record, variant, effect-row, constrained, quantified, and
  higher-rank type notation.
- [ ] **G061 — Gap — primitive numeric relationships.** Decide whether numeric
  overloading uses traits, literal constraints, defaulting, coercions, or
  distinct operators.
- [ ] **G062 — Gap — aliases, opaque types, and newtypes.** Define identity,
  representation, constructor access, coercion, deriving, and error messages.
- [x] **C063 — Complete — generalization boundary.** The effect-aware hybrid
  rule freezes generalization, signature subsumption, and recursive annotation
  behavior.
- [x] **C064 — Complete — row semantics.** Record, variant, and effect row
  equality are separate, including duplicate effects, lacks constraints, and
  ambiguity.
- [x] **C065 — Complete — trait constraint solving.** Version 0.1.1 freezes
  instance scope, termination, coherence, ambiguity rejection, no defaulting,
  and failure diagnostics.
- [ ] **G066 — Gap — type-directed name resolution.** State whether field, method,
  constructor, literal, and operator resolution may depend on inferred types.
- [ ] **G067 — Gap — dynamic and unsafe boundaries.** Define casts, runtime type
  inspection, unchecked operations, compiler intrinsics, and how unsafety is
  made visible—or explicitly exclude them.
- [x] **C068 — Complete — checked advanced type profile.** Predicative explicit
  higher rank, signature-directed GADTs, branch-local equalities, and explicit
  rigid constructor existentials are specified behind an annotation boundary.
- [ ] **D140 — Deferred — excluded advanced type features.** Impredicativity,
  inferred higher rank, general linear and dependent types, unrestricted
  type-level computation, and higher-kinded polymorphism over arbitrary kinds stay
  outside version 0.1.1.

## 8. Traits, derivation, and categorical libraries

- [x] **C069 — Complete — declaration and implementation forms.** Normative 0.1.4
  defines kinded parameters, parents, constraints, exact minimal methods,
  visibility metadata, implementation ownership, and placement through JSON
  AST 0.1.4. Public parser punctuation remains deliberately unfrozen.
- [x] **C070 — Complete — coherence and ownership.** Version 0.1.1 freezes
  trait-or-type ownership, prohibits overlap and local implementations, and
  requires import-order-independent identity and separate compilation.
- [x] **C071 — Complete — associated information.** Traits support methods,
  multi-parameter constraints, functional dependencies, and associated types;
  associated constants are excluded.
- [x] **C072 — Complete — laws and trusted evidence.** Normative 0.1.4 admits only
  promised, tested, and compiler-derived evidence, reserves trusted and proved,
  fixes the pure-total finite law domain, and forbids law rewrites.
- [x] **C073 — Complete — derivation.** Normative 0.1.4 adds explicit-target
  `Equatable`, `Orderable`, `Mapper`, `TwoSlotMapper`, `Reducible`, and
  `CollectingMapper` instances and type-qualified functions without override
  hooks, with tested stack-safe standard `List` mapping and reduction.
- [x] **C074 — Complete — operational contracts.** Normative 0.1.4 freezes strict
  left-to-right order, exact-once declaration-order visits, subject-last ABI,
  separate early termination, no law-implied concurrency, and standard
  collection stack safety.
- [x] **C075 — Complete — dispatch and dictionary observability.** Normative 0.1.4
  specifies deterministic manifest-directed specialization, direct calls, one
  companion BEAM, no reflection, and complete evidence erasure, with published
  artifact inspection and repeat-build evidence.

## 9. Effects, failure, and resource scopes

- [x] **C076 — Complete — effect declaration and use syntax.** Normative 0.1.5
  freezes normal parameter-list operations, `request`, behavior-first `uses`,
  optional explicit capability qualification, module-level `handler`
  declarations, `handle ... using ... as ...`, mandatory return and complete
  operation clauses, and `resume ... with ...`, with executable positive,
  negative, interface, and cross-module conformance evidence.
- [x] **C077 — Complete — handler selection.** Duplicate effect rows preserve
  lexical capability identity; handling removes the statically selected
  occurrence, never a runtime nearest-label match.
- [x] **C078 — Complete — resumption discipline.** Affine use is checked in the
  typed core and backed by a runtime consumed token; resumptions cannot escape,
  be stored, or be resumed twice.
- [x] **C079 — Complete — effect ordering.** Normative 0.1.5 freezes strict handler
  argument order, exact identity forwarding, observable nesting order, abort,
  deep reinstallation, and outer-scope effects from return and operation
  clauses. The independent free-request evaluator and generated BEAM agree on
  the bounded conformance traces.
- [ ] **G080 — Gap — cleanup and resource scopes.** Specify acquisition, release,
  cancellation, abort, panic, normal return, process exit, and foreign-frame
  unwinding.
- [ ] **G081 — Gap — exception boundary.** Decide whether exceptions are an effect,
  process exits, foreign failures, programmer panics, or several distinct
  mechanisms, and how each is typed and caught.
- [ ] **G082 — Gap — top-level effects.** Define which requests an application entry
  point may leave unhandled and who interprets them.
- [ ] **D083 — Deferred — scoped and multi-shot computations.** Explicitly bound
  generators, async, nondeterminism, transactions, shallow handlers,
  higher-order effects, and multi-shot continuations until their semantics are
  separately specified.

## 10. Processes, concurrency, and distribution

- [ ] **G084 — Gap — process creation and lifetime.** Define spawn, normal completion,
  crash, links, monitors, trapping exits, parent-child relationships, and
  structured task scopes.
- [ ] **G085 — Gap — message semantics.** Define send results, copying and sharing,
  ordering guarantees, mailbox growth, unsupported values, and remote delivery.
- [ ] **P086 — Partial — selective receive.** C003 provides a typed
  native-only lowering harness requiring one closed message type and portable
  inlined conditions, while preserving rejected messages. Connect public
  syntax, effect and protocol typing, timeouts, mailbox scan order, starvation,
  cancellation, and cost explanations in one normative rule.
- [ ] **G087 — Gap — typed protocols.** Decide whether mailbox protocols, process
  handles, replies, and protocol evolution are statically tracked or library
  conventions.
- [ ] **G088 — Gap — cancellation and time.** Define cancellation propagation,
  deadlines, monotonic time, sleep, timer races, and cleanup.
- [ ] **G089 — Gap — supervision.** Specify which OTP supervision concepts are direct
  language features, standard-library APIs, generated specifications, or plain
  Erlang interoperability.
- [ ] **G090 — Gap — scheduler observability.** State fairness assumptions, reduction
  preemption, process priority, blocking foreign work, and determinism limits.
- [ ] **G091 — Gap — distribution.** Define node identity, serialization, code-version
  skew, connection failure, partitions, authentication, and delivery claims.
- [ ] **G092 — Gap — hot code upgrade.** Define state migration, old and new code
  coexistence, capability and type compatibility, rollback, and governance
  evidence.

## 11. BEAM representation and Erlang interoperability

- [ ] **P093 — Partial — Catena-to-BEAM value mapping.** C002 defines and
  differentially checks uniform and compact nominal ADT layouts behind a
  layout-free typed interface. Records, variants, closures, trait dictionaries,
  capabilities, erased artifacts, and the full primitive model remain open.
- [ ] **G094 — Gap — calling conventions.** Define exported names and arities,
  currying, closures, tail calls, callbacks, stack traces, and module metadata.
- [ ] **G095 — Gap — Erlang type boundary.** Specify how dynamically typed terms enter
  Catena, which checks occur, how failures are represented, and whether gradual
  or explicit dynamic types exist.
- [ ] **G096 — Gap — foreign calls and callbacks.** Define syntax, effect declarations,
  trust, exceptions, blocking behavior, cancellation, ownership, and callback
  lifetime.
- [ ] **G097 — Gap — binaries, maps, PIDs, ports, references, and funs.** Define which
  BEAM-native values are first-class and what type and equality guarantees they
  receive.
- [ ] **G098 — Gap — NIFs and ports.** Define unsafe boundaries, scheduler classes,
  resource finalization, VM crashes, capability requirements, and packaging.
- [ ] **G099 — Gap — OTP compatibility policy.** Define supported versions, feature
  detection, portable guard subset, generated bytecode level, and upgrade
  cadence.
- [ ] **G100 — Gap — debugging metadata.** Define source locations, inlined frames,
  generated code, erased specifications, effect handlers, and dictionary frames
  in traces and tooling.

## 12. Standard library contract

- [ ] **G101 — Gap — minimum prelude.** Freeze core types, constructors, functions,
  traits, effects, and automatic imports.
- [ ] **P102 — Partial — collection protocols.** Specify list, map, set, iterator,
  stream, fold, traversal, builder, and early-termination contracts, including
  complexity.
- [ ] **P103 — Partial — outcome types.** Define `Option`, `Result`, validation, panic,
  and process failure without conflating their behavior.
- [ ] **G104 — Gap — text and binary model.** Define Unicode scalar values, graphemes,
  indexing, slicing, normalization, encoding conversion, interpolation, and
  binary pattern matching.
- [ ] **G105 — Gap — numeric library.** Define integer ranges or arbitrary precision,
  floating-point behavior, decimal support, conversions, parsing, and checked
  arithmetic.
- [ ] **G106 — Gap — environmental effects.** Define standard capabilities for I/O,
  files, network, time, randomness, environment, logging, and process control.
- [ ] **P107 — Partial — category-inspired API names.** Normative 0.1.4 chooses the
  canonical behavior-first trait and method ABI and confines formal names to
  reference metadata. Independent comprehension and usability validation is
  still required.
- [ ] **G108 — Gap — stability and performance policy.** State which APIs, laws,
  traversal orders, asymptotic bounds, and representations are compatibility
  promises.

## 13. Specifications, governance, and erasure

- [ ] **P109 — Partial — surface grammar.** Freeze syntax for claims, evidence,
  assumptions, governed scopes, policy, authorization, decisions, and
  transitions. Normative 0.1.6 freezes semantic JSON forms but intentionally
  leaves public parser punctuation open.
- [x] **C110 — Complete — checking language.** Normative 0.1.6 fixes an explicitly
  typed pure fragment, exact integer, Boolean, and nested-tuple examples,
  deterministic left-to-right evaluation, distinct failure outcomes, and a
  fixed 20,000-step bound. The compiler and independent tests enforce the
  typing, purity, dependency, and budget boundaries.
- [x] **C111 — Complete — enforcement modes.** Normative 0.1.6 selects optional
  package adoption, separate specification and governance adoption, additive
  package-to-subject scopes, inherited dependency claims, fail-closed policy,
  and distinct `build`, `publish`, and `activate` gates.
- [x] **C112 — Complete — evidence lifecycle.** Normative 0.1.6 binds compiler
  evidence, signed attestations, and explicit assumptions to exact claim,
  subject, tool, artifact, role, and logical sequence identities. Revocation,
  delegation, replacement, and hash-chained lifecycle replay have executable
  positive and adversarial coverage.
- [x] **C113 — Complete — erasure semantics.** Normative 0.1.6 forbids runtime
  reachability and export of verification-only definitions, erases the
  specification graph before Erlang Abstract Format, and requires complete
  accounting plus byte-identical package BEAM artifacts with and without fully
  discharged specifications. Runtime monitors are outside this version.
- [x] **C114 — Complete — artifact format.** Normative 0.1.6 fixes strict JCS,
  SHA-256, domain-separated Ed25519 signatures, trust-root, governance-bundle,
  and assurance-manifest formats, exact multi-module artifact binding, staged
  output transactions, and an external-signer payload.
- [x] **C115 — Complete — governance identity and trust roots.** Normative 0.1.6
  fixes offline principals, distinct-actor role thresholds, scoped delegation,
  revocation, old-and-new normal rotation, predeclared recovery, and historical
  root replay. Transparency services and network identity are excluded from
  the bounded offline protocol and remain possible later additions.
- [ ] **G116 — Gap — long-term evolution.** Define schema migration, policy-version
  interpretation, archived evidence, reproducible historical decisions, and
  compatibility with newer compilers.

## 14. Diagnostics, tools, and developer experience

- [ ] **P117 — Partial — diagnostic contract.** C008 adds explicit
  error/warning severity, stable `EDN`, `PRV`, and `DEP` families,
  deterministic details, ordered structured edits, and warning denial. Define
  secondary locations, inferred-type presentation, constraint provenance,
  missing-pattern witnesses, guard explanations, generated-code attribution,
  and a complete cross-language contract.
- [ ] **G118 — Gap — formatter.** Define canonical formatting, comments, idempotence,
  version coupling, and whether formatting is part of source compatibility.
- [ ] **G119 — Gap — documentation tool.** Define doc attachment, links, examples,
  doctests, hidden APIs, traits and implementations, effects, laws, and
  specification views.
- [ ] **G120 — Gap — interactive environment.** Define REPL typing and effects,
  declaration replacement, process lifetime, module loading, history, and
  governance behavior.
- [ ] **G121 — Gap — build system and package manager.** Define project discovery,
  profiles, dependency fetching, code generation, cache keys, offline builds,
  and reproducibility.
- [ ] **G122 — Gap — testing tools.** Define unit, property, model, concurrency, and
  specification tests; seeds; shrinking; timeouts; and evidence capture.
- [ ] **G123 — Gap — editor protocol.** Define incremental parsing and typing, partial
  programs, completion, hover, rename, formatting, semantic tokens, and stable
  diagnostic identity.
- [ ] **G124 — Gap — debugging and observability.** Define breakpoints, stack traces,
  handlers, processes, messages, generated derivations, erased declarations,
  tracing, profiling, and crash reports.
- [ ] **P125 — Partial — migration tools.** C008 defines conservative
  `json-edit` suggestions with explicit applicability and requires the C008
  compiler to report rather than apply them. Define transactional application,
  backups, rollback, source rewrites, API refactors, and deprecated-syntax
  handling.

## 15. Security, reproducibility, and operational limits

- [ ] **G126 — Gap — trusted computing base.** Enumerate parser, type checker, trait
  solver, effect checker, proof kernel, serializer, signer, runtime, and foreign
  components whose bugs can violate guarantees.
- [ ] **G127 — Gap — unsafe-code policy.** Define whether unsafe operations exist,
  where they may appear, what obligations they assume, and how artifacts expose
  them.
- [ ] **G128 — Gap — reproducible builds.** Define environmental inputs, timestamps,
  path normalization, dependency integrity, generated files, compiler version,
  and byte-for-byte expectations.
- [ ] **G129 — Gap — resource exhaustion.** Define compiler limits, runtime memory and
  mailbox pressure, recursion, unbounded type search, denial-of-service risks,
  and required diagnostics or controls.
- [ ] **G130 — Gap — supply-chain policy.** Define package signing, provenance,
  compromised releases, yanks, lockfiles, native dependencies, and governance
  evidence.
- [ ] **G131 — Gap — secrets and capabilities.** Define how credentials and ambient VM
  authority enter programs without being hidden by effects, build scripts, or
  specification evaluation.

## 16. Formal validation and release gates

- [ ] **P132 — Partial — progress and preservation targets.** C002 states the
  nominal and structural claims; C003 adds condition typing, closed
  safety, predicate expansion, fallthrough, commitment, guarded exhaustive
  progress, fact soundness, lowering equivalence, receive preservation, and
  evidence-erasure targets. Effects, public processes, foreign values, and the
  integrated theorem remain open.
- [ ] **P133 — Partial — reference evaluator.** The executable oracle now covers
  C001 pure expressions, C002 nominal matching and folds, and C003
  primitive conditions, lazy Boolean composition, predicate calls, and ordered
  fallthrough. Effects, processes, foreign values, explicit failures, and the
  remaining language forms are not yet modeled.
- [ ] **P134 — Partial — differential testing.** C002 compares reference,
  uniform-layout, and compact-layout observations; C003 compares the
  reference evaluator with forced native and ordinary BEAM condition lowering.
  Effects, failures, traces, public concurrency, foreign values, and resource
  scopes remain open.
- [ ] **G135 — Gap — optimizer validity.** Identify which rewrites rely on pure
  semantics, trait laws, evaluation order, totality, or trusted evidence and
  reject rewrites whose premises are absent.
- [ ] **P136 — Partial — compatibility suite.** C008 tests retained
  exact pins, neutral interfaces, selection-bound manifests, historical 0.1.6
  signature domains, and 0.1.7 downgrade/substitution rejection. Extend this
  to public signatures, data evolution, package resolution, OTP versions, hot
  upgrades, ecosystem-scale dependency graphs, and future edition boundaries.
- [ ] **G137 — Gap — usability gate.** Test whether programmers can predict `map`,
  `map2`, `and_then`, traversal, handlers, guards, comprehensions, and
  diagnostics without prerequisite mathematical vocabulary.
- [ ] **G138 — Gap — performance envelope.** Benchmark direct calls, traits, ADTs,
  pattern matching, guards, comprehensions, effects, processes, erasure, code
  size, compile time, and diagnostic provenance.
- [ ] **G139 — Gap — release-readiness definition.** State the minimum normative
  chapters, conformance coverage, platform support, known limitations, and
  stability promises required before calling a version complete.
- [ ] **G141 — Gap — compiler self-hosting.** Define the late-0.x milestone at
  which Catena can implement its own compiler, including the required language
  subset, parser and module facilities, tool effects, host interoperability,
  bootstrap trust, stage-one and stage-two builds, fixed-point or semantic
  equivalence checks, reproducibility, rollback, distribution, and the
  retained OTP 29 Abstract Format boundary. Elixir remains the bootstrap
  implementation through C008; changing the implementation language
  does not change Catena's BEAM-only target.

## Suggested research order

The checklist is too broad to turn into independent deep dives all at once.
The following order resolves dependencies first:

1. **Surface and dynamic kernel:** lexical grammar, expression grammar,
   evaluation order, failures, and core pattern contexts.
2. **Modules and execution boundary:** names, signatures, packages, entry
   points, separate compilation, and BEAM calling conventions.
3. **Collections and iteration:** concrete collection model, iterator protocol,
   list comprehensions, generator failure, effect order, and lowering.
4. **Effects and runtime scopes:** exceptions, cleanup, cancellation,
   processes, selective receive, and supervision.
5. **Interoperability and standard library:** BEAM values, Erlang calls, text,
   numerics, environmental effects, and compatibility policy.
6. **Normative consolidation:** combine existing type, ADT, guard, trait,
   effect, and governance research into a versioned reference plus tests.
7. **Tooling and release gates:** formatter, documentation, REPL, package and
   build tools, diagnostics, conformance, security, and performance.

## Connections

- The [Catena Language Overview](../language-overview.md) supplies the current
  architecture and its explicit open design boundaries; this checklist expands
  those boundaries into reviewable specification obligations.
- [A Greenfield Type System for Catena](../20-notes/catena-greenfield-type-system.md)
  constrains the type-system and elaboration items but remains a design
  synthesis rather than a normative reference.
- [Algebraic Data Types](../20-notes/algebraic-data-types.md) and
  [Clause Guards](../20-notes/clause-guards.md) constrain patterns, coverage,
  failure, and selective receive, including several decisions needed by
  comprehension qualifiers.
- [Combinators for Algebraic Data and Categorical Programming](../20-notes/combinators-for-algebraic-data-and-categorical-programming.md)
  supplies the operations to which comprehensions might lower, while leaving
  their surface syntax and operational equivalence unspecified.
- [Algebraic Effects and Handlers](../20-notes/algebraic-effects-and-handlers.md)
  constrains comprehension effects, generators, cancellation, and resource
  scopes without defining those features completely.
- [Language-Integrated Specifications and Governance](../20-notes/language-integrated-specifications-and-governance.md)
  supplies the assurance architecture that a complete language reference must
  eventually express normatively.

## Promotion criterion

After review, split this capture into a selective specification-roadmap map and
focused inquiries for the highest-priority gaps. Archive or remove the inbox
copy once every retained item has an owner, destination, and explicit initial
language boundary.
