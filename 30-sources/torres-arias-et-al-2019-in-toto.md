---
title: "in-toto: Providing Farm-to-Table Guarantees for Bits and Bytes"
kind: source
created: "2026-08-01"
authors:
  - "Santiago Torres-Arias"
  - "Hammad Afzali"
  - "Trishank Karthik Kuppusamy"
  - "Reza Curtmola"
  - "Justin Cappos"
published: 2019
citation_key: "torresAriasEtAl2019inToto"
container: "28th USENIX Security Symposium"
edition: null
isbn: "978-1-939133-06-9"
doi: null
url: "https://www.usenix.org/conference/usenixsecurity19/presentation/torres-arias"
accessed: "2026-08-01"
tags:
  - governance
  - provenance
  - supply-chain-security
aliases:
  - "in-toto supply-chain guarantees"
---

# in-toto: Providing Farm-to-Table Guarantees for Bits and Bytes

## Reference

Santiago Torres-Arias, Hammad Afzali, Trishank Karthik Kuppusamy, Reza
Curtmola, and Justin Cappos. “in-toto: Providing Farm-to-Table Guarantees for
Bits and Bytes.” In *28th USENIX Security Symposium* (2019): 1393–1410.
[USENIX paper](https://www.usenix.org/conference/usenixsecurity19/presentation/torres-arias).

## Contribution

in-toto lets a project owner sign a supply-chain layout describing required
steps and authorized functionaries. Each performed step emits signed link
metadata over its materials and products, allowing a consumer to verify the
chain and detect omitted, reordered, or tampered steps.

## Method

The paper defines the threat model, metadata, workflow, and verification
procedure; integrates the framework into several real supply chains; measures
overheads; and analyzes 30 historical compromises against multiple deployment
configurations.

## Findings

- Evidence needs cryptographic binding to the exact artifacts, step, and actor;
  an unsigned statement that “tests passed” is not durable provenance.
- A signed normative layout and signed observed links play different roles:
  one states what must happen, while the others attest to what an actor reports
  doing.
- Thresholds and role separation reduce dependence on a single key or step,
  though the protection depends on the integration and trust assumptions.

## Relevance

Many Catena specification claims will be checked outside the compiler—for
example performance measurements, compatibility suites, or release builds.
This source motivates typed attestation records with artifact digests,
environment and tool identity, issuer, and a policy-governed verification path.

## Limits

Signatures establish origin and integrity, not the semantic truth or adequacy
of an authorized actor’s claim. Compromised keys, colluding functionaries,
incorrect layouts, incomplete instrumentation, and secrets outside the
captured artifacts remain trust boundaries. The framework secures process
provenance rather than proving program correctness.

## Derived work

- [Language-Integrated Specifications and Governance](../20-notes/language-integrated-specifications-and-governance.md)
- [Language-Integrated Specifications and Governance map](../10-maps/language-integrated-specifications-and-governance.md)
