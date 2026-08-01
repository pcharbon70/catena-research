---
title: "The Temporal Logic of Actions"
kind: source
created: "2026-08-01"
authors:
  - "Leslie Lamport"
published: 1994
citation_key: "lamport1994temporal"
container: "ACM Transactions on Programming Languages and Systems 16(3)"
edition: null
isbn: null
doi: "10.1145/177492.177726"
url: "https://lamport.azurewebsites.net/tla/papers.html"
accessed: "2026-08-01"
tags:
  - concurrency
  - formal-methods
  - specification
aliases:
  - "TLA"
---

# The Temporal Logic of Actions

## Reference

Leslie Lamport. “The Temporal Logic of Actions.” *ACM Transactions on
Programming Languages and Systems* 16, no. 3 (1994): 872–923.
[DOI](https://doi.org/10.1145/177492.177726).

## Contribution

TLA represents a concurrent system and its desired properties in one logic of
state predicates, actions, and temporal formulas. Satisfaction and refinement
can therefore both be stated as logical implication rather than as an informal
relationship between unrelated artifacts.

## Method

The paper gives the logic’s syntax, formal semantics, and proof rules, then
demonstrates their use for specifying and verifying concurrent algorithms.

## Findings

- State-by-state input/output contracts cannot express eventual progress,
  permitted histories, fairness, or refinement between concurrent designs.
- Stuttering-insensitive behavior supports specifications that hide lower-level
  implementation steps while preserving visible behavior.
- Safety and liveness claims require different reasoning, even when written in
  one semantic framework.

## Relevance

Catena targets a concurrent runtime. Governance transitions and actor
protocols therefore need history-sensitive claims alongside local contracts.
The source also supports treating implementation conformance as an explicit
refinement claim rather than a manually assigned status.

## Limits

The logic specifies behavior; it does not automatically connect formulas to
compiled code, choose finite model bounds, identify organizational actors, or
produce trustworthy external event histories. Proof and model-checking tools
add their own trusted assumptions and usability costs.

## Derived work

- [Language-Integrated Specifications and Governance](../20-notes/language-integrated-specifications-and-governance.md)
- [Language-Integrated Specifications and Governance map](../10-maps/language-integrated-specifications-and-governance.md)
