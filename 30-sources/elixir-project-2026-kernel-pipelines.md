---
title: "Elixir Kernel Pipelines and Their Pitfalls"
kind: "source"
created: "2026-09-12"
authors: ["Elixir project"]
published: 2026
citation_key: "elixirproject2026kernelpipelines"
container: "Elixir 1.20.4 documentation"
doi: null
url: "https://elixir.hexdocs.pm/Kernel.html"
accessed: "2026-09-12"
tags: ["language-design","syntax","usability"]
aliases: []
---

# Elixir Kernel Pipelines and Their Pitfalls

## Reference

Elixir project. Kernel. Elixir 1.20.4 documentation, 2026. [Canonical source](https://elixir.hexdocs.pm/Kernel.html).

Reading locations: Kernel.|>/2, its Pitfalls subsection, and then/2. Documentation version observed: 1.20.4.

## Method

Official API definitions and examples specify the pipe macro's transformation and limitations.

## Findings

Elixir inserts the left expression as the first argument of the right call. Optional parentheses interact with precedence; anonymous-function calls require their invocation form. The documentation supplies explicit pitfalls.

## Limits

These are language rules, not evidence that users prefer or comprehend them. Catena's curried application and subject-last ABI use a different contract.

## Relevance

Borrow the readability objective of visible data flow. Compare pipe elaborations before borrowing the surface, and preserve Catena's existing evaluation and application semantics.

## Derived work

[Grammar and Vocabulary for Approachable Catena](../20-notes/grammar-and-vocabulary-for-approachable-catena.md) distinguishes these findings from Catena-specific recommendations.
