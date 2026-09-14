---
title: "A Minimalistic Verified Bootstrapped Compiler"
kind: source
created: "2026-09-14"
authors: ["Magnus O. Myreen"]
published: 2021
citation_key: "myreen2021minimalisticverifiedbootstrap"
container: "Certified Programs and Proofs 2021, 32–45"
doi: "10.1145/3437992.3439915"
url: "https://doi.org/10.1145/3437992.3439915"
accessed: "2026-09-14"
tags: [compiler, bootstrap, language-design]
aliases: []
---

# A Minimalistic Verified Bootstrapped Compiler

## Reference

Magnus O. Myreen. A Minimalistic Verified Bootstrapped Compiler (Proof Pearl). Certified Programs and Proofs 2021, 32–45, 2021. [Canonical source](https://doi.org/10.1145/3437992.3439915); [text consulted](https://www.cse.chalmers.se/~myreen/cpp2021-bootstrap-myreen.pdf).

Reading locations: Sections 2, 7, 8, and 10; full title includes '(Proof Pearl)'.

## Method

A deliberately small compiler and mechanized bootstrap in HOL4.

## Findings

Compiler source representation, a correctness theorem, and evaluation in the logic combine to produce a verified implementation. Self-application equality is distinct from the main correctness result.

## Limits

The paper prioritizes clarity over realism, generality, and performance; its resource observations should not forecast Catena's.

## Relevance

Keep source correspondence and semantic correctness explicit when describing what self-compilation establishes.

## Derived work

[Feature Evolution in a Self-Hosted Catena Compiler](../20-notes/feature-evolution-in-a-self-hosted-catena-compiler.md) separates source evidence from Catena recommendations.
