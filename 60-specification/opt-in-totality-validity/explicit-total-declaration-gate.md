---
title: "Opt-In Totality Validity Amendment"
kind: specification
created: "2026-09-15"
status: normative
spec_version: "0.1.99"
tags:
  - conformance
  - recursion
  - specification
  - termination
  - totality
aliases:
  - "Catena total-transform validity gate"
---

# Opt-In Totality Validity Amendment

## Status and authority

This normative C034 amendment is governed by
[Specification Authority](../../SPECIFICATION-AUTHORITY.md),
[Catena Conformance Vocabulary](../../CONFORMANCE-VOCABULARY.md), and
[Catena Implementation Limits and Portability](../../IMPLEMENTATION-LIMITS.md).
Under [C008 cumulative applicability](../editions-and-feature-lifecycle/edition-selection-and-applicability.md#cumulative-applicability),
it introduces the stable `opt-in-totality-validity-gate` feature at exact
revision `0.1.99` in edition `0.1`.

For selection `0.1.99`, this chapter explicitly replaces only the
**No totality checking exists** paragraph in
[Program Recursion Is Unrestricted](../recursion-and-termination/program-recursion-is-unrestricted.md#the-stance)
and `RT-OBL-004` in
[Recursion and Termination Diagnostics and Conformance](../recursion-and-termination/diagnostics-and-conformance.md#conformance-obligations).
It adopts the remaining `0.1.31` recursion stance, separation table, entry
rule, diagnostics, and obligations unchanged. Later same-edition selections
inherit this amendment unless another normative lifecycle record explicitly
replaces it. Historical selection `0.1.31` retains its original meaning.

## Amended program-recursion stance

> **Normative definition.**

```text
Ordinary program recursion is unrestricted. A declaration that does not
explicitly opt into a separately admitted totality contract remains valid
without a termination proof and may diverge.

A separately admitted explicit-total declaration may make successful
totality verification a condition of that declaration's validity. Such a
gate applies only to the declaration carrying the explicit opt-in.
```

Divergence of an ordinary program remains non-termination, never a trap or
conformance defect, and acquires no fallback outcome (`RT-OBL-010`). Proper
tail calls remain the only general stack guarantee. Removing an explicit-total marker
from an otherwise legal recursive declaration returns that declaration to the
ordinary unrestricted regime; an implementation MUST NOT infer the marker or
extend a totality rejection to an unmarked declaration (`RT-OBL-011`).

This amendment replaces the former permanent prohibition on validity-gating
totality analysis. It does not replace unrestricted recursion with a total
language and does not require whole-program termination inference.

## Gate for an explicit-total declaration

A later same-edition slice MAY admit an explicit-total declaration only when
that slice satisfies every requirement below (`RT-OBL-012`):

1. It defines one unambiguous source or decoded declaration role that the
   author selects explicitly. Documentation, an inferred property, a naming
   convention, or a compiler flag is not an opt-in.
2. It defines the declaration's complete type-and-effect preconditions. An
   admitted `total transform` form has a closed empty effect row; local
   handling is acceptable only when the residual row is empty under C005.
3. It defines totality over every admitted well-typed input: evaluation reaches
   a value in finitely many abstract semantic steps and reaches no
   language-level trap. A typed `Option`, `Result`, or other failure-shaped
   value is a value and therefore can be a total result.
4. It defines a sound, deterministic acceptance discipline. The discipline can
   conservatively reject a declaration whose totality is true but not
   established; it cannot accept an unestablished claim.
5. It defines a deterministic proof or certificate object and an independent
   verifier whose acceptance is required before compiler output is authorized.
   Trust in the analysis that constructed the certificate is insufficient.
6. It defines how calls, primitives, branching, pattern coverage, direct and
   mutual recursion, higher-order arguments, partial application, and imported
   interfaces preserve or invalidate totality evidence.
7. It defines stable diagnostics, compatibility effects, interface identity,
   erasure behavior, proof invalidation, implementation limits, exhaustion
   outcomes, and executable conformance evidence in the admitting change.

The initial recursive proof discipline for the proposed `total transform`
surface is structural descent. Every recursive strongly connected component
identifies a decreasing parameter, and each recursive edge supplies a value
that is a strict constructor subvalue of the caller's corresponding parameter.
All non-recursive calls in the component depend only on declarations or
primitives carrying accepted totality evidence. A future well-founded relation
beyond constructor subvalues requires its own normative admission and
independently checkable certificate; an implementation MUST NOT infer such a
relation from tests, timeouts, profiling, or author assertion (`RT-OBL-013`).

Explicit trap producers, partial primitives without an admitted total wrapper,
dynamic or unsafe operations, foreign operations without a total boundary
contract, non-exhaustive branching, and recursion without an accepted decrease
certificate cannot appear in an accepted initial totality certificate. This
restriction classifies what the future admitting slice must prove; it does not
make any such ordinary unmarked computation invalid.

## Evidence and finite resources

Bounded examples, generated property tests, observed completion, and timeouts
are evidence about sampled executions. They do not establish universal
termination or absence of traps and MUST NOT authorize an explicit-total
declaration (`RT-OBL-013`).

The certificate constructor and verifier are compile-time evaluators and remain
under [The Separation Table](../recursion-and-termination/the-separation-table.md#the-entry-rule). Their
admitting slice must make each evaluator total or bound it with a declared
implementation limit. Limit exhaustion is a distinct implementation refusal or
inconclusive evidence result under the implementation-limits policy; it is not
a counterexample and does not prove the declaration non-total
(`RT-OBL-014`). No compiler output may be authorized while required totality
verification is inconclusive.

The semantic claim excludes finite-machine availability. Memory exhaustion,
configured compiler or runtime limits, process termination, VM loss, unavailable
hardware, and realtime deadlines retain their existing classifications. A total
declaration promises termination and absence of language-level traps in the
abstract model, not completion within a wall-clock or allocation bound.

## No premature source or checker adoption

Revision `0.1.99` changes the C034 admission policy only. It introduces no
`transform`, `total`, or `guarantee` token; no public parser production, decoded
syntax node, effect rule, diagnostic family, interface field, proof-object
format, checker API, executable frontend, or persisted artifact version
(`RT-OBL-015`). The concrete
[`total transform` proposal](../../20-notes/catena-first-version-grammar-and-vocabulary.md#total-transform-is-an-opt-in-verified-claim)
must enter through a later source-adoption slice satisfying this gate. This
amendment alone does not complete P107 or P109 and cannot support a totality
conformance claim.

## Lifecycle and migration

The lifecycle record `change-0-1-99-opt-in-totality-validity-gate` has
predecessor `0.1.98`, target `0.1.99`, classification
`compatible-correction`, affected dimension `static-meaning`, and stable
feature identifier `opt-in-totality-validity-gate` (`RT-OBL-009`). It corrects
the overbroad claim that validity-gating totality analysis is forever excluded;
it accepts no new source and changes no existing program's static or dynamic
meaning.

Migration selects revision `0.1.99`; no source edit exists because this
amendment admits no declaration form. A compiler claiming `0.1.99` exposes the
exact feature and change records through C008 language information, accepts the
revision, retains every prior exact selection, and demonstrates that no new
source form or diagnostic has appeared. Retained interface, artifact, manifest,
signature, kernel, and governance format versions remain unchanged.

## Conformance obligations

| ID | Obligation | Required evidence |
| --- | --- | --- |
| `RT-OBL-009` | register exact revision `0.1.99`, the stable gate feature, and its compatible-correction lifecycle record | exact selection, registry, retention, and migration-record tests |
| `RT-OBL-010` | preserve unrestricted ordinary recursion and divergence as non-termination | retained recursive completion and divergence witnesses |
| `RT-OBL-011` | confine every future totality validity gate to an explicit declaration opt-in | absence and unmarked-recursion regression tests |
| `RT-OBL-012` | require a later admitting slice to define every listed totality contract component together | registry, specification-shape, and future-slice coverage checks |
| `RT-OBL-013` | reject tests, timeouts, profiling, and author assertion as universal totality proof | adversarial certificate-provenance tests in the admitting slice |
| `RT-OBL-014` | keep construction and verification total-or-bounded and classify exhaustion separately from a counterexample | limit, exhaustion, and transactional-publication tests in the admitting slice |
| `RT-OBL-015` | add no source, diagnostic, checker, proof format, interface field, executable frontend, or persisted-format change at `0.1.99` | public-boundary and retained-format absence tests |

Until executable evidence covers these obligations, a compiler does not claim
conformance to revision `0.1.99`. This does not weaken the complete historical
`0.1.31` evidence for `RT-OBL-001` through `RT-OBL-008`.

## Rationale and design route (non-normative)

The [first-version source design](../../20-notes/catena-first-version-grammar-and-vocabulary.md#functions-transforms-totality-and-guarantees)
records the approved progression from ordinary functions to pure transforms,
checked total transforms, and named guarantees. The amendment deliberately
lands before the source feature: it removes C034's contradiction while making
the later implementation earn a deterministic, independently verified
totality claim rather than treating a keyword or bounded test as proof.
