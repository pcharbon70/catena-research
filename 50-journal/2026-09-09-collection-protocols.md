---
title: "Collection Protocol Implementation"
kind: journal
created: "2026-09-09"
tags: [language-design, collections, conformance]
aliases: []
---

# Collection Protocol Implementation

## Starting point and scope

C100 merged through [compiler PR 146](https://github.com/pcharbon70/catena/pull/146)
and [research PR 96](https://github.com/pcharbon70/catena-research/pull/96).
Compiler `rewrite` was `aa7107ccc4398c28fde445a074e1153748832ed6`;
research `main` was `c9210e0d89de52b317de96fb850917405dc9f03a`.
Both integration branches were synchronized before their feature branches were
deleted. This slice uses `codex/collection-protocols`. The user's session-wide
revision approval covers `0.1.65`; no continuation is scheduled.

The [CP-102 plan](../20-notes/language-completion-plan-delivery.md#item-102-collection-protocols)
and [original decision register](../20-notes/design-decision-register.md)
select lawful families, semantic order, owned pulls and strict construction.
The [normative contract](../60-specification/collection-protocols/finite-families-and-owned-pulls.md)
supplies those semantics while keeping public vocabulary held. P101 is downstream
of this work and P104/P105/P106; its minimum prelude is not frozen here.

## Implementation decisions

Every row records four alternatives considered during implementation. The agent
selected its recommendation under the user's delegation; there are no overrides
of the original CP-102 selections.

| Decision | Four alternatives explored | Recommended and selected |
| --- | --- | --- |
| CL-I01 | A host maps as language collections; B nominal finite families with explicit checked descriptors; C one dynamic container; D no keyed values. | **B**, recommended and selected. retain C042 and keep records distinct. |
| CL-I02 | A arbitrary comparator fun; B exact compiler-owned order evidence for C035 orderable scalar kinds; C sample a comparator and call it lawful; D sort by raw host term order. | **B**, recommended and selected. refuse unsupported/inconsistent evidence. |
| CL-I03 | A first duplicate wins; B last duplicate wins; C typed duplicate failure for strict construction; D silently combine. | **C**, recommended and selected. from CP-102-4. |
| CL-I04 | A sorted-key callback ordering during combining; B consume duplicate-combining callbacks in input order, then sort final keys; C random order; D parallel callbacks. | **B**, recommended and selected. preserve deterministic trap/callback order. |
| CL-I05 | A destructive update; B immutable explicit replacement; C implicit replacement during strict construction; D invalidate original values. | **B**, recommended and selected.  |
| CL-I06 | A accept raw host functions as pure; B verified compiled pure callback descriptors at the explicit operation boundary; C infer purity from arity; D disable callbacks. | **B**, recommended and selected. reuse C094/P096 checking. |
| CL-I07 | A claim constant-time all operations; B publish bounds separately for conversion, construction, lookup, update and callback work; C expose representation; D omit costs. | **B**, recommended and selected.  |
| CL-I08 | A implicit lazy language evaluation; B eager finite families plus explicit owned pull sessions; C consume every stream eagerly; D defer all streams. | **B**, recommended and selected. retain D059. |
| CL-I09 | A GC-only stream cleanup; B C080 scope cleanup and explicit idempotent close; C borrowed handles outlive owner; D finalizers run arbitrary language effects. | **B**, recommended and selected.  |
| CL-I10 | A stream grants ambient host access; B exact typed pull/release declarations and current foreign authority; C infer release from function names; D arbitrary path or MFA execution. | **B**, recommended and selected.  |
| CL-I11 | A traversal catches traps as expected failure; B separate success/failure/accumulation contracts with explicit adapters; C one universal exception type; D retry failed callbacks. | **B**, recommended and selected. retain C103/C081 boundaries. |
| CL-I12 | A source signatures only; B ordinary nominal package and executable host/runtime bridge with independent models; C native helpers alone prove language delivery; D introduce public API names now. | **B**, recommended and selected.  |
| CL-I13: Law certificates | A: certify any pure callback; B: closed exact Int sum/min/max derivations; C: sampling proves universal laws; D: Float addition is associative. | **B**, recommended and selected. Separates ordered arbitrary combining from genuinely algebraic evidence; no identity is claimed for min/max. |
| CL-I14: Set mapping | A: claim unconstrained Mapper; B: explicit checked transform with strict collision outcome; C: drop collisions; D: preserve duplicate elements as a set. | **B**, recommended and selected. Mapping can identify distinct elements, so the weakest lawful family excludes an unconditional Mapper instance. |
| CL-I15: Typed callback boundary | A: accept every nominal/native payload; B: retain closed-data foreign callback codecs and distinguish ordinary generic dictionaries; C: infer schemas from values; D: erase type checks. | **B**, recommended and selected. Does not silently widen C094/P096 while ordinary compiler-established methods remain polymorphic. |
| CL-I16: Outcome adaptation | A: implicit nominal coercion; B: named structural success/failure wire adapter to C103; C: raw exception tuples are expected failures; D: one mode chosen from input values. | **B**, recommended and selected. Each mode has fixed callback order, error schema and empty-result behavior. |
| CL-I17: State after timeout | A: accept late state; B: close admission, cancel and release last accepted state; C: replay pull; D: claim rollback. | **B**, recommended and selected. Source declarations must support releasing from that state; trusted foreign effects may already have happened. |
| CL-I18: Bounded collection cap | A: pull an extra element to detect end; B: stop exactly at the cap and close; C: silently ignore cap; D: defer cleanup until GC. | **B**, recommended and selected. No source work occurs solely to discover a suffix that the consumer will not use. |
| CL-I19: Release confirmation | A: close a process and assume reclamation; B: typed release completion plus nested scope cleanup, bounded and cached; C: retry every failure; D: allow borrowed cross-owner cleanup. | **B**, recommended and selected. A missing confirmation remains mandatory cleanup failure; release attempts do not repeat. |
| CL-I20: Pull evidence storage | A: claim constant memory; B: publish P096 call/event retention proportional to bounded pulls; C: drop all evidence invisibly; D: allow unlimited retained calls. | **B**, recommended and selected. Keeps cost claims faithful to the actual session implementation. |
| CL-I21: Versioning | A: new source grammar; B: exact semantic 0.1.65 contract over retained ordinary package and callback formats; C: relabel C042; D: silently change frozen 0.1.4 standard package. | **B**, recommended and selected. The collection package is separate and exact; historical formats remain unchanged. |
| CL-I22: Missing replacement | A: upsert; B: optional absence for a missing selected key; C: trap; D: erase the original. | **B**, recommended and selected. Matches the reviewed selected-key replacement and C042 typed-miss rule. |
| CL-I23: Budget classification | A: relabel exhaustion as malformed collection; B: preserve conversion/limit errors through builders and bound outcome wrappers; C: silently truncate; D: validate elements only. | **B**, recommended and selected. Whole results, not just payloads, consume explicit carrier budgets. |
| CL-I24: Early-stop evidence | A: constant callback result alone; B: skipped later trap and traced source demand; C: callback count inferred from output; D: unrestricted effectful probe accepted as pure. | **B**, recommended and selected. Independent negative witnesses establish stop behavior without admitting impure language callbacks. |

## Implementation and research basis

`Standard.Collections` supplies explicit finite descriptors, ordinary nominal
carriers, typed strict builders, optional lookup/replacement, maps, folds,
early-stop folds, ordered combining and outcome traversal. `Order` admits only
C035's five scalar orderable kinds. It does not confuse the broader comparable
set with lawful key ordering; Float bit identity preserves signed zeros.
`Combining` separates closed Int algebraic derivations from an arbitrary checked
pure ordered combining callback. Repeated keys are processed before final sorting.

`Callback` reuses C094 verified compiled pure closures and C095 complete codecs.
A focused variant test exposed the need to encode semantic callback results back
to native structural carriers; this was corrected before final validation.
Raw host functions used in independent model tests are harness observations,
not an admission route for effectful language callbacks. An actual compiled
unhandled-effect callback is rejected by the descriptor constructor.

The separate embedded `catena-collections-0.1.65.json` package contains five
ordinary nominal roles and six ordinary functions. Keyed/Unique construction is
abstract; ordered views remain available. Sequence and partially applied Keyed
have coherent Mapper/Reducible instances and four specialization templates.
`Collections.compile` uses the retained ordinary frontend and verifier; compiled
specialized BEAM dictionaries execute identity/composition/fold witnesses.
This is a semantic/package addition, not a new standalone executable artifact,
source spelling or change to the frozen canonical C004 package.

`Iterator` owns its P096 scope in a monitored worker so release can use the
latest accepted state even after the user's owner dies. Private release authority
is distinct from the public handle. Next is demand-driven. End, explicit close,
early collection caps, body abandonment and owner death release once. The final
private acknowledgement follows nested foreign-scope cleanup. Late request
replies use aliases, which are disabled after the caller's wait expires.

The source state contract requires release to remain valid after interrupted
work. Cooperative cancellation cannot undo host effects or reconstruct an
unobserved returned state. This is explicitly retained from P096, not hidden
behind a stronger stream guarantee. Tests use a registered host fixture only as
trusted observation machinery; P106 environmental APIs are not introduced.

Costs are published per operation, including complete conversion preflight,
scalar-key cost, arbitrary callback work, nominal depth and retained pull
history. Tail-recursive structural loops do not imply constant-space carrier
validation or constant-memory foreign sessions. This follows the
[collection synthesis](../20-notes/catena-collection-operations.md) and C042's
separation of category-theory laws from implementation costs.

## Executed witnesses

`test/catena/collection_protocol_test.exs` exercises compiled ordinary package
construction/views, independently verified core, exact package rejection,
strict first-duplicate ordering, immutable replacement, missing-key absence,
signed-zero set identity, forged/unsupported ordering, verified pure maps,
input-order combining traps, 50,000-element list equations, structural-variant
callbacks, independent errors in input order, specialized list/keyed dictionaries,
closed Int associativity, actual effectful callback refusal, a dependent failure
that skips a later trap, independent traversal that preserves that trap,
set-collision failure and complete-output exhaustion.

`test/catena/collection_iterator_test.exs` records real pull/release traces for
no-eager-pull startup, cached end, explicit double close, expired/cross-owner
handles, missing grants, bounded collection truncation, unused abandonment,
owner death, step exhaustion, timed-out cooperative pull, release failure and a
compiled pure consumer that stops before another pull.

Initial full-suite failures were exact current-revision discovery assertions
still expecting 0.1.64. Their expectations were advanced to 0.1.65 while the
historical debug/artifact/source format selections stayed fixed. Initial tuple
fixture non-exhaustiveness was fixed by an explicit fallback; it was not a
collection-runtime defect. Builder review also preserved limit classifications
instead of collapsing them into generic invalid-input errors.

## Verification

The final focused collection/iterator/lifecycle run passed 35 tests. Complete
regression, production compilation, escript and archive results are recorded
below after the final checks. The reproducible compiler commands are `mix test`,
`MIX_ENV=prod mix compile --warnings-as-errors` and `MIX_ENV=prod mix escript.build`.
Research validation uses `python3 validate_archive.py` and `git diff --check`.

Final validation passed **917 compiler tests**, production warnings-as-errors
compilation and production escript packaging. Archive validation passed with
634 documents, 77 directories, 121 source notes, 191 specification chapters and
862 obligations (767 traced, 74 partial, 21 untraced). Both diffs passed
`git diff --check`. The checklist now totals 103 complete, 24 partial,
12 gaps and two deferred items.

Compiler implementation commit: `4aa49bae35750f3705bc2dc734e45ebd7407f0a4`.

Compiler [PR 147](https://github.com/pcharbon70/catena/pull/147) merged as
`14cbf00a1c515259abdab57790efe5dfc7968295`. Compiler `rewrite` was synchronized
before deleting the local and remote feature branches.
