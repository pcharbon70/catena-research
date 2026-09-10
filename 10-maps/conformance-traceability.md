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
- [Selective Receive Specification](../60-specification/selective-receive/README.md)
  — the C086 source for `RC-OBL-*` obligations.
- [Exception Boundary Specification](../60-specification/exception-boundary/README.md)
  — the C081 source for `XB-OBL-*` obligations.
- [Top-Level Effects Specification](../60-specification/top-level-effects/README.md)
  — the C082 source for `TL-OBL-*` obligations.

## Identifier and registry convention

An **obligation** is one conformance requirement. In the `MUST`/`MUST NOT`
phase, every obligation receives a permanent, area-scoped identifier of the
form `AREA-OBL-NNN`. The numeric suffix is never reused; if an obligation is
retired its identifier is retired with it, mirroring the checklist's own
convention.

| Area code | Normative area or governance policy | Slice or milestone |
| --- | --- | --- |
| `RS` | resource-scopes | 0.1.51 |
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
| `RC` | selective-receive | 0.1.46 |
| `CK` | closed-capability-kernel | 0.1.50 |
| `XB` | exception-boundary | 0.1.47 |
| `TL` | top-level-effects | 0.1.48 |

The **registry** lives in this map (per-area tables below) and records, for each
obligation:

| Column | Meaning |
| --- | --- |
| ID | The permanent `AREA-OBL-NNN` identifier. |
| Obligation | A short noun phrase for the requirement. |
| Normative or governance anchor | A relative link to the governing heading, e.g. [`syntax-and-safety.md#clause-form`](../60-specification/clause-conditions/syntax-and-safety.md#clause-form). |
| Evidence | The exercising compiler test path and name, plus any stable diagnostic identifier(s). Cross-repo evidence uses a GitHub web link so the archive's local-link check is unaffected. |
| Status | `traced`, `partial`, or `untraced`. |

A registry entry is `traced` only when at least one tagged, passing compiler
test covers the obligation. A test tags its obligations with ExUnit
`@tag obligation: "AREA-OBL-NNN"` (or `obligations: [...]`), scanned by the
compiler coverage check. A tag is an index, not evidence that every required
behavior was exercised. Use `partial` where existing witnesses cover only
part of the obligation or its controlling rule has an unresolved conflict;
record the missing work and its current checklist owner.

## Per-area status

`MUST`/`MUST NOT` counts are fixed precisely when each area's obligation set is
extracted; all current normative areas and the C012 governance policy are
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
| `LC` list-comprehensions | 14 | `c047_list_comprehensions_test.exs` (14) | compiler-tagged + gated (`3216831`); 14 traced; 0 partial after C057 serial acceptance |
| `NR` numeric-relationships | 8 | `c061_numeric_relationships_test.exs` (9) | compiler-tagged + gated (`fd75cb7`); all obligations traced |
| `AN` aliases-and-newtypes | 8 | `c062_aliases_newtypes_test.exs` (11) | compiler-tagged + gated (`1de0a7d`); all obligations traced |
| `RN` name-resolution | 8 | `c066_name_resolution_test.exs` (10) | compiler-tagged + gated (`bef5fd5`); all obligations traced |
| `DU` dynamic-and-unsafe-boundaries | 8 | `c067_dynamic_unsafe_test.exs` (10) | compiler-tagged + gated (`ed14901`); all obligations traced |
| `EA` excluded-advanced-type-features | 7 | `c140_excluded_advanced_test.exs` (8) | compiler-tagged + gated (`77fba75`); all obligations traced |
| `PP` progress-and-preservation | 8 | `c132_progress_preservation_test.exs` (10) | compiler-tagged + gated (`5525662`); all obligations traced |
| `RC` selective-receive | 8 | `c086_selective_receive_test.exs` (6), `c086_receive_completion_test.exs` (4) | historical base plus tested uncommitted 0.1.49 correction; 8 traced; tag inventory is not semantic proof |
| `XB` exception-boundary | 7 | `c081_exception_boundary_test.exs` (7) | compiler-tagged + gated (`e0f2a9e`); all obligations traced |
| `TL` top-level-effects | 7 | `c082_top_level_test.exs` (6) | compiler-tagged + gated (`e962b73`); all obligations traced |

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
| IL-OBL-014 | Aggregate source files, bytes, and decoded nodes meet their portable floors and refuse the next unit distinctly | [`IMPLEMENTATION-LIMITS.md#bootstrap-portable-minima`](../IMPLEMENTATION-LIMITS.md#bootstrap-portable-minima) | resource_exhaustion: LIM006–LIM008 exact thresholds and aggregate small inputs | traced |
| IL-OBL-015 | Aggregate publication output meets its portable floor and refuses before final output changes | [`IMPLEMENTATION-LIMITS.md#limit-diagnostics-and-transactional-failure`](../IMPLEMENTATION-LIMITS.md#limit-diagnostics-and-transactional-failure) | resource_exhaustion: LIM009 boundary; retained package transaction tests | traced |
| IL-OBL-016 | Explicit runtime admission reports limits and applies reject or terminate without silent success | [`IMPLEMENTATION-LIMITS.md#runtime-and-mailbox-capacity`](../IMPLEMENTATION-LIMITS.md#runtime-and-mailbox-capacity) | resource_exhaustion: queue admission, FIFO rejection and terminal overload | traced |
| IL-OBL-017 | Queue cleanup is observable while host-fatal exhaustion remains a disclosed residual | [`IMPLEMENTATION-LIMITS.md#runtime-and-mailbox-capacity`](../IMPLEMENTATION-LIMITS.md#runtime-and-mailbox-capacity) | resource_exhaustion: pressured close, owner death and profile residuals | traced |

C012 coverage is 12 `traced` and 1 governance-only `untraced` obligation.
`IL-OBL-013` is exercised by the C018 decimal-component boundary test and
remains gated with the `NM` set. `IL-OBL-014` through `IL-OBL-017` are
exercised by the C129 aggregate-budget and capacity tests. The compiler
coverage gate explicitly allow-lists IL-OBL-012 because emitting a language
revision is a repository and release-governance decision, not an executable
compiler behavior.

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
- **c025 #12** *keeps the engine deterministic, source-only, and outside P121/P130 phases*

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
| PK-OBL-012 | Keep the engine deterministic, source-only, and outside P121/P130 phases | [`diagnostics-and-conformance.md#revision-and-persistence-separation`](../60-specification/package-identity-and-dependencies/diagnostics-and-conformance.md#revision-and-persistence-separation) | c025 #1, #12 | traced |

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
- **c026 #10** *keeps the wiring deterministic, source-only, and outside P101/P121*

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
| PL-OBL-010 | Keep the wiring deterministic, source-only, and outside P101/P121 phases | [`diagnostics-and-conformance.md#abstract-public-boundaries`](../60-specification/prelude-policy/diagnostics-and-conformance.md#abstract-public-boundaries) | c026 #1, #10 | traced |

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
- **c027 #10** *keeps the wiring deterministic, source-only, and outside P084/P121 machinery*

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
| EN-OBL-010 | Keep the wiring deterministic, source-only, and outside P084/G088/P121 machinery, with compilation roots unchanged | [`diagnostics-and-conformance.md#abstract-public-boundaries`](../60-specification/entry-points/diagnostics-and-conformance.md#abstract-public-boundaries) | c027 #1, #10 | traced |

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
- **c032 #8** *keeps the model deterministic and outside G033/P034/G037/P094/P109 claims with zero new families*

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
| FC-OBL-008 | Keep the model deterministic and outside G033/P034/G037/P094/P109 claims with zero new diagnostic families | [`diagnostics-and-conformance.md#abstract-public-boundaries`](../60-specification/functions-and-calls/diagnostics-and-conformance.md#abstract-public-boundaries) | c032 #8 | traced |

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
- **c034 #8** *keeps the classification deterministic and outside G036/G038/P084/G088/P109 claims with zero new families*

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
| RT-OBL-008 | Keep the classification deterministic and outside G036/G038/P084/G088/P109 claims with zero new families | [`diagnostics-and-conformance.md#abstract-public-boundaries`](../60-specification/recursion-and-termination/diagnostics-and-conformance.md#abstract-public-boundaries) | c034 #8 | traced |

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
- **c036 #8** *keeps the taxonomy deterministic and outside P084/G088/G092/G095/P105/P109 claims with zero new families*

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
| FT-OBL-008 | Keep the taxonomy deterministic and outside P084/G088/G092/G095/P105/P109 claims with zero new families | [`diagnostics-and-conformance.md#abstract-public-boundaries`](../60-specification/runtime-failure-taxonomy/diagnostics-and-conformance.md#abstract-public-boundaries) | c036 #8 | traced |

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
- **c037 #8** *keeps the classification deterministic and outside G080s/P084/P085/G095/G124 claims with zero new families*

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
| RO-OBL-008 | Keep the classification deterministic and outside G080s/P084/P085/G095/G124 claims with zero new families | [`diagnostics-and-conformance.md#abstract-public-boundaries`](../60-specification/resource-observability/diagnostics-and-conformance.md#abstract-public-boundaries) | c037 #8 | traced |

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
- **c038 #8** *keeps the classification deterministic and outside P109/G040/G005/P116/P121 claims with zero new families*

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
| CE-OBL-008 | Keep the classification deterministic and outside P109/G040/G005/P116/P121 claims with zero new families | [`diagnostics-and-conformance.md#abstract-public-boundaries`](../60-specification/compile-time-evaluation/diagnostics-and-conformance.md#abstract-public-boundaries) | c038 #8 | traced |

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
- **c040 #8** *keeps the model deterministic and outside G042/P084/P101/P105/P109 claims with zero new families*

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
| BM-OBL-008 | Keep the model deterministic and outside G042/P084/P101/P105/P109 claims with zero new families | [`diagnostics-and-conformance.md#abstract-public-boundaries`](../60-specification/built-in-data-model/diagnostics-and-conformance.md#abstract-public-boundaries) | c040 #8 | traced |

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
gate rejects unknown identifiers and fails if any `RC-OBL-*` identifier
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
- **c042 #5** *excludes complexity from the language layer, delegating documentation to P101*
- **c042 #6** *fixes duplicate-key behavior as a P101 declaration obligation, explicit in the declaring slice*
- **c042 #7** *rides C035 for ordering and key equality: keys must be comparable*
- **c042 #8** *keeps the contract deterministic and outside P101/P105/P109 claims with zero new families*

Anchors point at the normative 0.1.37 chapters. Status reflects the
merged compiler evidence (`246019f`, branch `agent/c042-collections`).

| ID | Obligation | Normative anchor | Evidence | Status |
| --- | --- | --- | --- | --- |
| CO-OBL-001 | Apply collection behavior only at exact 0.1.37 and register the stable lifecycle addition | [`diagnostics-and-conformance.md#revision-and-persistence-separation`](../60-specification/collection-construction-and-update/diagnostics-and-conformance.md#revision-and-persistence-separation) | c042 #1; EDN001 | traced |
| CO-OBL-002 | Fix the six-topic decision with shipped machinery and named owners | [`the-six-topic-decision.md#the-decision`](../60-specification/collection-construction-and-update/the-six-topic-decision.md#the-decision) | c042 #2 | traced |
| CO-OBL-003 | Keep construction and update as constructor application and match recursion, distinct from records | [`the-six-topic-decision.md#construction-is-construction`](../60-specification/collection-construction-and-update/the-six-topic-decision.md#construction-is-construction) | c042 #3 | traced |
| CO-OBL-004 | Classify a lookup miss as typed failure as a value: total operations, never a trap | [`miss-as-value-and-complexity.md#miss-as-value`](../60-specification/collection-construction-and-update/miss-as-value-and-complexity.md#miss-as-value) | c042 #4 | traced |
| CO-OBL-005 | Exclude complexity from the language layer, delegating documentation to P101 | [`miss-as-value-and-complexity.md#the-complexity-exclusion`](../60-specification/collection-construction-and-update/miss-as-value-and-complexity.md#the-complexity-exclusion) | c042 #5 | traced |
| CO-OBL-006 | Fix duplicate-key behavior as a P101 declaration obligation, explicit in the declaring slice | [`the-six-topic-decision.md#the-decision`](../60-specification/collection-construction-and-update/the-six-topic-decision.md#the-decision) | c042 #6 | traced |
| CO-OBL-007 | Ride C035 for ordering and key equality: keys must be comparable | [`the-six-topic-decision.md#the-decision`](../60-specification/collection-construction-and-update/the-six-topic-decision.md#the-decision) | c042 #7 | traced |
| CO-OBL-008 | Keep the contract deterministic and outside P101/P105/P109 claims with zero new families | [`diagnostics-and-conformance.md#abstract-public-boundaries`](../60-specification/collection-construction-and-update/diagnostics-and-conformance.md#abstract-public-boundaries) | c042 #8 | traced |

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

Anchors point at the normative 0.1.39 chapters. The labels above retain
the original evidence inventory (`3216831`, branch
`agent/c047-comprehensions`); they do not themselves establish completion.
The completion audit supplies the partial classifications below. The
[first implementation follow-up](../50-journal/2026-09-06-language-completion-plan.md#first-implementation-findings)
records additional working-tree evidence in
`test/catena/c047_effects_completion_test.exs`, without promoting those statuses.

| ID | Obligation | Normative anchor | Evidence | Status |
| --- | --- | --- | --- | --- |
| LC-OBL-001 | Apply comprehension rules only at exact 0.1.39, register the lifecycle addition, and declare the LCP families and the elaboration API | [`diagnostics-and-conformance.md#revision-and-persistence-separation`](../60-specification/list-comprehensions/diagnostics-and-conformance.md#revision-and-persistence-separation) | c047 #1 | traced |
| LC-OBL-002 | Fix the grammar's semantic roles and keywords with the adoption boundary at the surface capstone | [`the-surface-contract.md#the-grammars-semantic-roles`](../60-specification/list-comprehensions/the-surface-contract.md#the-grammars-semantic-roles) | c047 #2 | traced |
| LC-OBL-003 | Require `List A` sources with the excluded-source boundary | [`generator-and-qualifier-rules.md#sources`](../60-specification/list-comprehensions/generator-and-qualifier-rules.md#sources) | c047 #3 | traced |
| LC-OBL-004 | Fix left-to-right depth-first traversal with dependency, once-per-prefix source evaluation, and empty-input behavior | [`generator-and-qualifier-rules.md#traversal`](../60-specification/list-comprehensions/generator-and-qualifier-rules.md#traversal) | c047 #4 | traced |
| LC-OBL-005 | Ordinary filters preserve effects, false-as-skip, failures and enclosing-handler abort at 0.1.50 | [Fragment checking](../60-specification/closed-capability-kernel/identity-rows-and-comprehension-target.md#fragment-checking-and-generated-workers) | c047 capability filter, false-filter trap, outer decline and result-type witnesses | traced |
| LC-OBL-006 | Consume C044's split: total ordinary generators, `case` mismatch-as-skip, `LCP002`/`LCP003` markers, `M001` reuse | [`generator-and-qualifier-rules.md#the-pattern-generator-split`](../60-specification/list-comprehensions/generator-and-qualifier-rules.md#the-pattern-generator-split) | c047 #6 | traced |
| LC-OBL-007 | Fix left-to-right scope, non-escaping non-recursive bindings, `LCP001` rebinding, `BS001` reuse | [`generator-and-qualifier-rules.md#scope-and-rebinding`](../60-specification/list-comprehensions/generator-and-qualifier-rules.md#scope-and-rebinding) | c047 #7 | traced |
| LC-OBL-008 | Fix exact order, multiplicity, non-short-circuiting filters, and failure timing with visible effect rows | [`evaluation-effects-and-execution.md#exact-order`](../60-specification/list-comprehensions/evaluation-effects-and-execution.md#exact-order) | c047 #8; capability context/pattern witnesses | traced |
| LC-OBL-009 | Fix eager ordered production with lazy and infinite inputs excluded | [`the-surface-contract.md#eager-ordered-production`](../60-specification/list-comprehensions/the-surface-contract.md#eager-ordered-production) | c047 #9 | traced |
| LC-OBL-010 | Fix the typed qualifier-tree target, the extensional equations, and the no-dispatch rule | [`elaboration-and-lowering.md#the-qualifier-tree-target`](../60-specification/list-comprehensions/elaboration-and-lowering.md#the-qualifier-tree-target) | c047 #10 | traced |
| LC-OBL-011 | Fix `List B` results with all other targets excluded | [`the-surface-contract.md#the-result-type-boundary`](../60-specification/list-comprehensions/the-surface-contract.md#the-result-type-boundary) | c047 #11 | traced |
| LC-OBL-012 | Make sequential execution normative and parallel forms excluded | [`evaluation-effects-and-execution.md#sequential-execution-is-normative`](../60-specification/list-comprehensions/evaluation-effects-and-execution.md#sequential-execution-is-normative) | c047 #12; noncommuting capability handler | traced |
| LC-OBL-013 | Produce the fused tail-recursive worker with linear allocation, source-faithful diagnostics, and cost honesty | [`elaboration-and-lowering.md#the-fused-worker`](../60-specification/list-comprehensions/elaboration-and-lowering.md#the-fused-worker) | c047 #13 | traced |
| LC-OBL-014 | Keep the contract deterministic and outside unowned claims with the reuse map enforced | [`diagnostics-and-conformance.md#abstract-public-boundaries`](../60-specification/list-comprehensions/diagnostics-and-conformance.md#abstract-public-boundaries) | c047 #14 | traced |

Comprehension coverage is 14 `traced`, 0 `partial`, and 0 untraced
obligations. The [completion audit](../50-journal/2026-09-06-checklist-completion-audit.md#comprehension-evidence)
historically reopened P050/P053/P057. The 0.1.50 target now discharges
C050's escaping-filter and enclosing-handler boundary; LC-OBL-005 is traced.
LC-OBL-008 is traced after context/pattern acceptance. LC-OBL-012 is traced
after noncommuting handler results and rejected parallel admission. The complete
closed-target implementation has its own CK registry below.

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
- **c061 #7** *routes division, remainder, and reserved spellings to P105 with no divide or remainder operator existing*
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
| NR-OBL-007 | Route division, remainder, and reserved spellings to P105 with no divide or remainder operator existing | [`exclusions-and-routings.md#division-and-remainder`](../60-specification/numeric-relationships/exclusions-and-routings.md#division-and-remainder) | c061 #7 | traced |
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
- **c140 #2** *keeps all eight forms excluded with the checked profile unchanged*
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
| EA-OBL-002 | Keep all eight forms excluded with the checked profile unchanged | [`the-exclusion-table-and-gate.md#the-exclusion-table`](../60-specification/excluded-advanced-type-features/the-exclusion-table-and-gate.md#the-exclusion-table) | c140 #2 | traced |
| EA-OBL-003 | Keep the seven-point gate as the only amendment route | [`the-exclusion-table-and-gate.md#the-arrival-gate`](../60-specification/excluded-advanced-type-features/the-exclusion-table-and-gate.md#the-arrival-gate) | c140 #3 | traced |
| EA-OBL-004 | Keep rejections identifying the profile boundary | [`the-exclusion-table-and-gate.md#the-exclusion-table`](../60-specification/excluded-advanced-type-features/the-exclusion-table-and-gate.md#the-exclusion-table) | c140 #4 | traced |
| EA-OBL-005 | Keep C068's checked advanced profile checking unchanged | [`the-exclusion-table-and-gate.md#the-exclusion-table`](../60-specification/excluded-advanced-type-features/the-exclusion-table-and-gate.md#the-exclusion-table) | c140 #5 | traced |
| EA-OBL-006 | Admit no omnibus advanced-features revision | [`the-exclusion-table-and-gate.md#the-arrival-gate`](../60-specification/excluded-advanced-type-features/the-exclusion-table-and-gate.md#the-arrival-gate) | c140 #6 | traced |
| EA-OBL-007 | Keep the contract deterministic with no excluded spelling accepted | [`diagnostics-and-conformance.md#abstract-public-boundaries`](../60-specification/excluded-advanced-type-features/diagnostics-and-conformance.md#abstract-public-boundaries) | c140 #7 | traced |

C140 coverage is 7 `traced` and 0 untraced obligations. The dedicated
gate rejects unknown identifiers and fails if any `EA-OBL-*` identifier
lacks a focused tag.

## Progress and preservation registry (`PP`, 0.1.45)

Evidence labels refer to focused tests in
`test/catena/c132_progress_preservation_test.exs` and its
`test/catena/c132_traceability_coverage_test.exs` gate in the sibling
compiler repository. The focused set is:

- **c132 #1** *applies target rules only at exact 0.1.45 with zero new families and the lifecycle registered*
- **c132 #2** *states the effects-and-failure targets over the shipped calculus only*
- **c132 #3** *keeps effect progress and trap terminality as stated with kernel-verbatim reasons*
- **c132 #4** *carries each target's evidence obligation with the C030 dual-agreement discipline*
- **c132 #5** *keeps the integrated theorem as a composed statement with the conditional summary*
- **c132 #6** *keeps the composition lemma a routed proof obligation, never a claim*
- **c132 #7** *keeps the process and foreign extensions conditional and routed to their owners*
- **c132 #8** *keeps the contract deterministic with the component corpora unchanged*

Anchors point at the normative 0.1.45 chapters. Status reflects the
merged compiler evidence (`5525662`, branch `agent/c132-metatheory`).

| ID | Obligation | Normative anchor | Evidence | Status |
| --- | --- | --- | --- | --- |
| PP-OBL-001 | Apply target rules only at exact 0.1.45 and register the stable lifecycle addition with zero new families and no new API | [`diagnostics-and-conformance.md#revision-and-persistence-separation`](../60-specification/progress-and-preservation/diagnostics-and-conformance.md#revision-and-persistence-separation) | c132 #1 | traced |
| PP-OBL-002 | State the effects-and-failure targets over the shipped calculus only | [`the-effects-and-failure-targets.md#the-targets`](../60-specification/progress-and-preservation/the-effects-and-failure-targets.md#the-targets) | c132 #2 | traced |
| PP-OBL-003 | Keep effect progress and trap terminality as stated with kernel-verbatim reasons | [`the-effects-and-failure-targets.md#the-targets`](../60-specification/progress-and-preservation/the-effects-and-failure-targets.md#the-targets) | c132 #3 | traced |
| PP-OBL-004 | Carry each target's evidence obligation with the C030 dual-agreement discipline | [`the-effects-and-failure-targets.md#evidence-obligations`](../60-specification/progress-and-preservation/the-effects-and-failure-targets.md#evidence-obligations) | c132 #4 | traced |
| PP-OBL-005 | Keep the integrated theorem as a composed statement with the conditional summary | [`the-integrated-theorem.md#the-composed-statement`](../60-specification/progress-and-preservation/the-integrated-theorem.md#the-composed-statement) | c132 #5 | traced |
| PP-OBL-006 | Keep the composition lemma a routed proof obligation, never a claim | [`the-integrated-theorem.md#the-composition-lemma`](../60-specification/progress-and-preservation/the-integrated-theorem.md#the-composition-lemma) | c132 #6 | traced |
| PP-OBL-007 | Keep the process and foreign extensions conditional and routed to their owners | [`the-integrated-theorem.md#conditional-extensions`](../60-specification/progress-and-preservation/the-integrated-theorem.md#conditional-extensions) | c132 #7 | traced |
| PP-OBL-008 | Keep the contract deterministic with the component corpora unchanged | [`diagnostics-and-conformance.md#abstract-public-boundaries`](../60-specification/progress-and-preservation/diagnostics-and-conformance.md#abstract-public-boundaries) | c132 #8 | traced |

C132 coverage is 8 `traced` and 0 untraced obligations. The dedicated
gate rejects unknown identifiers and fails if any `PP-OBL-*` identifier
lacks a focused tag.

## Selective receive registry (`RC`, 0.1.46)

Evidence labels refer to focused tests in
`test/catena/c086_selective_receive_test.exs` and its
`test/catena/c086_traceability_coverage_test.exs` gate in the sibling
compiler repository. The focused set is:

- **c086 #1** *applies receive rules only at exact 0.1.46 with zero new families and the lifecycle registered*
- **c086 #2** *keeps the rule set: FIFO scan, preservation, one-time removal, no hidden semantics*
- **c086 #3** *keeps the typing and condition rules: closed message type, effect-free form, portable conditions, CND006*
- **c086 #4** *keeps the starvation statement: honest cost, no fairness claim*
- **c086 #5** *keeps the P109 interface with the timeout clause named as C044's explicit total fallback*
- **c086 #6** *keeps the G088 interface: timeout evaluation, races, totality, and cancellation disposal stated as G088's obligations*
- **c086 #7** *keeps the P087 and P085 interfaces: protocol typing composes, send-side claims stay P085's*
- **c086 #8** *keeps the contract deterministic with the C003/C010 receive corpus unchanged*

Anchors point at the normative 0.1.46 chapters. Status reflects the
merged compiler evidence (`b202887`, branch `agent/c086-receive`).

| ID | Obligation | Normative anchor | Evidence | Status |
| --- | --- | --- | --- | --- |
| RC-OBL-001 | Apply receive rules only at exact 0.1.46 and register the stable lifecycle addition with zero new families and no new API | [`diagnostics-and-conformance.md#revision-and-persistence-separation`](../60-specification/selective-receive/diagnostics-and-conformance.md#revision-and-persistence-separation) | c086 #1 | traced |
| RC-OBL-002 | Keep the rule set: FIFO scan, preservation, one-time removal, no hidden semantics | [`the-receive-rule-set.md#the-rules`](../60-specification/selective-receive/the-receive-rule-set.md#the-rules) | c086 #2 | traced |
| RC-OBL-003 | Keep the typing and condition rules: closed message type, effect-free form, portable conditions, CND006 | [`the-receive-rule-set.md#the-rules`](../60-specification/selective-receive/the-receive-rule-set.md#the-rules) | c086 #3 | traced |
| RC-OBL-004 | No-match suspension, rejected-prefix bypass, examined-candidate cost, no fairness promise at 0.1.49 | [Waiting and scan work](../60-specification/selective-receive-correction/waiting-and-scan-cost-amendment.md#waiting-and-selection) | c086 completion #2–4 | traced |
| RC-OBL-005 | Keep the P109 interface with the timeout clause named as C044's explicit total fallback | [`the-routed-interfaces.md#public-syntax-p109`](../60-specification/selective-receive/the-routed-interfaces.md#public-syntax-p109) | c086 #5 | traced |
| RC-OBL-006 | Keep the G088 interface: timeout evaluation, races, totality, and cancellation disposal stated as G088's obligations | [`the-routed-interfaces.md#timeouts-and-cancellation-g088`](../60-specification/selective-receive/the-routed-interfaces.md#timeouts-and-cancellation-g088) | c086 #6 | traced |
| RC-OBL-007 | Keep the P087 and P085 interfaces: protocol typing composes, send-side claims stay P085's | [`the-routed-interfaces.md#typed-protocols-p087`](../60-specification/selective-receive/the-routed-interfaces.md#typed-protocols-p087) | c086 #7 | traced |
| RC-OBL-008 | Keep the contract deterministic with the C003/C010 receive corpus unchanged | [`diagnostics-and-conformance.md#abstract-public-boundaries`](../60-specification/selective-receive/diagnostics-and-conformance.md#abstract-public-boundaries) | c086 #8 | traced |

Receive coverage is 8 `traced`, 0 `partial`, and 0 untraced obligations for
the amended contract. The original `0.1.46` evidence above remains historical.
The [0.1.49 amendment](../60-specification/selective-receive-correction/waiting-and-scan-cost-amendment.md) replaces RC-OBL-004 and extends RC-OBL-001's
selection/lifecycle boundary. `test/catena/c086_receive_completion_test.exs`
adds **c086 completion #1** (exact correction registration), **#2** (successive
oldest selection and residual mailbox on stepper/BEAM), **#3–4** (empty and
all-rejected waiting on both targets). The tag inventory includes both test
files and is explicitly not semantic proof. The [journal](../50-journal/2026-09-08-capability-kernel-integration.md)
records the tested uncommitted compiler state, not a merged release.

## Exception boundary registry (`XB`, 0.1.47)

Evidence labels refer to focused tests in
`test/catena/c081_exception_boundary_test.exs` and its
`test/catena/c081_traceability_coverage_test.exs` gate in the sibling
compiler repository. The focused set is:

- **c081 #1** *applies partition rules only at exact 0.1.47 with zero new families and the lifecycle registered*
- **c081 #2** *keeps the partition: values, the pattern, and the terminal trap visibly distinct with no silent conversion*
- **c081 #3** *keeps the pattern blessing descriptive: declining to resume aborts to the handler's result, per unchanged C005*
- **c081 #4** *keeps panics as trap kinds entering with their producers*
- **c081 #5** *keeps the routing table's owners: P084, G095/G096, G088, P105, G103*
- **c081 #6** *keeps the reopening door as the only amendment route for a language exception form*
- **c081 #7** *keeps the contract deterministic with the C036/C010 failure corpus unchanged*

Anchors point at the normative 0.1.47 chapters. Status reflects the
merged compiler evidence (`e0f2a9e`, branch `agent/c081-exceptions`).

| ID | Obligation | Normative anchor | Evidence | Status |
| --- | --- | --- | --- | --- |
| XB-OBL-001 | Apply partition rules only at exact 0.1.47 and register the stable lifecycle addition with zero new families and no new API | [`diagnostics-and-conformance.md#revision-and-persistence-separation`](../60-specification/exception-boundary/diagnostics-and-conformance.md#revision-and-persistence-separation) | c081 #1 | traced |
| XB-OBL-002 | Keep the partition: values, the pattern, and the terminal trap visibly distinct with no silent conversion | [`the-mechanism-partition.md#the-partition`](../60-specification/exception-boundary/the-mechanism-partition.md#the-partition) | c081 #2 | traced |
| XB-OBL-003 | Keep the pattern blessing descriptive: declining to resume aborts to the handler's result, per unchanged C005 | [`the-mechanism-partition.md#the-partition`](../60-specification/exception-boundary/the-mechanism-partition.md#the-partition) | c081 #3 | traced |
| XB-OBL-004 | Keep panics as trap kinds entering with their producers | [`the-mechanism-partition.md#panic-classification`](../60-specification/exception-boundary/the-mechanism-partition.md#panic-classification) | c081 #4 | traced |
| XB-OBL-005 | Keep the routing table's owners: P084, G095/G096, G088, P105, G103 | [`the-mechanism-partition.md#the-routing-table`](../60-specification/exception-boundary/the-mechanism-partition.md#the-routing-table) | c081 #5 | traced |
| XB-OBL-006 | Keep the reopening door as the only amendment route for a language exception form | [`the-mechanism-partition.md#the-door`](../60-specification/exception-boundary/the-mechanism-partition.md#the-door) | c081 #6 | traced |
| XB-OBL-007 | Keep the contract deterministic with the C036/C010 failure corpus unchanged | [`diagnostics-and-conformance.md#abstract-public-boundaries`](../60-specification/exception-boundary/diagnostics-and-conformance.md#abstract-public-boundaries) | c081 #7 | traced |

C081 coverage is 7 `traced` and 0 untraced obligations. The dedicated
gate rejects unknown identifiers and fails if any `XB-OBL-*` identifier
lacks a focused tag.

## Top-level effects registry (`TL`, 0.1.48)

Evidence labels refer to focused tests in
`test/catena/c082_top_level_test.exs` and its
`test/catena/c082_traceability_coverage_test.exs` gate in the sibling
compiler repository. The focused set is:

- **c082 #1** *applies boundary rules only at exact 0.1.48 with zero new families and the lifecycle registered*
- **c082 #2** *keeps the boundary: entries leave nothing unhandled and nobody interprets*
- **c082 #3** *keeps launch as invocation only: to completion, no scope, no injection*
- **c082 #4** *keeps the capability interface: explicit typed values via P106's channel or nothing; entry rules bind until then*
- **c082 #5** *keeps no ambient handler reserved and supervision routed as failure-only*
- **c082 #6** *keeps the door: entry-form widening amends C027 explicitly with who-interprets-what stated*
- **c082 #7** *keeps the contract deterministic with the C027 entry corpus unchanged*

Anchors point at the normative 0.1.48 chapters. Status reflects the
merged compiler evidence (`e962b73`, branch `agent/c082-toplevel`).

| ID | Obligation | Normative anchor | Evidence | Status |
| --- | --- | --- | --- | --- |
| TL-OBL-001 | Apply boundary rules only at exact 0.1.48 and register the stable lifecycle addition with zero new families and no new API | [`diagnostics-and-conformance.md#revision-and-persistence-separation`](../60-specification/top-level-effects/diagnostics-and-conformance.md#revision-and-persistence-separation) | c082 #1 | traced |
| TL-OBL-002 | Keep the boundary: entries leave nothing unhandled and nobody interprets | [`the-top-level-boundary.md#the-boundary`](../60-specification/top-level-effects/the-top-level-boundary.md#the-boundary) | c082 #2 | traced |
| TL-OBL-003 | Keep launch as invocation only: to completion, no scope, no injection | [`the-top-level-boundary.md#the-boundary`](../60-specification/top-level-effects/the-top-level-boundary.md#the-boundary) | c082 #3 | traced |
| TL-OBL-004 | Keep the capability interface: explicit typed values via P106's channel or nothing; entry rules bind until then | [`the-top-level-boundary.md#the-capability-interface`](../60-specification/top-level-effects/the-top-level-boundary.md#the-capability-interface) | c082 #4 | traced |
| TL-OBL-005 | Keep no ambient handler reserved and supervision routed as failure-only | [`the-top-level-boundary.md#the-supervision-routing`](../60-specification/top-level-effects/the-top-level-boundary.md#the-supervision-routing) | c082 #5 | traced |
| TL-OBL-006 | Keep the door: entry-form widening amends C027 explicitly with who-interprets-what stated | [`the-top-level-boundary.md#the-door`](../60-specification/top-level-effects/the-top-level-boundary.md#the-door) | c082 #6 | traced |
| TL-OBL-007 | Keep the contract deterministic with the C027 entry corpus unchanged | [`diagnostics-and-conformance.md#abstract-public-boundaries`](../60-specification/top-level-effects/diagnostics-and-conformance.md#abstract-public-boundaries) | c082 #7 | traced |

C082 coverage is 7 `traced` and 0 untraced obligations. The dedicated
gate rejects unknown identifiers and fails if any `TL-OBL-*` identifier
lacks a focused tag.

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

## Closed capability-kernel registry (`CK`, 0.1.50)

The [normative target](../60-specification/closed-capability-kernel/identity-rows-and-comprehension-target.md) defines the compound boundary. Evidence is
in sibling `kernel_capability_integration_test.exs`, `kernel_capability_row_test.exs`,
`kernel_capability_binding_test.exs`, and `c047_capability_comprehension_test.exs`.
The tag-inventory test is bookkeeping, not semantic proof. Tests use the
production deterministic BEAM compiler and the independent reference stepper.

| ID | Obligation | Normative anchor | Evidence | Status |
| --- | --- | --- | --- | --- |
| CK-OBL-001 | Exact selection and retained-format separation | [Input](../60-specification/closed-capability-kernel/identity-rows-and-comprehension-target.md#input-and-selection) | registered boundary test, old selection and metadata | traced |
| CK-OBL-002 | Structural identity and same-family descriptor consistency | [Input](../60-specification/closed-capability-kernel/identity-rows-and-comprehension-target.md#input-and-selection) | identity properties and two-slot handler witness | traced |
| CK-OBL-003 | Closed identity rows and simultaneous instantiation | [Rows](../60-specification/closed-capability-kernel/identity-rows-and-comprehension-target.md#identity-rows-and-lexical-scope) | row laws, subtraction, substitution and malformed rows | traced |
| CK-OBL-004 | Lexical scope, fresh handling and escape rejection | [Scope](../60-specification/closed-capability-kernel/identity-rows-and-comprehension-target.md#identity-rows-and-lexical-scope) | ambient/escaping rejection and enclosing abort | traced |
| CK-OBL-005 | Independent context and fragment row checking | [Probes](../60-specification/closed-capability-kernel/identity-rows-and-comprehension-target.md#fragment-checking-and-generated-workers) | understated/overstated rows and recursive-context rejection | traced |
| CK-OBL-006 | Worker arrow stages and whole-traversal handler scope | [Workers](../60-specification/closed-capability-kernel/identity-rows-and-comprehension-target.md#fragment-checking-and-generated-workers) | exact nested traces, all first/last failures, result-type change | traced |
| CK-OBL-007 | Independent verification and identity-aware CPS | [Verification](../60-specification/closed-capability-kernel/identity-rows-and-comprehension-target.md#verification-and-beam-artifacts) | forged core and recursive reference/BEAM agreement | traced |
| CK-OBL-008 | Fully handled entry and distinct artifact | [Artifact](../60-specification/closed-capability-kernel/identity-rows-and-comprehension-target.md#verification-and-beam-artifacts) | unhandled/latent entry rejection and production metadata | traced |

## Owned resource registry (`RS`, 0.1.51)

The [owned lifetime contract](../60-specification/resource-scopes/owned-lifetime-and-mandatory-cleanup.md)
is normative. Compiler witnesses below are tagged behavioral tests in
`test/catena/resource_*_test.exs`; the separate inventory test checks tags only.
The local contract excludes process-affine foreign resources and forced-loss
cleanup guarantees. General task propagation remains G088.

| Obligation | Requirement | Normative source | Executable witnesses | Status |
| --- | --- | --- | --- | --- |
| RS-OBL-001 | Checked exact compound formation | [Owned lifetime](../60-specification/resource-scopes/owned-lifetime-and-mandatory-cleanup.md#compound-input-and-static-semantics) | kernel #1–2 | traced |
| RS-OBL-002 | Success-only registration | [Owned lifetime](../60-specification/resource-scopes/owned-lifetime-and-mandatory-cleanup.md#acquisition-and-cleanup-order) | execution #4, #6; lifecycle #1, #3 | traced |
| RS-OBL-003 | Reverse cleanup before continuation and actor exit | [Owned lifetime](../60-specification/resource-scopes/owned-lifetime-and-mandatory-cleanup.md#acquisition-and-cleanup-order) | execution #1, #9; process #1 | traced |
| RS-OBL-004 | Real handler resume, abandonment and trap | [Owned lifetime](../60-specification/resource-scopes/owned-lifetime-and-mandatory-cleanup.md#outcomes-and-provenance) | execution #1–2, #6–7 | traced |
| RS-OBL-005 | Primary outcomes, release failure precedence and reentry | [Owned lifetime](../60-specification/resource-scopes/owned-lifetime-and-mandatory-cleanup.md#outcomes-and-provenance) | execution #2–3, #7–9; handle #6; lifecycle #2, #4 | traced |
| RS-OBL-006 | Scoped identity, reads and no escape/capture | [Owned lifetime](../60-specification/resource-scopes/owned-lifetime-and-mandatory-cleanup.md#compound-input-and-static-semantics) | kernel #1; handle #1–3; lifecycle #5 | traced |
| RS-OBL-007 | Owned cancellation and cooperative exit | [Owned lifetime](../60-specification/resource-scopes/owned-lifetime-and-mandatory-cleanup.md#local-cancellation-exit-and-deadlines) | handle #4; lifecycle #6; explorer #1 | traced |
| RS-OBL-008 | Bounded release and eligible deadline races | [Owned lifetime](../60-specification/resource-scopes/owned-lifetime-and-mandatory-cleanup.md#local-cancellation-exit-and-deadlines) | execution #5; lifecycle #7; explorer #2 | traced |
| RS-OBL-009 | Local actor cleanup and explicit external exclusions | [Owned lifetime](../60-specification/resource-scopes/owned-lifetime-and-mandatory-cleanup.md#host-boundary-and-exclusions) | process #1; handle #5; lifecycle #8 | traced |
| RS-OBL-010 | Verified deterministic artifact and closed entry | [Owned lifetime](../60-specification/resource-scopes/owned-lifetime-and-mandatory-cleanup.md#artifacts-diagnostics-and-conformance) | kernel #1, #3 | traced |

Witness numbers follow declaration order within the named resource test file.

## Process lifetime registry (`OT`, 0.1.52)

The [lifetime contract](../60-specification/process-lifetimes/owned-tasks-and-managed-relationships.md)
defines C084. Named witnesses below are in sibling `test/catena/task_*_test.exs`.
The tag inventory is bookkeeping; actual state, cleanup and artifact assertions
supply the evidence. General time tests remain experimental G088 work.

| ID | Obligation | Normative anchor | Evidence | Status |
| --- | --- | --- | --- | --- |
| OT-OBL-001 | Exact verified deterministic artifact and old-format separation | [Artifact](../60-specification/process-lifetimes/owned-tasks-and-managed-relationships.md#diagnostics-and-conformance) | kernel selected artifact; managed_kernel selected artifact and forged entry | traced |
| OT-OBL-002 | Scoped identities and handle escape rejection | [Ownership](../60-specification/process-lifetimes/owned-tasks-and-managed-relationships.md#static-ownership-and-capability-boundary) | kernel escaped/captured handles; runtime stale scope; monitor_kernel escape | traced |
| OT-OBL-003 | Registration before start and normal join | [Scopes](../60-specification/process-lifetimes/owned-tasks-and-managed-relationships.md#structured-lifetime-transitions) | runtime immediate completion and twenty-child join; lifecycle raw-child isolation | traced |
| OT-OBL-004 | First child failure and secondary evidence | [Scopes](../60-specification/process-lifetimes/owned-tasks-and-managed-relationships.md#structured-lifetime-transitions) | runtime sibling failure; kernel outcome evidence; lifecycle first observation | traced |
| OT-OBL-005 | Ordered cleanup and acquisition cancellation | [Scopes](../60-specification/process-lifetimes/owned-tasks-and-managed-relationships.md#structured-lifetime-transitions) | kernel handler abandonment and mixed release order; runtime parent acquisition cancellation | traced |
| OT-OBL-006 | Typed independent terminal monitoring | [Monitors](../60-specification/process-lifetimes/owned-tasks-and-managed-relationships.md#monitored-completion) | monitor independence/absence/duplicate rejection; monitor_kernel CEK and BEAM | traced |
| OT-OBL-007 | Demonitoring and private observer closure | [Monitors](../60-specification/process-lifetimes/owned-tasks-and-managed-relationships.md#monitored-completion) | monitor scope closure and message preservation; lifecycle/OTP demonitor flush | traced |
| OT-OBL-008 | Symmetric links and cleanup before exit | [Links](../60-specification/process-lifetimes/owned-tasks-and-managed-relationships.md#linked-propagation-and-trapping) | managed one-sided registration failure and normal linked exit; monitor_kernel | traced |
| OT-OBL-009 | Unlink and generation races | [Links](../60-specification/process-lifetimes/owned-tasks-and-managed-relationships.md#linked-propagation-and-trapping) | managed remote unlink/relink and absence; managed_reference stale signal and pending remote observation | traced |
| OT-OBL-010 | Trapping selection and restoration | [Links](../60-specification/process-lifetimes/owned-tasks-and-managed-relationships.md#linked-propagation-and-trapping) | monitor_kernel real handler abandonment; managed_reference ignored normal exit; lifecycle delivery selection | traced |
| OT-OBL-011 | Safe points and bounded shutdown | [Cancellation](../60-specification/process-lifetimes/owned-tasks-and-managed-relationships.md#cancellation-and-shutdown-bounds) | kernel virtual expiry and recursive cancellation; runtime forced loss and cleanup; instrument automatic polling | traced |
| OT-OBL-012 | Capability isolation and separate control channels | [Ownership](../60-specification/process-lifetimes/owned-tasks-and-managed-relationships.md#static-ownership-and-capability-boundary) | kernel parent-handler rejection; managed_kernel raw-context rejection and selected receive envelopes | traced |

## Cancellation and time registry (`TM`, 0.1.53)

The [time contract](../60-specification/cancellation-and-time/deadlines-waits-and-cancellation.md)
defines C088. Witnesses are in sibling `task_time_kernel_test.exs` and
`task_time_runtime_test.exs`, with inherited lifetime/expiry evidence in the
owned-task and resource suites. The separate tag inventory is bookkeeping.

| ID | Obligation | Normative anchor | Evidence | Status |
| --- | --- | --- | --- | --- |
| TM-OBL-001 | Exact verified deterministic artifact and old-boundary rejection | [Artifacts](../60-specification/cancellation-and-time/deadlines-waits-and-cancellation.md#diagnostics-artifacts-and-conformance) | time_kernel selected artifacts, wrong selection and forged evidence | traced |
| TM-OBL-002 | Exact duration, large values and virtual eligibility | [Units](../60-specification/cancellation-and-time/deadlines-waits-and-cancellation.md#durations-and-local-origins) | time_kernel positive/negative deadlines; time_runtime large exact conversion | traced |
| TM-OBL-003 | Once-before-scan, zero-time queued match and mailbox preservation | [Receive](../60-specification/cancellation-and-time/deadlines-waits-and-cancellation.md#timed-selective-receive) | time_kernel effectful duration, zero timeout and fallback preservation | traced |
| TM-OBL-004 | Opaque origin and shared absolute budget | [Origins](../60-specification/cancellation-and-time/deadlines-waits-and-cancellation.md#durations-and-local-origins) | time_kernel repeated absolute waits and escape rejection; time_runtime foreign/ended/forged origin | traced |
| TM-OBL-005 | Owned blocking and post-wait cancellation | [Cancellation](../60-specification/cancellation-and-time/deadlines-waits-and-cancellation.md#cancellation-and-completion-choices) | time_kernel raw actor with explicit owned scope and post-wait interruption; retained recursive cancellation | traced |
| TM-OBL-006 | Single selected branch/completion across races | [Choices](../60-specification/cancellation-and-time/deadlines-waits-and-cancellation.md#cancellation-and-completion-choices) | time_kernel reply-before/after selection and post-wait interruption; managed_reference selected linked failure; task_kernel expiry races | traced |
| TM-OBL-007 | Masked cleanup, expiry and foreign exclusion | [Cleanup](../60-specification/cancellation-and-time/deadlines-waits-and-cancellation.md#masking-expiry-and-foreign-boundaries) | time_runtime repeated cancellation during blocked finalization; task_runtime noncooperative forced shutdown | traced |
| TM-OBL-008 | No timer leakage or rejected-message loss | [Waiting](../60-specification/cancellation-and-time/deadlines-waits-and-cancellation.md#relative-and-absolute-waiting) | time_runtime mailbox inspection; time_kernel fallback preservation and nested absolute waits | traced |

## Outcome contract registry (`OV`, 0.1.54)

The [outcome chapter](../60-specification/outcome-contracts/values-sequencing-and-validation.md)
defines C103. The sibling `outcome_contract_test.exs` supplies the following
behavioral witnesses; the [journal](../50-journal/2026-09-08-outcome-contracts.md)
records immutable publication evidence.

| ID | Obligation | Normative source | Executable evidence | Status |
| --- | --- | --- | --- | --- |
| OV-OBL-001 | Explicit digest-bound package and retained formats | [Rule](../60-specification/outcome-contracts/values-sequencing-and-validation.md#status-and-authority) | outcome_contract: deterministic package and tampering tests | traced |
| OV-OBL-002 | Distinct nominal shapes and invalid input rejection | [Rule](../60-specification/outcome-contracts/values-sequencing-and-validation.md#type-shapes-and-separation) | outcome_contract: wrong payload, empty invalid constructor and nested outcomes | traced |
| OV-OBL-003 | Mapping and dependent laws | [Rule](../60-specification/outcome-contracts/values-sequencing-and-validation.md#mapping-and-dependent-sequencing) | outcome_contract: reference/BEAM maps, bounded identity/composition/associativity | traced |
| OV-OBL-004 | Eager binary and skipped dependent callbacks | [Rule](../60-specification/outcome-contracts/values-sequencing-and-validation.md#mapping-and-dependent-sequencing) | outcome_contract: failure callback counts and first failure preservation | traced |
| OV-OBL-005 | Ordered independent accumulation and coherence | [Rule](../60-specification/outcome-contracts/values-sequencing-and-validation.md#independent-accumulation) | outcome_contract: four-combination specialized artifact and absent Workflow instance | traced |
| OV-OBL-006 | Explicit elimination and conversions | [Rule](../60-specification/outcome-contracts/values-sequencing-and-validation.md#explicit-elimination-and-conversion) | outcome_contract: empty sequence, singleton errors, nested absence and adapter counts | traced |
| OV-OBL-007 | Separate traps and process exits | [Rule](../60-specification/outcome-contracts/values-sequencing-and-validation.md#explicit-elimination-and-conversion) | outcome_contract: throw/exit/arithmetic propagation without interception | traced |
| OV-OBL-008 | Deterministic implementation and linear stack-safe accumulation | [Rule](../60-specification/outcome-contracts/values-sequencing-and-validation.md#execution-diagnostics-and-limits) | outcome_contract: repeated compilation/linking and 50,001-error sequence | traced |

## Local protocol contract registry (`LP`, 0.1.55)

The [contract](../60-specification/local-protocol-contracts/schemas-sessions-and-outcomes.md)
and [journal](../50-journal/2026-09-08-local-protocol-contracts.md) define the
explicit local library boundary. Peer event scripts in the reference model
are not a claim that it executes native peers.

| Obligation | Meaning | Normative source | Executable evidence | Status |
| --- | --- | --- | --- | --- |
| LP-OBL-001 | Exact selection and artifact identity | [Rule](../60-specification/local-protocol-contracts/schemas-sessions-and-outcomes.md#status-and-authority) | protocol_program: historical rejection, forged selection and deterministic compile metadata | traced |
| LP-OBL-002 | Closed schema and pre-payload negotiation | [Rule](../60-specification/local-protocol-contracts/schemas-sessions-and-outcomes.md#schema-and-admission) | protocol_contract and protocol_session: malformed schema, digest/version changes, mismatch without request traffic | traced |
| LP-OBL-003 | Checked producers and nominal ownership | [Rule](../60-specification/local-protocol-contracts/schemas-sessions-and-outcomes.md#checked-application-boundary) | protocol_program: wrong producer, unknown/duplicate key, bounds, forged evidence and alternate nominal owner | traced |
| LP-OBL-004 | Correlation and admission credit | [Rule](../60-specification/local-protocol-contracts/schemas-sessions-and-outcomes.md#session-transitions-and-credit) | protocol_model, protocol_session and protocol_program: reversed replies, overload, unread completed credit and observation recovery | traced |
| LP-OBL-005 | Single terminal result and non-resetting time | [Rule](../60-specification/local-protocol-contracts/schemas-sessions-and-outcomes.md#session-transitions-and-credit) | protocol_model: all reply/cancel/expiry permutations; protocol_session: zero time, invalid/late responses and cancellation | traced |
| LP-OBL-006 | Owned cleanup and peer loss | [Rule](../60-specification/local-protocol-contracts/schemas-sessions-and-outcomes.md#time-and-owned-lifetime) | protocol_session: peer death, cancellation joins worker, abandoned aliases and stale handle | traced |
| LP-OBL-007 | Ordinary monitor variant composition | [Rule](../60-specification/local-protocol-contracts/schemas-sessions-and-outcomes.md#representation-composition-and-evidence) | task_monitor_kernel: selected typed observation match agrees on stepper/BEAM; task_time_kernel regression | traced |
| LP-OBL-008 | Independent model and compiled peers | [Rule](../60-specification/local-protocol-contracts/schemas-sessions-and-outcomes.md#representation-composition-and-evidence) | protocol_program: model/native agreement; protocol_session: compiled client exchanges with compiled typed actor | traced |

## Typed supervision registry (`SU`, 0.1.56)

The [contract](../60-specification/typed-supervision/checked-trees-and-lifecycle.md)
and [journal](../50-journal/2026-09-08-typed-supervision.md) define the supported
static worker subset and narrow lifecycle admission.

| ID | Obligation | Normative source | Executable evidence | Status |
| --- | --- | --- | --- | --- |
| SU-OBL-001 | Exact library selection and historical gates | [Rule](../60-specification/typed-supervision/checked-trees-and-lifecycle.md#status-and-authority) | supervision_description: all earlier selections and forged profile rejected; BEAM selection metadata | traced |
| SU-OBL-002 | Strategy and child policy matrix | [Rule](../60-specification/typed-supervision/checked-trees-and-lifecycle.md#supported-policy-inventory) | supervision_model and supervision_runtime: three strategies, temporary collateral removal, transient normal completion | traced |
| SU-OBL-003 | Checked entries and fresh provisioning | [Rule](../60-specification/typed-supervision/checked-trees-and-lifecycle.md#child-entry-and-provisioning) | supervision_description: wrong/parameterized child, captured provisioning, duplicate ID; runtime fresh process per restart | traced |
| SU-OBL-004 | Startup acknowledgment and rollback | [Rule](../60-specification/typed-supervision/checked-trees-and-lifecycle.md#child-entry-and-provisioning) | supervision_runtime: failed start rolls back previous child, repeated immediate body failure | traced |
| SU-OBL-005 | Intensity and stale generation | [Rule](../60-specification/typed-supervision/checked-trees-and-lifecycle.md#restart-intensity-and-generations) | supervision_model: inclusive window and stale identity; supervision_runtime: restart storm terminates tree | traced |
| SU-OBL-006 | Bounded shutdown and cleanup order | [Rule](../60-specification/typed-supervision/checked-trees-and-lifecycle.md#shutdown-and-owned-integration) | supervision_runtime: reverse stop order and noncooperative zero-grace forced termination; description rejects bad bounds | traced |
| SU-OBL-007 | Managed owner and tree failure | [Rule](../60-specification/typed-supervision/checked-trees-and-lifecycle.md#shutdown-and-owned-integration) | supervision_runtime: trapped tree loss, already-dead root join and child cleanup before owner result | traced |
| SU-OBL-008 | Origin-bound deterministic artifacts | [Rule](../60-specification/typed-supervision/checked-trees-and-lifecycle.md#generated-artifacts-and-compatibility) | supervision_description: byte/manifest tampering, deterministic compile, loaded typed worker restart and owned artifact startup | traced |

## OTP compatibility registry (`OC`, 0.1.57)

The [policy](../60-specification/otp-compatibility/support-probes-and-artifacts.md)
and [journal](../50-journal/2026-09-08-otp-compatibility.md) distinguish actual
supported-host execution from simulated rejection fixtures.

| ID | Obligation | Normative source | Executable evidence | Status |
| --- | --- | --- | --- | --- |
| OC-OBL-001 | Retained formats and separate toolchain axis | [Rule](../60-specification/otp-compatibility/support-probes-and-artifacts.md#status-and-authority) | language_version and lifecycle regressions; historical frontends still compile | traced |
| OC-OBL-002 | Exact tested matrix | [Rule](../60-specification/otp-compatibility/support-probes-and-artifacts.md#tested-support-matrix) | otp_profile: measured host equals singleton support row; full corpus on that row | traced |
| OC-OBL-003 | Required facilities and early rejection | [Rule](../60-specification/otp-compatibility/support-probes-and-artifacts.md#observations-and-required-facilities) | otp_profile: every missing facility and altered fingerprint rejected; private probe mailbox empty | traced |
| OC-OBL-004 | Deterministic discovery | [Rule](../60-specification/otp-compatibility/support-probes-and-artifacts.md#observations-and-required-facilities) | otp_profile: repeated discovery equal; language-info/conformance-info regressions | traced |
| OC-OBL-005 | Deterministic fingerprint-bearing artifacts | [Rule](../60-specification/otp-compatibility/support-probes-and-artifacts.md#artifact-provenance-and-loading) | otp_profile: repeated binary equality and compile-info fingerprint/digest | traced |
| OC-OBL-006 | Checked load and entry diagnostics | [Rule](../60-specification/otp-compatibility/support-probes-and-artifacts.md#artifact-provenance-and-loading) | otp_profile: malformed/untagged/mismatched artifacts and entry rejection; separate VM load executes 42 | traced |
| OC-OBL-007 | Evidence-gated expansion | [Rule](../60-specification/otp-compatibility/support-probes-and-artifacts.md#expansion-and-retirement) | otp_profile: unsupported patch/platform fixtures refused; journal labels separate-VM and single-host limits | traced |
| OC-OBL-008 | Explicit retirement and rebuild policy | [Rule](../60-specification/otp-compatibility/support-probes-and-artifacts.md#expansion-and-retirement) | normative review: no scheduled row retirement; old untagged artifact rejected with rebuild diagnostic | traced |


## Value-boundary registry (`VB`, 0.1.58)

The [contract](../60-specification/value-boundaries/carriers-and-checked-conversion.md)
and [journal](../50-journal/2026-09-08-value-boundaries.md) bind observations to
verified layout ownership and retain the exclusions on foreign authority.

| ID | Obligation | Normative source | Executable evidence | Status |
| --- | --- | --- | --- | --- |
| VB-OBL-001 | Exact selection and retained formats | [Rule](../60-specification/value-boundaries/carriers-and-checked-conversion.md#status-and-authority) | value_boundary: exact selection, old interface decoding and persisted-format lists | traced |
| VB-OBL-002 | Descriptor ownership | [Rule](../60-specification/value-boundaries/carriers-and-checked-conversion.md#representation-ownership) | value_boundary: forged descriptor and wrong nominal identity rejected | traced |
| VB-OBL-003 | Primitive invariants | [Rule](../60-specification/value-boundaries/carriers-and-checked-conversion.md#representation-ownership) | value_boundary: independent verifier payload checks; signed zero, UTF-8, scalar range and Bytes | traced |
| VB-OBL-004 | Pure typed tree | [Rule](../60-specification/value-boundaries/carriers-and-checked-conversion.md#pure-value-tree-boundary) | value_boundary: typed Text capture, stepper/native observations and latent process-effect rejection | traced |
| VB-OBL-005 | Independent verification and artifacts | [Rule](../60-specification/value-boundaries/carriers-and-checked-conversion.md#pure-value-tree-boundary) | value_boundary: changed old core rejected; deterministic 0.1.58 artifact provenance | traced |
| VB-OBL-006 | Structural conversion | [Rule](../60-specification/value-boundaries/carriers-and-checked-conversion.md#checked-structural-and-nominal-conversion) | value_boundary: nested records/variants/products, extra fields and malformed ingress | traced |
| VB-OBL-007 | Nominal conversion | [Rule](../60-specification/value-boundaries/carriers-and-checked-conversion.md#checked-structural-and-nominal-conversion) | value_boundary: compact/uniform/fixed round-trips, generic Text, private constructors and improper payloads | traced |
| VB-OBL-008 | Closures and authority exclusions | [Rule](../60-specification/value-boundaries/carriers-and-checked-conversion.md#checked-structural-and-nominal-conversion) | value_boundary: captured closure and raw fun/PID/reference rejection; resource_handle, c004_categorical, kernel_capability_binding suites | traced |
| VB-OBL-009 | Explicit payload budgets | [Rule](../60-specification/value-boundaries/carriers-and-checked-conversion.md#budgets-diagnostics-and-limits) | value_boundary: node/byte exhaustion, empty binary, large integer and deep structures | traced |
| VB-OBL-010 | Inherited compiler limits | [Rule](../60-specification/value-boundaries/carriers-and-checked-conversion.md#budgets-diagnostics-and-limits) | value_boundary: decoded literal at/above configured limit; generated module/arity checks and full limits suite | traced |


## Calling-convention registry (`CV`, 0.1.59)

The [contract](../60-specification/calling-conventions/checked-calls-and-artifact-identity.md)
and [journal](../50-journal/2026-09-09-calling-conventions.md) bind calling
observations to verified artifacts and preserve separately owned foreign work.

| ID | Obligation | Normative source | Executable evidence | Status |
| --- | --- | --- | --- | --- |
| CV-OBL-001 | Exact selection and retained formats | [Rule](../60-specification/calling-conventions/checked-calls-and-artifact-identity.md#status-and-authority) | calling_selection: exact selection, historical core/interface/signed boundaries | traced |
| CV-OBL-002 | Call inventory and typed admission | [Rule](../60-specification/calling-conventions/checked-calls-and-artifact-identity.md#call-classes-and-admission) | calling_descriptor, calling_callback, calling_lifecycle: checked entries and explicit refusals | traced |
| CV-OBL-003 | Written and semantic arity | [Rule](../60-specification/calling-conventions/checked-calls-and-artifact-identity.md#descriptor-and-executable-identity) | calling_descriptor, calling_metadata: spine/BEAM distinction, per-stage effects and private worker arity | traced |
| CV-OBL-004 | Compiler and artifact metadata | [Rule](../60-specification/calling-conventions/checked-calls-and-artifact-identity.md#descriptor-and-executable-identity) | calling_metadata: interface-owned builder, compile-info digest and forged compiler/forms refusal | traced |
| CV-OBL-005 | Rebuild-bound artifact verification | [Rule](../60-specification/calling-conventions/checked-calls-and-artifact-identity.md#descriptor-and-executable-identity) | calling_descriptor, calling_lifecycle: replaced binaries and rewritten digests rejected before entry | traced |
| CV-OBL-006 | Application stages and capture | [Rule](../60-specification/calling-conventions/checked-calls-and-artifact-identity.md#application-stages-and-lifetime) | calling_scope: partial/saturated agreement, independent captures and first-stage trap | traced |
| CV-OBL-007 | Handle ownership and exhaustion | [Rule](../60-specification/calling-conventions/checked-calls-and-artifact-identity.md#application-stages-and-lifetime) | calling_scope, calling_callback: cross-owner, forged, revoked, expired and bounded handles | traced |
| CV-OBL-008 | Synchronous typed callback | [Rule](../60-specification/calling-conventions/checked-calls-and-artifact-identity.md#application-stages-and-lifetime) | calling_callback: separately compiled Erlang ingress, explicit authority and expiry | traced |
| CV-OBL-009 | Retained managed lifecycle | [Rule](../60-specification/calling-conventions/checked-calls-and-artifact-identity.md#application-stages-and-lifetime) | calling_lifecycle: actual child exports, OTP callback arities and owner shutdown | traced |
| CV-OBL-010 | Checked failures and data budgets | [Rule](../60-specification/calling-conventions/checked-calls-and-artifact-identity.md#failures-frames-and-limits) | calling_descriptor, calling_callback: wrong data refusal, callback trap identity; value_boundary budgets | traced |
| CV-OBL-011 | Traceable technical frames | [Rule](../60-specification/calling-conventions/checked-calls-and-artifact-identity.md#failures-frames-and-limits) | calling_metadata: actual trap stack maps to origin, technical frames retained, unknown frame unmapped | traced |
| CV-OBL-012 | Arity and proper-tail limits | [Rule](../60-specification/calling-conventions/checked-calls-and-artifact-identity.md#failures-frames-and-limits) | calling_metadata: private 255-arity CPS worker and million-step saturated/partial tail calls; full limits regressions | traced |


## Erlang-type-boundary registry (`ET`, 0.1.60)

The [contract](../60-specification/erlang-type-boundary/typed-conversion-and-preservation.md)
and [journal](../50-journal/2026-09-09-erlang-type-boundary.md) bind typed
conversion to verified declarations and complete input/output bounds.

| ID | Obligation | Normative source | Executable evidence | Status |
| --- | --- | --- | --- | --- |
| ET-OBL-001 | Exact selection and retained formats | [Rule](../60-specification/erlang-type-boundary/typed-conversion-and-preservation.md#status-and-authority) | foreign_codec: exact selection, forged codec and unchanged executable/interface/signed boundaries | traced |
| ET-OBL-002 | Trusted schema and metadata | [Rule](../60-specification/erlang-type-boundary/typed-conversion-and-preservation.md#trusted-descriptions-and-admitted-meanings) | foreign_codec: re-derived export descriptions and forged metadata rejection | traced |
| ET-OBL-003 | Primitive and structural invariants | [Rule](../60-specification/erlang-type-boundary/typed-conversion-and-preservation.md#trusted-descriptions-and-admitted-meanings) | foreign_codec, foreign_native: nested closed data, UTF-8/scalar/type rejection and finite Float bits | traced |
| ET-OBL-004 | Nominal identity and visibility | [Rule](../60-specification/erlang-type-boundary/typed-conversion-and-preservation.md#trusted-descriptions-and-admitted-meanings) | foreign_codec: compact/uniform/fixed layouts, private sequence and wrong constructors refused; retained value_boundary private-constructor tests | traced |
| ET-OBL-005 | Authority exclusions | [Rule](../60-specification/erlang-type-boundary/typed-conversion-and-preservation.md#trusted-descriptions-and-admitted-meanings) | foreign_codec: raw PID/reference/fun and forged handle refused | traced |
| ET-OBL-006 | Verified proper sequence relation | [Rule](../60-specification/erlang-type-boundary/typed-conversion-and-preservation.md#declared-sequence-relation) | foreign_codec: explicit roles, private/reversed roles, improper lists and bad suffixes refused | traced |
| ET-OBL-007 | Wire and runtime separation | [Rule](../60-specification/erlang-type-boundary/typed-conversion-and-preservation.md#declared-sequence-relation) | foreign_codec: list-to-fixed carrier, both backend literal lowerers and independent verifier | traced |
| ET-OBL-008 | Whole-carrier explicit bounds | [Rule](../60-specification/erlang-type-boundary/typed-conversion-and-preservation.md#whole-carrier-budgets-and-expected-failure) | foreign_codec: exact node/byte/depth thresholds, output depth exhaustion and large scalar witnesses | traced |
| ET-OBL-009 | Expected conversion failure | [Rule](../60-specification/erlang-type-boundary/typed-conversion-and-preservation.md#whole-carrier-budgets-and-expected-failure) | foreign_codec: malformed payload, invalid codec, unsupported carrier and budget reason checks | traced |
| ET-OBL-010 | Preservation | [Rule](../60-specification/erlang-type-boundary/typed-conversion-and-preservation.md#preservation-obligation) | foreign_codec, foreign_native: generated sequence round-trips, independent Erlang nested data and bit-exact finite Float corpus | traced |


## Foreign-adapter registry (`FA`, 0.1.61)

The [contract](../60-specification/foreign-adapters/authority-calls-and-callback-lifetime.md)
and [journal](../50-journal/2026-09-09-foreign-adapters.md) cover the executed
P096 milestone; public syntax and broader callback authority remain open.

| ID | Obligation | Normative source | Executable evidence | Status |
| --- | --- | --- | --- | --- |
| FA-OBL-001 | Exact selection and retained axes | [Rule](../60-specification/foreign-adapters/authority-calls-and-callback-lifetime.md#status-and-authority) | foreign_adapter: exact selection and retained codec/interface/signed boundaries | traced |
| FA-OBL-002 | Pinned host declaration | [Rule](../60-specification/foreign-adapters/authority-calls-and-callback-lifetime.md#explicit-declarations-and-authority) | foreign_adapter: setup denial, altered descriptor and replaced host module refused | traced |
| FA-OBL-003 | Scope-owned explicit grants | [Rule](../60-specification/foreign-adapters/authority-calls-and-callback-lifetime.md#explicit-declarations-and-authority) | foreign_adapter: denied host entry, copied scope and forged call/callback handles | traced |
| FA-OBL-004 | Visible foreign effects | [Rule](../60-specification/foreign-adapters/authority-calls-and-callback-lifetime.md#explicit-declarations-and-authority) | foreign_adapter: actual compiled capability request and terminal trace; no denied host entry | traced |
| FA-OBL-005 | Typed vectors and callback arguments | [Rule](../60-specification/foreign-adapters/authority-calls-and-callback-lifetime.md#typed-calls-and-outcomes) | foreign_adapter: argument arity/type checks, exact callback codecs and wrong result refusal | traced |
| FA-OBL-006 | Trap outcomes | [Rule](../60-specification/foreign-adapters/authority-calls-and-callback-lifetime.md#typed-calls-and-outcomes) | foreign_adapter: foreign raise and typed result trap; bounded diagnostic conversion | traced |
| FA-OBL-007 | Cancellation and completion race | [Rule](../60-specification/foreign-adapters/authority-calls-and-callback-lifetime.md#cooperative-cancellation-and-cleanup) | foreign_adapter: cooperative stop, ignored cancellation then completion, repeated and terminal cancellation | traced |
| FA-OBL-008 | Mandatory cleanup and owner death | [Rule](../60-specification/foreign-adapters/authority-calls-and-callback-lifetime.md#cooperative-cancellation-and-cleanup) | foreign_adapter: outstanding worker termination, owner kill and deliberately stalled cleanup deadline | traced |
| FA-OBL-009 | Verified callback capture | [Rule](../60-specification/foreign-adapters/authority-calls-and-callback-lifetime.md#scoped-compiled-callbacks) | foreign_adapter: immutable captured addition, changed capture/type/name refusal | traced |
| FA-OBL-010 | Scoped publication and revocation | [Rule](../60-specification/foreign-adapters/authority-calls-and-callback-lifetime.md#scoped-compiled-callbacks) | foreign_adapter: explicit callback authority, retained cross-process invocation, revocation and expiry | traced |
| FA-OBL-011 | Overlap and callback worker lifetime | [Rule](../60-specification/foreign-adapters/authority-calls-and-callback-lifetime.md#scoped-compiled-callbacks) | foreign_adapter: nonterminating compiled callback, overlap refusal and release of waiting caller | traced |
| FA-OBL-012 | Checked capability artifact | [Rule](../60-specification/foreign-adapters/authority-calls-and-callback-lifetime.md#checked-capability-program-bridge) | foreign_adapter: matching/missing/wrong-typed bindings, interface builders, forged binary refusal and native execution | traced |


## Native-value-role registry (`NV`, 0.1.62)

The [contract](../60-specification/native-value-roles/typed-admission-and-native-identity.md)
and [journal](../50-journal/2026-09-09-native-value-roles.md) cover C097
native-kind admission, role authority and explicit exclusions.

| ID | Obligation | Normative source | Executable evidence | Status |
| --- | --- | --- | --- | --- |
| NV-OBL-001 | Exact native-role selection | [Rule](../60-specification/native-value-roles/typed-admission-and-native-identity.md#status-and-authority) | native_value: exact 0.1.62, refusal of explicit old selection and unchanged executable/artifact/interface/signed boundaries | traced |
| NV-OBL-002 | Immutable binary and map meaning | [Rule](../60-specification/native-value-roles/typed-admission-and-native-identity.md#immutable-data-mappings) | native_value: one-megabyte Bytes round-trip, bound exhaustion, invalid UTF-8 and unsupported/extra keys | traced |
| NV-OBL-003 | Registered explicit authority | [Rule](../60-specification/native-value-roles/typed-admission-and-native-identity.md#registered-role-authority) | native_value: indexed grants, forged token/role and raw PID/reference refusal | traced |
| NV-OBL-004 | Transferred borrowed process send | [Rule](../60-specification/native-value-roles/typed-admission-and-native-identity.md#borrowed-local-process-send-role) | native_value: checked Int sends, cross-process send-only transfer, borrowed target survival and dead-target Unit | traced |
| NV-OBL-005 | Fresh reference lifetime and role | [Rule](../60-specification/native-value-roles/typed-admission-and-native-identity.md#fresh-correlation-reference-role) | native_value: actual reference host argument, wrong-scope/owner/operation refusal and expired reference | traced |
| NV-OBL-006 | Checked fun admission | [Rule](../60-specification/native-value-roles/typed-admission-and-native-identity.md#functions-and-ports) | native_value: raw fun refusal; foreign_adapter: scoped compiled capture, typed ingress, overlap and expiry | traced |
| NV-OBL-007 | Open and closed port exclusion | [Rule](../60-specification/native-value-roles/typed-admission-and-native-identity.md#functions-and-ports) | native_value: live and closed cat-process port witnesses both refused; explicit port-role refusal | traced |
| NV-OBL-008 | Equality, reflection and type checks | [Rule](../60-specification/native-value-roles/typed-admission-and-native-identity.md#value-equality-and-transport-checking) | native_value: Values classification/comparison, checker role-operation and forged equality flag rejection | traced |
| NV-OBL-009 | Bounds and ownership cleanup | [Rule](../60-specification/native-value-roles/typed-admission-and-native-identity.md#lifetime-and-limits) | native_value: grant/send capacity, expired handles and borrowed target preservation; retained foreign_adapter bounded cleanup | traced |


## C098 native service obligations

The [contract](../60-specification/native-services/signed-loading-and-owned-execution.md)
and [journal](../50-journal/2026-09-09-native-services.md) connect signed native
admission to actual port and disposable-VM NIF witnesses.

| Obligation | Subject | Normative source | Executable evidence | Status |
| --- | --- | --- | --- | --- |
| NI-OBL-001 | Exact native envelope | [Rule](../60-specification/native-services/signed-loading-and-owned-execution.md#status-and-authority) | native_services: signed metadata, retained version discovery | traced |
| NI-OBL-002 | External trust and identity | [Rule](../60-specification/native-services/signed-loading-and-owned-execution.md#explicit-package-authority) | native_services: unsigned/tampered/missing trust/kind/size/obligation refusal | traced |
| NI-OBL-003 | Scheduler declarations | [Rule](../60-specification/native-services/signed-loading-and-owned-execution.md#scheduling-and-native-trust) | native_services: wrong scheduler refusal and actual enif_thread_type observation | traced |
| NI-OBL-004 | Native crash scope | [Rule](../60-specification/native-services/signed-loading-and-owned-execution.md#scheduling-and-native-trust) | native_services: port crash isolation and native abort in disposable VM | traced |
| NI-OBL-005 | Typed finite Float ABI | [Rule](../60-specification/native-services/signed-loading-and-owned-execution.md#typed-calls-and-transport) | native_services: finite bit patterns, nonfinite and wrong-type rejection | traced |
| NI-OBL-006 | Bounded waits | [Rule](../60-specification/native-services/signed-loading-and-owned-execution.md#deadlines-and-failure) | native_services: port timeout/reaping and NIF timeout with poisoned scope | traced |
| NI-OBL-007 | Owned close and fallback | [Rule](../60-specification/native-services/signed-loading-and-owned-execution.md#owned-lifetime-and-finalization) | native_services: double close, GC fallback, owner death, expiry and private release token | traced |
| NI-OBL-008 | Failure inventory | [Rule](../60-specification/native-services/signed-loading-and-owned-execution.md#diagnostics-and-conformance) | native_services: native_services suite admission/load/call/close outcomes | traced |


## C100 debugging metadata obligations

The [contract](../60-specification/debugging-metadata/verified-origins-and-redacted-frames.md)
and [journal](../50-journal/2026-09-09-debugging-metadata.md) connect source-bound
sidecars to executed generated-code failures and evidence-erasure checks.

| Obligation | Subject | Normative source | Executable evidence | Status |
| --- | --- | --- | --- | --- |
| DB-OBL-001 | Explicit debug profile | [Rule](../60-specification/debugging-metadata/verified-origins-and-redacted-frames.md#status-and-authority) | debugging_metadata: exact artifact/source selection and retained format discovery | traced |
| DB-OBL-002 | Source and node identity | [Rule](../60-specification/debugging-metadata/verified-origins-and-redacted-frames.md#input-source-and-node-identity) | debugging_metadata: normalized path refusal, deterministic rebuild and changed input/binary rejection | traced |
| DB-OBL-003 | Original Unicode coordinates | [Rule](../60-specification/debugging-metadata/verified-origins-and-redacted-frames.md#input-source-and-node-identity) | debugging_metadata: ordinary JSON expression, byte/scalar split, CRLF and dotted-key disambiguation | traced |
| DB-OBL-004 | Bounded generated origins | [Rule](../60-specification/debugging-metadata/verified-origins-and-redacted-frames.md#lowered-locations-and-origin-chains) | debugging_metadata: escaped closure, handler and actual inline expansion chains | traced |
| DB-OBL-005 | Actual runtime frames | [Rule](../60-specification/debugging-metadata/verified-origins-and-redacted-frames.md#lowered-locations-and-origin-chains) | debugging_metadata: physical source faults, different-runtime refusal and unmapped host frames | traced |
| DB-OBL-006 | Foreign authority and disclosure | [Rule](../60-specification/debugging-metadata/verified-origins-and-redacted-frames.md#foreign-entry-and-disclosure-boundary) | debugging_metadata: granted/denied foreign entry, redacted host reason and checked tuple disclosure | traced |
| DB-OBL-007 | External evidence and verification | [Rule](../60-specification/debugging-metadata/verified-origins-and-redacted-frames.md#verification-and-evidence-erasure) | debugging_metadata: tampered/missing sidecars and unchanged BEAM after erased-checker change | traced |
| DB-OBL-008 | Retention and limits | [Rule](../60-specification/debugging-metadata/verified-origins-and-redacted-frames.md#retention-modes-and-limits) | debugging_metadata: stripped frames and source/node/inline/history bounds | traced |

## C102 collection protocols

The [contract](../60-specification/collection-protocols/finite-families-and-owned-pulls.md)
and [journal](../50-journal/2026-09-09-collection-protocols.md) connect finite
families and owned pulls to ordinary compiled and independent model evidence.

| Obligation | Contract | Rule | Evidence | Status |
| --- | --- | --- | --- | --- |
| CL-OBL-001 | Exact ordinary package | [Rule](../60-specification/collection-protocols/finite-families-and-owned-pulls.md#status-and-authority) | collection_protocol: compilation, package identity and retained revision discovery | traced |
| CL-OBL-002 | Semantic order | [Rule](../60-specification/collection-protocols/finite-families-and-owned-pulls.md#finite-families-and-order) | collection_protocol: signed-zero identity and fabricated/unsupported order refusal | traced |
| CL-OBL-003 | Strict construction | [Rule](../60-specification/collection-protocols/finite-families-and-owned-pulls.md#construction-lookup-and-update) | collection_protocol: first duplicate and immutable typed lookup/replacement | traced |
| CL-OBL-004 | Explicit combining | [Rule](../60-specification/collection-protocols/finite-families-and-owned-pulls.md#construction-lookup-and-update) | collection_protocol: input-order traps and independent Int associativity equations | traced |
| CL-OBL-005 | Lawful pure transformations | [Rule](../60-specification/collection-protocols/finite-families-and-owned-pulls.md#mapping-folds-and-traversal) | collection_protocol: specialized BEAM identity/composition/folds and compiled effectful callback rejection | traced |
| CL-OBL-006 | Ordered outcome traversal | [Rule](../60-specification/collection-protocols/finite-families-and-owned-pulls.md#mapping-folds-and-traversal) | collection_protocol: accumulated errors, empty values and dependent skip versus independent trap | traced |
| CL-OBL-007 | Pull authority | [Rule](../60-specification/collection-protocols/finite-families-and-owned-pulls.md#owned-pull-protocol) | collection_iterator: absent grants and cross-owner/expired handles | traced |
| CL-OBL-008 | Demand and lifetime | [Rule](../60-specification/collection-protocols/finite-families-and-owned-pulls.md#owned-pull-protocol) | collection_iterator: no eager pull, early cap, compiled pure stop, abandonment and owner death | traced |
| CL-OBL-009 | Cancellation and cleanup | [Rule](../60-specification/collection-protocols/finite-families-and-owned-pulls.md#owned-pull-protocol) | collection_iterator: timeout, step exhaustion, last-state release and failed-release single attempt | traced |
| CL-OBL-010 | Costs and budgets | [Rule](../60-specification/collection-protocols/finite-families-and-owned-pulls.md#costs-bounds-and-failure) | collection_protocol/collection_iterator: 50,000-element equations, result bounds and explicit pull limits | traced |

## C104 text and binary model

The [contract](../60-specification/text-binary-model/units-unicode-and-checked-binary-operations.md)
and [journal](../50-journal/2026-09-09-text-binary-model.md) bind explicit text
semantics to pinned primary data and executable ordinary/tree adoption.

| Obligation | Contract | Rule | Evidence | Status |
| --- | --- | --- | --- | --- |
| TB-OBL-001 | Exact profile and data | [Rule](../60-specification/text-binary-model/units-unicode-and-checked-binary-operations.md#status-and-authority) | text_unicode/text_program: table manifest, exact artifact and retained discovery | traced |
| TB-OBL-002 | Distinct nominal units | [Rule](../60-specification/text-binary-model/units-unicode-and-checked-binary-operations.md#index-units-and-nominal-roles) | text_program/text_binary: compiled nominal conversion, wrong constructor and mixed units | traced |
| TB-OBL-003 | Checked slices | [Rule](../60-specification/text-binary-model/units-unicode-and-checked-binary-operations.md#measurement-and-slices) | text_binary: empty/huge/reversed bounds, scalar split and byte slicing | traced |
| TB-OBL-004 | Pinned graphemes | [Rule](../60-specification/text-binary-model/units-unicode-and-checked-binary-operations.md#pinned-unicode-algorithms) | text_unicode: all 766 official vectors and contextual long runs | traced |
| TB-OBL-005 | Explicit normalization | [Rule](../60-specification/text-binary-model/units-unicode-and-checked-binary-operations.md#pinned-unicode-algorithms) | text_unicode: all 20,034 vector equations and supplementary scalar invariant | traced |
| TB-OBL-006 | Strict encodings | [Rule](../60-specification/text-binary-model/units-unicode-and-checked-binary-operations.md#strict-encoding-conversion) | text_binary: UTF-8/16/32 round trips, malformed offsets and BOM/noncharacter preservation | traced |
| TB-OBL-007 | Pure formatting | [Rule](../60-specification/text-binary-model/units-unicode-and-checked-binary-operations.md#pure-composition-and-format-roles) | text_binary/text_program: typed fragments, compiled formatting and no implicit normalization | traced |
| TB-OBL-008 | Binary matching | [Rule](../60-specification/text-binary-model/units-unicode-and-checked-binary-operations.md#sequential-binary-pattern-contract) | text_binary: independent integer model, declared fields and whole-input mismatch | traced |
| TB-OBL-009 | Typed compiled adoption | [Rule](../60-specification/text-binary-model/units-unicode-and-checked-binary-operations.md#retained-input-compiled-adoption) | text_program: both lowering owners, fixed pipeline types and early dependent failure | traced |
| TB-OBL-010 | Rebuilt artifact identity | [Rule](../60-specification/text-binary-model/units-unicode-and-checked-binary-operations.md#retained-input-compiled-adoption) | text_program: changed sidecar/steps refusal and exact-code reuse versus module conflict | traced |
| TB-OBL-011 | Carrier and operation bounds | [Rule](../60-specification/text-binary-model/units-unicode-and-checked-binary-operations.md#bounds-and-costs) | text_binary/text_program: complete output budgets, huge slices and typed descriptors | traced |
| TB-OBL-012 | Declared cost scope | [Rule](../60-specification/text-binary-model/units-unicode-and-checked-binary-operations.md#bounds-and-costs) | text_unicode/text_binary: long combining/contextual runs and oversized segment refusal without requested allocation | traced |

## C105 numeric library

The [contract](../60-specification/numeric-library/checked-arithmetic-and-explicit-rounding.md)
and [journal](../50-journal/2026-09-09-numeric-library.md) bind numeric promises to
independent rational evidence and compiled/reference execution.

| Obligation | Contract | Rule | Evidence | Status |
| --- | --- | --- | --- | --- |
| NL-OBL-001 | Exact profile | [Rule](../60-specification/numeric-library/checked-arithmetic-and-explicit-rounding.md#status-and-authority) | numeric_program: exact artifact identity and nominal package | traced |
| NL-OBL-002 | Euclidean arithmetic | [Rule](../60-specification/numeric-library/checked-arithmetic-and-explicit-rounding.md#integer-arithmetic-and-division) | numeric_library: signed identities and 5001-digit input | traced |
| NL-OBL-003 | Finite Float operations | [Rule](../60-specification/numeric-library/checked-arithmetic-and-explicit-rounding.md#finite-binary64-arithmetic) | numeric_library: 6688 independent Fraction vectors and finite boundary bits | traced |
| NL-OBL-004 | Trap versus typed answer | [Rule](../60-specification/numeric-library/checked-arithmetic-and-explicit-rounding.md#primitive-traps-and-typed-answers) | numeric_program: compiled primitive overflow versus checked failure | traced |
| NL-OBL-005 | Explicit conversions | [Rule](../60-specification/numeric-library/checked-arithmetic-and-explicit-rounding.md#explicit-conversions) | numeric_library: midpoint, very large Int and decimal loss | traced |
| NL-OBL-006 | Ordinary decimal contexts | [Rule](../60-specification/numeric-library/checked-arithmetic-and-explicit-rounding.md#decimal-package-and-contexts) | numeric_program/numeric_library: ordinary constructor/eliminator and forged context | traced |
| NL-OBL-007 | Single decimal rounding | [Rule](../60-specification/numeric-library/checked-arithmetic-and-explicit-rounding.md#decimal-package-and-contexts) | numeric_library/numeric_program: declared modes, precision and compiled division | traced |
| NL-OBL-008 | Deterministic text conversion | [Rule](../60-specification/numeric-library/checked-arithmetic-and-explicit-rounding.md#parsing-and-formatting) | numeric_library: over 2000 exact bit round trips and malformed/huge exponent input | traced |
| NL-OBL-009 | Validated math scope | [Rule](../60-specification/numeric-library/checked-arithmetic-and-explicit-rounding.md#mathematical-functions-and-admission) | numeric_library: exact root midpoint bounds and unsupported sine refusal | traced |
| NL-OBL-010 | Typed operations | [Rule](../60-specification/numeric-library/checked-arithmetic-and-explicit-rounding.md#typed-compiled-and-reference-adoption) | numeric_program: both input owners, incompatible steps, early failure and 253/254 caps | traced |
| NL-OBL-011 | Rebuilt execution identity | [Rule](../60-specification/numeric-library/checked-arithmetic-and-explicit-rounding.md#typed-compiled-and-reference-adoption) | numeric_program: sidecar mutation, repeated reuse and loaded conflict | traced |
| NL-OBL-012 | Costs and budgets | [Rule](../60-specification/numeric-library/checked-arithmetic-and-explicit-rounding.md#bounds-and-costs) | numeric_library: large integers, parser/decimal limits and complete input/output budgets | traced |


## C106 environmental effects

The [contract](../60-specification/environmental-effects/explicit-authority-and-closed-launches.md)
and [journal](../50-journal/2026-09-09-environmental-effects.md) distinguish actual
host observations from the checked launch and authority rules. Tests are in
`test/catena/environment_{kernel,policy,runtime,program}_test.exs` in the sibling compiler.

| Obligation | Contract | Rule | Behavioral witness | Status |
| --- | --- | --- | --- | --- |
| EV-OBL-001 | Exact profile | [Rule](../60-specification/environmental-effects/explicit-authority-and-closed-launches.md#status-and-authority) | environment_kernel: exact scalar/capability profile and retained refusal | traced |
| EV-OBL-002 | Entry amendment | [Rule](../60-specification/environmental-effects/explicit-authority-and-closed-launches.md#versioned-entry-amendment) | environment_program: compiled explicit entry and missing/forged bindings | traced |
| EV-OBL-003 | Closed launch | [Rule](../60-specification/environmental-effects/explicit-authority-and-closed-launches.md#versioned-entry-amendment) | environment_program: empty authority, local handler and absent grant | traced |
| EV-OBL-004 | Authority identity | [Rule](../60-specification/environmental-effects/explicit-authority-and-closed-launches.md#authority-transport-and-attenuation) | environment_runtime: nonce forgery and cross-owner refusal; retained capability-scope suite | traced |
| EV-OBL-005 | Attenuation | [Rule](../60-specification/environmental-effects/explicit-authority-and-closed-launches.md#authority-transport-and-attenuation) | environment_policy/environment_runtime: resource escalation, expiry and descendant revocation | traced |
| EV-OBL-006 | Service shapes | [Rule](../60-specification/environmental-effects/explicit-authority-and-closed-launches.md#service-contracts) | environment_policy: all operation codecs; environment_runtime: eight real services | traced |
| EV-OBL-007 | Whole answers | [Rule](../60-specification/environmental-effects/explicit-authority-and-closed-launches.md#service-contracts) | environment_runtime: wrong-service failure and oversized output refusal | traced |
| EV-OBL-008 | Relative file access | [Rule](../60-specification/environmental-effects/explicit-authority-and-closed-launches.md#filesystem-and-network-confinement) | environment_runtime: real read/write, symlink and escape refusal | traced |
| EV-OBL-009 | Exact TCP authority | [Rule](../60-specification/environmental-effects/explicit-authority-and-closed-launches.md#filesystem-and-network-confinement) | environment_runtime: loopback exchange and ungranted alias refusal | traced |
| EV-OBL-010 | Owned child and devices | [Rule](../60-specification/environmental-effects/explicit-authority-and-closed-launches.md#host-process-and-device-ownership) | environment_runtime: explicit devices, exact child input and PID reaping | traced |
| EV-OBL-011 | Terminal arbitration | [Rule](../60-specification/environmental-effects/explicit-authority-and-closed-launches.md#lifetime-cancellation-and-shutdown) | environment_runtime: cancel/revoke/expiry and one completed event per request | traced |
| EV-OBL-012 | Mandatory release | [Rule](../60-specification/environmental-effects/explicit-authority-and-closed-launches.md#lifetime-cancellation-and-shutdown) | environment_runtime: owner death, source trap and suspended-worker cleanup failure | traced |
| EV-OBL-013 | Executable identity | [Rule](../60-specification/environmental-effects/explicit-authority-and-closed-launches.md#artifact-and-manifest-boundary) | environment_program: compiled/reference trace, sidecar mutation and manifest refusal | traced |
| EV-OBL-014 | Bounds | [Rule](../60-specification/environmental-effects/explicit-authority-and-closed-launches.md#bounds-and-costs) | environment_policy/environment_runtime: policy bounds, request cap and whole-carrier refusal | traced |


## C101 minimum prelude

The [contract](../60-specification/minimum-prelude/explicit-minimum-and-component-identity.md)
and [journal](../50-journal/2026-09-09-minimum-prelude.md) bind the new assembly to
`test/catena/minimum_prelude_test.exs` and its retained source fixtures in the sibling compiler.
Existing family laws remain traced by C004 and C102–C106.

| Obligation | Contract | Rule | Behavioral witness | Status |
| --- | --- | --- | --- | --- |
| MP-OBL-001 | Exact scope | [Rule](../60-specification/minimum-prelude/explicit-minimum-and-component-identity.md#status-and-authority) | minimum_prelude: catalog identity and retained hierarchy | traced |
| MP-OBL-002 | Semantic families | [Rule](../60-specification/minimum-prelude/explicit-minimum-and-component-identity.md#minimum-semantic-inventory) | minimum_prelude: five compiled modules plus inherited outcome/collection/text/numeric law suites | traced |
| MP-OBL-003 | Explicit services | [Rule](../60-specification/minimum-prelude/explicit-minimum-and-component-identity.md#minimum-semantic-inventory) | minimum_prelude: real compiled I/O denied without actual authority | traced |
| MP-OBL-004 | Foundation laws | [Rule](../60-specification/minimum-prelude/explicit-minimum-and-component-identity.md#ordinary-foundation-meaning) | minimum_prelude: 61-input identity/composition/product laws, reference identity and callback order | traced |
| MP-OBL-005 | Pinned content | [Rule](../60-specification/minimum-prelude/explicit-minimum-and-component-identity.md#exact-package-and-component-selection) | minimum_prelude: rehashed changed catalog and hierarchy refusal | traced |
| MP-OBL-006 | Selection shape | [Rule](../60-specification/minimum-prelude/explicit-minimum-and-component-identity.md#exact-package-and-component-selection) | minimum_prelude: missing/duplicate packages, extra fields and wrong version/digest | traced |
| MP-OBL-007 | Dependency replay | [Rule](../60-specification/minimum-prelude/explicit-minimum-and-component-identity.md#prelude-dependency-and-names) | minimum_prelude: actual five-interface lock generation and exact content replay | traced |
| MP-OBL-008 | Opt-out and names | [Rule](../60-specification/minimum-prelude/explicit-minimum-and-component-identity.md#prelude-dependency-and-names) | minimum_prelude: empty application, absent standard nominal type and conflicting aliases | traced |
| MP-OBL-009 | Ordinary delivery | [Rule](../60-specification/minimum-prelude/explicit-minimum-and-component-identity.md#checked-executable-delivery) | minimum_prelude: compiled transformation and validation via selected nominal interfaces | traced |
| MP-OBL-010 | Checked entry selection | [Rule](../60-specification/minimum-prelude/explicit-minimum-and-component-identity.md#checked-executable-delivery) | minimum_prelude: numeric/reference, Unicode and explicitly authorized compiled service execution | traced |
| MP-OBL-011 | Bounds and costs | [Rule](../60-specification/minimum-prelude/explicit-minimum-and-component-identity.md#bounds-costs-and-exclusions) | minimum_prelude: oversized manifest and component capacity plus inherited carrier/source limits | traced |


## C126 trusted computing base

The [contract](../60-specification/trusted-computing-base/guarantees-assumptions-and-boundary-checks.md)
and [journal](../50-journal/2026-09-09-trusted-computing-base.md) bind guarantee
claims to `test/catena/trust_boundary_test.exs` and the checked machine inventory
in the sibling compiler. Undetected semantic changes remain explicit residual trust.

| Obligation | Contract | Rule | Behavioral witness | Status |
| --- | --- | --- | --- | --- |
| TC-OBL-001 | Exact disclosure | [Rule](../60-specification/trusted-computing-base/guarantees-assumptions-and-boundary-checks.md#status-and-authority) | trust_boundary: profile identity and false proof/sandbox flags | traced |
| TC-OBL-002 | Guarantee graph | [Rule](../60-specification/trusted-computing-base/guarantees-assumptions-and-boundary-checks.md#guarantee-specific-graph) | trust_boundary: 12 guarantees and complete unique source ownership | traced |
| TC-OBL-003 | Structural checking | [Rule](../60-specification/trusted-computing-base/guarantees-assumptions-and-boundary-checks.md#independent-checks-and-their-limits) | trust_boundary: ordinary/kernel forged types and kernel effect evidence | traced |
| TC-OBL-004 | Lowering trust | [Rule](../60-specification/trusted-computing-base/guarantees-assumptions-and-boundary-checks.md#independent-checks-and-their-limits) | trust_boundary: wrong OTP result accepted; exact original artifact refuses substituted bytes | traced |
| TC-OBL-005 | Proof scope | [Rule](../60-specification/trusted-computing-base/guarantees-assumptions-and-boundary-checks.md#independent-checks-and-their-limits) | trust_boundary: well-typed changed source accepted; profile disclaims proof verification | traced |
| TC-OBL-006 | Authenticity distinction | [Rule](../60-specification/trusted-computing-base/guarantees-assumptions-and-boundary-checks.md#authenticity-and-ingress) | trust_boundary: valid signature on unsupported claim; changed payload refused | traced |
| TC-OBL-007 | Typed ingress | [Rule](../60-specification/trusted-computing-base/guarantees-assumptions-and-boundary-checks.md#authenticity-and-ingress) | trust_boundary: nested malformed UTF-8 and forged authority refusal | traced |
| TC-OBL-008 | Source/data coverage | [Rule](../60-specification/trusted-computing-base/guarantees-assumptions-and-boundary-checks.md#executable-source-and-data-inventory) | trust_boundary: current inventory, new/missing paths, native format and build-literal mutations | traced |
| TC-OBL-009 | Scanner limits | [Rule](../60-specification/trusted-computing-base/guarantees-assumptions-and-boundary-checks.md#executable-source-and-data-inventory) | trust_boundary: comments ignored, guard-only difference not detected and Python input not executed | traced |
| TC-OBL-010 | Maintained profile | [Rule](../60-specification/trusted-computing-base/guarantees-assumptions-and-boundary-checks.md#profile-and-maintenance) | trust_boundary: canonical profile forgery refusal and machine conformance disclosure | traced |
| TC-OBL-011 | Bounds and costs | [Rule](../60-specification/trusted-computing-base/guarantees-assumptions-and-boundary-checks.md#bounds-and-reporting) | trust_boundary: oversized source refused and finite syntax/data audit | traced |


## C127 trusted obligation policy

The [policy contract](../60-specification/trusted-obligation-policy/transitive-disclosure-and-scoped-admission.md)
and [journal](../50-journal/2026-09-09-trusted-obligation-policy.md) bind the following
obligations to `test/catena/trusted_policy_test.exs` in the sibling compiler.
Underlying unsafe exclusions and native/foreign enforcement retain their original witnesses.

| Obligation | Contract | Rule | Behavioral witness | Status |
| --- | --- | --- | --- | --- |
| TP-OBL-001 | Exact policy | [Rule](../60-specification/trusted-obligation-policy/transitive-disclosure-and-scoped-admission.md#status-and-authority) | trusted_policy: revision disclosure preserves retained executable/signed formats; c067_dynamic_unsafe exclusions | traced |
| TP-OBL-002 | Derived obligations | [Rule](../60-specification/trusted-obligation-policy/transitive-disclosure-and-scoped-admission.md#obligations-and-responsibility) | trusted_policy: verified pure/foreign/native inputs; forged core/artifact refusal | traced |
| TP-OBL-003 | Evidence limits | [Rule](../60-specification/trusted-obligation-policy/transitive-disclosure-and-scoped-admission.md#obligations-and-responsibility) | trusted_policy: host-safety flag false; native and host obligation records remain visible | traced |
| TP-OBL-004 | Transitive closure | [Rule](../60-specification/trusted-obligation-policy/transitive-disclosure-and-scoped-admission.md#exact-dependency-closure) | trusted_policy: diamond closure, missing/cyclic/duplicate/unreachable graph rejection | traced |
| TP-OBL-005 | Owner-qualified identity | [Rule](../60-specification/trusted-obligation-policy/transitive-disclosure-and-scoped-admission.md#exact-dependency-closure) | trusted_policy: package renaming/version replacement and signed native replacement require new grants | traced |
| TP-OBL-006 | Artifact binding | [Rule](../60-specification/trusted-obligation-policy/transitive-disclosure-and-scoped-admission.md#interface-and-artifact-exposure) | trusted_policy: rehashed omission decodes but fails rebinding to checked inputs | traced |
| TP-OBL-007 | Explicit admission | [Rule](../60-specification/trusted-obligation-policy/transitive-disclosure-and-scoped-admission.md#scoped-admission) | trusted_policy: missing grants and incomplete acknowledgements deny transitive application entry | traced |
| TP-OBL-008 | Scoped attenuation | [Rule](../60-specification/trusted-obligation-policy/transitive-disclosure-and-scoped-admission.md#scoped-admission) | trusted_policy: forgery/cross-owner refusal, subset checks, escaped scope and owner-death expiry | traced |
| TP-OBL-009 | Revocation | [Rule](../60-specification/trusted-obligation-policy/transitive-disclosure-and-scoped-admission.md#scoped-admission) | trusted_policy: existing/future descendants denied; child revocation preserves parent | traced |
| TP-OBL-010 | Checked execution | [Rule](../60-specification/trusted-obligation-policy/transitive-disclosure-and-scoped-admission.md#execution) | trusted_policy: actual compiled pure/foreign entries and signed native service execution | traced |
| TP-OBL-011 | Bounds and refusal | [Rule](../60-specification/trusted-obligation-policy/transitive-disclosure-and-scoped-admission.md#limits-and-refusal) | trusted_policy: graph/sidecar/grant/scope limits, unchanged grants after denied attenuation, conformance disclosure | traced |

## C131 secret capabilities

The [secret contract](../60-specification/secret-capabilities/sealed-values-and-protected-delivery.md)
and [journal](../50-journal/2026-09-09-secret-capabilities.md) bind these obligations
to `test/catena/secret_capabilities_test.exs` and retained language version tests.

| Obligation | Contract | Rule | Behavioral witness | Status |
| --- | --- | --- | --- | --- |
| SK-OBL-001 | Exact revision | [Rule](../60-specification/secret-capabilities/sealed-values-and-protected-delivery.md#status-and-authority) | language_version: revision 72 and retained formats | traced |
| SK-OBL-002 | Explicit retrieval | [Rule](../60-specification/secret-capabilities/sealed-values-and-protected-delivery.md#sealed-values) | secret_capabilities: supplied input and authorized environment lookup; missing provider denied | traced |
| SK-OBL-003 | Sealed operations | [Rule](../60-specification/secret-capabilities/sealed-values-and-protected-delivery.md#sealed-values) | secret_capabilities: base64/hex/concat and nested reply projection remain references | traced |
| SK-OBL-004 | Scope narrowing | [Rule](../60-specification/secret-capabilities/sealed-values-and-protected-delivery.md#scope-and-lineage) | secret_capabilities: ownership, forgery, subset, expiry and owner death | traced |
| SK-OBL-005 | Origin lifetime | [Rule](../60-specification/secret-capabilities/sealed-values-and-protected-delivery.md#scope-and-lineage) | secret_capabilities: parent-derived value, pending job and completed reply preserve child revocation | traced |
| SK-OBL-006 | Recipient delivery | [Rule](../60-specification/secret-capabilities/sealed-values-and-protected-delivery.md#checked-delivery) | secret_capabilities: exact foreign descriptor and approved process stdin | traced |
| SK-OBL-007 | Network boundary | [Rule](../60-specification/secret-capabilities/sealed-values-and-protected-delivery.md#checked-delivery) | secret_capabilities: actual loopback broker and refused remote grant | traced |
| SK-OBL-008 | Cleanup publication | [Rule](../60-specification/secret-capabilities/sealed-values-and-protected-delivery.md#checked-delivery) | secret_capabilities: cancellation, crash, owner death and actual forced seven-second deadline | traced |
| SK-OBL-009 | Protected observations | [Rule](../60-specification/secret-capabilities/sealed-values-and-protected-delivery.md#public-observations-and-artifacts) | secret_capabilities: marker/nested redaction, fixed context diagnostics/traces, status and sensitivity restoration | traced |
| SK-OBL-010 | Artifact refusal | [Rule](../60-specification/secret-capabilities/sealed-values-and-protected-delivery.md#public-observations-and-artifacts) | secret_capabilities: canonical JSON/JCS and assurance refusal, closed crash reason | traced |
| SK-OBL-011 | Compiled entry | [Rule](../60-specification/secret-capabilities/sealed-values-and-protected-delivery.md#compiled-entry) | secret_capabilities: actual compiled Unit entry, absent provider and changed artifact refusal | traced |
| SK-OBL-012 | Value bounds | [Rule](../60-specification/secret-capabilities/sealed-values-and-protected-delivery.md#limits-and-exhaustion) | secret_capabilities: input/transformation/storage object limits and malformed setup | traced |
| SK-OBL-013 | Exhaustion outcome | [Rule](../60-specification/secret-capabilities/sealed-values-and-protected-delivery.md#limits-and-exhaustion) | secret_capabilities: no truncation, scope capacity, actual force deadline and false erasure/host-secrecy profile | traced |

## C128 reproducible builds

The [reproducibility contract](../60-specification/reproducible-builds/exact-inputs-and-canonical-packages.md)
and [journal](../50-journal/2026-09-09-reproducible-packages.md) bind the following
obligations to `test/catena/reproducible_package_test.exs` and revision discovery.

| Obligation | Contract | Rule | Behavioral witness | Status |
| --- | --- | --- | --- | --- |
| RB-OBL-001 | Exact scope | [Rule](../60-specification/reproducible-builds/exact-inputs-and-canonical-packages.md#status-and-authority) | reproducible_package: revision discovery and fixed profile; retained package compilation | traced |
| RB-OBL-002 | Complete envelope | [Rule](../60-specification/reproducible-builds/exact-inputs-and-canonical-packages.md#input-envelope) | reproducible_package: changed files and generator declarations change identity; forged input refused | traced |
| RB-OBL-003 | Toolchain identity | [Rule](../60-specification/reproducible-builds/exact-inputs-and-canonical-packages.md#input-envelope) | reproducible_package: wrong compiler rejected before build; verified cache identity | traced |
| RB-OBL-004 | Acquired bytes | [Rule](../60-specification/reproducible-builds/exact-inputs-and-canonical-packages.md#input-envelope) | reproducible_package: changed supplied lock bytes change identity; full interface and assurance outputs | traced |
| RB-OBL-005 | Closed generators | [Rule](../60-specification/reproducible-builds/exact-inputs-and-canonical-packages.md#generators-and-environment) | reproducible_package: declared public environment generator executes; missing and arbitrary generator refused | traced |
| RB-OBL-006 | Sensitivity and events | [Rule](../60-specification/reproducible-builds/exact-inputs-and-canonical-packages.md#generators-and-environment) | reproducible_package: marked file/environment input refused; build-only manifest admission | traced |
| RB-OBL-007 | Fresh roots | [Rule](../60-specification/reproducible-builds/exact-inputs-and-canonical-packages.md#independent-build-roots) | reproducible_package: existing root contents preserved; traversal and absolute paths refused | traced |
| RB-OBL-008 | Logical paths | [Rule](../60-specification/reproducible-builds/exact-inputs-and-canonical-packages.md#independent-build-roots) | reproducible_package: independent roots under changed environment produce identical bytes | traced |
| RB-OBL-009 | Complete outputs | [Rule](../60-specification/reproducible-builds/exact-inputs-and-canonical-packages.md#independent-build-roots) | reproducible_package: four-file package and empty package two-file output; temporary root removed | traced |
| RB-OBL-010 | Canonical metadata | [Rule](../60-specification/reproducible-builds/exact-inputs-and-canonical-packages.md#canonical-full-output-archive) | reproducible_package: order independence, fixed mode/time, duplicates and modified metadata rejected | traced |
| RB-OBL-011 | Rebuild assurance | [Rule](../60-specification/reproducible-builds/exact-inputs-and-canonical-packages.md#canonical-full-output-archive) | reproducible_package: rehashed substituted output decodes but full rebuild verification refuses it | traced |
| RB-OBL-012 | Atomic publication | [Rule](../60-specification/reproducible-builds/exact-inputs-and-canonical-packages.md#publication-and-interruption) | reproducible_package: staging cancellation/corruption and actual owner death preserve prior destination | traced |
| RB-OBL-013 | Capacity refusal | [Rule](../60-specification/reproducible-builds/exact-inputs-and-canonical-packages.md#limits-and-variability-register) | reproducible_package: oversized file, file count, generator and public environment bounds; machine profile | traced |

## C130 supply-chain policy

The [registry contract](../60-specification/supply-chain-policy/signed-registry-and-immutable-acquisition.md)
and [journal](../50-journal/2026-09-10-signed-package-registry.md) bind these
obligations to `test/catena/package_registry_test.exs`, the trusted-boundary audit,
and retained revision tests.

| Obligation | Contract | Rule | Behavioral witness | Status |
| --- | --- | --- | --- | --- |
| RG-OBL-001 | Exact scope | [Rule](../60-specification/supply-chain-policy/signed-registry-and-immutable-acquisition.md#status-and-authority) | package_registry: revision/profile and real source build; native safety and governance remain separate | traced |
| RG-OBL-002 | Root shape | [Rule](../60-specification/supply-chain-policy/signed-registry-and-immutable-acquisition.md#trust-roots-and-rotation) | package_registry: canonical root, exact fields, derived key identities and forged loaded-root refusal | traced |
| RG-OBL-003 | Root rotation | [Rule](../60-specification/supply-chain-policy/signed-registry-and-immutable-acquisition.md#trust-roots-and-rotation) | package_registry: old-plus-new normal threshold, missing-new denial and recovery authority | traced |
| RG-OBL-004 | Snapshot authenticity | [Rule](../60-specification/supply-chain-policy/signed-registry-and-immutable-acquisition.md#signed-snapshots-and-history) | package_registry: signed canonical opening, persisted-client reconstruction and mutation refusal | traced |
| RG-OBL-005 | Monotonic history | [Rule](../60-specification/supply-chain-policy/signed-registry-and-immutable-acquisition.md#signed-snapshots-and-history) | package_registry: rollback, equivocation and attempted post-compromise restoration refusal | traced |
| RG-OBL-006 | Publisher/status separation | [Rule](../60-specification/supply-chain-policy/signed-registry-and-immutable-acquisition.md#publisher-authority-and-immutable-releases) | package_registry: publisher-signed artifacts plus registry-signed status; altered artifact invalidates signature | traced |
| RG-OBL-007 | Source provenance | [Rule](../60-specification/supply-chain-policy/signed-registry-and-immutable-acquisition.md#publisher-authority-and-immutable-releases) | package_registry: C025 environment resolution/lock and exact C128 plan/build from acquired source | traced |
| RG-OBL-008 | Native provenance | [Rule](../60-specification/supply-chain-policy/signed-registry-and-immutable-acquisition.md#publisher-authority-and-immutable-releases) | package_registry: package/content/toolchain/platform/obligation binding and wrong-platform refusal | traced |
| RG-OBL-009 | Current acquisition | [Rule](../60-specification/supply-chain-policy/signed-registry-and-immutable-acquisition.md#acquisition-mirrors-and-status) | package_registry: explicit observation, expired metadata, yanked new acquisition and unsupported options refuse | traced |
| RG-OBL-010 | Mirror bytes | [Rule](../60-specification/supply-chain-policy/signed-registry-and-immutable-acquisition.md#acquisition-mirrors-and-status) | package_registry: first exact mirror accepted; replacement and empty mirror set refused | traced |
| RG-OBL-011 | Lock replay | [Rule](../60-specification/supply-chain-policy/signed-registry-and-immutable-acquisition.md#acquisition-mirrors-and-status) | package_registry: assurance-level C025 replay and snapshot-bound lock mutation refusal | traced |
| RG-OBL-012 | Offline/compromise | [Rule](../60-specification/supply-chain-policy/signed-registry-and-immutable-acquisition.md#offline-and-compromise-semantics) | package_registry: yanked exact offline replay succeeds; observed compromised replay fails | traced |
| RG-OBL-013 | Bounded refusal | [Rule](../60-specification/supply-chain-policy/signed-registry-and-immutable-acquisition.md#limits-refusal-and-host-trust) | package_registry: metadata/canonical rejection and machine-reported ceilings | traced |
| RG-OBL-014 | Residual trust | [Rule](../60-specification/supply-chain-policy/signed-registry-and-immutable-acquisition.md#limits-refusal-and-host-trust) | trust_boundary: registry source/calls classified; profile names root/time/key residuals | traced |

## C129 resource exhaustion

The [resource-exhaustion contract](../60-specification/resource-exhaustion/aggregate-budgets-and-runtime-admission.md)
defines aggregate compiler limits and explicit bounded runtime admission at
revision `0.1.75`.

| Obligation | Requirement | Normative anchor | Compiler evidence | Status |
| --- | --- | --- | --- | --- |
| RX-OBL-001 | Scope and retained boundaries | [Rule](../60-specification/resource-exhaustion/aggregate-budgets-and-runtime-admission.md#status-and-authority) | resource_exhaustion: lifecycle/profile revision; raw send unchanged | traced |
| RX-OBL-002 | Aggregate source count and bytes | [Rule](../60-specification/resource-exhaustion/aggregate-budgets-and-runtime-admission.md#aggregate-compiler-input) | resource_exhaustion: exact file/byte thresholds and many-small-source acceptance | traced |
| RX-OBL-003 | Aggregate decoded nodes | [Rule](../60-specification/resource-exhaustion/aggregate-budgets-and-runtime-admission.md#aggregate-compiler-input) | resource_exhaustion: exact recursive node threshold and next-unit LIM008 refusal | traced |
| RX-OBL-004 | Compiler integration | [Rule](../60-specification/resource-exhaustion/aggregate-budgets-and-runtime-admission.md#aggregate-compiler-input) | resource_exhaustion plus retained JSON/kernel/SCC/package suites | traced |
| RX-OBL-005 | Pre-publication output budget | [Rule](../60-specification/resource-exhaustion/aggregate-budgets-and-runtime-admission.md#publication-and-diagnostics) | resource_exhaustion: output threshold; retained package transaction tests | traced |
| RX-OBL-006 | Stable aggregate diagnostics | [Rule](../60-specification/resource-exhaustion/aggregate-budgets-and-runtime-admission.md#publication-and-diagnostics) | resource_exhaustion: LIM006–LIM009 exact observed values; c012 profile details | traced |
| RX-OBL-007 | Refusal classification | [Rule](../60-specification/resource-exhaustion/aggregate-budgets-and-runtime-admission.md#publication-and-diagnostics) | c012 implementation-limit/evidence-bound distinction and transactional compiler APIs | traced |
| RX-OBL-008 | Queue bounds and accounting | [Rule](../60-specification/resource-exhaustion/aggregate-budgets-and-runtime-admission.md#explicit-bounded-runtime-queues) | resource_exhaustion: message/byte admission and external-size profile | traced |
| RX-OBL-009 | Authority and FIFO | [Rule](../60-specification/resource-exhaustion/aggregate-budgets-and-runtime-admission.md#explicit-bounded-runtime-queues) | resource_exhaustion: several producers, owner-only operations, ordered take and forged-handle refusal | traced |
| RX-OBL-010 | Reject overload | [Rule](../60-specification/resource-exhaustion/aggregate-budgets-and-runtime-admission.md#explicit-bounded-runtime-queues) | resource_exhaustion: explicit overload with intact FIFO payloads and rejection count | traced |
| RX-OBL-011 | Terminate overload | [Rule](../60-specification/resource-exhaustion/aggregate-budgets-and-runtime-admission.md#explicit-bounded-runtime-queues) | resource_exhaustion: capacity-exhausted return, owner event and process exit | traced |
| RX-OBL-012 | Cancellation and cleanup | [Rule](../60-specification/resource-exhaustion/aggregate-budgets-and-runtime-admission.md#explicit-bounded-runtime-queues) | resource_exhaustion: full-queue close reports discard and owner death cancels | traced |
| RX-OBL-013 | Host-fatal residuals | [Rule](../60-specification/resource-exhaustion/aggregate-budgets-and-runtime-admission.md#denial-of-service-and-residual-failure) | conformance profile and trust inventory disclose no host-fatal recovery | traced |
| RX-OBL-014 | Raw and remote exclusions | [Rule](../60-specification/resource-exhaustion/aggregate-budgets-and-runtime-admission.md#denial-of-service-and-residual-failure) | resource_exhaustion: raw-send status false; P085/G091 owner references | traced |
| RX-OBL-015 | Complete profile and suite | [Rule](../60-specification/resource-exhaustion/aggregate-budgets-and-runtime-admission.md#profile-and-conformance) | resource_exhaustion, c008, c012, language_version and trust_boundary suites | traced |

## C091 distribution

The [distribution contract](../60-specification/distribution/typed-authenticated-transport.md)
defines authenticated typed remote transport at revision `0.1.76`.

| Obligation | Requirement | Normative anchor | Compiler evidence | Status |
| --- | --- | --- | --- | --- |
| DS-OBL-001 | Exact scope and revision | [Rule](../60-specification/distribution/typed-authenticated-transport.md#status-and-authority) | distribution: lifecycle/profile revision and local-handle separation | traced |
| DS-OBL-002 | Endpoint identity | [Rule](../60-specification/distribution/typed-authenticated-transport.md#endpoint-and-peer-identity) | distribution: distinct valid contracts and digest mutation refusal | traced |
| DS-OBL-003 | Peer authorization | [Rule](../60-specification/distribution/typed-authenticated-transport.md#endpoint-and-peer-identity) | distribution: certificate, service and package mismatch refusal | traced |
| DS-OBL-004 | Mutual application greeting | [Rule](../60-specification/distribution/typed-authenticated-transport.md#endpoint-and-peer-identity) | distribution: successful mutual ready and server-side policy refusal observed by client | traced |
| DS-OBL-005 | TLS carrier | [Rule](../60-specification/distribution/typed-authenticated-transport.md#transport-and-framing) | distribution: separate CA-signed client/server certificates over TLS 1.3 socket | traced |
| DS-OBL-006 | Exact frame binding | [Rule](../60-specification/distribution/typed-authenticated-transport.md#transport-and-framing) | distribution: stable round trip, unknown-field and noncanonical refusal | traced |
| DS-OBL-007 | Typed canonical values | [Rule](../60-specification/distribution/typed-authenticated-transport.md#transport-and-framing) | distribution: integer and nominal payload round trips; exact float/profile declaration | traced |
| DS-OBL-008 | Authority exclusion | [Rule](../60-specification/distribution/typed-authenticated-transport.md#transport-and-framing) | distribution: process value rejected; wire implementation avoids external-term decode | traced |
| DS-OBL-009 | Ingress limits | [Rule](../60-specification/distribution/typed-authenticated-transport.md#limits-and-refusal) | distribution: oversized frame refusal and disclosed byte/node/depth/digit limits | traced |
| DS-OBL-010 | Configuration disclosure | [Rule](../60-specification/distribution/typed-authenticated-transport.md#limits-and-refusal) | distribution profile plus exact TLS configuration validation | traced |
| DS-OBL-011 | Pending admission | [Rule](../60-specification/distribution/typed-authenticated-transport.md#delivery-and-partition-semantics) | distribution: disconnected and over-capacity preparation refuse | traced |
| DS-OBL-012 | Partition outcomes | [Rule](../60-specification/distribution/typed-authenticated-transport.md#delivery-and-partition-semantics) | distribution: prepared maps to not-enqueued; transmitted maps to delivery-unknown | traced |
| DS-OBL-013 | Retry and duplicates | [Rule](../60-specification/distribution/typed-authenticated-transport.md#delivery-and-partition-semantics) | distribution: exact duplicate suppressed, conflicting duplicate rejected, no automatic retry | traced |
| DS-OBL-014 | Reconnection | [Rule](../60-specification/distribution/typed-authenticated-transport.md#delivery-and-partition-semantics) | distribution: pending clear and fresh authenticated reconnect | traced |
| DS-OBL-015 | Compatibility | [Rule](../60-specification/distribution/typed-authenticated-transport.md#compatibility-and-ordering) | distribution: differing local-protocol revision refused at handshake | traced |
| DS-OBL-016 | Profile and complete suite | [Rule](../60-specification/distribution/typed-authenticated-transport.md#diagnostics-and-conformance) | distribution, lifecycle, language_version and trust_boundary suites | traced |

## C085 message semantics

The [message contract](../60-specification/message-semantics/values-capacity-and-transport.md)
integrates local, capacity-sensitive, foreign/native, and remote behavior at
revision `0.1.77`.

| Obligation | Requirement | Normative anchor | Compiler evidence | Status |
| --- | --- | --- | --- | --- |
| MS-OBL-001 | Exact scope and revision | [Rule](../60-specification/message-semantics/values-capacity-and-transport.md#status-and-authority) | message_semantics and lifecycle: exact revision; retained frontends | traced |
| MS-OBL-002 | Trusted message descriptor | [Rule](../60-specification/message-semantics/values-capacity-and-transport.md#message-values-and-observations) | message_semantics: exact codec round trip and invalid payload refusal | traced |
| MS-OBL-003 | Sendable data and authority | [Rule](../60-specification/message-semantics/values-capacity-and-transport.md#message-values-and-observations) | value_boundary plus native_value: data and borrowed local process role | traced |
| MS-OBL-004 | Excluded carriers | [Rule](../60-specification/message-semantics/values-capacity-and-transport.md#message-values-and-observations) | foreign_codec, native_value, secret_capabilities and distribution negative cases | traced |
| MS-OBL-005 | Copy/share opacity | [Rule](../60-specification/message-semantics/values-capacity-and-transport.md#message-values-and-observations) | message_semantics: immutable binary snapshot and profile observations | traced |
| MS-OBL-006 | Unit and dead target | [Rule](../60-specification/message-semantics/values-capacity-and-transport.md#local-raw-send) | message_semantics, task_kernel and native_value dead-target cases | traced |
| MS-OBL-007 | Sender order | [Rule](../60-specification/message-semantics/values-capacity-and-transport.md#local-raw-send) | message_semantics: two producers; retained kernel and selective-receive suites | traced |
| MS-OBL-008 | Raw capacity boundary | [Rule](../60-specification/message-semantics/values-capacity-and-transport.md#local-raw-send) | resource_exhaustion: explicit queue and host-fatal/raw-send profile | traced |
| MS-OBL-009 | Checked local send | [Rule](../60-specification/message-semantics/values-capacity-and-transport.md#checked-local-and-bounded-admission) | message_semantics: valid, invalid and dead-target checked sends | traced |
| MS-OBL-010 | Checked capacity admission | [Rule](../60-specification/message-semantics/values-capacity-and-transport.md#checked-local-and-bounded-admission) | message_semantics: pre-accounting refusal, success, overload and FIFO | traced |
| MS-OBL-011 | Capacity disclosure | [Rule](../60-specification/message-semantics/values-capacity-and-transport.md#checked-local-and-bounded-admission) | conformance_info and resource_exhaustion profile assertions | traced |
| MS-OBL-012 | Foreign snapshot | [Rule](../60-specification/message-semantics/values-capacity-and-transport.md#foreign-and-native-boundaries) | foreign_codec and value_boundary complete conversion/budget corpus | traced |
| MS-OBL-013 | Native send role | [Rule](../60-specification/message-semantics/values-capacity-and-transport.md#foreign-and-native-boundaries) | native_value: live/expired/forged handles, mailbox codec and operation budget | traced |
| MS-OBL-014 | Remote outcomes | [Rule](../60-specification/message-semantics/values-capacity-and-transport.md#remote-transport) | distribution: not-enqueued, delivery-unknown and admitted transitions | traced |
| MS-OBL-015 | Retry and skew | [Rule](../60-specification/message-semantics/values-capacity-and-transport.md#remote-transport) | distribution: duplicates, protocol skew and no automatic retry | traced |
| MS-OBL-016 | Profile and complete suite | [Rule](../60-specification/message-semantics/values-capacity-and-transport.md#diagnostics-and-conformance) | message_semantics plus retained message/resource/native/distribution suites | traced |

## C090 scheduler observability

The [scheduler contract](../60-specification/scheduler-observability/policy-classes-and-visible-limits.md)
defines observable schedule and foreign-work limits at revision `0.1.78`.

| Obligation | Requirement | Normative anchor | Compiler evidence | Status |
| --- | --- | --- | --- | --- |
| SC-OBL-001 | Exact scope and revision | [Rule](../60-specification/scheduler-observability/policy-classes-and-visible-limits.md#status-and-authority) | scheduler_observability and lifecycle exact revision | traced |
| SC-OBL-002 | Preserved semantics | [Rule](../60-specification/scheduler-observability/policy-classes-and-visible-limits.md#observable-schedule-semantics) | retained kernel, message, effect, resource and authority suites | traced |
| SC-OBL-003 | Reduction opacity | [Rule](../60-specification/scheduler-observability/policy-classes-and-visible-limits.md#observable-schedule-semantics) | scheduler profile validation and mutation refusal | traced |
| SC-OBL-004 | No fairness claim | [Rule](../60-specification/scheduler-observability/policy-classes-and-visible-limits.md#observable-schedule-semantics) | scheduler profile false deterministic/fairness fields; kernel quiescence cases | traced |
| SC-OBL-005 | Runtime preemption | [Rule](../60-specification/scheduler-observability/policy-classes-and-visible-limits.md#preemption-and-priorities) | profile runtime-defined preemption and unobservable-count fields | traced |
| SC-OBL-006 | Deployment priorities | [Rule](../60-specification/scheduler-observability/policy-classes-and-visible-limits.md#preemption-and-priorities) | scheduler policy accepts exact low/normal/high set and rejects invalid options | traced |
| SC-OBL-007 | Exact work classes | [Rule](../60-specification/scheduler-observability/policy-classes-and-visible-limits.md#foreign-work-classes) | scheduler_observability: Catena, foreign, native, unknown and unsafe cases | traced |
| SC-OBL-008 | Existing adapter duties | [Rule](../60-specification/scheduler-observability/policy-classes-and-visible-limits.md#foreign-work-classes) | retained foreign_adapter and native_services suites | traced |
| SC-OBL-009 | Worker capacity | [Rule](../60-specification/scheduler-observability/policy-classes-and-visible-limits.md#capacity-and-blocking-isolation) | scheduler_observability: exact one-worker exhaustion and token release | traced |
| SC-OBL-010 | Blocking isolation | [Rule](../60-specification/scheduler-observability/policy-classes-and-visible-limits.md#capacity-and-blocking-isolation) | scheduler_observability: independent process advances beside owned blocking worker | traced |
| SC-OBL-011 | Capacity disclosure | [Rule](../60-specification/scheduler-observability/policy-classes-and-visible-limits.md#capacity-and-blocking-isolation) | scheduler profile and invalid-policy tests | traced |
| SC-OBL-012 | Bounded exploration | [Rule](../60-specification/scheduler-observability/policy-classes-and-visible-limits.md#reference-exploration-and-evidence) | scheduler_observability and c010: multiple schedules and exhausted bound | traced |
| SC-OBL-013 | Evidence scope | [Rule](../60-specification/scheduler-observability/policy-classes-and-visible-limits.md#reference-exploration-and-evidence) | explorer reports set/bounds without runtime timing claims | traced |
| SC-OBL-014 | Profile and complete suite | [Rule](../60-specification/scheduler-observability/policy-classes-and-visible-limits.md#diagnostics-and-conformance) | scheduler_observability, c010, foreign_adapter, native_services and trust_boundary | traced |

## C092 hot code upgrade

The [upgrade contract](../60-specification/hot-code-upgrade/checked-migration-and-activation.md)
defines checked migration and activation at revision `0.1.79`.

| Obligation | Requirement | Normative anchor | Compiler evidence | Status |
| --- | --- | --- | --- | --- |
| HU-OBL-001 | Scope and revision | [Rule](../60-specification/hot-code-upgrade/checked-migration-and-activation.md#status-and-authority) | hot_code_upgrade and lifecycle exact revision | traced |
| HU-OBL-002 | Exact descriptor | [Rule](../60-specification/hot-code-upgrade/checked-migration-and-activation.md#upgrade-descriptor-and-preflight) | upgrade descriptor shape and digest validation | traced |
| HU-OBL-003 | Semantic compatibility | [Rule](../60-specification/hot-code-upgrade/checked-migration-and-activation.md#upgrade-descriptor-and-preflight) | Package.Compat integration and wrong-module refusal | traced |
| HU-OBL-004 | Node version set | [Rule](../60-specification/hot-code-upgrade/checked-migration-and-activation.md#upgrade-descriptor-and-preflight) | unsupported third node version refused | traced |
| HU-OBL-005 | Quiescence blockers | [Rule](../60-specification/hot-code-upgrade/checked-migration-and-activation.md#quiescence-and-coexistence) | live capability blocker and exact blocker inventory | traced |
| HU-OBL-006 | Coexistence ceiling | [Rule](../60-specification/hot-code-upgrade/checked-migration-and-activation.md#quiescence-and-coexistence) | second upgrade refused while draining | traced |
| HU-OBL-007 | Drain messages | [Rule](../60-specification/hot-code-upgrade/checked-migration-and-activation.md#quiescence-and-coexistence) | message queued and delivered after activation | traced |
| HU-OBL-008 | Bounded typed migration | [Rule](../60-specification/hot-code-upgrade/checked-migration-and-activation.md#migration-and-activation) | success, failure, timeout and schema checks | traced |
| HU-OBL-009 | Precommit restoration | [Rule](../60-specification/hot-code-upgrade/checked-migration-and-activation.md#migration-and-activation) | failed and exhausted migration restore old state | traced |
| HU-OBL-010 | Atomic activation boundary | [Rule](../60-specification/hot-code-upgrade/checked-migration-and-activation.md#migration-and-activation) | artifact/interface/schema/state commit transition | traced |
| HU-OBL-011 | Explicit reverse migration | [Rule](../60-specification/hot-code-upgrade/checked-migration-and-activation.md#migration-and-activation) | reverse succeeds; missing reverse refuses | traced |
| HU-OBL-012 | Managed OTP path | [Rule](../60-specification/hot-code-upgrade/checked-migration-and-activation.md#otp-realization) | real sys suspend/change_code/resume fixture | traced |
| HU-OBL-013 | OTP boundary | [Rule](../60-specification/hot-code-upgrade/checked-migration-and-activation.md#otp-realization) | source note and adapter exclude raw load/purge | traced |
| HU-OBL-014 | Published limits | [Rule](../60-specification/hot-code-upgrade/checked-migration-and-activation.md#variability-and-limits) | conformance profile and bounded migration tests | traced |
| HU-OBL-015 | Complete retained suite | [Rule](../60-specification/hot-code-upgrade/checked-migration-and-activation.md#diagnostics-and-conformance) | 1,063 tests, production build, escript and trust audit | traced |

## C116 long-term evolution

The [evolution contract](../60-specification/long-term-evolution/historical-replay-and-migration.md)
defines exact historical interpretation and migration at revision `0.1.80`.

| Obligation | Requirement | Normative anchor | Compiler evidence | Status |
| --- | --- | --- | --- | --- |
| LE-OBL-001 | Scope and revision | [Rule](../60-specification/long-term-evolution/historical-replay-and-migration.md#status-and-authority) | long_term_evolution and lifecycle | traced |
| LE-OBL-002 | Exact interpreters | [Rule](../60-specification/long-term-evolution/historical-replay-and-migration.md#interpretation-ledger) | formats 0.1.6–0.1.8 replay | traced |
| LE-OBL-003 | Unknown refusal | [Rule](../60-specification/long-term-evolution/historical-replay-and-migration.md#interpretation-ledger) | 0.1.99 rejection | traced |
| LE-OBL-004 | Historical roots | [Rule](../60-specification/long-term-evolution/historical-replay-and-migration.md#interpretation-ledger) | revoked-root cases | traced |
| LE-OBL-005 | Missing context | [Rule](../60-specification/long-term-evolution/historical-replay-and-migration.md#interpretation-ledger) | tool/dependency outcomes | traced |
| LE-OBL-006 | Adjacent chain | [Rule](../60-specification/long-term-evolution/historical-replay-and-migration.md#adjacent-migration) | deterministic two-hop path | traced |
| LE-OBL-007 | Loss refusal | [Rule](../60-specification/long-term-evolution/historical-replay-and-migration.md#adjacent-migration) | reported-loss rejection | traced |
| LE-OBL-008 | Immutable source | [Rule](../60-specification/long-term-evolution/historical-replay-and-migration.md#adjacent-migration) | bytes/signature retained | traced |
| LE-OBL-009 | Derived envelope | [Rule](../60-specification/long-term-evolution/historical-replay-and-migration.md#adjacent-migration) | canonical path envelope | traced |
| LE-OBL-010 | Verification | [Rule](../60-specification/long-term-evolution/historical-replay-and-migration.md#adjacent-migration) | source digest/version checks | traced |
| LE-OBL-011 | Archive set | [Rule](../60-specification/long-term-evolution/historical-replay-and-migration.md#archive-portability) | context availability checks | traced |
| LE-OBL-012 | Derived governance | [Rule](../60-specification/long-term-evolution/historical-replay-and-migration.md#archive-portability) | distinct derived identity | traced |
| LE-OBL-013 | Published support | [Rule](../60-specification/long-term-evolution/historical-replay-and-migration.md#variability-and-limits) | exact profile ledger | traced |
| LE-OBL-014 | Complete suite | [Rule](../60-specification/long-term-evolution/historical-replay-and-migration.md#diagnostics-and-conformance) | 1,068 tests and release checks | traced |

## C121 build system and package manager

The [build contract](../60-specification/build-system/project-graphs-acquisition-and-offline-builds.md)
defines deterministic orchestration and offline retained compilation at revision `0.1.81`.

| Obligation | Requirement | Normative anchor | Compiler evidence | Status |
| --- | --- | --- | --- | --- |
| BG-OBL-001 | Scope, revision, and vocabulary hold | [Rule](../60-specification/build-system/project-graphs-acquisition-and-offline-builds.md#status-and-authority) | build_system and lifecycle tests | traced |
| BG-OBL-002 | Discovery precedence and ambiguity | [Rule](../60-specification/build-system/project-graphs-acquisition-and-offline-builds.md#project-discovery-and-profiles) | explicit/root/nested discovery cases | traced |
| BG-OBL-003 | Exact named profiles | [Rule](../60-specification/build-system/project-graphs-acquisition-and-offline-builds.md#project-discovery-and-profiles) | development/test/release profile tests | traced |
| BG-OBL-004 | Finite valid DAG | [Rule](../60-specification/build-system/project-graphs-acquisition-and-offline-builds.md#workspace-graph) | missing edge, duplicate, malformed, and cycle refusal | traced |
| BG-OBL-005 | Stable one-time topological execution | [Rule](../60-specification/build-system/project-graphs-acquisition-and-offline-builds.md#workspace-graph) | diamond workspace order and one-build evidence | traced |
| BG-OBL-006 | Transitive cache identity | [Rule](../60-specification/build-system/project-graphs-acquisition-and-offline-builds.md#workspace-graph) | dependency change invalidates core and app keys | traced |
| BG-OBL-007 | Locked digest verification | [Rule](../60-specification/build-system/project-graphs-acquisition-and-offline-builds.md#acquisition-and-offline-execution) | exact external bundle acquisition | traced |
| BG-OBL-008 | Transactional acquisition | [Rule](../60-specification/build-system/project-graphs-acquisition-and-offline-builds.md#acquisition-and-offline-execution) | interrupted second download returns original empty cache | traced |
| BG-OBL-009 | Network-free offline refusal | [Rule](../60-specification/build-system/project-graphs-acquisition-and-offline-builds.md#acquisition-and-offline-execution) | missing and corrupt cache cases | traced |
| BG-OBL-010 | Generator confinement | [Rule](../60-specification/build-system/project-graphs-acquisition-and-offline-builds.md#generators-and-cache-identity) | relative declarations and parent-escape refusal | traced |
| BG-OBL-011 | Generator and capability identity | [Rule](../60-specification/build-system/project-graphs-acquisition-and-offline-builds.md#generators-and-cache-identity) | changed generator/capability key cases | traced |
| BG-OBL-012 | Cached archive input binding | [Rule](../60-specification/build-system/project-graphs-acquisition-and-offline-builds.md#generators-and-cache-identity) | canonical archive and expected input validation | traced |
| BG-OBL-013 | Clean/cached/offline equivalence | [Rule](../60-specification/build-system/project-graphs-acquisition-and-offline-builds.md#output-publication) | real retained compiler archive equality | traced |
| BG-OBL-014 | Transactional publication | [Rule](../60-specification/build-system/project-graphs-acquisition-and-offline-builds.md#output-publication) | corrupt replacement preserves destination | traced |
| BG-OBL-015 | Published finite profile | [Rule](../60-specification/build-system/project-graphs-acquisition-and-offline-builds.md#variability-and-limits) | conformance build_system profile | traced |
| BG-OBL-016 | Complete suite and trust | [Rule](../60-specification/build-system/project-graphs-acquisition-and-offline-builds.md#diagnostics-and-conformance) | 1,077 tests, production builds, trust audit | traced |

## C136 compatibility suite

The [compatibility-suite contract](../60-specification/compatibility-suite/layered-matrix-and-edition-policy.md)
defines bounded layered matrix evidence at revision `0.1.82`.

| Obligation | Requirement | Normative anchor | Compiler evidence | Status |
| --- | --- | --- | --- | --- |
| CS-OBL-001 | Scope, revision, and vocabulary hold | [Rule](../60-specification/compatibility-suite/layered-matrix-and-edition-policy.md#status-and-authority) | lifecycle and compatibility profile tests | traced |
| CS-OBL-002 | Canonical finite matrix identity | [Rule](../60-specification/compatibility-suite/layered-matrix-and-edition-policy.md#matrix-identity-and-scope) | define, validation, duplicate, and digest cases | traced |
| CS-OBL-003 | Seven distinct layers | [Rule](../60-specification/compatibility-suite/layered-matrix-and-edition-policy.md#matrix-identity-and-scope) | integrated seven-layer matrix | traced |
| CS-OBL-004 | Digest-bound complete report | [Rule](../60-specification/compatibility-suite/layered-matrix-and-edition-policy.md#matrix-identity-and-scope) | deterministic report equality and case digests | traced |
| CS-OBL-005 | Pass, fail, and unsupported separation | [Rule](../60-specification/compatibility-suite/layered-matrix-and-edition-policy.md#observations-and-outcomes) | three-outcome and expectation-mismatch cases | traced |
| CS-OBL-006 | Missing and malformed adapter outcomes | [Rule](../60-specification/compatibility-suite/layered-matrix-and-edition-policy.md#observations-and-outcomes) | absent adapter and invalid protocol paths | traced |
| CS-OBL-007 | Exact retained source selections | [Rule](../60-specification/compatibility-suite/layered-matrix-and-edition-policy.md#layer-authorities) | 0.1.1, 0.1.82, wrong revision, and edition suite | traced |
| CS-OBL-008 | Semantic interface classification | [Rule](../60-specification/compatibility-suite/layered-matrix-and-edition-policy.md#layer-authorities) | C028 classifier adapter and retained suite | traced |
| CS-OBL-009 | Complete exact dependency replay | [Rule](../60-specification/compatibility-suite/layered-matrix-and-edition-policy.md#layer-authorities) | diamond, width-64, depth-48, and lock replay | traced |
| CS-OBL-010 | Historical data and immutable provenance | [Rule](../60-specification/compatibility-suite/layered-matrix-and-edition-policy.md#layer-authorities) | C116 replay adapter and migration suite | traced |
| CS-OBL-011 | Exact endpoint host profiles | [Rule](../60-specification/compatibility-suite/layered-matrix-and-edition-policy.md#layer-authorities) | oldest/newest supported fingerprint rows | traced |
| CS-OBL-012 | Original historical signature domain | [Rule](../60-specification/compatibility-suite/layered-matrix-and-edition-policy.md#layer-authorities) | Ed25519 compatibility adapter and governance suite | traced |
| CS-OBL-013 | Checked runtime-upgrade authority | [Rule](../60-specification/compatibility-suite/layered-matrix-and-edition-policy.md#layer-authorities) | C092 preflight adapter and upgrade suite | traced |
| CS-OBL-014 | Curated and generated coverage | [Rule](../60-specification/compatibility-suite/layered-matrix-and-edition-policy.md#coverage-and-edition-policy) | retained authorities and generated graph families | traced |
| CS-OBL-015 | Claim closure and retained edition | [Rule](../60-specification/compatibility-suite/layered-matrix-and-edition-policy.md#coverage-and-edition-policy) | exact revision and outcome aggregation | traced |
| CS-OBL-016 | No ecosystem-wide inference | [Rule](../60-specification/compatibility-suite/layered-matrix-and-edition-policy.md#coverage-and-edition-policy) | profile ecosystem_wide_claim false | traced |
| CS-OBL-017 | Published finite limits | [Rule](../60-specification/compatibility-suite/layered-matrix-and-edition-policy.md#variability-and-limits) | 4,096-case and 1-MiB case profile/refusal | traced |
| CS-OBL-018 | Complete suite and trust | [Rule](../60-specification/compatibility-suite/layered-matrix-and-edition-policy.md#diagnostics-and-conformance) | 1,083 tests, production builds, and trust audit | traced |

## C133 reference evaluator

The [reference-observation contract](../60-specification/reference-evaluator/common-observations-and-bounded-models.md)
defines integrated bounded observations at revision `0.1.83`.

| Obligation | Requirement | Normative anchor | Compiler evidence | Status |
| --- | --- | --- | --- | --- |
| RE-OBL-001 | Scope, revision, vocabulary hold, and proof limit | [Rule](../60-specification/reference-evaluator/common-observations-and-bounded-models.md#status-and-authority) | lifecycle, profile, and public-source-hold cases | traced |
| RE-OBL-002 | Fixed common observation record | [Rule](../60-specification/reference-evaluator/common-observations-and-bounded-models.md#observation-contract) | all reference_observation cases | traced |
| RE-OBL-003 | Distinct terminal and coverage statuses | [Rule](../60-specification/reference-evaluator/common-observations-and-bounded-models.md#observation-contract) | value, trap, timeout, exhaustion, rejection, and unsupported cases | traced |
| RE-OBL-004 | Independently structured model adapters | [Rule](../60-specification/reference-evaluator/common-observations-and-bounded-models.md#observation-contract) | expression/effect/kernel/resource/foreign dispatch | traced |
| RE-OBL-005 | Pure result and semantic fuel | [Rule](../60-specification/reference-evaluator/common-observations-and-bounded-models.md#semantic-engines) | pure value and exact fuel-exhaustion cases | traced |
| RE-OBL-006 | Effect order and host deadline distinction | [Rule](../60-specification/reference-evaluator/common-observations-and-bounded-models.md#semantic-engines) | handled trace and external host-timeout cases | traced |
| RE-OBL-007 | Kernel terminals, trace, lifetime, and steps | [Rule](../60-specification/reference-evaluator/common-observations-and-bounded-models.md#semantic-engines) | kernel adapter plus C010/C036/C081 task suites | traced |
| RE-OBL-008 | Bounded schedule outcome sets | [Rule](../60-specification/reference-evaluator/common-observations-and-bounded-models.md#semantic-engines) | schedule adapter and kernel explorer exhaustion suite | traced |
| RE-OBL-009 | Resource lifetime and cleanup evidence | [Rule](../60-specification/reference-evaluator/common-observations-and-bounded-models.md#boundary-models) | lifecycle exploration plus release success/failure suites | traced |
| RE-OBL-010 | Checked foreign-value model | [Rule](../60-specification/reference-evaluator/common-observations-and-bounded-models.md#boundary-models) | valid and invalid C095 codec observations | traced |
| RE-OBL-011 | Explicit external response catalog | [Rule](../60-specification/reference-evaluator/common-observations-and-bounded-models.md#boundary-models) | value, trap, host-timeout, and absent request cases | traced |
| RE-OBL-012 | Retained source elaboration | [Rule](../60-specification/reference-evaluator/common-observations-and-bounded-models.md#source-and-model-coverage) | checked kernel source adapter and parser refusal suite | traced |
| RE-OBL-013 | Public-source hold | [Rule](../60-specification/reference-evaluator/common-observations-and-bounded-models.md#source-and-model-coverage) | public format reports held-for-P109 unsupported | traced |
| RE-OBL-014 | Unknown and malformed model refusal | [Rule](../60-specification/reference-evaluator/common-observations-and-bounded-models.md#source-and-model-coverage) | forged core, unknown engine, and invalid-bound cases | traced |
| RE-OBL-015 | Published per-engine bounds | [Rule](../60-specification/reference-evaluator/common-observations-and-bounded-models.md#bounds-evidence-and-proof-status) | reference_evaluator conformance profile | traced |
| RE-OBL-016 | Admitted semantic coverage | [Rule](../60-specification/reference-evaluator/common-observations-and-bounded-models.md#bounds-evidence-and-proof-status) | integrated adapters and retained subsystem suites | traced |
| RE-OBL-017 | Agreement is evidence, not proof | [Rule](../60-specification/reference-evaluator/common-observations-and-bounded-models.md#bounds-evidence-and-proof-status) | profile agreement_is_proof false | traced |
| RE-OBL-018 | Complete suite and trust | [Rule](../60-specification/reference-evaluator/common-observations-and-bounded-models.md#diagnostics-and-conformance) | 1,089 tests, production builds, and trust audit | traced |

## C122 testing tools

The [testing-tools contract](../60-specification/testing-tools/isolated-seeded-and-scoped-runs.md)
defines subject-bound, seeded, isolated finite test evidence at revision `0.1.84`.

| Obligation | Requirement | Normative anchor | Compiler evidence | Status |
| --- | --- | --- | --- | --- |
| TT-OBL-001 | Scope, revision, and public-vocabulary hold | [Rule](../60-specification/testing-tools/isolated-seeded-and-scoped-runs.md#status-and-authority) | lifecycle and testing-tools profile cases | traced |
| TT-OBL-002 | Nonempty plan identity and explicit seed | [Rule](../60-specification/testing-tools/isolated-seeded-and-scoped-runs.md#plans-subjects-and-identities) | definition, zero-test, seed, duplicate, and bound cases | traced |
| TT-OBL-003 | Canonical portable plan identity | [Rule](../60-specification/testing-tools/isolated-seeded-and-scoped-runs.md#plans-subjects-and-identities) | plan digest and deterministic replay cases | traced |
| TT-OBL-004 | Stale, tampered, and empty-plan refusal | [Rule](../60-specification/testing-tools/isolated-seeded-and-scoped-runs.md#plans-subjects-and-identities) | stale subject, tampered plan, and zero-test cases | traced |
| TT-OBL-005 | Six distinct result kinds | [Rule](../60-specification/testing-tools/isolated-seeded-and-scoped-runs.md#result-kinds-and-evidence-scope) | integrated all-kinds execution case | traced |
| TT-OBL-006 | Subject-bound finite report and digest | [Rule](../60-specification/testing-tools/isolated-seeded-and-scoped-runs.md#result-kinds-and-evidence-scope) | report shape, order, scope, and digest assertions | traced |
| TT-OBL-007 | Portable finite evidence | [Rule](../60-specification/testing-tools/isolated-seeded-and-scoped-runs.md#result-kinds-and-evidence-scope) | live process evidence refusal | traced |
| TT-OBL-008 | Exact governed-evidence subject | [Rule](../60-specification/testing-tools/isolated-seeded-and-scoped-runs.md#result-kinds-and-evidence-scope) | specification subject mismatch case | traced |
| TT-OBL-009 | Deterministic derived seeds and reproduction | [Rule](../60-specification/testing-tools/isolated-seeded-and-scoped-runs.md#seeds-generation-and-shrinking) | repeated property report equality | traced |
| TT-OBL-010 | Generator domain validation | [Rule](../60-specification/testing-tools/isolated-seeded-and-scoped-runs.md#seeds-generation-and-shrinking) | invalid-generator case | traced |
| TT-OBL-011 | Stable invariant-preserving shrinking | [Rule](../60-specification/testing-tools/isolated-seeded-and-scoped-runs.md#seeds-generation-and-shrinking) | typed minimal threshold counterexample | traced |
| TT-OBL-012 | Explicit nonminimal shrink exhaustion | [Rule](../60-specification/testing-tools/isolated-seeded-and-scoped-runs.md#seeds-generation-and-shrinking) | one-step shrink-bound case | traced |
| TT-OBL-013 | Runner-owned child cleanup | [Rule](../60-specification/testing-tools/isolated-seeded-and-scoped-runs.md#isolation-effects-and-cleanup) | live child terminated before report | traced |
| TT-OBL-014 | Declared effect accounting | [Rule](../60-specification/testing-tools/isolated-seeded-and-scoped-runs.md#isolation-effects-and-cleanup) | declared pass and undeclared-effect failure | traced |
| TT-OBL-015 | Trusted callback boundary | [Rule](../60-specification/testing-tools/isolated-seeded-and-scoped-runs.md#isolation-effects-and-cleanup) | trust profile residual boundary | traced |
| TT-OBL-016 | Distinct semantic, schedule, shrink, and host bounds | [Rule](../60-specification/testing-tools/isolated-seeded-and-scoped-runs.md#bounds-and-outcomes) | four-outcome integrated bounds case | traced |
| TT-OBL-017 | Published finite limits and partial evidence | [Rule](../60-specification/testing-tools/isolated-seeded-and-scoped-runs.md#bounds-and-outcomes) | testing_tools conformance profile and exhaustion reports | traced |
| TT-OBL-018 | Complete suite and trust | [Rule](../60-specification/testing-tools/isolated-seeded-and-scoped-runs.md#diagnostics-and-conformance) | 1,097 tests, production builds, and trust audit | traced |

## C134 differential testing

The [differential-testing contract](../60-specification/differential-testing/generated-and-adversarial-agreement.md)
defines independent generated and adversarial observation comparison at revision
`0.1.85`.

| Obligation | Requirement | Normative anchor | Compiler evidence | Status |
| --- | --- | --- | --- | --- |
| DF-OBL-001 | Revision scope and public-source hold | [Rule](../60-specification/differential-testing/generated-and-adversarial-agreement.md#status-and-authority) | lifecycle, profile, and source-status cases | traced |
| DF-OBL-002 | Bound scenario and explicit unsupported outcome | [Rule](../60-specification/differential-testing/generated-and-adversarial-agreement.md#differential-scenarios) | unknown scenario and bound validation cases | traced |
| DF-OBL-003 | Structurally independent reference and production paths | [Rule](../60-specification/differential-testing/generated-and-adversarial-agreement.md#differential-scenarios) | stepper and BEAM adapters in semantic generators | traced |
| DF-OBL-004 | Generated and retained domain disclosure | [Rule](../60-specification/differential-testing/generated-and-adversarial-agreement.md#differential-scenarios) | differential_testing conformance profile | traced |
| DF-OBL-005 | Declared canonical C133 observation projections | [Rule](../60-specification/differential-testing/generated-and-adversarial-agreement.md#declared-observations) | retained cross-feature and foreign comparisons | traced |
| DF-OBL-006 | Exact deterministic equality | [Rule](../60-specification/differential-testing/generated-and-adversarial-agreement.md#declared-observations) | 64 generated and retained exact comparisons | traced |
| DF-OBL-007 | Normatively bounded allowed observation sets | [Rule](../60-specification/differential-testing/generated-and-adversarial-agreement.md#declared-observations) | permitted schedule-set and invented-observation cases | traced |
| DF-OBL-008 | Distinct terminal and bound outcomes | [Rule](../60-specification/differential-testing/generated-and-adversarial-agreement.md#declared-observations) | normalized C133 status comparison | traced |
| DF-OBL-009 | Typed generated domain and separate invalid mutations | [Rule](../60-specification/differential-testing/generated-and-adversarial-agreement.md#generation-and-adversarial-mutation) | descriptor validator and mutation-family cases | traced |
| DF-OBL-010 | Seeded reproducible generation | [Rule](../60-specification/differential-testing/generated-and-adversarial-agreement.md#generation-and-adversarial-mutation) | deterministic 64-observation C122 property plan | traced |
| DF-OBL-011 | Value, event-order, callback-count, and cancellation detection | [Rule](../60-specification/differential-testing/generated-and-adversarial-agreement.md#generation-and-adversarial-mutation) | four injected mutation cases | traced |
| DF-OBL-012 | Stable domain-preserving shrinking | [Rule](../60-specification/differential-testing/generated-and-adversarial-agreement.md#generation-and-adversarial-mutation) | minimized `%{"n" => 3}` generated disagreement | traced |
| DF-OBL-013 | Counterexample provenance and identity | [Rule](../60-specification/differential-testing/generated-and-adversarial-agreement.md#retained-counterexamples) | four retained canonical corpus entries | traced |
| DF-OBL-014 | Corpus recomputation, retention, and tamper refusal | [Rule](../60-specification/differential-testing/generated-and-adversarial-agreement.md#retained-counterexamples) | valid corpus plus altered digest refusal | traced |
| DF-OBL-015 | Published finite differential limits | [Rule](../60-specification/differential-testing/generated-and-adversarial-agreement.md#bounds-scope-and-proof-claims) | differential_testing conformance profile | traced |
| DF-OBL-016 | Finite agreement is not proof | [Rule](../60-specification/differential-testing/generated-and-adversarial-agreement.md#bounds-scope-and-proof-claims) | profile agreement_is_proof false | traced |
| DF-OBL-017 | Complete machine-readable disclosure | [Rule](../60-specification/differential-testing/generated-and-adversarial-agreement.md#bounds-scope-and-proof-claims) | feature profile and exact 0.1.85 lifecycle selection | traced |
| DF-OBL-018 | Complete suite and trusted-boundary audit | [Rule](../60-specification/differential-testing/generated-and-adversarial-agreement.md#diagnostics-and-conformance) | 1,106 tests, production builds, and trust audit | traced |
