---
title: "2026-09-10 Build System and Package Manager"
kind: journal
created: "2026-09-10"
tags: [specification, packages, tooling, reproducibility]
aliases: []
---

# 2026-09-10 Build System and Package Manager

## Scope

Execute [P121](../20-notes/language-completion-plan-delivery.md#item-121-build-system-and-package-manager)
after C116. Revision `0.1.81` is covered by the user's session-wide approval.
CP-121-1..4 retain their recommended selections and public vocabulary remains
deferred to P109.

## Implementation decisions

| Decision | Four alternatives | Recommended and selected |
| --- | --- | --- |
| BS-I01 Discovery | A ambient upward search; B explicit, then root, then unique nested; C first filesystem result; D environment variable | B: deterministic precedence exposes ambiguity. |
| BS-I02 Profiles | A arbitrary maps; B closed named profiles bound into identity; C one profile; D host build modes | B: the plan records a stable supported choice. |
| BS-I03 Graph | A shell order; B validated DAG; C alphabetical packages; D recursive implicit discovery | B: dependency order and cycle refusal are explicit. |
| BS-I04 Diamond | A rebuild shared nodes; B one node per plan; C duplicate versions silently; D last writer wins | B: one identity has one result in a plan. |
| BS-I05 Acquisition | A fetch during compile; B verified phase before build; C path cache trust; D no ecosystem | B: network authority ends before execution. |
| BS-I06 Partial download | A expose prefix; B transaction rollback; C retry forever; D mark complete | B: interruption cannot poison the cache. |
| BS-I07 Cache key | A timestamps; B inputs/toolchain/profile/capabilities/dependencies/generators; C package name; D disabled | B: all meaning-bearing inputs invalidate results. |
| BS-I08 Transitive key | A dependency name only; B recursive dependency cache key; C version only; D rebuild all | B: a leaf change invalidates its dependents precisely. |
| BS-I09 Generator authority | A shell; B declared relative inputs and output; C prohibit; D trust generated files | B: generation stays finite and attributable. |
| BS-I10 Cache admission | A key presence; B canonical archive plus expected input digest; C timestamp; D filename | B: substitution across package keys is refused. |
| BS-I11 Execution | A online callbacks; B offline retained compiler; C host build system; D resolver only | B: the complete existing compilation path is exercised. |
| BS-I12 Publication | A overwrite in place; B verified stage and atomic rename; C copy then inspect; D leave temporary | B: a failed replacement preserves prior output. |

## Results

Compiler [PR 163](https://github.com/pcharbon70/catena/pull/163) merged feature
commit `b7c10f2` as `d29cdfbdc8ada13adcce756cbf402806bbea715b`
into `rewrite`. The complete suite passes 1,077 tests. Production compilation
with warnings as errors, production escript construction, trust inventory audit,
and diff checks pass.

The [normative contract](../60-specification/build-system/project-graphs-acquisition-and-offline-builds.md)
promotes P121 to C121. Its retained-input build path composes existing package
and governance contracts without adopting project-file or source-language
vocabulary.
