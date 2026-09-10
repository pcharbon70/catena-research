---
title: "Erlang/OTP 29 Distribution Security and External Terms"
kind: source
created: "2026-09-10"
tags: [beam, concurrency, distribution, security]
aliases: []
authors: ["Ericsson AB"]
published: "2026"
url: "https://www.erlang.org/doc/apps/ssl/ssl_distribution.html"
accessed: "2026-09-10"
---

# Erlang/OTP 29 Distribution Security and External Terms

## Reference

Ericsson AB. *Erlang/OTP 29.0.6 documentation*: [Erlang Distribution over
TLS](https://www.erlang.org/doc/apps/ssl/ssl_distribution.html),
[Distribution Protocol](https://www.erlang.org/doc/apps/erts/erl_dist_protocol.html),
[`binary_to_term/2` and `term_to_binary/2`](https://www.erlang.org/doc/apps/erts/erlang.html),
and the [`ssl` reference](https://www.erlang.org/doc/apps/ssl/ssl.html).
Accessed 2026-09-10.

## Research question

Which OTP guarantees can support Catena's first remote transport, and which
application-level checks remain necessary?

## Findings

The native distribution protocol describes connection setup, node-name
exchange, cookie authentication, and connected operation, but explicitly says
the protocol is not secure by itself. OTP supplies TLS distribution as a bearer;
its guidance recommends server peer verification and rejecting a missing client
certificate. TLS therefore supports encrypted mutual authentication when
configured correctly, while Catena still needs its own service, package, schema,
and protocol authorization.

OTP's safe external-term decoder prevents selected runtime-resource attacks,
including creation of new atoms and external function references. The same
documentation warns that host-safe decoding does not establish application
safety and calls for application validation. Deterministic external-term
encoding is guaranteed only within one OTP major release. These constraints
support a closed schema-directed Catena encoding instead of treating arbitrary
BEAM terms or ETF bytes as a portable typed wire contract.

## Relevance

The findings ground C091's mutual-TLS carrier, application greeting, exact
protocol identity, and rejection of unrestricted external-term admission. The
transport uses OTP's supported SSL API while keeping Catena's semantic wire
format independent of native distribution and OTP-major encoding drift.

## Limits

The documentation specifies runtime interfaces and operational warnings; it
does not prove Catena's protocol, certificate operations, availability, or
partition behavior. A loopback TLS test cannot reproduce every network,
certificate-authority, resolver, operating-system, or cryptographic failure.

## Derived work

- [Typed Authenticated Transport](../60-specification/distribution/typed-authenticated-transport.md)
- [Distribution implementation journal](../50-journal/2026-09-10-distribution.md)
- [Formal Semantic Kernel map](../10-maps/formal-semantic-kernel.md)
