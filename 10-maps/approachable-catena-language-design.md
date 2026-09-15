---
title: "Approachable Catena Language Design"
kind: map
created: "2026-08-01"
tags:
  - api-design
  - catena
  - documentation
  - language-design
  - programming-language-education
  - usability
aliases:
  - "Catena vocabulary map"
  - "Behavior-first Catena design"
---

# Approachable Catena Language Design

## Scope

This map follows the design question of how Catena can expose mathematically
rigorous composition through ordinary programming vocabulary. It connects the
candidate public language, its evaluation inquiry, the formal models it must
preserve, and primary work relevant to notation and diagnostics.

The route is deliberately not a translation course from friendly names to
category theory. The formal documents provide the design audit; the public
path should remain usable without them.

## Start here

- [Catena First-Version Grammar and Vocabulary](../20-notes/catena-first-version-grammar-and-vocabulary.md)
  selects concrete candidate expressions, explains the choices, and shows
  representative programs. The user authorized this design on 15 September
  2026 and excluded participant studies during development. Normative adoption
  and implementation remain pending; observed usability is not claimed.
- [Grammar and Vocabulary for Approachable Catena](../20-notes/grammar-and-vocabulary-for-approachable-catena.md)
  compares empirical syntax research, Elixir, effect-language designs, and
  historical Catena. Its twelve four-way recommendations inform P107/P109
  without adopting final spellings or claiming observed usability.
- [Catena Literal Grammar](../20-notes/catena-literal-grammar.md) fixes the
  first programmer-visible value spellings, exact decoding, and source
  provenance while keeping numeric meaning and complete parsing separate.
- [Catena Comments and Documentation Comments](../20-notes/catena-comments-and-documentation-comments.md)
  fixes declaration-documentation attachment and a safe, versioned document
  format without requiring a complete grammar or renderer.
- [Catena Whitespace, Layout, and Line Continuation](../20-notes/catena-whitespace-layout-and-line-continuation.md)
  fixes the layout structure on which the remaining approachable grammar can
  build without assigning meaning to indentation.
- [An Approachable Vocabulary for Catena](../20-notes/approachable-language-vocabulary.md)
  proposes the behavior-first terms, operation families, capability names,
  internal semantic ledger, diagnostic shape, and learning sequence.
- [How Should Catena Expose Mathematical Structure Without Mathematical Jargon?](../40-inquiries/how-should-catena-expose-mathematical-structure-without-mathematical-jargon.md)
  tracks semantic questions and historical prediction, selection, transfer,
  and repair research; participant-study paths are outside development scope.

## Trails

### Evaluate the notation rather than admiring the names

- [Usability Analysis of Visual Programming Environments: A Cognitive Dimensions Framework](../30-sources/green-petre-1996-cognitive-dimensions.md)
  supplies questions about closeness, consistency, role-expressiveness,
  hidden dependencies, abstraction gradient, premature commitment, and
  progressive evaluation.
- The active
  [vocabulary inquiry](../40-inquiries/how-should-catena-expose-mathematical-structure-without-mathematical-jargon.md)
  applies those questions to tasks. Its participant paths and older thresholds
  are historical research proposals outside current development;
  the [normative G137 protocol](../60-specification/usability-gate/observed-prediction-transfer-and-repair.md)
  governs any future claim under that retained contract and remains unpassed.

### Compare expectations with observed performance

- [Stefik and Siebert](../30-sources/stefik-siebert-2013-programming-language-syntax.md)
  distinguish syntax ratings from novice code-writing tasks;
  [Lappi and colleagues](../30-sources/lappi-et-al-2023-syntax-intuitiveness-replication.md)
  replicate the rating line of work, not the programming-performance comparison.
- [Pane and colleagues](../30-sources/pane-et-al-2001-non-programmer-problem-solutions.md)
  examine naturally expressed solutions, while
  [Gordon](../30-sources/gordon-2024-linguistics-of-programming.md) explains how
  prior language and context can shape expectations.
- [Lu and Krishnamurthi](../30-sources/lu-krishnamurthi-2024-language-behavior-misconceptions.md)
  motivate discriminating examples for wrong interpretations.
  [The 2026 comments study](../30-sources/abdelsalam-et-al-2026-comments-and-comprehension.md)
  cautions against assuming more explanatory text always improves performance.

### Learn from language designs without importing their semantics

- [Elixir pipelines](../30-sources/elixir-project-2026-kernel-pipelines.md)
  and [the formatter's introduction](../30-sources/valim-2018-elixir-formatter.md)
  connect readable flow to actual call rules and deliberate layout.
- [Koka](../30-sources/leijen-koka-book-surface-and-handlers.md),
  [Effekt](../30-sources/effekt-project-contextual-effect-polymorphism.md),
  and [Frank](../30-sources/lindley-et-al-2017-frank.md) offer different
  arrangements of effect complexity; the Catena synthesis audits the boundaries.
- [Gleam's use expressions](../30-sources/gleam-project-use-expressions.md)
  supply callback sugar, whose existence alone promises neither cleanup nor
  affine control.
- [API usability](../30-sources/myers-stylos-2016-api-usability.md) and
  [Swift's guidelines](../30-sources/swift-project-api-design-guidelines.md)
  connect naming to discovery and clarity at actual use sites.
- [The historical inspection](../50-journal/2026-09-12-grammar-and-vocabulary-research.md)
  records Catena's earlier teaching examples, obsolete grammar assumptions,
  and a reproducible parser observation.

### Make compiler explanations part of the language

- [How Should Compilers Explain Problems to Developers?](../30-sources/barik-et-al-2018-compiler-explanations.md)
  provides empirical evidence about explanatory structure and repair-oriented
  information.
- [Compiler Errors for Humans](../30-sources/czaplicki-2015-compiler-errors-for-humans.md)
  provides a primary design report on source-local context, focused hints, and
  deliberate message layout.
- The synthesis converts these into action, source, reason, repair, and
  optional-technical-detail layers for Catena diagnostics.

### Preserve the exact semantic foundations

- [Category Theory for Programming](category-theory-for-programming.md) and
  [its synthesis](../20-notes/category-theory-for-programming.md) define the
  seventeen formal structures, their laws, kinds, parent relationships, and
  operational boundaries.
- [Combinators for Algebraic Data and Categorical Programming](combinators-for-algebraic-data-and-categorical-programming.md)
  and [its synthesis](../20-notes/combinators-for-algebraic-data-and-categorical-programming.md)
  distinguish universal, class-derived, datatype-derived, domain, and
  compiler operations.
- [Algebraic Data Types](algebraic-data-types.md) and
  [its synthesis](../20-notes/algebraic-data-types.md) constrain `variant`,
  `payload`, `match`, structural derivation, and coverage explanations.
- [Algebraic Effects and Handlers](algebraic-effects-and-handlers.md) and
  [its synthesis](../20-notes/algebraic-effects-and-handlers.md) constrain the
  meanings of `effect`, `operation`, `uses`, `handle`, and `resume`.
- [Catena Type-System Design](catena-type-system-design.md) and
  [its synthesis](../20-notes/catena-greenfield-type-system.md) constrain
  inference, requirements, evidence, coherence, and the technical details
  hidden behind plain-language type errors.
- [Language-Integrated Specifications and Governance](language-integrated-specifications-and-governance.md)
  constrains the public meanings of needs, promises, examples, properties,
  evidence, approvals, activation, and replacement while keeping checking
  method and authority visible.

### Move from prototypes to guides

The first-version proposal now provides concrete forms and examples. The next
development step is versioned adoption and a shared parser/elaborator, with
semantic comparison, formatting, and diagnostic cases for `map`, independent
`map2`, dependent `and_then`, structure-wide `collect_map`, trait guarantees,
effects, and process failure. Explain successful cases and deliberate errors
through the same rules. These development checks do not constitute participant
observations or satisfy the historical G137 evidence gate.

## Open questions

- Which of the candidate capability names make programmers predict the wrong
  shape, dependency, effect, ordering, mutation, or cost?
- Do all seventeen formal structures need distinct public traits, or should
  some remain derived, module-scoped, or advanced-only interfaces?
- Can the `map` / `map2` / `and_then` / `collect_map` decision family transfer
  across data, validation, parsing, effects, and concurrency without becoming
  misleadingly uniform?
- How should Catena expose a capability's formal lineage to interested readers
  without turning it into prerequisite vocabulary?
- Which guarantees can the compiler derive or verify, and which remain
  documented programmer obligations that optimizers must not trust?
- What diagnostic detail boundary serves both ordinary repair and compiler-
  developer investigation?

Track these questions in the
[active vocabulary inquiry](../40-inquiries/how-should-catena-expose-mathematical-structure-without-mathematical-jargon.md).
