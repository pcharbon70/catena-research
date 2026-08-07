---
title: "A Structural Approach to Operational Semantics"
kind: source
created: "2026-08-06"
authors:
  - "Gordon D. Plotkin"
published: 2004
citation_key: "plotkin2004structuralOperationalSemantics"
container: "The Journal of Logic and Algebraic Programming 60–61"
edition: null
isbn: null
doi: "10.1016/j.jlap.2004.05.001"
url: "https://homepages.inf.ed.ac.uk/gdp/publications/sos_jlap.pdf"
accessed: "2026-08-06"
tags:
  - formal-semantics
  - operational-semantics
aliases:
  - "Aarhus structural operational semantics notes"
---

# A Structural Approach to Operational Semantics

## Reference

Gordon D. Plotkin. “A Structural Approach to Operational Semantics.” *The
Journal of Logic and Algebraic Programming* 60–61 (2004): 17–139.
[DOI](https://doi.org/10.1016/j.jlap.2004.05.001).

## Contribution

The published Aarhus notes define language behavior through syntax-directed
transition systems and interpreting automata, including expressions,
commands, dynamic errors, and static checking.

## Findings

Small transitions make evaluation order, intermediate states, divergence, and
concurrency premises explicit. Structural induction over derivations supports
proofs that connect syntax, typing, and execution.

## Relevance

Catena uses evaluation contexts for one local process and labeled global
transitions for process scheduling. The separation lets handler, trap, and
mailbox rules share one reduction relation.

## Limits

The work supplies a semantic method, not Catena's row, handler, actor, or BEAM
choices. An executable transcription can still encode an incorrect rule.

## Derived work

- [Catena's Formal Semantic Kernel](../20-notes/catena-formal-semantic-kernel.md)
- [Formal Semantic Kernel map](../10-maps/formal-semantic-kernel.md)
