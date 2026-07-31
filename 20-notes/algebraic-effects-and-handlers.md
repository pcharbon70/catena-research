---
title: "Algebraic Effects and Handlers"
kind: note
created: "2026-07-31"
maturity: developing
tags:
  - algebraic-effects
  - catena
  - effect-handlers
  - effect-rows
  - language-design
  - resumptions
aliases:
  - "Algebraic effects deep dive"
  - "A greenfield algebraic-effect design for Catena"
---

# Algebraic Effects and Handlers

## Executive conclusion

Algebraic effects should be understood as a separation of **requests** from
their **interpretations**:

- an effect declaration gives typed operation signatures;
- performing an operation suspends the surrounding computation up to a
  handler;
- the handler receives the operation's argument and the delimited remainder
  of the computation;
- the handler may abort that remainder, resume it once, or—if the language
  permits—resume it more than once;
- a static effect system records which requests may remain unhandled, but does
  not by itself determine handler lookup, resumption multiplicity, or runtime
  representation.

The word *algebraic* is technical. An algebraic operation commutes with the
continuation supplied by later sequencing. In the semantic account developed
by [Plotkin and Power](../30-sources/plotkin-power-2003-algebraic-operations-generic-effects.md),
such operations correspond to generic effects for a strong monad. In
[Plotkin and Pretnar's handler account](../30-sources/plotkin-pretnar-2009-handlers-algebraic-effects.md),
a handler interprets the free model induced by those operations. This explains
why `throw`, nondeterministic choice, state access, and many I/O requests fit
the framework, while `catch`, dynamic scoping constructs, and unrestricted
continuation operators need additional treatment.

For a greenfield Catena, the smallest defensible initial design is:

1. nominal effect signatures containing first-order operations;
2. row-polymorphic function effects, with unhandled operations forwarded;
3. lexical, statically identifiable handler capabilities rather than
   unrestricted nearest-handler capture;
4. deep handlers, whose resumptions reinstall the handler;
5. affine resumptions that may be discarded or resumed once, cannot escape
   their clause, and are checked dynamically or linearly in the core;
6. no general multi-shot, shallow, or higher-order scoped handlers in the
   first language;
7. explicit language mechanisms for resource scopes and structured
   concurrency until their cancellation and cleanup laws are specified; and
8. a native stack-segment implementation only after a free-model interpreter
   and typed operational semantics agree on observable behavior.

This recommendation deliberately gives up the canonical “collect every
nondeterministic result by invoking the continuation twice” example in the
initial language. Multi-shot control can be added later with control-flow
linearity or a similarly explicit account of which captured resources may be
duplicated. Treating every resumption as freely copyable would silently
conflict with files, channels, mutable cells, foreign frames, and other linear
or stateful resources.

This is a fresh language-design synthesis. It does not use a Catena
specification, implementation, or design summary from another repository.

## Scope and decision standard

This note asks four different questions that are too often collapsed:

1. **Denotation:** which operations are algebraic, and what does a handler
   mean?
2. **Dynamics:** where does an operation transfer control, and what exactly is
   captured?
3. **Typing:** how are unhandled operations, handler transformations,
   resumption scope, and multiplicity represented?
4. **Implementation:** how are the semantics compiled without imposing
   control-flow overhead on unrelated code?

A proposed Catena mechanism is acceptable only if it has:

- a deterministic operational rule for handler selection;
- preservation and progress for closed programs, including a precise account
  of permitted top-level effects;
- an effect-row solver with a documented principality claim;
- an abstraction theorem, or a narrower property, showing higher-order code
  cannot accidentally intercept effects it was polymorphic over;
- a rule preventing a resumption from duplicating or discarding resources
  contrary to their type;
- defined behavior for exceptions, cancellation, cleanup, and foreign frames;
- a reference semantics against which optimized implementations can be
  tested; and
- diagnostics that identify the performed operation, intended capability,
  selected handler, and residual effect row.

The literature proves these properties for particular calculi. It does not
make them transfer automatically to Catena merely because Catena adopts
similar syntax.

## Vocabulary: six objects, not one feature

An effect system becomes easier to reason about when six roles stay distinct.

| Object | Role | Example |
| --- | --- | --- |
| Effect signature | Names a family of typed requests | `State s` with `get` and `put` |
| Operation | One request constructor | `get : Unit -> s` |
| Effect instance or capability | Identifies which use of a signature receives the request | state cell `left` rather than `right` |
| Effect row | Static approximation of requests that may escape | `<State s @ i, Console | e>` |
| Handler | Interprets a computation's return and operation cases | state as `s -> (a, s)` |
| Resumption | Delimited remainder of the handled computation | `k : operation-result -> handler-result` |

“Effect” is used informally for all six, but a language must say which one is
being named at each site. A row containing `State Int` does not say which
state cell handles it. A handler for `State Int` does not imply whether its
resumption is deep or shallow. A resumption's function-like surface does not
imply it can be copied like an ordinary closure.

## The algebra beneath the syntax

### Operations are constructors of computations

Suppose an operation accepts a parameter `P` and produces a reply `Q`:

```text
op : P -> Q
```

At the call site, `perform op p` appears to have result type `Q`, but it does
not compute a `Q` locally. It constructs or signals a request containing `p`
and waits for an interpreter to decide how the surrounding computation
continues.

A useful computation-tree intuition is:

```text
Computation a
  = Return a
  | Op request (reply -> Computation a)
```

The continuation stored after an operation is not an implementation trick
added by handlers; it is the branching structure required to describe what
should happen after the operation replies. A free monad is one concrete
representation of this tree. Native handlers can realize the same observable
control behavior without allocating the whole tree.

### What “algebraic” means

Schematic sequencing for an algebraic operation satisfies:

```text
op(p, k) >>= f  =  op(p, fn x -> k(x) >>= f)
```

Later computation can be pushed uniformly into every continuation position of
the operation. Plotkin and Power formulate this as naturality in the Kleisli
category and prove a correspondence between algebraic operations and generic
effects. The practical reading is that the operation constructs a request
without inspecting or capturing the particular continuation supplied after
it.

An effect signature may also declare equations. Nondeterministic choice might
be idempotent or commutative; state operations might obey read/write equations.
Then an interpretation claiming to be a model must respect those equations.
Most programming-language handler systems instead begin with a **free**
signature—operations with no equations—because arbitrary user handlers may not
preserve intended laws. Catena should do the same initially. Documentation may
state laws, but the optimizer must not rewrite by them until the language can
justify handler lawfulness.

### Not every effectful construct is algebraic

The distinction is between an operation and a construct that controls the
scope or continuation around other computations:

- raising a particular exception is algebraic; catching exceptions is a
  handler or scoped construct;
- reading and writing a fixed store are algebraic; allocating a fresh local
  cell introduces scope and identity;
- asking for an environment is algebraic; `local`, which runs a subcomputation
  under a modified environment, is scoped;
- emitting a request is algebraic; `bracket`, which governs acquisition,
  cancellation, and cleanup around a subcomputation, is higher-order;
- unrestricted `call/cc` is not algebraic in Plotkin and Power's sense because
  it directly depends on the current continuation.

[Effect Handlers in Scope](../30-sources/wu-et-al-2014-effect-handlers-in-scope.md)
demonstrates that first-order syntax delimiters are insufficient for operations
whose arguments are themselves computations. A language can extend the
framework with scoped or higher-order signatures, but that is a second design,
not a free consequence of first-order algebraic effects.

## Operational semantics

### The deep-handler reduction

Let `C` be an evaluation context containing no intervening handler selected for
operation `op`, and let handler `H` contain a return clause and an `op` clause.
A standard call-by-value deep semantics is captured by two rules:

```text
handle H in return v
  --> H.return(v)

handle H in C[perform op p]
  --> H.op(p, fn q -> handle H in C[return q])
```

The second rule explains all of the characteristic behavior:

- control is delimited by the selected handler, not by the whole program;
- the operation clause receives the already evaluated parameter `p`;
- `q` is the operation's reply type;
- the resumption contains the rest of `C`;
- resuming re-enters `H`, so later matching operations in `C` are handled by
  the same handler; and
- operations performed directly by the clause are not automatically captured
  by `H`, because the clause itself runs outside the reinstalled continuation.

The last point is observable and must be specified. A programmer who wants a
clause's own operation to reach the same handler must explicitly arrange
recursion or nesting according to the language's handler form.

### Three canonical clauses

An exception handler discards the resumption:

```text
throw(error, k) -> Error(error)
```

A state handler resumes exactly once, threading state through the handler
result:

```text
return x       -> fn s -> (x, s)
get((), k)     -> fn s -> k(s)(s)
put(next, k)   -> fn _ -> k(())(next)
```

A collect-all nondeterminism handler resumes more than once:

```text
choose((left, right), k) -> append(k(left), k(right))
fail((), k)              -> []
```

These are not merely different effect libraries. They demand different
control-flow multiplicities: zero uses, one use, and multiple uses of `k`.

### Forwarding is part of composition

An open handler interprets only its declared operations and forwards all
others to an outer handler. [Handlers in Action](../30-sources/kammar-et-al-2013-handlers-in-action.md)
shows why this matters: one handler can transform state requests into state
plus logging while remaining polymorphic in unrelated effects.

Effect polymorphism is the static counterpart:

```text
handle_state : (a ! <State s | e>) -> ((a, s) ! e)
```

The tail `e` says the handler preserves requests it does not interpret. A
closed handler that pretends `e` is empty prevents modular composition. An
untyped forward operation postpones failure until runtime. Catena needs both
open dynamics and row-polymorphic types.

### Handler order is semantic

Two handlers do not generally commute. A logging handler placed outside state
may observe operations that an inner state handler would otherwise consume; if
the state handler is outside, the logger may never see them. Similarly,
exception handling around state can either preserve, discard, or expose state
updates depending on the interpretations.

Algebraic effects improve modular definition and selective interpretation.
They do not imply that independently defined effects commute. Handler order is
program logic and should remain visible in syntax or elaborated evidence.

## Deep versus shallow handlers

A deep resumption automatically reinstalls the current handler. A shallow
resumption continues without it:

```text
deep k(q)     = handle H in C[return q]
shallow k(q)  = C[return q]
```

| Property | Deep | Shallow |
| --- | --- | --- |
| View of computation | Fold over a computation tree | One-step case split |
| Repeated matching operations | Handled automatically | Caller must install the next handler |
| Ordinary state, exceptions, search | Direct | More explicit plumbing |
| Streams, protocols, mutually changing handlers | Can be awkward | Direct control over the next interpreter |
| Resumption type | Returns under the same handler transformation | Exposes the remaining computation protocol |

[Hillerström and Lindley](../30-sources/hillerstrom-lindley-2018-shallow-effect-handlers.md)
show that deep and shallow handlers can simulate one another up to specified
administrative reductions. That expressiveness result does not make the choice
irrelevant. It changes default recursion, types, resource lifetime, and what a
programmer sees when resuming.

**Catena proposal:** expose only deep handlers initially. They match the free
model/fold account and make the common “interpret every request of this
signature” case local. Add shallow handlers only if stream, coroutine, or
protocol examples show that explicit rehandling is materially clearer and the
core calculus can state both forms without ambiguous syntax.

## One-shot, affine, and multi-shot resumptions

There are two related but distinct questions:

- may a handler clause use `k` zero, one, or many times?
- may a captured continuation be copied, stored, or resumed after its dynamic
  scope has otherwise ended?

| Discipline | Permitted uses | Representative effects | Main cost or risk |
| --- | --- | --- | --- |
| Exactly once | one | cooperative handoff, some protocols | cannot express abort |
| Affine / one-shot | zero or one | exceptions, state, generators, async | runtime use-after-resume check or affine typing |
| Multi-shot | any finite number | backtracking, probabilistic enumeration | continuation copying and duplicated resources |

Native OCaml handlers use one-shot continuations for use cases such as
concurrency, generators, and coroutines, and raise an exception on a second
resume. The implementation work in
[Retrofitting Effect Handlers onto OCaml](../30-sources/sivaramakrishnan-et-al-2021-retrofitting-effect-handlers-ocaml.md)
shows the efficiency advantage of moving stack segments instead of copying
them. It is evidence for a viable point in the design space, not evidence that
one-shot control serves every effect.

Multi-shot control becomes a soundness issue when the captured continuation
contains a linear value. Invoking the continuation twice can use a channel or
file twice; discarding it can leak an obligation. [Soundly Handling Linearity](../30-sources/tang-et-al-2024-soundly-handling-linearity.md)
documents such a bug in a language combining handlers and session-typed linear
resources, and develops control-flow linearity so continuation use agrees with
captured value use.

**Catena proposal:** make clause resumptions affine and lexically scoped in the
initial core:

- a clause may return without resuming;
- it may resume once;
- a second resume is rejected statically when the core can prove it, and must
  trap before reuse otherwise;
- the resumption cannot be stored, returned, captured by an escaping closure,
  sent to another task, or generalized;
- the type checker treats it as a distinct control capability, not an ordinary
  function value.

Multi-shot handlers should require a later, explicit `multi` capability and a
proof or inferred constraint that the captured continuation is duplicable.
Pure nondeterminism remains implementable in the initial language by building
an explicit search tree; what is deferred is transparent duplication of the
native continuation.

## Handler identity and abstraction safety

### Why nearest matching label is not enough

Suppose a higher-order `map` is effect-polymorphic in its callback. If `map`
internally installs a handler for an effect label that the callback also uses,
ordinary dynamic nearest-handler lookup may cause `map` to intercept a request
that belongs to its client. The program remains type safe in the narrow
progress/preservation sense but breaks representation independence: changing
an implementation can change which client effect is captured.

[Zhang and Myers](../30-sources/zhang-myers-2019-abstraction-safe-effect-handlers.md)
make this accidental handling problem explicit and develop tunneling semantics
in which effects unknown to higher-order polymorphic code pass through its
handlers. Their result demonstrates that “all effects are handled” is weaker
than modular abstraction safety.

### Multiple uses of one signature

Even without higher-order abstraction, a program may need two `State Int`
cells or two reader environments. Plain signature labels cannot distinguish
them. Nesting order chooses one implicitly, which makes refactoring handler
structure change meaning.

[Biernacki et al.](../30-sources/biernacki-et-al-2020-effect-instances-lexically-scoped-handlers.md)
model an effect instance as a lexically scoped name bound by a handler and
tracked in the type-and-effect system. Their formal development also shows
that combining instance binding, effect polymorphism, and reduction under
binders is delicate; “just attach a fresh integer at runtime” is not a complete
language design.

### A provisional Catena model

Catena should separate nominal **signature identity** from lexical **instance
identity**:

```text
effect State[s] {
  get : Unit -> s
  put : s -> Unit
}

-- schematic, not final syntax
with left  : State[Int] handled by state(0) in
with right : State[Int] handled by state(10) in
  perform left.get() + perform right.get()
```

The elaborated operation carries a capability selected statically. A handler
binds the capability for its handled expression, and an effect row can track
the capability when distinction matters:

```text
<State Int @ left, State Int @ right | e>
```

Public effect-polymorphic functions should quantify the identity rather than
leak a local name. Surface syntax may infer a unique ambient capability, but
ambiguity among two matching instances must require a qualifier; lexical
nesting alone must not silently decide. Higher-order code polymorphic in an
effect cannot handle that effect unless its type explicitly receives the
capability or handler evidence.

This is a proposal, not a settled calculus. The open inquiry must compare
lexical instances, tunneling, explicit capability passing, and dynamically
generated instances for inference quality and abstraction theorems.

## Type-and-effect design

### Effects belong on computations and arrows

Use `A ! e` for a computation returning `A` with effects `e`, and
`A ->{e} B` for a function whose body produces such a computation. Pure
functions abbreviate the empty row:

```text
A -> B  =  A ->{<>} B
```

An operation signature:

```text
op : P -> Q in E
```

gives a performance type schematically equivalent to:

```text
perform E.op : P ->{<E>} Q
```

The operation's result type is the input type of the resumption. It is not the
handler's final result type.

### A handler transforms both result and effects

A useful schematic handler type is:

```text
Handler E A B h
handle : Handler E A B h
      -> (A ! <E | e>)
      -> (B ! <h | e>)
```

`A` is the handled computation's return type, `B` is the handler's result type,
`e` is the forwarded tail, and `h` contains effects performed by handler
clauses. For an operation `op : P -> Q`, a deep clause receives approximately:

```text
p : P
k : Q ->{<h | e>} B
```

This explains several behaviors that exception-only syntax obscures:

- a handler may change the computation's result type;
- interpreting one effect may introduce another;
- a handler removes only the selected occurrence or instance;
- effects not named by the handler remain in `e`; and
- every operation clause and the return clause must agree on `B` and residual
  effects.

### Row equality is a semantic choice

[Koka's row-polymorphic effect system](../30-sources/leijen-2014-koka-row-polymorphic-effects.md)
permits duplicate effect labels so eliminating one label has a most-general
solution without pervasive lacks constraints. This differs intentionally from
record rows, where duplicate field labels are usually meaningless.

Catena can retain duplicate occurrences for inference while using nominal
signature and instance identities for selection. It must then specify:

- whether row equality is ordered, set-like, or multiset-like;
- how one handled instance is subtracted;
- how duplicate occurrences print in diagnostics;
- whether an instance variable can escape its handler;
- how effect masking interacts with polymorphic row tails; and
- what ambiguity remains when a row contains two instances of one signature.

### Generalization and resumptions

The earlier Catena type-system proposal already restricts generalization of
expansive effectful bindings. Handlers add a stricter local rule: a resumption
must never be generalized. Its types mention the handler's answer type,
residual effect row, capability identities, and control-flow multiplicity. Any
one of those escaping can make the handler's local invariant unsound.

The initial rule should be syntactic and semantic:

1. resumption variables are affine core binders;
2. their free variables include the handler's scoped type, effect, and
   instance variables;
3. no value containing a resumption can leave the operation clause;
4. no `let` under a resumption binder generalizes a variable fixed by those
   scoped environments; and
5. the typed core verifier independently checks the escape and multiplicity
   judgments.

Effect rows state **which** requests may occur. They do not state how often a
resumption runs, whether a resource is duplicated, or whether an operation
must occur before another. Those properties require multiplicities, protocols,
or a richer effect discipline.

### Closed programs and top-level effects

A closed executable should not be considered safe merely because the runtime
will search until it reaches the top of the stack. Catena should define a host
handler boundary:

```text
main : Unit ->{<Console, Process>} ExitCode
```

The platform interprets only this documented set. All other effects must be
eliminated before `main` or rejected statically. FFI escape hatches should
introduce a visible `Unsafe` or `Foreign` effect rather than turn “unhandled
operation” into an undocumented process trap.

## Scoped and higher-order effects

First-order operations accept values. Higher-order operations accept or delimit
computations:

```text
local    : Environment -> (Unit ->{e} a) -> a
catch    : (Unit ->{e, Throw x} a) -> (x ->{e} a) -> a
bracket  : acquire -> (resource ->{e} a) -> release -> a
timeout  : Duration -> (Unit ->{e} a) -> a
```

Encoding the subcomputation as an ordinary thunk hides important structure:
which handler applies inside it, whether it may escape, how effects are scoped,
and what happens if its resumption is discarded or duplicated. Wu, Schrijvers,
and Hinze show why a first-order syntax representation cannot in general give
handlers access to the scoped syntax required for such operations.

Catena should therefore reserve three categories:

1. **first-order algebraic operations** for ordinary typed requests;
2. **scoped operations** for handlers that interpret a delimited
   subcomputation; and
3. **structured runtime scopes** for cleanup, cancellation, and task lifetime,
   where the host must uphold guarantees even across exceptions and foreign
   calls.

The first release needs only the first category. `bracket` and structured
concurrency should not be marketed as ordinary library handlers until their
unwind semantics are proven under aborting and resuming clauses.

## Implementation strategies

The same surface semantics can be implemented in substantially different ways.

| Strategy | Strength | Main cost or complication | Best role |
| --- | --- | --- | --- |
| Free computation tree | Direct executable model; handlers are folds | allocation and dispatch overhead; stack behavior differs from direct style | reference interpreter and testing |
| Whole-program CPS | handlers and resumptions become ordinary control flow | changes calling convention broadly; interoperability and debugging costs | simple compiler core or closed world |
| Type-directed selective CPS | direct code remains direct when effects do not require CPS | polymorphic effect variables need multiple representations or conservative translation | portable optimizing compiler |
| Native stack segments or fibers | direct style, efficient one-shot capture, existing stack reused | runtime, GC, unwinding, debugger, profiler, and FFI integration | mature native runtime |

[Leijen 2017](../30-sources/leijen-2017-type-directed-compilation-row-typed-algebraic-effects.md)
presents an end-to-end Koka design with row inference, direct operational
semantics, and type-directed selective CPS. The paper reports that effect-type
simplification reduced the functions receiving CPS translation in Koka's core
library by over 80%; that is a result for that compiler and library, not a
universal overhead guarantee.

The OCaml retrofit instead captures portions of the native stack as fibers and
optimizes for one-shot continuations. Its reported macrobenchmarks average
about 1% overhead when handlers are not used, while retaining compatibility
with stack-sensitive tooling. This establishes feasibility for a carefully
engineered runtime, but not for multi-shot cloning or every language backend.

### Recommended implementation sequence

1. Define a small typed calculus and executable free-tree interpreter.
2. Write golden traces for return, abort, resume, nested handlers, forwarding,
   clause effects, instance selection, and resource unwinding.
3. Implement row inference and elaborate every implicit capability and handler
   choice into a typed core.
4. Add a simple CPS backend and differentially test it against the interpreter.
5. Measure representative direct-style workloads before choosing selective
   CPS or native stack segments.
6. Treat debuggers, backtraces, profilers, cancellation, GC roots, and FFI
   frames as semantic acceptance tests, not post-release optimizations.

## Comparisons that clarify the design

### Versus exceptions

Exceptions are one point in the handler space: `throw` has no useful reply and
the handler discards the continuation. Algebraic handlers generalize the
operation result type and expose the delimited continuation. Calling them
“resumable exceptions” is operationally suggestive but hides effect
polymorphism, interpretation changes, and multi-clause signatures.

### Versus monads and transformer stacks

A monad fixes a representation and sequencing discipline for a whole
computation. Monad transformers compose representations, but order affects
types and lifting can expose the stack. Algebraic operations let client code
name requests independently; handlers choose interpretations later and can
forward unknown operations.

This does not make handlers universally superior. A monad's explicit data can
be easier to serialize, inspect, replay, and reason about. The free-monad
implementation of handlers makes the relationship concrete. Catena should use
handlers where delayed interpretation and local control are the benefit, not
replace every explicit state machine with invisible control transfer.

### Versus delimited continuations

Effect handlers can be implemented using delimited continuations, and each
operation captures a delimited remainder. The algebraic interface adds named,
typed requests, structured clauses, effect tracking, and a disciplined
interpretation boundary. Raw delimited control is more primitive and can
express control patterns outside the algebraic theory. A compiler may lower
handlers to control operators without making those operators part of the
source language.

### Versus an effect row alone

An effect row is a static approximation, not a programming mechanism. It can
track exceptions in a language with no resumptions, I/O in a direct runtime,
or capabilities passed explicitly. Conversely, handlers without static rows
can be dynamically meaningful while leaving unhandled requests and accidental
capture unchecked. Catena needs the row system and the handler calculus to be
specified separately and then proved consistent.

## Proposed Catena core contract

The following matrix turns “support algebraic effects” into falsifiable design
choices.

| Axis | Initial Catena choice | Deferred alternative |
| --- | --- | --- |
| Signature identity | nominal declaration identity | structural operation bundles |
| Instance selection | lexical capability, statically elaborated | nearest dynamically matching label |
| Effect typing | open duplicate-label rows with instance-aware selection | sets, presence flags, subeffecting |
| Handler coverage | open by default; unmentioned effects forward | closed exhaustive handlers |
| Handler depth | deep | shallow |
| Resumption use | affine: zero or one | multi-shot with control-flow multiplicity |
| Resumption lifetime | clause scoped, nonescaping | first-class stored continuations |
| Operation order | ordinary call-by-value evaluation | lazy or parallel argument evaluation |
| Scoped computations | separate future construct | encode all scopes as thunks |
| Top-level behavior | documented host effects only | runtime search failure |
| Reference implementation | free tree | none |
| Optimized implementation | chosen after measurement; likely selective CPS or stack segments | one mandatory representation across backends |

### Surface principles

- `perform` should remain visible at request sites unless an operation is
  intentionally imported with unmistakable syntax.
- Handler syntax should distinguish the return clause from operation clauses.
- The resumption should have a dedicated invocation form such as `resume k x`,
  reinforcing that it is not an ordinary function.
- An ambiguous effect instance should be a compile error with candidate
  capabilities listed.
- Public signatures should show residual effect rows but may quantify lexical
  instance identities with a readable capability abstraction.
- Diagnostics should say whether an effect escaped because no handler was in
  scope, because the wrong instance was selected, or because a clause itself
  introduced the effect.

## Unsound or misleading shortcuts

### “The type row says it is safe”

Rows can prove absence of unhandled named requests under their typing rules.
They do not prevent multi-shot duplication of linear values, accidental
handling across an abstraction, or cleanup loss when a clause aborts.

### “Handlers compose automatically”

Open handlers compose syntactically by forwarding, but their order can change
meaning. Duplicate signatures also require identity. Composition is a
capability, not commutativity.

### “Every effect is algebraic”

Scope-taking constructs and unrestricted continuation inspection do not obey
the first-order algebraic account. Encoding them as thunks may recover some
programs while losing the equations or scoping discipline that made the
construct safe.

### “Deep and shallow are only syntax”

They can simulate one another, but they expose different recursion and
resumption protocols. A surface language must choose a default and type it.

### “One-shot means exactly once”

Exception handlers discard continuations, so the practical native discipline
is normally affine: at most one resume. Exactly-once use is a stricter linear
property.

### “Multi-shot is just calling a function twice”

A resumption contains stack frames and their resources. Copying it may require
copying or sharing mutable state, foreign state, dynamic bindings, handlers,
and cleanup obligations. Ordinary function syntax hides those costs.

## Verification and falsification

The proposal should be narrowed or rejected if any of these tests fails.

### Static properties

- The effect-row unifier returns a most-general solution under the declared row
  equality.
- Handling one effect occurrence preserves every unrelated row tail.
- No well-typed operation can select a handler for a different nominal
  signature or lexical instance.
- Higher-order effect-polymorphic code cannot intercept an effect introduced
  solely by its callback unless its type explicitly receives that authority.
- Resumption types cannot escape their handler's answer type, instance scope,
  residual row, or multiplicity context.
- A closed `main` contains only the documented host effects.

### Dynamic properties

- Deep resume reinstalls the selected handler; a clause's direct operations
  follow the documented outer lookup rule.
- Forwarding preserves the operation parameter, selected identity, and
  continuation behavior.
- A discarded continuation runs exactly the cleanup mandated by the resource
  model, neither silently leaking nor inventing finalizers.
- A second resume of an affine continuation is impossible or traps before any
  duplicated user action.
- Exception propagation, cancellation, stack traces, and foreign calls behave
  identically in the reference and optimized implementations.

### Differential programs

At minimum, compare traces for:

1. two nested handlers for different effects;
2. two instances of the same signature;
3. a handler clause that performs its own handled operation;
4. an effect-polymorphic higher-order callback crossing an internal handler;
5. abort before and after resource acquisition;
6. one-shot double resume;
7. deep repeated operations and an explicit shallow simulation;
8. handler-order reversal where semantics should differ; and
9. pure code compiled with and without effect support.

## What the evidence supports

The combined primary literature supports these conclusions:

- algebraic operations have a precise continuation-compatible semantic
  criterion, not just a programming-language branding;
- handlers interpret operation trees and may change both result type and
  remaining effects;
- open forwarding and effect polymorphism are central to modular handling;
- deep and shallow handlers are expressively related but operationally
  distinct;
- one-shot native handlers are efficient and useful, while multi-shot handlers
  need an account of captured linear resources;
- plain dynamic nearest-handler lookup can violate higher-order abstraction;
- multiple instances of one signature require names, capabilities, or another
  explicit identity mechanism;
- first-order operations do not subsume scoped computations; and
- both selective CPS and segmented native stacks are viable implementation
  families with different polymorphism and runtime-integration costs.

The evidence does **not** yet establish that the provisional Catena combination
has principal inference, abstraction safety, or acceptable ergonomics. Those
properties require one integrated calculus and prototype.

## Research priorities

1. Specify lexical capability binding and compare it with tunneling on the same
   higher-order examples.
2. Define an instance-aware duplicate-label effect-row theory and prove or
   disprove principal unification.
3. Give deep affine handlers an operational semantics with explicit cleanup
   behavior.
4. Decide whether the affine property lives in syntax, an affine core type, a
   runtime token, or all three.
5. Build the free-tree interpreter and a small corpus covering state,
   exceptions, logging, generators, async scheduling, and explicit search.
6. Specify a separate calculus for scoped resource and concurrency operations
   before exposing `bracket`, `timeout`, or task groups as handler libraries.
7. Compare selective CPS and stack-segment backends using trace equivalence,
   stack tooling, FFI, and measured overhead.

These decisions are tracked in
[Which Algebraic-Effect Semantics Should Catena Adopt?](../40-inquiries/which-algebraic-effect-semantics-should-catena-adopt.md).

## Source trail

### Foundations

- [Plotkin and Power 2003](../30-sources/plotkin-power-2003-algebraic-operations-generic-effects.md)
  — algebraic operations, generic effects, strong monads, and nonexamples.
- [Plotkin and Pretnar 2009](../30-sources/plotkin-pretnar-2009-handlers-algebraic-effects.md)
  — handlers as interpretations of free models and induced homomorphisms.

### Composition and handler shape

- [Kammar, Lindley, and Oury 2013](../30-sources/kammar-et-al-2013-handlers-in-action.md)
  — modular open handlers, forwarding, formal dynamics, and implementation
  comparisons.
- [Wu, Schrijvers, and Hinze 2014](../30-sources/wu-et-al-2014-effect-handlers-in-scope.md)
  — the gap between first-order operations and scoped subcomputations.
- [Hillerström and Lindley 2018](../30-sources/hillerstrom-lindley-2018-shallow-effect-handlers.md)
  — formal shallow handlers and their relationship to deep handlers.

### Typing, identity, and control safety

- [Leijen 2014](../30-sources/leijen-2014-koka-row-polymorphic-effects.md)
  — duplicate-label effect rows, inference, and effect-directed
  generalization.
- [Zhang and Myers 2019](../30-sources/zhang-myers-2019-abstraction-safe-effect-handlers.md)
  — accidental capture and abstraction-safe tunneling.
- [Biernacki et al. 2020](../30-sources/biernacki-et-al-2020-effect-instances-lexically-scoped-handlers.md)
  — lexically named effect instances and their metatheoretic constraints.
- [Tang et al. 2024](../30-sources/tang-et-al-2024-soundly-handling-linearity.md)
  — control-flow linearity for multi-shot handlers over linear resources.

### Compilation and runtime evidence

- [Leijen 2017](../30-sources/leijen-2017-type-directed-compilation-row-typed-algebraic-effects.md)
  — direct semantics and type-directed selective CPS for row-typed effects.
- [Sivaramakrishnan et al. 2021](../30-sources/sivaramakrishnan-et-al-2021-retrofitting-effect-handlers-ocaml.md)
  — one-shot native stack segments, runtime integration, and measured
  overheads.

## Connections

- [A Greenfield Type System for Catena](catena-greenfield-type-system.md)
  supplies the wider inference and effect-row architecture that this note
  refines.
- [How Hindley–Milner Type Inference Works](hindley-milner-type-inference.md)
  explains the principal rank-1 baseline and why handler typing must state its
  additional solver and generalization claims.
- [Algebraic Effects and Handlers](../10-maps/algebraic-effects-and-handlers.md)
  provides curated reading trails through this research bundle.
