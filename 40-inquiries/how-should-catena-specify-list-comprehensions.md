---
title: "How Should Catena Specify List Comprehensions?"
kind: inquiry
created: "2026-08-01"
status: open
tags:
  - catena
  - comprehensions
  - language-design
aliases:
  - "Catena list comprehension design"
---

# How Should Catena Specify List Comprehensions?

## Why this matters

A list comprehension appears to be compact collection syntax, but it fixes a
large operational boundary. Its meaning includes pattern failure, nested
traversal, binding scope, effect repetition, output order, failure timing,
allocation, and the relationship between language syntax and categorical
operations.

Catena's architecture makes these choices unusually consequential:

- algebraic data patterns are exhaustive by default;
- clause guards use a total effect-free fragment;
- ordinary effects remain visible in type rows;
- categorical `map` remains pure and law-bearing;
- the BEAM rewards tail-recursive fused list loops; and
- approachable syntax should not require programmers to infer semantics from
  monad vocabulary or punctuation.

The [synthesis](../20-notes/list-comprehensions.md) motivated the narrow initial
contract adopted in normative `0.1.39`. This inquiry is reopened for
P050/P053/P057: the required executable witnesses for effectful filters,
effect order, and failure timing are incomplete. The existing semantic roles,
effect boundary, and binding rules remain fixed; P109 retains concrete source
adoption, with usability, performance, and extensions owned separately.

## Operational question

Can one list-comprehension design let programmers correctly predict:

1. source and result types;
2. nested versus lockstep traversal;
3. total versus intentionally filtering patterns;
4. left-to-right scope and evaluation;
5. the count and order of effects;
6. failure propagation and partial effects;
7. result order and cardinality; and
8. BEAM cost;

without learning category-theory terminology or inspecting generated
`map`/`flat_map` calls?

The original research program asked for:

- a grammar integrated with the complete expression syntax;
- declarative typing and effect rules;
- a small-step or executable dynamic account;
- a typed qualifier-tree elaboration;
- coverage and scope diagnostics;
- a reference evaluator and BEAM differential suite;
- representative usability evidence; and
- benchmark evidence for allocation and stack behavior.

The bounded `0.1.39` promotion separated these goals: it fixed the semantics
and dormant elaboration boundary, transferred complete source adoption to
P109, and left usability and performance to G137/G138. The current reopening
concerns required executable evidence within that promoted boundary, as
specified in the [resolution criteria](#resolution-criteria).

## Original working hypotheses

These hypotheses preserve the research route. The `0.1.39` specification now
fixes the initial source/result carrier, generator split, filters, scope,
effect order, elaboration, and exclusion boundaries.

1. **Lists should be the only initial source and result carrier.** One concrete
   shape gives the feature a stable order, emptiness, builder, and failure
   contract.
2. **Ordinary generator patterns should be total.** An unintended partial
   pattern should be a compile error rather than data loss or a runtime match
   failure.
3. **Refutable filtering should be explicit.** A word-level marker such as
   `case` will communicate intent more reliably than a punctuation change.
4. **Filters should be typed `Bool`, not truthy values.** Non-Boolean results
   are static errors and ordinary failures propagate.
5. **Comprehension filters need not be clause guard-safe.** Effect rows and an
   exact execution order can make repeated effects visible without conflating
   filtering with coverage or selective receive.
6. **Multiple generators should be nested and depth-first.** Zip remains an
   explicit `zip_exact` or `zip_shortest` operation until dedicated syntax
   proves necessary.
7. **The semantic target should be a typed qualifier tree.** Pure equations
   with `map` and `flat_map` aid reasoning, but open trait dispatch should not
   define execution.
8. **The backend should fuse into tail-recursive workers.** A reversed
   accumulator plus one final reverse should preserve order without
   intermediate mapped and filtered lists.
9. **Generic monad comprehensions should be deferred.** Monad structure does
   not supply filtering zero, evaluation order, effect multiplicity, or output
   policy.
10. **Streams, binaries, maps, reduction, and parallel traversal need separate
    contracts.** Adding them as options would obscure resource and failure
    boundaries.

## Paths to explore

### Surface comprehension studies

Compare at least these schematic forms with programmers who do not know
Haskell or Scala:

```text
for
  item in items
  when item.active
yield item.name
```

```text
collect item.name
from item in items
when item.active
```

```text
[item.name | item in items, item.active]
```

Measure:

- time to identify source and result;
- predicted order and cardinality;
- predicted effect count;
- interpretation of pattern mismatch;
- confusion with imperative loops; and
- repair success after a compiler diagnostic.

### Pattern-intent study

Test ordinary and explicitly filtering patterns over `Option`, `Result`, and
sum types:

```text
Some(value) in values
case Some(value) in values
matching Some(value) in values
```

Determine whether `case`, `matching`, or another task word best communicates
“skip nonmatching elements” and whether users understand the total-pattern
error.

### Effect study

Construct programs with effects in:

- the outer source;
- a dependent inner source;
- a local binding;
- a filter;
- the result expression; and
- failure after earlier effects.

Ask users to predict the trace, then compare pure-only, fully effectful, and
restricted-filter variants. Record whether displayed effect rows plus
multiplicity diagnostics are sufficient.

### Formal model

Define a typed qualifier tree with:

```text
EachTotal
EachCase
Keep
BindTotal
Yield
```

Prove or test:

- type preservation through elaboration;
- lexical scope preservation;
- total-generator match success;
- filtering mismatch as the only implicit skip;
- order and effect-trace preservation;
- equivalence of the pure subset with list `map`, filtering, and `flat_map`;
  and
- semantic preservation of the fused worker lowering.

### Backend experiments

Compare:

1. a qualifier-tree reference interpreter;
2. direct recursive source code;
3. calls to list library operations;
4. fused private workers with reversed accumulation; and
5. native-compatible Erlang/Core Erlang comprehension lowering where safe.

Measure runtime, allocation, reductions, code size, compile time, stack use,
failure traces, and source debugging on empty, long, highly filtered, and
Cartesian inputs.

### Extension pressure

Gather real examples before adding:

- exact or shortest zip qualifiers;
- iterators and lazy streams;
- binary parsing and construction;
- map or set result builders;
- reduction and early termination;
- sorting, grouping, and uniqueness;
- effect-only loops; and
- structured parallel traversal.

For each request, record whether an explicit library operation is clearer and
whether syntax would avoid a measured allocation or diagnostic problem.

## Findings

### Primary language evidence

- The [Haskell report](../30-sources/marlow-2010-haskell-language-report.md)
  gives list comprehensions a nested depth-first translation through
  `concatMap`, with silent generator-pattern skipping and separate local
  declarations.
- The [Erlang reference](../30-sources/erlang-otp-expressions-and-guard-sequences.md)
  demonstrates list, binary, and map targets; strict and relaxed patterns;
  nested and zip traversal; and filter failure tied to syntactic class.
- [EEP 70](../30-sources/erlang-eep-70-strict-and-relaxed-generators.md)
  documents silent data loss as sufficient motivation for an explicit strict
  form in a production language.
- [EEP 73](../30-sources/erlang-eep-73-zip-generators.md) demonstrates that
  lockstep traversal adds length, pattern, evaluation, precedence, diagnostic,
  and allocation decisions.
- [Elixir](../30-sources/elixir-1-20-comprehensions.md) demonstrates the
  convenience and breadth of a generic effectful `Enumerable`/`Collectable`
  form on the BEAM.
- [Scala](../30-sources/scala-3-4-for-comprehensions.md) demonstrates an
  explicit `case` marker for refutable filtering and carrier-provided
  `map`/`flatMap`/`withFilter` translation.

### Formal evidence

- [Wadler](../30-sources/wadler-1992-comprehending-monads.md) shows that
  dependent generator composition has a monadic account but Boolean filtering
  needs an additional zero operation and laws.
- [Peyton Jones and Wadler](../30-sources/peyton-jones-wadler-2007-comprehensive-comprehensions.md)
  show that grouping, ordering, zip, and arbitrary transformations can be
  formalized, while also changing qualifier scope and binder types.

### Current inference

The evidence favors a concrete list feature over a generic abstraction
surface. It also favors separating total and filtering patterns at the source
level. These are cross-source inferences, not conclusions established by any
one comparison language.

### Completion audit

The [2026-09-06 audit](../50-journal/2026-09-06-checklist-completion-audit.md)
compared the required
[conformance evidence](../60-specification/list-comprehensions/diagnostics-and-conformance.md#conformance-obligations)
with the actual sibling compiler suite. The
[filter test](https://github.com/pcharbon70/catena/blob/d7e0fcc484d3e1c3b4a292d4d3e703ddcc330535/test/catena/c047_list_comprehensions_test.exs#L113)
executes pure filtering and rejects a non-`Bool` filter; despite its name, it
does not execute a failing filter. The
[order and sequential-execution test](https://github.com/pcharbon70/catena/blob/d7e0fcc484d3e1c3b4a292d4d3e703ddcc330535/test/catena/c047_list_comprehensions_test.exs#L206)
checks generated conditional and `(uses Ask)` text and absent parallel APIs.
It contains no request or handler and does not execute the generated
program carrying the effect-row annotation.

The [original evidence record](../50-journal/2026-08-31-c047-comprehensions.md#evidence)
accurately describes this as effect-row threading. That evidence supports
part of `LC-OBL-005`, `LC-OBL-008`, and `LC-OBL-012`, but the
[required evidence set](../60-specification/list-comprehensions/diagnostics-and-conformance.md#required-evidence-sets)
also requires an effect-bearing comprehension with a source-order trace.
P050/P053/P057 therefore remain partial even if all existing tagged tests
pass. Pure execution, diagnostics, the worker shape, and the dormant API
remain accomplishments.

## Resolution criteria

Resolve the reopened P050/P053/P057 evidence question when the sibling compiler
provides tagged executable witnesses satisfying the existing
[filter, order, and sequential-execution obligations](../60-specification/list-comprehensions/diagnostics-and-conformance.md#conformance-obligations):

1. A comprehension with actual handled requests runs through
   `Catena.Comprehension.elaborate/1`, kernel checking, the reference stepper,
   and compiled BEAM. Its exact traces agree across nested sources, filters,
   bindings, and yields, including once-per-prefix source evaluation and
   completion of each element's suffix before the next element (`LC-OBL-008`).
2. An effectful filter returning `false` performs its own effect once and skips
   only its suffix. A trapping filter and a handler-aborting qualifier stop
   later qualifiers and elements, with agreeing outcomes and traces on both
   targets (`LC-OBL-005`, `LC-OBL-008`).
3. The executed trace witnesses establish sequential source order, and the
   existing parallel-entry-point absence tests remain covered
   (`LC-OBL-012`).
4. The evidence record identifies the tested compiler revision and results;
   the checklist and traceability registry are reconciled with what those
   tests actually exercise.

Source-grammar integration remains P109; usability G137; performance G138;
and neighboring iteration forms D059. These separate owners do not change the
above evidence gate or reopen the shipped normative semantics.

## Outcome

The [2026-08-31 promotion](../50-journal/2026-08-31-c047-comprehensions.md)
recorded C047–C058 complete at revision `0.1.39` (area `list-comprehensions`):
an eager, ordered, `List A → List B` `for ... yield` expression with
total generators, explicitly filtering `case` generators, typed
Boolean `when` filters, exhaustive local `let` bindings, visible
effects, and depth-first left-to-right sequential execution. The
contract is authoritative in the
[normative chapters](../60-specification/list-comprehensions/README.md), the
reasoning in the
[synthesis](../20-notes/list-comprehensions.md), and the forks in
the [design decision register](../20-notes/design-decision-register.md).

The completion audit reopens P050/P053/P057 for the missing runtime witnesses
above; it does not withdraw the normative revision or the implemented
elaborator. The inquiry is now open until those witnesses are recorded.

Token-level syntax reliability
testing belongs to the P109 surface-grammar adoption: this slice
fixes the grammar's semantic roles and keywords normatively, while
punctuation, layout, and block forms integrate with the complete
concrete grammar there. And the implementation is dormant by the
frozen-frontend constraint: the elaborator
(`Catena.Comprehension.elaborate/1`, qualifier tree to kernel
S-expressions) is implemented, tested, and validated by
pure desugaring-equivalence on stepper and BEAM — the first
comprehension-bearing frontend arrives with P109. D059's
neighboring iteration syntax (ranges, zip, streams, binary and map
comprehensions, generic collectors) remains independently
researched.

The evidence route is curated in the
[List Comprehensions map](../10-maps/list-comprehensions.md).
