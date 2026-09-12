---
title: "2026-09-12 Usability Gate"
kind: journal
created: "2026-09-12"
tags: [specification, usability, tooling]
aliases: []
---

# 2026-09-12 Usability Gate

## Scope

Execute G137's preparation at `0.1.97` without contacting participants or
choosing P107 vocabulary and P109 grammar. CP-137-1..3 select an observed human
task study, materials before separately authorized outreach, and a six-person
pilot followed by preregistration and a 24-person main study. This slice makes
the package executable and records its blocked evidence state.

## Implementation decisions

| Decision | Four alternatives | Recommended and selected |
| --- | --- | --- |
| UG-I01 Evidence | A agent assessment; B observed programmer behavior; C preference poll; D expert review alone | B: prediction, completion, transfer, and repair require actual human observations. |
| UG-I02 Work now | A recruit immediately; B prepare materials and require separate outreach authorization; C invent results; D defer all preparation | B: authorized implementation can finish without implying contact authority. |
| UG-I03 Study sequence | A main study only; B pilot then preregister main; C repeated informal pilots; D thresholds after results | B: calibration precedes a frozen confirmatory plan. |
| UG-I04 Pilot size | A 2; B 6; C 12; D 24 | B: six permits three people per stratum while keeping calibration distinct from confirmation. |
| UG-I05 Main size | A 6; B 12; C 24; D 100 | C: 24 supports 12 participants per stratum and balanced condition orders within the planned scope. |
| UG-I06 Strata | A one mixed pool; B general and functional programmers; C category theorists only; D compiler authors only | B: the intended audience and transfer from functional experience remain separately visible. |
| UG-I07 Conditions | A approved public language only; B semantic foundation and future public language; C category notation versus prose; D host languages | B: matched semantics can isolate the approved language presentation after P107/P109. |
| UG-I08 Counterbalancing | A one fixed order; B alternate order within phase and stratum; C random without a seed; D participant choice | B: the order difference is bounded and reproducible. |
| UG-I09 Task scope | A mapping only; B eight required semantic families; C arbitrary coding exercise; D syntax trivia | B: the checklist's behaviors and diagnostics receive explicit coverage. |
| UG-I10 Prediction | A ask after execution; B record unaided prediction first; C omit prediction; D infer it from code | B: prediction directly measures the stated gate. |
| UG-I11 Transfer | A repeat identical values; B structurally different matched example; C ask for a definition; D self-rated confidence | B: transfer distinguishes a learned rule from memorized output. |
| UG-I12 Repair | A free-form debugging; B supplied structured diagnostic and bounded repair choice; C no failures; D facilitator fixes it | B: repair measures whether the diagnostic supports safe action. |
| UG-I13 Outcome codes | A prose notes; B five fixed task outcomes; C pass/fail only; D numerical impression | B: fixed codes retain failure and protocol errors without collecting personal text. |
| UG-I14 Timing | A exact timestamps; B four coarse duration bands; C no timing; D keystroke logs | B: coarse bands support task calibration with less identifying data. |
| UG-I15 Data | A recordings; B five minimized fields; C names and answers; D unrestricted notes | B: aggregates remain reproducible without personal content. |
| UG-I16 Consent | A implied by attendance; B explicit voluntary consent with skip and withdrawal; C employer approval; D repository access | B: participation and continued use of observations remain voluntary. |
| UG-I17 Raw retention | A permanent sheets; B delete after two-person aggregate verification; C upload recordings; D delete before verification | B: the aggregate is checked while raw exposure remains temporary. |
| UG-I18 Exclusions | A decide after results; B three predefined reasons; C remove outliers; D no exclusions even after withdrawal | B: consent and protocol failures are handled without outcome-driven filtering. |
| UG-I19 Thresholds | A choose now without pilot; B calibrate in pilot and preregister before main; C choose after main; D universal perfection | B: the main test has fixed criteria informed by actual material difficulty. |
| UG-I20 Material identity | A filenames; B SHA-256 map plus canonical package digest; C modification time; D git branch name | B: the exact materials behind any future aggregate are recoverable. |
| UG-I21 Evidence state | A call preparation a pass; B publish blocked until observed study; C omit status; D simulate participants | B: tool readiness and usability evidence remain distinct. |
| UG-I22 Revision and trust | A unversioned test files; B 0.1.97 lifecycle entry in `tools-profile`; C rewrite 0.1.90; D defer all registration | B: the new normative gate is cumulative, inspectable, and does not alter earlier revision meaning. |

Every recommendation was selected under the user's delegated decision
authority. No recommendation was overridden.

## Executed evidence

Compiler [PR 193](https://github.com/pcharbon70/catena/pull/193) merged feature
commit `c188b9e` as merge commit `784497f` into `rewrite`. Seven focused cases
exercise the blocked evidence result, canonical package digest, exact material
hashes, fabricated-result and participant-data refusal, outreach and public-hold
enforcement, balanced phase/stratum assignments, invalid assignments, and the
published conformance boundary.

Compiler [PR 194](https://github.com/pcharbon70/catena/pull/194) merged feature
commit `17de08a` as merge commit `eda990d`. It introduces the usability study at
`0.1.97`, preserves G123 at `0.1.96`, appends the cumulative frontend revision,
and moves the unknown-future sentinel to `0.1.98`.

The complete 1,188-test suite, production compilation with warnings as errors,
escript construction, reviewed trust-inventory verification, and
`git diff --check` pass. The study package contains consent and data handling,
facilitator instructions, a vocabulary-neutral semantic task book, analysis
plan, and machine-readable manifest. No participant was contacted and no human
result was recorded.

The [normative contract](../60-specification/usability-gate/observed-prediction-transfer-and-repair.md)
makes the preparation and eventual evidence criteria durable. G137 stays
partial until P107/P109 are approved, outreach is separately authorized, the
pilot is observed, thresholds are preregistered, and the main study supplies a
passing reproducible aggregate.
