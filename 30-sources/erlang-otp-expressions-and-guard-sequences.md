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
accessed: "2026-08-01"
tags:
  - compilers
  - pattern-matching
aliases:
  - "Erlang guard expressions"
---

# Erlang/OTP Expressions and Guard Sequences

## Reference

Erlang/OTP, “Expressions,” *Erlang/OTP System Documentation*, current online
edition accessed 2026-08-01.
[Canonical documentation](https://www.erlang.org/doc/system/expressions.html).

The page is living documentation. It identified itself as Erlang/OTP 29.0.3
when consulted; the canonical URL may later describe a newer release.

## Research question

What selection, safety, failure, and mailbox-scanning semantics does the BEAM's
source language attach to clause guards?

## Findings

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

## Relevance

This is the nearest runtime precedent for Catena. It demonstrates that
side-effect freedom is valuable for both ordinary clause selection and
selective receive. It also exposes two choices Catena should make explicitly
rather than inherit accidentally: whether guard faults mean false, and whether
the source language should mirror a runtime-maintained whitelist of guard BIFs.

The receive rules show why guard cost is observable even when guards are pure:
one source guard may run against many queued messages before a selection
succeeds.

## Limits

Erlang is dynamically typed and treats guard failure as a normal filtering
mechanism. Its exact-`true` rule and exception-to-failure conversion do not
follow automatically for a statically typed language with explicit effects.
The documented BIF set also changes between OTP releases, so it cannot be
Catena's stable semantic definition.

## Derived work

- [Clause Guards](../20-notes/clause-guards.md)
- [How Should Catena Design Clause Guards?](../40-inquiries/how-should-catena-design-clause-guards.md)
- [Clause Guards map](../10-maps/clause-guards.md)
