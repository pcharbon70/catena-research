---
title: "Catena Type and Effect System at 0f61d16"
kind: source
created: "2026-07-31"
authors:
  - "Catena contributors"
published: "Git commit 0f61d16f4f51500e2c27790c0d8c94eaf4784797"
citation_key: "catena2026TypeEffectSystem"
container: "Catena source repository"
edition: null
isbn: null
doi: null
url: "https://github.com/pcharbon70/catena/blob/0f61d16f4f51500e2c27790c0d8c94eaf4784797/specs/compiler/type_and_effect_system.md"
accessed: "2026-07-31"
tags:
  - catena
  - effect-rows
  - trait-constraints
  - type-inference
aliases:
  - "Current Catena type system"
---

# Catena Type and Effect System at 0f61d16

## Reference

Catena contributors, [“Type and Effect System”](https://github.com/pcharbon70/catena/blob/0f61d16f4f51500e2c27790c0d8c94eaf4784797/specs/compiler/type_and_effect_system.md),
with the corresponding compiler implementation under
[`src/compiler/types`](https://github.com/pcharbon70/catena/tree/0f61d16f4f51500e2c27790c0d8c94eaf4784797/src/compiler/types),
Git commit `0f61d16f4f51500e2c27790c0d8c94eaf4784797`, inspected July 31, 2026.

## Promoted design

The specification identifies Hindley–Milner-style inference as Catena's
current type-theoretic core. The promoted surface adds trait constraints and
instance resolution, pre-inference kind validation, concrete effects and effect
rows, typed handlers, and first-class `Resumption k a b e` values.

## Method

This source note is based on a static inspection of the canonical specification
and the corresponding Erlang modules for expression inference, schemes,
environments, substitutions, unification, constraints, effects, and row
polymorphism. Exact commands and code-level observations are preserved in the
[implementation-audit journal](../50-journal/2026-07-31-catena-hm-implementation-audit.md).

## Findings

- `catena_infer_expr` follows the recognizable W cases for variables, lambdas,
  application, nonrecursive `let`, and monomorphic `letrec`.
- `catena_type_scheme` represents both ordinary and qualified schemes and
  quantifies variables found in types or trait constraints but not in the
  environment.
- `catena_infer_unify` performs occurs-checked type unification and extends it
  with kinds, applications, records, effect rows, and resumptions.
- Trait obligations are accumulated in inference state, substituted and
  simplified at the public boundary, then resolved against built-in instances.
- Effect functionality is distributed across concrete effect tracking,
  `teffectrow` unification, a separate `catena_effect_poly` representation, and
  row-polymorphism integration helpers. The specification describes a promoted
  integrated surface, but the core scheme path and the row/effect helper paths
  are not yet one obviously canonical abstraction.
- The public `check_program` path stores inferred top-level results as
  monomorphic schemes, even though expression-level `let` generalizes.

## Relevance

This is the project-local evidence that turns the HM deep dive into an
engineering question. Catena already has most named mechanisms; the remaining
research task is to state and test which principality, soundness, coherence,
and generalization guarantees the combined system intends to preserve.

## Limits

Static inspection demonstrates structure and identifies proof obligations; it
does not establish semantic soundness or algorithmic completeness. The working
tree also contained unrelated research-document changes during inspection, so
this record pins claims to the committed source revision and did not modify the
Catena repository.

## Derived work

- [Hindley–Milner type inference](../20-notes/hindley-milner-type-inference.md)
- [Catena HM implementation audit](../50-journal/2026-07-31-catena-hm-implementation-audit.md)
- [How should Catena preserve principal inference while extending HM?](../40-inquiries/how-should-catena-preserve-principal-inference.md)
