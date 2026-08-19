---
title: "How Should Catena Bound Implementation Limits?"
kind: inquiry
created: "2026-08-17"
status: resolved
tags:
  - conformance
  - governance
  - language-design
  - specification
aliases:
  - "Catena C012 inquiry"
---

# How Should Catena Bound Implementation Limits?

## Why this matters

Catena already rejects otherwise valid work at several deterministic compiler
budgets, returns inconclusive results from bounded evidence tools, targets a VM
with concrete representation ceilings, and relies on mailboxes backed by finite
deployment resources. Without one policy, an implementation could configure a
tiny bound, report search exhaustion as a semantic error, silently drift from
its documentation, or turn runtime pressure into message loss while still
claiming the ordinary language behavior.

## Operational question

A successful answer must classify every current finite boundary, define
portable minima for exposed source and artifact dimensions, state whether
implementations may support more, standardize measurement and diagnostic
details, preserve transactional failure, and provide deterministic
machine-readable discovery. It must explain mailboxes without inventing a
false portable count and must not consume language revision `0.1.9` for a
governance decision.

## Working hypotheses

- Portable floors should be lower bounds; implementations may configure
  larger values but not smaller ones.
- Target-runtime ceilings need translation through the complete lowering
  strategy rather than direct copying into the source language.
- Compiler refusals and evidence cutoffs need different classifications and
  outcomes even when both use the same numeric default.
- A central executable registry can prevent profile, diagnostic, and
  production-check drift.
- Mailbox capacity is deployment-defined, but resource pressure cannot weaken
  language ordering, targeting, or live-target delivery observations.
- A reserved not-applicable entry is more honest than enforcing a limit on a
  literal form the language does not yet have.

## Paths to explore

- Audit the current normative variability registers and sibling compiler for
  every hard-coded 20,000-step or 1,024-depth boundary.
- Derive the callable floor from
  [OTP 29 system limits](../30-sources/erlang-otp-29-system-limits.md) and the
  current two-argument CPS worker overhead.
- Compare heap, queue-storage, and distribution controls in
  [OTP 29 runtime resource controls](../30-sources/erlang-otp-29-runtime-resource-controls.md).
- Test the greatest supported and first refused value across both compiler
  frontends and at the generated BEAM boundary.
- Extend C011's stable traceability pattern to cross-cutting governance
  obligations without claiming that the root policy is a language chapter.

## Findings

The corpus supports four roles: implementation limits, evidence bounds,
runtime capacities, and explicitly not-applicable reserved dimensions. The
existing diagnostics already embody the distinction but lacked a common
measurement contract and executable registry.

OTP's arity-255 ceiling yields a 253-argument source floor because current
effect workers add handler state and a continuation. The selected integer,
decoded-payload, and generated-module floors—4,096 decimal digits, 65,536
decoded bytes, and 1,048,576 BEAM bytes—are generous bootstrap baselines with
unambiguous units and boundary pairs. Existing language-area budgets remain
20,000, and kernel parser depth remains 1,024.

Mailbox research does not support one portable message count. ERTS heap
limits, garbage-collection timing, on/off-heap queue storage, distribution
buffers, and host memory interact. The portable result is therefore a semantic
constraint on any later capacity policy, not a numeric C012 floor.

The complete reasoning, tradeoffs, and falsification criteria are developed in
[Catena Implementation Limits and Portability](../20-notes/catena-implementation-limits-and-portability.md).

## Outcome

The question is resolved by the root
[Catena Implementation Limits and Portability policy](../IMPLEMENTATION-LIMITS.md),
the compiler's central `Catena.ImplementationLimits` registry and deterministic
`catena conformance-info` command, `LIM001`–`LIM003`, common structured limit
details, and the `IL-OBL-001`–`IL-OBL-012`
[traceability registry](../10-maps/conformance-traceability.md).

The [C012 record](../50-journal/2026-08-17-c012-implementation-limits.md)
preserves the immutable compiler identity and validation. C017 now activates
the decoded literal floor as `LIM004`; G068 and G129 own concrete concurrency capacity,
backpressure, and failure semantics; and G126–G131 retain the wider security,
reproducibility, TCB, and operational-resource program. Those exclusions do
not reopen the bounded C012 decision.
