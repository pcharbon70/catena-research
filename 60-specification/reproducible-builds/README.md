---
title: "Reproducible Builds"
kind: map
created: "2026-09-09"
tags: [specification, conformance, security]
aliases: []
---

# Reproducible Builds (`60-specification/reproducible-builds`)

## Purpose

Exact build-input identity and full-output comparison under
[authority](../../SPECIFICATION-AUTHORITY.md),
[conformance vocabulary](../../CONFORMANCE-VOCABULARY.md) and
[implementation limits](../../IMPLEMENTATION-LIMITS.md).

## What belongs here

Reproducibility envelopes, closed generators, canonical archives and publication.
Registry authentication and new governance events remain separate contracts.

## Index

### Subdirectories

None yet.

### Documents

- [Exact Inputs and Canonical Packages](exact-inputs-and-canonical-packages.md) —
  C128's independent build and archive assurance contract.

## Variability register

The chapter fixes input/output ceilings, generator forms and archive metadata.
The supported OTP and host filesystem contracts retain their own responsibilities;
no cross-toolchain or power-loss durability promise is implied.

## Maintaining this index

Update the normative chapter, profile, journal, traceability and checklist together.
