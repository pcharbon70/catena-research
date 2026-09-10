---
title: "Diagnostic Contract"
kind: map
created: "2026-09-10"
tags: [specification, diagnostics, tooling, source-location]
aliases: []
---

# Diagnostic Contract (`60-specification/diagnostic-contract`)

## Purpose

The normative structured diagnostic and repair-evidence boundary under
[Specification Authority](../../SPECIFICATION-AUTHORITY.md),
[Catena Conformance Vocabulary](../../CONFORMANCE-VOCABULARY.md), and
[Catena Implementation Limits and Portability](../../IMPLEMENTATION-LIMITS.md).

## What belongs here

Rules for related source locations, type presentation, causal provenance,
coverage and guard explanations, generated origins, and structured edits.

## Index

### Subdirectories

None yet.

### Documents

- [Structured Explanations and Repairs](structured-explanations-and-repairs.md) — P117's revision 0.1.91 semantic diagnostic contract and P109 hold.

## Variability register

Implementations may present additional technical detail after the required
bounded source-level explanation and may decline to offer a repair. Consumer
wording for the fixed `unspecified` applicability class may vary. They must
preserve stable identities, exact locations, provenance bounds, and edit
applicability.

## Maintaining this index

Keep diagnostic producers, reports, source coordinates, generated metadata,
migration edits, conformance traceability, and P109 parse coverage aligned.
