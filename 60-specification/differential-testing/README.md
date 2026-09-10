---
title: "Differential Testing"
kind: map
created: "2026-09-10"
tags: [specification, testing, conformance, semantics]
aliases: []
---

# Differential Testing (`60-specification/differential-testing`)

## Purpose

The normative contract for comparing independent Catena reference and BEAM
executions through declared observations, generated admitted programs, hostile
mutations, and durable minimized counterexamples under
[specification authority](../../SPECIFICATION-AUTHORITY.md), the
[conformance vocabulary](../../CONFORMANCE-VOCABULARY.md), and
[implementation limits](../../IMPLEMENTATION-LIMITS.md).

## What belongs here

Rules for generator independence, exact and allowed-set comparison, boundary
matrices, mutation detection, shrinking, retained-corpus identity, finite
bounds, and the limits of empirical agreement.

## Index

### Subdirectories

None yet.

### Documents

- [Generated and Adversarial Agreement](generated-and-adversarial-agreement.md) — C134's revision 0.1.85 differential execution, mutation, shrinking, and counterexample contract.

## Variability register

Implementations publish positive generation, semantic-fuel, schedule,
shrink-step, and host-time limits. A scenario may declare an allowed finite
observation set only where its governing semantics permit variability.

## Maintaining this index

Keep the reference evaluator, testing tools, optimizer comparison path,
retained corpus, lifecycle profile, trust inventory, and conformance
traceability synchronized with this contract. Public source generation remains
held by P109.
