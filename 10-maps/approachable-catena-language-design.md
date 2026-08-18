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
  turns the proposal into prediction, selection, transfer, repair, collision,
  and semantic-audit tests.

## Trails

### Evaluate the notation rather than admiring the names

- [Usability Analysis of Visual Programming Environments: A Cognitive Dimensions Framework](../30-sources/green-petre-1996-cognitive-dimensions.md)
  supplies questions about closeness, consistency, role-expressiveness,
  hidden dependencies, abstraction gradient, premature commitment, and
  progressive evaluation.
- The active
  [vocabulary inquiry](../40-inquiries/how-should-catena-expose-mathematical-structure-without-mathematical-jargon.md)
  applies those questions to tasks and sets provisional evidence thresholds.

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

The next artifact should be a small set of controlled guide prototypes, not a
complete documentation suite. The prototypes should test `map`, independent
`map2`, dependent `and_then`, structure-wide `collect_map`, trait guarantees,
effects, and process failure in one continuing example. Results should feed
back into the inquiry before names or syntax are stabilized.

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
