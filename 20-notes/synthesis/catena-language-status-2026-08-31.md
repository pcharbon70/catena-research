---
title: "Catena Language Status: 31 August 2026"
kind: note
created: "2026-08-31"
maturity: developing
tags:
  - catena
  - language-design
  - status-report
aliases:
  - "Catena status report 0.1.39"
  - "Catena Sections 5 and 6 completion report"
---

# Catena Language Status: 31 August 2026

## Executive summary

As of revision `0.1.39` (C047–C058, merged 2026-08-31), the
checklist's Sections 1–6 are **complete** except D059's deferred
neighbors: 80 of 141 items, **40 normative specification areas**, and
644 registered conformance obligations with 545 fully traced to
executable compiler tests. The compiler (502 tests,
warnings-as-errors clean, byte-deterministic outputs) implements
every normative area on OTP 29 through the sole binary boundary
`compile:noenv_forms/2`.

Two sections closed since
[the 29 August report](catena-language-status-2026-08-29.md)
(`0.1.34`, 63/141). **Section 5 — data, collections, and patterns —
closed in four slices**: the built-in data model (C040's twelve-way
classification; Text/Character/Bytes elaborated from scanned
literals by the C018 scanner→meaning pattern; lists, maps, and sets
as library territory; references excluded), structural records and
variants (C041's seven-operation table with kernel rows verbatim and
semantic-map representation), collection construction and update
(C042's six-topic decision: persistent update IS constructor
application plus match recursion, miss is typed failure as a value,
complexity excluded because representation is invisible), and
pattern contexts (C044's three classes with C046's programmable-
pattern exclusion folded in). **Section 6 — comprehensions — closed
in one twelve-item slice** (C047–C058): the `for ... yield`
contract, eager and sequential over `List A → List B`, implemented
as a *dormant elaboration boundary* because both frontends are
frozen.

The shape of the era: nothing became a built-in. The only `List`
in the corpus is a declared nominal Cons list (`Nil`/`Cons`), the
comprehension elaborator emits its own, and the language promises
values, effects, and totals — never representations. What
deliberately does not exist is unchanged in kind but larger in
detail: a surface grammar (P109, now carrying accumulated adoption
debts), a standard library (G101+), processes and supervision
(G084/G089), cancellation (G088), distribution and hot upgrade
(G091/G092), migration engines (G116/P125), registry operations
(G130), tooling defaults (G121), plus the era's new exclusions —
language-level complexity promises, collection built-ins, exception
clauses, programmable patterns, and every non-list comprehension
source or target.

## Scope and method

This snapshot supersedes
[the 29 August report](catena-language-status-2026-08-29.md) (which
recorded `0.1.34` and Section 4's completion); that report remains
as history, as do
[the 26 August report](catena-language-status-2026-08-26.md)
(`0.1.29`) and [the August 24 report](catena-language-status-2026-08.md)
(`0.1.24`). Evidence is the archive's own state at this moment: the
[completeness checklist](../../00-inbox/language-specification-completeness-checklist.md),
the [traceability map](../../10-maps/conformance-traceability.md),
`validate_archive.py` (502 documents, 5,388 links, 644 obligations),
the sibling compiler's suite on `rewrite` at merge `7b0591d` (502
tests), the [decision register](../design-decision-register.md)
(forks C018–C058, every fork logged), and the specification corpus.
Claims cite their anchors; this note adds no new rules.

## The completed normative corpus

Forty areas. The table records this era's additions; the foundation
and organization bands are unchanged since
[the 29 August report](catena-language-status-2026-08-29.md#the-completed-normative-corpus).

| Rev | Area | Signature facts | Obligations |
| --- | --- | --- | --- |
| 0.1.1–0.1.24 | Foundation, source surface, organization | unchanged — HM typing; nominal ADTs; the kernel behavior contract; packages, entries, compatibility | 504 |
| 0.1.25–0.1.34 | Core expressions and evaluation | unchanged — values, order, bindings, functions, branching, equality, recursion, failure, observability, compile-time | 80 |
| 0.1.35 | Built-in data model | twelve-way classification; Text/Character/Bytes elaborated from C017 scanned literals (`Catena.Text`); lists/maps/sets as G101 library territory; references excluded | 8 |
| 0.1.36 | Structural records and variants | seven-operation table (literal, select, update, extend, restrict, inject, match) kernel-verbatim; closed literals; duplicate-label rejection; type-position tails; semantic maps | 8 |
| 0.1.37 | Collection construction and update | six-topic decision: update is constructor application plus match recursion; duplicate keys a G101 declaration obligation; ordering and key equality ride the comparable set; miss is typed failure as a value; complexity excluded | 8 |
| 0.1.38 | Pattern contexts | three classes — match the only exhaustive context, irrefutable-only the default, explicit-failure the only honest refutability; public receives reserved; exception clauses and programmable patterns excluded (C046) | 9 |
| 0.1.39 | List comprehensions | `for ... yield`: total generators, `case` mismatch-as-skip, typed `when` filters, exhaustive `let` bindings, visible effects, sequential depth-first traversal; dormant qualifier-tree elaboration to a fused worker chain; three `LCP` families | 14 |

## Checklist position by section

| Section | Complete / items | State |
| --- | --- | --- |
| Research consolidation | 6/6 | done |
| 1. Specification form and conformance | 6/6 | done |
| 2. Lexical grammar and source files | 8/8 | done |
| 3. Names, modules, packages, separate compilation | 8/8 | done |
| 4. Core expressions and evaluation | 10/10 | done |
| 5. Data, collections, and patterns | **8/8** | **done — closed by C040–C042, C044, C046** |
| 6. Comprehensions, generators, iteration | **12/13** | **done except D059 (neighboring iteration syntax, independently researched)** |
| 7. Type-system surface and advanced boundaries | 5/10 | partial — the next unchecked items live here |
| 8. Traits, derivation, categorical libraries | 7/7 | done |
| 9. Effects, failure, resource scopes | 4/8 | partial (failure closed; resource scopes remain) |
| 10. Processes, concurrency, distribution | 0/9 | open (runtime era) |
| 11. BEAM representation and Erlang interop | 0/8 | open |
| 12. Standard library contract | 0/8 | open (G101+) |
| 13. Specifications, governance, erasure | 6/8 | partial (P109 the large remainder) |
| 14. Diagnostics, tools, developer experience | 0/9 | open (P109/G121 era) |
| 15. Security, reproducibility, limits | 0/6 | open |
| 16. Formal validation and release gates | 0/9 | open |

Totals: 80 of 141 complete; the next semantic patch is `0.1.40`.

## The data-era method, recorded

Section 5 ran the Section 4 pattern into its natural limit:
**decide, don't build**. C040 classified rather than constructed;
C041 elevated the kernel's existing operations verbatim; C042 made
construction and update a routing decision over shipped machinery;
C044 turned C002's standing reservation into per-context classes
rather than new grammar. Each slice closed with zero or near-zero
new surface — the era added two public APIs total
(`Catena.Text.elaborate` and `Catena.Comprehension.elaborate/1`)
and four new diagnostic families (`EQN001` closed the prior era;
this era added only `LCP001`–`LCP003`). C047–C058 then showed the
pattern's newest form: a **dormant implementation** — the full
contract (typing, dynamics, effects, lowering, cost honesty)
implemented and validated through an elaboration boundary, with
surface tokens explicitly awaiting P109 — generalizing C035's
correct-but-dormant lowering from one operation to a whole feature.

The gates now standing add three shapes to Section 4's four
(edition-record, entry-rule, producer-gated finalization,
totality-or-bounded): **representation-invisibility exclusions**
(C041 semantic maps, C042's complexity exclusion — a language cost
bound would make representation observable), **reservation
consumption** (C044's context table consumed row-by-row by C047's
generator split), and **dormant adoption** (contracts implemented
beneath frozen frontends, adoption owned by P109).

## Cross-cutting guarantees

Unchanged in substance from
[the 29 August report](catena-language-status-2026-08-29.md#cross-cutting-guarantees),
now with the data era's teeth: determinism everywhere; nothing
implicit; the three-way partition (value, trap, running); semantic
identity with representation invisible — extended from values to
collections (a Cons list is the *declared* shape, never a language
guarantee, and BEAM lowers `Cons` to constructor tuples, not native
cons cells); evidence erasure and interface-only contracts;
compilation without execution; exact revisions.

## Declared absences and their owners

The prior table stands
([29 August report](catena-language-status-2026-08-29.md#declared-absences-and-their-owners));
the era adds:

| Absence | Owner | Note |
| --- | --- | --- |
| Collection built-ins / list-map-set types | G101 | collections are declared nominal ADTs; construction is constructor application |
| Language-level complexity promises | C042 exclusion | documentation is G101's library-level contract |
| Exception clauses | C036/C044 | trap is terminal; failures are typed values or traps |
| Programmable patterns | C046 | arrival conditions recorded (effects, totality, coverage, count, cost) |
| Lazy/parallel comprehension, non-list sources and targets | C047–C058 | each requires its own slice |
| References | C040/G084 | excluded from the data model |
| Comprehension surface tokens | P109 | the dormant boundary is the executable surface until adoption |

## Process and quality gates

- **Publication order held throughout**: research bundle → candidate
  chapters → obligation registry → compiler branch with gated tests →
  atomic promotion → compiler PR first → research PR. This era's
  merges, all tree-identical: compiler #115–#119 (`646e117`,
  `a4439eb`, `06f5584`, `e21a7b5`, `7b0591d`) against research
  #63–#67.
- **Gates.** `mix compile --warnings-as-errors`, 502 tests,
  `python3 validate_archive.py` (502 documents, 5,388 links, 644
  obligations), 26 validator unit tests, `git diff --check`.
- **Registry health.** 644 obligations: 545 traced, 78 partial
  (scoped follow-ups owned by their areas), 21 untraced
  (governance/version allow-lists).
- **Decision record.** Every fork logged since C018;
  recommendations carried on every fork since C021; the two
  overrides remain the early, durable ones (`.cat` extension,
  admitting recursion).
- **Recurring hazard, now a standing check**: the lifecycle
  `feature/2` registration has been lost by multi-edits four times
  (C033, C036, C040, C047); the per-area
  `{:ok, :stable} == LanguageLifecycle.state(...)` assertion catches
  it every time.
- **Documentation debt paid**: C042's promotion repaired
  CONFORMANCE.md — per-slice sections had stopped after C035 and
  the identity rows still said `0.1.22`; the convention is current
  through `0.1.39` and must stay so.

## Frontend facts worth keeping visible

The frozen frontends now shape every witness: the JSON AST
(`0.1.1`–`0.1.7`) cannot express self-recursive definitions (its
inference folds left-to-right), so recursive programs — collections
witnesses, comprehension worker chains — live on the kernel path
(`check_kernel`/`compile_kernel`/stepper/BEAM). The kernel checker's
coverage test is constructor-head exhaustiveness only;
usefulness-based redundancy (`M002`) lives in the JSON inference
path. Nested constructor sub-patterns read as partial for kernel
exhaustiveness, so generated code destructures through nested
matches. And the published parser nesting limit (1024 levels)
bounds literal witnesses — the comprehension stack-safety witness
runs 900 elements. All four facts are recorded in the era's
[journals](../../50-journal/README.md).

## Recommended next moves

1. **Section 7 — type-system surface and advanced boundaries**
   (5/10): the next unchecked items in order (G061 numeric
   relationships, G062 aliases and newtypes, G066 type-directed
   resolution, G067 dynamic and unsafe boundaries, D140 excluded
   advanced features) — the natural continuation of the
   decision-not-design method.
2. **Section 9's resource half** (G080 cleanup and resource scopes,
   G081 the exception boundary — largely pre-answered by C036/C044's
   exclusions, G082 top-level effects) as a compact second track.
3. **P109 readiness accounting** before any capstone work: the
   adoption debts now include the conditional sugar promise,
   multi-parameter sugar, comprehension tokens, irrefutable-only
   pattern bindings, and span-faithful comprehension diagnostics —
   a scoping note would keep the capstone from becoming several
   slices in disguise.

## Route to sources

- The [completeness checklist](../../00-inbox/language-specification-completeness-checklist.md)
  for position, [remaining research areas](../../00-inbox/remaining-catena-research-areas.md)
  for the open program, and the [decision register](../design-decision-register.md)
  for every fork.
- The era's evidence: journals for
  [C040](../../50-journal/2026-08-29-c040-data-model.md),
  [C041](../../50-journal/2026-08-29-c041-records.md),
  [C042](../../50-journal/2026-08-31-c042-collections.md),
  [C044](../../50-journal/2026-08-31-c044-pattern-contexts.md), and
  [C047](../../50-journal/2026-08-31-c047-comprehensions.md).
- The topic maps for
  [records](../../10-maps/structural-records.md),
  [collections](../../10-maps/collection-construction-and-update.md),
  [pattern contexts](../../10-maps/pattern-contexts.md), and
  [comprehensions](../../10-maps/list-comprehensions.md).
