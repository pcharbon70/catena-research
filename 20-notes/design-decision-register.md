---
title: "Catena Design Decision Register"
kind: note
created: "2026-08-24"
maturity: developing
tags:
  - catena
  - decision-log
  - language-design
aliases:
  - "Catena fork decision register"
---

# Catena Design Decision Register

## Purpose

This register is the durable record of every developer fork decision made
during gap-plan review: where a plan posed enumerated options, which
option the developer chose, which option carried the recommendation, and
where the choice became normative. The plan conversations themselves are
the only other place the options-as-posed survive; this register removes
that single point of loss.
It records **plan-fork decisions only**. Two neighbors hold related
material and are not duplicated here: decisions that *emerged during
implementation* (for example C022's qualified-references-don't-count
rule, C024's inhabitation seeding) live in each slice's journal under
`## Observations`, and the reasoning for and against each option lives in
each synthesis under "Selected model" and "Rejected alternatives".

**Maintenance rule:** every future gap plan's forks get their rows added
here in the same change as that plan's Phase 1 research bundle.

**Notation:** in each Options column, `(rec)` marks the option the plan
recommended; `†` on the Chosen column marks a developer override of that
recommendation. Two overrides exist so far — the `.cat` extension (C020)
and admitting module recursion (C024) — and both proved durable.

## C018 — numeric literal semantics (`0.1.14`, 2026-08-21)

Fixed in: [specification](../60-specification/numeric-literal-semantics/README.md)
· [synthesis](catena-numeric-literal-semantics.md)
· [journal](../50-journal/2026-08-21-c018-numeric-literal-semantics.md)

| Fork | Options offered | Chosen |
| --- | --- | --- |
| Slice scope | G018 only (rec) / G018+G061 / integers only | G018 only |
| Float model | finite binary64, BEAM traps (rec) / full IEEE 754 / exact rational | finite binary64 |
| Literal typing | monomorphic, no defaulting (rec) / constrained+defaulting / expected-type adaptation | monomorphic |
| Coercions | none (rec) / literal-only widening / general Int→Float | none |
| Literal overflow | static invalid `NUM001` (rec) / trap-at-runtime value / new implementation limit | static invalid |
| Negation | semantics, not syntax (rec) / negative patterns / defer to G019 | semantics only |
| Float digit bound | new portable floor `LIM005` 4,096 (rec) / no limit / defer | `LIM005` |
| Fold-in repairs | full fold-in (rec) / C018-only / minimal evidence | full |

## C019 — operators and punctuation (`0.1.15`, 2026-08-21)

Fixed in: [specification](../60-specification/operators-and-punctuation/README.md)
· [synthesis](catena-operators-and-punctuation.md)
· [journal](../50-journal/2026-08-21-c019-operators-and-punctuation.md)

| Fork | Options offered | Chosen |
| --- | --- | --- |
| Deliverable | tokens + whole lexer + operator expressions (rec) / tokens+lexer only / atomic scanner only | full stack |
| Operator set | closed semantic-mapped (rec) / full speculative table / word operators | closed set |
| Fixity model | fixed table, no user fixity (rec) / user fixity declarations / full parenthesization | fixed table |
| Pipes | include `\|>` (rec) / defer / forward+backward | include |
| Delimiter frames | parens+brackets continued, braces block (rec) / all continued / defer to P109 | split modes |
| Negation `-` | prefix operator only (rec) / negative-literal folding / one token two roles | prefix only |
| Qualification | dot-only, C014-aligned (rec) / namespace separators / plain punctuation | dot-only |
| Parse recovery | deterministic reject, no recovery (rec) / resynchronization | no recovery |

## C020 — file-to-module relationship (`0.1.16`, 2026-08-22)

Fixed in: [specification](../60-specification/files-and-modules/README.md)
· [synthesis](catena-files-and-modules.md)
· [journal](../50-journal/2026-08-22-c020-files-and-modules.md)

| Fork | Options offered | Chosen |
| --- | --- | --- |
| Modules per file | at most one (rec) / exactly one, empties invalid / multiple | at most one |
| Filename match | must match, else invalid (rec) / warning only / filename-derived name | must match |
| File extension | `.catena` (rec) / `.cat` / multiple / don't fix | `.cat` † (accepted Windows-collision cost) |
| Generated files | first-line marker comment (rec) / filename convention / sidecar manifest / defer | marker comment |
| Module-name spelling | ASCII uppercase-initial (rec) / C014 XID / defer to P109 | ASCII word |
| Deliverable | abstract events API (rec) / API + check-file CLI / normative-only | abstract API |

## C021 — namespaces and shadowing (`0.1.17`, 2026-08-22)

Fixed in: [specification](../60-specification/namespaces-and-shadowing/README.md)
· [synthesis](catena-namespaces-and-shadowing.md)
· [journal](../50-journal/2026-08-22-c021-namespaces-and-shadowing.md)

| Fork | Options offered | Chosen |
| --- | --- | --- |
| Deliverable | namespace contract + abstract resolver (rec) / G021+G022 combined / normative-only | abstract resolver |
| Namespace model | per-category + spelling classes (rec) / single flat / per-category spelling-free | per-category |
| Type variables | own namespace, may shadow types (rec) / no shadowing / defer | may shadow |
| Shadowing policy | allow, deterministic, silent (rec) / deny-able warning / forbid | silent |
| Ambiguity | local > imported; collisions reject (rec) / all collisions invalid / order-based priority | precedence + reject |
| Governed identities | own namespaces, fully separate (rec) / share program namespaces / defer | separate |
| Qualification depth | exactly two segments (rec) / arbitrary nesting / defer to G022 | two segments |

## C022 — imports and exports (`0.1.18`, 2026-08-22)

Fixed in: [specification](../60-specification/imports-and-exports/README.md)
· [synthesis](catena-imports-and-exports.md)
· [journal](../50-journal/2026-08-22-c022-imports-and-exports.md)

| Fork | Options offered | Chosen |
| --- | --- | --- |
| Slice scope | G022 only (rec) / G022+G024 / normative-only | G022 only |
| Import admission | qualification + explicit name list (rec) / unqualified by default / qualification-only | qualify + list |
| Renaming | excluded (rec) / module aliases / per-name renames | excluded |
| Re-exports | excluded, deferred to G025 (rec) / forwarding form now | excluded |
| Unused imports | deny-able warning `IMP001` (rec) / hard error / defer to P117 | deny-able warning |
| Visibility default | explicit export, else private (rec) / public by default / per-category defaults | private by default |
| Deliverable | abstract events + analysis (rec) / API + CLI / normative-only | events + analysis |

## C023 — abstraction boundaries (`0.1.19`, 2026-08-23)

Fixed in: [specification](../60-specification/abstraction-boundaries/README.md)
· [synthesis](catena-abstraction-boundaries.md)
· [journal](../50-journal/2026-08-23-c023-abstraction-boundaries.md)

| Fork | Options offered | Chosen |
| --- | --- | --- |
| Slice shape | thin slice at `0.1.19` (rec) / no-revision amendment / full feature slice | thin slice |
| Stable layout | declared exclusion, owner G028 (rec) / admit now / reserve spelling | exclusion |
| Authority split | binary modes + blessed idiom (rec) / construction-only mode / both directions | binary + idiom |
| Evidence | exclusion-proof + idiom tests (rec) / normative-only | executable corpus |

## C024 — module dependency cycles (`0.1.20`, 2026-08-24)

Fixed in: [specification](../60-specification/module-dependency-cycles/README.md)
· [synthesis](catena-dependency-cycles.md)
· [journal](../50-journal/2026-08-24-c024-dependency-cycles.md)

Round 1 — the original plan forks:

| Fork | Options offered | Chosen |
| --- | --- | --- |
| Module recursion | declared exclusion (rec) / admit SCC compilation / pre-declared interfaces | **admit SCC** † |
| Detection model | graph edges in builder (rec) / provided-graph only / separate checker API | edges in builder |
| Diagnostic shape | single `CYC001` with path (rec) / `CYC001`+`CYC002` split / reuse existing families | single `CYC001` |
| Failure timing | at the closing event (rec) / at first resolution | closing event |
| Consequence clauses | confirm as-is (rec) / defer to G025 | confirm (superseded below) |
| Mutual-recursion story | inversion idiom normative (rec) / non-normative note / omit | normative |

Round 2 — reconciliation forks, required because round 1 admitted SCC
while the other answers had assumed the exclusion route:

| Fork | Options offered | Chosen |
| --- | --- | --- |
| SCC semantics | SCC unit, signatures inside (rec) / pre-declared interfaces everywhere / fixpoint digests | signatures inside |
| `CYC001` role | regime/signature violations (rec) / no `CYC001` / bounded cycles only | regime violations |
| Consequence clauses | SCC-adapted confirmations (rec) / literal as-is | SCC-adapted |
| Slice size | full admission slice (rec) / abstract-only / revert to exclusion | full slice |


## C025 — package identity and dependency resolution (`0.1.21`, 2026-08-24)

Fixed in: [specification](../60-specification/package-identity-and-dependencies/README.md)
· [synthesis](catena-package-identity-and-dependencies.md)
· [journal](../50-journal/2026-08-24-c025-package-identity.md)

| Fork | Options offered | Chosen |
| --- | --- | --- |
| Dependency declaration | manifest `dependencies` field (rec) / separate deps file / path-only deps | manifest field |
| Version grammar | SemVer + `^`/`~`/exact, Cargo-style 0.x caret (rec) / exact pins only / full Hex operators | SemVer + three forms |
| Conflict policy | single version, highest-satisfying (rec) / side-by-side versions / first-found wins | single version |
| Lockfile | generated `catena.lock` with replay (rec) / no lockfile / normative-only | generated lockfile |
| Identity + integrity | neutral name+version+SHA-256 bundle digest, Hex as profile (rec) / tarball-checksum identity / signed lockfile now | neutral digest |
| Re-exports | stay excluded, re-owned by G028 era (rec) / minimal forwarding now / silent | excluded, re-owned |
| Deliverable | `Catena.Package.Deps` engine library (rec) / engine + CLI / normative-only | engine library |

## C026 — prelude policy (`0.1.22`, 2026-08-24)

Fixed in: [specification](../60-specification/prelude-policy/README.md)
· [synthesis](catena-prelude-policy.md)
· [journal](../50-journal/2026-08-24-c026-prelude-policy.md)

| Fork | Options offered | Chosen |
| --- | --- | --- |
| Automatic imports | opt-in via manifest (rec) / always-on with opt-out / declared full absence | opt-in via manifest |
| Precedence | ordinary import origin (rec) / weaker-than-imports tier / prelude-priority tier | ordinary origin |
| Opt-out shape | absent/null = out (rec) / explicit none-sentinel / per-name hiding | absent/null = out |
| Edition guarantee | 0.1 guarantees zero implicit names (rec) / names empty seed prelude / defer the clause | zero implicit names |
| G101 boundary | mechanism now, contents G101 (rec) / mechanism + minimal contents / normative-only | mechanism now |
| Deliverable | event grammar + manifest + locks (rec) / events only / mechanism + tooling default | full wiring |


## C027 — entry points and application structure (`0.1.23`, 2026-08-24)

Fixed in: [specification](../60-specification/entry-points/README.md)
· [synthesis](catena-entry-points.md)
· [journal](../50-journal/2026-08-24-c027-entry-points.md)

| Fork | Options offered | Chosen |
| --- | --- | --- |
| Root shape | named entry exports in manifest (rec) / reserved `main` name / declared full absence | named entry exports |
| Top-level effects | effect-closed entries (rec) / implicit host handler / manifest-named handlers | effect-closed |
| Startup model | invocation-only (rec) / OTP application start / spawn-per-entry | invocation-only |
| Shutdown results | return-is-shutdown (rec) / exit-code mapping / defer shutdown clause | return-is-shutdown |
| Library distinction | derived from zero entries (rec) / explicit `kind` field | derived |
| Deliverable | manifest entries + launch op (rec) / normative-only / entries + CLI | entries + launch op |


## C028 — API and ABI compatibility (`0.1.24`, 2026-08-24)

Fixed in: [specification](../60-specification/api-and-abi-compatibility/README.md)
· [synthesis](catena-api-and-abi-compatibility.md)
· [journal](../50-journal/2026-08-24-c028-api-compat.md)

| Fork | Options offered | Chosen |
| --- | --- | --- |
| Layer coverage | source+type rules, principled absence (rec) / full four-layer rules / type-only | source+type, absences |
| Major version | SemVer major + Cargo 0.x (rec) / new Catena scheme / defer to 1.0 | SemVer major + Cargo 0.x |
| Breaking matrix | strict diff matrix (rec) / removals-only / over-strict | strict diff matrix |
| BEAM ABI stance | declared absence (rec) / minimal ABI contract | declared absence |
| Re-export facades | formal exclusion (rec) / minimal facade mechanism / defer again | formal exclusion |
| Deliverable | compat diff + claim validator (rec) / normative-only / classifier + tooling | diff + validator |
| Source evidence | Erlang compatibility chapter (rec) / existing notes only / ecosystem-tooling note too | Erlang chapter |


## C029 — values and evaluation (`0.1.25`, 2026-08-24)

Fixed in: [specification](../60-specification/values-and-evaluation/README.md)
· [synthesis](catena-values-and-evaluation.md)
· [journal](../50-journal/2026-08-24-c029-values.md)

| Fork | Options offered | Chosen |
| --- | --- | --- |
| Area shape | new area VA 0.1.25 (rec) / amend the kernel area / defer into a neighbor | new area VA |
| Value grammar | closed: kernel + Float (rec) / open canonical-forms / kernel list verbatim | closed, +Float |
| First-classness | uniform first-class (rec) / tiered passable-storable / per-type restrictions | uniform |
| Strictness stance | invariant + exceptions + gate (rec) / kernel restatement / merge with P030 | invariant + gate |
| Deliverable | classifier + property tests (rec) / normative-only / classifier + eval entry | classifier + tests |


## C030 — evaluation order (`0.1.26`, 2026-08-25)

Fixed in: [specification](../60-specification/evaluation-order/README.md)
· [synthesis](catena-evaluation-order.md)
· [journal](../50-journal/2026-08-25-c030-evaluation-order.md)

| Fork | Options offered | Chosen |
| --- | --- | --- |
| Area shape | new area EO 0.1.26 (rec) / extend values area / defer into G031 | new area EO |
| Account shape | closed table + entry rule (rec) / general rule only / table without entry rule | closed table + entry rule |
| G031/G032 line | order vs structure split (rec) / leave bindings to G031 / fold G031 in | order vs structure |
| Observability | observable via traces (rec) / advisory for pure forms | observable via traces |
| Deliverable | dual-target trace tests (rec) / order table module / normative-only | dual-target trace tests |


## C031 — bindings and sequencing (`0.1.27`, 2026-08-25)

Fixed in: [specification](../60-specification/bindings-and-sequencing/README.md)
· [synthesis](catena-bindings-and-sequencing.md)
· [journal](../50-journal/2026-08-25-c031-bindings.md)

| Fork | Options offered | Chosen |
| --- | --- | --- |
| Area shape | new area BS 0.1.27 (rec) / extend evaluation-order / merge with G032 | new area BS |
| Recursion line | definitions-only recursion (rec) / local recursive let / local letrec-and | definitions-only |
| Unused bindings | valid + deny-able BS001 (rec) / valid, silent only / hard error | valid + BS001 |
| Sequencing form | let-idiom is the form (rec) / distinct sequence form | let-idiom |
| Shadowing line | C021 verbatim (rec) / restrict import shadowing | C021 verbatim |
| Deliverable | witnesses + BS001 wiring (rec) / descriptive module / normative-only | witnesses + BS001 |


## C032 — functions and calls (`0.1.28`, 2026-08-25)

Fixed in: [specification](../60-specification/functions-and-calls/README.md)
· [synthesis](catena-functions-and-calls.md)
· [journal](../50-journal/2026-08-25-c032-functions.md)

| Fork | Options offered | Chosen |
| --- | --- | --- |
| Arity model | semantic-unary curried (rec) / fixed arity / hybrid | semantic-unary curried |
| Partial application | free prefix application (rec) / excluded / explicit-only | free prefix |
| Closure capture | lexical, immutable (rec) / by-reference / explicit captures | lexical, immutable |
| Local functions | let-bound closures (rec) / local recursion now / new sugar form | let-bound closures |
| Tail calls | elevate + deep witness (rec) / state only / defer | elevate + deep witness |
| Deliverable | witnesses, zero families (rec) / arity diagnostics / normative-only | witnesses, zero families |


## C033 — branching (`0.1.29`, 2026-08-25)

Fixed in: [specification](../60-specification/branching/README.md)
· [synthesis](catena-branching.md)
· [journal](../50-journal/2026-08-25-c033-branching.md)

| Fork | Options offered | Chosen |
| --- | --- | --- |
| Area shape | new area BR 0.1.29 (rec) / extend clause-conditions / defer to G040 | new area BR |
| General conditional | match-only + sugar promise (rec) / match-only, no promise / new if form now | match-only + promise |
| Statement forms | declared absence (rec) / defer to P109 / reserve statement tier | declared absence |
| Consolidation scope | full consolidation (rec) / minimal residuals only | full consolidation |
| Deliverable | witnesses, zero families (rec) / new branch warnings / normative-only | witnesses, zero families |


## C035 — equality and ordering (`0.1.30`, 2026-08-26)

Fixed in: [specification](../60-specification/equality-and-ordering/README.md)
· [synthesis](catena-equality-and-ordering.md)
· [journal](../50-journal/2026-08-26-c035-equality.md)

| Fork | Options offered | Chosen |
| --- | --- | --- |
| Area shape | new area EQ 0.1.30 (rec) / extend clause-conditions / extend values area | new area EQ |
| Float equality | bit-exact, −0.0 ≠ 0.0 (rec) / IEEE −0.0 = 0.0 / defer to G061 | bit-exact |
| Comparable domain | primitives + structural (rec) / primitives only / everything with identity | primitives + structural |
| Mixed numerics | monomorphic (rec) / exact mixed comparison | monomorphic |
| Trait layer | built-ins now, traits later (rec) / overloading via traits now / built-ins forever | built-ins now |
| Deliverable | classifier + wiring + EQN001 (rec) / wiring only, reuse CND003 / normative-only | classifier + EQN001 |


## C034 — recursion and termination (`0.1.31`, 2026-08-26)

Fixed in: [specification](../60-specification/recursion-and-termination/README.md)
· [synthesis](catena-recursion-and-termination.md)
· [journal](../50-journal/2026-08-26-c034-recursion.md)

| Fork | Options offered | Chosen |
| --- | --- | --- |
| Area shape | new area RT 0.1.31 (rec) / extend functions area / defer into G038 | new area RT |
| Program stance | unrestricted + elevated (rec) / reserve a checker / check termination now | unrestricted + elevated |
| Separation table | cited classification table (rec) / minimal prose only | cited table |
| Future-fragment gate | entry-rule gate (rec) / design the fragment now / no gate | entry-rule gate |
| Deliverable | witnesses, zero families (rec) / analysis module / normative-only | witnesses, zero families |


## C036 — runtime failure taxonomy (`0.1.32`, 2026-08-26)

Fixed in: [specification](../60-specification/runtime-failure-taxonomy/README.md)
· [synthesis](catena-runtime-failure-taxonomy.md)
· [journal](../50-journal/2026-08-26-c036-failure.md)

| Fork | Options offered | Chosen |
| --- | --- | --- |
| Area shape | new area FT 0.1.32 (rec) / extend values area / defer to G084 | new area FT |
| Taxonomy shape | one outcome, kinded reasons (rec) / multi-class outcomes | one outcome, kinded |
| Category mapping | six-way mapping (rec) / all six defined now / trap only | six-way mapping |
| Trap observability | kernel verbatim + witnesses (rec) / classification only / link-monitor exits | kernel verbatim |
| Entry rule | per producer (rec) / pre-defined spellings / no gate | per producer |
| Deliverable | witnesses, zero families (rec) / classification module / normative-only | witnesses, zero families |


## C037 — resource observability (`0.1.33`, 2026-08-26)

Fixed in: [specification](../60-specification/resource-observability/README.md)
· [synthesis](catena-resource-observability.md)
· [journal](../50-journal/2026-08-26-c037-observability.md)

| Fork | Options offered | Chosen |
| --- | --- | --- |
| Area shape | new area RO 0.1.33 (rec) / extend values area / defer to G084 | new area RO |
| Model shape | kernel verbatim, six-way (rec) / list only / admit observables | kernel verbatim, six-way |
| Finalization | declared absence + gate (rec) / design cleanup now / reserve spellings | declared absence + gate |
| Identity rule | two-clause identity (rec) / defer closure identity / handle identity equality | two-clause |
| Deliverable | witnesses, zero families (rec) / identity helpers / normative-only | witnesses, zero families |


## C038 — compile-time evaluation (`0.1.34`, 2026-08-26)

Fixed in: [specification](../60-specification/compile-time-evaluation/README.md)
· [synthesis](catena-compile-time-evaluation.md)
· [journal](../50-journal/2026-08-26-c038-compile-time.md)

| Fork | Options offered | Chosen |
| --- | --- | --- |
| Area shape | new area CE 0.1.34 (rec) / extend recursion area / defer to P109 | new area CE |
| Overall stance | absence + gate (rec) / design const-eval now / design macros now | absence + gate |
| Derivations | compiler-internal generation (rec) / treat as gated execution / defer to G040 | compiler-internal |
| Restrictions | cited restriction table (rec) / gate citation only | cited table |
| Deliverable | witnesses, zero families (rec) / evaluator skeleton / normative-only | witnesses, zero families |


## C040 — built-in data model (`0.1.35`, 2026-08-29)

Fixed in: [specification](../60-specification/built-in-data-model/README.md)
· [synthesis](catena-built-in-data-model.md)
· [journal](../50-journal/2026-08-29-c040-data-model.md)

| Fork | Options offered | Chosen |
| --- | --- | --- |
| Area shape | new area BM 0.1.35 (rec) / extend values area / defer to P109 | new area BM |
| 12-way classification | typed now, library, excluded (rec) / all twelve built-in / classify existing only | typed now, library, excluded |
| Text semantics | C018 pattern, three types (rec) / Character as Int alias / text-as-bytes | C018 pattern, three types |
| Comparability | content-based entries (rec) / equality only / defer to G101 | content-based entries |
| Deliverable | elaboration + classifier (rec) / pipeline integration / normative-only | elaboration + classifier |


## C041 — structural records and variants (`0.1.36`, 2026-08-29)

Fixed in: [specification](../60-specification/structural-records-and-variants/README.md)
· [synthesis](catena-structural-records.md)
· [journal](../50-journal/2026-08-29-c041-records.md)

| Fork | Options offered | Chosen |
| --- | --- | --- |
| Area shape | new area SR 0.1.36 (rec) / extend data-and-patterns / defer to G042 | new area SR |
| Coverage shape | full kernel consolidation (rec) / partial elevation | full consolidation |
| Row typing | kernel rows verbatim (rec) / open-record literals / defer tails | kernel rows verbatim |
| Representation | semantic maps verbatim (rec) / stable layout | semantic maps |
| Deliverable | kernel-path witnesses (rec) / frontend integration / normative-only | kernel-path witnesses |


## C042 — collection construction and update (`0.1.37`, 2026-08-31)

Fixed in: [synthesis](catena-collection-operations.md) — the
normative specification, journal, and this table's durable links land
with this slice's promotion commits.

| Fork | Options offered | Chosen |
| --- | --- | --- |
| Area shape | new area CO 0.1.37 (rec) / defer to G101 / extend data-model area | new area CO |
| Six-way stance | decision + routing (rec) / design operations now / routing table only | decision + routing |
| Bounds failures | typed failure as value (rec) / trap on miss / defer to G105 | typed failure as value |
| Complexity | excluded from language (rec) / promise complexity now / defer silently | excluded from language |
| Deliverable | nominal-ADT witnesses (rec) / collection built-ins / normative-only | nominal-ADT witnesses |

## C044 — pattern contexts (`0.1.38`, 2026-08-31)

Fixed in: [synthesis](catena-pattern-contexts.md) — the
normative specification, journal, and this table's durable links land
with this slice's promotion commits. Closes P044 and D046.

| Fork | Options offered | Chosen |
| --- | --- | --- |
| Slice shape | classification slice (rec) / implement let-patterns too / pointer-only closure | classification slice |
| Generators | fix principle, defer grammar to P051 (rec) / leave entirely to Section 6 | fix principle, defer grammar |
| Absent contexts | reserve public receives + exclude exception clauses (rec) / reserve both / exclude both | reserve receives, exclude exceptions |
| D046 handling | fold exclusion in (rec) / leave deferred as its own slice | fold exclusion in |
| Area naming | pattern-contexts PC (rec) / refutability-by-context RC / extend data-and-patterns | pattern-contexts PC |


## C047–C058 — list comprehensions (`0.1.39`, 2026-08-31)

Fixed in: [synthesis](list-comprehensions.md) — the normative
specification, journal, and this table's durable links land with this
slice's promotion commits. Closes P047–P058; D059 stays deferred.

| Fork | Options offered | Chosen |
| --- | --- | --- |
| Scope | P047–P058, all of Section 6's checkable items (rec) / P047–P056 only | P047–P058 |
| Implementation | dormant elaboration to kernel, P109 adopts surface (rec) / normative-only / new frontend now | dormant elaboration |
| Grammar home | semantic roles and keywords here, token integration P109 (rec) / all grammar at P109 | grammar here, integration P109 |
| Area naming | list-comprehensions LC (rec) / comprehensions-and-iteration CI | list-comprehensions LC |
| Diagnostics | minimal new LCP set — rebinding, never-match marker, unnecessary marker (rec) / full 12-diagnostic set / zero new families | minimal LCP set |

## C061 — numeric relationships (`0.1.40`, 2026-08-31)

Fixed in: [synthesis](catena-numeric-relationships.md) — the
normative specification, journal, and this table's durable links land
with this slice's promotion commits. Closes G061.

| Fork | Options offered | Chosen |
| --- | --- | --- |
| Mechanism | closed-set instantiation, no dispatch (rec) / Numeric trait dispatch / defer to P109 | closed-set instantiation |
| Float arithmetic | extend, witness via annotations (rec) / codify but keep Int-only | extend, witness via annotations |
| Division/remainder | route to G105 (rec) / fix division now | route to G105 |
| Area naming | numeric-relationships NR (rec) / extend operators area / numeric-operator-instantiation NOI | numeric-relationships NR |

## C062 — aliases and newtypes (`0.1.41`, 2026-09-01)

Fixed in: [synthesis](catena-aliases-and-newtypes.md) — the
normative specification, journal, and this table's durable links land
with this slice's promotion commits. Closes G062.

| Fork | Options offered | Chosen |
| --- | --- | --- |
| Type aliases | exclude with arrival conditions (rec) / define now dormant / leave open | exclude with conditions |
| Newtype deriving | explicit-target only, no inheritance (rec) / Haskell-style automatic | explicit only |
| Slice shape | classification slice on existing machinery (rec) / dormant implementation / defer | classification slice |
| Area naming | aliases-and-newtypes AN (rec) / aliases-opaque-and-newtypes AON / type-wrappers TW | aliases-and-newtypes AN |

## C066 — name resolution (`0.1.42`, 2026-09-01)

Fixed in: [synthesis](catena-name-resolution.md) — the normative
specification, journal, and this table's durable links land with this
slice's promotion commits. Closes G066.

| Fork | Options offered | Chosen |
| --- | --- | --- |
| The stance | type-independent resolution with the five-way table (rec) / admit per class / defer | type-independent |
| Evidence carve-out | instance selection is evidence, not resolution (rec) / count as resolution | evidence, not resolution |
| Slice shape | classification slice on existing machinery (rec) / dormant implementation / merge with G067 | classification slice |
| Area naming | name-resolution NMR (rec) / resolution-independence RI / type-independent-resolution TIR | name-resolution (code RN — the validator's two-letter obligation-ID contract) |

## C067 — dynamic and unsafe boundaries (`0.1.43`, 2026-09-01)

Fixed in: [synthesis](catena-dynamic-and-unsafe-boundaries.md) — the
normative specification, journal, and this table's durable links land
with this slice's promotion commits. Closes G067.

| Fork | Options offered | Chosen |
| --- | --- | --- |
| The stance | exclude intralingually with arrival conditions (rec) / define dyn now / partial reservation | exclude intralingually |
| Visibility routing | route to foreign owners as a requirement (rec) / define mechanism now | route to foreign owners |
| Slice shape | exclusion slice on existing machinery (rec) / dormant machinery / defer to foreign era | exclusion slice |
| Area naming | dynamic-and-unsafe-boundaries DU (rec) / unsafe-boundaries UB / casts-and-dynamics CD | dynamic-and-unsafe-boundaries DU |

## C140 — excluded advanced type features (`0.1.44`, 2026-09-01)

Fixed in: [synthesis](catena-excluded-advanced-types.md) — the
normative specification, journal, and this table's durable links land
with this slice's promotion commits. Closes D140; Section 7 completes
at 10/10.

| Fork | Options offered | Chosen |
| --- | --- | --- |
| Slice shape | small confirmation slice at 0.1.44 (rec) / pointer-only closure / fold into P132 | confirmation slice |
| Table scope | full C001 list of seven forms (rec) / D140's five forms only | full C001 list |
| Arrival conditions | adopt the seven-point gate verbatim (rec) / bespoke per form | seven-point gate |
| Area naming | excluded-advanced-type-features EA (rec) / advanced-type-boundaries AB / extend type-system area | excluded-advanced-type-features EA |

## C132 — progress and preservation (`0.1.45`, 2026-09-01)

Fixed in: [synthesis](catena-progress-and-preservation.md) — the
normative specification, journal, and this table's durable links land
with this slice's promotion commits. Closes P132; Section 16 opens.

| Fork | Options offered | Chosen |
| --- | --- | --- |
| Completion bar | state targets + evidence, route proofs (rec) / prove now / split and defer | state targets + evidence |
| Integrated theorem | composed statement with routed lemma (rec) / defer to Section 16 / claim now | composed statement |
| Processes/foreign | conditional + routed extensions (rec) / unconditional now | conditional + routed |
| Area naming | progress-and-preservation PP (rec) / metatheory-targets MT / extend type-system | progress-and-preservation PP |

## C086 — selective receive (`0.1.46`, 2026-09-01)

Fixed in: [synthesis](catena-selective-receive.md) — the normative
specification, journal, and this table's durable links land with this
slice's promotion commits. Closes P086; Section 9 advances to 5/8.

| Fork | Options offered | Chosen |
| --- | --- | --- |
| Completion stance | rule set + routed interfaces (rec) / full feature with timeouts now / defer to process era | rule set + routed interfaces |
| Starvation stance | honest cost explanation (rec) / fairness guarantee | honest cost explanation |
| Witness scope | preservation witness (rec) / re-pin only / dormant machinery | preservation witness |
| Area naming | selective-receive SR (rec) / receive-semantics RS / extend clause-conditions | selective-receive (code RC — SR is structural-records') |

## C081 — exception boundary (`0.1.47`, 2026-09-01)

Fixed in: [synthesis](catena-exception-boundary.md) — the normative
specification, journal, and this table's durable links land with this
slice's promotion commits. Closes G081; Section 9 advances to 6/8.

| Fork | Options offered | Chosen |
| --- | --- | --- |
| Mechanism stance | partition + no language mechanism (rec) / admit exceptions / defer | partition + none |
| Panic classification | panic = trap kind (rec) / separate panic construct | panic = trap kind |
| Effect pattern | bless non-resumed requests as the pattern (rec) / leave unstated | bless the pattern |
| Area naming | exception-boundary XB (rec) / failure-boundaries FB / panic-and-escape PE | exception-boundary XB |

## C082 — top-level effects (`0.1.48`, 2026-09-01)

Fixed in: [synthesis](catena-top-level-effects.md) — the normative
specification, journal, and this table's durable links land with this
slice's promotion commits. Closes G082; Section 9 advances to 7/8.

| Fork | Options offered | Chosen |
| --- | --- | --- |
| Completion stance | confirm and route (rec) / design the capability channel now / defer | confirm and route |
| Capability interface | explicit typed values, never ambient (rec) / reserve a host handler | explicit values |
| Slice shape | two-chapter confirmation slice (rec) / three chapters | two chapters |
| Area naming | top-level-effects TL (rec) / entry-effects EE / ambient-boundaries AB | top-level-effects TL |

## Cross-cutting decisions

- **Package publishing substrate (2026-08-22):** adopt the Hex registry
  Gleam-style as the working hypothesis for G025/G121/G130, with Catena
  governance kept inner-package. Not a plan fork — an out-of-band
  developer decision recorded in
  [the inbox capture](../00-inbox/package-publishing-hypothesis-hex.md).
  Subsequently profiled normatively by C025.

## Connections

- Each slice's synthesis (linked per section) holds the option reasoning
  and falsification criteria; its journal holds emergent implementation
  decisions; its specification holds the chosen rules.
- The [completeness checklist](../00-inbox/language-specification-completeness-checklist.md)
  tracks which gaps have consumed forks; this register tracks what the
  forks chose.
- [Remaining Catena Research Areas](../00-inbox/remaining-catena-research-areas.md)
  names the programs whose future plans will extend this register.
