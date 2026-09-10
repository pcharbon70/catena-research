---
title: "Source-Aware Bounded Debug Sessions"
kind: specification
created: "2026-09-10"
status: normative
spec_version: "0.1.89"
tags: [specification, debugging, observability, tooling]
aliases: []
---

# Source-Aware Bounded Debug Sessions

## Status and authority

G124 defines revision `0.1.89` under [authority](../../SPECIFICATION-AUTHORITY.md),
[conformance vocabulary](../../CONFORMANCE-VOCABULARY.md), and
[implementation limits](../../IMPLEMENTATION-LIMITS.md). It executes the
[G124 plan](../../20-notes/language-completion-plan-delivery.md#item-124-debugging-and-observability)
over P100 verified origins, P117 structured reports, the admitted process and
resource semantics, and P131 secret capabilities. It adds no public language
vocabulary or source grammar (`DO-OBL-001`).

## Session and breakpoint authority

A debug session MUST rebuild and verify the selected executable and its P100
sidecar before accepting a breakpoint, trace event, stack, profile, crash
report, or evidence request. Session control MUST be an owner-bound
capability; expiration, owner death, tampering, and cross-owner control MUST
have explicit refusal outcomes (`DO-OBL-002`).

A source breakpoint MUST identify a node present in the verified sidecar.
Sidecar mode MUST return its original Catena path and span. Stripped mode and
unknown nodes MUST be reported as unavailable and MUST NOT synthesize an
origin from host filenames or stale sidecars (`DO-OBL-003`).

Breakpoint suspension MUST occur only at an explicit executable checkpoint.
The debugger MUST report a stable pause identity and MUST require an explicit
owner continuation. Closing the session MUST release suspended callers with
an explicit closed-session outcome (`DO-OBL-004`).

## Stacks, handlers, processes, and messages

Stack and handler views MUST map verified Catena frames through P100 and MUST
leave unknown host frames unmapped. Closure, handler, ordinary-expression,
foreign-entry, cancellation, and failure paths MUST retain their applicable
Catena event identity without exposing private host arguments (`DO-OBL-005`).

Every observed process MUST receive an opaque session-local identity. Parent,
child, sender, receiver, exit, cancellation, and supervision relationships
MUST use those identities rather than making raw PIDs part of portable
debugger output (`DO-OBL-006`).

Message observations MUST distinguish send, admission, receive, duplicate,
rejection, and delivery-unknown outcomes when the governing runtime contract
distinguishes them. Message payloads MUST be redacted by default; event order
MUST reflect observed order without claiming an unobserved scheduler order
(`DO-OBL-007`).

The minimum event inventory MUST cover checkpoints, returns, closures,
handlers, process spawn and exit, message send and receive, foreign entry and
exit, cancellation, failure, and generated derivation. Additional events MUST
identify their implementation profile and MUST NOT weaken these meanings
(`DO-OBL-008`).

## Bounded traces and profiles

A trace buffer MUST have a published positive finite capacity. Exhaustion MUST
drop the oldest retained event, increment an exact loss count, and mark the
snapshot incomplete. It MUST NOT silently discard loss or block forever to
retain an unbounded history (`DO-OBL-009`).

Tracing and breakpoints perturb execution. Reports MUST say so and MUST NOT
promise preservation of timing, scheduling, mailbox races, timeout outcomes,
or reduction counts. Stable event identities and declared semantic ordering
remain required within the observations actually retained (`DO-OBL-010`).

Profiling MUST group observations by source node and event kind, carry the
verified origin when available, and report count plus host-relative first and
last observation times. These times are nonsemantic host evidence and MUST
NOT become portable latency, allocation, or scheduler guarantees
(`DO-OBL-011`).

Crash reports MUST distinguish error, exit, throw, and unknown classes, carry
verified redacted frames and the bounded trace snapshot, report trace loss,
and label erased runtime values unavailable. Raw failure values MUST be
redacted unless an explicit typed disclosure policy authorizes their shape
(`DO-OBL-012`).

## Values, generated code, and erased evidence

Values, arguments, payloads, messages, and secret fields MUST be redacted by
default. Any disclosure MUST pass an explicit typed bounded codec and P131
redaction. Holding a debug capability MUST NOT grant new application,
environmental, foreign, native, or secret authority (`DO-OBL-013`).

Unavailable optimized values MUST be labeled unavailable. Generated
derivations MUST identify both the generated event and the originating source
node when that relation is present in the verified sidecar. A debugger MUST
NOT invent eliminated values or pretend a generated host frame is handwritten
source (`DO-OBL-014`).

C113 verification-only declarations MUST remain absent from runtime code and
values. A verified external evidence link may navigate their original source
locator and digest; it MUST NOT load them into the executing module. Stripped
artifacts retain neither source recovery nor an exception to erasure
(`DO-OBL-015`).

An implementation claiming G124 MUST publish session, bound, redaction,
breakpoint, loss, perturbation, timing, erasure, stripped-build, and
public-source fields. Conformance MUST execute a compiled source checkpoint
and failure, verify mapped stacks, exercise trace overflow, process identity,
profiling, stripped mode, owner death, event-size refusal, external evidence,
lifecycle selection, trust inventory, production build, and the full suite
(`DO-OBL-016`).

## Rationale and evidence (non-normative)

The [implementation journal](../../50-journal/2026-09-10-debugging-and-observability.md)
records sixteen four-way choices and compiler PR 173. Cooperative checkpoints
make suspension explicit in the current bootstrap while preserving a path for
future P109 source instrumentation. They do not turn debugger timing into
program semantics.

