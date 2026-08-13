---
title: "How Should Catena Classify Conformance Behavior?"
kind: inquiry
created: "2026-08-05"
status: resolved
tags:
  - governance
  - language-design
  - specification
aliases:
  - "Catena C009 inquiry"
---

# How Should Catena Classify Conformance Behavior?

## Why this matters

Catena's normative chapters already contain binding declarative rules,
uppercase requirement words, optional forms, recommendations, invalid inputs,
fixed budgets, explicit traps, and one presentation allowance. Without one
shared interpretation, an implementation could confuse optional technique
with optional semantics, treat silence as permission, or report resource
refusal as a type or policy result.

## Operational question

A successful answer must let readers and tools distinguish normative force
from behavior class, identify the consequence of every invalid statement,
bound every permitted implementation variation, disclose actual compiler
choices, and prohibit undefined behavior. It must cover all current normative
chapters without inventing language revision `0.1.8` or changing compiler
semantics and formats.

## Working hypotheses

- Five canonical uppercase words are sufficient when declarative prose remains
  normative.
- Recommendations should apply only to quality or technique and require a
  profile disposition.
- Malformed and ill-formed inputs can be useful subcategories of one
  transactional invalidity class.
- Implementation-defined behavior needs enumerated choices and profile
  publication; bounded presentation variation needs neither when semantics and
  identity cannot change.
- An explicit trap is safer and more reviewable than undefined behavior.
- Area registers plus a release profile can expose every existing `MAY`,
  `SHOULD`, and limit without moving authority out of the chapters.

## Paths to explore

- Compare requirement force and capitalization in
  [RFC 2119](../30-sources/bradner-1997-rfc-2119.md) and
  [RFC 8174](../30-sources/leiba-2017-rfc-8174.md).
- Compare implementation-defined, unspecified, trap, limit, and undefined
  behavior in [WG14 N1570](../30-sources/wg14-2011-n1570.md).
- Compare validation, explicit traps, nondeterminism, and implementation
  limitations in the [WebAssembly Core Specification](../30-sources/rossberg-2026-webassembly-core-specification.md).
- Audit every normative uppercase `MAY` and `SHOULD`, every invalidity
  statement, and the sibling compiler's current choices and limits.
- Extend the archive validator with focused positive, negative, exemption,
  link, callout, and register tests.

## Findings

The evidence supports a two-layer model developed in
[Catena Conformance Vocabulary and Behavior Classes](../20-notes/catena-conformance-vocabulary-and-behavior-classes.md).
Requirement words specify force; the separate taxonomy specifies required,
invalid, implementation-defined, bounded unspecified presentation,
implementation-limit, and explicit runtime-failure behavior.

The existing corpus contains no true implementation-defined choice. Its
uppercase permissions cover program forms, explicit options, optional
metadata, compatibility paths, and semantics-constrained techniques. The one
fresh-variable/constraint spelling allowance is bounded unspecified
presentation. Five substantive recommendations concern diagnostics,
implementation technique, and performance, so profile dispositions can record
current deviations without weakening semantics.

## Outcome

The bounded question is resolved by the repository-level
[Catena Conformance Vocabulary](../CONFORMANCE-VOCABULARY.md), area variability
registers, validator enforcement, and the sibling compiler's format-1
`CONFORMANCE.md` profile. Catena has no undefined behavior. Specification
silence is a defect; invalid input must fail without successful outputs; and
future foreign or unsafe facilities must specify rejection, failure, or traps.

The [C009 record](../50-journal/2026-08-05-c009-conformance-vocabulary.md)
captures the audit and verification. G012 implementation-limit policy, P117
diagnostic completeness, P125 edit application, and G138 performance remain
separate work and do not reopen this decision.
