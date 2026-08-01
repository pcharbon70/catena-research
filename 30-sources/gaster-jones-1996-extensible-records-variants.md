---
title: "A Polymorphic Type System for Extensible Records and Variants"
kind: source
created: "2026-07-31"
authors:
  - "Benedict R. Gaster"
  - "Mark P. Jones"
published: 1996
citation_key: "gasterJones1996ExtensibleRecordsVariants"
container: "University of Nottingham Technical Report NOTTCS-TR-96-3"
edition: null
isbn: null
doi: null
url: "https://web.cecs.pdx.edu/~mpj/pubs/96-3.pdf"
accessed: "2026-07-31"
tags:
  - extensible-records
  - qualified-types
  - row-polymorphism
  - variants
aliases:
  - "Gaster–Jones rows"
---

# A Polymorphic Type System for Extensible Records and Variants

## Reference

Benedict R. Gaster and Mark P. Jones, “A Polymorphic Type System for
Extensible Records and Variants,” University of Nottingham Technical Report
NOTTCS-TR-96-3 (November 1996).
[Author-hosted paper](https://web.cecs.pdx.edu/~mpj/pubs/96-3.pdf).

## Contribution

The paper develops a practical row-based type system for extensible records and
variants. It combines polymorphic operations, effective inference, and a
compilation strategy by expressing row constraints through qualified types.

## Method

The authors define record and variant constructors over a distinct row kind,
give types to selection, extension, injection, and elimination operations, and
use predicates such as “row `r` lacks label `l`” to ensure label uniqueness.
They then generalize labels to first-class values and give an
evidence-parameter implementation in which row predicates supply offsets.

## Findings

- Record and variant polymorphism can be expressed as an extension of an
  HM-style qualified type system rather than through nominal subtyping.
- Rows need their own kind, so ordinary value types cannot be substituted where
  rows are expected.
- If labels must be unique, extension needs an explicit lacks predicate. The
  constraint is semantic, not merely an implementation check.
- Row predicates can carry compilation evidence, such as field offsets, much
  as class predicates carry dictionaries.
- First-class labels are possible but add expressive and implementation
  machinery beyond ordinary fixed-label row polymorphism.

## Relevance

This gives a principled option for structural data in a greenfield Catena. It
also shows why record rows and effect rows should not automatically share one
equality theory: unique fields naturally use lacks constraints, whereas effect
elimination may benefit from duplicate labels.

## Limits

The work is a technical report and does not cover algebraic effects,
higher-rank polymorphism, GADTs, or a modern module system. Its first-class
label machinery is optional for the greenfield proposal and should not be
included without a clear user need.

## Derived work

- [Algebraic Data Types](../20-notes/algebraic-data-types.md)
- [How Should Catena Specify Algebraic Data Types?](../40-inquiries/how-should-catena-specify-algebraic-data-types.md)
- [Algebraic Data Types map](../10-maps/algebraic-data-types.md)
- [A Greenfield Type System for Catena](../20-notes/catena-greenfield-type-system.md)
- [What Should a Greenfield Catena Type System Guarantee?](../40-inquiries/what-should-a-greenfield-catena-type-system-guarantee.md)
- [Catena Type-System Design](../10-maps/catena-type-system-design.md)
