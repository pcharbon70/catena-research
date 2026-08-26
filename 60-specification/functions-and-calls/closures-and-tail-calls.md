---
title: "Closures and Tail Calls"
kind: specification
created: "2026-08-25"
status: normative
spec_version: "0.1.28"
tags:
  - functions
  - specification
  - closures
  - tail-calls
aliases:
  - "Catena closure and tail-call contract"
---

# Closures and Tail Calls

## Status and authority

This chapter is the normative Catena 0.1.28 closure and tail-call
contract. It is governed by
[Specification Authority](../../SPECIFICATION-AUTHORITY.md),
[Catena Conformance Vocabulary](../../CONFORMANCE-VOCABULARY.md), and
[Catena Implementation Limits and Portability](../../IMPLEMENTATION-LIMITS.md).
It elevates, without amending, the closure and tail rules of
[Sequential Dynamics](../formal-semantic-kernel/sequential-dynamics.md)
and the tail preservation of
[BEAM Diagnostics and Conformance](../formal-semantic-kernel/beam-diagnostics-and-conformance.md),
over the binding discipline of
[Binding Structure and Scope](../bindings-and-sequencing/binding-structure-and-scope.md).

The rules apply only to source-language revision `0.1.28`. They do not
reinterpret retained manifests, interfaces, artifacts, or signed formats,
and they change no 0.1.8 kernel rule.

## Closure capture

A closure captures its defining environment by value (`FC-OBL-004`):

> **Normative definition.**

```text
closure = ( parameter , body , environment )
```

- Capture is **lexical**: the environment is the one where the `fn`
  evaluates, per C031's sequential-lexical scope.
- Capture is **immutable**: captured bindings are values and cannot
  change; a closure applied twice observes the same captured values.
- Allocation identity — whether two evaluations of the same `fn`
  produce distinguishable closures — is **not** a compatibility or
  semantics surface here; it remains G037's observability exclusion
  (`FC-OBL-008`).

## The local-function form

The local function **is** the let-bound closure (`FC-OBL-005`):

> **Normative definition.**

```text
let f = fn (x) -> body ; rest
```

- `f` binds the closure value with all of C031's rules: non-recursive
  (the `fn` cannot see `f`), silently shadowing, valid when unused
  (`BS001` applies as to any binder).
- The bound closure is first-class: passable, returnable, storable.
- No separate local-function form exists; any future local-recursion
  form enters through the edition-record gate C029 fixed, not by
  amending C031's boundary.

## Proper tail calls

The kernel guarantee, elevated verbatim (`FC-OBL-006`):

> **Normative definition.**

```text
A call in tail position MUST NOT cause unbounded growth of the
Catena call stack.
```

Tail position includes: a call that is immediately a definition's
result; a call after pattern or handler selection commits to its
clause body; and a process loop's call after receive. Both lowering
paths preserve proper tail position, as
[BEAM Diagnostics and Conformance](../formal-semantic-kernel/beam-diagnostics-and-conformance.md)
fixes; an implementation whose compiled code grows the stack on a
tail-recursive definition is nonconformant.

## Determinism

Equal applications under equal environments produce equal values and
traces; the model is deterministic on every target (`FC-OBL-008`).

## Deliberately separate work

Termination beyond the tail guarantee remains P034's. Closure
allocation observability remains G037's. Process-entry tails beyond
C010's clause remain G084's. Stack-frame shape outside proper tail
calls remains the kernel's own exclusion.

## Rationale and evidence (non-normative)

The [functions synthesis](../../20-notes/catena-functions-and-calls.md)
records why the tail witness runs one million match-dispatched
iterations on compiled BEAM — the guarantee's strongest clause, where
any per-call stack retention exhausts the machine — with the stepper
witnessing termination at moderate depth. The [topic
map](../../10-maps/functions-and-calls.md) routes the decision.
