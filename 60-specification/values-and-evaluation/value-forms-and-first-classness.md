---
title: "Value Forms and First-Classness"
kind: specification
created: "2026-08-24"
status: normative
spec_version: "0.1.25"
tags:
  - values
  - specification
aliases:
  - "Catena value grammar"
---

# Value Forms and First-Classness

## Status and authority

This chapter is the normative Catena 0.1.25 value-grammar and
first-classness contract. It is governed by
[Specification Authority](../../SPECIFICATION-AUTHORITY.md),
[Catena Conformance Vocabulary](../../CONFORMANCE-VOCABULARY.md), and
[Catena Implementation Limits and Portability](../../IMPLEMENTATION-LIMITS.md).
It elevates, without amending, the value rules of
[Sequential Dynamics](../formal-semantic-kernel/sequential-dynamics.md)
and admits the Float of
[Numeric Literal Semantics](../numeric-literal-semantics/README.md).

The rules apply only to source-language revision `0.1.25`. They do not
reinterpret retained manifests, interfaces, artifacts, or signed formats,
and they change no 0.1.8 kernel rule.

## The value grammar

Values are exactly the following closed set of forms
(`VA-OBL-002`, `VA-OBL-003`):

> **Normative definition.**

```text
value ::= integer | boolean | unit | float
        | tuple { value }          -- every field is a value
        | closure                  -- code with its environment
        | constructor-value        -- nominal, fully applied
        | record { value }         -- finite label-to-value map
        | injection ( label , value )
        | process-handle           -- opaque process identity
```

- The nine kernel forms are fixed by
  [Sequential Dynamics](../formal-semantic-kernel/sequential-dynamics.md)
  and restated here at the language level, unchanged.
- **Float** (`VA-OBL-003`) is the one form the kernel grammar predates:
  a finite binary64 value under C018, including signed zero, admitted
  here as the tenth value form. Nothing about C018's literal,
  rounding, or overflow rules changes.
- Structural forms close recursively: a tuple, record, or injection is
  a value exactly when every contained form is a value.

## The non-value list

The following forms exist in programs and are **never** values
(`VA-OBL-002`):

> **Normative definition.**

```text
non-value ::= evidence | handler-declaration | capability-name
            | resumption | trap | effect-row | signature
```

Evidence, handler declarations, capability names, and traps are the
kernel's non-values carried up unchanged. Resumptions are runnable
affine state under
[Deep Handlers and Affine Resumptions](../effects-and-handlers/deep-handlers-and-affine-resumptions.md)
— classifying a one-shot continuation as data would make an affine
resource copyable. Effect rows and signatures are static descriptions,
not program data. This list is closed in the same sense as the value
list: a future form enters it explicitly through its own slice.

## First-classness

Every value is uniformly first-class (`VA-OBL-004`): it MAY be bound
to a name, passed as an argument, returned as a result, and stored in
any value container. No tier, restriction, or per-type second class
exists at this revision.

Exclusions are named, not tiered (`VA-OBL-008`): what storing a
process handle lets a program observe belongs to G037 (allocation
observability) and G085 (message semantics); whether and how values
compare belongs to P035; how values render belongs to G110/G118.
Nothing here pre-decides those owners' answers.

## Future types

A future type — string, binary, list, map, set, or any G040 built-in —
enters the language **with its value status declared in its own
normative slice** (`VA-OBL-005`). Value membership never widens
silently: a form not in the closed grammar is not a value until a
revision says so, exactly as Float waited for this one.

## Deliberately separate work

Per-form evaluation order remains P030's. Bindings, calls, and
branching remain G031–G033's. Equality and ordering remain P035's. The
failure taxonomy beyond traps remains G036's. Allocation observability
remains G037's. Compile-time evaluation remains G038's. Surface
syntax remains P109's.

## Rationale and evidence (non-normative)

The [values synthesis](../../20-notes/catena-values-and-evaluation.md)
records why a closed grammar was selected over open canonical forms,
why uniform first-classness defers observability to G037/G085, and why
Float is the tenth form. The [resolved
inquiry](../../40-inquiries/what-are-catenas-values-and-strictness.md)
and [topic map](../../10-maps/values-and-evaluation.md) preserve the
decision route.
