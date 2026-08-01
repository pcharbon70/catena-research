---
title: "Clause Guards"
kind: map
created: "2026-08-01"
tags:
  - catena
  - compilers
  - language-design
  - pattern-matching
aliases:
  - "Clause-guard research map"
---

# Clause Guards

## Scope

This map follows clause guards from ordered selection through static safety,
coverage, type facts, match compilation, and BEAM selective receive. It treats
guards as a boundary among several language subsystems rather than a Boolean
syntax attachment.

## Start here

Read [Clause Guards](../20-notes/clause-guards.md) for the complete synthesis
and initial Catena recommendation. It proposes checked Boolean-only clause
conditions, a total effect-free guard fragment, conservative coverage, a typed
guard-tree IR, and separate ordinary versus receive lowering.

Then use
[How Should Catena Design Clause Guards?](../40-inquiries/how-should-catena-design-clause-guards.md)
for the unresolved proof, prototype, performance, and usability work.

## Trails

### Begin with ordered clause meaning

1. [OCaml 5.4 Expressions and Pattern-Matching Guards](../30-sources/ocaml-5-4-expressions-and-pattern-guards.md)
   gives the minimal pattern-then-Boolean-then-body account.
2. [Haskell 2010 Language Report](../30-sources/marlow-2010-haskell-language-report.md)
   broadens guards to refutable patterns and bindings, then translates them to
   a small kernel.
3. [The Rust Reference: Match Expressions](../30-sources/rust-reference-match-expressions.md)
   exposes the binding, ownership, effect, and multiple-evaluation questions
   created by richer guards.

This trail motivates Catena's initial Boolean-only surface and explicit
one-evaluation rule.

### Connect safety to the BEAM

1. [Erlang/OTP Expressions and Guard Sequences](../30-sources/erlang-otp-expressions-and-guard-sequences.md)
   explains the restricted side-effect-free guard subset, failure conversion,
   and selective-receive scan.
2. [Erlang/OTP Function Matching and Optimization](../30-sources/erlang-otp-function-matching-optimization.md)
   shows how a guarded overlapping row constrains compiler reordering.
3. [Algebraic Effects and Handlers](algebraic-effects-and-handlers.md) explains
   why an empty effect row is necessary but does not by itself establish
   termination or totality.

This trail separates Catena's semantic guard-safe fragment from the
backend-specific native-lowerable subset.

### Build coverage from structure to facts

1. [Warnings for Pattern Matching](../30-sources/maranget-2007-warnings-pattern-matching.md)
   supplies usefulness, exhaustiveness, redundancy, and witness generation for
   structural patterns.
2. [Lower Your Guards](../30-sources/graf-et-al-2020-lower-your-guards.md)
   supplies a compositional guard-tree IR and refinement descriptions.
3. [Structural and Semantic Pattern Matching Analysis in Haskell](../30-sources/kalvoda-kerckhove-2019-structural-semantic-pattern-matching.md)
   demonstrates the precision and cost of an SMT-backed fact oracle.

This trail supports a sound structural baseline plus an optional
proof-producing precision tier.

### Rejoin the wider language

- [Algebraic Data Types](../20-notes/algebraic-data-types.md) defines the
  structural pattern vocabulary, ordered matching, and exhaustive default that
  guards refine.
- [A Greenfield Type System for Catena](../20-notes/catena-greenfield-type-system.md)
  supplies principal inference, trait evidence, effect rows, and the boundary
  against solver-driven public types.
- [Language-Integrated Specifications and Governance](../20-notes/language-integrated-specifications-and-governance.md)
  distinguishes universal proof from tests, assumptions, and approvals when a
  specification is used to simplify a guard.
- [List Comprehensions](list-comprehensions.md) separates effect-free,
  guard-safe clause conditions from ordinary effect-typed Boolean
  comprehension filters.
- [Catena Language Overview](../language-overview.md) locates match coverage and
  guard elaboration in the whole compiler.

## Open questions

The active
[clause-guard inquiry](../40-inquiries/how-should-catena-design-clause-guards.md)
tracks:

- the smallest practical total expression fragment;
- verified user predicates and trait evidence;
- deterministic proof-producing guard facts;
- portable BEAM-native receive guards;
- guard-tree interpretation and lowering equivalence;
- diagnostics and public vocabulary;
- whether clause conditions and comprehension filters should share a surface
  keyword despite different safety, failure, and coverage judgments; and
- evidence needed before adding pattern or handler guards.
