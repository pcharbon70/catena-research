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

Fixed in: [synthesis](catena-equality-and-ordering.md) — the
normative specification, journal, and this table's durable links land
with this slice's promotion commits.

| Fork | Options offered | Chosen |
| --- | --- | --- |
| Area shape | new area EQ 0.1.30 (rec) / extend clause-conditions / extend values area | new area EQ |
| Float equality | bit-exact, −0.0 ≠ 0.0 (rec) / IEEE −0.0 = 0.0 / defer to G061 | bit-exact |
| Comparable domain | primitives + structural (rec) / primitives only / everything with identity | primitives + structural |
| Mixed numerics | monomorphic (rec) / exact mixed comparison | monomorphic |
| Trait layer | built-ins now, traits later (rec) / overloading via traits now / built-ins forever | built-ins now |
| Deliverable | classifier + wiring + EQN001 (rec) / wiring only, reuse CND003 / normative-only | classifier + EQN001 |


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
