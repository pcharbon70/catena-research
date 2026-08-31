---
title: "How Do Collections Construct and Update?"
kind: inquiry
created: "2026-08-31"
status: resolved
tags:
  - catena
  - collections
  - lists
  - language-design
aliases:
  - "G042 collection operations inquiry"
---

# How Do Collections Construct and Update?

## Purpose

G042 asks the checklist question: "Define persistent update, duplicate
map keys, ordering, key equality, bounds failures, and complexity
promises." C040 classified collections as library territory (G101
nominal ADTs) and C041 distinguished records from collections while
deferring here. This inquiry resolves the six topics with the
decision-not-design pattern the era established.

## Operational definitions

- **Collection** — a nominal ADT holding multiple elements (List,
  Map, Set), declared as any datatype, per C040's classification.
- **Persistent update** — producing a new collection value sharing
  no observable state with the old (C037 makes sharing invisible,
  so "persistent" is the only kind of update there is).
- **Miss** — a lookup finding no value.

## Hypotheses

1. A new area `collection-construction-and-update` at `0.1.37`
   (code `CO`) carries the contract, completing the Section 5
   decision trilogy. *(Recommended: one-version-per-area.)*
2. **Decision + routing per topic**: persistent update IS ordinary
   constructor application and match-based recursion (expressible
   today, witnessed); duplicate map keys are a G101 declaration
   question with the language fixing only explicitness; ordering and
   key equality ride C035's comparable set; bounds failures classify
   per G036; complexity gets its own exclusion.
3. **Bounds failures are typed failure as a value**: a lookup miss
   is a domain answer (Option-style), never a trap — collections
   stay total; the concrete miss type is the declaring library's
   (G101/G105).
4. **Complexity promises are excluded from the language layer**:
   representation is invisible (C037), collections are libraries
   over invisible representations, and a language-level complexity
   promise would make representation observable (amending C037,
   narrowing C002). Complexity documentation is G101's library-level
   contract.
5. The deliverable is nominal-ADT witnesses with zero new
   diagnostic families: a declared List exercised end-to-end on the
   JSON-AST path, a key-equality witness, the miss-as-value witness,
   and the complexity-exclusion absence.

## Paths explored

- **Design collection syntax now** (literals, indexing, update
  operators) — rejected: P109-era surface design for types that do
  not exist; the invented-form pattern C038 rejected.
- **Trap on miss** — rejected: makes ordinary queries abnormal
  terminations, contradicting G036's typed-failure classification.
- **Promise complexity now** — rejected: makes representation
  observable, amending C037.
- **Defer silently (complexity or bounds)** — rejected: leaves the
  checklist's explicit clauses unanswered.
- **Routing table without per-topic rows / collection built-ins /
  normative-only** — rejected patterns.

## Findings

All five hypotheses held; the developer chose the recommended option
on every fork (five of five, no overrides). The trilogy's shape
confirmed: C040 decided which types exist, C041 stated the
structural operations, and C042 decides how collections behave —
each with shipped machinery and named owners, none with invented
forms.

## Outcome

Resolved as C042 at revision `0.1.37`: the contract lives in the
[Collection Construction and Update Specification](../60-specification/collection-construction-and-update/README.md),
the
reasoning in
[Catena Collection Operations](../20-notes/catena-collection-operations.md),
and the forks in the [design decision
register](../20-notes/design-decision-register.md). G101 collection
declarations, G105 miss types and libraries, P109 spellings, and
C040/C041's classifications remain with their owners.
