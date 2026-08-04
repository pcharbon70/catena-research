---
title: "How Should Catena Design Clause Guards?"
kind: inquiry
created: "2026-08-01"
status: open
tags:
  - catena
  - compilers
  - language-design
  - pattern-matching
aliases:
  - "What guard semantics should Catena adopt?"
---

# How Should Catena Design Clause Guards?

## Why this matters

Clause guards sit at the boundary among pattern matching, Boolean computation,
effects, coverage, optimization, and BEAM selective receive. A guard that looks
like a small convenience can:

- make an otherwise structural match non-exhaustive;
- run more than once under an or-pattern or mailbox scan;
- hide a failure by falling through;
- introduce effects into clause selection;
- require facts beyond Hindley–Milner inference;
- prevent match-test reordering; or
- be impossible to lower as a native BEAM receive guard.

The initial language needs one coherent semantic contract before syntax,
standard predicates, diagnostics, or backend shortcuts become difficult to
change.

The developed proposal is in [Clause Guards](../20-notes/clause-guards.md);
the normative
[0.1.3 Clause Condition Specification](../60-specification/clause-conditions/README.md)
and published historical compiler implementation settle one exact total
fragment, typed receive harness, and evidence format. That implementation used
the retired identifier; the fresh `0.1.3` protocol-evidence gate is in the
[renumbering record](../50-journal/2026-08-04-prototype-slice-renumbering.md).
This inquiry remains open only for public syntax, usability, performance,
trait, recursive-totality, and complete receive semantics beyond that bounded
contract.

## Operational question

Determine whether Catena can implement a clause-condition system satisfying all
of these criteria:

1. Every accepted condition has type `Bool`, an empty effect row, and
   checkable evidence of total deterministic evaluation.
2. Interpretation, optimized matching, and BEAM code select the same clause
   for every typed input.
3. A false condition continues with exactly the next source clause, and a
   condition runs once per successful structural row attempt.
4. No solver guess can make a non-exhaustive match compile as exhaustive.
5. Selective receive never consumes, reorders, or duplicates a message because
   of guard lowering.
6. Common validation and routing predicates remain concise.
7. Diagnostics explain guard safety and missing fallbacks in task language.
8. Compile time and generated-code cost remain within a declared budget on
   representative and adversarial inputs.

Evidence sufficient to resolve the inquiry includes:

- a small formal or executable guard calculus;
- a typed guard-tree reference interpreter;
- a sound coverage checker with concrete witnesses;
- native and ordinary-branch BEAM backends;
- differential and property tests;
- representative function, match, and receive programs;
- measured compile-time and runtime behavior; and
- comprehension and repair tests for diagnostics.

## Working hypotheses

### H1: Boolean-only guards are the right initial surface

Pattern guards and local guard bindings save nesting but create a second
matching and scoping language. Real-program evidence should precede them.

### H2: empty effects are not a sufficient safety criterion

The initial fragment must also exclude partiality and unproved
nontermination. A pure Boolean function can still hang or fail.

### H3: guard safety must be checked, not asserted

Trusted primitives and non-recursive predicates checked in the guard fragment
can provide an initial usable core. An unchecked annotation would only rename
the problem.

### H4: structural coverage should remain authoritative

Guarded rows do not close a coverage gap unless a small trusted checker
establishes the proposition. Unknown and timeout both require an explicit
fallback.

### H5: one typed guard tree can connect semantics and compilation

Surface guards and patterns should elaborate into an ordered tree before
coverage, optimization, or BEAM-specific classification.

### H6: receive needs a stricter subset

Ordinary matches can lower non-native predicates as pure branches. Selective
receive initially needs operations that can be inlined into portable native
BEAM guard tests, because consuming and re-enqueuing a rejected message is not
semantics preserving.

### H7: guard-safe trait use needs explicit operational evidence

Coherent selection and mathematical laws do not prove termination or
totality. Built-in, derived, or separately verified trait methods can carry the
needed evidence.

## Paths to explore

### Semantics prototype

- Define `PatternTest`, `GuardTest`, `Commit`,
  sequencing, and source-order choice.
- Give ordinary matches, multi-clause functions, and receives separate
  terminal behavior.
- Test or-pattern overlap and one-evaluation semantics.
- Prove or test that a committed body failure never resumes selection.

### Guard-safe checker

- Inventory useful total primitives.
- Check empty effects independently of totality.
- Start with non-recursive user predicates and structural termination.
- Decide how imported signatures carry recheckable guard-safety evidence.
- Test trait method selection with built-in, derived, and user instances.

### Coverage prototype

- Extend the existing structural pattern matrix with a guard-tree front end.
- Report guarded missing witnesses and structural shadowing separately.
- Add a finite Boolean/literal oracle before integer arithmetic.
- Evaluate a proof-producing linear-integer solver with strict timeout and
  certificate rechecking.
- Include empty types, structural variants, or-patterns, and later GADT facts.

### BEAM prototype

- Map the portable primitive fragment to supported BEAM guard/test operations.
- Compare native and ordinary pure-branch lowering for matches and functions.
- Compile representative selective receives and verify mailbox order.
- Measure mailbox scan cost across queue sizes and rejection rates.
- Test supported OTP versions so portability is explicit.

### Usability study

- Ask programmers to predict selection order and guard evaluation count.
- Compare “clause condition” with “guard” in first-contact material.
- Test repair of effectful, partial, non-exhaustive, and receive-only errors.
- Compare nested matches with proposed pattern-guard notation on real tasks.

## Findings

### Comparative semantics

- [Erlang/OTP](../30-sources/erlang-otp-expressions-and-guard-sequences.md)
  restricts guard expressions to a side-effect-free subset, converts specified
  guard-operation failures into rejection, and uses guards during mailbox
  scanning.
- [OCaml](../30-sources/ocaml-5-4-expressions-and-pattern-guards.md)
  admits arbitrary Boolean expressions after successful patterns.
- [Haskell 2010](../30-sources/marlow-2010-haskell-language-report.md)
  combines Boolean, pattern, and local-binding guards and defines them by
  translation into nested matches and conditionals.
- [Rust](../30-sources/rust-reference-match-expressions.md) permits conditional
  matches and side effects, exposing multiple-evaluation and binding-lifetime
  questions.

### Coverage

- [Maranget's usefulness analysis](../30-sources/maranget-2007-warnings-pattern-matching.md)
  is a sound structural baseline but deliberately does not solve guards.
- [Lower Your Guards](../30-sources/graf-et-al-2020-lower-your-guards.md)
  shows that a small ordered guard-tree IR can unify rich surface constructs
  without requiring one monolithic source-pattern analysis.
- [Kalvoda and Kerckhove](../30-sources/kalvoda-kerckhove-2019-structural-semantic-pattern-matching.md)
  show that an SMT oracle can prove more arithmetic guard partitions, while
  also exposing translation, complexity, and integration costs.

### Backend

- The [Erlang efficiency guide](../30-sources/erlang-otp-function-matching-optimization.md)
  confirms that overlapping guarded rows constrain test reordering.
- Erlang's receive semantics makes guard lowerability a correctness issue, not
  only a performance opportunity.

### Provisional synthesis

The evidence currently favors:

- Boolean-only clause conditions;
- a checked effect-free and total fragment;
- no exception-to-false conversion;
- one guard evaluation after a successful row pattern;
- structural coverage by default;
- optional certified semantic facts;
- a typed guard-tree IR;
- dual native and ordinary-branch lowering; and
- a native-only portable subset for receive.

This synthesis preceded the bounded implementation result recorded next; its
wider trait, usability, and public receive claims remain proposals.

### Normative 0.1.3 semantics and historical implementation

Published sibling compiler commit
[`165fc4837f101d01016248e62479ef4caa0f20ce`](https://github.com/pcharbon70/catena/commit/165fc4837f101d01016248e62479ef4caa0f20ce)
implements the normative semantic answer under the retired `0.3` protocol
identifier with:

- exact `Bool`/`Int` operations and no ordinary or recursive calls;
- explicitly signed, first-order, acyclic condition predicates;
- canonical predicate bodies and dependency evidence in version 0.1.3 module
  interfaces;
- ordered guard-tree metadata and shared continuations for or-patterns;
- deterministic Boolean and integer difference-constraint coverage facts;
- forced native and ordinary BEAM lowering checked against the pure evaluator;
  and
- a native-only receive harness requiring one closed message type.

The [C003 evidence journal](../50-journal/2026-08-02-c003-executable-clause-condition-conformance.md)
records 46 passing tests on the pinned Elixir/OTP 29 toolchain. Nonlinear
arithmetic remains conservatively unknown for coverage, and no external SMT
solver participates in acceptance.

This establishes historical executable conformance for the bounded semantic
kernel. It does not establish the renumbered wire identity or provide
performance measurements, mailbox experiments, or usability results for later
extensions.

## Outcome

Open, with the 0.1.3 semantic core resolved. The normative specification and
published compiler evidence agree on the bounded corpus. Remaining work asks
whether later predicate, diagnostic, performance, usability, and public
receive extensions are practical; it no longer blocks C003. The
[Clause Guards map](../10-maps/clause-guards.md) is the curated route through
current evidence.
