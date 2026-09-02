---
title: "Conformance Traceability"
kind: map
created: "2026-08-10"
tags:
  - conformance
  - specification
  - testing
aliases:
  - "P011 traceability map"
---

# Conformance Traceability

## Scope

This map owns the scheme that connects Catena normative rules and cross-cutting
governance obligations to the executable evidence that exercises them. It is
the workbench that closed checklist item P011 as C011 and implements the
traceability and stable-identifier responsibilities that
[Specification Authority](../SPECIFICATION-AUTHORITY.md) assigns to it. The map
and its registry are non-normative: they describe and index controlling
documents; they never amend them. Compiler tests remain evidence, never
authority.

The first completion pass targets `MUST`/`MUST NOT` obligations only. `SHOULD`,
`MAY`, declarative prose rules, and normative definitions become a separate
follow-up item now that C011 is reached.

## Start here

- [How Should Catena Achieve Exhaustive Rule-to-Test Traceability?](../40-inquiries/how-should-catena-achieve-exhaustive-rule-to-test-traceability.md)
  — the resolved inquiry and decision record.
- [Language Specification Completeness Checklist](../00-inbox/language-specification-completeness-checklist.md)
  — C011 (completed) is the item this work closed.
- [C011 Executable Conformance Suite](../50-journal/2026-08-12-c011-executable-conformance-suite.md)
  — the promotion record and immutable compiler identity.
- [Specification Authority](../SPECIFICATION-AUTHORITY.md) — assigns rule-ID and
  traceability ownership to this work and defines the heading-anchor citation unit.
- [Catena Conformance Vocabulary](../CONFORMANCE-VOCABULARY.md) — requirement
  force and behavior classes the evidence must respect.
- [Catena Implementation Limits and Portability](../IMPLEMENTATION-LIMITS.md)
  — the C012 governance policy and `IL-OBL-*` obligation source.
- [Source Text Specification](../60-specification/source-text/README.md)
  — the normative C013 source for `ST-OBL-*` obligations.
- [Identifier Specification](../60-specification/identifiers/README.md)
  — the normative C014 source for `ID-OBL-*` obligations.
- [Whitespace and Layout Specification](../60-specification/whitespace-and-layout/README.md)
  — the normative C015 source for `LY-OBL-*` obligations.
- [Comments and Documentation Comments Specification](../60-specification/comments-and-documentation-comments/README.md)
  — the normative C016 source for `CM-OBL-*` obligations.
- [Literal Grammar Specification](../60-specification/literal-grammar/README.md)
  — the normative C017 source for `LT-OBL-*` obligations.
- [Numeric Literal Semantics Specification](../60-specification/numeric-literal-semantics/README.md)
  — the normative C018 source for `NM-OBL-*` obligations.
- [Operators and Punctuation Specification](../60-specification/operators-and-punctuation/README.md)
  — the normative C019 source for `OP-OBL-*` obligations.
- [Files and Modules Specification](../60-specification/files-and-modules/README.md)
  — the normative C020 source for `FU-OBL-*` obligations.
- [Namespaces and Shadowing Specification](../60-specification/namespaces-and-shadowing/README.md)
  — the normative C021 source for `NS-OBL-*` obligations.
- [Imports and Exports Specification](../60-specification/imports-and-exports/README.md)
  — the normative C022 source for `IM-OBL-*` obligations.
- [Abstraction Boundaries Specification](../60-specification/abstraction-boundaries/README.md)
  — the normative C023 source for `AB-OBL-*` obligations.
- [Module Dependency Cycles Specification](../60-specification/module-dependency-cycles/README.md)
  — the normative C024 source for `CY-OBL-*` obligations.
- [Package Identity and Dependencies Specification](../60-specification/package-identity-and-dependencies/README.md)
  — the normative C025 source for `PK-OBL-*` obligations.
- [Prelude Policy Specification](../60-specification/prelude-policy/README.md)
  — the normative C026 source for `PL-OBL-*` obligations.
- [Entry Points Specification](../60-specification/entry-points/README.md)
  — the C027 source for `EN-OBL-*` obligations.
- [API and ABI Compatibility Specification](../60-specification/api-and-abi-compatibility/README.md)
  — the C028 source for `CP-OBL-*` obligations.
- [Values and Evaluation Specification](../60-specification/values-and-evaluation/README.md)
  — the C029 source for `VA-OBL-*` obligations.
- [Evaluation Order Specification](../60-specification/evaluation-order/README.md)
  — the C030 source for `EO-OBL-*` obligations.
- [Bindings and Sequencing Specification](../60-specification/bindings-and-sequencing/README.md)
  — the C031 source for `BS-OBL-*` obligations.
- [Functions and Calls Specification](../60-specification/functions-and-calls/README.md)
  — the C032 source for `FC-OBL-*` obligations.
- [Branching Specification](../60-specification/branching/README.md)
  — the C033 source for `BR-OBL-*` obligations.
- [Equality and Ordering Specification](../60-specification/equality-and-ordering/README.md)
  — the C035 source for `EQ-OBL-*` obligations.
- [Recursion and Termination Specification](../60-specification/recursion-and-termination/README.md)
  — the C034 source for `RT-OBL-*` obligations.
- [Runtime Failure Taxonomy Specification](../60-specification/runtime-failure-taxonomy/README.md)
  — the C036 source for `FT-OBL-*` obligations.
- [Resource Observability Specification](../60-specification/resource-observability/README.md)
  — the C037 source for `RO-OBL-*` obligations.
- [Compile-Time Evaluation Specification](../60-specification/compile-time-evaluation/README.md)
  — the C038 source for `CE-OBL-*` obligations.
- [Built-In Data Model Specification](../60-specification/built-in-data-model/README.md)
  — the C040 source for `BM-OBL-*` obligations.
- [Structural Records and Variants Specification](../60-specification/structural-records-and-variants/README.md)
  — the C041 source for `SR-OBL-*` obligations.
- [Collection Construction and Update Specification](../60-specification/collection-construction-and-update/README.md)
  — the C042 source for `CO-OBL-*` obligations.
- [Pattern Contexts Specification](../60-specification/pattern-contexts/README.md)
  — the C044 source for `PC-OBL-*` obligations.
- [List Comprehensions Specification](../60-specification/list-comprehensions/README.md)
  — the C047 source for `LC-OBL-*` obligations.
- [Numeric Relationships Specification](../60-specification/numeric-relationships/README.md)
  — the C061 source for `NR-OBL-*` obligations.
- [Aliases and Newtypes Specification](../60-specification/aliases-and-newtypes/README.md)
  — the C062 source for `AN-OBL-*` obligations.
- [Name Resolution Specification](../60-specification/name-resolution/README.md)
  — the C066 source for `RN-OBL-*` obligations.
- [Dynamic and Unsafe Boundaries Specification](../60-specification/dynamic-and-unsafe-boundaries/README.md)
  — the C067 source for `DU-OBL-*` obligations.
- [Excluded Advanced Type Features Specification](../60-specification/excluded-advanced-type-features/README.md)
  — the C140 source for `EA-OBL-*` obligations.
- [Progress and Preservation Specification](../60-specification/progress-and-preservation/README.md)
  — the C132 source for `PP-OBL-*` obligations.

## Identifier and registry convention

An **obligation** is one conformance requirement. In the `MUST`/`MUST NOT`
phase, every obligation receives a permanent, area-scoped identifier of the
form `AREA-OBL-NNN`. The numeric suffix is never reused; if an obligation is
retired its identifier is retired with it, mirroring the checklist's own
convention.

| Area code | Normative area or governance policy | Slice or milestone |
| --- | --- | --- |
| `TS` | type-system | 0.1.1 |
| `DP` | data-and-patterns | 0.1.2 |
| `CC` | clause-conditions | 0.1.3 |
| `TR` | traits-and-categorical-operations | 0.1.4 |
| `EF` | effects-and-handlers | 0.1.5 |
| `SG` | specifications-and-governance | 0.1.6 |
| `ED` | editions-and-feature-lifecycle | 0.1.7 |
| `FK` | formal-semantic-kernel | 0.1.8 |
| `IL` | implementation limits and portability | C012 governance |
| `ST` | source-text | 0.1.9 |
| `ID` | identifiers | 0.1.10 |
| `LY` | whitespace-and-layout | 0.1.11 |
| `CM` | comments-and-documentation-comments | 0.1.12 |
| `LT` | literal-grammar | 0.1.13 |
| `NM` | numeric-literal-semantics | 0.1.14 |
| `OP` | operators-and-punctuation | 0.1.15 |
| `FU` | files-and-modules | 0.1.16 |
| `NS` | namespaces-and-shadowing | 0.1.17 |
| `IM` | imports-and-exports | 0.1.18 |
| `AB` | abstraction-boundaries | 0.1.19 |
| `CY` | module-dependency-cycles | 0.1.20 |
| `PK` | package-identity-and-dependencies | 0.1.21 |
| `PL` | prelude-policy | 0.1.22 |
| `EN` | entry-points | 0.1.23 |
| `CP` | api-and-abi-compatibility | 0.1.24 |
| `VA` | values-and-evaluation | 0.1.25 |
| `EO` | evaluation-order | 0.1.26 |
| `BS` | bindings-and-sequencing | 0.1.27 |
| `FC` | functions-and-calls | 0.1.28 |
| `BR` | branching | 0.1.29 |
| `EQ` | equality-and-ordering | 0.1.30 |
| `RT` | recursion-and-termination | 0.1.31 |
| `FT` | runtime-failure-taxonomy | 0.1.32 |
| `RO` | resource-observability | 0.1.33 |
| `CE` | compile-time-evaluation | 0.1.34 |
| `BM` | built-in-data-model | 0.1.35 |
| `SR` | structural-records-and-variants | 0.1.36 |
| `CO` | collection-construction-and-update | 0.1.37 |
| `PC` | pattern-contexts | 0.1.38 |
| `LC` | list-comprehensions | 0.1.39 |
| `NR` | numeric-relationships | 0.1.40 |
| `AN` | aliases-and-newtypes | 0.1.41 |
| `RN` | name-resolution | 0.1.42 |
| `DU` | dynamic-and-unsafe-boundaries | 0.1.43 |
| `EA` | excluded-advanced-type-features | 0.1.44 |
| `PP` | progress-and-preservation | 0.1.45 |

The **registry** lives in this map (per-area tables below) and records, for each
obligation:

| Column | Meaning |
| --- | --- |
| ID | The permanent `AREA-OBL-NNN` identifier. |
| Obligation | A short noun phrase for the requirement. |
| Normative or governance anchor | A relative link to the governing heading, e.g. [`syntax-and-safety.md#clause-form`](../60-specification/clause-conditions/syntax-and-safety.md#clause-form). |
| Evidence | The exercising compiler test path and name, plus any stable diagnostic identifier(s). Cross-repo evidence uses a GitHub web link so the archive's local-link check is unaffected. |
| Status | `traced`, `in-progress`, or `untraced`. |

A registry entry is `traced` only when at least one tagged, passing compiler
test covers the obligation. A test tags its obligations with ExUnit
`@tag obligation: "AREA-OBL-NNN"` (or `obligations: [...]`), scanned by the
compiler coverage check.

## Per-area status

`MUST`/`MUST NOT` counts are fixed precisely when each area's obligation set is
extracted; all forty-one normative areas and the C012 governance policy are now
extracted. "Compiler-tagged + gated" means
the per-area tests carry `@tag obligations: [...]` and a
`<suite>_traceability_coverage_test.exs` gate is merged (or pending) in the
sibling compiler repository.

| Area | `MUST`/`MUST NOT` | Compiler tests (file) | Status |
| --- | --- | --- | --- |
| `CC` clause-conditions | 49 | `c003_clause_condition_test.exs` (10) | compiler-tagged + gated (merged); 3 gaps filled, 7 allow-listed |
| `TS` type-system | 44 | `type_conformance_test.exs` + `compiler_test.exs` (13) | compiler-tagged + gated (PR #84 open) |
| `DP` data-and-patterns | 71 | `c002_data_test.exs` (29) | compiler-tagged + gated (merged); all substantive gaps filled, 7 architectural/future allow-listed |
| `TR` traits | 32 | `c004_categorical_test.exs` (9) | compiler-tagged + gated (merged) |
| `EF` effects | 27 | `c005_effects_test.exs` (19) | compiler-tagged + gated (merged) |
| `SG` specifications-and-governance | 44 | `c006_specification_governance_test.exs` (34) | compiler-tagged + gated (merged) |
| `ED` editions | 36 | `c008_editions_lifecycle_test.exs` (16) | compiler-tagged + gated (merged) |
| `FK` formal-semantic-kernel | 15 | `c010_formal_semantic_kernel_test.exs` (17) | compiler-tagged + gated (merged) |
| `IL` implementation limits | 12 | `c012_implementation_limits_test.exs` (6) | compiler-tagged + gated (draft PR #88); 1 governance/version obligation allow-listed |
| `ST` source-text | 10 | `c013_source_text_test.exs` (7) | compiler-tagged + gated (working tree); all obligations traced |
| `ID` identifiers | 13 | `c014_identifiers_test.exs` (9) | compiler-tagged + gated (working tree); all obligations traced |
| `LY` whitespace-and-layout | 11 | `c015_whitespace_layout_test.exs` (9) | compiler-tagged + gated (merged); all obligations traced |
| `CM` comments-and-documentation-comments | 12 | `c016_comments_documentation_test.exs` (9) | compiler-tagged + gated (working tree); all obligations traced |
| `LT` literal-grammar | 12 | `c017_literal_grammar_test.exs` (10) | compiler-tagged + gated (`d51b307`); all obligations traced |
| `NM` numeric-literal-semantics | 14 | `c018_numeric_literal_semantics_test.exs` (10) | compiler-tagged + gated (`6fb2ad8`); all obligations traced |
| `OP` operators-and-punctuation | 16 | `c019_operators_test.exs` (12) | compiler-tagged + gated (`6e13bdf`); all obligations traced |
| `FU` files-and-modules | 12 | `c020_file_unit_test.exs` (9) | compiler-tagged + gated (`677a8f4`); all obligations traced |
| `NS` namespaces-and-shadowing | 14 | `c021_namespaces_test.exs` (12) | compiler-tagged + gated (`b482b4c`); all obligations traced |
| `IM` imports-and-exports | 13 | `c022_import_exports_test.exs` (9) | compiler-tagged + gated (`02da5c1`); all obligations traced |
| `AB` abstraction-boundaries | 7 | `c023_abstraction_test.exs` (6) | compiler-tagged + gated (`bbce0ee`); all obligations traced |
| `CY` module-dependency-cycles | 10 | `c024_module_cycles_test.exs` (7) | compiler-tagged + gated (`ca2be79`); all obligations traced |
| `PK` package-identity-and-dependencies | 12 | `c025_package_deps_test.exs` (9) | compiler-tagged + gated (`dcd7da0`); all obligations traced |
| `PL` prelude-policy | 10 | `c026_prelude_policy_test.exs` (7) | compiler-tagged + gated (`484d797`); all obligations traced |
| `EN` entry-points | 10 | `c027_entry_points_test.exs` (9) | compiler-tagged + gated (`cd0e5c5`); all obligations traced |
| `CP` api-and-abi-compatibility | 10 | `c028_api_compat_test.exs` (11) | compiler-tagged + gated (`0d96f96`); all obligations traced |
| `VA` values-and-evaluation | 8 | `c029_values_test.exs` (9) | compiler-tagged + gated (`f8d8fa9`); all obligations traced |
| `EO` evaluation-order | 8 | `c030_evaluation_order_test.exs` (9) | compiler-tagged + gated (`5e1e894`); all obligations traced |
| `BS` bindings-and-sequencing | 8 | `c031_bindings_test.exs` (8) | compiler-tagged + gated (`17b5be7`); all obligations traced |
| `FC` functions-and-calls | 8 | `c032_functions_test.exs` (9) | compiler-tagged + gated (`0af785c`); all obligations traced |
| `BR` branching | 8 | `c033_branching_test.exs` (7) | compiler-tagged + gated (`221338f`); all obligations traced |
| `EQ` equality-and-ordering | 8 | `c035_equality_test.exs` (9) | compiler-tagged + gated (`91c4d49`); all obligations traced |
| `RT` recursion-and-termination | 8 | `c034_recursion_test.exs` (7) | compiler-tagged + gated (`252da7b`); all obligations traced |
| `FT` runtime-failure-taxonomy | 8 | `c036_failure_test.exs` (7) | compiler-tagged + gated (`22c6a43`); all obligations traced |
| `RO` resource-observability | 8 | `c037_observability_test.exs` (7) | compiler-tagged + gated (`734aafe`); all obligations traced |
| `CE` compile-time-evaluation | 8 | `c038_compile_time_test.exs` (5) | compiler-tagged + gated (`30426d5`); all obligations traced |
| `BM` built-in-data-model | 8 | `c040_data_model_test.exs` (8) | compiler-tagged + gated (`44f7dd2`); all obligations traced |
| `SR` structural-records-and-variants | 8 | `c041_records_test.exs` (7) | compiler-tagged + gated (`f42c958`); all obligations traced |
| `CO` collection-construction-and-update | 8 | `c042_collections_test.exs` (8) | compiler-tagged + gated (`246019f`); all obligations traced |
| `PC` pattern-contexts | 9 | `c044_pattern_contexts_test.exs` (10) | compiler-tagged + gated (`00bd04c`); all obligations traced |
| `LC` list-comprehensions | 14 | `c047_list_comprehensions_test.exs` (14) | compiler-tagged + gated (`3216831`); all obligations traced |
| `NR` numeric-relationships | 8 | `c061_numeric_relationships_test.exs` (9) | compiler-tagged + gated (`fd75cb7`); all obligations traced |
| `AN` aliases-and-newtypes | 8 | `c062_aliases_newtypes_test.exs` (11) | compiler-tagged + gated (`1de0a7d`); all obligations traced |
| `RN` name-resolution | 8 | `c066_name_resolution_test.exs` (10) | compiler-tagged + gated (`bef5fd5`); all obligations traced |
| `DU` dynamic-and-unsafe-boundaries | 8 | `c067_dynamic_unsafe_test.exs` (10) | compiler-tagged + gated (`ed14901`); all obligations traced |
| `EA` excluded-advanced-type-features | 7 | `c140_excluded_advanced_test.exs` (8) | compiler-tagged + gated (`77fba75`); all obligations traced |
| `PP` progress-and-preservation | 8 | `c132_progress_preservation_test.exs` (planned) | obligations extracted against candidate chapters; compiler tests planned |

## Trails

### Pilot: clause-conditions 0.1.3

The pilot extracts the `MUST`/`MUST NOT` obligation set for
[Clause Conditions](../60-specification/clause-conditions/README.md), assigns
`CC-OBL-NNN` identifiers, maps the seven existing tests, and records the gap
set to fill. It is the template for the other seven areas. Tagging the tests,
filling the gaps, and wiring the validator hook and compiler coverage check are
the compiler-side steps P5–P7.

## Pilot registry — clause-conditions (`CC`, 0.1.3)

Evidence labels refer to tests in
[`c003_clause_condition_test.exs`](https://github.com/pcharbon70/catena/blob/rewrite/test/catena/c003_clause_condition_test.exs):

- **c003 #1** *checks exhaustive integer condition partitions and lowers them both ways*
- **c003 #2** *requires safe, typed, acyclic condition declarations*
- **c003 #3** *fact reasoning proves redundancy but remains conservative outside its theory*
- **c003 #4** *exports canonical condition evidence and imports it explicitly*
- **c003 #5** *rejects tampered nested condition evidence independently of the interface digest*
- **c003 #6** *receive harness accepts only native conditions over a closed message type*
- **c003 #7** *rejects unsupported partial and higher-order condition forms*
- **c003 #8** *condition signatures reject a nonempty effect (CND002)*
- **c003 #9** *ordinary match expressions must be exhaustive*
- **c003 #10** *or-pattern alternatives must bind the same names at the same types (M003)*

`traced` = at least one current test exercises it; `partial` = some facets
covered; `untraced` = no current test (a P6 gap). Process-only and future-type
`MUST` clauses (the metatheory counterexample rule, the "later versions must
specify" rule, and the future fixed-width integer rule) are intentionally
outside this executable registry.

### Positive execution

| ID | Obligation | Normative anchor | Evidence | Status |
| --- | --- | --- | --- | --- |
| CC-OBL-001 | Boolean literals and variables as conditions | [`syntax-and-safety.md#exact-initial-expression-set`](../60-specification/clause-conditions/syntax-and-safety.md#exact-initial-expression-set) | c003 #1, #2 | traced |
| CC-OBL-002 | Lazy negation, conjunction, disjunction | [`syntax-and-safety.md#exact-initial-expression-set`](../60-specification/clause-conditions/syntax-and-safety.md#exact-initial-expression-set) | c003 #3 | traced |
| CC-OBL-003 | Exact Boolean and integer equality and inequality | [`syntax-and-safety.md#exact-initial-expression-set`](../60-specification/clause-conditions/syntax-and-safety.md#exact-initial-expression-set) | c003 #1 | traced |
| CC-OBL-004 | Integer order, negation, add, sub, multiply | [`syntax-and-safety.md#exact-initial-expression-set`](../60-specification/clause-conditions/syntax-and-safety.md#exact-initial-expression-set) | c003 #1 | traced |
| CC-OBL-005 | Direct fully-applied local and imported predicates | [`condition-predicates-and-interfaces.md#declaration-contract`](../60-specification/clause-conditions/condition-predicates-and-interfaces.md#declaration-contract) | c003 #4 | traced |
| CC-OBL-006 | Forward acyclic predicate dependencies | [`condition-predicates-and-interfaces.md#dependency-and-expansion-evidence`](../60-specification/clause-conditions/condition-predicates-and-interfaces.md#dependency-and-expansion-evidence) | c003 #4 | traced |
| CC-OBL-007 | Ordinary matches and signed multi-clause functions | [`clause-contexts-and-receive.md#multi-clause-functions`](../60-specification/clause-conditions/clause-contexts-and-receive.md#multi-clause-functions) | c003 #1 | traced |
| CC-OBL-008 | Negative/zero/positive integer partitions proved exhaustive | [`coverage-and-fact-evidence.md#supported-fact-theory`](../60-specification/clause-conditions/coverage-and-fact-evidence.md#supported-fact-theory) | c003 #1 | traced |
| CC-OBL-009 | Condition false falls through to exactly the next clause | [`guard-tree-semantics.md#ordered-selection`](../60-specification/clause-conditions/guard-tree-semantics.md#ordered-selection) | c003 #1 | traced |
| CC-OBL-010 | Or-pattern lowering with one shared condition continuation | [`beam-lowering.md#shared-clause-continuation`](../60-specification/clause-conditions/beam-lowering.md#shared-clause-continuation) | — | untraced |
| CC-OBL-011 | 0.1.2 interfaces consumed without condition evidence | [`condition-predicates-and-interfaces.md#module-interfaces`](../60-specification/clause-conditions/condition-predicates-and-interfaces.md#module-interfaces) | — | untraced |
| CC-OBL-012 | 0.1.3 interface round-trips with canonical evidence | [`condition-predicates-and-interfaces.md#module-interfaces`](../60-specification/clause-conditions/condition-predicates-and-interfaces.md#module-interfaces) | c003 #4 | traced |
| CC-OBL-013 | Typed receive harness over a closed message type | [`clause-contexts-and-receive.md#selective-receive-harness`](../60-specification/clause-conditions/clause-contexts-and-receive.md#selective-receive-harness) | c003 #6 | traced |

### Negative rejection

| ID | Obligation | Normative anchor | Evidence | Status |
| --- | --- | --- | --- | --- |
| CC-OBL-014 | Malformed or missing condition signature | [`syntax-and-safety.md#clause-form`](../60-specification/clause-conditions/syntax-and-safety.md#clause-form) | CND001; c003 #2,#7 | partial |
| CC-OBL-015 | Non-Boolean condition or predicate result rejected | [`diagnostics-and-conformance.md#stable-diagnostics`](../60-specification/clause-conditions/diagnostics-and-conformance.md#stable-diagnostics) | CND002; c003 #2 | traced |
| CC-OBL-016 | Nonempty condition effect rejected | [`diagnostics-and-conformance.md#stable-diagnostics`](../60-specification/clause-conditions/diagnostics-and-conformance.md#stable-diagnostics) | CND002; c003 #8 | traced |
| CC-OBL-017 | Ordinary/lambda/partial/local/foreign/effect/trait ops excluded | [`syntax-and-safety.md#excluded-forms`](../60-specification/clause-conditions/syntax-and-safety.md#excluded-forms) | CND003; c003 #2,#7 | traced |
| CC-OBL-018 | Division/remainder/unchecked partial primitives excluded | [`syntax-and-safety.md#excluded-forms`](../60-specification/clause-conditions/syntax-and-safety.md#excluded-forms) | CND001; c003 #7 | traced |
| CC-OBL-019 | Recursive predicate dependency rejected | [`condition-predicates-and-interfaces.md#dependency-and-expansion-evidence`](../60-specification/clause-conditions/condition-predicates-and-interfaces.md#dependency-and-expansion-evidence) | CND004; c003 #2 | traced |
| CC-OBL-020 | Missing/implicit/duplicate/tampered import rejected | [`condition-predicates-and-interfaces.md#explicit-imports`](../60-specification/clause-conditions/condition-predicates-and-interfaces.md#explicit-imports) | CND005; c003 #5 | traced |
| CC-OBL-021 | 0.1.3 syntax in an earlier AST version rejected | [`syntax-and-safety.md#clause-form`](../60-specification/clause-conditions/syntax-and-safety.md#clause-form) | CND001; c003 #7 | traced |
| CC-OBL-022 | Proved-false or fact-shadowed redundant clause rejected | [`coverage-and-fact-evidence.md#condition-classification`](../60-specification/clause-conditions/coverage-and-fact-evidence.md#condition-classification) | M002; c003 #3 | traced |
| CC-OBL-023 | Nonlinear partition claimed exhaustive rejected as unknown | [`coverage-and-fact-evidence.md#supported-fact-theory`](../60-specification/clause-conditions/coverage-and-fact-evidence.md#supported-fact-theory) | M001; c003 #3 | traced |
| CC-OBL-024 | Condition or fact budget below minimum rejected | [`condition-predicates-and-interfaces.md#budget`](../60-specification/clause-conditions/condition-predicates-and-interfaces.md#budget) | CND007; c003 #2 | traced |
| CC-OBL-025 | Receive harness with free type/nonnative/expanded-or-pattern rejected | [`clause-contexts-and-receive.md#native-only-rule`](../60-specification/clause-conditions/clause-contexts-and-receive.md#native-only-rule) | c003 #6 | partial |

### Differential, determinism, and independent verification

| ID | Obligation | Normative anchor | Evidence | Status |
| --- | --- | --- | --- | --- |
| CC-OBL-026 | Reference/native/ordinary lowering agree on clause and result | [`diagnostics-and-conformance.md#differential-evidence`](../60-specification/clause-conditions/diagnostics-and-conformance.md#differential-evidence) | c003 #1 | traced |
| CC-OBL-027 | BEAM and interface output deterministic for identical inputs | [`diagnostics-and-conformance.md#differential-evidence`](../60-specification/clause-conditions/diagnostics-and-conformance.md#differential-evidence) | c003 #1 | partial |
| CC-OBL-028 | Verifier independently rejects corrupted condition evidence | [`diagnostics-and-conformance.md#differential-evidence`](../60-specification/clause-conditions/diagnostics-and-conformance.md#differential-evidence) | c003 #5 | traced |
| CC-OBL-029 | Fact checker must not report M001/M002 for unsupported or timed-out input | [`diagnostics-and-conformance.md#stable-diagnostics`](../60-specification/clause-conditions/diagnostics-and-conformance.md#stable-diagnostics) | c003 #3 | partial |

### Lowering and pipeline invariants

| ID | Obligation | Normative anchor | Evidence | Status |
| --- | --- | --- | --- | --- |
| CC-OBL-030 | Three lowering selections exposed (auto/native/ordinary) | [`beam-lowering.md#native-lowering`](../60-specification/clause-conditions/beam-lowering.md#native-lowering) | c003 #1 | partial |
| CC-OBL-031 | Receive harness emits native Erlang receive guards only | [`beam-lowering.md#selective-receive`](../60-specification/clause-conditions/beam-lowering.md#selective-receive) | c003 #6 | traced |
| CC-OBL-032 | OTP Abstract Format is the sole BEAM-generation boundary | [`clause-condition-overview.md#compiler-boundary`](../60-specification/clause-conditions/clause-condition-overview.md#compiler-boundary) | — | untraced |
| CC-OBL-033 | Typed core, effects, source attribution preserved through lowering | [`clause-condition-overview.md#compiler-boundary`](../60-specification/clause-conditions/clause-condition-overview.md#compiler-boundary) | — | untraced |

### Exhaustiveness, clause structure, and guard-tree semantics

| ID | Obligation | Normative anchor | Evidence | Status |
| --- | --- | --- | --- | --- |
| CC-OBL-034 | Ordinary match expressions must be exhaustive | [`clause-contexts-and-receive.md#ordinary-matches`](../60-specification/clause-conditions/clause-contexts-and-receive.md#ordinary-matches) | c003 #9 | traced |
| CC-OBL-035 | Multi-clause set exhaustive with uniform result type | [`clause-contexts-and-receive.md#multi-clause-functions`](../60-specification/clause-conditions/clause-contexts-and-receive.md#multi-clause-functions) | c003 #1 | traced |
| CC-OBL-036 | Elaboration preserves source clause order and bindings | [`clause-contexts-and-receive.md#multi-clause-functions`](../60-specification/clause-conditions/clause-contexts-and-receive.md#multi-clause-functions) | c003 #1 | partial |
| CC-OBL-037 | Structural match then condition evaluated once, in order | [`guard-tree-semantics.md#ordered-selection`](../60-specification/clause-conditions/guard-tree-semantics.md#ordered-selection) | c003 #1 | traced |
| CC-OBL-038 | Body failure or divergence does not resume clause selection | [`guard-tree-semantics.md#ordered-selection`](../60-specification/clause-conditions/guard-tree-semantics.md#ordered-selection) | — | untraced |
| CC-OBL-039 | Verifier rejects duplicated condition evaluation | [`guard-tree-semantics.md#guard-tree-core`](../60-specification/clause-conditions/guard-tree-semantics.md#guard-tree-core) | — | untraced |
| CC-OBL-040 | Or-pattern alternatives bind the same names | [`guard-tree-semantics.md#or-patterns`](../60-specification/clause-conditions/guard-tree-semantics.md#or-patterns) | M003; c003 #10 | traced |
| CC-OBL-041 | Exhaustiveness accepted only under the stated conditions | [`coverage-and-fact-evidence.md#structural-baseline`](../60-specification/clause-conditions/coverage-and-fact-evidence.md#structural-baseline) | c003 #1 | traced |
| CC-OBL-042 | Unknown never closes an exhaustiveness gap or proves redundancy | [`coverage-and-fact-evidence.md#condition-classification`](../60-specification/clause-conditions/coverage-and-fact-evidence.md#condition-classification) | c003 #3 | traced |

### Predicate and interface integrity

| ID | Obligation | Normative anchor | Evidence | Status |
| --- | --- | --- | --- | --- |
| CC-OBL-043 | Predicate well-formedness: signature, totality, effect-free | [`condition-predicates-and-interfaces.md#declaration-contract`](../60-specification/clause-conditions/condition-predicates-and-interfaces.md#declaration-contract) | c003 #2 | traced |
| CC-OBL-044 | `expanded_core` equals the canonical body | [`condition-predicates-and-interfaces.md#canonical-identity-and-core`](../60-specification/clause-conditions/condition-predicates-and-interfaces.md#canonical-identity-and-core) | c003 #4 | traced |
| CC-OBL-045 | Consumer recomputes digest and verifies evidence | [`condition-predicates-and-interfaces.md#explicit-imports`](../60-specification/clause-conditions/condition-predicates-and-interfaces.md#explicit-imports) | c003 #4,#5 | traced |
| CC-OBL-046 | Normalization and inlining terminate under the budget | [`condition-predicates-and-interfaces.md#budget`](../60-specification/clause-conditions/condition-predicates-and-interfaces.md#budget) | c003 #2 | traced |
| CC-OBL-047 | Minimum supported budget is 20,000 | [`condition-predicates-and-interfaces.md#budget`](../60-specification/clause-conditions/condition-predicates-and-interfaces.md#budget) | c003 #2 | traced |

### Coverage reporting and no-conversion

| ID | Obligation | Normative anchor | Evidence | Status |
| --- | --- | --- | --- | --- |
| CC-OBL-048 | Implementation limit reported as limit or unknown, not semantic proof | [`coverage-and-fact-evidence.md#budgets-and-diagnostics`](../60-specification/clause-conditions/coverage-and-fact-evidence.md#budgets-and-diagnostics) | — | untraced |
| CC-OBL-049 | No truthiness or invalid-operation conversion | [`syntax-and-safety.md#evaluation`](../60-specification/clause-conditions/syntax-and-safety.md#evaluation) | c003 #2 | traced |

### Pilot gap set (P6)

The pilot gap set has been filled down to its architectural remainder. Three
gaps were filled by focused tests (CC-OBL-016, 034, 040 as c003 #8, #9, #10)
and CC-OBL-049 was recovered by tagging c003 #2. The seven remaining
allow-listed obligations (CC-OBL-010, 011, 032, 033, 038, 039, 048) are
architectural or have no focused c003 unit; the compiler coverage gate carries
them with reasons.

### Scale-out

After the pilot validates the scheme, one coordinated research/compiler PR pair
per area applies it. The research side assigns identifiers and records anchors;
the compiler side tags and fills tests. The pair mirrors the C010 coordination
(`catena-research#24` ↔ `catena#74`).

## Registry — formal-semantic-kernel (`FK`, 0.1.8)

Evidence labels refer to tests in
[`c010_formal_semantic_kernel_test.exs`](https://github.com/pcharbon70/catena/blob/rewrite/test/catena/c010_formal_semantic_kernel_test.exs).
The mapping is provisional; the compiler-side tagging PR establishes the
authoritative test-to-obligation links and the gap set.

- **c010 #1** *the exact S-expression envelope preserves spans and rejects malformed input*
- **c010 #2** *parser node and nesting limits are distinct from malformed syntax*
- **c010 #3** *kernel selection is exact and JSON frontends remain bounded at 0.1.7*
- **c010 #4** *rows, closed variants, strict order, and integrated core evidence check together*
- **c010 #5** *regular nominal data is typed, exhaustive, sendable, and fixed-layout*
- **c010 #6** *trait evidence and deep affine handling are integrated and erased*
- **c010 #7** *proper tail calls agree between the stepper and generated BEAM*
- **c010 #8** *selective receive preserves skipped messages and process traps stay local*
- **c010 #9** *dead-target send drops the message and waiting configurations are quiescent*
- **c010 #10** *bounded exploration admits both cross-sender receive orders*
- **c010 #11** *self-send preserves per-sender FIFO order*
- **c010 #12** *generated closed terms make progress and preserve their checked result types*
- **c010 #13** *local let bindings generalize only under the value and effect restriction*
- **c010 #14** *interfaces bind public process identities and reject substitution*
- **c010 #15** *sendability, process contexts, and forged core evidence are rejected*
- **c010 #16** *explicit trap is a typed bottom and lowers to the fixed BEAM trap*
- **c010 #17** *kernel artifacts and interfaces are deterministic and record the kernel frontend*

| ID | Obligation | Normative anchor | Evidence | Status |
| --- | --- | --- | --- | --- |
| FK-OBL-001 | Accepted kernel module elaborates to unified typed core, independent verification, and small-step meaning | [`overview-and-applicability.md#integrated-boundary`](../60-specification/formal-semantic-kernel/overview-and-applicability.md#integrated-boundary) | c010 #4, #12 | traced |
| FK-OBL-002 | Command or package selection must equal the written edition and revision | [`canonical-kernel-syntax.md#input-envelope`](../60-specification/formal-semantic-kernel/canonical-kernel-syntax.md#input-envelope) | c010 #3 | traced |
| FK-OBL-003 | Elaboration preserves the span of the source form | [`canonical-kernel-syntax.md#source-locations`](../60-specification/formal-semantic-kernel/canonical-kernel-syntax.md#source-locations) | c010 #1 | traced |
| FK-OBL-004 | Verifier independently rechecks the integrated kernel judgment | [`static-semantics-and-elaboration.md#independent-verification`](../60-specification/formal-semantic-kernel/static-semantics-and-elaboration.md#independent-verification) | c010 #4, #15 | traced |
| FK-OBL-005 | Tail calls, including after selection and receive loops, must not grow the call stack | [`sequential-dynamics.md#functions-bindings-and-branching`](../60-specification/formal-semantic-kernel/sequential-dynamics.md#functions-bindings-and-branching) | c010 #7 | traced |
| FK-OBL-006 | Local filesystem path is diagnostic context only; it must not alter interface identity or BEAM bytes | [`beam-diagnostics-and-conformance.md#fixed-beam-representation`](../60-specification/formal-semantic-kernel/beam-diagnostics-and-conformance.md#fixed-beam-representation) | c010 #17 | traced |
| FK-OBL-007 | Envelope accept plus malformed, delimiter, unknown-form, duplicate-export, node-limit, and depth-limit rejection | [`beam-diagnostics-and-conformance.md#required-executable-evidence`](../60-specification/formal-semantic-kernel/beam-diagnostics-and-conformance.md#required-executable-evidence) | SYN001-003; c010 #1, #2 | traced |
| FK-OBL-008 | Records, open-row rejection, closed/open variant coverage, constructors, local generalization, forged evidence, fixed layout, strict order | [`beam-diagnostics-and-conformance.md#required-executable-evidence`](../60-specification/formal-semantic-kernel/beam-diagnostics-and-conformance.md#required-executable-evidence) | c010 #4, #5, #13 | traced |
| FK-OBL-009 | One source fixture combining value rows, a trait call, a handled ordinary effect, a process entry, spawn, send, and receive | [`beam-diagnostics-and-conformance.md#required-executable-evidence`](../60-specification/formal-semantic-kernel/beam-diagnostics-and-conformance.md#required-executable-evidence) | c010 #4, #5, #6, #8 | partial |
| FK-OBL-010 | Sendability, process-context rejection, interface substitution, and forged-core attacks | [`beam-diagnostics-and-conformance.md#required-executable-evidence`](../60-specification/formal-semantic-kernel/beam-diagnostics-and-conformance.md#required-executable-evidence) | PRC001-004; c010 #14, #15 | traced |
| FK-OBL-011 | Self, per-sender order, cross-sender outcomes, skipped-message preservation, dead-target send, return, trap, and quiescence | [`beam-diagnostics-and-conformance.md#required-executable-evidence`](../60-specification/formal-semantic-kernel/beam-diagnostics-and-conformance.md#required-executable-evidence) | c010 #8, #9, #10, #11, #16 | traced |
| FK-OBL-012 | Proper-tail-call stress cases | [`beam-diagnostics-and-conformance.md#required-executable-evidence`](../60-specification/formal-semantic-kernel/beam-diagnostics-and-conformance.md#required-executable-evidence) | c010 #7 | traced |
| FK-OBL-013 | Generated closed-term progress, result-type, and reference/BEAM agreement | [`beam-diagnostics-and-conformance.md#required-executable-evidence`](../60-specification/formal-semantic-kernel/beam-diagnostics-and-conformance.md#required-executable-evidence) | c010 #12 | traced |
| FK-OBL-014 | Bounded all-schedule reference exploration and focused reference/BEAM observations | [`beam-diagnostics-and-conformance.md#required-executable-evidence`](../60-specification/formal-semantic-kernel/beam-diagnostics-and-conformance.md#required-executable-evidence) | c010 #10 | traced |
| FK-OBL-015 | Exact selection, backward-interface, deterministic artifact, erasure, and sole-OTP-compiler boundary | [`beam-diagnostics-and-conformance.md#required-executable-evidence`](../60-specification/formal-semantic-kernel/beam-diagnostics-and-conformance.md#required-executable-evidence) | c010 #3, #14, #17 | partial |

Provisional coverage: 13 `traced`, 2 `partial` (FK-OBL-009 combined fixture, FK-OBL-015 sole-OTP-boundary is architectural). The compiler-side PR establishes the authoritative mapping and gap set.

## Registry — effects-and-handlers (`EF`, 0.1.5)

Evidence labels refer to tests in
[`c005_effects_test.exs`](https://github.com/pcharbon70/catena/blob/rewrite/test/catena/c005_effects_test.exs).
The mapping is provisional; the compiler-side tagging PR establishes the
authoritative test-to-obligation links and the gap set.

- **c005 #1** *deep handlers resume exactly once in the reference model and generated BEAM*
- **c005 #2** *a clause can abort without invoking the captured continuation*
- **c005 #3** *selection rejects missing and ambiguous capabilities and accepts a qualifier*
- **c005 #4** *rejects incomplete handlers and statically non-affine resumptions*
- **c005 #5** *operation callbacks must have a closed empty effect row*
- **c005 #6** *effectful definitions forward their selected capability through a CPS worker*
- **c005 #7** *handler clauses may request an explicitly declared outer capability*
- **c005 #8** *effect diagnostics cover type mismatch, missing return, and capability escape*
- **c005 #9** *the runtime token traps before a second continuation entry*
- **c005 #10** *generic effects, unnamed uses, open rows, and pure direct lowering round trip*
- **c005 #11** *typed-core verification rejects forged effect-row evidence*
- **c005 #12** *operations accept ordinary data and closed pure functions*
- **c005 #13** *effectful branches preserve existing exhaustive match semantics*
- **c005 #14** *interfaces preserve nominal effect identities across module checking*
- **c005 #15** *handler arguments evaluate left to right in the outer capability scope*
- **c005 #16** *two capabilities of one family remain distinct and subtraction removes only one*
- **c005 #17** *version 0.1.5 interfaces reject duplicate nominal effect identities*
- **c005 #18** *reversing nested handlers observably reverses their return transformations*
- **c005 #19** *affine checking permits one resume on each mutually exclusive branch*

| ID | Obligation | Normative anchor | Evidence | Status |
| --- | --- | --- | --- | --- |
| EF-OBL-001 | Row sorting preserves distinct capability identities and order | [`capabilities-rows-and-selection.md#hybrid-row-equality`](../60-specification/effects-and-handlers/capabilities-rows-and-selection.md#hybrid-row-equality) | c005 #16 | traced |
| EF-OBL-002 | A locally fresh capability must not escape into a public scheme or data | [`capabilities-rows-and-selection.md#scope-and-abstraction`](../60-specification/effects-and-handlers/capabilities-rows-and-selection.md#scope-and-abstraction) | EFX003; c005 #8 | traced |
| EF-OBL-003 | Operation parameter and reply types exclude effectful, open, capability, handler, and resumption values | [`declarations-requests-and-signatures.md#nominal-declarations`](../60-specification/effects-and-handlers/declarations-requests-and-signatures.md#nominal-declarations) | c005 #5, #12 | traced |
| EF-OBL-004 | Lexical nesting must not break a capability tie; qualified form mandatory on ambiguity | [`declarations-requests-and-signatures.md#request-sites`](../60-specification/effects-and-handlers/declarations-requests-and-signatures.md#request-sites) | EFX004, EFX005; c005 #3 | traced |
| EF-OBL-005 | Public definitions must write their `uses` entries | [`declarations-requests-and-signatures.md#function-signatures`](../60-specification/effects-and-handlers/declarations-requests-and-signatures.md#function-signatures) | c005 #10 | partial |
| EF-OBL-006 | Anonymous function bodies must have a closed empty latent effect row | [`declarations-requests-and-signatures.md#function-signatures`](../60-specification/effects-and-handlers/declarations-requests-and-signatures.md#function-signatures) | CPS001, EFX003; c005 #5 | traced |
| EF-OBL-007 | Every handler has exactly one return clause and one operation clause per operation; args evaluate left to right | [`declarations-requests-and-signatures.md#named-handlers`](../60-specification/effects-and-handlers/declarations-requests-and-signatures.md#named-handlers) | EFX006; c005 #4, #15 | traced |
| EF-OBL-008 | The union of clause rows must equal the handler declaration | [`declarations-requests-and-signatures.md#named-handlers`](../60-specification/effects-and-handlers/declarations-requests-and-signatures.md#named-handlers) | EFX008; c005 #7 | traced |
| EF-OBL-009 | A resumption is a binder; it must not be returned, stored, placed in data, or escape | [`deep-handlers-and-affine-resumptions.md#affine-resumption-form`](../60-specification/effects-and-handlers/deep-handlers-and-affine-resumptions.md#affine-resumption-form) | RES001, RES002; c005 #4, #19 | traced |
| EF-OBL-010 | An inference-independent verifier rechecks effect judgment and rejects forged core | [`typed-core-cps-and-beam.md#explicit-typed-core`](../60-specification/effects-and-handlers/typed-core-cps-and-beam.md#explicit-typed-core) | c005 #11 | traced |
| EF-OBL-011 | The reference evaluator materializes and folds the free-request form independently of production | [`typed-core-cps-and-beam.md#reference-semantics`](../60-specification/effects-and-handlers/typed-core-cps-and-beam.md#reference-semantics) | c005 #1 | traced |
| EF-OBL-012 | Adding 0.1.5 support must not CPS-translate unrelated C001–C004 definitions | [`typed-core-cps-and-beam.md#effect-directed-cps`](../60-specification/effects-and-handlers/typed-core-cps-and-beam.md#effect-directed-cps) | c005 #6, #10 | traced |
| EF-OBL-013 | Backend must not introduce Rust, Python, Core Erlang, BEAM assembly, or another VM | [`typed-core-cps-and-beam.md#beam-boundary-and-interfaces`](../60-specification/effects-and-handlers/typed-core-cps-and-beam.md#beam-boundary-and-interfaces) | — | untraced |
| EF-OBL-014 | Nominal generic and nongeneric families with multi-parameter operations | [`diagnostics-and-conformance.md#positive-corpus`](../60-specification/effects-and-handlers/diagnostics-and-conformance.md#positive-corpus) | c005 #10, #12 | traced |
| EF-OBL-015 | Operation parameters accept ordinary data and closed pure functions | [`diagnostics-and-conformance.md#positive-corpus`](../60-specification/effects-and-handlers/diagnostics-and-conformance.md#positive-corpus) | c005 #12 | traced |
| EF-OBL-016 | Two capabilities of one family remain distinct; subtraction removes only one | [`diagnostics-and-conformance.md#positive-corpus`](../60-specification/effects-and-handlers/diagnostics-and-conformance.md#positive-corpus) | c005 #14, #16 | traced |
| EF-OBL-017 | Repeated requests through one capability coalesce to one identity | [`diagnostics-and-conformance.md#positive-corpus`](../60-specification/effects-and-handlers/diagnostics-and-conformance.md#positive-corpus) | c005 #1, #6 | partial |
| EF-OBL-018 | Named and unnamed `uses` entries plus an open row tail | [`diagnostics-and-conformance.md#positive-corpus`](../60-specification/effects-and-handlers/diagnostics-and-conformance.md#positive-corpus) | c005 #10 | traced |
| EF-OBL-019 | Normal return, abort, one resume, repeated deep requests, and unrelated forwarding | [`diagnostics-and-conformance.md#positive-corpus`](../60-specification/effects-and-handlers/diagnostics-and-conformance.md#positive-corpus) | c005 #1, #2 | traced |
| EF-OBL-020 | Nested handlers of different families and of one family | [`diagnostics-and-conformance.md#positive-corpus`](../60-specification/effects-and-handlers/diagnostics-and-conformance.md#positive-corpus) | c005 #18 | traced |
| EF-OBL-021 | Observable handler-order reversal | [`diagnostics-and-conformance.md#positive-corpus`](../60-specification/effects-and-handlers/diagnostics-and-conformance.md#positive-corpus) | c005 #18 | traced |
| EF-OBL-022 | Clause-introduced outer effects and exact selected-identity subtraction | [`diagnostics-and-conformance.md#positive-corpus`](../60-specification/effects-and-handlers/diagnostics-and-conformance.md#positive-corpus) | c005 #6, #7, #15, #16 | traced |
| EF-OBL-023 | Reference and BEAM traces agree on values and ordered events | [`diagnostics-and-conformance.md#differential-traces-and-compatibility`](../60-specification/effects-and-handlers/diagnostics-and-conformance.md#differential-traces-and-compatibility) | c005 #1 | traced |
| EF-OBL-024 | Dynamic consumed-token traps before a second continuation entry | [`diagnostics-and-conformance.md#positive-corpus`](../60-specification/effects-and-handlers/diagnostics-and-conformance.md#positive-corpus) | c005 #9, #19 | traced |
| EF-OBL-025 | 0.1.5 interface round trips, cross-module handlers, and 0.1.2–0.1.4 compatibility | [`diagnostics-and-conformance.md#positive-corpus`](../60-specification/effects-and-handlers/diagnostics-and-conformance.md#positive-corpus) | c005 #14, #17 | traced |
| EF-OBL-026 | Negative battery: malformed, duplicate, unknown, arity/type, missing/ambiguous capability, wrong family, hidden, escape, missing return, incomplete, mismatch, resumption misuse, forged core, bad interface | [`diagnostics-and-conformance.md#negative-corpus`](../60-specification/effects-and-handlers/diagnostics-and-conformance.md#negative-corpus) | c005 #3, #4, #8, #11, #17 | traced |
| EF-OBL-027 | Effectful branches preserve exhaustive match semantics | [`diagnostics-and-conformance.md#positive-corpus`](../60-specification/effects-and-handlers/diagnostics-and-conformance.md#positive-corpus) | c005 #13 | traced |

Provisional coverage: 24 `traced`, 2 `partial`, 1 `untraced` (EF-OBL-005 public-`uses` writing; EF-OBL-013 backend language boundary is architectural; EF-OBL-017 coalescing observation). The compiler-side PR establishes the authoritative mapping and gap set.

## Registry — traits-and-categorical-operations (`TR`, 0.1.4)

Evidence labels refer to tests in
[`c004_categorical_test.exs`](https://github.com/pcharbon70/catena/blob/rewrite/test/catena/c004_categorical_test.exs).
The mapping is provisional; the compiler-side tagging PR establishes the
authoritative test-to-obligation links and the gap set. TR has nine tests
against thirty-two obligations, so more entries are provisional or allow-listed
than in the CC, FK, or EF areas.

- **c004 #1** *standard interface freezes all seventeen approachable capabilities and method ABI*
- **c004 #2** *standard List mapping and reduction stay stack safe on large inputs*
- **c004 #3** *AST 0.1.4 derives implicit instances and executable type-qualified operations*
- **c004 #4** *all standard capabilities resolve coherent parent evidence and Workflow has two useful witnesses*
- **c004 #5** *law testing requires explicit Equatable evidence and bounded function samples*
- **c004 #6** *package specialization resolves evidence to a direct call and is deterministic*
- **c004 #7** *toolchain manifest writes the declared companion BEAM relative to itself*
- **c004 #8** *0.1.4 rejects reserved law trust and incomplete template closure*
- **c004 #9** *type term codec preserves higher-kinded applications*

| ID | Obligation | Normative anchor | Evidence | Status |
| --- | --- | --- | --- | --- |
| TR-OBL-001 | Each argument matches its trait parameter kind | [`declarations-instances-and-coherence.md#kinds-and-relations`](../60-specification/traits-and-categorical-operations/declarations-instances-and-coherence.md#kinds-and-relations) | TRT002; c004 #9 | traced |
| TR-OBL-002 | Instance set is globally non-overlapping; no local preference | [`declarations-instances-and-coherence.md#ownership-and-overlap`](../60-specification/traits-and-categorical-operations/declarations-instances-and-coherence.md#ownership-and-overlap) | TRT003; c004 #8 | partial |
| TR-OBL-003 | Functional-dependency output positions unify at all outputs | [`declarations-instances-and-coherence.md#ownership-and-overlap`](../60-specification/traits-and-categorical-operations/declarations-instances-and-coherence.md#ownership-and-overlap) | TRT002 | partial |
| TR-OBL-004 | Instance context constraints are structurally decreasing | [`declarations-instances-and-coherence.md#termination`](../60-specification/traits-and-categorical-operations/declarations-instances-and-coherence.md#termination) | TRT003; c004 #8 | partial |
| TR-OBL-005 | Parent routes select one globally coherent instance | [`declarations-instances-and-coherence.md#parent-evidence`](../60-specification/traits-and-categorical-operations/declarations-instances-and-coherence.md#parent-evidence) | c004 #4 | traced |
| TR-OBL-006 | Law-suite equality comes from an explicit `Equatable` | [`laws-derivation-and-testing.md#law-domain`](../60-specification/traits-and-categorical-operations/laws-derivation-and-testing.md#law-domain) | c004 #5 | traced |
| TR-OBL-007 | Reserved law trust is rejected in 0.1.4 input | [`laws-derivation-and-testing.md#evidence-tiers`](../60-specification/traits-and-categorical-operations/laws-derivation-and-testing.md#evidence-tiers) | TRT005; c004 #8 | traced |
| TR-OBL-008 | Standard recursive collection instances use structural derivation | [`laws-derivation-and-testing.md#structural-derivation`](../60-specification/traits-and-categorical-operations/laws-derivation-and-testing.md#structural-derivation) | DRV001; c004 #3 | traced |
| TR-OBL-009 | Generated checks record trait, instance, and law identity | [`laws-derivation-and-testing.md#law-testing`](../60-specification/traits-and-categorical-operations/laws-derivation-and-testing.md#law-testing) | c004 #3 | partial |
| TR-OBL-010 | Mapper, reducer, or collector must not reorder, duplicate, or short-circuit | [`operational-semantics.md#strict-sequential-baseline`](../60-specification/traits-and-categorical-operations/operational-semantics.md#strict-sequential-baseline) | c004 #2 | partial |
| TR-OBL-011 | Selection and erasure must not change callback count, order, or exceptions | [`operational-semantics.md#divergence-and-effects`](../60-specification/traits-and-categorical-operations/operational-semantics.md#divergence-and-effects) | c004 #6 | partial |
| TR-OBL-012 | Standard list and collection instances are stack safe | [`operational-semantics.md#stack-and-cost-obligations`](../60-specification/traits-and-categorical-operations/operational-semantics.md#stack-and-cost-obligations) | c004 #2 | traced |
| TR-OBL-013 | A general derived operation must disclose or reject unsafe recursion | [`operational-semantics.md#stack-and-cost-obligations`](../60-specification/traits-and-categorical-operations/operational-semantics.md#stack-and-cost-obligations) | — | untraced |
| TR-OBL-014 | 0.1.4 interface decoders attach to 0.1.2/0.1.3 evidence | [`interfaces-specialization-and-beam.md#interface-version-014`](../60-specification/traits-and-categorical-operations/interfaces-specialization-and-beam.md#interface-version-014) | c004 #7 | partial |
| TR-OBL-015 | Identical inputs produce byte-identical companion BEAM | [`interfaces-specialization-and-beam.md#specialization`](../60-specification/traits-and-categorical-operations/interfaces-specialization-and-beam.md#specialization) | c004 #6, #7 | traced |
| TR-OBL-016 | Instance identity is compile-time-only; it must not appear at runtime | [`interfaces-specialization-and-beam.md#erasure`](../60-specification/traits-and-categorical-operations/interfaces-specialization-and-beam.md#erasure) | c004 #6 | traced |
| TR-OBL-017 | An implementation supplies exactly the minimal declared methods | [`standard-hierarchy-and-vocabulary.md#canonical-public-surface`](../60-specification/traits-and-categorical-operations/standard-hierarchy-and-vocabulary.md#canonical-public-surface) | c004 #1 | traced |
| TR-OBL-018 | Must not relabel an older valid or invalid program | [`diagnostics-and-conformance.md#stable-diagnostics`](../60-specification/traits-and-categorical-operations/diagnostics-and-conformance.md#stable-diagnostics) | — | partial |
| TR-OBL-019 | Generated forms show direct calls and no dictionary or reflective identity | [`diagnostics-and-conformance.md#erasure-and-compatibility-checks`](../60-specification/traits-and-categorical-operations/diagnostics-and-conformance.md#erasure-and-compatibility-checks) | c004 #6 | traced |
| TR-OBL-020 | All seventeen traits and every direct parent edge | [`diagnostics-and-conformance.md#positive-corpus`](../60-specification/traits-and-categorical-operations/diagnostics-and-conformance.md#positive-corpus) | c004 #1, #4 | traced |
| TR-OBL-021 | The Workflow and CollectingMapper diamonds share ancestor evidence | [`diagnostics-and-conformance.md#positive-corpus`](../60-specification/traits-and-categorical-operations/diagnostics-and-conformance.md#positive-corpus) | c004 #4 | traced |
| TR-OBL-022 | Value-, unary-, and binary-constructor-kinded heads | [`diagnostics-and-conformance.md#positive-corpus`](../60-specification/traits-and-categorical-operations/diagnostics-and-conformance.md#positive-corpus) | c004 #9 | traced |
| TR-OBL-023 | Parameterized instances, functional dependencies, and associated types | [`diagnostics-and-conformance.md#positive-corpus`](../60-specification/traits-and-categorical-operations/diagnostics-and-conformance.md#positive-corpus) | c004 #3 | traced |
| TR-OBL-024 | Two useful examples for each unitless capability | [`diagnostics-and-conformance.md#positive-corpus`](../60-specification/traits-and-categorical-operations/diagnostics-and-conformance.md#positive-corpus) | c004 #4 | partial |
| TR-OBL-025 | The six structural derivations, including two TwoSlotMapper targets | [`diagnostics-and-conformance.md#positive-corpus`](../60-specification/traits-and-categorical-operations/diagnostics-and-conformance.md#positive-corpus) | c004 #3 | traced |
| TR-OBL-026 | Promised, tested, and derived law evidence | [`diagnostics-and-conformance.md#positive-corpus`](../60-specification/traits-and-categorical-operations/diagnostics-and-conformance.md#positive-corpus) | c004 #5, #8 | traced |
| TR-OBL-027 | Explicit `Equatable` law checks and bounded function samples | [`diagnostics-and-conformance.md#positive-corpus`](../60-specification/traits-and-categorical-operations/diagnostics-and-conformance.md#positive-corpus) | c004 #5 | traced |
| TR-OBL-028 | Callback count and order observations | [`diagnostics-and-conformance.md#positive-corpus`](../60-specification/traits-and-categorical-operations/diagnostics-and-conformance.md#positive-corpus) | c004 #6 | partial |
| TR-OBL-029 | Standard `List` `Mapper`/`Reducible` on 250,000+ elements without stack exhaustion | [`diagnostics-and-conformance.md#positive-corpus`](../60-specification/traits-and-categorical-operations/diagnostics-and-conformance.md#positive-corpus) | c004 #2 | traced |
| TR-OBL-030 | Deterministic interface round trips and package specialization | [`diagnostics-and-conformance.md#positive-corpus`](../60-specification/traits-and-categorical-operations/diagnostics-and-conformance.md#positive-corpus) | c004 #6, #7 | traced |
| TR-OBL-031 | Reference-evaluator/BEAM agreement for generated operations | [`diagnostics-and-conformance.md#positive-corpus`](../60-specification/traits-and-categorical-operations/diagnostics-and-conformance.md#positive-corpus) | c004 #6 | partial |
| TR-OBL-032 | Negative battery: wrong kinds, undeclared, cycles, foreign ownership, overlap, nondecreasing, missing/extra methods, unresolved/ambiguous, reserved tiers, invalid derivation, tampered interfaces, missing helpers, recursive specialization, exhausted budgets | [`diagnostics-and-conformance.md#negative-corpus`](../60-specification/traits-and-categorical-operations/diagnostics-and-conformance.md#negative-corpus) | c004 #8, #9 | partial |

Provisional coverage: 19 `traced`, 12 `partial`, 1 `untraced` (TR-OBL-013 unsafe-recursion disclosure). TR has the thinnest test-to-obligation ratio of the traced areas; the compiler-side gate is expected to carry a larger allow-list until dedicated tests are added.

## Registry — editions-and-feature-lifecycle (`ED`, 0.1.7)

Evidence labels refer to tests in
[`c008_editions_lifecycle_test.exs`](https://github.com/pcharbon70/catena/blob/rewrite/test/catena/c008_editions_lifecycle_test.exs).
The mapping is provisional; the compiler-side tagging PR establishes the
authoritative test-to-obligation links and the gap set.

- **c008 #1** *the language registry exposes exact retained selections and a closed lifecycle*
- **c008 #2** *selection validation rejects aliases, mismatches, duplicate previews, and unknown pins*
- **c008 #3** *every retained exact revision compiles through the 0.1.7 artifact schema*
- **c008 #4** *a module-level selection cannot contradict its package selection*
- **c008 #5** *standalone compilation reports current selection and legacy inference without byte changes*
- **c008 #6** *an explicit older pin rejects newer constructs but accepts neutral newer transport*
- **c008 #7** *0.1.2 matching is not mistaken for 0.1.3 clause conditions*
- **c008 #8** *0.1.7 retains 0.1.6 verification-only definitions*
- **c008 #9** *0.1.7 package manifests require exact selection and legacy manifests report safe additions*
- **c008 #10** *making a legacy manifest selection explicit preserves all output bytes*
- **c008 #11** *interfaces bind enabled and publicly required previews and consumers fail closed*
- **c008 #12** *0.1.7 artifacts and assurance bind the package selection without runtime dispatch*
- **c008 #13** *specialization identities change with exact selection*
- **c008 #14** *the 0.1.7 policy algebra constrains selection and agrees with its reference oracle*
- **c008 #15** *trust roots and signatures use one declared version domain without fallback*
- **c008 #16** *language-info is available as mutation-free JSON from the CLI*

| ID | Obligation | Normative anchor | Evidence | Status |
| --- | --- | --- | --- | --- |
| ED-OBL-001 | Revision major/minor must equal its edition; numeric resemblance is not a substitution | [`edition-selection-and-applicability.md#version-axes`](../60-specification/editions-and-feature-lifecycle/edition-selection-and-applicability.md#version-axes) | EDN001; c008 #2 | traced |
| ED-OBL-002 | Package manifest requires `edition`, `language_revision`, and `previews` | [`edition-selection-and-applicability.md#package-selection`](../60-specification/editions-and-feature-lifecycle/edition-selection-and-applicability.md#package-selection) | c008 #9 | traced |
| ED-OBL-003 | Edition names a retained edition, revision a published revision, previews a duplicate-free sorted accepted list | [`edition-selection-and-applicability.md#package-selection`](../60-specification/editions-and-feature-lifecycle/edition-selection-and-applicability.md#package-selection) | c008 #2, #9 | traced |
| ED-OBL-004 | Construct availability is checked against the selection; a newer construct is rejected | [`edition-selection-and-applicability.md#package-selection`](../60-specification/editions-and-feature-lifecycle/edition-selection-and-applicability.md#package-selection) | EDN001; c008 #6, #7 | traced |
| ED-OBL-005 | A module-level selection must equal the package selection or `EDN001` | [`edition-selection-and-applicability.md#package-selection`](../60-specification/editions-and-feature-lifecycle/edition-selection-and-applicability.md#package-selection) | c008 #4 | traced |
| ED-OBL-006 | Standalone compilation reports the resolved selection in success output and every artifact | [`edition-selection-and-applicability.md#standalone-and-interactive-selection`](../60-specification/editions-and-feature-lifecycle/edition-selection-and-applicability.md#standalone-and-interactive-selection) | c008 #5 | traced |
| ED-OBL-007 | Legacy inference issues the `EDN002` advisory and reports the inferred selection | [`edition-selection-and-applicability.md#standalone-and-interactive-selection`](../60-specification/editions-and-feature-lifecycle/edition-selection-and-applicability.md#standalone-and-interactive-selection) | c008 #5, #9, #10 | traced |
| ED-OBL-008 | No numeric-larger rule preference when applicability overlaps | [`edition-selection-and-applicability.md#cumulative-applicability`](../60-specification/editions-and-feature-lifecycle/edition-selection-and-applicability.md#cumulative-applicability) | c008 #2 | partial |
| ED-OBL-009 | Accept every published stable revision; an exact pin must not float | [`edition-selection-and-applicability.md#retention`](../60-specification/editions-and-feature-lifecycle/edition-selection-and-applicability.md#retention) | c008 #1, #3, #6 | traced |
| ED-OBL-010 | Changing the current default must not change a package with an explicit pin | [`edition-selection-and-applicability.md#retention`](../60-specification/editions-and-feature-lifecycle/edition-selection-and-applicability.md#retention) | c008 #6 | partial |
| ED-OBL-011 | A language change occurs at a revision boundary and satisfies its compatibility rule | [`edition-selection-and-applicability.md#prototype-compatibility-boundary`](../60-specification/editions-and-feature-lifecycle/edition-selection-and-applicability.md#prototype-compatibility-boundary) | c008 #1 | partial |
| ED-OBL-012 | A withdrawn or removed identifier must not be reused | [`feature-lifecycle-and-compatibility.md#lifecycle-registry`](../60-specification/editions-and-feature-lifecycle/feature-lifecycle-and-compatibility.md#lifecycle-registry) | c008 #1, #14 | partial |
| ED-OBL-013 | Reserved features must not appear as package previews | [`feature-lifecycle-and-compatibility.md#states-and-transitions`](../60-specification/editions-and-feature-lifecycle/feature-lifecycle-and-compatibility.md#states-and-transitions) | c008 #2 | partial |
| ED-OBL-014 | A preview name must be in the published preview set | [`feature-lifecycle-and-compatibility.md#preview-selection`](../60-specification/editions-and-feature-lifecycle/feature-lifecycle-and-compatibility.md#preview-selection) | PRV001; c008 #2 | traced |
| ED-OBL-015 | Implementations must not add vendor preview names | [`feature-lifecycle-and-compatibility.md#preview-selection`](../60-specification/editions-and-feature-lifecycle/feature-lifecycle-and-compatibility.md#preview-selection) | — | untraced |
| ED-OBL-016 | A compatibility change identifies the affected dimensions | [`feature-lifecycle-and-compatibility.md#compatibility-dimensions`](../60-specification/editions-and-feature-lifecycle/feature-lifecycle-and-compatibility.md#compatibility-dimensions) | c008 #14 | traced |
| ED-OBL-017 | A consumer must understand the interface schema, nominal identities, and types | [`feature-lifecycle-and-compatibility.md#package-local-interoperation`](../60-specification/editions-and-feature-lifecycle/feature-lifecycle-and-compatibility.md#package-local-interoperation) | c008 #11 | traced |
| ED-OBL-018 | Evidence or inherited public obligation must not appear in the interface | [`feature-lifecycle-and-compatibility.md#package-local-interoperation`](../60-specification/editions-and-feature-lifecycle/feature-lifecycle-and-compatibility.md#package-local-interoperation) | c008 #11 | partial |
| ED-OBL-019 | Generated runtime code must not dispatch on edition | [`feature-lifecycle-and-compatibility.md#package-local-interoperation`](../60-specification/editions-and-feature-lifecycle/feature-lifecycle-and-compatibility.md#package-local-interoperation) | c008 #12 | traced |
| ED-OBL-020 | Decoding an implication must not rewrite or redigest the artifact | [`interfaces-artifacts-and-governance.md#selection-bearing-interfaces`](../60-specification/editions-and-feature-lifecycle/interfaces-artifacts-and-governance.md#selection-bearing-interfaces) | c008 #10 | traced |
| ED-OBL-021 | Interfaces, artifacts, and assurance bind the resolved selection | [`interfaces-artifacts-and-governance.md#package-and-assurance-artifacts`](../60-specification/editions-and-feature-lifecycle/interfaces-artifacts-and-governance.md#package-and-assurance-artifacts) | c008 #3, #12, #13 | traced |
| ED-OBL-022 | Replacing any artifact component without recomputation or reauthorization must fail verification | [`interfaces-artifacts-and-governance.md#package-and-assurance-artifacts`](../60-specification/editions-and-feature-lifecycle/interfaces-artifacts-and-governance.md#package-and-assurance-artifacts) | c008 #15 | traced |
| ED-OBL-023 | Historical 0.1.6 artifacts remain independently verifiable with no cross-version fallback | [`interfaces-artifacts-and-governance.md#version-aware-signature-domains`](../60-specification/editions-and-feature-lifecycle/interfaces-artifacts-and-governance.md#version-aware-signature-domains) | c008 #8, #15 | traced |
| ED-OBL-024 | Edition, revision, preview, migration, and governance selection must not cause runtime dispatch | [`interfaces-artifacts-and-governance.md#beam-metadata-and-erasure`](../60-specification/editions-and-feature-lifecycle/interfaces-artifacts-and-governance.md#beam-metadata-and-erasure) | c008 #12 | traced |
| ED-OBL-025 | No retry of another version domain after a signature failure | [`interfaces-artifacts-and-governance.md#version-aware-signature-domains`](../60-specification/editions-and-feature-lifecycle/interfaces-artifacts-and-governance.md#version-aware-signature-domains) | c008 #15 | traced |
| ED-OBL-026 | Safe edits are reported; C008 must not modify a file | [`migration-diagnostics-and-conformance.md#safe-edit-suggestions`](../60-specification/editions-and-feature-lifecycle/migration-diagnostics-and-conformance.md#safe-edit-suggestions) | c008 #9 | traced |
| ED-OBL-027 | The `EDN002` advisory must not alter source, interfaces, BEAM bytes, assurance, signing payloads, or paths | [`migration-diagnostics-and-conformance.md#legacy-manifest-behavior`](../60-specification/editions-and-feature-lifecycle/migration-diagnostics-and-conformance.md#legacy-manifest-behavior) | c008 #5, #10 | traced |
| ED-OBL-028 | `language-info` returns canonical mutation-free JSON and performs no mutation | [`migration-diagnostics-and-conformance.md#language-information-contract`](../60-specification/editions-and-feature-lifecycle/migration-diagnostics-and-conformance.md#language-information-contract) | c008 #16 | traced |
| ED-OBL-029 | Corpus: every retained revision plus rejection of invalid pairs, floats, aliases, prereleases, and unknown pins | [`migration-diagnostics-and-conformance.md#conformance-corpus`](../60-specification/editions-and-feature-lifecycle/migration-diagnostics-and-conformance.md#conformance-corpus) | c008 #1, #2, #3 | traced |
| ED-OBL-030 | Corpus: lifecycle edges, identifier non-reuse, stale preview opt-in, revision-bound state lookup | [`migration-diagnostics-and-conformance.md#conformance-corpus`](../60-specification/editions-and-feature-lifecycle/migration-diagnostics-and-conformance.md#conformance-corpus) | c008 #14 | partial |
| ED-OBL-031 | Corpus: private vs public preview propagation and downstream opt-in rejection | [`migration-diagnostics-and-conformance.md#conformance-corpus`](../60-specification/editions-and-feature-lifecycle/migration-diagnostics-and-conformance.md#conformance-corpus) | PRV002; c008 #11 | traced |
| ED-OBL-032 | Corpus: exact selection binding across digests, specialization, BEAM metadata, assurance, approvals, and governance | [`migration-diagnostics-and-conformance.md#conformance-corpus`](../60-specification/editions-and-feature-lifecycle/migration-diagnostics-and-conformance.md#conformance-corpus) | c008 #12, #13 | traced |
| ED-OBL-033 | Corpus: 0.1.6 verification, 0.1.7 domains, and downgrade, substitution, removal, and tampering attacks | [`migration-diagnostics-and-conformance.md#conformance-corpus`](../60-specification/editions-and-feature-lifecycle/migration-diagnostics-and-conformance.md#conformance-corpus) | c008 #15 | traced |
| ED-OBL-034 | Corpus: default deprecation warnings and project/governance promotion to failure | [`migration-diagnostics-and-conformance.md#conformance-corpus`](../60-specification/editions-and-feature-lifecycle/migration-diagnostics-and-conformance.md#conformance-corpus) | DEP001 | partial |
| ED-OBL-035 | Corpus: absence of runtime edition dispatch and preservation of 0.1.6 erasure guarantees | [`migration-diagnostics-and-conformance.md#conformance-corpus`](../60-specification/editions-and-feature-lifecycle/migration-diagnostics-and-conformance.md#conformance-corpus) | c008 #8, #12 | traced |
| ED-OBL-036 | Corpus: normalized interfaces across retained revisions and modelled future edition boundaries | [`migration-diagnostics-and-conformance.md#conformance-corpus`](../60-specification/editions-and-feature-lifecycle/migration-diagnostics-and-conformance.md#conformance-corpus) | c008 #11 | partial |

Provisional coverage: 26 `traced`, 9 `partial`, 1 `untraced` (ED-OBL-015 vendor-preview prohibition). The compiler-side PR establishes the authoritative mapping and gap set.

## Registry — specifications-and-governance (`SG`, 0.1.6)

Evidence labels refer to tests in
[`c006_specification_governance_test.exs`](https://github.com/pcharbon70/catena/blob/rewrite/test/catena/c006_specification_governance_test.exs).
The mapping is provisional; the compiler-side tagging PR establishes the
authoritative test-to-obligation links and the gap set. SG has the densest
test corpus of the traced areas.

- **c006 #1** *Catena's JCS profile is deterministic and rejects ambiguous signed JSON*
- **c006 #2** *OTP 29 Ed25519 verification agrees with the RFC 8032 empty-message vector*
- **c006 #3** *AST 0.1.6 type-checks exact rules, exports claim summaries, and erases checkers*
- **c006 #4** *fully discharged specifications do not change emitted BEAM bytes*
- **c006 #5** *runtime references to verification-only definitions fail before lowering*
- **c006 #6** *claim subject and example failures keep stable diagnostic families*
- **c006 #7** *all 0.1.6 claim subject kinds resolve against the typed module and package graph*
- **c006 #8** *semantic claim digests ignore JSON formatting but change with meaning*
- **c006 #9** *mistyped, effectful, failing, and over-budget rule checkers remain distinct*
- **c006 #10** *verification definitions cannot become runtime exports*
- **c006 #11** *the rule evaluator reports deterministic budget exhaustion separately*
- **c006 #12** *production policy evaluation agrees with the independent oracle*
- **c006 #13** *governance combines every matching policy additively and fails closed*
- **c006 #14** *the 20000-step policy budget is shared across every matching policy*
- **c006 #15** *package, module, subject, action, output, interface, and profile scopes add*
- **c006 #16** *trust roots count distinct Ed25519 principals and require old plus new rotation authority*
- **c006 #17** *signature thresholds reject duplicate actors and cross-domain substitution*
- **c006 #18** *predeclared recovery can replace normal authority without new-root self-authorization*
- **c006 #19** *delegated signatures remain bounded by action, subject, profile, and sequence*
- **c006 #20** *assumptions count only when policy names them and an authorized role signs the exact decision*
- **c006 #21** *external attestations are signed, sequence-bounded, and claim-bound*
- **c006 #22** *lifecycle replay rejects skipped, terminal, and broken hash-chain transitions*
- **c006 #23** *activate requires a signed lifecycle transition into Active*
- **c006 #24** *lifecycle replay covers every valid edge and rejects reordering*
- **c006 #25** *0.1.6 package build stages outputs, emits a sidecar, and verifies exact artifacts*
- **c006 #26** *fully discharged specifications leave every package BEAM byte-identical*
- **c006 #27** *a governed build consumes compiler evidence and emits the external signing payload*
- **c006 #28** *imported interfaces carry claim obligations and semantic dependency digests*
- **c006 #29** *signed assurance manifests bind the exact payload and artifact*
- **c006 #30** *publish exposes an exact candidate payload, writes nothing, then accepts external signing*
- **c006 #31** *failed governed gates and unsafe paths leave final outputs absent*
- **c006 #32** *package-level claim subjects must name declared outputs, interfaces, actions, and profiles*
- **c006 #33** *artifact substitution invalidates a previously valid assurance manifest*
- **c006 #34** *assurance verification refuses artifact paths that escape through symlinks*

| ID | Obligation | Normative anchor | Evidence | Status |
| --- | --- | --- | --- | --- |
| SG-OBL-001 | Every rule and example is well formed, type checked, and evaluated | [`overview-and-adoption.md#adoption-boundary`](../60-specification/specifications-and-governance/overview-and-adoption.md#adoption-boundary) | c006 #3 | traced |
| SG-OBL-002 | Verification material satisfies the erasure and artifact-binding rules | [`overview-and-adoption.md#adoption-boundary`](../60-specification/specifications-and-governance/overview-and-adoption.md#adoption-boundary) | c006 #3, #27 | traced |
| SG-OBL-003 | Every matching policy is enforced | [`overview-and-adoption.md#adoption-boundary`](../60-specification/specifications-and-governance/overview-and-adoption.md#adoption-boundary) | c006 #13 | traced |
| SG-OBL-004 | Malformed, missing, stale, unauthorized, or contradictory material is rejected | [`overview-and-adoption.md#adoption-boundary`](../60-specification/specifications-and-governance/overview-and-adoption.md#adoption-boundary) | c006 #13 | partial |
| SG-OBL-005 | No ignore/force switch reports a governed action as ungoverned | [`overview-and-adoption.md#adoption-boundary`](../60-specification/specifications-and-governance/overview-and-adoption.md#adoption-boundary) | — | untraced |
| SG-OBL-006 | Narrower scope must not weaken policy inherited from a broader scope | [`overview-and-adoption.md#adoption-boundary`](../60-specification/specifications-and-governance/overview-and-adoption.md#adoption-boundary) | c006 #13, #15 | traced |
| SG-OBL-007 | Diagnostics use formal terminology internally while leading with source concepts | [`overview-and-adoption.md#public-and-internal-vocabulary`](../60-specification/specifications-and-governance/overview-and-adoption.md#public-and-internal-vocabulary) | c006 #6 | partial |
| SG-OBL-008 | A future parser must elaborate to the same specification graph | [`claims-examples-and-checking.md#module-declarations`](../60-specification/specifications-and-governance/claims-examples-and-checking.md#module-declarations) | c006 #3 | partial |
| SG-OBL-009 | The compiler resolves subjects against the typed module and package graph | [`claims-examples-and-checking.md#subject-resolution`](../60-specification/specifications-and-governance/claims-examples-and-checking.md#subject-resolution) | SPC001; c006 #7, #32 | traced |
| SG-OBL-010 | A meaning-preserving change keeps the semantic digest; a meaning change alters it | [`claims-examples-and-checking.md#stable-identity-and-semantic-digest`](../60-specification/specifications-and-governance/claims-examples-and-checking.md#stable-identity-and-semantic-digest) | c006 #8 | traced |
| SG-OBL-011 | An assumption remains distinct from technical evidence and approval | [`claims-examples-and-checking.md#claim-vocabulary`](../60-specification/specifications-and-governance/claims-examples-and-checking.md#claim-vocabulary) | c006 #20 | traced |
| SG-OBL-012 | A rule checker is verification-only, pure, total, and effect-free | [`claims-examples-and-checking.md#rule-checking-fragment`](../60-specification/specifications-and-governance/claims-examples-and-checking.md#rule-checking-fragment) | SPC003; c006 #9, #11 | traced |
| SG-OBL-013 | Verification-only definitions are absent from the runtime definition | [`claims-examples-and-checking.md#erasure-dependency`](../60-specification/specifications-and-governance/claims-examples-and-checking.md#erasure-dependency) | ERS001; c006 #5, #10 | traced |
| SG-OBL-014 | A signature from one version domain must not verify in another | [`evidence-identity-and-lifecycle.md#canonical-signed-values`](../60-specification/specifications-and-governance/evidence-identity-and-lifecycle.md#canonical-signed-values) | c006 #17 | traced |
| SG-OBL-015 | The compiler verifies supplied signatures and must never handle private keys | [`evidence-identity-and-lifecycle.md#offline-trust-root`](../60-specification/specifications-and-governance/evidence-identity-and-lifecycle.md#offline-trust-root) | c006 #27, #30 | traced |
| SG-OBL-016 | `activate` requires a contiguous signed `Accepted -> Active` transition | [`evidence-identity-and-lifecycle.md#immutable-transition-history`](../60-specification/specifications-and-governance/evidence-identity-and-lifecycle.md#immutable-transition-history) | c006 #23 | traced |
| SG-OBL-017 | Approval, claim, subject, and artifact binding exactly reproduces the decision | [`evidence-identity-and-lifecycle.md#immutable-transition-history`](../60-specification/specifications-and-governance/evidence-identity-and-lifecycle.md#immutable-transition-history) | c006 #28, #29 | traced |
| SG-OBL-018 | Sequences are contiguous, prior digests match, and every edge appears; reordering, deletion, and skipping are rejected | [`evidence-identity-and-lifecycle.md#immutable-transition-history`](../60-specification/specifications-and-governance/evidence-identity-and-lifecycle.md#immutable-transition-history) | GOV004; c006 #22, #24 | traced |
| SG-OBL-019 | A module declaration must not contain private key material | [`scopes-policy-and-authorization.md#placement-and-coverage`](../60-specification/specifications-and-governance/scopes-policy-and-authorization.md#placement-and-coverage) | c006 #27 | partial |
| SG-OBL-020 | Participating policies combine additively; a narrower policy must not cancel a broader requirement | [`scopes-policy-and-authorization.md#placement-and-coverage`](../60-specification/specifications-and-governance/scopes-policy-and-authorization.md#placement-and-coverage) | c006 #13, #15 | traced |
| SG-OBL-021 | An invalid signature or unrecognized subject denies without shadowing or guessing | [`scopes-policy-and-authorization.md#decision-combination`](../60-specification/specifications-and-governance/scopes-policy-and-authorization.md#decision-combination) | GOV003; c006 #17 | traced |
| SG-OBL-022 | Ungoverned-shaped material encoded as a governed 0.1.6 action is rejected | [`scopes-policy-and-authorization.md#protected-actions`](../60-specification/specifications-and-governance/scopes-policy-and-authorization.md#protected-actions) | c006 #13 | partial |
| SG-OBL-023 | A failed gate before final output leaves no new or partially replaced output | [`artifacts-erasure-and-cli.md#package-build-transaction`](../60-specification/specifications-and-governance/artifacts-erasure-and-cli.md#package-build-transaction) | c006 #25, #30, #31 | traced |
| SG-OBL-024 | Declared output paths stay within the manifest directory unless explicitly allowed | [`artifacts-erasure-and-cli.md#package-build-transaction`](../60-specification/specifications-and-governance/artifacts-erasure-and-cli.md#package-build-transaction) | ART001; c006 #34 | traced |
| SG-OBL-025 | An admitted build must not change BEAM execution; changing a bound byte fails later verification | [`artifacts-erasure-and-cli.md#assurance-manifest`](../60-specification/specifications-and-governance/artifacts-erasure-and-cli.md#assurance-manifest) | c006 #25, #29, #33 | traced |
| SG-OBL-026 | Verification digests must not occur in runtime positions | [`artifacts-erasure-and-cli.md#erasure-rule`](../60-specification/specifications-and-governance/artifacts-erasure-and-cli.md#erasure-rule) | c006 #3, #5, #10 | traced |
| SG-OBL-027 | Adding fully discharged specifications must produce byte-identical output | [`artifacts-erasure-and-cli.md#erasure-rule`](../60-specification/specifications-and-governance/artifacts-erasure-and-cli.md#erasure-rule) | c006 #4, #26 | traced |
| SG-OBL-028 | Verification-only values must not be exported as callable runtime values | [`artifacts-erasure-and-cli.md#interface-boundary`](../60-specification/specifications-and-governance/artifacts-erasure-and-cli.md#interface-boundary) | c006 #3, #10, #28 | traced |
| SG-OBL-029 | Diagnostics name action, subject, policy, requirement, digest/state, and path | [`diagnostics-and-conformance.md#stable-diagnostic-families`](../60-specification/specifications-and-governance/diagnostics-and-conformance.md#stable-diagnostic-families) | c006 #6 | traced |
| SG-OBL-030 | The immutable conformance revision passes the required corpus | [`diagnostics-and-conformance.md#required-corpus`](../60-specification/specifications-and-governance/diagnostics-and-conformance.md#required-corpus) | c006 corpus | partial |
| SG-OBL-031 | A separately structured reference evaluator reproduces the production decision | [`diagnostics-and-conformance.md#independent-oracle`](../60-specification/specifications-and-governance/diagnostics-and-conformance.md#independent-oracle) | c006 #12 | traced |
| SG-OBL-032 | The reference evaluator must not call the production policy evaluator | [`diagnostics-and-conformance.md#independent-oracle`](../60-specification/specifications-and-governance/diagnostics-and-conformance.md#independent-oracle) | c006 #12 | traced |
| SG-OBL-033 | Corpus: subject resolution for every supported kind and rejection of future kinds | [`diagnostics-and-conformance.md#required-corpus`](../60-specification/specifications-and-governance/diagnostics-and-conformance.md#required-corpus) | c006 #7, #32 | traced |
| SG-OBL-034 | Corpus: typed, mistyped, effectful, and runtime-referenced rule checkers | [`diagnostics-and-conformance.md#required-corpus`](../60-specification/specifications-and-governance/diagnostics-and-conformance.md#required-corpus) | c006 #9 | traced |
| SG-OBL-035 | Corpus: counterexample, runtime-error, and budget-exhausted examples | [`diagnostics-and-conformance.md#required-corpus`](../60-specification/specifications-and-governance/diagnostics-and-conformance.md#required-corpus) | EVD002, EVD003; c006 #11 | traced |
| SG-OBL-036 | Corpus: formatting-invariant and meaning-sensitive semantic digest | [`diagnostics-and-conformance.md#required-corpus`](../60-specification/specifications-and-governance/diagnostics-and-conformance.md#required-corpus) | c006 #8 | traced |
| SG-OBL-037 | Corpus: additive policies and explicit deny | [`diagnostics-and-conformance.md#required-corpus`](../60-specification/specifications-and-governance/diagnostics-and-conformance.md#required-corpus) | c006 #13, #15 | traced |
| SG-OBL-038 | Corpus: duplicate-actor, threshold, assumption-authorization, and policy-budget cases | [`diagnostics-and-conformance.md#required-corpus`](../60-specification/specifications-and-governance/diagnostics-and-conformance.md#required-corpus) | c006 #14, #16, #17, #20 | traced |
| SG-OBL-039 | Corpus: valid/invalid Ed25519, domain substitution, duplicate names, unsafe integers, noncanonical payloads | [`diagnostics-and-conformance.md#required-corpus`](../60-specification/specifications-and-governance/diagnostics-and-conformance.md#required-corpus) | c006 #1, #2, #17 | traced |
| SG-OBL-040 | Corpus: evidence/artifact substitution, revocation, replay, and logical-window attacks | [`diagnostics-and-conformance.md#required-corpus`](../60-specification/specifications-and-governance/diagnostics-and-conformance.md#required-corpus) | c006 #19, #21, #33 | traced |
| SG-OBL-041 | Corpus: every valid lifecycle edge and every invalid/backward/terminal/skipped/reordered/broken edge | [`diagnostics-and-conformance.md#required-corpus`](../60-specification/specifications-and-governance/diagnostics-and-conformance.md#required-corpus) | c006 #22, #24 | traced |
| SG-OBL-042 | Corpus: normal dual-threshold root rotation and predeclared recovery | [`diagnostics-and-conformance.md#required-corpus`](../60-specification/specifications-and-governance/diagnostics-and-conformance.md#required-corpus) | c006 #16, #18 | traced |
| SG-OBL-043 | Corpus: output traversal, symlink escape, collision, and failed-gate no-output | [`diagnostics-and-conformance.md#required-corpus`](../60-specification/specifications-and-governance/diagnostics-and-conformance.md#required-corpus) | ART001; c006 #31, #34 | traced |
| SG-OBL-044 | Corpus: byte-identical BEAM with and without fully discharged specifications | [`diagnostics-and-conformance.md#required-corpus`](../60-specification/specifications-and-governance/diagnostics-and-conformance.md#required-corpus) | c006 #4, #26 | traced |

Provisional coverage: 36 `traced`, 7 `partial`, 1 `untraced` (SG-OBL-005 no ignore/force switch). SG has the densest test corpus of the traced areas.

## Registry — type-system (`TS`, 0.1.1)

Evidence labels refer to tests in
[`type_conformance_test.exs`](https://github.com/pcharbon70/catena/blob/rewrite/test/catena/type_conformance_test.exs)
(`tc#N`) and
[`compiler_test.exs`](https://github.com/pcharbon70/catena/blob/rewrite/test/catena/compiler_test.exs)
(`co#N`). TS is the foundational area: many of its obligations are also
exercised transitively by the data (`c002`), trait (`c004`), effect (`c005`),
kernel (`c010`), and resumption-token suites; those are noted where relevant.
The mapping is provisional; the compiler-side tagging PR establishes the
authoritative links and gap set.

| ID | Obligation | Normative anchor | Evidence | Status |
| --- | --- | --- | --- | --- |
| TS-OBL-001 | The compiler identifies an advanced-profile annotation and must not silently weaken the principal-core guarantee | [`type-system-overview.md#two-guarantee-profiles`](../60-specification/type-system/type-system-overview.md#two-guarantee-profiles) | T010; co#6 | partial |
| TS-OBL-002 | Both profiles satisfy the shared static contract | [`type-system-overview.md#shared-static-contract`](../60-specification/type-system/type-system-overview.md#shared-static-contract) | c002–c010 | partial |
| TS-OBL-003 | All exported values have explicit signatures; private principal-core generalizes | [`type-system-overview.md#shared-static-contract`](../60-specification/type-system/type-system-overview.md#shared-static-contract) | T008; co#2 | traced |
| TS-OBL-004 | Higher-rank quantification is explicit; the implementation prints kinds | [`type-language-and-kinds.md#type-grammar`](../60-specification/type-system/type-language-and-kinds.md#type-grammar) | co#6 | traced |
| TS-OBL-005 | Unification performs an occurs check and a kind check | [`type-language-and-kinds.md#rows-and-kinds`](../60-specification/type-system/type-language-and-kinds.md#rows-and-kinds) | T003, T004; co#5 | traced |
| TS-OBL-006 | Every exported value declares a signature | [`type-language-and-kinds.md#signatures-and-exports`](../60-specification/type-system/type-language-and-kinds.md#signatures-and-exports) | T008; co#2 | traced |
| TS-OBL-007 | Type aliases are expanded for equality and preserved where possible | [`type-language-and-kinds.md#signatures-and-exports`](../60-specification/type-system/type-language-and-kinds.md#signatures-and-exports) | — | untraced |
| TS-OBL-008 | Inference follows Algorithm W with kinded, occurs-checked unification | [`principal-inference-and-generalization.md#declarative-judgment`](../60-specification/type-system/principal-inference-and-generalization.md#declarative-judgment) | tc#1, co#1 | traced |
| TS-OBL-009 | Principal-core inference returns a scheme at least as general as every alternative | [`principal-inference-and-generalization.md#declarative-judgment`](../60-specification/type-system/principal-inference-and-generalization.md#declarative-judgment) | tc#1 | traced |
| TS-OBL-010 | Generalization rejects ambiguity | [`principal-inference-and-generalization.md#generalization`](../60-specification/type-system/principal-inference-and-generalization.md#generalization) | T006 | partial |
| TS-OBL-011 | A skolem must not escape its signature scope | [`principal-inference-and-generalization.md#recursive-bindings-and-signatures`](../60-specification/type-system/principal-inference-and-generalization.md#recursive-bindings-and-signatures) | T009; co#4 | traced |
| TS-OBL-012 | Solver work-list order yields alpha-equivalent schemes and equivalent typed core | [`principal-inference-and-generalization.md#determinism-and-failure`](../60-specification/type-system/principal-inference-and-generalization.md#determinism-and-failure) | c004 | partial |
| TS-OBL-013 | Infinite types, kind mismatches, and unresolved constraints are rejected | [`principal-inference-and-generalization.md#determinism-and-failure`](../60-specification/type-system/principal-inference-and-generalization.md#determinism-and-failure) | T003, T004, T007; co#5 | traced |
| TS-OBL-014 | Lacks constraints survive generalization | [`rows-traits-and-effects.md#unique-value-rows`](../60-specification/type-system/rows-traits-and-effects.md#unique-value-rows) | T005; tc#2 | traced |
| TS-OBL-015 | Capability resolution is lexical; the runtime must not search for a handler | [`rows-traits-and-effects.md#duplicate-effect-rows-and-capabilities`](../60-specification/type-system/rows-traits-and-effects.md#duplicate-effect-rows-and-capabilities) | tc#3; c005 | traced |
| TS-OBL-016 | Duplicate effect rows preserve multiplicity and identity | [`rows-traits-and-effects.md#duplicate-effect-rows-and-capabilities`](../60-specification/type-system/rows-traits-and-effects.md#duplicate-effect-rows-and-capabilities) | tc#3 | traced |
| TS-OBL-017 | An instance head is headed by an owned nominal type constructor | [`rows-traits-and-effects.md#traits`](../60-specification/type-system/rows-traits-and-effects.md#traits) | T007; tc#4 | traced |
| TS-OBL-018 | Visible instances must not unify (no overlap) | [`rows-traits-and-effects.md#traits`](../60-specification/type-system/rows-traits-and-effects.md#traits) | T007; tc#4 | traced |
| TS-OBL-019 | Resolution is stable under import order | [`rows-traits-and-effects.md#traits`](../60-specification/type-system/rows-traits-and-effects.md#traits) | tc#4 | partial |
| TS-OBL-020 | Functional-dependency coverage: output positions occur in inputs | [`rows-traits-and-effects.md#traits`](../60-specification/type-system/rows-traits-and-effects.md#traits) | tc#4 | partial |
| TS-OBL-021 | Functional-dependency determinism: equal inputs agree on outputs | [`rows-traits-and-effects.md#traits`](../60-specification/type-system/rows-traits-and-effects.md#traits) | — | partial |
| TS-OBL-022 | Associated types normalize only after instance selection | [`rows-traits-and-effects.md#traits`](../60-specification/type-system/rows-traits-and-effects.md#traits) | tc#4 | partial |
| TS-OBL-023 | Each solver step progresses, rechecks, or reports a diagnostic | [`rows-traits-and-effects.md#solver-interface`](../60-specification/type-system/rows-traits-and-effects.md#solver-interface) | c004 | partial |
| TS-OBL-024 | Solver scheduling must not affect accepted programs | [`rows-traits-and-effects.md#solver-interface`](../60-specification/type-system/rows-traits-and-effects.md#solver-interface) | c004 | partial |
| TS-OBL-025 | A GADT-matching function has an enclosing signature | [`advanced-type-checking.md#gadt-patterns`](../60-specification/type-system/advanced-type-checking.md#gadt-patterns) | c002 | partial |
| TS-OBL-026 | GADT equalities must not refine sibling branches or the environment | [`advanced-type-checking.md#gadt-patterns`](../60-specification/type-system/advanced-type-checking.md#gadt-patterns) | tc#5 | traced |
| TS-OBL-027 | Existential constructor variables are explicit and must not escape the branch | [`advanced-type-checking.md#gadt-patterns`](../60-specification/type-system/advanced-type-checking.md#gadt-patterns) | T009; tc#5 | traced |
| TS-OBL-028 | Rigid existentials must not be generalized without a local signature | [`advanced-type-checking.md#gadt-patterns`](../60-specification/type-system/advanced-type-checking.md#gadt-patterns) | tc#5 | traced |
| TS-OBL-029 | The affine resumption runtime token rejects double consumption | [`advanced-type-checking.md#affine-resumptions`](../60-specification/type-system/advanced-type-checking.md#affine-resumptions) | T011; resumption_token, c005 | traced |
| TS-OBL-030 | Advanced-profile inference identifies the profile boundary | [`advanced-type-checking.md#explicit-exclusions`](../60-specification/type-system/advanced-type-checking.md#explicit-exclusions) | T010; co#6 | traced |
| TS-OBL-031 | Every accepted term elaborates to a typed core | [`typed-core-elaboration.md#explicit-core`](../60-specification/type-system/typed-core-elaboration.md#explicit-core) | co#8; c002 | traced |
| TS-OBL-032 | Source spans remain attached through elaboration | [`typed-core-elaboration.md#explicit-core`](../60-specification/type-system/typed-core-elaboration.md#explicit-core) | c010 | partial |
| TS-OBL-033 | An inference-independent verifier checks the elaborated core | [`typed-core-elaboration.md#core-verifier`](../60-specification/type-system/typed-core-elaboration.md#core-verifier) | c002, c010 | traced |
| TS-OBL-034 | The verifier rechecks types, effects, evidence, coercion, and affine use; lowering accepts only verified core | [`typed-core-elaboration.md#core-verifier`](../60-specification/type-system/typed-core-elaboration.md#core-verifier) | c002, c010 | traced |
| TS-OBL-035 | A verifier failure after successful surface checking is an implementation defect, not a user error | [`typed-core-elaboration.md#core-verifier`](../60-specification/type-system/typed-core-elaboration.md#core-verifier) | — | partial |
| TS-OBL-036 | The backend uses OTP Erlang source or Abstract Format; it must not emit BEAM assembly or construct `.beam` directly | [`typed-core-elaboration.md#beam-only-backend-boundary`](../60-specification/type-system/typed-core-elaboration.md#beam-only-backend-boundary) | co#7 | traced |
| TS-OBL-037 | Every rejection has a stable family identifier, primary span, and explanation | [`diagnostics-and-conformance.md#diagnostic-contract`](../60-specification/type-system/diagnostics-and-conformance.md#diagnostic-contract) | T001–T012; co#3, co#6 | traced |
| TS-OBL-038 | A later edition may subdivide a family but must document the compatibility mapping | [`diagnostics-and-conformance.md#diagnostic-contract`](../60-specification/type-system/diagnostics-and-conformance.md#diagnostic-contract) | — | untraced |
| TS-OBL-039 | Alpha-renaming and declaration-order variants normalize to the same result | [`diagnostics-and-conformance.md#executable-input-boundary`](../60-specification/type-system/diagnostics-and-conformance.md#executable-input-boundary) | tc#1 | partial |
| TS-OBL-040 | Corpus: positive and negative tests for every diagnostic family | [`diagnostics-and-conformance.md#conformance-gate`](../60-specification/type-system/diagnostics-and-conformance.md#conformance-gate) | co#3, co#5, co#6 | partial |
| TS-OBL-041 | Corpus: principal-core examples versus a separately structured declarative checker | [`diagnostics-and-conformance.md#conformance-gate`](../60-specification/type-system/diagnostics-and-conformance.md#conformance-gate) | tc#1 | traced |
| TS-OBL-042 | Corpus: solver-order and alpha-renaming stability | [`diagnostics-and-conformance.md#conformance-gate`](../60-specification/type-system/diagnostics-and-conformance.md#conformance-gate) | tc#1 | partial |
| TS-OBL-043 | Corpus: typed-core verification and OTP 29 compile, load, and execute | [`diagnostics-and-conformance.md#conformance-gate`](../60-specification/type-system/diagnostics-and-conformance.md#conformance-gate) | co#7 | traced |
| TS-OBL-044 | Corpus: runtime affine double-consumption and no direct BEAM output path | [`diagnostics-and-conformance.md#conformance-gate`](../60-specification/type-system/diagnostics-and-conformance.md#conformance-gate) | resumption_token, co#7 | traced |

Provisional coverage: 26 `traced`, 16 `partial`, 2 `untraced` (TS-OBL-007 type aliases; TS-OBL-038 family-subdivision mapping). TS is foundational: many `partial` obligations are exercised transitively by the data, trait, effect, and kernel suites, which the compiler-side gate scans as well.

## Registry — data-and-patterns (`DP`, 0.1.2)

Evidence labels refer to tests in
[`c002_data_test.exs`](https://github.com/pcharbon70/catena/blob/rewrite/test/catena/c002_data_test.exs).
DP is the largest area (nine normative chapters). The mapping is provisional;
the compiler-side tagging PR establishes the authoritative test-to-obligation
links and the gap set.

- **c002 #1** *the durable C002 conformance fixture stays executable under reference, uniform, and compact lowering and hides layout from the interface*
- **c002 #2** *AST 0.1.1 normalizes into the 0.1.2 compiler representation with frontend provenance*
- **c002 #3** *duplicate declarations and unsupported pattern forms keep stable diagnostics A002 and M005*
- **c002 #4** *exhaustive nominal matches infer, verify, evaluate, and compile deterministically in both layouts with a sorted interface*
- **c002 #5** *non-exhaustive matches are rejected with a concrete machine-readable witness*
- **c002 #6** *redundant clauses are rejected with M002*
- **c002 #7** *empty and negative recursive declarations are accepted with computed inhabitation, positivity, and variance*
- **c002 #8** *an empty match is accepted only over a proven-empty type*
- **c002 #9** *named-field evaluation runs left to right in written order while payloads stay in declaration order*
- **c002 #10** *an explicit constructor-complete fold is generated, verified, and dispatched once*
- **c002 #11** *interfaces preserve nominal identity and hide abstract constructors (A004)*
- **c002 #12** *explicit constructor imports are the sole unqualified imported access*
- **c002 #13** *a tampered interface digest is rejected with A005*
- **c002 #14** *an origin change is a nominal identity change and mismatches are rejected with A005*
- **c002 #15** *annotated GADT matches use local equalities under the annotation-directed profile*
- **c002 #16** *existential values escaping a match branch are rejected with T009*
- **c002 #17** *ordered guard fallthrough is preserved and a false guard is redundant (M002)*
- **c002 #18** *exhaustive or patterns expand without changing branch bindings*
- **c002 #19** *deterministic coverage budget exhaustion is reported as M004*
- **c002 #20** *mutually recursive groups elaborate atomically with computed inhabitation*
- **c002 #21** *the typed-core verifier independently rejects corrupted constructor and decision evidence*
- **c002 #22** *a bounded Boolean pattern corpus agrees with the finite coverage model*
- **c002 #23** *positional and named constructor styles must not interchange (A003)*
- **c002 #24** *a variable name occurs at most once in a single pattern (M003)*
- **c002 #25** *a call expression in a pattern position is rejected as impure (M005)*
- **c002 #26** *a constructor pattern with the wrong arity is rejected (M003)*
- **c002 #27** *an existential variable appearing in the datatype result is rejected (T009)*
- **c002 #28** *a GADT pattern match without an enclosing signature is rejected (T010)*
- **c002 #29** *coverage uses GADT equalities to exclude impossible constructors but not to excuse a missing case (M001 over a generic index)*

### Declarations and nominal identity

| ID | Obligation | Normative anchor | Evidence | Status |
| --- | --- | --- | --- | --- |
| DP-OBL-001 | Parameters and explicit existential binders carry kinds in the resolved syntax | [`declarations-and-nominal-identity.md#surface-form`](../60-specification/data-and-patterns/declarations-and-nominal-identity.md#surface-form) | c002 #7 | partial |
| DP-OBL-002 | Each declaration generates a fresh nominal type identity | [`declarations-and-nominal-identity.md#nominal-generation`](../60-specification/data-and-patterns/declarations-and-nominal-identity.md#nominal-generation) | c002 #14 | traced |
| DP-OBL-003 | An alias is a different declaration form and must not silently generate a new identity | [`declarations-and-nominal-identity.md#nominal-generation`](../60-specification/data-and-patterns/declarations-and-nominal-identity.md#nominal-generation) | — | untraced |
| DP-OBL-004 | A mutually recursive group elaborates atomically; a failed group publishes nothing | [`declarations-and-nominal-identity.md#recursive-groups`](../60-specification/data-and-patterns/declarations-and-nominal-identity.md#recursive-groups) | c002 #20 | traced |
| DP-OBL-005 | Duplicate type, constructor, field, binder, or alias names are invalid (A002) | [`declarations-and-nominal-identity.md#recursive-groups`](../60-specification/data-and-patterns/declarations-and-nominal-identity.md#recursive-groups) | A002; c002 #3 | traced |
| DP-OBL-006 | Positivity and regularity are calculated before any operation depending on either | [`declarations-and-nominal-identity.md#recursive-groups`](../60-specification/data-and-patterns/declarations-and-nominal-identity.md#recursive-groups) | c002 #7 | partial |
| DP-OBL-007 | Every ordinary constructor returns the declared type applied to its parameters in declaration order | [`declarations-and-nominal-identity.md#constructor-schemes`](../60-specification/data-and-patterns/declarations-and-nominal-identity.md#constructor-schemes) | c002 #4, #9 | traced |
| DP-OBL-008 | Ordinary constructor schemes preserve the C001 principal-core guarantee | [`declarations-and-nominal-identity.md#constructor-schemes`](../60-specification/data-and-patterns/declarations-and-nominal-identity.md#constructor-schemes) | c002 #4 | partial |
| DP-OBL-009 | An explicit `returns` result is the declared nominal type at the correct arity | [`declarations-and-nominal-identity.md#constructor-schemes`](../60-specification/data-and-patterns/declarations-and-nominal-identity.md#constructor-schemes) | c002 #15 | traced |
| DP-OBL-010 | A public datatype interface is exactly transparent or abstract | [`declarations-and-nominal-identity.md#visibility-and-names`](../60-specification/data-and-patterns/declarations-and-nominal-identity.md#visibility-and-names) | c002 #11 | traced |
| DP-OBL-011 | A client may construct or match only constructors in a transparent imported interface | [`declarations-and-nominal-identity.md#visibility-and-names`](../60-specification/data-and-patterns/declarations-and-nominal-identity.md#visibility-and-names) | A004; c002 #11, #12 | traced |
| DP-OBL-012 | Imported constructors stay qualified unless an explicit import supplies a name or alias; ambiguous or duplicate aliases are invalid | [`declarations-and-nominal-identity.md#visibility-and-names`](../60-specification/data-and-patterns/declarations-and-nominal-identity.md#visibility-and-names) | c002 #12 | traced |
| DP-OBL-013 | Unit, empty, phantom, nested, mutually recursive, positive, and negative ordinary declarations are accepted | [`diagnostics-and-conformance.md#required-positive-cases`](../60-specification/data-and-patterns/diagnostics-and-conformance.md#required-positive-cases) | c002 #7, #20 | traced |
| DP-OBL-014 | Unknown kinds, unsaturated named types, invalid constructor results, and existential result escape are rejected | [`diagnostics-and-conformance.md#required-negative-cases`](../60-specification/data-and-patterns/diagnostics-and-conformance.md#required-negative-cases) | c002 #3 | partial |

### Construction and pattern typing

| ID | Obligation | Normative anchor | Evidence | Status |
| --- | --- | --- | --- | --- |
| DP-OBL-015 | Positional construction supplies exactly the constructor arity | [`construction-and-pattern-typing.md#construction`](../60-specification/data-and-patterns/construction-and-pattern-typing.md#construction) | c002 #4, #9 | traced |
| DP-OBL-016 | Named construction supplies every field once, in any order; fields evaluate left to right in written order; payload is stored in declaration order | [`construction-and-pattern-typing.md#construction`](../60-specification/data-and-patterns/construction-and-pattern-typing.md#construction) | c002 #9 | traced |
| DP-OBL-017 | Positional and named constructor styles must not be interchanged implicitly | [`construction-and-pattern-typing.md#construction`](../60-specification/data-and-patterns/construction-and-pattern-typing.md#construction) | A003; c002 #23 | traced |
| DP-OBL-018 | The 0.1.2 pattern grammar supports exactly the enumerated forms | [`construction-and-pattern-typing.md#complete-012-pattern-grammar`](../60-specification/data-and-patterns/construction-and-pattern-typing.md#complete-012-pattern-grammar) | c002 #4, #18 | partial |
| DP-OBL-019 | Unsupported pattern forms (list, record, row-variant, map, binary, string, range, view, active, synonym) produce M005 | [`construction-and-pattern-typing.md#complete-012-pattern-grammar`](../60-specification/data-and-patterns/construction-and-pattern-typing.md#complete-012-pattern-grammar) | M005; c002 #3 | traced |
| DP-OBL-020 | Wildcard, binder, and `as` binding rules; `as` checks its inner pattern then binds the complete value | [`construction-and-pattern-typing.md#binding-rules`](../60-specification/data-and-patterns/construction-and-pattern-typing.md#binding-rules) | c002 #4, #18 | partial |
| DP-OBL-021 | A variable name occurs at most once in a single pattern; equality is written as a guard | [`construction-and-pattern-typing.md#binding-rules`](../60-specification/data-and-patterns/construction-and-pattern-typing.md#binding-rules) | M003; c002 #24 | traced |
| DP-OBL-022 | Every `or` alternative binds the same names at the same types and establishes the same GADT refinements | [`construction-and-pattern-typing.md#binding-rules`](../60-specification/data-and-patterns/construction-and-pattern-typing.md#binding-rules) | c002 #18 | partial |
| DP-OBL-023 | Pattern typing is a checking judgment against an already inferred scrutinee type | [`construction-and-pattern-typing.md#structural-pattern-typing`](../60-specification/data-and-patterns/construction-and-pattern-typing.md#structural-pattern-typing) | c002 #4 | partial |
| DP-OBL-024 | Patterns are pure: no calls, effects, conversions, or user-defined tests | [`construction-and-pattern-typing.md#structural-pattern-typing`](../60-specification/data-and-patterns/construction-and-pattern-typing.md#structural-pattern-typing) | M005; c002 #25 | traced |
| DP-OBL-025 | Invalid bindings, arity, field use, or alternative agreement use M003 | [`construction-and-pattern-typing.md#diagnostics-and-evidence`](../60-specification/data-and-patterns/construction-and-pattern-typing.md#diagnostics-and-evidence) | M003; c002 #26 | traced |
| DP-OBL-026 | Non-match contexts admit only irrefutable patterns or an explicit failure construct; no implicit runtime match exception | [`construction-and-pattern-typing.md#refutability-boundary`](../60-specification/data-and-patterns/construction-and-pattern-typing.md#refutability-boundary) | — | untraced |

### Match semantics and coverage

| ID | Obligation | Normative anchor | Evidence | Status |
| --- | --- | --- | --- | --- |
| DP-OBL-027 | Match evaluation tests top to bottom, structural-then-guard, selecting the first true-guard body after one scrutinee evaluation | [`match-semantics-and-coverage.md#dynamic-semantics`](../60-specification/data-and-patterns/match-semantics-and-coverage.md#dynamic-semantics) | c002 #4, #17 | traced |
| DP-OBL-028 | A false guard resumes with the next clause; clause bodies share one unifiable result type | [`match-semantics-and-coverage.md#dynamic-semantics`](../60-specification/data-and-patterns/match-semantics-and-coverage.md#dynamic-semantics) | c002 #17 | traced |
| DP-OBL-029 | No well-typed 0.1.2 program reaches an implicit match-failure exception | [`match-semantics-and-coverage.md#dynamic-semantics`](../60-specification/data-and-patterns/match-semantics-and-coverage.md#dynamic-semantics) | c002 #8 | partial |
| DP-OBL-030 | Exhaustiveness and redundancy are determined from one typed usefulness relation | [`match-semantics-and-coverage.md#usefulness-model`](../60-specification/data-and-patterns/match-semantics-and-coverage.md#usefulness-model) | c002 #5, #6, #22 | traced |
| DP-OBL-031 | Coverage analysis is independent of backend match lowering | [`match-semantics-and-coverage.md#usefulness-model`](../60-specification/data-and-patterns/match-semantics-and-coverage.md#usefulness-model) | c002 #4 | partial |
| DP-OBL-032 | A missing case is invalid (M001) with a deterministic concrete witness when the witness language can express one | [`match-semantics-and-coverage.md#usefulness-model`](../60-specification/data-and-patterns/match-semantics-and-coverage.md#usefulness-model) | M001; c002 #5 | traced |
| DP-OBL-033 | A useless clause is invalid (M002); `or` is semantic union and sharing must not change usefulness | [`match-semantics-and-coverage.md#usefulness-model`](../60-specification/data-and-patterns/match-semantics-and-coverage.md#usefulness-model) | M002; c002 #6, #17, #18 | traced |
| DP-OBL-034 | Coverage treats each type domain as specified (nominal finite, Boolean, tuple product, integer points, abstract open, GADT refined-result) | [`match-semantics-and-coverage.md#type-domains`](../60-specification/data-and-patterns/match-semantics-and-coverage.md#type-domains) | c002 #22 | partial |
| DP-OBL-035 | String, range, structural-variant, list-syntax, and binary coverage are outside 0.1.2, not silently approximated | [`match-semantics-and-coverage.md#type-domains`](../60-specification/data-and-patterns/match-semantics-and-coverage.md#type-domains) | M005; c002 #3 | traced |
| DP-OBL-036 | A terminating three-valued inhabitation fact is calculated; only a proven-empty scrutinee permits a zero-clause match | [`match-semantics-and-coverage.md#empty-and-recursive-types`](../60-specification/data-and-patterns/match-semantics-and-coverage.md#empty-and-recursive-types) | c002 #7, #8 | partial |
| DP-OBL-037 | Coverage consumes only proved-true, proved-false, or unknown guard classification | [`match-semantics-and-coverage.md#guards-and-coverage-facts`](../60-specification/data-and-patterns/match-semantics-and-coverage.md#guards-and-coverage-facts) | c002 #17 | partial |
| DP-OBL-038 | Coverage terminates with at least 20,000 usefulness steps; exhaustion reports M004 and must not mislabel as M001 or M002 | [`match-semantics-and-coverage.md#deterministic-implementation-limit`](../60-specification/data-and-patterns/match-semantics-and-coverage.md#deterministic-implementation-limit) | M004; c002 #19 | traced |
| DP-OBL-039 | Backend lowering preserves source order, guard fallthrough, and bindings | [`match-semantics-and-coverage.md#decision-representation`](../60-specification/data-and-patterns/match-semantics-and-coverage.md#decision-representation) | c002 #4, #17 | partial |
| DP-OBL-040 | The typed-core verifier rejects a decision representation not marked exhaustive or not corresponding to its checked clauses | [`match-semantics-and-coverage.md#decision-representation`](../60-specification/data-and-patterns/match-semantics-and-coverage.md#decision-representation) | c002 #21 | traced |

### GADT and existential patterns

| ID | Obligation | Normative anchor | Evidence | Status |
| --- | --- | --- | --- | --- |
| DP-OBL-041 | A refined `returns` result is the declared nominal type at full arity | [`gadt-and-existential-patterns.md#explicit-advanced-declarations`](../60-specification/data-and-patterns/gadt-and-existential-patterns.md#explicit-advanced-declarations) | c002 #15 | traced |
| DP-OBL-042 | An existential variable may appear in constructor fields but must not appear in the datatype result | [`gadt-and-existential-patterns.md#explicit-advanced-declarations`](../60-specification/data-and-patterns/gadt-and-existential-patterns.md#explicit-advanced-declarations) | T009; c002 #27 | traced |
| DP-OBL-043 | A definition matching a refined or existential constructor must have an enclosing signature; absence is invalid (T010) | [`gadt-and-existential-patterns.md#required-annotation-boundary`](../60-specification/data-and-patterns/gadt-and-existential-patterns.md#required-annotation-boundary) | T010; c002 #28 | traced |
| DP-OBL-044 | GADT pattern checking freshens parameters, instantiates existentials as rigid skolems, compares the result, and scopes equalities to the branch | [`gadt-and-existential-patterns.md#branch-local-checking`](../60-specification/data-and-patterns/gadt-and-existential-patterns.md#branch-local-checking) | c002 #15 | partial |
| DP-OBL-045 | The branch environment is not generalized under active equality; an impossible constructor is excluded from coverage | [`gadt-and-existential-patterns.md#branch-local-checking`](../60-specification/data-and-patterns/gadt-and-existential-patterns.md#branch-local-checking) | c002 #15 | partial |
| DP-OBL-046 | No rigid existential or branch-local equality escapes to a result, scheme, closure, or interface; escape is invalid (T009) | [`gadt-and-existential-patterns.md#escape-prevention`](../60-specification/data-and-patterns/gadt-and-existential-patterns.md#escape-prevention) | T009; c002 #16 | traced |
| DP-OBL-047 | The verifier independently checks field arity, nominal result identity, branch binding types, equality scope, and non-escape | [`gadt-and-existential-patterns.md#typed-core-evidence`](../60-specification/data-and-patterns/gadt-and-existential-patterns.md#typed-core-evidence) | c002 #21 | partial |
| DP-OBL-048 | Coverage may use local equalities to reject impossible constructors but must not justify an unsound branch type | [`gadt-and-existential-patterns.md#typed-core-evidence`](../60-specification/data-and-patterns/gadt-and-existential-patterns.md#typed-core-evidence) | M001; c002 #29 | traced |

### Interfaces and representation

| ID | Obligation | Normative anchor | Evidence | Status |
| --- | --- | --- | --- | --- |
| DP-OBL-049 | Successful compilation produces a deterministic `.cati.json` interface beside the `.beam`; check-only consumes but does not write artifacts | [`interfaces-and-representation.md#deterministic-module-interface`](../60-specification/data-and-patterns/interfaces-and-representation.md#deterministic-module-interface) | c002 #4 | partial |
| DP-OBL-050 | Consumers verify the digest before trusting an interface and reject tampering (A005) | [`interfaces-and-representation.md#deterministic-module-interface`](../60-specification/data-and-patterns/interfaces-and-representation.md#deterministic-module-interface) | A005; c002 #13, #14 | traced |
| DP-OBL-051 | An interface must not expose the chosen runtime layout (no tag, tuple shape, boxing, niche, or coercion) | [`interfaces-and-representation.md#deterministic-module-interface`](../60-specification/data-and-patterns/interfaces-and-representation.md#deterministic-module-interface) | c002 #1, #4 | traced |
| DP-OBL-052 | A transparent import supplies the constructor family; an abstract import supplies only nominal kinded identity | [`interfaces-and-representation.md#separate-compilation`](../60-specification/data-and-patterns/interfaces-and-representation.md#separate-compilation) | A004; c002 #11 | traced |
| DP-OBL-053 | An origin, module, or type disagreement is nominal incompatibility regardless of shape; layout equality never repairs identity | [`interfaces-and-representation.md#separate-compilation`](../60-specification/data-and-patterns/interfaces-and-representation.md#separate-compilation) | A005; c002 #14 | traced |
| DP-OBL-054 | Constructor semantic value is identity plus payload in declaration order; pattern selection compares semantic identity | [`interfaces-and-representation.md#source-semantic-value`](../60-specification/data-and-patterns/interfaces-and-representation.md#source-semantic-value) | c002 #1, #9 | traced |
| DP-OBL-055 | Uniform and compact layouts are both supported; every conformance program checks and executes under both and typed observation agrees | [`interfaces-and-representation.md#required-beam-layouts`](../60-specification/data-and-patterns/interfaces-and-representation.md#required-beam-layouts) | c002 #1, #4 | traced |
| DP-OBL-056 | Layout selection occurs after typed-core verification; the backend must not reconstruct nominal meaning from spelling or tuple arity | [`interfaces-and-representation.md#typed-layout-boundary`](../60-specification/data-and-patterns/interfaces-and-representation.md#typed-layout-boundary) | — | untraced |
| DP-OBL-057 | The verifier rejects inconsistent arity, type identity, ordinal, payload, dispatch, or layout coercion as L001 implementation failure | [`interfaces-and-representation.md#typed-layout-boundary`](../60-specification/data-and-patterns/interfaces-and-representation.md#typed-layout-boundary) | — | untraced |
| DP-OBL-058 | Only OTP 29 `compile:noenv_forms/2` may generate `.beam` content; Core Erlang, assembly, and binary construction are not alternate paths | [`interfaces-and-representation.md#typed-layout-boundary`](../60-specification/data-and-patterns/interfaces-and-representation.md#typed-layout-boundary) | — | untraced |
| DP-OBL-059 | An untrusted Erlang term must not become a typed Catena ADT by shape alone; the later G095 boundary defines validation | [`interfaces-and-representation.md#dynamic-and-evolution-boundary`](../60-specification/data-and-patterns/interfaces-and-representation.md#dynamic-and-evolution-boundary) | — | untraced |

### Derived folds

| ID | Obligation | Normative anchor | Evidence | Status |
| --- | --- | --- | --- | --- |
| DP-OBL-060 | Only `derives fold` is supported; unknown derivations are invalid (A001) and GADT or existential constructors are ineligible (A003) | [`derived-folds.md#explicit-request`](../60-specification/data-and-patterns/derived-folds.md#explicit-request) | c002 #10 | partial |
| DP-OBL-061 | The generated fold takes one handler per constructor in declaration order, then the value; a nullary handler is a result and a payload handler is curried in field order | [`derived-folds.md#signature`](../60-specification/data-and-patterns/derived-folds.md#signature) | c002 #10 | traced |
| DP-OBL-062 | The selected handler is invoked exactly once; unselected handlers are not invoked; payload values pass without recursive traversal | [`derived-folds.md#signature`](../60-specification/data-and-patterns/derived-folds.md#signature) | c002 #10 | traced |
| DP-OBL-063 | The generated operation is constructor-complete case elimination only; it is not a recursive catamorphism, traversal, or categorical instance | [`derived-folds.md#meaning-and-limits`](../60-specification/data-and-patterns/derived-folds.md#meaning-and-limits) | c002 #10 | partial |
| DP-OBL-064 | Generated code carries `compiler-derived` provenance, lives in typed core, is rejected on inconsistency, and is public only when constructors are transparent | [`derived-folds.md#generated-evidence`](../60-specification/data-and-patterns/derived-folds.md#generated-evidence) | c002 #10, #11 | partial |

### Diagnostics, differential, and deterministic evidence

| ID | Obligation | Normative anchor | Evidence | Status |
| --- | --- | --- | --- | --- |
| DP-OBL-065 | Diagnostics include the JSON path or eventual source span when one is available | [`diagnostics-and-conformance.md#stable-diagnostics`](../60-specification/data-and-patterns/diagnostics-and-conformance.md#stable-diagnostics) | — | untraced |
| DP-OBL-066 | M001 carries a machine-readable witness; M004 states the minimum budget and must not masquerade as M001 or M002 | [`diagnostics-and-conformance.md#stable-diagnostics`](../60-specification/data-and-patterns/diagnostics-and-conformance.md#stable-diagnostics) | M001, M004; c002 #5, #19 | traced |
| DP-OBL-067 | A conformance fixture runs through the reference evaluator, uniform-layout BEAM, and compact-layout BEAM, compared by typed observation | [`diagnostics-and-conformance.md#differential-and-deterministic-evidence`](../60-specification/data-and-patterns/diagnostics-and-conformance.md#differential-and-deterministic-evidence) | c002 #1, #4 | traced |
| DP-OBL-068 | Generated BEAM and `.cati.json` output is byte-for-byte deterministic for identical inputs and options | [`diagnostics-and-conformance.md#differential-and-deterministic-evidence`](../60-specification/data-and-patterns/diagnostics-and-conformance.md#differential-and-deterministic-evidence) | c002 #4 | traced |
| DP-OBL-069 | The suite includes a deterministic bounded pattern corpus independent of the inference and coverage implementation | [`diagnostics-and-conformance.md#differential-and-deterministic-evidence`](../60-specification/data-and-patterns/diagnostics-and-conformance.md#differential-and-deterministic-evidence) | c002 #22 | traced |

### Compiler boundary and independent verification

| ID | Obligation | Normative anchor | Evidence | Status |
| --- | --- | --- | --- | --- |
| DP-OBL-070 | Input JSON AST 0.1.1 is normalized into the 0.1.2 internal form and carries no datatype declarations | [`data-and-pattern-overview.md#compiler-boundary`](../60-specification/data-and-patterns/data-and-pattern-overview.md#compiler-boundary) | c002 #2 | traced |
| DP-OBL-071 | The verifier independently rejects malformed constructor, binding, equality, coverage, derivation, or layout evidence | [`data-and-pattern-overview.md#compiler-boundary`](../60-specification/data-and-patterns/data-and-pattern-overview.md#compiler-boundary) | c002 #21 | traced |

Provisional coverage: 43 `traced`, 21 `partial`, 7 `untraced`. Every substantive
data-and-patterns obligation now has a focused test. The seven remaining
untraced obligations are all architectural, future-version, or diagnostic-quality
boundaries with no focused c002 unit (DP-OBL-003 future alias declaration form;
DP-OBL-026 future refutability context P044; DP-OBL-056 backend reconstruction
prevention; DP-OBL-057 L001 implementation-failure path; DP-OBL-058
sole-OTP-boundary architectural; DP-OBL-059 future G095 validation boundary;
DP-OBL-065 P117 diagnostic quality).

## Governance registry — implementation limits (`IL`, C012)

Evidence labels refer to tests in the immutable compiler
[`c012_implementation_limits_test.exs`](https://github.com/pcharbon70/catena/blob/841af5ee342a31ff4769749bbdaa18a675b1bb21/test/catena/c012_implementation_limits_test.exs)
and its
[`c012_traceability_coverage_test.exs`](https://github.com/pcharbon70/catena/blob/841af5ee342a31ff4769749bbdaa18a675b1bb21/test/catena/c012_traceability_coverage_test.exs)
gate:

- **c012 #1** *conformance-info is deterministic and backed by the executable registry*
- **c012 #2** *the 253-argument portable floor reaches an effectful OTP worker of arity 255*
- **c012 #3** *both frontends accept 4096 integer digits and reject 4097 as LIM002*
- **c012 #4** *literal and generated-module bounds have explicit applicability and diagnostics*
- **c012 #5** *analysis refusals and inconclusive evidence bounds remain distinct*
- **c012 #6** *mailbox capacity is a deployment concern without a compiler message-count cap*

| ID | Obligation | Governance anchor | Evidence | Status |
| --- | --- | --- | --- | --- |
| IL-OBL-001 | Every claimed compiler release emits a deterministic machine-readable profile | [`IMPLEMENTATION-LIMITS.md#machine-readable-reporting`](../IMPLEMENTATION-LIMITS.md#machine-readable-reporting) | c012 #1 | traced |
| IL-OBL-002 | Every active finite bound and reserved dimension appears in one executable registry and profile | [`IMPLEMENTATION-LIMITS.md#machine-readable-reporting`](../IMPLEMENTATION-LIMITS.md#machine-readable-reporting) | c012 #1 | traced |
| IL-OBL-003 | Each profile entry declares classification, unit, floor, configuration, applicability, and exhaustion | [`IMPLEMENTATION-LIMITS.md#machine-readable-reporting`](../IMPLEMENTATION-LIMITS.md#machine-readable-reporting) | c012 #1 | traced |
| IL-OBL-004 | Source arity 253 is accepted, 254 reports LIM001, and the effect worker may reach OTP arity 255 | [`IMPLEMENTATION-LIMITS.md#bootstrap-portable-minima`](../IMPLEMENTATION-LIMITS.md#bootstrap-portable-minima) | LIM001; c012 #2 | traced |
| IL-OBL-005 | Applicable integer inputs accept values through 4,096 decimal digits and reject 4,097 as LIM002, including based C017 spellings | [`IMPLEMENTATION-LIMITS.md#bootstrap-portable-minima`](../IMPLEMENTATION-LIMITS.md#bootstrap-portable-minima) | LIM002; c012 #3; c017 #9 | traced |
| IL-OBL-006 | C017 text and byte literals accept 65,536 decoded bytes and reject the next byte as LIM004 | [`IMPLEMENTATION-LIMITS.md#bootstrap-portable-minima`](../IMPLEMENTATION-LIMITS.md#bootstrap-portable-minima) | LIM004; c012 #4; c017 #9 | traced |
| IL-OBL-007 | Generated BEAM through 1,048,576 bytes crosses no module-size limit and the next byte reports LIM003 | [`IMPLEMENTATION-LIMITS.md#bootstrap-portable-minima`](../IMPLEMENTATION-LIMITS.md#bootstrap-portable-minima) | LIM003; c012 #4 | traced |
| IL-OBL-008 | Compiler and governance refusal budgets retain their distinct diagnostics and outcomes | [`IMPLEMENTATION-LIMITS.md#analysis-refusals-and-evidence-bounds`](../IMPLEMENTATION-LIMITS.md#analysis-refusals-and-evidence-bounds) | c012 #5 | traced |
| IL-OBL-009 | Evidence exhaustion remains inconclusive and cannot become semantic rejection | [`IMPLEMENTATION-LIMITS.md#analysis-refusals-and-evidence-bounds`](../IMPLEMENTATION-LIMITS.md#analysis-refusals-and-evidence-bounds) | c012 #5 | traced |
| IL-OBL-010 | Mailbox capacity is deployment-defined with ordering, targeting, and live-target delivery constraints | [`IMPLEMENTATION-LIMITS.md#runtime-and-mailbox-capacity`](../IMPLEMENTATION-LIMITS.md#runtime-and-mailbox-capacity) | c012 #6 | traced |
| IL-OBL-011 | Limit refusals report common structured measurements before successful output publication | [`IMPLEMENTATION-LIMITS.md#limit-diagnostics-and-transactional-failure`](../IMPLEMENTATION-LIMITS.md#limit-diagnostics-and-transactional-failure) | LIM001–LIM004; c012 #2–#4; c017 #9 | traced |
| IL-OBL-012 | C012 changes governance and compiler conformance behavior without creating revision 0.1.9 | [`IMPLEMENTATION-LIMITS.md#evolution-and-version-axes`](../IMPLEMENTATION-LIMITS.md#evolution-and-version-axes) | Governance/version-axis obligation; compiler coverage gate allow-list | untraced |
| IL-OBL-013 | C018 decimal literals accept exact components through 4,096 total digits and refuse the next digit as LIM005 | [`IMPLEMENTATION-LIMITS.md#bootstrap-portable-minima`](../IMPLEMENTATION-LIMITS.md#bootstrap-portable-minima) | LIM005; c018 #9 in the `NM` registry above | traced |

C012 coverage is 12 `traced` and 1 governance-only `untraced` obligation.
`IL-OBL-013` is exercised by the C018 decimal-component boundary test and
gated with the `NM` set. The compiler coverage gate explicitly allow-lists
IL-OBL-012 because emitting a language revision is a repository and
release-governance decision, not an executable compiler behavior.

## Source-text registry (`ST`, 0.1.9)

Evidence labels refer to focused tests in immutable compiler commit
[`d4e8e5c0ad41f47ebe86d59047cdabe017762f38`](https://github.com/pcharbon70/catena/commit/d4e8e5c0ad41f47ebe86d59047cdabe017762f38):
[`c013_source_text_test.exs`](https://github.com/pcharbon70/catena/blob/d4e8e5c0ad41f47ebe86d59047cdabe017762f38/test/catena/c013_source_text_test.exs)
and its
[`c013_traceability_coverage_test.exs`](https://github.com/pcharbon70/catena/blob/d4e8e5c0ad41f47ebe86d59047cdabe017762f38/test/catena/c013_traceability_coverage_test.exs)
gate:

- **c013 #1** *preserves well-formed Unicode scalars without normalization*
- **c013 #2** *maps LF and CRLF to logical LF with original-byte scalar spans*
- **c013 #3** *accepts mixed endings and rejects only C013 lone CR newlines*
- **c013 #4** *rejects malformed UTF-8 without replacement or fallback*
- **c013 #5** *distinguishes leading BOMs from alternate encoding signatures*
- **c013 #6** *keeps 0.1.9 source-only and exposes deterministic discovery*
- **c013 #7** *handles empty input and deterministic command-line validation*

| ID | Obligation | Normative anchor | Evidence | Status |
| --- | --- | --- | --- | --- |
| ST-OBL-001 | Apply the source envelope only to 0.1.9 and preserve older format boundaries | [`diagnostics-and-conformance.md#revision-and-frontend-separation`](../60-specification/source-text/diagnostics-and-conformance.md#revision-and-frontend-separation) | c013 #6; EDN001 | traced |
| ST-OBL-002 | Accept well-formed UTF-8 scalar sequences and reject malformed or alternate encodings | [`source-text-envelope.md#utf-8-byte-domain`](../60-specification/source-text/source-text-envelope.md#utf-8-byte-domain) | c013 #1, #4, #5; SRC001 | traced |
| ST-OBL-003 | Never replace, skip, or reinterpret malformed bytes | [`source-text-envelope.md#utf-8-byte-domain`](../60-specification/source-text/source-text-envelope.md#utf-8-byte-domain) | c013 #1, #4; SRC001 | traced |
| ST-OBL-004 | Reject a leading UTF-8 BOM while preserving embedded U+FEFF | [`source-text-envelope.md#byte-order-marks-and-signatures`](../60-specification/source-text/source-text-envelope.md#byte-order-marks-and-signatures) | c013 #1, #5; SRC002 | traced |
| ST-OBL-005 | Map LF and CRLF, reject lone CR, and preserve other Unicode separators as scalars | [`source-text-envelope.md#logical-newlines`](../60-specification/source-text/source-text-envelope.md#logical-newlines) | c013 #2, #3; SRC003 | traced |
| ST-OBL-006 | Preserve the source scalar sequence without normalization or normalization checks | [`source-text-envelope.md#normalization-boundary`](../60-specification/source-text/source-text-envelope.md#normalization-boundary) | c013 #1, #3 | traced |
| ST-OBL-007 | Retain original bytes and one original half-open span per logical scalar | [`source-text-envelope.md#source-units-and-locations`](../60-specification/source-text/source-text-envelope.md#source-units-and-locations) | c013 #2, #7 | traced |
| ST-OBL-008 | Use zero-based bytes, one-based scalar coordinates, and a zero-width EOF span | [`source-text-envelope.md#source-units-and-locations`](../60-specification/source-text/source-text-envelope.md#source-units-and-locations) | c013 #2, #7 | traced |
| ST-OBL-009 | Emit stable SRC failures and no successful result for invalid input | [`diagnostics-and-conformance.md#stable-diagnostics`](../60-specification/source-text/diagnostics-and-conformance.md#stable-diagnostics) | c013 #4, #5; SRC001–SRC003 | traced |
| ST-OBL-010 | Keep decoder and validation command deterministic without creating artifacts | [`diagnostics-and-conformance.md#command-line-validation`](../60-specification/source-text/diagnostics-and-conformance.md#command-line-validation) | c013 #6, #7 | traced |

C013 coverage is 10 `traced` and 0 untraced obligations. The dedicated gate
rejects unknown identifiers and fails if any `ST-OBL-*` identifier lacks a
focused tag.

## Identifier registry (`ID`, 0.1.10)

Evidence labels refer to focused tests in
[`c014_identifiers_test.exs`](https://github.com/pcharbon70/catena/blob/rewrite/test/catena/c014_identifiers_test.exs)
and its
[`c014_traceability_coverage_test.exs`](https://github.com/pcharbon70/catena/blob/rewrite/test/catena/c014_traceability_coverage_test.exs)
gate:

- **c014 #1** *accepts Unicode 17 XID names with case-sensitive, role-neutral identity*
- **c014 #2** *rejects non-NFC spelling with an original-byte replacement fix*
- **c014 #3** *enforces General Security and Highly Restrictive profiles per segment*
- **c014 #4** *hard-reserves the complete keyword set and validates backtick escapes*
- **c014 #5** *validates nonempty dot qualification one segment at a time*
- **c014 #6** *emits deterministic, deny-able confusable warnings*
- **c014 #7** *keeps 0.1.10 source-only and exposes deterministic CLI discovery*
- **c014 #8** *runs the packaged executable with its embedded pinned Unicode table*
- **c014 #9** *checks Catena NFC against the complete Unicode 17 normalization corpus*

| ID | Obligation | Normative anchor | Evidence | Status |
| --- | --- | --- | --- | --- |
| ID-OBL-001 | Pin Unicode 17 data and revision | [`identifier-syntax-and-equivalence.md#unicode-data-and-profile`](../60-specification/identifiers/identifier-syntax-and-equivalence.md#unicode-data-and-profile) | c014 #1, #7, #8, #9 | traced |
| ID-OBL-002 | Apply the exact XID start and continuation production | [`identifier-syntax-and-equivalence.md#unicode-data-and-profile`](../60-specification/identifiers/identifier-syntax-and-equivalence.md#unicode-data-and-profile) | c014 #1; IDN001 | traced |
| ID-OBL-003 | Preserve case-sensitive, role-neutral identity | [`identifier-syntax-and-equivalence.md#case-and-canonical-identity`](../60-specification/identifiers/identifier-syntax-and-equivalence.md#case-and-canonical-identity) | c014 #1 | traced |
| ID-OBL-004 | Require filtered NFC without silent normalization | [`identifier-syntax-and-equivalence.md#nfc-spelling`](../60-specification/identifiers/identifier-syntax-and-equivalence.md#nfc-spelling) | c014 #2, #9; IDN002 | traced |
| ID-OBL-005 | Apply the General Security Profile | [`qualification-keywords-and-security.md#general-security-profile`](../60-specification/identifiers/qualification-keywords-and-security.md#general-security-profile) | c014 #3; IDN003 | traced |
| ID-OBL-006 | Apply Highly Restrictive script checks per segment | [`qualification-keywords-and-security.md#highly-restrictive-scripts`](../60-specification/identifiers/qualification-keywords-and-security.md#highly-restrictive-scripts) | c014 #3; IDN004 | traced |
| ID-OBL-007 | Reserve the complete closed keyword set | [`qualification-keywords-and-security.md#reserved-words-and-escaping`](../60-specification/identifiers/qualification-keywords-and-security.md#reserved-words-and-escaping) | c014 #4; IDN005 | traced |
| ID-OBL-008 | Preserve identity through valid backtick escapes | [`qualification-keywords-and-security.md#reserved-words-and-escaping`](../60-specification/identifiers/qualification-keywords-and-security.md#reserved-words-and-escaping) | c014 #4; IDN005 | traced |
| ID-OBL-009 | Validate nonempty dot qualification and every segment | [`qualification-keywords-and-security.md#qualified-names`](../60-specification/identifiers/qualification-keywords-and-security.md#qualified-names) | c014 #5; IDN001, IDN006 | traced |
| ID-OBL-010 | Emit deterministic confusable warnings and promote on denial | [`qualification-keywords-and-security.md#confusable-comparison`](../60-specification/identifiers/qualification-keywords-and-security.md#confusable-comparison) | c014 #6; IDN007 | traced |
| ID-OBL-011 | Preserve original-byte spans and exact fixes | [`diagnostics-and-conformance.md#stable-diagnostics`](../60-specification/identifiers/diagnostics-and-conformance.md#stable-diagnostics) | c014 #2; IDN002 | traced |
| ID-OBL-012 | Expose a deterministic non-artifact command | [`diagnostics-and-conformance.md#command-line-boundary`](../60-specification/identifiers/diagnostics-and-conformance.md#command-line-boundary) | c014 #7, #8 | traced |
| ID-OBL-013 | Keep 0.1.10 source-only and separated from persisted formats | [`identifier-syntax-and-equivalence.md#source-spans-and-selection`](../60-specification/identifiers/identifier-syntax-and-equivalence.md#source-spans-and-selection) | c014 #7; EDN001 | traced |

C014 coverage is 13 `traced` and 0 untraced obligations. The dedicated gate
rejects unknown identifiers and fails if any `ID-OBL-*` identifier lacks a
focused tag.

## Whitespace and layout registry (`LY`, 0.1.11)

Evidence labels refer to focused tests in
[`c015_whitespace_layout_test.exs`](https://github.com/pcharbon70/catena/blob/rewrite/test/catena/c015_whitespace_layout_test.exs)
and its
[`c015_traceability_coverage_test.exs`](https://github.com/pcharbon70/catena/blob/rewrite/test/catena/c015_traceability_coverage_test.exs)
gate:

- **c015 #1** *keeps 0.1.11 source-only and requires exact layout selection*
- **c015 #2** *accepts SPACE, TAB, and logical LF while rejecting other whitespace*
- **c015 #3** *proves indentation and tab width do not create structure*
- **c015 #4** *preserves hard LF, semicolon, blank lines, and optional final LF*
- **c015 #5** *continues forms from before/after token capabilities*
- **c015 #6** *distinguishes nested continued and block delimiter frames*
- **c015 #7** *reports unexpected, mismatched, and unclosed delimiters*
- **c015 #8** *rejects separator and EOF interruption of required continuation*
- **c015 #9** *shields opaque token content and resolves deterministically*

| ID | Obligation | Normative anchor | Evidence | Status |
| --- | --- | --- | --- | --- |
| LY-OBL-001 | Apply layout only to 0.1.11 and preserve source-only format boundaries | [`diagnostics-and-conformance.md#revision-and-persistence-separation`](../60-specification/whitespace-and-layout/diagnostics-and-conformance.md#revision-and-persistence-separation) | c015 #1; EDN001 | traced |
| LY-OBL-002 | Accept only SPACE, TAB, and logical LF as layout whitespace | [`whitespace-and-indentation.md#layout-whitespace`](../60-specification/whitespace-and-layout/whitespace-and-indentation.md#layout-whitespace) | c015 #2; LAY001 | traced |
| LY-OBL-003 | Make indentation and tab width semantically inert | [`whitespace-and-indentation.md#indentation-has-no-semantic-effect`](../60-specification/whitespace-and-layout/whitespace-and-indentation.md#indentation-has-no-semantic-effect) | c015 #3 | traced |
| LY-OBL-004 | Preserve hard LF and semicolon separators | [`separators-and-line-continuation.md#hard-separators`](../60-specification/whitespace-and-layout/separators-and-line-continuation.md#hard-separators) | c015 #4 | traced |
| LY-OBL-005 | Classify blank lines and complete or incomplete EOF exactly | [`separators-and-line-continuation.md#eof-and-incomplete-input`](../60-specification/whitespace-and-layout/separators-and-line-continuation.md#eof-and-incomplete-input) | c015 #4, #8; LAY003 | traced |
| LY-OBL-006 | Resolve before/after token continuation capabilities | [`separators-and-line-continuation.md#token-continuation-capabilities`](../60-specification/whitespace-and-layout/separators-and-line-continuation.md#token-continuation-capabilities) | c015 #5, #8; LAY003 | traced |
| LY-OBL-007 | Distinguish and validate continued and block delimiter frames | [`separators-and-line-continuation.md#delimiter-frames`](../60-specification/whitespace-and-layout/separators-and-line-continuation.md#delimiter-frames) | c015 #6, #7; LAY002 | traced |
| LY-OBL-008 | Emit stable layout diagnostic identities and reasons | [`diagnostics-and-conformance.md#stable-diagnostics`](../60-specification/whitespace-and-layout/diagnostics-and-conformance.md#stable-diagnostics) | c015 #2, #7, #8; LAY001–LAY003 | traced |
| LY-OBL-009 | Preserve original-byte spans including CRLF and multibyte scalars | [`whitespace-and-indentation.md#layout-whitespace`](../60-specification/whitespace-and-layout/whitespace-and-indentation.md#layout-whitespace) | c015 #2 | traced |
| LY-OBL-010 | Return a lossless deterministic classified event stream | [`separators-and-line-continuation.md#resolution-order`](../60-specification/whitespace-and-layout/separators-and-line-continuation.md#resolution-order) | c015 #1, #3, #4, #9 | traced |
| LY-OBL-011 | Keep comments, literals, and concrete operator assignment outside C015 | [`diagnostics-and-conformance.md#public-library-boundary`](../60-specification/whitespace-and-layout/diagnostics-and-conformance.md#public-library-boundary) | c015 #9 | traced |

C015 coverage is 11 `traced` and 0 untraced obligations. The dedicated gate
rejects unknown identifiers and fails if any `LY-OBL-*` identifier lacks a
focused tag.

## Comments and documentation registry (`CM`, 0.1.12)

Evidence labels refer to focused tests in
[`c016_comments_documentation_test.exs`](https://github.com/pcharbon70/catena/blob/rewrite/test/catena/c016_comments_documentation_test.exs)
and its
[`c016_traceability_coverage_test.exs`](https://github.com/pcharbon70/catena/blob/rewrite/test/catena/c016_traceability_coverage_test.exs)
gate:

- **c016 #1** *keeps 0.1.12 source-only with exact abstract frontend selections*
- **c016 #2** *fixes line, block, documentation, and degenerate delimiter edges*
- **c016 #3** *balances mixed and deep nested blocks and reports EOF depth*
- **c016 #4** *preserves Unicode spelling and original CRLF byte spans*
- **c016 #5** *normalizes only defined documentation edges and common margins*
- **c016 #6** *classifies every internal LF through the C015 layout engine*
- **c016 #7** *combines outer documentation and attaches it to the next target*
- **c016 #8** *keeps CommonMark, raw HTML, and doctest selection inert metadata*
- **c016 #9** *rejects every misplaced or unattached documentation group*

| ID | Obligation | Normative anchor | Evidence | Status |
| --- | --- | --- | --- | --- |
| CM-OBL-001 | Apply comment behavior only at exact 0.1.12 | [`diagnostics-and-conformance.md#revision-and-persistence-separation`](../60-specification/comments-and-documentation-comments/diagnostics-and-conformance.md#revision-and-persistence-separation) | c016 #1; EDN001 | traced |
| CM-OBL-002 | Recognize exact line/block/documentation edges and leave line LF unconsumed | [`comment-lexing-and-layout.md#comment-forms`](../60-specification/comments-and-documentation-comments/comment-lexing-and-layout.md#comment-forms) | c016 #2 | traced |
| CM-OBL-003 | Balance every nested block opener without a language depth limit | [`comment-lexing-and-layout.md#nested-block-comments`](../60-specification/comments-and-documentation-comments/comment-lexing-and-layout.md#nested-block-comments) | c016 #3; CMT002 | traced |
| CM-OBL-004 | Preserve C013 scalars, spans, and every internal LF without normalization | [`comment-lexing-and-layout.md#source-units-and-body-preservation`](../60-specification/comments-and-documentation-comments/comment-lexing-and-layout.md#source-units-and-body-preservation) | c016 #4, #6 | traced |
| CM-OBL-005 | Normalize documentation bodies by the exact algorithm | [`documentation-attachment-and-markdown.md#documentation-body-normalization`](../60-specification/comments-and-documentation-comments/documentation-attachment-and-markdown.md#documentation-body-normalization) | c016 #5 | traced |
| CM-OBL-006 | Combine adjacent documentation and attach only to the next valid target | [`documentation-attachment-and-markdown.md#grouping-and-declaration-attachment`](../60-specification/comments-and-documentation-comments/documentation-attachment-and-markdown.md#grouping-and-declaration-attachment) | c016 #7, #9; DOC001 | traced |
| CM-OBL-007 | Classify every comment-internal LF through unchanged C015 rules | [`comment-lexing-and-layout.md#layout-integration`](../60-specification/comments-and-documentation-comments/comment-lexing-and-layout.md#layout-integration) | c016 #6 | traced |
| CM-OBL-008 | Pin CommonMark, inert raw HTML, and exact explicit doctest metadata | [`documentation-attachment-and-markdown.md#markdown-profile`](../60-specification/comments-and-documentation-comments/documentation-attachment-and-markdown.md#markdown-profile) | c016 #7, #8 | traced |
| CM-OBL-009 | Emit stable comment and documentation diagnostics with reasons and spans | [`diagnostics-and-conformance.md#stable-diagnostics`](../60-specification/comments-and-documentation-comments/diagnostics-and-conformance.md#stable-diagnostics) | c016 #3, #9; CMT001, CMT002, DOC001 | traced |
| CM-OBL-010 | Keep scanner and resolver abstract and lossless | [`diagnostics-and-conformance.md#abstract-public-boundaries`](../60-specification/comments-and-documentation-comments/diagnostics-and-conformance.md#abstract-public-boundaries) | c016 #2, #6, #7 | traced |
| CM-OBL-011 | Produce deterministic scan and resolve results | [`diagnostics-and-conformance.md#conformance-obligations`](../60-specification/comments-and-documentation-comments/diagnostics-and-conformance.md#conformance-obligations) | c016 #1, #6 | traced |
| CM-OBL-012 | Preserve source-only and persisted-format separation | [`diagnostics-and-conformance.md#revision-and-persistence-separation`](../60-specification/comments-and-documentation-comments/diagnostics-and-conformance.md#revision-and-persistence-separation) | c016 #1 | traced |

C016 coverage is 12 `traced` and 0 untraced obligations. The dedicated gate
rejects unknown identifiers and fails if any `CM-OBL-*` identifier lacks a
focused tag.

## Literal grammar registry (`LT`, 0.1.13)

Evidence labels refer to focused tests in
[`c017_literal_grammar_test.exs`](https://github.com/pcharbon70/catena/blob/rewrite/test/catena/c017_literal_grammar_test.exs)
and its
[`c017_traceability_coverage_test.exs`](https://github.com/pcharbon70/catena/blob/rewrite/test/catena/c017_traceability_coverage_test.exs)
gate:

- **c017 #1** *keeps 0.1.13 source-only with exact lifecycle and persisted-format boundaries*
- **c017 #2** *fixes Boolean keyword and caller-supplied unit-index boundaries*
- **c017 #3** *returns exact normalized metadata for every integer base and decimal-float form*
- **c017 #4** *rejects malformed numeric digits, separators, zeros, exponents, suffixes, and signs*
- **c017 #5** *decodes the closed cooked escape set without Unicode normalization*
- **c017 #6** *matches arbitrary exact raw hashes and owns every internal LF*
- **c017 #7** *enforces one-scalar characters and exact cooked/raw byte domains*
- **c017 #8** *retains logical LF plus original CRLF and multibyte spans losslessly*
- **c017 #9** *accepts the exact LIM002/LIM004 floors and refuses the next unit*
- **c017 #10** *keeps compound, symbolic, byte-character, and interpolation forms excluded*

| ID | Obligation | Normative anchor | Evidence | Status |
| --- | --- | --- | --- | --- |
| LT-OBL-001 | Apply literal behavior only at exact 0.1.13 and register the stable lifecycle addition | [`diagnostics-limits-and-conformance.md#revision-and-persistence-separation`](../60-specification/literal-grammar/diagnostics-limits-and-conformance.md#revision-and-persistence-separation) | c017 #1; EDN001 | traced |
| LT-OBL-002 | Recognize exactly the six atomic kinds and keep named exclusions outside C017 | [`literal-forms-and-boundaries.md#atomic-literal-set`](../60-specification/literal-grammar/literal-forms-and-boundaries.md#atomic-literal-set) | c017 #2, #10; LIT001 | traced |
| LT-OBL-003 | Enforce numeric bases, separators, leading zeros, suffix boundaries, and exact components | [`literal-forms-and-boundaries.md#numeric-token-grammar`](../60-specification/literal-grammar/literal-forms-and-boundaries.md#numeric-token-grammar) | c017 #3, #4; LIT003 | traced |
| LT-OBL-004 | Recognize cooked delimiters and arbitrary exact raw hash delimiters | [`text-characters-and-bytes.md#text-character-and-byte-forms`](../60-specification/literal-grammar/text-characters-and-bytes.md#text-character-and-byte-forms) | c017 #5, #6; LIT002 | traced |
| LT-OBL-005 | Preserve lexeme, C013 units/spans, scalar spelling, decoded pieces, and no normalization | [`text-characters-and-bytes.md#decoded-payload-and-provenance`](../60-specification/literal-grammar/text-characters-and-bytes.md#decoded-payload-and-provenance) | c017 #5, #8 | traced |
| LT-OBL-006 | Enforce closed escapes, scalar validity, one-scalar characters, and direct-ASCII bytes | [`text-characters-and-bytes.md#cooked-escape-decoding`](../60-specification/literal-grammar/text-characters-and-bytes.md#cooked-escape-decoding) | c017 #5, #7; LIT003 | traced |
| LT-OBL-007 | Keep every raw LF inside the token and outside C015 layout | [`text-characters-and-bytes.md#raw-line-break-ownership`](../60-specification/literal-grammar/text-characters-and-bytes.md#raw-line-break-ownership) | c017 #6, #8 | traced |
| LT-OBL-008 | Accept the LIM002/LIM004 floors and refuse the next unit with structured measurements | [`diagnostics-limits-and-conformance.md#literal-implementation-limits`](../60-specification/literal-grammar/diagnostics-limits-and-conformance.md#literal-implementation-limits) | c017 #9; LIM002, LIM004 | traced |
| LT-OBL-009 | Emit stable literal and limit failures with reasons and original-byte spans | [`diagnostics-limits-and-conformance.md#stable-diagnostics`](../60-specification/literal-grammar/diagnostics-limits-and-conformance.md#stable-diagnostics) | c017 #2, #4–#9; LIT001–LIT003, LIM002, LIM004 | traced |
| LT-OBL-010 | Keep the scanner atomic, lossless, and outside whole lexing, parsing, rendering, and runtime typing | [`diagnostics-limits-and-conformance.md#abstract-public-boundary`](../60-specification/literal-grammar/diagnostics-limits-and-conformance.md#abstract-public-boundary) | c017 #1–#3, #5–#8, #10 | traced |
| LT-OBL-011 | Produce deterministic literal results and diagnostics | [`diagnostics-limits-and-conformance.md#determinism`](../60-specification/literal-grammar/diagnostics-limits-and-conformance.md#determinism) | c017 #1 | traced |
| LT-OBL-012 | Preserve source-only/persisted-format separation and static existing text forms | [`diagnostics-limits-and-conformance.md#revision-and-persistence-separation`](../60-specification/literal-grammar/diagnostics-limits-and-conformance.md#revision-and-persistence-separation) | c017 #1, #10 | traced |

C017 coverage is 12 `traced` and 0 untraced obligations. The dedicated gate
rejects unknown identifiers and fails if any `LT-OBL-*` identifier lacks a
focused tag.

## Numeric literal semantics registry (`NM`, 0.1.14)

Evidence labels refer to focused tests in the immutable compiler
[`c018_numeric_literal_semantics_test.exs`](https://github.com/pcharbon70/catena/blob/6fb2ad89a5cc5518528106f73d60b5adc9387d74/test/catena/c018_numeric_literal_semantics_test.exs)
and its
[`c018_traceability_coverage_test.exs`](https://github.com/pcharbon70/catena/blob/6fb2ad89a5cc5518528106f73d60b5adc9387d74/test/catena/c018_traceability_coverage_test.exs)
gate:

- **c018 #1** *keeps 0.1.14 exact selection with 0.1.13 scanning pinned and the lifecycle registered*
- **c018 #2** *fixes `Int` and finite binary64 `Float` domains with exact based-integer values*
- **c018 #3** *types literals monomorphically without constraints, defaulting, or coercion*
- **c018 #4** *elaborates negation totally on `Int` and sign-flipping on `Float` including `-0.0`*
- **c018 #5** *constructs exact rational meaning and rounds once with ties to even*
- **c018 #6** *admits subnormal results and underflow to signed zero*
- **c018 #7** *refuses overflow decimals as `NUM001` at the exact halfway boundary*
- **c018 #8** *keeps patterns unsigned and infinities and NaN unconstructible*
- **c018 #9** *accepts the `LIM005` floor and refuses the next decimal digit*
- **c018 #10** *keeps elaboration deterministic and outside later phases*

| ID | Obligation | Normative anchor | Evidence | Status |
| --- | --- | --- | --- | --- |
| NM-OBL-001 | Apply numeric meaning only at exact 0.1.14 and register the stable lifecycle addition | [`diagnostics-limits-and-conformance.md#revision-and-persistence-separation`](../60-specification/numeric-literal-semantics/diagnostics-limits-and-conformance.md#revision-and-persistence-separation) | c018 #1; EDN001 | traced |
| NM-OBL-002 | Fix `Int` as the unbounded mathematical integers with no value overflow | [`numeric-types-and-literal-typing.md#numeric-value-domains`](../60-specification/numeric-literal-semantics/numeric-types-and-literal-typing.md#numeric-value-domains) | c018 #2 | traced |
| NM-OBL-003 | Fix `Float` as finite binary64 with signed zero and no infinities or NaN | [`numeric-types-and-literal-typing.md#numeric-value-domains`](../60-specification/numeric-literal-semantics/numeric-types-and-literal-typing.md#numeric-value-domains) | c018 #2, #8 | traced |
| NM-OBL-004 | Type integer literals `Int` and decimal literals `Float`, monomorphically and context-independently | [`numeric-types-and-literal-typing.md#literal-typing`](../60-specification/numeric-literal-semantics/numeric-types-and-literal-typing.md#literal-typing) | c018 #3 | traced |
| NM-OBL-005 | Introduce no numeric defaulting, constraint generation, or expected-type adaptation | [`numeric-types-and-literal-typing.md#no-defaulting-and-no-implicit-coercion`](../60-specification/numeric-literal-semantics/numeric-types-and-literal-typing.md#no-defaulting-and-no-implicit-coercion) | c018 #3 | traced |
| NM-OBL-006 | Introduce no implicit numeric coercion; mixed numeric operands are ill-typed | [`numeric-types-and-literal-typing.md#no-defaulting-and-no-implicit-coercion`](../60-specification/numeric-literal-semantics/numeric-types-and-literal-typing.md#no-defaulting-and-no-implicit-coercion) | c018 #3 | traced |
| NM-OBL-007 | Elaborate numeric negation total on `Int` and sign-flipping on `Float`, including `-0.0` | [`numeric-types-and-literal-typing.md#numeric-negation`](../60-specification/numeric-literal-semantics/numeric-types-and-literal-typing.md#numeric-negation) | c018 #4 | traced |
| NM-OBL-008 | Keep the pattern grammar unsigned; negative and float pattern forms stay excluded | [`numeric-types-and-literal-typing.md#pattern-boundary`](../60-specification/numeric-literal-semantics/numeric-types-and-literal-typing.md#pattern-boundary) | c018 #8 | traced |
| NM-OBL-009 | Denote an integer literal by its exact C017 mathematical value | [`decimal-conversion-and-overflow.md#integer-literal-values`](../60-specification/numeric-literal-semantics/decimal-conversion-and-overflow.md#integer-literal-values) | c018 #2 | traced |
| NM-OBL-010 | Construct the exact rational meaning from the C017 components | [`decimal-conversion-and-overflow.md#exact-decimal-meaning`](../60-specification/numeric-literal-semantics/decimal-conversion-and-overflow.md#exact-decimal-meaning) | c018 #5 | traced |
| NM-OBL-011 | Round once to nearest binary64 with ties to even, admitting subnormals and underflow to zero | [`decimal-conversion-and-overflow.md#correct-rounding`](../60-specification/numeric-literal-semantics/decimal-conversion-and-overflow.md#correct-rounding) | c018 #5, #6 | traced |
| NM-OBL-012 | Refuse a decimal whose rounded result is not finite as `NUM001` static invalidity | [`decimal-conversion-and-overflow.md#overflow-and-static-invalidity`](../60-specification/numeric-literal-semantics/decimal-conversion-and-overflow.md#overflow-and-static-invalidity) | c018 #7; NUM001 | traced |
| NM-OBL-013 | Accept the `LIM005` 4,096-digit floor and refuse the next digit with structured measurements | [`diagnostics-limits-and-conformance.md#numeric-literal-implementation-limits`](../60-specification/numeric-literal-semantics/diagnostics-limits-and-conformance.md#numeric-literal-implementation-limits) | c018 #9; LIM005 | traced |
| NM-OBL-014 | Map `Int` to the Erlang integer and `Float` to the Erlang float and preserve persistence separation | [`diagnostics-limits-and-conformance.md#beam-representation`](../60-specification/numeric-literal-semantics/diagnostics-limits-and-conformance.md#beam-representation) | c018 #1, #2 | traced |

C018 coverage is 14 `traced` and 0 untraced obligations. The dedicated gate
rejects unknown identifiers and fails if any `NM-OBL-*` identifier lacks a
focused tag.

## Operators and punctuation registry (`OP`, 0.1.15)

Evidence labels refer to focused tests in the immutable compiler
[`c019_operators_test.exs`](https://github.com/pcharbon70/catena/blob/6e13bdf72547c4b363d794461c3f875fd0a16119/test/catena/c019_operators_test.exs)
and its
[`c019_traceability_coverage_test.exs`](https://github.com/pcharbon70/catena/blob/6e13bdf72547c4b363d794461c3f875fd0a16119/test/catena/c019_traceability_coverage_test.exs)
gate:

- **c019 #1** *keeps 0.1.15 exact selection with every predecessor default pinned and the lifecycle registered*
- **c019 #2** *recognizes the closed inventory and rejects reserved spellings as `OPR001`*
- **c019 #3** *enforces maximal munch and spacing-invariant tokenization against every atom*
- **c019 #4** *assigns the exact capability pair to every token*
- **c019 #5** *pushes paren/bracket continued and brace block frames and closes innermost matching*
- **c019 #6** *resolves the fixed ladder with exact grouping and associativity*
- **c019 #7** *rejects chained and mixed comparisons as `OPR002`, accepting regroupings*
- **c019 #8** *fixes prefix minus and not above the ladder and never inside a literal*
- **c019 #9** *binds `|>` left-associative at the loosest level with application structure*
- **c019 #10** *keeps `->` and `.` outside 0.1.15 expression rules*
- **c019 #11** *exposes the lossless stream and tree-or-diagnostic boundary with no recovery*
- **c019 #12** *keeps tokenization and parsing deterministic and outside later phases*

| ID | Obligation | Normative anchor | Evidence | Status |
| --- | --- | --- | --- | --- |
| OP-OBL-001 | Apply operator behavior only at exact 0.1.15 and register the stable lifecycle addition | [`diagnostics-and-conformance.md#revision-and-persistence-separation`](../60-specification/operators-and-punctuation/diagnostics-and-conformance.md#revision-and-persistence-separation) | c019 #1; EDN001 | traced |
| OP-OBL-002 | Recognize exactly the closed inventory and no other operator or punctuation spelling | [`token-inventory-and-maximal-munch.md#closed-inventory`](../60-specification/operators-and-punctuation/token-inventory-and-maximal-munch.md#closed-inventory) | c019 #2 | traced |
| OP-OBL-003 | Enforce maximal munch and spacing-invariant tokenization against every atom | [`token-inventory-and-maximal-munch.md#maximal-munch`](../60-specification/operators-and-punctuation/token-inventory-and-maximal-munch.md#maximal-munch) | c019 #3 | traced |
| OP-OBL-004 | Reject reserved and invalid symbol spellings as `OPR001` without re-tokenization | [`token-inventory-and-maximal-munch.md#reserved-and-invalid-spellings`](../60-specification/operators-and-punctuation/token-inventory-and-maximal-munch.md#reserved-and-invalid-spellings) | c019 #2; OPR001 | traced |
| OP-OBL-005 | Assign the exact `join_before`/`join_after` capability pair to every token | [`capabilities-and-delimiter-frames.md#token-continuation-capabilities`](../60-specification/operators-and-punctuation/capabilities-and-delimiter-frames.md#token-continuation-capabilities) | c019 #4 | traced |
| OP-OBL-006 | Push `paren`/`bracket` continued and `brace` block frames and close innermost matching | [`capabilities-and-delimiter-frames.md#delimiter-families-and-frame-modes`](../60-specification/operators-and-punctuation/capabilities-and-delimiter-frames.md#delimiter-families-and-frame-modes) | c019 #5; LAY002 | traced |
| OP-OBL-007 | Fix the precedence ladder and per-level associativity exactly, with no fixity declarations | [`precedence-and-associativity.md#the-fixed-ladder`](../60-specification/operators-and-punctuation/precedence-and-associativity.md#the-fixed-ladder) | c019 #6 | traced |
| OP-OBL-008 | Reject comparison and equality chains as `OPR002`, accepting parenthesized regrouping | [`precedence-and-associativity.md#comparison-and-equality-chaining`](../60-specification/operators-and-punctuation/precedence-and-associativity.md#comparison-and-equality-chaining) | c019 #7; OPR002 | traced |
| OP-OBL-009 | Fix prefix `-`/`!` above the binary ladder, right-recursively, never inside a literal | [`precedence-and-associativity.md#prefix-operators`](../60-specification/operators-and-punctuation/precedence-and-associativity.md#prefix-operators) | c019 #8 | traced |
| OP-OBL-010 | Fix `\|>` left-associative at the loosest level denoting application of right to left | [`precedence-and-associativity.md#the-pipe`](../60-specification/operators-and-punctuation/precedence-and-associativity.md#the-pipe) | c019 #9 | traced |
| OP-OBL-011 | Tokenize `->` while excluding it from 0.1.15 expression rules | [`precedence-and-associativity.md#the-reserved-arrow`](../60-specification/operators-and-punctuation/precedence-and-associativity.md#the-reserved-arrow) | c019 #10 | traced |
| OP-OBL-012 | Fix `.` as qualification-only, never field access | [`capabilities-and-delimiter-frames.md#the-dot-interaction`](../60-specification/operators-and-punctuation/capabilities-and-delimiter-frames.md#the-dot-interaction) | c019 #10 | traced |
| OP-OBL-013 | Expose the lossless whole-source stream and the tree-or-diagnostic parse boundary | [`diagnostics-and-conformance.md#abstract-public-boundaries`](../60-specification/operators-and-punctuation/diagnostics-and-conformance.md#abstract-public-boundaries) | c019 #11 | traced |
| OP-OBL-014 | Reject transactionally with `OPR001`/`OPR002`/C015 events and no recovery | [`diagnostics-and-conformance.md#recovery`](../60-specification/operators-and-punctuation/diagnostics-and-conformance.md#recovery) | c019 #11; OPR001, OPR002, LAY002, LAY003 | traced |
| OP-OBL-015 | Produce deterministic streams and trees | [`diagnostics-and-conformance.md#determinism`](../60-specification/operators-and-punctuation/diagnostics-and-conformance.md#determinism) | c019 #12 | traced |
| OP-OBL-016 | Preserve source-only and persisted-format separation and claim no later phase | [`diagnostics-and-conformance.md#revision-and-persistence-separation`](../60-specification/operators-and-punctuation/diagnostics-and-conformance.md#revision-and-persistence-separation) | c019 #1, #12 | traced |

C019 coverage is 16 `traced` and 0 untraced obligations. The dedicated gate
rejects unknown identifiers and fails if any `OP-OBL-*` identifier lacks a
focused tag.

## Files and modules registry (`FU`, 0.1.16)

Evidence labels refer to focused tests in the immutable compiler
[`c020_file_unit_test.exs`](https://github.com/pcharbon70/catena/blob/677a8f4a91f047d3ee97f197992b24401cff9a41/test/catena/c020_file_unit_test.exs)
and its
[`c020_traceability_coverage_test.exs`](https://github.com/pcharbon70/catena/blob/677a8f4a91f047d3ee97f197992b24401cff9a41/test/catena/c020_traceability_coverage_test.exs)
gate:

- **c020 #1** *keeps 0.1.16 exact selection with every predecessor default pinned and the lifecycle registered*
- **c020 #2** *requires the `.cat` extension and reports `FIL001` otherwise*
- **c020 #3** *classifies module and no-module files with valid empty and comment-only units*
- **c020 #4** *rejects multiple module declarations as `FIL002` and bad spellings as `FIL003`*
- **c020 #5** *verifies declared names against basenames with `FIL004` and no name for no-module files*
- **c020 #6** *recognizes the exact marker grammar with varied tool identifiers*
- **c020 #7** *enforces first-unit placement and keeps marker text inert elsewhere*
- **c020 #8** *rejects malformed first-unit markers as `FIL005`*
- **c020 #9** *emits stable diagnostics with spans and both names on mismatch*
- **c020 #10** *keeps the resolver deterministic, source-only, and outside later phases*

| ID | Obligation | Normative anchor | Evidence | Status |
| --- | --- | --- | --- | --- |
| FU-OBL-001 | Apply file-unit behavior only at exact 0.1.16 and register the stable lifecycle addition | [`diagnostics-and-conformance.md#revision-and-persistence-separation`](../60-specification/files-and-modules/diagnostics-and-conformance.md#revision-and-persistence-separation) | c020 #1; EDN001 | traced |
| FU-OBL-002 | Require the `.cat` extension and report `FIL001` otherwise | [`file-units-and-module-binding.md#source-file-extension`](../60-specification/files-and-modules/file-units-and-module-binding.md#source-file-extension) | c020 #2; FIL001 | traced |
| FU-OBL-003 | Classify module and no-module files with valid empty and comment-only units | [`file-units-and-module-binding.md#file-units`](../60-specification/files-and-modules/file-units-and-module-binding.md#file-units) | c020 #3 | traced |
| FU-OBL-004 | Reject more than one module declaration as `FIL002` | [`file-units-and-module-binding.md#module-multiplicity`](../60-specification/files-and-modules/file-units-and-module-binding.md#module-multiplicity) | c020 #4; FIL002 | traced |
| FU-OBL-005 | Enforce the ASCII uppercase-initial module-name spelling with `FIL003` | [`file-units-and-module-binding.md#file-level-module-name-spelling`](../60-specification/files-and-modules/file-units-and-module-binding.md#file-level-module-name-spelling) | c020 #4; FIL003 | traced |
| FU-OBL-006 | Verify the declared name against the basename with `FIL004`, matching no name for no-module files | [`file-units-and-module-binding.md#declared-name-basename-verification`](../60-specification/files-and-modules/file-units-and-module-binding.md#declared-name-basename-verification) | c020 #5; FIL004 | traced |
| FU-OBL-007 | Recognize the exact marker grammar with its tool identifier | [`generated-file-markers.md#marker-spelling`](../60-specification/files-and-modules/generated-file-markers.md#marker-spelling) | c020 #6 | traced |
| FU-OBL-008 | Enforce first-unit placement and single recognition | [`generated-file-markers.md#first-unit-placement`](../60-specification/files-and-modules/generated-file-markers.md#first-unit-placement) | c020 #7 | traced |
| FU-OBL-009 | Reject malformed first-unit markers as `FIL005` and keep the text inert elsewhere | [`generated-file-markers.md#inert-elsewhere`](../60-specification/files-and-modules/generated-file-markers.md#inert-elsewhere) | c020 #7, #8; FIL005 | traced |
| FU-OBL-010 | Emit stable file diagnostics with spans and both names on mismatch | [`diagnostics-and-conformance.md#stable-diagnostics`](../60-specification/files-and-modules/diagnostics-and-conformance.md#stable-diagnostics) | c020 #9; FIL001–FIL005 | traced |
| FU-OBL-011 | Expose the lossless resolver boundary deterministically | [`diagnostics-and-conformance.md#abstract-public-boundary`](../60-specification/files-and-modules/diagnostics-and-conformance.md#abstract-public-boundary) | c020 #10 | traced |
| FU-OBL-012 | Preserve source-only and persisted-format separation and claim no later phase | [`diagnostics-and-conformance.md#revision-and-persistence-separation`](../60-specification/files-and-modules/diagnostics-and-conformance.md#revision-and-persistence-separation) | c020 #1, #10 | traced |

C020 coverage is 12 `traced` and 0 untraced obligations. The dedicated
gate rejects unknown identifiers and fails if any `FU-OBL-*` identifier
lacks a focused tag.

## Namespaces and shadowing registry (`NS`, 0.1.17)

Evidence labels refer to focused tests in the immutable compiler
[`c021_namespaces_test.exs`](https://github.com/pcharbon70/catena/blob/b482b4cacc4017b8e479173fb3bd3c0ceac4f675/test/catena/c021_namespaces_test.exs)
and its
[`c021_traceability_coverage_test.exs`](https://github.com/pcharbon70/catena/blob/b482b4cacc4017b8e479173fb3bd3c0ceac4f675/test/catena/c021_traceability_coverage_test.exs)
gate:

- **c021 #1** *keeps 0.1.17 exact selection with every predecessor default pinned and the lifecycle registered*
- **c021 #2** *keeps categories disjoint so one spelling coexists across them*
- **c021 #3** *enforces the hard spelling-class partition with `NSP002`*
- **c021 #4** *rejects same-scope duplicates per uniqueness domain as `NSP001`*
- **c021 #5** *keeps governed identities out of program resolution and vice versa*
- **c021 #6** *resolves exactly two-segment qualification and rejects deeper chains as `NSP005`*
- **c021 #7** *resolves innermost-visible bindings with silent cross-category-safe shadowing*
- **c021 #8** *scopes type variables per quantifier with type shadowing and value separation*
- **c021 #9** *enforces local-over-imported precedence and order-independent `NSP004` ambiguity*
- **c021 #10** *rejects unbound references as `NSP003`*
- **c021 #11** *emits stable diagnostics with spelling, category, and all colliding origins*
- **c021 #12** *keeps the resolver deterministic, source-only, and outside later phases*

| ID | Obligation | Normative anchor | Evidence | Status |
| --- | --- | --- | --- | --- |
| NS-OBL-001 | Apply namespace behavior only at exact 0.1.17 and register the stable lifecycle addition | [`diagnostics-and-conformance.md#revision-and-persistence-separation`](../60-specification/namespaces-and-shadowing/diagnostics-and-conformance.md#revision-and-persistence-separation) | c021 #1; EDN001 | traced |
| NS-OBL-002 | Enforce disjoint categories where one spelling resolves in at most its requested category | [`namespace-inventory-and-spelling.md#namespace-categories`](../60-specification/namespaces-and-shadowing/namespace-inventory-and-spelling.md#namespace-categories) | c021 #2 | traced |
| NS-OBL-003 | Enforce the hard spelling-class partition with `NSP002` | [`namespace-inventory-and-spelling.md#spelling-class-partition`](../60-specification/namespaces-and-shadowing/namespace-inventory-and-spelling.md#spelling-class-partition) | c021 #3; NSP002 | traced |
| NS-OBL-004 | Reject same-scope duplicates per uniqueness domain as `NSP001` | [`namespace-inventory-and-spelling.md#uniqueness-domains`](../60-specification/namespaces-and-shadowing/namespace-inventory-and-spelling.md#uniqueness-domains) | c021 #4; NSP001 | traced |
| NS-OBL-005 | Keep governed identities out of program resolution and vice versa | [`namespace-inventory-and-spelling.md#governed-identity-separation`](../60-specification/namespaces-and-shadowing/namespace-inventory-and-spelling.md#governed-identity-separation) | c021 #5 | traced |
| NS-OBL-006 | Resolve exactly two-segment qualification and reject deeper chains as `NSP005` | [`namespace-inventory-and-spelling.md#qualification-depth`](../60-specification/namespaces-and-shadowing/namespace-inventory-and-spelling.md#qualification-depth) | c021 #6; NSP005 | traced |
| NS-OBL-007 | Resolve innermost-visible bindings with silent deterministic shadowing | [`shadowing-and-ambiguity.md#shadowing`](../60-specification/namespaces-and-shadowing/shadowing-and-ambiguity.md#shadowing) | c021 #7 | traced |
| NS-OBL-008 | Scope type variables per quantifier with type shadowing and value separation | [`shadowing-and-ambiguity.md#type-variables`](../60-specification/namespaces-and-shadowing/shadowing-and-ambiguity.md#type-variables) | c021 #8 | traced |
| NS-OBL-009 | Enforce local-over-imported precedence and order-independent `NSP004` ambiguity rejection | [`shadowing-and-ambiguity.md#cross-origin-precedence`](../60-specification/namespaces-and-shadowing/shadowing-and-ambiguity.md#cross-origin-precedence) | c021 #9; NSP004 | traced |
| NS-OBL-010 | Reject unbound references as `NSP003` | [`shadowing-and-ambiguity.md#cross-origin-precedence`](../60-specification/namespaces-and-shadowing/shadowing-and-ambiguity.md#cross-origin-precedence) | c021 #10; NSP003 | traced |
| NS-OBL-011 | Emit stable diagnostics with spelling, category, and all colliding origins | [`diagnostics-and-conformance.md#stable-diagnostics`](../60-specification/namespaces-and-shadowing/diagnostics-and-conformance.md#stable-diagnostics) | c021 #11; NSP001–NSP005 | traced |
| NS-OBL-012 | Expose the environment-building and reference-resolution boundaries as tree-or-diagnostic operations | [`diagnostics-and-conformance.md#abstract-public-boundaries`](../60-specification/namespaces-and-shadowing/diagnostics-and-conformance.md#abstract-public-boundaries) | c021 #12 | traced |
| NS-OBL-013 | Produce deterministic environments and resolutions | [`diagnostics-and-conformance.md#determinism`](../60-specification/namespaces-and-shadowing/diagnostics-and-conformance.md#determinism) | c021 #12 | traced |
| NS-OBL-014 | Preserve source-only and persisted-format separation and claim no later phase | [`diagnostics-and-conformance.md#revision-and-persistence-separation`](../60-specification/namespaces-and-shadowing/diagnostics-and-conformance.md#revision-and-persistence-separation) | c021 #1, #12 | traced |

C021 coverage is 14 `traced` and 0 untraced obligations. The dedicated
gate rejects unknown identifiers and fails if any `NS-OBL-*` identifier
lacks a focused tag.

## Imports and exports registry (`IM`, 0.1.18)

Evidence labels refer to focused tests in the immutable compiler
[`c022_import_exports_test.exs`](https://github.com/pcharbon70/catena/blob/02da5c178ad5d797e55bdb3290cd950fbf7f4f31/test/catena/c022_import_exports_test.exs)
and its
[`c022_traceability_coverage_test.exs`](https://github.com/pcharbon70/catena/blob/02da5c178ad5d797e55bdb3290cd950fbf7f4f31/test/catena/c022_traceability_coverage_test.exs)
gate:

- **c022 #1** *keeps 0.1.18 exact selection with every predecessor default pinned and the lifecycle registered*
- **c022 #2** *exports nothing by default and private names never resolve elsewhere*
- **c022 #3** *validates export events with categories, spelling classes, and transparency modes*
- **c022 #4** *rejects exports of undeclared names as `EXP001`*
- **c022 #5** *admits qualification against export sets plus listed unqualified names with the empty qualified-only form*
- **c022 #6** *rejects unexported listed names as `IMP002` and unknown modules as `IMP003`*
- **c022 #7** *admits no wildcard, hiding, renaming, alias, or re-export form*
- **c022 #8** *feeds imports into C021 precedence and reference-time `NSP004` unchanged*
- **c022 #9** *reports unused names and wholly unused modules as deny-able `IMP001` warnings only*
- **c022 #10** *emits stable diagnostics with spelling, category, and module*
- **c022 #11** *keeps the resolver and analysis deterministic, source-only, and outside later phases*

| ID | Obligation | Normative anchor | Evidence | Status |
| --- | --- | --- | --- | --- |
| IM-OBL-001 | Apply import/export behavior only at exact 0.1.18 and register the stable lifecycle addition | [`diagnostics-and-conformance.md#revision-and-persistence-separation`](../60-specification/imports-and-exports/diagnostics-and-conformance.md#revision-and-persistence-separation) | c022 #1; EDN001 | traced |
| IM-OBL-002 | Export nothing without an explicit export declaration; private names never resolve elsewhere | [`export-declarations-and-visibility.md#private-by-default`](../60-specification/imports-and-exports/export-declarations-and-visibility.md#private-by-default) | c022 #2 | traced |
| IM-OBL-003 | Enforce export events with categories, spelling classes, and type transparency modes | [`export-declarations-and-visibility.md#export-declaration-events`](../60-specification/imports-and-exports/export-declarations-and-visibility.md#export-declaration-events) | c022 #3 | traced |
| IM-OBL-004 | Reject exports of undeclared names as `EXP001` | [`export-declarations-and-visibility.md#validation`](../60-specification/imports-and-exports/export-declarations-and-visibility.md#validation) | c022 #4; EXP001 | traced |
| IM-OBL-005 | Enforce two-effect admission: qualification against the export set plus listed unqualified admission with the empty qualified-only form | [`import-declarations-and-admission.md#admission`](../60-specification/imports-and-exports/import-declarations-and-admission.md#admission) | c022 #5 | traced |
| IM-OBL-006 | Reject unexported listed names as `IMP002` and unknown modules as `IMP003` | [`import-declarations-and-admission.md#validation`](../60-specification/imports-and-exports/import-declarations-and-admission.md#validation) | c022 #6; IMP002, IMP003 | traced |
| IM-OBL-007 | Admit no wildcard, hiding, renaming, alias, or re-export form | [`import-declarations-and-admission.md#declared-exclusions`](../60-specification/imports-and-exports/import-declarations-and-admission.md#declared-exclusions) | c022 #7 | traced |
| IM-OBL-008 | Feed imported names into C021 precedence and reference-time `NSP004` unchanged | [`import-declarations-and-admission.md#precedence-interaction`](../60-specification/imports-and-exports/import-declarations-and-admission.md#precedence-interaction) | c022 #8 | traced |
| IM-OBL-009 | Emit stable import/export diagnostics with spelling, category, and module | [`diagnostics-and-conformance.md#stable-diagnostics`](../60-specification/imports-and-exports/diagnostics-and-conformance.md#stable-diagnostics) | c022 #10 | traced |
| IM-OBL-010 | Keep `IMP001` a deny-able warning that never affects acceptance | [`diagnostics-and-conformance.md#stable-diagnostics`](../60-specification/imports-and-exports/diagnostics-and-conformance.md#stable-diagnostics) | c022 #9; IMP001 | traced |
| IM-OBL-011 | Expose the unused-import analysis returning warnings only | [`diagnostics-and-conformance.md#abstract-public-boundaries`](../60-specification/imports-and-exports/diagnostics-and-conformance.md#abstract-public-boundaries) | c022 #9 | traced |
| IM-OBL-012 | Produce deterministic environments, diagnostics, and warning order | [`diagnostics-and-conformance.md#determinism`](../60-specification/imports-and-exports/diagnostics-and-conformance.md#determinism) | c022 #11 | traced |
| IM-OBL-013 | Preserve source-only and persisted-format separation and claim no later phase | [`diagnostics-and-conformance.md#revision-and-persistence-separation`](../60-specification/imports-and-exports/diagnostics-and-conformance.md#revision-and-persistence-separation) | c022 #1, #11 | traced |

C022 coverage is 13 `traced` and 0 untraced obligations. The dedicated
gate rejects unknown identifiers and fails if any `IM-OBL-*` identifier
lacks a focused tag.

## Abstraction boundaries registry (`AB`, 0.1.19)

Evidence labels refer to focused tests in the immutable compiler
[`c023_abstraction_test.exs`](https://github.com/pcharbon70/catena/blob/bbce0ee25fe6f8b64204a4ec757dc6d281d63f9f/test/catena/c023_abstraction_test.exs)
and its
[`c023_traceability_coverage_test.exs`](https://github.com/pcharbon70/catena/blob/bbce0ee25fe6f8b64204a4ec757dc6d281d63f9f/test/catena/c023_traceability_coverage_test.exs)
gate:

- **c023 #1** *keeps 0.1.19 exact selection with every predecessor default pinned and the lifecycle registered*
- **c023 #2** *keeps the transparent/abstract pair the complete authority vocabulary on export events and persisted interfaces*
- **c023 #3** *admits no stable-layout spelling on any frontend and keeps both-layout conformance mandatory*
- **c023 #4** *sanctions the smart-constructor idiom with typed-failure validation and rejects public-constructor wrappers*
- **c023 #5** *enforces wildcard-plus-observers coverage for abstract scrutinees*
- **c023 #6** *keeps abstract constructors unconstructible and unmatchable through digest-bound interfaces*
- **c023 #7** *adds no frontend surface and claims no later phase*

| ID | Obligation | Normative anchor | Evidence | Status |
| --- | --- | --- | --- | --- |
| AB-OBL-001 | Apply abstraction-boundary behavior only at exact 0.1.19 and register the stable lifecycle addition | [`smart-constructor-idiom-and-conformance.md#revision-and-persistence-separation`](../60-specification/abstraction-boundaries/smart-constructor-idiom-and-conformance.md#revision-and-persistence-separation) | c023 #1; EDN001 | traced |
| AB-OBL-002 | Keep the transparent/abstract pair the complete authority vocabulary on every frontend | [`authority-and-representation-exclusions.md#the-authority-vocabulary-is-complete`](../60-specification/abstraction-boundaries/authority-and-representation-exclusions.md#the-authority-vocabulary-is-complete) | c023 #2; EXP001 | traced |
| AB-OBL-003 | Admit no stable-layout form on any frontend; keep both-layout conformance mandatory | [`authority-and-representation-exclusions.md#representation-is-never-observable`](../60-specification/abstraction-boundaries/authority-and-representation-exclusions.md#representation-is-never-observable) | c023 #3; L001 | traced |
| AB-OBL-004 | Sanction the abstract-plus-validating-constructor-plus-observer idiom and reject wrappers as invariants | [`smart-constructor-idiom-and-conformance.md#the-sanctioned-invariant-idiom`](../60-specification/abstraction-boundaries/smart-constructor-idiom-and-conformance.md#the-sanctioned-invariant-idiom) | c023 #4 | traced |
| AB-OBL-005 | Enforce the wildcard-plus-observers coverage consequence for abstract scrutinees outside the defining module | [`smart-constructor-idiom-and-conformance.md#coverage-consequence`](../60-specification/abstraction-boundaries/smart-constructor-idiom-and-conformance.md#coverage-consequence) | c023 #5 | traced |
| AB-OBL-006 | Keep abstract constructors unconstructible and unmatchable through digest-bound interfaces | [`smart-constructor-idiom-and-conformance.md#the-sanctioned-invariant-idiom`](../60-specification/abstraction-boundaries/smart-constructor-idiom-and-conformance.md#the-sanctioned-invariant-idiom) | c023 #6 | traced |
| AB-OBL-007 | Preserve source-only and persisted-format separation and claim no later phase | [`smart-constructor-idiom-and-conformance.md#revision-and-persistence-separation`](../60-specification/abstraction-boundaries/smart-constructor-idiom-and-conformance.md#revision-and-persistence-separation) | c023 #1, #7 | traced |

C023 coverage is 7 `traced` and 0 untraced obligations. The dedicated
gate rejects unknown identifiers and fails if any `AB-OBL-*` identifier
lacks a focused tag.

## Module dependency cycles registry (`CY`, 0.1.20)

Evidence labels refer to focused tests in the immutable compiler
[`c024_module_cycles_test.exs`](https://github.com/pcharbon70/catena/blob/ca2be792e3f5fe081c67ec7ca9e845d40a5087c0/test/catena/c024_module_cycles_test.exs)
and its
[`c024_traceability_coverage_test.exs`](https://github.com/pcharbon70/catena/blob/ca2be792e3f5fe081c67ec7ca9e845d40a5087c0/test/catena/c024_traceability_coverage_test.exs)
gate:

- **c024 #1** *keeps 0.1.20 exact selection with every predecessor default pinned and the lifecycle registered*
- **c024 #2** *admits cycles: SCC grouping of pairs, self-loops, and rings; no shape is an error*
- **c024 #3** *enforces the two regimes with backward-compatible optional fields*
- **c024 #4** *keeps acyclic behavior byte-identical to C022 including degenerate components*
- **c024 #5** *rejects regime mixing and signature gaps as `CYC001` at the closing event*
- **c024 #6** *computes deterministic joint digests invariant to member order*
- **c024 #7** *records dependency inversion as the sanctioned non-cyclic restructuring*
- **c024 #8** *confirms definition-only initialization and per-member inference*
- **c024 #9** *makes the component the atomic cache unit*
- **c024 #10** *compiles genuine two- and three-module components end-to-end deterministically*

| ID | Obligation | Normative anchor | Evidence | Status |
| --- | --- | --- | --- | --- |
| CY-OBL-001 | Apply cycle behavior only at exact 0.1.20 and register the stable lifecycle addition | [`diagnostics-and-conformance.md#revision-and-persistence-separation`](../60-specification/module-dependency-cycles/diagnostics-and-conformance.md#revision-and-persistence-separation) | c024 #1; EDN001 | traced |
| CY-OBL-002 | Admit cycles: multi-module components group and resolve; no cycle shape is an error | [`scc-admission-and-resolution.md#cycle-admission`](../60-specification/module-dependency-cycles/scc-admission-and-resolution.md#cycle-admission) | c024 #2 | traced |
| CY-OBL-003 | Enforce the two regimes: signature resolution inside components, digest admission across, with backward-compatible optional fields | [`scc-admission-and-resolution.md#the-two-resolution-regimes`](../60-specification/module-dependency-cycles/scc-admission-and-resolution.md#the-two-resolution-regimes) | c024 #3 | traced |
| CY-OBL-004 | Keep acyclic behavior byte-identical to C022, including degenerate single-member components | [`scc-admission-and-resolution.md#the-degenerate-acyclic-case`](../60-specification/module-dependency-cycles/scc-admission-and-resolution.md#the-degenerate-acyclic-case) | c024 #4 | traced |
| CY-OBL-005 | Reject regime mixing and signature gaps as `CYC001` at the closing event, transactionally | [`diagnostics-and-conformance.md#stable-diagnostics`](../60-specification/module-dependency-cycles/diagnostics-and-conformance.md#stable-diagnostics) | c024 #5; CYC001 | traced |
| CY-OBL-006 | Compute deterministic joint component digests over sorted members and member interfaces | [`scc-admission-and-resolution.md#joint-component-digest`](../60-specification/module-dependency-cycles/scc-admission-and-resolution.md#joint-component-digest) | c024 #6 | traced |
| CY-OBL-007 | Record the dependency-inversion alternative as the sanctioned non-cyclic restructuring | [`scc-admission-and-resolution.md#the-inversion-alternative`](../60-specification/module-dependency-cycles/scc-admission-and-resolution.md#the-inversion-alternative) | c024 #7 | traced |
| CY-OBL-008 | Confirm definition-only initialization with per-component loading and per-member inference | [`checking-initialization-and-caching.md#initialization`](../60-specification/module-dependency-cycles/checking-initialization-and-caching.md#initialization) | c024 #8 | traced |
| CY-OBL-009 | Make the component the atomic cache unit: rebuilding any member re-digests the component | [`checking-initialization-and-caching.md#separate-compilation-and-caching`](../60-specification/module-dependency-cycles/checking-initialization-and-caching.md#separate-compilation-and-caching) | c024 #9 | traced |
| CY-OBL-010 | Compile genuine multi-module components end-to-end deterministically | [`diagnostics-and-conformance.md#abstract-public-boundaries`](../60-specification/module-dependency-cycles/diagnostics-and-conformance.md#abstract-public-boundaries) | c024 #10 | traced |

C024 coverage is 10 `traced` and 0 untraced obligations. The dedicated
gate rejects unknown identifiers and fails if any `CY-OBL-*` identifier
lacks a focused tag.

## Package identity and dependencies registry (`PK`, 0.1.21)

Evidence labels refer to focused tests in the immutable compiler
[`c025_package_deps_test.exs`](https://github.com/pcharbon70/catena/blob/dcd7da056ba1317fcd7df1df8716981ff8363e1d/test/catena/c025_package_deps_test.exs)
and its
[`c025_traceability_coverage_test.exs`](https://github.com/pcharbon70/catena/blob/dcd7da056ba1317fcd7df1df8716981ff8363e1d/test/catena/c025_traceability_coverage_test.exs)
gate:

- **c025 #1** *keeps 0.1.21 exact selection with every predecessor default pinned and the lifecycle registered*
- **c025 #2** *validates the `dependencies` field and rejects malformed names and requirements as `PKG001`*
- **c025 #3** *enforces the SemVer grammar and precedence including pre-release ordering and build exclusion*
- **c025 #4** *enforces the three-form requirement grammar rejecting other operators and operand build metadata*
- **c025 #5** *enforces exact/caret/tilde satisfaction with the Cargo 0.x rule and pre-release operand restriction*
- **c025 #6** *computes registry-neutral bundle digests stable under reordering*
- **c025 #7** *rejects cyclic package graphs as `PKG002` with the cycle path*
- **c025 #8** *resolves single-version highest-satisfying per name, order-independently*
- **c025 #9** *rejects unsatisfiable sets as `PKG003` with every requirer and unknown names as `PKG004`*
- **c025 #10** *generates byte-deterministic `catena.lock` records and replays them as exact pins*
- **c025 #11** *rejects stale and tampered lockfiles as `PKG005`*
- **c025 #12** *keeps the engine deterministic, source-only, and outside G121/G130 phases*

| ID | Obligation | Normative anchor | Evidence | Status |
| --- | --- | --- | --- | --- |
| PK-OBL-001 | Apply package behavior only at exact 0.1.21 and register the stable lifecycle addition | [`diagnostics-and-conformance.md#revision-and-persistence-separation`](../60-specification/package-identity-and-dependencies/diagnostics-and-conformance.md#revision-and-persistence-separation) | c025 #1; EDN001 | traced |
| PK-OBL-002 | Validate the `dependencies` field: names, single requirement strings, absence means free | [`manifest-dependencies-and-versions.md#the-dependencies-field`](../60-specification/package-identity-and-dependencies/manifest-dependencies-and-versions.md#the-dependencies-field) | c025 #2; PKG001 | traced |
| PK-OBL-003 | Enforce the SemVer grammar and precedence including pre-release ordering and build exclusion | [`manifest-dependencies-and-versions.md#version-grammar`](../60-specification/package-identity-and-dependencies/manifest-dependencies-and-versions.md#version-grammar) | c025 #3 | traced |
| PK-OBL-004 | Enforce the three-form requirement grammar, rejecting other operators, compounds, and operand build metadata | [`manifest-dependencies-and-versions.md#requirement-grammar`](../60-specification/package-identity-and-dependencies/manifest-dependencies-and-versions.md#requirement-grammar) | c025 #4; PKG001 | traced |
| PK-OBL-005 | Enforce exact/caret/tilde satisfaction with the Cargo 0.x rule and the pre-release operand restriction | [`manifest-dependencies-and-versions.md#satisfaction`](../60-specification/package-identity-and-dependencies/manifest-dependencies-and-versions.md#satisfaction) | c025 #5 | traced |
| PK-OBL-006 | Compute registry-neutral bundle digests as SHA-256 over canonical JCS of semantic fields plus member and component digests | [`resolution-and-lockfile.md#bundle-digest-identity`](../60-specification/package-identity-and-dependencies/resolution-and-lockfile.md#bundle-digest-identity) | c025 #6 | traced |
| PK-OBL-007 | Reject cyclic package graphs as `PKG002` with the cycle path | [`resolution-and-lockfile.md#the-dependency-graph-is-a-dag`](../60-specification/package-identity-and-dependencies/resolution-and-lockfile.md#the-dependency-graph-is-a-dag) | c025 #7; PKG002 | traced |
| PK-OBL-008 | Resolve single-version highest-satisfying per name, order-independently | [`resolution-and-lockfile.md#single-version-resolution`](../60-specification/package-identity-and-dependencies/resolution-and-lockfile.md#single-version-resolution) | c025 #8 | traced |
| PK-OBL-009 | Reject unsatisfiable sets as `PKG003` with every requirer and absent names as `PKG004` | [`resolution-and-lockfile.md#single-version-resolution`](../60-specification/package-identity-and-dependencies/resolution-and-lockfile.md#single-version-resolution) | c025 #9; PKG003, PKG004 | traced |
| PK-OBL-010 | Generate canonical byte-deterministic `catena.lock` records | [`resolution-and-lockfile.md#the-lockfile`](../60-specification/package-identity-and-dependencies/resolution-and-lockfile.md#the-lockfile) | c025 #10 | traced |
| PK-OBL-011 | Replay a matching lockfile as exact pins and reject stale or tampered locks as `PKG005` | [`resolution-and-lockfile.md#the-lockfile`](../60-specification/package-identity-and-dependencies/resolution-and-lockfile.md#the-lockfile) | c025 #10, #11; PKG005 | traced |
| PK-OBL-012 | Keep the engine deterministic, source-only, and outside G121/G130 phases | [`diagnostics-and-conformance.md#revision-and-persistence-separation`](../60-specification/package-identity-and-dependencies/diagnostics-and-conformance.md#revision-and-persistence-separation) | c025 #1, #12 | traced |

C025 coverage is 12 `traced` and 0 untraced obligations. The dedicated
gate rejects unknown identifiers and fails if any `PK-OBL-*` identifier
lacks a focused tag.

## Prelude policy registry (`PL`, 0.1.22)

Evidence labels refer to focused tests in the immutable compiler
[`c026_prelude_policy_test.exs`](https://github.com/pcharbon70/catena/blob/484d797a33eaf580f2c43ddd0776c6675078c4f9/test/catena/c026_prelude_policy_test.exs)
and its
[`c026_traceability_coverage_test.exs`](https://github.com/pcharbon70/catena/blob/484d797a33eaf580f2c43ddd0776c6675078c4f9/test/catena/c026_traceability_coverage_test.exs)
gate:

- **c026 #1** *keeps 0.1.22 exact selection with every predecessor default pinned and the lifecycle registered*
- **c026 #2** *enforces the one-selection rule with absent/null equivalence and zero-export preludes*
- **c026 #3** *rejects malformed selections as `PRE001` with the offending shape*
- **c026 #4** *admits the resolved prelude as an ordinary import origin, reusing `PKG004`/`PKG003`*
- **c026 #5** *resolves, locks, and replays the prelude as an ordinary dependency with marked requirers and bundle digest*
- **c026 #6** *executes unchanged C021 precedence with `NSP004` collisions naming both origins*
- **c026 #7** *makes absent/null the complete opt-out*
- **c026 #8** *guarantees zero implicit names for edition 0.1*
- **c026 #9** *emits stable diagnostics with unchanged reused identities*
- **c026 #10** *keeps the wiring deterministic, source-only, and outside G101/G121*

| ID | Obligation | Normative anchor | Evidence | Status |
| --- | --- | --- | --- | --- |
| PL-OBL-001 | Apply prelude behavior only at exact 0.1.22 and register the stable lifecycle addition | [`diagnostics-and-conformance.md#revision-and-persistence-separation`](../60-specification/prelude-policy/diagnostics-and-conformance.md#revision-and-persistence-separation) | c026 #1; EDN001 | traced |
| PL-OBL-002 | Enforce the one-selection rule with absent/`null` equivalence and zero-export packages admitted | [`prelude-selection-and-admission.md#the-prelude-field`](../60-specification/prelude-policy/prelude-selection-and-admission.md#the-prelude-field) | c026 #2 | traced |
| PL-OBL-003 | Reject malformed selections as `PRE001` with the offending shape | [`prelude-selection-and-admission.md#the-prelude-field`](../60-specification/prelude-policy/prelude-selection-and-admission.md#the-prelude-field) | c026 #3; PRE001 | traced |
| PL-OBL-004 | Admit the resolved prelude as an ordinary import-class origin under C022 validation, reusing `PKG004`/`PKG003` | [`prelude-selection-and-admission.md#admission-as-an-origin`](../60-specification/prelude-policy/prelude-selection-and-admission.md#admission-as-an-origin) | c026 #4 | traced |
| PL-OBL-005 | Resolve, lock, and replay the prelude selection as an ordinary dependency with marked requirers and bundle digest | [`prelude-selection-and-admission.md#admission-as-an-origin`](../60-specification/prelude-policy/prelude-selection-and-admission.md#admission-as-an-origin) | c026 #5 | traced |
| PL-OBL-006 | Execute unchanged C021 precedence: locals win; prelude-import collisions reject as `NSP004` naming both origins; no tier exists | [`shadowing-optout-and-edition-guarantee.md#precedence`](../60-specification/prelude-policy/shadowing-optout-and-edition-guarantee.md#precedence) | c026 #6; NSP004 | traced |
| PL-OBL-007 | Make absent/`null` the complete opt-out: no origin, no qualification, no suggestion | [`shadowing-optout-and-edition-guarantee.md#opt-out`](../60-specification/prelude-policy/shadowing-optout-and-edition-guarantee.md#opt-out) | c026 #7 | traced |
| PL-OBL-008 | Guarantee zero implicit names for edition 0.1 and require a lifecycle record for any future default | [`shadowing-optout-and-edition-guarantee.md#the-edition-guarantee`](../60-specification/prelude-policy/shadowing-optout-and-edition-guarantee.md#the-edition-guarantee) | c026 #8 | traced |
| PL-OBL-009 | Emit stable diagnostics: `PRE001` plus the reused families with unchanged identities | [`diagnostics-and-conformance.md#stable-diagnostics`](../60-specification/prelude-policy/diagnostics-and-conformance.md#stable-diagnostics) | c026 #9 | traced |
| PL-OBL-010 | Keep the wiring deterministic, source-only, and outside G101/G121 phases | [`diagnostics-and-conformance.md#abstract-public-boundaries`](../60-specification/prelude-policy/diagnostics-and-conformance.md#abstract-public-boundaries) | c026 #1, #10 | traced |

C026 coverage is 10 `traced` and 0 untraced obligations. The dedicated
gate rejects unknown identifiers and fails if any `PL-OBL-*` identifier
lacks a focused tag.

## Entry points registry (`EN`, 0.1.23)

Evidence labels refer to focused tests in the immutable compiler
[`c027_entry_points_test.exs`](https://github.com/pcharbon70/catena/blob/cd0e5c543ee7ddb7ca840c6657451e3b6c21d7c5/test/catena/c027_entry_points_test.exs)
and its
[`c027_traceability_coverage_test.exs`](https://github.com/pcharbon70/catena/blob/cd0e5c543ee7ddb7ca840c6657451e3b6c21d7c5/test/catena/c027_traceability_coverage_test.exs)
gate:

- **c027 #1** *keeps 0.1.23 exact selection with every predecessor default pinned and the lifecycle registered*
- **c027 #2** *accepts the optional `entries` array with the entry object grammar and optional `launch: true`*
- **c027 #3** *rejects every malformed entry declaration as `ENT001` with the offending shape*
- **c027 #4** *derives libraries from zero declared entries with absent/`null`/`[]` equivalence and no kind flag*
- **c027 #5** *enforces at most one launch marker and launches any declared entry by name*
- **c027 #6** *launches by invoking the entry's function to completion under unchanged kernel semantics*
- **c027 #7** *reports completed-with-value or failed-with-trap — return-is-shutdown*
- **c027 #8** *rejects a launch naming an undeclared entry as `ENT002`*
- **c027 #9** *emits stable diagnostics with unchanged reused identities*
- **c027 #10** *keeps the wiring deterministic, source-only, and outside G084/G121 machinery*

Anchors point at the normative 0.1.23 chapters; `EN-OBL-*` obligations
are fully traced against the immutable compiler commit.

| ID | Obligation | Normative anchor | Evidence | Status |
| --- | --- | --- | --- | --- |
| EN-OBL-001 | Apply entry behavior only at exact 0.1.23 and register the stable lifecycle addition | [`diagnostics-and-conformance.md#revision-and-persistence-separation`](../60-specification/entry-points/diagnostics-and-conformance.md#revision-and-persistence-separation) | c027 #1; EDN001 | traced |
| EN-OBL-002 | Accept the optional `entries` array with the entry object grammar and optional `launch: true` | [`entry-declarations.md#the-entries-field`](../60-specification/entry-points/entry-declarations.md#the-entries-field) | c027 #2 | traced |
| EN-OBL-003 | Reject every malformed entry declaration as `ENT001` with the offending shape | [`entry-declarations.md#entry-validity`](../60-specification/entry-points/entry-declarations.md#entry-validity) | c027 #3; ENT001 | traced |
| EN-OBL-004 | Derive libraries from zero declared entries with absent/`null`/`[]` equivalence and no kind flag | [`entry-declarations.md#libraries-and-executables`](../60-specification/entry-points/entry-declarations.md#libraries-and-executables) | c027 #4 | traced |
| EN-OBL-005 | Enforce at most one launch marker and allow launching any declared entry by name | [`entry-declarations.md#libraries-and-executables`](../60-specification/entry-points/entry-declarations.md#libraries-and-executables) | c027 #5 | traced |
| EN-OBL-006 | Launch by invoking the entry's function to completion under unchanged strict kernel semantics, introducing no scope or process | [`startup-and-shutdown.md#launch`](../60-specification/entry-points/startup-and-shutdown.md#launch) | c027 #6 | traced |
| EN-OBL-007 | Report completed-with-value or failed-with-trap: return-is-shutdown with the trap identity | [`startup-and-shutdown.md#return-is-shutdown`](../60-specification/entry-points/startup-and-shutdown.md#return-is-shutdown) | c027 #7; ENT003 | traced |
| EN-OBL-008 | Reject a launch naming an undeclared entry as `ENT002` | [`startup-and-shutdown.md#launch`](../60-specification/entry-points/startup-and-shutdown.md#launch) | c027 #8; ENT002 | traced |
| EN-OBL-009 | Emit stable diagnostics: `ENT001`–`ENT003` plus the reused families with unchanged identities | [`diagnostics-and-conformance.md#stable-diagnostics`](../60-specification/entry-points/diagnostics-and-conformance.md#stable-diagnostics) | c027 #9 | traced |
| EN-OBL-010 | Keep the wiring deterministic, source-only, and outside G084/G088/G121 machinery, with compilation roots unchanged | [`diagnostics-and-conformance.md#abstract-public-boundaries`](../60-specification/entry-points/diagnostics-and-conformance.md#abstract-public-boundaries) | c027 #1, #10 | traced |

C027 coverage is 10 `traced` and 0 untraced obligations. The dedicated
gate rejects unknown identifiers and fails if any `EN-OBL-*` identifier
lacks a focused tag.

## API and ABI compatibility registry (`CP`, 0.1.24)

Evidence labels refer to focused tests in the immutable compiler
[`c028_api_compat_test.exs`](https://github.com/pcharbon70/catena/blob/0d96f96792aa161ed2711edb304d75e4cee54af2/test/catena/c028_api_compat_test.exs)
and its
[`c028_traceability_coverage_test.exs`](https://github.com/pcharbon70/catena/blob/0d96f96792aa161ed2711edb304d75e4cee54af2/test/catena/c028_traceability_coverage_test.exs)
gate:

- **c028 #1** *keeps 0.1.24 exact selection with every predecessor default pinned and the lifecycle registered*
- **c028 #2** *fixes one stance per layer with the two declared absences*
- **c028 #3** *keeps retained revisions immutable with pinned predecessor selections*
- **c028 #4** *classifies every matrix row from decoded interfaces with itemized reasons*
- **c028 #5** *enforces version claims: 1.0+ major-as-breaking, 0.x minor-as-breaking, with `CMP001` under-claims*
- **c028 #6** *reports unclassifiable drift as `CMP003` and malformed input as `CMP002`*
- **c028 #7** *resolves the C022–C027 deferrals: facade exclusion, digest identity, lock skew, prelude bumps, entry rows*
- **c028 #8** *keeps representation changes and digest recomputation never breaking alone*
- **c028 #9** *emits stable diagnostics with unchanged reused identities*
- **c028 #10** *keeps the classifier deterministic, interface-only, and outside behavior/ABI/migration claims*

Anchors point at the normative 0.1.24 chapters; `CP-OBL-*` obligations
are fully traced against the immutable compiler commit.

| ID | Obligation | Normative anchor | Evidence | Status |
| --- | --- | --- | --- | --- |
| CP-OBL-001 | Apply compatibility behavior only at exact 0.1.24 and register the stable lifecycle addition | [`diagnostics-and-conformance.md#revision-and-persistence-separation`](../60-specification/api-and-abi-compatibility/diagnostics-and-conformance.md#revision-and-persistence-separation) | c028 #1; EDN001 | traced |
| CP-OBL-002 | Fix one stance per layer: source rules, interface matrix, behavior absence, ABI absence | [`compatibility-layers-and-versions.md#the-four-layers`](../60-specification/api-and-abi-compatibility/compatibility-layers-and-versions.md#the-four-layers) | c028 #2 | traced |
| CP-OBL-003 | Keep retained revisions immutable with cumulative-forward acceptance | [`compatibility-layers-and-versions.md#the-four-layers`](../60-specification/api-and-abi-compatibility/compatibility-layers-and-versions.md#the-four-layers) | c028 #1, #3 | traced |
| CP-OBL-004 | Classify every matrix row correctly from decoded interfaces with itemized reasons | [`breaking-change-matrix.md#the-matrix`](../60-specification/api-and-abi-compatibility/breaking-change-matrix.md#the-matrix) | c028 #4 | traced |
| CP-OBL-005 | Enforce version-meaning claims: major-as-breaking at 1.0+, minor-as-breaking under 0.x, with `CMP001` under-claims | [`compatibility-layers-and-versions.md#version-increment-meanings`](../60-specification/api-and-abi-compatibility/compatibility-layers-and-versions.md#version-increment-meanings) | c028 #5; CMP001 | traced |
| CP-OBL-006 | Report unclassifiable drift as `CMP003` and malformed input as `CMP002`, never guessing | [`breaking-change-matrix.md#the-matrix`](../60-specification/api-and-abi-compatibility/breaking-change-matrix.md#the-matrix) | c028 #6; CMP002, CMP003 | traced |
| CP-OBL-007 | Resolve the C022–C027 deferrals: facade exclusion, digest identity-only, lock-replay skew, prelude-bump classification, entry-set rows | [`breaking-change-matrix.md#deferral-resolutions`](../60-specification/api-and-abi-compatibility/breaking-change-matrix.md#deferral-resolutions) | c028 #7 | traced |
| CP-OBL-008 | Keep representation changes, digest recomputation, and warning additions never breaking alone | [`compatibility-layers-and-versions.md#what-versions-do-not-carry`](../60-specification/api-and-abi-compatibility/compatibility-layers-and-versions.md#what-versions-do-not-carry) | c028 #8 | traced |
| CP-OBL-009 | Emit stable diagnostics: `CMP001`–`CMP003` plus the reused families with unchanged identities | [`diagnostics-and-conformance.md#stable-diagnostics`](../60-specification/api-and-abi-compatibility/diagnostics-and-conformance.md#stable-diagnostics) | c028 #9 | traced |
| CP-OBL-010 | Keep the classifier deterministic, interface-only, and outside behavior/ABI/migration/tooling claims | [`diagnostics-and-conformance.md#abstract-public-boundaries`](../60-specification/api-and-abi-compatibility/diagnostics-and-conformance.md#abstract-public-boundaries) | c028 #10 | traced |

C028 coverage is 10 `traced` and 0 untraced obligations. The dedicated
gate rejects unknown identifiers and fails if any `CP-OBL-*` identifier
lacks a focused tag.

## Values and evaluation registry (`VA`, 0.1.25)

Evidence labels refer to focused tests in the immutable compiler
[`c029_values_test.exs`](https://github.com/pcharbon70/catena/blob/f8d8fa96e536df9b7ff00db246d8817f39b1c381/test/catena/c029_values_test.exs)
and its
[`c029_traceability_coverage_test.exs`](https://github.com/pcharbon70/catena/blob/f8d8fa96e536df9b7ff00db246d8817f39b1c381/test/catena/c029_traceability_coverage_test.exs)
gate:

- **c029 #1** *keeps 0.1.25 exact selection with every predecessor default pinned and the lifecycle registered*
- **c029 #2** *fixes the closed value grammar and closed non-value list with kernel rules unchanged*
- **c029 #3** *admits Float as the tenth value form with C018 semantics unchanged*
- **c029 #4** *guarantees uniform first-classness with exclusions named, not tiered*
- **c029 #5** *keeps value membership closed: no outside form classifies as a value*
- **c029 #6** *enforces the strictness invariant with the two named exceptions and value-or-trap terminals*
- **c029 #7** *gates every future lazy form behind an edition record*
- **c029 #8** *keeps classification deterministic with zero new diagnostic families*

Anchors point at the normative 0.1.25 chapters; `VA-OBL-*` obligations
are fully traced against the immutable compiler commit.

| ID | Obligation | Normative anchor | Evidence | Status |
| --- | --- | --- | --- | --- |
| VA-OBL-001 | Apply values behavior only at exact 0.1.25 and register the stable lifecycle addition | [`diagnostics-and-conformance.md#revision-and-persistence-separation`](../60-specification/values-and-evaluation/diagnostics-and-conformance.md#revision-and-persistence-separation) | c029 #1; EDN001 | traced |
| VA-OBL-002 | Fix the closed value grammar and the closed non-value list with kernel rules unchanged | [`value-forms-and-first-classness.md#the-value-grammar`](../60-specification/values-and-evaluation/value-forms-and-first-classness.md#the-value-grammar) | c029 #2 | traced |
| VA-OBL-003 | Admit Float as the tenth value form with C018 semantics unchanged | [`value-forms-and-first-classness.md#the-value-grammar`](../60-specification/values-and-evaluation/value-forms-and-first-classness.md#the-value-grammar) | c029 #3 | traced |
| VA-OBL-004 | Guarantee uniform first-classness: bindable, passable, returnable, storable, with exclusions named not tiered | [`value-forms-and-first-classness.md#first-classness`](../60-specification/values-and-evaluation/value-forms-and-first-classness.md#first-classness) | c029 #4 | traced |
| VA-OBL-005 | Keep value membership closed: no form outside the grammar classifies as a value | [`value-forms-and-first-classness.md#the-non-value-list`](../60-specification/values-and-evaluation/value-forms-and-first-classness.md#the-non-value-list) | c029 #5 | traced |
| VA-OBL-006 | Enforce the strictness invariant with the two named exceptions and the value-or-trap terminal contract | [`strictness-and-terminal-outcomes.md#the-strictness-invariant`](../60-specification/values-and-evaluation/strictness-and-terminal-outcomes.md#the-strictness-invariant) | c029 #6 | traced |
| VA-OBL-007 | Gate every future lazy or multi-evaluation form behind an edition record | [`strictness-and-terminal-outcomes.md#the-edition-record-gate`](../60-specification/values-and-evaluation/strictness-and-terminal-outcomes.md#the-edition-record-gate) | c029 #7 | traced |
| VA-OBL-008 | Keep classification deterministic and outside P035/G036/G037/P109 claims with zero new diagnostic families | [`diagnostics-and-conformance.md#abstract-public-boundaries`](../60-specification/values-and-evaluation/diagnostics-and-conformance.md#abstract-public-boundaries) | c029 #8 | traced |

C029 coverage is 8 `traced` and 0 untraced obligations. The dedicated
gate rejects unknown identifiers and fails if any `VA-OBL-*` identifier
lacks a focused tag.

## Evaluation order registry (`EO`, 0.1.26)

Evidence labels refer to focused tests in the immutable compiler
[`c030_evaluation_order_test.exs`](https://github.com/pcharbon70/catena/blob/5e1e8948249701a45029379e604b7aa0e8376e92/test/catena/c030_evaluation_order_test.exs)
and its
[`c030_traceability_coverage_test.exs`](https://github.com/pcharbon70/catena/blob/5e1e8948249701a45029379e604b7aa0e8376e92/test/catena/c030_traceability_coverage_test.exs)
gate:

- **c030 #1** *keeps 0.1.26 exact selection with every predecessor default pinned and the lifecycle registered*
- **c030 #2** *fixes one declared order for every kernel-listed form, unchanged from the kernel's rules*
- **c030 #3** *fixes the typed-core completions: curried application, trait-call order, handler installation, annotate transparency*
- **c030 #4** *keeps the C002/C003/C004/C005 fragment rules exactly as their areas fixed them*
- **c030 #5** *keeps the table closed: no outside form has a declared order*
- **c030 #6** *makes declared order observable: equal traces on the stepper and compiled BEAM*
- **c030 #7** *keeps the `and`/`or` skips as the only exceptions under the C029 gate*
- **c030 #8** *keeps the contract deterministic and definitional with zero new diagnostic families*

Anchors point at the normative 0.1.26 chapters; `EO-OBL-*` obligations
are fully traced against the immutable compiler commit.

| ID | Obligation | Normative anchor | Evidence | Status |
| --- | --- | --- | --- | --- |
| EO-OBL-001 | Apply order behavior only at exact 0.1.26 and register the stable lifecycle addition | [`diagnostics-and-conformance.md#revision-and-persistence-separation`](../60-specification/evaluation-order/diagnostics-and-conformance.md#revision-and-persistence-separation) | c030 #1; EDN001 | traced |
| EO-OBL-002 | Fix one declared order for every kernel-listed form, unchanged from the kernel's rules | [`ordered-forms-and-entry-rule.md#the-ordered-forms-table`](../60-specification/evaluation-order/ordered-forms-and-entry-rule.md#the-ordered-forms-table) | c030 #2 | traced |
| EO-OBL-003 | Fix the typed-core completions: curried application, trait-call subject-then-arguments, handler installation, annotate transparency | [`ordered-forms-and-entry-rule.md#typed-core-completions`](../60-specification/evaluation-order/ordered-forms-and-entry-rule.md#typed-core-completions) | c030 #3 | traced |
| EO-OBL-004 | Keep the C002/C003/C004/C005 fragment rules exactly as their areas fixed them | [`ordered-forms-and-entry-rule.md#the-ordered-forms-table`](../60-specification/evaluation-order/ordered-forms-and-entry-rule.md#the-ordered-forms-table) | c030 #4 | traced |
| EO-OBL-005 | Keep the table closed: no form outside it has a declared order; future forms enter with their own entry | [`ordered-forms-and-entry-rule.md#the-entry-rule`](../60-specification/evaluation-order/ordered-forms-and-entry-rule.md#the-entry-rule) | c030 #5 | traced |
| EO-OBL-006 | Make declared order observable: equal effect-request traces on the stepper and compiled BEAM for the same program | [`observability-and-trace-agreement.md#order-is-observable-semantics`](../60-specification/evaluation-order/observability-and-trace-agreement.md#order-is-observable-semantics) | c030 #6 | traced |
| EO-OBL-007 | Keep the `and`/`or` skips as the only exceptions, under the C029 edition-record gate | [`ordered-forms-and-entry-rule.md#the-ordered-forms-table`](../60-specification/evaluation-order/ordered-forms-and-entry-rule.md#the-ordered-forms-table) | c030 #7 | traced |
| EO-OBL-008 | Keep the contract deterministic, definitional, and outside G031–G033/G040/G088/P109 claims with zero new diagnostic families | [`diagnostics-and-conformance.md#abstract-public-boundaries`](../60-specification/evaluation-order/diagnostics-and-conformance.md#abstract-public-boundaries) | c030 #8 | traced |

C030 coverage is 8 `traced` and 0 untraced obligations. The dedicated
gate rejects unknown identifiers and fails if any `EO-OBL-*` identifier
lacks a focused tag.

## Bindings and sequencing registry (`BS`, 0.1.27)

Evidence labels refer to focused tests in the immutable compiler
[`c031_bindings_test.exs`](https://github.com/pcharbon70/catena/blob/17b5be7b1bce9cd6a4603b9d6b6f5f5d8060951b/test/catena/c031_bindings_test.exs)
and its
[`c031_traceability_coverage_test.exs`](https://github.com/pcharbon70/catena/blob/17b5be7b1bce9cd6a4603b9d6b6f5f5d8060951b/test/catena/c031_traceability_coverage_test.exs)
gate:

- **c031 #1** *keeps 0.1.27 exact selection with every predecessor default pinned and the lifecycle registered*
- **c031 #2** *keeps local bindings strictly non-recursive: a self-referential RHS is `T001`*
- **c031 #3** *enforces sequential-lexical scope with silent innermost-wins shadowing*
- **c031 #4** *keeps recursion definitions-only with C024's SCC as mutual recursion's home*
- **c031 #5** *keeps unused bindings valid with RHS effects preserved on every target*
- **c031 #6** *emits `BS001` exactly on non-`_`-prefixed unused binders with deny promotion*
- **c031 #7** *fixes the let idiom as sequencing: first to a value with effects, discard, then second*
- **c031 #8** *keeps the contract deterministic and outside G032/G033/P034/P109 claims*

Anchors point at the normative 0.1.27 chapters; `BS-OBL-*` obligations
are fully traced against the immutable compiler commit.

| ID | Obligation | Normative anchor | Evidence | Status |
| --- | --- | --- | --- | --- |
| BS-OBL-001 | Apply bindings behavior only at exact 0.1.27 and register the stable lifecycle addition | [`diagnostics-and-conformance.md#revision-and-persistence-separation`](../60-specification/bindings-and-sequencing/diagnostics-and-conformance.md#revision-and-persistence-separation) | c031 #1; EDN001 | traced |
| BS-OBL-002 | Keep local bindings strictly non-recursive: an RHS referencing its own binder is `T001` unbound | [`binding-structure-and-scope.md#local-binding-structure`](../60-specification/bindings-and-sequencing/binding-structure-and-scope.md#local-binding-structure) | c031 #2; T001 | traced |
| BS-OBL-003 | Enforce sequential-lexical scope with silent innermost-wins shadowing of any in-scope name | [`binding-structure-and-scope.md#scope-and-shadowing`](../60-specification/bindings-and-sequencing/binding-structure-and-scope.md#scope-and-shadowing) | c031 #3 | traced |
| BS-OBL-004 | Keep recursion definitions-only with C024's SCC as mutual recursion's home | [`binding-structure-and-scope.md#the-recursion-boundary`](../60-specification/bindings-and-sequencing/binding-structure-and-scope.md#the-recursion-boundary) | c031 #4 | traced |
| BS-OBL-005 | Keep unused bindings valid with RHS effects preserved on every target | [`unused-bindings-and-sequencing.md#unused-bindings-are-valid`](../60-specification/bindings-and-sequencing/unused-bindings-and-sequencing.md#unused-bindings-are-valid) | c031 #5 | traced |
| BS-OBL-006 | Emit `BS001` exactly on non-`_`-prefixed unused binders with deny promotion | [`unused-bindings-and-sequencing.md#the-bs001-warning`](../60-specification/bindings-and-sequencing/unused-bindings-and-sequencing.md#the-bs001-warning) | c031 #6; BS001 | traced |
| BS-OBL-007 | Fix the let idiom as sequencing: first to a value with effects, discard, then second | [`unused-bindings-and-sequencing.md#the-sequencing-idiom`](../60-specification/bindings-and-sequencing/unused-bindings-and-sequencing.md#the-sequencing-idiom) | c031 #7 | traced |
| BS-OBL-008 | Keep the contract deterministic and outside G032/G033/P034/P109 claims | [`diagnostics-and-conformance.md#abstract-public-boundaries`](../60-specification/bindings-and-sequencing/diagnostics-and-conformance.md#abstract-public-boundaries) | c031 #8 | traced |

C031 coverage is 8 `traced` and 0 untraced obligations. The dedicated
gate rejects unknown identifiers and fails if any `BS-OBL-*` identifier
lacks a focused tag.

## Functions and calls registry (`FC`, 0.1.28)

Evidence labels refer to focused tests in the immutable compiler
[`c032_functions_test.exs`](https://github.com/pcharbon70/catena/blob/0af785cf32de1893c9638ebd145944bdc37f52b3/test/catena/c032_functions_test.exs)
and its
[`c032_traceability_coverage_test.exs`](https://github.com/pcharbon70/catena/blob/0af785cf32de1893c9638ebd145944bdc37f52b3/test/catena/c032_traceability_coverage_test.exs)
gate:

- **c032 #1** *keeps 0.1.28 exact selection with every predecessor default pinned and the lifecycle registered*
- **c032 #2** *fixes the semantic-unary model with multi-parameter desugaring and no arity diagnostics*
- **c032 #3** *makes any prefix application a value: free partial application, callable on both targets*
- **c032 #4** *enforces lexical immutable capture: two applications observe the same captured values*
- **c032 #5** *makes the let-bound closure the local-function form under C031's rules*
- **c032 #6** *keeps the proper-tail-call guarantee: deep BEAM recursion completes, stepper terminates*
- **c032 #7** *keeps named functions as definitions with C031's recursion environment and C022's exports*
- **c032 #8** *keeps the model deterministic and outside G033/P034/G037/G094/P109 claims with zero new families*

Anchors point at the normative 0.1.28 chapters; `FC-OBL-*` obligations
are fully traced against the immutable compiler commit.

| ID | Obligation | Normative anchor | Evidence | Status |
| --- | --- | --- | --- | --- |
| FC-OBL-001 | Apply function-model behavior only at exact 0.1.28 and register the stable lifecycle addition | [`diagnostics-and-conformance.md#revision-and-persistence-separation`](../60-specification/functions-and-calls/diagnostics-and-conformance.md#revision-and-persistence-separation) | c032 #1; EDN001 | traced |
| FC-OBL-002 | Fix the semantic-unary model: multi-parameter desugaring and repeated unary application with no arity diagnostics | [`arity-and-application.md#the-semantic-unary-model`](../60-specification/functions-and-calls/arity-and-application.md#the-semantic-unary-model) | c032 #2 | traced |
| FC-OBL-003 | Make any prefix application a value: free partial application, first-class and callable | [`arity-and-application.md#partial-application`](../60-specification/functions-and-calls/arity-and-application.md#partial-application) | c032 #3 | traced |
| FC-OBL-004 | Enforce lexical immutable capture: two applications observe the same captured values | [`closures-and-tail-calls.md#closure-capture`](../60-specification/functions-and-calls/closures-and-tail-calls.md#closure-capture) | c032 #4 | traced |
| FC-OBL-005 | Make the let-bound closure the local-function form under all of C031's rules | [`closures-and-tail-calls.md#the-local-function-form`](../60-specification/functions-and-calls/closures-and-tail-calls.md#the-local-function-form) | c032 #5 | traced |
| FC-OBL-006 | Keep the proper-tail-call guarantee: deep tail recursion completes without unbounded stack growth | [`closures-and-tail-calls.md#proper-tail-calls`](../60-specification/functions-and-calls/closures-and-tail-calls.md#proper-tail-calls) | c032 #6 | traced |
| FC-OBL-007 | Keep named functions as definitions with C031's recursion environment and C022's export rules | [`arity-and-application.md#named-and-anonymous-functions`](../60-specification/functions-and-calls/arity-and-application.md#named-and-anonymous-functions) | c032 #7 | traced |
| FC-OBL-008 | Keep the model deterministic and outside G033/P034/G037/G094/P109 claims with zero new diagnostic families | [`diagnostics-and-conformance.md#abstract-public-boundaries`](../60-specification/functions-and-calls/diagnostics-and-conformance.md#abstract-public-boundaries) | c032 #8 | traced |

C032 coverage is 8 `traced` and 0 untraced obligations. The dedicated
gate rejects unknown identifiers and fails if any `FC-OBL-*` identifier
lacks a focused tag.

## Branching registry (`BR`, 0.1.29)

Evidence labels refer to focused tests in the immutable compiler
[`c033_branching_test.exs`](https://github.com/pcharbon70/catena/blob/221338face094ad9c9306dcf8805a75910b1d1d7/test/catena/c033_branching_test.exs)
and its
[`c033_traceability_coverage_test.exs`](https://github.com/pcharbon70/catena/blob/221338face094ad9c9306dcf8805a75910b1d1d7/test/catena/c033_traceability_coverage_test.exs)
gate:

- **c033 #1** *keeps 0.1.29 exact selection with every predecessor default pinned and the lifecycle registered*
- **c033 #2** *keeps match the single branch form with no other form on any retained input*
- **c033 #3** *fixes the conditional sugar promise: Bool-pattern match desugaring with exhaustive dispatch*
- **c033 #4** *keeps every consolidated rule exactly as its citing area fixed it*
- **c033 #5** *keeps statement-like control forms absent, gated behind edition records*
- **c033 #6** *preserves commitment irreversibility: only the selected body's effects are observable*
- **c033 #7** *preserves condition fallthrough: a false condition continues with later clauses*
- **c033 #8** *keeps the contract deterministic and outside P034/G036/G040/P109/G088 claims with zero new families*

Anchors point at the normative 0.1.29 chapters; `BR-OBL-*` obligations
are fully traced against the immutable compiler commit.

| ID | Obligation | Normative anchor | Evidence | Status |
| --- | --- | --- | --- | --- |
| BR-OBL-001 | Apply branching behavior only at exact 0.1.29 and register the stable lifecycle addition | [`diagnostics-and-conformance.md#revision-and-persistence-separation`](../60-specification/branching/diagnostics-and-conformance.md#revision-and-persistence-separation) | c033 #1; EDN001 | traced |
| BR-OBL-002 | Keep match the single branch form with no other form existing on any retained input | [`the-branch-form-and-its-desugaring.md#match-is-the-only-branch-form`](../60-specification/branching/the-branch-form-and-its-desugaring.md#match-is-the-only-branch-form) | c033 #2 | traced |
| BR-OBL-003 | Fix the conditional sugar promise: Bool-pattern match desugaring, `true`/`false` exhaustive dispatch | [`the-branch-form-and-its-desugaring.md#the-conditional-sugar-promise`](../60-specification/branching/the-branch-form-and-its-desugaring.md#the-conditional-sugar-promise) | c033 #3 | traced |
| BR-OBL-004 | Keep every consolidated rule exactly as its citing area fixed it | [`branch-rules-consolidated.md#the-consolidated-rules`](../60-specification/branching/branch-rules-consolidated.md#the-consolidated-rules) | c033 #4 | traced |
| BR-OBL-005 | Keep statement-like control forms absent, sequenced through the let idiom, gated behind edition records | [`branch-rules-consolidated.md#statement-like-control-forms`](../60-specification/branching/branch-rules-consolidated.md#statement-like-control-forms) | c033 #5 | traced |
| BR-OBL-006 | Preserve commitment irreversibility: only the selected body's effects are observable | [`branch-rules-consolidated.md#the-consolidated-rules`](../60-specification/branching/branch-rules-consolidated.md#the-consolidated-rules) | c033 #6 | traced |
| BR-OBL-007 | Preserve condition fallthrough: a false condition continues with later clauses | [`branch-rules-consolidated.md#the-consolidated-rules`](../60-specification/branching/branch-rules-consolidated.md#the-consolidated-rules) | c033 #7 | traced |
| BR-OBL-008 | Keep the contract deterministic and outside P034/G036/G040/P109/G088 claims with zero new diagnostic families | [`diagnostics-and-conformance.md#abstract-public-boundaries`](../60-specification/branching/diagnostics-and-conformance.md#abstract-public-boundaries) | c033 #8 | traced |

C033 coverage is 8 `traced` and 0 untraced obligations. The dedicated
gate rejects unknown identifiers and fails if any `BR-OBL-*` identifier
lacks a focused tag.

## Equality and ordering registry (`EQ`, 0.1.30)

Evidence labels refer to focused tests in the immutable compiler
[`c035_equality_test.exs`](https://github.com/pcharbon70/catena/blob/91c4d4929ea2fef316e44d3b1500a8854715b9be/test/catena/c035_equality_test.exs)
and its
[`c035_traceability_coverage_test.exs`](https://github.com/pcharbon70/catena/blob/91c4d4929ea2fef316e44d3b1500a8854715b9be/test/catena/c035_traceability_coverage_test.exs)
gate:

- **c035 #1** *keeps 0.1.30 exact selection with every predecessor default pinned and the lifecycle registered*
- **c035 #2** *fixes the comparable set with structural recursion and bit-exact float equality (`−0.0 ≠ 0.0`)*
- **c035 #3** *fixes the orderable set (Int, Float) with total float ordering (`−0.0 < 0.0`)*
- **c035 #4** *rejects closure, handle, and containing-composite comparisons as `EQN001`*
- **c035 #5** *keeps comparison monomorphic: mixed Int/Float is the existing type error*
- **c035 #6** *keeps the sets closed: no outside type compares*
- **c035 #7** *keeps the guard fragment frozen: guards reject Float comparisons via C003's families*
- **c035 #8** *keeps comparison deterministic and outside G036/G037/G040/G061/P109 claims, reusing existing families*

Anchors point at the normative 0.1.30 chapters; `EQ-OBL-*` obligations
are fully traced against the immutable compiler commit.

| ID | Obligation | Normative anchor | Evidence | Status |
| --- | --- | --- | --- | --- |
| EQ-OBL-001 | Apply equality behavior only at exact 0.1.30 and register the stable lifecycle addition | [`diagnostics-and-conformance.md#revision-and-persistence-separation`](../60-specification/equality-and-ordering/diagnostics-and-conformance.md#revision-and-persistence-separation) | c035 #1; EDN001 | traced |
| EQ-OBL-002 | Fix the comparable set with structural recursion and bit-exact float equality (`−0.0 ≠ 0.0`) | [`the-comparable-set.md#the-comparable-and-orderable-domains`](../60-specification/equality-and-ordering/the-comparable-set.md#the-comparable-and-orderable-domains) | c035 #2 | traced |
| EQ-OBL-003 | Fix the orderable set (Int, Float) with total float ordering (`−0.0 < 0.0`) | [`float-equality-and-semantics.md#total-ordering`](../60-specification/equality-and-ordering/float-equality-and-semantics.md#total-ordering) | c035 #3 | traced |
| EQ-OBL-004 | Reject closure, handle, and containing-composite comparisons as `EQN001` | [`the-comparable-set.md#the-exclusion-list`](../60-specification/equality-and-ordering/the-comparable-set.md#the-exclusion-list) | c035 #4; EQN001 | traced |
| EQ-OBL-005 | Keep comparison monomorphic: mixed Int/Float is the existing type error | [`the-comparable-set.md#monomorphism`](../60-specification/equality-and-ordering/the-comparable-set.md#monomorphism) | c035 #5 | traced |
| EQ-OBL-006 | Keep the sets closed: no outside type compares; future types enter with their own entry | [`the-comparable-set.md#the-entry-rule`](../60-specification/equality-and-ordering/the-comparable-set.md#the-entry-rule) | c035 #6 | traced |
| EQ-OBL-007 | Keep the guard fragment frozen: guards reject Float comparisons via C003's families; general expressions admit them | [`the-comparable-set.md#the-guard-split`](../60-specification/equality-and-ordering/the-comparable-set.md#the-guard-split) | c035 #7 | traced |
| EQ-OBL-008 | Keep comparison deterministic and outside G036/G037/G040/G061/P109 claims, reusing existing families | [`diagnostics-and-conformance.md#abstract-public-boundaries`](../60-specification/equality-and-ordering/diagnostics-and-conformance.md#abstract-public-boundaries) | c035 #8 | traced |

C035 coverage is 8 `traced` and 0 untraced obligations. The dedicated
gate rejects unknown identifiers and fails if any `EQ-OBL-*` identifier
lacks a focused tag.

## Recursion and termination registry (`RT`, 0.1.31)

Evidence labels refer to focused tests in the immutable compiler
[`c034_recursion_test.exs`](https://github.com/pcharbon70/catena/blob/252da7b287dfbfae95056fa778e0b7ce0979599f/test/catena/c034_recursion_test.exs)
and its
[`c034_traceability_coverage_test.exs`](https://github.com/pcharbon70/catena/blob/252da7b287dfbfae95056fa778e0b7ce0979599f/test/catena/c034_traceability_coverage_test.exs)
gate:

- **c034 #1** *keeps 0.1.31 exact selection with every predecessor default pinned and the lifecycle registered*
- **c034 #2** *keeps program recursion unrestricted: non-tail recursion runs and completes alongside tail recursion*
- **c034 #3** *keeps divergence non-termination: budget exhaustion on the stepper, never a trap diagnostic*
- **c034 #4** *keeps totality checking absent: no validity gate on recursion*
- **c034 #5** *keeps every meta-level evaluator total-or-bounded per its cited regime*
- **c034 #6** *enforces the entry rule: no unbounded meta-level evaluator may be claimed*
- **c034 #7** *keeps recursive conditions rejecting as `CND004` unchanged*
- **c034 #8** *keeps the classification deterministic and outside G036/G038/G084/G088/P109 claims with zero new families*

Anchors point at the normative 0.1.31 chapters; `RT-OBL-*` obligations
are fully traced against the immutable compiler commit.

| ID | Obligation | Normative anchor | Evidence | Status |
| --- | --- | --- | --- | --- |
| RT-OBL-001 | Apply recursion behavior only at exact 0.1.31 and register the stable lifecycle addition | [`diagnostics-and-conformance.md#revision-and-persistence-separation`](../60-specification/recursion-and-termination/diagnostics-and-conformance.md#revision-and-persistence-separation) | c034 #1; EDN001 | traced |
| RT-OBL-002 | Keep program recursion unrestricted: non-tail recursion runs and completes alongside tail recursion | [`program-recursion-is-unrestricted.md#the-stance`](../60-specification/recursion-and-termination/program-recursion-is-unrestricted.md#the-stance) | c034 #2 | traced |
| RT-OBL-003 | Keep divergence non-termination: budget exhaustion on the stepper, never a trap diagnostic | [`program-recursion-is-unrestricted.md#the-stance`](../60-specification/recursion-and-termination/program-recursion-is-unrestricted.md#the-stance) | c034 #3 | traced |
| RT-OBL-004 | Keep totality checking absent: no validity gate on recursion, analysis-only through the edition gate | [`program-recursion-is-unrestricted.md#the-stance`](../60-specification/recursion-and-termination/program-recursion-is-unrestricted.md#the-stance) | c034 #4 | traced |
| RT-OBL-005 | Keep every meta-level evaluator total-or-bounded per its cited regime | [`the-separation-table.md#the-separation`](../60-specification/recursion-and-termination/the-separation-table.md#the-separation) | c034 #5 | traced |
| RT-OBL-006 | Enforce the entry rule: no unbounded meta-level evaluator may be claimed | [`the-separation-table.md#the-entry-rule`](../60-specification/recursion-and-termination/the-separation-table.md#the-entry-rule) | c034 #6 | traced |
| RT-OBL-007 | Keep recursive conditions rejecting as `CND004` unchanged | [`the-separation-table.md#the-separation`](../60-specification/recursion-and-termination/the-separation-table.md#the-separation) | c034 #7; CND004 | traced |
| RT-OBL-008 | Keep the classification deterministic and outside G036/G038/G084/G088/P109 claims with zero new families | [`diagnostics-and-conformance.md#abstract-public-boundaries`](../60-specification/recursion-and-termination/diagnostics-and-conformance.md#abstract-public-boundaries) | c034 #8 | traced |

C034 coverage is 8 `traced` and 0 untraced obligations. The dedicated
gate rejects unknown identifiers and fails if any `RT-OBL-*` identifier
lacks a focused tag.

## Runtime failure taxonomy registry (`FT`, 0.1.32)

Evidence labels refer to focused tests in the immutable compiler
[`c036_failure_test.exs`](https://github.com/pcharbon70/catena/blob/22c6a437f483f5a2bb94627d3481fb51e2ce04ba/test/catena/c036_failure_test.exs)
and its
[`c036_traceability_coverage_test.exs`](https://github.com/pcharbon70/catena/blob/22c6a437f483f5a2bb94627d3481fb51e2ce04ba/test/catena/c036_traceability_coverage_test.exs)
gate:

- **c036 #1** *keeps 0.1.32 exact selection with every predecessor default pinned and the lifecycle registered*
- **c036 #2** *keeps `trap(reason)` the single runtime failure outcome with the three-way partition*
- **c036 #3** *keeps trap observability kernel-verbatim: mailbox discarded, no exit signal, no spawner effect*
- **c036 #4** *keeps trap reason identity stable and agreeing across evaluator and BEAM*
- **c036 #5** *keeps the six-category mapping exactly as classified*
- **c036 #6** *enforces the entry rule: no unclassified failure kind, no second outcome class*
- **c036 #7** *keeps typed failure classified as values, not failures*
- **c036 #8** *keeps the taxonomy deterministic and outside G084/G088/G092/G095/G105/P109 claims with zero new families*

Anchors point at the normative 0.1.32 chapters; `FT-OBL-*` obligations
are fully traced against the immutable compiler commit.

| ID | Obligation | Normative anchor | Evidence | Status |
| --- | --- | --- | --- | --- |
| FT-OBL-001 | Apply failure behavior only at exact 0.1.32 and register the stable lifecycle addition | [`diagnostics-and-conformance.md#revision-and-persistence-separation`](../60-specification/runtime-failure-taxonomy/diagnostics-and-conformance.md#revision-and-persistence-separation) | c036 #1; EDN001 | traced |
| FT-OBL-002 | Keep `trap(reason)` the single runtime failure outcome with the three-way partition stated | [`the-single-outcome.md#the-one-outcome`](../60-specification/runtime-failure-taxonomy/the-single-outcome.md#the-one-outcome) | c036 #2 | traced |
| FT-OBL-003 | Keep trap observability kernel-verbatim: mailbox discarded, no exit signal, no spawner effect, uninterceptable | [`the-single-outcome.md#trap-observability`](../60-specification/runtime-failure-taxonomy/the-single-outcome.md#trap-observability) | c036 #3 | traced |
| FT-OBL-004 | Keep trap reason identity stable and agreeing across evaluator and BEAM | [`the-single-outcome.md#reason-identity`](../60-specification/runtime-failure-taxonomy/the-single-outcome.md#reason-identity) | c036 #4 | traced |
| FT-OBL-005 | Keep the six-category mapping exactly as classified | [`the-six-categories.md#the-mapping`](../60-specification/runtime-failure-taxonomy/the-six-categories.md#the-mapping) | c036 #5 | traced |
| FT-OBL-006 | Enforce the entry rule: no unclassified failure kind, no second outcome class | [`the-six-categories.md#the-entry-rule`](../60-specification/runtime-failure-taxonomy/the-six-categories.md#the-entry-rule) | c036 #6 | traced |
| FT-OBL-007 | Keep typed failure classified as values, not failures | [`the-six-categories.md#typed-failure-is-not-failure`](../60-specification/runtime-failure-taxonomy/the-six-categories.md#typed-failure-is-not-failure) | c036 #7 | traced |
| FT-OBL-008 | Keep the taxonomy deterministic and outside G084/G088/G092/G095/G105/P109 claims with zero new families | [`diagnostics-and-conformance.md#abstract-public-boundaries`](../60-specification/runtime-failure-taxonomy/diagnostics-and-conformance.md#abstract-public-boundaries) | c036 #8 | traced |

C036 coverage is 8 `traced` and 0 untraced obligations. The dedicated
gate rejects unknown identifiers and fails if any `FT-OBL-*` identifier
lacks a focused tag.

## Resource observability registry (`RO`, 0.1.33)

Evidence labels refer to focused tests in the immutable compiler
[`c037_observability_test.exs`](https://github.com/pcharbon70/catena/blob/734aafeb3d1739af7d85b021a8fc7b1569b39c20/test/catena/c037_observability_test.exs)
and its
[`c037_traceability_coverage_test.exs`](https://github.com/pcharbon70/catena/blob/734aafeb3d1739af7d85b021a8fc7b1569b39c20/test/catena/c037_traceability_coverage_test.exs)
gate:

- **c037 #1** *keeps 0.1.33 exact selection with every predecessor default pinned and the lifecycle registered*
- **c037 #2** *fixes the six-way classification with stack use bounded by the tail guarantee*
- **c037 #3** *keeps semantic identity: equal values interchangeable, representation never changing meaning*
- **c037 #4** *keeps process identity the only identity-bearing value: fresh per spawn, never comparable*
- **c037 #5** *keeps every other value semantically identical only: closures, records, and messages carry no identity*
- **c037 #6** *keeps finalization declared absent with its gate*
- **c037 #7** *keeps stack use observable only through completion versus the tail guarantee*
- **c037 #8** *keeps the classification deterministic and outside G080s/G084/G085/G095/G124 claims with zero new families*

Anchors point at the normative 0.1.33 chapters; `RO-OBL-*` obligations
are fully traced against the immutable compiler commit.

| ID | Obligation | Normative anchor | Evidence | Status |
| --- | --- | --- | --- | --- |
| RO-OBL-001 | Apply observability behavior only at exact 0.1.33 and register the stable lifecycle addition | [`diagnostics-and-conformance.md#revision-and-persistence-separation`](../60-specification/resource-observability/diagnostics-and-conformance.md#revision-and-persistence-separation) | c037 #1; EDN001 | traced |
| RO-OBL-002 | Fix the six-way classification: addresses, sharing, GC, and identity (except process) unobservable; stack only via the tail guarantee; finalization absent | [`the-observability-model.md#the-six-way-classification`](../60-specification/resource-observability/the-observability-model.md#the-six-way-classification) | c037 #2 | traced |
| RO-OBL-003 | Keep semantic identity: equal values interchangeable, representation never changing meaning, storage observing nothing | [`the-observability-model.md#semantic-identity`](../60-specification/resource-observability/the-observability-model.md#semantic-identity) | c037 #3 | traced |
| RO-OBL-004 | Keep process identity the only identity-bearing value: fresh per spawn, kernel operations only, never comparable | [`identity-and-finalization.md#the-two-clause-identity-rule`](../60-specification/resource-observability/identity-and-finalization.md#the-two-clause-identity-rule) | c037 #4 | traced |
| RO-OBL-005 | Keep every other value semantically identical only: closure allocation, record sharing, message copying unobservable | [`identity-and-finalization.md#the-two-clause-identity-rule`](../60-specification/resource-observability/identity-and-finalization.md#the-two-clause-identity-rule) | c037 #5 | traced |
| RO-OBL-006 | Keep finalization declared absent with its gate: no cleanup form exists or arrives ungated | [`identity-and-finalization.md#finalization`](../60-specification/resource-observability/identity-and-finalization.md#finalization) | c037 #6 | traced |
| RO-OBL-007 | Keep stack use observable only through completion versus the tail guarantee | [`the-observability-model.md#stack-use`](../60-specification/resource-observability/the-observability-model.md#stack-use) | c037 #7 | traced |
| RO-OBL-008 | Keep the classification deterministic and outside G080s/G084/G085/G095/G124 claims with zero new families | [`diagnostics-and-conformance.md#abstract-public-boundaries`](../60-specification/resource-observability/diagnostics-and-conformance.md#abstract-public-boundaries) | c037 #8 | traced |

C037 coverage is 8 `traced` and 0 untraced obligations. The dedicated
gate rejects unknown identifiers and fails if any `RO-OBL-*` identifier
lacks a focused tag.

## Compile-time evaluation registry (`CE`, 0.1.34)

Evidence labels refer to focused tests in the immutable compiler
[`c038_compile_time_test.exs`](https://github.com/pcharbon70/catena/blob/30426d558f79498f791a398a5ff01c7590b18cad/test/catena/c038_compile_time_test.exs)
and its
[`c038_traceability_coverage_test.exs`](https://github.com/pcharbon70/catena/blob/30426d558f79498f791a398a5ff01c7590b18cad/test/catena/c038_traceability_coverage_test.exs)
gate:

- **c038 #1** *keeps 0.1.34 exact selection with every predecessor default pinned and the lifecycle registered*
- **c038 #2** *fixes the four-form decision: constants never execute; attributes and macros absent; derivations are generation*
- **c038 #3** *keeps the gate inherited: no unbounded evaluator is claimed*
- **c038 #4** *keeps derivations compiler-internal: no user code evaluated, provenance marked, output checked*
- **c038 #5** *keeps the restriction table exact: the gate plus the three cited budgets*
- **c038 #6** *keeps compilation deterministic: equal declarations, equal derived output, equal bytes*
- **c038 #7** *keeps the three meta-evaluators under their unchanged regimes*
- **c038 #8** *keeps the classification deterministic and outside P109/G040/G005/G116/G121 claims with zero new families*

Anchors point at the normative 0.1.34 chapters; `CE-OBL-*` obligations
are fully traced against the immutable compiler commit.

| ID | Obligation | Normative anchor | Evidence | Status |
| --- | --- | --- | --- | --- |
| CE-OBL-001 | Apply compile-time behavior only at exact 0.1.34 and register the stable lifecycle addition | [`diagnostics-and-conformance.md#revision-and-persistence-separation`](../60-specification/compile-time-evaluation/diagnostics-and-conformance.md#revision-and-persistence-separation) | c038 #1; EDN001 | traced |
| CE-OBL-002 | Fix the four-form decision: constants never execute; attributes and macros absent; derivations are generation | [`the-compile-time-stance.md#the-decision`](../60-specification/compile-time-evaluation/the-compile-time-stance.md#the-decision) | c038 #2 | traced |
| CE-OBL-003 | Keep the gate inherited: no evaluator arrives total-or-bounded-free; none is claimed | [`the-compile-time-stance.md#the-decision`](../60-specification/compile-time-evaluation/the-compile-time-stance.md#the-decision) | c038 #3 | traced |
| CE-OBL-004 | Keep derivations compiler-internal: no user code evaluated, provenance marked, output checked | [`the-compile-time-stance.md#generated-derivations`](../60-specification/compile-time-evaluation/the-compile-time-stance.md#generated-derivations) | c038 #4 | traced |
| CE-OBL-005 | Keep the restriction table exact: the gate plus the three cited budgets, complete at 0.1.34 | [`totality-and-determinism-restrictions.md#the-restriction-table`](../60-specification/compile-time-evaluation/totality-and-determinism-restrictions.md#the-restriction-table) | c038 #5 | traced |
| CE-OBL-006 | Keep compilation deterministic: equal declarations, equal derived output, equal bytes | [`totality-and-determinism-restrictions.md#determinism`](../60-specification/compile-time-evaluation/totality-and-determinism-restrictions.md#determinism) | c038 #6 | traced |
| CE-OBL-007 | Keep the three meta-evaluators under their unchanged regimes | [`totality-and-determinism-restrictions.md#the-restriction-table`](../60-specification/compile-time-evaluation/totality-and-determinism-restrictions.md#the-restriction-table) | c038 #7 | traced |
| CE-OBL-008 | Keep the classification deterministic and outside P109/G040/G005/G116/G121 claims with zero new families | [`diagnostics-and-conformance.md#abstract-public-boundaries`](../60-specification/compile-time-evaluation/diagnostics-and-conformance.md#abstract-public-boundaries) | c038 #8 | traced |

C038 coverage is 8 `traced` and 0 untraced obligations. The dedicated
gate rejects unknown identifiers and fails if any `CE-OBL-*` identifier
lacks a focused tag.

## Built-in data model registry (`BM`, 0.1.35)

Evidence labels refer to focused tests in the immutable compiler
[`c040_data_model_test.exs`](https://github.com/pcharbon70/catena/blob/44f7dd22b57757accc1da654bf4e99b93db728b4/test/catena/c040_data_model_test.exs)
and its
[`c040_traceability_coverage_test.exs`](https://github.com/pcharbon70/catena/blob/44f7dd22b57757accc1da654bf4e99b93db728b4/test/catena/c040_traceability_coverage_test.exs)
gate:

- **c040 #1** *keeps 0.1.35 exact selection with every predecessor default pinned and the lifecycle registered*
- **c040 #2** *fixes the twelve-way classification with the seven shipped types restated unchanged*
- **c040 #3** *elaborates the three scanner kinds deterministically, cooked/raw form-irrelevant over equal content*
- **c040 #4** *executes the content-based comparability entries: three new comparable-and-orderable types*
- **c040 #5** *keeps collections as library territory and references excluded, both gated*
- **c040 #6** *states the frontend absence honestly: no compiled-program text literals*
- **c040 #7** *keeps the Character one-scalar invariant and Text/Bytes content identity*
- **c040 #8** *keeps the model deterministic and outside G042/G084/G101/G105/P109 claims with zero new families*

Anchors point at the normative 0.1.35 chapters; `BM-OBL-*` obligations
are fully traced against the immutable compiler commit.

| ID | Obligation | Normative anchor | Evidence | Status |
| --- | --- | --- | --- | --- |
| BM-OBL-001 | Apply data-model behavior only at exact 0.1.35 and register the stable lifecycle addition | [`diagnostics-and-conformance.md#revision-and-persistence-separation`](../60-specification/built-in-data-model/diagnostics-and-conformance.md#revision-and-persistence-separation) | c040 #1; EDN001 | traced |
| BM-OBL-002 | Fix the twelve-way classification with the seven shipped types restated unchanged | [`the-twelve-way-classification.md#the-decision`](../60-specification/built-in-data-model/the-twelve-way-classification.md#the-decision) | c040 #2 | traced |
| BM-OBL-003 | Elaborate the three scanner kinds deterministically and totally, cooked/raw form-irrelevant over equal content | [`text-character-and-bytes.md#elaboration`](../60-specification/built-in-data-model/text-character-and-bytes.md#elaboration) | c040 #3 | traced |
| BM-OBL-004 | Execute the content-based comparability entries: three new comparable-and-orderable types with total orders | [`text-character-and-bytes.md#comparability-entries`](../60-specification/built-in-data-model/text-character-and-bytes.md#comparability-entries) | c040 #4 | traced |
| BM-OBL-005 | Keep collections as library territory and references excluded, both gated | [`the-twelve-way-classification.md#library-territory-not-exclusion`](../60-specification/built-in-data-model/the-twelve-way-classification.md#library-territory-not-exclusion) | c040 #5 | traced |
| BM-OBL-006 | State the frontend absence honestly: no compiled-program text literals; coverage entries at P109 | [`text-character-and-bytes.md#the-frontend-absence`](../60-specification/built-in-data-model/text-character-and-bytes.md#the-frontend-absence) | c040 #6 | traced |
| BM-OBL-007 | Keep the Character one-scalar invariant and Text/Bytes content identity | [`text-character-and-bytes.md#the-three-types`](../60-specification/built-in-data-model/text-character-and-bytes.md#the-three-types) | c040 #7 | traced |
| BM-OBL-008 | Keep the model deterministic and outside G042/G084/G101/G105/P109 claims with zero new families | [`diagnostics-and-conformance.md#abstract-public-boundaries`](../60-specification/built-in-data-model/diagnostics-and-conformance.md#abstract-public-boundaries) | c040 #8 | traced |

C040 coverage is 8 `traced` and 0 untraced obligations. The dedicated
gate rejects unknown identifiers and fails if any `BM-OBL-*` identifier
lacks a focused tag.

## Structural records registry (`SR`, 0.1.36)

Evidence labels refer to focused tests in the immutable compiler
[`c041_records_test.exs`](https://github.com/pcharbon70/catena/blob/f42c9588541b6e61e82fffdf823270e587f2c386/test/catena/c041_records_test.exs)
and its
[`c041_traceability_coverage_test.exs`](https://github.com/pcharbon70/catena/blob/f42c9588541b6e61e82fffdf823270e587f2c386/test/catena/c041_traceability_coverage_test.exs)
gate:

- **c041 #1** *keeps 0.1.36 exact selection with every predecessor default pinned and the lifecycle registered*
- **c041 #2** *fixes the seven-operation table with cited homes unchanged*
- **c041 #3** *enforces closed literals: duplicate labels reject; missing-label operations unreachable; no expression produces an open row*
- **c041 #4** *keeps field order an effect-order fact only, with tails composing through type positions*
- **c041 #5** *keeps records semantic maps: order never affects equality; representation invisible*
- **c041 #6** *states the frontend absence: kernel calculus only; spellings at P109*
- **c041 #7** *keeps variant inject a value and dispatch by semantic label then payload*
- **c041 #8** *keeps the contract deterministic and outside G042/G062/P044/P109 claims with zero new families*

Anchors point at the normative 0.1.36 chapters; `SR-OBL-*` obligations
are fully traced against the immutable compiler commit.

| ID | Obligation | Normative anchor | Evidence | Status |
| --- | --- | --- | --- | --- |
| SR-OBL-001 | Apply record behavior only at exact 0.1.36 and register the stable lifecycle addition | [`diagnostics-and-conformance.md#revision-and-persistence-separation`](../60-specification/structural-records-and-variants/diagnostics-and-conformance.md#revision-and-persistence-separation) | c041 #1; EDN001 | traced |
| SR-OBL-002 | Fix the seven-operation table with cited homes unchanged | [`the-operation-table.md#the-operations`](../60-specification/structural-records-and-variants/the-operation-table.md#the-operations) | c041 #2 | traced |
| SR-OBL-003 | Enforce closed literals: duplicate labels reject; missing-label operations statically unreachable; no expression produces an open row | [`rows-and-representation.md#the-row-model`](../60-specification/structural-records-and-variants/rows-and-representation.md#the-row-model) | c041 #3 | traced |
| SR-OBL-004 | Keep field order an effect-order fact only, with tails composing through type positions | [`rows-and-representation.md#the-row-model`](../60-specification/structural-records-and-variants/rows-and-representation.md#the-row-model) | c041 #4 | traced |
| SR-OBL-005 | Keep records semantic maps: order never affects equality; representation invisible | [`rows-and-representation.md#the-representation-clause`](../60-specification/structural-records-and-variants/rows-and-representation.md#the-representation-clause) | c041 #5 | traced |
| SR-OBL-006 | State the frontend absence: kernel calculus only; spellings at P109 | [`the-operation-table.md#the-frontend-absence`](../60-specification/structural-records-and-variants/the-operation-table.md#the-frontend-absence) | c041 #6 | traced |
| SR-OBL-007 | Keep variant inject a value and dispatch by semantic label then payload | [`the-operation-table.md#the-operations`](../60-specification/structural-records-and-variants/the-operation-table.md#the-operations) | c041 #7 | traced |
| SR-OBL-008 | Keep the contract deterministic and outside G042/G062/P044/P109 claims with zero new families | [`diagnostics-and-conformance.md#abstract-public-boundaries`](../60-specification/structural-records-and-variants/diagnostics-and-conformance.md#abstract-public-boundaries) | c041 #8 | traced |

C041 coverage is 8 `traced` and 0 untraced obligations. The dedicated
gate rejects unknown identifiers and fails if any `SR-OBL-*` identifier
lacks a focused tag.

## Collection construction registry (`CO`, 0.1.37)

Evidence labels refer to focused tests in
`test/catena/c042_collections_test.exs` and its
`test/catena/c042_traceability_coverage_test.exs` gate in the sibling
compiler repository. The focused set is:

- **c042 #1** *keeps 0.1.37 exact selection with every predecessor default pinned and the lifecycle registered*
- **c042 #2** *fixes the six-topic decision with shipped machinery and named owners*
- **c042 #3** *keeps construction and update as constructor application and match recursion, distinct from records*
- **c042 #4** *classifies a lookup miss as typed failure as a value: total operations, never a trap*
- **c042 #5** *excludes complexity from the language layer, delegating documentation to G101*
- **c042 #6** *fixes duplicate-key behavior as a G101 declaration obligation, explicit in the declaring slice*
- **c042 #7** *rides C035 for ordering and key equality: keys must be comparable*
- **c042 #8** *keeps the contract deterministic and outside G101/G105/P109 claims with zero new families*

Anchors point at the normative 0.1.37 chapters. Status reflects the
merged compiler evidence (`246019f`, branch `agent/c042-collections`).

| ID | Obligation | Normative anchor | Evidence | Status |
| --- | --- | --- | --- | --- |
| CO-OBL-001 | Apply collection behavior only at exact 0.1.37 and register the stable lifecycle addition | [`diagnostics-and-conformance.md#revision-and-persistence-separation`](../60-specification/collection-construction-and-update/diagnostics-and-conformance.md#revision-and-persistence-separation) | c042 #1; EDN001 | traced |
| CO-OBL-002 | Fix the six-topic decision with shipped machinery and named owners | [`the-six-topic-decision.md#the-decision`](../60-specification/collection-construction-and-update/the-six-topic-decision.md#the-decision) | c042 #2 | traced |
| CO-OBL-003 | Keep construction and update as constructor application and match recursion, distinct from records | [`the-six-topic-decision.md#construction-is-construction`](../60-specification/collection-construction-and-update/the-six-topic-decision.md#construction-is-construction) | c042 #3 | traced |
| CO-OBL-004 | Classify a lookup miss as typed failure as a value: total operations, never a trap | [`miss-as-value-and-complexity.md#miss-as-value`](../60-specification/collection-construction-and-update/miss-as-value-and-complexity.md#miss-as-value) | c042 #4 | traced |
| CO-OBL-005 | Exclude complexity from the language layer, delegating documentation to G101 | [`miss-as-value-and-complexity.md#the-complexity-exclusion`](../60-specification/collection-construction-and-update/miss-as-value-and-complexity.md#the-complexity-exclusion) | c042 #5 | traced |
| CO-OBL-006 | Fix duplicate-key behavior as a G101 declaration obligation, explicit in the declaring slice | [`the-six-topic-decision.md#the-decision`](../60-specification/collection-construction-and-update/the-six-topic-decision.md#the-decision) | c042 #6 | traced |
| CO-OBL-007 | Ride C035 for ordering and key equality: keys must be comparable | [`the-six-topic-decision.md#the-decision`](../60-specification/collection-construction-and-update/the-six-topic-decision.md#the-decision) | c042 #7 | traced |
| CO-OBL-008 | Keep the contract deterministic and outside G101/G105/P109 claims with zero new families | [`diagnostics-and-conformance.md#abstract-public-boundaries`](../60-specification/collection-construction-and-update/diagnostics-and-conformance.md#abstract-public-boundaries) | c042 #8 | traced |

C042 coverage is 8 `traced` and 0 untraced obligations. The dedicated
gate rejects unknown identifiers and fails if any `CO-OBL-*` identifier
lacks a focused tag.

## Pattern contexts registry (`PC`, 0.1.38)

Evidence labels refer to focused tests in
`test/catena/c044_pattern_contexts_test.exs` and its
`test/catena/c044_traceability_coverage_test.exs` gate in the sibling
compiler repository. The focused set is:

- **c044 #1** *applies pattern-context rules only at exact 0.1.38 with zero new families and the lifecycle registered*
- **c044 #2** *fixes the three context classes with exactly one exhaustive context*
- **c044 #3** *keeps match's C045 authority and the no-implicit-runtime-match property with unchanged diagnostics*
- **c044 #4** *keeps `let` and parameters plain-named today with the irrefutable-only default reserved for arrivals*
- **c044 #5** *fixes the generator principle: ordinary total, filtering explicitly mismatch-as-skip, grammar deferred*
- **c044 #6** *reserves public receives as exhaustive-or-explicit-fallback in their own slice*
- **c044 #7** *keeps handler clauses on plain binders with irrefutable-only arrival*
- **c044 #8** *excludes exception clauses under C036's terminal trap taxonomy*
- **c044 #9** *excludes programmable patterns with recorded arrival conditions*

Anchors point at the normative 0.1.38 chapters. Status reflects the
merged compiler evidence (`00bd04c`, branch `agent/c044-pattern-contexts`).

| ID | Obligation | Normative anchor | Evidence | Status |
| --- | --- | --- | --- | --- |
| PC-OBL-001 | Apply pattern-context rules only at exact 0.1.38 and register the stable lifecycle addition with zero new families | [`diagnostics-and-conformance.md#revision-and-persistence-separation`](../60-specification/pattern-contexts/diagnostics-and-conformance.md#revision-and-persistence-separation) | c044 #1 | traced |
| PC-OBL-002 | Fix the three context classes with exactly one exhaustive context | [`the-three-context-classes.md#the-classification`](../60-specification/pattern-contexts/the-three-context-classes.md#the-classification) | c044 #2 | traced |
| PC-OBL-003 | Keep match's C045 authority and the no-implicit-runtime-match property with unchanged diagnostics | [`the-three-context-classes.md#match-is-the-only-exhaustive-context`](../60-specification/pattern-contexts/the-three-context-classes.md#match-is-the-only-exhaustive-context) | c044 #3 | traced |
| PC-OBL-004 | Keep `let` and parameters plain-named today with the irrefutable-only default reserved for arrivals | [`context-rules-and-reservations.md#the-context-table`](../60-specification/pattern-contexts/context-rules-and-reservations.md#the-context-table) | c044 #4 | traced |
| PC-OBL-005 | Fix the generator principle: ordinary total, filtering explicitly mismatch-as-skip, grammar deferred | [`context-rules-and-reservations.md#the-context-table`](../60-specification/pattern-contexts/context-rules-and-reservations.md#the-context-table) | c044 #5 | traced |
| PC-OBL-006 | Reserve public receives as exhaustive-or-explicit-fallback in their own slice | [`context-rules-and-reservations.md#the-context-table`](../60-specification/pattern-contexts/context-rules-and-reservations.md#the-context-table) | c044 #6 | traced |
| PC-OBL-007 | Keep handler clauses on plain binders with irrefutable-only arrival | [`context-rules-and-reservations.md#the-context-table`](../60-specification/pattern-contexts/context-rules-and-reservations.md#the-context-table) | c044 #7 | traced |
| PC-OBL-008 | Exclude exception clauses under C036's terminal trap taxonomy | [`context-rules-and-reservations.md#the-context-table`](../60-specification/pattern-contexts/context-rules-and-reservations.md#the-context-table) | c044 #8 | traced |
| PC-OBL-009 | Exclude programmable patterns with recorded arrival conditions | [`context-rules-and-reservations.md#the-programmable-pattern-exclusion`](../60-specification/pattern-contexts/context-rules-and-reservations.md#the-programmable-pattern-exclusion) | c044 #9 | traced |

C044 coverage is 9 `traced` and 0 untraced obligations. The dedicated
gate rejects unknown identifiers and fails if any `PC-OBL-*` identifier
lacks a focused tag.

## List comprehensions registry (`LC`, 0.1.39)

Evidence labels refer to focused tests in
`test/catena/c047_list_comprehensions_test.exs` and its
`test/catena/c047_traceability_coverage_test.exs` gate in the sibling
compiler repository. The focused set is:

- **c047 #1** *applies comprehension rules only at exact 0.1.39 with the LCP families declared and the elaboration API registered*
- **c047 #2** *fixes the grammar's semantic roles and keywords with the adoption boundary at the surface capstone*
- **c047 #3** *requires List A sources with the excluded-source boundary*
- **c047 #4** *fixes left-to-right depth-first traversal with dependency, once-per-prefix source evaluation, and empty-input behavior*
- **c047 #5** *fixes when-filter semantics: visible effects, false-as-skip, all other failures propagate, no guard fragment*
- **c047 #6** *consumes C044's split: total ordinary generators, case mismatch-as-skip, LCP002/LCP003 markers, M001 reuse*
- **c047 #7** *fixes left-to-right scope, non-escaping non-recursive bindings, LCP001 rebinding, BS001 reuse*
- **c047 #8** *fixes exact order, multiplicity, non-short-circuiting filters, and failure timing with visible effect rows*
- **c047 #9** *fixes eager ordered production with lazy and infinite inputs excluded*
- **c047 #10** *fixes the typed qualifier-tree target, the extensional equations, and the no-dispatch rule*
- **c047 #11** *fixes List B results with all other targets excluded*
- **c047 #12** *makes sequential execution normative and parallel forms excluded*
- **c047 #13** *produces the fused tail-recursive worker chain with linear allocation, source-faithful diagnostics, and cost honesty*
- **c047 #14** *keeps the contract deterministic and outside unowned claims with the reuse map enforced*

Anchors point at the normative 0.1.39 chapters. Status reflects the
merged compiler evidence (`3216831`, branch `agent/c047-comprehensions`).

| ID | Obligation | Normative anchor | Evidence | Status |
| --- | --- | --- | --- | --- |
| LC-OBL-001 | Apply comprehension rules only at exact 0.1.39, register the lifecycle addition, and declare the LCP families and the elaboration API | [`diagnostics-and-conformance.md#revision-and-persistence-separation`](../60-specification/list-comprehensions/diagnostics-and-conformance.md#revision-and-persistence-separation) | c047 #1 | traced |
| LC-OBL-002 | Fix the grammar's semantic roles and keywords with the adoption boundary at the surface capstone | [`the-surface-contract.md#the-grammars-semantic-roles`](../60-specification/list-comprehensions/the-surface-contract.md#the-grammars-semantic-roles) | c047 #2 | traced |
| LC-OBL-003 | Require `List A` sources with the excluded-source boundary | [`generator-and-qualifier-rules.md#sources`](../60-specification/list-comprehensions/generator-and-qualifier-rules.md#sources) | c047 #3 | traced |
| LC-OBL-004 | Fix left-to-right depth-first traversal with dependency, once-per-prefix source evaluation, and empty-input behavior | [`generator-and-qualifier-rules.md#traversal`](../60-specification/list-comprehensions/generator-and-qualifier-rules.md#traversal) | c047 #4 | traced |
| LC-OBL-005 | Fix `when` filter semantics: visible effects, false-as-skip, all other failures propagate, no guard fragment | [`generator-and-qualifier-rules.md#filters`](../60-specification/list-comprehensions/generator-and-qualifier-rules.md#filters) | c047 #5 | traced |
| LC-OBL-006 | Consume C044's split: total ordinary generators, `case` mismatch-as-skip, `LCP002`/`LCP003` markers, `M001` reuse | [`generator-and-qualifier-rules.md#the-pattern-generator-split`](../60-specification/list-comprehensions/generator-and-qualifier-rules.md#the-pattern-generator-split) | c047 #6 | traced |
| LC-OBL-007 | Fix left-to-right scope, non-escaping non-recursive bindings, `LCP001` rebinding, `BS001` reuse | [`generator-and-qualifier-rules.md#scope-and-rebinding`](../60-specification/list-comprehensions/generator-and-qualifier-rules.md#scope-and-rebinding) | c047 #7 | traced |
| LC-OBL-008 | Fix exact order, multiplicity, non-short-circuiting filters, and failure timing with visible effect rows | [`evaluation-effects-and-execution.md#exact-order`](../60-specification/list-comprehensions/evaluation-effects-and-execution.md#exact-order) | c047 #8 | traced |
| LC-OBL-009 | Fix eager ordered production with lazy and infinite inputs excluded | [`the-surface-contract.md#eager-ordered-production`](../60-specification/list-comprehensions/the-surface-contract.md#eager-ordered-production) | c047 #9 | traced |
| LC-OBL-010 | Fix the typed qualifier-tree target, the extensional equations, and the no-dispatch rule | [`elaboration-and-lowering.md#the-qualifier-tree-target`](../60-specification/list-comprehensions/elaboration-and-lowering.md#the-qualifier-tree-target) | c047 #10 | traced |
| LC-OBL-011 | Fix `List B` results with all other targets excluded | [`the-surface-contract.md#the-result-type-boundary`](../60-specification/list-comprehensions/the-surface-contract.md#the-result-type-boundary) | c047 #11 | traced |
| LC-OBL-012 | Make sequential execution normative and parallel forms excluded | [`evaluation-effects-and-execution.md#sequential-execution-is-normative`](../60-specification/list-comprehensions/evaluation-effects-and-execution.md#sequential-execution-is-normative) | c047 #12 | traced |
| LC-OBL-013 | Produce the fused tail-recursive worker with linear allocation, source-faithful diagnostics, and cost honesty | [`elaboration-and-lowering.md#the-fused-worker`](../60-specification/list-comprehensions/elaboration-and-lowering.md#the-fused-worker) | c047 #13 | traced |
| LC-OBL-014 | Keep the contract deterministic and outside unowned claims with the reuse map enforced | [`diagnostics-and-conformance.md#abstract-public-boundaries`](../60-specification/list-comprehensions/diagnostics-and-conformance.md#abstract-public-boundaries) | c047 #14 | traced |

C047 coverage is 14 `traced` and 0 untraced obligations. The dedicated
gate rejects unknown identifiers and fails if any `LC-OBL-*` identifier
lacks a focused tag.

## Numeric relationships registry (`NR`, 0.1.40)

Evidence labels refer to focused tests in
`test/catena/c061_numeric_relationships_test.exs` and its
`test/catena/c061_traceability_coverage_test.exs` gate in the sibling
compiler repository. The focused set is:

- **c061 #1** *applies numeric-relationship rules only at exact 0.1.40 with zero new families and the lifecycle registered*
- **c061 #2** *fixes the closed-set instantiation rule: operands unify with each other over exactly {Int, Float}*
- **c061 #3** *keeps operators free of dispatch, evidence, and user overloadability*
- **c061 #4** *re-affirms no defaulting, no implicit coercion, no literal constraints; mixed operands ill-typed*
- **c061 #5** *makes arithmetic same-type over {Int, Float}: annotated float parameters check and run*
- **c061 #6** *keeps the contract deterministic with zero new families and the reuse boundary enforced*
- **c061 #7** *routes division, remainder, and reserved spellings to G105 with no divide or remainder operator existing*
- **c061 #8** *keeps the closed set amendable only by a new revision amending the enumeration*

Anchors point at the normative 0.1.40 chapters. Status reflects the
merged compiler evidence (`fd75cb7`, branch `agent/c061-numerics`).

| ID | Obligation | Normative anchor | Evidence | Status |
| --- | --- | --- | --- | --- |
| NR-OBL-001 | Apply numeric-relationship rules only at exact 0.1.40 and register the stable lifecycle addition with zero new families and no new API | [`diagnostics-and-conformance.md#revision-and-persistence-separation`](../60-specification/numeric-relationships/diagnostics-and-conformance.md#revision-and-persistence-separation) | c061 #1 | traced |
| NR-OBL-002 | Fix the closed-set instantiation rule: operands unify with each other over exactly {Int, Float} | [`the-closed-set-instantiation-rule.md#the-rule`](../60-specification/numeric-relationships/the-closed-set-instantiation-rule.md#the-rule) | c061 #2 | traced |
| NR-OBL-003 | Keep operators free of dispatch, evidence, and user overloadability | [`exclusions-and-routings.md#no-dispatch-no-overloadability`](../60-specification/numeric-relationships/exclusions-and-routings.md#no-dispatch-no-overloadability) | c061 #3 | traced |
| NR-OBL-004 | Re-affirm no defaulting, no implicit coercion, no literal constraints; mixed operands ill-typed | [`exclusions-and-routings.md#the-frozen-exclusions-re-affirmed`](../60-specification/numeric-relationships/exclusions-and-routings.md#the-frozen-exclusions-re-affirmed) | c061 #4 | traced |
| NR-OBL-005 | Make arithmetic same-type over {Int, Float}: annotated float parameters check and run | [`the-closed-set-instantiation-rule.md#float-arithmetic`](../60-specification/numeric-relationships/the-closed-set-instantiation-rule.md#float-arithmetic) | c061 #5 | traced |
| NR-OBL-006 | Keep the contract deterministic with zero new families and the reuse boundary enforced | [`diagnostics-and-conformance.md#abstract-public-boundaries`](../60-specification/numeric-relationships/diagnostics-and-conformance.md#abstract-public-boundaries) | c061 #6 | traced |
| NR-OBL-007 | Route division, remainder, and reserved spellings to G105 with no divide or remainder operator existing | [`exclusions-and-routings.md#division-and-remainder`](../60-specification/numeric-relationships/exclusions-and-routings.md#division-and-remainder) | c061 #7 | traced |
| NR-OBL-008 | Keep the closed set amendable only by a new revision amending the enumeration | [`the-closed-set-instantiation-rule.md#the-closed-set`](../60-specification/numeric-relationships/the-closed-set-instantiation-rule.md#the-closed-set) | c061 #8 | traced |

C061 coverage is 8 `traced` and 0 untraced obligations. The dedicated
gate rejects unknown identifiers and fails if any `NR-OBL-*` identifier
lacks a focused tag.

## Aliases and newtypes registry (`AN`, 0.1.41)

Evidence labels refer to focused tests in
`test/catena/c062_aliases_newtypes_test.exs` and its
`test/catena/c062_traceability_coverage_test.exs` gate in the sibling
compiler repository. The focused set is:

- **c062 #1** *applies alias-and-newtype rules only at exact 0.1.41 with zero new families and the lifecycle registered*
- **c062 #2** *keeps transparent aliases excluded with the four arrival conditions recorded*
- **c062 #3** *fixes the newtype as the nominal single-constructor single-field datatype with its own identity*
- **c062 #4** *keeps representation invisible with no cost or layout promises attached to a newtype*
- **c062 #5** *routes opaque types to the binary authority vocabulary and keeps nominal-spelled diagnostics*
- **c062 #6** *keeps coercion explicit: constructor wraps, pattern unwraps, confusion rejects*
- **c062 #7** *keeps deriving explicit-target only with no instance flow through the wrapper*
- **c062 #8** *keeps the exclusion amendable only by a revision discharging all four arrival conditions*

Anchors point at the normative 0.1.41 chapters. Status reflects the
merged compiler evidence (`1de0a7d`, branch `agent/c062-newtypes`).

| ID | Obligation | Normative anchor | Evidence | Status |
| --- | --- | --- | --- | --- |
| AN-OBL-001 | Apply alias-and-newtype rules only at exact 0.1.41 and register the stable lifecycle addition with zero new families and no new API | [`diagnostics-and-conformance.md#revision-and-persistence-separation`](../60-specification/aliases-and-newtypes/diagnostics-and-conformance.md#revision-and-persistence-separation) | c062 #1 | traced |
| AN-OBL-002 | Keep transparent aliases excluded with the four arrival conditions recorded | [`the-alias-exclusion.md#the-exclusion`](../60-specification/aliases-and-newtypes/the-alias-exclusion.md#the-exclusion) | c062 #2 | traced |
| AN-OBL-003 | Fix the newtype as the nominal single-constructor single-field datatype with its own identity | [`the-newtype-form.md#the-newtype-is-a-declared-form`](../60-specification/aliases-and-newtypes/the-newtype-form.md#the-newtype-is-a-declared-form) | c062 #3 | traced |
| AN-OBL-004 | Keep representation invisible with no cost or layout promises attached to a newtype | [`the-newtype-form.md#representation-and-cost`](../60-specification/aliases-and-newtypes/the-newtype-form.md#representation-and-cost) | c062 #4 | traced |
| AN-OBL-005 | Route opaque types to the binary authority vocabulary and keep nominal-spelled diagnostics | [`the-newtype-form.md#constructor-access-and-the-opaque-routing`](../60-specification/aliases-and-newtypes/the-newtype-form.md#constructor-access-and-the-opaque-routing) | c062 #5 | traced |
| AN-OBL-006 | Keep coercion explicit: constructor wraps, pattern unwraps, confusion rejects | [`the-newtype-form.md#coercion`](../60-specification/aliases-and-newtypes/the-newtype-form.md#coercion) | c062 #6 | traced |
| AN-OBL-007 | Keep deriving explicit-target only with no instance flow through the wrapper | [`the-newtype-form.md#deriving`](../60-specification/aliases-and-newtypes/the-newtype-form.md#deriving) | c062 #7 | traced |
| AN-OBL-008 | Keep the exclusion amendable only by a revision discharging all four arrival conditions | [`the-alias-exclusion.md#arrival-conditions`](../60-specification/aliases-and-newtypes/the-alias-exclusion.md#arrival-conditions) | c062 #8 | traced |

C062 coverage is 8 `traced` and 0 untraced obligations. The dedicated
gate rejects unknown identifiers and fails if any `AN-OBL-*` identifier
lacks a focused tag.

## Name resolution registry (`RN`, 0.1.42)

Evidence labels refer to focused tests in
`test/catena/c066_name_resolution_test.exs` and its
`test/catena/c066_traceability_coverage_test.exs` gate in the sibling
compiler repository. The focused set is:

- **c066 #1** *applies resolution rules only at exact 0.1.42 with zero new families and the lifecycle registered*
- **c066 #2** *keeps resolution type-independent: annotations never change a name's target and results never depend on elaboration order*
- **c066 #3** *keeps the five-way classification: labels not names, constructors by visibility, literals by spelling, operators closed-set*
- **c066 #4** *keeps evidence selection distinct from name resolution, settled at the instance with no call-site deferral*
- **c066 #5** *keeps the four exclusions: no overloading by type, no expected-type adaptation, no call-site deferral, no inference-directed field access*
- **c066 #6** *keeps the table amendable only by a revision stating order-independence*
- **c066 #7** *keeps scope-structure resolution with collision rejection unchanged from C021*
- **c066 #8** *keeps the contract deterministic with the reuse map enforced*

Anchors point at the normative 0.1.42 chapters. Status reflects the
merged compiler evidence (`bef5fd5`, branch `agent/c066-resolution`).

| ID | Obligation | Normative anchor | Evidence | Status |
| --- | --- | --- | --- | --- |
| RN-OBL-001 | Apply resolution rules only at exact 0.1.42 and register the stable lifecycle addition with zero new families and no new API | [`diagnostics-and-conformance.md#revision-and-persistence-separation`](../60-specification/name-resolution/diagnostics-and-conformance.md#revision-and-persistence-separation) | c066 #1 | traced |
| RN-OBL-002 | Keep resolution type-independent: annotations never change a name's target and results never depend on elaboration order | [`the-resolution-invariant.md#the-invariant`](../60-specification/name-resolution/the-resolution-invariant.md#the-invariant) | c066 #2 | traced |
| RN-OBL-003 | Keep the five-way classification: labels not names, constructors by visibility, literals by spelling, operators closed-set | [`the-resolution-invariant.md#the-five-way-classification`](../60-specification/name-resolution/the-resolution-invariant.md#the-five-way-classification) | c066 #3 | traced |
| RN-OBL-004 | Keep evidence selection distinct from name resolution, settled at the instance with no call-site deferral | [`the-resolution-invariant.md#the-evidence-selection-carve-out`](../60-specification/name-resolution/the-resolution-invariant.md#the-evidence-selection-carve-out) | c066 #4 | traced |
| RN-OBL-005 | Keep the four exclusions: no overloading by type, no expected-type adaptation, no call-site deferral, no inference-directed field access | [`boundaries-and-reservations.md#the-exclusions`](../60-specification/name-resolution/boundaries-and-reservations.md#the-exclusions) | c066 #5 | traced |
| RN-OBL-006 | Keep the table amendable only by a revision stating order-independence | [`boundaries-and-reservations.md#arrival-conditions`](../60-specification/name-resolution/boundaries-and-reservations.md#arrival-conditions) | c066 #6 | traced |
| RN-OBL-007 | Keep scope-structure resolution with collision rejection unchanged from C021 | [`the-resolution-invariant.md#the-invariant`](../60-specification/name-resolution/the-resolution-invariant.md#the-invariant) | c066 #7 | traced |
| RN-OBL-008 | Keep the contract deterministic with the reuse map enforced | [`diagnostics-and-conformance.md#abstract-public-boundaries`](../60-specification/name-resolution/diagnostics-and-conformance.md#abstract-public-boundaries) | c066 #8 | traced |

C066 coverage is 8 `traced` and 0 untraced obligations. The dedicated
gate rejects unknown identifiers and fails if any `RN-OBL-*` identifier
lacks a focused tag.

## Dynamic and unsafe boundaries registry (`DU`, 0.1.43)

Evidence labels refer to focused tests in
`test/catena/c067_dynamic_unsafe_test.exs` and its
`test/catena/c067_traceability_coverage_test.exs` gate in the sibling
compiler repository. The focused set is:

- **c067 #1** *applies boundary rules only at exact 0.1.43 with zero new families and the lifecycle registered*
- **c067 #2** *keeps all five intralanguage exclusions: no casts, no runtime type inspection, no unchecked operations, no intrinsics, no reflection*
- **c067 #3** *keeps the guard fragment's rejection of the dynamic vocabulary unchanged from C003*
- **c067 #4** *enforces the cross-edge requirement: dynamic or unsafe values enter only through a visible, typed, failure-classified foreign boundary*
- **c067 #5** *keeps the standing precedents cited and adds no mechanism or spelling*
- **c067 #6** *keeps the exclusions amendable only by a revision discharging all four arrival conditions*
- **c067 #7** *keeps erasure intact: no runtime type or specification material for inspection*
- **c067 #8** *keeps the contract deterministic with no dyn, any, or unknown type existing*

Anchors point at the normative 0.1.43 chapters. Status reflects the
merged compiler evidence (`ed14901`, branch `agent/c067-boundaries`).

| ID | Obligation | Normative anchor | Evidence | Status |
| --- | --- | --- | --- | --- |
| DU-OBL-001 | Apply boundary rules only at exact 0.1.43 and register the stable lifecycle addition with zero new families and no new API | [`diagnostics-and-conformance.md#revision-and-persistence-separation`](../60-specification/dynamic-and-unsafe-boundaries/diagnostics-and-conformance.md#revision-and-persistence-separation) | c067 #1 | traced |
| DU-OBL-002 | Keep all five intralanguage exclusions: no casts, no runtime type inspection, no unchecked operations, no intrinsics, no reflection | [`the-intralanguage-exclusions.md#the-exclusions`](../60-specification/dynamic-and-unsafe-boundaries/the-intralanguage-exclusions.md#the-exclusions) | c067 #2 | traced |
| DU-OBL-003 | Keep the guard fragment's rejection of the dynamic vocabulary unchanged from C003 | [`the-intralanguage-exclusions.md#the-exclusions`](../60-specification/dynamic-and-unsafe-boundaries/the-intralanguage-exclusions.md#the-exclusions) | c067 #3 | traced |
| DU-OBL-004 | Enforce the cross-edge requirement: dynamic or unsafe values enter only through a visible, typed, failure-classified foreign boundary | [`the-foreign-visibility-routing.md#the-cross-edge-requirement`](../60-specification/dynamic-and-unsafe-boundaries/the-foreign-visibility-routing.md#the-cross-edge-requirement) | c067 #4 | traced |
| DU-OBL-005 | Keep the standing precedents cited and add no mechanism or spelling | [`the-foreign-visibility-routing.md#standing-precedents`](../60-specification/dynamic-and-unsafe-boundaries/the-foreign-visibility-routing.md#standing-precedents) | c067 #5 | traced |
| DU-OBL-006 | Keep the exclusions amendable only by a revision discharging all four arrival conditions | [`the-intralanguage-exclusions.md#arrival-conditions`](../60-specification/dynamic-and-unsafe-boundaries/the-intralanguage-exclusions.md#arrival-conditions) | c067 #6 | traced |
| DU-OBL-007 | Keep erasure intact: no runtime type or specification material for inspection | [`diagnostics-and-conformance.md#abstract-public-boundaries`](../60-specification/dynamic-and-unsafe-boundaries/diagnostics-and-conformance.md#abstract-public-boundaries) | c067 #7 | traced |
| DU-OBL-008 | Keep the contract deterministic with no dyn, any, or unknown type existing | [`diagnostics-and-conformance.md#abstract-public-boundaries`](../60-specification/dynamic-and-unsafe-boundaries/diagnostics-and-conformance.md#abstract-public-boundaries) | c067 #8 | traced |

C067 coverage is 8 `traced` and 0 untraced obligations. The dedicated
gate rejects unknown identifiers and fails if any `DU-OBL-*` identifier
lacks a focused tag.

## Excluded advanced type features registry (`EA`, 0.1.44)

Evidence labels refer to focused tests in
`test/catena/c140_excluded_advanced_test.exs` and its
`test/catena/c140_traceability_coverage_test.exs` gate in the sibling
compiler repository. The focused set is:

- **c140 #1** *applies exclusion rules only at exact 0.1.44 with zero new families and the lifecycle registered*
- **c140 #2** *keeps all seven forms excluded with the checked profile unchanged*
- **c140 #3** *keeps the seven-point gate as the only amendment route*
- **c140 #4** *keeps rejections identifying the profile boundary*
- **c140 #5** *keeps C068's checked advanced profile checking unchanged*
- **c140 #6** *admits no omnibus advanced-features revision*
- **c140 #7** *keeps the contract deterministic with no excluded spelling accepted*

Anchors point at the normative 0.1.44 chapters. Status reflects the
merged compiler evidence (`77fba75`, branch `agent/c140-advanced-exclusions`).

| ID | Obligation | Normative anchor | Evidence | Status |
| --- | --- | --- | --- | --- |
| EA-OBL-001 | Apply exclusion rules only at exact 0.1.44 and register the stable lifecycle addition with zero new families and no new API | [`diagnostics-and-conformance.md#revision-and-persistence-separation`](../60-specification/excluded-advanced-type-features/diagnostics-and-conformance.md#revision-and-persistence-separation) | c140 #1 | traced |
| EA-OBL-002 | Keep all seven forms excluded with the checked profile unchanged | [`the-exclusion-table-and-gate.md#the-exclusion-table`](../60-specification/excluded-advanced-type-features/the-exclusion-table-and-gate.md#the-exclusion-table) | c140 #2 | traced |
| EA-OBL-003 | Keep the seven-point gate as the only amendment route | [`the-exclusion-table-and-gate.md#the-arrival-gate`](../60-specification/excluded-advanced-type-features/the-exclusion-table-and-gate.md#the-arrival-gate) | c140 #3 | traced |
| EA-OBL-004 | Keep rejections identifying the profile boundary | [`the-exclusion-table-and-gate.md#the-exclusion-table`](../60-specification/excluded-advanced-type-features/the-exclusion-table-and-gate.md#the-exclusion-table) | c140 #4 | traced |
| EA-OBL-005 | Keep C068's checked advanced profile checking unchanged | [`the-exclusion-table-and-gate.md#the-exclusion-table`](../60-specification/excluded-advanced-type-features/the-exclusion-table-and-gate.md#the-exclusion-table) | c140 #5 | traced |
| EA-OBL-006 | Admit no omnibus advanced-features revision | [`the-exclusion-table-and-gate.md#the-arrival-gate`](../60-specification/excluded-advanced-type-features/the-exclusion-table-and-gate.md#the-arrival-gate) | c140 #6 | traced |
| EA-OBL-007 | Keep the contract deterministic with no excluded spelling accepted | [`diagnostics-and-conformance.md#abstract-public-boundaries`](../60-specification/excluded-advanced-type-features/diagnostics-and-conformance.md#abstract-public-boundaries) | c140 #7 | traced |

C140 coverage is 7 `traced` and 0 untraced obligations. The dedicated
gate rejects unknown identifiers and fails if any `EA-OBL-*` identifier
lacks a focused tag.

## Progress and preservation registry (`PP`, 0.1.45)

Evidence labels will refer to focused tests in
`test/catena/c132_progress_preservation_test.exs` and its
`test/catena/c132_traceability_coverage_test.exs` gate in the sibling
compiler repository. The planned focused set is:

- **c132 #1** *applies target rules only at exact 0.1.45 with zero new families and the lifecycle registered*
- **c132 #2** *states the effects-and-failure targets over the shipped calculus only*
- **c132 #3** *keeps effect progress and trap terminality as stated with kernel-verbatim reasons*
- **c132 #4** *carries each target's evidence obligation with the C030 dual-agreement discipline*
- **c132 #5** *keeps the integrated theorem as a composed statement with the conditional summary*
- **c132 #6** *keeps the composition lemma a routed proof obligation, never a claim*
- **c132 #7** *keeps the process and foreign extensions conditional and routed to their owners*
- **c132 #8** *keeps the contract deterministic with the component corpora unchanged*

Anchors currently point at the candidate 0.1.45 chapters and become
normative anchors at C132 promotion. Status is `untraced` until the
compiler evidence lands.

| ID | Obligation | Normative anchor | Evidence | Status |
| --- | --- | --- | --- | --- |
| PP-OBL-001 | Apply target rules only at exact 0.1.45 and register the stable lifecycle addition with zero new families and no new API | [`diagnostics-and-conformance.md#revision-and-persistence-separation`](../60-specification/progress-and-preservation/diagnostics-and-conformance.md#revision-and-persistence-separation) | c132 #1 | untraced |
| PP-OBL-002 | State the effects-and-failure targets over the shipped calculus only | [`the-effects-and-failure-targets.md#the-targets`](../60-specification/progress-and-preservation/the-effects-and-failure-targets.md#the-targets) | c132 #2 | untraced |
| PP-OBL-003 | Keep effect progress and trap terminality as stated with kernel-verbatim reasons | [`the-effects-and-failure-targets.md#the-targets`](../60-specification/progress-and-preservation/the-effects-and-failure-targets.md#the-targets) | c132 #3 | untraced |
| PP-OBL-004 | Carry each target's evidence obligation with the C030 dual-agreement discipline | [`the-effects-and-failure-targets.md#evidence-obligations`](../60-specification/progress-and-preservation/the-effects-and-failure-targets.md#evidence-obligations) | c132 #4 | untraced |
| PP-OBL-005 | Keep the integrated theorem as a composed statement with the conditional summary | [`the-integrated-theorem.md#the-composed-statement`](../60-specification/progress-and-preservation/the-integrated-theorem.md#the-composed-statement) | c132 #5 | untraced |
| PP-OBL-006 | Keep the composition lemma a routed proof obligation, never a claim | [`the-integrated-theorem.md#the-composition-lemma`](../60-specification/progress-and-preservation/the-integrated-theorem.md#the-composition-lemma) | c132 #6 | untraced |
| PP-OBL-007 | Keep the process and foreign extensions conditional and routed to their owners | [`the-integrated-theorem.md#conditional-extensions`](../60-specification/progress-and-preservation/the-integrated-theorem.md#conditional-extensions) | c132 #7 | untraced |
| PP-OBL-008 | Keep the contract deterministic with the component corpora unchanged | [`diagnostics-and-conformance.md#abstract-public-boundaries`](../60-specification/progress-and-preservation/diagnostics-and-conformance.md#abstract-public-boundaries) | c132 #8 | untraced |

C132 coverage is 0 `traced` and 8 untraced obligations pending the
sibling compiler implementation. The planned dedicated gate rejects
unknown identifiers and fails if any `PP-OBL-*` identifier lacks a
focused tag.

## Open questions

- Registry placement: keep identifiers in this non-normative map (preferred) or
  embed them in each normative `diagnostics-and-conformance.md` chapter, which
  is a per-area normative edit.
- Evidence-link durability: pin cross-repo evidence URLs to an immutable commit
  or reference the `rewrite` path.
- Validator enforcement ramp: warn before failing, so the registry can grow
  incrementally.
- Whether the `SHOULD`/`MAY`/declarative/definitions follow-up is a new
  checklist item or a sub-item of C011.
