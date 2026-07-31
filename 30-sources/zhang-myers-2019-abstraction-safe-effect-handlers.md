---
title: "Abstraction-Safe Effect Handlers via Tunneling"
kind: source
created: "2026-07-31"
authors:
  - "Yizhou Zhang"
  - "Andrew C. Myers"
published: 2019
citation_key: "zhangMyers2019Tunneling"
container: "Proceedings of the ACM on Programming Languages 3(POPL), Article 5: 1–29"
edition: null
isbn: null
doi: "10.1145/3290318"
url: "https://popl19.sigplan.org/details/POPL-2019-Research-Papers/92/Abstraction-Safe-Effect-Handlers-via-Tunneling"
accessed: "2026-07-31"
tags:
  - abstraction
  - algebraic-effects
  - effect-handlers
aliases:
  - "Tunneling effect handlers"
---

# Abstraction-Safe Effect Handlers via Tunneling

## Reference

Yizhou Zhang and Andrew C. Myers, “Abstraction-Safe Effect Handlers via
Tunneling,” *Proceedings of the ACM on Programming Languages* 3 (POPL 2019),
Article 5, 1–29. [DOI](https://doi.org/10.1145/3290318) and
[official conference record](https://popl19.sigplan.org/details/POPL-2019-Research-Papers/92/Abstraction-Safe-Effect-Handlers-via-Tunneling).

## Research question

Can a statically typed handler language guarantee both that effects are
handled and that higher-order effect-polymorphic abstractions cannot
accidentally intercept effects originating in their clients?

## Method

The paper constructs examples where conventional handler lookup distinguishes
implementations that should be abstractly equivalent. It proposes tunneling
semantics that statically resolve handler awareness, develops a typed language
around that semantics, and uses a logical-relations model connected to
contextual equivalence to prove abstraction properties.

## Findings

- Ordinary type safety and effect safety do not imply abstraction safety. A
  higher-order procedure may install a handler whose label also matches an
  effect raised by an unknown callback.
- If that callback effect is handled merely by dynamic nesting, a client can
  distinguish implementations of the higher-order abstraction that should
  otherwise be equivalent.
- Tunneling lets effects pass through code polymorphic in and unaware of them;
  only code with static authority for an effect can select its handler.
- The type system still guarantees handling while the logical-relations result
  supports stronger modular reasoning and contextual equivalences.
- Handler selection is therefore part of the abstraction model, not merely a
  runtime search optimization.

## Relevance

This paper supplies the strongest reason for Catena not to define handler
selection solely as “the nearest matching label.” A greenfield language can
choose lexical capabilities, tunneling, or an equivalent static elaboration,
but it should demand the same higher-order test: effect-polymorphic code must
not acquire interception authority from accidental nesting.

## Limits

The proposed language has its own handler-passing and typing design. The paper
does not establish that lexical instances plus duplicate-label rows have the
same abstraction theorem, nor does it settle one-shot control, scoped effects,
or native compilation. Catena must reproduce the critical examples in its own
calculus.

## Derived work

- [Algebraic Effects and Handlers](../20-notes/algebraic-effects-and-handlers.md)
- [Which Algebraic-Effect Semantics Should Catena Adopt?](../40-inquiries/which-algebraic-effect-semantics-should-catena-adopt.md)
- [Algebraic Effects and Handlers map](../10-maps/algebraic-effects-and-handlers.md)
