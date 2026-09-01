---
title: "Catena Name Resolution"
kind: note
created: "2026-09-01"
maturity: developing
tags:
  - catena
  - name-resolution
  - type-system
  - language-design
aliases:
  - "type-independent resolution"
---

# Catena Name Resolution

## Executive conclusion

Name resolution in Catena is type-independent: every written name
denotes exactly one declaration, chosen by scope structure alone,
and no annotation — added, removed, or changed — ever moves a
name's target. Five classes confirm the invariant from their own
corners: field labels are not names at all, trait method names
resolve normally (instance selection is evidence, chosen before
the call site exists), constructors are declaration-scoped,
literals self-describe by spelling, and operators instantiate over
a closed set with no name choice to make. The invariant is not a
new rule so much as the roof over four standing pillars.

## Scope, method, and definitions

This note synthesizes the archive's evidence for closing G066 at
revision `0.1.42`. It reads C021's namespace model, C018's
no-adaptation clause, C065's instance-level ambiguity rejection,
and C061's closed-set instantiation; it proposes no mechanism.

- **Type-directed resolution** — choosing among candidate
  declarations for one name using inferred or expected types.
- **Order-dependence hazard** — resolution results that depend on
  elaboration order (which annotations were seen first), the failure
  mode that motivates the invariant.

## The four pillars

1. **C021**: resolution is a function of scope structure —
   local-beats-imported precedence with rejection on import
   collision; the OCaml open-re-shadowing model was rejected
   precisely because it made resolution order-dependent.
2. **C018** (`NM-OBL-005`): literals carry no constraints and
   adapt to no expected type — spelling decides.
3. **C065**: trait ambiguity is rejected at the instance, "not a
   deferred call-site ambiguity" — evidence settles before calls.
4. **C061**: operators are closed-set instantiation — one rule per
   operator, no candidate list, no choice.

## The carve-out that keeps the invariant honest

Trait dispatch looks like type-directed resolution and is not.
The name `reveal` denotes one method declaration, resolved by
scope; which dictionary runs is **evidence selection** under
coherence, with ambiguity rejected at the instance. The
distinction has teeth: evidence selection cannot rename anything,
cannot be shadowed, and never defers a decision to a call site.
If instance selection were resolution, C065's model and the
invariant would contradict each other; classified as evidence,
they are the same discipline seen from two sides.

## What the invariant forbids, and what would falsify it

No overloaded-by-type names, no expected-type-adapted literals, no
call-site ambiguity deferral, no field access that infers which
field from the expression's type. Falsification: any context where
changing only an annotation changes which declaration a name
denotes, or where resolution results depend on elaboration order.
Each exclusion is amendable only by a revision that amends the
classification table explicitly.

## Route to sources

- The [Name Resolution Specification](../60-specification/name-resolution/README.md)
  defines the normative `0.1.42` contract this note argues for.
- [Catena Namespaces and Shadowing](catena-namespaces-and-shadowing.md)
  — the scope-structural model (pillar one).
- [Numeric Types and Literal Typing](../60-specification/numeric-literal-semantics/numeric-types-and-literal-typing.md)
  — the no-adaptation clause (pillar two).
- [Declarations, Instances, and Coherence](../60-specification/traits-and-categorical-operations/declarations-instances-and-coherence.md)
  — instance-level ambiguity rejection (pillar three).
- [The Closed-Set Instantiation Rule](../60-specification/numeric-relationships/the-closed-set-instantiation-rule.md)
  — the no-name-choice rule (pillar four).
- The [resolved inquiry](../40-inquiries/may-name-resolution-depend-on-inferred-types.md)
  preserves the decision route.
