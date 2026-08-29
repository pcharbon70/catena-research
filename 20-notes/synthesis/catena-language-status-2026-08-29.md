---
title: "Catena Language Status: 29 August 2026"
kind: note
created: "2026-08-29"
maturity: developing
tags:
  - catena
  - language-design
  - status-report
aliases:
  - "Catena status report 0.1.34"
  - "Catena Section 4 completion report"
---

# Catena Language Status: 29 August 2026

## Executive summary

As of revision `0.1.34` (C038, merged 2026-08-26), the checklist's
Sections 1–4 are **complete**: 63 of 141 items, 34 normative
specification areas, and 597 registered conformance obligations with
498 fully traced to executable compiler tests. The compiler (451
tests, warnings-as-errors clean, byte-deterministic outputs)
implements every normative area on OTP 29 through the sole binary
boundary `compile:noenv_forms/2`.

Section 4 — core expressions and evaluation — closed in ten slices
(C029–C038), five gaps and five partials, each an elevation of the
C010 kernel's calculus to language-level rules without amending any
retained revision: **values** (the closed ten-form grammar with
Float), **order** (the ordered-forms table, trace-observable),
**bindings** (non-recursive `let`, the sequencing idiom, `BS001`),
**functions** (semantic-unary currying, free partial application,
the elevated tail guarantee witnessed at five million BEAM
iterations), **branching** (match-only with the conditional sugar
promise, statement forms absent), **equality** (the closed comparable
set with bit-exact `-0.0 ≠ 0.0` floats and structural recursion),
**recursion** (unrestricted with divergence as non-termination, the
G038 gate), **failure** (the single `trap(reason)` outcome with
kinded reasons), **observability** (semantic identity, process
identity alone identity-bearing, finalization gated absent), and
**compile-time evaluation** (constants never execute, derivations
are generation not execution, the cited restriction table).

Section 5 (data, collections, and patterns) is the next era, anchored
by G040 (the built-in data model) with 3/8 done and P041 (structural
records and variants) at its edge. What deliberately does not exist:
a surface declaration grammar (P109, the widened capstone — its sugar
promises for conditionals and multi-parameters are already fixed), a
standard library (G101+), runtime processes and supervision
(G084/G089), cancellation (G088), distribution and hot upgrade
(G091/G092), migration engines (G116/P125), registry operations
(G130), and tooling defaults (G121).

## Scope and method

This snapshot supersedes
[the 26 August report](catena-language-status-2026-08-26.md) (which
recorded `0.1.29` and Section 4's gap-free state); that report
remains as history, as does
[the August 24 report](catena-language-status-2026-08.md) (`0.1.24`).
Evidence is the archive's own state at this moment: the
[completeness checklist](../../00-inbox/language-specification-completeness-checklist.md),
the [traceability map](../../10-maps/conformance-traceability.md),
`validate_archive.py` (462 documents, 4,989 links, 597 obligations),
the sibling compiler's suite on `rewrite` at merge `f0bb719` (451
tests), the [decision register](../design-decision-register.md)
(forks C018–C038, ~164 fork rows), and the specification corpus.
Claims cite their anchors; this note adds no new rules.

## The completed normative corpus

Thirty-four areas, each with a versioned chapter set, a stable
diagnostic vocabulary, and a gated compiler suite.

| Rev | Area | Signature facts | Obligations |
| --- | --- | --- | --- |
| 0.1.1–0.1.8 | Foundation | HM typing; nominal ADTs; ordered exhaustive matching; kinded coherent traits; lexical effects with deep handlers; typed specifications with BEAM erasure; exact editions; the executable kernel — *the* behavior contract | 44+71+49+32+27+44+36+15 |
| 0.1.9–0.1.16 | Source surface | Strict UTF-8; identifiers; layout; comments; literal grammar; finite-binary64 numerics; closed operator inventory; `.cat` file units | 10+13+11+12+12+14+16+12 |
| 0.1.17–0.1.24 | Program organization | Namespaces; private-by-default imports; abstraction exclusions; SCC cycles; SemVer packages with `catena.lock`; opt-in prelude (zero implicit names); effect-closed entries; strict compat matrix with declared absences | 14+13+7+10+12+10+10+10 |
| 0.1.25 | Values | Closed ten-form grammar (kernel nine + Float); uniform first-classness; strictness invariant with edition-record gate; value-or-trap terminals | 8 |
| 0.1.26 | Evaluation order | Closed ordered-forms table + typed-core completions; trace-observable, reference/BEAM agreement | 8 |
| 0.1.27 | Bindings | Non-recursive `let`; silent innermost shadowing; definitions-only recursion (SCC = mutual); the let idiom; deny-able `BS001` | 8 |
| 0.1.28 | Functions | Semantic-unary currying; free partial application; lexical immutable capture; let-bound local functions; proper tail calls (5M BEAM witness) | 8 |
| 0.1.29 | Branching | Match is the only branch form; the conditional sugar promise; statement forms declared absent | 8 |
| 0.1.30 | Equality | Closed comparable set with structural recursion; bit-exact floats (`-0.0 ≠ 0.0`); monomorphic; `EQN001`; guards keep the frozen fragment | 8 |
| 0.1.31 | Recursion | Unrestricted with divergence as non-termination; the cited separation table; the G038 gate | 8 |
| 0.1.32 | Failure | Single `trap(reason)` outcome, kinded reasons; six-category mapping; per-producer gate; kernel-verbatim observability | 8 |
| 0.1.33 | Observability | Six-way non-observability; semantic identity; two-clause identity rule (process identity alone); gated finalization absence | 8 |
| 0.1.34 | Compile-time | Constants never execute; attributes/macros absent and gated; derivations as generation; the cited restriction table | 8 |

## Checklist position by section

| Section | Complete / items | State |
| --- | --- | --- |
| Research consolidation | 6/6 | done |
| 1. Specification form and conformance | 6/6 | done |
| 2. Lexical grammar and source files | 8/8 | done |
| 3. Names, modules, packages, separate compilation | 8/8 | done (closed by C028) |
| 4. Core expressions and evaluation | **10/10** | **done — gaps closed by C029–C033, partials by C034–C038** |
| 5. Data, collections, and patterns | 3/8 | partial — the next era (G040 anchor, P041 edge) |
| 6. Comprehensions, generators, iteration | 0/13 | open (synthesis exists) |
| 7. Type-system surface and advanced boundaries | 5/10 | partial |
| 8. Traits, derivation, categorical libraries | 7/7 | done |
| 9. Effects, failure, resource scopes | 4/8 | partial (the failure half closed by C036; resource scopes remain) |
| 10. Processes, concurrency, distribution | 0/9 | open (runtime era) |
| 11. BEAM representation and Erlang interop | 0/8 | open |
| 12. Standard library contract | 0/8 | open (G101+) |
| 13. Specifications, governance, erasure | 6/8 | partial (P109 the large remainder) |
| 14. Diagnostics, tools, developer experience | 0/9 | open (P109/G121 era) |
| 15. Security, reproducibility, limits | 0/6 | open |
| 16. Formal validation and release gates | 0/9 | open |

Totals: 63 of 141 complete; the next semantic patch is `0.1.35`.

## The Section 4 method, recorded

The ten-slice run perfected one pattern: take a frozen kernel
paragraph, restate it at the language level with only the
completions the kernel calculus lacked, fix a **closed set plus an
entry rule** so nothing widens silently, prefer **declared absences
with named owners and gates** over invented machinery, and witness
with tri-target evidence (stepper, evaluator, BEAM) — new public API
only where a warning earns its keep (`BS001`), new diagnostics only
where a family owns a real rejection (`EQN001`). The compiler
commits `f8d8fa9` through `30426d5`, each tree-identical to its
merged PR. The gates now standing: edition-record (C029, exceptions
to strictness), entry-rule (C030 order, C035 comparability, C036
failure kinds), producer-gated finalization (C037), and the
totality-or-bounded gate (C034/C038) — four gate shapes, all
inherited-verbatim by their successors.

## Cross-cutting guarantees

- **Determinism everywhere** — equal inputs produce equal
  interfaces, binaries, lock bytes, classifications, warnings,
  values, traces, and trap reasons.
- **Nothing implicit** — no name enters scope unasked; no implicit
  host handler; no silent defaults; warnings are deny-able, never
  validity-changing.
- **The three-way partition** — every evaluation is a value, a trap,
  or running; divergence is never failure; failures are never
  values.
- **Semantic identity** — equal values are interchangeable;
  representation is invisible; process identity alone is
  identity-bearing and never comparable.
- **Evidence erasure and interface-only contracts** — governance
  evidence never reaches BEAM; cross-package verdicts run exclusively
  through digest-verified interfaces.
- **Compilation without execution** — checking plus generation; every
  meta-evaluator acyclic or budgeted; any arrival gated.
- **Exact revisions** — retained revisions immutable; acceptance
  cumulative-forward; breaking language change travels as an edition.

## Declared absences and their owners

| Absence | Owner | Note |
| --- | --- | --- |
| Surface declaration grammar | P109 (widened capstone) | conditional and multi-param sugar promises fixed |
| Standard library / prelude contents | G101+, P102 | mechanism shipped, contents unfrozen |
| Processes, supervision, scheduling | G084/G089 | entries invocation-only |
| Cancellation, time, deadlines | G088 | |
| Distribution, hot upgrade | G091/G092 | |
| Migration engines | G116/P125 | consume C028's classification |
| Tooling, CLI, scaffolding | G121 | may pre-fill, never imply |
| Registry, yanks, signing | G130 | Hex is transport only |
| Behavioral compatibility | C028 absence | the kernel is the contract |
| BEAM ABI / serialization | C028 absence | representation is not a surface |
| Statement-like control forms | C033 absence | edition-record gated |
| Identity equality | C035/C037 | semantic identity only |
| Finalization | C037 absence | producer-gated |
| Const-eval, macros, attributes | C038 absence | gate-inherited |

## Process and quality gates

- **Publication order held for ten slices running**: research bundle
  → candidate chapters → obligation registry → compiler branch with
  gated tests → atomic promotion → compiler PR merged first →
  research PR. No promotion-repair debt since the August fixes; the
  deferral-pointer sweep is a standing promotion step.
- **Gates.** `mix compile --warnings-as-errors`, 451 tests,
  `python3 validate_archive.py` (462 documents, 4,989 links, 597
  obligations), 26 validator unit tests, `git diff --check`.
- **Decision record.** Twenty-one slices (C018–C038) with every fork
  logged (~164 rows); two developer overrides total, both durable;
  recommendations followed 100% since C021 — arbitration has become
  audit trail.
- **Registry health.** 597 obligations; 498 traced, 78 partial
  (scoped follow-ups owned by their areas), 21 untraced
  (governance/version allow-lists).
- **Two validator-forced honest wordings** worth keeping: C034's
  "undefined outcome" (the prohibited "undefined behavior" phrase)
  and C037's opaque-presentation citation — the conformance
  vocabulary policing the corpus's own prose.

## Recommended next moves

1. **A refreshed synthesis snapshot era-opener for Section 5**, or
   directly **G040 — the built-in data model**: decides strings,
   binaries, lists, maps, sets, and each one's value status,
   comparability entry, and coverage — the anchor that unlocks
   G101+.
2. **P041 — structural records and variants**: Section 5's edge
   item; literal, selection, and update forms beyond C002's nominal
   shapes; well-prepared on C035's semantic record equality.
3. **Section 6's comprehensions program** (0/13, synthesis exists) —
   G040's collections are its prerequisite.
4. **P109** — the widened capstone; the grammar exercise consumes
   the fixed sugar promises and the no-statement discipline.

## Evidence route

- [Completeness checklist](../../00-inbox/language-specification-completeness-checklist.md)
  — item states and per-slice completion paragraphs.
- [Conformance traceability](../../10-maps/conformance-traceability.md)
  — the 597-obligation registry with immutable compiler commits.
- [Specification corpus](../../60-specification/README.md) — the 34
  normative areas and their conformance journals.
- [Home map](../../10-maps/home.md) — curated routes.
- [Decision register](../design-decision-register.md) — every fork
  since C018.
- Compiler: `catena` repo, branch `rewrite`, merge `f0bb719`.
- Prior snapshots: [26 August](catena-language-status-2026-08-26.md),
  [August 24](catena-language-status-2026-08.md).

## Sources

- The C029–C038 syntheses and conformance journals — the Section 4
  run this snapshot records.
- [Catena API and ABI Compatibility](../catena-api-and-abi-compatibility.md)
  for the compat frame the run sits inside.
