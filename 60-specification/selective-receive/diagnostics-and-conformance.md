---
title: "Selective Receive Diagnostics and Conformance"
kind: specification
created: "2026-09-01"
status: candidate
spec_version: "0.1.46"
tags:
  - conformance
  - diagnostics
  - receive
  - specification
  - testing
aliases:
  - "Catena 0.1.46 receive conformance"
---

# Selective Receive Diagnostics and Conformance

## Status and authority

This chapter is the normative Catena 0.1.46 selective-receive
diagnostic, abstract frontend, and conformance contract. It is
governed by
[Specification Authority](../../SPECIFICATION-AUTHORITY.md),
[Catena Conformance Vocabulary](../../CONFORMANCE-VOCABULARY.md), and
[Catena Implementation Limits and Portability](../../IMPLEMENTATION-LIMITS.md).
It applies [The Receive Rule Set](the-receive-rule-set.md) and
[The Routed Interfaces](the-routed-interfaces.md).

## Stable diagnostics

This area introduces **zero new diagnostic families**
(`SR-OBL-001`, `SR-OBL-002`). Or-pattern receive clauses keep
`CND006`; non-portable conditions keep the C003 condition
diagnostics; a non-closed message type keeps the harness typing
diagnostics.

## Abstract public boundaries

The shipped boundaries witness the contract on existing machinery;
the bootstrap adds no new public API (`SR-OBL-001`):

- **Kernel process receive** — the `Selective`-shape process:
  guarded constructor clauses over a closed message type, running
  on the reference stepper and compiled BEAM.
- **Preservation witness** — a process sent `Some 0` then
  `Some 1` whose guarded receive (`message > 0`) selects `Some 1`
  while `Some 0` remains queued, observed through the stepper's
  exposed mailboxes.

Implementations MUST NOT use these boundaries to claim public
receive syntax on general frontends, timeout forms, protocol
typing, or send-side semantics beyond C010's standing results
(`SR-OBL-005`, `SR-OBL-006`).

## Determinism

Unchanged programs produce identical values, traces, final
mailboxes, and diagnostics on every conforming target
(`SR-OBL-002`).

## Conformance obligations

| ID | Obligation | Required executable evidence |
| --- | --- | --- |
| `SR-OBL-001` | apply receive rules only at exact 0.1.46 and register the stable lifecycle addition with zero new families and no new API | exact selection, registry, and lifecycle tests |
| `SR-OBL-002` | keep the rule set: FIFO scan, preservation, one-time removal, no hidden semantics | preservation witnesses |
| `SR-OBL-003` | keep the typing and condition rules: closed message type, effect-free form, portable conditions, `CND006` | typing and condition witnesses |
| `SR-OBL-004` | keep the starvation statement: honest cost, no fairness claim | cost-statement pinning |
| `SR-OBL-005` | keep the P109 interface with the timeout clause named as C044's explicit total fallback | routing witnesses |
| `SR-OBL-006` | keep the G088 interface: timeout evaluation, races, totality, and cancellation disposal stated as G088's obligations | routing witnesses |
| `SR-OBL-007` | keep the G087 and G085 interfaces: protocol typing composes, send-side claims stay G085's | routing witnesses |
| `SR-OBL-008` | keep the contract deterministic with the C003/C010 receive corpus unchanged | determinism and re-pin tests |

Every obligation has at least one tagged passing test. The sibling
compiler gates the complete `SR-OBL-*` set against unknown and
uncovered identifiers before C086 conformance is claimed.

## Required evidence sets

Positive evidence includes the preservation witness (selected
value and retained mailbox agreeing across stepper and BEAM); the
C010 `Selective` fixture re-pinned; and the lifecycle registration
of 0.1.46.

Negative evidence — in the definitional sense — includes
or-pattern receive clauses rejecting `CND006`; a non-closed
message type rejecting; and no public receive, timeout, or
protocol entry points existing.

Exclusion evidence demonstrates unchanged predecessor diagnostic
identities and predecessor APIs retaining their exact selections
and defaults.

## Revision and persistence separation

Revision `0.1.46` adds the rule set and the routed interfaces; it
adds no JSON AST version, kernel S-expression version, interface
version, artifact version, signature domain, typing rule, runtime
behavior, BEAM representation, manifest field, public API name, or
diagnostic family, and amends no retained revision (`SR-OBL-001`,
`SR-OBL-002`).

The source-text decoder accepts cumulative revisions `0.1.9` through
`0.1.46`; every predecessor API retains its exact selection. The next
unused semantic patch is `0.1.47`.

## Rationale and evidence (non-normative)

The design route is preserved in the
[synthesis](../../20-notes/catena-selective-receive.md), the
[resolved inquiry](../../40-inquiries/how-does-selective-receive-complete.md),
and the [topic map](../../10-maps/selective-receive.md). The C086
evidence record will preserve the sibling-compiler commands and
archive validation.
