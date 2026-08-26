---
title: "Catena Bindings and Sequencing"
kind: note
created: "2026-08-25"
maturity: developing
tags:
  - catena
  - language-design
  - bindings
  - sequencing
aliases:
  - "Catena binding model"
---

# Catena Bindings and Sequencing

## Executive conclusion

Catena's binding model at `0.1.27` is the kernel's, elevated and
completed. A local binding is **non-recursive**: one plain value name,
one right-hand side, one body — the RHS cannot see the name being
bound, and substitution happens only after the RHS is a value. Scope is
**sequential and lexical**: each `let` extends the environment for its
body alone. A local binding **may silently shadow anything in scope**
— outer bindings, module definitions, imports, the prelude origin —
C021's innermost-wins rule stated once at the binding level.

**Recursion is definitions-only.** Named definitions recurse through
the kernel's signed environment; mutual recursion is C024's SCC
statement at module level, elevated here as the language answer. Local
recursive or mutual forms are excluded with G032 (named local
functions) and P034 (termination) as their owners.

An **unused binding is valid and its RHS still evaluates** — effects
observable, per C030's schedule — elevated verbatim from the kernel.
New at the language level: a deny-able `BS001` warning fires on
genuinely unused binders, with a `_`-prefix exemption as the
deliberate-discard escape hatch, exactly the IMP001 pattern C022
established for unused imports.

**Sequencing of effectful expressions is the let idiom**:
`let _ = e1; e2` evaluates e1 to a value, discards it, then evaluates
e2. This is the only sequencing the retained JSON AST can express —
its tags are frozen at 0.1.1–0.1.7 — so elevating the idiom rather
than declaring a distinct form keeps the compiled path conformant; the
kernel's bare sequence form stays kernel-calculus; P109 may surface
dedicated punctuation later.

The deliverable is C030-style witnesses — stepper, reference
evaluator, and compiled BEAM agreeing on values and effect traces —
plus the `BS001` compiler wiring. This is the first new diagnostic
family since C027's `ENT`, and the first warning family since C022.

## Scope and method

The operational target is independent agreement on binding structure,
scope, the recursion boundary, unused-binding fate, sequencing, and
shadowing — made executable through tri-target witness agreement and
the warning. Primary evidence is internal: the [kernel's let and
signed-environment rules](../60-specification/formal-semantic-kernel/sequential-dynamics.md),
[C021's precedence table](../60-specification/namespaces-and-shadowing/shadowing-and-ambiguity.md),
[C024's SCC admission](../60-specification/module-dependency-cycles/scc-admission-and-resolution.md),
[C030's schedules](../60-specification/evaluation-order/ordered-forms-and-entry-rule.md),
and [C022's IMP001 precedent](../60-specification/imports-and-exports/import-declarations-and-admission.md).
Source claims stay distinct from Catena proposals below.

## Relation to the current corpus

The [kernel's paragraph](../60-specification/formal-semantic-kernel/sequential-dynamics.md)
fixes substitute-after-value, unused-bindings-valid, and named
recursion through the signed environment — frozen at 0.1.8. C031
elevates without touching it, exactly as C029 elevated its value
paragraph and C030 its order list.

[C021](../60-specification/namespaces-and-shadowing/shadowing-and-ambiguity.md)
already fixed that a local declaration silently shadows anything
weaker in its category — the innermost-wins rule this slice restates
at the bindings level. No new collision diagnostics exist here
because none are needed: `NSP004` remains an import-vs-import
phenomenon, and a local always wins without comment.

[C024](../60-specification/module-dependency-cycles/scc-admission-and-resolution.md)
answered mutual recursion where it actually lives: among named module
definitions, admitted as strongly-connected components with signature
regimes. Elevating that as *the* mutual-recursion statement closes
G031's clause without inventing a local letrec.

[C030](../60-specification/evaluation-order/ordered-forms-and-entry-rule.md)
fixed the `let` and sequence schedules — when things evaluate. C031
fixes the structure of what binds. The sequencing idiom composes the
two: first-to-value-then-second is C030's row; that a `_` binder
achieves it is C031's statement.

[C022's IMP001](../60-specification/imports-and-exports/import-declarations-and-admission.md)
is the corpus's only warning family — deny-able through the manifest's
`diagnostics.deny` field. `BS001` copies the pattern wholesale:
default warning, deny promotes to error, transactional emission, and
now an exemption the import warning never needed — `_`-prefixed
binders are exempt because the normative sequencing idiom uses one.

## Comparative evidence and inference

### Why non-recursion is an elevation, not a choice

The kernel's rule — substitute only after the RHS is a value — already
means the RHS evaluates in an environment without the binder. A
"recursive let" would be a new form with a fixpoint or knot semantics,
not a reading of the existing one. So G031's "recursive bindings"
clause resolves honestly as: they do not exist locally; named
definitions carry recursion (kernel), and mutual recursion is the
module-level SCC (C024). Local recursive *functions* remain expressible
as named local bindings of closures in the surface era — G032's
question.

### Why the warning needs an exemption

An unused-binding warning that fires on `let _ = e1; e2` would flag
the normative sequencing form itself — self-defeating. The `_`-prefix
exemption is the standard resolution (Rust, OCaml, Erlang all mark
deliberate discard), and it keeps `BS001` honest: it warns on binders
that look intended for use but never occur.

## Selected model

> **Normative definitions (placed in the candidate chapters).**

### Binding structure

```text
let name = rhs ; body
```

- `name` is one value name; `rhs` evaluates in the environment *without*
  `name` (non-recursive); `body` evaluates with `name` bound to the
  RHS's value.
- Scope is sequential-lexical: the binding extends the environment for
  `body` alone; inner bindings shadow outer ones silently (C021).

### Recursion boundary

Named definitions recurse via the signed definition environment;
mutual recursion among definitions is C024's SCC. No local recursive
binding form exists; a let RHS referencing its own binder is `T001`
unbound.

### Unused bindings

Valid; RHS effects preserved (C030 schedule). `BS001` warns when a
non-`_`-prefixed binder never occurs in its body; deny promotes to
error.

### Sequencing

`let _ = e1; e2` is the normative sequencing form: e1 to a value
(effects observable), discarded, then e2.

### Rejected alternatives

- **Local recursive let / letrec-and** — G032/P034 territory.
- **Unused as hard error** — contradicts the kernel.
- **Silent only** — declines the cheap ergonomic.
- **Distinct sequence form** — unconformant with the retained AST.
- **Shadowing restrictions** — contradicts C021.
- **Descriptive module / normative-only** — rejected patterns.

## What C031 adds to the design

Section 4's structural core completes: values, order, and now
bindings. G032 (functions and calls) starts from a fixed binding
discipline; G033's branch forms bind into it; the stdlib era's
`Option`/`Result` idioms get their `let`-chain scaffold; and the
widened-P109 grammar gains the sequencing punctuation decision with
its semantics already fixed.

## Remaining questions and falsification criteria

G032 owns arity, currying as typing, closure capture, tail calls, and
named local functions; G033 branching; P034 termination; P035
equality; P109 all syntax; G088 cancellation mid-sequence.

The model should be revisited if G032's local-function work demands
value recursion for ergonomics (the remedy is a G032 slice adding
`fn`-knot semantics, not amending non-recursion here), or if linting
evidence shows `_`-exemption too coarse (the remedy is a refined
exemption rule in a later patch, not removing the warning).

## Connections

- The [resolved bindings inquiry](../40-inquiries/how-should-catena-define-bindings-and-sequencing.md)
  records the question, hypotheses, and outcome.
- The [Bindings and Sequencing map](../10-maps/bindings-and-sequencing.md)
  routes through the kernel rules, the shipped contracts, and the
  future owners.
- The [Bindings and Sequencing Specification](../60-specification/bindings-and-sequencing/README.md)
  defines the normative `0.1.27` contract this note argued for.
- [Catena Values and Evaluation](catena-values-and-evaluation.md) and
  [Catena Evaluation Order](catena-evaluation-order.md) are the
  trilogy's first two members.

## Sources

- [Sequential Dynamics](../60-specification/formal-semantic-kernel/sequential-dynamics.md)
- [Shadowing and Ambiguity](../60-specification/namespaces-and-shadowing/shadowing-and-ambiguity.md)
- [SCC Admission and Resolution](../60-specification/module-dependency-cycles/scc-admission-and-resolution.md)
- [Ordered Forms and Entry Rule](../60-specification/evaluation-order/ordered-forms-and-entry-rule.md)
- [Import Declarations and Admission](../60-specification/imports-and-exports/import-declarations-and-admission.md)
