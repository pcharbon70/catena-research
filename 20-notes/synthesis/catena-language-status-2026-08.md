---
title: "Catena Language Status: August 2026"
kind: note
created: "2026-08-24"
maturity: developing
tags:
  - catena
  - language-design
  - status-report
aliases:
  - "Catena status report 0.1.24"
  - "Catena Section 3 completion report"
---

# Catena Language Status: August 2026

## Executive summary

As of revision `0.1.24` (C028, merged 2026-08-24), Catena's checklist
Sections 1–3 — specification form, lexical/source foundations, and the
entire names-modules-packages-program — are **complete**: 53 of 141
checklist items, 24 normative specification areas, and 517 registered
conformance obligations with 419 fully traced to executable compiler
tests. The compiler (355 tests, warnings-as-errors clean, byte-
deterministic outputs) implements every normative area on OTP 29
through the sole binary boundary `compile:noenv_forms/2`.

The language now has a complete static core: Hindley–Milner typing
over nominal, origin-qualified data; safe ordered pattern matching;
kinded coherent traits; lexical algebraic effects with deep handlers
and affine resumptions; an executable formal kernel that *is* the
behavior contract; a strictly-cumulative source surface from bytes to
operator expressions; and a program organization stack — namespaces,
private-by-default imports/exports, abstraction boundaries, SCC cycle
admission, SemVer packages with lockfiles, an opt-in prelude with the
zero-implicit-names guarantee, effect-closed entry points, and a
strict API-compatibility matrix with declared behavior and ABI
absences.

What deliberately does not exist: a surface declaration grammar
(P109), a standard library (G101+), runtime processes and supervision
(G084/G089), cancellation (G088), distribution and hot upgrade
(G091/G092), migration engines (G116/P125), registry operations
(G130), and tooling defaults (G121). Each absence is normative,
owned, and dated — not an accident.

## Scope and method

This report synthesizes the archive's own evidence at one snapshot:
the [completeness checklist](../../00-inbox/language-specification-completeness-checklist.md)
(item states), the [traceability map](../../10-maps/conformance-traceability.md)
(obligation registry and per-area coverage), `validate_archive.py`
(document, link, and obligation integrity), the sibling compiler's
test suite (355 tests on `rewrite` at merge `e0e3c16`), the
[decision register](../design-decision-register.md) (fork history
C018–C028), and the [specification corpus](../../60-specification/README.md)
itself. Claims below cite their anchors; this note adds no new rules.

## Architecture

Two repositories, four version axes, one pipeline.

- **Repos.** `catena-research` (this archive; normative authority,
  evidence, and maps) and `catena` (the executable model and
  conformance evidence, branch `rewrite`). Every semantic slice lands
  compiler-first, then as a research promotion.
- **Version axes.** The language line `0.1.x` (24 revisions, one per
  semantic slice — `LanguageVersion` is the exact-revision registry);
  the manifest format (0.1.7, extended only backward-compatibly);
  interface/artifact versions (0.1.2–0.1.8); and the compiler package
  (`0.1.0`, independent of the language). SemVer 2.0.0 governs
  packages; editions govern the language.
- **Pipeline.** Source text is validated byte-by-byte, assembled
  through scanner-level slices (identifiers → layout → comments →
  literals → numerics → operators → file units), organized
  (namespaces → imports → abstraction → cycles → packages → prelude →
  entries → compatibility), then inferred, elaborated to typed core,
  independently verified, and lowered — CPS or direct — to Erlang
  Abstract Format and BEAM. Retained inputs: versioned JSON AST
  (0.1.1–0.1.7) and the exact kernel S-expression (0.1.8).

## The completed normative corpus

Twenty-four areas, each with a versioned chapter set, a stable
diagnostic vocabulary, and a gated compiler test suite. Obligation
counts are the registry's fixed extraction counts.

| Rev | Area | What it guarantees (signature facts) | Obligations |
| --- | --- | --- | --- |
| 0.1.1 | Type system | HM inference; export signatures mandatory; two guarantee profiles | 44 |
| 0.1.2 | Data and patterns | Nominal ADTs (`origin::module::name` identity); transparent/abstract; exhaustive ordered matching; digest-verified interfaces | 71 |
| 0.1.3 | Clause conditions | Safe conditions only; ordered guard trees; coverage facts | 49 |
| 0.1.4 | Traits | Kinded traits; coherence; derived laws; erased specialization | 32 |
| 0.1.5 | Effects and handlers | Lexical capabilities; deep handlers; affine resumptions; trace agreement | 27 |
| 0.1.6 | Specifications and governance | Typed rules with exact examples; canonical signatures; offline trust; complete BEAM erasure | 44 |
| 0.1.7 | Editions and lifecycle | Package-local selection; per-dimension change classification; no runtime dispatch | 36 |
| 0.1.8 | Formal semantic kernel | Executable SOS; strict order; explicit terminal states; typed actors; traps | 15 |
| 0.1.9–0.1.16 | Source surface | Strict UTF-8; identifiers; layout; comments/docs; literal grammar; finite-binary64 numerics (`NUM001`); closed operator inventory; `.cat` file units | 10+13+11+12+12+14+16+12 |
| 0.1.17 | Namespaces | Per-category; innermost-wins; `NSP004` collisions name all origins | 14 |
| 0.1.18 | Imports and exports | Private by default; C002 transparency modes; list admission; deny-able `IMP001` | 13 |
| 0.1.19 | Abstraction boundaries | Binary authority vocabulary; no stable layout; smart-constructor idiom | 7 |
| 0.1.20 | Dependency cycles | SCC admission; signature regimes; joint digests; inversion alternative | 10 |
| 0.1.21 | Packages | SemVer exact/caret/tilde (Cargo 0.x); single-version resolution; `catena.lock` replay; bundle digests; Hex profile | 12 |
| 0.1.22 | Prelude | Opt-in selection at ordinary precedence; absent/`null` = out; zero implicit names | 10 |
| 0.1.23 | Entry points | Named zero-argument effect-closed entries; derived libraries; invocation-only launch; return-is-shutdown | 10 |
| 0.1.24 | API compatibility | Strict 15-row diff matrix; major-as-breaking at 1.0+/minor under 0.x; behavior and ABI declared absences; facade exclusion | 10 |

## Checklist position by section

| Section | Complete / items | State |
| --- | --- | --- |
| Existing research consolidation | 6/6 | done |
| 1. Specification form and conformance | 6/6 | done |
| 2. Lexical grammar and source files | 8/8 | done |
| 3. Names, modules, packages, separate compilation | 8/8 | **done — closed by C028** |
| 4. Core expressions and evaluation | 0/3 | next program (P029 first) |
| 5. Data, collections, and patterns | 3/8 | partial |
| 6. Comprehensions, generators, iteration | 0/2 | open |
| 7. Type-system surface and advanced boundaries | 5/10 | partial |
| 8. Traits, derivation, categorical libraries | 7/7 | done |
| 9. Effects, failure, resource scopes | 4/8 | partial |
| 10. Processes, concurrency, distribution | 0/4 | open (runtime era) |
| 11. BEAM representation and Erlang interop | 0/4 | open |
| 12. Standard library contract | 0/5 | open (G101+) |
| 13. Specifications, governance, erasure | 6/8 | partial |
| 14. Diagnostics, tools, developer experience | 0/9 | open (P109/G121 era) |
| 15. Security, reproducibility, limits | 0/4 | open (G128/G130) |
| 16. Formal validation and release gates | 0/3 | open |

Totals: 53 of 141 items complete; the next semantic patch is
`0.1.25`.

## Cross-cutting guarantees

These hold corpus-wide, not per-area:

- **Determinism.** Equal inputs produce equal interfaces, binaries,
  lock bytes, classifications, and launch reports. Compilation is
  byte-reproducible; `catena.lock` replays as exact pins.
- **Nothing implicit.** No name enters scope unasked (C026 guarantee,
  extended unchanged over entries); no implicit host handler exists
  (entries are effect-closed or invalid); no silent defaults anywhere
  the corpus has spoken.
- **Evidence erasure.** Governance and specification evidence never
  reaches BEAM; runtime code never queries editions or previews.
- **Interface-only contracts.** Cross-package interoperation and
  compatibility verdicts run exclusively through digest-verified
  semantic interfaces; binaries and digests are identity, never
  compatibility.
- **Exact revisions.** Retained revisions are immutable; acceptance is
  cumulative-forward; breaking language change travels as an edition
  through a lifecycle record.

## Declared absences and their owners

| Absence | Owner | Note |
| --- | --- | --- |
| Surface declaration grammar | P109 | JSON AST and kernel S-expressions remain the inputs |
| Standard library / prelude contents | G101+, P102 | mechanism shipped, contents unfrozen |
| Processes, supervision, scheduling | G084/G089 | entries are invocation-only by design |
| Cancellation, time, deadlines | G088 | |
| Distribution, hot upgrade | G091/G092 | |
| Migration engines | G116/P125 | consume C028's classification |
| Tooling, CLI, scaffolding | G121 | may pre-fill, never imply |
| Registry, yanks, signing | G130 | Hex is transport only |
| Behavioral compatibility promise | C028 absence | the kernel is the contract; no bug-compatibility |
| BEAM ABI / wire / serialization | C028 absence | representation is not a surface |

## Process and quality gates

- **Publication order.** Every slice: research bundle → candidate
  chapters → obligation registry → compiler branch with tagged tests
  and a coverage gate → atomic promotion → compiler PR merged first,
  then research PR. Both repos end synced and validated.
- **Gates.** `mix compile --warnings-as-errors`, 355 tests,
  `python3 validate_archive.py` (379 documents, 4,031 links, 517
  obligations), 26 validator unit tests, `git diff --check`.
- **Decision record.** 70+ plan-fork decisions across C018–C028 in the
  [register](../design-decision-register.md); two developer overrides
  total (`.cat` extension C020; admitting module recursion C024), both
  durable.
- **Known process debt.** Two promotions (C026, C027) initially missed
  sibling-index repairs (the G026 checklist flip; stale G027/G028
  deferral pointers); both were repaired in the next slice's
  promotion, and the pattern is now an explicit promotion step. The 77
  partial and 21 untraced obligations are scoped follow-ups owned by
  their areas, not silent gaps — the registry names each.

## Recommended next moves

1. **P029 — value and evaluation definition** opens Section 4 and is
   the natural next slice; it sits on the finished kernel.
2. **G040 + G061** (built-in data model; numeric trait relationships)
   unlock the standard-library era on finished machinery.
3. **P109 — surface grammar capstone** remains the largest single
   usability lever and consumes the finished scanner stack.

## Evidence route

- [Completeness checklist](../../00-inbox/language-specification-completeness-checklist.md)
  — item states and per-slice completion paragraphs.
- [Conformance traceability](../../10-maps/conformance-traceability.md) —
  the 517-obligation registry, per-area status, and immutable compiler
  commits.
- [Specification corpus](../../60-specification/README.md) — the 24
  normative areas and their conformance journals.
- [Home map](../../10-maps/home.md) — curated routes through the corpus.
- [Decision register](../design-decision-register.md) — every fork since
  C018.
- Compiler: `catena` repo, branch `rewrite`, merge `e0e3c16`
  (tree-identical to slice commit `0d96f96`).

## Sources

- [Catena API and ABI Compatibility](../catena-api-and-abi-compatibility.md)
  and the C027/C028 syntheses for the newest areas.
- [C028 evidence record](../../50-journal/2026-08-24-c028-api-compat.md)
  and its sibling journals for per-slice verification commands.
