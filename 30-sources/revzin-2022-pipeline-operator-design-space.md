---
title: "Exploring the Design Space for a Pipeline Operator"
kind: "source"
created: "2026-09-12"
authors: ["Barry Revzin"]
published: "2022-10-13"
citation_key: "revzin2022pipelineoperatordesignspace"
container: "WG21 P2672R0"
doi: null
url: "https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2022/p2672r0.html"
accessed: "2026-09-12"
tags: ["language-design","syntax","usability"]
aliases: []
---

# Exploring the Design Space for a Pipeline Operator

## Reference

Barry Revzin. Exploring the Design Space for a Pipeline Operator. WG21 P2672R0, 2022-10-13. [Canonical source](https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2022/p2672r0.html).

Reading locations: Sections 1–2 and 3.2–3.3.

## Method

A standards proposal compares left-threading, inverted invocation, placeholders, and language-bind designs, including evaluation details.

## Findings

Similar pipe notation can encode different argument placement, callable requirements, and evaluation behavior. The paper's recommendations are motivated by C++ constraints.

## Limits

P2672R0 is a design exploration, not an adopted C++ rule or user study. Catena's curried functions change the tradeoffs.

## Relevance

Use the four-way taxonomy to audit Catena's pipe against its own ABI; do not import another language's conclusion along with the diagram.

## Derived work

[Grammar and Vocabulary for Approachable Catena](../20-notes/grammar-and-vocabulary-for-approachable-catena.md) distinguishes these findings from Catena-specific recommendations.
