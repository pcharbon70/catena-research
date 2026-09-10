---
title: "Supply-Chain Policy"
kind: map
created: "2026-09-10"
tags: [specification, conformance, security, supply-chain-security]
aliases: []
---

# Supply-Chain Policy (`60-specification/supply-chain-policy`)

## Purpose

Authenticated package publication and immutable acquisition under
[authority](../../SPECIFICATION-AUTHORITY.md),
[conformance vocabulary](../../CONFORMANCE-VOCABULARY.md), and
[implementation limits](../../IMPLEMENTATION-LIMITS.md).

## What belongs here

Registry roots, signed snapshots, publisher delegation, release status, mirror
verification, locked replay, and source or native acquisition provenance.

## Index

### Subdirectories

None yet.

### Documents

- [Signed Registry and Immutable Acquisition](signed-registry-and-immutable-acquisition.md)
  — C130's authenticated registry and package acquisition contract.

## Variability register

The chapter fixes document shapes, signing domains, SHA-256 content identity,
status meanings, replay rules, ceilings, and refusal. Trust-root delivery, clock
integrity, key custody, mirror availability, storage, and admitted native code
remain declared host responsibilities. No implementation-defined registry
semantics or bounded unspecified presentation is admitted.

## Maintaining this index

Update registry metadata, compiler profile, attack fixtures, journal,
traceability, lifecycle records, and checklist together.
