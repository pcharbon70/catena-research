---
title: "Catena Aliases and Newtypes"
kind: note
created: "2026-09-01"
maturity: developing
tags:
  - catena
  - type-system
  - newtypes
  - language-design
aliases:
  - "Catena alias exclusion"
---

# Catena Aliases and Newtypes

## Executive conclusion

Catena needs no new machinery for G062 — it needs one exclusion and
two routings. Transparent type aliases are **excluded**: every type
name is a nominal declaration, and any future alias slice must state
identity-sharing, comparability interaction, compatibility
treatment, and error-message naming before existing. Opaque types
**are** C022's `abstract` export mode, whose constructor-authority
vocabulary C023 declared complete. Newtypes **are**
single-constructor single-field nominal ADTs, expressible today,
with explicit-only coercion, explicit-only deriving — instances
never flow through the wrapper — and no cost promises, because
representation is invisible and both layouts conform.

## Scope, method, and definitions

This note synthesizes the archive's evidence for closing G062 at
revision `0.1.41`. It reads C002's nominal identity and interface
contract, C022's transparency modes, C023's authority vocabulary
and smart-constructor idiom, C035's comparability, C073's
explicit-target derivation, and the C042 complexity-exclusion
precedent; it invents no syntax and proposes no new declarations.

- **Newtype** — a nominal datatype with exactly one constructor of
  exactly one field; the wrapper is distinct in identity from the
  wrapped type and from every other wrapper.
- **Arrival condition** — the obligations a future slice must
  discharge before an excluded form may exist.

## Why aliases lose

Three corpus pillars close the door. First, **nominal identity is
the spine**: C002 anchors type identity in declarations, C035
compares through declared structure, and diagnostics name
declarations — an erasable synonym blurs all three. Second, **the
authority vocabulary is complete** (C023): transparent|abstract,
with every other authority-bearing form excluded; an alias would be
a third kind of type visibility arriving through the back door.
Third, **nothing implicit**: an alias silently retyping every use
site is the definition of implicit. The honest spelling for "this
type name is clearer" is a newtype or a comment; the honest
spelling for "these are the same values" is using one type.

## What a newtype gets and never gets

Gets: nominal identity, constructor and pattern access (the binary
vocabulary), the smart-constructor idiom over `abstract` export,
comparability through C035's structural recursion, explicit-target
derivation, and nominal-spelled diagnostics. Never gets: implicit
coercion in either direction (constructor wraps, pattern unwraps,
the library converts), automatic instance inheritance (the wrapper
is a fresh nominal type in every respect — deriving says so
explicitly, per C073), and cost or layout promises — both-layout
conformance and representation invisibility (C023, C037) make
"zero-cost" unstateable, exactly as C042 excluded complexity for
the same architectural reason.

## Tradeoffs, limitations, falsification

The exclusion costs some convenience where aliases shine
(long generic types, documentation); newtypes cover the
safety-relevant cases at the price of one constructor application.
The explicit-deriving rule costs boilerplate against Haskell's
`deriving newtype`; it buys instance-level honesty. If an alias
form ever ships without first stating the four arrival conditions,
or an instance ever flows through a wrapper unasked, this contract
is falsified and must be amended by a new revision.

## Route to sources

- The [Aliases and Newtypes Specification](../60-specification/aliases-and-newtypes/README.md)
  defines the normative `0.1.41` contract this note argues for.
- [Authority and Representation Exclusions](../60-specification/abstraction-boundaries/authority-and-representation-exclusions.md)
  — C023's complete authority vocabulary the exclusion extends.
- [Declarations and Nominal Identity](../60-specification/data-and-patterns/declarations-and-nominal-identity.md)
  — the identity spine.
- [The Comparable Set](../60-specification/equality-and-ordering/the-comparable-set.md)
  — wrapper comparability.
- [Laws, Derivation, and Testing](../60-specification/traits-and-categorical-operations/laws-derivation-and-testing.md)
  — C073's explicit evidence discipline.
- The [resolved inquiry](../40-inquiries/should-catena-admit-type-aliases-and-newtypes.md)
  preserves the decision route.
