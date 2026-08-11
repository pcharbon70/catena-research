---
title: "How Should Catena Achieve Exhaustive Rule-to-Test Traceability?"
kind: inquiry
created: "2026-08-10"
status: open
tags:
  - conformance
  - specification
  - testing
aliases:
  - "P011 traceability inquiry"
---

# How Should Catena Achieve Exhaustive Rule-to-Test Traceability?

## Why this matters

[Specification Authority](../SPECIFICATION-AUTHORITY.md) gives checklist item
P010/P011 two owned outcomes: exhaustive rule-to-test traceability and any later
stable rule-identifier scheme. Today neither exists. The 0.1.1 through 0.1.8
normative corpus spans fifty-six chapters and roughly 244 `MUST`/`MUST NOT`
clauses, and the bootstrap compiler's conformance suite (~145 tests, 35 stable
diagnostic identifiers) cites no normative heading at all. A rule with no
evidence is a latent conformance gap; a test with no governing rule is evidence
without authority. Under the
[Conformance Vocabulary](../CONFORMANCE-VOCABULARY.md) and its rejection of
undefined behavior, either state is a specification defect waiting to be
exercised.

This inquiry generalizes the heading-anchor citation that
[Specification Authority](../SPECIFICATION-AUTHORITY.md) already requires for
conflict reports into a durable, machine-checkable link between every hard
requirement and the executable evidence that exercises it.

## Operational question

What is the smallest stable scheme that gives every `MUST`/`MUST NOT`
obligation a permanent identifier, links it to a normative heading anchor and to
executable evidence, and is enforceable by the archive validator and a compiler
coverage check—without making tests normative, churning normative prose, or
requiring a new language revision?

## Working hypotheses

- **Obligation-level identifiers** recorded in a non-normative registry balance
  precision against invasiveness: one identifier per enumerated *Required
  positive/negative case* in each area's `diagnostics-and-conformance.md`
  chapter, plus one per standalone `MUST` clause not already captured.
- **`MUST`/`MUST NOT` first** is sufficient to claim C011. `SHOULD`, `MAY`,
  declarative rules, and normative definitions can follow as a separately
  tracked item.
- The existing **35 stable diagnostic identifiers** are the natural "expected
  diagnostic" bridge, so evidence entries can name both a test and a diagnostic.
- A **clause-conditions 0.1.3 pilot** validates the scheme on the smallest,
  most conformance-rich area before it is applied to the other seven.
- Tagging ExUnit tests with `@tag obligation: "AREA-OBL-NNN"` plus a coverage
  check that scans those tags is sufficient machine evidence, and keeps the
  compiler repo non-normative.

## Paths to explore

- Registry placement: a non-normative map (preferred) versus identifiers
  embedded in the normative `diagnostics-and-conformance.md` lists, which would
  be a per-area normative edit.
- Coverage-check form: a Mix task versus a focused test that asserts every
  registry obligation has at least one tagged test.
- Validator enforcement ramp: warn, then fail, so the registry can be populated
  incrementally without blocking unrelated archive work.
- Cross-repo evidence-link durability: pin evidence URLs to an immutable commit
  versus a branch path.

## Findings

The accepted plan is recorded on the
[Conformance Traceability map](../10-maps/conformance-traceability.md):
obligation-level identifiers, `MUST`/`MUST NOT` first, clause-conditions 0.1.3
as pilot, coordinated research/compiler PRs per area mirroring the C010
`catena-research#24` ↔ `catena#74` pattern.

All eight normative areas are now extracted on the map and merged on the
compiler side with a per-area coverage gate. The clause-conditions pilot
(`CC-OBL-001`..`049`) validated the scheme; three pilot gaps were filled
(CC-OBL-016, 034, 040) and seven architectural or not-yet-filled gaps are
allow-listed. The other six areas — type-system (`TS`), data-and-patterns
(`DP`), traits (`TR`), effects (`EF`), governance (`SG`), editions (`ED`), and
the formal semantic kernel (`FK`) — are compiler-tagged and gated. The
data-and-patterns area (`DP-OBL-001`..`071`, the largest) filled eight gaps in
follow-ups (DP-OBL-017, 021, 024, 025, 035, 042, 043, 048); the seven remaining
allow-listed entries are all architectural, future-version, or P117
diagnostic-quality boundaries. The archive
validator guards registry integrity (well-formed, unique identifiers, and a
status per row) and reports the obligation counts.

## Outcome

Open. The inquiry resolves to C011 when all eight normative areas' `MUST`/
`MUST NOT` obligations carry a permanent identifier, a resolved normative
anchor, and at least one tagged passing test; when
`validate_archive.py` enforces the registry; and when the compiler coverage
check is green. `SHOULD`, `MAY`, declarative rules, and normative definitions
then become a new checklist item rather than part of C011.
