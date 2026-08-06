---
title: "Effect and Handler Overview"
kind: specification
created: "2026-08-02"
status: normative
spec_version: "0.1.5"
tags:
  - algebraic-effects
  - effect-handlers
  - specification
aliases:
  - "Catena 0.1.5 effect boundary"
---

# Effect and Handler Overview

## Status and authority

This chapter and its five siblings are the normative Catena 0.1.5 effect slice.
They extend the [0.1.1 type and row system](../type-system/README.md),
[0.1.2 data model](../data-and-patterns/README.md),
[0.1.3 clause conditions](../clause-conditions/README.md), and
[0.1.4 traits](../traits-and-categorical-operations/README.md). Requirement
words, invalidity, permitted variation, limits, and explicit failures follow
the repository
[Catena Conformance Vocabulary](../../CONFORMANCE-VOCABULARY.md).

Historical immutable compiler commit
[`b24e58d587c830dbb9d8c87770105714745fcd1b`](https://github.com/pcharbon70/catena/commit/b24e58d587c830dbb9d8c87770105714745fcd1b)
supports the C005 semantic boundary under the retired `0.1` through `0.5`
identifiers. Its environment, commands, results, and bounded evidence are
preserved in the
[C005 conformance journal](../../50-journal/2026-08-03-c005-executable-effect-conformance.md).
It is not evidence for the exact renumbered protocol strings; the fresh gate is
recorded in
[Prototype Slice Renumbering](../../50-journal/2026-08-04-prototype-slice-renumbering.md).

Document status, content labels, rule references, and conflict handling follow
the repository
[Specification Authority](../../SPECIFICATION-AUTHORITY.md).

## Public model

An effect names a family of typed requests. `request` asks for one operation;
`uses` states which request families a computation may leave for its caller;
a lexical capability identifies the intended use of a family; and a named
handler interprets requests around one expression.

The initial surface uses three structural words:

> **Non-normative example.**

```text
handler Recover for failure: Failure[error] { ... }
handle risky_work() using Recover as failure
request failure.raise(reason)
```

The capability qualifier may be omitted only when exactly one compatible
capability is in lexical scope. Formal terms such as algebra, free model, and
continuation remain explanatory vocabulary, not competing syntax.

## Guarantees

Version 0.1.5 provides:

- nominal effect-family and operation identity;
- normal multi-parameter operations over data and closed pure functions;
- behavior-first `request` and `uses` forms;
- statically selected lexical capabilities with explicit ambiguity errors;
- open identity-aware effect rows;
- named module-level handlers that are referenceable across module interfaces
  but are not first-class values;
- complete operation coverage and one mandatory return clause;
- strict call-by-value deep handling with unrelated requests forwarded;
- clause-scoped affine resumptions with a runtime consumed token;
- an executable free-request reference semantics;
- effect-directed CPS for computations that need control capture while pure
  definitions retain the ordinary direct BEAM path; and
- Erlang Abstract Format as the sole OTP 29 `.beam` generation boundary.

## Deliberate exclusions

Version 0.1.5 does not define cleanup or resource scopes, an exception taxonomy,
application host effects, process failure, cancellation, structured
concurrency, higher-order or scoped operations, shallow handlers, multi-shot
resumptions, first-class handler values, effect masking, or public parser
implementation. Those exclusions preserve checklist items G080, G081, G082,
and D083.

## Connections (non-normative)

The rationale and unresolved wider design remain in
[Algebraic Effects and Handlers](../../20-notes/algebraic-effects-and-handlers.md),
the [effect-semantics inquiry](../../40-inquiries/which-algebraic-effect-semantics-should-catena-adopt.md),
and the [effect map](../../10-maps/algebraic-effects-and-handlers.md).
