---
title: "The Rust Reference: Operator Expressions and Precedence"
kind: source
created: "2026-08-21"
authors:
  - "Rust Project"
published: null
citation_key: "rustProject2026OperatorExpressions"
container: "The Rust Reference"
edition: null
isbn: null
doi: null
url: "https://doc.rust-lang.org/reference/expressions.html"
accessed: "2026-08-21"
tags:
  - expressions
  - language-design
  - operators
  - rust
  - syntax
aliases:
  - "Rust operator expressions"
---

# The Rust Reference: Operator Expressions and Precedence

## Reference

Rust Project, “Expressions” and “Operator Expressions,” *The Rust Reference*,
accessed 2026-08-21.
[Official expressions reference](https://doc.rust-lang.org/reference/expressions.html);
[official operator-expression reference](https://doc.rust-lang.org/reference/expressions/operator-expr.html).

## Research question or contribution

How does a production language with a fixed, non-extensible operator set
order its precedence ladder, classify associativity, and treat ambiguous or
mixed comparison chains?

## Method

The official expression-precedence table and the operator-expression chapter
were read for level ordering, associativity classes, operand evaluation
order, and the treatment of comparison chaining. Compiler behavior and
tutorials were not used as authority.

## Findings

- The reference orders operator precedence in one fixed table from strong to
  weak binding: paths, method calls, and field access; function calls and
  indexing; `?`; unary `-` `!` `*` and borrow; `as`; multiplicative `* / %`;
  additive `+ -`; shifts; bitwise `&`, then `^`, then `|`; comparisons; lazy
  `&&`; lazy `||`; ranges; assignment.
- Associativity is stated per level: arithmetic, shift, bitwise, and the lazy
  Boolean levels group left to right; assignment groups right to left.
- The comparison level — `== != < > <= >=` — is grouped in one flat level and
  marked “Require parentheses”: comparison chains such as `a == b == c` are
  not resolved by associativity but rejected as ambiguous. Ranges behave the
  same way.
- Unary minus and logical not are prefix operators above every binary level,
  and the reference states that `-1.0` is negation applied to the literal
  expression `1.0`, not a negative literal.
- For a wide class of expressions including all binary operator expressions,
  operands are evaluated left to right as written, before applying the
  operator's own effects.
- Many operators can be overloaded through named traits in `core::ops` and
  `core::cmp`; the reference treats overloadability as a library mechanism
  above an unchanged precedence table.

## Relevance

Rust is the closest published model for Catena's chosen design: one fixed
ladder with per-level associativity, no user fixity declarations, prefix
minus as an operator rather than a literal sign, and — critically —
non-associative comparisons requiring parentheses, which resolves `a < b < c`
by rejection rather than by a silent grouping. Catena adopts the same
rejection rule and the same left-to-right operand evaluation commitment,
while declining Rust's overloadability until G061 decides numeric traits and
Rust's full level set (shifts, bitwise operators, ranges, assignment) until
later slices own their semantics.

## Limits

The reference describes Rust, whose expression surface includes place/value
and move semantics, dereference, borrowing, `?`, and compound assignment that
Catena does not share. Its table also mixes operators with non-operator
expression forms; the ladder ordering, not the grammatical machinery, is the
transferable evidence.

## Derived work

- [Catena Operators and Punctuation](../20-notes/catena-operators-and-punctuation.md)
- [How Should Catena Fix Operators and Punctuation?](../40-inquiries/how-should-catena-fix-operators-and-punctuation.md)
- [Operators and Punctuation map](../10-maps/operators-and-punctuation.md)
