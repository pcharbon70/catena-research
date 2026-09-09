---
title: "Signed Loading and Owned Native Execution"
kind: specification
created: "2026-09-09"
status: normative
spec_version: "0.1.63"
tags: [specification, foreign-boundary, beam-vm]
aliases: []
---

# Signed Loading and Owned Native Execution

## Status and authority

This C098 contract applies to edition `0.1`, revision `0.1.63`, without
previews, under the [authority policy](../../SPECIFICATION-AUTHORITY.md),
[conformance vocabulary](../../CONFORMANCE-VOCABULARY.md), and
[implementation limits](../../IMPLEMENTATION-LIMITS.md). It completes the
[reviewed native-service gate](../../20-notes/language-completion-plan-delivery.md#item-098-nifs-and-ports).
The initial executable ABI is a unary finite Float service. It introduces no
public source vocabulary and does not widen C097's raw-port admission.

Native packages use their own envelope format `1` and exact language-revision
metadata `0.1.63`. Existing source-executable, Catena artifact, interface and
signed-governance formats retain their prior identities. Parsing native metadata
alone does not confer admission (`NI-OBL-001`).

## Explicit package authority

A package contains exactly its description, payload map, publisher public key
and Ed25519 signature. Admission requires an external policy with exactly:
allowed publisher keys, allowed kinds, a positive maximum payload-byte count,
and acknowledged unsafe obligations. Missing grants, unsigned or changed bytes,
unknown files, extra description fields and unsupported metadata are refused.

The signature covers the canonical JCS description prefixed by the literal
domain `catena:native-package:1` followed by one LF. It binds each exact file's
SHA-256 digest, kind, wrapper module, scheduler, maximum work units, call timeout,
unsafe obligations, the current supported toolchain fingerprint, and the port
guardian digest when applicable. Payload size is the sum of complete binary
file lengths. A ready-package record is reconstructed and compared before use.
No filename, package-supplied key or checksum alone grants execution authority
(`NI-OBL-002`).

A port package contains only `service`; a NIF package contains only
`catena_native_service.beam` and `catena_native_service.so`. Payloads are nonempty.
The wrapper module is fixed to `catena_native_service` for a NIF and absent for
a port. The host matches [C099's support matrix](../otp-compatibility/support-probes-and-artifacts.md#status-and-authority).
The loader writes verified payloads into a fresh private directory, never a
caller-supplied executable path. Port execution uses an argument vector without
a shell. The embedded guardian's digest is part of port admission.

## Scheduling and native trust

The admitted port scheduler is `os_process`. The admitted NIF computational
scheduler is `dirty_cpu`; ordinary-scheduler and dirty-I/O declarations are
refused by this initial profile. A different workload class needs its own
reviewed contract. Each package declares a positive maximum work-unit count at
most 9,007,199,254,740,991 and a timeout of 1 through 4,294,967,295 milliseconds.
A work unit means one complete declared unary service request; its native
implementation and finite work bound are publisher attestations, not a proof
obtained by inspecting machine code. The timeout supplies a separate measured
caller deadline.

Port obligations are bounded work, direct-child-only execution and process
isolation. NIF obligations are bounded work, garbage-collector finalizer fallback,
idempotent close, scheduler correctness and possible VM crash. All require
explicit acknowledgement. Correct scheduler metadata is necessary but cannot
prove that arbitrary C code honestly uses the declared scheduler. The retained
NIF witness checks the actual dirty-CPU thread through `enif_thread_type`.
The wrapper returns a `dirty_cpu` marker with its result; a different marker
is refused, and this marker remains a trusted native assertion (`NI-OBL-003`).

A NIF executes inside the VM's address space. Arbitrary native corruption or
abort can destroy that VM; Catena makes no VM-survival promise. Port service
failure is isolated from the VM address space. The guardian is not an OS
security sandbox: trusted native code can have external effects, and its
no-descendant obligation is not enforced against malicious process escape.
Crash experiments for NIFs run in disposable OS/BEAM subprocesses
(`NI-OBL-004`).

## Typed calls and transport

Input and output use the retained [C095 Float codec](../erlang-type-boundary/typed-conversion-and-preservation.md#trusted-descriptions-and-admitted-meanings)
with exactly one node, eight scalar-payload bytes and depth zero. Int, raw native
handles and non-Float results are refused. Finite binary64 bit patterns,
including negative zero and subnormal values, are preserved. Nonfinite wire
patterns are refused without normalization. Native memory corruption is outside
the documented term-constructor guarantee.

The port protocol has a two-byte big-endian length header and exactly eight
big-endian binary64 payload bytes per request/response. Only one request is
pending; overlapping, oversized, unsolicited or malformed frames cause guardian
failure. The guardian sends a one-byte `R` ready payload and uses a zero-length
owner command for close. A close acknowledgement is the one-byte `C` payload
after child reaping. These control frames cannot be Float results.
The loader requires Python 3 with the standard-library selector/subprocess APIs;
absence is an expected load failure. Startup waits at most 2,000 milliseconds.

The NIF wrapper exports `init_library/1`, `open/0`, `call/2`, and `close/1`.
The signed BEAM module and library are loaded as one payload identity. Identical
loaded payloads can be reused; replacing them in the same VM is refused. The
opened native resource is private to the manager and its bounded call workers.
A successful call returns the scheduler marker and finite Float; host raises,
throws, malformed results and failed loading become explicit failures
(`NI-OBL-005`).

## Deadlines and failure

The guardian starts a monotonic deadline when it forwards a complete request.
Timeout kills and reaps its direct child before exit status 124. Child EOF is
status 125; protocol failure is status 126. A caller waits the declared timeout
plus 1,000 milliseconds for guardian transport completion. Service exit is a
failure, never an implicit retry. A guardian exit observed after its cleanup
confirms direct-child reaping; it does not undo earlier external effects.

NIF open, call and close run in monitored linked workers under the declared
caller timeout. On timeout the worker is terminated and the result explicitly
reports that native work may continue. A dirty NIF can continue after its BEAM
process is logically dead. A timed-out call poisons its scope against additional
calls while still permitting cleanup. Timeout is neither rollback nor proof of
physical native termination (`NI-OBL-006`).

## Owned lifetime and finalization

The scope owner alone can call or close its service. Registered scope equality
is required; arbitrary handles do not confer authority. The release helper has
a separate private token. Escaped scopes fail after the manager terminates.
Owner death terminates the manager and releases its owned transport.

Explicit close is idempotent after confirmed success, and later calls fail.
Mandatory release follows [C080](../resource-scopes/owned-lifetime-and-mandatory-cleanup.md#status-and-authority),
with a supplied nonnegative release grace in nanoseconds, default 2,000,000,000.
A port close is confirmed only by its post-reap acknowledgement followed by
successful guardian exit, within 1,000 milliseconds. Unconfirmed cleanup is a
failure. Closing a pipe alone is not treated as a proof of child termination;
parent EOF causes guardian cleanup as a fallback.

A NIF's explicit close and resource destructor share an idempotent physical
release operation. The destructor supplies host-GC fallback and cannot run
arbitrary Catena effects. It does not replace mandatory lexical cleanup or
promise to run after VM destruction. Resource memory remains valid while a
native call retains it. The signer owns thread-safety and racing-close correctness
for that resource. Owned temporary files are removed at manager termination
(`NI-OBL-007`).

## Variability register

Policy payload bytes, package timeout, work units and release grace are explicit
inputs with the units and ranges above. The initial fixed ABI has no dynamic
wire-allocation budget. Startup and close budgets are fixed as stated. The
supported native host is C099's exact row plus the declared Python 3 guardian
facility for ports; missing tools, native loader incompatibility and allocation
failure refuse setup. Actual native scheduler and finite-work properties remain
explicit trust obligations, never hidden implementation freedom. Unsafe NIF
crash and continuing-work limits are part of the admission contract.

## Diagnostics and conformance

Admission, ownership, Float conversion, native loading, scheduler/result,
service exit, timeout and unconfirmed cleanup each have explicit failure results.
They do not produce a successful typed value. A suite witness covers signed
positive admission and every refusal above, port death/deadline reaping, finite
bit preservation, nonfinite rejection, dirty scheduler execution, double close,
GC fallback, owner death, expired scope authority and isolated NIF VM death
(`NI-OBL-008`).

## Rationale and evidence (non-normative)

The [journal](../../50-journal/2026-09-09-native-services.md) records the decisions,
retained native sources and execution commands. The
[OTP source note](../../30-sources/erlang-otp-nif-float-construction.md) distinguishes
API claims from the pinned local evidence. Effectful native authority does not
supply pure equality, categorical laws or new public language vocabulary.
