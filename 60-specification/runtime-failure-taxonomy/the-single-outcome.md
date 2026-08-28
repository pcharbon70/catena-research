---
title: "The Single Outcome"
kind: specification
created: "2026-08-26"
status: normative
spec_version: "0.1.32"
tags:
  - failure
  - traps
  - specification
aliases:
  - "Catena single failure outcome"
---

# The Single Outcome

## Status and authority

This chapter is the normative Catena 0.1.32 single-outcome contract.
It is governed by
[Specification Authority](../../SPECIFICATION-AUTHORITY.md),
[Catena Conformance Vocabulary](../../CONFORMANCE-VOCABULARY.md), and
[Catena Implementation Limits and Portability](../../IMPLEMENTATION-LIMITS.md).
It elevates, without amending, the trap rules of
[Actors, Messages, and Failures](../formal-semantic-kernel/actors-messages-and-failures.md),
the terminal contract of
[Strictness and Terminal Outcomes](../values-and-evaluation/strictness-and-terminal-outcomes.md),
and the handler boundary of
[Deep Handlers and Affine Resumptions](../effects-and-handlers/deep-handlers-and-affine-resumptions.md).

The rules apply only to source-language revision `0.1.32`. They do not
reinterpret retained manifests, interfaces, artifacts, or signed formats.

## The one outcome

> **Normative definition.**

```text
outcome ::= value | trap ( reason )
```

Runtime failure is `trap(reason)` — **the single** abnormal outcome
(`FT-OBL-002`). A `reason` is an ordinary value; its identity follows
the value semantics of its own type. No second outcome class exists
at 0.1.32, and none may arrive except through an explicit later
semantic revision amending this chapter — the entry rule in
[The Six Categories](the-six-categories.md) classifies every arriving
failure kind as `trap(reason)`.

The three-way partition holds at the language level (`FT-OBL-002`):

| State | Meaning |
| --- | --- |
| value | normal termination |
| trap(reason) | runtime failure |
| running | divergence — C034's non-termination, explicitly outside this taxonomy |

## Trap observability

The kernel's side-effect rules, elevated verbatim (`FT-OBL-003`):

> **Normative definition.**

A process reaching `trap(reason)` terminates abnormally and:

- **discards its mailbox** — unread messages are gone;
- **sends no exit signal** — neither termination nor abnormality
  notifies the spawner or any other process;
- **affects no spawner** — the trapping process's fate changes no
  other process's state or outcome;
- **is unobservable through Catena handles** — no handle operation
  reveals the trap; and
- **cannot be intercepted** — no handler resumes from a trap and no
  match catches it (C005/C010).

The external conformance harness MAY record return and trap labels;
that recording is outside program semantics.

## Reason identity

The reason value's identity is stable per evaluation: equal trapping
evaluations carry equal reasons, on every conforming target
(`FT-OBL-004`). Reference and compiled machines agree on the reason
value itself, not merely on trapping.

## Deliberately separate work

The terminal contract remains C029's; divergence remains C034's;
handler semantics remain C005's. Exit signals, links, and monitors
remain G084's — their arrival composes with the unmodified trap
outcome rather than extending it. Cancellation remains G088's —
distinct from failure. Allocation observability of failure paths
remains G037's.

## Rationale and evidence (non-normative)

The [failure synthesis](../../20-notes/catena-runtime-failure-taxonomy.md)
records why one outcome is forced (four frozen areas already fix it)
and why reason identity, not merely trap occurrence, is the
executable claim. The [resolved
inquiry](../../40-inquiries/what-counts-as-runtime-failure.md) and
[topic map](../../10-maps/runtime-failure-taxonomy.md) preserve the
decision route.
