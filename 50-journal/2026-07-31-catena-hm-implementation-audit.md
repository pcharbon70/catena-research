---
title: "2026-07-31 Catena HM Implementation Audit"
kind: journal
created: "2026-07-31"
tags:
  - catena
  - hindley-milner
  - implementation-audit
  - type-inference
aliases: []
---

# 2026-07-31 Catena HM Implementation Audit

## Observations

This was a read-only static inspection of the sibling Catena repository for
the HM deep dive. No Catena files were modified and no build was run.

The inspected committed revision was:

```text
0f61d16f4f51500e2c27790c0d8c94eaf4784797
https://github.com/pcharbon70/catena.git
```

The working tree contained unrelated research-document changes, so durable
claims in the synthesis are pinned to the committed revision rather than to
those uncommitted documents.

## Evidence

### Discovery commands

```bash
git -C ../catena rev-parse HEAD
git -C ../catena remote get-url origin
rg --files ../catena/src/compiler/types ../catena/specs/compiler ../catena/specs
rg -n "generaliz|instantiat|occurs_check|principal|constraint|row.*polym" \
  ../catena/test/compiler/types ../catena/test/compiler/effects
```

### Core files inspected

- `specs/design.md`
- `specs/compiler/type_and_effect_system.md`
- `specs/planning/current_status.md`
- `src/compiler/types/catena_infer.erl`
- `src/compiler/types/catena_infer_expr.erl`
- `src/compiler/types/catena_infer_unify.erl`
- `src/compiler/types/catena_infer_state.erl`
- `src/compiler/types/catena_type_scheme.erl`
- `src/compiler/types/catena_type_env.erl`
- `src/compiler/types/catena_type_subst.erl`
- `src/compiler/types/catena_types.erl`
- `src/compiler/types/catena_constraint.erl`
- `src/compiler/types/catena_trait_resolve.erl`
- `src/compiler/types/catena_effect_poly.erl`
- `src/compiler/types/catena_row_unify.erl`
- `src/compiler/types/catena_row_poly_integration.erl`

### Positive alignment with HM

- The expression inferencer has explicit cases for variable instantiation,
  monomorphic lambda parameters, application unification, `let`
  generalization, and monomorphic recursive placeholders.
- The unifier applies the current substitution, performs occurs checks, and
  composes the new result back into inference state.
- Type schemes quantify variables free in a type or its trait constraints but
  absent from environment free variables.
- Scheme instantiation refreshes quantified variables and their constraints.
- Tests exist for scheme generalization and instantiation, substitution before
  generalization, occurs checks, constraint propagation, trait resolution, row
  occurs checks, and row-variable generalization.

### Integration boundaries observed

1. The nonrecursive `let` case applies the state substitution to the inferred
   expression type, then calls `generalize(Type, Env, State)` with the original
   environment. That helper calculates `ftv_env(Env)` directly; no environment
   substitution is visible on this path.
2. The same helper reads the complete accumulated constraint set from state.
   No binding-local constraint delta or retained/deferred split is visible.
3. `catena_infer_expr` duplicates scheme instantiation logic and includes a
   TODO about consolidating it with `catena_type_scheme:instantiate/2`.
4. `catena_infer:check_program` inserts every inferred top-level type with
   `catena_type_scheme:mono/1`.
5. The `letrec` expression path binds a monomorphic placeholder and does not
   generalize the completed recursive binding before typing its body.
6. Core function types validate concrete `{effect_set, Effects}` values;
   `catena_infer_unify:unify_effects/2` compares those sets for equality.
   Standalone `{teffectrow, Effects, Tail}` values have a separate row unifier,
   and `catena_effect_poly` uses another `{evar, Id}` representation.
7. `catena_types:type_vars/1` traverses the argument and result of `tfun` but
   ignores its effect field. It does collect the tail of standalone effect-row
   and resumption effect-row types.
8. The core lambda inference case constructs an empty latent effect set with a
   `pure for now` comment even though expression state tracks performed
   effects.

These are targets for formalization and regression tests, not conclusions from
runtime reproduction.

## Threads

- [How Hindley–Milner Type Inference Works](../20-notes/hindley-milner-type-inference.md)
  interprets the code against the primary literature.
- [How should Catena preserve principal inference while extending HM?](../40-inquiries/how-should-catena-preserve-principal-inference.md)
  turns the observed seams into answerable research tasks.
- [Current Catena type-system source](../30-sources/catena-2026-type-and-effect-system.md)
  records the stable project citation.

## Follow-ups

- Add minimal executable regressions for substituted-environment
  generalization and binding-local constraint ownership.
- Trace the production frontend path to determine which core and effect helper
  APIs are authoritative for source programs.
- Record test commands and outputs in a new journal entry when implementation
  changes are authorized.
