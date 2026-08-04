---
title: "Edwards-Curve Digital Signature Algorithm"
kind: source
created: "2026-08-03"
authors:
  - "Simon Josefsson"
  - "Ilari Liusvaara"
published: 2017
citation_key: "josefssonLiusvaara2017eddsa"
container: "RFC 8032"
edition: null
isbn: null
doi: "10.17487/RFC8032"
url: "https://www.rfc-editor.org/info/rfc8032/"
accessed: "2026-08-03"
tags:
  - cryptography
  - governance
  - provenance
aliases:
  - "RFC 8032"
  - "Ed25519 specification"
---

# Edwards-Curve Digital Signature Algorithm

## Reference

Simon Josefsson and Ilari Liusvaara. “Edwards-Curve Digital Signature
Algorithm (EdDSA).” RFC 8032, January 2017.
[RFC record and text](https://www.rfc-editor.org/info/rfc8032/).

## Contribution

RFC 8032 specifies Ed25519 and Ed448 key, signing, verification, encoding, and
test-vector behavior. Catena's bounded protocol uses the pure Ed25519 variant
with an empty Ed25519 context and performs application-level domain separation
in the signed message.

## Method

The RFC supplies the algorithms, parameter sets, encodings, security
considerations, and known-answer vectors for interoperable implementations.

## Findings

- Public-key verification establishes that the holder of a corresponding
  private key signed exact bytes; it does not establish the truth of their
  meaning or the signer's authority.
- Test vectors are necessary to catch key, signature, message, and variant
  encoding mistakes that local sign/verify round trips can share.
- An application must keep signed message domains distinct; Catena does that
  by prefixing canonical payload bytes with a versioned payload kind.

## Relevance

Catena 0.1.6 needs a small offline signature contract for evidence, approvals,
transitions, delegations, and trust-root changes. Ed25519 is supported by the
OTP 29 cryptographic runtime used by the bootstrap compiler, so the compiler
can verify without owning private keys.

## Limits

The RFC does not prescribe organizational roles, thresholds, revocation,
recovery, payload canonicalization, or key storage ceremonies. Those remain
application protocol responsibilities.

## Derived work

- [Evidence, Identity, Trust, and Lifecycle](../60-specification/specifications-and-governance/evidence-identity-and-lifecycle.md)
- [Language-Integrated Specifications and Governance map](../10-maps/language-integrated-specifications-and-governance.md)
