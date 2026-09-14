---
title: "A Nanopass Framework for Commercial Compiler Development"
kind: source
created: "2026-09-14"
authors: ["Andrew W. Keep","R. Kent Dybvig"]
published: 2013
citation_key: "keepetal2013nanopasscompilerdevelopment"
container: "ICFP 2013, 343–350"
doi: "10.1145/2500365.2500618"
url: "https://doi.org/10.1145/2500365.2500618"
accessed: "2026-09-14"
tags: [compiler, bootstrap, language-design]
aliases: []
---

# A Nanopass Framework for Commercial Compiler Development

## Reference

Andrew W. Keep, R. Kent Dybvig. A Nanopass Framework for Commercial Compiler Development. ICFP 2013, 343–350, 2013. [Canonical source](https://doi.org/10.1145/2500365.2500618); [text consulted](https://www.cs.tufts.edu/comp/150FP/archive/icfp13.pdf).

Reading locations: Sections 2, 3.2–3.3, and 4: intermediate languages, compatibility, and benchmark tradeoffs.

## Method

Compiler infrastructure and a replacement Chez Scheme compiler evaluated with compatibility tests and benchmarks.

## Findings

Small passes with explicit intermediate languages support a substantial compiler implementation. The replacement retained compatibility; improved generated-code performance came with slower compilation in the reported comparisons.

## Limits

This does not measure person-hours per new feature, and multiple architectural changes confound a simple causal claim.

## Relevance

Localize feature lowering and pass invariants while measuring the resulting build cost instead of assuming more passes are free.

## Derived work

[Feature Evolution in a Self-Hosted Catena Compiler](../20-notes/feature-evolution-in-a-self-hosted-catena-compiler.md) separates source evidence from Catena recommendations.
