---
title: "Catena Compile-Time Evaluation"
kind: note
created: "2026-08-26"
maturity: developing
tags:
  - catena
  - language-design
  - compile-time-evaluation
  - derivations
aliases:
  - "Catena compile-time model"
---

# Catena Compile-Time Evaluation

## Executive conclusion

Catena's answer to G038 at `0.1.34` is a decision, not a design.
**No user-authored code executes during compilation beyond the three
already-bounded meta-evaluators** — condition normalization (acyclic,
C003), specification-example checking (20,000 steps, C006), and law
checking (bounded samples, C004). **Constants never execute**:
definitions compile, they do not run. **No attribute system and no
macro system exist**; if either ever arrives, it enters through its
own slice under C034's gate — total-or-bounded in the admitting
change, never unbounded, never as a compatible addition.

**Generated derivations classify as compiler-internal generation,
not execution.** The shipped derivation engine (`Catena.Derive`)
emits folds and capabilities by template over declared types: it
evaluates no user expression, marks every derived definition with
`compiler_derived` provenance, is deterministic and total by
construction (structural recursion over finite declarations), and its
output is ordinary checked definitions that flow through the same
inference, verification, and erasure as handwritten ones.

The **restriction table** — C034's gate plus the three shipped
budgets — is the complete totality and determinism set at `0.1.34`,
cited in one place. The deliverable is witnesses with **zero new
diagnostic families**: the derivation provenance regression with
byte-identical recompilation, the three budget regressions, the
absence matrix, and determinism.

## Scope and method

The operational target is independent agreement on the stance, the
derivations classification, and the restriction table — made
executable through the witness set. Primary evidence is internal:
[C034's gate](../60-specification/recursion-and-termination/the-separation-table.md),
the three shipped meta-evaluators
([C003](../60-specification/clause-conditions/diagnostics-and-conformance.md),
[C006](../60-specification/specifications-and-governance/claims-examples-and-checking.md),
[C004](../60-specification/traits-and-categorical-operations/README.md)),
and the derivation engine's provenance model (`Catena.Derive`).
Source claims stay distinct from Catena proposals below.

## Relation to the current corpus

[C034's separation table](../60-specification/recursion-and-termination/the-separation-table.md)
listed compile-time evaluation as its gated row; this slice is the
gate's consumer becoming its owner. Nothing in C034 changes — the
entry rule is inherited verbatim and restated as this area's first
normative rule.

The three meta-evaluators are frozen with their budgets; this slice
cites them as the complete shipped set, exactly as C030's table
consolidated the order fragments.

[C002's derivation engine](../60-specification/data-and-patterns/README.md)
and [C004's capability derivations](../60-specification/traits-and-categorical-operations/README.md)
generate definitions marked `generated?: true` with
`provenance: :compiler_derived` — the shipped fact this slice
classifies: generation, not execution. The distinction matters for
the gate: a future derivation that *evaluated user code* (say, a
derive-that-runs-a-law) would be execution and would need its own
gated slice; today's derivations never do.

[C006's 20,000-step checker](../60-specification/specifications-and-governance/claims-examples-and-checking.md)
remains the canonical budget precedent; C034's stance chapter
already cites divergence as budget exhaustion — the same discipline
this table consolidates.

## Comparative evidence and inference

### Why a decision, not a design

The checklist says "decide whether." Nothing exists to design: no
constant form, no attribute syntax, no macro spelling — all P109-era
surface. Designing semantics for forms that cannot even be written
would invert the corpus's own method (C032's sugar promise fixed
*meanings* for spellings P109 will draw; here there is no meaning to
fix because there is no form). The decision — absence, gated — is
the truthful completion, and it protects the compiler: no
const-eval, macro, or attribute evaluator can arrive as a compatible
addition.

### Why derivations are not execution

The derivation engine is a total function from declarations to
definitions: structural recursion over finite datatype declarations,
emitting typed core. It never calls an evaluator, never reduces a
user expression, and its determinism is the compiler's own
(byte-identical recompilation, already witnessed since C002).
Classifying it as execution would subject template generation to a
gate designed for user-code evaluation — a category error that
would also misdescribe the provenance system the interfaces already
carry.

## Selected model

> **Normative definitions (placed in the candidate chapters).**

### The stance

| Form | Decision at 0.1.34 |
| --- | --- |
| Constants | never execute — definitions compile, not run |
| Attributes | no attribute system exists |
| Macros | no macro system exists |
| Generated derivations | compiler-internal generation, no user code |

Any arrival: its own slice, under C034's gate.

### The restriction table

| Evaluator | Regime | Home |
| --- | --- | --- |
| The gate itself | total-or-bounded in the admitting slice; no unbounded arrival | C034 |
| Condition normalization | acyclic, budgeted | C003 |
| Specification examples | 20,000 semantic steps | C006 |
| Law checking | bounded samples | C004 |

### Rejected alternatives

As enumerated in the resolved inquiry.

## What C038 adds to the design

Section 4 closes except for P041's edge: every core-expression
question now has a language-level answer. The optimizer and tooling
eras gain a precise promise — compilation is checking plus
generation, never silent execution — and G040's deriving extensions
arrive into a classified home rather than an open question.

## Remaining questions and falsification criteria

P109 owns spellings for any future const/macro/attribute surface;
G040 owns deriving extensions, classified under this area's rules on
arrival; G005/G116 own code-generation programs; G121 owns build
tooling.

The model should be revisited if the stdlib era demands constant
folding (the remedy is a gated const-eval slice with a bounded
evaluator — the gate already prices it), or if derive extensions
want to run user code (the remedy is a new gated evaluator in its
own slice, never an amendment here).

## Connections

- The [resolved compile-time inquiry](../40-inquiries/what-executes-during-compilation.md)
  records the question, hypotheses, and outcome.
- The [Compile-Time Evaluation map](../10-maps/compile-time-evaluation.md)
  routes through the gate, the shipped evaluators, and the future
  owners.
- The Compile-Time Evaluation Specification (candidate, then
  normative at promotion, in
  `60-specification/compile-time-evaluation/`) will define the
  contract this note argues for.
- [Catena Recursion and Termination](catena-recursion-and-termination.md)
  fixes the gate this slice inherits.

## Sources

- [The Separation Table](../60-specification/recursion-and-termination/the-separation-table.md)
- [Clause Conditions Diagnostics](../60-specification/clause-conditions/diagnostics-and-conformance.md)
- [Claims, Examples, and Checking](../60-specification/specifications-and-governance/claims-examples-and-checking.md)
- [Traits README](../60-specification/traits-and-categorical-operations/README.md)
- [Data and Patterns README](../60-specification/data-and-patterns/README.md)
