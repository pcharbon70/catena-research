---
title: "The Twelve-Way Classification"
kind: specification
created: "2026-08-29"
status: candidate
spec_version: "0.1.35"
tags:
  - data-model
  - specification
aliases:
  - "Catena type classification"
---

# The Twelve-Way Classification

## Status and authority

This chapter is the normative Catena 0.1.35 type-classification
contract. It is governed by
[Specification Authority](../../SPECIFICATION-AUTHORITY.md),
[Catena Conformance Vocabulary](../../CONFORMANCE-VOCABULARY.md), and
[Catena Implementation Limits and Portability](../../IMPLEMENTATION-LIMITS.md).
It executes the entry rules of
[Value Forms and First-Classness](../values-and-evaluation/value-forms-and-first-classness.md),
[The Comparable Set](../equality-and-ordering/the-comparable-set.md),
and
[Branch Rules Consolidated](../branching/branch-rules-consolidated.md),
over the scanner kinds of
[Text, Characters, and Bytes](../literal-grammar/text-characters-and-bytes.md).

The rules apply only to source-language revision `0.1.35`. They do not
reinterpret retained manifests, interfaces, artifacts, or signed formats.

## The decision

The checklist's twelve candidates classify as (`BM-OBL-002`):

> **Normative definition.**

| Type | Decision | Value status | Comparability |
| --- | --- | --- | --- |
| Unit | built-in, classified | value (C029) | non-comparable (C035, standing) |
| Bool | built-in, classified | value | comparable; not orderable |
| Int | built-in, classified | value | comparable, orderable |
| Float | built-in, classified | value | comparable, orderable (bit-exact, C035) |
| Tuple | built-in, classified | value | structural (C035) |
| Function | built-in, classified | value | never comparable |
| Process handle | built-in, classified | value | never comparable (C037) |
| Text | **built-in, elaborated now** | value (this slice) | comparable, orderable |
| Character | **built-in, elaborated now** | value (this slice) | comparable, orderable |
| Bytes | **built-in, elaborated now** | value (this slice) | comparable, orderable |
| List, map, set | **library territory** (G101) | with G101's declarations | with G101, via constructor recursion |
| Reference | **excluded** | never | never |

No shipped type's status changes: the seven classified built-ins
restate C029/C035/C037 facts in one place, exactly as C030's table
consolidated the order fragments.

## Library territory, not exclusion

List, map, and set are **not excluded from the language** — they are
excluded from the *built-in list*. A nominal ADT declaring `Nil` and
`Cons` constructors expresses a list today, with C002 constructor
patterns, C035 constructor-field comparability, and C004 derivations
already serving it; G101 declares the canonical collections on this
machinery with representation chosen by evidence. Built-in status
would buy only dedicated literal syntax — a P109-era surface — and
would pre-decide representation (`BM-OBL-005`).

## Reference excluded

No reference type exists at 0.1.35: no mutable cells, no aliasing
operations, and C037's semantic identity leaves nothing for a
reference to observe. Any arrival is G084's gated era; none may enter
as a compatible addition (`BM-OBL-005`).

## Coverage

No frontend encodes Text, Character, or Bytes literals in compiled
programs at 0.1.35, so no scrutinee of these types exists; literal-
pattern coverage entries arrive with the P109-era pattern surface,
per C033's rule (`BM-OBL-006`). This is stated absence, not omission.

## Deliberately separate work

Collection declarations remain G101's; construction and update G042's;
string libraries G105's; references G084's; spellings and the
compiled-program path P109's; numeric trait relationships G061's.

## Rationale and evidence (non-normative)

The [data-model synthesis](../../20-notes/catena-built-in-data-model.md)
records why library routing beats built-in status for collections and
why the classification rides shipped machinery. The [resolved
inquiry](../../40-inquiries/which-types-are-built-in.md) and [topic
map](../../10-maps/built-in-data-model.md) preserve the decision
route.
