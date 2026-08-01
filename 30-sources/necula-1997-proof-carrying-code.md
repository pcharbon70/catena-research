---
title: "Proof-Carrying Code"
kind: source
created: "2026-08-01"
authors:
  - "George C. Necula"
published: 1997
citation_key: "necula1997proofCarryingCode"
container: "Proceedings of POPL 1997"
edition: null
isbn: "0-89791-853-3"
doi: "10.1145/263699.263712"
url: "https://people.eecs.berkeley.edu/~necula/pcc.html"
accessed: "2026-08-01"
tags:
  - formal-methods
  - proof-carrying-code
  - security
aliases:
  - "PCC"
---

# Proof-Carrying Code

## Reference

George C. Necula. “Proof-Carrying Code.” In *Proceedings of POPL 1997*,
106–119. [DOI](https://doi.org/10.1145/263699.263712).

## Contribution

Proof-carrying code shifts proof construction to a producer. A consumer defines
a safety policy, receives code plus a machine-checkable proof, derives the
corresponding verification condition, and uses a comparatively simple checker
before admitting the code.

## Method

The paper formalizes the architecture and applies it to the safe interaction of
untrusted native code with a typed-language runtime. Related prototype cases
measure proof size and checking cost for low-level safety policies.

## Findings

- Verification can be decoupled from trust in the producer: the consumer need
  only trust the policy, condition generator, proof rules, and checker.
- A portable certificate can make an expensive producer-side argument cheap to
  validate repeatedly.
- The certificate must be bound to the exact code and exact policy it proves;
  a detached success bit has no comparable meaning.

## Relevance

Catena should prefer evidence that a small trusted kernel can recheck over an
opaque “solver succeeded” status. The architecture also clarifies governance:
the policy owner chooses what admission means, while an evidence producer
supplies a witness and does not grant itself authority.

## Limits

The guarantee is no stronger than the consumer’s policy and trusted checking
base. Proof production can be expensive and proof formats can be large or
tool-specific. The original case studies concern code safety, not human
approval, changing organizational roles, or arbitrary empirical evidence.

## Derived work

- [Language-Integrated Specifications and Governance](../20-notes/language-integrated-specifications-and-governance.md)
- [Language-Integrated Specifications and Governance map](../10-maps/language-integrated-specifications-and-governance.md)
