---
title: "The Update Framework Specification"
kind: source
created: "2026-08-03"
authors:
  - "The Update Framework community"
published: null
citation_key: "theUpdateFrameworkSpecification"
container: null
edition: "1.0 series"
isbn: null
doi: null
url: "https://theupdateframework.github.io/specification/latest/"
accessed: "2026-08-03"
tags:
  - cryptography
  - governance
  - provenance
  - supply-chain-security
aliases:
  - "TUF specification"
---

# The Update Framework Specification

## Reference

The Update Framework community. *The Update Framework Specification*, latest
1.0-series publication consulted 2026-08-03.
[Versioned specification](https://theupdateframework.github.io/specification/latest/).

## Contribution

The specification defines signed metadata roles, distinct-key signature
thresholds, delegated scopes, versioned root metadata, rollback protection,
revocation by root replacement, and a continuity rule for root-key rotation.

## Method

It specifies file formats and a client workflow against explicit attacker
goals. For root rotation, each next root is checked against both the threshold
authorized by its immediate predecessor and the threshold declared by the new
root.

## Findings

- A signature threshold must count distinct authorized key IDs, never repeated
  signatures from one identity.
- Secure root replacement needs a chain of intermediate versions; accepting
  only the new root's own signatures would let newly asserted authority
  bootstrap itself.
- Root private keys should remain offline, and delegated authority should be
  bounded to named roles and targets.
- **Catena inference:** emergency replacement after threshold compromise needs
  separately predeclared recovery authority or a new out-of-band trust
  decision; the ordinary old-plus-new continuity rule cannot manufacture an
  uncompromised old threshold.

## Relevance

Catena 0.1.6 adapts dual-threshold root continuity, distinct-signer counting,
offline keys, scoped delegation, and explicit recovery to language governance.
It replaces wall-clock and repository-version assumptions with logical
sequence windows and an initially declared recovery quorum.

## Limits

TUF secures software-repository metadata and includes snapshot, timestamp,
expiry, download, and target-path concerns that do not define Catena language
semantics. Catena does not adopt TUF's repository protocol or claim that a TUF
implementation is interchangeable with its governance bundle.

## Derived work

- [Evidence, Identity, Trust, and Lifecycle](../60-specification/specifications-and-governance/evidence-identity-and-lifecycle.md)
- [Language-Integrated Specifications and Governance map](../10-maps/language-integrated-specifications-and-governance.md)
