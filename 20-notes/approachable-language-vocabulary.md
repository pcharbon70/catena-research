---
title: "An Approachable Vocabulary for Catena"
kind: note
created: "2026-08-01"
maturity: developing
tags:
  - api-design
  - catena
  - documentation
  - language-design
  - programming-language-education
  - usability
aliases:
  - "Approachable Catena vocabulary"
  - "Behavior-first Catena terminology"
---

# An Approachable Vocabulary for Catena

## Executive conclusion

Catena should not ask programmers to learn category theory before they can
read ordinary code. The mathematics should determine which compositions are
valid, which transformations preserve meaning, and which guarantees an
implementation must satisfy. It should not determine the first words a user
must memorize.

The proposed design therefore has two deliberately separated vocabularies:

1. a **public, behavior-first language** used in code, diagnostics, standard
   library documentation, and introductory guides; and
2. an **internal semantic ledger** used by language designers to connect each
   public capability to a precise mathematical structure, laws, kind, and
   derivation rule.

This is not a scheme for teaching a friendly nickname and then revealing the
“real” name. The behavior-first name is the real Catena interface. A programmer
should be able to become proficient without crossing into the semantic ledger.
The compiler, libraries, and test tooling carry the rigor on the programmer's
behalf.

The vocabulary below is a proposal to test, not a settled surface
specification. Several names predict the intended behavior well; several
others remain risky and should not enter guides until comprehension tests show
that programmers infer the right operation from them.

## Scope

This note asks:

> What words, operation families, diagnostics, and learning sequence let a
> regular programmer use Catena's typed, compositional design without needing
> its formal mathematical terminology?

This note concentrates on user-facing vocabulary and pedagogy. The underlying
type, data, effect, categorical, and combinator models remain developed in
their dedicated notes. Any public name proposed here must remain an exact view
of those models rather than silently weakening them.

Every candidate term, example, learning sequence, and argument-order rule in
this note is a Catena-specific proposal. Only the independent primary research
recorded below is treated as evidence for evaluating those proposals.

## What “approachable” means

Approachability must be observable rather than asserted. For Catena, it means
that a programmer who has no category-theory vocabulary can:

- finish representative data-transformation, validation, effect, and process
  tasks after a short language introduction;
- choose an operation by the dependency and shape of the computation—for
  example, distinguish independent combination from a later step that depends
  on an earlier value;
- predict what a trait or operation permits from its Catena name;
- transfer the same operation from `Option` to `Result`, lists, and trees;
- understand whether an operation preserves shape, can stop early, performs an
  external effect, or may change evaluation cost;
- repair representative type and capability errors from the default compiler
  explanation; and
- do all of this while the implementation still satisfies the formal laws,
  coherence rules, and operational contracts recorded by the language design.

These criteria reject two shallow substitutes for accessibility: merely
renaming mathematical abstractions, and hiding behavior so completely that
users cannot predict cost or effects.

## Evidence and its limits

The evidence supports design tests more strongly than it supports any one
word.

- Green and Petre's cognitive-dimensions framework recommends evaluating a
  notation through tradeoffs such as closeness of mapping, consistency,
  role-expressiveness, hidden dependencies, hard mental operations,
  abstraction gradient, premature commitment, and progressive evaluation. It
  is a discussion framework based chiefly on visual-programming environments,
  not a controlled comparison of names for functional abstractions. It gives
  Catena an evaluation lens, not a naming answer. See
  [the source note](../30-sources/green-petre-1996-cognitive-dimensions.md).
- Barik and colleagues found, through 68 professional developers and 210
  Stack Overflow question-and-answer pairs, that compiler explanations need
  both sound explanatory structure and actionable repair information. This is
  direct evidence for diagnostic design, although it does not test Catena's
  abstractions. See
  [the source note](../30-sources/barik-et-al-2018-compiler-explanations.md).
- Elm's compiler-error design report demonstrates source-local explanations,
  contextual hints, and deliberate layout, but it reports a design practice
  rather than a controlled usability study. See
  [the source note](../30-sources/czaplicki-2015-compiler-errors-for-humans.md).
Consequently, the proposed vocabulary requires user testing. Intuition and
precedent can nominate words; they cannot validate them.

## Design policy

### Behavior before abstraction

Introduce a capability through a problem the programmer already recognizes:
changing a value inside an `Option`, validating two independent fields,
choosing a later lookup from an earlier result, or rebuilding a tree while
collecting failures. Name the behavior, show its type and cost, then identify
the reusable capability.

### Operations are verbs; capabilities are roles

Operations should read as actions: `map`, `compare`, `combine`, `summarize`,
`and_then`, `compose`, and `extract`. Capability names should identify the role
a type can play: `Mapper`, `Orderable`, `Combiner`, and `Composable`.

This convention is a default, not a reason to force awkward grammar. A name
must still predict behavior in an expression, a constraint, and a diagnostic.

### One term should mark one distinction

Closely related names are dangerous when their difference is invisible. In
particular, `Pairable`, `Applicator`, `Chainable`, and `Pipeline` must each
correspond to a user-observable dependency or construction rule. If ordinary
programmers cannot state that difference after concrete examples, Catena
should merge the public concepts or choose sharper names.

### Do not maintain two public synonyms

Introductory documentation should not say “`Mapper`, also known as Functor” or
put a mathematical translation table next to every API. That makes the formal
term a hidden prerequisite and forces users to remember two labels. Formal
connections belong in an optional theory appendix, the specification, and
research documents such as this one.

### Concrete types precede trait constraints

Teach `Option.map`, `Result.map`, and `List.map` before a generic `Mapper`
constraint. The generic capability becomes useful when the learner has already
recognized the shared behavior. Qualified examples also improve searchability
and make the subject type visible.

### Dependency, effects, order, and cost stay visible

Friendly vocabulary must not conceal execution. Documentation and types should
distinguish:

- independent values from a later step selected by an earlier value;
- an ordinary domain outcome from an external operation;
- ordered from potentially parallel combination;
- full traversal from early termination;
- lazy from eager work; and
- shape-preserving from shape-changing operations.

### State guarantees as refactoring promises

Public explanations should say which rewrites preserve behavior. “Grouping
these combinations differently produces the same result” is more directly
useful than naming associativity. The specification can record the exact
equation and its mathematical classification.

### Prefer named operations before symbolic shortcuts

Named operations provide searchable vocabulary and better diagnostics.
Operators may be introduced later for frequent, unambiguous patterns, but
every operator should have a canonical named form and documentation should
teach that form first.

## Core language vocabulary

The smallest public vocabulary should use ordinary programming words wherever
they remain precise.

| Catena term | Meaning in ordinary use | Terms kept out of the entry path |
| --- | --- | --- |
| value | Data available to a program | object in a category |
| transform | A pure value-to-value function | morphism |
| type | The set and structure of permitted values | object, carrier |
| record | A value with named fields | product |
| tuple | A value with positional fields | product |
| variant type | A type whose value is one of named alternatives | sum, coproduct |
| variant | One named alternative of a variant type | injection |
| payload | The values carried by a variant | summand |
| match | Select behavior from a value's variant and payload | elimination, case morphism |
| trait | A named capability required from a type | type class |
| implementation | How a type provides a trait | instance, dictionary |
| requirement | A capability a generic definition needs | constraint, context |
| guarantee | A behavior-preserving promise implementations must keep | law |
| effect | A named external ability a transform may use | algebraic effect |
| operation | One request provided by an effect | effect operation |
| handle | Supply behavior for an effect's operations | handler interpretation |
| resume | Continue a handled computation with a value | invoke a continuation |
| process | One isolated concurrent computation | actor |
| link | Propagate abnormal process termination | failure edge |
| monitor | Observe another process's termination | observation edge |
| supervise | Apply a restart policy to child processes | supervision tree semantics |
| restart | Start a failed child again under its policy | recovery transition |

`transform` should mean a pure computation by default. If the type and effect
syntax makes `uses Clock` or `uses Database` visible, “effectful transform” is
an acceptable explanatory phrase. `context` should not be a general beginner
synonym for `Option`, `Result`, a collection, an effect, and a process mailbox;
that one vague word would hide distinctions the design needs users to see.

### Algebraic data

The public path should teach data by construction and observation:

```catena
type DeliveryStatus =
  | Queued
  | InTransit { tracking_id: TrackingId }
  | Delivered { at: Instant }
  | Failed { reason: DeliveryFailure }
```

The user needs `variant type`, `variant`, `payload`, `construct`, and `match`.
The compiler can generate qualified operations such as `DeliveryStatus.map`
when the declaration meets a precise derivation rule. The phrases “sum type,”
“initial algebra,” and “eliminator” add no necessary power to this first
explanation. The underlying requirements remain those developed in
[Algebraic Data Types](algebraic-data-types.md).

### Types and requirements

Normal type errors should describe a value's **type shape** and where a type
parameter is stored, produced, or accepted as input. Terms such as `kind`,
`covariant`, `contravariant`, evidence dictionary, and higher-kinded type may
appear in technical details and the specification, but should not be required
to understand the first diagnostic.

For example, a failed `Mapper` derivation should explain that a field accepts
`A` as input, so changing stored `A` values cannot produce a `Consumer B`.
That states the reason at the declaration site instead of reporting only a
kind mismatch or variance classification. The deeper inference and coherence
obligations remain those in
[A Greenfield Type System for Catena](catena-greenfield-type-system.md).

## Proposed capability vocabulary

Catena's current formal design tracks seventeen precise structures. The table
tests possible public views; it does not establish that every structure needs
a distinct public trait or that any candidate name is ready for the standard
library.

| Public capability | Core operations | What a programmer can predict | Design-ledger structure |
| --- | --- | --- | --- |
| `Equatable` | `equals` | Test whether two values count as the same | Setoid |
| `Orderable` | `compare` | Place values in a consistent order | Ord |
| `Combiner` | `combine` | Join two values of one type without changing the result when regrouped | Semigroup |
| `Accumulator` | `empty`, `combine_all` | Start with a neutral value and combine any number of values | Monoid |
| `Reducible` | `summarize`, `fold_left`, `fold_right`, `fold_until` | Consume a structure into a result, optionally stopping early | Foldable |
| `Mapper` | `map`, `replace` | Change every stored result while preserving the outer shape | Functor |
| `DualMapper` | `map_both`, `map_first`, `map_second` | Change either of two stored result positions | Bifunctor |
| `Pairable` | `map2`, `map3`, `pair` | Combine independent wrapped values | Apply |
| `Applicator` | `from_value` plus inherited `map2` | Lift a plain value and combine independent wrapped values | Applicative |
| `Collector` | `collect_map`, `collect` | Rebuild one structure while accumulating an independent result or effect | Traversable |
| `Chainable` | `and_then`, `flatten` plus inherited `map2` | Run a later wrapped step selected by an earlier value | Chain |
| `Pipeline` | derived workflow operations | Use value injection and dependent sequencing together | Monad |
| `Composable` | `compose` | Connect compatible transforms without requiring a universal identity | Semigroupoid |
| `System` | `identity` plus `compose` | Compose transforms and express a do-nothing transform | Category |
| `Flow` | `from_transform`, `on_first`, `on_second`, `side_by_side`, `fan_out` | Route structured inputs through composable transforms | Arrow |
| `ContextMapper` | `map_with_context` | Compute each result from a position together with its surrounding structure | Extend |
| `Extractor` | `extract`, `duplicate_context` | Read a focused value and extend computations over its contexts | Comonad |

### Candidate hierarchy

The public hierarchy should expose only real capability extension:

```text
Equatable -> Orderable
Combiner -> Accumulator
Reducible
Mapper -> Pairable -> Applicator --\
                   -> Chainable --+-> Pipeline
Mapper -> ContextMapper -> Extractor
Mapper + Reducible -> Collector
DualMapper
Composable -> System -> Flow
```

This diagram describes available operations, not a lesson in mathematical
inheritance. `Chainable` retains `Pairable`'s independent combination as well
as adding a value-selected next step. The diagram also deliberately
distinguishes `Pairable` from `Applicator`: the former combines already wrapped
independent values, while the latter can also introduce a plain value.
`Pipeline` combines plain-value introduction with dependent sequencing.

### Names that need evidence

Several candidates may produce the wrong intuition:

- `Accumulator` may imply mutation or an accumulator argument even though the
  essential addition is a neutral value.
- `Pairable` may suggest that the output must be a tuple, while `map2` can
  produce any result.
- `DualMapper` may suggest reversal or mathematical duality rather than two
  independently changeable result positions.
- `Applicator` is close to the formal word, does not clearly advertise
  `from_value`, and differs from `Pairable` by a subtle capability.
- `Collector` can be confused with a collection data type or builder.
- `Pipeline` already names ordinary forward piping and may not communicate the
  combination of injection and dependent sequencing.
- `System` is broad enough to suggest an operating system or component
  boundary rather than identity-bearing composition.
- `Flow` may imply runtime streaming, concurrency, or effects that its formal
  structure does not provide by itself.
- `ContextMapper` uses the vague word this note otherwise avoids and may not
  explain neighborhood-sensitive computation.
- `Extractor` may imply removal or destructive access rather than reading the
  distinguished value of a focused structure.

These are research findings, not minor copy-editing concerns. Each risky name
needs prediction and task-selection tests. A merged or restructured public API
is preferable to preserving a distinction that only a theory translation can
explain.

## Internal semantic ledger

The public vocabulary is safe only if the language team retains an exact
ledger. The following information belongs in the specification, compiler
tests, and advanced theory material—not in every introductory guide or routine
diagnostic.

| Public capability | Formal identity | Required formal obligation |
| --- | --- | --- |
| `Equatable` | Setoid | equivalence: reflexive, symmetric, transitive |
| `Orderable` | Ord | total ordering compatible with equality |
| `Combiner` | Semigroup | associativity |
| `Accumulator` | Monoid | associative combination with left and right identity |
| `Reducible` | Foldable | coherent reduction through its summary operation |
| `Mapper` | Functor | identity and composition preservation |
| `DualMapper` | Bifunctor | identity and composition preservation in both positions |
| `Pairable` | Apply | associative application/composition compatible with mapping |
| `Applicator` | Applicative | identity, composition, homomorphism, and interchange |
| `Collector` | Traversable | identity, composition, and naturality of traversal |
| `Chainable` | Chain | associative dependent sequencing compatible with inherited independent combination |
| `Pipeline` | Monad | left identity, right identity, and associativity |
| `Composable` | Semigroupoid | associative composition |
| `System` | Category | associative composition with left and right identity |
| `Flow` | Arrow | category, lifting, and structured-routing laws |
| `ContextMapper` | Extend | associative extension and mapping coherence |
| `Extractor` | Comonad | left identity, right identity, and associative extension |

The exact kinds, minimal definitions, derived operations, superclass evidence,
law trust levels, and operational contracts remain specified by
[Category Theory for Programming](category-theory-for-programming.md). A
friendly public name does not relax any of them.

## Operation families and selection rules

### Pipe-compatible argument order

Where it remains unambiguous, callback arguments should precede the subject so
the subject can be piped as the final argument:

```catena
map normalize parcel

parcel
|> map normalize

lookup_sender parcel
|> and_then lookup_rate
```

This is a Catena-specific design hypothesis rather than an evidence-backed
conclusion or a commitment to the exact pipe syntax. Binary operations,
effects, named records, partial application, and error locality must be tested
before fixing argument order globally.

### Four recurring choices

Most early generic programming can be taught through four questions:

| Question | Operation | Dependency made visible |
| --- | --- | --- |
| Do I already have one wrapped value and only need to change its result? | `map` | no new wrapped dependency |
| Do I have independent wrapped values to combine? | `map2` or `map3` | all inputs can be obtained independently |
| Does the next wrapped step depend on the value produced so far? | `and_then` | later computation is selected by earlier data |
| Am I rebuilding a whole structure while collecting independent results or effects? | `collect_map` | structure-wide collection |

These choices expose more than a hierarchy diagram. They guide code review,
parallelization, error accumulation, and effect interpretation.

### Concrete examples first

Changing a successful result without touching failure:

```catena
Result.map calculate_total shipment_result
```

Changing either side when both are meaningful data:

```catena
Result.map_both describe_lookup_failure normalize_rate rate_result
```

Combining independent validations:

```catena
Validation.map2 build_address
  (validate_street input.street)
  (validate_postal_code input.postal_code)
```

Choosing a later lookup from an earlier value:

```catena
find_zone parcel.destination
|> Result.and_then find_rate_for
```

Rebuilding a manifest while collecting independent validations:

```catena
List.collect_map validate_parcel manifest.parcels
```

Only after these operations work on concrete types should a guide introduce a
generic requirement such as `requires Mapper F`.

## Effects, outcomes, and process failure

Catena should keep three ideas distinct:

1. `Result Value Problem` is ordinary data describing an expected domain
   outcome;
2. `uses RateLookup, Clock` records external abilities requested by a
   transform; and
3. process termination is a concurrency event observed through links,
   monitors, and supervisors.

```catena
quote parcel : Result Quote QuoteProblem uses RateLookup, Clock =
  zone = RateLookup.zone_for parcel.destination
  now = Clock.now
  build_quote parcel zone now
```

A handler supplies an implementation for an effect operation. If an operation
allows continuation, the handler may `resume` it with a value. The beginner
does not need “algebraic signature,” “effect row,” or “affine resumption” to
read this program, but the implementation must obey the exact scope, row, and
resumption semantics developed in
[Algebraic Effects and Handlers](algebraic-effects-and-handlers.md).

The same policy applies to BEAM concurrency. `supervise worker with policy`
should state an operational relationship. It must not pretend that process
failure is a typed `Result` or an algebraic effect merely to make the concepts
look uniform.

## Guarantees instead of prerequisite law vocabulary

Each capability should document **what programmers may safely change**.

For `Combiner`:

> Grouping a sequence of `combine` calls differently must not change the
> observable result.

For `Accumulator`:

> Combining a value with `empty` on either side must preserve the value.

For `Mapper`:

> Mapping a value once with two composed transforms must agree with mapping in
> two stages, and mapping with the do-nothing transform must preserve the
> value.

The formal ledger calls these associativity, identity, and composition laws.
Public documentation may show the corresponding equations after the prose,
but should not require their names to understand the contract.

The language also needs a visible trust model. A user-authored `guarantee`
cannot justify optimizer rewrites merely because it is asserted. Compiler-
trusted laws require proof, construction, restricted derivation, exhaustive
testing under a stated model, or an explicitly unsafe trust boundary. Friendly
wording must not turn an unverified promise into optimization evidence.

## Diagnostics are part of the vocabulary

Default diagnostics should contain four layers:

1. a plain-language headline naming the failed action;
2. the exact source declaration or expression;
3. a causal explanation in the same public vocabulary as the guide; and
4. one or more repairs that preserve likely intent.

Optional technical details can then expose kinds, variance, generated
evidence, effect rows, or the formal structure for readers and compiler
developers who need them.

For example:

```text
`map` cannot be generated for `Consumer A`

  field `accept` has type `A -> Bool`
                         ^
  This field accepts an `A` as input. `map` can change stored or produced
  values, but it cannot replace a value that this type consumes.

Try one of these:
  - define `map_input` and state how input values should be converted; or
  - remove `derives Mapper` from `Consumer`.

Technical details: `A` occurs in an input position.
```

A missing independent-combination capability should be equally direct:

```text
`map2` needs `Report` to support `Pairable`

You are combining two independent `Report` values, but `Report` only defines
how to change one existing value with `map`.

Define how two `Report` values combine, or use `and_then` if the second report
must be chosen from the first result.
```

The causal structure and repair orientation are supported by the compiler
explanation evidence, while the exact text remains a hypothesis to test.

## Documentation architecture

The main learning path should be organized by programming decisions, not the
formal hierarchy:

1. values and pure transforms;
2. records, variant types, construction, and matching;
3. changing stored results with `map`;
4. combining independent results with `map2`;
5. choosing dependent steps with `and_then`;
6. reducing structures and rebuilding them with `collect_map`;
7. naming reusable capabilities with traits and stating guarantees;
8. requesting and handling external effects;
9. processes, messages, links, monitors, and supervision; and
10. a capstone that connects data, outcomes, effects, and fault-tolerant
    processes without collapsing their distinctions.

Each chapter should use one concrete task, show the type before the generic
capability, include a failing example and its compiler explanation, state
effect and cost behavior, and link to the next decision the programmer will
face.

An optional theory path may explain the semantic ledger for interested
readers. It must be discoverable without being interleaved into the ordinary
path. Search for `Mapper`, `map`, or a compiler error should never require a
user to know the word “Functor.”

Full guides should follow vocabulary validation rather than freezing these
names prematurely. Small guide prototypes are useful as test instruments now;
a polished guide set is not.

## Terms to keep out of the entry path

The following terms can remain exact specification vocabulary but should not
be prerequisites for ordinary programming:

- category, object, morphism, functor, bifunctor, applicative, monad, comonad,
  semigroupoid, arrow, natural transformation, and adjunction;
- product, coproduct, initial algebra, catamorphism, anamorphism, and
  eliminator;
- higher-kinded type, variance, dictionary passing, evidence term, and
  principal constraint entailment;
- algebraic signature, effect row, deep handler, delimited continuation, and
  affine resumption; and
- associativity, homomorphism, interchange, naturality, and coherence as
  unexplained labels.

Avoiding the labels does not mean avoiding their content. Catena must explain
the observable guarantee, dependency, or operation each term formalizes.

## Evaluation through cognitive dimensions

| Dimension | Question for Catena | Failure signal |
| --- | --- | --- |
| closeness of mapping | Does the operation name match the programmer's task? | users translate through a theory term before selecting it |
| consistency | Do related verbs and capability roles behave alike across types? | `collect`, `map`, or `combine` changes meaning unexpectedly |
| role-expressiveness | Can readers tell why `map2` rather than `and_then` appears? | correct code is produced but its dependency structure is misunderstood |
| hidden dependencies | Are effects, ordering, early exit, and required implementations visible? | a refactor changes behavior that the surface implied was irrelevant |
| hard mental operations | How many hierarchy distinctions must be held at once? | users rely on a memorized seventeen-item chart for a local task |
| abstraction gradient | Can users start concrete and generalize when repetition appears? | traits must be learned before `Option.map` can be understood |
| premature commitment | Must users choose a capability before their dependency shape is known? | early annotations force rewrites as the program develops |
| progressive evaluation | Can a partial example run, type-check, or produce a focused explanation? | a learner must complete an entire generic design before receiving feedback |

This framework should be used to compare vocabulary revisions rather than to
declare one design universally “more usable.”

## Tradeoffs and falsification criteria

Behavior-first vocabulary carries real risks:

- ordinary words may be too broad to search or too weak to distinguish nearby
  capabilities;
- hiding formal names may make advanced literature harder to discover;
- a friendly hierarchy can still be cognitively expensive if all seventeen
  capabilities appear at once;
- names may imply stronger execution behavior than the laws provide; and
- local ease can harm transfer if the same verb behaves differently across
  data types.

The proposal should be rejected or revised if testing finds any of the
following:

- programmers routinely choose `map2`, `and_then`, or `collect_map` for the
  wrong dependency structure after the concrete introduction;
- a public name causes a systematic false prediction about output shape,
  effects, ordering, or cost;
- programmers need the formal translation to explain an ordinary error;
- the public hierarchy cannot map one-to-one to the formal obligations without
  exceptions that users can observe;
- qualified concrete APIs and generic APIs drift into incompatible operation
  families; or
- hiding a formal term removes information required to write correct code
  rather than merely changing how that information is explained.

## Research priorities

1. Test the risky capability names through prediction tasks before stabilizing
   syntax or guides.
2. Prototype the four-operation decision path—`map`, `map2`, `and_then`, and
   `collect_map`—across `Option`, `Result`, validation, lists, trees, parsers,
   and effects.
3. Write paired default and technical diagnostics for derivation, missing
   requirements, ambiguous effects, and non-exhaustive matches.
4. Audit every public operation for shape, dependency, ordering, termination,
   effect, allocation, and strictness promises.
5. Determine whether the seventeen formal structures require seventeen public
   traits, or whether some should remain derived interfaces, modules, or
   advanced-only constraints.
6. Establish how programmers discover the formal lineage when they want it
   without making it prerequisite knowledge.
7. Build guide prototypes only as controlled artifacts for the active
   [vocabulary inquiry](../40-inquiries/how-should-catena-expose-mathematical-structure-without-mathematical-jargon.md).

## Route through the evidence and design

- Follow the
  [Approachable Catena Language Design map](../10-maps/approachable-catena-language-design.md)
  for the evidence, semantic foundations, and evaluation path.
- Use [Category Theory for Programming](category-theory-for-programming.md) for
  the exact formal hierarchy and law obligations.
- Use
  [Combinators for Algebraic Data and Categorical Programming](combinators-for-algebraic-data-and-categorical-programming.md)
  for the operation layers and execution contracts.
- Use [Algebraic Data Types](algebraic-data-types.md),
  [Algebraic Effects and Handlers](algebraic-effects-and-handlers.md), and
  [A Greenfield Type System for Catena](catena-greenfield-type-system.md) for
  the semantic boundaries the public vocabulary must preserve.
