---
title: "Values, Capacity, and Transport"
kind: specification
created: "2026-09-10"
status: normative
spec_version: "0.1.77"
tags: [specification, concurrency, runtime, foreign-boundary]
aliases: []
---

# Values, Capacity, and Transport

## Status and authority

C085 defines revision `0.1.77` under [authority](../../SPECIFICATION-AUTHORITY.md),
[conformance vocabulary](../../CONFORMANCE-VOCABULARY.md), and
[implementation limits](../../IMPLEMENTATION-LIMITS.md). It completes the
[reviewed message plan](../../20-notes/language-completion-plan-semantics.md#item-085-messages-capacity-and-transport-p085)
by composing retained local send, typed protocol, resource-capacity, foreign
value, native-role, and distribution contracts. It adds checked internal APIs
without selecting final public source vocabulary (`MS-OBL-001`).

## Message values and observations

A message is admitted only under a trusted static mailbox type or an explicit
checked codec supplied by trusted setup. The payload must be a recursively
valid immutable value of that declared type. Incoming payload structure cannot
select or replace its type, nominal identity, codec, owner, or authority
(`MS-OBL-002`).

Integers, Booleans, Unit, finite Float, Text, Character, Bytes, tuples, closed
records, closed variants, and admitted closed nominal data are ordinary
sendable data when their complete recursive payload passes its governing
checks. A local Catena process handle is sendable only where its static mailbox
type admits that handle. A C097 borrowed local-process native handle transfers
only its registered send authority under that live scope's exact mailbox codec
(`MS-OBL-003`).

Functions, resumptions, lexical capabilities, secrets, task/resource handles,
fresh native references, raw PIDs, raw ports, arbitrary host funs, unchecked
host terms, and forged native wrappers are not ordinary sendable data. A
specialized checked boundary can admit only the operation already authorized
by its governing contract; this never turns its carrier into general data
(`MS-OBL-004`).

The semantic observation of a sent immutable value is independent of physical
copying. An implementation can copy, retain, or share immutable substructure
and binaries when receiver-visible values, identities, authority, order,
lifetime, and resource outcomes remain unchanged. Programs receive no pointer,
buffer, allocation, copy-count, or sharing-identity observation
(`MS-OBL-005`).

## Local raw send

C010 local send remains asynchronous and returns Unit after accepting a
well-typed send step. Unit does not acknowledge target liveness, mailbox
admission, receipt, processing, completion, or effect commitment. Sending to a
dead local target returns Unit and discards the payload under the retained
rule. It does not produce a liveness race or retry (`MS-OBL-006`).

For messages sent sequentially by one local sender to one local receiver, the
receiver's mailbox preserves that sender's order. Messages from different
senders can interleave in any order consistent with each sender's order. No
scheduler fairness or cross-sender total order is implied. C086 selection can
bypass unmatched messages without changing the preserved residual order
(`MS-OBL-007`).

Raw local mailbox capacity is deployment-defined. Resource pressure does not
authorize a conforming implementation to retarget, reorder, mutate, or silently
discard an already accepted live-target message while reporting the ordinary
successful C010 step. Emulator or operating-system fatal exhaustion remains
outside recoverable language behavior (`MS-OBL-008`).

## Checked local and bounded admission

A checked local boundary validates and round-trips the complete payload through
its exact codec and explicit node, byte, and depth budgets before sending. An
invalid or exhausted payload sends nothing. A successful checked local send
then uses C010's Unit and dead-target behavior; validation success is not a
delivery acknowledgement (`MS-OBL-009`).

A capacity-sensitive sender uses C129's explicit bounded queue. Payload
validation completes before capacity accounting or queue mutation. Successful
admission returns `admitted`; over-capacity work returns the selected explicit
overload outcome and is not enqueued. Accepted payloads remain FIFO in admission
order, and several producers retain each producer's sequential order
(`MS-OBL-010`).

> **Implementation-defined choice.** Deployments configure raw mailbox controls
> outside the language and configure each checked capacity service with positive
> message and encoded-byte bounds and its C129 overload policy. The implementation
> profile exposes the configured ceilings, accounting method, and supported
> outcomes (`MS-OBL-011`).

## Foreign and native boundaries

C095 codec conversion validates the complete foreign value before it becomes a
message snapshot. Mutable or authority-bearing foreign objects are not admitted
by resemblance to an immutable Catena shape. Trusted host code can retain its
own object after conversion; Catena promises only that subsequent host mutation
cannot alter the admitted semantic message (`MS-OBL-012`).

C097 local-process authority checks the live registered scope, exact role,
target locality, mailbox codec, payload, and operation budget for every send.
The holder cannot reflect the PID, compare the handle, change the codec, acquire
target ownership, or use an expired/forged scope. The successful result remains
Unit and preserves C010 dead-target behavior (`MS-OBL-013`).

## Remote transport

Remote messages use C091's mutually authenticated endpoint and bounded typed
frame rather than C010 raw send. `not_enqueued` states that transport did not
transmit the work; `delivery_unknown` states that transmission occurred without
a remote-admission acknowledgement; `admitted` states only that the authenticated
receiver admitted the checked frame. None states that application processing or
an effect completed (`MS-OBL-014`).

Remote retry is application-owned and supplies a stable message identity.
There is no automatic retry or exactly-once-processing promise. Exact duplicates
are suppressed and conflicting reuse of one message identity is rejected under
C091. Protocol, package, service, certificate, or distribution skew is refused
before application delivery (`MS-OBL-015`).

## Diagnostics and conformance

The machine-readable profile MUST expose the revision, raw local and dead-target
results, checked capacity status, physical-copy requirement, physical-sharing
observability, native authority discipline, and remote contract revision. Tests
MUST cover checked local success, invalid-payload non-send, dead target, immutable
binary observations, validation before capacity accounting, exact capacity and
overload, several producers with per-sender order, C097 authority/lifetime,
C091 partition outcomes, and retained C010/C086 behavior (`MS-OBL-016`).

## Rationale and evidence (non-normative)

The [implementation journal](../../50-journal/2026-09-10-message-semantics.md)
records twelve four-way implementation decisions and the complete compiler run.
The [OTP process evidence](../../30-sources/erlang-otp-29-processes.md) and
[runtime resource evidence](../../30-sources/erlang-otp-29-runtime-resource-controls.md)
support separating message order from scheduler and memory policy. C095/C097
executable evidence supplies checked foreign conversion and scoped native send;
C091 supplies authenticated remote uncertainty.
