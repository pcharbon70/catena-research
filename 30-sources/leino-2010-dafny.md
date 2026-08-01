---
title: "Dafny: An Automatic Program Verifier for Functional Correctness"
kind: source
created: "2026-08-01"
authors:
  - "K. Rustan M. Leino"
published: 2010
citation_key: "leino2010dafny"
container: "Logic for Programming, Artificial Intelligence, and Reasoning, LPAR-16"
edition: null
isbn: "978-3-642-17510-7"
doi: "10.1007/978-3-642-17511-4_20"
url: "https://www.microsoft.com/en-us/research/publication/dafny-automatic-program-verifier-functional-correctness-2/"
accessed: "2026-08-01"
tags:
  - formal-methods
  - language-design
  - program-verification
aliases:
  - "Dafny automatic program verifier"
---

# Dafny: An Automatic Program Verifier for Functional Correctness

## Reference

K. Rustan M. Leino. “Dafny: An Automatic Program Verifier for Functional
Correctness.” In *Logic for Programming, Artificial Intelligence, and
Reasoning*, LNCS 6355 (2010): 348–370.
[DOI](https://doi.org/10.1007/978-3-642-17511-4_20).

## Contribution

Dafny integrates executable programs, contracts, loop invariants, frame
conditions, termination measures, and ghost state in one verification-aware
language. The verifier translates those declarations into proof obligations
for automated solver discharge.

## Method

The paper tours the language and its encoding, works through small examples,
and presents a complete functional specification of the pointer-intensive
Schorr–Waite graph algorithm as a larger case study.

## Findings

- Pre- and postconditions support modular reasoning only when mutation is also
  bounded by explicit frame conditions.
- Loop invariants and termination measures expose facts that automated solvers
  generally cannot infer from implementation text alone.
- Ghost declarations let proof structure live beside executable code without
  becoming runtime state.
- Automation can discharge substantial functional-correctness obligations,
  but language design and user annotations shape the resulting solver problem.

## Relevance

The paper is evidence that specifications can be first-class compiler inputs
without making every programmer interact directly with a proof assistant. It
also motivates a clean separation between executable declarations, proof-only
material, and the trusted translation and checking pipeline.

## Limits

Verification is relative to the written specification, language model,
translation, axioms, and solver behavior. The 2010 evaluation is chiefly a
language tour plus one substantial case study; it does not establish low
annotation cost across ordinary projects. It also does not model human
approval, external jobs, or evidence provenance.

## Derived work

- [Language-Integrated Specifications and Governance](../20-notes/language-integrated-specifications-and-governance.md)
- [Language-Integrated Specifications and Governance map](../10-maps/language-integrated-specifications-and-governance.md)
