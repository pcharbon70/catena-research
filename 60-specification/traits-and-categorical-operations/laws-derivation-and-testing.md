---
title: "Laws, Derivation, and Testing"
kind: specification
created: "2026-08-02"
status: normative
spec_version: "0.1.4"
tags:
  - algebraic-data-types
  - category-theory
  - specification
  - trait-constraints
aliases:
  - "Catena 0.1.4 trait laws and derivation"
---

# Laws, Derivation, and Testing

## Law domain

Standard law schemas describe equations over pure, total operations, finite
values, and total callbacks. Function equality in a generated test suite is
bounded extensional equality over an explicit finite input set. Divergent or
effectful callbacks do not inhabit the law domain, though their execution is
still governed by the operational order contract.

Every equality used by a law suite MUST come from an explicit `Equatable`
instance for the compared result type. Host-language equality may implement
that instance; it may not be silently substituted for missing Catena
evidence.

## Evidence tiers

Version 0.1.4 admits exactly three law statuses:

- `promised`: the instance author accepts the obligations;
- `tested`: a named finite property suite passed for recorded generators and
  bounds; and
- `derived`: the compiler generated the implementation through a specified
  structural algorithm.

`trusted` and `proved` are reserved for a later proof and governance design
and MUST be rejected in 0.1.4 input. None of the three admitted tiers authorizes
an optimizer rewrite. Law metadata supports documentation, tests, diagnostics,
and future evidence work only.

There is no general user law language in 0.1.4. The standard interface carries
named schemas and their domains; an instance supplies a status, not arbitrary
compiler-executed propositions.

## Structural derivation

The compiler accepts explicit derivation requests for:

- `Equatable`;
- `Orderable`;
- `Mapper`;
- `TwoSlotMapper`;
- `Reducible`; and
- `CollectingMapper`.

Every request names its target type parameters, including the two distinct
targets of `TwoSlotMapper`. The compiler checks transparency, target existence,
kind, variance, positivity, regular recursion, required field instances, and
the operation's structural shape. Unsupported nested, negative, existential,
GADT, or irregular positions are rejected with `DRV001`; a requested name is
never sufficient evidence.

A successful request generates one implicit `derived` instance and a
type-qualified operation such as `Tree.map`. The generated implementation is
constructor complete, preserves shape, evaluates fields in declaration order,
and carries compiler provenance. Instance authors cannot supply optimized
derived-operation overrides in 0.1.4; the minimal method set remains singular.

`CollectingMapper` derivation sequences callback-produced contexts through
the selected `ValueEmbedder` and `MultiMapper` evidence. It is not an alias for
ordinary pure mapping. Standard recursive collection instances MUST use
stack-safe library implementations even when a general user datatype's
structural derivation is not stack safe.

The 0.1.4 standard interface supplies tested `Mapper` and `Reducible` instances
for `List`. Their ordinary-library implementations use reverse accumulation
and an iterative left fold, respectively, so their public whole-list paths do
not consume stack in proportion to list length. `CollectingMapper` for standard
collections remains outside 0.1.4; the derived datatype template is not evidence
for such an instance.

## Law testing

Generated checks MUST record the trait, instance identity, law identifier,
sample domain, callback sample set, generator seed when randomization is used,
and result. Passing tests promote evidence only to `tested`; changing an
instance, relevant type, standard interface digest, or generator inputs
invalidates the record.

The representative conformance suite includes intentionally unlawful cases,
explicit equality evidence, and bounded extensional callback comparisons.
Tests do not make nontermination, exhaustive function equality, or proof
claims.

## Connections (non-normative)

The evidence ladder and limitations come from the
[categorical hierarchy inquiry](../../40-inquiries/how-should-catena-specify-its-initial-categorical-hierarchy.md)
and the [combinator synthesis](../../20-notes/combinators-for-algebraic-data-and-categorical-programming.md).
