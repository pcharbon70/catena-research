---
title: "Kernel Static Semantics and Elaboration"
kind: specification
created: "2026-08-06"
status: normative
spec_version: "0.1.8"
tags:
  - row-polymorphism
  - specification
  - type-inference
aliases:
  - "Catena integrated kernel typing"
---

# Kernel Static Semantics and Elaboration

## Unified judgment

The integrated kernel judgment is `Σ ; Γ ; Π ⊢ e : t ! ε ⇝ c`. `Σ` contains
the local regular datatypes, closed trait instances, ordinary effects, named
handlers, signed definitions, and local or digest-verified process entries.
`Γ` maps values to monotypes or rank-1 schemes. `Π` is either absent or
contains the current closed mailbox type and reserved Process capability. `c`
is explicit typed core.

Every expression records its result type, canonical evaluation-effect row,
and source span. Constructor, trait-call, handler, and spawn nodes additionally
record the selected declaration or interface evidence. Patterns record their
scrutinee type and selected constructor where applicable. These records are
proof-relevant compiler data and are not source values.

## Structural rows

Record and variant rows contain unique labels. Record construction yields a
closed row. Selection and update require the label to be present and preserve
the row. Extension requires the label absent and adds it. Restriction requires
the label present, discards its value, and removes it.

Variant injection yields a row containing its label and a fresh open tail
unless an expected type closes it. A match over a closed variant is exhaustive
only when all possible labels are covered. A match over an open variant
requires a final binder or wildcard clause. Duplicate labels, missing labels,
and incompatible payloads are invalid.

The solver does not infer general row equations or structural record patterns.
An operation can inspect only labels already written in its operand row.
Selection, update, and restriction preserve a written tail, but extension is
accepted only on a closed row so absence is established without an implicit
lacks constraint. Open injected variants must be closed by an expected type or
consumed by a match with an unguarded catch-all before they reach a closed
public or process boundary.

## Functions, schemes, recursion, and effects

The core function type is unary. Multiple written parameters and arguments
elaborate to nested functions and left-associated calls. Supplying fewer
arguments returns a closure. General recursion is permitted for signed named
definitions; divergence is a program behavior rather than invalid input.

A definition signature quantifies every type variable written in that
signature. A `let` binding generalizes exactly the variables free in the
inferred value type and absent from `Γ` when evaluation has no effects and the
right-hand side is either non-expansive or contains no request, handle, or
resume form. Integers, Booleans, Unit, variables, functions, tuples of
non-expansive terms, records of non-expansive fields, constructors of
non-expansive fields, and annotations over those forms are non-expansive. In
all other cases the binding is monomorphic. The typed core records the chosen
scheme, and each use records an instance.

Evaluation effects compose in written order. Trait calls elaborate to one
coherent closed instance and module-definition identity. An ordinary request
is identified by its declared effect and operation. `handle H e` statically
selects `H`, removes one occurrence of H's effect from `e`, and uses deep
handling. Handler return and operation bodies are effect free in this kernel.
Each operation clause may abandon its resumption or use it once; a second
syntactic use is invalid. No evidence, handler, or resumption is a source
value.

## Process types and sendability

`Process M` is well kinded when `M : Type`, is closed, and is sendable. A type
is sendable exactly when its finite unfolding uses only Int, Bool, Unit,
tuples, closed nominal data, closed structural records or variants, and
`Process N` for sendable `N`. Functions, open rows, capabilities, handlers,
resumptions, equality evidence, and trait evidence are not sendable.

A process entry has first-order sendable parameters, one closed sendable
mailbox type, and Unit result. Its residual effect is empty or contains only
its reserved Process capability. It cannot inherit a caller's ordinary
capability. A public process entry records origin-qualified identity,
parameters, mailbox type, and arity in the module interface.

`spawn P(args)` checks the statically selected local or imported entry and
returns `Process M`. `self` is valid only under `Π` and returns `Process M`.
`send target message` requires `target : Process M` and `message : M`, returns
Unit, and adds Process to the evaluation effect. `receive` is valid only under
`Π`; every clause pattern has mailbox type `M`, every condition satisfies the
portable condition rules, and all bodies have one result type.

The reserved Process effect cannot be declared, requested through ordinary
request syntax, handled, exported as a user effect, or forged by an interface.

## Explicit trap

If `reason` has a closed sendable type, `trap reason` may synthesize any
expected result type. Its evaluation effect is the effect of evaluating
`reason`; the terminal transfer itself is recorded explicitly in core. A trap
does not become a typed value and cannot be caught in 0.1.8.

## Normal forms

> **Normative unspecified presentation.**

Fresh synthesized type-variable and open-variant-tail spelling is bounded
unspecified presentation. It may differ only when local schemes and typed core
remain equivalent under alpha-renaming and selected evidence, stable
diagnostic identity, runtime behavior, interface bytes, and artifact identity
do not change.

## Independent verification

The verifier MUST recheck the integrated kernel judgment without trusting the
checker substitution or its acceptance result. It derives expression and
pattern types, effect composition, let-generalization eligibility, head
coverage, handler completeness and affinity, selected constructor/trait/
handler/process evidence, recursive sendability, public exports, process-entry
identity, mailbox types, receive clauses, and closed trap-reason types. It also
requires a source span on every executable expression. Backend lowering
accepts only verified core.

The corresponding transitions are defined by
[Sequential Dynamics](sequential-dynamics.md) and
[Actors, Messages, and Failures](actors-messages-and-failures.md).
