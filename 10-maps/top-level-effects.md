---
title: "Top-Level Effects"
kind: map
created: "2026-09-01"
tags:
  - archive-navigation
  - effects
  - entry-points
  - catena
aliases:
  - "G082 top-level effects route"
---

# Top-Level Effects

## Purpose

This map routes the G082 question — which requests an application
entry point may leave unhandled and who interprets them — through
the archive's decision trail. The normative answer is revision
`0.1.48` in the [Top-Level Effects
Specification](../60-specification/top-level-effects/README.md).

## The route

1. **The standing answer.** [Entry
   Declarations](../60-specification/entry-points/entry-declarations.md)
   (C027) fixes effect-closed entries (`ENT001`), denies implicit
   host handlers, and names itself the 0.1.23 answer to G082.
2. **Launch as invocation.** [Startup and
   Shutdown](../60-specification/entry-points/startup-and-shutdown.md)
   — the launch root runs a total entry to completion; return is
   shutdown; no scope, no interpretation.
3. **The implicit-names pillar.** [Prelude
   Policy](../60-specification/prelude-policy/README.md) (C026) —
   nothing enters scope unasked; the capability interface's
   nearest standing analogue.
4. **The visible-boundary analogue.** [The Intralanguage
   Exclusions](../60-specification/dynamic-and-unsafe-boundaries/the-intralanguage-exclusions.md)
   (C067) — explicit, typed, failure-classified entry for anything
   foreign.
5. **The distinctness routing.** [The Mechanism
   Partition](../60-specification/exception-boundary/the-mechanism-partition.md)
   (C081) and C036 — failure interpretation is a separate concern;
   G084's supervision observes traps, never requests.
6. **The contract.** The [Top-Level Effects
   Specification](../60-specification/top-level-effects/README.md):
   the boundary statement, the G106 capability interface, the
   supervision routing, the door, and conformance.
7. **The reasoning and decision record.** [Catena Top-Level
   Effects](../20-notes/catena-top-level-effects.md) argues the
   silent top level; the [resolved
   inquiry](../40-inquiries/who-interprets-top-level-requests.md)
   preserves the forks.

## Related maps

- [Entry Points map](entry-points.md) — C027's area.
- [Exception Boundary map](exception-boundary.md) — the failure
  side kept distinct.
