---
title: "RFC 2119: Key Words for Use in RFCs to Indicate Requirement Levels"
kind: source
created: "2026-08-05"
authors:
  - "Scott Bradner"
published: 1997
citation_key: "bradner1997Rfc2119"
container: "Best Current Practice 14"
edition: "RFC 2119"
isbn: null
doi: "10.17487/RFC2119"
url: "https://www.rfc-editor.org/rfc/rfc2119.html"
accessed: "2026-08-05"
tags:
  - governance
  - language-design
  - specification
aliases:
  - "BCP 14 requirement levels"
---

# RFC 2119: Key Words for Use in RFCs to Indicate Requirement Levels

## Reference

Scott Bradner. “Key words for use in RFCs to Indicate Requirement Levels.”
RFC 2119, BCP 14, March 1997. DOI
[10.17487/RFC2119](https://doi.org/10.17487/RFC2119).
[RFC Editor edition](https://www.rfc-editor.org/rfc/rfc2119.html).

## Contribution

RFC 2119 defines conventional force for absolute requirements and
prohibitions, recommendations that can have justified exceptions, and truly
optional items. It also cautions authors to use imperatives sparingly where
interoperation or harm actually requires them.

## Method

This is an IETF Best Current Practice for authoring and interpreting protocol
specifications, not an empirical study or programming-language semantics.

## Findings

- `MUST` and `MUST NOT` express absolute requirements and prohibitions.
- `SHOULD` and `SHOULD NOT` permit exceptional deviations only after their
  implications are understood and weighed.
- `MAY` permits genuine optionality and expects implementations to tolerate
  presence or absence where interoperability applies.
- The RFC treats several words such as `SHALL`, `REQUIRED`, and `OPTIONAL` as
  synonyms for its principal keywords.

## Relevance

Catena adopts the force distinctions while selecting only five canonical
spellings. Its policy narrows recommendations to quality and implementation
technique and records deviations in conformance profiles. Catena's `MAY`
also covers source permissions and explicit tool options, so it does not
automatically declare implementation-defined behavior.

## Limits

RFC 2119 targets IETF documents and does not define invalid programs,
translation limits, type-system rejection, runtime traps, artifact
transactions, or implementation profiles. RFC 8174 later clarifies its
capitalization ambiguity.

## Derived work

- [Catena Conformance Vocabulary and Behavior Classes](../20-notes/catena-conformance-vocabulary-and-behavior-classes.md)
- [How Should Catena Classify Conformance Behavior?](../40-inquiries/how-should-catena-classify-conformance-behavior.md)
- [Catena Conformance Vocabulary map](../10-maps/catena-conformance-vocabulary.md)
