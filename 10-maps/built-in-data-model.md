---
title: "Built-In Data Model"
kind: map
created: "2026-08-29"
tags:
  - archive-navigation
  - catena
  - data-model
  - text
aliases:
  - "Catena data model map"
---

# Built-In Data Model

## Scope

This map connects C017's scanner kinds and C018's elaboration
precedent to the C029/C033/C035 entry rules, the C040 decision
artifacts — the twelve-way classification, the three elaborated types,
the content-based comparability entries — and the owners of
collections, construction, spellings, and references.

## Start here

- [Catena Built-In Data Model](../20-notes/catena-built-in-data-model.md)
  develops the classification, the three types, and the entries.
- [Resolved data-model inquiry](../40-inquiries/which-types-are-built-in.md)
  records the operational question, hypotheses, and resolution.
- [Built-In Data Model Specification](../60-specification/built-in-data-model/README.md)
  is the candidate version 0.1.35 contract.
- [Equality and Ordering map](equality-and-ordering.md) fixed the
  entry rule this executes.

## Trails

### Foundations that constrain any answer

- [Text, Characters, and Bytes](../60-specification/literal-grammar/text-characters-and-bytes.md)
  scans the three kinds with decoded payloads and provenance.
- [Numeric Literal Semantics Specification](../60-specification/numeric-literal-semantics/README.md)
  fixes the scanner-to-meaning pattern this executes.
- [Value Forms and First-Classness](../60-specification/values-and-evaluation/value-forms-and-first-classness.md)
  and [The Comparable Set](../60-specification/equality-and-ordering/the-comparable-set.md)
  fix the entry rules awaiting this slice.

### Limits and traceability

- [Conformance Traceability](conformance-traceability.md) will
  register `BM-OBL-001` through `BM-OBL-008` against normative anchors
  and sibling compiler tests.
- P109 spellings and the compiled-program path; G101 collection
  declarations; G042 construction and update; G084 references; G105
  string libraries remain the future owners.

## Open questions

C040 is complete at revision `0.1.35`. Collections arrive as library
nominal types at G101; references stay excluded until G084's era if
ever; text literals reach compiled programs at P109.
