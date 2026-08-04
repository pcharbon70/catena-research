---
title: "Effect Typed Core, CPS, and BEAM"
kind: specification
created: "2026-08-02"
status: normative
spec_version: "0.1.5"
tags:
  - algebraic-effects
  - beam-vm
  - compilers
  - effect-handlers
  - specification
aliases:
  - "Catena 0.1.5 effect lowering"
---

# Effect Typed Core, CPS, and BEAM

## Explicit typed core

Accepted 0.1.5 input elaborates every implicit choice into core records:

> **Normative definition.**

```text
capability c : Family[types] in computation
request c operation evaluated_arguments
handle c handler_identity handler_arguments computation
resume_once token continuation reply
abandon token
```

Every node carries its value type, normalized evaluation row, source path, and
nominal identities. Handler declarations carry their complete operation table,
input and output types, clause effects, visibility, and origin. A capability
selected by unique inference is no less explicit in core than a written one.

An inference-independent verifier MUST recheck request arity and types,
capability selection, row union and exact subtraction, complete clauses,
handler result agreement, deep-resumption metadata, affine use, non-escape,
and declaration identity. Backend lowering accepts only verified core.

## Reference semantics

The reference evaluator represents a computation as either a returned value or
a request containing family identity, capability identity, operation,
arguments, and a single-use continuation. Handlers fold this request form,
forward unrelated identities, and reinstall themselves around a resumed
remainder. Traces expose selection, forwarding, clause entry, resume, abort,
and return.

This evaluator MUST materialize and fold the free-request form independently;
calling the production handler-dispatch helper from both evaluators is not
differential evidence. The two paths may share the defensive affine-token
primitive and trace recorder, but not handler selection or forwarding logic.

The reference model is executable evidence, not the required production
representation. Its observations must agree with compiled BEAM for the bounded
conformance corpus.

## Effect-directed CPS

Version 0.1.5 uses effect-directed CPS for definitions whose bodies contain a
request, handler, or resume boundary or whose `uses` row is nonempty. Their
workers receive explicit lexical handler state and a continuation. Requests
become statically identity-keyed dispatch; deep resumptions close over the
current handler state; handler clauses run with the saved outer state.

Definitions proven pure and containing no effect-control form retain the 0.1.4
direct calling convention and ordinary direct Erlang Abstract Format. A pure
caller may call a locally handling exported function through its direct wrapper.
The implementation MUST demonstrate that adding 0.1.5 support does not CPS
translate unrelated C001–C004 definitions.

An effectful named definition lowers to an ordinary direct wrapper plus a
private worker that receives lexical handler state and a continuation. Calls
rebind each abstract signature capability to the statically selected caller
identity before entering the worker. Anonymous effectful functions are outside
0.1.5 as specified by the surface chapter, so the worker ABI never becomes an
untyped first-class closure convention.

The affine consumed token is allocated only when a request captures a
resumption. Token comparison must happen before entering the captured
continuation. Helper closure is emitted or linked deterministically; no runtime
family-label search or reflective handler dictionary is source observable.

## BEAM boundary and interfaces

Both direct and CPS forms lower to Erlang Abstract Format and use OTP 29
`compile:noenv_forms/2`. The compiler remains Elixir and targets only BEAM. It
MUST NOT introduce Rust, a Python compiler component, Core Erlang as a
normative interchange, direct BEAM assembly, or another target VM.

Module interfaces version 0.1.5 carry public effect families, operations, named
handlers, normalized `uses` rows, origin identities, and the 0.1.4 categorical
payload. Interface decoding retains versions 0.1.2 through 0.1.4. Imported handler
and effect identities are verified before lowering.

A public handler additionally receives two deterministic hidden BEAM entry
points in its declaring module: one constructs its operation dispatcher from
ordinary handler arguments and outer handler state, and one evaluates its
return clause. These entry points are compiler ABI, not Catena values; source
code cannot call, store, inspect, or dynamically choose them. An importing
module derives them only from a digest-verified handler interface and retains
the same static capability rebinding and typed-core checks as a local handler.

## Connections (non-normative)

The BEAM route extends the normative
[typed-core boundary](../type-system/typed-core-elaboration.md) and the
implementation comparison in
[Algebraic Effects and Handlers](../../20-notes/algebraic-effects-and-handlers.md).
