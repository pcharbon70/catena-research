---
title: "2026-09-10 Distribution"
kind: journal
created: "2026-09-10"
tags: [specification, concurrency, distribution, security]
aliases: []
---

# 2026-09-10 Distribution

## Scope

Execute [G091](../20-notes/language-completion-plan-semantics.md#item-091-distribution-g091)
from compiler C129 merge `af912f4282031e0c52041fd08a5e5ec6be6d0e09`.
Revision `0.1.76` is covered by the user's session-wide approval. CP-091-1..7
retain their recommended selections.
Compiler PR [158](https://github.com/pcharbon70/catena/pull/158) merged feature
commit `79eac2d3f888ab0aa55d44e039e44a227ee0f504` as
`c04d047edcee4aa62e4f3028bb85f31fbd6e50a3` into `rewrite`.

## Implementation decisions

Each implementation fork compares four alternatives and selects the
recommendation.

| Decision | Four alternatives | Recommended and selected |
| --- | --- | --- |
| DS-I01 Carrier | A native Erlang distribution; B mutually authenticated TLS 1.3 socket; C plaintext TCP; D mandatory external broker | B: a narrow TLS carrier supplies confidentiality and peer certificates without importing host-term semantics or universal infrastructure. |
| DS-I02 Identity | A host/PID; B DNS name alone; C opaque node plus service, package and protocol digests; D certificate subject alone | C: semantic and deployment identities stay explicit and independently checked. |
| DS-I03 Certificate policy | A CA validity only; B cookie only; C exact configured SHA-256 fingerprint after chain validation; D trust first seen | C: an accepted chain cannot silently authorize a different Catena service. |
| DS-I04 Handshake completion | A one-sided greeting; B TLS completion alone; C mutual greeting plus ready acknowledgement; D first application message | C: neither endpoint reports success while the peer is refusing application authorization. |
| DS-I05 Wire format | A ETF; B generated binary protocol; C canonical JSON with tagged schema-directed values; D language source text | C: existing canonical machinery gives exact inspectable bytes while retaining a replaceable artifact boundary. |
| DS-I06 Numeric encoding | A JSON numbers; B decimal for every number; C decimal integers and exact binary64-bit float hex; D host textual inspection | C: large integers remain exact and every admitted finite float preserves its bits. |
| DS-I07 Payload domain | A arbitrary host terms; B all Catena runtime values; C closed C087 data schemas only; D bytes only | C: tuples, records, variants and nominal data cross while authority-bearing and executable values remain excluded. |
| DS-I08 Decoder posture | A parse then ignore extras; B host-safe ETF; C bounded exact schema plus canonical re-encoding; D deserialize dynamically then type-test | C: unknown fields, alternate spellings, smuggling and resource amplification are refused before delivery. |
| DS-I09 Frame bounds | A unbounded; B resident-memory limit; C exact bytes, nodes, depth and integer digits; D timeout only | C: deterministic dimensions support portable refusal without pretending to reserve physical memory. |
| DS-I10 Pending capacity | A unbounded; B silent drop; C explicit finite pending count with overload; D blocking wait | C: callers observe pressure before a transmission claim and retain control of retry policy. |
| DS-I11 Delivery states | A success/failure boolean; B exactly-once; C not-enqueued, in-flight uncertainty and admitted; D local dead-target discard | C: the result states the strongest fact supported at each connection boundary. |
| DS-I12 Acknowledgement | A processing complete; B remote frame admitted; C socket write complete; D no acknowledgement | B: admission is useful and testable without claiming that user code ran or committed effects. |
| DS-I13 Duplicate policy | A redeliver every retry; B message ID alone wins; C ID plus frame digest suppresses exact and rejects conflicting duplicates; D global sequence | C: stable application identities prevent accidental double delivery and expose identity reuse with changed meaning. |
| DS-I14 Reconnect | A resume prior authorization; B reauthenticate and clear connection-local pending state; C retry every uncertain frame; D permanently fail endpoint | B: changed certificates or policies apply and every unresolved old transmission receives an explicit outcome. |
| DS-I15 Version skew | A accept matching names; B dynamically widen; C exact protocol/package/distribution identities; D use OTP release alone | C: an explicit adapter is required rather than guessing compatibility from representation. |
| DS-I16 Evidence | A healthy unit test only; B random stress only; C pure failure model plus real mutual-TLS logical endpoints; D production deployment anecdote | C: deterministic failure cases and an actual encrypted socket jointly test the selected boundary without overstating proof. |

## Verification route

Exercise exact authorization and forged fingerprint, service and package cases;
canonical round trips and malformed, unknown, noncanonical, oversized and
foreign payloads; closed nominal data; disconnected, overloaded, prepared,
in-flight, acknowledged and reconnect transitions; exact and conflicting
duplicates; protocol-version skew; mutual TLS exchange; application refusal
after successful certificate-chain validation; profile and lifecycle discovery.

## Results

The compiler adds an explicit distribution contract, canonical typed codec,
bounded transition model, and mutually authenticated TLS 1.3 adapter. Nine
focused distribution tests pass as part of 1,047 compiler tests. Production
compilation with warnings as errors, escript construction, and the reviewed
trust-boundary audit pass. The
[normative contract](../60-specification/distribution/typed-authenticated-transport.md)
promotes G091 to C091.

The real transport fixture uses two separately certified logical nodes over a
loopback connection. The pure model supplies reproducible partition and
reconnect transitions. Residual network, key-custody, certificate-authority,
resolver, OS, and cryptographic trust remain disclosed.
