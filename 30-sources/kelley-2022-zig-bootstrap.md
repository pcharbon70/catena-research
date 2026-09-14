---
title: "Goodbye to the C++ Implementation of Zig"
kind: source
created: "2026-09-14"
authors: ["Andrew Kelley"]
published: "2022-12-07"
citation_key: "kelley2022zigbootstrap"
container: "Zig project news"
doi: null
url: "https://ziglang.org/news/goodbye-cpp/"
accessed: "2026-09-14"
tags: [compiler, bootstrap, language-design]
aliases: []
---

# Goodbye to the C++ Implementation of Zig

## Reference

Andrew Kelley. Goodbye to the C++ Implementation of Zig. Zig project news, 2022-12-07. [Canonical source](https://ziglang.org/news/goodbye-cpp/).

Reading locations: Problem statement, new build process, and moving forward.

## Method

Firsthand account of replacing a second compiler implementation with an archived WebAssembly bootstrap artifact.

## Findings

The previous design duplicated feature work. The replacement updates its seed when self-compilation needs a feature or fix, while acknowledging a loss of fixed-step source-only reconstruction.

## Limits

A dated engineering account, not current Zig instructions or a controlled productivity comparison. Its timings are explicitly noisy.

## Relevance

A seed snapshot can simplify maintenance, but artifact provenance and source reconstruction remain separate obligations.

## Derived work

[Feature Evolution in a Self-Hosted Catena Compiler](../20-notes/feature-evolution-in-a-self-hosted-catena-compiler.md) separates source evidence from Catena recommendations.
