---
title: "List Comprehensions"
kind: note
created: "2026-08-01"
maturity: stable
tags:
  - catena
  - comprehensions
  - functional-programming
  - language-design
aliases:
  - "Catena list comprehensions"
---

# List Comprehensions

## Executive conclusion

Catena should begin with one deliberately small comprehension: an eager,
ordered expression that consumes lists and returns a list. It should make four
qualifier roles distinct:

1. a **total generator** whose pattern must match every element;
2. an explicitly marked **filtering generator** whose pattern may reject an
   element;
3. a typed Boolean **filter**; and
4. an exhaustive local **binding**.

The surface should read in execution order, provisionally using a familiar
`for ... yield` shape. Exact punctuation remains open, but failure behavior
must not be encoded by a subtle punctuation variant. An illustrative form is:

```text
for
  order in orders
  item in order.items
  when item.available
  let total = item.price * item.quantity
yield {order.id, total}
```

Refutable pattern filtering should be visibly requested:

```text
for
  case Some(value) in values
yield value
```

Without `case`, `Some(value) in values` is rejected when `values` has element
type `Option A`, because the pattern does not cover `None`. This prevents a
data-quality assertion from silently becoming a filter.

Comprehensions may contain effectful source, filter, binding, and result
expressions, but their inferred effect row and their exact left-to-right,
depth-first execution order must remain visible. This form is a control-flow
construct, not a claim that categorical `map` has become effectful.

The initial form should not be generic over `Monad`, `Foldable`, `Enumerable`,
or an output builder. It should not include zip, parallelism, streams,
grouping, sorting, reduction, uniqueness, or binary and map targets. Those are
useful operations with independent failure, order, resource, and law contracts.

## Question, scope, and decision standard

### Research question

How can Catena provide concise list construction without hiding pattern
failure, effect repetition, evaluation order, collection policy, or
category-theory machinery?

### Scope

This note covers:

- generator, filter, and local-binding syntax;
- nested traversal and lexical scope;
- refutable pattern behavior;
- static types and effects;
- dynamic evaluation order and failure;
- extensional desugaring and normative elaboration;
- BEAM lowering, allocation, stack safety, and optimization;
- diagnostics and approachable vocabulary; and
- boundaries with traits, algebraic effects, guards, streams, zip, and query
  syntax.

It does not settle Catena's complete lexical grammar or collection library. All
surface examples are schematic until the broader grammar is designed.

### Operational standard

A complete comprehension design must let a reader predict, without knowing its
compiler translation:

- which input elements are visited and in what order;
- which pattern mismatches are rejected, skipped, or propagated;
- when each expression runs and how often;
- which names are in scope at each point;
- which effects and failures the whole expression may expose;
- which collection is returned and in what order;
- whether an optimization may change an effect trace or failure point; and
- the asymptotic source visits and output allocation.

“Syntactic sugar for map and filter” does not meet this standard. It states an
intuition while leaving the operational contract underspecified.

## Evidence method

The evidence trail combines three kinds of primary work:

- language definitions for Haskell, Erlang/OTP, Elixir, and Scala;
- accepted Erlang proposals that isolate strict pattern failure and zip
  traversal; and
- original papers deriving monad comprehensions and later query-like
  extensions.

The comparison separates reported language behavior from the Catena proposal.
No sibling Catena implementation or guide is treated as evidence.

## Terms that must remain distinct

### Comprehension

A **comprehension** builds zero or more output elements by evaluating a result
expression in environments produced by an ordered qualifier sequence.

The term says nothing by itself about source types, output type, strictness,
effects, or parallelism.

### Generator

A **generator** evaluates a source collection, visits its elements, matches a
pattern, and introduces bindings for later qualifiers and the result.

Multiple ordinary generators are nested. They do not zip merely because they
are adjacent.

### Total generator

A **total generator** promises that its pattern covers the source element type.
Its pattern selects fields and introduces names but does not filter.

```text
item in items
{key, value} in entries
```

The second example is valid only when the element type is known to be a pair.

### Filtering generator

A **filtering generator** explicitly requests a refutable pattern. A mismatch
skips the current source element and continues with the next one.

```text
case Some(value) in values
```

This is selection by data shape, not an assertion that every source element has
that shape.

### Boolean filter

A **Boolean filter** evaluates an expression of type `Bool` once for the current
candidate environment. `false` skips the candidate; `true` proceeds.

```text
when item.available
```

An exception, panic, unhandled effect, or foreign failure is not converted into
`false`.

### Local binding

A **local binding** evaluates an expression once for each candidate that reaches
it and extends the environment for later qualifiers and the result.

```text
let total = item.price * item.quantity
```

Its pattern must be exhaustive for the expression type. Refutable selection
belongs in a filtering generator or an explicit match.

### Result expression

The **result expression** runs once for every complete environment that passes
all qualifiers. Its values appear in the result list in execution order.

### Iterator, stream, and generator function

An iterator protocol, a lazy stream, and a resumable function that produces
values are not list comprehensions. They may eventually feed or resemble a
comprehension, but each adds lifetime, cancellation, resource, and re-entry
rules that an eager list does not need.

## What existing designs establish

| Design | Source and result | Pattern mismatch | Filters | Binding and order | Main lesson |
| --- | --- | --- | --- | --- | --- |
| Haskell 2010 | list to lazy list | silently skip | arbitrary `Bool` | nested depth-first; local declarations | a small kernel translation can define generator, filter, and binding roles |
| Erlang/OTP 29 | list, bit string, or map to list, binary, or map | relaxed skip or strict runtime failure | split behavior for guard and ordinary expressions | nested or explicit zip; fresh/shadowing bindings | failure and zip policies need explicit syntax and diagnostics |
| Elixir 1.20 | `Enumerable` to list or `Collectable` | silently skip | truthy ordinary expressions | nested Cartesian; effectful qualifiers allowed | one form can grow into a generic effectful collection language |
| Scala 3.4 | carrier-defined result via methods | total by default; `case` explicitly filters | Boolean guard via `withFilter` | `map`, `flatMap`, and generated binding translations | explicit refutability is valuable; carrier-defined semantics are broad |

The [Haskell report](../30-sources/marlow-2010-haskell-language-report.md)
defines the clearest list-specific calculus: qualifiers are nested depth-first,
patterns skip mismatches, filters return `Bool`, and a `concatMap` translation
supplies a kernel meaning.

The current [Erlang expression reference](../30-sources/erlang-otp-expressions-and-guard-sequences.md)
shows the BEAM's expanded design space: three source and target shapes,
strict and relaxed patterns, nested and zip generators, and filter failure that
depends on whether an expression belongs to the guard subset.

[EEP 70](../30-sources/erlang-eep-70-strict-and-relaxed-generators.md)
is direct evidence that silent pattern skipping can hide malformed input. It
added a second symbolic operator because existing compatibility prevented a
safer default.

[EEP 73](../30-sources/erlang-eep-73-zip-generators.md) shows that
lockstep traversal is not a cosmetic variant: it needs length-mismatch errors,
round-level pattern behavior, precedence, and error priority.

The [Elixir guide](../30-sources/elixir-1-20-comprehensions.md) shows the
ergonomic appeal and semantic breadth of combining arbitrary enumerables,
truthy filters, pattern skipping, effectful calls, binary iteration, and
generic result collectors.

The [Scala specification](../30-sources/scala-3-4-for-comprehensions.md)
supplies the best surface precedent for separating total patterns from
explicit filtering patterns. It also demonstrates how method-driven
desugaring lets the carrier determine result and execution behavior.

## The algebra explains possibilities, not the initial surface

### Lists give map and flatten naturally

For a single total generator, a pure comprehension has the familiar
extensional relationship:

```text
for x in xs
yield f(x)

==

List.map(xs, f)
```

With a dependent second generator, the outer traversal maps each value to a
list and concatenates the lists:

```text
for
  x in xs
  y in next(x)
yield pair(x, y)

==

List.flat_map(xs, fn x ->
  List.map(next(x), fn y -> pair(x, y))
)
```

These equations explain result values for pure, total programs. They are not
permission to ignore strict evaluation, source evaluation count, effects,
failure timing, stack behavior, or allocation.

### Monad is insufficient for filtered comprehensions

[Wadler 1992](../30-sources/wadler-1992-comprehending-monads.md)
derives generator composition from `map`, `unit`, and `join`, which is the
monadic structure behind dependent sequencing. The same paper shows that a
Boolean filter needs a meaningful zero or empty computation with additional
annihilation laws.

Therefore:

```text
Monad F
```

does not by itself justify:

```text
for x in fx
when predicate(x)
yield result(x)
```

for arbitrary `F`. Catena's initial class hierarchy deliberately does not say
that every monad has a lawful filtering zero. Pretending otherwise would hide a
new requirement or select an incoherent failure policy.

### Public trait operations do not fix execution

Even where `map` and `flat_map` exist, their mathematical laws do not fully
specify:

- eager or lazy execution;
- callback effect order;
- callback multiplicity;
- behavior after callback failure;
- stack safety;
- output builder allocation; or
- debugger frames.

Those are operational contracts. Catena should preserve the useful algebraic
relationship without defining list-comprehension execution by open trait
dispatch.

### Rich query qualifiers are later language design

[Peyton Jones and Wadler 2007](../30-sources/peyton-jones-wadler-2007-comprehensive-comprehensions.md)
show that ordering, grouping, limiting, zip, and user-provided transformations
can all fit a formally typed comprehension calculus. They also show that such
qualifiers alter scope and may change every in-scope variable's type.

That is evidence for a possible later query language, not a reason to put every
collection operation in Catena's initial comprehension.

## Proposed Catena surface contract

### Illustrative grammar

The following grammar describes semantic roles, not final tokens:

```text
comprehension ::= "for" generator qualifier* "yield" expression

generator ::= pattern "in" expression
            | "case" pattern "in" expression

qualifier ::= generator
            | "when" expression
            | "let" pattern "=" expression
```

Requirements:

- a comprehension contains at least one generator;
- the first qualifier is a generator;
- an ordinary generator pattern is exhaustive for the element type;
- a `case` generator pattern may be refutable and filters mismatches;
- a `when` expression has type `Bool`;
- a local binding pattern is exhaustive for its expression type; and
- the result is always `List B` in the initial language.

Newline, comma, and block punctuation should be resolved with the complete
Catena grammar. The semantic form should not depend on layout accidents.

### Read in execution order

The result-last form is longer than `[result | qualifiers]`, but it follows the
order in which programmers must reason about bindings:

```text
for user in users
when user.enabled
yield user.name
```

The reader encounters `user` before either use. This reduces forward
references and resembles ordinary control flow without turning the construct
into a result-discarding loop.

`yield` is essential in this provisional spelling. A `for` without `yield`
would be a different effect-only iteration form and should not be smuggled in
as the same construct.

### Lists only at first

The initial typing rule fixes generator sources and output:

```text
source : List A
result : B
whole  : List B
```

This choice provides:

- one encounter order;
- one finite eager result model;
- one empty value;
- one pattern element type;
- one builder strategy; and
- diagnostics that can name the concrete operation.

It does not prevent later syntax for streams, iterators, binaries, maps, or
generic collectors. It prevents those future contracts from being chosen
implicitly by whatever trait happens to resolve.

## Static semantics

### Generator typing

For an ordinary generator:

```text
Γ ⊢ source : List A ! εs
Γ ⊢ pattern : A ⇒ Δ total
---------------------------------
Γ ⊢ pattern in source ⇒ Δ ! εs
```

`Δ` contains the bindings introduced by the pattern. “Total” means coverage
analysis proves that every value of `A` matches under the visible constructor
and row information.

For a filtering generator:

```text
Γ ⊢ source : List A ! εs
Γ ⊢ pattern : A ⇒ Δ
---------------------------------
Γ ⊢ case pattern in source ⇒ Δ ! εs
```

The pattern may be refutable. Coverage diagnostics can still report that
`case` is unnecessary when the pattern is already total, or that the pattern
can never match.

### Filter typing

```text
Γ ⊢ predicate : Bool ! εp
---------------------------------
Γ ⊢ when predicate ⇒ {} ! εp
```

This is an ordinary typed Boolean expression, not the clause guard-safe
fragment. It may perform declared effects and may diverge or fail according to
ordinary expression semantics.

The distinction is intentional:

- a clause guard participates in fallthrough, coverage, and selective receive;
- a comprehension filter participates in explicit repeated iteration; and
- effect rows already make non-pure filter behavior visible.

A filter fault propagates. It never means `false`.

### Local binding typing

```text
Γ ⊢ expression : A ! εb
Γ ⊢ pattern : A ⇒ Δ total
---------------------------------
Γ ⊢ let pattern = expression ⇒ Δ ! εb
```

Local bindings are non-recursive within a qualifier sequence. Generalization
should follow Catena's ordinary effect-aware `let` policy, but a binder that is
effectfully recomputed for each candidate must not be hoisted as though it were
a once-only outer declaration.

### Result and effect typing

After checking qualifiers from left to right, the result is checked in the
environment extended by every surviving binding:

```text
Γ, Δall ⊢ result : B ! εr
---------------------------------
Γ ⊢ comprehension : List B ! (εq ∪ εr)
```

The row records which effects may occur, while the dynamic semantics records
how often and in what order they may occur. An effect row is a set-like
capability contract, not a multiplicity count.

### Hindley–Milner boundary

Generator-bound variables are lambda-like binders introduced once per source
element. They are not generalized merely because their qualifier resembles a
`let` declaration.

An explicit local `let` qualifier may use ordinary generalization only when
Catena's value/effect restriction permits it. This mirrors the broader type
system rather than inventing a comprehension-specific inference loophole.

## Lexical scope and names

Qualifiers extend scope from left to right:

```text
for
  x in xs
  let ys = related(x)   -- x is visible
  y in ys               -- x and ys are visible
yield combine(x, y)     -- all bindings are visible
```

The exact surface keywords remain provisional; the semantic rules are:

- the source expression of a generator sees earlier bindings but not the
  bindings introduced by its own pattern;
- a filter sees every earlier binding;
- a local binding's right side sees earlier bindings but not its new names;
- the result sees every surviving qualifier binding;
- no qualifier binding escapes the comprehension;
- patterns are linear; and
- rebinding a name already introduced in the same comprehension is an error.

Shadowing an outer name should follow Catena's ordinary shadowing rule, with a
focused diagnostic when the outer name is used in the generator source. Erlang
shows how treating every generator variable as fresh can turn an intended
comparison into accidental shadowing; Catena should not copy that rule.

## Dynamic semantics

### Single generator

For:

```text
for pattern in source
yield result
```

evaluation proceeds as follows:

1. evaluate `source` exactly once;
2. require the resulting value to be a list through static typing or an
   explicit dynamic boundary check;
3. visit list elements from head to tail;
4. match the exhaustive pattern once against each element;
5. evaluate `result` once in the extended environment; and
6. append that value logically to the output sequence.

An implementation may build the list in reverse and reverse it once, provided
result evaluation and observable effects remain in source order.

### Nested generators

Multiple ordinary generators are nested, left to right:

```text
for
  x in xs
  y in next(x)
yield {x, y}
```

means:

1. evaluate `xs` once;
2. for each `x` from left to right, evaluate `next(x)` once;
3. visit that inner list from left to right;
4. evaluate the result for every pair; and
5. finish the entire inner traversal before advancing to the next `x`.

The output is a stable depth-first Cartesian traversal. Empty outer or inner
lists contribute no results.

### Filters and bindings

For each current candidate environment:

- evaluate a local binding once when execution reaches it;
- evaluate a Boolean filter once when execution reaches it;
- on `false`, skip all later qualifiers and the result for that candidate;
- on `true`, continue;
- on ordinary failure, propagate immediately; and
- preserve effects already performed before failure.

Moving a filter earlier can change which effects run, even if the final pure
list would be equal. Filter reordering is therefore not generally valid.

### Filtering generator

For a `case` generator:

1. evaluate its source at the same nesting point as an ordinary generator;
2. visit elements in list order;
3. match the pattern once per element;
4. on mismatch, continue with the next element without evaluating later
   qualifiers; and
5. on success, extend the environment and continue.

Pattern mismatch is the only failure converted into skipping. An effect,
exception, divergence, or fault while evaluating the source is not a mismatch.

### Failure and partial effects

The comprehension is an ordinary strict expression. If it fails after some
effects have run, those effects are not rolled back unless an enclosing handler
or resource scope explicitly provides rollback.

No partially built list is returned after failure. Its internal accumulator is
unobservable unless unsafe or foreign code violates the abstraction.

## Effects are allowed but not hidden

### Why pure-only is too restrictive

Restricting comprehensions to pure expressions would make their equations
simple, but it would force common ordered workflows into unrelated syntax:

- reading a property for every file;
- asking a capability for data derived from an earlier element;
- logging or measuring accepted elements; and
- handling a typed request once per candidate.

Catena already has effect rows. The comprehension syntax itself visibly
communicates repetition.

### Why effectful comprehension is not effectful `map`

The public categorical `map` should remain pure and law-bearing. A
comprehension is a language control form with an operational effect trace.

For pure expressions, the compiler and advanced documentation may state
equivalences with `map`, filtering, and `flat_map`. For effectful expressions,
the normative elaboration targets a comprehension IR that explicitly sequences
each evaluation.

### Effect trace

Given:

```text
for
  x in source_effect()
  when filter_effect(x)
yield result_effect(x)
```

the observable trace is:

```text
source_effect
filter_effect(x1)
[result_effect(x1) when true]
filter_effect(x2)
[result_effect(x2) when true]
...
```

Nested generator source effects occur once for each surviving outer prefix, not
once for the entire comprehension.

### Handlers, cancellation, and cleanup

An enclosing handler interprets operations in the usual lexical manner. A
resumption may re-enter comprehension evaluation only according to Catena's
affine handler rules; the compiler must not duplicate a captured iterator
state.

Cancellation and resource cleanup are not ordinary list semantics. If a source
or qualifier owns a resource, its scope mechanism must define cleanup on
completion, filter rejection, failure, and cancellation. This remains coupled
to the open structured-runtime research.

## Coverage and pattern diagnostics

### Total generators reuse coverage analysis

The existing pattern matrix can decide whether a generator pattern covers its
element type:

```text
for Some(x) in options
yield x
```

should produce a diagnostic such as:

```text
This generator claims to accept every Option value, but None is not matched.

Use `case Some(x) in options` to deliberately skip None, or handle None in an
explicit match before yielding a result.
```

This is more informative than either a runtime crash or silent omission.

### Filtering patterns still need usefulness checks

An explicit filtering generator can receive:

- an error when its pattern is impossible for the element type;
- a suggestion when its pattern is total and `case` is unnecessary;
- redundancy diagnostics inside nested or-or patterns; and
- witnesses for the shapes it intentionally excludes when that helps review.

Its excluded shapes do not make the enclosing program non-exhaustive. The
source explicitly requested filtering.

### Comprehension filters are not clause guards

Both use Boolean conditions, but their contracts differ:

| Axis | Clause guard | Comprehension filter |
| --- | --- | --- |
| Purpose | choose an ordered clause | keep or skip an iterated candidate |
| Allowed effects | none in the initial design | ordinary inferred effects |
| Totality | required | not required by the comprehension construct |
| False result | try another clause or mailbox item | skip this candidate |
| Coverage role | may refine clause accessibility | does not establish structural exhaustiveness |
| Failure | rejected by guard-safe checking | propagates under ordinary semantics |

Reusing the same keyword may still be possible, but diagnostics and internal
judgments must preserve this distinction.

## Elaboration and intermediate representation

### Use a dedicated qualifier tree

The front end should elaborate surface syntax into a typed form such as:

```text
BuildList(result, qualifiers)

qualifier ::=
  EachTotal(pattern, source, next)
  EachCase(pattern, source, next)
  Keep(predicate, next)
  BindTotal(pattern, expression, next)
  Yield
```

Each node carries:

- source span;
- inferred input, binding, and result types;
- inferred effects;
- pattern coverage result;
- lexical binding identities; and
- source-order position.

This representation gives type checking, effect checking, diagnostics,
optimization, and BEAM lowering one explicit contract.

### Do not elaborate through open trait dispatch

The normative elaboration should not be:

```text
source.flat_map(...).with_filter(...).map(...)
```

because method resolution could make the comprehension depend on:

- local implementations;
- carrier-specific filtering behavior;
- overloaded result types;
- different callback order or multiplicity; or
- pure categorical operations acquiring effects.

The compiler may later optimize a typed `BuildList` into equivalent library
primitives when their implementations are trusted and their operational
contracts match.

### Preserve source vocabulary in diagnostics

An error in a result expression should say “result of this list
comprehension,” not “argument to generated `flat_map`.” An effect trace should
identify the qualifier that repeated an operation. Generated workers should
retain the comprehension and qualifier source spans.

## BEAM lowering

### Direct list worker

The initial backend can lower a qualifier tree to private recursive workers
that thread a reversed output accumulator:

```text
walk([], accumulator) = accumulator
walk([head | tail], accumulator) =
  accumulator2 = run_remaining_qualifiers(head, accumulator)
  walk(tail, accumulator2)

result = reverse(walk(source, []))
```

The result expression is evaluated in source order; only list-link
construction is reversed. This avoids repeated append and its quadratic cost.

Nested generators thread the same accumulator through inner workers before
advancing the outer tail. A filtering generator selects either the inner worker
or the unchanged accumulator.

### Native Erlang comprehension is an optimization, not the semantics

Some pure Catena forms may map cleanly to Core Erlang or BEAM patterns similar
to Erlang comprehensions. Catena should use that path only when it preserves:

- total versus filtering generator behavior;
- typed Boolean filters;
- exception and effect propagation;
- binding identity and scope;
- exact traversal order; and
- source diagnostics.

Erlang's relaxed/strict operators and guard-sensitive filter failures are not
Catena's semantic definition.

### Stack safety

Every generated list traversal should be tail-recursive in the accumulator.
Nested traversal depth should depend on the number of syntactic generators,
not the number of elements. The final reversal is a linear standard-library
operation.

An optimizer may avoid the reversal with a trusted builder or lower directly
to a BEAM list-construction loop. The public contract is stable order and
linear output construction, not a particular accumulator representation.

### Allocation

For one generator over `n` inputs producing `m` outputs:

- source visits are `n`;
- result evaluations are `m`;
- output list allocation is `O(m)`; and
- no intermediate mapped or filtered list is required.

For independent nested sources of sizes `n1` through `nk`, the upper result
count is their product. Dependent sources require a sum of per-prefix sizes.
This multiplicative behavior is semantic and should be teachable even when the
compiler uses a fused worker.

## Optimization rules

### Always safe structural optimizations

Subject to ordinary expression semantics, the compiler can:

- generate one fused worker rather than intermediate lists;
- use a reversed accumulator and one final reversal;
- eliminate impossible filtering patterns identified by coverage;
- remove a `case` marker whose pattern is proven total after issuing any
  configured style diagnostic; and
- specialize known list constructors and small literal lists.

### Optimizations requiring purity or totality

Reordering, hoisting, or combining qualifiers may change effects, failure, or
termination. The compiler may apply such a rewrite only when it has the needed
evidence.

Examples:

- hoist an inner source only if it is independent of outer bindings and moving
  it changes neither effects nor failure timing;
- combine adjacent filters only when their Boolean and effect evaluation order
  is preserved;
- move a filter before a binding only when the binding is pure, total, and its
  value is not required by the filter;
- distribute or reassociate generators only under pure total list semantics;
  and
- parallelize nothing without explicit parallel semantics.

### Law evidence is not cost evidence

Monad or functor laws can justify extensional equalities. They do not show that
a rewrite preserves an effect trace, allocation, error location, or space use.
Optimizer proof obligations must name both the algebraic and operational
premises they consume.

## Result shape and neighboring features

### Map and set results

Map construction needs a duplicate-key policy. Set construction needs equality
or ordering evidence. Neither is just a list result with different brackets.

The initial language should write those policies through explicit builders or
library calls. A later result-target form must specify:

- builder identity and trait requirements;
- duplicate or collision behavior;
- encounter-order preservation;
- partial construction on failure; and
- complexity guarantees.

### Binary comprehensions

Binary iteration needs segment sizes, encodings, incomplete trailing input,
and construction overflow rules. EEP 70 demonstrates why patterns define
segmentation rather than merely filter natural elements. Binary comprehensions
deserve separate research with the foreign and BEAM binary model.

### Streams and iterators

A lazy result changes:

- when source and qualifier effects run;
- how long bindings and resources remain live;
- whether failure occurs at construction or consumption;
- cancellation and early termination;
- repeated traversal; and
- sharing between consumers.

Use an explicit stream or iterator API until those questions have a complete
language-level answer.

### Zip

The combinator research already distinguishes:

```text
zip_exact     -- fail on unequal lengths
zip_shortest  -- stop with the shorter input
```

Those names expose the key policy. The initial comprehension can consume the
result of either operation with an exhaustive pair pattern. Dedicated zip
qualifiers should wait for evidence that avoiding tuple allocation materially
improves real Catena programs and diagnostics.

### Reduction and effect-only loops

`fold`, `fold_while`, collection builders, and result-discarding iteration
have different accumulator, early-stop, and return contracts. A `reduce`
option or `for` without `yield` should not be attached to list comprehension
merely because it shares traversal syntax.

### Parallel comprehensions

Parallel execution changes effect order, cancellation, failure aggregation,
resource use, and result ordering. Associativity does not grant permission to
run callbacks concurrently. A future parallel form must be visibly distinct
and connected to Catena's structured-concurrency model.

### Grouping, ordering, and query translation

Grouping changes binder cardinality and often binder types. Ordering buffers
and rearranges results. Remote query translation introduces quotation,
capability, partial evaluation, and provider-semantics questions.

These operations belong in libraries or a separately researched query
language until their benefits justify dedicated syntax.

## Diagnostics and approachable vocabulary

### Prefer task words

Entry-level diagnostics should use:

- “source list” rather than “monadic carrier”;
- “visit” rather than “bind”;
- “keep this item” rather than “zero/choice”; and
- “result expression” rather than “mapped continuation.”

The semantic reference can explain the map/flatten relationship for readers
who want it. The compiler need not teach category theory to explain a partial
pattern or repeated effect.

### Required diagnostics

The initial implementation should test at least:

1. source is not a list;
2. ordinary generator pattern is not exhaustive;
3. filtering generator pattern can never match;
4. unnecessary filtering marker on a total pattern;
5. filter expression is not `Bool`;
6. local binding pattern is refutable;
7. name is rebound in the same comprehension;
8. binding is unused;
9. result types disagree through an explicit branch;
10. inferred effect comes from a repeated qualifier;
11. nested generators produce a Cartesian product when zip may have been
    intended; and
12. a known literal or statically sized product has suspiciously large output.

The last two are lints, not type errors. They should explain the predicted
behavior and name `zip_exact` or `zip_shortest` when appropriate.

### Effect multiplicity explanation

When an effectful inner source depends on an outer binding, hover information
or a diagnostic should be able to say:

```text
This request is inside the second generator. It may run once for every item
that reaches it from the first generator.
```

An effect row alone cannot communicate that operational fact.

## Alternatives considered

### Haskell/Erlang bracket syntax

```text
[result | qualifiers]
```

**Benefit:** compact and historically well understood in functional languages.

**Cost:** result uses names before their binding appears, symbolic separators
carry substantial meaning, and the notation competes visually with list
literals and pattern syntax.

**Decision:** retain as semantic evidence, not the leading approachable
surface.

### Generic `for ... yield` over carrier methods

**Benefit:** one notation for lists, options, results, validation, queries, and
user types.

**Cost:** the carrier silently selects mapping, flattening, filtering, failure,
effect, and result behavior; filtered forms require more than `Monad`; error
messages expose generated methods.

**Decision:** reject for the initial language.

### Silent refutable patterns

**Benefit:** concise selection by data shape.

**Cost:** a typo or weakened data invariant silently removes values. EEP 70
exists because this is a production problem.

**Decision:** require an explicit filtering marker.

### Strict and relaxed punctuation operators

**Benefit:** compact and maps directly to Erlang/OTP 28.

**Cost:** a one-character difference controls data loss versus failure, and a
statically typed language can reject unintended partial patterns earlier.

**Decision:** use a word-level distinction and coverage checking.

### Guard-safe filters only

**Benefit:** filters are total, deterministic, and optimizable.

**Cost:** comprehension filters do not participate in clause coverage or
mailbox scanning, while ordinary effect rows can expose useful repeated work.

**Decision:** use ordinary `Bool` expressions with normal effect and failure
semantics.

### Pure comprehensions only

**Benefit:** simplest laws and optimizer.

**Cost:** splits common ordered workflows into another construct and
underuses Catena's explicit effect system.

**Decision:** permit effects, specify their exact trace, and preserve a pure
optimization subset.

### Generic output collectors

**Benefit:** one syntax builds lists, sets, maps, binaries, and streams.

**Cost:** hides collision, order, termination, resource, and builder policies.

**Decision:** list result only initially.

## Proposed initial contract

| Axis | Initial Catena choice |
| --- | --- |
| Surface shape | result-producing `for ... yield`, exact tokens provisional |
| Source | `List A` only |
| Result | eager `List B` only |
| Ordinary pattern | statically exhaustive for `A` |
| Filtering pattern | explicit `case`; mismatch skips |
| Filter | ordinary expression of type `Bool` |
| Filter effects | allowed and included in the effect row |
| False | skip current candidate |
| Failure | propagate; never convert to false |
| Local binding | non-recursive, exhaustive pattern |
| Multiple generators | nested, dependent, depth-first Cartesian traversal |
| Scope | left-to-right; bindings do not escape; no same-comprehension rebinding |
| Order | source lists left-to-right; inner traversal completes before next outer item |
| Lowering | typed qualifier tree to fused tail-recursive list worker |
| Trait dependency | none in the normative semantics |
| Zip | use explicit `zip_exact` or `zip_shortest` library operations |
| Streams, binaries, maps | deferred separate contracts |
| Parallelism | none; future syntax must be explicit |

## Formal and implementation obligations

### Static properties

- Every accepted ordinary generator pattern covers its element type.
- A filtering pattern binds only names available on its success path.
- Every filter has type `Bool`.
- Every local binding pattern is exhaustive.
- All uses are in lexical scope and same-comprehension rebinding is rejected.
- The result type is principal within the ordinary rank-1 fragment.
- The inferred effect row contains effects from every reachable source,
  binding, filter, and result expression.

### Dynamic properties

- Each source is evaluated exactly once at its nesting point.
- Each source element is visited exactly once per activation of that generator.
- Qualifiers evaluate left to right.
- Nested generators traverse depth-first in source order.
- A false filter or filtering-pattern mismatch runs no later qualifier for that
  candidate.
- Ordinary failures propagate at the same source point before and after
  optimization.
- Results retain source encounter order.

### Backend properties

- A single-generator comprehension is linear in source visits and output
  construction.
- Generated loops are tail-recursive with respect to list length.
- Fused lowering does not allocate intermediate map/filter lists.
- Source spans survive generated workers and inlining.
- Pure and effectful comprehensions produce equivalent values to the reference
  evaluator and equivalent observable effect traces where effects exist.

### Property and differential tests

Generate small lists, patterns, filters, and nested qualifier trees and compare:

- surface evaluation with a direct qualifier-tree interpreter;
- the interpreter with BEAM output;
- pure single generators with reference `map`;
- pure nested generators with reference `flat_map` plus `map`;
- filtering generators with explicit `filter_map`;
- failure and effect traces before and after optimizer passes; and
- output cardinality and order under empty, singleton, and nested inputs.

## Falsification criteria

Reconsider the proposal if evidence shows that:

- programmers routinely expect plain refutable patterns to filter and find the
  explicit marker harder to understand even after diagnostics;
- list-only syntax causes pervasive duplication that a small, lawful iterator
  abstraction can remove without making operational behavior carrier-specific;
- allowing effects makes code harder to predict than a pure-only form plus
  explicit traversal;
- `for ... yield` is consistently confused with imperative loops or future
  generator functions;
- direct BEAM lowering cannot preserve effect order, failure locations, and
  stack safety at acceptable cost;
- dedicated zip syntax eliminates material allocation or bugs that explicit
  `zip_exact` and `zip_shortest` do not; or
- common Catena programs require streams, binaries, maps, grouping, or
  reduction often enough that list-only syntax ceases to be a coherent unit.

## Staged implementation recommendation

### Stage 1: semantic kernel

1. Add the typed qualifier-tree IR.
2. Implement total generators, Boolean filters, and results in a reference
   evaluator.
3. Reuse pattern coverage for generator exhaustiveness.
4. Specify effect accumulation and exact trace order.

### Stage 2: pattern filtering and bindings

1. Add the explicit filtering generator.
2. Add exhaustive non-recursive local bindings.
3. Implement scope, shadowing, usefulness, and effect-multiplicity diagnostics.
4. Test interaction with abstract constructors and structural rows.

### Stage 3: BEAM backend

1. Generate tail-recursive workers with one reversed accumulator.
2. Preserve qualifier source spans and effect provenance.
3. Differentially test values, failures, and effect traces.
4. Measure direct recursion, public list functions, and generated workers.

### Stage 4: evidence-gated extensions

Evaluate, independently:

- iterator sources;
- stream results and resource scopes;
- exact and shortest zip qualifiers;
- binary source and result forms;
- map and set builders;
- effect-only iteration;
- grouping and ordering; and
- structured parallel traversal.

No extension should change the meaning of an already valid initial
comprehension.

## Open questions and research priorities

The connected
[inquiry](../40-inquiries/how-should-catena-specify-list-comprehensions.md)
tracks the remaining empirical and formal work. Highest priorities are:

1. Does `for ... yield` best fit Catena's complete expression grammar and
   behavior-first vocabulary?
2. Is `case` the clearest explicit marker for a filtering pattern, or does a
   task word such as `matching` transfer better?
3. Should effectful filters be allowed from the first release, or should
   effects initially be limited to generator sources and result expressions?
4. Does a local binding qualifier justify syntax, or is an ordinary nested
   `let` clearer?
5. Which shadowing policy minimizes mistakes without making nested
   comprehensions verbose?
6. Can the qualifier-tree IR share machinery with clause guard trees without
   conflating their safety and coverage judgments?
7. Which BEAM lowering best preserves source traces while avoiding
   intermediate lists?
8. When do real programs need zip, iterator, stream, binary, or generic builder
   forms?

## Annotated source route

### Semantic foundations

- [Haskell 2010 Language Report](../30-sources/marlow-2010-haskell-language-report.md)
  gives the list-specific grammar, depth-first behavior, pattern filtering,
  local bindings, and kernel translation.
- [Comprehending Monads](../30-sources/wadler-1992-comprehending-monads.md)
  derives generator composition from monadic structure and proves that filters
  require a separate zero operation.
- [Comprehensive Comprehensions](../30-sources/peyton-jones-wadler-2007-comprehensive-comprehensions.md)
  formalizes zip, grouping, ordering, qualifier scope, and binder-type changes,
  exposing the cost of extension.

### BEAM evidence

- [Erlang/OTP Expressions and Guard Sequences](../30-sources/erlang-otp-expressions-and-guard-sequences.md)
  records current list, binary, map, filter, strict, relaxed, nested, zip, and
  scope behavior.
- [EEP 70](../30-sources/erlang-eep-70-strict-and-relaxed-generators.md)
  isolates silent skipping from assertive pattern matching.
- [EEP 73](../30-sources/erlang-eep-73-zip-generators.md) isolates
  lockstep traversal, length mismatch, pattern interaction, and tuple-allocation
  avoidance.
- [Elixir 1.20 Comprehensions](../30-sources/elixir-1-20-comprehensions.md)
  demonstrates a generic, effectful, approachable BEAM surface and its broad
  semantic footprint.

### Explicit refutability and carrier translation

- [Scala 3.4 For Comprehensions](../30-sources/scala-3-4-for-comprehensions.md)
  distinguishes irrefutable generators from explicit `case` filtering and
  specifies a method-driven translation.

## Connections

- [Algebraic Data Types](algebraic-data-types.md) supplies the pattern,
  exhaustiveness, constructor-visibility, and representation boundaries used
  by total and filtering generators.
- [Clause Guards](clause-guards.md) supplies the deliberately stricter
  condition contract for ordered clauses and selective receive; comprehension
  filters remain ordinary effect-typed Boolean expressions.
- [Combinators for Algebraic Data and Categorical Programming](combinators-for-algebraic-data-and-categorical-programming.md)
  supplies the pure `map`, dependent `and_then`, traversal, fold, iterator, and
  zip policies that comprehension syntax must not blur.
- [Algebraic Effects and Handlers](algebraic-effects-and-handlers.md) supplies
  the lexical effect and affine resumption model governing effectful qualifier
  execution.
- The [List Comprehensions map](../10-maps/list-comprehensions.md) organizes the
  complete evidence and decision route.
