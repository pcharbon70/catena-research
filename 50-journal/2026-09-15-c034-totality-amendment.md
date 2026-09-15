---
title: "C034 Opt-In Totality Amendment"
kind: journal
created: "2026-09-15"
tags:
  - catena
  - conformance
  - recursion
  - specification
  - termination
  - totality
aliases:
  - "C034 0.1.99 amendment record"
---

# C034 Opt-In Totality Amendment

## Decision

The user approved the recommended progression from `fn` through `transform`
and `total transform` to named guarantees, then explicitly requested the C034
amendment needed by that design. The resulting normative
[Opt-In Totality Validity Amendment](../60-specification/opt-in-totality-validity/explicit-total-declaration-gate.md)
uses language revision `0.1.99`.

The amendment replaces only the 0.1.31 claim that a termination checker can
never affect validity. Ordinary program recursion remains unrestricted and
divergence remains non-termination. A later slice can gate validity only for a
declaration whose author explicitly opts into totality. Removing the marker
returns the same otherwise legal body to ordinary recursion.

## Admission boundary

The amendment makes the later source slice responsible for the complete
contract: explicit syntax or decoded role, type and effect preconditions,
abstract totality meaning, sound conservative acceptance, deterministic proof
objects, independent verification, call and recursion evidence, diagnostics,
interface identity, compatibility, erasure, implementation limits, exhaustion,
and executable conformance evidence.

Structural constructor descent is the initial recursive proof discipline.
Tests, timeouts, profiling, and author assertion cannot establish universal
totality. Proof construction and verification remain total-or-bounded, and
finite-resource exhaustion stays distinct from a semantic counterexample.

## Lifecycle and implementation status

The immutable change record is
`change-0-1-99-opt-in-totality-validity-gate`, from `0.1.98` to `0.1.99`,
classified as a compatible correction affecting static meaning. It repairs the
overbroad future prohibition while accepting no new source and changing no
existing program.

This research change does not implement exact `0.1.99` selection in the sibling
compiler. It adds no `transform`, `total`, or `guarantee` token, parser node,
totality checker, proof-object format, diagnostic, interface field, or persisted
format. `RT-OBL-009`–`RT-OBL-015` are therefore registered as partial in the
[traceability map](../10-maps/conformance-traceability.md). Historical 0.1.31
evidence for `RT-OBL-001`–`RT-OBL-008` remains intact.

## Verification

`python3 validate_archive.py` passed with 780 documents, 111 directories,
8,812 local links, 225 specification chapters, 104 classified fenced
blocks, and 1,373 traceability obligations. The seven new amendment obligations
are deliberately `partial`, bringing the corpus totals to 1,246 traced, 106
partial, and 21 untraced obligations. All 37 validator unit tests passed, and
`git diff --check` passed.

## Next work

P109 must admit the selected source forms and provide the parser, conservative
checker, independent verifier, totality evidence in interfaces, dedicated
diagnostics, finite limits, retained-revision regressions, and reference/BEAM
agreement. Only that later slice can claim that `total transform` is implemented.
