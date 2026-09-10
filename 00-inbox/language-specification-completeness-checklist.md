---
title: "Catena Language Specification Completeness Checklist"
kind: note
created: "2026-08-01"
maturity: developing
tags:
  - catena
  - language-design
  - specification
aliases:
  - "Catena missing specification checklist"
---

# Catena Language Specification Completeness Checklist

> Current work-ahead ledger for completing the language definition. This is
> an audit and planning document, not normative language authority or a
> commitment to implement every feature listed.

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

### Audited status and evidence boundary

The [6 September 2026 audit](../50-journal/2026-09-06-checklist-completion-audit.md)
checks this ledger against the normative archive and the sibling `../catena`
implementation at commit `d7e0fcc484d3e1c3b4a292d4d3e703ddcc330535`,
which supports exact revisions through `0.1.48`. The next unused semantic
patch is `0.1.49`; this audit introduces no language revision.

A checkbox records the full stated item's completion, including its required
verification. A normative chapter, passing suite, or obligation tag alone
is insufficient when its required behavioral witness is missing or its rules
conflict. Conversely, a defined exclusion or an implemented bounded contract
can be complete without a general-purpose parser: P109 owns source adoption.
Whole-language composition proofs and release readiness remain separate work.

The numeric suffix is the permanent item identity. Current owner references
use the status prefix below; historical promotion records, immutable test
names, and machine-profile strings may retain their recorded prefix. Dated
journals and snapshots are historical evidence, not current status summaries.

The current checkboxes total **127 complete, 6 partial, 6 gaps, and 2
deferred: 141 items**. Counts measure item coverage, not remaining effort.
The audit reopened four formerly checked items (P050/P053/P057/P086); C086
is restored by the 8 September correction at `0.1.49`. The current next unused
semantic patch is `0.1.90`; the closed target at `0.1.50` restores C050. In the audit, 22 gaps
are reclassified as partial because bounded work already exists. No new
item is marked complete by this audit.

| Section | Complete | Partial | Gap | Deferred | Total |
| --- | ---: | ---: | ---: | ---: | ---: |
| Research foundations | 6 | 0 | 0 | 0 | 6 |
| 1. Specification form and conformance | 6 | 0 | 0 | 0 | 6 |
| 2. Lexical grammar and source files | 8 | 0 | 0 | 0 | 8 |
| 3. Names, modules, packages, and separate compilation | 8 | 0 | 0 | 0 | 8 |
| 4. Core expressions and evaluation | 10 | 0 | 0 | 0 | 10 |
| 5. Data, collections, and patterns | 8 | 0 | 0 | 0 | 8 |
| 6. List comprehensions, generators, and iteration | 12 | 0 | 0 | 1 | 13 |
| 7. Type-system surface and advanced boundaries | 10 | 0 | 0 | 0 | 10 |
| 8. Traits, derivation, and categorical libraries | 7 | 0 | 0 | 0 | 7 |
| 9. Effects, failure, and resource scopes | 7 | 0 | 0 | 1 | 8 |
| 10. Processes, concurrency, and distribution | 9 | 0 | 0 | 0 | 9 |
| 11. BEAM representation and Erlang interoperability | 7 | 1 | 0 | 0 | 8 |
| 12. Standard library contract | 6 | 2 | 0 | 0 | 8 |
| 13. Specifications, governance, and erasure | 7 | 1 | 0 | 0 | 8 |
| 14. Diagnostics, tools, and developer experience | 2 | 3 | 4 | 0 | 9 |
| 15. Security, reproducibility, and operational limits | 6 | 0 | 0 | 0 | 6 |
| 16. Formal validation and release gates | 5 | 0 | 4 | 0 | 9 |
| **Total** | **124** | **7** | **8** | **2** | **141** |

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
Normative C021 uses `0.1.17` for namespaces and shadowing. Its inventory,
shadowing and ambiguity rules, diagnostics, and verification are recorded
in the
[C021 conformance journal](../50-journal/2026-08-22-c021-namespaces-and-shadowing.md).
Normative C022 uses `0.1.18` for imports and exports. Its export and
admission rules, exclusions, diagnostics, and verification are recorded in
the
[C022 conformance journal](../50-journal/2026-08-22-c022-imports-and-exports.md).
Normative C023 uses `0.1.19` for abstraction boundaries. Its authority
and representation exclusions, sanctioned idiom, and verification are
recorded in the
[C023 conformance journal](../50-journal/2026-08-23-c023-abstraction-boundaries.md).
Normative C024 uses `0.1.20` for module dependency cycles. Its SCC
admission, resolution regimes, joint digests, and verification are
recorded in the
[C024 conformance journal](../50-journal/2026-08-24-c024-dependency-cycles.md).
Normative C025 uses `0.1.21` for package identity and dependency
resolution. Its dependency grammar, resolution, lockfile, identity, and
verification are recorded in the
[C025 conformance journal](../50-journal/2026-08-24-c025-package-identity.md).
Normative C026 uses `0.1.22` for the prelude. Its selection, precedence,
opt-out, edition guarantee, and verification are recorded in the
[C026 conformance journal](../50-journal/2026-08-24-c026-prelude-policy.md).
Normative C027 uses `0.1.23` for entry points. Its entry declarations,
derived libraries, launch semantics, shutdown reports, and verification
are recorded in the
[C027 conformance journal](../50-journal/2026-08-24-c027-entry-points.md).
Normative C028 uses `0.1.24` for API and ABI compatibility. Its layer
stances, breaking matrix, claim validation, and verification are
recorded in the
[C028 conformance journal](../50-journal/2026-08-24-c028-api-compat.md).
Normative C029 uses `0.1.25` for values and evaluation. Its value
grammar, strictness invariant, terminal contract, and verification are
recorded in the
[C029 conformance journal](../50-journal/2026-08-24-c029-values.md).
Normative C030 uses `0.1.26` for evaluation order. Its ordered-forms
table, entry rule, trace observability, and verification are recorded
in the
[C030 conformance journal](../50-journal/2026-08-25-c030-evaluation-order.md).
Normative C031 uses `0.1.27` for bindings and sequencing. Its binding
structure, sequencing idiom, `BS001` warning, and verification are
recorded in the
[C031 conformance journal](../50-journal/2026-08-25-c031-bindings.md).
Normative C032 uses `0.1.28` for functions and calls. Its arity model,
capture discipline, local functions, tail guarantee, and verification
are recorded in the
[C032 conformance journal](../50-journal/2026-08-25-c032-functions.md).
Normative C033 uses `0.1.29` for conditionals and branching. Its
branch form, sugar promise, consolidated rules, statement absence, and
verification are recorded in the
[C033 conformance journal](../50-journal/2026-08-25-c033-branching.md).
Normative C035 uses `0.1.30` for equality and ordering. Its comparable
set, float semantics, guard split, and verification are recorded in
the
[C035 conformance journal](../50-journal/2026-08-26-c035-equality.md).
Normative C034 uses `0.1.31` for recursion and termination. Its
unrestricted stance, separation table, entry rule, and verification
are recorded in the
[C034 conformance journal](../50-journal/2026-08-26-c034-recursion.md).
Normative C036 uses `0.1.32` for the runtime failure taxonomy. Its
single outcome, category mapping, entry rule, and verification are
recorded in the
[C036 conformance journal](../50-journal/2026-08-26-c036-failure.md).
Normative C037 uses `0.1.33` for resource observability. Its six-way
classification, identity rule, finalization gate, and verification
are recorded in the
[C037 conformance journal](../50-journal/2026-08-26-c037-observability.md).
Normative C038 uses `0.1.34` for compile-time evaluation. Its stance,
derivations classification, restriction table, and verification are
recorded in the
[C038 conformance journal](../50-journal/2026-08-26-c038-compile-time.md).
Normative C040 uses `0.1.35` for the built-in data model. Its
classification, type elaboration, comparability entries, and
verification are recorded in the
[C040 conformance journal](../50-journal/2026-08-29-c040-data-model.md).
Normative C041 uses `0.1.36` for structural records and variants.
Its operation table, row model, representation clause, and
verification are recorded in the
[C041 conformance journal](../50-journal/2026-08-29-c041-records.md).

## Consolidated research foundations

These six research areas have versioned normative contracts and bounded
implementation evidence. Their remaining extensions have separate owners below.

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
  traces. Cleanup and scoped control remain G080/D083; C081/C082 subsequently
  define exception and top-level boundaries; C106 supplies environmental APIs.
  Performance/usability G138/G137 remain open.
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
  obligations at that milestone; the registry now covers every later
  specification area as well. Its evidence-status counts are maintained
  separately from compiler obligation-tag coverage. The
  [resolved inquiry](../40-inquiries/how-should-catena-achieve-exhaustive-rule-to-test-traceability.md)
  and [C011 record](../50-journal/2026-08-12-c011-executable-conformance-suite.md)
  record the coordinated compiler PRs (#76–#87) and the immutable compiler
  identity. The milestone's twenty untraced registry obligations were not
  the whole compiler allowlist: partial and transitive evidence also appears
  in those gates. The current audit records both counts and checks the
  substance of tagged tests; C011 completes the traceability mechanism,
  not exhaustive behavioral or proof coverage.
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
  remains deployment-defined under C084/C129/P085 without permitting silent
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
  fixes the file-to-module relationship; C021 fixes namespaces and
  shadowing; and C022 fixes imports and exports.
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
  retains declaration grammar; P119/G118
  retain rendering/formatting; P119 retains actual doctest execution.
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
  `LT-OBL-001`–`LT-OBL-012` coverage with 233 passing tests. C040/C041/C042 subsequently classify data, structural operations, and
  collection construction. Concrete source adoption remains P109; C102 supplies collection
  protocols while P101 retains prelude admission, and C093/C097 supply foreign/native data; negation spelling and the token
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
  tests. C061 subsequently fixes primitive numeric relationships, C035
  comparison, and C036 failure categories. Explicit conversions and numeric
  library operations are defined by C105, including each fault producer's policy.
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
  relations are complete as C020, namespace resolution as C021, and
  imports and exports as C022. C041 defines record selection and C061
  primitive operator instantiation; their source adoption remains P109,
  and editor recovery G123.
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
  syntax remains P109; module-name resolution is fixed by C021 and
  import/export admission by C022; package
  assembly is defined by C025 and entry declarations by C027.

## 3. Names, modules, packages, and separate compilation

- [x] **C021 — Complete — namespaces and shadowing.** The normative
  [0.1.17 namespaces specification](../60-specification/namespaces-and-shadowing/README.md),
  [synthesis](../20-notes/catena-namespaces-and-shadowing.md),
  [resolved inquiry](../40-inquiries/how-should-catena-organize-namespaces-and-shadowing.md),
  [topic map](../10-maps/namespaces-and-shadowing.md), and
  [C021 record](../50-journal/2026-08-22-c021-namespaces-and-shadowing.md) fix
  per-category namespaces under the hard spelling-class partition with
  per-category uniqueness domains and flat constructor uniqueness; silent
  innermost-wins shadowing that never crosses categories; quantifier-scoped
  type variables that may shadow type and trait names; local-over-imported
  precedence with order-independent `NSP004` ambiguity rejection naming
  every origin; governed-identity separation keeping C006 identities out of
  program resolution; and exactly-two-segment qualification with deeper
  chains reserved. Sibling compiler commit
  [`b482b4cacc4017b8e479173fb3bd3c0ceac4f675`](https://github.com/pcharbon70/catena/commit/b482b4cacc4017b8e479173fb3bd3c0ceac4f675)
  supplies complete `NS-OBL-001`–`NS-OBL-014` coverage with 285 passing
  tests through the abstract scope-event resolver, extended by C022.
  C024 subsequently defines module recursion, C025 package assembly,
  C026 prelude selection, and C066 type-independent name resolution.
  Prelude contents remain P101 and source punctuation P109.
- [x] **C022 — Complete — imports and exports.** The normative
  [0.1.18 imports specification](../60-specification/imports-and-exports/README.md),
  [synthesis](../20-notes/catena-imports-and-exports.md),
  [resolved inquiry](../40-inquiries/how-should-catena-handle-imports-and-exports.md),
  [topic map](../10-maps/imports-and-exports.md), and
  [C022 record](../50-journal/2026-08-22-c022-imports-and-exports.md) fix
  private-by-default explicit exports carrying C002 transparency modes
  with `EXP001` undeclared rejection; import admission through
  two-segment qualification against digest-bound export sets plus explicit
  possibly-empty unqualified name lists with `IMP002`/`IMP003` validation;
  the declared exclusion of wildcards, hiding, renaming, and aliases; the
  re-export exclusion since re-owned by C025 to the C028 compatibility
  era; and the deny-able `IMP001` unused-import warning whose
  qualified references never satisfy unqualified admissions. Sibling
  compiler commit
  [`02da5c178ad5d797e55bdb3290cd950fbf7f4f31`](https://github.com/pcharbon70/catena/commit/02da5c178ad5d797e55bdb3290cd950fbf7f4f31)
  supplies complete `IM-OBL-001`–`IM-OBL-013` coverage with 295 passing
  tests through the extended scope-event resolver, with C023 confirming
  the transparency vocabulary complete and C024 admitting cyclic event
  graphs over the same resolver. C025 subsequently fixes package identity, C028 excludes re-export
  facades, C026 fixes prelude selection, and C027 fixes entry declarations; concrete `use`/`export`
  punctuation remains P109.
- [x] **C023 — Complete — abstraction boundaries.** The normative
  [0.1.19 abstraction specification](../60-specification/abstraction-boundaries/README.md),
  [synthesis](../20-notes/catena-abstraction-boundaries.md),
  [resolved inquiry](../40-inquiries/how-should-catena-draw-its-abstraction-boundaries.md),
  [topic map](../10-maps/abstraction-boundaries.md), and
  [C023 record](../50-journal/2026-08-23-c023-abstraction-boundaries.md)
  confirm the transparent/abstract pair as the complete
  constructor-authority vocabulary on every frontend; declare that no
  stable-layout opt-in exists in edition 0.1 with both-layout conformance
  mandatory, `L001` unchanged, and C028 owning any future
  layout-stability contract together with P093/P094/C095; exclude
  selective construction/matching authority and views as extensions excluded by C046 and subject to its explicit
  arrival conditions; and sanction the abstract-type-plus
  validating-constructor-plus-observer invariant idiom with typed failure
  and wildcard-plus-observers coverage for abstract scrutinees. Sibling
  compiler commit
  [`bbce0ee25fe6f8b64204a4ec757dc6d281d63f9f`](https://github.com/pcharbon70/catena/commit/bbce0ee25fe6f8b64204a4ec757dc6d281d63f9f)
  supplies complete `AB-OBL-001`–`AB-OBL-007` exclusion-proof and idiom
  coverage with 303 passing tests, including key-whitelisted export
  events that reject layout attributes as invalid. Module recursion is
  subsequently admitted by C024.
- [x] **C024 — Complete — dependency cycles.** The normative
  [0.1.20 cycles specification](../60-specification/module-dependency-cycles/README.md),
  [synthesis](../20-notes/catena-dependency-cycles.md),
  [resolved inquiry](../40-inquiries/how-should-catena-handle-module-dependency-cycles.md),
  [topic map](../10-maps/module-dependency-cycles.md), and
  [C024 record](../50-journal/2026-08-24-c024-dependency-cycles.md) admit
  module dependency cycles: maximal strongly-connected components are the
  units of checking, resolution, and caching; intra-component references
  resolve against companions' declared signatures with digest-free
  imports while regime mixing and signature gaps are `CYC001` at the
  closing transaction; cross-component imports stay digest-bound as C022
  fixed them; components receive one deterministic member-order- and
  layout-invariant joint digest; initialization is definition-only with
  per-component loading and no top-level evaluation; inference checks
  each member independently; and dependency inversion is the sanctioned
  non-cyclic alternative. Sibling compiler commit
  [`ca2be792e3f5fe081c67ec7ca9e845d40a5087c0`](https://github.com/pcharbon70/catena/commit/ca2be792e3f5fe081c67ec7ca9e845d40a5087c0)
  supplies complete `CY-OBL-001`–`CY-OBL-010` coverage with 312 passing
  tests through the abstract SCC grouping and `Catena.compile_scc/2`.
  Package assembly and lockfile representation are subsequently fixed by
  C025; the concrete
  recursive surface remains P109; C028 classifies joint digests as identity
  rather than an independent compatibility promise.
- [x] **C025 — Complete — package identity and dependency resolution.**
  The normative
  [0.1.21 package specification](../60-specification/package-identity-and-dependencies/README.md),
  [synthesis](../20-notes/catena-package-identity-and-dependencies.md),
  [resolved inquiry](../40-inquiries/how-should-catena-define-package-identity-and-dependency-resolution.md),
  [topic map](../10-maps/package-identity-and-dependencies.md), and
  [C025 record](../50-journal/2026-08-24-c025-package-identity.md) fix
  the optional manifest `dependencies` field; the SemVer 2.0.0 grammar
  and precedence; exact/caret/tilde requirements with the Cargo 0.x rule
  and pre-release operand restriction; single-version
  highest-satisfying order-independent resolution with `PKG002`/`PKG003`/
  `PKG004` rejection; the generated `catena.lock` with exact-pin replay
  and `PKG005` stale/tamper separation; and registry-neutral (name,
  version, SHA-256 bundle digest) identity over manifest semantics plus
  member interface and C024 component digests, with hex.pm as the
  bootstrap transport profile. Sibling compiler commit
  [`dcd7da056ba1317fcd7df1df8716981ff8363e1d`](https://github.com/pcharbon70/catena/commit/dcd7da056ba1317fcd7df1df8716981ff8363e1d)
  supplies complete `PK-OBL-001`–`PK-OBL-012` coverage with 323 passing
  tests through the `Catena.Package.Deps` engine. Build and fetch
  tooling are completed by C121; reproducible-build consumption remains P128;
  registry signing and threat modeling are completed by C130. C028 subsequently fixes
  compatibility and excludes re-export facades; C026 fixes prelude selection.
- [x] **C026 — Complete — prelude policy.**
  The normative
  [0.1.22 prelude specification](../60-specification/prelude-policy/README.md),
  [synthesis](../20-notes/catena-prelude-policy.md),
  [resolved inquiry](../40-inquiries/how-should-catena-define-its-prelude-policy.md),
  [topic map](../10-maps/prelude-policy.md), and
  [C026 record](../50-journal/2026-08-24-c026-prelude-policy.md) fix
  the opt-in manifest `prelude` selection of one package and
  requirement; admission of the resolved package's exports as an
  ordinary import-class origin under unchanged C021 precedence with
  `NSP004` collisions naming both origins; absent/`null` as the complete
  opt-out with no sentinel or per-name hiding; the zero-implicit-names
  edition guarantee with lifecycle-record path for any future default;
  and prelude resolution, locking, and replay as ordinary C025
  dependencies with marked requirers and bundle digests. Sibling
  compiler commit
  [`484d797a33eaf580f2c43ddd0776c6675078c4f9`](https://github.com/pcharbon70/catena/commit/484d797a33eaf580f2c43ddd0776c6675078c4f9)
  supplies complete `PL-OBL-001`–`PL-OBL-010` coverage with 332 passing
  tests through the manifest decoder, namespace builder, and
  `Catena.Package.Deps` wiring. Prelude contents and the name freeze
  remain P101; collection protocols are C102; tooling scaffolding
  is completed by C121. C028 classifies prelude version changes; integrated
  bounded compatibility-suite coverage is C136.
- [x] **C027 — Complete — entry points and application structure.**
  The normative
  [0.1.23 entry points specification](../60-specification/entry-points/README.md),
  [synthesis](../20-notes/catena-entry-points.md),
  [resolved inquiry](../40-inquiries/how-should-catena-define-entry-points-and-application-structure.md),
  [topic map](../10-maps/entry-points.md), and
  [C027 record](../50-journal/2026-08-24-c027-entry-points.md) fix
  the optional manifest `entries` array naming existing zero-argument,
  total, effect-closed exports with recorded result spellings and at
  most one launch marker; libraries derived from zero declared entries
  with absent/`null`/`[]` equivalence and no kind flag; invocation-only
  launch under unchanged strict kernel semantics that introduces no
  scope and spawns no process; return-is-shutdown reports carrying the
  entry's value or the trap identity; and `ENT001`–`ENT003` stable
  diagnostics with `PKG001`/`EDN001` reused unchanged. Sibling compiler
  commit
  [`cd0e5c543ee7ddb7ca840c6657451e3b6c21d7c5`](https://github.com/pcharbon70/catena/commit/cd0e5c543ee7ddb7ca840c6657451e3b6c21d7c5)
  supplies complete `EN-OBL-001`–`EN-OBL-010` coverage with 342 passing
  tests through the manifest decoder, package linker validation, and
  `Catena.Entry.launch/2`. Supervision and process lifetime are
  C084/C089; cancellation remains C088; CLI and host-process boundaries
  are completed by C121; distribution and upgrades are C091/C092. C028
  subsequently fixes entry-set compatibility.
- [x] **C028 — Complete — API and ABI compatibility.**
  The normative
  [0.1.24 compatibility specification](../60-specification/api-and-abi-compatibility/README.md),
  [synthesis](../20-notes/catena-api-and-abi-compatibility.md),
  [resolved inquiry](../40-inquiries/how-should-catena-define-api-and-abi-compatibility.md),
  [topic map](../10-maps/api-and-abi-compatibility.md), and
  [C028 record](../50-journal/2026-08-24-c028-api-compat.md) fix
  the four compatibility layers — real source and interface rules with
  declared behavior (the kernel is the contract, no bug-compatibility)
  and BEAM ABI (representation is not a surface) absences; version
  meanings — breaking requires SemVer major at 1.0.0+ and minor below
  it under the Cargo 0.x rule C025 already fixed for operators, with
  edition bumps as the language-level instrument; the strict breaking
  matrix over decoded interfaces — removals, renames, scheme changes,
  and effect-row widening breaking, additions minor, representation
  never breaking alone, entry additions minor and removals or result
  changes breaking; the formal re-export facade exclusion closing the
  C022/C025 deferral; joint and bundle digests as identity-only; and
  claim validation with `CMP001`–`CMP003` stable diagnostics.
  Sibling compiler commit
  [`0d96f96792aa161ed2711edb304d75e4cee54af2`](https://github.com/pcharbon70/catena/commit/0d96f96792aa161ed2711edb304d75e4cee54af2)
  supplies complete `CP-OBL-001`–`CP-OBL-010` coverage with 355 passing
  tests through the `Catena.Package.Compat` classifier. Migration
  engines remain P116/P125; registry retirement and yanks are fixed by C130;
  hot upgrade remains G092; representation, calling-convention, and
  foreign-term contracts remain P093/P094/C095; tooling automation
  is completed by C121. C136 retains the 0.x convention and leaves any
  post-prototype policy to a later explicit edition decision.

## 4. Core expressions and evaluation

- [x] **C029 — Complete — value and evaluation definition.**
  The normative
  [0.1.25 values specification](../60-specification/values-and-evaluation/README.md),
  [synthesis](../20-notes/catena-values-and-evaluation.md),
  [resolved inquiry](../40-inquiries/what-are-catenas-values-and-strictness.md),
  [topic map](../10-maps/values-and-evaluation.md), and
  [C029 record](../50-journal/2026-08-24-c029-values.md) fix
  the closed ten-form value grammar — the kernel's integer, Boolean,
  Unit, tuple, closure, constructor-value, record, injection, and
  opaque process-handle forms plus Float with C018 semantics
  unchanged — with the closed non-value list (evidence, handler
  declarations, capability names, resumptions, traps, effect rows,
  signatures); uniform first-classness with C037/P085 observability
  named as exclusions; the C040 entry rule for future types; the
  strictness invariant — every subexpression evaluates at most once,
  to a value or a terminal trap, before use — with the kernel's
  `and`/`or` skips as the only named exceptions and an edition-record
  gate for any future lazy form; and value-or-trap terminal outcomes
  with suspended requests as pending continuations. Sibling compiler
  commit
  [`f8d8fa96e536df9b7ff00db246d8817f39b1c381`](https://github.com/pcharbon70/catena/commit/f8d8fa96e536df9b7ff00db246d8817f39b1c381)
  supplies complete `VA-OBL-001`–`VA-OBL-008` coverage with 366 passing
  tests through the `Catena.Values` classifier and stepper terminal
  witnesses. The slice is definitional: zero new diagnostic families.
  C030–C038 subsequently define order, bindings, calls, branching,
  equality, recursion, failures, observability, and compile-time evaluation;
  C040 adds Text/Character/Bytes meanings. Full source adoption remains P109.
- [x] **C030 — Complete — evaluation order.**
  The normative
  [0.1.26 order specification](../60-specification/evaluation-order/README.md),
  [synthesis](../20-notes/catena-evaluation-order.md),
  [resolved inquiry](../40-inquiries/when-does-each-subexpression-evaluate.md),
  [topic map](../10-maps/evaluation-order.md), and
  [C030 record](../50-journal/2026-08-25-c030-evaluation-order.md) fix
  the closed ordered-forms table — the kernel's list elevated verbatim
  plus the typed-core completions: curried multi-argument application
  as repeated unary left-to-right, trait-call subject then arguments,
  handler installation before body, annotate transparency — with the
  future-form entry rule (collections, interpolation, and C040
  compounds declare their order in their own slices), the
  order-versus-structure boundary against C031/C032, and trace
  observability: a conforming implementation's effect-request trace
  equals the declared order's trace, generalizing C004's traversal and
  C005's handler-order rules, with reference-evaluator and
  compiled-BEAM traces agreeing per program. Sibling compiler commit
  [`5e1e8948249701a45029379e604b7aa0e8376e92`](https://github.com/pcharbon70/catena/commit/5e1e8948249701a45029379e604b7aa0e8376e92)
  supplies complete `EO-OBL-001`–`EO-OBL-008` coverage with 377 passing
  tests through dual-target trace agreement. The slice is definitional:
  no new public API and zero new diagnostic families. C031/C032/C033 subsequently fix binding structure, currying, and
  branching; C040/C041 fix further data operations. P109 owns source adoption.
- [x] **C031 — Complete — bindings and sequencing.**
  The normative
  [0.1.27 bindings specification](../60-specification/bindings-and-sequencing/README.md),
  [synthesis](../20-notes/catena-bindings-and-sequencing.md),
  [resolved inquiry](../40-inquiries/how-should-catena-define-bindings-and-sequencing.md),
  [topic map](../10-maps/bindings-and-sequencing.md), and
  [C031 record](../50-journal/2026-08-25-c031-bindings.md) fix
  the binding account: local `let` is strictly non-recursive (a
  self-referential RHS is `T001` unbound) with plain value-name
  binders and substitute-after-value timing; scope is
  sequential-lexical with silent innermost-wins shadowing of any
  in-scope name (C021 restated); recursion is definitions-only — the
  kernel's signed environment with C024's SCC as mutual recursion's
  home; an unused binding stays valid with its RHS effects preserved;
  the deny-able `BS001` warning fires exactly on non-`_`-prefixed
  binders never occurring in their body, with manifest deny promotion;
  and `let _ = e1; e2` is the normative sequencing form. Sibling
  compiler commit
  [`17b5be7b1bce9cd6a4603b9d6b6f5f5d8060951b`](https://github.com/pcharbon70/catena/commit/17b5be7b1bce9cd6a4603b9d6b6f5f5d8060951b)
  supplies complete `BS-OBL-001`–`BS-OBL-008` coverage with 387
  passing tests through the `Catena.Bindings` warning walk, dual
  evaluator/BEAM traces, and kernel recursion witnesses. C032/C033/C034 subsequently fix functions, branching, and recursion;
  C044 constrains pattern-binding positions, whose surface forms remain P109.
- [x] **C032 — Complete — functions and calls.**
  The normative
  [0.1.28 functions specification](../60-specification/functions-and-calls/README.md),
  [synthesis](../20-notes/catena-functions-and-calls.md),
  [resolved inquiry](../40-inquiries/what-is-catenas-function-and-call-model.md),
  [topic map](../10-maps/functions-and-calls.md), and
  [C032 record](../50-journal/2026-08-25-c032-functions.md) fix
  the function model: every function is semantically unary with
  multi-parameter definitions as nested-unary sugar and multi-argument
  calls as repeated unary application under C030's order — no arity
  mismatch exists to diagnose; any prefix application is a
  first-class closure value (free partial application); capture is
  lexical and immutable with allocation identity C037's exclusion;
  the let-bound closure is the local-function form under all of
  C031's rules; named functions are definitions with C022's export
  rules; and the kernel's proper-tail-call guarantee is elevated
  verbatim. Sibling compiler commit
  [`0af785cf32de1893c9638ebd145944bdc37f52b3`](https://github.com/pcharbon70/catena/commit/0af785cf32de1893c9638ebd145944bdc37f52b3)
  supplies complete `FC-OBL-001`–`FC-OBL-008` coverage with 397
  passing tests, including curried and partial-application agreement
  on evaluator and BEAM and a five-million-iteration match-dispatched
  tail recursion completing on compiled BEAM. Zero new diagnostic
  families. C033/C034 subsequently fix branching and unrestricted
  recursion; the full calling-convention contract remains P094.
- [x] **C033 — Complete — conditionals and general branching.**
  The normative
  [0.1.29 branching specification](../60-specification/branching/README.md),
  [synthesis](../20-notes/catena-branching.md),
  [resolved inquiry](../40-inquiries/what-is-catenas-branching-model.md),
  [topic map](../10-maps/branching.md), and
  [C033 record](../50-journal/2026-08-25-c033-branching.md) fix
  the branching model: match is the single branch form (scrutinee
  once, source-order clauses, pattern-before-condition, exactly-once
  `Bool` conditions, false fallthrough, irreversible commitment,
  clause bodies unifying with the match's type, `M001` missing
  witnesses and redundancy rejection unchanged from C002); the
  conditional sugar promise fixes that any future `if` spelling
  desugars to a Bool-pattern match with shipped semantics; and
  statement-like control forms are declared absent — everything is an
  expression, effects sequence through the let idiom, and any
  exception enters through the edition-record gate. Sibling compiler
  commit
  [`221338face094ad9c9306dcf8805a75910b1d1d7`](https://github.com/pcharbon70/catena/commit/221338face094ad9c9306dcf8805a75910b1d1d7)
  supplies complete `BR-OBL-001`–`BR-OBL-008` coverage with 406
  passing tests through Bool-pattern dispatch, guarded fallthrough,
  commitment traces, and `M001` regression witnesses. Zero new
  diagnostic families. C034/C036 subsequently fix recursion and
  failures; C040/C044 classify data and pattern contexts. Spellings remain
  P109. Section 4's current status is recorded in the audited summary above.
- [x] **C034 — Complete — recursion and termination.**
  The normative
  [0.1.31 recursion specification](../60-specification/recursion-and-termination/README.md),
  [synthesis](../20-notes/catena-recursion-and-termination.md),
  [resolved inquiry](../40-inquiries/how-does-catena-separate-recursion-from-termination.md),
  [topic map](../10-maps/recursion-and-termination.md), and
  [C034 record](../50-journal/2026-08-26-c034-recursion.md) fix
  the separation: program recursion is unrestricted — divergence is
  non-termination (never a trap, never undefined behavior), the tail
  guarantee is the only stack promise, and no expression-level
  totality checking exists, with any future checker gated as an
  opt-in analysis; every meta-level evaluator is total-or-bounded by
  its own shipped mechanism (conditions acyclic with `CND004`,
  specification examples under the fixed 20,000-step checker, laws
  with bounded samples); and any recursive-total fragment — C038
  compile-time evaluation foremost — must ship with its totality-or-
  boundedness regime in its admitting slice. Sibling compiler commit
  [`252da7b287dfbfae95056fa778e0b7ce0979599f`](https://github.com/pcharbon70/catena/commit/252da7b287dfbfae95056fa778e0b7ce0979599f)
  supplies complete `RT-OBL-001`–`RT-OBL-008` coverage with 426
  passing tests through non-tail recursion at 10,000 depth on BEAM,
  the stepper's budget-exhaustion divergence witness, tail
  termination, the `CND004` regression, and the bounded-regime
  matrix. Zero new diagnostic families. C038 subsequently applies the gate to compilation; C036 fixes the
  failure taxonomy, with divergence outside it.
- [x] **C035 — Complete — equality and ordering of primitive values.**
  The normative
  [0.1.30 equality specification](../60-specification/equality-and-ordering/README.md),
  [synthesis](../20-notes/catena-equality-and-ordering.md),
  [resolved inquiry](../40-inquiries/which-values-compare-and-how.md),
  [topic map](../10-maps/equality-and-ordering.md), and
  [C035 record](../50-journal/2026-08-26-c035-equality.md) fix
  the comparison model: the closed comparable set — Int, Bool, and
  Float primitives plus structural recursion over tuples, records
  (semantic, field order irrelevant), variant injections, and
  constructor values — with ordering over Int and Float only; Float
  equality is bit-exact with `-0.0 != 0.0` and total ordering with
  `-0.0 < 0.0`, and no NaN exists under C018's finite-only contract;
  comparison is monomorphic (mixed Int/Float is the existing type
  error, no coercion); closures and process handles never compare
  (`EQN001`); guards keep C003's frozen Int/Bool fragment, enforced
  by the independent condition checker; the operators are
  non-overloadable built-ins under C061; library-level Eq/Ord naming remains P101, while C102 supplies closed semantic key-order evidence. C040
  subsequently adds Text/Character/Bytes comparison. Sibling compiler commit
  [`91c4d4929ea2fef316e44d3b1500a8854715b9be`](https://github.com/pcharbon70/catena/commit/91c4d4929ea2fef316e44d3b1500a8854715b9be)
  supplies complete `EQ-OBL-001`–`EQ-OBL-008` coverage with 417
  passing tests through the `Catena.Values` classifier
  (`comparable?/1`, `orderable?/1`, `compare/2`), tuple and
  constructor-value equality agreement on evaluator and BEAM, `EQN001`
  exclusions, monomorphism rejections, and the guard split. C037 subsequently fixes identity observability and C040 the
  Text/Character/Bytes comparison entries. Public handle extensions remain C084.
- [x] **C036 — Complete — runtime failure taxonomy.**
  The normative
  [0.1.32 failure specification](../60-specification/runtime-failure-taxonomy/README.md),
  [synthesis](../20-notes/catena-runtime-failure-taxonomy.md),
  [resolved inquiry](../40-inquiries/what-counts-as-runtime-failure.md),
  [topic map](../10-maps/runtime-failure-taxonomy.md), and
  [C036 record](../50-journal/2026-08-26-c036-failure.md) fix
  the taxonomy: `trap(reason)` is the single runtime failure outcome
  with kinded reasons (the three-way partition — values, traps,
  running — stated once); trap observability stays kernel-verbatim
  (mailbox discarded, no exit signal, no spawner effect,
  unobservable through handles, uninterceptable); the six categories
  map — explicit panic is the kernel `trap` expression, typed failure
  is an ordinary value (C103 owns the outcome types), VM
  termination is operational (C084/C092/C121), and arithmetic
  faults, assertions, and foreign exceptions are reserved kinds
  entering with their producers classified as `trap(reason)`; and the
  per-producer entry rule forbids any second outcome class. Sibling
  compiler commit
  [`22c6a437f483f5a2bb94627d3481fb51e2ce04ba`](https://github.com/pcharbon70/catena/commit/22c6a437f483f5a2bb94627d3481fb51e2ce04ba)
  supplies complete `FT-OBL-001`–`FT-OBL-008` coverage with 435
  passing tests through trap reason agreement across stepper and
  BEAM, the process-context witness (trapping child, spared spawner,
  discarded mailbox), the classifier partition, and the reserved-kind
  absences. Zero new diagnostic families. Outcome-type contents remain
  C103's; foreign calls C095/G096's; process death C084's;
  cancellation C088's.
- [x] **C037 — Complete — resource and allocation observability.**
  The normative
  [0.1.33 observability specification](../60-specification/resource-observability/README.md),
  [synthesis](../20-notes/catena-resource-observability.md),
  [resolved inquiry](../40-inquiries/what-may-programs-observe-of-resources.md),
  [topic map](../10-maps/resource-observability.md), and
  [C037 record](../50-journal/2026-08-26-c037-observability.md) fix
  the six-way classification: allocation addresses, sharing, garbage
  collection, and object identity (except process identity) are not
  observable; stack use is observable only through completion versus
  the proper-tail-call guarantee; finalization is declared absent
  with its gate (resource-scope and foreign eras). Values carry
  semantic identity — equal values are interchangeable, physical
  representation never changes meaning, storage observes nothing —
  and the two-clause identity rule makes process identity the only
  identity-bearing value (fresh per spawn, kernel operations only,
  never comparable), closing C032's and C035's deferrals. Debugging
  observes the implementation from outside program semantics (G124's
  channel). Sibling compiler commit
  [`734aafeb3d1739af7d85b021a8fc7b1569b39c20`](https://github.com/pcharbon70/catena/commit/734aafeb3d1739af7d85b021a8fc7b1569b39c20)
  supplies complete `RO-OBL-001`–`RO-OBL-008` coverage with 444
  passing tests through distinct-site record equality on evaluator
  and BEAM, closure-allocation irrelevance, fresh process identity
  per spawn, handle non-comparability, the finalization absence, and
  the stack boundary. Zero new diagnostic families. Handle operations
  beyond the kernel's remain C084's; message-copy details P085's;
  resource scopes G080's; foreign finalization C095's;
  debugging tools G124's.
- [x] **C038 — Complete — compile-time evaluation.**
  The normative
  [0.1.34 compile-time specification](../60-specification/compile-time-evaluation/README.md),
  [synthesis](../20-notes/catena-compile-time-evaluation.md),
  [resolved inquiry](../40-inquiries/what-executes-during-compilation.md),
  [topic map](../10-maps/compile-time-evaluation.md), and
  [C038 record](../50-journal/2026-08-26-c038-compile-time.md) fix
  the decision: constants never execute (definitions compile, not
  run); no attribute system and no macro system exist — each
  arriving, if ever, through its own slice under C034's gate;
  generated derivations classify as compiler-internal template
  generation executing no user code, with `compiler_derived`
  provenance, deterministic and total by construction, and output
  checked like handwritten definitions; and the cited restriction
  table — the gate plus condition normalization (acyclic, C003),
  the 20,000-step specification checker (C006), and bounded law
  samples (C004) — is the complete totality and determinism regime.
  Sibling compiler commit
  [`30426d558f79498f791a398a5ff01c7590b18cad`](https://github.com/pcharbon70/catena/commit/30426d558f79498f791a398a5ff01c7590b18cad)
  supplies complete `CE-OBL-001`–`CE-OBL-008` coverage with 451
  passing tests through the derivation provenance regression with
  byte-identical recompilation, the three budget regressions, the
  absence matrix, and determinism. Zero new diagnostic families.
  Spellings remain P109's; future derivations must follow C038's
  checking discipline; constrained code generation and build tooling are C121's.


## 5. Data, collections, and patterns

- [x] **C039 — Complete — algebraic data declaration syntax.** The 0.1.2 normative specification
  specifies kinded parameters, nullary, positional, and named-product
  constructors, atomic recursive groups, explicit existentials and refined
  results, `derives fold`, and transparent or abstract export.
- [x] **C040 — Complete — built-in data model.**
  The normative
  [0.1.35 data model specification](../60-specification/built-in-data-model/README.md),
  [synthesis](../20-notes/catena-built-in-data-model.md),
  [resolved inquiry](../40-inquiries/which-types-are-built-in.md),
  [topic map](../10-maps/built-in-data-model.md), and
  [C040 record](../50-journal/2026-08-29-c040-data-model.md) fix
  the twelve-way classification: the seven shipped types (unit, Bool,
  Int, Float, tuple, function, process handle) restated unchanged;
  Text, Character, and Bytes as built-ins elaborated from C017's
  scanned literals by the C018 pattern (Text the decoded scalar
  sequence, Character its one code point, Bytes the byte sequence),
  deterministic and total, with content-based comparability — all
  three comparable and orderable (lexicographic scalar order for
  Text and Character, byte order for Bytes); list, map, and set as
  library territory (P101 declares them as ordinary nominal ADTs);
  and references excluded (C084). The types live at the meaning and
  classifier level until a frontend encodes their literals. Sibling
  compiler commit
  [`44f7dd22b57757accc1da654bf4e99b93db728b4`](https://github.com/pcharbon70/catena/commit/44f7dd22b57757accc1da654bf4e99b93db728b4)
  supplies complete `BM-OBL-001`–`BM-OBL-008` coverage with 461
  passing tests through the `Catena.Text` elaboration module, the
  `Catena.Values` and `Data.comparable_type?` extensions, and the
  content-order witnesses. Zero new diagnostic families. C102 supplies explicit collection
  declarations and operations; P101 retains prelude admission. C042 defines construction
  and update. C104 supplies explicit text libraries while source spellings remain P109;
  native reference admission remains C097/G098 subject to C040's exclusion.
- [x] **C041 — Complete — structural records and variants.**
  The normative
  [0.1.36 records specification](../60-specification/structural-records-and-variants/README.md),
  [synthesis](../20-notes/catena-structural-records.md),
  [resolved inquiry](../40-inquiries/what-are-structural-records-and-variants.md),
  [topic map](../10-maps/structural-records.md), and
  [C041 record](../50-journal/2026-08-29-c041-records.md) fix
  the structural contract: the seven-operation table — record
  literal, select, update, extend, restrict, variant inject, and
  match — elevated from the kernel with cited homes; literals are
  closed unique-label rows with duplicate labels static invalidity;
  written field order controls evaluation order (C030) and never
  equality, comparison, or row identity (C035/C037); extend and
  restrict produce closed rows over closed inputs; open tails exist
  only in type positions, composing row polymorphism through
  signatures; missing-label operations are statically unreachable;
  records are semantic maps with invisible representation; and the
  kernel S-expression path is the only frontend expressing the
  operations until P109. Sibling compiler commit
  [`f42c9588541b6e61e82fffdf823270e587f2c386`](https://github.com/pcharbon70/catena/commit/f42c9588541b6e61e82fffdf823270e587f2c386)
  supplies complete `SR-OBL-001`–`SR-OBL-008` coverage with 470
  passing tests through the fixture's operation round-trip on stepper
  and compiled BEAM, variant dispatch agreement, duplicate-label
  rejection, type-position tails, and the frontend absence. Zero new
  diagnostic families. C042/C062/C044 subsequently fix collection construction, the
  alias exclusion/newtype idiom, and pattern-context refutability.
  Spellings remain P109.
- [x] **C042 — Complete — collection construction and update.** Normative
  `0.1.37` fixes the six topics: persistent update is constructor
  application plus match-based recursion (no dedicated operator);
  duplicate-key behavior is a P101 declaration obligation; ordering and
  key equality ride C035's comparable set; a bounds-failure miss is
  typed failure as a value (total, never a trap); and complexity
  promises are excluded from the language layer — representation is
  invisible, so a language cost bound would make it observable, and
  documentation stays P101's. Compiler witnesses on the kernel path
  (`246019f`): a declared List (construction, head/tail, length,
  replace-head) and a Pair-keyed lookup agreeing on stepper and BEAM,
  with a miss returning an Option-typed value. Zero new diagnostic
  families. Miss-type contents remain P101/C103's; spellings P109's;
  C062/C044 subsequently fix the alias/newtype and pattern-context rules.
- [x] **C043 — Complete — initial pattern grammar.** The 0.1.2 normative specification supports
  wildcard, binder, integer and Boolean literal, tuple, positional and named
  constructor, `as`, `or`, and nested patterns; it explicitly excludes list,
  structural-record, row-variant, binary, range, and programmable forms.
- [x] **C044 — Complete — refutability by context.** Normative `0.1.38`
  fixes three context classes: match the only exhaustive context
  (C045's usefulness relation and `M001`/`M002` unchanged),
  irrefutable-only the default for binding positions, explicit-failure
  the only honest refutability — no context inherits an implicit
  runtime match failure. `let` binders and function parameters stay
  plain-named today (a pattern-position `let` binder rejects `SYN002`)
  and are irrefutable-only on arrival; the generator principle is
  fixed (ordinary total, filtering explicitly mismatch-as-skip) with
  grammar deferred to Section 6; public receives are reserved as
  exhaustive-or-explicit-fallback; handler clauses keep plain binders;
  exception clauses are excluded unless a future revision explicitly
  reopens C036's terminal trap taxonomy. Compiler witnesses (`00bd04c`): match regression pin
  agreeing on stepper and BEAM, unchanged `M001`/`M002`, kernel and
  JSON-AST negative boundary tests, entry-point absences. Zero new
  diagnostic families.
- [x] **C045 — Complete — initial coverage and redundancy.** The 0.1.2 normative specification
  uses one usefulness relation for closed nominal data, Booleans, tuples,
  integer literals, abstract types, three-valued inhabitation, guards, `or`
  patterns, and GADT refinements, with witnesses and deterministic limits.
- [x] **C046 — Complete — programmable patterns excluded.** Closed with
  C044 at `0.1.38`: view patterns, pattern synonyms, and active
  patterns are excluded; patterns stay pure (no calls, effects,
  conversions, or user-defined tests, per C002); any arrival is its
  own slice stating effects, totality, coverage obligations,
  evaluation count, and cost, with no hidden conversion semantics
  reserved.

## 6. List comprehensions, generators, and iteration

The [list-comprehension synthesis](../20-notes/list-comprehensions.md)
proposed the initial answer, and revision `0.1.39` made its contract
normative with a dormant elaboration boundary. The audit retains the
implemented pure paths and reopens P050/P053/P057 for required effect and
failure witnesses. Source adoption remains P109; D059 remains deferred.

- [x] **C047 — Complete — list-comprehension surface syntax.** Normative
  `0.1.39` fixes the semantic-role grammar: `for pattern in source
  qualifier* yield expression` with `case ... in` filtering
  generators, `when` Bool filters, and exhaustive `let` bindings;
  at least one generator, the first qualifier a generator. Keywords
  are normative; token-level punctuation, layout, and block forms
  adopt with P109. Eager ordered production; lazy streams and
  infinite inputs excluded.

- [x] **C048 — Complete — generator protocol.** Sources are `List A`
  only: iterators, streams, effectful producers, and generic
  foldable sources are excluded; a non-list source is a typing
  error (`T002` through the elaborated module).

- [x] **C049 — Complete — multiple-generator meaning.** Left-to-right
  depth-first Cartesian traversal with dependency: each source is
  evaluated once per enclosing prefix visit, later sources may
  depend on earlier bindings, and an empty input at any depth
  yields no elements — witnessed `[14, 15, 24, 25]` agreeing on
  stepper and BEAM.

- [x] **C050 — Complete — filter semantics and evidence.** The explicit
  [0.1.50 target](../60-specification/closed-capability-kernel/identity-rows-and-comprehension-target.md) executes ordinary typed `Bool` filters with
  visible escaping effects, false-as-skip, immediate trap propagation and
  whole-computation handler abort. Independent nonrecursive probes reject
  forged fragment rows before recursive worker annotation. Reference and
  production BEAM witnesses preserve false-filter effects and all first/last
  failure prefixes; an enclosing handler can also change the whole result
  type. This completes `LC-OBL-005` without changing exact 0.1.8 or choosing
  public vocabulary. See the [implementation journal](../50-journal/2026-09-08-capability-kernel-integration.md).
- [x] **C051 — Complete — pattern-generator failure.** Consumes
  C044's split: ordinary generators are checked total by the
  usefulness relation (non-total rejects `M001`), `case` generators
  mismatch-as-skip explicitly, `LCP002` fires on a never-matching
  filtering pattern, and `LCP003` advises an unnecessary marker.

- [x] **C052 — Complete — qualifier bindings and scope.** Bindings
  are visible left-to-right, non-recursive, and never escape;
  same-comprehension rebinding is `LCP001`; unused bindings report
  `BS001`; outer shadowing follows the ordinary rule.

- [x] **C053 — Complete — evaluation and effect-order evidence.** The
  [0.1.50 target](../60-specification/closed-capability-kernel/identity-rows-and-comprehension-target.md)
  checks exact fragment rows and charges worker effects at the final call
  stage. Explicit nested request sequences and first/last failures agree on
  reference and production BEAM. Effectful context references preserve
  dependency order and repeated evaluation; unused definitions remain inert.
  Dependent filtering patterns retain source effects while skipping only
  their suffix. Total-pattern advisories use the selected target's checker.
  This completes `LC-OBL-008`; see the
  [acceptance journal](../50-journal/2026-09-08-capability-kernel-integration.md).
- [x] **C054 — Complete — eager versus lazy production.** Eager
  ordered `List B` results are normative; lazy streams and infinite
  inputs stay under a separate future resource-and-cancellation
  contract, with no lazy entry points.

- [x] **C055 — Complete — elaboration contract.** A dedicated typed
  qualifier tree elaborates to the kernel typed core through
  `Catena.Comprehension.elaborate/1` — no open trait dispatch —
  satisfying the pure extensional equations with `map`/`flat_map`
  (witnessed by desugaring-equivalence with a hand-written
  recursive map).

- [x] **C056 — Complete — result type.** Results are `List B` only;
  maps, sets, binaries, streams, validation values, and arbitrary
  `Applicative`/`Monad` targets are excluded with no entry
  points.

- [x] **C057 — Complete — sequential-execution evidence.** The
  [0.1.50 target](../60-specification/closed-capability-kernel/identity-rows-and-comprehension-target.md)
  preserves complete candidate suffixes, false-filter effects, empty inner
  sources and whole-traversal abort on reference and production BEAM.
  An enclosing handler returns a positional encoding of requests whose
  exact value rejects reversed and interleaved alternatives. Unsupported
  parallel execution options reject; lowering retains serial worker calls.
  This completes `LC-OBL-012` without admitting a parallel form. See the
  [acceptance journal](../50-journal/2026-09-08-capability-kernel-integration.md).
- [x] **C058 — Complete — termination and cost honesty.** The fused
  worker chain — one tail-recursive definition per generator depth,
  one shared accumulator, a final ordering pass, no intermediate
  map/filter lists — is stack-safe within the published parser
  nesting limit (900-element witness on BEAM), allocation is
  linear in output, Cartesian cost is explained by traversal and
  visible multiplicity rather than asymptotic language promises
  (C042's exclusion).

- [ ] **D059 — Deferred — neighboring iteration syntax.** Research ranges,
  effect-only loops, generator functions, async streams, binary and map
  comprehensions, zip qualifiers, and generic collectors independently.

## 7. Type-system surface and advanced boundaries

- [x] **C060 — Complete — type syntax.** Version 0.1.1 freezes function, tuple,
  constructor, record, variant, effect-row, constrained, quantified, and
  higher-rank type notation.
- [x] **C061 — Complete — primitive numeric relationships.** Normative
  `0.1.40` fixes closed-set instantiation: numeric operators are
  built-in primitive forms whose operands unify with each other and
  instantiate over exactly `{Int, Float}` — never trait dispatch,
  instance evidence, or user overloadability; the closed set is
  amendable only by a new revision. Arithmetic joins ordering and
  negation over `Float`, correct-but-dormant (no frozen frontend
  carries a float type or literal spelling; witnessed by driving the
  inference engine with float-typed operands, `fd75cb7`). No
  defaulting, implicit coercion, or literal constraints (`NM-OBL-005`/
  `006` re-affirmed); division, remainder, checked and decimal
  arithmetic, and explicit conversions are defined by C105. Zero new
  diagnostic families and no new public API.
- [x] **C062 — Complete — aliases, opaque types, and newtypes.** Normative
  `0.1.41` fixes one exclusion and two routings: transparent aliases are
  excluded from edition 0.1 with four recorded arrival conditions
  (identity-sharing, comparability interaction, C028 compatibility
  treatment, error-message naming); an opaque type is C022's `abstract`
  export routed, not redefined — the binary authority vocabulary stays
  complete; and the newtype is the nominal single-constructor
  single-field datatype with its own identity, representation invisible
  with no cost or layout promises, explicit coercion (constructor wraps,
  pattern unwraps, confusion rejects), explicit-target deriving only
  with no instance flow through the wrapper, and nominal-spelled
  diagnostics. Compiler witnesses on existing machinery (`1de0a7d`):
  kernel and JSON newtype programs on stepper/evaluator/BEAM, the
  smart-constructor idiom over an abstract export, explicit trait
  instances attaching and the instance-less twin rejecting, and the
  transparency-mode closure rejecting `alias` itself. Zero new
  diagnostic families and no new public API.
- [x] **C063 — Complete — generalization boundary.** The effect-aware hybrid
  rule freezes generalization, signature subsumption, and recursive annotation
  behavior.
- [x] **C064 — Complete — row semantics.** Record, variant, and effect row
  equality are separate, including duplicate effects, lacks constraints, and
  ambiguity.
- [x] **C065 — Complete — trait constraint solving.** Version 0.1.1 freezes
  instance scope, termination, coherence, ambiguity rejection, no defaulting,
  and failure diagnostics.
- [x] **C066 — Complete — type-directed name resolution.** Normative `0.1.42`
  fixes the invariant: name resolution is type-independent — every name
  resolves as a function of scope structure alone (C021), annotations
  never change a name's target, and results never depend on elaboration
  order. The five-way classification: field labels are not resolved
  names; trait instance selection is evidence settled at the instance
  (never deferred to call sites); constructors by visibility; literals
  by spelling; operators by closed-set instantiation. Four exclusions
  with arrival conditions: no overloading by type, no expected-type
  adaptation, no call-site deferral, no inference-directed field
  access. Compiler witnesses on existing machinery (`bef5fd5`):
  annotation-invariance pairs, scope-structural shadowing, trait
  evidence running and rejecting at the instance (`TRT005`),
  `A004` unknown-constructor rejection, import-collision rejection.
  Zero new diagnostic families and no new public API.
- [x] **C067 — Complete — dynamic and unsafe boundaries.** Normative `0.1.43`
  excludes all five forms intralingually: no casts, no runtime type
  inspection, no unchecked operations, no compiler intrinsics, no
  reflection — unsafety cannot be written in Catena source. Three
  anchors: the guard fragment already rejects the dynamic vocabulary
  (C003), erasure leaves no runtime type material (C006/C113), and the
  failure taxonomy has no cast kind (C036). Arrival conditions per form:
  representation, failure classification, visibility, and evidence
  interaction must all be amended in a future form's own revision.
  Visibility routes to the foreign owners: dynamic values enter only
  through a visible, typed, failure-classified boundary owned by
  C095/G096/G098. Compiler witnesses on existing machinery (`ed14901`):
  guard rejections unchanged, BEAM chunk inventories free of
  specification/governance chunks, no cast/typecase/dyn spellings, no
  foreign entry paths. Zero new diagnostic families and no new public
  API.
- [x] **C068 — Complete — checked advanced type profile.** Predicative explicit
  higher rank, signature-directed GADTs, branch-local equalities, and explicit
  rigid constructor existentials are specified behind an annotation boundary.
- [x] **C140 — Complete — excluded advanced type features.** Normative `0.1.44`
  keeps the eight forms excluded (C001's 0.1.1 exclusions restated as
  routing rows: impredicativity, inferred higher rank, first-class
  existentials beyond declared constructors, general linear types,
  dependent types, unrestricted type families, higher-kinded
  polymorphism over arbitrary kinds, unrestricted GADT inference) with
  C068's checked profile unchanged, and makes the seven-point arrival
  gate normative: problem statement, repeated-use evidence, interaction
  audit, formal semantics, operational contract, diagnostic story, and
  a library comparison — stated per form, independently, with no
  omnibus revision. Compiler witnesses on existing machinery
  (`77fba75`): profile-boundary rejections (`T012` spellings, `T010`
  unannotated GADT matches, `T009` existential escapes) and a
  signature-directed GADT program evaluating unchanged. Zero new
  diagnostic families and no new public API. Section 7's ten items are complete within their stated boundaries.

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
- [x] **C080 — Complete — cleanup and resource scopes.** Normative
  [0.1.51 owned lifetimes](../60-specification/resource-scopes/owned-lifetime-and-mandatory-cleanup.md)
  implement successful-acquisition registration, reverse mandatory cleanup,
  actual handler abandonment, primary traps, typed failure values, owner
  cancellation and cooperative exit. Scoped handles cannot escape or be
  captured. Reference execution, production BEAM and bounded schedule tests
  cover release failure precedence, deadline races and local actor return.
  Forced process/VM loss has no cleanup guarantee; process-affine foreign
  resources remain unadmitted until their adapter exists. General task/time
  propagation remains C088. See the
  [implementation evidence](../50-journal/2026-09-08-resource-lifetime.md).
- [x] **C081 — Complete — exception boundary.** Normative `0.1.47` fixes the
  partition: typed failure is a value (C103's contents); exception-style
  catching is the effect pattern — a handler declining to resume aborts to
  its result, visible in the effect row, a library idiom over unchanged
  C005; and `trap(reason)` is the one terminal mechanism, never catchable
  (C036 unchanged). Panics are traps with the reserved assertion/panic
  kind entering with their producers. Process exits route to C084,
  foreign failures map to trap at the visible boundary (C095/G096 with
  C067's rule), cancellation to C088, library faults to C105, outcome
  types to C103; C044's reopening door is the only amendment route for a
  language exception form. Compiler witnesses on existing machinery
  (`e0f2a9e`): the declining-handler pattern (`0`, not `100`, both
  targets), the trap fixture terminal, C010's spared spawner re-pinned,
  and exception-form absences on both frontends. Zero new diagnostic
  families and no new public API.
- [x] **C082 — Complete — top-level effects.** Normative `0.1.48` fixes the
  silent top level: an entry leaves nothing unhandled (effect-closed,
  `ENT001`, C027 unchanged); nobody interprets unhandled requests because
  none exist — no ambient host handler exists or is reserved; and launch
  is invocation only, to completion under unchanged kernel semantics with
  no scope and no injection. The capability interface now supplied by C106:
  capabilities reach an entry only as explicit typed values through a
  channel C106's slice defines and justifies — deny-able, never ambient —
  with retained zero-argument entries unchanged and the new 0.1.68 entry
  explicitly amended to receive authority while remaining effect-closed.
  C084's supervision interprets process failure, never requests; the
  door requires entry-form widening to amend C027 explicitly with
  who-interprets-what stated. Compiler witnesses on C027's existing
  machinery (`e962b73`): the launch re-pin (completed twice) and the
  `ENT001` non-effect-closed rejection. Zero new diagnostic families
  and no new public API.
- [ ] **D083 — Deferred — scoped and multi-shot computations.** Explicitly bound
  generators, async, nondeterminism, transactions, shallow handlers,
  higher-order effects, and multi-shot continuations until their semantics are
  separately specified.

## 10. Processes, concurrency, and distribution

- [x] **C084 — Complete — process creation and lifetime.** The
  [0.1.52 lifetime contract](../60-specification/process-lifetimes/owned-tasks-and-managed-relationships.md)
  retains raw isolated spawn and adds checked owned task scopes, typed monitors,
  symmetric managed links, trapping regions and bounded cleanup. Reference and
  BEAM witnesses cover registration/death, unlink generations, first failure,
  sibling cancellation, parent cancellation during acquisition, scoped handles,
  capability isolation and deterministic artifacts. General time remains C088;
  supervision is G089 and distributed transport G091. See the
  [implementation evidence](../50-journal/2026-09-08-owned-task-lifetimes.md).
- [x] **C085 — Complete — message semantics.** The
  [0.1.77 integrated contract](../60-specification/message-semantics/values-capacity-and-transport.md)
  retains Unit-returning raw local send, dead-target discard, immutable values,
  per-sender FIFO, and cross-sender interleaving. Checked local and capacity
  paths validate the complete declared value before sending or accounting;
  physical copy/share identity is unobservable; C095/C097 conversions and
  borrowed process authority remain typed and scope-bound. C129 supplies
  explicit overload above deployment-sized raw mailboxes, and C091 supplies
  authenticated `not_enqueued`, `delivery_unknown`, and admission outcomes
  without automatic retry or exactly-once processing. See the
  [implementation evidence](../50-journal/2026-09-10-message-semantics.md).
- [x] **C086 — Complete — selective receive.** The [0.1.49 amendment](../60-specification/selective-receive-correction/waiting-and-scan-cost-amendment.md)
  repairs the rejected-prefix starvation contradiction with explicit
  applicability and migration. A receive bypasses rejected messages to select
  the oldest match; with no match it waits without consumption. Two successive
  selections, exact remaining-mailbox order, and empty/all-rejected waiting
  agree on reference stepper and BEAM. Scan cost counts actually examined
  candidates without a universal rescan or fairness promise. The
  [implementation journal](../50-journal/2026-09-08-capability-kernel-integration.md)
  records verification. Historical 0.1.46 text and formats remain preserved.
  Public syntax remains P109, timeouts/cancellation C088, typed protocols
  P087, and send-side extensions P085.
- [x] **C087 — Complete — typed protocols.** The
  [0.1.55 explicit local library contract](../60-specification/local-protocol-contracts/schemas-sessions-and-outcomes.md)
  binds closed payloads and role schemas to verified process interfaces,
  rejects incompatible peers before application traffic, and enforces distinct
  correlations, one terminal result, observation-bound admission credit and
  owned cleanup. Checked payload producers and exact selected artifacts are
  exercised by compiled client/actor exchange and independent model evidence.
  Wrong payloads, nominal owner mismatches, late/double replies, cancellation,
  timeout and peer loss have explicit outcomes. This closes the chosen library
  contract, not static session fidelity or G091 remote transport. See the
  [implementation evidence](../50-journal/2026-09-08-local-protocol-contracts.md).
- [x] **C088 — Complete — cancellation and time.** The
  [0.1.53 contract](../60-specification/cancellation-and-time/deadlines-waits-and-cancellation.md)
  defines exact durations, opaque scope-local deadlines, sleep, total timed
  receive and cancellation boundaries. Selected reference/BEAM witnesses cover
  once-before-scan evaluation, queued zero-time matches, skipped messages,
  shared absolute budgets, origin rejection, deadline/reply choices, masked
  finalizer expiry and no timer-message leaks. Foreign interruption and
  distributed clocks remain explicitly outside this target. See the
  [implementation evidence](../50-journal/2026-09-08-cancellation-and-time.md).
- [x] **C089 — Complete — supervision.** The
  [0.1.56 library contract](../60-specification/typed-supervision/checked-trees-and-lifecycle.md)
  defines three restart strategies, three child restart classes, explicit
  intensity and shutdown bounds, fresh checked worker entries, deterministic
  origin-bound OTP child artifacts and managed owner cleanup. Model and native
  witnesses cover ordered restart/shutdown, temporary children, stale identity,
  startup rollback, restart storms, forced termination and owner observation.
  The supported static-worker inventory explicitly excludes arbitrary callbacks,
  nested supervisor descriptions and hot upgrades. See the
  [implementation evidence](../50-journal/2026-09-08-typed-supervision.md).
- [x] **C090 — Complete — scheduler observability.** The
  [0.1.78 policy contract](../60-specification/scheduler-observability/policy-classes-and-visible-limits.md)
  preserves nondeterministic runnable-process selection, permitted
  interleavings, quiescence, and no fairness guarantee. Reduction counts and
  run queues are unobservable; deployment priorities cannot weaken semantics.
  Work is classified as preemptible, scheduled blocking, or unsafe unbounded;
  unknown/unsafe work is refused and admitted blocking work uses explicit
  finite worker capacity. Bounded exploration retains multiple schedules and
  reports incomplete bounds honestly; a real owned foreign worker permits
  independent runnable progress. See the
  [implementation evidence](../50-journal/2026-09-10-scheduler-observability.md).
- [x] **C091 — Complete — distribution.** The
  [0.1.76 typed authenticated transport](../60-specification/distribution/typed-authenticated-transport.md)
  binds opaque node/service identity to exact package and local-protocol
  digests, mutually authenticated TLS certificates, bounded canonical typed
  frames, and explicit peer policy. It refuses version skew and malformed or
  authority-bearing payloads before delivery; distinguishes `not_enqueued`,
  `delivery_unknown`, and remote admission; and makes neither automatic-retry,
  exactly-once-processing, nor synchronized-clock claims. A deterministic
  transition model covers capacity, partitions, reconnects, and duplicate
  conflicts; two separately certified logical endpoints exchange a checked
  frame over a real TLS 1.3 loopback socket. See the
  [implementation evidence](../50-journal/2026-09-10-distribution.md). Public
  source vocabulary remains P109 and hot replacement remains G092.
- [x] **C092 — Complete — hot code upgrade.** The normative
  [0.1.79 contract](../60-specification/hot-code-upgrade/checked-migration-and-activation.md)
  defines exact artifact/interface/schema/evidence preflight, explicit
  quiescence, one active and one draining generation, bounded checked state
  migration, ordered messages during drain, precommit snapshot restoration,
  explicit reverse migration after commit, mixed-node admission, and the
  narrow managed OTP adapter. Compiler
  [PR 161](https://github.com/pcharbon70/catena/pull/161) supplies complete
  `HU-OBL-001`–`HU-OBL-015` evidence with 1,063 passing tests. Public upgrade
  syntax remains P109; release tooling and compatibility-matrix automation
  is C121, while the bounded compatibility matrix is C136.

## 11. BEAM representation and Erlang interoperability

- [x] **C093 — Complete — Catena-to-BEAM value mapping.** The
  [0.1.58 contract](../60-specification/value-boundaries/carriers-and-checked-conversion.md)
  adds an exact pure value-tree boundary for finite Float, Text, Character and
  Bytes, including typed closure capture and reference/BEAM agreement. Checked
  scalar, product, record, variant and nominal conversion preserves compact,
  uniform and fixed layouts, qualified identity and explicit node/byte budgets.
  Existing dictionary/evidence erasure and scoped-handle ownership retain their
  contracts; raw foreign funs, references and authority-bearing handles are not
  admitted by ordinary data conversion. General callbacks remain P096 and no
  stable external ABI or final vocabulary is adopted. See the
  [implementation evidence](../50-journal/2026-09-08-value-boundaries.md).
- [x] **C094 — Complete — calling conventions.** The
  [0.1.59 contract](../60-specification/calling-conventions/checked-calls-and-artifact-identity.md)
  binds actual exports, written and semantic arities, stage effects, private
  worker arguments, compiler/interface identity and generated source origins.
  Checked saturated and partial calls preserve immutable capture, stage traps
  and proper tails. Scoped synchronous callbacks reject forged, expired and
  wrong-owner handles; retained managed-process/OTP lifecycle adapters have
  exact call sidecars. General foreign declarations and asynchronous callbacks
  remain P096; C095 supplies recursive data conversion, and C100 supplies verified stack/source tooling.
  No stable cross-build ABI or final vocabulary is adopted. See the
  [implementation evidence](../50-journal/2026-09-09-calling-conventions.md).
- [x] **C095 — Complete — Erlang type boundary.** The
  [0.1.60 contract](../60-specification/erlang-type-boundary/typed-conversion-and-preservation.md)
  requires explicit typed codecs, re-derived nominal identity, complete
  input/output node/byte/depth validation and expected conversion failures.
  Proper Erlang lists map only to verified declared constructor roles; wire
  encoding and Catena runtime layout stay distinct. Independent Erlang and
  isolated native fixtures preserve finite Float bits and refuse non-finite
  NIF/ETF construction. Generic raw handles remain excluded and no dynamic
  type or final vocabulary is introduced. See the
  [implementation evidence](../50-journal/2026-09-09-erlang-type-boundary.md).
- [ ] **P096 — Partial — foreign calls and callbacks.** The
  [0.1.61 adapter milestone](../60-specification/foreign-adapters/authority-calls-and-callback-lifetime.md)
  executes typed capability-bound host calls and scope-owned pure callbacks,
  with checked captures, visible traps, cooperative cancellation races and
  C080 bounded cleanup. A retained C050 entry runs through checked foreign
  bindings and a separate artifact. General effectful/resource-capturing
  callbacks, application authority provisioning and the plan's public-surface
  gate remain open. See the [implementation evidence](../50-journal/2026-09-09-foreign-adapters.md).
- [x] **C097 — Complete — binaries, maps, PIDs, ports, references, and funs.**
  The [0.1.62 native-role inventory](../60-specification/native-value-roles/typed-admission-and-native-identity.md)
  assigns every kind an executable typed role or justified exclusion. Checked
  binary/map codecs retain C095; borrowed local PID send authority and fresh
  references use live scope registries; P096 supplies compiled callbacks.
  Handle equality, reflection, forged wrappers and generic raw fun/port
  admission are refused. Dead PID sends preserve Unit without liveness claims;
  C098 supplies separately admitted native service loading and port/NIF lifecycle rules. See the
  [implementation evidence](../50-journal/2026-09-09-native-value-roles.md).
- [x] **C098 — Complete — NIFs and ports.** The
  [0.1.63 native-service contract](../60-specification/native-services/signed-loading-and-owned-execution.md)
  supplies signed payload admission, explicit publisher/unsafe grants, scheduler
  and work contracts, finite Float calls, a bounded guardian-owned port service,
  and separately admitted dirty-CPU NIFs. Port death/deadline reaping, double
  close, GC fallback, owner death and isolated NIF VM-crash witnesses execute.
  NIF timeout reports potentially continuing native work; it promises neither
  rollback nor VM survival. See the
  [implementation evidence](../50-journal/2026-09-09-native-services.md).
- [x] **C099 — Complete — OTP compatibility policy.** The
  [0.1.57 policy](../60-specification/otp-compatibility/support-probes-and-artifacts.md)
  publishes the exact tested OTP 29.0.4/ERTS 17.0.4/Elixir 1.20.2 row,
  required feature probes, early unsupported-host rejection and toolchain-bound
  artifact loading. Discovery reports observed support and retirement policy.
  Separate-VM execution passes on the measured row; other patches and hosts
  remain unsupported, with simulated mismatch tests explicitly labeled.
  Expansion requires full semantic/artifact evidence; retirement has an explicit
  notice window and rebuild path. See the
  [implementation evidence](../50-journal/2026-09-08-otp-compatibility.md).
- [x] **C100 — Complete — debugging metadata.** The
  [0.1.64 sidecar contract](../60-specification/debugging-metadata/verified-origins-and-redacted-frames.md)
  maps actual closure, handler, ordinary-expression and foreign-entry frames
  through rebuilt source/BEAM identities. Bounded inline chains retain call-site
  history; Unicode scalar columns and collision-free JSON paths refer to original
  bytes. Missing/tampered sidecars and different runtime identities cannot supply
  origins. Stripped frames remain unmapped, values default to redaction and
  erased evidence is navigable only through external verified references.
  [Executed evidence](../50-journal/2026-09-09-debugging-metadata.md) includes unchanged
  BEAM bytes after an erased-checker change and preserved foreign authority.
## 12. Standard library contract

- [x] **C101 — Complete — minimum prelude.** Exact `0.1.69`
  [explicit minimum and component identity](../60-specification/minimum-prelude/explicit-minimum-and-component-identity.md)
  assembles ordinary foundations, the retained categorical hierarchy, outcomes,
  collections, text/binary and numerics with separately selectable environmental
  contracts. Exact package/component/interface digests bind dependency resolution
  and lock replay. Opt-out supplies no standard interfaces or implicit names;
  importing services grants no authority. [Evidence](../50-journal/2026-09-09-minimum-prelude.md)
  includes foundation laws and compiled transformation, validation, numeric, text
  and actual capability-using applications. Public vocabulary and grammar remain held.
- [x] **C102 — Complete — collection protocols.** The
  [0.1.65 contract](../60-specification/collection-protocols/finite-families-and-owned-pulls.md)
  defines ordinary finite families, semantic key order, strict duplicate failure,
  explicit replacement/combining, lawful dictionaries, ordered folds/traversal,
  checked pure callbacks and owned demand-driven streams. Costs include complete
  conversion and retained pull evidence; early stop, owner death and abandonment
  have mandatory bounded release. The [executed evidence](../50-journal/2026-09-09-collection-protocols.md)
  covers compiled dictionaries, independent laws, large lists, typed collisions,
  callback refusal and pull/release traces. Public vocabulary remains held.
- [x] **C103 — Complete — outcome types.** The
  [0.1.54 contract](../60-specification/outcome-contracts/values-sequencing-and-validation.md)
  defines ordinary optional and dependent values, nonempty accumulating
  validation, coherent categorical dictionaries, explicit conversion and
  elimination, callback counts and failure-class separation. The explicit
  digest-bound package has ordinary compiler and specialized BEAM evidence
  against independent equations; public vocabulary remains P109 and foreign
  admission remains C095/G096. See the
  [implementation evidence](../50-journal/2026-09-08-outcome-contracts.md).
- [x] **C104 — Complete — text and binary model.** The
  [0.1.66 contract](../60-specification/text-binary-model/units-unicode-and-checked-binary-operations.md)
  separates nominal byte/scalar/grapheme indices, checked slices, Unicode 17
  extended graphemes and explicit normalization, strict UTF-8/16/32 conversion,
  pure formatting and checked sequential binary segments. A rebuilt artifact
  executes typed pipelines over retained core; source/interpolation spelling
  remains P109. [Executed evidence](../50-journal/2026-09-09-text-binary-model.md)
  includes all pinned grapheme/normalization vectors, the supplementary scalar
  invariant, long combining runs, independent bit arithmetic and both backend owners.
- [x] **C105 — Complete — numeric library.** Exact `0.1.67`
  [checked arithmetic and rounding](../60-specification/numeric-library/checked-arithmetic-and-explicit-rounding.md)
  defines Euclidean quotient/remainder, finite binary64 operations, distinct
  primitive arithmetic traps and checked failures, explicit conversions, ordinary
  decimal values/contexts, deterministic exact decimal print/parse and correctly
  rounded square root. Typed pipelines execute over retained inputs without
  widening old source grammar. [Evidence](../50-journal/2026-09-09-numeric-library.md)
  includes independent rational vectors and compiled/reference witnesses.
  Transcendentals remain absent behind named admission gate NL-T01, as the
  reviewed plan permits; public vocabulary remains held.
- [x] **C106 — Complete — environmental effects.** Exact `0.1.68`
  [explicit authority and closed launches](../60-specification/environmental-effects/explicit-authority-and-closed-launches.md)
  amend C027/C082 for a typed service-authority parameter, preserving closed effects
  and retained zero-argument entries. Eight concrete adapters cover I/O, filesystem,
  numeric-endpoint TCP, time, randomness, environment, logging and approved host
  processes. Attenuation, denied/expired/revoked authority, owned cleanup and
  deterministic models have [compiled/reference and real-host evidence](../50-journal/2026-09-09-environmental-effects.md).
  Public names and launch syntax remain held; P096 callback composition remains
  separate, and approved host commands are trusted code rather than an OS sandbox.
- [ ] **P107 — Partial — category-inspired API names.** Normative 0.1.4 chooses the
  canonical behavior-first trait and method ABI and confines formal names to
  reference metadata. Independent comprehension and usability validation is
  still required.
- [x] **P108 — Complete — stability and performance policy.** The normative
  [0.1.87 operation contract](../60-specification/standard-stability-and-performance/versioned-operation-contracts.md)
  inventories every selected standard role's laws, order, callback
  multiplicity, failures, worst-case time and auxiliary-space class, constant
  stack obligation, stability tier, and representation stance. The compiler
  validates a canonical digest-bound catalog, classifies strengthened
  requirements or semantic/cost regressions as breaking, permits bound
  improvements, and binds empirical samples to exact toolchains without
  creating portable time, ABI, or layout promises. Focused mutation and
  tamper cases plus the complete 1,120-test suite are recorded in the
  [implementation journal](../50-journal/2026-09-10-standard-stability-and-performance.md).
  G138 retains the broader measured performance envelope.

## 13. Specifications, governance, and erasure

- [ ] **P109 — Partial — surface grammar (the capstone).** Freeze syntax for claims,
  evidence, assumptions, governed scopes, policy, authorization, decisions, and
  transitions. Normative 0.1.6 freezes semantic JSON forms but intentionally
  leaves public parser punctuation open.

  **Scope note (2026-08-24):** P109 is the *capstone* of the language line
  and its completion scope extends **beyond its original governance
  declaration syntax**. The original item covered only the specification and
  governance surface; the concrete *programming* grammar — declaration
  syntax for modules, imports/exports (the `use`/`export` punctuation
  C022 and ~20 shipped chapters defer here), values, functions and calls
  (C031/C032), conditionals and match expressions (C033), patterns,
  traits, effects and handlers, specifications, and entry declarations —
  has no other owner. P109 therefore owns four deliverables:
  (1) the general declaration and expression grammar over the completed
  C013–C020 scanner stack, parser included; (2) the original governance
  surface syntax; (3) the grammar's diagnostics, completing P117's
  parse-error half; and (4) the input contract for Section 14 tooling
  (G118 formatter, P119 doc tool, G120 REPL, G123 editor protocol) and
  the surface adoption of C047 and any admitted D059/G096 forms,
  all of which depend on it.

  Sequencing stays as the corpus already executes it: semantics first
  over the retained inputs (Sections 4–5, 9–11, stdlib contracts),
  grammar last. The widening exercise itself — deciding what an
  *original* Catena grammar should be rather than borrowing another
  language's shape — is joint developer-and-agent design work; the
  [approachable-language-design research](../10-maps/approachable-catena-language-design.md)
  accumulates the criteria it will consume, and every widened decision
  must land through the normal slice process (fork questions with
  options and recommendations, recorded in the
  [decision register](../20-notes/design-decision-register.md)).
  Deferral pointers in shipped chapters that name P109 for declaration
  grammar resolve to this widened scope; none need re-pointing.
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
- [x] **C116 — Complete — long-term evolution.** The normative
  [0.1.80 contract](../60-specification/long-term-evolution/historical-replay-and-migration.md)
  fixes exact-version interpretation for retained governance formats,
  deterministic adjacent schema migration, semantic-loss refusal, immutable
  original-byte and signature retention, derived provenance, historical-root
  replay, and explicit missing-tool/dependency outcomes. Compiler
  [PR 162](https://github.com/pcharbon70/catena/pull/162) supplies complete
  `LE-OBL-001`–`LE-OBL-014` evidence with 1,068 passing tests. Unknown future
  formats remain refused rather than guessed.
## 14. Diagnostics, tools, and developer experience

- [ ] **P117 — Partial — diagnostic contract.** C008 defines severity, stable
  `EDN`/`PRV`/`DEP` families, deterministic details, structured edits, and
  warning denial; C010/C013 add primary spans and source coordinates. Define
  secondary locations, inferred-type presentation, constraint provenance,
  missing-pattern witnesses, guard explanations, generated-code attribution,
  and a complete cross-language contract.
- [ ] **G118 — Gap — formatter.** Define canonical formatting, comments, idempotence,
  version coupling, and whether formatting is part of source compatibility.
- [ ] **P119 — Partial — documentation tool.** C016 specifies documentation
  attachment, normalized CommonMark bodies, inert raw HTML, and explicit
  future doctest opt-in; extraction is implemented. Complete rendering,
  symbol links, executable doctests, hidden APIs, traits/implementations,
  effects, laws, and specification views. Extraction is not a complete
  documentation tool.
- [ ] **G120 — Gap — interactive environment.** Define REPL typing and effects,
  declaration replacement, process lifetime, module loading, history, and
  governance behavior.
- [x] **C121 — Complete — build system and package manager.** The normative
  [0.1.81 contract](../60-specification/build-system/project-graphs-acquisition-and-offline-builds.md)
  fixes deterministic discovery, named profiles, finite workspace DAGs,
  verified transactional acquisition, transitive content-addressed cache
  keys, constrained declared generators, offline retained compilation, and
  verified atomic publication. Compiler
  [PR 163](https://github.com/pcharbon70/catena/pull/163) supplies complete
  `BG-OBL-001`–`BG-OBL-016` evidence with 1,077 passing tests. Public project
  and source vocabulary remains deferred to P109.
- [x] **C122 — Complete — testing tools.** Normative `0.1.84`'s
  [bounded runner contract](../60-specification/testing-tools/isolated-seeded-and-scoped-runs.md)
  and [implementation evidence](../50-journal/2026-09-10-testing-tools.md)
  define distinct unit, law, property, model, concurrency, and specification
  results; exact subject-bound plans; explicit deterministic seeds; typed
  generation; invariant-preserving bounded shrinking; declared effect
  accounting; runner-owned process cleanup; and portable finite reports.
  Compiler [PR 167](https://github.com/pcharbon70/catena/pull/167) passes 1,097
  tests and keeps semantic fuel, schedule bounds, shrink bounds, and host
  timeout distinct. Public test notation remains held for P109/P107, and
  passing observations do not claim proof.
- [ ] **G123 — Gap — editor protocol.** Define incremental parsing and typing, partial
  programs, completion, hover, rename, formatting, semantic tokens, and stable
  diagnostic identity.
- [x] **C124 — Complete — debugging and observability.** Normative `0.1.89`'s
  [source-aware bounded sessions](../60-specification/debugging-and-observability/source-aware-bounded-debug-sessions.md)
  verify executable and P100 sidecar identity before admitting owner-bound
  cooperative checkpoints, mapped redacted stacks, actor/message/handler/
  foreign/cancellation events, bounded drop-oldest traces, host-relative
  profiles, and crash reports. Stripped origins and optimized values remain
  explicitly unavailable; C113 declarations stay erased and navigate only
  through verified external evidence. Compiler
  [PR 173](https://github.com/pcharbon70/catena/pull/173) passes 1,128 tests,
  while [PR 174](https://github.com/pcharbon70/catena/pull/174) closes explicit
  optimized-value and derivation evidence. Production compilation, escript
  construction, and the trust audit pass without
  adopting P107 vocabulary or P109 grammar. See the
  [implementation evidence](../50-journal/2026-09-10-debugging-and-observability.md).
- [ ] **P125 — Partial — migration tools.** C008 defines conservative
  `json-edit` suggestions with explicit applicability and requires the C008
  compiler to report rather than apply them. Define transactional application,
  backups, rollback, source rewrites, API refactors, and deprecated-syntax
  handling.

## 15. Security, reproducibility, and operational limits

- [x] **C126 — Complete — trusted computing base.** Normative 0.1.70's
  [guarantee-specific trust contract](../60-specification/trusted-computing-base/guarantees-assumptions-and-boundary-checks.md)
  names enforcement components, shared helpers and residual host assumptions.
  The maintained compiler profile inventories source/call/data boundaries;
  mutation tests demonstrate both detected substitutions and undetected semantic
  changes. The [verification journal](../50-journal/2026-09-09-trusted-computing-base.md)
  records the evidence. This completes disclosure and its development gate,
  without claiming a proof-verified compiler or closing the formal program.
- [x] **C127 — Complete — unsafe-code policy.** Normative 0.1.71's
  [trusted obligation policy](../60-specification/trusted-obligation-policy/transitive-disclosure-and-scoped-admission.md)
  derives owner-qualified transitive obligations from exact checked artifacts,
  binds separate interface/assurance metadata, and enforces scoped admission,
  attenuation and future-admission revocation. C067's source exclusions remain.
  [Compiled and native evidence](../50-journal/2026-09-09-trusted-obligation-policy.md)
  covers diamonds, forged omissions, denied dependencies and replacement.
  This completes policy for admitted boundaries; host honesty, VM safety,
  future registry acquisition and unadmitted callback forms remain explicit limits.
- [x] **C128 — Complete — reproducible builds.** Normative `0.1.73`
  defines [exact inputs and canonical packages](../60-specification/reproducible-builds/exact-inputs-and-canonical-packages.md):
  explicit files/environment/generators, exact compiler/toolchain identity,
  normalized build paths, full-output archives and rebuild assurance. Independent
  roots compare actual BEAM, interface and assurance bytes; altered inputs and
  rehashed output substitutions fail identity/rebuild checks. Interrupted staging
  preserves the published archive. Registry authentication is completed by C130
  while general workflows are completed by C121;
  see the [evidence journal](../50-journal/2026-09-09-reproducible-packages.md).
- [x] **C129 — Complete — resource exhaustion.** Normative `0.1.75` defines
  [aggregate budgets and runtime admission](../60-specification/resource-exhaustion/aggregate-budgets-and-runtime-admission.md):
  portable and configured limits for transaction-wide files, source bytes,
  decoded nodes, and package output bytes; `LIM006`–`LIM009` structured
  refusal before publication; and an explicit bounded FIFO queue with
  message and encoded-byte admission, reject or terminate overload policy,
  owner-only consumption, observable cleanup, and owner-death cancellation.
  Raw send remains unchanged, P085 owns sendable payload integration, and VM
  or operating-system fatal exhaustion remains explicit deployment risk. The
  [verification journal](../50-journal/2026-09-10-resource-exhaustion.md)
  records exact-boundary, pressure, cancellation, profile, full-suite, and
  trusted-inventory evidence.
- [x] **C130 — Complete — supply-chain policy.** Normative `0.1.74` defines a
  [signed registry and immutable acquisition contract](../60-specification/supply-chain-policy/signed-registry-and-immutable-acquisition.md):
  explicit roots and dual-authority rotation, threshold snapshots, scoped
  publishers, immutable content/provenance, current acquisition, exact offline
  replay, and distinct yank/compromise rules. Source fixtures resolve through
  C025 and build through C128; native fixtures bind platform, toolchain and C127
  obligations. Forgery, replacement, staleness, rollback, equivocation and wrong
  platform fail closed. Registry signatures remain separate from C006 governance;
  see the [verification journal](../50-journal/2026-09-10-signed-package-registry.md).
- [x] **C131 — Complete — secrets and capabilities.** Normative `0.1.72`
  defines [sealed values and protected delivery](../60-specification/secret-capabilities/sealed-values-and-protected-delivery.md):
  explicit providers, scoped recipients, sensitivity-preserving transformations
  and replies, origin revocation, redacted observations, artifact refusal and
  bounded owned cleanup. Compiled capability, process stdin and loopback broker
  witnesses use synthetic sentinels. Host/native trust and lack of secure erasure
  remain explicit; general source adoption remains P109 while retained builds are C121. See the
  [verification journal](../50-journal/2026-09-09-secret-capabilities.md).

## 16. Formal validation and release gates

- [x] **C132 — Complete — progress and preservation targets.** Normative
  `0.1.45` states the remaining targets on the C002/C003 bar: the
  effects-and-failure targets over the shipped handler calculus
  (installation, resume-once, return-clause preservation; effect
  progress; trap terminality with kernel-verbatim reasons); the
  integrated theorem as a composed statement — the standing
  component theorems plus a composition lemma that is a routed
  proof obligation owned by the formal-validation program, never a
  claim; and conditional extensions (public processes on
  C084/P085's own statement, foreign values by construction of
  C067's typed boundary). Compiler witnesses on existing machinery
  (`5525662`): handler programs agreeing on stepper and BEAM, the
  trap fixture, the unhandled-request rejection, and the kernel
  fixture's composition-parts pin. Zero new diagnostic families
  and no new public API. The composition proof remains outstanding in
  the [formal-validation inquiry](../40-inquiries/what-should-a-greenfield-catena-type-system-guarantee.md#outcome);
  C133/P134 supply evidence, and G139 must state its release disposition.
  This item completes the statement of targets only.
- [x] **C133 — Complete — reference evaluator.** The normative
  [0.1.83 contract](../60-specification/reference-evaluator/common-observations-and-bounded-models.md)
  and [implementation evidence](../50-journal/2026-09-10-reference-evaluator.md)
  integrate the independent expression, effect, kernel, schedule, resource,
  foreign, external-response, and retained-source models through one common
  observation record. Compiler [PR 166](https://github.com/pcharbon70/catena/pull/166)
  preserves values, kinded terminals, ordered events, lifetime states,
  semantic fuel, schedule bounds, host deadlines, rejection, and unsupported
  coverage with 1,089 passing tests. Public source reports the P109 hold
  explicitly, and bounded agreement does not claim C132's outstanding
  composition proof.
- [x] **C134 — Complete — differential testing.** The normative
  [0.1.85 contract](../60-specification/differential-testing/generated-and-adversarial-agreement.md)
  and [implementation evidence](../50-journal/2026-09-10-differential-testing.md)
  define independent reference/BEAM comparison over declared C133
  observations, deterministic typed-kernel and comprehension generation,
  allowed finite schedule sets, domain-preserving shrinking, four adversarial
  mutation families, and a source/toolchain/scenario/observation-bound retained
  corpus. Compiler [PR 168](https://github.com/pcharbon70/catena/pull/168)
  supplies nine focused cases and 1,106 passing tests. Unsupported scope is
  explicit, public source remains P109, optimizer transformations remain P135,
  and finite agreement does not claim C132's composition proof.
- [x] **C135 — Complete — optimizer validity.** The normative
  [0.1.86 contract](../60-specification/optimizer-validity/checked-rewrites-and-observation-preservation.md)
  and [implementation evidence](../50-journal/2026-09-10-optimizer-validity.md)
  classify every current transformation owner and define an explicitly
  selected checked optimizer with a closed two-rule inventory. Compiler
  [PR 169](https://github.com/pcharbon70/catena/pull/169) verifies input and
  output core, emits digest-bound local certificates, replays the complete
  certificate sequence before lowering, preserves exact-once calls and traps,
  and refuses nonliteral integer annihilation without machine-checked purity
  and totality. Nine focused cases and the 1,115-test suite establish bounded
  evidence; public syntax remains P109 and testing does not claim proof.
- [x] **C136 — Complete — compatibility suite.** The normative
  [0.1.82 contract](../60-specification/compatibility-suite/layered-matrix-and-edition-policy.md)
  and [implementation evidence](../50-journal/2026-09-10-compatibility-suite.md)
  define a canonical bounded matrix with separate source, interface,
  dependency, data, toolchain, historical-signature, and runtime-upgrade
  rows. Compiler [PR 164](https://github.com/pcharbon70/catena/pull/164) and
  outcome-regression [PR 165](https://github.com/pcharbon70/catena/pull/165)
  supplies exact retained and current selections, semantic interface checks,
  wide and deep generated lock graphs, historical replay and Ed25519
  verification, exact oldest/newest supported-host rows, checked hot-upgrade
  preflight, explicit pass/fail/unsupported outcomes, published limits, and
  trust classification with 1,083 passing tests. Bounded fixtures make no
  ecosystem-wide or future-edition claim.
- [ ] **G137 — Gap — usability gate.** Test whether programmers can predict `map`,
  `map2`, `and_then`, traversal, handlers, guards, comprehensions, and
  diagnostics without prerequisite mathematical vocabulary.
- [x] **G138 — Complete — performance envelope.** The normative
  [0.1.88 supported-host contract](../60-specification/performance-envelope/supported-host-workloads-and-regression-policy.md)
  requires fifteen workload families spanning calls, traits, data, control,
  effects, processes, resources, foreign conversion, erasure, code size,
  compilation, and diagnostics. The retained OTP 29/Linux/x86-64 report has
  45 semantically matched rows with raw samples, memory observations, exact
  host and workload identities, and explicit nonportable scope. Mismatch,
  timeout, tamper, and artificial-regression fixtures enforce the scoring gate;
  the [journal](../50-journal/2026-09-10-performance-envelope.md) records all
  decisions and measured limits.
- [ ] **G139 — Gap — release-readiness definition.** State the minimum normative
  chapters, conformance coverage, platform support, known limitations, and
  stability promises required before calling a version complete.
- [ ] **G141 — Gap — compiler self-hosting.** Define the late-0.x milestone at
  which Catena can implement its own compiler, including the required language
  subset, parser and module facilities, tool effects, host interoperability,
  bootstrap trust, stage-one and stage-two builds, fixed-point or semantic
  equivalence checks, reproducibility, rollback, distribution, and the
  retained OTP 29 Abstract Format boundary. Elixir remains the bootstrap
  implementation at the audited `0.1.48` compiler; changing the implementation language
  does not change Catena's BEAM-only target.

## Suggested research order

The [detailed implementation plan](../20-notes/language-completion-plan.md)
covers every item with explored alternatives, recommended selections,
dependencies and acceptance evidence. Its delegated decisions do not mark
work complete. Public vocabulary and the final grammar remain held for later
joint design; the plan begins with semantics over retained compiler inputs.

The P109 scope note governs sequencing: semantics first over retained
inputs, complete public grammar as the capstone. This order reflects the
current ledger rather than the earlier pre-consolidation plan.

1. **Repair recorded completion gaps.** Resolve P086's normative conflict
   and discharge P050/P053/P057's required effect/failure witnesses. Keep
   the specification, evidence registry, inquiries, and checkbox states
   consistent; no new feature is needed to repair those claims.
2. **Resource lifetime and the public runtime.** Specify G080 together with
   the cancellation interface C088 needs, then complete C084/P085/P087/P090
   and G089. Coordinate G091/G092 with the foreign and compatibility layers.
3. **BEAM interoperability and library contracts.** Complete P093–P108,
   including foreign admission, environmental capability delivery, and
   numeric failure behavior, against the existing exclusions and guarantees.
4. **Surface capstone.** Jointly design and implement P109's full programming
   and governance grammar, parser, parse diagnostics, and tooling input
   contract. Track accumulated adoption requirements throughout the prior
   work; do not silently borrow or freeze a grammar ahead of that review.
5. **Tools and long-lived assurance.** Complete P116–P131 alongside the
   interfaces they depend on. Build, security, and evidence work that does
   not require the final parser can proceed earlier.
6. **Integrated validation and release.** Complete P133–G139 with explicit
   coverage and measured release gates, including C132's outstanding
   composition proof. Treat self-hosting G141 as the separately gated
   late-0.x milestone, retaining the BEAM target and supported OTP boundary.

Deferred D059/D083 extensions require their own evidence and inclusion or
exclusion decisions; they are not automatically prerequisites for release.

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
  supplies the library-operation research behind the fixed comprehension
  elaboration contract; P050/P053/P057 track its remaining evidence gaps.
- [Algebraic Effects and Handlers](../20-notes/algebraic-effects-and-handlers.md)
  constrains comprehension effects, generators, cancellation, and resource
  scopes without defining those features completely.
- [Language-Integrated Specifications and Governance](../20-notes/language-integrated-specifications-and-governance.md)
  supplies the assurance architecture that a complete language reference must
  eventually express normatively.

## Promotion criterion

Maintain this file as the current work-ahead ledger while the language
definition is being completed. Focused inquiries and topic maps carry the
research for individual items. A later move out of the inbox must preserve
every numeric item identity, incoming link, current status, and evidence
route; a writing pass alone does not complete or retire an item.
