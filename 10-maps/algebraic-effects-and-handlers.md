---
title: "Algebraic Effects and Handlers"
kind: map
created: "2026-07-31"
tags:
  - algebraic-effects
  - effect-handlers
  - language-design
aliases:
  - "Algebraic effects map"
  - "Effect handlers map"
---

# Algebraic Effects and Handlers

## Scope

This map routes through the mathematical meaning of algebraic operations, the
operational behavior of handlers and resumptions, static effect tracking,
handler identity and abstraction, scoped computations, and realistic compiler
and runtime strategies. It culminates in a greenfield Catena proposal; it does
not inherit semantics from another Catena repository.

## Start here

- [Algebraic Effects and Handlers](../20-notes/algebraic-effects-and-handlers.md)
  is the main synthesis, operational model, design matrix, and provisional
  Catena contract.
- [Which Algebraic-Effect Semantics Should Catena Adopt?](../40-inquiries/which-algebraic-effect-semantics-should-catena-adopt.md)
  turns the unresolved combination of identity, rows, resumptions, resources,
  and compilation into a falsifiable research program.
- [A Greenfield Type System for Catena](../20-notes/catena-greenfield-type-system.md)
  provides the wider inference-first architecture into which effect handlers
  must fit.

## Trails

### Understand why the effects are algebraic

1. [Plotkin and Power 2003](../30-sources/plotkin-power-2003-algebraic-operations-generic-effects.md)
   define the continuation-compatible coherence condition and connect
   algebraic operations to generic effects.
2. [Plotkin and Pretnar 2009](../30-sources/plotkin-pretnar-2009-handlers-algebraic-effects.md)
   treat handlers as models and handling as the homomorphism from a free
   computation.
3. Return to the synthesis's
   [algebraic foundation](../20-notes/algebraic-effects-and-handlers.md#the-algebra-beneath-the-syntax)
   to separate operations from handlers and scoped constructs.

### See handlers as a programming abstraction

1. [Handlers in Action](../30-sources/kammar-et-al-2013-handlers-in-action.md)
   shows open forwarding, partial interpretation, handler order, and several
   implementation encodings.
2. [Koka's row-polymorphic effects](../30-sources/leijen-2014-koka-row-polymorphic-effects.md)
   explains why effect-polymorphic functions need open rows and why duplicate
   labels can preserve principal elimination.
3. The synthesis's
   [operational semantics](../20-notes/algebraic-effects-and-handlers.md#operational-semantics)
   follows one request through handler selection, capture, and deep resume.

### Choose resumption shape deliberately

1. [Shallow Effect Handlers](../30-sources/hillerstrom-lindley-2018-shallow-effect-handlers.md)
   compares a deep fold with a shallow one-step case analysis.
2. [Retrofitting Effect Handlers onto OCaml](../30-sources/sivaramakrishnan-et-al-2021-retrofitting-effect-handlers-ocaml.md)
   supplies native one-shot runtime evidence.
3. [Soundly Handling Linearity](../30-sources/tang-et-al-2024-soundly-handling-linearity.md)
   explains why multi-shot control can duplicate or discard captured linear
   resources and develops a static remedy.
4. Use the synthesis's
   [multiplicity table](../20-notes/algebraic-effects-and-handlers.md#one-shot-affine-and-multi-shot-resumptions)
   to compare exactly-once, affine, and multi-shot contracts.

### Preserve identity and abstraction

1. [Abstraction-Safe Effect Handlers via Tunneling](../30-sources/zhang-myers-2019-abstraction-safe-effect-handlers.md)
   demonstrates accidental interception across higher-order polymorphic code.
2. [Binders by Day, Labels by Night](../30-sources/biernacki-et-al-2020-effect-instances-lexically-scoped-handlers.md)
   treats multiple uses of one signature as lexically scoped, typed instance
   names.
3. The synthesis proposes
   [nominal signatures plus lexical capabilities](../20-notes/algebraic-effects-and-handlers.md#a-provisional-catena-model),
   while the inquiry keeps the required abstraction theorem open.

### Keep scoped computations separate

1. [Effect Handlers in Scope](../30-sources/wu-et-al-2014-effect-handlers-in-scope.md)
   shows why first-order operations do not adequately represent operations
   with program arguments.
2. The synthesis distinguishes
   [first-order, scoped, and structured runtime effects](../20-notes/algebraic-effects-and-handlers.md#scoped-and-higher-order-effects).
3. The inquiry asks `local`, `catch`, `bracket`, timeouts, and task groups to
   justify their category through concrete cleanup and cancellation examples.

### Connect semantics to implementation

1. [Leijen 2017](../30-sources/leijen-2017-type-directed-compilation-row-typed-algebraic-effects.md)
   gives row inference, direct semantics, typed elaboration, and selective CPS.
2. [Sivaramakrishnan et al. 2021](../30-sources/sivaramakrishnan-et-al-2021-retrofitting-effect-handlers-ocaml.md)
   give a native fiber-stack implementation integrated with a mature runtime.
3. Follow the synthesis's
   [recommended implementation sequence](../20-notes/algebraic-effects-and-handlers.md#recommended-implementation-sequence)
   from free-tree oracle through differential backends.

## Open questions

- Can lexical capability identity coexist with Koka-style duplicate labels and
  retain principal inference?
- Does static capability elaboration obtain the same abstraction boundary as
  tunneling for higher-order effect-polymorphic code?
- Is an affine core binder plus runtime consumed bit sufficient for Catena's
  resource types, or is inferred control-flow linearity needed immediately?
- Which operations require a higher-order scoped calculus, and which require a
  privileged structured runtime scope?
- Does selective CPS or native stack segmentation better serve Catena's target
  platforms, FFI, and debugging expectations?

Track answers in
[Which Algebraic-Effect Semantics Should Catena Adopt?](../40-inquiries/which-algebraic-effect-semantics-should-catena-adopt.md),
and promote settled conclusions into the
[main synthesis](../20-notes/algebraic-effects-and-handlers.md).
