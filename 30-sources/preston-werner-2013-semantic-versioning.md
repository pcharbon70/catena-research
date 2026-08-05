---
title: "Semantic Versioning 2.0.0"
kind: source
created: "2026-08-05"
authors:
  - "Tom Preston-Werner"
published: "2013"
citation_key: "prestonWerner2013SemanticVersioning"
container: "Semantic Versioning"
edition: "2.0.0"
isbn: null
doi: null
url: "https://semver.org/spec/v2.0.0.html"
accessed: "2026-08-05"
tags:
  - compatibility
  - language-design
  - versioning
aliases:
  - "SemVer 2.0.0"
---

# Semantic Versioning 2.0.0

## Reference

Tom Preston-Werner. “Semantic Versioning 2.0.0,” 2013. Current specification
accessed 2026-08-05. [Official specification](https://semver.org/spec/v2.0.0.html).

## Contribution

Semantic Versioning relates three numeric components to compatibility of a
declared public API: major for incompatible changes, minor for backward-
compatible additions, and patch for backward-compatible fixes. It separately
states that initial `0.y.z` development is unstable and may change at any
time.

## Method

The document is a normative versioning convention. It supplies definitions
and ordering rules rather than experimental evidence that projects classify
changes correctly.

## Findings

- Compatibility statements are meaningful only after the public contract is
  declared.
- A post-1.0 major increment signals an incompatible public change.
- A post-1.0 minor increment adds compatible functionality.
- A post-1.0 patch increment contains compatible corrections.
- The `0.y.z` line is explicitly allowed to change incompatibly.

## Relevance

Catena uses the syntax while defining its own language-specific public
contract. Edition `0.1` remains a prototype track where breaking changes need
an explicit revision and migration record. After 1.0, Catena applies the
standard major/minor/patch compatibility meanings to language revisions.

## Limits

Semantic Versioning does not define language editions, compiler retention,
source versus behavior compatibility, previews, deprecation windows, or
artifact schemas. Those meanings must be specified rather than inferred from
the numeric shape alone.

## Derived work

- [Language Editions and Feature Lifecycle](../20-notes/language-editions-and-feature-lifecycle.md)
- [Catena 0.1.7 edition selection](../60-specification/editions-and-feature-lifecycle/edition-selection-and-applicability.md)
