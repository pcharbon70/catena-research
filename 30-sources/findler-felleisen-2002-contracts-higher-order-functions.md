---
title: "Contracts for Higher-Order Functions"
kind: source
created: "2026-08-01"
authors:
  - "Robert Bruce Findler"
  - "Matthias Felleisen"
published: 2002
citation_key: "findlerFelleisen2002contracts"
container: "Proceedings of ICFP 2002"
edition: null
isbn: "1-58113-487-8"
doi: "10.1145/581478.581484"
url: "https://users.cs.northwestern.edu/~robby/pubs/papers/ho-contracts-icfp2002.pdf"
accessed: "2026-08-01"
tags:
  - contracts
  - functional-programming
  - language-design
aliases:
  - "Higher-order contracts"
---

# Contracts for Higher-Order Functions

## Reference

Robert Bruce Findler and Matthias Felleisen. “Contracts for Higher-Order
Functions.” In *Proceedings of ICFP 2002*, 48–59.
[DOI](https://doi.org/10.1145/581478.581484).

## Contribution

The paper gives higher-order contracts a language semantics. A function-valued
argument cannot be declared conforming once at the call boundary; it must be
wrapped and monitored when later applied. The calculus tracks positive and
negative obligations so a detected violation can be assigned to the party that
broke its promise.

## Method

The authors define the typed lambda calculus lambda-CON, give a contract
compilation, establish type-soundness and implementation-correspondence
results, and relate the model to examples from a working programming
environment.

## Findings

- First-order predicate checks do not generalize directly to functions because
  future uses, storage, and callbacks delay the point at which a violation
  becomes observable.
- Contract wrappers preserve monitoring through higher-order flows and carry
  enough boundary information for blame assignment.
- Contracts can be first-class values, but their interaction with dependent
  ranges, state, callbacks, and tail recursion requires explicit semantics.

## Relevance

Catena’s specifications will cross module boundaries containing functions,
handlers, and callbacks. This work shows that “check on entry” is unsound as a
general contract model and that diagnostics need a polarity-aware account of
who promised what to whom.

## Limits

Monitoring detects only exercised violations and can add allocation and call
overhead. Arbitrary predicates can diverge or have effects unless the language
restricts them. The calculus does not address signed evidence, organizational
authority, temporal protocols, or distributed execution histories.

## Derived work

- [Language-Integrated Specifications and Governance](../20-notes/language-integrated-specifications-and-governance.md)
- [Language-Integrated Specifications and Governance map](../10-maps/language-integrated-specifications-and-governance.md)
