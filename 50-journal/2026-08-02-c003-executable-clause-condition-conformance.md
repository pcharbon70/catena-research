---
title: "C003 Executable Clause Condition Conformance"
kind: journal
created: "2026-08-02"
tags:
  - compilers
  - pattern-matching
  - specification
aliases:
  - "C003 implementation evidence"
---

# C003 Executable Clause Condition Conformance

## Observations

The sibling Catena compiler now has a published implementation of the
normative 0.3 clause-condition contract at commit
[`165fc4837f101d01016248e62479ef4caa0f20ce`](https://github.com/pcharbon70/catena/commit/165fc4837f101d01016248e62479ef4caa0f20ce).
It was merged into `rewrite` through
[compiler PR #65](https://github.com/pcharbon70/catena/pull/65). The change
extends the Elixir bootstrap directly and
still targets only the BEAM through Erlang/OTP 29 Abstract Format and
`compile:noenv_forms/2`.

The implementation adds:

- JSON AST 0.3 condition declarations, unary and binary condition operations,
  and same-arity multi-clause definitions;
- explicit monomorphic `Int`/`Bool` predicate signatures ending in `Bool`;
- closed safe-core normalization, acyclic dependency checking, transitive
  inlining, and a minimum 20,000-node budget;
- exact primitive operator typing and lazy Boolean evaluation;
- ordered guard-tree metadata and shared clause continuations that preserve
  one evaluation for an or-pattern's condition;
- conservative coverage reasoning over Boolean formulas and mathematical
  integer difference constraints;
- version 0.3 interfaces with canonical condition core and nested evidence
  digests, while retaining version 0.2 decoding;
- explicit condition imports;
- forced native and ordinary lowering for differential testing; and
- a typed native selective-receive lowering harness over one closed message
  type.

No Python, Rust, Core Erlang emitter, BEAM assembler, public receive AST, trait
operator, effect implementation, or external SMT dependency was added.

## Evidence

Environment observed in the sibling compiler repository:

```text
branch: agent/c003-clause-conditions
baseline rewrite commit: ae311604ef587a022ce2b7b46599200fcb96a7ab
implementation commit: 165fc4837f101d01016248e62479ef4caa0f20ce
merge commit: a4c4a053c02dc13411afde9a2c462aae989ddff3
pull request: https://github.com/pcharbon70/catena/pull/65
Elixir: 1.20.2
Erlang/OTP: 29.0.4
target: BEAM only
```

Commands run from `/home/ducky/code/catena`:

```bash
mix format --check-formatted
mix clean
mix compile --warnings-as-errors
mix test
mix escript.build
git diff --check
```

Observed test result:

```text
Compiling 28 files (.ex)
Generated catena app
Running ExUnit
..............................................
Finished in 0.3 seconds
Result: 46 passed
Generated escript catena with MIX_ENV=dev
```

The new conformance module exercises:

- negative, zero, and positive integer partitions;
- reference-evaluator, native-BEAM, and ordinary-BEAM agreement;
- safe predicate declarations, forward references, cycles, wrong result types,
  disallowed ordinary and higher-order calls, malformed operators, and minimum
  budgets;
- exact redundancy proofs and conservative nonlinear unknowns;
- interface export, explicit import, inlining, round trip, and independently
  tampered nested evidence;
- earlier AST rejection of 0.3 operations; and
- closed-message receive-harness acceptance and rejection.

Existing C001 and C002 cases remain green in the same 46-test run.

## Promotion result

The full command sequence above was rerun with the immutable implementation
commit checked out. The branch was then published and merged by compiler PR
#65. The [0.3 specification](../60-specification/clause-conditions/README.md)
is therefore normative and checklist item C003 is complete.

The [clause-condition inquiry](../40-inquiries/how-should-catena-design-clause-guards.md)
remains open only for later usability, performance, trait, recursive-totality,
and public receive work; those questions do not weaken the bounded 0.3
contract.

## Threads

The executable slice supports one decision-complete semantic core, but it does
not settle public parser syntax, usability, performance, public receive and
timeout semantics, trait-safe operations, recursive total predicates, or an
integrated effect and process calculus. Those are later decisions rather than
hidden capabilities of the prototype.

The fact checker carries normalized, recheckable compiler evidence and uses no
external solver. Its current implementation recognizes only the specified
difference-constraint fragment; nonlinear arithmetic remains valid runtime
condition code but unknown for coverage.

## Follow-ups

1. Treat public receive syntax, timeouts, process effects, traits, recursive
   totality, performance, and usability as separate follow-up work.
2. Preserve commit `165fc4837f101d01016248e62479ef4caa0f20ce` as the
   conformance identity for any implementation claim tied specifically to
   Catena 0.3.
