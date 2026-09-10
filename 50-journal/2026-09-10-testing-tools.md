---
title: "2026-09-10 Testing Tools"
kind: journal
created: "2026-09-10"
tags: [specification, testing, conformance, tooling]
aliases: []
---

# 2026-09-10 Testing Tools

## Scope

Execute [G122](../20-notes/language-completion-plan-delivery.md#item-122-testing-tools)
at revision `0.1.84`. CP-122-1..3 retain their recommended selections. Because
P134 names G122 as a dependency while the G122 plan names P134, this slice
establishes the reusable runner and evidence contract first; P134 can now use
it for systematic differential generation. Public test notation remains held
for P109/P107.

## Implementation decisions

| Decision | Four alternatives | Recommended and selected |
| --- | --- | --- |
| TT-I01 Result taxonomy | A Boolean; B six explicit kinds; C proof/failure only; D external-tool strings | B: unit, law, property, model, concurrency, and specification preserve evidence scope. |
| TT-I02 Suite identity | A callback hash; B canonical portable plan plus local callbacks; C filename; D timestamp | B: stable inputs bind replay without pretending functions are portable. |
| TT-I03 Subject binding | A path; B exact digest checked before execution; C latest checkout; D optional label | B: stale evidence is rejected deterministically. |
| TT-I04 Empty suites | A pass; B explicit refusal; C warning; D omit report | B: absence of observations cannot become success evidence. |
| TT-I05 Seeds | A global RNG; B explicit suite seed with deterministic derived seeds; C clock; D fixed zero | B: unchanged runs reproduce while cases remain independent. |
| TT-I06 Generator domain | A accept all values; B validate every generated value; C validate only failures; D byte fuzzing | B: generator defects remain distinct from property counterexamples. |
| TT-I07 Shrink order | A parallel race; B stable first failing candidate; C random; D smallest host term | B: deterministic replay has a defined search path. |
| TT-I08 Shrink invariant | A coerce candidates; B discard candidates failing the domain predicate; C allow invalid minima; D disable shrinking | B: reported counterexamples retain their admitted type/domain. |
| TT-I09 Shrink limit | A claim current value minimal; B preserve best value and report nonminimal exhaustion; C loop forever; D drop failure | B: finite resources do not strengthen evidence. |
| TT-I10 Case isolation | A shared process; B per-case Task.Supervisor; C OS process per assertion; D no cleanup | B: runner-owned tasks have a clear lifetime with modest host cost. |
| TT-I11 Child API | A raw spawn; B runner-owned spawn callback; C forbid concurrency; D inspect all VM processes | B: the runner can guarantee cleanup for work it owns. |
| TT-I12 Effect accounting | A infer host calls; B explicit ordered context events checked against declarations; C ignore effects; D sandbox claim | B: evidence records intended observations without claiming complete host mediation. |
| TT-I13 Evidence form | A arbitrary terms; B finite canonical values; C printed inspect text; D opaque files | B: reports remain comparable, digestible, and free of live host identities. |
| TT-I14 Governed evidence | A trust case name; B require exact subject digest in specification evidence; C current revision only; D signature implies freshness | B: governed claims cannot drift from the tested subject. |
| TT-I15 Bound taxonomy | A one timeout; B semantic fuel, schedule, shrink, and host time separately; C retries; D unbounded | B: tool exhaustion cannot be mistaken for language behavior. |
| TT-I16 Aggregate status | A last result; B fail, host-timeout, exhausted, pass precedence; C Boolean all; D first completion | B: the report keeps the strongest observed inability while retaining every case. |
| TT-I17 Proof wording | A passing tests prove correctness; B finite-observation-not-proof; C omit scope; D proof by reference agreement | B: bounded evidence does not discharge C132's composition lemma. |
| TT-I18 Vocabulary | A invent syntax now; B internal API pending P109/P107; C borrow ExUnit syntax; D permanently external | B: tooling executes without pre-empting the language-wide grammar decision. |

## Results

Compiler [PR 167](https://github.com/pcharbon70/catena/pull/167) merged feature
commit `50c3e91` as merge commit `abbbd0cd2632c008f872159cd26bb57a1f5fc8f3`
into `rewrite`. `Catena.Tool.TestRunner` binds canonical plans to exact subjects,
executes all six result kinds with explicit seeds, shrinks failing generated
values inside their declared domain, accounts for declared effects, cleans
runner-owned children, and separates semantic, schedule, shrink, and host-time
bounds.

The complete suite passes 1,097 tests. Production compilation with warnings as
errors, production escript construction, trust inventory audit, and diff checks
pass. The compiler repository does not define the optional `mix spec.diffcheck`
task. The [normative contract](../60-specification/testing-tools/isolated-seeded-and-scoped-runs.md)
promotes G122 to C122 without selecting public syntax or claiming proof.
