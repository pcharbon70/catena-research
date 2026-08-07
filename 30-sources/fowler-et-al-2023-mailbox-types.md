---
title: "Special Delivery: Programming with Mailbox Types"
kind: source
created: "2026-08-06"
authors:
  - "Simon Fowler"
  - "Duncan Paul Attard"
  - "Franciszek Sowul"
  - "Simon J. Gay"
  - "Phil Trinder"
published: 2023
citation_key: "fowlerEtAl2023specialDelivery"
container: "Proceedings of the ACM on Programming Languages 7 (ICFP)"
edition: null
isbn: null
doi: "10.1145/3607832"
url: "https://eprints.gla.ac.uk/298712/"
accessed: "2026-08-06"
tags:
  - actors
  - concurrency
  - type-systems
aliases:
  - "Pat mailbox types"
---

# Special Delivery: Programming with Mailbox Types

## Reference

Simon Fowler, Duncan Paul Attard, Franciszek Sowul, Simon J. Gay, and Phil
Trinder. “Special Delivery: Programming with Mailbox Types.” *Proceedings of
the ACM on Programming Languages* 7, ICFP (2023), article 191.
[DOI](https://doi.org/10.1145/3607832).

## Contribution

The paper presents Pat, a programming language and algorithmic type system in
which behavioral mailbox types describe accepted message combinations for
asynchronous selective receive.

## Findings

Mailbox typing can express substantially more than a union of possible
messages, including constraints on mailbox contents and receive behavior. That
power requires a dedicated algebra, algorithm, and programming model.

## Relevance

The evidence helps bound C010 honestly. `Process M` guarantees message type
only; it does not claim behavioral protocol progress, deadlock freedom, or the
mailbox expressions provided by Pat.

## Limits

Pat is not a direct model of Catena's lexical effects, first-order process
entries, or exact BEAM lowering. Its stronger type system is a comparison, not
an implementation dependency.

## Derived work

- [Catena's Formal Semantic Kernel](../20-notes/catena-formal-semantic-kernel.md)
- [Formal Semantic Kernel map](../10-maps/formal-semantic-kernel.md)
