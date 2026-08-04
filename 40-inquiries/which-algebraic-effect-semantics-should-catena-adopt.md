---
title: "Which Algebraic-Effect Semantics Should Catena Adopt?"
kind: inquiry
created: "2026-07-31"
status: open
tags:
  - algebraic-effects
  - catena
  - effect-handlers
  - language-design
  - resumptions
aliases:
  - "Catena algebraic-effect semantics inquiry"
  - "How should Catena handle effects?"
---

# Which Algebraic-Effect Semantics Should Catena Adopt?

## Why this matters

“Algebraic effects and handlers” names a family of language designs, not one
complete feature. Two languages may share `perform` and `handle` syntax while
disagreeing about which handler receives an operation, whether resuming
reinstalls that handler, whether a continuation may run twice, which effects
remain in the result type, and what happens to resources when a continuation
is abandoned.

Catena's earlier greenfield type-system synthesis chose effect rows and
lexically scoped at-most-once resumptions—now described more precisely as
affine—as a direction. The
[algebraic-effects deep dive](../20-notes/algebraic-effects-and-handlers.md)
refines that direction into a provisional semantic bundle. The normative 0.1.5
slice now supplies bounded executable evidence for its rows, selection,
handling, verifier, and BEAM lowering, but it does not establish principal
inference or abstraction proofs, sound resource behavior, performance, or
usable surface syntax.

This inquiry is independent of any Catena repository outside this archive. It
starts from the language-design goals recorded here and from the linked
primary literature.

## Operational question

Can one small Catena calculus and prototype satisfy all of the following?

- Effect signatures have nominal identity and typed first-order operations.
- Multiple uses of one signature are distinguished by lexically scoped
  capabilities rather than implicit nesting order.
- Higher-order effect-polymorphic code cannot accidentally intercept effects
  raised by an unknown callback.
- Function effects use open rows with most-general inference under a stated
  row equality.
- An open handler removes exactly its selected effect occurrence and forwards
  every unrelated operation unchanged.
- Deep resumptions reinstall the selected handler, while clause bodies obey a
  documented outer lookup rule.
- A resumption may be discarded or invoked once, cannot escape, and cannot
  duplicate or lose a typed resource contrary to its multiplicity.
- Closed programs eliminate every effect except a documented set of host
  effects.
- A free-tree interpreter, a CPS implementation, and any native implementation
  produce equivalent traces for the conformance corpus.
- Cleanup, cancellation, exceptions, backtraces, FFI frames, and stack
  inspection have specified behavior around abort and resume.

“Satisfy” means the operational semantics, declarative typing, inference
algorithm, elaborated core, core verifier, and executable implementations agree
on accepted programs and traces. Passing examples without those artifacts is
useful prototype evidence, not resolution.

## Working hypotheses

1. **Nominal signatures plus lexical capabilities** are a better default than
   dynamically choosing the nearest handler with the same operation label.
2. **Deep open handlers** cover the initial interpretation use cases with a
   smaller surface and typing story than exposing both deep and shallow forms.
3. **Affine resumptions**—zero or one invocation—are a sounder initial contract
   than transparent multi-shot continuations and still cover exceptions,
   state, generators, coroutines, and cooperative scheduling.
4. **Duplicate-label effect rows** can retain principal elimination, but
   capability identity must be integrated into row equality rather than added
   after inference.
5. **Static capability elaboration** can provide a tunneling-style abstraction
   property, but this must be proved on higher-order callbacks rather than
   assumed from lexical syntax.
6. **Scoped and higher-order effects** require a separate calculus. Encoding
   every scoped computation as a thunk will obscure handler scope and resource
   obligations.
7. **A free computation tree** is the appropriate reference semantics, while
   selective CPS and native stack segments should compete as optimized
   implementations after trace equivalence is established.

## Paths to explore

### Semantic kernel

- Define values, computations, evaluation contexts, operation performance,
  capability binding, open forwarding, return clauses, and deep resumption.
- Specify whether operations performed directly by a handler clause can reach
  the same handler and encode that choice in a reduction rule.
- Define abort, normal return, exception propagation, cancellation, and final
  cleanup without appealing to a particular stack implementation.
- State a deterministic handler-selection lemma.

### Handler identity and abstraction

- Reproduce the accidental-capture examples from
  [Zhang and Myers](../30-sources/zhang-myers-2019-abstraction-safe-effect-handlers.md)
  using Catena's proposed higher-order functions.
- Compare tunneling, explicit capability arguments, lexical instance binders,
  and generated runtime labels on identical examples.
- Reproduce the two-state-cell and instance-escape examples from
  [Biernacki et al.](../30-sources/biernacki-et-al-2020-effect-instances-lexically-scoped-handlers.md).
- State the contextual equivalence Catena expects module abstraction to
  preserve.

### Type-and-effect inference

- Define kinds for value types, effect signatures, effect instances, and
  effect rows.
- Extend the existing duplicate-label row theory so handling a named instance
  yields a most-general residual row.
- Decide when instance variables are explicit, inferred, or quantified in
  public signatures.
- Prove substitution, row-unifier soundness, most-generality, preservation,
  progress, and no-instance-escape.
- Check how effect-aware `let` generalization interacts with handler answer
  types and clause-local resumption variables.

### Resumption multiplicity and resources

- Give resumptions a dedicated affine core type and an independent escape
  check.
- Compare static affine checking with a runtime consumed bit and require the
  latter as defense in depth if unsafe or foreign code can bypass typing.
- Model a file, session channel, mutable reference, dynamic binding, and
  cleanup obligation inside captured continuations.
- Attempt the Links counterexample from
  [Tang et al.](../30-sources/tang-et-al-2024-soundly-handling-linearity.md).
- Specify what a future `multi` handler must prove about a captured
  continuation before cloning it.

### Scoped computations

- Build examples for `local`, `catch`, nondeterministic pruning, `bracket`,
  timeout, task groups, and transactions.
- Classify which examples are first-order operations, scoped operations, or
  structured runtime primitives.
- Compare higher-order signatures with dedicated block constructs using the
  representation gap identified by
  [Wu, Schrijvers, and Hinze](../30-sources/wu-et-al-2014-effect-handlers-in-scope.md).
- Require explicit laws for cancellation and cleanup before a resource scope
  becomes an ordinary handler library.

### Reference implementation

- Implement a free-tree interpreter whose traces expose operation identity,
  handler selection, forwarding, resume count, and cleanup.
- Add deep state, exception, logging, reader, generator, and scheduler
  handlers; represent nondeterministic search explicitly rather than assuming
  multi-shot control.
- Generate nested-handler programs and compare interpreter traces with bounded
  declarative reduction.
- Preserve every implicit capability and row decision in a typed elaborated
  core that a separate verifier checks.

### Optimized implementations

- Implement a simple CPS backend and differentially test it against the
  reference interpreter.
- Prototype type-directed selective CPS using the complications documented by
  [Leijen](../30-sources/leijen-2017-type-directed-compilation-row-typed-algebraic-effects.md).
- Prototype native one-shot stack segments only if Catena commits to a native
  runtime, using the integration surface documented by
  [Sivaramakrishnan et al.](../30-sources/sivaramakrishnan-et-al-2021-retrofitting-effect-handlers-ocaml.md).
- Measure pure code, handler-heavy microbenchmarks, realistic scheduler and
  parser workloads, code size, continuation allocation, and stack-tooling
  behavior.

### Usability and diagnostics

- Test whether a unique capability can be inferred without making two matching
  capabilities depend silently on nesting.
- Show residual effect rows and clause-introduced effects in diagnostics.
- Compare `resume k x` with function-call syntax for teaching affine use.
- Evaluate whether public signatures can hide local instance names while
  remaining understandable and stable under refactoring.
- Ask users to predict handler selection and final traces before showing the
  result; prediction accuracy is the operational measure of “understandable.”

## Findings

The current evidence supports a constrained starting point:

- [Plotkin and Power](../30-sources/plotkin-power-2003-algebraic-operations-generic-effects.md)
  provide a precise boundary between algebraic operations and continuation-
  dependent nonexamples.
- [Plotkin and Pretnar](../30-sources/plotkin-pretnar-2009-handlers-algebraic-effects.md)
  justify interpreting the free computation with a deep handler.
- [Kammar, Lindley, and Oury](../30-sources/kammar-et-al-2013-handlers-in-action.md)
  show why open forwarding and partial interpretation are central to modular
  use, and why handler order remains semantic.
- [Hillerström and Lindley](../30-sources/hillerstrom-lindley-2018-shallow-effect-handlers.md)
  show that shallow handlers are a coherent alternative, but do not force both
  forms into the initial language.
- [Zhang and Myers](../30-sources/zhang-myers-2019-abstraction-safe-effect-handlers.md)
  demonstrate that effect safety alone does not prevent accidental capture
  across higher-order abstractions.
- [Biernacki et al.](../30-sources/biernacki-et-al-2020-effect-instances-lexically-scoped-handlers.md)
  demonstrate both the usefulness and metatheoretic delicacy of lexically
  named instances.
- [Tang et al.](../30-sources/tang-et-al-2024-soundly-handling-linearity.md)
  show that multi-shot continuations need a control-flow account when they can
  capture linear resources.
- Koka and OCaml establish two viable but different implementation families:
  selective CPS for row-typed polymorphic effects and native stack segments
  optimized for one-shot control.

These findings motivate the working hypotheses; they do not prove that their
combination is coherent.

### Bounded 0.1.5 prototype finding

The [C005 executable conformance record](../50-journal/2026-08-03-c005-executable-effect-conformance.md)
freezes one authorized Elixir/OTP 29 compiler identity. Its 19 focused cases
show agreement between an independently folded free-request evaluator and
generated BEAM for lexical selection, exact identity forwarding and
subtraction, deep resume, abort, nested handler order, and outer clause
requests. The same implementation checks affine use statically and with a
runtime consumed token, preserves identities through module interfaces, and
executes a public handler across a module boundary.

This is positive evidence for the bounded first-order design, not proof of the
whole hypothesis bundle. The implementation deliberately rejects effectful
anonymous functions and excludes resource cleanup, cancellation, exceptions,
host effects, scoped operations, performance claims, and user-facing parser
validation. Its finite corpus cannot establish most-generality, preservation,
progress, contextual abstraction, or usability.

## Outcome

Open. Normative 0.1.5 closes the bounded C005 implementation question, but this
wider inquiry resolves only when the archive contains:

1. one integrated operational and declarative Catena calculus;
2. proofs or mechanized checks for type safety, instance scope, handler
   selection, row-unifier most-generality, and the chosen abstraction property;
3. an executable free-tree interpreter and typed-core verifier;
4. a conformance corpus covering nested identity, forwarding, abort, resume,
   resource cleanup, and higher-order capture;
5. at least one optimized backend shown trace-equivalent to the reference;
6. measured evidence for runtime and tooling behavior; and
7. usability evidence that programmers can predict instance selection,
   resumption depth, and residual effects.

If lexical instances plus principal duplicate-label inference cannot satisfy
those conditions together, narrow the language: require explicit capabilities
in more signatures, use a simpler row theory, or delay user-defined handlers.
Do not preserve the surface feature by weakening its guarantees silently.

The curated evidence route is the
[Algebraic Effects and Handlers map](../10-maps/algebraic-effects-and-handlers.md).
Whether programmers can use that model through `effect`, `uses`, `handle`, and
`resume` without confusing it with domain failure or process termination is
tested by the
[vocabulary inquiry](how-should-catena-expose-mathematical-structure-without-mathematical-jargon.md).
