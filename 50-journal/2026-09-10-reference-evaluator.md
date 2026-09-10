---
title: "2026-09-10 Reference Evaluator"
kind: journal
created: "2026-09-10"
tags: [specification, formal-semantics, conformance, testing]
aliases: []
---

# 2026-09-10 Reference Evaluator

## Scope

Execute [P133](../20-notes/language-completion-plan-delivery.md#item-133-reference-evaluator)
before P134 and G122. Revision `0.1.83` is covered by the user's session-wide
approval. CP-133-1..3 retain their recommended selections. Public-source
adoption remains held for P109 and finite model agreement remains separate from
C132's outstanding composition proof.

## Implementation decisions

| Decision | Four alternatives | Recommended and selected |
| --- | --- | --- |
| RE-I01 Integration | A production backend as oracle; B adapters over independent models; C rewrite one evaluator; D disconnected tests | B: common observations preserve structural independence. |
| RE-I02 Shape | A result-specific tuples; B fixed record with status/value/reason/events/lifetime/bounds; C strings; D internal machine state | B: cross-engine comparison is explicit without freezing representation. |
| RE-I03 Terminals | A Boolean success; B nine distinct statuses; C timeout equals divergence; D every stop is trap | B: promised semantic distinctions survive normalization. |
| RE-I04 Pure bound | A wall clock; B semantic evaluation fuel; C unbounded; D recursion depth only | B: exhaustion is deterministic and replayable. |
| RE-I05 Effect bound | A call production handlers; B retain effect reference trace plus separate host deadline; C omit effects; D deadline means divergence | B: ordering evidence remains independent and deadline meaning stays honest. |
| RE-I06 Kernel output | A final value only; B value/reason, trace, lifetime, and steps; C raw state equality; D process count | B: the observation relation includes promised actor behavior. |
| RE-I07 Schedules | A one scheduler run; B bounded distinct outcome set; C require one ordering; D random retry | B: nondeterminism is represented as allowed observations. |
| RE-I08 Resource model | A production callbacks; B lifecycle transition explorer; C final resource count; D ignore cleanup errors | B: ownership and cleanup order remain explicit and deterministic. |
| RE-I09 Foreign values | A raw terms; B checked C095 codec; C production callback; D serialized bytes only | B: boundary shape and finite limits are re-derived. |
| RE-I10 External effects | A real network/time; B finite response catalog; C fixed success; D skip missing operations | B: values, traps, exits, deadlines, and unsupported requests replay exactly. |
| RE-I11 Source | A invent public grammar; B retained kernel adapter and explicit P109 hold; C no source entry; D host Elixir syntax | B: useful elaboration evidence respects the vocabulary hold. |
| RE-I12 Unknown model | A skip; B explicit unsupported; C assume success; D crash | B: coverage gaps remain machine-visible. |
| RE-I13 Malformed core | A harness crash; B rejected observation; C undefined behavior; D coerce | B: forged model inputs cannot produce silent evidence. |
| RE-I14 Limits | A unlimited; B published per-engine ceilings in every observation; C one global timeout; D omit partial results | B: each exhaustion retains its precise scope. |
| RE-I15 Proof claim | A tests prove soundness; B agreement is bounded evidence; C model existence proves semantics; D no evidence language | B: C132's composition lemma stays open until checked separately. |

## Results

Compiler [PR 166](https://github.com/pcharbon70/catena/pull/166) merged feature
commit `afa80f47c0866cf63864ac686409f73582faa1fc` as
`d5b697ec1591c30b2e3911d7bdefe9fc5afb1a6a` into `rewrite`. The new
`Catena.Reference.Observation` adapter covers pure, effect, kernel, schedule,
resource, foreign, external-response, and retained-source engines. Its fixtures
exercise handled-effect order, actor lifetime, bounded schedule sets, cleanup,
checked foreign carriers, abstract external outcomes, forged core, fuel
exhaustion, and the public-source hold.

The complete suite passes 1,089 tests. Production compilation with warnings as
errors, production escript construction, trust inventory audit, and diff checks
pass. The [normative contract](../60-specification/reference-evaluator/common-observations-and-bounded-models.md)
promotes P133 to C133 without claiming mechanized proof or selecting public
syntax.
