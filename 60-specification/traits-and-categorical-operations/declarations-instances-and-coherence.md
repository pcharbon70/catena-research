---
title: "Declarations, Instances, and Coherence"
kind: specification
created: "2026-08-02"
status: normative
spec_version: "0.4"
tags:
  - specification
  - trait-constraints
  - type-inference
aliases:
  - "Catena 0.4 trait coherence"
---

# Declarations, Instances, and Coherence

## Declaration model

A trait declaration records a stable identity, public name, origin, one or
more kinded parameters, direct parents, minimal methods, law schemas,
functional dependencies, and visibility. An instance records its trait,
kind-correct head arguments, owner, decreasing prerequisite constraints,
exact minimal methods, associated-type equations, law status, and optional
compiler-derivation provenance.

The JSON AST is declarative transport. It does not freeze eventual source
punctuation. Declarations are checked before instances; instance evidence is
available only after the complete import and local declaration environment is
known.

## Kinds and relations

Each argument MUST match its trait parameter kind. Constructor application is
left-associated and kind checked. Multi-parameter traits MAY declare
functional dependencies as input and output parameter positions. Associated
types are permitted and reduce only after one coherent instance has been
selected. Associated constants are excluded from 0.4.

## Ownership and overlap

An implicit instance is legal only when its declaring origin owns the trait or
owns a nominal constructor in the instance head. The complete visible
instance set MUST be globally non-overlapping; local preference, declaration
order, import order, and “most specific” selection are not tie breakers.

For every functional dependency, any two heads that unify at all input
positions MUST also unify at all output positions. Violation is a declaration
error, not a deferred call-site ambiguity.

Alternate orders, monoids, or execution policies over one representation use
an explicit nominal wrapper. Runtime dictionaries are not a back door around
coherence.

## Termination

Every prerequisite constraint in an instance context MUST be structurally
smaller than its instance head. Resolution rejects recursive goals and runs
with a deterministic minimum budget of 20,000 steps. A budget exhaustion is a
compiler diagnostic and never falls back to dynamic lookup.

Type-growing polymorphic recursion during package template specialization is
also rejected. This restriction keeps package linking deterministic without
requiring unrestricted type-level evaluation.

## Parent evidence

Parent predicates are instantiated with the child's actual type arguments,
not with unresolved declaration variables. Evidence solving memoizes each
canonical trait-and-argument goal. When parent paths form a diamond, equal
goals reuse the same evidence identity and method set.

In the standard hierarchy, `Workflow m` entails one `ValueEmbedder m` and one
`Chainable m`;
their routes to `Mapper m` MUST select the same globally coherent Mapper
instance. Parent evidence is compiler data and is erased after specialization.

## Inference boundary

Ordinary unqualified expressions retain principal rank-1 inference. Trait
constraints are solved at monomorphic specialization roots or retained as
verified interface templates. Ambiguous variables that do not determine one
instance are rejected rather than defaulted. Higher-kinded trait parameters
are rigid; 0.4 does not add arbitrary type lambdas or higher-rank inference.

## Connections (non-normative)

The type-theoretic rationale is in
[A Greenfield Type System for Catena](../../20-notes/catena-greenfield-type-system.md)
and its [active inquiry](../../40-inquiries/what-should-a-greenfield-catena-type-system-guarantee.md).
