---
title: "Message Semantics"
kind: map
created: "2026-09-10"
tags: [specification, concurrency, runtime, foreign-boundary]
aliases: []
---

# Message Semantics (`60-specification/message-semantics`)

## Purpose

The integrated local, capacity-sensitive, foreign, and remote message contract
under [authority](../../SPECIFICATION-AUTHORITY.md),
[conformance vocabulary](../../CONFORMANCE-VOCABULARY.md), and
[implementation limits](../../IMPLEMENTATION-LIMITS.md).

## What belongs here

Message value observations, validation and admission, copy/share
representation freedom, sender order, overload, dead-target, native authority,
and remote delivery outcomes.

## Index

### Subdirectories

None yet.

### Documents

- [Values, Capacity, and Transport](values-capacity-and-transport.md) — C085's
  integrated message contract across all admitted boundaries.

## Variability register

Physical copying and immutable storage sharing are unobservable. Raw mailbox
capacity remains deployment-defined. Explicit capacity services select positive
count and byte bounds and a published overload policy. Remote configuration
retains C091's declared choices. No bounded unspecified presentation is
admitted.

## Maintaining this index

Keep the C010, C037, C085, C087, C091, C095, C097, and C129 boundaries,
machine profile, implementation tests, traceability register, lifecycle record,
and checklist synchronized.
