---
title: "Grammar and Vocabulary for Approachable Catena"
kind: note
created: "2026-09-12"
maturity: developing
tags:
  - catena
  - language-design
  - syntax
  - usability
  - algebraic-effects
  - api-design
aliases:
  - "Catena grammar and vocabulary research"
---

# Grammar and Vocabulary for Approachable Catena

## Design recommendation

Catena should make the programmer's immediate task legible: transform this
value, combine these independent results, continue using this earlier result,
request this service, and supply this interpretation. Category theory should
make these operations coherent and dependable without becoming the entry
vocabulary. Effects should expose dependencies and control boundaries without
requiring every application programmer to reason about continuations.

The recommended direction is a compact expression language with consistent
function application, a small fixed operator set, visible effect requests,
and progressive access to formal detail. A canonical formatter, useful
diagnostics, and a task-oriented standard-library reference belong to that
design from the beginning. These are analytical recommendations for Catena,
not findings that an experiment has already validated.

The evidence does not identify one universally beautiful grammar. It does
support treating initial recognition, successful use, transfer, and error
repair as different questions. Familiar-looking words can encourage an
incorrect model; mathematical precision can coexist with ordinary operation
names; brevity can reduce typing while increasing interpretation work.
A successful surface must be tested as an interacting system.

This study informs the held P107 vocabulary and P109 grammar capstone.
It does not adopt new keywords, replace existing normative spellings, or
complete the usability gate. Recommendations below concern candidate design
and evaluation. The [completion plan](language-completion-plan-delivery.md#item-109-surface-grammar-capstone)
continues to govern adoption.

## Scope and evidence

The primary audience is a programmer comfortable with ordinary application
development who has not studied category theory. Functional programmers are
a necessary comparison group, especially where an apparently familiar form
carries a different meaning in Catena. Absolute beginners and mathematical
experts can reveal additional problems, but neither alone represents this
audience.

“Grammar” includes how source is grouped, how expressions compose, where
blocks end, and what incomplete input means to tools. “Vocabulary” includes
keywords, library operations, trait names, diagnostic phrases, and the terms
used to explain behavior. “Beautiful to write” is a design objective with
several potentially conflicting components:

| Component | Observable question |
| --- | --- |
| Predictable reading | Can a reader identify arguments, scope, dependencies, and execution order before running the code? |
| Writing and editing | Can an ordinary change be made locally without reworking unrelated nesting or punctuation? |
| Visual rhythm | Does formatting reveal the program's structure across short and long examples? |
| Discoverability | Can someone find the operation they need from a task description? |
| Conceptual economy | Does one reusable rule explain several forms without important exceptions? |
| Repair | Does a mistake lead to a useful explanation and a correct next attempt? |
| Experienced fluency | Does the notation remain pleasant after its novelty and unfamiliarity have worn off? |

These dimensions are a proposed Catena assessment framework. They are not
a validated composite score, and they should not be collapsed into a single
“beauty percentage.”

The study combines primary empirical research, formal language papers,
official language documentation, firsthand design articles, and an inspection
of Catena's retained specification and historical compiler. It is a focused
research synthesis, not an exhaustive systematic review or a new participant
study. The [research journal](../50-journal/2026-09-12-grammar-and-vocabulary-research.md)
records the historical revision, methods, and reproducible parser observation.

| Evidence class | Examples | What it can establish |
| --- | --- | --- |
| Observed participant behavior | Syntax-writing tasks, misconception tasks, comment-comprehension tasks | Results for the actual population, materials, and outcomes measured |
| Ratings and elicitation | Intuitiveness surveys, non-programmer descriptions | Expectations, associations, and expressed representations |
| Design frameworks and essays | Cognitive dimensions, linguistic analysis | Useful questions and plausible explanations |
| Formal language work | Frank, PEGs | Precisely defined mechanisms and their technical properties |
| Official documentation and design reports | Elixir, Koka, Effekt, Gleam, Swift, Elm | Actual language rules and designers' stated choices |
| Local historical evidence | Catena guides, lexer, grammar generation | What the inspected artifacts contain and what the recorded command produced |

No class in the table substitutes for all the others. In particular, a formal
account does not measure learnability, a preference does not demonstrate
correctness, and a prototype's existence does not prove that all its documented
features execute correctly.

## Findings from human-centered language research

Stefik and Siebert's four-study investigation distinguishes syntax ratings
from novice programming performance. Its results give a reason to take
surface design seriously, but its short tasks do not rank languages for
professional development or settle effect-system notation.[^1]

Lappi and colleagues replicated a syntax-intuitiveness rating study with
Finnish-speaking participants. Several earlier patterns recurred, with
important limits from English proficiency and the rating task itself.
This replication concerns expectations about syntax; it is not a replication
of the Randomo programming-performance comparison.[^2]

Pane and colleagues studied how people without programming training expressed
solutions. Aggregate and set-oriented descriptions are relevant to the way
Catena might introduce collection operations. Such descriptions also leave
details implicit, so natural-language resemblance alone cannot supply an
executable language's precision.[^3]

Gordon's linguistic analysis offers a complementary explanation: words and
forms carry expectations shaped by earlier languages and context. This is
a conceptual account rather than a controlled comparison of candidate
grammars.[^4] For Catena, a plain term deserves the same scrutiny as an
unfamiliar symbol. A word that suggests concurrency, persistence, or
automatic recovery creates a behavioral promise whether the designer
intended one or not.

Lu and Krishnamurthi model misconceptions as alternative executable
interpretations and examine corrective instruction. Their formative study
found mixed changes across misconceptions.[^5] The useful design inference
is to write down likely wrong interpretations of Catena examples, then
construct examples on which those interpretations produce different answers.
Testing only examples where all interpretations agree conceals the problem.

A 2026 comment-comprehension study also found that helpfulness was not
uniform across snippets. Its small student sample and adapted Java materials
limit generalization.[^6] Catena should consequently test the density and
placement of explanatory text. More words around a difficult construct are
not automatically a clearer interface.

Cognitive dimensions supply a vocabulary for reviewing hidden dependencies,
consistency, abstraction barriers, and the cost of change.[^7] API-usability
work broadens the question from naming to discovery and use.[^8] Swift's
official guidelines offer a concrete precedent for evaluating a declaration
at its call sites.[^9] These sources motivate an integrated review of
Catena examples, library lookup, and edits; they do not establish which
Catena keyword will win.

The evidence favors an iterative strategy: formulate a prediction, create
discriminating tasks, observe mistakes, and revise the notation or teaching
model. It does not justify treating English words as inherently intuitive,
symbols as inherently harmful, or a familiar language as the default winner.

## Elixir as a design reference

Elixir is useful as a reference for a coherent programming experience on the
BEAM. Its syntax documentation establishes concrete forms, while the
formatter's introduction records explicit readability and consistency
goals.[^10][^11] Neither source measures how much of Elixir's appeal is caused
by syntax as opposed to its libraries, tools, community, or execution model.

The appropriate comparison is therefore at the level of design choices and
programmer tasks. Catena can learn from a readable flow of operations, useful
pattern clauses, and deliberate formatting while retaining its own typing,
application, effects, and governance contracts.

| Design question | Catena interpretation |
| --- | --- |
| Can a calculation read in the order its data flows? | Prefer transformations whose argument roles and intermediate values remain clear through a pipeline. |
| Can long functions retain visible structure? | Compare block delimiters and formatter layouts on nested handlers, matches, and resource scopes. |
| Does convenient call syntax remain predictable when nested? | Test ordinary calls, callbacks, partially applied functions, and pipeline stages together. |
| Can pattern cases communicate domain behavior? | Present domain alternatives directly, with the retained coverage and binding rules. |
| Does one attractive idiom explain too much? | Avoid using one block shape for unrelated scoping, failure, authority, and continuation behavior without discriminating cues. |
| Is readability maintained by tools? | Design parser recovery, comments, formatting, and diagnostic locations alongside each candidate. |

### The pipe has an important semantic boundary

Elixir's pipe inserts its left operand into the first argument position of a
call on the right; the official documentation also describes precedence and
anonymous-call pitfalls.[^12] Catena's current contract instead applies the
right-hand function to the left-hand value.

Under Catena's [pipe rule](../60-specification/operators-and-punctuation/precedence-and-associativity.md#the-pipe),
`x |> f` means application of `f` to `x`. Its
[standard argument convention](../60-specification/traits-and-categorical-operations/standard-hierarchy-and-vocabulary.md#argument-convention)
places callbacks before data and the main subject last. Preparing a mapping
function with its callback therefore fits the semantic direction of the pipe.
Borrowing first-argument insertion would change that relationship.

This affects more than an isolated operator. A candidate must explain whether
the right side is a function value or a call template, how a pipeline stage is
partially applied, and what a multiline stage evaluates first. The visual
similarity of two pipes is not evidence that their grammar or elaboration is
interchangeable.

The C++ pipeline design-space paper is useful because it compares several
possible mechanisms rather than treating one glyph as one inevitable
meaning.[^13] For Catena, the retained meaning is the constraint: use the
comparison to expose assumptions, not to reopen application semantics
implicitly.

## Lessons from pre-rewrite Catena

The inspected compiler history is revision
[`20159d7cb2ae7e1dbb9e09bbd41b10a0ea57d793`](https://github.com/pcharbon70/catena/tree/20159d7cb2ae7e1dbb9e09bbd41b10a0ea57d793),
dated 31 July 2026. The local `main` and `archive/poc-v1` references pointed
to the same commit when inspected. This is a historical input to design;
the active compiler integration branch remains `rewrite`.

The strongest teaching feature is the continuing Parcel Relay example.
The [values guide](https://github.com/pcharbon70/catena/blob/20159d7cb2ae7e1dbb9e09bbd41b10a0ea57d793/guides/language/02_values_and_transforms.md)
begins with domain calculations rather than a taxonomy of abstractions.
The [composition guide](https://github.com/pcharbon70/catena/blob/20159d7cb2ae7e1dbb9e09bbd41b10a0ea57d793/guides/language/04_composition_and_context.md)
and [effects guide](https://github.com/pcharbon70/catena/blob/20159d7cb2ae7e1dbb9e09bbd41b10a0ea57d793/guides/language/06_effects_and_handlers.md)
extend the same domain. Reusing that instructional structure is promising
even if every surface spelling is reconsidered.

| Historical feature | Useful idea | Reason to reconsider it |
| --- | --- | --- |
| `transform` declarations, curried calls, and pipelines | Present calculation and composition directly | The declaration word is a candidate; familiarity and verbosity need testing |
| Whitespace application and `fn` expressions | Uniform first-class function use | Nested calls and lambda boundaries need discriminating examples |
| Explicit `perform` requests and effect annotations | Make service requests visible | Exact spellings and legacy annotation punctuation are not the current contract |
| `do` sequencing and `<-` | Flatten repeated dependent work | The notation must not silently select an effect, collection, or resource policy |
| Many categorical symbolic operators | Compact notation for experienced users | Increases the amount of notation to learn and creates competition with named operations |
| Nearest-handler descriptions | A seemingly simple lexical story | Conflicts with current unique-capability resolution and explicit disambiguation |
| Shallow and multi-shot handler modes | Explores control expressiveness | Exceeds the retained deep, affine resumption contract |
| One continuing application domain | Reduces simultaneous domain changes while teaching | Transfer still needs unrelated examples after the introduction |

### Historical grammar observations

The historical [parser](https://github.com/pcharbon70/catena/blob/20159d7cb2ae7e1dbb9e09bbd41b10a0ea57d793/src/compiler/parser/catena_parser.yrl)
declares a right-associative pipe. The current C019 rule is left-associative.
That difference is sufficient to require a deliberate migration decision;
copying the old precedence table would not preserve current rules.

Ordinary historical application uses whitespace, while `perform` requests
require parentheses. The grammar comments explain the latter restriction
through parsing conflicts. Such a distinction may be defensible, but it should
be a language-level rule readers can predict, rather than an accidental
consequence of grammar maintenance.

The comments report 17 parser conflicts. Regenerating that exact grammar with
the available OTP 27 toolchain produced **38 shift/reduce conflicts and zero
reduce/reduce conflicts**, together with unused-symbol warnings. The
[journal](../50-journal/2026-09-12-grammar-and-vocabulary-research.md#historical-parser-experiment)
preserves the command and output. This does not prove incorrect parsing.
It does establish that the comment count cannot serve as current parser
evidence. Conflict explanations need reproducible witnesses and regression
cases.

The historical lexer discards newlines with other whitespace and uses
`--` and `{- ... -}` comments. Current layout and comment chapters have
different contracts. Tokens for features such as actors also appear unused
in this grammar. A token inventory, guide example, parser production, and
end-to-end executable feature are different levels of evidence.

The recommendation is to retain a historical example catalog, annotate each
example with the behavior it was meant to teach, and re-express that behavior
in competing candidates. Reinstating the old grammar wholesale would mix
useful ideas with obsolete semantic and lexical assumptions.

## Category theory beneath an ordinary programming interface

### Organize the first encounter around decisions

The initial library guide should answer “which operation fits this dependency?”
before it explains the trait hierarchy. The following names already occur in
the retained [0.1.4 ABI](../60-specification/traits-and-categorical-operations/standard-hierarchy-and-vocabulary.md#canonical-public-surface).
They are authoritative for that revision; the table is not an announcement
of a newly adopted vocabulary.

| Programmer's task | Retained operation | Distinction the explanation should preserve |
| --- | --- | --- |
| Change a successful or present value through a pure transformation | `map` | The operation works through the particular type's structure; it does not promise every type is a physical container |
| Combine inputs where neither calculation needs the other's returned value | `map2` | Independence of data dependency does not itself promise parallel execution or a particular error-accumulation policy |
| Choose the next computation using an earlier returned value | `and_then` | The later step depends on the earlier result; concrete instance behavior still matters |
| Apply a context-producing operation across a finite structure and collect it | `collect_map` | Both the traversed structure and the collected context matter; their order and failure contracts remain visible |

Start with a parcel field that may be absent, an address validation result,
and a collection of parcels. Then introduce a tree or a different result
policy to test transfer. A guide that only presents four variations on lists
can accidentally teach “four list functions” instead of reusable structure.

Each operation page should have a short purpose, a concrete example, a nearby
counterexample, the dependency rule, and links to exact guarantees. A type
signature alone is not sufficient evidence of ordering, cost, callback
multiplicity, or error policy. For example, two values wrapped in a result
type do not tell the reader whether an available combination accumulates
failures; a list-related interface does not imply zip semantics.

### Keep the formal relationship available

Mathematical names remain useful for auditing, literature search, and advanced
library work. Put the formal correspondence, kinds, laws, and derivation
conditions in reference material linked from the ordinary operation page.
Do not require readers to learn two public synonyms before they can write
their first useful program.

The formal hierarchy is also not a license to erase operational differences.
A law valid under specified pure functions and evidence does not justify
reordering observable effects, duplicating callbacks, changing failure order,
or ignoring finite resources. The
[standard operation contracts](../60-specification/standard-stability-and-performance/versioned-operation-contracts.md)
and [optimizer validity rules](../60-specification/optimizer-validity/README.md)
remain the authority for such transformations.

Explain a law first through a permitted change and its conditions. Then offer
the equation and formal name. A safe refactoring example should show both a
case where the change is permitted and a superficially similar case where
its assumptions fail. This makes the theory useful without suggesting that
every elegant equation is an unconditional optimization.

### Design names as a connected vocabulary

Candidate words should be reviewed for the predictions they invite across
the whole language. Avoid giving “context” equally prominent meanings for an
optional value, a lexical environment, a runtime service, and a focused
data structure. Avoid a term suggesting a concurrent task for an operation
that merely expresses dependency.

Use a consistent grammatical role: operations do things, types describe
values, constraints describe supported behavior, and diagnostics explain
mismatches. Shortness is valuable when the term is common and unambiguous
within its setting. Longer wording is justified when it makes an important
role visible at a call site.

Searchability and explanation matter alongside typing. A reader should be
able to ask for “stop when the previous result failed” and find the relevant
operation without knowing its mathematical class. Documentation can index
those task descriptions without creating additional accepted source aliases.

## Effects with progressive disclosure

### Three programmer roles

A useful presentation separates three activities without pretending they are
three different effect systems.

| Role | Immediate questions | Detail that can remain in a later reference layer |
| --- | --- | --- |
| Application author | What does this operation return, and which service does this computation need? | Row normalization, capability evidence representation, continuation lowering |
| Application composer | Which interpretation supplies the request, what remains required outside it, and when is the scope closed? | Backend calling conventions and handler implementation machinery |
| Handler author | How does this operation reply, terminate, or resume, and which resources remain live? | Formal transition derivations, provided the operational rules are explained directly |

The first lesson can introduce a parcel-rate request and a fixed-rate
interpretation used in a test. The next can show that a different
interpretation needs an outer service. Advanced control comes after the
programmer can predict which request is handled and what value continues.

### Keep semantic boundaries visible

Consider this semantic scenario, expressed in prose rather than proposed
source syntax:

1. Construct the values needed by a fixed-rate handler.
2. Install its fresh lexical capability around the parcel calculation.
3. Evaluate a rate request's arguments.
4. Transfer that selected request to the matching handler clause.
5. Produce a reply and, when the clause resumes, continue the calculation.
6. Leave the scope under the applicable lifetime and cleanup rules.

A surface form should let a reader recover this order. In particular, handler
configuration is evaluated before the new handler scope exists.
A visually convenient suffix must not imply that configuration happens after
the calculation. The retained
[deep-handler rules](../60-specification/effects-and-handlers/deep-handlers-and-affine-resumptions.md#strict-handler-application)
and [resource-scope contract](../60-specification/resource-scopes/owned-lifetime-and-mandatory-cleanup.md#acquisition-and-cleanup-order)
supply these obligations.

Likewise, two compatible capabilities of the same family require qualification.
The [request-site rule](../60-specification/effects-and-handlers/declarations-requests-and-signatures.md#request-sites)
forbids choosing whichever handler is textually nearest. A helpful diagnostic
can show the two available capability names and point to the ambiguous request.
Silently selecting one would hide a decision the language currently requires.

A type-level effect requirement, the lexical capability selected for a request,
and permission to access an external resource are related but distinct.
Supplying a handler is not automatically authorization to read a file or start
a host process. The [environmental-authority contract](../60-specification/environmental-effects/explicit-authority-and-closed-launches.md)
must remain legible at application boundaries.

### Borrow mechanisms selectively

Koka illustrates a distinction between general control operations and more
restricted reply-producing handler forms.[^14] This motivates a candidate
Catena convenience layer for common replies. Its admissibility would require
a precise translation preserving affine resumption, clause effects, and
cleanup; Koka's syntax is not itself that proof.

Effekt demonstrates why apparently simple annotations require careful reading:
an empty contextual block requirement is not equivalent to an ordinary pure
function.[^15] Frank provides another formal design for implicit ambient
abilities.[^16] These are evidence that effect detail can be organized
differently, not permission to erase Catena's capability identities or
reinterpret its retained empty rows.

Gleam's `use` expression packages the rest of a block into a callback.[^17]
That is a useful flattening technique to study. It does not by itself provide
exactly-once execution, guaranteed cleanup, or algebraic effects.
Catena's ordinary callback argument convention also differs, so source sugar
would need an explicit semantic translation.

### Simplicity must not disguise control or failure

Recommend keeping an explicit request cue at effect-operation sites in the
first candidates. The spelling is a later decision. The cue should say that
this is a request whose interpretation is supplied elsewhere, while ordinary
function calls remain visually ordinary.

At stable public interfaces, show effect requirements. Inside a computation,
use inference and optional tool displays to avoid repetitive annotation,
subject to the applicable revision's inference rules. The retained
[0.1.5 signatures](../60-specification/effects-and-handlers/declarations-requests-and-signatures.md#function-signatures)
have specific restrictions, including their anonymous-function boundary;
later cumulative revisions must be checked before extending examples.
A future grammar must not quietly import another language's more permissive
higher-order effects.

Do not teach an empty effect row as a guarantee of termination, absence of
traps, or unlimited resources. Do not teach resumption as retry: resuming a
captured continuation and rerunning an earlier action have different
consequences for duplicated external work. Keep the
[exception boundary](catena-exception-boundary.md) clear between expected
failure values, effect requests, terminal traps, and process exits.

The most demanding handler operations should remain visibly demanding.
Hiding continuation implementation is useful; hiding whether a computation
can be abandoned or a resource released is a source of incorrect programs.
The existing affine restriction should guide the basic lesson, rather than
reintroducing historical multi-shot modes for symmetry.

## Grammar candidates and four-way comparisons

The following are research recommendations, with four alternatives considered
for each fork. None is a normative selection or an executed implementation
decision. Existing fixed semantics are constraints on candidates. Any change
to admitted tokens, layout, or interfaces requires explicit versioned adoption.

### GV-01 — Overall surface family

- **A: Uniform delimited calls and explicit blocks.** Makes argument and scope boundaries easy to inspect; adds punctuation and may need careful layouts for partial application.
- **B: Curried whitespace calls and keyword blocks.** Fits functional expression flow; nesting and mixed operators require disciplined precedence and examples.
- **C: Broad optional parentheses and interchangeable block forms.** Offers local stylistic freedom; increases the number of interactions readers and tools must handle.
- **D: Extensible phrase-oriented or macro-defined grammars.** Accommodates domain expression; makes recognition and diagnostics depend on local extensions.

**Recommendation: A as the leading evaluation candidate, with B as the serious
comparator.** This is a hypothesis about inspectable boundaries, not evidence
that parentheses are universally superior. Both candidates retain curried
semantics. Avoid freezing either before matched tasks.

### GV-02 — Function application

- **A: Change calls to fixed host arity.** Familiar to some audiences; conflicts with Catena's semantic-unary model.
- **B: Offer one consistent call grammar elaborating to repeated unary application.** Preserves partial application; requires an explicit rule for argument grouping.
- **C: Require a special partial-application marker.** Makes some intentions visible; changes the retained rule that prefix application is an ordinary value.
- **D: Guess grouping or saturation from inferred types.** Can shorten examples; makes parsing and reading depend on later semantic information.

**Recommendation: B.** Define evaluation of the callee and each written
argument before choosing whether commas, spaces, or another approved
separator present that model. Do not describe a remaining function value
as an arity error.

### GV-03 — Pipeline elaboration

- **A: First-argument insertion.** Suits some APIs; conflicts with the retained pipe and subject-last convention.
- **B: Apply the right-hand function to the left-hand value.** Preserves current semantics and ordinary function values.
- **C: An implicit placeholder chooses an argument position.** Flexible; adds binding and nesting questions.
- **D: Dispatch pipe behavior by type or library.** Enables local conventions; makes the same notation carry different structural meanings.

**Recommendation: B.** Compare surface grouping rules around that meaning.
A pipeline is a readable application path, not an opportunity for a second
calling model.

### GV-04 — Blocks and line structure

- **A: Braces with canonical formatting.** Gives visible boundaries; nested constructs can accumulate punctuation.
- **B: Keyword-delimited blocks.** Offers verbal structure; repeated closing words may obscure the opening construct.
- **C: Significant indentation.** Removes explicit terminators; would reopen the retained non-semantic indentation policy.
- **D: Several equivalent block styles.** Supports preferences; multiplies recovery and formatting cases.

**Recommendation: evaluate A first and B alongside it.** Preserve the retained
layout contract during comparison. Any new keyword-delimited frame must be
specified; visual indentation alone does not currently define scope.

### GV-05 — Ordinary categorical operations

- **A: Formal mathematical terms everywhere.** Precise for specialists; imposes prerequisite vocabulary.
- **B: Behavior-oriented methods with linked formal metadata.** Supports task discovery and audit; names still need empirical testing.
- **C: Friendly and formal aliases accepted equally in source.** Aids transition; doubles the public reading vocabulary.
- **D: Symbolic operators as the primary interface.** Concise for fluent users; makes discovery and verbal explanation harder to evaluate.

**Recommendation: B.** Retain one canonical operation name per intended role
and provide search aliases in documentation before considering source aliases.

### GV-06 — Visibility of trait structure

- **A: Introduce every trait before using its methods.** Complete but front-loads abstractions.
- **B: Teach concrete operations, then generalization, then the formal hierarchy.** Supports incremental models; requires carefully chosen transfer examples.
- **C: Hide all constraints even in diagnostics.** Looks simple until a call is rejected.
- **D: Replace shared traits with unrelated datatype-specific methods.** Locally concrete; conceals useful common structure and increases duplication.

**Recommendation: B.** Keep actual interface requirements inspectable from the
first example. Progressive teaching does not mean changing the checked ABI.

### GV-07 — Effect-operation sites

- **A: Make requests indistinguishable from all calls.** Compact; hides a consequential boundary.
- **B: One explicit request cue with optional capability qualification when unambiguous.** Makes the operation role visible while preserving unique resolution.
- **C: Write the entire handler and effect row at every request.** Explicit but repetitive and difficult to edit.
- **D: Use punctuation varying by effect family.** Compact within one domain; fragments the language-wide model.

**Recommendation: B.** Test whether the cue improves correct predictions.
The actual word is still a vocabulary decision, and qualification remains
mandatory where the current rule requires it.

### GV-08 — Effect annotations

- **A: Infer everything, including exported contracts.** Minimal declarations; obscures stable dependency changes.
- **B: Annotate every internal expression.** Exposes the model; overwhelms ordinary calculations.
- **C: Explicit public boundaries with inference inside and optional explanations.** Concentrates declarations where readers and compatibility checks need them.
- **D: Omit effects from types and rely on documentation.** Easy-looking signatures; loses checked obligations.

**Recommendation: C within applicable inference rules.** Do not turn contextual
effect inference from another language into an implicit semantic extension.

### GV-09 — Handler presentation

- **A: Expose raw continuation machinery everywhere.** Uniformly expressive; burdens ordinary service implementations.
- **B: Restricted reply-oriented convenience plus an explicit advanced control layer.** Reduces common-case ceremony; needs a proven elaboration.
- **C: Always resume implicitly, with no advanced form.** Short; cannot express all retained handler behavior.
- **D: Reintroduce arbitrary shallow and multi-shot modes immediately.** Broad expressiveness; changes the admitted control and lifetime model.

**Recommendation: B as an experiment after semantic review.** Until a
translation is specified, teach the retained explicit affine form rather
than presenting proposed sugar as implemented.

### GV-10 — Sequential convenience forms

- **A: Only nested calls and bindings.** Small grammar; can make long dependent workflows awkward.
- **B: One constrained sequencing form with published expansion.** Can flatten common work while keeping dependency explicit.
- **C: One overloaded form selecting monadic, asynchronous, resource, or exception behavior implicitly.** Concise examples; too many hidden policies.
- **D: A separate block language for every library.** Locally tailored; multiplies forms to learn and tool.

**Recommendation: B only where the expansion preserves the retained operation,
order, multiplicity, and lifetime rules.** In some cases an ordinary binding
is already the clearest answer; syntactic sugar needs a demonstrated task.

### GV-11 — Diagnostics and formatting

- **A: Add them after grammar acceptance.** Fast parser prototype; delays evidence about ordinary mistakes.
- **B: Ship each candidate with canonical layout, incomplete-input cases, and layered diagnostics.** More work per candidate; tests the experience people actually use.
- **C: Delegate all behavior to individual editors.** Flexible; fragments the language's explanations.
- **D: Show full internal terms as the default.** Exact implementation detail; often obscures the source-level repair.

**Recommendation: B.** A useful first message identifies the attempted action,
the relevant source, why it fails, and the available repair. Technical detail
remains accessible rather than becoming the opening sentence.

### GV-12 — Adoption evidence

- **A: Designer preference and attractive demonstrations.** Fast selection; weak evidence of transfer.
- **B: Popularity or community polls.** Broad opinions; substantial selection and familiarity effects.
- **C: Semantic audit, adversarial grammar examples, and preregistered observed tasks.** Slower; separates correctness, comprehension, and preference.
- **D: Automated agents acting as participants.** Cheap repetition; does not establish human comprehension.

**Recommendation: C.** Use preference as additional exploratory information
only under an appropriate study design. G137's existing metric and data
contracts remain binding.

## Parser, formatter, and diagnostic design

A short grammar is valuable only if its interactions are understandable.
Publish the precedence and association rules, the treatment of newlines, and
the boundary between an expression and a following declaration. Avoid
resolving an unclear call by consulting an inferred type. The same incomplete
text should have a coherent interpretation in the compiler, formatter, and
editor.

PEGs demonstrate a precise ordered-choice parsing model; this does not settle
human expectations or error recovery.[^18] Choosing PEG, LR, or a handwritten
parser is therefore an implementation decision made against the candidate
grammar and tool requirements. Parser-generator conflict counts are useful
engineering evidence, but neither zero conflicts nor deterministic recognition
proves readability.

For every sugar, document its expansion and the corresponding source origins.
Repeated unary application must retain written evaluation order. A flattened
workflow must retain which callback can run, how often it can run, and what
scope it captures. Errors should point back to the programmer's construct,
with the generated form available for investigation.

Compiler-message research supports studying explanations as a designed
interface.[^19] Elm provides a firsthand example of deliberate source-local
message design.[^20] Catena's existing
[diagnostic contract](../60-specification/diagnostic-contract/README.md) is the
starting point. Grammar research should extend its concrete parse and
incomplete-program cases rather than invent a competing diagnostic system.

A candidate formatter should preserve comments and documentation attachment,
produce stable layouts, and reveal the same grouping after a line wrap.
A parse-format-parse check should compare semantic structure; an additional
lossless-source check should verify that comments and origin information have
not disappeared. Neither comparison alone replaces the other.

## Candidate corpus and validation path

### Engineering corpus

Use the same domain behavior and semantic observations across candidates.
Include short examples, one longer application, unfinished edits, and
intentionally wrong programs. These are proposed engineering fixtures, not
additional authorized G137 participant fields.

| Case | Distinction to test |
| --- | --- |
| Mapping an optional parcel field | Transforming the contained value versus changing the enclosing policy |
| Combining address validations | Data independence versus execution order and error accumulation |
| Looking up a rate after finding a zone | Genuine dependency on an earlier result |
| Collecting a finite tree of lookups | Structure, callback order, and collected context |
| A partially applied function passed through a pipeline | Function value versus inserted argument template |
| A multiline pipeline stage containing an anonymous function | Call boundary, block closure, and grouping after formatting |
| Two rate-service capabilities in scope | Required qualification rather than nearest-handler selection |
| Handler setup using an outer service | Configuration runs before the new handler is installed |
| A handler clause that resumes or terminates | Continuation use and scope cleanup |
| A comprehension with guards and a failing pattern | Selection, sequencing, and failure classification |
| A resource scope around cancellable work | Lifetime ownership, cleanup order, and remaining external effects |
| A module with imports, documentation, claims, and an entry declaration | Whole-language coherence beyond expressions |

For every case, add a plausible wrong interpretation and an observation that
distinguishes it from the intended meaning. Include missing delimiters, a
misplaced comment, an unfinished clause, and one extra argument that attempts
to apply a non-function value. Do not invent a fixed-arity error for the last
case.

The longer application should use the existing Parcel Relay domain for the
introduction, then a different domain for transfer. Keep the semantics stable
between candidate renderings: changing both the algorithm and the notation
would make the comparison uninterpretable.

### Sequence without a circular gate

1. **Build the semantic corpus and candidate descriptions.** Use retained
   contracts to state observations, likely misconceptions, and tool
   obligations. Research recommendations remain non-normative.
2. **Release the design holds for authorized candidate co-design.** Produce
   concrete competing spellings with four-way decisions and a shared semantic
   audit. This permits a candidate to be studied without calling it final.
3. **Implement bounded candidate prototypes and their tools.** Check
   source-to-retained-input equivalence, invalid inputs, formatting, comments,
   diagnostics, and representative long examples.
4. **Prepare and run the applicable human study.** Stabilize materials for
   each phase, conduct the pilot, set the main-study thresholds, and observe
   real task performance under the approved protocol.
5. **Adopt, version, and integrate the selected language.** If the evidence
   exposes a material failure, revise the candidate and obtain appropriate
   new evidence before making the completion claim.

The distinction between a study candidate and an adopted stable language is
essential. Requiring final vocabulary before studying vocabulary would make
the gate circular; treating an unstudied prototype as final would make it
meaningless.

### Relationship to G137

The normative [observed prediction, transfer, and repair protocol](../60-specification/usability-gate/observed-prediction-transfer-and-repair.md)
currently requires a six-person pilot and a separate 24-person main cohort,
balanced between general and functional programmers. It defines eight task
families, four outcome metrics, counterbalanced conditions, restricted coded
data, and thresholds fixed after the pilot and before the main study.
Prepared materials and agent simulations do not close that gate.

The earlier inquiry's numerical targets are exploratory hypotheses, not
the current preregistered acceptance thresholds. Likewise, its suggested
background records and open-ended explanations are not automatically
permitted data under G137. That contract limits collection to condition,
duration band, outcome code, programmer stratum, and task identity, with
specific verification and deletion requirements.

Aesthetic ratings, detailed prior-language histories, delayed retention,
eye tracking, or broader candidate comparisons could be useful in a separate
exploratory study or an explicitly amended protocol. They should not be added
silently to G137 or used to substitute for its required outcomes. This research
does not recruit participants or supply observed scores.

## Limits and research priorities

There is no direct controlled comparison here of final Catena syntax
candidates, and the historical parser experiment measures parser generation,
not user understanding or full runtime correctness. Published studies use
different populations and tasks; a result about novice syntax or Java comments
does not establish how experienced programmers will understand affine
handlers.

The language comparisons are selective. Elixir informs call-site and tooling
questions; Koka, Effekt, and Frank expose alternative arrangements of effect
complexity; Gleam supplies a callback-sugar example; Swift supplies vocabulary
discipline. None supplies a complete Catena grammar or justifies importing
foreign semantics. Further broad cataloging is less valuable now than
discriminating Catena examples.

The next design work should concentrate on three unresolved questions:
whether delimited or whitespace application best exposes Catena's curried
model; how an explicit request and capability scope can stay readable in
ordinary application code; and which operation names reliably communicate
dependency and failure behavior across different structures. These questions
are concrete enough to prototype and consequential enough to change the
language experience.

## Sources

The source notes preserve bibliographic detail, reading locations, method,
findings, limitations, and links back to this synthesis. Online sources were
accessed on 12 September 2026; living documentation versions are observations,
not permanent version guarantees.

[^1]: Andreas Stefik and Susanna Siebert. “[An Empirical Investigation into Programming Language Syntax](https://doi.org/10.1145/2534973).” ACM Transactions on Computing Education 13(4), Article 19, 2013. [Source note](../30-sources/stefik-siebert-2013-programming-language-syntax.md).
[^2]: Vilma Lappi, Ville Tirronen, and Jonne Itkonen. “[A Replication Study on the Intuitiveness of Programming Language Syntax](https://link.springer.com/article/10.1007/s11219-023-09631-7).” Software Quality Journal 31, 1211–1240, 2023. [Source note](../30-sources/lappi-et-al-2023-syntax-intuitiveness-replication.md).
[^3]: John F. Pane, Chotirat Ann Ratanamahatana, and Brad A. Myers. “[Studying the Language and Structure in Non-Programmers' Solutions to Programming Problems](https://john.pane.net/IJHCS.html).” International Journal of Human-Computer Studies 54(2), 237–264, 2001. [Source note](../30-sources/pane-et-al-2001-non-programmer-problem-solutions.md).
[^4]: Colin S. Gordon. “[The Linguistics of Programming](https://csgordon.github.io/publications/onward24/).” Onward! 2024, 162–182. [Source note](../30-sources/gordon-2024-linguistics-of-programming.md).
[^5]: Kuang-Chen Lu and Shriram Krishnamurthi. “[Identifying and Correcting Programming Language Behavior Misconceptions](https://cel.cs.brown.edu/paper/identifying-correcting-pl-misconceptions/).” Proceedings of the ACM on Programming Languages 8, OOPSLA1, Article 106, 2024. [Source note](../30-sources/lu-krishnamurthi-2024-language-behavior-misconceptions.md).
[^6]: Youssef Abdelsalam, Norman Peitek, Annabelle Bergum, and Sven Apel. “[The Effect of Comments on Program Comprehension: An Eye-tracking Study](https://link.springer.com/article/10.1007/s10664-025-10721-2).” Empirical Software Engineering 31, Article 94, 2026. [Source note](../30-sources/abdelsalam-et-al-2026-comments-and-comprehension.md).
[^7]: T. R. G. Green and M. Petre. “[Usability Analysis of Visual Programming Environments: A Cognitive Dimensions Framework](https://doi.org/10.1006/jvlc.1996.0009).” Journal of Visual Languages and Computing 7(2), 131–174, 1996. [Source note](../30-sources/green-petre-1996-cognitive-dimensions.md).
[^8]: Brad A. Myers and Jeffrey Stylos. “[Improving API Usability](https://doi.org/10.1145/2896587).” Communications of the ACM 59(6), 62–69, 2016. [Source note](../30-sources/myers-stylos-2016-api-usability.md).
[^9]: Swift project. “[API Design Guidelines](https://www.swift.org/documentation/api-design-guidelines/).” Living project guidance, undated. [Source note](../30-sources/swift-project-api-design-guidelines.md).
[^10]: Elixir project. “[Syntax Reference](https://elixir.hexdocs.pm/syntax-reference.html).” Documentation observed at 1.20.4. [Source note](../30-sources/elixir-project-2026-elixir-syntax-and-unicode.md).
[^11]: José Valim. “[Elixir v1.6 Released](https://elixir-lang.org/blog/2018/01/17/elixir-v1-6-0-released/).” 17 January 2018, formatter section. [Source note](../30-sources/valim-2018-elixir-formatter.md).
[^12]: Elixir project. “[Kernel](https://elixir.hexdocs.pm/Kernel.html).” Documentation observed at 1.20.4, pipe and pitfalls sections. [Source note](../30-sources/elixir-project-2026-kernel-pipelines.md).
[^13]: Barry Revzin. “[Exploring the Design Space for a Pipeline Operator](https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2022/p2672r0.html).” WG21 P2672R0, 13 October 2022; proposal, not an adopted standard. [Source note](../30-sources/revzin-2022-pipeline-operator-design-space.md).
[^14]: Daan Leijen. “[The Koka Programming Language](https://koka-lang.github.io/koka/doc/book.html).” Sections 3.4.2–3.4.3; embedded draft grammar identifies v3.2.3. [Source note](../30-sources/leijen-koka-book-surface-and-handlers.md).
[^15]: Effekt research team. “[Effect Polymorphism](https://effekt-lang.org/docs/concepts/effect-polymorphism)” and “[Effect Safety](https://effekt-lang.org/docs/concepts/effect-safety).” Living documentation, undated. [Source note](../30-sources/effekt-project-contextual-effect-polymorphism.md).
[^16]: Sam Lindley, Conor McBride, and Craig McLaughlin. “[Do Be Do Be Do](https://arxiv.org/abs/1611.09259).” POPL 2017, 500–514; arXiv revision 2, 2017. [Source note](../30-sources/lindley-et-al-2017-frank.md).
[^17]: Gleam project. “[Use](https://tour.gleam.run/advanced-features/use/).” Language tour, undated. [Source note](../30-sources/gleam-project-use-expressions.md).
[^18]: Bryan Ford. “[Parsing Expression Grammars: A Recognition-Based Syntactic Foundation](https://pdos.csail.mit.edu/~baford/packrat/popl04/).” POPL 2004, 111–122. [Source note](../30-sources/ford-2004-parsing-expression-grammars.md).
[^19]: Titus Barik, Denae Ford, Emerson Murphy-Hill, and Chris Parnin. “[How Should Compilers Explain Problems to Developers?](https://doi.org/10.1145/3236024.3236040)” ESEC/FSE 2018. [Source note](../30-sources/barik-et-al-2018-compiler-explanations.md).
[^20]: Evan Czaplicki. “[Compiler Errors for Humans](https://elm-lang.org/news/compiler-errors-for-humans).” 2015. [Source note](../30-sources/czaplicki-2015-compiler-errors-for-humans.md).

## Connections

- [Approachable Catena Language Design](../10-maps/approachable-catena-language-design.md) organizes the research and formal constraints.
- [An Approachable Vocabulary for Catena](approachable-language-vocabulary.md) contains the earlier candidate vocabulary and teaching proposal.
- [Vocabulary inquiry](../40-inquiries/how-should-catena-expose-mathematical-structure-without-mathematical-jargon.md) tracks unresolved human-comprehension questions.
- [Language completion checklist](../00-inbox/language-specification-completeness-checklist.md) retains P107/P109 and observed usability as unfinished gates.
- [Historical inspection and research journal](../50-journal/2026-09-12-grammar-and-vocabulary-research.md) preserves local evidence separately from design recommendations.
