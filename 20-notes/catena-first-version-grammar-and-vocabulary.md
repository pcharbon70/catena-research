---
title: "Catena First-Version Grammar and Vocabulary"
kind: note
created: "2026-09-15"
maturity: developing
tags:
  - catena
  - language-design
  - syntax
  - api-design
  - algebraic-effects
aliases:
  - "Catena first public surface proposal"
---

# Catena First-Version Grammar and Vocabulary

## Recommendation and status

Use **`fn`, `transform`, `total transform`, parenthesized calls, brace blocks,
immutable `let` bindings, explicit `match`, and data-last pipelines**. Use
`guarantee` to connect checked declarations to named laws. Keep effects visible
through `uses`, `request`, `handler`, `handle`, `reply`, and `resume`. Keep the
current behavior-oriented standard operations: `map`, `map2`, `and_then`,
`collect_map`, and `summarize`. Teach these through ordinary data before
introducing their trait hierarchy.

This is a concrete design selected under the user's 15 September 2026 request,
combining [An Approachable Vocabulary for Catena](approachable-language-vocabulary.md)
with the accepted directions in
[Grammar and Vocabulary for Approachable Catena](grammar-and-vocabulary-for-approachable-catena.md).
It chooses spellings and explains their meaning; it does not merely propose
another vocabulary investigation. “First version” means the first coherent
public source surface, not a declaration of language release `1.0`.

**All Catena code below illustrates the proposed source surface. It has not
been compiled by a public Catena parser.** Existing normative semantic owners
constrain the design; this note has no normative authority. The adoption work
listed below is required before source conformance can be claimed. No compiler
implementation, performance result, or observed human comprehension is claimed.

The previous user-held vocabulary freeze is released for this design. The user
has explicitly excluded participant studies during language development.
Engineering evaluation will use semantic review, adversarial examples,
automated parsing and conformance, formatting, and diagnostic checks. The
historical [G137 observed-usability contract](../60-specification/usability-gate/observed-prediction-transfer-and-repair.md)
is not passed by those checks. A successor to the relevant
[G139 release policy](../60-specification/release-readiness/evidence-gates-and-release-claims.md)
must record the changed development policy before making complete/stable claims
under a different evidence profile. Existing observations and historical
decisions remain intact; no human study is a prerequisite of the work proposed here.

## A first complete example

The example defines a pure module. `Shipping.cat` contains:

```catena
module Shipping

export type Parcel {
  Parcel(record { weight: Int, fragile: Bool })
}

/// Calculate a price from whole, nonnegative weight units.
export fn price(parcel: Parcel) -> Int {
  match parcel {
    Parcel(details) -> {
      let base = details.weight * 3
      if details.fragile { base + 5 } else { base }
    }
  }
}

export fn example() -> Int {
  let parcel = Parcel(record { weight = 4, fragile = true })
  parcel |> price
}
```

`example()` returns `17`. The comment describes an application assumption;
`Int` alone does not prove nonnegativity. A production constructor can validate
the weight and return a `Result`. Neither the type declaration nor its comment
silently adds refinement types.

This example exposes a nominal datatype, an immutable record, a pure function,
pattern matching, an expression-valued conditional, and composition. It needs
none of the words “functor,” “monad,” or “algebraic.” The mathematical structure
remains available when the program needs reusable operations or guarantees.

## Why these choices

The research supports design mechanisms and cautions, rather than proving that
one punctuation scheme is universally easier. Delimiters make written
boundaries inspectable; one call form reduces competing interpretations;
behavioral operation names expose dependency; explicit requests expose service
use. Those are the design reasons for the choices here, not empirical rankings.

The accepted study decisions are GV-01 A, GV-02 B, GV-03 B, GV-04 A, GV-05 B,
GV-06 B, GV-07 B, GV-08 C, GV-09 B, GV-10 B, and GV-11 B. GV-12 retains the
semantic-audit and adversarial-example parts of C, with its participant-study
requirement explicitly overridden by the user. GV-01/GV-04 now select their
leading candidates instead of requiring a comparison study. The
[decision register](design-decision-register.md#first-version-source-design-2026-09-15)
preserves the four original alternatives, recommendations, and selections.

The further concrete forks are recorded below. **Each selected option is the
agent's recommendation under the user's delegation**, not a claim that the
user separately approved every spelling. Existing retained rules are identified
as constraints rather than presented as newly invented choices.

| ID | Four concrete alternatives considered | Selected and why |
| --- | --- | --- |
| FV-01 | A `fn`; B `def`; C `transform`; D separate `fn` and `action` declarations | **A** for the general callable declaration. One short word covers named and anonymous functions; effects stay in the type rather than creating an incompatible function species. The later FV-25 decision adds `transform` as a checked restriction that elaborates to this same callable model. |
| FV-02 | A round calls and square type arguments; B round brackets for both; C whitespace for both; D angle type brackets | **A**. `f(x)` and `List[a]` have different visible roles, and `<` retains its comparison meaning. |
| FV-03 | A `let` plus final expression; B bare assignment; C mandatory `return`; D mutable declarations by default | **A**. Introduces a name explicitly, preserves expression-oriented control, and does not suggest reassignment. |
| FV-04 | A brace constructor families with exact payload lists; B equals-and-bar declarations; C classes with constructor methods; D implicit structural alternatives | **A**. Reuses block structure while retaining nominal identity; no new bar operator or class model. |
| FV-05 | A `record` and `update` forms with value-headed field access; B bare braces for records and blocks; C tuple-only products; D method-style mutable fields | **A**. The opener distinguishes data from executable blocks before type checking. |
| FV-06 | A plain-name parameters/bindings and explicit `match`; B all patterns everywhere; C implicit failing destructuring; D programmable patterns | **A**. Keeps retained binding rules and makes the place for branching visible; comprehensions retain their separate irrefutable-pattern rule. |
| FV-07 | A `export` on declarations and explicit category-tagged imports; B everything public; C wildcards and aliases; D inferred exports | **A**. Readable ownership with private defaults and no import-order convention. |
| FV-08 | A canonical `Module.member` including constructors; B `Module.Type.Constructor`; C nested modules; D type-directed qualification guessing | **A**. Follows the newer namespace contract, with constructor owner identity retained in metadata. |
| FV-09 | A current 17 trait names; B restore every earlier exploratory name; C mathematical names; D dual source aliases | **A**. Keeps the retained ABI and its improvements to ambiguous older names. |
| FV-10 | A `Option[a]`, `Result[e,a]`, `Validation[e,a]`; B value-first outcomes; C exceptions for expected failure; D one universal nullable outcome | **A**. Names absence, fail-fast outcomes, and accumulation distinctly; the success parameter remains available for unary mapping. |
| FV-11 | A `request`; B `perform`; C ordinary invisible calls; D different cue per service | **A**. Names the application author's action without implying how a handler implements it. |
| FV-12 | A omitted `uses` means pure at exported boundaries, private inference, optional explicit purity; B mandatory `uses` on every exported function; C infer exported and private effects; D documentation-only effects | **A, revised at the user's request**. Pure public functions need no empty annotation; nonempty requirements remain explicit and checked, while `uses {}` can assert purity where useful. |
| FV-13 | A named capability entries plus `using` evidence at calls; B nearest-handler selection; C manually passed runtime dictionaries; D global service lookup | **A**. Expresses retained identity selection without making capabilities storable values. |
| FV-14 | A named `handler`, explicit `handle`, terminal `reply`, advanced `resume`; B implicit reply everywhere; C callbacks only; D raw continuations everywhere | **A**. The common clause reads as a response while control-changing clauses remain explicit. |
| FV-15 | A `chain Family` with `bind` and `yield`; B overloaded `do`; C implicit error propagation after every call; D new symbolic bind operators | **A**. The selected outcome family determines sequencing; ordinary requests and resource scopes keep their own forms. |
| FV-16 | A `scope ... acquire ... release ... within ...` with explicit handle reads; B generic `defer`; C garbage-collection cleanup; D automatic foreign-handle ownership | **A**. Names the retained bounded ownership operation without promising broader resource semantics. |
| FV-17 | A `trait`, `implementation`, `requires`, `derives`, linked `guarantee`; B classes/inheritance; C implicit duck typing; D formal symbols | **A**. Checked behavior stays discoverable, and a named guarantee does not masquerade as proof. |
| FV-18 | A existing `for`/`in`/`case`/`when`/`yield` in one brace form; B SQL clauses; C list-first bar notation; D a generic target-selecting comprehension | **A**. Preserves the settled result-last, lists-only contract. |
| FV-19 | A ordinary typed library operations for processes/services; B an actor sublanguage; C `async`/`await` over all effects; D shell-like commands | **A**. Avoids confusing dependency with concurrency or inventing a second effect system. |
| FV-20 | A source `specification` claims and external canonical governance bundles; B governance mixed into executable blocks; C prose comments as authority; D a new general policy language | **A**. Gives claims a visible source form while retaining exact signed identities and the closed policy evaluator. |
| FV-21 | A closed initial effect annotations and pure anonymous functions, with explicit later row extension; B silently admit effectful callbacks; C infer higher-rank rows; D remove effect checking | **A**. The first surface is honest about the integrated kernel's boundary; richer retained contracts need separately tracked integration. |
| FV-22 | A fixed operators and canonical formatter; B user fixities; C several block styles; D editor-defined formatting | **A**. Keeps reading and diagnostics independent of local syntax extensions. |
| FV-23 | A explicit discard with `let _ = expression`; B implicit discard of any non-final expression; C implicit discard only for Unit; D mandatory statement terminators choosing discard | **A**. Preserves the existing sequencing idiom and makes ignored outcomes visible without introducing a second discard policy. |
| FV-24 | A contextual `value` members for zero-argument trait methods; B Unit-taking wrappers as the ABI; C call every member a constant; D omit empty/identity methods | **A**. Preserves retained method arity and distinguishes an implementation-supplied method slot from an associated constant. |
| FV-25 | A make `transform` a separate runtime callable type; B make it a pure declaration that elaborates to an ordinary function; C accept it as an unchecked synonym for `fn`; D keep it only as documentation prose | **B, approved by the user**. It visibly asserts an empty effect row without duplicating calling, currying, closure, or runtime representation rules. |
| FV-26 | A make `total transform` an opt-in checked declaration rejected when totality cannot be established; B issue an advisory termination warning; C accept bounded tests as totality; D trust an author annotation | **A, approved by the user**. Totality becomes useful evidence only when checked; this requires a versioned amendment to the retained no-totality-validity-gate rule. |
| FV-27 | A link `guarantee` to stable typed claims with separate evidence status; B embed arbitrary Boolean law bodies directly in declarations; C treat comments as laws; D let a promise immediately authorize optimization | **A, approved by the user**. Stable claims preserve identity and evidence provenance; the word alone is never proof or optimizer authority. |

FV-12 replaces the initial mandatory empty annotation after the user requested
the simpler rule. The [revision record](design-decision-register.md#fv-12-revision-optional-empty-effect-annotations)
preserves the original alternatives and the user-approved change.
FV-25–FV-27 record the user's subsequent approval of the recommended transform,
totality, and law model. Their
[adoption record](design-decision-register.md#transform-totality-and-guarantees)
preserves the semantic and versioning qualifications.

## Words and their jobs

The small everyday layer is `module`, `import`, `export`, `type`, `fn`, `let`,
`if`, `else`, and `match`. `record` introduces structural data. `transform`
and `total` state stronger properties when a library wants those guarantees.
A programmer
using services adds `uses`, `request`, and `handle`. Library and handler authors
encounter the remaining words only when they need those facilities.

| Role | Chosen vocabulary | Meaning |
| --- | --- | --- |
| Ordinary data | value, type, record, tuple, variant, payload | Describe values and their structure. No implicit null or mutable object model. |
| Calculation | function, `fn`, `transform`, `total`, parameter, argument, result | `fn` is general; a transform is pure; a total transform is also terminating and trap-free in the semantic model. |
| Local naming | `let` | Introduce one immutable, non-recursive name. |
| Choice | `if`, `else`, `match`, `when`, `or` | Boolean branching; exhaustive case analysis; restricted clause guard; pattern alternatives. |
| Visibility | `module`, `import`, `export`, `opaque` | Declare the unit, admitted names, public declarations, and abstract type exports. |
| Generic behavior | `trait`, `implementation`, `requires`, `derives`, `guarantee` | Define requirements, supply coherent evidence, request permitted derivation, and name checked law schemas. |
| External abilities | `effect`, `uses`, `request` | Declare a request family, require selected capabilities, issue one request. |
| Interpretation | `handler`, `handle`, `reply`, `resume`, `with`, `as`, `using` | Define/install an interpretation, continue explicitly, and select identity evidence. |
| Outcome sequencing | `chain`, `bind`, `yield` | Dependent pure steps through one selected `Workflow` family. |
| Finite traversal | `for`, `in`, `case`, `when`, `yield` | Ordered list production with visible filtering. |
| Owned lifetime | `scope`, `acquire`, `release`, `within`, `read` | Create a bounded scope and access its immutable payload. |
| Verification | `specification`, `verification`, `rule`, `example`, `conformance`, `attestation`, `assumption` | Separate claims, finite checks, external evidence, and explicitly unverified premises. |

`true`, `false`, `rec`, `transform`, `total`, `guarantee`, `variant`, `update`,
`for`, `handles`, `return`,
`associated`, and `determines` also have grammar roles below. `transform`,
`total`, and `guarantee` are contextual in the declaration positions defined
below, so an established ordinary identifier with the same spelling remains
unambiguous outside those positions. `return` is a
handler-clause header only; it is not an early-exit expression. `Type` is a
kind name. `Mapper`, `Result`, `List`, and operation names are ordinary library
identifiers, not magic lexer keywords. No public synonyms such as both `def`
and `fn`, or both `perform` and `request`, are accepted.

Contextual words such as `value`, `datatype`, `instance`, `action`, and
`profile` are closed tags inside imports or specifications. They do not change
the meaning of arbitrary expressions. The implementation must publish the
exact reserved/contextual inventory as part of lexical adoption.

## Source, layout, and literal conventions

Keep the retained source encoding, Unicode security rules, numeric decoding,
and [comment forms](../60-specification/comments-and-documentation-comments/comment-lexing-and-layout.md).
Write ordinary comments with `//` or nested `/* ... */`; attach documentation
with `///` or the admitted documentation block form. Examples use ASCII names
for readability, without withdrawing the admitted Unicode identifier policy.

Braces define blocks; indentation does not. Canonical formatting uses two
spaces per nesting level. Top-level declarations and block forms are separated
by hard newlines; `;` is available for explicit separation. The last expression
is the block value. Empty expression blocks are rejected: write `()` for Unit.
Every earlier computation is explicitly bound with `let`; use
`let _ = expression` to discard a result deliberately. There are no bare
non-final expression statements. The existing unused-binding warning and
`_`-prefix exemption remain in force; discarded computations still execute.

Parentheses and square brackets continue across lines. A comma does not
globally suppress a newline. Record, type-member, row, and import productions
explicitly admit hard newlines at their item boundaries. An operator such as
`|>` preserves its existing joining behavior. Multiline records are therefore
legal by their own grammar, not by an indentation heuristic:

```catena
let address = record {
  street = "Main Street",
  postal_code = "H0H 0H0"
}
```

Use existing integer, float, text, character, and binary literal rules where
their owning chapters admit them; this note adds no interpolation, implicit
numeric coercion, or alternate string delimiters. Lists use `[a, b]`; tuples
use `(a, b)`; `()` is Unit; `(a)` is grouping. A singleton tuple has no new
surface shorthand in this version. Indexing is an explicitly named library
operation, leaving `[]` unambiguously available for type application after a name.

The proposed new punctuation is **`:` for annotations/labelled types and `=`
for definitions/labelled values**. Neither is a new infix expression operator.
Retain `->` for type arrows and match arms. Do not add `=>`, `<-`, bare `|`,
custom operator declarations, `/`, or `%` in this surface. Named numeric
operations retain their existing checked contracts.

## Functions, application, and composition

```catena
fn add(x: Int, y: Int) -> Int { x + y }

let increment = add(1)
let six = increment(5)
let also_six = add(1, 5)
let ten = [1, 2, 3] |> List.map(increment) |> List.summarize(add, 1)
```

The last binding is `10`: mapped values are `[2, 3, 4]`, reduced from `1`.
The snippet assumes `List` is imported; the examples in this section are
fragments inside an appropriate definition, not top-level mutable scripts.

Catena keeps [semantic unary application](../60-specification/functions-and-calls/arity-and-application.md).
`add(1, 5)` means `add(1)(5)`. Evaluate the callee, evaluate `1`, apply the
first stage, then evaluate `5` and apply the remaining stage. Do not first
evaluate every argument and then make a host-arity call. `f(a)` can correctly
be a function value. `f((a, b))` supplies one tuple argument.

`fn add(x, y) { body }` elaborates to nested unary functions whose body runs
at the final stage. `fn fresh() { body }` has one unnamed Unit parameter;
`fresh()` means `fresh(())`. This is convenient spelling for an ordinary
function, not a second zero-arity calling model. Constructor calls, by
contrast, have the exact declared product payload arity and cannot be partially
applied; use `fn(x) { Some(x) }` when a constructor needs a function wrapper.
Requests and handler setup also take exact argument lists; their empty `()`
means no declared request/setup payloads. Unit insertion belongs only to
ordinary function application and function declarations.

Anonymous functions use the same cue:

```catena
List.map(fn(weight) { weight * 3 }, weights)
```

Private parameters and results may be inferred under existing rank-1 rules.
Exported functions declare type parameters, parameter/result types, constraints,
and any nonempty effect requirements. Omitting `uses` on an exported function
declares a closed pure contract; it does not infer effects into the public API.
An explicit `uses {}` remains an optional purity assertion, including on private
functions whose effects would otherwise be inferred. The initial anonymous-function
surface has a closed empty effect row. Pure means no residual effect requirement;
a locally handled request may still leave an empty row. Purity does not guarantee
termination or immunity from traps and finite resource limits.

The pipe is ordinary function application written in processing order:

```catena
parcel
|> normalize
|> label
```

Evaluate the left operand, evaluate the right function, then apply it. A partial
call such as `List.map(normalize)` is one such function. There is no implicit
insertion into the first argument and no placeholder binding rule. Direct
`List.map(make_callback(), make_values())` and a reversed written pipe need
not have the same effects while their operands are being formed. Bind effectful
operands explicitly before rearranging them. Ordinary wrappers pre-evaluate
their arguments before issuing primitive trait dispatch, preserving the
[separate call and trait evaluation rules](../60-specification/evaluation-order/ordered-forms-and-entry-rule.md).

Calls, explicit type application, and field access bind more tightly than
prefix `-` and `!`. Below that, keep the
[fixed ladder](../60-specification/operators-and-punctuation/precedence-and-associativity.md):
`*`; `+ -`; comparisons; equality; `&&`; `||`; `|>`.
Pipes group left. Comparison/equality chains remain invalid: use
`a < b && b < c`. No formatter may silently regroup such an invalid expression.

Use ordinary named self-recursion under the existing checker and `rec { ... }`
for a mutually recursive declaration group. `let` does not introduce recursion.
No `return`, `break`, `continue`, exception statement, or hidden mutable loop
is added to expression evaluation.

## Functions, transforms, totality, and guarantees

These declarations form a progression of checked promises while retaining one
function representation and one calling model:

| Declaration | Additional checked meaning |
| --- | --- |
| `fn` | An ordinary curried function; its effect contract follows the public/private rules above. |
| `transform` | An ordinary function constrained to a closed empty effect row. It can still diverge or trap. |
| `total transform` | A transform additionally established to terminate and avoid language-level traps for every admitted input value. |
| `total transform ... guarantee ...` | A total transform connected to one or more named typed law claims and separately classified evidence. |

### `transform` is a restriction, not another callable species

```catena
transform normalize(name: Text) -> Text {
  Text.trim(name)
}

fn load_name(id: UserId) -> Text uses {users: UserStore} {
  request users.find_name(id)
}
```

`transform` elaborates to the same semantic function form as an ordinary `fn`
with an explicit closed empty effect row. It uses the same currying, partial
application, closure, parameter, call, and BEAM representation rules. A transform
can be passed wherever its ordinary function type is accepted. Its purity
evidence is retained in checked source/interface metadata and erased from the
runtime value.

A request or call with a nonempty residual effect row inside `normalize` is a
declaration error. A locally handled request may be admitted only when the
resulting row is empty under the retained handler rules. `transform` says
nothing about termination, traps, performance, allocation, or mathematical
laws. It is more visible than an omitted public `uses` and, unlike omission on
a private `fn`, forbids effect inference. Writing `uses` on a transform is
redundant and rejected; use `fn ... uses {...}` for an effectful computation.

The initial form is for named declarations. Anonymous functions remain `fn`
and pure under the initial anonymous-function rule, avoiding a second lambda
grammar with no additional semantic distinction.

### `total transform` is an opt-in verified claim

```catena
total transform absolute(value: Int) -> Int {
  if value < 0 { -value } else { value }
}
```

For every well-typed input in Catena's abstract semantic model, a total
transform must reach a value of its result type in finitely many semantic steps
and must not reach a language-level trap. Its effect row is already empty because
it is a transform. A normal failure value is still a value, so expected partial
domain operations can expose total interfaces:

```catena
total transform checked_divide(left: Int, right: Int)
  -> Result[DivisionProblem, Int]
{
  if right == 0 {
    Result.Error(DivisionByZero())
  } else {
    Result.Ok(Int.quotient(left, right))
  }
}
```

This example assumes `Int.quotient` is certified total for a nonzero divisor
under the numeric contract and that the branch fact is available to the checker.
If either fact cannot be established, the `total transform` declaration rejects;
a passing example or timeout is not a substitute.

The initial checker should be deliberately conservative. It admits acyclic
calls to certified total operations, exhaustive branching, and structural
recursion whose recursive arguments are visibly smaller. For example:

```catena
total transform length[a](values: List[a]) -> Int {
  match values {
    List.Empty() -> 0
    List.Prepend(_, rest) -> 1 + length(rest)
  }
}
```

It rejects explicit trap producers, partial primitives without a proved safe
condition, calls lacking totality evidence, dynamic/unsafe/foreign operations,
and recursion whose decrease it cannot establish. Mutually recursive definitions
require a single checked decreasing argument across their strongly connected
group. General well-founded measures and proof-supplied termination can be
added later with their own four-way design and proof contract; the first version
does not guess them from tests or timeouts.

The totality evidence belongs to the declaration and interface, not the runtime
closure representation. A named total transform passed as a callback can carry
that static evidence where a law checker requires a total callback. An arbitrary
function value is not promoted by runtime observation. Exact rules for preserving
evidence through partial application and higher-order interfaces belong to the
totality adoption slice and must be tested before completion.

“Total” does not promise completion on a finite physical machine. Memory
exhaustion, configured implementation limits, process termination, forced VM
loss, and unavailable hardware remain classified by their existing owners. The
claim is termination and absence of language-level traps in the abstract model,
not a realtime deadline, constant cost, or infallible deployment.

The normative
[0.1.99 opt-in totality amendment](../60-specification/opt-in-totality-validity/explicit-total-declaration-gate.md)
now replaces the retained 0.1.31 rule that had permanently forbidden totality
analysis from gating validity. It permits rejection only after a later slice
admits an explicitly total declaration under a complete proof, verifier,
diagnostic, compatibility, limit, and evidence contract. Removing `total`
leaves ordinary legal recursion governed by the unrestricted rule. The
amendment deliberately adds no source token or checker, so this proposal still
does not mark `total transform` adopted or implemented.

### `guarantee` names a law obligation

`guarantee` connects a declaration to a stable typed claim; it does not embed an
unchecked equation or assign its own proof status:

```catena
total transform absolute(value: Int) -> Int
  guarantee AbsoluteLaws.Idempotent
{
  if value < 0 { -value } else { value }
}

verification fn absolute_idempotent(value: Int) -> Bool {
  absolute(absolute(value)) == absolute(value)
}

specification AbsoluteLaws {
  rule Idempotent on value absolute = absolute_idempotent
  example Positive for Idempotent(3) = true
  example Negative for Idempotent(-3) = true
}
```

The elaborator resolves `AbsoluteLaws.Idempotent`, checks that its subject is
this exported value, and verifies that its quantified inputs and result agree
with the transform. Multiple obligations repeat the singular clause or use a
comma-separated claim list; canonical formatting uses one `guarantee` line per
claim. Claim identity and semantic digest follow the retained specification
graph, so renaming display text or formatting source does not invent a new law.

The clause declares an obligation. Its evidence remains one of the admitted
statuses: `promised`, `tested`, or `derived`. A finite passing example or generated
suite can establish only recorded bounded evidence; it does not prove the
equation for every input. `trusted` and `proved` remain unavailable until their
own proof/governance design is admitted. A `guarantee` never by itself authorizes
an optimizer rewrite, reorders observable operations, changes callback counts,
or establishes a cost bound. Optimizer use still requires the independent
checked justification owned by C135.

For the initial surface, function-level algebraic guarantees attach only to
`total transform` declarations. This matches the existing law domain of pure,
total operations. Traits may also name law schemas through the already proposed
member form:

```catena
trait Combiner[a: Type] {
  fn combine(left: a, right: a) -> a
  guarantee associativity = CombinerLaws.Associativity
}
```

An implementation supplies its exact methods and law-evidence status; it does
not repeat or override the inherited law schema. The compiler verifies claim
identity, subject, domain, and evidence provenance. The current
[law model](../60-specification/traits-and-categorical-operations/laws-derivation-and-testing.md)
already carries standard schemas and the three evidence statuses, but explicitly
has no general user law language. These source forms are the proposed adoption
of that missing layer, not evidence that it has already shipped.

## Types, data, and pattern matching

Declare nominal alternatives in a block. Constructor names belong to the
declaring module, are unique there, and retain their owning datatype identity:

```catena
export type DeliveryStatus {
  Queued()
  InTransit(Text)
  Delivered(Int)
  Failed(Text)
}

fn describe(status: DeliveryStatus) -> Text {
  match status {
    Queued() -> "Waiting for collection"
    InTransit(tracking) -> tracking
    Delivered(_) -> "Delivered"
    Failed(reason) -> reason
  }
}
```

Zero-payload constructors keep `()` in construction and patterns. This
distinguishes `Queued()` from a type name or bare value binding. There is no
null value hiding behind it.

`match` is exhaustive, with branch result types agreeing. Arms use a pattern,
optional `when` guard, `->`, and an expression or brace block. Guards retain
the admitted restricted pure predicate fragment. `or` alternatives bind the
same names with the same types. Wildcard `_` ignores one value; repeated names
do not mean equality. Integer/Boolean literal patterns retain their existing
restrictions; a negative integer is not silently admitted as a new literal
pattern. Use a binding and an admissible guard where needed.

Function parameters and ordinary `let` bind plain names initially. A destructuring
calculation uses `match`; comprehension-local bindings have the explicitly
different irrefutable-pattern rule. Do not introduce implicit failure while
claiming this is only a prettier binding notation.

Structural records use `record { field: Type }` in types and
`record { field = value }` in expressions. `details.weight` selects a field;
`update details { weight = 5 }` returns a new record of the checked shape.
It never mutates `details`. Existing structural row rules determine admissible
fields. Structural variants use `variant Tag(payload)` and the type form
`variant { Tag(Type), Other(Type) }`; their nominal counterparts above remain
different identities. Public row extensions require explicit owner-approved
row notation before their parser admission; the first examples use closed rows.

There are no transparent type aliases. A one-constructor datatype supplies a
nominal wrapper; `export opaque type` exposes its identity while keeping all
constructors private. A transparent `export type` exposes its whole constructor
family. The keyword does not itself validate data or manufacture trusted
evidence. These choices preserve the
[alias exclusion](../60-specification/aliases-and-newtypes/the-alias-exclusion.md)
and existing abstraction boundary.

Types use square application and right-associated arrows:
`List[Int]`, `Result[Problem, Quote]`, `(Int, Text)`, and `a -> b -> c`.
Type variables are lower-case identifiers, explicitly quantified as
`fn identity[a](value: a) -> a { value }`. A higher-kinded parameter is written
`f: Type -> Type`. Type application is left-associated and kind checked;
`Result[Problem]` leaves its final success slot open. No arbitrary type lambdas,
implicit higher-rank polymorphism, or variance inference is added.
An unannotated generic parameter has kind `Type`. Ordinary rank-1 instantiation
can infer the type arguments; the explicit form states the same instantiation:

```catena
identity(1)
identity[Int](1)
```

These are separate expressions to compare. Explicit type arguments follow a
named callable before its call chain, not arbitrary computed values or
collection-index expressions.

## Modules and imports

One flat module occupies one matching file, such as `module Shipping` in
`Shipping.cat`. The module identifier obeys the retained ASCII naming rule.
Directories can organize files without inventing nested module names.

```catena
module Checkout

import List
import Shipping { type Parcel, value price }
import Result { type Result, constructor Ok, constructor Error }

export fn total(parcel: Parcel) -> Int {
  price(parcel)
}
```

`import List` admits qualified references. Selective imports explicitly name
their namespace categories; they add unqualified spellings without removing
the module's qualified path. No wildcard, renaming, module alias, or precedence
by import order is introduced. Datatype visibility still controls constructors.
The import category vocabulary is `value`, `type`, `constructor`, `trait`,
`effect`, and `handler`, mapped to the retained namespaces; implementation
evidence enters by the existing module rules, not a local preference list.

The canonical qualified form is `Module.member`: `Shipping.Parcel` names the
type, `Shipping.InTransit(...)` a constructor if `DeliveryStatus` is declared
in `Shipping`, and
`Result.Ok(...)` a constructor exported by module `Result`. A type does not
create a second source namespace merely by being a type. Three-segment
`Module.Type.Constructor` paths are excluded. Adoption must explicitly reconcile
the earlier C002 explanatory owner-qualified spelling with
[C021's later namespace contract](../60-specification/namespaces-and-shadowing/namespace-inventory-and-spelling.md).
Constructor metadata still retains the exact owner type.
The existing compiler interface metadata can retain an older
`Module.Type.Constructor` owner-qualified field. A source resolution adapter
must connect the new spelling to those unchanged constructor/type identities;
it must not rewrite a frozen interface schema as an incidental syntax change.

Dot has two separately parsed ordinary roles: an upper-case module head gives
qualified lookup; a lower-case value head or parenthesized expression gives
record selection. `request` has its own capability-selection context. Parsing
does not guess between module names and record types from inference results.

Package identity, dependencies, compiler revision/edition, prelude selection,
preview opt-ins, and entry selection stay in the explicitly selected package
manifest. A source `import` does not fetch packages or grant authority. Keep
`main()` as the source spelling of the selected entry; a familiar name alone
does not select it. An explicit entry adapter invokes that ordinary function
with Unit and connects it to the retained zero-argument entry-body metadata.
The separately admitted environmental authority parameter is supplied only by
the launch adapter. This mapping needs adoption evidence; a source function's
Unit convention does not silently change the retained entry ABI.

## A concrete vocabulary for categorical programming

Start with these five questions. The data policies are part of the operation's
contract, not deductions from its mathematical class name.

| What the program needs | Name | Example |
| --- | --- | --- |
| Transform an available/successful payload with a pure function | `map` | `Option.map(normalize, maybe_name)` |
| Combine independently obtained wrapped values | `map2` | `Validation.map2(make_address, street, postal_code)` |
| Choose the next wrapped step from the previous result | `and_then` | `zone |> Result.and_then(find_rate)` |
| Traverse a finite structure and collect a chosen outcome | `collect_map` | `List.collect_map(validate_parcel, parcels)` |
| Reduce a structure to one summary | `summarize` | `List.summarize(add, 0, prices)` |

Use these public nominal roles, bound to C103's retained identities rather than
creating duplicate incompatible outcome types:

```catena
// In module Option
export type Option[a] { None(); Some(a) }

// In module Result
export type Result[e, a] { Error(e); Ok(a) }

// In module Validation
export type Validation[e, a] { Invalid(Nonempty[e]); Valid(a) }
```

These are three separate module fragments; `Nonempty` is the explicitly
imported admitted nonempty error sequence. Error-first type parameters leave
the successful value in the position transformed by unary `Mapper` evidence.
The order is less familiar to some readers, but avoids pretending the existing
kind system can arbitrarily rearrange type arguments.

```catena
fn find_rate(zone: Int) -> Result[Text, Int] {
  if zone == 1 { Result.Ok(7) } else { Result.Error("Unknown zone") }
}

let rate = Result.Ok(1) |> Result.and_then(find_rate)
let doubled = rate |> Result.map(fn(value) { value * 2 })
```

With `Result` imported, `doubled` is `Result.Ok(14)`. An error passes through
unchanged; `map` does not call its callback on that error. `and_then` takes a
callback producing another `Result`, and skips it on error.

For independent address checks, use:

```catena
Validation.map2(
  fn(street, postal_code) { record { street = street, postal_code = postal_code } },
  validate_street(input.street),
  validate_postal_code(input.postal_code)
)
```

Assuming both validators return `Validation[Problem, Text]`, both inputs are
checked and invalid results accumulate in the retained order. `map2` does not
mean parallel execution. `Result.map2` also evaluates both subject expressions;
its result-selection policy is fail-fast data combination, not prevention of
the second expression's execution. Use `and_then` for a genuinely dependent
step. `Validation` deliberately has no `Chainable` or `Workflow` instance.

For `List.collect_map(validate_parcel, parcels)`, declare the callback outcome:
`Result` stops at the first error, `Option` at absence, and `Validation` visits
all elements and accumulates ordered errors. The output retains the traversed
list shape when successful. Ordinary callbacks in these contracts are pure;
do not place `request` inside one and imply a new effectful callback ABI.
The [outcome contracts](../60-specification/outcome-contracts/values-sequencing-and-validation.md)
remain authoritative for details.

### The full trait vocabulary

Retain the current 17 names. Formal labels below are documentation/search
metadata, never a second set of accepted source aliases.

| Public trait | Minimal methods | Formal correspondence |
| --- | --- | --- |
| `Equatable` | `equals(left, right)` | Setoid |
| `Orderable` | `compare(left, right)` | Ord |
| `Combiner` | `combine(left, right)` | Semigroup |
| `EmptyCombiner` | `empty` | Monoid |
| `Reducible` | `summarize(callback, initial, subject)` | Foldable |
| `Mapper` | `map(callback, subject)` | Functor |
| `TwoSlotMapper` | `map_both(first_callback, second_callback, subject)` | Bifunctor |
| `MultiMapper` | `map2(callback, first_subject, second_subject)` | Apply |
| `ValueEmbedder` | `from_value(value)` | Applicative |
| `CollectingMapper` | `collect_map(callback, subject)` | Traversable |
| `Chainable` | `and_then(callback, subject)` | Chain |
| `Workflow` | parent methods, no additional primitive | Monad |
| `Composable` | `compose(first, next)` | Semigroupoid |
| `IdentityComposer` | `identity` | Category |
| `TransformRouter` | `from_transform(transform)`, `on_first(transform)` | Arrow |
| `ContextualMapper` | `map_with_context(callback, subject)` | Extend |
| `FocusReader` | `read_focus(subject)` | Comonad |

The [normative hierarchy](../60-specification/traits-and-categorical-operations/standard-hierarchy-and-vocabulary.md)
already improves several names from the first note: `EmptyCombiner` avoids
suggesting a mutable accumulator; `TwoSlotMapper` describes its two positions;
`MultiMapper` does not promise a tuple; `Workflow` avoids confusing the trait
with `|>`; `IdentityComposer` is more specific than “System”; `TransformRouter`
avoids a streaming/concurrency implication; `FocusReader` does not imply removal.
`Chainable` inherits `Mapper`, not `MultiMapper`; `Workflow` combines
`ValueEmbedder` and `Chainable`. The older diagram is not the ABI.

`compose(first, next)` runs `first` and then `next`. Laws do not authorize
reordering requests, changing callback counts, or silently selecting a different
error policy. Built-in `==` is not automatically overloaded by an `Equatable`
implementation. Alternative orders or combination policies use nominal wrappers.

### Generic signatures and implementations

```catena
export fn change[f: Type -> Type, a, b](
  transform: a -> b,
  subject: f[a]
) -> f[b] requires Mapper[f] {
  Mapper.map(transform, subject)
}
```

Here `Mapper` is the explicitly imported trait; `Mapper.map` is trait-qualified
method resolution in a call context. The spelling identifies which interface
is required; it does not alter ordinary call evaluation or introduce runtime
dictionary selection. Adoption must register this qualification context beside
module lookup, with collisions rejected rather than type-directed guessing.

Trait authors use a declarative shape, for example:

```catena
export trait Describe[a: Type] {
  fn describe(value: a) -> Text
}

implementation Describe[Int] {
  fn describe(value: Int) -> Text { "an integer" }
}
```

The example supplies a valid simple behavior, not an integer rendering library.
An implementation supplies exactly its trait's minimal methods, with parent
methods obtained from coherent parent evidence. No overrides of inherited
methods, orphan exceptions, local priority, or import-order tie breakers are added.

Zero-argument trait methods need a distinct declaration form to preserve the
ABI of `empty` and `identity`. Write `value empty: a` inside a trait and
`value empty: Count = Count(0)` in its implementation, assuming the appropriate
Count datatype and parent evidence. These are implementation-supplied method
slots whose read dispatches with zero data arguments; they are **not** a new
associated-constant facility. Their expressions are pure under the existing
method contract. A source use such as `EmptyCombiner.empty[Count]` selects that
method evidence without adding `()`. Converting it to `fn empty()` would
instead produce a Unit-taking function and change the ABI. `value` is
contextual inside trait/implementation members and import/subject tags.

The extended trait declaration vocabulary is `requires Parent[...]`,
`associated type Item: Type`, and `determines input -> output` for the retained
associated types and functional dependencies. An implementation writes
`associated type Item = T`. There are no associated constants. `derives Mapper`
on a datatype requests only the already admitted checked derivation; it is not
an automatic promise for every field shape.

`guarantee name = Specification.claim` links a trait law schema to its checked
claim identity. The linked rule declares quantified parameters and the exact
Boolean law; the phrase alone proves nothing. Derived provenance, proof status,
assumptions, and optimizer trust follow existing evidence rules. An instance
cannot upgrade a finite test or an author assertion to compiler-trusted proof.

## Effects without continuation vocabulary in ordinary code

An effect names a family of requests. A capability selects which interpretation
may answer those requests. A result such as `Result.Error(...)` is ordinary
data. A process termination is a distinct runtime event. These three roles
stay separate in syntax and documentation.

```catena
effect Clock {
  now() -> Int
}

fn stamp(offset: Int) -> Int uses {clock: Clock} {
  offset + request clock.now()
}

handler FixedClock[a](tick: Int) for Clock handles a -> a {
  now() { reply tick }
  return(value) { value }
}

let observed = handle Clock with FixedClock(100) as fixed {
  stamp(7) using {clock = fixed}
}
```

The expression produces `107`. This is a deterministic local interpretation,
not access to the machine clock. Handler arguments are evaluated in the outer
environment first, then a fresh capability identity is installed, then the
handled body runs. `handles a -> a` declares the handled input and output
types; another handler may change that result type. Named handler parameters
are explicit data parameters, not first-class dynamically captured handlers.

In `uses {clock: Clock}`, `clock` is a capability parameter name, not an ordinary
value parameter. `using {clock = fixed}` supplies identity evidence at the
call. This evidence application attaches to the complete written call chain;
it checks/substitutes required slots before evaluating that chain and does not
run an expression. Duplicate, unknown, or missing ambiguous entries reject.
A prefix application may retain abstract requirements for its later stage;
explicitly supplied local identities remain subject to escape checking.
The final stage of a multi-parameter named function carries its declared body
effects; forming earlier pure stages does not itself issue requests.

An unnamed `uses {Clock}` entry and `request now()` are allowed only when
retained unique resolution succeeds. The optional `request Clock.now()` form
selects an imported effect family in request context and still requires exactly
one compatible capability. With two clocks, write `request first.now()` and
`request second.now()` or pass named evidence explicitly. The nearest handler
does not win. Importing the family or writing `uses` does not grant host authority.

### Effect annotation defaults

Write `uses` when it states a requirement or deliberately asserts purity:

| Declaration | Omitted `uses` | Explicit `uses {}` |
| --- | --- | --- |
| Exported function | Closed empty effect row; reject any residual effect requirement | The same public purity contract, stated explicitly |
| Private named function | Infer effects within the retained rules, even if other types are annotated | Check against a closed empty row instead of inferring a nonempty one |
| `transform` or `total transform` | Always closed and pure; writing `uses` is rejected as redundant or contradictory | Not accepted; the declaration word already asserts the empty row |
| Trait method signature or handler declaration | Closed empty contract; there is no public inference from an implementation | The same empty contract, stated explicitly |
| Anonymous or verification function in this initial surface | Pure under its existing restrictions | Optional explicit purity; those restrictions still apply |

An implementation must satisfy its trait method's declared contract. A private
implementation body cannot widen a method's default-pure interface by inference.
For handlers, the default concerns their outer clause effects, not the effect
family interpreted by `for Clock`. The initial handler target remains pure.

Adding an unhandled request to an exported function without `uses` is therefore
an error until its signature declares the requirement. Local handling may still
leave an empty residual row where the retained rules permit it. No formatter
should insert empty annotations routinely or remove a deliberately written
one: on a private function, that would change an assertion into inference.

For example, a library can deliberately pin a private helper's purity:

```catena
fn normalize(value: Int) -> Int uses {} {
  value + 1
}
```

Its empty annotation is intentional and optional; the earlier ordinary examples
omit it. Public effectful functions still write nonempty requirements, such as
`uses {clock: Clock}` on an exported version of `stamp`.

This source-default rule is a proposed amendment to the
[retained public annotation requirement](../60-specification/effects-and-handlers/declarations-requests-and-signatures.md#function-signatures).
During adoption, omission at a public boundary elaborates to an explicit empty
row in the checked interface. Existing retained inputs keep their versioned
meaning; changing the proposal does not change their decoder or compiler.

The initial surface admits closed rows with named/unnamed entries. Open effect
tails and effectful anonymous functions are **not silently added**; they need a separate
syntax/integration slice against the richer row owners. An ordinary callback
cannot capture an effect request just because its enclosing function has `uses`.

### Reply and explicit control

`reply expression` is accepted only as the terminal form of a simple operation
clause with no explicit continuation binder. Its exact hygienic expansion is:

```text
let generated_reply = expression
resume generated_continuation with generated_reply
```

The expression is evaluated once, in the clause's outer environment; the fresh
binder cannot collide with a source name. If that expression returns normally,
the continuation is consumed exactly once. If it traps or diverges, execution
never reaches the resume; the normal trap/lifetime rules still apply.
The resumed remainder reinstalls the same handler. `reply` does not return
directly from the whole handler, issue the request again, or retry earlier work.
The mandatory `return(value)` clause handles the normal final result.

An advanced clause exposes its dedicated control binder:

```catena
handler StopClock() for Clock handles Int -> Int {
  now() resume continuation { 0 }
  return(value) { value }
}

let stopped = handle Clock with StopClock() as clock {
  1 + request clock.now()
}
```

`stopped` is `0`, not `1`: the clause does not resume, so the captured remainder,
including addition, is abandoned. To continue it, the clause could instead
end with `resume continuation with 10`, producing `11`. A resumption may be
used at most once; it cannot be stored, returned, passed as data, sent, or
captured by a closure. There is no shallow or multi-shot mode.

The retained [deep-handler rules](../60-specification/effects-and-handlers/deep-handlers-and-affine-resumptions.md)
permit broader outer effects than the integrated closed target. The first
examples and initial source admission use effect-free handler clauses and
ordinary immutable data parameters. Parameterized-handler lowering still needs
integration evidence; its richer retained contract is not proof of support in
the narrower [closed capability target](../60-specification/closed-capability-kernel/identity-rows-and-comprehension-target.md).
Resource cleanup on abandonment remains mandatory under its separate owner.

For effectful dependent work, ordinary `let` and `match` are enough:

```catena
fn quote(key: Int) -> Result[Text, Int] uses {rates: Rates} {
  let found = request rates.find_zone(key)
  match found {
    Result.Error(problem) -> Result.Error(problem)
    Result.Ok(zone) -> request rates.find_rate(zone)
  }
}
```

Here a declared `Rates` effect has operations `find_zone(Int)` and
`find_rate(Int)`, each replying with `Result[Text, Int]`. The second request
happens only on success. This does not put an effectful callback inside the
pure `Result.and_then` contract. Trusted environmental adapters that return
closed structural outcomes require an explicit checked conversion before using
these nominal outcome names.

## One outcome sequencing convenience

Use a constrained `chain` block for pure `Workflow` operations:

```catena
chain Result {
  bind zone = find_zone(destination)
  bind rate = find_rate(zone)
  yield make_quote(rate)
}
```

For this snippet, both lookup functions are **pure data lookups returning
`Result[Problem, Int]`**, distinct from the request-based function above.
`bind` says that the payload becomes available only if that step succeeds.
`yield` embeds the final ordinary value. The exact expansion is:

```catena
Result.and_then(fn(zone) {
  Result.and_then(fn(rate) {
    Result.from_value(make_quote(rate))
  }, find_rate(zone))
}, find_zone(destination))
```

A `let` inside the chain is an ordinary pure binding at that position. Each
`bind` introduces a fresh plain name and evaluates its expression once on the
path that reaches it. `yield` occurs exactly once and last. Every `bind`, `let`,
and `yield` expression must have an empty evaluated effect row, including the
first `bind` expression that appears outside generated lambdas in the expansion.
Generated lambdas must also have empty effect rows. The qualifier supplies one
coherent `Workflow` family, such as `Option` or the unary view of
`Result[Problem]`; error parameters
must be determined by surrounding types, not defaulted. `Validation` rejects.
No implicit selection among outcomes, tasks, external effects, and resources
is allowed. This deliberately small sugar makes category-based dependency
useful without requiring the word “monad” at the call site.

## Comprehensions, ownership, and concurrency

The lists-only comprehension uses the already settled words:

```catena
for {
  weight in weights
  when weight > 0
  let doubled = weight * 2
  yield doubled
}

for {
  case Option.Some(weight) in maybe_weights
  yield weight
}
```

An ordinary generator must match every element; only `case` permits a pattern
mismatch to skip. `when` explicitly filters. Generator qualifiers run in the
retained order and the complete list is produced eagerly. Comprehension-local
patterns must be irrefutable where specified. Effects belong to the full
comprehension row and whole-computation handler scope; its implementation must
use the retained lowering, not the pure callback ABI of `List.map`. Lazy
streams, arbitrary target containers, and neighboring iteration remain deferred.

Use a dedicated ownership form:

```catena
scope item acquire 7 release fn(value) { () } within 1000000 {
  read item + 1
}
```

This intentionally modest example has body result `8`, returned if cleanup
succeeds. Even its no-op release can lose a scheduling race against the 1 ms
allowance, producing the retained mandatory-release-failure trap. It demonstrates
an immutable payload, not a file descriptor. `within` is an exact nonnegative
integer nanosecond release allowance, written as an integer literal in this
initial surface. It is retained metadata, not an arbitrary effectful expression.
The release function is formed **before** acquisition, despite
appearing after it in this readable declaration; only successful acquisition
registers release. Nested scopes unwind in reverse acquisition order before
the enclosing suffix continues. `read item` copies the admitted payload; the
handle cannot escape, be sent, or be captured even by an apparently local
closure. Release failures are observable terminal outcomes, not silently ignored.
Forced process/VM loss has no new cleanup guarantee.

The [owned-scope contract](../60-specification/resource-scopes/owned-lifetime-and-mandatory-cleanup.md)
currently admits pure release callbacks over closed sendable immutable data.
This syntax does not authorize arbitrary foreign resources or filesystem
callbacks. Handler clauses cannot acquire such scopes. Broader native-service
resource management remains with its existing trusted adapters.

Keep concurrency in typed library operations named for their actual behavior:
`spawn`, `send`, `receive`, `link`, `monitor`, `cancel`, `supervise`, and
`restart` where the owning interface admits the operation. These are proposed
public labels to map to existing interfaces, not a claim of newly admitted
signatures. Process/task owners, protocol types, supervisor policies, deadlines,
and launch capabilities must remain explicit typed arguments or requirements.
Their source adapters are a tracked adoption item; no invented `async` block
turns all effects into tasks. Distribution, upgrades, foreign adapters, and
environmental services use the same declaration/call grammar and their exact
existing contracts, not new unchecked keyword shortcuts.

## Specifications and governed work

P109 includes verification/governance, not just expressions. Give typed claims
a source form while retaining the separate signed governance artifact:

```catena
verification fn nonnegative(value: Int) -> Bool {
  value >= 0
}

specification Pricing {
  rule Nonnegative on value price = nonnegative
  example Zero for Nonnegative(0) = true
}
```

This is an authoring example: `price` must be a valid exported value subject
and the rule and nested example must elaborate to the retained claim graph.
The example invokes a finite integer checker; it does **not** prove that
`price` always produces a nonnegative result. Each specification and claim has
a stable name. The elaborator resolves the typed subject, checker, dependencies,
and exact example arguments to the retained specification graph. `verification`
definitions are unreachable from runtime definitions and erased from artifacts.
Their checker fragment excludes `request`, `handle`, and `resume`, even when
handling would leave an empty effect row. Exact examples accept the retained
integers, Booleans, and recursively nested tuples, not arbitrary source values.
Compiler conformance is derived evidence; any source conformance-requirement
declaration needs a catalog-bound elaboration, rather than an invented checker
name. Such extended claim authoring remains an explicit adoption obligation.

Subject tags are `value`, `datatype`, `trait`, `instance`, `effect`, `handler`,
`module`, `package`, `interface`, `action`, and `profile`, mapped one-to-one to
the [retained subject kinds](../60-specification/specifications-and-governance/claims-examples-and-checking.md).
An `attestation Name on subject = "statement"` declares an evidence requirement,
not a signature. An `assumption Name for Claim = "reason"` records an explicit
unverified premise; it counts only when matching policy authorizes it.
`guarantee` links to these stable rule identities, with the trust distinctions
described above.

For the first version, package governance remains the **existing canonical
bundle format**, selected by the build. This is a deliberate concrete format
choice, avoiding a second authoring language whose signature semantics would
also need design. Its closed policy vocabulary is `all`, `any`, `threshold`,
`role`, `evidence`, `action`, `state`, `profile`, `sequence`, and `deny`.
Protected actions are `build`, `publish`, and `activate`. Broader and narrower
governed scopes add requirements; a local declaration cannot override them.

Principals, role memberships, policy, evidence envelopes, approvals, and
transitions belong in that artifact. Private signing keys remain external.
Approvals are authorization records, not technical evidence. The lifecycle
remains Draft → Proposed; Proposed → Accepted/Rejected/Withdrawn;
Accepted → Active/Withdrawn; Active → Deprecated; Deprecated → Superseded.
Each signed transition retains exact payload identity and replay rules.
Formatting Catena source never rewrites signed bytes or creates authority.
See the [placement and policy contract](../60-specification/specifications-and-governance/scopes-policy-and-authorization.md)
and [evidence lifecycle](../60-specification/specifications-and-governance/evidence-identity-and-lifecycle.md).

## Grammar summary

This is a compact **design grammar**, not a conflict-tested parser artifact.
`sep` is one or more hard newline/semicolon separators. `items(X)` is a
comma-separated sequence with optional trailing comma and grammar-local hard
newlines around entries; it is not a global newline rule. `members(X)` is a
possibly empty separator-delimited sequence with optional leading/trailing
separators. `gap` admits boundary hard newlines/semicolons, including immediately
after `{`. `name`, `TypeName`, literal scanning, qualified
identifiers, and pattern subproductions reuse their owning lexical contracts.
Square brackets in EBNF mean optional syntax; quoted brackets are literal.

```ebnf
source       = gap, [ module ], gap, EOF ;
module       = "module", ModuleName, [ sep, members(module-item) ] ;
module-item  = import | declaration ;
import       = "import", ModuleName, [ "{", items(import-item), "}" ] ;
import-item  = category, name ;
declaration  = [ "export" ], ( callable | datatype | trait | effect | handler )
             | implementation | specification | verification-function
             | "rec", "{", members(callable), "}" ;
callable     = function | transform ;
function     = "fn", name, [ generics ], parameters, [ signature ], block ;
transform    = [ "total" ], "transform", name, [ generics ], parameters,
               "->", type, [ requirements ], { guarantee-clause }, block ;
guarantee-clause = "guarantee", claim-reference,
                   { ",", claim-reference } ;
generics     = "[", items(type-parameter), "]" ;
parameters   = "(", [ items(parameter) ], ")" ;
parameter    = name, [ ":", type ] ;
signature    = "->", type, [ requirements ], [ effects ] ;
requirements = "requires", constraint, { ",", constraint } ;
constraint   = trait-name, "[", items(type), "]" ;
effects      = "uses", "{", [ items(effect-entry) ], "}" ;
effect-entry = [ name, ":" ], effect-type ;
datatype     = [ "opaque" ], "type", TypeName, [ generics ],
               [ "derives", trait-name, { ",", trait-name } ],
               "{", members(constructor), "}" ;
constructor  = ConstructorName, "(", [ items(type) ], ")" ;
type         = type-atom, [ "->", type ] ;
type-atom    = type-name, [ "[", items(type), "]" ]
             | "(", type, ")" | "(", type, ",", items(type), ")" | "()"
             | "record", "{", items(type-field), "}"
             | "variant", "{", items(variant-field), "}" ;
block        = "{", gap, { local-form, sep }, expression, gap, "}" ;
local-form   = "let", name, [ ":", type ], "=", expression ;
expression   = resumption | pipe-expression ;
pipe-expression = or-expression, { "|>", or-expression } ;
or-expression = and-expression, { "||", and-expression } ;
and-expression = relation, { "&&", relation } ;
relation     = sum, [ relation-operator, sum ] ;
relation-operator = "<" | "<=" | ">" | ">=" | "==" | "!=" ;
sum          = product, { ( "+" | "-" ), product } ;
product      = prefix, { "*", prefix } ;
prefix       = ( "-" | "!" ), prefix | postfix ;
postfix      = callee, { call | field-selection }, [ evidence ] ;
callee       = named-atom, [ type-arguments ] | primary ;
primary      = literal | grouping | tuple | list | record | record-update
             | structural-variant | "read", name | block | lambda
             | conditional | match | request | handle | chain | comprehension | scope ;
type-arguments = "[", items(type), "]" ;
call         = "(", [ items(expression) ], ")" ;
evidence     = "using", "{", items(capability-binding), "}" ;
lambda       = "fn", parameters, [ signature ], block ;
conditional  = "if", expression, block, "else", block ;
match        = "match", expression, "{", members(arm), "}" ;
arm          = pattern, [ "when", guard ], "->", expression ;
request      = "request", operation-selector, call ;
handle       = "handle", effect-type, "with", handler-name, call,
               "as", name, block ;
handler      = "handler", HandlerName, [ generics ], parameters,
               "for", effect-type, "handles", type-atom, "->", type,
               [ effects ], "{", members(handler-clause), "}" ;
handler-clause = "return", "(", name, ")", block
              | operation-name, parameters, "{", gap, { local-form, sep },
                "reply", expression, gap, "}"
              | operation-name, parameters, "resume", name, block ;
resumption   = "resume", name, "with", expression ;
chain        = "chain", workflow-selector, "{", gap, { chain-step, sep },
               "yield", expression, gap, "}" ;
chain-step   = ( "bind" | "let" ), name, "=", expression ;
comprehension = "for", "{", gap, generator, sep,
                { qualifier, sep }, "yield", expression, gap, "}" ;
generator    = [ "case" ], pattern, "in", expression ;
qualifier    = generator | "when", expression | "let", pattern, "=", expression ;
scope        = "scope", name, "acquire", expression, "release", expression,
               "within", nonnegative-integer-literal, block ;
```

Imports precede other module items; no separator is required after the last
declaration before EOF. An empty/comment-only file remains a valid no-module
unit. Boundary gaps are normalization conveniences in this design summary;
an executable grammar should consume a boundary separator in one place rather
than introduce ambiguous empty paths. `relation` groups the non-chainable
comparison/equality levels into one rejecting production; parentheses admit
intentional combinations. `resume k with expression` consumes the full following
expression at the lowest level and is valid only in its dedicated clause context.
Declaration keywords are never operators. The parser must distinguish an
if/match/handle header expression from its following block by this production,
not by guessing at an optional trailing callback. Functions have no trailing
block call shorthand.

This summary intentionally delegates the full pattern grammar and the retained
trait/specification graph field schemas to their owners. The chosen trait,
effect, implementation, and claim declaration spellings above need expanded
machine grammar productions during adoption. A schema name in this summary is
not evidence that a complete parser or lossless source AST already exists.
Exported functions require type signatures and applicable constraints, but
their optional `effects` clause defaults to a closed empty row. Private named
functions may infer an omitted effect row even with explicit parameter/result
types; explicit `uses {}` constrains that inference. Method declarations require
signatures and no bodies; method/handler effect clauses default to empty.
Verification functions require a pure Bool result. These are checked context
conditions, not inference-based parsing.

Every transform has an explicit result signature and a forced empty row;
`effects` is not part of its production. `total` is valid only immediately
before `transform`. Function-level `guarantee` clauses are valid only on a
total transform, despite their shared syntactic production, and each reference
must resolve through the specification graph. Trait guarantee members use their
separate declaration grammar. These are context checks with dedicated diagnostics.

## Diagnostics and canonical formatting

The formatter preserves the tree, selected capability identities, comments,
and relevant source attribution. Its chosen output uses two-space blocks,
one space around binary operators, comma-space short lists, and one item per
line when a list is broken. Multiline calls have a trailing comma; multiline
record fields do too. Pipelines put `|>` at the start of continuation lines.
Formatting must be idempotent and preserve parse/elaboration results.

Incomplete-input diagnostics identify an action, the relevant source, and a
repair. Suggested messages are examples of the desired contract, not newly
assigned stable diagnostic codes:

| Input/problem | Useful first explanation |
| --- | --- |
| `add(1` at end of input | “This call is missing its closing `)`. The call began here.” Interactive input remains incomplete until submission. |
| `let result =` | “Give `result` a value after `=`.” |
| `if ready { 1 }` | “An `if` expression needs an `else` result.” |
| `add(1)` used where `Int` is required | “This expression still needs an `Int` argument; its current value is a function.” |
| `a < b < c` | “Write the two comparisons explicitly: `a < b && b < c`.” |
| Two compatible clocks and `request now()` | “Two Clock capabilities can answer `now`. Select one, for example `request first.now()`.” |
| Unhandled effect in an exported function without `uses` | “This exported function declares a pure contract by omitting `uses`. Declare the required effect or handle it within the function.” |
| Request or nonempty residual row in a `transform` | “A transform must be pure. Use `fn ... uses {...}` for this computation or handle the request completely.” |
| Unproved `total transform` | “Totality could not be established: this recursive call is not visibly smaller.” Show the call and the expected structural argument. |
| `guarantee` on an ordinary `fn` or non-total transform | “Function-level algebraic guarantees require a total transform in this language version.” |
| Unknown or mismatched guarantee claim | “This claim does not describe this transform.” Show the resolved claim subject and expected signature. |
| Request in a pure mapping callback | “This callback must be pure. Move the request into the surrounding function and choose the next step with `match`.” |
| `chain Validation { ... }` | “Validation accumulates independent failures and has no Workflow implementation. Use `map2` or `collect_map`.” |
| A second `resume` | “This continuation can be resumed at most once. Its first use is here.” |
| Returning a scope handle | “This handle belongs to a scope that ends here. Return an allowed copied payload instead.” |

Technical details, inferred types, rows, and evidence identities remain available
in a secondary diagnostic view. Recovery must not invent a successful program
by silently changing tuple grouping, dropping a branch, or selecting a capability.

## Adoption work and evidence

This design is acceptable as the first implementation target because its common
forms have explicit meanings and its differences from retained contracts are
visible. It is not yet a complete P109 conformance artifact. Work should proceed
in this order, without participant recruitment or a human-study gate:

1. **Publish source adoption and changed-policy records.** Select the exact
   language revision through existing lifecycle rules. Register punctuation,
   keywords, token joining, optional empty annotations and public-pure defaults,
   transform elaboration, totality evidence, guarantee references,
   call/field forms, module/trait/request qualification
   contexts, constructor spelling reconciliation, and the chosen outcome names.
   Record the new development evidence policy and the successor release profile.
2. **Admit opt-in totality through its completed gate.** Apply the normative
   [C034 amendment](../60-specification/opt-in-totality-validity/explicit-total-declaration-gate.md)
   in the source-adoption slice. That slice must make `total transform` alone
   create the validity gate while ordinary recursion remains unrestricted, and
   must supply the conservative termination/trap analysis, structural decrease,
   evidence preservation through currying, interface identity, limits,
   independent verification, diagnostics, and incompatibility rules.
3. **Close the full grammar and source AST.** Expand this grammar against all
   retained input schemas, including traits, associated types, declarations,
   specifications, external governance selection, and restricted pattern forms.
   Decide exact source coverage for retained open rows before claiming full
   P109 completion; initial closed rows are an explicit boundary, not an omission
   to paper over. Preserve source spans and provenance through every elaboration.
4. **Implement lexing, parsing, and canonical formatting together.** Build
   positive and negative fixture pairs. Explain every parser conflict with a
   reproducible input or eliminate it. Include incomplete calls, nested matches,
   operator continuations, multiline records, and comments at boundaries.
5. **Lower and independently verify.** Check unary application order, partial
   application, constructor payload arity, pipe operand formation, data-last
   wrappers, coherent traits, public effects, omitted-public purity rejection,
   private inference versus explicit empty assertions, transform purity,
   totality rejection and evidence, guarantee identity/status, identity evidence, reply expansion,
   chain expansion, ownership, and erasure. Parameterized handlers, native
   service adapters, process interfaces, and richer rows need explicit integrated
   evidence; separate retained passes do not prove their joint implementation.
6. **Run the example corpus through the compiler and tools.** Assert values,
   ordered traces, skipped work, accumulated errors, abandonment, cleanup,
   rejection categories, source spans, and formatter round trips. Compare
   reference and BEAM results. These are semantic/tooling tests, not measurements
   of how people understand the language.
7. **Update partial completion with evidence.** P107/P109 close only when their
   actual adoption obligations pass. Integrate source diagnostics, documentation,
   REPL, editor services, and migrations before closing their source halves.
   Then admit real Catena compiler source under G141 and the
   [self-hosted evolution plan](self-hosted-compiler-evolution-plan.md).

The initial engineering corpus should include the complete Shipping example;
ordinary functions beside pure transforms; accepted and rejected totality
claims, including structural recursion and a guarded partial primitive; matching
and mismatched guarantee references at every evidence tier; Option and Result
mapping; independent validation; fail-fast and accumulating traversals; partial
functions and tuple arguments; two simultaneous capabilities; handler argument
evaluation before installation; reply versus abandonment; resource release on
every local exit; filtering comprehensions; opaque exports; coherence failures;
specification erasure; and governance authority rejection.
For every attractive example, include a nearby wrong interpretation with a
different trace or diagnostic. This checks whether the implementation preserves
the design's distinctions without pretending to measure human comprehension.

## Connections and evidence trail

- [An Approachable Vocabulary for Catena](approachable-language-vocabulary.md)
  supplies behavior-first names, the concrete-to-generic teaching order, and
  the distinction among outcomes, service requests, and process failure.
- [Grammar and Vocabulary for Approachable Catena](grammar-and-vocabulary-for-approachable-catena.md)
  supplies GV-01–12, the Elixir and historical Catena comparisons, primary-source
  research, and the limits of evidence about readability. This note makes the
  actual selection; it does not attribute its invented spellings to those sources.
- [Standard Hierarchy and Vocabulary](../60-specification/traits-and-categorical-operations/standard-hierarchy-and-vocabulary.md)
  fixes the method ABI and formal correspondences retained here.
- [The completion checklist](../00-inbox/language-specification-completeness-checklist.md)
  tracks what is implemented; this proposal does not turn partial boxes into
  completed features.
- [The approachability map](../10-maps/approachable-catena-language-design.md)
  connects the earlier research, this source design, and the remaining inquiries.
- [The decision register](design-decision-register.md#first-version-source-design-2026-09-15)
  records accepted research choices, the user override, and concrete selections.
