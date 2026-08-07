---
title: "Catena's Formal Semantic Kernel"
kind: note
created: "2026-08-06"
maturity: developing
tags:
  - concurrency
  - formal-semantics
  - row-polymorphism
aliases:
  - "C010 semantic kernel synthesis"
---

# Catena's Formal Semantic Kernel

## Executive conclusion

Catena should consolidate its already implemented type, data, condition,
trait, and handler fragments with the smallest new runtime surface that makes
their interactions explicit. The result is a strict small-step kernel, not an
attempt to settle every future source-language or OTP feature.

The bounded design uses a canonical S-expression module as a retained 0.1.8
conformance input, gives record and variant rows actual term forms, and adds
local typed actor operations as a reserved host effect. Paper proofs, an
independent stepper, bounded schedule exploration, and BEAM differential tests
form one evidence stack.

## Decision standard

C010 is complete because a reader can follow one term from syntax through
typing, elaboration, verification, reduction, process scheduling, interface
serialization, and BEAM observation without importing a missing rule from the
compiler. The model must classify value, divergence, suspension, explicit
trap, invalid input, and analysis exhaustion separately.

It is not necessary to add layout-sensitive ergonomic syntax, foreign terms,
supervision, distribution, or machine-checked proofs. Those additions would
multiply boundaries without helping the existing fragments agree.

## Sequential spine

The sequential calculus is unary and curried, strict left to right, and
generally recursive. `let` sequences its right-hand side even when unused.
Matches retain structural-first, condition-second selection. Proper tail
calls are the only stack promise.

Structural records are finite unique-label products. Variants are
unique-label sums. Written field order controls effects, while semantic row
identity ignores order. Record selection/update/extension/restriction and
variant injection/matching expose exactly the operations already assumed by
the row solver.

Trait evidence remains explicit in core and erased after specialization.
Effect rows retain named effect identity and multiplicity; `handle` records
one selected named deep handler, and its resumption is affine. The bounded
kernel does not reproduce C005's wider capability-alias or outer-clause-effect
surface. An explicit uncatchable trap closes the soundness theorem's failure
case without inventing a catch mechanism.

## Actor boundary

`Process M` is deliberately weaker than a protocol or session type: it says
only which closed first-order values may be sent. Named process entries avoid
effect-bearing anonymous closures and captured lexical handlers. Their
ordinary effects must be handled internally; only the reserved, unhandleable
Process effect reaches the runtime.

Per-sender FIFO and oldest-matching selective receive align the language
contract with the useful local BEAM guarantees. Cross-sender scheduling has no
fairness or determinism promise. A dead-target send succeeds and drops its
message; normal return and trap discard the mailbox. Links, monitors,
timeouts, cancellation, and supervision remain separate designs rather than
half-defined flags.

## Formal model

Evaluation contexts give a deterministic local reduction. A global
configuration maps logical process identities to local states and typed
mailboxes. One nondeterministic global step chooses a runnable process. This
separation supports ordinary preservation, mailbox preservation, and a global
progress classification that admits quiescence without pretending to prove
deadlock freedom.

The executable reference should mirror the rules but remain structurally
independent from inference and BEAM lowering. Logical spawn-order identities
make traces comparable. Exhaustive bounded schedule exploration records a set
of reachable outcomes; reaching the bound is inconclusive.

## Representation and compatibility

The bootstrap compiler can use one fixed row layout—Erlang maps for records, a
tagged three-tuple for structural variants, and a constructor tag plus field
tuple for regular nominal data—because the language exposes no foreign
inspection. Public process-entry interfaces carry types and deterministic
spawn symbols, not PID or private worker layout.

The S-expression input is normative for exact revision 0.1.8 but intentionally
does not consume the wider ergonomic-source gaps. Existing JSON revisions,
interfaces, governance records, and signature domains remain valid.

## Falsification criteria

Narrow or reject the design if:

- a well-typed closed term gets stuck outside value, request, process
  operation, suspension, or trap;
- two row or trait solver orders change evidence meaning;
- a process mailbox contains a value outside its declared type;
- a spawned process observes a parent lexical handler;
- a rejected receive message moves or disappears;
- reference and BEAM results disagree outside scheduler interleaving or opaque
  process spelling; or
- a finite evidence limit is mistaken for a semantic rejection.

## Source trail

- [A Structural Approach to Operational Semantics](../30-sources/plotkin-2004-structural-operational-semantics.md)
  supplies the transition-system discipline.
- [A Syntactic Approach to Type Soundness](../30-sources/wright-felleisen-1994-syntactic-type-soundness.md)
  supplies the progress-and-preservation proof shape.
- [Actors](../30-sources/agha-1986-actors.md) separates asynchronous process
  identity from shared-state threads.
- [Special Delivery](../30-sources/fowler-et-al-2023-mailbox-types.md) shows the
  additional guarantees deliberately not claimed by a simple `Process M`.
- [A Formalisation of Core Erlang](../30-sources/bereczky-et-al-2024-core-erlang-formalisation.md)
  demonstrates a modular concurrent Erlang configuration model.
- [Erlang/OTP 29 Processes](../30-sources/erlang-otp-29-processes.md) supplies
  the target runtime ordering and lifetime evidence.
- Existing notes on [extensible records and variants](../30-sources/gaster-jones-1996-extensible-records-variants.md),
  [row-typed effects](../30-sources/leijen-2017-type-directed-compilation-row-typed-algebraic-effects.md),
  and [handlers in action](../30-sources/kammar-et-al-2013-handlers-in-action.md)
  constrain the sequential integration.

## Connections

The [formal-kernel inquiry](../40-inquiries/how-should-catena-integrate-its-formal-semantic-kernel.md)
records the bounded decisions. The [topic map](../10-maps/formal-semantic-kernel.md)
routes into the normative [0.1.8 specification](../60-specification/formal-semantic-kernel/README.md).
