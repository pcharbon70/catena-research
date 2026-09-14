---
title: "Reflections on Trusting Trust"
kind: source
created: "2026-09-14"
authors: ["Ken Thompson"]
published: 1984
citation_key: "thompson1984reflectionsontrustingtrust"
container: "Communications of the ACM 27(8), 761–763"
doi: "10.1145/358198.358210"
url: "https://doi.org/10.1145/358198.358210"
accessed: "2026-09-14"
tags: [compiler, bootstrap, language-design]
aliases: []
---

# Reflections on Trusting Trust

## Reference

Ken Thompson. Reflections on Trusting Trust. Communications of the ACM 27(8), 761–763, 1984. [Canonical source](https://doi.org/10.1145/358198.358210); [text consulted](https://www.cs.cmu.edu/~rdriley/487/papers/Thompson_1984_ReflectionsonTrustingTrust.pdf).

Reading locations: Stages II and III, pp. 762–763.

## Method

A constructive compiler example, followed by a demonstration of persistent compiler subversion.

## Findings

A new escape can first be implemented using an old numeric representation, then used in the compiler source after rebuilding. Self-reproduction alone does not establish trustworthy compilation.

## Limits

An illustrative construction, not a measurement of feature-development effort or a complete security proof.

## Relevance

Separate implementing a feature from using it, and separate bootstrap repetition from independent correctness evidence.

## Derived work

[Feature Evolution in a Self-Hosted Catena Compiler](../20-notes/feature-evolution-in-a-self-hosted-catena-compiler.md) separates source evidence from Catena recommendations.
