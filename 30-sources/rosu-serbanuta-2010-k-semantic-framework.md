---
title: "An Overview of the K Semantic Framework"
kind: source
created: "2026-08-01"
authors:
  - "Grigore Roșu"
  - "Traian-Florin Șerbănuță"
published: 2010
citation_key: "rosuSerbanuta2010k"
container: "The Journal of Logic and Algebraic Programming 79(6)"
edition: null
isbn: null
doi: "10.1016/j.jlap.2010.03.012"
url: "https://www.sciencedirect.com/science/article/pii/S1567832610000160"
accessed: "2026-08-01"
tags:
  - formal-semantics
  - language-design
  - rewriting
aliases:
  - "K semantic framework overview"
---

# An Overview of the K Semantic Framework

## Reference

Grigore Roșu and Traian-Florin Șerbănuță. “An Overview of the K Semantic
Framework.” *The Journal of Logic and Algebraic Programming* 79, no. 6
(2010): 397–434. [DOI](https://doi.org/10.1016/j.jlap.2010.03.012).

## Contribution

K is an executable framework for defining languages, calculi, type systems,
and analysis tools with configurations, computations, and rewrite rules. A
configuration divides program state into named cells, while rules state which
parts they read, change, or leave unconstrained.

## Method

The paper explains the framework, illustrates control-intensive and concurrent
semantics, surveys uses available at the time, and tests expressiveness against
a deliberately challenging example language.

## Findings

- A language definition can be precise enough to execute rather than existing
  only as explanatory prose.
- Rules that expose read and write footprints can remain modular as unrelated
  state cells are added and can represent concurrency without imposing a
  single global sequential rewrite.
- Parsers, interpreters, state exploration, and formal analysis can be derived
  from a shared semantic definition, reducing duplicated semantic accounts.

## Relevance

Catena’s specification and governance constructs need one normative meaning
shared by the compiler, checker, evidence runner, and documentation tooling.
An executable semantic kernel is a credible way to prevent each tool from
silently inventing a different lifecycle or rule interpretation.

## Limits

Executability does not make a definition correct: mistakes in the semantic
rules are faithfully executed. Framework implementation and translation remain
trusted. The paper addresses language semantics, not organizational identity,
signed evidence, usability, or governance bootstrapping.

## Derived work

- [Language-Integrated Specifications and Governance](../20-notes/language-integrated-specifications-and-governance.md)
- [Language-Integrated Specifications and Governance map](../10-maps/language-integrated-specifications-and-governance.md)
