---
title: "Catena Conformance Vocabulary"
kind: map
created: "2026-08-05"
tags:
  - governance
  - language-design
  - specification
aliases:
  - "Catena conformance map"
---

# Catena Conformance Vocabulary

## Scope

This map connects requirement words, behavior classes, invalidity, permitted
variation, implementation limits, explicit traps, corpus enforcement, and the
bootstrap compiler profile. C009 is repository governance across every
normative revision, not language revision `0.1.8`.

## Start here

- [Catena Conformance Vocabulary and Behavior Classes](../20-notes/catena-conformance-vocabulary-and-behavior-classes.md)
  develops the two-layer model and rejected alternatives.
- [How Should Catena Classify Conformance Behavior?](../40-inquiries/how-should-catena-classify-conformance-behavior.md)
  records the operational question and bounded resolution.
- [Catena Conformance Vocabulary](../CONFORMANCE-VOCABULARY.md) is the
  repository policy governing all normative chapters.
- [C009 Conformance Vocabulary](../50-journal/2026-08-05-c009-conformance-vocabulary.md)
  records the corpus audit, validator enforcement, compiler documentation
  checks, and absence of a semantic promotion gate.

## Trails

### Requirement force and capitalization

[RFC 2119](../30-sources/bradner-1997-rfc-2119.md) separates absolute,
recommended, and optional requirements. [RFC 8174](../30-sources/leiba-2017-rfc-8174.md)
clarifies uppercase-only special meanings and confirms that declarative prose
can remain normative. Catena adopts five canonical words and prohibits the
synonym set.

### Behavior and failure classes

[WG14 N1570](../30-sources/wg14-2011-n1570.md) provides comparative definitions
for implementation-defined and unspecified values, traps, limits, and
conformance. Catena rejects its undefined-behavior rule and makes silence a
specification defect.

The [WebAssembly Core Specification](../30-sources/rossberg-2026-webassembly-core-specification.md)
separates well-formedness, validation, execution, traps, and implementation
limits. Catena adapts the explicit-failure discipline while defining its own
transactional invalidity and narrower presentation variability.

### Authority and implementation disclosure

[Specification Authority](../SPECIFICATION-AUTHORITY.md) identifies the
normative material to which the vocabulary applies. Every specification-area
index now registers its permissions, recommendations, presentation latitude,
and limits. The sibling compiler's format-1 `CONFORMANCE.md` records its actual
choices and recommendation dispositions without claiming that a profile can
amend the language.

## Remaining questions

The bounded C009 inquiry is resolved. The
[C012 policy](../IMPLEMENTATION-LIMITS.md) now supplies the general
implementation-limit contract; the resolved C011 delivered exhaustive
rule-to-test traceability; and P117, P125, and G138 remain responsible for the
diagnostic, migration-tool, and performance work exposed by the recommendation
audit.
