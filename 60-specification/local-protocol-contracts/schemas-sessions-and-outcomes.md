---
title: "Local Protocol Schemas, Sessions and Outcomes"
kind: specification
created: "2026-09-08"
status: normative
spec_version: "0.1.55"
tags:
  - specification
  - actors
aliases: []
---

# Local Protocol Schemas, Sessions and Outcomes

## Status and authority

This chapter completes C087 as an explicit local library contract at `0.1.55`,
under the [authority policy](../../SPECIFICATION-AUTHORITY.md),
[conformance vocabulary](../../CONFORMANCE-VOCABULARY.md) and
[implementation-limit policy](../../IMPLEMENTATION-LIMITS.md).
It admits a checked protocol-application builder over retained `0.1.8` payload
producers and closed exported process interfaces. Selection is exactly
`0.1.55`, without previews. Earlier source frontends, interfaces and signed
formats retain their admission boundaries. Generated protocol artifacts record
the exact selection and frontend; they do not export a new interface format
(`LP-OBL-001`).

Operation and wire-role names below identify semantic roles, not adopted
public vocabulary. This is a library state machine with dynamic terminal-state
enforcement. It does not establish linear ownership or static session fidelity.
The [advanced-type exclusions](../excluded-advanced-type-features/README.md)
remain in force. Remote serialization, node negotiation and partitions belong
to G091; no remote process is admitted by this local adapter.

## Schema and admission

A schema contains a nonempty protocol identity, exact three-component version,
a verified exported process interface, and four distinct nonempty UTF-8 role
labels. The process mailbox is a closed sum of negotiation and request. A
negotiation carries a reply process. A request carries an integer correlation,
a request payload, and a reply process. Both reply processes have the same
closed mailbox: readiness carries the schema identity integer; reply carries
an integer correlation and a response payload. Request and response types
satisfy the existing closed sendability rules (`LP-OBL-002`).

Schema identity binds the protocol identity/version, complete interface digest,
nominal process identity, encoded mailbox type and role map using canonical
JSON and SHA-256. The wire identity is that digest interpreted as an unsigned
integer. Any change requires new exact agreement; matching display names,
constructor prefixes or a supposedly compatible wider sum are insufficient.
The adapter validates the complete binding before starting. Negotiation sends
no application payload. A wrong readiness identity returns schema mismatch;
peer death returns peer loss; budget expiry returns negotiation timeout. No
request is transmitted before matching readiness (`LP-OBL-002`).

The host representation checks only values admitted by the closed schema:
integers, booleans, Unit, tuples, closed records and variants, declared nominal
constructors, and local process handles, recursively. Functions, raw references
and arbitrary foreign terms are rejected. Native labels are the same atoms
used by ordinary compiled variants and records; schema labels remain strings.
Artifacts carry the checked wire labels. Incoming messages never create atoms.
Schema agreement is a compatibility check, not authentication of a hostile peer.

## Checked application boundary

A checked application supplies verified pure zero-argument payload producers,
a contract, positive capacity, nonnegative integer handshake and shutdown
budgets, and a finite nonempty sequence of operations. Budgets use exact
nanoseconds. The builder defaults are capacity one and one billion nanoseconds
for each bracket budget. Explicit values replace those defaults. Each submit
provides a fresh nonempty local request key, producer name and nonnegative
relative request budget. Await and cancel refer to a preceding submit key.
Producer result types equal the schema's request type. When that type contains
a nominal type, the producer module's interface digest must equal the contract's
interface digest; equal spelling is insufficient (`LP-OBL-003`).

Invalid selection, bounds, producers, unknown keys, duplicate submit keys or
forged checked evidence are rejected before compilation with `PRT001`.
Repeated observation is admitted but returns an explicit invalid-handle outcome.
No claim that duplication is statically impossible follows from this builder.
The operation sequence is a concrete admitted application form; there is no new
surface parser syntax, automatic protocol inference or general session type.

Producers evaluate once in source operation order, before submission. A producer
trap remains a trap. Submission refusal does not turn that evaluation into
skipped work. Await returns a response or an explicit expected failure. Cancel
returns cancellation selected or a refusal. The application returns the ordered
tuple of await/cancel observations, or Unit when none exist, inside completion;
failed negotiation returns unavailability. Expected outcomes compose as ordinary
closed sums and products, following the [outcome separation](../outcome-contracts/values-sequencing-and-validation.md#explicit-elimination-and-conversion).

## Session transitions and credit

A session starts unnegotiated, becomes ready on exact agreement, and closes on
negotiation failure, peer loss or bracket completion. Closed sessions never
reopen. Each admitted request uses the next monotonically increasing correlation
integer, starting at zero, scoped to that live session. IDs are never recycled.
Concurrent requests remain distinct regardless of reply order (`LP-OBL-004`).

A request is pending, completed but unobserved, or observed. Capacity counts
both pending and completed-but-unobserved requests. At capacity, submission
returns overload before application transmission. Observation releases credit
exactly once. Completion alone retains credit so unread results cannot bypass
admission. A terminal request cannot be cancelled or completed again; after
observation its old handle is invalid. Raw Unit-returning asynchronous send is
unchanged; this bound belongs to the explicit protocol layer (`LP-OBL-004`).

| Current state | Selected event | Result |
| --- | --- | --- |
| Pending | Valid matching reply | Complete with response |
| Pending | Matching reply with invalid payload | Complete with invalid response |
| Pending | Cancellation | Complete with cancellation |
| Pending | Due expiry | Complete with timeout |
| Pending | Peer death | Complete with peer loss |
| Completed | Later reply, expiry or cancellation | Preserve first outcome |
| Completed | First observation | Return outcome and release credit |
| Observed or unknown | Reply | Ignore; never create a request |

No implicit retry, acknowledgement of application execution, exactly-once
application effect or remote delivery guarantee is introduced (`LP-OBL-005`).
Cancellation and timeout stop local waiting; they do not undo peer effects or
send a new cancellation command to the application peer.

## Time and owned lifetime

Request admission creates an absolute local monotonic deadline from its
relative budget. Waiting never restarts it. At a native receive opportunity,
queued matching events can be selected before expiry, including at a zero
budget; if no event is selected and the budget is due, expiry completes pending
requests in correlation order. The first selected terminal event wins. Clock
values and external message arrival are not portable deterministic observations.
The independent event model fixes an explicit event order; it does not promise
scheduler fairness or a real-time response bound. This follows the
[time contract](../cancellation-and-time/deadlines-waits-and-cancellation.md)
(`LP-OBL-005`).

The private protocol worker belongs to an existing owned task scope. Bracket
exit disposes private response aliases and requests closure; the enclosing
scope joins the worker under its shutdown budget. Cancellation of an owner
blocked in negotiation or observation remains a cancellation checkpoint.
Abandoned results cannot leak private response messages to subsequent caller
receives. Peer death completes all pending requests, preserves already completed
results, and prevents new traffic through the lost session. A caller needing
another peer creates and negotiates another session (`LP-OBL-006`).

A stale or foreign-owner host session handle traps at the adapter boundary;
typed application plans do not expose that handle. Unexpected private-worker
loss produces session loss. Existing scope failure and cleanup precedence
continue to apply; expected protocol failures do not intercept arbitrary traps.

## Representation composition and evidence

Task and managed-link observation results use the ordinary closed-variant
representation so that their typed results can be consumed by variant patterns.
The string-label output from the previous adapter implementation was a defect,
not a second permitted representation (`LP-OBL-007`).

Conformance requires independently checked positive and negative witnesses:
exact selection and artifact identity; wrong schema and payload rejection;
nominal owner rejection; overlapping correlations; terminal-event permutations;
capacity recovery only after observation; peer loss and late reply; owned
cleanup; and a compiled client communicating with a compiled typed actor.
The reference model is independent of the native worker and evaluates payload
producers through the kernel stepper. Its peer events are explicitly supplied,
not evidence that it executes the peer actor itself (`LP-OBL-008`).

## Variability and limits

All new behavior is fixed by this chapter; no new variability is introduced.
Program-selected capacity and budgets are semantic inputs, not hidden limits.
Allocation, generated artifacts and atom resources inherit the
[standing capacity policy](../../IMPLEMENTATION-LIMITS.md#runtime-and-mailbox-capacity).
The [area register](README.md#variability-register) records this inheritance.
This contract supplies no universal mailbox capacity or scheduler fairness
floor. P085 and C129 retain deployment resource reporting; P085's remote facet
remains open until G091.

## Rationale and evidence (non-normative)

The [CP-087 plan](../../20-notes/language-completion-plan-semantics.md#item-087-typed-protocol-contracts-p087)
selects closed payloads, explicit state machines, correlation and exact evolution
checks. The [implementation journal](../../50-journal/2026-09-08-local-protocol-contracts.md)
records four-way decisions and model, native and compiled evidence. The
[traceability map](../../10-maps/conformance-traceability.md#local-protocol-contract-registry-lp-0155)
connects obligations to those witnesses. Distribution adds a later transport
contract rather than weakening this local compatibility boundary.
