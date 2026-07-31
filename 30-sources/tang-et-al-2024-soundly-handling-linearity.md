---
title: "Soundly Handling Linearity"
kind: source
created: "2026-07-31"
authors:
  - "Wenhao Tang"
  - "Daniel Hillerström"
  - "Sam Lindley"
  - "J. Garrett Morris"
published: 2024
citation_key: "tangEtAl2024HandlingLinearity"
container: "Proceedings of the ACM on Programming Languages 8(POPL), Article 54: 1600–1628"
edition: null
isbn: null
doi: "10.1145/3632896"
url: "https://www.research.ed.ac.uk/en/publications/soundly-handling-linearity/"
accessed: "2026-07-31"
tags:
  - effect-handlers
  - linear-types
  - resumptions
aliases:
  - "Control-flow linearity for handlers"
---

# Soundly Handling Linearity

## Reference

Wenhao Tang, Daniel Hillerström, Sam Lindley, and J. Garrett Morris, “Soundly
Handling Linearity,” *Proceedings of the ACM on Programming Languages* 8
(POPL 2024), Article 54, 1600–1628.
[DOI](https://doi.org/10.1145/3632896),
[open-access paper](https://www.research.ed.ac.uk/files/407801113/Soundly_Handling_TANG_DOA07112023_VOR_CC_BY.pdf),
and [official bibliographic record](https://www.research.ed.ac.uk/en/publications/soundly-handling-linearity/).

## Research question

How can multi-shot effect handlers coexist soundly with linear values when a
handler may discard or duplicate a continuation containing those values?

## Method

The authors exhibit a soundness bug in Links involving linear session
resources and multi-shot handlers. They introduce control-flow linearity,
formalize it first in a System F-style calculus with linear types and then in an
ML-style qualified-type calculus, prove that the semantics preserves linear
resource integrity, and adapt Links to implement the design. The ML-style
system infers linearity and effect constraints.

## Findings

- Conventional linear type systems often assume continuation use is exactly
  once, while effect handlers can discard a continuation for exceptions or
  invoke it repeatedly for backtracking.
- Value linearity alone therefore does not protect a linear resource captured
  in a resumption.
- The documented Links counterexample is a concrete soundness failure, not
  merely an optimization concern.
- Control-flow linearity tracks how continuations may be used and relates that
  use to the linearity of captured values, ruling out discard or duplication
  when it would violate resource integrity.
- The qualified-type calculus demonstrates that a fine-grained control-flow
  discipline can be inferred rather than requiring annotations on every
  handler.
- Multi-shot handling and linear resources are not inherently incompatible,
  but their combination requires a richer static account than ordinary effect
  rows.

## Relevance

This source explains why Catena's effect row cannot by itself justify
multi-shot resumptions. It supports an affine initial design and supplies a
credible future route: add explicit or inferred control-flow multiplicity only
when Catena is ready to connect it to captured resource types.

## Limits

The proposed calculi and Links implementation are considerably richer than a
minimal HM effect-row system. The paper establishes resource integrity for its
formal semantics, not cleanup, FFI behavior, cancellation, performance, or
abstraction safety for Catena's proposed lexical capabilities.

## Derived work

- [Algebraic Effects and Handlers](../20-notes/algebraic-effects-and-handlers.md)
- [A Greenfield Type System for Catena](../20-notes/catena-greenfield-type-system.md)
- [Which Algebraic-Effect Semantics Should Catena Adopt?](../40-inquiries/which-algebraic-effect-semantics-should-catena-adopt.md)
- [Algebraic Effects and Handlers map](../10-maps/algebraic-effects-and-handlers.md)
