---
title: "JSON Canonicalization Scheme"
kind: source
created: "2026-08-03"
authors:
  - "Anders Rundgren"
  - "Bray Jordan"
  - "Samuel Erdtman"
published: 2020
citation_key: "rundgrenEtAl2020jcs"
container: "RFC 8785"
edition: null
isbn: null
doi: "10.17487/RFC8785"
url: "https://www.rfc-editor.org/rfc/rfc8785.html"
accessed: "2026-08-03"
tags:
  - cryptography
  - json
  - provenance
aliases:
  - "RFC 8785"
---

# JSON Canonicalization Scheme

## Reference

Anders Rundgren, Bray Jordan, and Samuel Erdtman. “JSON Canonicalization
Scheme.” RFC 8785, June 2020.
[Canonical HTML](https://www.rfc-editor.org/rfc/rfc8785.html).

## Contribution

RFC 8785 defines deterministic JSON bytes for hashing and signing. It combines
the I-JSON input constraints, ECMAScript primitive serialization, no
insignificant whitespace, recursive object processing, and object-name order
by unsigned UTF-16 code units.

## Method

The RFC gives normative algorithms, worked values, interoperability guidance,
and test data. Its number table serializes IEEE 754 minus zero as `0`; Catena's
integer-only profile instead rejects a `-0` input lexeme as a deliberately
stricter local rule.

## Findings

- A cryptographic protocol cannot safely sign arbitrary serializer output;
  every verifier must reproduce the same bytes.
- Duplicate object names and invalid Unicode are invalid inputs rather than
  values a canonicalizer may repair.
- Object names sort in their unescaped form by UTF-16 code units recursively,
  including objects nested in arrays.
- The JSON number model creates avoidable ambiguity for a language protocol
  that needs only counters, thresholds, and sizes.

## Relevance

Catena 0.1.6 uses JCS for semantic digests and every signed governance payload.
It narrows the profile to safe integers and rejects floats and negative zero,
removing number-format interoperability from the initial assurance base.

## Limits

RFC 8785 is an informational RFC, not an authorization or signature protocol.
It does not define domain separation, trust roots, lifecycle replay, or which
fields an application must sign.

## Derived work

- [Evidence, Identity, Trust, and Lifecycle](../60-specification/specifications-and-governance/evidence-identity-and-lifecycle.md)
- [Language-Integrated Specifications and Governance map](../10-maps/language-integrated-specifications-and-governance.md)
