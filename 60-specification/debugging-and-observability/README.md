---
title: "Debugging and Observability"
kind: map
created: "2026-09-10"
tags: [specification, debugging, observability, tooling]
aliases: []
---

# Debugging and Observability (`60-specification/debugging-and-observability`)

## Purpose

The normative source-aware debugging, bounded tracing, profiling, crash-report,
and erased-evidence boundary under [Specification Authority](../../SPECIFICATION-AUTHORITY.md),
[Catena Conformance Vocabulary](../../CONFORMANCE-VOCABULARY.md), and
[Catena Implementation Limits and Portability](../../IMPLEMENTATION-LIMITS.md).

## What belongs here

Rules for verified source origins, cooperative breakpoints, stack and handler
views, process and message identities, trace loss, profiling attribution,
redaction, optimized or generated code, stripped artifacts, and external
evidence navigation.

## Index

### Subdirectories

None yet.

### Documents

- [Source-Aware Bounded Debug Sessions](source-aware-bounded-debug-sessions.md) — G124's revision 0.1.89 debugger, trace, profile, crash-report, and evidence contract.

## Variability register

Implementations may expose additional host-technical frames and event kinds,
choose a bounded trace capacity up to their published maximum, and provide
explicit typed value-disclosure codecs. They must preserve Catena event
identity, mark unavailable data, report trace loss and perturbation, and keep
values redacted by default.

## Maintaining this index

Keep the debugger session, P100 origin sidecars, P117 diagnostic records,
runtime event adapters, secret policy, conformance profile, and traceability
map in sync.

