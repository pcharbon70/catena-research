---
title: "Fully Countering Trusting Trust through Diverse Double-Compiling"
kind: source
created: "2026-09-14"
authors: ["David A. Wheeler"]
published: 2009
citation_key: "wheeler2009diversedoublecompiling"
container: "PhD dissertation, George Mason University"
doi: null
url: "https://dwheeler.com/trusting-trust/dissertation/"
accessed: "2026-09-14"
tags: [compiler, bootstrap, language-design]
aliases: []
---

# Fully Countering Trusting Trust through Diverse Double-Compiling

## Reference

David A. Wheeler. Fully Countering Trusting Trust through Diverse Double-Compiling. PhD dissertation, George Mason University, 2009. [Canonical source](https://dwheeler.com/trusting-trust/dissertation/); [text consulted](https://dwheeler.com/trusting-trust/dissertation/html/wheeler-trusting-trust-ddc.html).

Reading locations: Sections 4.2–4.5, formal assumptions in 5.6.4, and the
[dissertation errata](https://dwheeler.com/trusting-trust/dissertation-errata.html).

## Method

Formalized assumptions and proof for diverse double-compiling, with compiler demonstrations.

## Findings

A diverse compiler builds the parent source, whose result builds the candidate source for comparison. The conclusion is source–executable correspondence under assumptions, not that the source itself is benign or correct.

## Limits

The diverse compiler must implement the parent's needed semantics; trusted comparison, controlled inputs, and applicable errata matter.

## Relevance

A frozen Elixir compiler is not automatically a diverse checker for future Catena source that exceeds its supported subset.

## Derived work

[Feature Evolution in a Self-Hosted Catena Compiler](../20-notes/feature-evolution-in-a-self-hosted-catena-compiler.md) separates source evidence from Catena recommendations.
