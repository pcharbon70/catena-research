---
title: "Debugging Metadata"
kind: map
created: "2026-09-09"
tags: [specification, compiler, conformance]
aliases: []
---

# Debugging Metadata (`60-specification/debugging-metadata`)

## Purpose

C100's verified source/runtime/evidence navigation at exact `0.1.64`, following
[authority](../../SPECIFICATION-AUTHORITY.md),
[conformance vocabulary](../../CONFORMANCE-VOCABULARY.md), and
[implementation limits](../../IMPLEMENTATION-LIMITS.md).

## What belongs here

Source identity, generated origin chains, bounded inlining, default-redacted
frames, stripped runtime locations and external erased-evidence references.

## Index

### Subdirectories

None yet.

### Documents

- [Verified Origins and Redacted Frames](verified-origins-and-redacted-frames.md) —
  source-bound sidecars and exact runtime mapping without evidence embedding.

## Variability register

The explicit profile defaults to sidecar mode, inline depth zero, eight origin
chain entries, 100,000 lowered nodes and 1,048,576 source bytes. Allowed inline
depth is 0–8, chain length 1–64, lowered nodes 1–1,000,000 and source bytes positive.
Stripped mode omits runtime line mapping. C095 bounds govern optional disclosure;
parser, generated code and allocation limits retain the standing policy.

## Maintaining this index

Keep the chapter, conformance map, implementation evidence and checklist in sync.
Do not treat optimizer-elided or stripped frames as known source locations.
