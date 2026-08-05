---
title: "JEP 12: Preview Features"
kind: source
created: "2026-08-05"
authors:
  - "Alex Buckley"
published: "2018"
citation_key: "buckley2018PreviewFeatures"
container: "OpenJDK JEP Index"
edition: null
isbn: null
doi: null
url: "https://openjdk.org/jeps/12"
accessed: "2026-08-05"
tags:
  - compatibility
  - language-design
  - migration
aliases:
  - "OpenJDK preview feature process"
---

# JEP 12: Preview Features

## Reference

Alex Buckley. “JEP 12: Preview Features,” OpenJDK, created 2018 and current
process text accessed 2026-08-05. [Official JEP](https://openjdk.org/jeps/12).

## Contribution

JEP 12 defines a release-bound, disabled-by-default lifecycle for language,
VM, and API features whose specifications and implementations are complete
enough for real-world feedback but whose permanence is not promised. It also
requires generated artifacts to record preview dependence.

## Method

The JEP is an active platform process specification. It describes design
criteria, opt-in behavior, specification integration, compiler diagnostics,
artifact marking, and possible permanent or removed outcomes.

## Findings

- Preview status means impermanent, not partially implemented or low quality.
- Use requires explicit opt-in and produces warnings or errors when the
  required opt-in is absent.
- An artifact records when its source depends on a preview, including when
  lowering could otherwise erase evidence of the source feature.
- A preview may become permanent, be refined in another preview round, or be
  removed.
- Code tied to an older release's preview is not promised to work unchanged
  on a later release.

## Relevance

Catena adopts explicit opt-in, revision binding, artifact propagation, and a
choice between stabilization and withdrawal. Catena differs by naming
previews individually, keeping the BEAM runtime edition-neutral, and exposing
only public preview requirements through module interfaces.

## Limits

Java couples preview execution to JVM class-file rules and enables a release's
language previews as a group. Catena targets ordinary BEAM execution and uses
package-level named opt-ins, so JEP 12 supplies comparison evidence rather
than a protocol to copy.

## Derived work

- [Language Editions and Feature Lifecycle](../20-notes/language-editions-and-feature-lifecycle.md)
- [Catena feature lifecycle](../60-specification/editions-and-feature-lifecycle/feature-lifecycle-and-compatibility.md)
