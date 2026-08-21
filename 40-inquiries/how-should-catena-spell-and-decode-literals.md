---
title: "How Should Catena Spell and Decode Literals?"
kind: inquiry
created: "2026-08-18"
status: resolved
tags:
  - bytes
  - catena
  - characters
  - language-design
  - literals
  - syntax
  - text
aliases:
  - "Catena literal inquiry"
---

# How Should Catena Spell and Decode Literals?

## Why this matters

C013 through C016 fixed source units, identifiers, layout, and comments, but
implementations could still disagree about where a literal ends, which
escapes are valid, whether text is normalized or interpolated, whether a raw
newline reaches layout, and what an integer or float scanner returns.

Those disagreements would leak into parsing, diagnostics, formatting,
constant evaluation, numeric typing, and future compatibility. The reserved
C012 decoded-payload limit also could not become active until a literal
payload had an exact measurement point.

## Operational question

Choose an initial atomic grammar in which independent implementations agree
on:

- the admitted Boolean, numeric, text, character, and byte token forms;
- numeric bases, separators, leading zeros, decimal points, exponents, signs,
  suffix boundaries, and exact component output;
- cooked delimiters, the complete escape set, scalar validity, and source LF;
- raw delimiter matching, hash count, byte restrictions, and line ownership;
- preservation, normalization, decoded payload, source pieces, and spans;
- stable malformed-input and limit diagnostics; and
- explicit exclusions from the atomic slice.

The answer must compose with C013–C016 and C012 without silently deciding
G018 runtime numeric semantics, G019's whole tokenizer, P109's surface grammar,
or the G040/G042/P093/G097 data model.

## Paths explored

- [Rust literal tokens](../30-sources/rust-project-2026-literal-tokens.md)
  provide exact hash-delimited raw strings, a byte/text distinction, strict
  escapes, and numeric token evidence.
- [Python lexical analysis](../30-sources/python-software-foundation-2026-python-lexical-analysis.md)
  exposes the cross product created by prefixes, quoting styles, raw/bytes,
  formatted strings, based numbers, and separators.
- [Swift lexical structure](../30-sources/swift-project-2026-lexical-structure.md)
  shows extended string delimiters and delimiter-sensitive interpolation.
- [C013 source text](../60-specification/source-text/README.md),
  [C014 identifiers](../60-specification/identifiers/README.md),
  [C015 layout](../60-specification/whitespace-and-layout/README.md), and
  [C016 comments](../60-specification/comments-and-documentation-comments/README.md)
  supply the integration constraints.
- [C012 limits](../IMPLEMENTATION-LIMITS.md) supply the already approved
  integer and decoded-payload floors.

## Findings

The stable boundary is smaller than the original checklist wording. Atoms,
collections, and binary construction are not merely alternative literal
spellings; they settle primitive types, ordering, duplicate handling,
representation, and patterns. They remain with their data-model owners.

Exact raw hashes provide multiline and delimiter flexibility without an
escape language. Making raw LF token-owned is the only choice consistent with
C015's rule that layout sees whitespace outside tokens. A small closed cooked
escape set makes every backslash deterministic and lets unknown escapes fail
early.

Text, character, and bytes require three different decoded domains. Text is a
preserved scalar sequence, character is exactly one scalar, and bytes is an
octet sequence with direct ASCII only. Applying identifier NFC to text would
violate C013 preservation and change program data.

Returning exact numeric components avoids choosing G018's types and rounding
inside the lexer. Lowercase prefixes, no redundant decimal leading zeros, and
one underscore only between digits give a compact deterministic spelling.

Ordinary and raw strings cannot safely acquire interpolation later without
changing existing source meaning. A future interpolation feature therefore
needs a new prefix.

## Outcome

Resolved as C017 and source-only language revision `0.1.13`. Catena admits
atomic Booleans, unsigned based integers, decimal floats, cooked/raw text,
one-scalar cooked characters, and cooked/raw bytes. It uses the strict escape,
preservation, raw-line-ownership, provenance, diagnostic, and limit rules in
the [normative literal specification](../60-specification/literal-grammar/README.md).

G017 is complete through the
[literal synthesis](../20-notes/catena-literal-grammar.md),
[topic map](../10-maps/literal-grammar.md), and
[C017 evidence record](../50-journal/2026-08-18-c017-literal-grammar.md).
Numeric types, defaulting, rounding, overflow, exceptional values, and
negative-expression elaboration are complete as C018 at revision `0.1.14`.
G019/P109 own complete token and grammar
composition; compound and BEAM-native data remain separately owned.
