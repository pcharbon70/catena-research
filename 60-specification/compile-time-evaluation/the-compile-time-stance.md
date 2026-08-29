---
title: "The Compile-Time Stance"
kind: specification
created: "2026-08-26"
status: candidate
spec_version: "0.1.34"
tags:
  - compile-time-evaluation
  - specification
aliases:
  - "Catena compile-time stance"
---

# The Compile-Time Stance

## Status and authority

This chapter is the normative Catena 0.1.34 compile-time stance. It
is governed by
[Specification Authority](../../SPECIFICATION-AUTHORITY.md),
[Catena Conformance Vocabulary](../../CONFORMANCE-VOCABULARY.md), and
[Catena Implementation Limits and Portability](../../IMPLEMENTATION-LIMITS.md).
It inherits, without amending, the gate of
[The Separation Table](../recursion-and-termination/the-separation-table.md)
and classifies the derivation engines of
[Data and Patterns](../data-and-patterns/README.md) and
[Traits](../traits-and-categorical-operations/README.md).

The rules apply only to source-language revision `0.1.34`. They do not
reinterpret retained manifests, interfaces, artifacts, or signed formats.

## The decision

The checklist's four forms classify as (`CE-OBL-002`):

> **Normative definition.**

| Form | Decision at 0.1.34 |
| --- | --- |
| Constants | **never execute** — definitions compile; they are not run at compile time |
| Attributes | **no attribute system exists** |
| Macros | **no macro system exists** |
| Generated derivations | **compiler-internal generation** — no user code executes ([below](#generated-derivations)) |

No constant-folding, attribute-evaluation, or macro-expansion
evaluator exists, and none may arrive except through a slice that
ships its own totality-or-boundedness regime per the gate
(`CE-OBL-003`) — inherited verbatim from C034: total-or-bounded in
the admitting change; no unbounded arrival, ever; never as a
compatible addition. An implementation MUST NOT use this area's
boundary to claim a const-eval, macro, or attribute evaluator.

## Generated derivations

The shipped derivation engines — datatype folds
([C002](../data-and-patterns/README.md)) and capability helpers
([C004](../traits-and-categorical-operations/README.md)) — classify
as **compiler-internal generation, not execution** (`CE-OBL-004`):

- The engine is a total function from finite datatype declarations
  to typed-core definitions, by structural recursion over the
  declarations; it evaluates no user expression and invokes no
  evaluator.
- Every derived definition carries `compiler_derived` provenance and
  the generated marker; its scheme is checked, verified, and erased
  like any handwritten definition's.
- Generation is deterministic: equal declarations produce equal
  derived definitions and byte-identical binaries.
- A future derivation that *evaluates user code* — a
  derive-that-checks-a-law — is a new evaluator under the gate, in
  its own slice; it is not an extension of today's generation.

## Deliberately separate work

Spellings for any future const/macro/attribute surface remain
P109's; deriving extensions remain G040's, classified under this
area's rules on arrival; code-generation programs remain G005/G116's;
build tooling remains G121's.

## Rationale and evidence (non-normative)

The [compile-time synthesis](../../20-notes/catena-compile-time-evaluation.md)
records why the answer is a decision, not a design (nothing exists to
design; meanings attach to forms, and no forms exist), and why
derivations are generation rather than execution. The [resolved
inquiry](../../40-inquiries/what-executes-during-compilation.md) and
[topic map](../../10-maps/compile-time-evaluation.md) preserve the
decision route.
