---
title: "Effekt Effect Safety and Contextual Effect Polymorphism"
kind: "source"
created: "2026-09-12"
authors: ["Effekt research team"]
published: null
citation_key: "effektprojectcontextualeffectpolymorphism"
container: "Effekt language documentation"
doi: null
url: "https://effekt-lang.org/docs/concepts/effect-polymorphism"
accessed: "2026-09-12"
tags: ["language-design","syntax","usability"]
aliases: []
---

# Effekt Effect Safety and Contextual Effect Polymorphism

## Reference

Effekt research team. Lightweight Effect Polymorphism; Effect Safety. Effekt language documentation. [Effect polymorphism](https://effekt-lang.org/docs/concepts/effect-polymorphism); [effect safety](https://effekt-lang.org/docs/concepts/effect-safety).

Reading locations: Complete Effect Safety and Lightweight Effect Polymorphism pages; accessed 12 September 2026.

## Method

Official examples explain effects as requirements and distinguish value arguments from block arguments.

## Findings

Under contextual effect polymorphism, an empty requirement for a block does not imply that calling it has no observable effects. The caller can supply effects handled in the block's lexical context.

## Limits

This meaning of empty requirements differs from an ordinary closed pure effect row. The documentation establishes a design, not its ease of learning.

## Relevance

Borrow the practical explanation of supplying requirements, but preserve Catena's existing empty-row and lexical-identity rules. Omitted annotations need an exact expansion.

## Derived work

[Grammar and Vocabulary for Approachable Catena](../20-notes/grammar-and-vocabulary-for-approachable-catena.md) distinguishes these findings from Catena-specific recommendations.
