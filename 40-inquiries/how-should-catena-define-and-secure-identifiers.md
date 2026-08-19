---
title: "How Should Catena Define and Secure Identifiers?"
kind: inquiry
created: "2026-08-17"
status: resolved
tags:
  - identifiers
  - language-design
  - security
  - unicode
aliases:
  - "Catena C014 inquiry"
---

# How Should Catena Define and Secure Identifiers?

## Why this matters

C013 preserves every Unicode scalar and intentionally leaves identifier
meaning open. Without a versioned next layer, a host library could decide which
names exist, whether canonically equivalent spellings collide, how case
selects roles, and whether deceptive names pass unnoticed.

## Operational question

Choose a bounded standalone name contract for which independent
implementations agree on repertoire, NFC validity, case-sensitive identity,
qualification, keyword escaping, script security, and confusable warnings,
without inventing whole-source tokenization or namespace resolution.

## Working hypotheses

- Unicode 17 XID is a better international baseline than ASCII or general
  letter categories.
- Source spelling already in NFC keeps source, binding, and emitted identity
  aligned.
- Declaration context should determine semantic role so uncased scripts are
  not second-class.
- Security-profile and script failures are validity errors; confusable
  skeleton collisions are review warnings that policy can promote.
- Dot qualification can be fixed lexically while resolution remains later
  work.

## Paths explored

[UAX #31](../30-sources/davis-leroy-2025-unicode-identifiers-syntax.md) was used
for XID profiles and filtered NFC. [UTS #39](../30-sources/davis-suignard-2025-unicode-security-mechanisms.md)
was used for identifier status, Highly Restrictive scripts, and confusable
skeletons. [UTS #55](../30-sources/leroy-davis-2024-unicode-source-code-handling.md)
was used for programming-language case, normalization, and warning guidance.

The existing [source-text specification](../60-specification/source-text/README.md)
established exact decoded scalars and spans. Current normative examples were
audited for established words and dot-qualified forms, while the retained
JSON and kernel name patterns were treated as separate exact protocols.

## Findings

No one control solves Unicode identifier security. XID defines word-like
shape, the General Security Profile removes unsuitable characters, restriction
levels prevent unsafe mixtures, and skeleton diagnostics expose visual
collisions that remain among valid names.

Filtered NFC is stricter than UTS #55's preferred normalized equivalence, but
it avoids hidden comparison forms at this pre-lexer stage. A mandatory exact
replacement fix makes the tradeoff explicit. Role-neutral case is both more
inclusive and cleaner: later grammar already knows whether it is declaring or
using a value, type, variant, trait, effect, handler, or module.

The full comparison and rejected alternatives are developed in
[Catena Identifiers and Name Security](../20-notes/catena-identifiers-and-name-security.md).

## Outcome

Resolved as C014 and source-only language revision `0.1.10`. Catena pins
Unicode 17 `XID_Start`/`XID_Continue`, filtered NFC, the General Security
Profile, Highly Restrictive segments, a closed keyword set with backtick
escapes, ASCII-dot qualification, case-sensitive role-neutral identity, and a
deny-able `IDN007` confusable warning over supplied comparison domains.

The [normative identifier area](../60-specification/identifiers/README.md)
defines `IDN001`–`IDN007` and `ID-OBL-001` through `ID-OBL-013`. The sibling
compiler vendors exact Unicode data and implements standalone identifier,
qualified-name, audit, and CLI boundaries. C015 now supplies whitespace/layout
events, C016 supplies comments, and C017 supplies atomic literals; G019–G022
retain concrete tokenization, punctuation integration, namespaces, resolution,
imports, and exports.
