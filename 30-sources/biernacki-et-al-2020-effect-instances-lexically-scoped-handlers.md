---
title: "Binders by Day, Labels by Night: Effect Instances via Lexically Scoped Handlers"
kind: source
created: "2026-07-31"
authors:
  - "Dariusz Biernacki"
  - "Maciej Piróg"
  - "Piotr Polesiuk"
  - "Filip Sieczkowski"
published: 2020
citation_key: "biernackiEtAl2020EffectInstances"
container: "Proceedings of the ACM on Programming Languages 4(POPL), Article 48: 1–29"
edition: null
isbn: null
doi: "10.1145/3371116"
url: "https://maciejpirog.github.io/papers/binders-labels.pdf"
accessed: "2026-07-31"
tags:
  - algebraic-effects
  - effect-handlers
  - effect-instances
aliases:
  - "Binders by Day, Labels by Night"
  - "Lexically scoped effect instances"
---

# Binders by Day, Labels by Night: Effect Instances via Lexically Scoped Handlers

## Reference

Dariusz Biernacki, Maciej Piróg, Piotr Polesiuk, and Filip Sieczkowski,
“Binders by Day, Labels by Night: Effect Instances via Lexically Scoped
Handlers,” *Proceedings of the ACM on Programming Languages* 4 (POPL 2020),
Article 48, 1–29. [DOI](https://doi.org/10.1145/3371116) and
[author manuscript](https://maciejpirog.github.io/papers/binders-labels.pdf).

## Research question

How can a statically typed direct-style language distinguish multiple uses of
the same effect signature—such as two mutable cells—without letting dynamic
handler nesting choose their identity implicitly?

## Method

The authors model an effect instance as a lexically scoped variable bound by a
handler and tracked in types and effects. They define a core calculus, compare
open and generative operational semantics, prove key equivalence and safety
properties using Kripke-style logical relations, mechanize core results in Coq,
and present an experimental surface language.

## Findings

- A signature such as `State s` is insufficient to distinguish two cells of
  the same state type. Selecting the innermost matching handler makes identity
  depend on nesting.
- Lexically named instances let operations and handlers agree on one use of an
  effect, and let the type-and-effect system track that name.
- Instance names behave as binders in source reasoning and can be represented
  by generated labels at runtime, motivating the paper's title.
- The interaction with polymorphism is delicate: effectful values and
  polymorphic operation signatures can let instance identities escape or
  re-enter scopes in unsound ways if the semantics is chosen naively.
- The paper compares open reduction under instance binders with a generative
  semantics and identifies conditions under which well-typed programs agree.
- The formal and mechanized development is evidence that instance allocation
  is a semantic and type-system problem, not just a runtime tagging trick.

## Relevance

This source motivates Catena's provisional separation between nominal effect
signatures and lexically scoped effect capabilities. It also identifies the
proof burden hidden by attractive syntax: inference and polymorphism must not
smuggle a local capability out of its handler.

## Limits

The calculus makes particular restrictions, including around polymorphic
signatures, to obtain its results. It does not directly combine Koka-style
duplicate effect rows, Catena's proposed affine resumptions, scoped
higher-order effects, or a native runtime. Its surface language is a
demonstration, not a usability study.

## Derived work

- [Algebraic Effects and Handlers](../20-notes/algebraic-effects-and-handlers.md)
- [A Greenfield Type System for Catena](../20-notes/catena-greenfield-type-system.md)
- [Which Algebraic-Effect Semantics Should Catena Adopt?](../40-inquiries/which-algebraic-effect-semantics-should-catena-adopt.md)
- [Algebraic Effects and Handlers map](../10-maps/algebraic-effects-and-handlers.md)
