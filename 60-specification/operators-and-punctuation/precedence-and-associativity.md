---
title: "Precedence and Associativity"
kind: specification
created: "2026-08-21"
status: normative
spec_version: "0.1.15"
tags:
  - operators
  - specification
  - syntax
aliases:
  - "Catena precedence ladder"
---

# Precedence and Associativity

## Status and authority

This chapter is the normative Catena 0.1.15 precedence, associativity,
prefix-operator, and pipe contract. It is governed by
[Specification Authority](../../SPECIFICATION-AUTHORITY.md),
[Catena Conformance Vocabulary](../../CONFORMANCE-VOCABULARY.md), and
[Catena Implementation Limits and Portability](../../IMPLEMENTATION-LIMITS.md).
It consumes the token inventory fixed by
[Token Inventory and Maximal Munch](token-inventory-and-maximal-munch.md)
and denotes the operator meanings fixed by
[C003](../clause-conditions/syntax-and-safety.md), the
[C010 kernel](../formal-semantic-kernel/canonical-kernel-syntax.md), and
[C018 negation](../numeric-literal-semantics/numeric-types-and-literal-typing.md).

The rules apply only to source-language revision `0.1.15`.

## The fixed ladder

Operator expressions are resolved by one fixed precedence table. Levels bind
more tightly as their number decreases (`OP-OBL-007`):

> **Normative definition.**

```text
level  token class                    associativity
 1     atomic operands, groupings     —
 2     prefix  -  !                  prefix (right-recursive over level 2)
 3     binary  *                      left
 4     binary  +  -                   left
 5     binary  <  <=  >  >=           none
 6     binary  ==  !=                 none
 7     binary  &&                     left
 8     binary  ||                     left
 9     binary  |>                     left
```

Atomic operands are C014 names, C017 literals, and parenthesized
operator expressions. `[`, `{`, `,`, `;`, `.`, and `->` participate in no
level; their contents are owned by later grammars, and this chapter's rules
apply inside any region a later grammar fills with an operator expression.

The ladder is fixed by this table alone. Catena 0.1.15 has no fixity
declarations, no user-defined operators, and no program-visible way to
change a level or associativity; the checklist's "fixity declarations or
their absence" is answered by this declared absence. A later revision that
adds either requires an explicit lifecycle record (`OP-OBL-007`).

## Prefix operators

The prefix `-` and `!` bind more tightly than every binary operator and
apply right-recursively to a prefix operand: `--x` is `- (- x)` and
`!-x` is `! (- x)` (`OP-OBL-009`). Prefix `-` denotes C018 negation
elaboration; it is never part of a literal token, so `-1` is negation
applied to the literal `1`, and patterns remain unsigned under C002/C018.
Prefix `!` denotes Boolean `not`.

A prefix operator with no operand — at end of input, before a hard
separator, or before a closing delimiter of an unclosed grouping — is an
invalid form under [Diagnostics and Conformance](diagnostics-and-conformance.md).

## Comparison and equality chaining

Levels 5 and 6 are non-associative. Two consecutive comparison operators,
two consecutive equality operators, or a comparison adjacent to an equality
— `a < b < c`, `a == b == c`, `a < b == c` — are invalid forms that MUST be
rejected, not grouped (`OP-OBL-008`). Parentheses express intent: the value
comparison `(a < b) == c` remains a valid level-6 expression over a grouped
level-5 operand.

## Associativity and grouping

Left-associative levels group left: `a - b - c` is `(a - b) - c`, and
`a && b && c` is `(a && b) && c`. Operand evaluation order of every binary
operator is left to right, matching C010's strict dynamics; this chapter
fixes grouping and structure, and the evaluation-order obligation is
inherited from the slices that own each operator's dynamics.

## The pipe

`|>` is one left-associative binary operator at the loosest level
(`OP-OBL-010`). `x |> f` denotes the application of `f` to the value of
`x`; `x |> f |> g` groups as `(x |> f) |> g` and denotes `g` applied to
the result of the first application. The right operand of a pipe is an
atomic operand or grouping in 0.1.15; general application syntax, partial
application, and multi-argument pipes remain P109. This chapter fixes the
structure of the application relation; its typing and effect behavior
follow the function types of the slices that own application.

## The reserved arrow

`->` is tokenized but participates in no 0.1.15 expression rule. Its
clause-structure meaning remains P109, consistent with the C001 type
notation where the arrow is right-associative in types (`OP-OBL-011`).

## Deliberately separate work

Application, declaration, and clause grammar remain P109. Operator trait
dispatch and overloaded operators remain G061. Whether any operator
resolution may depend on inferred types remains G066. Division, remainder,
and every reserved spelling's eventual semantics remain G105/G061 with
their own later revisions.

## Rationale and evidence (non-normative)

The [operators synthesis](../../20-notes/catena-operators-and-punctuation.md)
compares Rust's rejecting comparisons, OCaml's left-grouped comparisons,
and Haskell's extensible fixity, and records why the fixed rejecting ladder
was selected.
