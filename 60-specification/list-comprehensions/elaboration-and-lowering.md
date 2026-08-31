---
title: "Elaboration and Lowering"
kind: specification
created: "2026-08-31"
status: candidate
spec_version: "0.1.39"
tags:
  - comprehensions
  - elaboration
  - lowering
  - specification
aliases:
  - "Catena comprehension elaboration"
---

# Elaboration and Lowering

## Status and authority

This chapter is the normative Catena 0.1.39 elaboration,
lowering, and cost-honesty rule set. It is governed by
[Specification Authority](../../SPECIFICATION-AUTHORITY.md),
[Catena Conformance Vocabulary](../../CONFORMANCE-VOCABULARY.md), and
[Catena Implementation Limits and Portability](../../IMPLEMENTATION-LIMITS.md).
It follows the generation-not-execution discipline of C038 and the
dormant-witness pattern of C035.

The rules apply only to source-language revision `0.1.39`.

## The qualifier-tree target

> **Normative definition.**

Comprehensions elaborate through a dedicated typed qualifier tree —
one node per generator, filter, and binding, in source order, each
carrying its pattern, type, and effect row (`LC-OBL-010`). The
elaboration target is the kernel typed core of revision `0.1.8`:
recursive worker definitions are expressible there, and no frozen
frontend gains comprehension expressions. Elaboration MUST NOT
route through open trait dispatch (`LC-OBL-010`): the generated
worker performs the traversal directly.

## Extensional equations

> **Normative definition.**

The qualifier tree satisfies the pure extensional equations with
`map` and `flat_map` (`LC-OBL-010`): a single ordinary generator
with `yield e` is `map (λx. e) source`; each additional generator
composes by `flat_map`; a `when` filter is the zero-or-unit
operation the algebra requires. These equations are proof tools
and optimization licenses; the traversal and failure rules of
[Generator and Qualifier Rules](generator-and-qualifier-rules.md)
and [Evaluation Effects and Execution](evaluation-effects-and-execution.md)
remain the operative semantics (`LC-OBL-010`).

## The fused worker

> **Normative definition.**

Lowering produces one fused tail-recursive worker per
comprehension (`LC-OBL-013`): a single recursive definition
traverses the sources in order, applies filters and bindings
inline, and accumulates the output; no intermediate `map`- or
`filter`-shaped intermediate lists exist between qualifiers
(`LC-OBL-013`). The worker is stack-safe for linear output, and
output allocation is linear in the number of yielded elements
(`LC-OBL-013`). Generated code is compiler-internal generation in
the C038 sense: it executes no user code the qualifiers do not
name, and diagnostics MUST name the source qualifier, never the
generated worker frame (`LC-OBL-013`). The native BEAM list
comprehension, where an implementation emits one, is an
optimization beneath this contract, not the semantics
(`LC-OBL-013`).

## Cost honesty

> **Normative definition.**

No complexity promise rides this area (C042's exclusion): the
Cartesian cost of multiple generators is explained by the
traversal rule — `|result| ≤ |source1| × … × |sourceN|` with each
source visited once per enclosing prefix — and by the visible
multiplicity of effectful qualifiers, not by asymptotic language
guarantees (`LC-OBL-013`).

## The dormant adoption boundary

> **Normative definition.**

Until the surface-grammar capstone adopts the tokens, the
executable witness of this contract is the dormant elaboration
boundary (`LC-OBL-001`, `LC-OBL-014`): a qualifier tree elaborates
to a kernel module that checks, runs on the reference stepper, and
compiles to BEAM agreeing on values, failures, and effect traces.
Implementations MUST NOT claim surface comprehension syntax,
generator sources other than lists, lazy production, parallel
traversal, or non-list targets from this area (`LC-OBL-014`).

## Rationale and evidence (non-normative)

The [synthesis](../../20-notes/list-comprehensions.md) records the
dedicated-tree decision (type checking, effect checking, and
diagnostics over one representation), the BEAM fused-worker
rationale, and why law evidence is not cost evidence. C035's
correct-but-dormant lowering supplies the adoption pattern.
