---
title: "GCC Bootstrap Builds and Stage Comparison"
kind: source
created: "2026-09-14"
authors: ["GCC project"]
published: null
citation_key: "gccproject2026bootstrapbuilds"
container: "GCC installation manual"
doi: null
url: "https://gcc.gnu.org/install/build.html"
accessed: "2026-09-14"
tags: [compiler, bootstrap, language-design]
aliases: []
---

# GCC Bootstrap Builds and Stage Comparison

## Reference

GCC project. Installing GCC: Building. GCC installation manual. [Canonical source](https://gcc.gnu.org/install/build.html).

Reading locations: Building a native compiler; three-stage bootstrap, comparison, and stage-specific flags.

## Method

Official build documentation for native compiler bootstrapping.

## Findings

The normal native bootstrap compares stage two with stage three. Different initial-builder flags and capabilities explain why the earliest outputs need not be the appropriate comparison pair.

## Limits

This is build-system behavior, not proof that passing the comparison establishes semantic correctness.

## Relevance

Specify Catena's exact comparison subjects and configuration; do not assume stage numbers imply equivalent provenance or code generation.

## Derived work

[Feature Evolution in a Self-Hosted Catena Compiler](../20-notes/feature-evolution-in-a-self-hosted-catena-compiler.md) separates source evidence from Catena recommendations.
