---
title: "Erlang/OTP 29 Processes"
kind: source
created: "2026-08-06"
authors:
  - "Ericsson AB"
published: "OTP 29"
citation_key: "erlangOtp2026processes"
container: "Erlang/OTP System Documentation"
edition: "29.0.4"
isbn: null
doi: null
url: "https://github.com/erlang/otp/blob/OTP-29.0.4/system/doc/reference_manual/ref_man_processes.md"
accessed: "2026-08-06"
tags:
  - actors
  - beam-vm
  - erlang
aliases:
  - "OTP 29 process semantics"
---

# Erlang/OTP 29 Processes

## Reference

Ericsson AB. “Processes.” *Erlang/OTP System Documentation*, OTP 29.0.4.
[Version-pinned documentation](https://github.com/erlang/otp/blob/OTP-29.0.4/system/doc/reference_manual/ref_man_processes.md),
accessed 2026-08-06.

## Research question

Which local ordering, queue, identity, and failure behaviors may Catena rely on
when lowering its bounded typed process calculus to OTP 29?

## Findings

Erlang processes have identities, isolated execution, asynchronous signals,
mailboxes, and selective receive. Ordinary messages corresponding to signals
from one sender retain signal order. Receive selects the first message from
the queue that matches its clauses. Process links, exit signals, priority
messages, distribution, and other facilities add behavior beyond the local
spawn/send/receive core.

## Relevance

C010 adopts local PIDs, per-sender ordering, and oldest-matching receive while
excluding priority messages, links, monitors, exit trapping, and distribution.
The backend can therefore lower directly without promising the wider OTP
process API as Catena semantics.

## Limits

The documentation defines Erlang and OTP behavior, not Catena typing,
sendability, host effects, interface identities, or proof obligations.

## Derived work

- [Actors, Messages, and Failures](../60-specification/formal-semantic-kernel/actors-messages-and-failures.md)
- [Kernel BEAM, Diagnostics, and Conformance](../60-specification/formal-semantic-kernel/beam-diagnostics-and-conformance.md)
