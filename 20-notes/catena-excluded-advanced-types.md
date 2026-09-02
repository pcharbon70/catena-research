---
title: "Catena Excluded Advanced Types"
kind: note
created: "2026-09-01"
maturity: developing
tags:
  - catena
  - type-system
  - language-design
aliases:
  - "the advanced type exclusion gate"
---

# Catena Excluded Advanced Types

## Executive conclusion

Catena's advanced type boundary has stood complete since `0.1.1`:
C001 excludes seven forms and requires rejection to identify the
profile boundary; C068 ships the checked profile — predicative
explicit higher rank, signature-directed GADTs, branch-local
equalities, explicit rigid existentials — behind an annotation
boundary. D140's completion adds the one missing piece: the
**seven-point arrival gate** as normative text. Any future slice
admitting an excluded form must state its independent problem
statement, evidence of repeated use, interaction audit, formal
semantics, operational contract, diagnostic story, and comparison
with an ordinary library or explicit core mechanism — the
discipline remaining-areas already fixed in prose, now with a
normative home.

## Scope, method, and definitions

This note synthesizes the archive's evidence for closing D140 at
revision `0.1.44`. It reads C001's explicit-exclusions section,
C068's checked profile, and the remaining-areas advanced-features
program; it invents no mechanism and proposes no form.

## The partition that already stood

The negative side (C001): impredicative instantiation, inferred
higher rank, first-class existential packages beyond declared
constructors, general linear types, dependent types, unrestricted
type families, higher-kinded polymorphism over arbitrary kinds,
and unrestricted GADT inference are excluded — and a rejection of
one of them must identify the profile boundary, not report an
unrelated unification failure. The positive side (C068): what IS
checked, at which boundary, with which evidence. D140's five named
forms are a subset of C001's seven; the table covers all seven so
existentials and GADT inference do not wait for a second slice.

## Why a gate rather than a ban

The exclusions are not aesthetic preferences — each guards a
guarantee the corpus prices highly: principality and the rank-1
hybrid (C063), coherent evidence (C065), erasure (C006),
determinism everywhere. A future form that pays for itself with
the seven statements can arrive; one that cannot, does not. The
gate's shape comes from the advanced-features program's own
warning: these must not become "one omnibus advanced features
project" — each arrives independently or not at all.

## Tradeoffs, limitations, falsification

The gate buys honesty at the cost of ceremony: a genuinely
valuable form carries a seven-part dossier. Falsification: an
excluded form arriving without discharging the gate, or a
rejection that reports an unrelated unification failure instead of
the profile boundary, voids this contract and demands amendment.

## Route to sources

- The [Excluded Advanced Type Features Specification](../60-specification/excluded-advanced-type-features/README.md)
  defines the normative `0.1.44` contract this note argues for.
- [Advanced Type Checking](../60-specification/type-system/advanced-type-checking.md)
  — C001's explicit exclusions and the checked profile.
- [Remaining research areas](../00-inbox/remaining-catena-research-areas.md)
  — the seven-point discipline the gate adopts.
- The [resolved inquiry](../40-inquiries/how-do-the-excluded-advanced-type-forms-stay-excluded.md)
  preserves the decision route.
