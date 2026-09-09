---
title: "Typed Admission and Native Identity"
kind: specification
created: "2026-09-09"
status: normative
spec_version: "0.1.62"
tags: [specification, foreign-boundary, beam-vm]
aliases: []
---

# Typed Admission and Native Identity

## Status and authority

This normative C097 contract applies to exact edition `0.1`, revision `0.1.62`,
without previews. It follows the [authority policy](../../SPECIFICATION-AUTHORITY.md),
[conformance vocabulary](../../CONFORMANCE-VOCABULARY.md), and
[implementation limits](../../IMPLEMENTATION-LIMITS.md). It completes the
[reviewed native-kind gate](../../20-notes/language-completion-plan-delivery.md#item-097-beam-native-values):
each native kind has an admitted typed role or an explicit justified exclusion,
and useful admitted roles execute.

This profile adds native role descriptions and scope grants, not a generic host
term type or final source vocabulary. Its host declarations explicitly select
`0.1.62`; the default P096 declaration/scope still selects `0.1.61` and refuses
new native roles. A `0.1.62` scope can use a retained verified `0.1.61` declaration.
An explicit conflicting selection is refused rather than overwritten. There is
no new source executable, artifact, serialized interface or signed format.
The C095 codecs and P096 capability-program artifact retain their own revisions
(`NV-OBL-001`).

## Native-kind admission inventory

| Native kind | Admitted meaning and owner | Identity, equality and transfer |
| --- | --- | --- |
| Whole-octet binary | C095 checked Bytes, or checked UTF-8 Text with its declared meaning. | Immutable data observations and type-directed comparison; no physical buffer identity or native reflection. |
| Native map | C095 closed structural record with explicit labels and recursively checked fields. | Structural data meaning; no arbitrary host-key domain or automatic nominal collection identity. |
| Local PID | A registered borrowed send-authority role with an explicit mailbox codec supplied by trusted setup. Retained Catena process/managed-process types keep their existing owners. | No equality, ordering or raw-PID reflection. Only checked send authority transfers between callers. |
| Reference | A fresh correlation reference created by scope setup and wrapped in a registered owner-scoped role. | No language equality, ordering, reflection or transfer. Only a matching explicitly granted host argument can unwrap it. |
| Host fun | Only the P096 verified compiled callback profile is admitted at its existing typed boundary. | Scope-owned invocation authority; no generic raw fun codec, equality or reflection. |
| Port | Excluded from this profile, whether open or closed. | No role, transfer or comparison permission is inferred from a port term. G098 owns executable port service, scheduler, package and cleanup admission. |

## Immutable data mappings

Binary and map admission retains the
[C095 checks](../erlang-type-boundary/typed-conversion-and-preservation.md#trusted-descriptions-and-admitted-meanings).
Bytes preserves every octet, Text refuses malformed UTF-8 without repair or
normalization, and records require their exact closed field set. Unsupported
map keys, missing/extra fields and partial-octet bitstrings are refused.
A native map cannot select the type against which it is checked.

Whole input/output node, byte and depth bounds apply before success. Large
binaries are accepted when they fit those bounds and refused when they do not;
copying or sharing a buffer supplies no additional semantic observation.
Nominal collection encodings remain governed by the selected C095 descriptor,
not by resemblance to a native map (`NV-OBL-002`).

## Registered role authority

Trusted scope setup supplies a finite ordered grant list. A process grant includes
a local PID and explicit mailbox codec. A reference grant requests a fresh
reference; an arbitrary incoming reference is not accepted as that request.
Raw ports, raw host funs, remote PIDs and unknown grant forms are refused.
The trusted external mailbox declaration is an assertion about the receiver's
intended interface. The adapter proves the type of its own outgoing payloads;
it does not prove the behavior of arbitrary native senders or receivers.

Each grant is stored in the scope manager with a fresh token. The owner obtains
an opaque handle by grant index. The handle carries the role but not the raw
native value. Its role description is reconstructed exactly. A changed token,
role, scope or mailbox description is not authority. Every operation checks the
handle against the live registry before unwrapping it (`NV-OBL-003`).

A matching `0.1.62` host declaration can accept a native-role argument. It requires
the exact registered role and the same owning scope; a PID/reference appearing
where a handle was expected is refused. Host results still use checked C095 data
codecs. This profile does not implicitly adopt raw native results into new roles.
Explicit host calls retain the visible foreign effect, trust and cancellation
rules of the [P096 adapter contract](../foreign-adapters/authority-calls-and-callback-lifetime.md#explicit-declarations-and-authority).

## Borrowed local process send role

The process role denotes checked send authority, not ownership of the target
process. Each send checks and encodes the semantic message through the mailbox
codec, then returns Unit. Native ingress cannot change that codec. A send to an
already dead process still returns Unit and never acknowledges liveness or
delivery, preserving the [C010 send contract](../formal-semantic-kernel/actors-messages-and-failures.md#send).

A holder in another process can use the transferred handle for checked sends
through its original live manager. It cannot use that handle to obtain scope
control, issue arbitrary host calls or transplant the native value into a
different scope's registry. Sends are recorded in manager receive order;
sequential sends by one caller preserve that caller's order. No node query,
raw PID extraction, receiver shutdown or liveness query is introduced
(`NV-OBL-004`).

## Fresh correlation-reference role

Scope setup creates the reference and retains its raw identity in the registry.
The owner can pass its handle only to a granted host parameter declaring that
exact reference role. Different scopes cannot substitute their handles. A
reference role does not support sends, transfer of send authority, equality,
ordering or reflection. Invoking a process-role operation on it is an explicit
refusal, not a successful return containing its raw reference (`NV-OBL-005`).

A trusted host implementation can use the received reference for its declared
correlation work. This does not create a pure language equality operation or
permission for other code to reflect on the reference. The scope ends the
Catena handle's validity; it does not claim that physical native copies already
held by trusted host code can be erased from that host's memory.

## Functions and ports

The [P096 callback profile](../foreign-adapters/authority-calls-and-callback-lifetime.md#scoped-compiled-callbacks)
is the admitted fun role: verified pure Catena code, checked data captures,
explicit callback authority, registered lifetime, overlap refusal and typed
input/output. An arbitrary native fun has no generic data or native-grant
admission. Further effectful or resource-capturing callbacks retain P096's
remaining gate (`NV-OBL-006`).

A raw open port and an already closed port are both refused. Port-shaped input
cannot grant access to an external process or file descriptor, and closure does
not turn a port into ordinary data. This exclusion is deliberate until G098
supplies its separate packaging, scheduler, trust and mandatory cleanup contract;
it does not prohibit that later separately versioned service (`NV-OBL-007`).

## Value, equality and transport checking

The ordinary value-shape classifier recognizes an opaque native-handle form;
that classification is not a registry-membership or authority proof. All
native operations still require the live registered handle. Native handles are
outside the comparable and orderable sets. Explicit role-operation checking
rejects equality and reflection, admits send/transfer-send only for the process
role, and admits owner-scoped host argument conversion only for the corresponding
role. A forged description with an equality flag does not change these rules.

These role judgments live at the explicit sidecar boundary. They do not make
an arbitrary native-handle annotation valid in retained kernel source or widen
that source's historical sendable-type grammar. No ordinary data codec admits
the opaque handle as a structural substitute (`NV-OBL-008`).

## Lifetime and limits

Grant count is at most the positive operation maximum supplied to the scope,
default 1,024. Each native send consumes one operation slot, shared with foreign
calls and callback invocations; exhaustion refuses further admission. The
immutable data bounds, callback-registration bound, wait rules and bounded
release grace retain the P096/C095 contracts.

Scope exit expires all registered native handles and uses P096/C080 cleanup for
owned call/callback workers. It does not kill a borrowed target PID. Subsequent
native sends and host calls through escaped handles fail at the expired scope.
Reference and process tokens confer no authority after their registry ends.
No wrapper comparison can be used as a substitute for this lifetime check
(`NV-OBL-009`).

## Variability register

The conversion, operation, grant-count and release bounds are explicit inputs.
The registered send role preserves the stated event-order and dead-target
behavior. No hidden liveness test, pointer-equality rule or implicit native
conversion is permitted. Allocation and generated-code limits retain the
standing implementation-limit policy.

## Rationale and evidence (non-normative)

The [implementation journal](../../50-journal/2026-09-09-native-value-roles.md)
records four alternatives per decision and executable witnesses for actual local
PID sends, cross-process send authority, fresh-reference host arguments,
forgery/role/equality rejection, dead processes, large binaries, malformed maps,
and live/closed port exclusion. Existing C095/P096 witnesses supply the retained
data and compiled-callback relations. Native identity is useful only through
its declared effectful role; it is not a new observation available to pure
categorical laws.
