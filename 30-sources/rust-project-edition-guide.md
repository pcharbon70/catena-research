---
title: "The Rust Edition Guide"
kind: source
created: "2026-08-05"
authors:
  - "The Rust Project"
published: null
citation_key: "rustProjectEditionGuide"
container: "The Rust Edition Guide"
edition: null
isbn: null
doi: null
url: "https://doc.rust-lang.org/edition-guide/editions/"
accessed: "2026-08-05"
tags:
  - compatibility
  - language-design
  - migration
aliases:
  - "Rust editions and migrations"
---

# The Rust Edition Guide

## Reference

The Rust Project. “What are editions?” and “Advanced migrations.” *The Rust
Edition Guide*, current online edition accessed 2026-08-05.
[Official guide](https://doc.rust-lang.org/edition-guide/editions/) and
[advanced migration chapter](https://doc.rust-lang.org/beta/edition-guide/editions/advanced-migrations.html).

## Contribution

The guide describes a package-local compatibility selection that permits
explicitly adopted language changes without dividing dependencies into
separate ecosystems. It also documents a migration workflow built from
diagnostics, mechanically applicable edits, rechecking, rollback, and manual
work where an automatic transformation cannot preserve intent.

## Method

This is official design and user documentation rather than an empirical
evaluation. It states the Rust project's intended edition contract and the
behavior of its migration tooling.

## Findings

- Each package chooses an edition explicitly and can migrate independently.
- Dependencies written for different supported editions interoperate because
  the compiler lowers them through shared semantic representations.
- A current compiler retains support for earlier editions.
- Edition migration diagnostics try to produce code valid before and after
  the transition.
- Automatic edits are rechecked and rolled back on failure; generated code,
  macros, and ambiguous intent can still require manual work.

## Relevance

Catena adopts package-local selection, retained earlier selections,
edition-neutral interfaces, and the rule that automation must not guess at
semantic intent. It deliberately uses `major.minor` edition names and exact
revision pins rather than Rust's calendar labels, and it records named
previews independently rather than inheriting Rust's feature mechanisms.

## Limits

The guide does not prove that all edition migrations are semantics-preserving,
nor does it define Catena's version axes, BEAM artifacts, governance records,
or pre-1.0 compatibility policy. Rust's macro system and release cadence are
not direct Catena constraints.

## Derived work

- [Language Editions and Feature Lifecycle](../20-notes/language-editions-and-feature-lifecycle.md)
- [How Should Catena Version Editions and Language Features?](../40-inquiries/how-should-catena-version-editions-and-language-features.md)
- [Language Editions and Feature Lifecycle map](../10-maps/language-editions-and-feature-lifecycle.md)
