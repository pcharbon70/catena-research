---
title: "2026-09-10 Standard Stability and Performance"
kind: journal
created: "2026-09-10"
tags: [specification, standard-library, compatibility, performance]
aliases: []
---

# 2026-09-10 Standard Stability and Performance

## Scope

Execute [P108](../20-notes/language-completion-plan-delivery.md#item-108-stability-and-performance-policy)
at revision `0.1.87`. CP-108-1..3 retain their recommended selections: version
types, laws, and operational guarantees; publish asymptotic, callback, and
stack contracts beside measured envelopes; and expose only guarantees clients
need. Public vocabulary remains held for P109.

## Implementation decisions

| Decision | Four alternatives | Recommended and selected |
| --- | --- | --- |
| SP-I01 Contract unit | A package prose; B per operation; C per module; D per backend | B: replacement checks need operation precision. |
| SP-I02 Identity | A display name; B stable internal role plus package revision; C BEAM MFA; D source token | B: identity survives implementation changes without selecting vocabulary. |
| SP-I03 Inventory | A free-form docs; B canonical digest-bound catalog; C reflection; D benchmark names | B: completeness and tampering are machine checkable. |
| SP-I04 Fields | A complexity only; B laws/order/callbacks/failures/cost/stack/representation; C types only; D timing | B: compatibility covers every client-visible obligation. |
| SP-I05 Stability tiers | A uniform; B language/interface/package/empirical; C stable/unstable; D host-defined | B: evidence cannot silently become semantics. |
| SP-I06 Time classes | A nanoseconds; B asymptotic worst-case classes; C average only; D undocumented | B: portable client planning needs scale behavior. |
| SP-I07 Service costs | A constant; B implementation-bounded under declared limits; C linear; D omit | B: host latency is not portable complexity. |
| SP-I08 Space measure | A total result size; B auxiliary space with explicit result exclusion; C heap words; D RSS | B: the contract remains representation independent. |
| SP-I09 Stack | A recursive depth; B constant host-call stack for accepted collections; C unspecified; D VM default | B: it carries C004's large-input obligation across the library. |
| SP-I10 Callback model | A prose; B closed multiplicity categories plus order; C final value only; D benchmark count | B: duplication and elision are compatibility facts. |
| SP-I11 Early stop | A may continue; B no callbacks after explicit stop; C implementation choice; D cancel asynchronously | B: side effects and traps after stop stay unobservable. |
| SP-I12 Replacement rule | A implementation version; B field preservation with bound improvement allowed; C benchmark threshold; D source diff | B: compatible replacements preserve published client assumptions. |
| SP-I13 Stronger inputs | A compatible; B breaking; C warning; D host-defined | B: an old accepted call must stay accepted. |
| SP-I14 Representation | A freeze BEAM terms; B promise none unless versioned explicitly; C freeze module names; D expose layout | B: C028 already excludes a stable ABI. |
| SP-I15 Observation identity | A elapsed time; B contract plus full toolchain and samples; C host name; D timestamp | B: results are attributable and replayable. |
| SP-I16 Work units | A omit; B semantic work units beside elapsed time; C reductions only; D allocations only | B: G138 can distinguish algorithmic work from host noise. |
| SP-I17 Portability | A observed time is normative; B always false at P108; C fastest run; D CI average | B: measurement does not invent a language guarantee. |
| SP-I18 Evidence scope | A tests prove bounds; B mutation and edge evidence with disclaimer; C benchmarks only; D review only | B: finite evidence checks the policy without claiming proof. |

## Results

Compiler [PR 171](https://github.com/pcharbon70/catena/pull/171) merged feature
commit `7f35b70` as merge commit
`819f7e70f50c37e18517a19f3725cd109b1b7a76` into `rewrite`.
`Catena.Standard.Contract` implements a canonical catalog for twenty internal
standard roles, validates complete records, classifies compatible and breaking
replacements, and creates digest-bound empirical observations. Focused tests
cover catalog integrity, improvements, semantic and complexity regressions,
toolchain binding, tampering, lifecycle registration, and policy exclusions.
The complete compiler suite passes with 1,120 tests, including the reviewed
trust-boundary audit. The [normative contract](../60-specification/standard-stability-and-performance/versioned-operation-contracts.md)
makes P108 complete while reserving measured performance envelopes for G138.
