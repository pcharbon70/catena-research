---
title: "A Syntactic Approach to Type Soundness"
kind: source
created: "2026-08-06"
authors:
  - "Andrew K. Wright"
  - "Matthias Felleisen"
published: 1994
citation_key: "wrightFelleisen1994syntacticSoundness"
container: "Information and Computation 115(1)"
edition: null
isbn: null
doi: "10.1006/inco.1994.1093"
url: "https://doi.org/10.1006/inco.1994.1093"
accessed: "2026-08-06"
tags:
  - formal-semantics
  - type-safety
aliases:
  - "Syntactic type soundness"
---

# A Syntactic Approach to Type Soundness

## Reference

Andrew K. Wright and Matthias Felleisen. “A Syntactic Approach to Type
Soundness.” *Information and Computation* 115, no. 1 (1994): 38–94.
[DOI](https://doi.org/10.1006/inco.1994.1093).

## Contribution

The paper develops a rewriting-based method for language type soundness,
centering subject reduction and the classification of well-typed program
states rather than relying on a denotational model.

## Findings

Progress and preservation obligations expose missing runtime states and
unsafe interactions when a language is extended with effects such as state or
control. The canonical-forms and substitution lemmas are part of the actual
soundness burden.

## Relevance

C010 names sequential and global preservation, progress classification,
mailbox preservation, and handler safety rather than using “sound” as an
unexpanded aspiration.

## Limits

The paper does not supply a typed actor calculus, row solvers, algebraic
handlers, or a differential backend proof. Catena's global quiescence case is
an explicit extension of the proof shape.

## Derived work

- [Formal Semantic Kernel Metatheory](../60-specification/formal-semantic-kernel/metatheory.md)
- [Formal Semantic Kernel map](../10-maps/formal-semantic-kernel.md)
