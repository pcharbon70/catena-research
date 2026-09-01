---
title: "The Resolution Invariant"
kind: specification
created: "2026-09-01"
status: normative
spec_version: "0.1.42"
tags:
  - name-resolution
  - type-system
  - specification
aliases:
  - "Catena resolution invariant"
---

# The Resolution Invariant

## Status and authority

This chapter is the normative Catena 0.1.42 name-resolution
invariant. It is governed by
[Specification Authority](../../SPECIFICATION-AUTHORITY.md),
[Catena Conformance Vocabulary](../../CONFORMANCE-VOCABULARY.md), and
[Catena Implementation Limits and Portability](../../IMPLEMENTATION-LIMITS.md).
It states the roof over four standing pillars: the scope-structural
resolution of C021, the no-adaptation clause of
[Numeric Types and Literal Typing](../numeric-literal-semantics/numeric-types-and-literal-typing.md),
the instance-level ambiguity rejection of
[Declarations, Instances, and Coherence](../traits-and-categorical-operations/declarations-instances-and-coherence.md),
and the closed-set instantiation of
[The Closed-Set Instantiation Rule](../numeric-relationships/the-closed-set-instantiation-rule.md).

The rules apply only to source-language revision `0.1.42`. They do
not reinterpret retained manifests, interfaces, artifacts, or
signed formats.

## The invariant

> **Normative definition.**

Name resolution is **type-independent** (`RN-OBL-002`): every
written name denotes exactly one declaration, chosen as a function
of scope structure alone (C021's model, unchanged). Adding,
removing, or changing a type annotation MUST NOT change which
declaration a name denotes (`RN-OBL-002`). Resolution results
MUST NOT depend on elaboration order, expected types, or any
information other than the scope structure (`RN-OBL-002`).

## The five-way classification

> **Normative definition.**

| Kind | Classification |
| --- | --- |
| Field labels | **not resolved names** — `select r l` is a typed operation over records (C041); the label's presence is well-typedness, not a choice among candidate declarations (`RN-OBL-003`) |
| Trait method names | **names resolve by scope** exactly as value names; which instance dictionary runs is **evidence selection** over the resolved name, governed by C065's coherence, termination, and instance-level ambiguity rejection — never deferred to a call site (`RN-OBL-004`) |
| Constructors | **declaration-scoped by visibility** (C002/C023): qualified references resolve by declaration and export mode, never by type (`RN-OBL-003`) |
| Literals | **self-describing by spelling** (C017/C018): a token's meaning is fixed by its components; no expected-type adaptation exists (`RN-OBL-003`) |
| Operators | **closed-set instantiation** (C061): one typing rule per operator; no candidate list exists and no name choice is made (`RN-OBL-003`) |

## The evidence-selection carve-out

> **Normative definition.**

Evidence selection is not name resolution (`RN-OBL-004`): it
chooses which instance dictionary executes an already-resolved
method name, cannot rename or shadow anything, and settles at the
instance under coherence with ambiguity rejected there (C065,
`TRT004`). An implementation MUST NOT defer evidence ambiguity to
a call site or resolve it by expected types (`RN-OBL-004`).

## Rationale and evidence (non-normative)

The [name-resolution synthesis](../../20-notes/catena-name-resolution.md)
argues the roof-over-pillars reading and why the carve-out has
teeth. The [resolved
inquiry](../../40-inquiries/may-name-resolution-depend-on-inferred-types.md)
preserves the decision route.
