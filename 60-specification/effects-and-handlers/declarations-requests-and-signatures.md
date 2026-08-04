---
title: "Effect Declarations, Requests, and Signatures"
kind: specification
created: "2026-08-02"
status: normative
spec_version: "0.5"
tags:
  - algebraic-effects
  - effect-handlers
  - specification
  - type-inference
aliases:
  - "Catena 0.5 effect surface"
---

# Effect Declarations, Requests, and Signatures

## Nominal declarations

An effect declaration introduces one origin-qualified family identity, zero or
more `Type` parameters, and one or more uniquely named operations. An operation
uses an ordinary ordered parameter list and one reply type:

> **Normative definition.**

```text
effect Prompt {
  ask(message: Text, validate: Text -> Bool) -> Text
}
```

Parameter expressions evaluate left to right before the request transfers
control. Operation parameter and reply types MAY contain data and functions
whose latent effect row is syntactically closed and empty. They MUST NOT
contain an effectful function, an open effect-row function, a capability, a
handler, or a resumption. A pure function value does not make the operation a
scoped or higher-order effect.

Effect parameters and operation types must be well kinded. Duplicate family,
operation, parameter, or exported names are invalid. Public identity is the
declaring package origin plus family name; operation names are local to that
identity.

## Request sites

The public forms are:

> **Normative definition.**

```text
request ask("Name?", nonempty)
request console.ask("Name?", nonempty)
```

The unqualified form resolves by operation name, expected family arguments,
and lexical capability scope. It is valid only with exactly one compatible
capability. The qualified form selects the named capability and is mandatory
when two compatible capabilities are visible. Lexical nesting MUST NOT break
such a tie.

A request expression has the operation reply type. Its evaluation effect adds
the selected capability identity once, regardless of how many paths or sites
request it. Selection is recorded explicitly in typed core; runtime lookup by
nearest family or operation label is forbidden.

## Function signatures

`uses` is the only public effect annotation word:

> **Normative definition.**

```text
lookup : Key -> Value uses Store[Key, Value]
copy : Key -> Value uses source: Store[Key, Value], target: Store[Key, Value]
```

An unnamed entry requires a unique compatible ambient capability at each call.
A named entry binds a capability parameter usable in the function body and
allows repeated uses of one family. Inferred private signatures normalize to
the same representation. Public definitions MUST write their `uses` entries;
an empty list states a closed pure boundary.

Version 0.5 attaches latent effects only to named definition signatures.
Anonymous function bodies therefore MUST have a closed empty latent effect
row. An anonymous function that captures a request is rejected with `CPS001`;
one that would carry a freshly handled capability out of its `handle` is
rejected with `EFX003`. Effect-bearing anonymous arrows and higher-rank effect
polymorphism require a later specification rather than an implicit calling
convention.

The body effect must be equal to, or be made equal by local handlers to, the
declared row. A declaration may not hide an escaping request, add an unused
abstract capability occurrence, or quantify a capability that escapes in its
value result.

## Named handlers

A handler declaration is module level, has a stable origin-qualified name,
may take ordinary value parameters, names exactly one effect family
instantiation, and declares handled input and output types. Public handlers are
exported through module interfaces. A handler name is not a value: it cannot
be passed, stored, returned, pattern matched, or selected dynamically.

Every handler MUST contain exactly one return clause and exactly one operation
clause for every operation in the selected family. Extra, missing, or duplicate
clauses are invalid. Handler value parameters evaluate left to right before
the fresh lexical capability is installed.

A handler may declare an outer `uses` row. Each return or operation clause may
use a subset of that row, while the union of all clause rows MUST equal the
declaration. This permits an operation clause to request an outer capability
without requiring an unreachable return path to perform the same request.

The application form is:

> **Normative definition.**

```text
handle expression using Handler(arguments) as capability
```

`as capability` may be omitted, producing an unnameable capability that still
participates in unique inference. A written binder is scoped only over the
handled expression, not over handler arguments or the handler's own clauses.

## Connections (non-normative)

The first-order boundary and public vocabulary specialize the research in
[Algebraic Effects and Handlers](../../20-notes/algebraic-effects-and-handlers.md)
and the separate
[approachable-vocabulary inquiry](../../40-inquiries/how-should-catena-expose-mathematical-structure-without-mathematical-jargon.md).
