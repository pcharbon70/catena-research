---
title: "Effect Diagnostics and Conformance"
kind: specification
created: "2026-08-02"
status: normative
spec_version: "0.1.5"
tags:
  - algebraic-effects
  - compilers
  - effect-handlers
  - specification
aliases:
  - "Catena 0.1.5 effect conformance"
---

# Effect Diagnostics and Conformance

## Stable diagnostics

Version 0.1.5 reserves these families:

| ID | Meaning |
| --- | --- |
| `EFX001` | malformed, duplicate, unknown, or ill-kinded effect or operation declaration |
| `EFX002` | effectful or open function type in a first-order operation |
| `EFX003` | invalid, hidden, or escaping `uses` row or capability variable |
| `EFX004` | no compatible lexical capability for a request |
| `EFX005` | ambiguous request with multiple compatible capabilities |
| `EFX006` | malformed handler, missing return, or missing, duplicate, or extra operation clause |
| `EFX007` | request, handler argument, return, reply, or clause type mismatch |
| `EFX008` | effect-row union, unification, subtraction, or residual mismatch |
| `RES001` | unknown, escaping, stored, generalized, captured, or otherwise invalid resumption |
| `RES002` | affine resumption used more than once statically or dynamically |
| `CPS001` | invalid effect-directed CPS evidence or direct/CPS boundary |

Diagnostics for EFX004 and EFX005 identify the family, operation, requested
type arguments, and zero or all candidate capability binders. EFX008 prints
the normalized declared, inferred, handled, and residual rows as applicable.

## Positive corpus

Conformance requires:

- nominal generic and nongeneric families with multi-parameter operations;
- data and closed pure-function operation parameters;
- unique unqualified and explicit qualified request selection;
- two capabilities of one family remaining distinct in a row;
- repeated requests through one capability coalescing;
- named and unnamed `uses` entries plus an open row tail;
- public and private named handlers with complete clauses;
- normal return, abort, one resume, repeated deep requests, and unrelated
  forwarding;
- two nested handlers of different families and two of one family;
- observable handler-order reversal;
- clause-introduced outer effects and exact selected-identity subtraction;
- reference/BEAM trace agreement;
- a dynamic consumed-token double-resume trap before duplicated user action;
- version 0.1.5 interface round trips, cross-module public-handler execution,
  and 0.1.2–0.1.4 compatibility; and
- pure C001–C004 functions remaining on the direct lowering path.

## Negative corpus

Conformance rejects malformed declarations, duplicate identities or clauses,
unknown operations, wrong arity and types, effectful or open operation
functions, missing and ambiguous capabilities, a qualifier of the wrong
family, hidden effects, bad residual rows, capability escape, missing return,
incomplete handlers, mismatched clause outputs, ordinary calls to resumptions,
storage or closure capture of a resumption, effectful anonymous functions,
static double resume, forged core evidence, and malformed interfaces.

G080, G081, G082, and D083 remain explicit gaps or deferrals; absence of their
features is not a negative conformance failure for 0.1.5.

## Differential traces and compatibility

The reference evaluator and BEAM output must agree on returned values and
ordered events for unique selection, explicit selection, forwarding, nested
handlers, deep resume, abort, clause requests, and handler-order reversal.
Generated forms must show CPS workers only where effect control requires them.
The complete C001–C005 suite remains green with warnings treated as errors.

## Conformance identity (non-normative)

The C005 semantic boundary was promoted after immutable sibling-compiler commit
[`b24e58d587c830dbb9d8c87770105714745fcd1b`](https://github.com/pcharbon70/catena/commit/b24e58d587c830dbb9d8c87770105714745fcd1b)
passed:

> **Non-normative evidence.**

```bash
mix format --check-formatted
mix clean
mix compile --warnings-as-errors
mix test
mix escript.build
git diff --check
```

The [C005 conformance journal](../../50-journal/2026-08-03-c005-executable-effect-conformance.md)
records the environment, results, focused trace cases, authorization, and
compiler identity. C005, C076, and C079 name the resulting completed checklist
boundaries. [Compiler PR #67](https://github.com/pcharbon70/catena/pull/67)
publishes that identity; its later merge metadata must be added without
replacing it. The wider effect inquiry remains open because resources,
exceptions, host effects, scoped control, performance, and usability exceed
0.1.5.

That immutable commit used the retired `0.1` through `0.5` protocol
identifiers. It does not establish the exact `0.1.1` through `0.1.5` strings.
The [prototype-slice renumbering record](../../50-journal/2026-08-04-prototype-slice-renumbering.md)
requires fresh cross-slice evidence before the renumbered executable identity
is published.

## Connections (non-normative)

The bounded promotion rule follows the archive's
[specification lifecycle](../README.md) and the falsification program in the
[effect inquiry](../../40-inquiries/which-algebraic-effect-semantics-should-catena-adopt.md).
