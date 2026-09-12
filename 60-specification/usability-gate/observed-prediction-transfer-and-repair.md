---
title: "Observed Prediction, Transfer, and Repair"
kind: specification
created: "2026-09-12"
status: normative
spec_version: "0.1.97"
tags: [specification, usability, tooling]
aliases: []
---

# Observed Prediction, Transfer, and Repair

## Status and authority

G137 defines its usability-study preparation and evidence gate at revision
`0.1.97` under [authority](../../SPECIFICATION-AUTHORITY.md),
[conformance vocabulary](../../CONFORMANCE-VOCABULARY.md), and
[implementation limits](../../IMPLEMENTATION-LIMITS.md). It executes the
[G137 plan](../../20-notes/language-completion-plan-delivery.md#item-137-usability-gate)
without selecting Catena's public vocabulary or grammar. Prepared materials,
agent simulations, expert opinion, and imagined scores do not satisfy the gate.
Observed public-language evidence remains held for P107 and P109, so G137
remains partial (`UG-OBL-001`).

## Evidence authority and consent

A passing usability claim MUST derive from observed task performance by real
programmers. It MUST NOT derive from an agent self-assessment, preference poll,
mathematical expert review alone, fabricated participant record, or prepared
study package (`UG-OBL-002`).

Recruitment and participant contact MUST require separate explicit
authorization and an approved channel. Preparation of materials MUST NOT count
as outreach authority. A session MUST begin only after voluntary informed
consent, MUST permit task skipping and withdrawal without explanation, and MUST
discard a withdrawing participant's observations (`UG-OBL-003`).

The study MUST collect only condition, duration band, outcome code, programmer
stratum, and task identity. It MUST NOT place names, contact details, free text,
source recordings, exact timestamps, IP addresses, or employer in the study
package. Recruitment records MUST remain separate. Raw coded sheets MUST be
deleted after two-person aggregate verification (`UG-OBL-004`).

## Cohorts and counterbalancing

The study MUST use a six-person pilot followed by a separately preregistered
24-person main cohort. Each phase MUST split participants evenly between
general and functional programmers. Pilot observations MUST NOT count toward
the main result (`UG-OBL-005`).

Within each phase and stratum, assignments MUST alternate between the semantic
foundation first and public language first. The count difference between the
two orders MUST be no greater than one. A public-language condition MUST NOT
execute while P107 or P109 remains held (`UG-OBL-006`).

The facilitator MUST give the same orientation and practice item, present tasks
in assigned order, record predefined codes, and answer procedural questions
only. Supplying a semantic rule or confirming an intermediate answer MUST be
classified as facilitator protocol failure (`UG-OBL-007`).

## Tasks and outcomes

The semantic foundation MUST cover single-context mapping, independent
combination, dependent sequencing, finite traversal, effect handling, guard
selection, comprehension behavior, and diagnostic repair. The future
public-language condition MUST preserve those semantic keys and vary only the
approved notation and diagnostic presentation (`UG-OBL-008`).

Each family MUST observe an unaided prediction before execution, task
completion, transfer to a structurally different example, and repair of a
supplied error where applicable. The four aggregate metrics MUST be prediction
accuracy, task completion, transfer success, and repair success
(`UG-OBL-009`).

Each task MUST record exactly one of correct unaided, correct after procedural
restate, incorrect, abandoned, or protocol failure. Duration MUST use only
under two minutes, two through five minutes, over five minutes, or not
completed. Duration MUST remain descriptive and MUST NOT substitute for a
correctness outcome (`UG-OBL-010`).

## Preregistration and analysis

The pilot MUST calibrate ambiguity, duration, rubric agreement, and metric
scorability. Numerical thresholds for all four metrics MUST be fixed and
preregistered after the pilot and before the first main-study observation.
Thresholds MUST NOT be selected or changed after inspecting main outcomes
(`UG-OBL-011`).

The retained analysis MUST report participant and task counts, order, stratum,
outcome proportions, paired within-participant differences when both conditions
exist, and uncertainty appropriate to the sample. It MUST report strata both
separately and together, retain incorrect and abandoned outcomes, and preserve
unsuccessful tasks (`UG-OBL-012`).

Only withdrawn consent, duplicate participation, and facilitator protocol
failure can exclude observations. Each exclusion MUST identify its predefined
reason and phase. An outlier, failed task, or inconvenient result MUST NOT be
removed after outcome inspection (`UG-OBL-013`).

## Package identity and gate result

The pre-study package MUST use a canonical machine-readable manifest with no
participant data or results. It MUST bind every material by exact SHA-256,
publish its task families, phases, strata, outcomes, data policy, exclusions,
threshold status, and P107/P109 holds, and produce a canonical package digest
(`UG-OBL-014`).

The preparatory conformance profile MUST publish revision, package format and
version, prepared status, blocked evidence status, outreach boundary,
participant-data prohibition, public holds, phases, strata, task families,
metrics, material identity, and threshold policy. G139 MUST continue to treat
usability evidence as blocked while G137 lacks a passing observed aggregate
(`UG-OBL-015`).

An implementation claiming this revision MUST exercise package validation,
material-digest verification, rejection of participant data and fabricated
results, rejection of unauthorized outreach and selected public conditions,
balanced pilot and main assignments, invalid assignment refusal, lifecycle
selection, production compilation, trust-inventory verification, and its
complete regression suite (`UG-OBL-016`).

## Limits and variability

This protocol has zero variability dispositions. An implementation MUST NOT
change cohort sizes, strata, task families, metric set, exclusion reasons,
condition-order bound, or data fields and describe the result as this contract.
Resource exhaustion or unavailable participants leave the gate blocked; they
do not lower its criteria (`UG-OBL-017`).

## Rationale and evidence (non-normative)

The [implementation journal](../../50-journal/2026-09-12-usability-gate.md)
records twenty-two four-way implementation decisions and compiler PRs
[193](https://github.com/pcharbon70/catena/pull/193) and
[194](https://github.com/pcharbon70/catena/pull/194). The executable package
makes study preparation reproducible and resistant to fabricated evidence while
preserving the decisive distinction: G137 can close only after an authorized,
preregistered human study using the approved future public language.
