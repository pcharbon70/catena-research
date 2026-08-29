---
title: "Catena Built-In Data Model"
kind: note
created: "2026-08-29"
maturity: developing
tags:
  - catena
  - language-design
  - data-model
  - text
  - builtins
aliases:
  - "Catena built-in types model"
---

# Catena Built-In Data Model

## Executive conclusion

Catena's built-in data model at `0.1.35` is a per-type decision over
the checklist's twelve candidates — the checklist's own "define or
exclude" shape, answered with shipped machinery:

| Type | Decision |
| --- | --- |
| Unit, Bool, Int, Float, tuple, function, process handle | **built-in, classified once** — shipped types, their value status and comparability stated together |
| Text, Character, Bytes | **built-in, elaborated now** — the C018 pattern: C017's scanner already mints the literals; elaboration gives them typed meaning |
| List, map, set | **library territory** — ordinary nominal ADTs; G101 declares `List` exactly as `Option` is declared today, and nothing about them needs built-in status |
| Reference | **excluded** — no mutation exists; G084's era if ever |

**Text is the decoded Unicode scalar sequence; Character is exactly
one scalar (its code point); Bytes is the byte sequence.** Elaboration
(`scan_literal` → typed meaning) is deterministic and total; raw-hash
counts and provenance remain scanner facts at 0.1.13; and the three
types live at the meaning and classifier level until a frontend can
encode their literals — exactly Float's post-C018 status, stated as
the witness-honesty clause.

**Comparability executes C035's entry rule**: Text comparable and
orderable (code-point sequence, lexicographic); Character comparable
and orderable; Bytes comparable and orderable (byte-sequence order).
List/map/set comparability arrives with G101's nominal declarations —
constructor-field recursion already handles them. References and
process handles never compare; Unit stays non-comparable.

The deliverable is a `Catena.Text` elaboration module plus
`Catena.Values` and `Data.comparable_type?` extensions, with **zero
new diagnostic families** — the C018 executable shape, applied to
the three scanner kinds.

## Scope and method

The operational target is independent agreement on the classification,
the three new types' semantics, and the comparability entries — made
executable through elaboration and classifier witnesses. Primary
evidence is internal: [C017's literal grammar](../60-specification/literal-grammar/text-characters-and-bytes.md)
(the scanner kinds with decoded payloads), [C018's elaboration
precedent](../60-specification/numeric-literal-semantics/README.md),
the [C029](../60-specification/values-and-evaluation/value-forms-and-first-classness.md),
[C033](../60-specification/branching/branch-rules-consolidated.md),
and [C035](../60-specification/equality-and-ordering/the-comparable-set.md)
entry rules, and the nominal-ADT expressibility of List. Source claims
stay distinct from Catena proposals below.

## Relation to the current corpus

[C017](../60-specification/literal-grammar/text-characters-and-bytes.md)
scans the three kinds with exact forms — cooked and hash-counted raw
text, single-quote characters decoding to one Unicode scalar, `b"`/
`br"` bytes — and guarantees equal source bytes produce equal decoded
payloads. Everything the elaborator needs is already normative; the
meaning layer is the only missing step, exactly as 0.1.13 scanned
numerics before 0.1.14 typed them.

[C018](../60-specification/numeric-literal-semantics/numeric-types-and-literal-typing.md)
fixed the pattern: `Catena.scan_literal` → `elaborate_numeric_literal`
→ `Numeric.Meaning`, deterministic and total, with the type living at
the meaning level until frontends encode it — Float reached compiled
programs only in spirit. This slice executes the same pattern for the
three text kinds; `Catena.Text.elaborate` and `Text.Meaning` mirror
`Numeric.Meaning` precisely.

[C029's entry rule](../60-specification/values-and-evaluation/value-forms-and-first-classness.md)
("a future type enters with its value status declared in its own
normative slice") names this slice for string, binary, list, map,
set. The classification is that statement executed: Text, Character,
and Bytes are values (the decoded content); list/map/set's value
status arrives with G101's declarations; reference is never a value.

[C035's entry rule](../60-specification/equality-and-ordering/the-comparable-set.md)
("every G040 built-in enters with its comparability") executes as
the content-based entries: three new comparable-and-orderable types,
with orders the decoded payloads give for free — code-point sequence
for Text and Character, byte sequence for Bytes. No NaN-like special
cases exist: the orders are total.

[C033's coverage rule](../60-specification/branching/branch-rules-consolidated.md)
("future scrutinee types enter with their coverage entries") defers
cleanly: no frontend encodes a Text scrutinee yet, so literal-pattern
coverage for the new types enters with the P109-era pattern surface —
stated as the exclusion, not silently omitted.

## Comparative evidence and inference

### Why library, not built-in, for collections

A `List` is expressible today: declare a nominal datatype with `Nil`
and `Cons` constructors, exactly as `Option` is declared. Built-in
status would buy dedicated literal syntax — a P109-era surface — and
nothing else: C002's constructor patterns, C035's constructor-field
comparability recursion, and C004's derivations all already serve
nominal ADTs. Making collections built-ins would also pre-decide
representation (linked lists? vectors?) that G101's library work
should choose with evidence. The checklist's "or explicitly exclude
each nonessential built-in" is satisfied by the honest routing: not
excluded from the language, excluded from the *built-in* list.

### Why three types, not one

C017 preserves exactly the distinction the types should carry: text
decodes to scalars, bytes to byte content, characters to exactly one
scalar. Collapsing Text into Bytes would erase the scalar/byte
distinction the scanner guarantees; aliasing Character to Int would
drop the one-scalar invariant from the type. Three scanner kinds,
three types — the grammar already decided.

### Why content orders, not equality only

The decoded payloads make code-point and byte ordering free and
total; equality-only entries would decline them and force G101's
map/set work to reopen C035 later. Content ordering is also what
every ecosystem's text comparison means in practice — lexicographic
scalar sequence.

## Selected model

> **Normative definitions (placed in the candidate chapters).**

### The classification

As the table above; the entry-rule consequences stated per type.

### The three types

```text
Text      ::= scalar-sequence      -- the decoded payload
Character ::= one Unicode scalar   -- its code point
Bytes     ::= byte-sequence
```

Elaboration: `scan_literal` → meaning, deterministic and total.

### Comparability

| Type | Comparable | Orderable | Order |
| --- | --- | --- | --- |
| Text | yes | yes | code-point sequence, lexicographic |
| Character | yes | yes | its scalar |
| Bytes | yes | yes | byte sequence, lexicographic |
| List/map/set | with G101 | with G101 | via constructor recursion |
| Reference, handle | never | never | — |
| Unit | no (C035 standing) | no | — |

### Rejected alternatives

As enumerated in the resolved inquiry.

## What C040 adds to the design

The Section 5 era opens with its anchor fixed: G101 declares
collections on nominal machinery with the entry rules' paths already
paved; G042's construction and update know what constructs; G105's
string library receives a typed Text; P109's grammar exercise
receives three literal semantics already elaborated (only the
compiled-program path remains); and the twelve-way table answers the
checklist's question in one place.

## Remaining questions and falsification criteria

P109 owns spellings and the compiled-program path for text literals;
G101 owns collection declarations and their entries; G042 construction
and update; G084 references; G105 string libraries; G061 numeric
trait relationships (unchanged by this slice).

The model should be revisited if G101's evidence shows nominal Lists
materially inadequate (the remedy is a dedicated slice promoting List
to built-in with its entry — the classification is a decision, not a
permanent exclusion), or if text performance demands a different
representation (the remedy is implementation freedom — content
semantics bind, representation stays free per C037).

## Connections

- The [resolved data-model inquiry](../40-inquiries/which-types-are-built-in.md)
  records the question, hypotheses, and outcome.
- The [Built-In Data Model map](../10-maps/built-in-data-model.md)
  routes through the scanner, the entry rules, and the future owners.
- The [Built-In Data Model Specification](../60-specification/built-in-data-model/README.md)
  defines the candidate — then normative at promotion — `0.1.35`
  contract this note argues for.
- [Catena Numeric Literal Semantics](catena-numeric-literal-semantics.md)
  fixed the elaboration pattern this executes.
- [Catena Equality and Ordering](catena-equality-and-ordering.md)
  fixed the entry rule this executes.

## Sources

- [Text, Characters, and Bytes](../60-specification/literal-grammar/text-characters-and-bytes.md)
- [Numeric Literal Semantics Specification](../60-specification/numeric-literal-semantics/README.md)
- [Value Forms and First-Classness](../60-specification/values-and-evaluation/value-forms-and-first-classness.md)
- [The Comparable Set](../60-specification/equality-and-ordering/the-comparable-set.md)
- [Branch Rules Consolidated](../60-specification/branching/branch-rules-consolidated.md)
