---
title: "Text and Binary Model"
kind: map
created: "2026-09-09"
tags: [specification, unicode, conformance]
aliases: []
---

# Text and Binary Model (`60-specification/text-binary-model`)

## Purpose

C104's exact `0.1.66` text/binary operations and compiled adoption under
[authority](../../SPECIFICATION-AUTHORITY.md),
[conformance vocabulary](../../CONFORMANCE-VOCABULARY.md), and
[implementation limits](../../IMPLEMENTATION-LIMITS.md).

## What belongs here

Index units, pinned Unicode algorithms, strict encodings, pure composition,
checked binary segments and retained-input artifact contracts.

## Index

### Subdirectories

None yet.

### Documents

- [Units, Unicode and Checked Binary Operations](units-unicode-and-checked-binary-operations.md) —
  explicit library meaning and executable adoption without public syntax selection.

## Variability register

Unicode 17.0.0, UAX #29 revision 47 and UAX #15 revision 57 are fixed. Units,
normalization form, encoding, fragment roles and binary segment details are
explicit inputs. Patterns and pipelines admit at most 253 entries, integer
fields 1–4096 bits with byte-aligned little endian. C095 node/byte/depth budgets
and inherited source/generated-code/runtime limits apply. No implicit locale,
normalization, BOM adjustment or host-default encoding is admitted.

## Maintaining this index

Update the chapter, journal, source provenance, conformance map and checklist
with every changed rule or bound. Keep public syntax adoption separately held.
