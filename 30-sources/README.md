---
title: "Sources"
kind: map
created: "2026-07-31"
tags:
  - archive-navigation
  - directory-index
aliases:
  - "Sources index"
---

# Sources (`30-sources`)

## Purpose

Source notes preserve bibliographic provenance and evidence-focused reading
notes separately from the archive's synthesis.

## What belongs here

Create one note for each substantively used paper, book, specification,
official documentation set, talk, dataset, or other primary work. Incidental
mentions can remain as citations in the document that uses them.

## Index

### Subdirectories

- None yet.

### Documents

- [Actors: A Model of Concurrent Computation in Distributed Systems](agha-1986-actors.md)
  — supplies the actor-model foundation for asynchronous messages, local
  state, and dynamically created communicating agents.
- [A Core Erlang Formalisation](bereczky-et-al-2024-core-erlang-formalisation.md)
  — records a mechanized sequential Core Erlang semantics and the boundary
  between formal core evaluation and full actor behavior.
- [Erlang/OTP 29 Processes](erlang-otp-29-processes.md) — documents the target
  runtime's process isolation, asynchronous send, mailbox order, links, and
  termination behavior.
- [Erlang/OTP 29 Runtime Resource Controls](erlang-otp-29-runtime-resource-controls.md)
  — documents process heap limits, on/off-heap message storage, and emulator
  controls that make mailbox capacity a deployment concern rather than one
  portable message count.
- [Erlang/OTP 29 System Limits](erlang-otp-29-system-limits.md) — records the
  arity-255 target ceiling and distinguishes VM ceilings from Catena portable
  source floors.
- [Structural Operational Semantics](plotkin-2004-structural-operational-semantics.md)
  — provides the transition-system method used for Catena's configurations,
  evaluation order, and explicit terminal states.
- [Syntactic Type Soundness for Actors](fowler-et-al-2023-mailbox-types.md) —
  develops mailbox types, selective receive, and preservation/progress
  arguments for typed actor calculi.
- [A Syntactic Approach to Type Soundness](wright-felleisen-1994-syntactic-type-soundness.md)
  — supplies the preservation-and-progress proof method for the sequential
  kernel.
- [RFC 2119: Key Words for Use in RFCs to Indicate Requirement Levels](bradner-1997-rfc-2119.md)
  — distinguishes absolute requirements, justified recommendations, and
  genuinely optional behavior while cautioning against unnecessary
  imperatives.
- [RFC 8174: Ambiguity of Uppercase vs Lowercase in RFC 2119 Key Words](leiba-2017-rfc-8174.md)
  — gives uppercase requirement words their specialized meaning, leaves
  lowercase words as ordinary English, and confirms that declarative prose can
  remain normative.
- [RFC 3629: UTF-8, a Transformation Format of ISO 10646](yergeau-2003-utf-8.md)
  — defines the Internet UTF-8 byte grammar, invalid-sequence security
  boundary, and leading-BOM protocol considerations used by C013.
- [The Unicode Standard, Version 17.0: Conformance and Encoding Forms](unicode-consortium-2025-unicode-standard-17.md)
  — defines Unicode scalars, well- and ill-formed UTF-8, and the strict
  encoding-form boundary used by Catena source text.
- [Unicode Standard Annex #15: Unicode Normalization Forms](whistler-2025-unicode-normalization-forms.md)
  — explains canonical and compatibility transformations, scalar reordering,
  and stability considerations behind C013's preservation policy.
- [Unicode Standard Annex #31: Unicode Identifiers and Syntax](davis-leroy-2025-unicode-identifiers-syntax.md)
  — defines Unicode 17 XID profiles, stable identifier syntax, and normalized
  or filtered identifier conformance used by C014.
- [Unicode Technical Standard #39: Unicode Security Mechanisms](davis-suignard-2025-unicode-security-mechanisms.md)
  — defines identifier status, restriction levels, script resolution, and
  confusable prototypes used by C014's security profile.
- [Unicode Technical Standard #55: Unicode Source Code Handling](leroy-davis-2024-unicode-source-code-handling.md)
  — applies normalization, case, confusable, display, and diagnostic guidance
  to programming languages and explains C014's layered policy.
- [WG14 N1570: ISO/IEC 9899:201x Committee Draft](wg14-2011-n1570.md) —
  distinguishes implementation-defined and unspecified values, traps,
  conformance, and translation limits while exposing the undefined-behavior
  model Catena rejects.
- [IEEE Std 754-2019: Floating-Point Arithmetic](ieee-2019-754-floating-point.md)
  — fixes the binary64 finite domain, signed zero, subnormals,
  `roundTiesToEven`, and correctly rounded decimal conversion used by the
  numeric literal model.
- [WebAssembly Core Specification 3.0](rossberg-2026-webassembly-core-specification.md)
  — separates representation well-formedness, declarative validation,
  execution, explicit traps, bounded nondeterminism, and implementation
  limitations.
- [JEP 12: Preview Features](buckley-2018-preview-features.md) — defines
  explicit release-bound opt-in, impermanent-but-complete language features,
  artifact marking, diagnostics, and stabilization or removal outcomes.
- [Semantic Versioning 2.0.0](preston-werner-2013-semantic-versioning.md) —
  relates major, minor, and patch components to a declared public contract and
  explicitly treats the pre-1.0 line as unstable.
- [The Rust Edition Guide](rust-project-edition-guide.md) — documents
  package-local compatibility selection, retained earlier editions,
  interoperable dependencies, and conservative migration edits.
- [Abstraction-Safe Effect Handlers via Tunneling](zhang-myers-2019-abstraction-safe-effect-handlers.md)
  — shows that nearest matching handlers can violate higher-order abstraction
  and develops a tunneling semantics with stronger guarantees.
- [Algebraic Operations and Generic Effects](plotkin-power-2003-algebraic-operations-generic-effects.md)
  — gives the technical continuation-compatible meaning of algebraic
  operations and their correspondence with generic effects.
- [Applicative Programming with Effects](mcbride-paterson-2008-applicative-programming-effects.md)
  — identifies fixed-shape effectful programming below monadic power and
  develops applicative laws, composition, and traversal.
- [Binders by Day, Labels by Night](biernacki-et-al-2020-effect-instances-lexically-scoped-handlers.md)
  — models multiple uses of one effect signature as lexically scoped instance
  names tracked by the type-and-effect system.
- [Automatic Synthesis of Typed Lambda-Programs on Term Algebras](bohm-berarducci-1985-typed-lambda-programs.md)
  — represents term-algebra values and their eliminators in second-order typed
  lambda calculus without primitive recursion or conditionals.
- [Compiler Errors for Humans](czaplicki-2015-compiler-errors-for-humans.md)
  — records Elm's source-local, contextual, deliberately laid-out approach to
  compiler explanations and the limits of its design-report evidence.
- [HOPE: An Experimental Applicative Language](burstall-et-al-1980-hope.md) —
  integrates declared algebraic constructors, parametric types, pattern
  equations, higher-order recursion patterns, and constructor hiding.
- [Principal Type-Schemes for Functional Programs](damas-and-milner-1982-principal-type-schemes.md)
  — proves Algorithm W's completeness and principal-type result for the
  `let`-polymorphic core.
- [Complete and Easy Bidirectional Typechecking for Higher-Rank Polymorphism](dunfield-krishnaswami-2013-bidirectional-typechecking.md)
  — gives a sound and complete annotation-directed algorithm for predicative
  higher-rank polymorphism.
- [Compiling to Categories](elliott-2017-compiling-to-categories.md) — turns
  the typed-lambda-calculus/category correspondence into modular alternate
  interpretations for circuits, differentiation, incremental computation, and
  analysis.
- [Data Types à la Carte](swierstra-2008-data-types-a-la-carte.md) — combines
  functor components, coproducts, fixed points, folds, and inferred injection
  to build modular syntax and semantics.
- [Deductive Systems and Categories III](lambek-1972-deductive-systems-categories-iii.md)
  — relates cartesian closed categories, intuitionistic deduction, and typed
  combinatory structure.
- [Effect Handlers in Scope](wu-et-al-2014-effect-handlers-in-scope.md) — shows
  why first-order operations cannot by themselves represent operations that
  scope over genuine subcomputations.
- [The Essence of Dataflow Programming](uustalu-vene-2005-essence-dataflow-programming.md)
  — uses comonads and coKleisli arrows to structure context-dependent stream
  and dataflow computation.
- [The Essence of the Iterator Pattern](gibbons-oliveira-2009-essence-iterator-pattern.md)
  — characterizes traversal as shape-preserving mapping with applicative
  accumulation and examines the limits of its usual laws.
- [Fantasy Land Algebraic Specification](fantasy-land-algebraic-specification.md)
  — provides operation signatures, parent relationships, and laws for most of
  the selected weak and strong algebraic interfaces.
- [Functional Programming with Bananas, Lenses, Envelopes and Barbed Wire](meijer-et-al-1991-functional-programming-bananas.md)
  — develops folds, unfolds, hylomorphisms, and program-calculation laws from
  recursive datatype structure.
- [Generalising Monads to Arrows](hughes-2000-generalising-monads-arrows.md) —
  gives analyzable input/output computations a lawful composition interface
  more general than monadic libraries.
- [A Polymorphic Type System for Extensible Records and Variants](gaster-jones-1996-extensible-records-variants.md)
  — develops unique-label structural rows with lacks predicates and effective
  inference.
- [The Principal Type-Scheme of an Object in Combinatory Logic](hindley-1969-principal-type-scheme.md)
  — establishes the principal-scheme foundation in combinatory logic.
- [A Theory of Qualified Types](jones-1994-theory-of-qualified-types.md) —
  extends HM inference with predicates, evidence, ambiguity, and coherence.
- [Handlers in Action](kammar-et-al-2013-handlers-in-action.md) — develops open
  forwarding handlers, practical examples, a typed operational calculus, and
  implementation comparisons.
- [Handlers of Algebraic Effects](plotkin-pretnar-2009-handlers-algebraic-effects.md)
  — interprets handlers as models of effect theories and handling as the
  induced homomorphism from a free computation.
- [How to Make Ad-Hoc Polymorphism Less Ad Hoc](wadler-blott-1989-ad-hoc-polymorphism.md)
  — introduces type classes as a systematic constrained-polymorphism
  mechanism with evidence-passing semantics.
- [How Should Compilers Explain Problems to Developers?](barik-et-al-2018-compiler-explanations.md)
  — empirically studies explanatory and repair information in compiler
  messages using professional developers and Stack Overflow examples.
- [Monadic Parsing in Haskell](hutton-meijer-1998-monadic-parsing.md) — builds
  parsers from pure, bind, failure, choice, character, repetition, expression,
  and token combinators while exposing recursive-descent limitations.
- [Typing Haskell in Haskell](jones-1999-typing-haskell-in-haskell.md) — gives
  an executable specification of substitutions, kinds, schemes, classes, and
  binding-group inference.
- [Type Classes with Functional Dependencies](jones-2000-functional-dependencies.md)
  — explains how declared dependencies improve ambiguity and precision in
  multi-parameter class relations.
- [Koka: Programming with Row-Polymorphic Effect Types](leijen-2014-koka-row-polymorphic-effects.md)
  — presents an HM-shaped, principal effect-row inference system and
  effect-directed generalization policy.
- [Monads for Functional Programming](wadler-1995-monads-functional-programming.md)
  — applies monadic sequencing to evaluator modularity, state-like array code,
  and parsing.
- [Notions of Computation as Monoids](rivas-jaskelioff-2017-notions-computation-monoids.md)
  — unifies monads, applicatives, and arrows as monoids in suitable monoidal
  categories while preserving their distinctions.
- [Notions of Computation and Monads](moggi-1991-notions-computation-monads.md)
  — separates values from computations and gives multiple effect notions a
  common categorical sequencing semantics.
- [A Theory of Type Polymorphism in Programming](milner-1978-type-polymorphism.md)
  — introduces the programming-language discipline and Algorithm W.
- [OutsideIn(X): Modular Type Inference with Local Assumptions](vytiniotis-et-al-2011-outsidein.md)
  — separates generation from solving and studies principality under scoped
  local assumptions.
- [Proving Properties of Programs by Structural Induction](burstall-1969-structural-induction.md)
  — derives a program-proof principle from finite constructor-built data and
  its well-founded constituent relation.
- [Profunctor Optics: Modular Data Accessors](pickering-et-al-2017-profunctor-optics.md)
  — represents lenses, prisms, and traversals as composable profunctor
  transformations and proves equivalence to concrete accessors.
- [Retrofitting Effect Handlers onto OCaml](sivaramakrishnan-et-al-2021-retrofitting-effect-handlers-ocaml.md)
  — implements native one-shot continuations with fiber stacks and evaluates
  runtime, tooling, FFI, and idle-overhead consequences.
- [Shallow Effect Handlers](hillerstrom-lindley-2018-shallow-effect-handlers.md)
  — formalizes shallow case-splitting handlers and their relationship to deep
  fold-style handlers.
- [Simple Unification-Based Type Inference for GADTs](peyton-jones-et-al-2006-gadt-inference.md)
  — separates ordinary uniform-result constructor inference from
  annotation-directed GADT pattern refinement and local equalities.
- [Simple Imperative Polymorphism](wright-1995-simple-imperative-polymorphism.md)
  — motivates and studies the value restriction for strict effectful
  languages.
- [Selective Applicative Functors](mokhov-et-al-2019-selective-applicative-functors.md)
  — develops analyzable conditional effects between applicative and monadic
  dependency and evaluates them in build and remote-query systems.
- [Soundly Handling Linearity](tang-et-al-2024-soundly-handling-linearity.md)
  — introduces control-flow linearity to prevent multi-shot resumptions from
  discarding or duplicating captured linear resources.
- [Type Directed Compilation of Row-Typed Algebraic Effects](leijen-2017-type-directed-compilation-row-typed-algebraic-effects.md)
  — combines effect-row inference and direct semantics with a type-directed
  selective CPS backend.
- [Types, Abstraction and Parametric Polymorphism](reynolds-1983-types-abstraction-parametric-polymorphism.md)
  — develops relational parametricity as a uniformity and representation-
  independence principle for polymorphic programs.
- [Usability Analysis of Visual Programming Environments: A Cognitive Dimensions Framework](green-petre-1996-cognitive-dimensions.md)
  — develops a tradeoff-oriented vocabulary for evaluating notation through
  closeness, consistency, hidden dependencies, abstraction, and related
  dimensions.
- [Theorems for Free!](wadler-1989-theorems-for-free.md) — derives useful
  program equations from polymorphic types through Reynolds's abstraction
  theorem.
- [The Definition of Standard ML (Revised)](milner-et-al-1997-definition-standard-ml.md)
  — formalizes nominal datatype generation, constructor schemes, ordered
  pattern matching, match failure, and module abstraction.
- [Unboxed Objects and Polymorphic Typing](leroy-1992-unboxed-objects.md) —
  reconciles specialized unboxed representations with polymorphic and abstract
  uniform-representation boundaries through typed coercions.
- [Views: A Way for Pattern Matching to Cohabit with Data Abstraction](wadler-1987-views-pattern-matching.md)
  — separates an abstract representation from the constructor vocabulary used
  to pattern-match its public observations.
- [Why Functional Programming Matters](hughes-1989-why-functional-programming-matters.md)
  — explains higher-order functions and lazy producer/consumer boundaries as
  program-decomposition glue.
- [Warnings for Pattern Matching](maranget-2007-warnings-pattern-matching.md) —
  derives exhaustiveness, redundancy, and missing-pattern witnesses from a
  usefulness analysis over typed pattern matrices.
- [A New Implementation Technique for Applicative Languages](turner-1979-applicative-language-implementation.md)
  — compiles lambda terms by bracket abstraction into variable-free
  combinator code for graph reduction.
- [Applying Design by Contract](meyer-1992-applying-design-by-contract.md) —
  makes preconditions, postconditions, invariants, and responsibility
  executable parts of component interfaces.
- [Contracts for Higher-Order Functions](findler-felleisen-2002-contracts-higher-order-functions.md)
  — gives delayed higher-order monitoring and blame assignment a typed
  language semantics.
- [Dafny: An Automatic Program Verifier for Functional Correctness](leino-2010-dafny.md)
  — integrates contracts, frames, invariants, termination, ghost state, and
  solver-backed proof obligations with programs.
- [Alloy: A Lightweight Object Modelling Notation](jackson-2002-alloy.md) —
  provides a compact relational specification language and automatic bounded
  counterexample search whose finite scope remains explicit.
- [The Temporal Logic of Actions](lamport-1994-temporal-logic-actions.md) —
  expresses concurrent systems, temporal properties, and refinement in one
  logic over behaviors.
- [An Overview of the K Semantic Framework](rosu-serbanuta-2010-k-semantic-framework.md)
  — shows how executable configurations and rewrite rules can drive multiple
  language-semantics tools from one definition.
- [Typestate: A Programming Language Concept for Enhancing Software Reliability](strom-yemini-1986-typestate.md)
  — makes permitted operations depend on a compiler-tracked lifecycle state.
- [Cedar: A New Language for Expressive, Fast, Safe, and Analyzable Authorization](cutler-et-al-2024-cedar.md)
  — isolates authorization decisions in a restricted language with validation
  and exact policy analysis.
- [in-toto: Providing Farm-to-Table Guarantees for Bits and Bytes](torres-arias-et-al-2019-in-toto.md)
  — binds a signed process layout to signed artifact and step provenance.
- [Proof-Carrying Code](necula-1997-proof-carrying-code.md) — separates
  producer-side proof construction from consumer-side policy and checking.
- [QuickCheck: A Lightweight Tool for Random Testing of Haskell Programs](claessen-hughes-2000-quickcheck.md)
  — makes properties executable through generated data while exposing sample,
  distribution, and finite-testing limits.
- [Erlang/OTP Modules and Code Loading](erlang-otp-modules-and-code-loading.md)
  — records the mandatory first module declaration, the declared-name
  basename rule, module-named artifacts, and generated-source provenance on
  the target.
- [The Rust Reference: Crates and Modules](rust-project-2026-crates-and-modules.md)
  — documents the filename-derived module model whose build-held identity
  Catena declines.
- [Erlang/OTP Expressions and Guard Sequences](erlang-otp-expressions-and-guard-sequences.md)
  — specifies ordered guarded clauses, the restricted side-effect-free guard
  subset, guard-operation failure, selective-receive mailbox scanning, and
  nested list, binary, and map comprehensions; it also records `badarith`
  exceptional float arithmetic, host-parser refusal of out-of-range decimals,
  and mixed-type numeric comparison on the target.
- [Erlang/OTP 29 Compiler Recommendations for Language Implementors](erlang-otp-29-compiler-recommendations-language-implementors.md)
  — establishes Erlang source or Abstract Format as the supported route for a
  BEAM language and warns against Core Erlang and BEAM assembly interfaces.
- [Erlang/OTP Function Matching and Optimization](erlang-otp-function-matching-optimization.md)
  — shows how overlapping guarded clauses constrain compiler test reordering
  and generated match structure.
- [Haskell 2010 Language Report](marlow-2010-haskell-language-report.md) —
  defines Boolean, pattern, and binding guards and translates them into nested
  matching and conditionals; it also gives list-comprehension typing, scope,
  evaluation order, and kernel translation, plus overloaded numeric literals
  with defaulting and undefined fixed-precision exceptional conditions, and module headers paired with filename conventions that default missing headers to `Main`. Its section 1.4 fixes six name kinds in two spelling classes with qualification as the ambiguity escape, and its fixity and module sections anchor the operator and file-binding comparisons.
- [Lower Your Guards: A Compositional Pattern-Match Coverage Checker](graf-et-al-2020-lower-your-guards.md)
  — elaborates rich patterns into a small guard-tree IR for modular coverage,
  refinement, witness, and accessibility analysis.
- [OCaml 5.4 Expressions and Pattern-Matching Guards](ocaml-5-4-expressions-and-pattern-guards.md)
  — supplies the ordered arbitrary-Boolean guard baseline: pattern bindings,
  true selection, and false fallthrough; it also fixes OCaml's precedence
  table with left-associative comparisons, right-associative `&&`/`||`, and
  unspecified operand order.
- [The Rust Reference: Match Expressions](rust-reference-match-expressions.md)
  — specifies Boolean and conditional-let guards while exposing side effects,
  binding scope, ownership, and multiple evaluation under or-patterns.
- [Structural and Semantic Pattern Matching Analysis in Haskell](kalvoda-kerckhove-2019-structural-semantic-pattern-matching.md)
  — evaluates an SMT-backed oracle that improves arithmetic guard coverage
  while retaining explicit theory and complexity limits.
- [EEP 70: Strict and Relaxed Generators](erlang-eep-70-strict-and-relaxed-generators.md)
  — distinguishes intentional pattern filtering from assertive matching and
  documents the production risk of silently skipped malformed input.
- [EEP 73: Zip Generator](erlang-eep-73-zip-generators.md) — specifies
  lockstep comprehension traversal, unequal-length and pattern failures,
  precedence, diagnostics, and tuple-allocation avoidance.
- [Elixir 1.20 Comprehensions](elixir-1-20-comprehensions.md) — demonstrates
  arbitrary enumerable sources, filtering patterns, truthy filters, effectful
  qualifiers, bit strings, and generic result collectors on the BEAM.
- [Elixir 1.19 Syntax and Unicode](elixir-project-2026-elixir-syntax-and-unicode.md)
  — defines explicit expression blocks, newline/semicolon separators,
  grammar-aware multiline forms, and Elixir's narrow whitespace repertoire.
- [Python 3.14 Lexical Analysis](python-software-foundation-2026-python-lexical-analysis.md)
  — defines physical and logical lines, continuation, semantic indentation,
  tab expansion, INDENT/DEDENT, blank lines, token separation, and the
  numeric/string/byte/interpolation feature cross product.
- [The Rust Reference: Whitespace](rust-project-2026-rust-whitespace.md) —
  defines Rust's free-form indentation principle and exact Unicode
  `Pattern_White_Space` repertoire.
- [Scala 3.4 For Comprehensions](scala-3-4-for-comprehensions.md) — separates
  exhaustive generators from explicit `case` filtering and translates the
  surface through carrier-provided mapping and filtering methods.
- [Comprehending Monads](wadler-1992-comprehending-monads.md) — derives
  generator composition from monadic operations while showing that Boolean
  filters require a separate lawful zero.
- [Comprehensive Comprehensions](peyton-jones-wadler-2007-comprehensive-comprehensions.md)
  — formalizes ordering, grouping, zip, qualifier scope, and transformations,
  exposing both the power and semantic cost of richer comprehension syntax.
- [JSON Canonicalization Scheme](rundgren-et-al-2020-json-canonicalization-scheme.md)
  — defines reproducible JSON bytes, strict input constraints, recursive
  UTF-16 property ordering, and the security-sensitive basis for signed Catena
  governance payloads.
- [Edwards-Curve Digital Signature Algorithm](josefsson-liusvaara-2017-eddsa.md)
  — specifies Ed25519 encoding, signing, verification, security constraints,
  and independent known-answer vectors.
- [The Update Framework Specification](the-update-framework-specification.md)
  — provides the distinct-key threshold, offline root, scoped delegation, and
  dual-authority root-continuity model adapted by the 0.1.6 candidate.
- [CommonMark Specification 0.31.2](macfarlane-2024-commonmark-specification.md)
  — fixes the Markdown grammar used by C016, including fenced info strings and
  the raw-HTML behavior that requires a separate safe-rendering rule.
- [ECMAScript 2026 Language Specification: Comments](ecma-international-2026-ecmascript-comments.md)
  — shows that a line-comment terminator remains separate and multiline
  comment line breaks remain syntactically observable.
- [Elixir 1.20 Writing Documentation](elixir-project-2026-writing-documentation.md)
  — separates API documentation from source comments, uses Markdown, and
  makes doctest execution an explicit test action.
- [The Rust Reference: Comments](rust-project-2026-rust-comments.md) — defines
  nested slash comments, exact outer/inner documentation prefixes, attachment,
  and awkward delimiter edge cases.
- [The Rust Reference: Literal Tokens and Expressions](rust-project-2026-literal-tokens.md)
  — documents exact raw hash delimiters, text/byte/character separation,
  escapes, numeric tokens, suffix boundaries, semantic conversion, and the
  `i32`/`f64` typed-literal resolution with static out-of-range rejection.
- [The Rust Reference: Operator Expressions and Precedence](rust-project-2026-operator-expressions.md)
  — documents the fixed precedence ladder, per-level associativity,
  non-associative comparison chains, prefix minus over positive literals,
  and left-to-right operand evaluation.
- [The Swift Programming Language: Lexical Structure](swift-project-2026-lexical-structure.md)
  — independently specifies balanced nested multiline comments, exact
  extended string delimiters, and delimiter-sensitive interpolation.

## Maintaining this index

Index every direct source note with a concise description. Preserve exact
metadata where available, never invent unknown fields, and link derived work.
