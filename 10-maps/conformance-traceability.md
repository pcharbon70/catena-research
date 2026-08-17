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
extracted; all ten normative areas and the C012 governance policy are now
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
| IL-OBL-005 | Both current frontends accept 4,096 integer digits and report LIM002 at 4,097 | [`IMPLEMENTATION-LIMITS.md#bootstrap-portable-minima`](../IMPLEMENTATION-LIMITS.md#bootstrap-portable-minima) | LIM002; c012 #3 | traced |
| IL-OBL-006 | The 65,536-byte decoded-literal floor is reported not applicable until G017 | [`IMPLEMENTATION-LIMITS.md#bootstrap-portable-minima`](../IMPLEMENTATION-LIMITS.md#bootstrap-portable-minima) | c012 #4 | traced |
| IL-OBL-007 | Generated BEAM through 1,048,576 bytes crosses no module-size limit and the next byte reports LIM003 | [`IMPLEMENTATION-LIMITS.md#bootstrap-portable-minima`](../IMPLEMENTATION-LIMITS.md#bootstrap-portable-minima) | LIM003; c012 #4 | traced |
| IL-OBL-008 | Compiler and governance refusal budgets retain their distinct diagnostics and outcomes | [`IMPLEMENTATION-LIMITS.md#analysis-refusals-and-evidence-bounds`](../IMPLEMENTATION-LIMITS.md#analysis-refusals-and-evidence-bounds) | c012 #5 | traced |
| IL-OBL-009 | Evidence exhaustion remains inconclusive and cannot become semantic rejection | [`IMPLEMENTATION-LIMITS.md#analysis-refusals-and-evidence-bounds`](../IMPLEMENTATION-LIMITS.md#analysis-refusals-and-evidence-bounds) | c012 #5 | traced |
| IL-OBL-010 | Mailbox capacity is deployment-defined with ordering, targeting, and live-target delivery constraints | [`IMPLEMENTATION-LIMITS.md#runtime-and-mailbox-capacity`](../IMPLEMENTATION-LIMITS.md#runtime-and-mailbox-capacity) | c012 #6 | traced |
| IL-OBL-011 | Limit refusals report common structured measurements before successful output publication | [`IMPLEMENTATION-LIMITS.md#limit-diagnostics-and-transactional-failure`](../IMPLEMENTATION-LIMITS.md#limit-diagnostics-and-transactional-failure) | LIM001–LIM003; c012 #2–#4 | traced |
| IL-OBL-012 | C012 changes governance and compiler conformance behavior without creating revision 0.1.9 | [`IMPLEMENTATION-LIMITS.md#evolution-and-version-axes`](../IMPLEMENTATION-LIMITS.md#evolution-and-version-axes) | Governance/version-axis obligation; compiler coverage gate allow-list | untraced |

C012 coverage is 11 `traced` and 1 governance-only `untraced` obligation. The
compiler coverage gate explicitly allow-lists IL-OBL-012 because emitting a
language revision is a repository and release-governance decision, not an
executable compiler behavior.

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
