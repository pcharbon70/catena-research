---
title: "Formal Semantic Kernel"
kind: map
created: "2026-08-06"
tags:
  - concurrency
  - formal-semantics
  - language-design
aliases:
  - "C010 research map"
---

# Formal Semantic Kernel

## Scope

This map connects the evidence, design, normative contract, executable model,
and promotion record for Catena's integrated 0.1.8 kernel.

## Start here

- [Catena's Formal Semantic Kernel](../20-notes/catena-formal-semantic-kernel.md)
  explains the bounded design and rejected expansion points.
- [How Should Catena Integrate Its Formal Semantic Kernel?](../40-inquiries/how-should-catena-integrate-its-formal-semantic-kernel.md)
  records the resolved integration and promotion decision.
- [Formal Semantic Kernel Specification](../60-specification/formal-semantic-kernel/README.md)
  contains the normative language contract.

## Trails

### From reductions to soundness

1. [Plotkin](../30-sources/plotkin-2004-structural-operational-semantics.md)
   supplies structural transitions.
2. [Wright and Felleisen](../30-sources/wright-felleisen-1994-syntactic-type-soundness.md)
   connect reduction to progress and preservation.
3. The normative [Metatheory](../60-specification/formal-semantic-kernel/metatheory.md)
   specializes those obligations to rows, handlers, and processes.

### From actors to BEAM

1. [Agha](../30-sources/agha-1986-actors.md) supplies the actor foundation.
2. [Special Delivery](../30-sources/fowler-et-al-2023-mailbox-types.md)
   shows the stronger behavioral typing left outside `Process M`.
3. [Concurrent Core Erlang](../30-sources/bereczky-et-al-2024-core-erlang-formalisation.md)
   and [OTP process rules](../30-sources/erlang-otp-29-processes.md) constrain
   the configuration and lowering.
4. [Actors, Messages, and Failures](../60-specification/formal-semantic-kernel/actors-messages-and-failures.md)
   states Catena's exact boundary.

### Compose the existing language

- [Catena Type-System Design](catena-type-system-design.md),
  [Algebraic Data Types](algebraic-data-types.md),
  [Clause Guards](clause-guards.md), and
  [Algebraic Effects and Handlers](algebraic-effects-and-handlers.md) lead into
  the unified judgment rather than being replaced as research trails.

## Open questions

- Source decoding is now fixed by C013, and identifiers, layout, comments,
  literals, and numeric literal meaning are fixed by C014–C018; token through
  file/module structure remain in G019–G020.
- Cleanup, exception catching, time, supervision, distribution, foreign
  values, and optimizer validity remain outside C010.
- Machine-checked metatheory may be considered after the paper model and
  executable evidence stabilize.
