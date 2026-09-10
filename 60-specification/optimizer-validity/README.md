---
title: "Optimizer Validity"
kind: map
created: "2026-09-10"
tags: [specification, optimization, semantics, conformance]
aliases: []
---

# Optimizer Validity (`60-specification/optimizer-validity`)

## Purpose

The normative checked-optimization contract under
[specification authority](../../SPECIFICATION-AUTHORITY.md), the
[conformance vocabulary](../../CONFORMANCE-VOCABULARY.md), and
[implementation limits](../../IMPLEMENTATION-LIMITS.md).

## What belongs here

Rules for transformation inventories, explicit optimizer selection, admitted
rewrite premises, replayable certificates, independent core verification,
observation preservation, refusal, determinism, and evidence limits.

## Index

### Subdirectories

None yet.

### Documents

- [Checked Rewrites and Observation Preservation](checked-rewrites-and-observation-preservation.md) — C135's revision 0.1.86 optimizer domain, certificate, refusal, and conformance contract.

## Variability register

Implementations may leave optimization disabled. A conforming `0.1.86` checked
mode exposes exactly the rule inventory and certificate format defined here;
additional transformations require their own later normative revision.

## Maintaining this index

Keep typed-core and kernel verification, backend options, differential tests,
debug provenance, trust inventory, lifecycle metadata, and conformance
traceability synchronized. Do not infer optimizer authority from library-law
tests or backend output.
