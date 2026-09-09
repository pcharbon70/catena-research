---
title: "Trusted Obligation Policy"
kind: map
created: "2026-09-09"
tags: [specification, conformance, security]
aliases: []
---

# Trusted Obligation Policy (`60-specification/trusted-obligation-policy`)

## Purpose

C127's transitive foreign/native trust disclosure and scoped admission under
[authority](../../SPECIFICATION-AUTHORITY.md),
[conformance vocabulary](../../CONFORMANCE-VOCABULARY.md) and
[implementation limits](../../IMPLEMENTATION-LIMITS.md).

## What belongs here

Exact artifact sidecars, owning package responsibilities, dependency closure,
admission, attenuation and revocation. Native safety remains an explicit assumption.

## Index

### Subdirectories

None yet.

### Documents

- [Transitive Disclosure and Scoped Admission](transitive-disclosure-and-scoped-admission.md) —
  checked graph identity, owner-qualified obligations and executable policy.

## Variability register

The exact profile fixes 64 graph nodes, 256 edges and boundaries, 64 MiB serialized
inputs, 1 MiB canonical metadata and 64 policy scopes. Grants contain at most
32 acknowledgements of at most 128 UTF-8 bytes each; package names cap at 128 bytes.
Inherited execution budgets and cleanup behavior remain with the owning adapter.
No choice permits unchecked intralanguage operations or claims native safety.

## Maintaining this index

Update the policy, compiler inventory, evidence journal, traceability map and
checklist together when admission or trust exposure changes.
