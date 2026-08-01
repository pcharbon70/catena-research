---
title: "Typestate: A Programming Language Concept for Enhancing Software Reliability"
kind: source
created: "2026-08-01"
authors:
  - "Robert E. Strom"
  - "Shaula Yemini"
published: 1986
citation_key: "stromYemini1986typestate"
container: "IEEE Transactions on Software Engineering SE-12(1)"
edition: null
isbn: null
doi: "10.1109/TSE.1986.6312929"
url: "https://research.ibm.com/publications/typestate-a-programming-language-concept-for-enhancing-software-reliability"
accessed: "2026-08-01"
tags:
  - language-design
  - protocols
  - type-systems
aliases:
  - "Typestate"
---

# Typestate: A Programming Language Concept for Enhancing Software Reliability

## Reference

Robert E. Strom and Shaula Yemini. “Typestate: A Programming Language Concept
for Enhancing Software Reliability.” *IEEE Transactions on Software
Engineering* SE-12, no. 1 (1986): 157–171.
[DOI](https://doi.org/10.1109/TSE.1986.6312929).

## Contribution

Typestate refines a value’s ordinary type with its current protocol state. The
compiler can then reject an operation that is valid for the general type but
invalid at this point in the value’s lifecycle, such as reading an
uninitialized variable or using a released resource.

## Method

The authors define typestate, show how a compiler can track it, work through
reliability and finalization examples, and report experience with a language
that incorporated the analysis.

## Findings

- A type can express both what an entity is and which operations its present
  state permits.
- Compile-time transition checking detects sequencing errors outside ordinary
  type and scope checking.
- Lifecycle invariants can drive compiler actions such as safe finalization,
  making protocol state operational rather than documentary.

## Relevance

The model suggests representing proposal, acceptance, activation,
deprecation, and replacement as explicit states with typed transitions. It
also warns against a freely mutable `status` field that admits impossible or
unauthorized jumps.

## Limits

Classic typestate tracks program values under a compiler analysis. Governance
events involve persistent identity, multiple actors, revocation, and histories
that may occur outside one compilation. Aliasing and distributed ownership can
also make precise state tracking difficult; some transitions will require
runtime or externally attested evidence.

## Derived work

- [Language-Integrated Specifications and Governance](../20-notes/language-integrated-specifications-and-governance.md)
- [Language-Integrated Specifications and Governance map](../10-maps/language-integrated-specifications-and-governance.md)
