---
title: "Catena Branching"
kind: note
created: "2026-08-25"
maturity: developing
tags:
  - catena
  - language-design
  - branching
  - conditionals
  - match
aliases:
  - "Catena branching model"
---

# Catena Branching

## Executive conclusion

Catena's branching model at `0.1.29` is **match, and only match**. The
match expression is the single branch form: one scrutinee, evaluated
once; clauses tested in source order, each testing its pattern before
its condition; a `Bool` condition evaluated exactly once on structural
success; a false condition falling through to later clauses; selection
committing irreversibly to the chosen body. **Branch typing** is
clause-body unification with the match's type; **missing
alternatives** are `M001` rejections carrying a witness value.
Everything is an expression: clause bodies yield the match's value,
and there are **no statement-like control forms** — no early return,
no break, no statement tier — declared normatively as an absence.

The **conditional sugar promise** fixes what any future conditional
surface spelling means before P109 draws it: `if`-like spellings
desugar to a match on a `Bool` scrutinee with `true`/`false` patterns,
and `when`-guarded spellings to C003's clause conditions — shipped
semantics, new punctuation only. This is the C032 multi-param-sugar
pattern applied to branching: freeze the desugaring now so the grammar
exercise consumes fixed semantics instead of inventing them.

The consolidated rules cite their homes: C002 owns match typing,
coverage, and redundancy; C003 owns the condition fragment; C010 owns
commitment dynamics; C029 owns the `and`/`or` skips conditions may
use; C030 owns the scrutinee and clause schedules; C032's tail
guarantee covers a call after clause selection. The deliverable is
witness evidence with **zero new diagnostic families** — the
definitional stance of the whole sibling run.

## Scope and method

The operational target is independent agreement on the single branch
form, the sugar promise, the statement absence, and the consolidated
rule table — made executable through evaluator/BEAM witnesses.
Primary evidence is internal: [C002's match and coverage](../60-specification/data-and-patterns/match-semantics-and-coverage.md),
[C003's condition fragment](../60-specification/clause-conditions/syntax-and-safety.md),
[C010's commitment dynamics](../60-specification/formal-semantic-kernel/sequential-dynamics.md),
and the C029–C032 siblings. Source claims stay distinct from Catena
proposals below.

## Relation to the current corpus

[C002](../60-specification/data-and-patterns/match-semantics-and-coverage.md)
fixed match expressions for the whole language: scrutinee typing,
ordered clauses, compile-time exhaustiveness with `M001` missing
witnesses, redundancy rejection, and the coverage calculus. C033
consolidates; it changes none of it and owns none of it.

[C003](../60-specification/clause-conditions/syntax-and-safety.md)
fixed the `pattern when condition -> body` fragment: `Bool`-typed
conditions from the closed safe operator set, exactly-once evaluation,
false fallthrough, irreversible commitment. Condition *purity* is part
of that answer — conditions are the side-effect-free fragment — so
branch-order observables come from scrutinee and body effects, not
condition effects.

[C010](../60-specification/formal-semantic-kernel/sequential-dynamics.md)
fixes the dynamic rule (scrutinee once, source order, commit), which
[C030](../60-specification/evaluation-order/ordered-forms-and-entry-rule.md)
scheduled and which [C032](../60-specification/functions-and-calls/closures-and-tail-calls.md)
extended into tail position — a call after pattern selection keeps
the proper-tail-call guarantee, witnessed by C032's five-million-
iteration recursion.

[C029](../60-specification/values-and-evaluation/strictness-and-terminal-outcomes.md)
gated the `and`/`or` right-operand skips conditions may compose with;
[C031](../60-specification/bindings-and-sequencing/unused-bindings-and-sequencing.md)
supplies the effect-sequencing idiom that replaces statement forms.

## Comparative evidence and inference

### Why match-only is an elevation, not a choice

The retained inputs' tags are frozen — no `if` expression exists on
any compilable input, and every conditional in the corpus's evidence
is already a match on `Bool` or a guarded clause. A separate
conditional form would be redundant surface for semantics match
already carries, which is exactly what the sugar promise records:
P109 gets spelling freedom over fixed meaning.

### Why the statement absence is an answer, not a gap

The kernel's everything-is-an-expression architecture (values from
bodies, effects through the let idiom, traps as terminals) leaves no
room for a statement tier without a second sequencing semantics. The
checklist's question — "whether any statement-like control forms
exist" — therefore has a truthful negative answer, and declaring it
normatively forecloses early-return and break proposals before they
can fragment the architecture.

## Selected model

> **Normative definitions (placed in the candidate chapters).**

### The branch form

```text
match scrutinee { clause* }        -- the only branch form
clause := pattern [when condition] -> body
```

### The sugar promise

```text
if e then a else b     ⟹    match e { true -> a, false -> b }
```

Any future conditional spelling desugars to match (Bool patterns) or
to C003 clause conditions; its semantics are shipped semantics.

### The consolidated rules (cited)

| Rule | Home |
| --- | --- |
| Scrutinee evaluates once, before clause tests | C002/C030 |
| Clauses test in source order; pattern before condition | C003/kernel |
| Condition is `Bool`, evaluated exactly once on structural success | C003 |
| False condition falls through; selection commits irreversibly | C003/kernel |
| Branch typing: bodies unify with the match's type | C002 |
| Missing alternatives: `M001` with witness; redundancy rejected | C002 |
| `and`/`or` composition with the C029 skips | C010/C029 |
| A call after clause selection keeps the tail guarantee | C032 |

### Statement forms

None exist. Sequencing-for-effect is C031's let idiom; branching
yields values; there is no early return, break, or statement tier,
and any future exception enters through the edition-record gate.

### Rejected alternatives

As enumerated in the resolved inquiry: new `if` form now, match-only
without the promise, reserved statement tier, deferred statement
question, extending C002/C003, residuals-only chapter, new branch
warnings, normative-only.

## What C033 adds to the design

Section 4's gaps close: values, order, bindings, functions, and
branching each have their language-level chapter. The stdlib era's
`Option`/`Result` combinators get their dispatch semantics fixed
before contents exist; and the widened-P109 grammar exercise receives
the conditional desugaring and the confirmed no-statement discipline
as inputs rather than questions.

## Remaining questions and falsification criteria

P034 owns termination beyond tail guarantees; G036 owns the failure
taxonomy (a trap during scrutinee evaluation is G036's to classify);
G040 owns each future scrutinee type's coverage entries; P109 owns
all spellings, consuming the sugar promise; G088 owns cancellation
mid-branch.

The model should be revisited if P109's ergonomics genuinely demand a
non-desugaring conditional (the remedy is an edition record naming the
form and why match's semantics are insufficient), or if the runtime
era needs structured exits (the remedy is a G084 slice composing with
traps, not a statement tier).

## Connections

- The [resolved branching inquiry](../40-inquiries/what-is-catenas-branching-model.md)
  records the question, hypotheses, and outcome.
- The [Branching map](../10-maps/branching.md) routes through the
  shipped fragments and the future owners.
- The [Branching Specification](../60-specification/branching/README.md)
  defines the normative `0.1.29` contract this note argued for.
- The sibling syntheses — [values](catena-values-and-evaluation.md),
  [order](catena-evaluation-order.md),
  [bindings](catena-bindings-and-sequencing.md),
  [functions](catena-functions-and-calls.md) — are the completed run
  this finishes.

## Sources

- [Match Semantics and Coverage](../60-specification/data-and-patterns/match-semantics-and-coverage.md)
- [Syntax and Safety](../60-specification/clause-conditions/syntax-and-safety.md)
- [Sequential Dynamics](../60-specification/formal-semantic-kernel/sequential-dynamics.md)
- [Strictness and Terminal Outcomes](../60-specification/values-and-evaluation/strictness-and-terminal-outcomes.md)
- [Ordered Forms and Entry Rule](../60-specification/evaluation-order/ordered-forms-and-entry-rule.md)
- [Proper Tail Calls](../60-specification/functions-and-calls/closures-and-tail-calls.md)
