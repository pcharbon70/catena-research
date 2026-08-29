---
title: "Which Types Are Built In?"
kind: inquiry
created: "2026-08-29"
status: resolved
tags:
  - catena
  - data-model
  - text
  - builtins
  - language-design
aliases:
  - "G040 built-in data model inquiry"
---

# Which Types Are Built In?

## Purpose

G040 asks the checklist question: "Define unit, Boolean, numeric,
string, binary, tuple, list, map, set, process, reference, and
function types, or explicitly exclude each nonessential built-in."
Three entry rules await the answer — value status (C029),
comparability (C035), coverage (C033) — and the corpus holds a ready
precedent: C017's scanner already mints text, character, and bytes
literals with decoded payloads, exactly as numeric literals scanned
at 0.1.13 before C018 elaborated their meaning.

## Operational definitions

- **Built-in** — a type the language definition itself fixes, with
  value status and comparability from this area.
- **Library type** — an ordinary nominal ADT, declared like any
  datatype; list, map, set need no built-in status because nominal
  declaration already expresses them.
- **Elaboration** — the scanner-to-meaning boundary (C018's pattern):
  a scanned literal become a typed meaning without any frontend able
  to encode the literal in a compiled program.

## Hypotheses

1. A new area `built-in-data-model` at `0.1.35` (code `BM`) carries
   the contract — the Section 5 anchor. *(Recommended:
   one-version-per-area; the entry rules' executor becomes their
   owner.)*
2. The twelve-way classification: **typed now** — unit, Bool, Int,
   Float, tuple, function, process handle (shipped, classified once)
   plus Text, Character, and Bytes as built-ins with C018-style
   elaboration; **library territory** — list, map, set as ordinary
   nominal ADTs (G101 declares `List` as `Option` is declared today);
   **excluded** — reference (no mutation; G084's era if ever).
   *(Recommended: every decision rides shipped machinery.)*
3. Text, Character, and Bytes follow **the C018 pattern with three
   types**: Text is the decoded Unicode scalar sequence, Character is
   exactly one scalar (its code point), Bytes is the byte sequence;
   elaboration deterministic and total; raw-hash and provenance stay
   scanner facts; the types live at the meaning and classifier level
   until a frontend can encode them — exactly Float's post-C018
   status.
4. Comparability executes **content-based entries**: Text comparable
   and orderable (code-point sequence, lexicographic); Character
   comparable and orderable; Bytes comparable and orderable
   (byte-sequence order); list/map/set enter with G101's nominal
   declarations; reference and handles never; Unit stays
   non-comparable.
5. The deliverable is a `Catena.Text` elaboration module plus the
   `Catena.Values` and `Data.comparable_type?` extensions, with zero
   new diagnostic families.

## Paths explored

- **All twelve built-in now** — rejected: the frozen frontends cannot
  encode list/map/set literals; pure P109-era design with zero
  executable witness, contradicting C038's decision-not-design
  stance.
- **Classify existing only, defer Text/Char/Bytes** — rejected:
  declines the C018 precedent sitting ready (the scanner already
  mints these literals).
- **Character as Int alias** — rejected: loses the one-scalar
  invariant and muddies C017's decoding contract.
- **Text-as-bytes single type** — rejected: collapses two scanner
  kinds and loses the scalar/byte distinction the scanner preserves.
- **Equality-only comparability** — rejected: declines the natural
  total orders the decoded payloads give; G101's maps and sets need
  ordering anyway.
- **Pipeline integration now / normative-only** — rejected patterns.

## Findings

All five hypotheses held; the developer chose the recommended option
on every fork (five of five, no overrides). One ambiguity surfaced
for Phase 4: a bare Elixir binary could be Text or Bytes at the
classifier — resolved by keying the value-classification on the
elaborated meaning (kind-carrying) while bare binaries classify
conservatively by content, with the rationale written in the journal.

## Outcome

Resolved as C040 at revision `0.1.35`: the contract lives in the
[Built-In Data Model Specification](../60-specification/built-in-data-model/README.md),
the reasoning in
[Catena Built-In Data Model](../20-notes/catena-built-in-data-model.md),
and the forks in the [design decision
register](../20-notes/design-decision-register.md). P109 spellings,
G101 collection declarations, G042 construction and update, and G084
references remain open with their owners.
