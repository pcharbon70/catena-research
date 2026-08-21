---
title: "OCaml 5.4 Expressions and Pattern-Matching Guards"
kind: source
created: "2026-08-01"
published: null
citation_key: null
container: "The OCaml Manual"
edition: "5.4"
isbn: null
doi: null
url: "https://ocaml.org/manual/5.4/expr.html"
accessed: "2026-08-21"
tags:
  - expressions
  - operators
  - pattern-matching
aliases:
  - "OCaml guard expressions"
---

# OCaml 5.4 Expressions and Pattern-Matching Guards

## Reference

OCaml, “The OCaml Language: Expressions,” *The OCaml Manual*, version 5.4,
section 7; first consulted 2026-08-01 for guards and re-read 2026-08-21 for
the precedence table and operator semantics (sections 7.1 and 7.5).
[Official manual](https://ocaml.org/manual/5.4/expr.html).

## Research question

What is the simplest mainstream ML account of an arbitrary Boolean clause
guard?

## Findings

- Function, `match`, and `try` cases may carry a `when`
  guard.
- The guard is an arbitrary expression required to have Boolean type.
- It is evaluated only after its pattern succeeds, in an environment extended
  by the pattern's bindings.
- A true result selects the associated body. A false result resumes matching
  at the following pattern rather than retrying the same pattern.
- Match alternatives are ordered; absent a successful case, ordinary
  `Match_failure` behavior applies.

### Precedence, associativity, and operators

- Section 7.1 fixes one table from highest to lowest binding: prefix and
  field-access forms; method access; function, constructor, and tag
  application; prefix `-` and `-.`; exponentiation and shifts
  (`**… lsl lsr asr`, right); multiplicative `*… /… %… mod` with bitwise
  integer operations (left); additive `+… -…` (left); cons `::` (right);
  list and string concatenation `@… ^…` (right); the flat comparison level
  `=… <… >… |… &… $… !=` (left); `& &&` (right); `or ||` (right); `,` (no
  associativity); assignments `<- :=` (right); `if`; `;` (right); and the
  let/match/fun/try forms.
- The comparison operators form one left-associative level that includes
  `=` and `!=`, so chained comparisons parse left-grouped rather than being
  rejected.
- `&&` and `||` are right-associative and short-circuit: the manual reduces
  `e1 && e2` to `if e1 then e2 else false` with the first operand evaluated
  first, and dually for `||`. The word forms `&` and `or` are deprecated
  synonyms.
- Prefix `-` and infix `-` are distinct functions (`~-` and `-`); both
  spellings exist, and the manual notes users may rebind operator symbols
  with ordinary `let` definitions, with `&&`, `||`, and `~-` handled
  specially.
- The manual does not fix operand evaluation order for most multi-operand
  forms: function application, tuple construction, and record construction
  all evaluate subexpressions in an unspecified order, while `e1; e2` and
  the Boolean operators fix left-first order.

Because the guard is an arbitrary expression, the ordinary OCaml semantics of
function calls, effects, divergence, and exceptions remain available inside
it. This last point is an inference from the unrestricted expression grammar
and the manual's general expression semantics, not a separate guard-specific
guarantee.

## Relevance

OCaml supplies the clean baseline rule Catena should keep: pattern first,
Boolean condition second, body on true, next clause on false. It also provides
the contrasting design Catena should not adopt without qualification. A
Boolean type alone says nothing about effects, termination, hidden failure, or
the cost of evaluating a guard.

For operator design, OCaml is the principal contrast case: its comparisons
are left-associative (so `a = b = c` silently parses as `(a = b) = c`, a
well-typed-looking chain with surprising `bool`-comparing behavior), its
`&&`/`||` are right-associative where Rust's are left, its prefix and infix
minus are separate functions, and its operand order is mostly unspecified.
Each difference from the Rust table shows that a fixed ladder is a genuine
design decision rather than an industry constant, and Catena's
deterministic left-to-right commitment rejects the unspecified-order
position.

## Limits

The manual specifies OCaml behavior rather than evaluating usability or
coverage precision. Its unrestricted guards coexist with OCaml's own effect,
exception, and exhaustiveness policies and cannot be transplanted into
Catena's explicit-effect architecture unchanged.

## Derived work

- [Clause Guards](../20-notes/clause-guards.md)
- [Clause Guards map](../10-maps/clause-guards.md)
- [Catena Operators and Punctuation](../20-notes/catena-operators-and-punctuation.md)
- [How Should Catena Fix Operators and Punctuation?](../40-inquiries/how-should-catena-fix-operators-and-punctuation.md)
- [Operators and Punctuation map](../10-maps/operators-and-punctuation.md)
