---
title: "Gleam Use Expressions"
kind: "source"
created: "2026-09-12"
authors: ["Gleam project"]
published: null
citation_key: "gleamprojectuseexpressions"
container: "The Gleam Language Tour"
doi: null
url: "https://tour.gleam.run/advanced-features/use/"
accessed: "2026-09-12"
tags: ["language-design","syntax","usability"]
aliases: []
---

# Gleam Use Expressions

## Reference

Gleam project. Use. The Gleam Language Tour. [Canonical source](https://tour.gleam.run/advanced-features/use/).

Reading locations: Complete Use page; living documentation accessed 12 September 2026.

## Method

The official tour gives a source-to-source explanation of use and its callback expansion.

## Findings

The remainder of the block becomes an anonymous function and bound variables become callback arguments. For a call on the right, that callback is inserted as its final argument.

## Limits

This is callback syntax, not a general guarantee of resource cleanup, cancellation, single execution, or algebraic-effect safety. Its argument convention also differs from Catena's.

## Relevance

Consider a flat visual shape for nested computations, but make callback scope and multiplicity explicit in the semantic contract before designing sugar.

## Derived work

[Grammar and Vocabulary for Approachable Catena](../20-notes/grammar-and-vocabulary-for-approachable-catena.md) distinguishes these findings from Catena-specific recommendations.
