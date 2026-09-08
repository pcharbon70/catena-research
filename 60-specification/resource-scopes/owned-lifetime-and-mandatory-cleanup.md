---
title: "Owned Lifetime and Mandatory Cleanup"
kind: specification
created: "2026-09-08"
status: normative
spec_version: "0.1.51"
tags:
  - specification
  - algebraic-effects
aliases: []
---

# Owned Lifetime and Mandatory Cleanup

## Status and authority

This chapter defines C080 at exact `0.1.51`, edition `0.1`, without previews.
The [authority policy](../../SPECIFICATION-AUTHORITY.md),
[conformance vocabulary](../../CONFORMANCE-VOCABULARY.md) and
[implementation-limit policy](../../IMPLEMENTATION-LIMITS.md) apply.

It extends the [closed capability target](../closed-capability-kernel/identity-rows-and-comprehension-target.md#input-and-selection)
with programmatically supplied scope, handle-read, owner-cancellation and
cooperative-exit nodes. The retained decoder supplies quoted `0.1.8` syntax
structure; the explicit compound input supplies the new meaning. Bare retained
source and exact `0.1.50` keep their previous semantics. No public source
keywords, standard-library names, new S-expression frontend, interface format
or signed format are introduced (`RS-OBL-001`).

For computations in this target, this chapter replaces stack-discarding
terminal behavior only to run the cleanup required below before termination.
It fills C005's resource-unwinding reservation and C037's absence of explicit
resource finalization for these owned scopes only. Garbage-collection timing
remains unobservable. It does not alter raw spawn isolation, admit catchable
traps, or change affine resumption rules.

## Compound input and static semantics

Input consists of a retained decoded module, explicit slot/family bindings,
and inserted scope/read/cancellation/exit nodes. A scope has acquisition,
release callback, body, nonnegative exact-integer nanosecond release grace,
and an optional lexical handle binder. The release callback is an explicit
function from the acquisition payload type to `Unit`, with an empty latent
effect row. The payload type is closed and sendable in the retained data
model. This admits immutable local values; it does not admit foreign pointers,
mutable buffers or process-affine foreign ownership (`RS-OBL-001`).

The release function is formed before acquisition executes. Successful
acquisition alone registers a release; acquisition trap or handler abandonment
registers nothing for that acquisition. Earlier acquired resources still
unwind when their scopes are abandoned (`RS-OBL-002`).

A handle has an opaque type indexed by a structural scope identity and payload
type. Identity is derived from module origin, module owner, definition-versus-
process role, entry position and scope preorder. Inserted nodes sharing source
spans still have distinct identities. Independent verification rederives them.
Each dynamic entry has a fresh runtime token even when recursion reuses the
same static scope (`RS-OBL-006`).

A handle read copies the admitted immutable payload while the handle is live.
A handle cannot be returned beyond its scope, sent in a message, or captured
by a function closure, including indirectly through a tuple, record or nominal
value. This initial contract rejects closure capture even when a caller expects
the closure to remain local. Reading an immutable value does not transfer the
handle. Unknown, foreign-owner and released tokens fail before resource use.
The independent verifier checks type evidence and the same lifetime boundary
(`RS-OBL-006`).

Scope nodes are admitted in value definitions and local process bodies.
Handler clauses do not acquire resource scopes in this revision. Release
execution cannot reenter acquisition or open another resource scope: a reached
reentry is a mandatory release failure (`RS-OBL-005`).

## Acquisition and cleanup order

Resource entries progress through acquisition, active ownership, release, and
released or release-failed states. A failed acquisition never reaches active
ownership. Released and failed entries cannot register or release again.
One runtime owner controls each registration (`RS-OBL-002`, `RS-OBL-006`).

Normal completion closes nested scopes from innermost to outermost. Within
an owner, resources unwind in reverse acquisition order. Cleanup occurs before
the enclosing computation's next continuation step. The implementation MUST
NOT postpone normal cleanup until that enclosing suffix finishes (`RS-OBL-003`).

Capturing an affine continuation suspends its scope frames without releasing
them. Resumption reinstalls those frames. If the handler declines resumption,
the captured resource scopes close before control returns to the handler's
outer continuation. Neither abandonment nor a trap can silently discard a live
registration. The abandoned computation is never resumed by cleanup
(`RS-OBL-004`).

Each release is attempted at most once. After a release fails or exhausts its
grace, remaining acquired releases are still attempted in their required order.
A failed release is recorded as failed; it is never reported as successful
cleanup (`RS-OBL-005`, `RS-OBL-008`).

## Outcomes and provenance

The selected primary outcome is recorded before cleanup. Ordered release
results retain secondary failures without creating a catchable aggregate
language value (`RS-OBL-005`).

| Primary outcome | Successful cleanup | Any mandatory release failure |
| --- | --- | --- |
| Normal value, including a typed failure value | Preserve that value | Terminal mandatory-release-failure trap |
| Handler abandonment | Preserve the handler result | Terminal mandatory-release-failure trap |
| Terminal trap, including a panic producer | Preserve the original trap | Preserve that original trap; retain secondary failures |
| Owner cancellation | Cancelled outcome | Terminal mandatory-release-failure trap |
| Cooperative owner exit | Exited outcome | Terminal mandatory-release-failure trap |
| External forced process loss or VM loss | No cleanup completion is promised | No stronger guarantee is inferred |

The earliest failed release determines a newly produced mandatory-release
trap. Later release failures remain ordered secondary evidence. An original
trap always keeps its reason. Typed failure remains an ordinary value;
implementations do not recognize failures by constructor spelling. Cleanup
never supplies a source-level trap-catching mechanism (`RS-OBL-004`,
`RS-OBL-005`, `RS-OBL-009`).

## Local cancellation, exit and deadlines

The local cancellation and cooperative-exit hooks require a live handle owned
by the current process and an integer reason. They abandon current computation,
unwind that owner's active scopes, and select distinct cancelled or exited
outcomes. They are not ordinary algebraic requests and cannot be intercepted
by a nearest-family handler (`RS-OBL-007`).

Cleanup masks cooperative cancellation. A release callback has no live owner
handle and cannot cancel its caller. Repeated cancellation does not duplicate
release or retroactively replace a scope outcome already selected. Task-tree
propagation, general safe-point insertion, sleep, receive deadlines and their
message races remain G088/P084 integration work (`RS-OBL-007`).

Release grace is measured from release dispatch. The BEAM target rounds it
up to whole milliseconds; zero requests an immediate deadline choice. Long
allowances use repeated finite waits against the original monotonic deadline,
not a reset allowance. Monotonic origins are local to one runtime. Grace is a
waiting allowance, not a realtime scheduling guarantee (`RS-OBL-008`).

The reference has an explicit nondecreasing virtual clock. Release expiry is
enabled only at or after that release's deadline. A successful completion and
an eligible deadline race by transition order: exactly one wins, and a late
completion cannot revive a failed release. Reference evaluator fuel is not
time. A finite scope stack has a finite sum of its per-release allowances,
subject to the standing runtime-capacity and external-loss limits (`RS-OBL-008`).

## Host boundary and exclusions

The admitted release callback executes over immutable local values in a
runtime-owned helper. The owner retains scope authority; the helper receives
only release computation and payload. The owner waits for completion or grace
expiry and stops an expired helper before continuing cleanup. This does not
license transfer of process-affine foreign resources (`RS-OBL-008`, `RS-OBL-009`).

External process kill, VM loss and noncooperative foreign execution cannot
receive a local unwinding promise. No foreign resource registration or foreign
frame adapter is admitted by this chapter. Future G095/G096/G098 admission
must specify ownership, unwinding and forced-termination limits explicitly.
Raw local process completion and traps run their admitted scope cleanup;
links, monitored typed completion, supervision and structured children remain
separate lifecycle work (`RS-OBL-009`).

## Artifacts, diagnostics and conformance

Production lowering verifies the core and applies the standing source and
generated-code limits before emitting a deterministic `0.1.51` BEAM artifact.
The entry is a zero-argument main with no residual or escaping ordinary
capability or resource handle. Intrinsic Process remains available. Compile
metadata names the `0.1.51` compound-tree target. Interface and signed-format
sets remain unchanged; this artifact returns no importable interface
(`RS-OBL-010`).

Wrong exact language selection is `EDN001`. Invalid scope formation, payload,
release type, binder, handle use, escape or closure capture uses `T002`.
Inconsistent typed-core evidence is `I001`; an incompletely closed entry uses
`EFX003`. Runtime owner violation, release reentry and mandatory release
failure are named terminal conditions. Standing explicit limit failures keep
their existing categories (`RS-OBL-001`, `RS-OBL-005`, `RS-OBL-006`,
`RS-OBL-010`).

| Obligation | Required evidence |
| --- | --- |
| RS-OBL-001 | Exact compound selection and checked acquisition/release formation; retained boundaries reject scope nodes |
| RS-OBL-002 | Successful acquisition registers once; failed or abandoned acquisition does not release that entry |
| RS-OBL-003 | Nested reverse release and cleanup before the enclosing suffix, including local process return |
| RS-OBL-004 | Real handler resume/abort and terminal trap cleanup agree across reference and BEAM |
| RS-OBL-005 | Primary provenance, first release failure, later attempts, reentry rejection and secondary evidence |
| RS-OBL-006 | Deterministic identity, opaque scoped reads, static escape/capture rejection and runtime owner/status checks |
| RS-OBL-007 | Owner cancellation and cooperative exit unwind distinctly, with terminal precedence on release failure |
| RS-OBL-008 | Bounded release, monotonic virtual deadline eligibility and single-winner completion races |
| RS-OBL-009 | Typed local actor cleanup and explicit forced-loss/foreign admission exclusions |
| RS-OBL-010 | Independently verified deterministic production artifact with closed entry and no old-format widening |

## Variability and limits

This area introduces no new configurable implementation choice, presentation
allowance or implementation-limit dimension. Explicit grace and permitted
clock-event ordering are part of the input/execution contract. The
[standing limits](../../IMPLEMENTATION-LIMITS.md#machine-readable-reporting)
continue to classify runtime capacity, reference fuel and bounded exploration.

## Lifecycle

The lifecycle record is `change-0-1-51-resource-scopes`, predecessor
`0.1.50`, compatible addition affecting source acceptance, static meaning,
dynamic behavior and artifacts. Existing bare programs are not rewritten.

## Evidence and rationale (non-normative)

The [implementation journal](../../50-journal/2026-09-08-resource-lifetime.md)
records the four-option decisions and target comparisons. The
[scope research](../../20-notes/algebraic-effects-and-handlers.md#scoped-and-higher-order-effects)
explains why first-order handlers alone do not establish lifetime. The
[pinned OTP source](../../30-sources/erlang-otp-29-time-and-process-bifs.md)
supports the host worker and monotonic-clock mapping without supplying Catena's
ownership rules. The [completion plan](../../20-notes/language-completion-plan-semantics.md#item-080-cleanup-and-resource-scopes-g080)
keeps later foreign and task integration explicit.
