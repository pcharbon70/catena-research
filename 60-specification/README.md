---
title: "Language Specification"
kind: map
created: "2026-08-01"
tags:
  - archive-navigation
  - directory-index
  - specification
aliases:
  - "Normative language definition"
---

# Language Specification (`60-specification`)

## Purpose

This directory contains Catena's versioned candidate and normative language
rules. Research notes supply rationale and evidence; normative chapters
determine conformance, while candidate chapters state the contract being
tested for promotion.

The repository-level [Specification Authority](../SPECIFICATION-AUTHORITY.md)
defines document status, rendered content labels, rule references, and
conflict handling independently of Catena language versions.
The companion
[Catena Conformance Vocabulary](../CONFORMANCE-VOCABULARY.md) defines
requirement force, behavior and failure classes, visible variability
declarations, limits, explicit traps, and implementation profiles across every
normative area.
The repository-level
[Catena Implementation Limits and Portability](../IMPLEMENTATION-LIMITS.md)
defines portable minima, machine-readable reporting, finite-resource
measurement, and exhaustion obligations without adding language semantics.

## What belongs here

Put separately versioned candidate or normative specification areas and their local indexes here. A
chapter becomes `normative` only when its required executable evidence and
cross-references are present. A version number, conformance case, executable
reference, or compiler behavior never overrides normative text by itself. An
explicit normative applicability or replacement statement is required when
language chapters overlap.

The C001 through C006 chapters retain normative semantic status through the
identifier-only `0.1.1` through `0.1.6` migration. Their historical commits
remain semantic evidence, while the exact renumbered protocol identity awaits
the fresh gate in
[Prototype Slice Renumbering](../50-journal/2026-08-04-prototype-slice-renumbering.md).
The normative C008 boundary is `0.1.7`; its explicitly authorized immutable
compiler evidence is recorded in the linked conformance journal. The
normative C010 formal semantic kernel is version `0.1.8`; its explicitly
authorized immutable compiler evidence is recorded in the
[C010 conformance journal](../50-journal/2026-08-06-c010-formal-semantic-kernel.md).
C012 governs finite implementation resources across these areas without
changing their normative status or consuming a language revision; its
[evidence record](../50-journal/2026-08-17-c012-implementation-limits.md)
preserves the coordinated compiler identity.
The normative C013 source-text envelope is version `0.1.9`; its strict UTF-8,
newline, normalization, location, and executable evidence are recorded in the
[C013 conformance journal](../50-journal/2026-08-17-c013-source-text-encoding-and-normalization.md).
The normative C014 identifier boundary is version `0.1.10`; its Unicode 17
repertoire, normalization, case, qualification, security, and executable
evidence are recorded in the
[C014 conformance journal](../50-journal/2026-08-17-c014-identifiers-and-name-security.md).
The normative C015 whitespace and layout boundary is version `0.1.11`; its
indentation-invariance, separator, continuation, delimiter-frame, and
executable evidence are recorded in the
[C015 conformance journal](../50-journal/2026-08-17-c015-whitespace-and-layout.md).
The normative C016 comment boundary is version `0.1.12`; its delimiter,
nesting, layout, documentation-attachment, Markdown, and executable evidence
are recorded in the
[C016 conformance journal](../50-journal/2026-08-18-c016-comments-and-documentation-comments.md).
The normative C017 literal boundary is version `0.1.13`; its atomic forms,
decoding, preservation, token ownership, diagnostics, active limits, and
executable evidence are recorded in the
[C017 conformance journal](../50-journal/2026-08-18-c017-literal-grammar.md).
The normative C018 numeric meaning boundary is version `0.1.14`; its
domains, monomorphic typing, correctly rounded conversion, static overflow
invalidity, negation, active limits, and executable evidence are recorded in
the [C018 conformance journal](../50-journal/2026-08-21-c018-numeric-literal-semantics.md).
  The normative C019 operator and punctuation boundary is version `0.1.15`;
  its closed inventory, maximal munch, capabilities and frames, fixed ladder,
  diagnostics, and executable evidence are recorded in the
  [C019 conformance journal](../50-journal/2026-08-21-c019-operators-and-punctuation.md).
  The normative C020 file-to-module boundary is version `0.1.16`; its file
  units, module binding, generated markers, diagnostics, and executable
  evidence are recorded in the
  [C020 conformance journal](../50-journal/2026-08-22-c020-files-and-modules.md).
  The normative C021 namespace boundary is version `0.1.17`; its
  inventory, shadowing and ambiguity rules, diagnostics, and executable
  evidence are recorded in the
  [C021 conformance journal](../50-journal/2026-08-22-c021-namespaces-and-shadowing.md).
  The normative C022 import/export boundary is version `0.1.18`; its
  export and admission rules, exclusions, diagnostics, and executable
  evidence are recorded in the
  [C022 conformance journal](../50-journal/2026-08-22-c022-imports-and-exports.md).
  The normative C023 abstraction boundary is version `0.1.19`; its two
  exclusions, sanctioned idiom, and executable evidence are recorded in
  the
  [C023 conformance journal](../50-journal/2026-08-23-c023-abstraction-boundaries.md).
  The normative C024 dependency-cycles boundary is version `0.1.20`; its
  SCC admission, resolution regimes, and executable evidence are recorded
  in the
  [C024 conformance journal](../50-journal/2026-08-24-c024-dependency-cycles.md).
  The normative C025 package boundary is version `0.1.21`; its
  dependency grammar, resolution, lockfile, and identity rules with
  executable evidence are recorded in the
  [C025 conformance journal](../50-journal/2026-08-24-c025-package-identity.md).
  The normative C026 prelude boundary is version `0.1.22`; its
  selection, precedence, opt-out, guarantee, and executable evidence are
  recorded in the
  [C026 conformance journal](../50-journal/2026-08-24-c026-prelude-policy.md).
  The normative C027 entry-points boundary is version `0.1.23`; its
  entry declarations, derived libraries, launch semantics, shutdown
  reports, and executable evidence are recorded in the
  [C027 conformance journal](../50-journal/2026-08-24-c027-entry-points.md).
  The normative C028 compatibility boundary is version `0.1.24`; its
  layer stances, breaking matrix, claim validation, and executable
  evidence are recorded in the
  [C028 conformance journal](../50-journal/2026-08-24-c028-api-compat.md).
  The normative C029 values boundary is version `0.1.25`; its value
  grammar, strictness invariant, terminal contract, and executable
  evidence are recorded in the
  [C029 conformance journal](../50-journal/2026-08-24-c029-values.md).
  The normative C030 order boundary is version `0.1.26`; its
  ordered-forms table, entry rule, trace observability, and executable
  evidence are recorded in the
  [C030 conformance journal](../50-journal/2026-08-25-c030-evaluation-order.md).
  The normative C031 bindings boundary is version `0.1.27`; its
  binding structure, sequencing idiom, `BS001` warning, and executable
  evidence are recorded in the
  [C031 conformance journal](../50-journal/2026-08-25-c031-bindings.md).
  The normative C032 functions boundary is version `0.1.28`; its
  arity model, capture discipline, local functions, tail guarantee,
  and executable evidence are recorded in the
  [C032 conformance journal](../50-journal/2026-08-25-c032-functions.md).
  The normative C033 branching boundary is version `0.1.29`; its
  branch form, sugar promise, consolidated rules, statement absence,
  and executable evidence are recorded in the
  [C033 conformance journal](../50-journal/2026-08-25-c033-branching.md).
  The normative C035 equality boundary is version `0.1.30`; its
  comparable set, float semantics, guard split, and executable
  evidence are recorded in the
  [C035 conformance journal](../50-journal/2026-08-26-c035-equality.md).
  The normative C034 recursion boundary is version `0.1.31`; its
  unrestricted stance, separation table, entry rule, and executable
  evidence are recorded in the
  [C034 conformance journal](../50-journal/2026-08-26-c034-recursion.md).
  The normative C036 failure boundary is version `0.1.32`; its single
  outcome, category mapping, entry rule, and executable evidence are
  recorded in the
  [C036 conformance journal](../50-journal/2026-08-26-c036-failure.md).
  The normative C037 observability boundary is version `0.1.33`; its
  six-way classification, identity rule, finalization gate, and
  executable evidence are recorded in the
  [C037 conformance journal](../50-journal/2026-08-26-c037-observability.md).
  The normative C038 compile-time boundary is version `0.1.34`; its
  stance, derivations classification, restriction table, and
  executable evidence are recorded in the
  [C038 conformance journal](../50-journal/2026-08-26-c038-compile-time.md).
  The normative C040 data-model boundary is version `0.1.35`; its
  classification, type elaboration, comparability entries, and
  executable evidence are recorded in the
  [C040 conformance journal](../50-journal/2026-08-29-c040-data-model.md).
  The normative C041 records boundary is version `0.1.36`; its
  operation table, row model, representation clause, and executable
  evidence are recorded in the
  [C041 conformance journal](../50-journal/2026-08-29-c041-records.md).
  The normative C042 collections boundary is version `0.1.37`; its
  six-topic decision, miss classification, complexity exclusion, and
  executable evidence are recorded in the
  [C042 conformance journal](../50-journal/2026-08-31-c042-collections.md).
  The normative C044 pattern-contexts boundary is version `0.1.38`;
  its three classes, per-context rules, reservations, exclusions,
  and executable evidence are recorded in the
  [C044 conformance journal](../50-journal/2026-08-31-c044-pattern-contexts.md).
  The normative C047–C058 list-comprehensions boundary is version
  `0.1.39`; its surface contract, qualifier rules, execution order,
  elaboration boundary, and executable evidence are recorded in the
  [C047 conformance journal](../50-journal/2026-08-31-c047-comprehensions.md).
  The normative C061 numeric-relationships boundary is version
  `0.1.40`; its instantiation rule, exclusions, routings, and
  executable evidence are recorded in the
  [C061 conformance journal](../50-journal/2026-08-31-c061-numerics.md).
  The normative C062 aliases-and-newtypes boundary is version
  `0.1.41`; its alias exclusion, newtype rules, opaque routing, and
  executable evidence are recorded in the
  [C062 conformance journal](../50-journal/2026-09-01-c062-newtypes.md).
  The normative C066 name-resolution boundary is version `0.1.42`;
  its invariant, classification table, exclusions, and executable
  evidence are recorded in the
  [C066 conformance journal](../50-journal/2026-09-01-c066-resolution.md).

## Index

### Subdirectories

- [Name Resolution](name-resolution/README.md)
  — the normative version 0.1.42 type-independence invariant with
  the five-way classification and the evidence carve-out.
- [Aliases and Newtypes](aliases-and-newtypes/README.md)
  — the normative version 0.1.41 alias exclusion with the newtype
  form and the opaque routing.
- [Numeric Relationships](numeric-relationships/README.md)
  — the normative version 0.1.40 closed-set instantiation contract
  with the dispatch exclusion and the G105 routings.
- [List Comprehensions](list-comprehensions/README.md)
  — the normative version 0.1.39 comprehension contract: surface
  roles, qualifier rules, execution order, fused-worker
  elaboration, and the `LCP` families.
- [Pattern Contexts](pattern-contexts/README.md)
  — the normative version 0.1.38 three-class refutability contract
  with per-context rules, reservations, and the D046 exclusion.
- [Collection Construction and Update](collection-construction-and-update/README.md)
  — the normative version 0.1.37 six-topic decision with
  miss-as-value bounds failures and the complexity exclusion.
- [Structural Records and Variants](structural-records-and-variants/README.md)
  — the normative version 0.1.36 consolidated operation table with
  kernel rows verbatim and the semantic-map representation clause.
- [Built-In Data Model](built-in-data-model/README.md) — the
  normative version 0.1.35 twelve-way classification with Text,
  Character, and Bytes elaborated and content-based comparability
  entries.
- [Compile-Time Evaluation](compile-time-evaluation/README.md) — the
  normative version 0.1.34 absence-plus-gate stance with the
  derivations-as-generation classification and the cited restriction
  table.
- [Resource Observability](resource-observability/README.md) — the
  normative version 0.1.33 six-way observability classification with
  semantic identity, the two-clause identity rule, and the
  finalization gate.
- [Runtime Failure Taxonomy](runtime-failure-taxonomy/README.md) —
  the normative version 0.1.32 single trap outcome with kinded
  reasons, the six-category mapping, and the per-producer entry rule.
- [Recursion and Termination](recursion-and-termination/README.md) —
  the normative version 0.1.31 unrestricted recursion stance with the
  cited separation table and the G038 entry rule.
- [Equality and Ordering](equality-and-ordering/README.md) — the
  normative version 0.1.30 closed comparable set with bit-exact float
  equality, structural recursion, monomorphic comparison, and the
  `EQN001` exclusion.
- [Branching](branching/README.md) — the normative version 0.1.29
  match-only branch form with the conditional sugar promise, the
  consolidated rule table, and the statement-form declared absence.
- [Functions and Calls](functions-and-calls/README.md) — the normative
  version 0.1.28 semantic-unary curried model with free partial
  application, lexical immutable capture, let-bound local functions,
  and the elevated proper-tail-call guarantee.
- [Bindings and Sequencing](bindings-and-sequencing/README.md) — the
  normative version 0.1.27 non-recursive binding structure,
  definitions-only recursion, sequencing idiom, and deny-able `BS001`
  with `_`-prefix exemption.
- [Evaluation Order](evaluation-order/README.md) — the normative
  version 0.1.26 closed ordered-forms table with typed-core
  completions, the future-form entry rule, and trace observability
  with dual-target agreement.
- [Values and Evaluation](values-and-evaluation/README.md) — the
  normative version 0.1.25 closed value grammar with Float, uniform
  first-classness, strictness invariant with edition-record gate, and
  value-or-trap terminal contract.
- [API and ABI Compatibility](api-and-abi-compatibility/README.md) —
  the normative version 0.1.24 layered compat stances, strict
  interface diff matrix, version-increment meanings, and claim
  validation contract.
- [Entry Points](entry-points/README.md) — the normative version 0.1.23
  manifest `entries` field, effect-closed entry validity, derived
  libraries, invocation-only launch, and return-is-shutdown contract.
- [Prelude Policy](prelude-policy/README.md) — the normative version
  0.1.22 opt-in manifest selection, ordinary-origin precedence,
  zero-implicit-names edition guarantee, and lockfile treatment.
- [Package Identity and Dependencies](package-identity-and-dependencies/README.md)
  — the normative version 0.1.21 dependencies field, SemVer operators,
  single-version resolution, `catena.lock`, and bundle-digest identity
  contract.
- [Module Dependency Cycles](module-dependency-cycles/README.md) — the
  normative version 0.1.20 SCC admission, resolution regimes, joint
  digests, consequence clauses, and conformance contract.
- [Abstraction Boundaries](abstraction-boundaries/README.md) — the
  normative version 0.1.19 authority and representation exclusions with
  the sanctioned smart-constructor invariant idiom.
- [Imports and Exports](imports-and-exports/README.md) — the normative
  version 0.1.18 private-by-default export, import admission, exclusion,
  and unused-import warning contract.
- [Namespaces and Shadowing](namespaces-and-shadowing/README.md) — the
  normative version 0.1.17 namespace inventory with spelling classes,
  shadowing and ambiguity resolution, diagnostics, and conformance
  contract.
- [Files and Modules](files-and-modules/README.md) — the normative version
  0.1.16 file-unit contract: `.cat` extension, at-most-one module with
  basename verification, ASCII module words, generated-file markers,
  diagnostics, and conformance obligations.
- [Operators and Punctuation](operators-and-punctuation/README.md) — the
  normative version 0.1.15 closed operator and punctuation inventory,
  maximal munch, capability and frame assignments, fixed precedence ladder,
  token-stream and operator-expression boundaries, diagnostics, and
  conformance contract.
- [Numeric Literal Semantics](numeric-literal-semantics/README.md) — the
  normative version 0.1.14 `Int` and finite binary64 `Float` domains,
  monomorphic literal typing, correctly rounded decimal conversion, static
  overflow invalidity, negation elaboration, limit, diagnostic, and
  conformance contract.
- [Literal Grammar](literal-grammar/README.md) — the normative version 0.1.13
  atomic Boolean, numeric, text, character, and byte spelling, decoding,
  provenance, line ownership, limit, diagnostic, and conformance contract.
- [Comments and Documentation Comments](comments-and-documentation-comments/README.md)
  — the normative version 0.1.12 slash-comment, nested block, layout,
  documentation attachment, CommonMark, doctest-policy, diagnostic, and
  conformance contract.
- [Whitespace and Layout](whitespace-and-layout/README.md) — the normative
  version 0.1.11 whitespace repertoire, indentation-invariance, separator,
  continuation, delimiter-frame, diagnostic, and conformance contract.
- [Identifiers](identifiers/README.md) — the normative version 0.1.10 Unicode
  XID, filtered NFC, role-neutral case, keyword escape, qualification,
  security, confusable diagnostic, and conformance contract.
- [Source Text](source-text/README.md) — the normative version 0.1.9 strict
  UTF-8, BOM, logical-newline, normalization-preservation, original-byte
  location, diagnostics, and conformance contract.
- [Formal Semantic Kernel](formal-semantic-kernel/README.md) — the normative
  version 0.1.8 exact S-expression syntax, row and process typing, sequential
  and actor dynamics, metatheory, BEAM correspondence, diagnostics, and
  completed promotion record.
- [Editions and Feature Lifecycle](editions-and-feature-lifecycle/README.md) —
  the normative version 0.1.7 package-local edition, exact-revision, preview,
  compatibility, migration, diagnostics, selection-bound artifact, and
  version-aware governance contract.
- [Specifications and Governance](specifications-and-governance/README.md) —
  the normative version 0.1.6 typed-rule, exact-example, additive-policy,
  offline-trust, lifecycle, artifact-binding, and total-erasure contract.
- [Effects and Handlers](effects-and-handlers/README.md) — the normative
  version 0.1.5 nominal request, lexical capability, identity-aware row, deep
  handler, affine resumption, typed-core, and effect-directed CPS contract.
- [Traits and Categorical Operations](traits-and-categorical-operations/README.md)
  — the normative version 0.1.4 behavior-first hierarchy, coherent evidence,
  laws, structural derivation, operational contracts, specialization, and
  BEAM erasure rules.
- [Clause Conditions](clause-conditions/README.md) — the normative version 0.1.3
  safe expression, reusable predicate, ordered guard-tree, coverage-fact,
  interface-evidence, BEAM lowering, and typed receive-harness contract.
- [Data and Patterns](data-and-patterns/README.md) — the normative version 0.1.2 nominal
  datatype, construction, pattern, match coverage, GADT, interface, layout,
  and derived-fold contract.
- [Type System](type-system/README.md) — the version 0.1.1 principal and
  annotation-directed static semantics, elaboration contract, and evidence.

### Documents

- None yet.

## Maintaining this index

Keep lifecycle state and versions explicit. Candidate chapters may record
local evidence but do not become authoritative until their immutable
conformance identity is published. A recorded identifier-only migration of an
already normative slice may preserve its semantic authority while requiring a
fresh executable protocol identity. Update the relevant research map, inquiry,
conformance evidence, and every affected index in the same change as a
normative rule. Keep every fenced block and every non-normative section visibly
classified according to the
[Specification Authority](../SPECIFICATION-AUTHORITY.md). Keep each area's
variability register and all normative wording aligned with the
[Catena Conformance Vocabulary](../CONFORMANCE-VOCABULARY.md).
Keep finite resource boundaries and profile disclosures aligned with
[Catena Implementation Limits and Portability](../IMPLEMENTATION-LIMITS.md).
