---
title: "Rows, Traits, and Effects"
kind: specification
created: "2026-08-01"
status: normative
spec_version: "0.1"
tags:
  - algebraic-effects
  - catena
  - row-polymorphism
  - specification
  - type-inference
aliases:
  - "Catena 0.1 row and trait solvers"
---

# Rows, Traits, and Effects

## Unique value rows

Records and variants use unordered unique-label rows. Extending a row with
label `l` generates `l absent r` for its tail. Unification aligns common
labels, propagates unmatched labels into an open tail, and fails on duplicate
labels, incompatible field types, a missing label in a closed row, or an
occurs-check violation. Closed row equality is label-order independent.

Projection requires the selected label in the record row. Variant injection
requires it in the variant row. There is no width or depth subtyping; openness
comes only from a quantified row tail. Lacks constraints MUST survive
generalization when they mention generalized tails.

## Duplicate effect rows and capabilities

Effect rows are unordered multisets of nominal operation-family occurrences.
Repeated labels are meaningful. Each occurrence carries a lexical capability
identity, so two capabilities for the same effect family are distinct unless
explicitly unified. An open tail expresses additional effects without erasing
multiplicity.

Performing an operation adds its capability occurrence to the evaluation
effect. Handling removes exactly the statically selected occurrence and
forwards the remainder. Resolution is lexical; the runtime MUST NOT search for
the nearest handler by label. Effect-row normalization may sort for stable
output but MUST preserve multiplicity and identity.

## Traits

Catena 0.1 has an open-world, coherent instance system with methods,
multi-parameter traits, functional dependencies, and associated types. It has
no overlapping instances, local instances, or associated constants.

An instance head MUST be headed by a nominal type constructor owned by either
the trait's defining package or that constructor's defining package. Two
visible instances MUST NOT unify. Instance constraints must be structurally
smaller than the head under a documented Paterson-style measure, and each
functional dependency must satisfy coverage. Associated type equations are
accepted only inside their instance and must terminate under the same measure.

Resolution selects the single matching instance, recursively solves its
context, and produces explicit evidence. Failure, multiple matches, a cycle,
or an undetermined variable is invalid. Resolution MUST be stable under import
order and separate compilation. There is no defaulting.

For a dependency `inputs -> outputs`, every variable in an instance's output
positions MUST occur in its input positions or be determined transitively by
another declared dependency. Any two instance heads that can agree on the
input positions MUST also agree on the output positions. Violating coverage or
consistency is invalid even when no current program selects both instances.

The termination measure is the multiset of constructor-and-variable counts in
the instance head. Every context predicate must contain no more occurrences of
any type variable and must be strictly smaller in total constructor count.
Associated-type right-hand sides may invoke normalization only at arguments
smaller by the same measure.

Functional dependencies improve determined-variable analysis. Associated
types normalize only after instance selection; they MUST NOT be used to choose
among otherwise competing instances. Exported signatures retain all
non-discharged constraints.

## Solver interface

Row unification, trait resolution, and associated-type normalization are
separate terminating solvers coordinated by a work list. Each step MUST either
reduce its documented measure, bind a fresh metavariable after kind and occurs
checks, or report a diagnostic. Solver scheduling MUST NOT affect accepted
programs, resulting schemes, or evidence identity.

The research routes for these choices are
[A Greenfield Type System for Catena](../../20-notes/catena-greenfield-type-system.md)
and [Algebraic Effects and Handlers](../../20-notes/algebraic-effects-and-handlers.md).
