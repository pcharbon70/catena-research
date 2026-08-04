---
title: "Guard Tree Semantics"
kind: specification
created: "2026-08-02"
status: normative
spec_version: "0.3"
tags:
  - compilers
  - pattern-matching
  - program-semantics
  - specification
aliases:
  - "Catena ordered condition selection"
---

# Guard Tree Semantics

## Ordered selection

For an ordinary match or multi-clause function, evaluation MUST:

1. evaluate the scrutinee or arguments exactly once;
2. consider clauses in source order;
3. test the next structural pattern without effects;
4. when the pattern fails, continue with the next clause;
5. when the pattern succeeds, establish its row-local bindings;
6. evaluate that clause's condition exactly once;
7. when the condition is `false`, discard row-local bindings and continue with
   exactly the next source clause;
8. when the condition is `true`, commit to the clause; and
9. evaluate only the committed body.

An omitted condition is `true`. A body failure, explicit crash, later effect,
or divergence occurs after commitment and MUST NOT resume clause selection.
Only condition value `false` performs ordinary fallthrough.

## Guard-tree core

Accepted clauses elaborate to an ordered acyclic guard tree with conceptual
nodes:

> **Normative definition.**

```text
PatternTest(pattern, success, failure)
ConditionTest(condition, yes, no)
Commit(body)
NoMatch
```

The typed representation records that it is exhaustive in ordinary contexts,
that condition false follows the source-order failure continuation, and that a
condition is not duplicated. The independent typed-core verifier MUST reject
a tree that is missing, not exhaustive where required, disconnected from its
checked clauses, or carries invalid condition evidence.

Implementations may share structural tests and continuations. They MUST NOT
move a condition before its pattern, across an overlapping earlier clause, or
into a body with different commitment behavior.

## Or-patterns

An or-pattern remains one source pattern. Its alternatives MUST bind the same
names at the same types as required by 0.2. The structural matcher may test
alternatives left to right, but after one alternative succeeds the shared
condition runs once.

Lowering an or-pattern to independent source clauses is invalid when that
could evaluate a shared condition more than once. A valid implementation may
lower alternatives to calls of one shared continuation, so overlapping
alternatives still have one condition evaluation and one fallthrough edge.

## Condition calls

Calling a verified predicate has the ordinary mathematical result of its
normalized body. An implementation may call, inline, specialize, or
constant-fold it when source evaluation order, result, and cost-visible failure
boundaries remain unchanged. Because 0.3 predicates are total, deterministic,
effect-free, and acyclic, inlining cannot introduce a new language-visible
failure.

## No exception-to-false rule

Catena does not inherit Erlang's behavior of treating specified guard
operation failures as failed guards. Every admitted 0.3 operation is defined
for all typed inputs. If a malformed typed core or foreign value violates that
invariant, the result is a compiler or dynamic-boundary defect, not selection
of the next source clause.

## Connections (non-normative)

Structural pattern rules remain in
[Match Semantics and Coverage](../data-and-patterns/match-semantics-and-coverage.md).
The relationship between tree leaves and certified facts is in
[Coverage and Fact Evidence](coverage-and-fact-evidence.md).
