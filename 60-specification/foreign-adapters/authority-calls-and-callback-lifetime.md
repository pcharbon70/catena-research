---
title: "Authority, Calls and Callback Lifetime"
kind: specification
created: "2026-09-09"
status: normative
spec_version: "0.1.61"
tags: [specification, foreign-boundary, algebraic-effects]
aliases: []
---

# Authority, Calls and Callback Lifetime

## Status and authority

This normative P096 milestone applies to exact edition `0.1`, revision `0.1.61`,
without previews. It follows the [authority policy](../../SPECIFICATION-AUTHORITY.md),
[conformance vocabulary](../../CONFORMANCE-VOCABULARY.md), and
[implementation limits](../../IMPLEMENTATION-LIMITS.md). The
[reviewed plan](../../20-notes/language-completion-plan-delivery.md#item-096-foreign-calls-and-callbacks)
requires executed adapters before public-surface adoption. This milestone supplies
those adapters; it does not complete the whole P096 item.

The new exact programmatic declaration and foreign-program artifact are distinct
from retained core, source, serialized interface and signed formats. C095 codecs
retain `0.1.60`, C094 calling artifacts retain `0.1.59`, and the foreign-program
input retains verified C050 `0.1.50` capability core. None is silently relabeled.
No final language or library vocabulary is selected (`FA-OBL-001`).

## Explicit declarations and authority

A trusted setup supplies a host module/export, argument and result codecs,
nonempty effect-family identity, trust class, scheduler contract and cancellation
contract. This milestone admits only explicitly trusted BEAM implementations
executed in an owned process with cooperative cancellation. It does not claim a
sandbox against malicious native code, native memory corruption or VM crashes.
Native execution and port policies remain G098's responsibility.

The host entry has one explicit native argument per declared parameter plus a
final hidden cooperative-control argument. Consequently at most 254 explicit
parameters fit the BEAM 255-arity ceiling. Setup verifies the actual export and
records the loaded module's code digest. Descriptor verification reconstructs
all fields and requires exact equality; the loaded code identity is checked again
immediately before entry. Replacement is refused, never silently adopted.
The identity covers the named host module, not every external service or transitively
called dependency (`FA-OBL-002`).

A scope receives an explicit list of complete declarations as grants. Every call
requires equality with one granted declaration; a payload cannot choose a new
host export, codec, effect identity or trust claim. Scope control, call handles,
result observation and cancellation belong to the creating process. Copying
those handles to another process does not transfer control authority. Callback
invocation is the separately scoped authority described below (`FA-OBL-003`).

All host invocations are visible foreign effects. No host purity assertion makes
a call eligible for pure categorical equations or elimination. An executed
request records its effect identity and checked host identity, then its terminal
outcome. Rejected grants do not enter host code (`FA-OBL-004`).

## Typed calls and outcomes

Arguments and results use the [C095 codec relation](../erlang-type-boundary/typed-conversion-and-preservation.md#trusted-descriptions-and-admitted-meanings).
Data arguments share a complete tuple-vector preflight before individual codec
conversion; their encoded data vector is checked again. Callback arguments have
explicit input/output codec roles and require a registered, live handle from the
same scope. Raw host funs and callback handles with different types are refused.
A host result never becomes a Catena value until its declared codec succeeds
(`FA-OBL-005`).

Each admitted host call executes in an owned worker. Completion reports a typed
semantic value. Wrong return types, ordinary host exceptions and abrupt worker
death report visible traps. Existing Catena trap reasons retain their identity
when representable within the explicit diagnostic budget. An unsupported or
oversized trap reason is replaced by the stable unrepresentable-foreign-failure
classification rather than exposing unchecked native authority. Conversion
refusals remain distinct from successful data (`FA-OBL-006`).

The owner can start a call, observe its pending or terminal state, and wait for
at most its supplied millisecond interval. Wait expiry reports pending. It does
not retry, cancel or claim the host did nothing. A terminal result is retained
for the scope's lifetime. The compiled synchronous bridge maps wait expiry to a
visible trap carrying the possibility of external effects; enclosing scope
cleanup still applies.

## Cooperative cancellation and cleanup

Cancellation sends one request to the worker's private control channel. A
checkpoint belongs to that worker only. If it observes cancellation, the call
reports cancellation with its supplied reason and the explicit possibility of
external effects. A checkpoint is not a transactional rollback boundary.
Repeated cancellation reports that the request already exists (`FA-OBL-007`).

If a terminal outcome was recorded first, cancellation reports that outcome as
already terminal. If cancellation is requested while work is pending, a host
that completes without observing a checkpoint still reports completion. These
outcomes are fixed by the received event order. No automatic retry occurs.

Scope exit revokes further callback admission and terminates outstanding owned
workers. An entry admitted before revocation can finish while its scope remains
open; revocation prevents later entries. Scope cleanup terminates even a callback
that has not returned. The owner waits for worker termination through the existing
[C080 mandatory bounded-release mechanism](../resource-scopes/owned-lifetime-and-mandatory-cleanup.md).
Failure to finish release within the supplied grace is a mandatory-release trap;
a stalled manager is terminated, and its linked workers lose their owner.
Owner death also initiates cleanup through the manager's owner monitor.
Cleanup records the number of outstanding workers and explicitly preserves the
possibility of prior external effects (`FA-OBL-008`).

## Scoped compiled callbacks

Callback setup requires a deterministically verified C094 artifact, named exported
entry, immutable typed data captures, and explicit input/output codecs. The
initial evaluation and every consumed function stage are pure. The final stage
is unary and data-valued; its types must match the supplied codecs. The complete
capture vector has a shared C095 preflight, followed by typed capture checks.
Host funs, resource handles, foreign authority and effectful closures are not
admitted as captures in this milestone (`FA-OBL-009`).

Callback registration additionally requires explicit callback authority at scope
setup. The scope creates an unforgeable registration token. Only the checked
host-call argument conversion publishes the corresponding host callable. A
trusted recipient can retain it and invoke it from another process while the
scope and registration remain live. It conveys invocation authority only.
Revocation and scope expiry are checked on every entry (`FA-OBL-010`).

One invocation at a time is admitted per registration. Any overlapping entry,
including reentry, is refused visibly rather than queued. Each admitted invocation
runs in an owned worker, recreating the verified pure closure from its immutable
captures and checking input and output through the codecs. Exact artifact
verification still occurs when an identical loaded callback binary is reused;
code reuse is not permission to accept a different module body. Callback entries
and terminal outcomes appear in the scope's ordered evidence (`FA-OBL-011`).

General effectful callback authority, native-owned resource capture, application
provisioning, callback surface syntax and a public vocabulary are not supplied
by this pure callback profile. They remain explicit P096/P106/P109/P131 work.

## Checked capability-program bridge

A foreign-program description binds a verified C050 capability core's exported
zero-argument, closed-data entry to host declarations. Its initial effect row is
nonempty and contains only explicit capability slots. Bindings cover exactly
those slots and every declared operation in each slot. The host declaration's
family, parameter codecs and result codec match the checked operation exactly.
Missing, extra, differently typed and wrong-family bindings are refused.

The backend derives a handler-bearing wrapper from the actual checked CPS worker.
The foreign artifact binds the complete forms, core, bindings, compiler identity,
exact selection and toolchain metadata. Invocation reconstructs the complete
artifact and compares it exactly, then verifies all grants before loading and
entry. Altering a binary or copied digest is not proof of a valid artifact.

The bridge converts native arguments into checked semantic values, dispatches the
visible foreign call, converts a successful result into its native Catena carrier,
and invokes the continuation once. No continuation is handed to host code.
Failures remain abrupt; a failed foreign call cannot be resumed with unchecked
native data. The interface-owned descriptor builders expose this checked sidecar
without extending persisted interfaces (`FA-OBL-012`).

## Variability register

The following are explicit programmatic inputs, not hidden implementation thresholds:

| Input | Admitted values and exhaustion behavior |
| --- | --- |
| Conversion bounds | Exactly C095's positive node and nonnegative byte/depth bounds; whole-value refusal on exhaustion. |
| Maximum operations | Positive integer, default 1,024. Each host call and callback invocation consumes one slot for the scope lifetime. Further admission is refused. |
| Callback registrations | At most the same supplied maximum, including revoked registrations; further registration is refused. |
| Wait interval | Integer milliseconds from zero through 4,294,967,295; expiry reports pending without retry. |
| Release grace | Nonnegative nanoseconds, default 1,000,000,000; C080's rounding, bounded release and failure rules apply. |

Per-scope terminal evidence is retained only for admitted operations and
registrations, which are bounded above. Cancellation/completion and callback
entry/revocation outcomes follow the explicit event-order rules. Allocation,
module-size, literal-size and generated-arity limits retain the standing policy.

## Rationale and evidence (non-normative)

The [implementation journal](../../50-journal/2026-09-09-foreign-adapters.md)
records four alternatives per implementation decision, grant and type refusals,
compiled capability requests, callback capture and overlap, cooperative and
noncooperative completion races, owner death and a deliberately stalled cleanup.
The design preserves pure categorical reasoning by keeping host operations in
visible effectful paths. It establishes a useful retained-input implementation,
while keeping the plan's later surface gate and broader callback work visible.
