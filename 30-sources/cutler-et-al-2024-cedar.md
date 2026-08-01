---
title: "Cedar: A New Language for Expressive, Fast, Safe, and Analyzable Authorization"
kind: source
created: "2026-08-01"
authors:
  - "Joseph W. Cutler"
  - "Craig Disselkoen"
  - "Aaron Eline"
  - "Shaobo He"
  - "Kyle Headley"
  - "Michael Hicks"
  - "Kesha Hietala"
  - "Eleftherios Ioannidis"
  - "John Kastner"
  - "Anwar Mamat"
  - "Darin McAdams"
  - "Matt McCutchen"
  - "Neha Rungta"
  - "Emina Torlak"
  - "Andrew Wells"
published: 2024
citation_key: "cutlerEtAl2024cedar"
container: "Proceedings of the ACM on Programming Languages 8(OOPSLA1), Article 118"
edition: null
isbn: null
doi: "10.1145/3649835"
url: "https://www.amazon.science/publications/cedar-a-new-language-for-expressive-fast-safe-and-analyzable-authorization"
accessed: "2026-08-01"
tags:
  - authorization
  - language-design
  - policy
aliases:
  - "Cedar authorization language"
---

# Cedar: A New Language for Expressive, Fast, Safe, and Analyzable Authorization

## Reference

Joseph W. Cutler et al. “Cedar: A New Language for Expressive, Fast, Safe, and
Analyzable Authorization.” *Proceedings of the ACM on Programming Languages*
8, OOPSLA1, article 118 (2024).
[DOI](https://doi.org/10.1145/3649835).

## Contribution

Cedar separates authorization policy from application control flow and gives
requests, principals, actions, resources, context, and policy evaluation a
purpose-built semantics. Its restricted structure is designed for readable
policies, predictable evaluation, optional validation, and exact logical
analysis.

## Method

The paper describes the language and evaluator, gives a sound and complete
logical encoding for analysis, reports mechanized proofs of core properties,
and compares readability and performance with two policy systems.

## Findings

- A narrow authorization language can be easier to analyze than arbitrary
  predicates embedded throughout application code.
- Policy validation can use an entity schema to catch mistakes without making
  every policy depend on static typing.
- A precise logical encoding supports questions beyond individual requests,
  including whether a policy refactor changes the authorized set.
- Mechanizing the language model can expose assumptions that ordinary tests of
  the production evaluator may miss.

## Relevance

Catena governance needs an explicit answer to “who may perform this transition
for this artifact under this context?” That is an authorization decision, not
a mathematical proof that the artifact is correct. Keeping policy restricted
and analyzable prevents arbitrary application effects from entering promotion
decisions.

## Limits

Authorization is only as accurate as the policies, entity data, request
context, and identity binding supplied to the evaluator. The work does not
establish that an approved claim is true, that an external test ran, or that a
signer’s key should be trusted. Its comparative readability evidence is partly
subjective and domain-specific.

## Derived work

- [Language-Integrated Specifications and Governance](../20-notes/language-integrated-specifications-and-governance.md)
- [Language-Integrated Specifications and Governance map](../10-maps/language-integrated-specifications-and-governance.md)
