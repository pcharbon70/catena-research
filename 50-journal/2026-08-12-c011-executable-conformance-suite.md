---
title: "C011 Executable Conformance Suite"
kind: journal
created: "2026-08-12"
tags:
  - conformance
  - testing
  - traceability
  - specification
aliases:
  - "C011 promotion record"
  - "C011 executable conformance suite record"
---

# C011 Executable Conformance Suite

## Observations

The coordinated implementation and archive now establish C011: every
`MUST`/`MUST NOT` obligation across the eight normative areas carries a
permanent area-scoped identifier (`AREA-OBL-NNN`), a resolved normative anchor,
and — where the obligation has a focused executable unit — at least one tagged,
passing compiler test enforced by a per-area coverage gate.

The scheme was piloted on clause-conditions 0.1.3 and scaled to the other seven
areas as coordinated research/compiler PR pairs. The research side holds the
non-normative registry of identifiers, anchors, and evidence on the
[Conformance Traceability](../10-maps/conformance-traceability.md) map; the
compiler side tags each test with `@tag obligations: ~w(...)` and a
`<suite>_traceability_coverage_test.exs` gate fails until every obligation in
the area is either covered by a tagged test or explicitly allow-listed with a
reason. The archive validator guards registry integrity (well-formed and unique
identifiers, a status per row) and reports the obligation counts.

## Evidence

### Coordinated PRs

The eight areas landed on the sibling compiler's `rewrite` branch as one
tag-and-gate PR each, with focused gap-fill PRs behind the clause-conditions,
data-and-patterns, and type-system areas:

| Area | Gate PR | Gap-fill PRs |
| --- | --- | --- |
| `CC` clause-conditions (0.1.3) | #76 | #77 (CC-OBL-016, 034), #78 (040) |
| `FK` formal semantic kernel (0.1.8) | #79 | — |
| `EF` effects (0.1.5) | #80 | — |
| `TR` traits (0.1.4) | #81 | — |
| `ED` editions (0.1.7) | #82 | — |
| `SG` governance (0.1.6) | #83 | — |
| `TS` type-system (0.1.1) | #84 | — |
| `DP` data-and-patterns (0.1.2) | #85 | #86 (017, 021, 024, 025, 035, 042, 043), #87 (048) |

### Immutable compiler identity

The compiler identity capturing all eight gates and gap-fills is the
post-merge `rewrite` head:

| Field | Value |
| --- | --- |
| Repository | `pcharbon70/catena` |
| Commit | [`107035277d5ae8db144df8d7142b7e0e14e66562`](https://github.com/pcharbon70/catena/commit/107035277d5ae8db144df8d7142b7e0e14e66562) |
| Subject | `Merge pull request #87 from pcharbon70/agent/p011-dp-gapfill-048` |
| Tree | `4b3f37d8c4417c10656e1ea2d15b92c2f421edaa` |

The post-commit commands below ran with Erlang/OTP 29.0.4 (`erts-17.0.4`),
Elixir 1.20.2 compiled for OTP 29, and compiler 10.0.3.

```text
asdf current
asdf exec elixir --version
asdf exec mix format --check-formatted
asdf exec mix test
git diff --check
```

Warning-free compilation and formatting succeeded, the complete suite reported
**171 passing tests** (eight coverage gates plus the area suites), and the
worktree remained clean. No compiler *semantic* change is part of C011: every
merged commit adds test tags, focused gap-fill tests, or coverage gates.

### Archive validation

```text
python3 validate_archive.py
python3 -m unittest -v test_validate_archive.py
git diff --check
```

The validator accepted 222 completed documents, 19 directories, 2056 local
links, 94 source notes, 56 specification chapters, 64 classified fenced blocks,
and **318 traceability obligations (221 traced, 77 partial, 20 untraced)**.

## Carried obligations

Twenty obligations remain `untraced` because they are architectural,
future-version, or diagnostic-quality boundaries with no focused executable
unit in the 0.1.x slice. They are explicitly allow-listed in their area coverage
gates and carried by their existing owner items rather than blocking C011:

| Area | Carried obligations | Owner |
| --- | --- | --- |
| `CC` | CC-OBL-010, 011, 032, 033, 038, 039, 048 | architectural / process / source-file gaps |
| `TS` | TS-OBL-007, 038 | future edition-family subdivision |
| `DP` | DP-OBL-003, 026, 056, 057, 058, 059, 065 | future alias (G0xx), P044 refutability, sole-OTP-boundary architectural, L001 implementation-failure, future G095 validation, P117 diagnostic quality |
| `TR` | TR-OBL-013 | unsafe-recursion disclosure |
| `EF` | EF-OBL-013 | backend language boundary architectural |
| `SG` | SG-OBL-005 | no ignore/force switch |
| `ED` | ED-OBL-015 | vendor-preview prohibition |

`partial` obligations (77) carry a tagged test covering some facets; they
satisfy the C011 "at least one tagged passing test" bar and remain tagged for
the post-C011 deepening pass.

## Promotion result

The immutable identity satisfies the C011 gate. Checklist item P011 is renamed
and completed as **C011**, the
[traceability inquiry](../40-inquiries/how-should-catena-achieve-exhaustive-rule-to-test-traceability.md)
is `status: resolved`, and every normative `MUST`/`MUST NOT` obligation has a
permanent identifier and resolved anchor. This repository-governance completion
creates **no language revision**, no new normative chapter, and no compiler
semantic change; C011 is an executable-conformance and traceability milestone,
not a `0.1.x` slice.

## Threads

- [Conformance Traceability map](../10-maps/conformance-traceability.md)
- [Traceability inquiry](../40-inquiries/how-should-catena-achieve-exhaustive-rule-to-test-traceability.md)

## Follow-ups

- The `SHOULD`, `MAY`, declarative-prose, and normative-definition rules are
  deliberately out of C011's scope; they become a new checklist item for a
  later pass.
- Resolve the traceability map's open evidence-link question (pin cross-repo
  evidence URLs to an immutable commit rather than the `rewrite` branch path).
- Deepen `partial` obligations toward full facet coverage as later slices land.
