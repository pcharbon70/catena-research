---
title: "Catena Structural Records"
kind: note
created: "2026-08-29"
maturity: developing
tags:
  - catena
  - language-design
  - records
  - variants
  - rows
aliases:
  - "Catena structural record model"
---

# Catena Structural Records

## Executive conclusion

Catena's structural records and variants at `0.1.36` are the
kernel's calculus, elevated once with the complete operation set in
one cited table. A **structural record** is a finite
unique-label-to-value map — literal, `select`, `update`, `extend`,
`restrict`. A **structural variant** is a labeled injection —
`inject` and match dispatch by semantic label. **Duplicate labels
reject** at the literal. **Written field order controls effects but
never equality or row identity** (C030's row, C037's maps). Every
missing-label operation is **statically unreachable**.

The **row typing is kernel rows verbatim**: record and variant
literals are closed rows; `extend` and `restrict` produce closed rows
over closed inputs; open tails exist only in type positions —
signatures and type variables — never from an expression; `select`
requires the label present. Row-polymorphic behavior is exactly
this: the open tail composes through type positions, and static
typing makes the missing-label cases unreachable. No new machinery,
no widening.

The **representation is semantic maps verbatim**: records are
semantic finite maps whose written order is an effect-order fact and
never an identity fact; representation — map, tuple, unboxed — is
invisible per C037; the BEAM backend rides maps as it already does.

The deliverable is kernel-path witnesses with **zero new diagnostic
families** — the C036/C037 target pair (stepper + compiled BEAM),
the fixture's full operation round-trip, duplicate-label rejection,
variant dispatch agreement, and the JSON-AST absence stated in
C040's frontend-absence pattern.

## Scope and method

The operational target is independent agreement on the operation
table, the row model, and the representation clause — made
executable through the witness set. Primary evidence is internal:
[the kernel's record and variant rules](../60-specification/formal-semantic-kernel/sequential-dynamics.md),
the C010 fixture, [C030's order rows](../60-specification/evaluation-order/ordered-forms-and-entry-rule.md),
[C037's semantic maps](../60-specification/resource-observability/the-observability-model.md),
and [C002's nominal exclusions](../60-specification/data-and-patterns/declarations-and-nominal-identity.md).
Source claims stay distinct from Catena proposals below.

## Relation to the current corpus

The [kernel](../60-specification/formal-semantic-kernel/sequential-dynamics.md)
fixes record and variant reduction — `select` extracts, `update`
replaces, `extend` adds, `restrict` removes, injection is a value,
matching tests the semantic label then the payload — frozen at
0.1.8. C041 elevates without touching it, the Section 4 pattern's
first Section 5 application.

[C002's declarations chapter](../60-specification/data-and-patterns/declarations-and-nominal-identity.md)
excluded structural ops from nominal declarations — "records do not
acquire row-polymorphic selection or update." The exclusion stays:
nominal and structural remain two deliberate forms, and this slice
classifies the structural one without merging them.

[C030](../60-specification/evaluation-order/ordered-forms-and-entry-rule.md)
schedules record fields in written order and record bases before
replacement values; [C033](../60-specification/branching/branch-rules-consolidated.md)
consolidates variant matching. This slice cites both; nothing
changes.

[C035](../60-specification/equality-and-ordering/the-comparable-set.md)
made records comparable as semantic maps — "field order never
affects equality" — and [C037](../60-specification/resource-observability/the-observability-model.md)
made record-map sharing and representation invisible. The
representation clause elevates these standing facts as the structural
contract's representation section.

[C040's frontend-absence pattern](../60-specification/built-in-data-model/text-character-and-bytes.md)
supplies the witness-honesty clause: the frozen JSON AST carries no
record or variant expression tags, so the types live at the kernel
calculus and language-rule level until a frontend encodes them —
P109's era.

## Comparative evidence and inference

### Why consolidation, not design

Every operation exists in the frozen kernel and its fixture; the
retained frontends cannot encode them; no consumer demands new
machinery. The elevation states once what seven shipped chapters
scatter, exactly as C030's table consolidated the order fragments
and C033's table the branching rules.

### Why closed literals and type-position tails

The kernel's type module carries tails for substitution — signatures
compose over records — but its expression grammar produces only
closed literals, and extend/restrict close over closed inputs. That
is the honest row-polymorphic model: polymorphism through type
positions, totality in expressions. An open-record literal would be
a new form the kernel never fixed, inventing what signatures already
provide.

## Selected model

> **Normative definitions (placed in the candidate chapters).**

### The operation table

| Operation | Rule | Home |
| --- | --- | --- |
| `record {l = v}` | closed literal; duplicate labels reject | kernel (this slice) |
| `select r l` | extracts `l`; requires present | kernel |
| `update r l v` | base then replacement value; label present | kernel/C030 |
| `extend r l v` | adds `l`; closed over closed | kernel |
| `restrict r l` | removes `l`; closed over closed | kernel |
| `inject l v` | a value; labeled payload a value | kernel |
| match on variant | semantic label, then payload | kernel/C033 |

### Row typing

Literals closed; extend/restrict closed over closed; tails in type
positions only; select requires present; missing-label operations
statically unreachable.

### Representation

Semantic maps; order is effects-only; representation invisible; BEAM
rides maps.

### Rejected alternatives

As enumerated in the resolved inquiry.

## What C041 adds to the design

Section 5's second item closes (4/8): the structural half of the
data program is stated once, G042's collection work receives a
cited predecessor (records are not collections), P109's grammar
exercise receives the operation semantics with only spellings left,
and P044's refutability question gains its record-pattern context.

## Remaining questions and falsification criteria

P109 owns spellings and the frontend path; G042 collection
construction and update; G062 aliases and newtypes; P044
refutability by context; C002 nominal declarations unchanged.

The model should be revisited if G042's maps demand record-style
literal syntax (the remedy is G042's own slice, on this table), or
if ergonomic evidence demands open-record literals (the remedy is a
gated slice extending the expression grammar — never a silent
widening).

## Connections

- The [resolved records inquiry](../40-inquiries/what-are-structural-records-and-variants.md)
  records the question, hypotheses, and outcome.
- The [Structural Records map](../10-maps/structural-records.md)
  routes through the kernel calculus, the shipped contracts, and the
  future owners.
- The Structural Records Specification (candidate, then normative at
  promotion, in `60-specification/structural-records-and-variants/`)
  will define the contract this note argues for.
- [Catena Built-In Data Model](catena-built-in-data-model.md) fixed
  the frontend-absence pattern this rides.
- [Catena Resource Observability](catena-resource-observability.md)
  fixed the semantic maps this elevates.

## Sources

- [Sequential Dynamics](../60-specification/formal-semantic-kernel/sequential-dynamics.md)
- [Declarations and Nominal Identity](../60-specification/data-and-patterns/declarations-and-nominal-identity.md)
- [Ordered Forms and Entry Rule](../60-specification/evaluation-order/ordered-forms-and-entry-rule.md)
- [The Observability Model](../60-specification/resource-observability/the-observability-model.md)
- [Text, Character, and Bytes](../60-specification/built-in-data-model/text-character-and-bytes.md)
