---
title: "Checked Supervision Trees and Lifecycle"
kind: specification
created: "2026-09-08"
status: normative
spec_version: "0.1.56"
tags:
  - specification
  - actors
aliases: []
---

# Checked Supervision Trees and Lifecycle

## Status and authority

This chapter defines C089's typed library supervision contract at exact
`0.1.56`, under the [authority policy](../../SPECIFICATION-AUTHORITY.md),
[conformance vocabulary](../../CONFORMANCE-VOCABULARY.md) and
[implementation-limit policy](../../IMPLEMENTATION-LIMITS.md).
It provides static checked worker descriptions, generated OTP child
specifications, and a narrow lifecycle adapter. It adds no core supervision
construct or public source vocabulary (`SU-OBL-001`).

The adapter accepts verified managed-process producers at `0.1.52` or `0.1.53`.
The enclosing supervision description selects exactly `0.1.56`, without
previews. Producer revisions retain their own meaning. Old kernel interfaces
and signed formats remain unchanged. The adapter manifest is a separate
origin-bound build description, not a new general interface or signed format.

This is the minimal lifecycle admission assigned to G096 by the completion
plan. It admits checked starts, linked managed ownership, typed relationship
observation and ordered shutdown through this adapter only. General foreign
calls, native callbacks and arbitrary host-term inspection remain G096 work.

## Supported policy inventory

A description has a finite nonempty ordered list of children and exactly one
strategy. The strategies restart the failed child alone, all children, or the
failed child and every later sibling. A child has exactly one restart class:
always restart, restart after abnormal exit, or never restart. Internal OTP
identifiers encode these roles without selecting Catena vocabulary
(`SU-OBL-002`).

| Strategy | Children stopped after a restart-triggering failure | Children started afterward |
| --- | --- | --- |
| Failed child alone | None beyond the failed child | Failed child |
| All children | Every remaining live child, in reverse declaration order | Retained children, in declaration order |
| Failed child and later siblings | Later live siblings, in reverse declaration order | Failed and later retained children, in declaration order |

Never-restart children are removed after their own exit and after collateral
shutdown; they are not restarted by either group strategy. Abnormal-only
children do not trigger restart after normal completion or an orderly shutdown.
Their retained descriptions can participate in a later sibling-triggered group
restart. Explicit shutdown of the tree never initiates another restart.

The supported child kind is a managed worker. Dynamic child insertion/removal,
registered/global names, significant children, automatic shutdown, arbitrary
supervisor callbacks, hot upgrades and nested supervisor child specifications
are not admitted by this description format. A program that needs them requires
a separately specified adapter; arbitrary host configuration is not a fallback.
The static root and worker list are a supervision tree, not a claim that every
OTP topology is available.

## Child entry and provisioning

Each child specifies a distinct nonempty identity, a checked local process
entry, restart class, cooperative grace and native shutdown budget. Process
entries have zero arguments and no captured capability slots. Provisioning is
explicitly fresh and empty at the boundary: each generation evaluates its body
in a new managed context and creates any admitted local scopes inside that
body. Active handles, resumptions, foreign closures and stale capability
instances cannot be supplied as restart arguments (`SU-OBL-003`).

The entry validator uses the existing checked process representation, independently
of a display-name-only lookup. Unknown entries, parameterized entries, captured
provisioning, duplicate identities and forged checked descriptions are rejected
before compilation. A restart never reuses a previous worker's process identity,
managed token, local state or scope handles. There is no automatic migration of
an old worker's state into its replacement.

A child start creates and links its managed broker before acknowledging readiness.
Acknowledgment establishes the managed process boundary; it does not claim that
application initialization inside the body has completed. A body that traps
immediately after acknowledgment is a child failure subject to restart policy.
Failure of a start function before acknowledgment causes startup rollback:
already-started children stop in reverse order before startup returns failure
(`SU-OBL-004`).

## Restart intensity and generations

Every description supplies a positive maximum restart count and a positive
window length in seconds; neither is taken from host defaults. The selected
OTP 29.0.4 profile measures this rolling window with local monotonic integer
seconds. A timestamp equal to the current second minus the period remains in
the window. A restart-triggering policy event counts once, even when it restarts
several siblings. Exceeding the count stops remaining children and then the
root with a shutdown reason (`SU-OBL-005`).

A fresh generation supersedes the prior process identity. An exit or reply
associated with an older generation does not terminate its replacement. The
independent model records generation numbers; native execution distinguishes
actual process identities. Neither numbering scheme is a public stable PID or
cross-restart routing service. Clients obtain a new target explicitly.

Restart limits control repeated failure, not the number of successful messages
or raw spawns. A child that fails on every startup eventually exhausts the
configured intensity. No infinite retry promise or scheduler fairness guarantee
is introduced.

## Shutdown and owned integration

Cooperative grace is an integer number of nanoseconds at least zero. Native
child shutdown is an integer number of milliseconds from one through
4,294,967,295. Grace is strictly less than that native budget converted to
nanoseconds. Both inputs are required; no implicit infinite shutdown is
accepted (`SU-OBL-006`).

An orderly stop first reaches the managed worker's cooperative stop path, using
existing function-entry, receive and resource-cleanup checkpoints. Exhausted
grace forces termination and retains the existing external-loss classification;
it is not successful user finalization. The outer native child timeout remains
a final forced-termination boundary. Budgets are elapsed-time allowances when
processes run, not a hard wall-clock guarantee under an unscheduled or stopped VM.

A supervisor started through the checked artifact adapter belongs to the calling
managed broker. The user worker is not linked directly to the supervisor.
Supervisor failure is interpreted through the existing managed relationship:
trapping code can observe the typed completion; otherwise linked failure selects
the cooperative stop path. A supervisor shutdown remains a process-lifecycle
event and does not interpret an arbitrary language effect (`SU-OBL-007`).

Before publishing its own completion, the managed broker stops and joins owned
supervisors in reverse acquisition order. Each static root shuts its workers
down in reverse declaration order under their individual budgets. There is no
second competing root timer that cuts the root off before it joins those
bounded worker shutdowns. A root already stopped is already joined; a bare or
wrapped no-process response does not replace the owner's result. Nested arbitrary
host supervisor callbacks are excluded precisely because this composition does
not establish their termination obligations.

Supervision does not implicitly wrap raw spawn, inherit ambient capabilities,
catch unrelated traps as expected success, or persist suspended effect handlers.
Existing cleanup precedence and the
[top-level effect boundary](../top-level-effects/the-top-level-boundary.md)
continue to govern owned process execution.

## Generated artifacts and compatibility

Compilation generates deterministic child specifications whose start functions
invoke the checked managed process body. Each specification records child
identity, restart class, explicit shutdown timeout, worker kind and owning
module. Bodies use the existing cancellation instrumentation. Source and
generated arity limits and artifact-capacity checks remain enforced
(`SU-OBL-008`).

The manifest binds source origin, module, producer revision, checked-core digest,
ordered children and strategy/bounds. In the selected implementation, the core
digest hashes deterministic Erlang term serialization; the manifest description
digest hashes canonical JSON. A separate artifact digest hashes the generated
BEAM bytes. This is a pinned build representation, not a portable serialization
of running processes or a signed proof. Loading through the adapter verifies the
complete description and deterministically regenerated artifact; altered bytes,
origin or manifest fields are rejected before starting children.

A changed child body, policy, identity or capability contract requires a new
checked build and fresh startup. No hot state migration, import widening or
implicit compatibility cast follows from matching names. Existing package
origin and entry rules remain authoritative; the adapter consumes the process
entry validator without redefining ordinary application-entry completion.

## Diagnostics, variability and limits

Invalid descriptions and artifact bindings use `SUP001`; process-entry
validation uses `ENT004`. Host failures during an admitted start retain their
lifecycle failure or trap classification. Unrelated raw host calls into the
implementation are outside checked admission.

All new behavior is fixed by this chapter; no new variability is introduced.
Program-selected policy bounds are semantic inputs. The
[register](README.md#variability-register) records inherited finite allocation,
arity, atom and artifact limits under the
[standing capacity policy](../../IMPLEMENTATION-LIMITS.md#runtime-and-mailbox-capacity).
This contract does not add a universal process-count capacity or a deployment
scheduler guarantee. The supported runtime mapping is pinned to OTP 29.0.4;
a different mapping requires an explicitly checked profile.

## Evidence and rationale (non-normative)

The [CP-089 plan](../../20-notes/language-completion-plan-semantics.md#item-089-supervision-g089)
selects library supervision, a bounded policy matrix and minimal lifecycle
admission. The [pinned OTP source note](../../30-sources/erlang-otp-29-supervision.md)
separates host documentation from Catena's chosen subset. The
[implementation journal](../../50-journal/2026-09-08-typed-supervision.md)
records four-way decisions and independent model, native tree and checked
artifact evidence. Those tests cover the selected policies and failure
boundaries; they do not prove all possible OTP interleavings.
