---
title: "Explicit Environmental Authority and Closed Launches"
kind: specification
created: "2026-09-09"
status: normative
spec_version: "0.1.68"
tags: [specification, effects, entry-points, conformance]
aliases: []
---

# Explicit Environmental Authority and Closed Launches

## Status and authority

C106 defines edition `0.1`, exact semantic revision `0.1.68`, without previews,
under [authority](../../SPECIFICATION-AUTHORITY.md),
[conformance vocabulary](../../CONFORMANCE-VOCABULARY.md) and
[implementation limits](../../IMPLEMENTATION-LIMITS.md). It executes the
[reviewed environmental plan](../../20-notes/language-completion-plan-delivery.md#item-106-environmental-effects).
This profile admits checked retained kernel trees with closed scalar data and
lexical capability slots. Its internal service labels and entry metadata do not
adopt public vocabulary, launch syntax or automatic imports (`EV-OBL-001`).

## Versioned entry amendment

For this exact profile, the zero-argument rule in C027's
[entry declarations](../entry-points/entry-declarations.md) and the no-injection
rule in C082's [boundary](../top-level-effects/the-top-level-boundary.md#the-boundary)
are replaced by a single explicit, typed environmental-authority parameter to
the generated launch entry. Its parameter contract enumerates required service
roles; its recorded effect row remains empty. The retained source body is an
exported zero-argument definition whose free capability slots are discharged by
this entry's fresh handlers. Every declared operation of each free slot requires
an exact service-family, argument and result contract. Missing, surplus or forged
bindings are invalid before launch (`EV-OBL-002`).

The launcher supplies granted authority data and an owned release scope. The entry
installs handlers from those values before executing its body; no unhandled
request is returned to the launcher or interpreted by a supervisor. Existing
local lexical handlers retain their ordinary scope and precedence. An empty
required-service set launches with an empty bundle. Missing, expired, revoked or
cross-owner required authority refuses entry. A declaration or manifest grants
nothing. Old zero-argument artifacts, manifests and revisions retain their rules.
This is the explicit amendment required by C082's
[door](../top-level-effects/the-top-level-boundary.md#the-door), not an ambient
host interpreter (`EV-OBL-003`).

## Authority transport and attenuation

A service authority is opaque, nominal data bound to a live scope endpoint,
its owner, service, fresh unpredictable nonce and private grant ledger. Validation
checks the whole carrier and ledger identity, not merely its tag. Copying bytes
does not create authority. Launch parameters never contain first-class lexical
capability names or affine resumptions; handler installation creates the lexical
identities under C050's discipline. Ordinary source code has no arbitrary BEAM
term inspection or process-message escape hatch (`EV-OBL-004`).

Each grant lists permitted operations, byte ceiling, lifetime and service-specific
resources. Attenuation preserves the service, root or device identity, selects
subsets of operations/resources and reduces or preserves byte and lifetime bounds.
Endpoint and command entries must remain exact members of the parent map.
A child's absolute expiry never exceeds its parent's. Revoking a grant also
revokes every descendant and interrupts their pending work. A valid but denied,
expired or revoked operation returns that typed failure; malformed or forged
authority and cross-owner access are boundary errors (`EV-OBL-005`).

## Service contracts

Every operation takes one typed argument, using a tuple when several components
are needed. Its result is a closed structural variant: success carries the payload
below; error carries a closed service-specific variant, each reason carrying Unit.
These are ordinary typed values. They neither introduce a universal dynamic type
nor claim C103's nominal outcome representation (`EV-OBL-006`).

| Service and operation | Argument | Successful payload and behavior |
| --- | --- | --- |
| I/O read | Int count | Bytes, at most count, empty at EOF, from the explicitly supplied device |
| I/O write | Bytes | Unit after writing to the supplied device |
| Filesystem read | Text relative path, Int count | Bytes, at most count, from the granted regular file |
| Filesystem write | Text relative path, Bytes | Unit after replacing the file contents; creates a missing leaf |
| Network exchange | Text endpoint alias, Bytes send, Int receive count | Bytes of exactly receive count after sending; zero count skips receiving |
| Time monotonic | Unit | Int nanoseconds from the host monotonic clock; its origin has no calendar meaning |
| Time wall | Unit | Int nanoseconds since the Unix epoch from the host wall clock; adjustments are observable |
| Time sleep | Int milliseconds | Unit after the requested wait, subject to cancellation, deadline and scheduling delay |
| Random bytes | Int count | Exactly count Bytes from the host cryptographic random generator |
| Environment get | Text name | Closed absent(Unit) or present(Bytes) value, only for an explicitly granted name |
| Logging emit | Text level, Text message | Unit after writing one UTF-8 JSON object with level/message and a newline to the supplied device |
| Process run | Text command alias, Bytes standard input | Int exit status and combined standard-output/error Bytes after the approved child finishes |

Each error set contains denied, expired, revoked, cancelled, timeout, limit,
unavailable and invalid_request. I/O and logging add io_failure; filesystem adds
not_found and io_failure; network adds network_failure; process adds not_found and
process_failure. Time, random and environment add nothing. An error from another
service is invalid. Complete C095 input/result codecs and node/byte/depth budgets
apply before admission and before publication, including error payloads. Successful
byte counts and policy output bounds are also validated. Codec or carrier-budget
refusals remain boundary errors, not fabricated service answers (`EV-OBL-007`).

## Filesystem and network confinement

A filesystem policy supplies an absolute root and explicit relative path list.
Paths are nonempty UTF-8 without NUL, backslash, empty components, dot or dot-dot.
The root and each traversed directory are opened without following their final
symlink; children are opened relative to the already-open parent descriptor.
The leaf is opened without symlink following and accepted only as a regular file
with one link. Write truncation occurs only after this check. Parent directories
are not created. Read and write counts obey the grant's byte ceiling. Acquired
file descriptors are closed on return or failure (`EV-OBL-008`).

This is an explicit path-operation boundary over external filesystem state,
not a snapshot of that state. Root path ancestors and approved roots are host
provisioning responsibilities; a hostile host can replace files or change links.
No guarantee of atomic replacement, rollback, durability, whole-path mount
confinement or immunity to concurrent privileged filesystem mutation is implied.

Network grants map aliases to exact numeric IPv4/IPv6 address and port pairs.
The adapter performs one passive raw TCP connection, send and bounded receive;
it closes the owned socket. It performs no DNS lookup, redirect, discovery or
TLS negotiation. There is no endpoint widening through alias substitution.
External peers and network timing are environmental inputs (`EV-OBL-009`).

## Host process and device ownership

Process grants bind an alias to an absolute executable, exact argument vector,
absolute working directory and complete explicit environment. No caller-supplied
shell command, inherited environment or implicit executable lookup is used for
the target. Each invocation copies a bounded regular executable opened without
following its final symlink to a private executable snapshot. This pins that
launch's bytes, not the executable's dependencies or future launches.

The helper launches the approved program in a fresh POSIX session, owns its pipes,
bounds captured output and on every exit path kills its process group and waits
for the direct child. The host approves trusted programs that stay within that
group. Deliberately detached descendants, executable interpreters/dependencies and
host filesystem authority remain trusted-host concerns; this service is not an
OS sandbox (`EV-OBL-010`).

Supplied I/O/logging devices are borrowed and remain owned by their provider.
Cancellation terminates owned request workers, sockets and helper lifetimes;
it does not close those borrowed devices. Reads can consume input and writes,
network sends, logging and child actions can have externally visible effects
before a failure or cancellation. No automatic retry or rollback occurs.

## Lifetime, cancellation and shutdown

The scope manager binds calls to its owner and monitors that owner. Each admitted
request consumes one request slot, creates an owned monitored worker and has
one terminal result. Completion is published only after worker termination.
The first manager-observed cancellation or revocation fixes that request's
cancellation reason. Otherwise an elapsed deadline takes precedence over a result
not yet published. The effective deadline is the earlier of the configured
operation timeout and grant expiry; expiry supplies the expired reason.
Repeated await returns the same completed answer; only one pending waiter is
admitted. Cancellation after completion reports already-completed (`EV-OBL-011`).

Return, source trap and owner death close admission and interrupt outstanding
work. Helpers cooperate with cancellation and confirm release before returning
an answer. A forced helper-worker kill, missing helper confirmation or helper
cleanup failure marks release unconfirmed; a live enclosing scope reports an
explicit environment-cleanup failure through C080's
[mandatory cleanup](../resource-scopes/owned-lifetime-and-mandatory-cleanup.md).
It never reports confirmed cleanup merely because the BEAM worker disappeared.
Cancellation is bounded but cannot promise reversal of external effects or
successful OS cleanup under an unresponsive host (`EV-OBL-012`).

## Artifact and manifest boundary

The checked entry sidecar binds the core, exported body, complete operation
bindings, required services, result codec, carrier budgets, service profile,
helper digest, full compiler identity, generated forms and exact BEAM bytes.
Verification rebuilds that artifact. Loading is serialized per module: identical
bytes are reused, conflicting loaded bytes are refused. Compiled execution and
reference execution independently evaluate the source; the latter uses explicit
handler frames and a scripted service model rather than invoking compiled code
(`EV-OBL-013`).

The separate environmental manifest has exactly format, version, entry and
services fields. Its format is catena-environment-entry, version is 0.1.68,
entry is a retained identifier and services is the sorted unique required-service
list. It must agree with the entry sidecar. It conveys requirements only and is
not accepted as a retained package manifest. Authority is supplied separately.
Malformed manifests, unknown services and sidecar mismatches refuse launch setup.
Process declarations, managed-task nodes and effectful foreign callback adoption
are outside this entry-core profile; their separate owners remain unchanged.

## Bounds and costs

The fixed service profile admits at most eight initial grants and 64 total
authorities per scope. Byte ceilings range 0..1,048,576; grant lifetimes and
operation timeouts range 1..1,000,000 milliseconds. Request capacity ranges
1..10,000 (default 1,024), concurrent requests 1..64 (default eight), and operation
timeout defaults to 1,000 milliseconds. Resource lists and argument vectors have
at most 256 entries, endpoint maps 64, command maps 32 and command environments
256 pairs. Nonempty policy text has at most 4,096 UTF-8 bytes; argument/environment
values can be empty. The executable snapshot cap is 16,777,216 bytes. Manifest
input has at most 16,384 bytes (`EV-OBL-014`).

Scripted models have at most the configured request capacity and consume one
matching service/operation/argument/result/delay item per admitted start. Delay
ranges 0..1,000,000 milliseconds. A mismatch or exhausted script returns typed
invalid_request; results still undergo whole-carrier and service checks. Scripts
supply environmental observations, not authority or arbitrary callbacks.

Cooperative worker grace is 1,500 milliseconds and enclosing release grace is
5,000 milliseconds. The implementation publishes all these fixed bounds and the
helper digest through its machine-readable environment profile. The real helper
requires Python 3 on POSIX with directory-relative open, O_DIRECTORY, O_NONBLOCK
and O_NOFOLLOW support; otherwise it returns unavailable. Grant ceilings express
host policy: exceeding requested authority returns denied. Configured request
capacity returns limit; ledger exhaustion returns an authority-limit boundary
error. Fixed schema/profile bounds outside their declared domains are invalid.
Inherited C012 source, generated-code and C095 carrier limits remain applicable.

Ledger retention is proportional to authorities; job and event retention is
proportional to admitted requests. Byte work is proportional to transferred or
encoded data; process launch additionally copies its executable. Validation and
artifact rebuilding cost their complete inputs. No constant-time service,
constant-space unbounded trace, bounded source termination or real-time scheduler
promise is added.

## Variability register

Operation schemas, authority ownership, attenuation, failure sets, profile bounds,
entry closure and retained-revision isolation are fixed. Grants, budgets, timeout,
request capacity, concurrency and scripted observations are explicit inputs.
Real clock/random/device/filesystem/network/process observations are environmental
inputs under the service contracts. Host dependencies and output interleaving are
not implicit language authority or permission to choose different semantics.
All finite bounds, units, defaults and exhaustion classes appear above.

## Rationale and evidence (non-normative)

The [decision journal](../../50-journal/2026-09-09-environmental-effects.md) records
four-way decisions, compiled/reference witnesses and actual adapter experiments.
The [Python OS reading](../../30-sources/python-directory-relative-os-operations.md),
[Python subprocess reading](../../30-sources/python-subprocess-session-ownership.md)
and [OTP TCP reading](../../30-sources/erlang-passive-tcp-sockets.md) support the
host mechanisms, not broader sandbox or rollback claims.
