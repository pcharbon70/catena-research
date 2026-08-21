---
title: "Operators and Punctuation"
kind: map
created: "2026-08-21"
tags:
  - archive-navigation
  - catena
  - language-design
  - operators
  - syntax
aliases:
  - "Catena operators map"
---

# Operators and Punctuation

## Scope

This map connects the C013–C018 atom contracts and the C015 capability/frame
debt that the operator boundary must pay, the primary fixed-ladder and
extensible-fixity evidence, the C019 decision artifacts, and the owners of
everything the token grammar deliberately does not decide.

## Start here

- [Catena Operators and Punctuation](../20-notes/catena-operators-and-punctuation.md)
  develops the closed semantic-mapped token set, the fixed precedence
  ladder with non-associative comparisons, capability and frame assignments,
  and the rejected alternatives.
- [Open operator inquiry](../40-inquiries/how-should-catena-fix-operators-and-punctuation.md)
  records the operational question, hypotheses, and evidence required for
  resolution.
- [Numeric Literal Semantics map](numeric-literal-semantics.md) fixes the
  negation meaning the prefix `-` spelling is to carry.

## Trails

### Foundations that constrain any answer

- [Separators and Line Continuation](../60-specification/whitespace-and-layout/separators-and-line-continuation.md)
  defines the `join_before`/`join_after` capabilities and delimiter frames
  this boundary must assign concretely.
- [Identifier Specification](../60-specification/identifiers/README.md)
  fixes `.` as the C014 qualification separator.
- [Literal Forms and Boundaries](../60-specification/literal-grammar/literal-forms-and-boundaries.md)
  fixes numeric munching (`1.0`, `1.`) that operator boundaries must not
  disturb.
- [Numeric Types and Literal Typing](../60-specification/numeric-literal-semantics/numeric-types-and-literal-typing.md)
  fixes negation as elaboration semantics awaiting its G019 spelling.
- [Clause Conditions](../60-specification/clause-conditions/syntax-and-safety.md)
  and the [Formal Semantic Kernel](../60-specification/formal-semantic-kernel/canonical-kernel-syntax.md)
  supply every proposed operator's meaning under its internal word name.

### Primary evidence

- [The Rust Reference: Operator Expressions and Precedence](../30-sources/rust-project-2026-operator-expressions.md)
  supplies the fixed ladder, left-to-right operands, prefix minus over
  positive literals, and rejected comparison chains.
- [OCaml 5.4 expressions](../30-sources/ocaml-5-4-expressions-and-pattern-guards.md)
  supplies the contrast: left-grouped comparisons, right-grouped `&&`/`||`,
  and unspecified operand order.
- [Haskell 2010 fixity findings](../30-sources/marlow-2010-haskell-language-report.md)
  supply the rejected user-fixity model with its silent `infixl 9` default
  and non-associative Prelude comparisons.
- [Erlang/OTP expressions](../30-sources/erlang-otp-expressions-and-guard-sequences.md)
  record the target's word operators and unspecified operand order.

### Limits and traceability

- [Implementation Limits and Portability map](implementation-limits-and-portability.md)
  carries the aggregate-input policy that a whole-file token stream defers
  to under G129.
- [Conformance Traceability](conformance-traceability.md) will register the
  operator obligations once candidate chapters exist.

## Open questions

The proposed model awaits normative chapters, a sibling compiler
whole-source tokenizer and operator-expression parser, and tagged executable
evidence. P109 retains application and declaration grammar and the `->`
structure; G020 retains file-to-module relations; G021/G022 retain qualified
name resolution; G040 retains field-like access; G061 retains operator trait
dispatch; G066 retains type-directed resolution questions; G123 retains
editor recovery.
