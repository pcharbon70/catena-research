---
title: "Categorical Operation Semantics"
kind: specification
created: "2026-08-02"
status: normative
spec_version: "0.4"
tags:
  - category-theory
  - evaluation-order
  - specification
  - trait-constraints
aliases:
  - "Catena 0.4 trait operation order"
---

# Categorical Operation Semantics

## Strict sequential baseline

All 0.4 standard operations are strict and sequential. Arguments are
evaluated left to right. A callback receives positions once in source
declaration order unless the operation's type says it may change cardinality,
as `and_then` can. A mapper, reducer, or collector MUST NOT reorder, duplicate,
or speculatively invoke callbacks.

The principal subject is the final argument. For a multi-subject operation,
the subjects retain their written left-to-right order. `summarize callback
initial subject` uses the initial accumulator before the first position and
threads each result into the next callback.

## Composition direction

`compose first next` runs `first` and then `next`. This differs from the
right-to-left reading common in some mathematical notation and is fixed by the
public vocabulary. `identity` is neutral on both sides within the pure total
law domain.

## Laws do not schedule work

Associativity, applicative shape, monoidal structure, or traversal laws do not
permit reordering, batching, concurrency, cancellation, or callback elision.
Any parallel or unordered operation must have a different explicit API and an
effect contract suitable for it.

## Divergence and effects

If a callback diverges or performs a visible effect, the implementation still
owes the prefix order above: only callbacks before the divergent position may
have run. Algebraic equations make no claim about such a program. Evidence
selection and erasure MUST NOT change callback count, order, exceptions,
messages, resource cleanup, or other source-observable behavior.

## Early termination

Mapping, combining, chaining, reduction, and collection do not acquire hidden
short-circuiting from their laws. An operation that can stop early uses a
separate result protocol and name. `equals` and `compare` MAY avoid later
structural fields once their result is determined only when that exact
short-circuiting behavior is part of the instance's documented operation,
not as a law-derived transformation.

## Stack and cost obligations

Standard list and collection instances MUST be stack safe for inputs accepted
by their public APIs. A general derived operation MUST disclose or reject a
shape for which the derivation algorithm cannot meet its declared stack
contract. Interfaces carry semantic templates and provenance, not a guarantee
that every operation is constant time or allocation free.

Version 0.4 applies that obligation to the standard `List` `Mapper` and
`Reducible` instances and requires conformance execution on at least 250,000
elements. It makes no stack-safety claim for a standard collection capability
that 0.4 does not provide.

## Connections (non-normative)

These rules specialize the distinction between algebraic law and execution in
[Combinators for Algebraic Data and Categorical Programming](../../20-notes/combinators-for-algebraic-data-and-categorical-programming.md).
