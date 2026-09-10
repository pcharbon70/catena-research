---
title: "Distribution"
kind: map
created: "2026-09-10"
tags: [specification, concurrency, distribution, security]
aliases: []
---

# Distribution (`60-specification/distribution`)

## Purpose

Authenticated remote service identity, typed canonical framing, bounded
admission, compatibility refusal, and explicit delivery uncertainty under
[authority](../../SPECIFICATION-AUTHORITY.md),
[conformance vocabulary](../../CONFORMANCE-VOCABULARY.md), and
[implementation limits](../../IMPLEMENTATION-LIMITS.md).

## What belongs here

Rules for crossing a node boundary without turning local process handles,
arbitrary host terms, credentials, or delivery assumptions into portable
language behavior.

## Index

### Subdirectories

None yet.

### Documents

- [Typed Authenticated Transport](typed-authenticated-transport.md) — C091's
  node, protocol, wire, authentication, failure, and compatibility contract.

## Variability register

Implementations configure addresses, certificate files, trusted authorities,
peer fingerprints, positive timeouts, and capacities. They may support
additional transport adapters only when each adapter preserves the same typed
frame, authentication, admission, and failure obligations. Every selected
value and supported adapter is disclosed; no bounded unspecified presentation
is admitted.

## Maintaining this index

Update the transport profile, trust inventory, executable model, compatibility
fixtures, traceability register, lifecycle record, and completion checklist
with this chapter.
