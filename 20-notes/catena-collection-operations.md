---
title: "Catena Collection Operations"
kind: note
created: "2026-08-31"
maturity: developing
tags:
  - catena
  - language-design
  - collections
  - lists
aliases:
  - "Catena collection operations model"
---

# Catena Collection Operations

## Executive conclusion

Catena's collection-construction and update contract at `0.1.37` is
the Section 5 decision trilogy's capstone — six checklist topics,
each answered with shipped machinery or a named owner:

| Topic | Decision |
| --- | --- |
| Persistent update | **is** ordinary constructor application and match-based recursion — expressible today, witnessed on a declared List |
| Duplicate map keys | a **G101 declaration question**; the language fixes only that the declaring slice states its behavior explicitly |
| Ordering | rides **C035's comparable set** — element and key ordering are the entries already shipped |
| Key equality | keys must be **comparable** (C035) to be usable in equality-dependent operations |
| Bounds failures | **typed failure as a value** — a lookup miss is a domain answer (Option-style), never a trap; the concrete miss type is the declaring library's (G101/G105) |
| Complexity promises | **excluded from the language layer** — representation is invisible (C037), so a language-level complexity promise would make representation observable; complexity documentation is G101's library-level contract |

The deliverable is nominal-ADT witnesses with **zero new diagnostic
families**: a declared `List` (Nil/Cons) exercised end-to-end on the
JSON-AST path — construction, head/tail match, length by recursion,
replace-head update — agreeing on evaluator and BEAM; a key-equality
witness (a Pair-keyed ADT with comparable Int keys); the
miss-as-value witness (a lookup returning an Option-typed answer,
verified by its terminal value outcome); the complexity-exclusion
absence; determinism.

## Scope and method

The operational target is independent agreement on the six-topic
routing, the miss classification, and the complexity exclusion —
made executable through the witness set. Primary evidence is
internal: [C040's classification](../60-specification/built-in-data-model/the-twelve-way-classification.md),
[C041's records-not-collections distinction](../60-specification/structural-records-and-variants/the-operation-table.md),
[C035's comparable set](../60-specification/equality-and-ordering/the-comparable-set.md),
[C036's taxonomy](../60-specification/runtime-failure-taxonomy/the-six-categories.md),
[C037's representation invisibility](../60-specification/resource-observability/the-observability-model.md),
and C002's constructor machinery. Source claims stay distinct from
Catena proposals below.

## Relation to the current corpus

[C040](../60-specification/built-in-data-model/the-twelve-way-classification.md)
routed list/map/set to G101 as library nominal ADTs — the routing
this slice executes. Everything a collection needs already serves
nominal types: C002's constructor patterns, C035's constructor-field
comparability recursion, C004's derivations, C031's recursion, and
C032's tail calls.

[C041](../60-specification/structural-records-and-variants/the-operation-table.md)
stated the boundary this slice inherits: records are structural
maps with select/update/extend/restrict; collections are nominal
ADTs with constructors and match. "Collection construction and
update remains G042's" — this contract — "records are not
collections."

[C035](../60-specification/equality-and-ordering/the-comparable-set.md)
fixes ordering and key equality: the comparable set's structural
recursion means a declared collection's elements and keys compare
when their types compare — the constructor-field rule already
covers `Cons Int Int`. Nothing new is needed.

[C036](../60-specification/runtime-failure-taxonomy/the-six-categories.md)
classifies typed failure as a value, not a failure — the
bounds-failure answer. A miss is normal termination with a domain
answer; collections stay total; no trap path exists by design.

[C037](../60-specification/resource-observability/the-observability-model.md)
makes the complexity exclusion forced, not chosen: representation
is invisible, so any language-level complexity bound would be a
promise about an invisible thing — observable the moment a
conforming implementation chose a different representation. The
honest language contract promises values, effects, and totals;
G101's library documentation promises operations' costs, clearly
separated.

## Comparative evidence and inference

### Why update is constructor application, not an operator

A persistent update — produce a new collection from an old one — is
already the language's most ordinary computation: match the
structure, rebuild the parts that change, reuse the rest. A
dedicated update operator would be syntax for what recursion
expresses, and syntax is P109's. The witness proves the claim: a
replace-head function on a declared List, agreeing on both targets.

### Why the complexity exclusion is architecture, not neglect

The corpus chose representation invisibility deliberately (C037's
three returns), chose nominal declarations for collections (C040),
and chose representation independence for nominal data (C002). A
language complexity promise would cut across all three. Libraries
can still document costs — G101's per-operation documentation —
because a *library* fixes a representation and may talk about it;
the *language* may not.

## Selected model

> **Normative definitions (placed in the 0.1.37 chapters).**

### The six-topic routing

As the table above; each row citing its shipped machinery or named
owner.

### Miss as value

```text
lookup : key -> collection -> Option value
```

A miss is a value; no trap path; the concrete miss type is the
declaring library's.

### Complexity exclusion

No complexity bound is a language-level promise; complexity
documentation is G101's, separated from semantics.

### Rejected alternatives

As enumerated in the resolved inquiry.

## What C042 adds to the design

Section 5's decision trilogy completes (5/8): types (C040),
structural records (C041), and collection operations (C042) leave
only the pattern partials (P044, D046) and the deferrals. G101
receives its complete precondition set — what to declare, how keys
must compare, what a miss returns, where complexity lives — and
P109's grammar exercise receives the operation semantics with only
spellings left.

## Remaining questions and falsification criteria

G101 owns collection declarations, duplicate-key choices, and
complexity documentation; G105 miss-type contents and libraries;
P109 spellings; C040/C041's classifications unchanged.

The model should be revisited if G101's evidence shows recursion
inadequate for realistic updates (the remedy is a G101-era slice
adding library combinators — not language syntax), or if the runtime
era demands complexity guarantees (the remedy is a gated
representation-visible profile, never an amendment of C037).

## Connections

- The [resolved collections inquiry](../40-inquiries/how-do-collections-construct-and-update.md)
  records the question, hypotheses, and outcome.
- The [Collection Construction and Update map](../10-maps/collection-construction-and-update.md)
  routes through the trilogy and the future owners.
- The [Collection Construction and Update Specification](../60-specification/collection-construction-and-update/README.md)
  defines the normative `0.1.37`
  contract this note argues for.
- [Catena Built-In Data Model](catena-built-in-data-model.md) fixed
  the classification this executes.
- [Catena Structural Records](catena-structural-records.md) fixed
  the boundary this inherits.

## Sources

- [The Twelve-Way Classification](../60-specification/built-in-data-model/the-twelve-way-classification.md)
- [The Operation Table](../60-specification/structural-records-and-variants/the-operation-table.md)
- [The Comparable Set](../60-specification/equality-and-ordering/the-comparable-set.md)
- [The Six Categories](../60-specification/runtime-failure-taxonomy/the-six-categories.md)
- [The Observability Model](../60-specification/resource-observability/the-observability-model.md)
