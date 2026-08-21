---
title: "Erlang/OTP Expressions and Guard Sequences"
kind: source
created: "2026-08-01"
published: null
citation_key: null
container: "Erlang/OTP System Documentation"
edition: null
isbn: null
doi: null
url: "https://www.erlang.org/doc/system/expressions.html"
accessed: "2026-08-21"
tags:
  - comprehensions
  - compilers
  - erlang
  - floats
  - pattern-matching
aliases:
  - "Erlang guard expressions"
---

# Erlang/OTP Expressions and Guard Sequences

## Reference

Erlang/OTP, “Expressions,” *Erlang/OTP System Documentation*, current online
edition; first consulted 2026-08-01 and re-read 2026-08-21 for the arithmetic,
term-comparison, and bit-syntax sections.
[Canonical documentation](https://www.erlang.org/doc/system/expressions.html).

The page is living documentation. It identified itself as Erlang/OTP 29.0.4
when first consulted and 29.0.5 when re-read; the canonical URL may later
describe a newer release.

## Research question

What selection, iteration, filtering, failure, and mailbox-scanning semantics
does the BEAM's source language attach to clause guards and comprehensions?

## Findings

### Guards and clauses

- `case` evaluates its scrutinee and tests clauses sequentially. A body is
  selected only when both its pattern and optional guard sequence succeed.
- A guard sequence is a short-circuit disjunction of guards. Each guard is a
  conjunction of guard expressions. Erlang therefore has two collection
  separators with different meanings.
- Guard expressions are a restricted subset of Erlang expressions. The
  reference explicitly motivates that restriction by requiring guards to be
  free of side effects. It admits data construction, comparisons, arithmetic,
  Boolean forms, and a documented set of guard BIFs rather than arbitrary
  function calls.
- Only the atom `true` makes a guard expression succeed. An invalid
  arithmetic operation, Boolean operation, short-circuit operation, or guard
  BIF call makes the guard fail rather than propagating that operation's
  exception from the guard.
- The same general clause shape appears in function clauses, `case`,
  `receive`, and parts of `try`.
- A selective receive scans messages from the front of the mailbox and tests
  clause patterns from top to bottom. A message is removed only after a
  pattern and its guard succeed; guard rejection leaves it in the mailbox and
  scanning continues. The reference records worst-case `O(N)` scanning
  cost in the number of earlier messages.

### Comprehensions

- Erlang/OTP 29 documents list, bit-string, and map result forms. Each uses a
  sequence of generators and filters, and all generator kinds can feed all
  result kinds.
- Ordinary adjacent generators are nested and produce combinations in source
  order. Zip generators advance two or more sources together.
- List, bit-string, and map generators each have relaxed and strict variants.
  Relaxed patterns skip mismatches; strict patterns raise. Map result collisions
  keep the last value for a key.
- Generator bindings shadow earlier bindings and do not escape the
  comprehension. The documented rules can make a repeated name surprisingly
  fresh rather than compare it with an outer value.
- A filter must ultimately be Boolean, but failure behavior depends on its
  syntactic category. A failing or non-Boolean guard expression counts as
  false; a non-guard expression that returns a non-Boolean value raises
  `bad_filter`; an exception from an ordinary call propagates.
- The result expression runs once for every generator combination whose
  patterns and filters succeed. Empty results have the identity value of the
  target container.

### Arithmetic, numeric terms, and float boundaries

- All subexpressions are evaluated before an operator is applied, but the
  page states operand evaluation order within one operator expression is “in
  any order”. A language that fixes left-to-right order, as Catena's C010
  kernel does, is deliberately strengthening this behavior.
- Arithmetic operators accept only numbers. Operand type errors and failing
  arithmetic raise exceptions of class `error`; division by zero raises
  `badarith`. `/` is always floating-point division (`4/2` yields `2.0`),
  while `div` and `rem` are integer operations.
- Local verification on OTP 29 confirms the target's finite-float posture:
  `1.0e308 * 1.0e308` raises `badarith` rather than producing an infinity,
  `1.0/0.0` raises `badarith`, and `list_to_float("1.0e400")` raises
  `badarg` rather than saturating. The arithmetic operations observable from
  Catena's target do not manufacture infinities or NaNs.
- Term comparisons mix numeric types: `1 == 1.0` is `true`, with a documented
  precision-dependent conversion strategy around ±9007199254740992.0 chosen
  to keep mixed integer/float ordering transitive.
- Term equivalence `=:=` distinguishes `0` from `0.0` and, since OTP 27,
  `0.0` from `-0.0`; the compiler warns when `0.0` is matched and offers
  `+0.0` as the deliberate form. Erlang therefore carries at least three
  numeric equality notions, chosen by operator rather than by type.
- Bit-syntax float segments require finite representations: matching fails
  if the segment bits do not encode a finite float, and construction raises
  when a segment is too small for the value.

## Relevance

This is the nearest runtime precedent for Catena. It demonstrates that
side-effect freedom is valuable for both ordinary clause selection and
selective receive. It also exposes choices Catena should make explicitly
rather than inherit accidentally: whether guard faults mean false, whether a
runtime whitelist defines source semantics, whether pattern mismatch filters,
and whether filter failure depends on the filter's syntax.

The receive rules show why guard cost is observable even when guards are pure:
one source guard may run against many queued messages before a selection
succeeds.

The comprehension rules show that a BEAM backend can support nested list
construction, strict and filtering patterns, and zip traversal. They do not
require Catena to copy Erlang's symbolic operators or its split filter-failure
rules.

For numeric literal semantics, the page supplies the target-behavior
precedent: a finite-float domain with raising arithmetic aligns a Catena
`Float` domain that excludes infinities and NaN with what the BEAM actually
does, and the host parser's refusal of out-of-range decimals is evidence that
static invalidity is implementable rather than exotic. Conversely, Erlang's
mixed-type numeric comparison and its operator-selected equality notions are
exactly the implicit coercions and silent ambiguity a statically typed Catena
must not inherit, informing the no-implicit-coercion boundary of C018 and the
open primitive-equality owner P035.

## Limits

Erlang is dynamically typed and treats some guard and generator failures as
normal filtering mechanisms. Its exact-`true` rule, exception-to-failure
conversion, fresh-variable generator rules, and runtime match errors do not
follow automatically for a statically typed language with explicit effects.
The documented feature and BIF sets also change between OTP releases, so they
cannot be Catena's stable semantic definition.

## Derived work

- [Clause Guards](../20-notes/clause-guards.md)
- [How Should Catena Design Clause Guards?](../40-inquiries/how-should-catena-design-clause-guards.md)
- [Clause Guards map](../10-maps/clause-guards.md)
- [List Comprehensions](../20-notes/list-comprehensions.md)
- [How Should Catena Specify List Comprehensions?](../40-inquiries/how-should-catena-specify-list-comprehensions.md)
- [List Comprehensions map](../10-maps/list-comprehensions.md)
- [Catena Numeric Literal Semantics](../20-notes/catena-numeric-literal-semantics.md)
- [How Should Catena Define Numeric Literal Semantics?](../40-inquiries/how-should-catena-define-numeric-literal-semantics.md)
- [Numeric Literal Semantics map](../10-maps/numeric-literal-semantics.md)
