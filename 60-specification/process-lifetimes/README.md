---
title: "Process Lifetimes"
kind: map
created: "2026-09-08"
tags:
  - specification
  - actors
aliases: []
---

# Process Lifetimes (`60-specification/process-lifetimes`)

## Purpose

This area defines the normative C084 process-lifetime contract at exact
`0.1.52`, including owned task scopes and managed relationships.

The [authority policy](../../SPECIFICATION-AUTHORITY.md),
[conformance vocabulary](../../CONFORMANCE-VOCABULARY.md), and
[implementation limits](../../IMPLEMENTATION-LIMITS.md) govern this area.

## What belongs here

Owned task scopes, monitored completion, managed linked propagation, trapping
and their required cleanup boundary. General time admission remains G088.

## Index

### Subdirectories

None yet.

### Documents

- [Owned Tasks and Managed Relationships](owned-tasks-and-managed-relationships.md)
  — normative transition contract and conformance obligations for C084.

## Variability register

This area introduces no implementation-defined choice, presentation
allowance or implementation-limit dimension. Explicit graces are input;
clock and scheduler races are defined nondeterminism. Standing capacity and
reference-evidence limits retain their classifications.

## Maintaining this index

Inventory every direct child and update status, authority, traceability and
executable evidence together when changing this boundary.
