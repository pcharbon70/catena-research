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

This map owns the scheme that connects every Catena normative rule to the
executable evidence that exercises it. It is the workbench for checklist item
P011 and implements the traceability and stable-identifier responsibilities
that [Specification Authority](../SPECIFICATION-AUTHORITY.md) assigns to it. The
map and its registry are non-normative: they describe and index the normative
corpus; they never amend it. Compiler tests remain evidence, never authority.

The first completion pass targets `MUST`/`MUST NOT` obligations only. `SHOULD`,
`MAY`, declarative prose rules, and normative definitions become a separate
follow-up item once C011 is reached.

## Start here

- [How Should Catena Achieve Exhaustive Rule-to-Test Traceability?](../40-inquiries/how-should-catena-achieve-exhaustive-rule-to-test-traceability.md)
  — the open inquiry and decision record.
- [Language Specification Completeness Checklist](../00-inbox/language-specification-completeness-checklist.md)
  — P011 is the partial item this work closes into C011.
- [Specification Authority](../SPECIFICATION-AUTHORITY.md) — assigns rule-ID and
  traceability ownership to P011 and defines the heading-anchor citation unit.
- [Catena Conformance Vocabulary](../CONFORMANCE-VOCABULARY.md) — requirement
  force and behavior classes the evidence must respect.

## Identifier and registry convention

An **obligation** is one conformance requirement. In the `MUST`/`MUST NOT`
phase, every obligation receives a permanent, area-scoped identifier of the
form `AREA-OBL-NNN`. The numeric suffix is never reused; if an obligation is
retired its identifier is retired with it, mirroring the checklist's own
convention.

| Area code | Normative area | Slice |
| --- | --- | --- |
| `TS` | type-system | 0.1.1 |
| `DP` | data-and-patterns | 0.1.2 |
| `CC` | clause-conditions | 0.1.3 |
| `TR` | traits-and-categorical-operations | 0.1.4 |
| `EF` | effects-and-handlers | 0.1.5 |
| `SG` | specifications-and-governance | 0.1.6 |
| `ED` | editions-and-feature-lifecycle | 0.1.7 |
| `FK` | formal-semantic-kernel | 0.1.8 |

The **registry** lives in this map (per-area tables below) and records, for each
obligation:

| Column | Meaning |
| --- | --- |
| ID | The permanent `AREA-OBL-NNN` identifier. |
| Obligation | A short noun phrase for the requirement. |
| Normative anchor | A relative link to the governing heading, e.g. [`syntax-and-safety.md#clause-form`](../60-specification/clause-conditions/syntax-and-safety.md#clause-form). |
| Evidence | The exercising compiler test path and name, plus any stable diagnostic identifier(s). Cross-repo evidence uses a GitHub web link so the archive's local-link check is unaffected. |
| Status | `traced`, `in-progress`, or `untraced`. |

A registry entry is `traced` only when at least one tagged, passing compiler
test covers the obligation. A test tags its obligations with ExUnit
`@tag obligation: "AREA-OBL-NNN"` (or `obligations: [...]`), scanned by the
compiler coverage check.

## Per-area status

`MUST`/`MUST NOT` counts are approximate; they are fixed precisely when each
area's obligation set is extracted.

| Area | `MUST`/`MUST NOT` | Compiler tests (file) | Status |
| --- | --- | --- | --- |
| `CC` clause-conditions | 49 | `c003_clause_condition_test.exs` (7) | pilot — extraction complete, 11 gaps pending fill |
| `TS` type-system | ~44 | `type_conformance_test.exs` (5) | untraced |
| `DP` data-and-patterns | ~61 | `c002_data_test.exs` (22) | untraced |
| `TR` traits | 32 | `c004_categorical_test.exs` (9) | extraction complete, mapping in progress |
| `EF` effects | 27 | `c005_effects_test.exs` (19) | extraction complete, mapping in progress |
| `SG` specifications-and-governance | ~37 | `c006_specification_governance_test.exs` (34) | untraced |
| `ED` editions | ~32 | `c008_editions_lifecycle_test.exs` (16) | untraced |
| `FK` formal-semantic-kernel | 15 | `c010_formal_semantic_kernel_test.exs` (17) | extraction complete, mapping in progress |

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
| CC-OBL-016 | Nonempty condition effect rejected | [`diagnostics-and-conformance.md#stable-diagnostics`](../60-specification/clause-conditions/diagnostics-and-conformance.md#stable-diagnostics) | CND002 | untraced |
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
| CC-OBL-034 | Ordinary match expressions must be exhaustive | [`clause-contexts-and-receive.md#ordinary-matches`](../60-specification/clause-conditions/clause-contexts-and-receive.md#ordinary-matches) | — (c002) | untraced in c003 |
| CC-OBL-035 | Multi-clause set exhaustive with uniform result type | [`clause-contexts-and-receive.md#multi-clause-functions`](../60-specification/clause-conditions/clause-contexts-and-receive.md#multi-clause-functions) | c003 #1 | traced |
| CC-OBL-036 | Elaboration preserves source clause order and bindings | [`clause-contexts-and-receive.md#multi-clause-functions`](../60-specification/clause-conditions/clause-contexts-and-receive.md#multi-clause-functions) | c003 #1 | partial |
| CC-OBL-037 | Structural match then condition evaluated once, in order | [`guard-tree-semantics.md#ordered-selection`](../60-specification/clause-conditions/guard-tree-semantics.md#ordered-selection) | c003 #1 | traced |
| CC-OBL-038 | Body failure or divergence does not resume clause selection | [`guard-tree-semantics.md#ordered-selection`](../60-specification/clause-conditions/guard-tree-semantics.md#ordered-selection) | — | untraced |
| CC-OBL-039 | Verifier rejects duplicated condition evaluation | [`guard-tree-semantics.md#guard-tree-core`](../60-specification/clause-conditions/guard-tree-semantics.md#guard-tree-core) | — | untraced |
| CC-OBL-040 | Or-pattern alternatives bind the same names | [`guard-tree-semantics.md#or-patterns`](../60-specification/clause-conditions/guard-tree-semantics.md#or-patterns) | — | untraced |
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
| CC-OBL-049 | No truthiness or invalid-operation conversion | [`syntax-and-safety.md#evaluation`](../60-specification/clause-conditions/syntax-and-safety.md#evaluation) | — | untraced |

### Pilot gap set (P6)

Eleven obligations currently have no covering test and are the pilot gap-fill
target: CC-OBL-010, 011, 016, 032, 033, 034, 038, 039, 040, 048, 049. A further
eight are `partial` and need additional assertions. The compiler-side work
(P5–P7) tags the seven existing tests with their obligation IDs, adds tests for
each gap, and makes the coverage check fail until every `CC-OBL-*` has at least
one tagged passing test.

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
