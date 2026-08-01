---
title: "Applying Design by Contract"
kind: source
created: "2026-08-01"
authors:
  - "Bertrand Meyer"
published: 1992
citation_key: "meyer1992applying"
container: "Computer 25(10)"
edition: null
isbn: null
doi: "10.1109/2.161279"
url: "https://www.kth.se/social/files/59526bfb56be5b4f17000807/meyer-92-contracts.pdf"
accessed: "2026-08-01"
tags:
  - contracts
  - formal-methods
  - language-design
aliases:
  - "Applying 'Design by Contract'"
---

# Applying Design by Contract

## Reference

Bertrand Meyer. “Applying ‘Design by Contract’.” *Computer* 25, no. 10
(1992): 40–51. [DOI](https://doi.org/10.1109/2.161279).

## Contribution

Meyer presents contracts as executable interface obligations rather than
informal comments. Preconditions describe what a caller must establish,
postconditions describe what an operation guarantees, and class invariants
describe properties preserved across public operations.

## Method

The article explains the discipline through language examples and connects
contracts to inheritance, exception handling, documentation, testing, and
debugging. It is a design argument and experience report, not a controlled
empirical comparison.

## Findings

- A contract allocates responsibility: violating a precondition implicates the
  client, while violating a postcondition or invariant implicates the supplier.
- Contract clauses can serve several tools because their meaning is part of the
  language: runtime checking, documentation extraction, and systematic tests
  can share the same declaration.
- Subtype redefinition cannot arbitrarily strengthen what clients must provide
  or weaken what implementations promise without breaking substitutability.

## Relevance

The work establishes the smallest useful unit for Catena’s specification
feature: a claim with defined evaluation points, an accountable boundary, and a
failure meaning. It also shows why prose requirements alone cannot support
reliable enforcement.

## Limits

The article’s responsibility model is first-order and object-oriented. It does
not solve delayed checking for higher-order values, concurrent histories,
external evidence, authorization, or governance lifecycle. Runtime contract
success also covers only executions that actually occur.

## Derived work

- [Language-Integrated Specifications and Governance](../20-notes/language-integrated-specifications-and-governance.md)
- [Language-Integrated Specifications and Governance map](../10-maps/language-integrated-specifications-and-governance.md)
