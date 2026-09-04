---
title: "Who Interprets Top-Level Requests?"
kind: inquiry
created: "2026-09-01"
status: resolved
tags:
  - catena
  - effects
  - entry-points
  - language-design
aliases:
  - "G082 top-level effects inquiry"
---

# Who Interprets Top-Level Requests?

## Purpose

G082 asks the checklist question: "Define which requests an
application entry point may leave unhandled and who interprets
them." C027 already answered it in passing — the entry-declarations
chapter fixes effect-closed entries (`ENT001`), denies any implicit
host handler, and names itself "the 0.1.23 answer to the deferred
G082 question." What completion adds is the answer's own normative
home, the capability interface G106 must satisfy, and the
supervision routing that keeps failure interpretation distinct.

## Operational definitions

- **Top-level boundary** — what an application entry may leave
  unhandled when the runtime invokes it.
- **Ambient interpreter** — a runtime-provided handler for requests
  no source handler caught; C027 denies one exists.
- **Capability channel** — how an entry could ever reach host
  services; G106's to define.

## Hypotheses

1. A new area `top-level-effects` at `0.1.48` (code `TL`) carries
   the completion as a confirmation/routing slice. *(Recommended:
   the C140 shape — the smallest slice type.)*
2. **The boundary stated**: an entry leaves nothing unhandled
   (effect-closed, `ENT001`, C027 unchanged); nobody interprets
   unhandled requests because none exist — no ambient host handler
   exists or is reserved, and the launch root invokes a total entry
   to completion under unchanged kernel semantics, introducing no
   scope and interpreting nothing.
3. **The capability interface for G106**: capabilities arrive only
   as explicit typed values through a channel G106's slice defines
   and justifies — deny-able, never ambient; the zero-argument and
   effect-closed rules bind until deliberately amended; no
   host-handler concept is reserved.
4. **The supervision routing**: G084 interprets process failure
   (trap observation), never effect requests — distinct mechanism,
   distinct slice.

## Paths explored

- **Design the capability channel now** — rejected: G106's
  territory, undesigned; inventing ahead of the owner is the
  pattern C038 rejected.
- **Reserve a host handler** — rejected: C027 explicitly denies
  implicit host handlers; reserving one contradicts the standing
  answer G082 exists to state.
- **Defer** — rejected: the answer exists but unowned; G106's
  designers would meet an unstated boundary.

## Findings

All four hypotheses held; the developer chose the recommended
option on all four forks (no overrides). The decisive corpus
facts: C027's chapter already carries the rule and names G082;
C026's zero-implicit-names and C067's visible-boundary discipline
prefigure the capability interface; C036/C081 keep failure
interpretation a separate concern from effect interpretation.

## Outcome

Resolved as C082 at revision `0.1.48`: the contract lives in the
[Top-Level Effects Specification](../60-specification/top-level-effects/README.md),
the reasoning in
[Catena Top-Level Effects](../20-notes/catena-top-level-effects.md),
and the forks in the [design decision
register](../20-notes/design-decision-register.md). G106 owns the
capability channel's design; G084 owns failure interpretation;
Section 9 advances to 7/8.
