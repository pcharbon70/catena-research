---
title: "Deep Handlers and Affine Resumptions"
kind: specification
created: "2026-08-02"
status: normative
spec_version: "0.5"
tags:
  - algebraic-effects
  - effect-handlers
  - evaluation-order
  - resumptions
  - specification
aliases:
  - "Catena 0.5 handler dynamics"
---

# Deep Handlers and Affine Resumptions

## Strict handler application

`handle subject using H(arguments) as c` evaluates handler arguments strictly
from left to right in the outer capability environment. It then creates `c`,
installs the selected handler, and evaluates `subject`. Normal return invokes
the mandatory return clause. The return clause and every operation clause run
in the outer capability environment.

Requests for identities other than `c` forward unchanged. Forwarding preserves
the selected identity, operation, already evaluated arguments, and delimited
remainder. Handler order is observable and no commutativity is implied.

## Deep request rule

For an evaluation context `C` with no intervening handler for capability `c`,
the normative dynamics are:

```text
handle return value using H as c
  --> H.return(value)

handle C[request c.operation(arguments)] using H as c
  --> H.operation(arguments, k)

where resume k with reply
  --> handle C[return reply] using H as c
```

The resumption therefore reinstalls the same handler. A matching request made
later by the resumed computation returns to `H`; a request made directly by an
operation clause is resolved only against outer capabilities. The current
handler is not implicitly recursive around its own clauses.

## Result and clause effects

The return clause receives the handled computation's value. An operation
clause receives its declared parameters and one dedicated resumption binder.
All clauses must produce the handler's declared output type and a compatible
outer effect row. A handler may change the result type and may introduce outer
effects.

Omitting `resume` aborts the captured remainder and the clause result becomes
the result of the complete `handle` expression. Version 0.5 defines this
control transfer but makes no cleanup, finalization, cancellation, or resource
unwinding promise; those are G080 rather than implicit behavior.

## Affine resumption form

The only invocation form is:

```text
resume continuation with reply
```

A resumption may be used zero or one time. It is a clause-scoped control
binder, not a function value. It MUST NOT be returned, stored, placed in data,
captured by a nested function, passed as an argument, generalized, sent to a
process, or referenced outside its operation clause.

Surface checking rejects statically visible duplicate use. Typed core records
creation, single consumption, or abandonment and independently rejects escape
or multiple-use paths. The BEAM implementation also attaches a consumed token
and traps before a second invocation can execute user code. This defense does
not turn resumptions into shareable runtime values.

## Evaluation observations

Request arguments, handler arguments, return clauses, operation clauses, and
resumed computation prefixes obey ordinary left-to-right call-by-value order.
A clause that aborts performs no action from the discarded remainder. A deep
resume runs that remainder exactly once from the request point and later
matching requests use the reinstalled handler.

## Connections

The distinctions among deep, shallow, affine, and multi-shot control are
developed with primary-source links in
[Algebraic Effects and Handlers](../../20-notes/algebraic-effects-and-handlers.md).
