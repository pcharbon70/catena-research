---
title: "C012 Implementation Limits"
kind: journal
created: "2026-08-17"
tags:
  - conformance
  - governance
  - specification
  - testing
aliases:
  - "C012 implementation-limits evidence"
---

# C012 Implementation Limits

## Observations

Checklist item G012 is complete as C012. The root
[Catena Implementation Limits and Portability policy](../IMPLEMENTATION-LIMITS.md)
defines portable minima, configurable implementation limits, evidence bounds,
runtime-capacity disclosure, structured exhaustion diagnostics, transactional
failure, machine-readable reporting, and version-axis separation.

The selected portable floors are 253 explicit callable arguments, 4,096
integer digits, a reserved 65,536-byte decoded literal payload, and 1,048,576
bytes per generated BEAM module. Existing 20,000-step budgets and the 1,024
kernel nesting-depth boundary retain their local semantics and diagnostics.
Condition fact analysis, reference execution, and schedule exploration remain
inconclusive evidence bounds. Mailbox capacity is deployment-defined and may
not silently change per-sender order, send targeting, or live-target delivery.

The decision was developed in the
[synthesis](../20-notes/catena-implementation-limits-and-portability.md) and
[resolved inquiry](../40-inquiries/how-should-catena-bound-implementation-limits.md),
with a [topic map](../10-maps/implementation-limits-and-portability.md) routing
through the official OTP 29
[system-limit](../30-sources/erlang-otp-29-system-limits.md) and
[runtime-control](../30-sources/erlang-otp-29-runtime-resource-controls.md)
evidence.

## Compiler evidence

The coordinated sibling-compiler implementation is immutable commit
[`841af5ee342a31ff4769749bbdaa18a675b1bb21`](https://github.com/pcharbon70/catena/commit/841af5ee342a31ff4769749bbdaa18a675b1bb21)
on draft PR [#88](https://github.com/pcharbon70/catena/pull/88), based on the
`rewrite` branch. It adds:

- `Catena.ImplementationLimits` as the executable registry used by production
  checks, diagnostics, tests, and profile output;
- deterministic `catena conformance-info` format
  `catena-conformance-info` version 1;
- `LIM001`, `LIM002`, and `LIM003` enforcement for source arity, integer
  magnitude, and generated BEAM size;
- common `limit_id`, `minimum_supported`, `configured`, `observed`, and `unit`
  diagnostic details;
- central values for every existing compiler refusal and evidence cutoff; and
- `IL-OBL-001` through `IL-OBL-012` coverage, with the governance-only version
  obligation explicitly allow-listed from compiler behavior.

The 253-argument kernel boundary test passes through effect-directed lowering
and inspects the resulting arity-255 OTP worker. Both current frontends accept
4,096 integer digits and refuse 4,097. Module-size helpers test the final
supported byte and first refused byte. Profile tests verify registry
completeness, deterministic encoded output, limit classifications, and mailbox
disclosure.

## Evidence

The compiler verification sequence was:

```text
mix format --check-formatted
mix clean
mix compile --warnings-as-errors
mix test
mix escript.build
git diff --check
```

The clean compiler build emitted no warnings, all 179 tests passed, the escript
was generated successfully, and the diff check passed. The compiler package
release remains `0.1.0`; the current language revision remains `0.1.8`.

The research archive verification sequence is:

```text
python3 -m unittest -v test_validate_archive.py
python3 validate_archive.py
git diff --check
```

The focused validator suite reported 26 passing tests. Complete archive
validation reported 229 completed documents, 19 directories, 2,215 local
links, 96 source notes, 56 specification chapters, 64 classified fenced
blocks, and 330 traceability obligations: 232 traced, 77 partial, and 21
untraced. The diff check passed.

## Result

C012 closes G012 without changing a normative language chapter. The milestone
governs how implementations bound and report existing or future language work
and supplies executable compiler conformance behavior, but it does not add
syntax, typing, runtime values, interface or artifact schema, signature
domains, or BEAM representation. It therefore consumes no language revision;
`0.1.9` remains the next unused semantic patch.

## Threads

- C017 now activates and refines the reserved decoded-literal dimension as
  `LIM004`.
- G068 and G129 define concrete mailbox quotas, process failure,
  backpressure, supervision, and deployment behavior.
- G126–G131 retain threat models, TCB scope, unsafe boundaries,
  reproducibility, denial-of-service policy, and supply-chain response.
- Aggregate input size, memory accounting, cancellation, and large-project
  performance remain part of the wider implementation-quality program.

## Follow-ups

Keep the root policy, area variability registers, sibling compiler registry,
human-readable compiler profile, and `conformance-info` schema synchronized.
Any new finite dimension must state its measurement point, unit, floor,
configured value, exhaustion outcome, transaction boundary, and version-axis
impact before a conformance claim depends on it.
