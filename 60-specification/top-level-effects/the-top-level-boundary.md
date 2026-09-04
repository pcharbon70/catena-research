---
title: "The Top-Level Boundary"
kind: specification
created: "2026-09-01"
status: normative
spec_version: "0.1.48"
tags:
  - effects
  - entry-points
  - specification
aliases:
  - "Catena top-level boundary"
---

# The Top-Level Boundary

## Status and authority

This chapter is the normative Catena 0.1.48 top-level boundary. It
is governed by
[Specification Authority](../../SPECIFICATION-AUTHORITY.md),
[Catena Conformance Vocabulary](../../CONFORMANCE-VOCABULARY.md), and
[Catena Implementation Limits and Portability](../../IMPLEMENTATION-LIMITS.md).
It elevates the standing answer of
[Entry Declarations](../entry-points/entry-declarations.md) (C027 —
whose chapter names itself "the 0.1.23 answer to the deferred G082
question") into this area's own normative home, amending nothing.

The rules apply only to source-language revision `0.1.48`. They do
not reinterpret retained manifests, interfaces, artifacts, or
signed formats.

## The boundary

> **Normative definition.**

An application entry point leaves **nothing** unhandled
(`TL-OBL-002`): the entry's recorded effect row is empty — every
request its body can perform is handled before return — or the
package is static invalidity (`ENT001`, C027 unchanged). **Nobody
interprets unhandled requests** because none exist (`TL-OBL-002`):
no ambient host handler exists, none is reserved, and the launch
root's whole behavior is to invoke a total, effect-closed entry to
completion under unchanged kernel semantics — introducing no
scope, injecting no value, and answering no request (`TL-OBL-003`).
Return is shutdown (C027, unchanged).

## The capability interface

> **Normative definition.**

Capabilities reach an entry only as **explicit typed values
through a channel G106's slice defines and justifies**
(`TL-OBL-004`): deny-able like every capability in the corpus,
never ambient, never implicit. Until that slice exists, the entry
form's zero-argument and effect-closed rules bind (`TL-OBL-004`).
An implementation MUST NOT provide, reserve, or imply a host
handler for top-level requests (`TL-OBL-005`).

## The supervision routing

> **Normative definition.**

Failure interpretation is a distinct concern: G084's supervision
observes process failure (trap identity, per C036/C081), never
effect requests (`TL-OBL-005`). A supervisor is not an
interpreter; nothing about the supervision program widens this
boundary.

## The door

> **Normative definition.**

Widening the entry form — admitting non-empty effect rows, ambient
interpretation, or parameterized launches — requires a revision
that amends C027's entry rules explicitly and states who
interprets what, with witnesses (`TL-OBL-006`).

## Rationale and evidence (non-normative)

The [synthesis](../../20-notes/catena-top-level-effects.md)
argues why the silent top level is the corpus's trajectory —
C026's zero implicit names, C067's visible boundaries, and C027's
completion rule converging — and what immediacy it trades for
total determinism at the boundary. The [resolved
inquiry](../../40-inquiries/who-interprets-top-level-requests.md)
preserves the decision route.
