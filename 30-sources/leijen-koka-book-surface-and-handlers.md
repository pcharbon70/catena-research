---
title: "The Koka Programming Language: Surface Forms and Effect Handlers"
kind: "source"
created: "2026-09-12"
authors: ["Daan Leijen"]
published: null
citation_key: "leijenkokabooksurfaceandhandlers"
container: "Koka language book"
doi: null
url: "https://koka-lang.github.io/koka/doc/book.html"
accessed: "2026-09-12"
tags: ["language-design","syntax","usability"]
aliases: []
---

# The Koka Programming Language: Surface Forms and Effect Handlers

## Reference

Daan Leijen. The Koka Programming Language. Koka language book. [Canonical source](https://koka-lang.github.io/koka/doc/book.html).

Reading locations: Sections 3.4.2–3.4.3 and 4; the embedded draft grammar identifies version v3.2.3.

## Method

The language author's book explains forms by examples, desugarings, and implementation discussion.

## Findings

General control operations expose resumption, while tail-resumptive operation forms can return a reply through restricted sugar. Handling one effect can leave another effect in the enclosing computation.

## Limits

Convenience and performance discussion is Koka-specific. The book does not establish comparative usability or justify transplanting its dynamic binding, control, or row semantics.

## Relevance

Research a simple reply-producing handler layer for Catena while keeping advanced control explicit. Such sugar requires a proven translation through Catena's affine and lifetime rules.

## Derived work

[Grammar and Vocabulary for Approachable Catena](../20-notes/grammar-and-vocabulary-for-approachable-catena.md) distinguishes these findings from Catena-specific recommendations.
