---
title: "Redesigning the Initial Bootstrap Sequence"
kind: source
created: "2026-09-14"
authors: ["Jieyou Xu"]
published: "2025-05-29"
citation_key: "xu2025rustbootstrapsequence"
container: "Inside Rust blog, on behalf of the Bootstrap team"
doi: null
url: "https://blog.rust-lang.org/inside-rust/2025/05/29/redesigning-the-initial-bootstrap-sequence/"
accessed: "2026-09-14"
tags: [compiler, bootstrap, language-design]
aliases: []
---

# Redesigning the Initial Bootstrap Sequence

## Reference

Jieyou Xu. Redesigning the Initial Bootstrap Sequence. Inside Rust blog, on behalf of the Bootstrap team, 2025-05-29. [Canonical source](https://blog.rust-lang.org/inside-rust/2025/05/29/redesigning-the-initial-bootstrap-sequence/).

Reading locations: Redesigned sequence, implementation considerations, and FAQs; clarification dated 30 May 2025.

## Method

Firsthand design account of a compiler and standard-library build transition.

## Findings

Using the seed's matching standard library for the initial compiler build removes much compatibility conditioning from the in-tree library. The new library is then built by the new compiler.

## Limits

This article announced a redesign; the current developer guide separately documents the resulting arrangement. It supplies no general productivity effect size.

## Relevance

Keep the libraries used to build the compiler distinct from the libraries compiled for new user programs.

## Derived work

[Feature Evolution in a Self-Hosted Catena Compiler](../20-notes/feature-evolution-in-a-self-hosted-catena-compiler.md) separates source evidence from Catena recommendations.
