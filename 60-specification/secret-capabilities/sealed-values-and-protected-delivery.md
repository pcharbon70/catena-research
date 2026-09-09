---
title: "Sealed Values and Protected Delivery"
kind: specification
created: "2026-09-09"
status: normative
spec_version: "0.1.72"
tags: [specification, conformance, security]
aliases: []
---

# Sealed Values and Protected Delivery

## Status and authority

C131 defines exact revision `0.1.72` under [authority](../../SPECIFICATION-AUTHORITY.md),
[conformance vocabulary](../../CONFORMANCE-VOCABULARY.md) and
[implementation limits](../../IMPLEMENTATION-LIMITS.md). It executes the
[reviewed secrets plan](../../20-notes/language-completion-plan-delivery.md#item-131-secrets-and-capabilities).
It admits explicit credential provisioning, sealed operations and checked recipient
delivery. Public vocabulary remains held for co-design. General source and build
adoption remain P109 and P121; existing unprotected host APIs acquire no implicit
secrecy guarantee (`SK-OBL-001`).

## Sealed values

Trusted host setup supplies named credential providers and named approved
recipients. A provider is either an explicit sensitive byte input or an authorized
C106 environment lookup. Retrieval checks the live scope's provider authority.
There is no ambient language environment lookup, compiler credential capture or
public plaintext extraction operation (`SK-OBL-002`).

A language-facing secret reference contains owner, manager and fresh opaque token,
without credential bytes. Only the manager associates that exact reference with
its value. Forged tokens, wrong owners, unknown providers and ungranted recipients
are refused. Host provisioning inputs contain bytes and are outside the ordinary
language value model; trusting their host creator is necessary.

Base64, lowercase hexadecimal encoding, concatenation with another sealed value
or explicit public bytes, and zero-based tuple-element projection produce sealed
references. Growth is checked before byte transformations. Recipient results are
always sealed, including nested structures and results that happen to equal public
values. No automatic declassification, secret-content hash or similarity-based
redaction is defined (`SK-OBL-003`).

## Scope and lineage

Scopes are owner-bound manager identities with explicit provider and recipient
sets, a monotonic deadline, ancestors and revocation state. Attenuation selects
subsets and a deadline no later than the parent. Revocation is monotone; descendants
inherit revoked ancestors. Child revocation does not revoke the parent. Scope
return, owner death and elapsed deadline end authority (`SK-OBL-004`).

Every value retains all originating scopes and provider labels. Derivation in a
parent, delivery through another admitted scope, recipient replies and nested
projection preserve that lineage. Use requires the destination's provider set to
cover all labels and every origin to remain live. Pending work is cancelled when
its scope or any origin expires or is revoked; publication checks these conditions
again. A parent cannot launder a child's secret into an independent lifetime
(`SK-OBL-005`). Revocation cannot undo bytes already delivered to an approved
recipient or erase copies retained by that trusted recipient.

## Checked delivery

A foreign recipient is an exact verified C096/C097 descriptor accepting one Bytes
argument. Its existing result codec verifies the complete result before sealing.
An environmental recipient uses a verified C106 process or network grant. Process
delivery supplies bytes on private stdin to the approved executable snapshot with
explicit argv, environment and working directory. It does not put credentials in
argv, inherited environment or public temporary files (`SK-OBL-006`).

Network delivery admits only an explicitly granted loopback endpoint (IPv4 127/8
or IPv6 ::1) as a local credential broker. Plain remote TCP is refused. Local
broker identity and behavior remain host trust; loopback alone is not peer
authentication. Authenticated remote credential transport requires a separately
admitted contract. Approved foreign/native code, executables and their subsequent
network or filesystem actions remain trusted behavior. These constraints are not
an OS syscall sandbox (`SK-OBL-007`).

The owner, vault, transport workers and sensitive foreign/environment service
managers and workers use OTP sensitive-process observation controls. Managers
redact all status-map values for status and abnormal termination reporting.
Credential-bearing operations have explicit bounded workers. Cancellation requests
the owning adapter's cleanup, suppresses results and waits for worker termination.
A result is published after the worker's normal termination, not merely receipt
of its candidate result. Forced termination or uncertain adapter release produces
an unconfirmed-cleanup failure; it never establishes successful cleanup
(`SK-OBL-008`).

## Public observations and artifacts

Sensitive host inputs and references have redacted inspection and recursive
redaction in diagnostic, report, trace and debugging observations. Throughout a
secret run, diagnostic creation/reporting emits fixed `SEC001` content, without
source paths, spans, details or fixes; trace events become a fixed activity marker.
The prior caller sensitivity and context are restored on exit. Scope audit emits
only operation-category atoms, without payloads, provider names or digests
(`SK-OBL-009`). Activity counts and timing are not hidden.

Scope-body errors, worker failures and exit reasons use closed public failure
labels. Cancellation payloads are redacted. Mandatory release failure reports
unconfirmed secret cleanup, never the underlying credential-bearing exception.
Canonical public JSON/JCS encoding refuses marked secret inputs/references;
assurance construction recursively rejects marked secret inputs before building
public artifact identity. Checked secret program artifacts contain only core,
role bindings, provider/recipient names, profile and compiler identity, never
provisioned values (`SK-OBL-010`). Arbitrary host code that extracts provisioning
bytes and submits them as unmarked public strings violates the trust boundary;
this contract does not implement whole-VM information-flow analysis.

## Compiled entry

The admitted executable entry reuses the checked `0.1.50` capability kernel,
without imports or processes, and exports a zero-argument Unit result. Every
entry effect is an exact capability binding in the internal secret family. Roles
have fixed signatures: fetch, base64 and hex consume one Int and return Int;
deliver consumes two Int values and returns Unit. Provider and recipient indices
refer to the artifact's ordered unique name lists. Secret indices refer only to
a fresh per-invocation private reference table; unallocated indices fail. They
never encode credential bytes (`SK-OBL-011`).

Build verifies core, source arities and integer bounds, lowers the checked entry,
checks generated arities and compiles exact revision `0.1.72`. Verification
rebuilds the entire artifact, including code, bindings, profile and compiler
identity. Invocation checks a live scope and exact loaded module identity. The
private table is removed on all invocation exits. The entry returns Unit only;
recipient replies remain sealed in the vault. These internal roles do not choose
public language vocabulary.

## Limits and exhaustion

The exact profile allows 64 providers and 64 recipients, each name containing
1–128 valid UTF-8 bytes. Setup input has a 1,048,576-byte serialized ceiling.
Provisioned byte inputs and generated byte transformations cap at 65,536 bytes.
A sealed value occupies at most 131,072 serialized bytes; all sealed objects
occupy at most 1,048,576 serialized bytes and 256 objects. Setup and object storage
are separate budgets. Serialization checks occur after serialization, not before
host allocation (`SK-OBL-012`).

There are at most 64 scopes including the root, 1,024 jobs and 8 pending workers.
Derivation nesting starts at depth zero and refuses depth greater than 16. Scope
lifetime is 1–1,000,000 milliseconds, default 10,000. Service timeout is 1,000
milliseconds; the outer worker deadline is 7,000 milliseconds and scope release
bound is 8,000 milliseconds. Environmental adapter values use 10,000 nodes,
131,072 bytes and depth 100. Environmental response requests cap at 65,536 bytes.
Existing adapters own their typed outcomes and cleanup rules.

Invalid setup, denied authority, oversized transformations, full storage and job
or scope exhaustion return explicit refusal, without truncating credentials.
Objects retain their quota until root release even after revocation. Fatal VM/OS
exhaustion and scheduler failure remain outside bounded local progress. The
conformance profile reports these limits and explicitly reports no secure erasure
and no secrecy against a hostile host (`SK-OBL-013`).

## Variability register

This exact profile fixes the supported provider/recipient forms, redaction,
lineage, loopback restriction and numerical ceilings. C106 and the foreign adapter
retain their platform and cleanup responsibilities. No host choice turns static
effect typing into OS isolation or retroactively protects an ordinary host API.

## Rationale and evidence (non-normative)

The [journal](../../50-journal/2026-09-09-secret-capabilities.md) records decisions,
sentinel tests and real compiled/process/network execution. OTP
[sensitive-process controls](../../30-sources/erlang-otp-29-runtime-resource-controls.md)
and [server status redaction](../../30-sources/erlang-otp-29-server-status-redaction.md)
cover complementary observation paths. They do not prevent privileged host state
inspection, malicious admitted native code, secure-memory-copy recovery or
credential exfiltration by an approved recipient. The
[trust graph](../trusted-computing-base/guarantees-assumptions-and-boundary-checks.md)
keeps these residual assumptions explicit.
