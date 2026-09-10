---
title: "Typed Authenticated Transport"
kind: specification
created: "2026-09-10"
status: normative
spec_version: "0.1.76"
tags: [specification, concurrency, distribution, security]
aliases: []
---

# Typed Authenticated Transport

## Status and authority

C091 defines revision `0.1.76` under [authority](../../SPECIFICATION-AUTHORITY.md),
[conformance vocabulary](../../CONFORMANCE-VOCABULARY.md), and
[implementation limits](../../IMPLEMENTATION-LIMITS.md). It executes the
[reviewed distribution plan](../../20-notes/language-completion-plan-semantics.md#item-091-distribution-g091)
without selecting future public source vocabulary (`DS-OBL-001`).

This chapter defines an explicit remote service boundary. A C010 `Process M`
handle remains node-local. Local send, mailbox selection, protocol correlation,
task lifetime, cancellation, supervision, package identity, and foreign-value
admission retain their existing contracts. Hot code replacement remains G092.

## Endpoint and peer identity

A distribution endpoint binds the exact distribution revision, node identity,
service identity, package digest, and C087 local-protocol digest. Node and service
identities are nonempty lowercase identifiers of at most 128 UTF-8 bytes.
Package, protocol, certificate, endpoint, contract, message, and frame digests
use lowercase SHA-256 hexadecimal text (`DS-OBL-002`).

A connection is admitted only when both endpoints present valid certificates
under configured trust roots and each side's peer policy authorizes the exact
certificate digest, node, service, package digest, and protocol digest. A valid
certificate chain alone does not grant Catena service authority. Credentials
and private keys remain provisioned host resources and MUST NOT enter Catena
source, ordinary values, frames, artifacts, diagnostics, or traces
(`DS-OBL-003`).

The peers exchange canonical endpoint greetings after TLS authentication. Both
sides acknowledge successful application authorization before either reports a
connected state. A failed, missing, malformed, stale, or unauthorized greeting
refuses the connection before application traffic (`DS-OBL-004`).

## Transport and framing

The portable transport profile is mutually authenticated TLS 1.3 over a
connection-oriented byte stream with four-byte length framing. A conforming
implementation MUST verify the peer certificate on both client and server and
the server MUST reject an absent client certificate. Plaintext transport and
unauthenticated native distribution do not conform (`DS-OBL-005`).

Each application frame binds its format and revision, sender and receiver node,
sender endpoint digest, service, package digest, protocol digest, protocol role,
monotonic connection-local sequence, caller-supplied message identity, and typed
payload. A complete-frame digest is derived from the canonical bytes. Unknown, missing, duplicate, reordered by
canonical representation, or digest-inconsistent fields are rejected
(`DS-OBL-006`).

Frames use exact canonical JSON bytes. Integers use canonical base-ten text;
finite `Float` values use their exact IEEE 754 binary64 bits in lowercase
hexadecimal; text is valid Unicode text; bytes use canonical Base64; characters
contain exactly one scalar. Tuples, closed records, closed variants, and closed
nominal constructors recurse according to the C087 schema. Records use sorted
field names. A receiver decodes from its previously checked protocol schema and
MUST reject values outside that schema (`DS-OBL-007`).

Processes, functions, resumptions, capabilities, tasks, resource handles,
secrets, arbitrary host terms, references, and unrecognized constructors are
not remote payloads. The transport MUST NOT use unrestricted external-term
decoding as typed admission, including an invocation whose host-level safety
option succeeds (`DS-OBL-008`).

## Limits and refusal

An encoded application frame is at most 1,048,576 bytes, a decoded frame visits
at most 16,384 structural nodes, nesting depth is at most 64, and an integer
encoding is at most 4,096 digits. An endpoint admits at most 64 configured peers.
The exact bounds succeed and the next unit is refused before payload delivery.
Malformed or exhausted ingress produces no partial Catena value
(`DS-OBL-009`).

> **Implementation-defined choice.** A deployment configures connection
> addresses, certificate and trust-root paths, exact peer allowlists, positive
> handshake/receive timeouts, and positive pending-message capacity within the
> published implementation ceiling. An implementation profile identifies those
> choices, the supported transport adapters, all wire limits, and their
> measurement units (`DS-OBL-010`).

## Delivery and partition semantics

Preparing remote work while disconnected returns `not_enqueued`. Preparing
while connected reserves one bounded pending slot and produces a stable token
and frame. Capacity exhaustion returns `overloaded` without transmitting,
discarding, or reporting success for that work (`DS-OBL-011`).

Before transport transmission, disconnect maps each prepared token to
`not_enqueued`. After transmission and before remote-admission acknowledgement,
disconnect maps each in-flight token to `delivery_unknown`. An acknowledgement
means only that the authenticated receiver admitted the frame; it does not mean
that application code started, completed, committed an effect, or replied
(`DS-OBL-012`).

The transport performs no automatic application retry and makes no exactly-once
processing claim. A caller that retries supplies and retains the message
identity and selects its application policy. A receiver delivers the first
valid frame for a message identity, suppresses an exact duplicate, and rejects
the same identity paired with a different frame digest as a conflicting
duplicate (`DS-OBL-013`).

A partition or connection loss clears connection-local pending state after
returning its exact outcomes. Reconnection repeats certificate and application
authorization and starts a new admitted connection. No session remains
authorized merely because an earlier connection succeeded; changing peer
policy or package/protocol identity therefore takes effect on reconnect
(`DS-OBL-014`).

## Compatibility and ordering

The handshake requires an exact local-protocol digest, distribution revision,
service, and package identity. Version skew is refused before application
messages rather than widened through runtime guessing. Compatible evolution
requires an explicitly checked C028/C087 adapter and a distinct bound endpoint
identity (`DS-OBL-015`).

The connection-local sequence supplies deterministic sender-order evidence; it
does not by itself detect loss or create cross-connection global order. C010 per-sender FIFO
continues only after a receiver admits frames into one local sender path. The
transport adds no fairness, synchronized-clock, failure-detector completeness,
total-order broadcast, consensus, or distributed transaction guarantee.

## Diagnostics and conformance

The machine-readable profile MUST disclose the distribution contract and wire
revision, TLS version, peer-verification rule, framing, bounds, delivery
outcomes, duplicate policy, automatic-retry status, exactly-once status, and
processing-acknowledgement status. Conformance tests MUST cover authenticated
two-endpoint exchange and reconnect; malformed, noncanonical, oversized,
schema-invalid, and authority-bearing payload refusal; certificate, service,
package and protocol mismatch; partition before and after transmission;
overload; exact and conflicting duplicates; and absence of a processing claim
(`DS-OBL-016`).

## Rationale and evidence (non-normative)

The [implementation journal](../../50-journal/2026-09-10-distribution.md)
records the selected implementation forks and 1,047-test compiler run. The
[OTP 29 source note](../../30-sources/erlang-otp-29-distribution-security-and-external-terms.md)
records why transport TLS, application authorization, typed framing, and
application validation are distinct obligations. The executable TLS witness
uses two logical endpoint identities over a real loopback socket; the bounded
state model supplies deterministic partition, reconnect, skew, and duplicate
evidence. Neither witness is a distributed-systems proof.
