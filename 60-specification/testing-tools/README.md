---
title: "Testing Tools"
kind: map
created: "2026-09-10"
tags: [specification, testing, conformance, tooling]
aliases: []
---

# Testing Tools (`60-specification/testing-tools`)

## Purpose

The internal bounded execution and evidence contract for Catena unit, law,
property, model, concurrency, and specification tests under
[authority](../../SPECIFICATION-AUTHORITY.md),
[conformance vocabulary](../../CONFORMANCE-VOCABULARY.md), and
[implementation limits](../../IMPLEMENTATION-LIMITS.md).

## What belongs here

Rules for test and subject identity, deterministic seeds, typed generators,
invariant-preserving shrinking, effect accounting, owned-process cleanup,
distinct execution bounds, evidence scope, and conformance reporting.

## Index

### Subdirectories

None yet.

### Documents

- [Isolated Seeded and Scoped Runs](isolated-seeded-and-scoped-runs.md) — C122's bounded test-plan, execution, shrinking, cleanup, and evidence contract.

## Variability register

Implementations publish positive host-timeout, observation-count, generator-size,
and shrink-step limits. These finite tool limits do not change language
divergence, schedule, effect, or proof semantics.

## Maintaining this index

Keep the reference evaluator, future differential generator, assurance checker,
build runner, documentation examples, public-syntax hold, trust inventory, and
traceability synchronized with this contract.
