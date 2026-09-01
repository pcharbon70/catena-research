---
title: "Should Catena Admit Type Aliases and Newtypes?"
kind: inquiry
created: "2026-09-01"
status: resolved
tags:
  - catena
  - type-system
  - language-design
aliases:
  - "G062 aliases and newtypes inquiry"
---

# Should Catena Admit Type Aliases and Newtypes?

## Purpose

G062 asks the checklist question: "Define identity, representation,
constructor access, coercion, deriving, and error messages" for
aliases, opaque types, and newtypes. Much of the space is already
settled: C022's export transparency modes and C023's complete binary
constructor-authority vocabulary supply the opaque mechanism, and
single-constructor single-field nominal ADTs are expressible today.
What actually remained open: whether transparent type synonyms are
admitted at all, whether trait instances flow through a newtype
wrapper, and what a newtype may promise about cost.

## Operational definitions

- **Type alias** — a transparent, erasable synonym for another type;
  both names denote one type.
- **Opaque type** — a type whose representation is hidden outside its
  defining module; construction and matching unavailable by
  constructor spelling.
- **Newtype** — a nominal wrapper around exactly one field of one
  other type, distinct in identity from both the wrapped type and
  every other wrapper.

## Hypotheses

1. A new area `aliases-and-newtypes` at `0.1.41` (code `AN`) carries
   the decision as a classification-and-routing slice. *(Recommended:
   the C044 shape.)*
2. **Transparent aliases are excluded** from edition 0.1 with
   recorded arrival conditions: any future alias slice must state
   identity-sharing, the comparability interaction, C028
   compatibility treatment, and error-message naming. The corpus
   spine — nominal identity everywhere, a constructor-authority
   vocabulary declared complete, nothing implicit, diagnostics
   naming declarations — has no room for erasable synonyms.
3. **Opaque types are C022's `abstract` export mode**, routed not
   redefined: identity nominal, representation invisible, the
   smart-constructor idiom sanctioned, per-constructor and
   selective exposure excluded by C023.
4. **The newtype is the single-constructor single-field nominal
   ADT**, already expressible: nominal identity (C002), no implicit
   coercion (wrap and unwrap via constructor and pattern;
   conversions are library territory), **deriving explicit-target
   only — instances never flow through the wrapper** (C073 with
   C065/C070 coherence and C072 law evidence), nominal-spelled
   diagnostics, and **no cost promises** — representation is
   invisible, so "zero-cost" is unstateable, the C042
   complexity-exclusion precedent applied to representation.

## Paths explored

- **Define alias semantics now, dormant** — rejected: fixes rules
  for a form nothing can express and pre-commits the
  identity/comparability interactions before any witness can test
  them.
- **Haskell-style automatic newtype deriving** — rejected: smuggles
  instance equivalence through a wrapper without the corpus's
  explicit-evidence pattern and complicates coherence ownership.
- **Dedicated newtype machinery** — rejected: nothing is missing;
  the declared form exists and runs today.
- **Cost promises** — rejected as unstateable: both-layout
  conformance and representation invisibility forbid them.

## Findings

All four hypotheses held; the developer chose the recommended
option on all four forks (no overrides). The decisive corpus facts:
C023's "authority vocabulary is complete" closes per-constructor
exposure; C002's nominal identity makes the manual wrapper already
a full newtype; and C073's explicit-target derivation gives the
wrapper its instances without inheritance.

## Outcome

Resolved as C062 at revision `0.1.41`: the contract will live in
`60-specification/aliases-and-newtypes/`, the reasoning in
[Catena Aliases and Newtypes](../20-notes/catena-aliases-and-newtypes.md),
and the forks in the [design decision
register](../20-notes/design-decision-register.md). G066, G067, and
D140 remain Section 7's open items; P109 owns any future surface
spellings.
