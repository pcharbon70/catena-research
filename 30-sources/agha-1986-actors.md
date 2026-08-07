---
title: "Actors: A Model of Concurrent Computation in Distributed Systems"
kind: source
created: "2026-08-06"
authors:
  - "Gul Agha"
published: 1986
citation_key: "agha1986actors"
container: "MIT Press Series in Artificial Intelligence"
edition: null
isbn: "9780262511414"
doi: null
url: "https://mitpress.mit.edu/9780262511414/actors/"
accessed: "2026-08-06"
tags:
  - actors
  - concurrency
  - formal-semantics
aliases:
  - "Agha actors"
---

# Actors: A Model of Concurrent Computation in Distributed Systems

## Reference

Gul Agha. *Actors: A Model of Concurrent Computation in Distributed Systems*.
MIT Press, 1986. ISBN 978-0-262-51141-4.

## Contribution

The book gives syntactic and semantic models for asynchronous actors with
identity, local state, message passing, dynamic creation, and open-system
interaction.

## Findings

Actor identity and asynchronous messages form a concurrency model distinct
from shared-state threads. Dynamic creation and nondeterministic message
arrival require global behavior to be described independently of a single
sequential evaluator.

## Relevance

Catena adopts the small local subset needed for typed BEAM processes: fresh
identity, spawn, asynchronous send, and owned receive. It does not import the
book's distributed or open-system scope into C010.

## Limits

The actor model alone does not determine mailbox typing, Erlang selective
receive, effect rows, failure propagation, or BEAM lowering.

## Derived work

- [Actors, Messages, and Failures](../60-specification/formal-semantic-kernel/actors-messages-and-failures.md)
- [Formal Semantic Kernel map](../10-maps/formal-semantic-kernel.md)
