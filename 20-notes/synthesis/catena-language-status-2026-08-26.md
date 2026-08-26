---
title: "Catena Language Status: 26 August 2026"
kind: note
created: "2026-08-26"
maturity: developing
tags:
  - catena
  - language-design
  - status-report
aliases:
  - "Catena status report 0.1.29"
  - "Catena Section 4 gaps complete report"
---

# Catena Language Status: 26 August 2026

## Executive summary

As of revision `0.1.29` (C033, merged 2026-08-26), the checklist's
Sections 1–4 have **no open gaps**: 58 of 141 items complete, 29
normative specification areas, and 557 registered conformance
obligations with 458 fully traced to executable compiler tests. The
compiler (406 tests, warnings-as-errors clean, byte-deterministic
outputs) implements every normative area on OTP 29 through the sole
binary boundary `compile:noenv_forms/2`.

The last five slices — one per day — closed Section 4's expression
core as a connected sibling run, each elevating the C010 kernel's
calculus to language-level rules without amending any retained
revision: **C029** values (the closed ten-form grammar with Float, the
strictness invariant with its edition-record gate), **C030** evaluation
order (the closed ordered-forms table with typed-core completions,
trace-observable with reference/BEAM agreement), **C031** bindings
(non-recursive `let`, definitions-only recursion, the sequencing
idiom, deny-able `BS001`), **C032** functions (semantic-unary currying,
free partial application, immutable capture, the elevated
proper-tail-call guarantee witnessed by a five-million-iteration BEAM
recursion), and **C033** branching (match as the single branch form,
the conditional sugar promise, statement forms declared absent).

Section 4's remainder is partials, not gaps: P034 termination, P035
equality, G036 failure taxonomy, G037 observability, G038 compile-time
evaluation — each waiting on fixed neighbors that now exist. What
still does not exist, deliberately: a surface declaration grammar
(P109, widened to the capstone), a standard library (G101+), runtime
processes and supervision (G084/G089), cancellation (G088),
distribution and hot upgrade (G091/G092), migration engines
(G116/P125), registry operations (G130), and tooling defaults (G121).

## Scope and method

This snapshot supersedes
[the August 24 report](catena-language-status-2026-08.md) (which
recorded `0.1.24` and Section 3's completion); that report remains as
history. Evidence is the archive's own state at this moment: the
[completeness checklist](../../00-inbox/language-specification-completeness-checklist.md),
the [traceability map](../../10-maps/conformance-traceability.md),
`validate_archive.py` (421 documents, 4,515 links, 557 obligations),
the sibling compiler's suite on `rewrite` at merge `7c313cb` (406
tests), the [decision register](../design-decision-register.md) (forks
C018–C033), and the specification corpus. Claims cite their anchors;
this note adds no new rules.

## The completed normative corpus

Twenty-nine areas, each with a versioned chapter set, a stable
diagnostic vocabulary, and a gated compiler suite.

| Rev | Area | Signature facts | Obligations |
| --- | --- | --- | --- |
| 0.1.1–0.1.8 | Foundation | HM typing; nominal ADTs (`origin::module::name`); ordered exhaustive matching; kinded coherent traits; lexical effects with deep handlers and affine resumptions; typed specifications with governance and BEAM erasure; exact editions; the executable kernel — *the* behavior contract | 44+71+49+32+27+44+36+15 |
| 0.1.9–0.1.16 | Source surface | Strict UTF-8; identifiers; layout; comments/docs; literal grammar; finite-binary64 numerics; closed operator inventory; `.cat` file units | 10+13+11+12+12+14+16+12 |
| 0.1.17–0.1.24 | Program organization | Per-category namespaces; private-by-default imports; abstraction exclusions; SCC cycles; SemVer packages with `catena.lock`; opt-in prelude (zero implicit names); effect-closed entries (return-is-shutdown); strict compat matrix with declared behavior/ABI absences | 14+13+7+10+12+10+10+10 |
| 0.1.25 | Values and evaluation | Closed ten-form value grammar (kernel nine + Float); uniform first-classness; strictness invariant, `and`/`or` the only skips, edition-record gate; value-or-trap terminals | 8 |
| 0.1.26 | Evaluation order | Closed ordered-forms table + typed-core completions (curried application, trait calls, handler install, annotate); trace-observable, reference/BEAM agreement | 8 |
| 0.1.27 | Bindings and sequencing | Non-recursive `let`; sequential-lexical scope, silent innermost shadowing; definitions-only recursion (SCC = mutual recursion); sequencing = the let idiom; deny-able `BS001` | 8 |
| 0.1.28 | Functions and calls | Semantic-unary currying; free partial application; lexical immutable capture; let-bound closures as local functions; elevated proper-tail-call guarantee | 8 |
| 0.1.29 | Branching | Match is the only branch form; conditional sugar promise; consolidated rules citing C002/C003/C010/C029/C030/C032; statement forms declared absent | 8 |

## Checklist position by section

| Section | Complete / items | State |
| --- | --- | --- |
| Research consolidation | 6/6 | done |
| 1. Specification form and conformance | 6/6 | done |
| 2. Lexical grammar and source files | 8/8 | done |
| 3. Names, modules, packages, separate compilation | 8/8 | done (closed by C028) |
| 4. Core expressions and evaluation | 5/10 | **gaps done (C029–C033); partials remain** |
| 5. Data, collections, and patterns | 3/8 | partial |
| 6. Comprehensions, generators, iteration | 0/13 | open (synthesis exists) |
| 7. Type-system surface and advanced boundaries | 5/10 | partial |
| 8. Traits, derivation, categorical libraries | 7/7 | done |
| 9. Effects, failure, resource scopes | 4/8 | partial |
| 10. Processes, concurrency, distribution | 0/9 | open (runtime era) |
| 11. BEAM representation and Erlang interop | 0/8 | open |
| 12. Standard library contract | 0/8 | open (G101+) |
| 13. Specifications, governance, erasure | 6/8 | partial |
| 14. Diagnostics, tools, developer experience | 0/9 | open (P109/G121 era) |
| 15. Security, reproducibility, limits | 0/6 | open |
| 16. Formal validation and release gates | 0/9 | open |

Totals: 58 of 141 complete; the next semantic patch is `0.1.30`.

## Cross-cutting guarantees

- **Determinism everywhere.** Equal inputs produce equal interfaces,
  binaries, lock bytes, classifications, warnings, values, and traces.
- **Nothing implicit.** No name enters scope unasked; no implicit host
  handler; no silent defaults; new warnings (`BS001`) are deny-able,
  never validity-changing.
- **Evidence erasure.** Governance and specification evidence never
  reaches BEAM; runtime code never queries editions.
- **Interface-only contracts.** Cross-package interoperation and
  compatibility verdicts run exclusively through digest-verified
  semantic interfaces.
- **Exact revisions.** Retained revisions are immutable; acceptance is
  cumulative-forward; C029's edition-record gate now covers every
  semantic exception (lazy forms, statement forms, non-desugaring
  conditionals).
- **Everything is an expression.** No statement tier, by normative
  declaration; effects sequence through the let idiom.

## The Section 4 sibling run (one slice per day)

The run's method deserves recording as the corpus's pattern for
elevation: take a kernel paragraph frozen at 0.1.8, restate it at the
language level with only the completions the kernel calculus lacked
(Float, curried application order, the local-function form, the
conditional desugaring), fix a closed list plus an entry rule so
nothing widens silently, and witness with dual-target (now
tri-target: stepper, evaluator, BEAM) evidence — zero new machinery
except where a warning earns its keep (`BS001`). The compiler commits
are `f8d8fa9`, `5e1e894`, `17b5be7`, `0af785c`, and `221338f`, each
tree-identical to its merged PR.

## Declared absences and their owners

| Absence | Owner | Note |
| --- | --- | --- |
| Surface declaration grammar | P109 (widened capstone) | sugar promises already fixed (multi-param, conditional) |
| Standard library / prelude contents | G101+, P102 | mechanism shipped, contents unfrozen |
| Processes, supervision, scheduling | G084/G089 | entries are invocation-only |
| Cancellation, time, deadlines | G088 | |
| Distribution, hot upgrade | G091/G092 | |
| Migration engines | G116/P125 | consume C028's classification |
| Tooling, CLI, scaffolding | G121 | may pre-fill, never imply |
| Registry, yanks, signing | G130 | Hex is transport only |
| Behavioral compatibility promise | C028 absence | kernel is the contract |
| BEAM ABI / wire / serialization | C028 absence | representation is not a surface |
| Statement-like control forms | C033 absence | gated behind edition records |

## Process and quality gates

- **Publication order held for five slices running**: research bundle →
  candidate chapters → obligation registry → compiler branch with
  gated tests → atomic promotion → compiler PR merged first → research
  PR. The two promotion-repair debts recorded in August (the C026
  checklist flip, stale G027/G028 pointers) have not recurred — the
  deferral-pointer sweep is now an explicit promotion step.
- **Gates.** `mix compile --warnings-as-errors`, 406 tests,
  `python3 validate_archive.py` (421 documents, 4,515 links, 557
  obligations), 26 validator unit tests, `git diff --check`.
- **Decision record.** Sixteen slices (C018–C033) with every fork
  logged; two developer overrides total, both durable; recommendations
  followed 100% since C021 — the register's value has shifted from
  arbitration to audit trail.
- **Registry health.** 557 obligations; 458 traced, 78 partial (scoped
  follow-ups owned by their areas), 21 untraced (governance/version
  allow-lists).

## Recommended next moves

1. **P035 — equality and ordering** is the best-positioned partial:
   C029's classifier is its designed input, the condition fragment
   fixed Bool/Int equality, and the stdlib era needs it.
2. **G036 — failure taxonomy** unifies traps, panics, and faults over
   the C010/C029 terminal contract; small and unblocking for G037.
3. **G040 + G061** — the built-in data model and numeric traits; the
   standard-library era's key.
4. **P034, G037, G038** complete Section 4's partials on their
   neighbors' outputs.
5. **P109** — the widened capstone; the grammar exercise consumes the
   sugar promises (multi-param, conditional) and the no-statement
   discipline as inputs.

## Evidence route

- [Completeness checklist](../../00-inbox/language-specification-completeness-checklist.md)
  — item states and per-slice completion paragraphs.
- [Conformance traceability](../../10-maps/conformance-traceability.md)
  — the 557-obligation registry with immutable compiler commits.
- [Specification corpus](../../60-specification/README.md) — the 29
  normative areas and their conformance journals.
- [Home map](../../10-maps/home.md) — curated routes.
- [Decision register](../design-decision-register.md) — every fork
  since C018.
- Compiler: `catena` repo, branch `rewrite`, merge `7c313cb`.
- Prior snapshot: [August 24 report](catena-language-status-2026-08.md).

## Sources

- The C029–C033 syntheses and conformance journals — the sibling run
  this snapshot records.
- [Catena API and ABI Compatibility](../catena-api-and-abi-compatibility.md)
  for the compat frame the run sits inside.
