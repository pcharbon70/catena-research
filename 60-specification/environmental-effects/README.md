---
title: "Environmental Effects"
kind: map
created: "2026-09-09"
tags: [specification, effects, entry-points, conformance]
aliases: []
---

# Environmental Effects (`60-specification/environmental-effects`)

## Purpose

C106's exact 0.1.68 authority channel under [authority](../../SPECIFICATION-AUTHORITY.md),
[conformance vocabulary](../../CONFORMANCE-VOCABULARY.md) and
[implementation limits](../../IMPLEMENTATION-LIMITS.md).

## What belongs here

Explicit launch authority, closed lexical handlers, environmental service contracts
and owned adapter cleanup without deciding public vocabulary.

## Index

### Subdirectories

None yet.

### Documents

- [Explicit Environmental Authority and Closed Launches](explicit-authority-and-closed-launches.md) —
  the C027/C082 amendment, eight services, attenuation, lifetime and executable evidence obligations.

## Variability register

Service schemas and profile bounds are fixed; grants, budgets, timeout, concurrency,
capacity and fake observations are explicit inputs. Initial grants cap at eight,
authorities at 64, bytes at 1,048,576, requests at 10,000, concurrency at 64 and
time/lifetime at 1,000,000 milliseconds. Policy text caps at 4,096 bytes, manifests
at 16,384, executable snapshots at 16,777,216; resource lists/argv/environments
cap at 256, endpoint maps at 64 and command maps at 32. Defaults, release grace,
exhaustion classes and inherited limits are fixed in the chapter. Real external
observations do not establish ambient authority.

## Maintaining this index

Update the amendment, decision journal, conformance map and checklist atomically.
Keep retained revisions and the public-vocabulary hold explicit.
