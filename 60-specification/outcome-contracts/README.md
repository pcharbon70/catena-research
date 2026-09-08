---
title: "Outcome Contracts"
kind: map
created: "2026-09-08"
tags:
  - specification
  - algebraic-data-types
aliases: []
---

# Outcome Contracts (`60-specification/outcome-contracts`)

## Purpose

The C103 ordinary outcome library contract at `0.1.54`, governed by the
[authority policy](../../SPECIFICATION-AUTHORITY.md),
[conformance vocabulary](../../CONFORMANCE-VOCABULARY.md), and
[implementation limits](../../IMPLEMENTATION-LIMITS.md).

## What belongs here

Optional and dependent values, independent validation, categorical coherence,
explicit conversions and operational obligations without new public names.

## Index

### Subdirectories

None yet.

### Documents

- [Outcome Values, Sequencing and Validation](values-sequencing-and-validation.md) —
  normative meanings and eight outcome obligations.

## Variability register

No new implementation-defined choice, presentation allowance or finite limit.
Allocation inherits the standing runtime-capacity policy. Error concatenation
has a specified linear cost in the combined input count; callback costs are
separate. Package layout and digest binding are fixed for this implementation
contract.

## Maintaining this index

Keep this complete inventory, authority, version registry, evidence and
traceability synchronized with changes to the contract.
