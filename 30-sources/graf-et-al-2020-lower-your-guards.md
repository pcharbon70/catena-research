---
title: "Lower Your Guards: A Compositional Pattern-Match Coverage Checker"
kind: source
created: "2026-08-01"
authors:
  - "Sebastian Graf"
  - "Simon Peyton Jones"
  - "Ryan G. Scott"
published: 2020
citation_key: "grafEtAl2020LowerYourGuards"
container: "Proceedings of the ACM on Programming Languages 4 (ICFP), Article 107"
edition: null
isbn: null
doi: "10.1145/3408989"
url: "https://doi.org/10.1145/3408989"
accessed: "2026-08-01"
tags:
  - compilers
  - pattern-matching
aliases:
  - "Lower Your Guards"
  - "LYG coverage checker"
---

# Lower Your Guards: A Compositional Pattern-Match Coverage Checker

## Reference

Sebastian Graf, Simon Peyton Jones, and Ryan G. Scott, “Lower Your Guards: A
Compositional Pattern-Match Coverage Checker,” *Proceedings of the ACM on
Programming Languages* 4, ICFP, Article 107 (August 2020), 30 pages.
[DOI](https://doi.org/10.1145/3408989) and
[author-hosted PDF](https://pp.ipd.kit.edu/uploads/publikationen/graf20lyg.pdf).

## Research question

Can a coverage checker remain compositional and precise when source patterns
include Boolean guards, pattern guards, view patterns, GADTs, strictness, and
other non-structural features?

## Method

The paper desugars a rich Haskell pattern language into a small guard-tree
intermediate representation. Recursive analyses annotate that tree with
refinement types and compute uncovered inputs, accessible right-hand sides,
and divergent matches. The authors implemented the design in GHC, evaluated
regression and adversarial cases, and compared it with the earlier GHC
checker.

## Findings

- Coverage becomes difficult once “pattern matching” includes arbitrary
  expressions, pattern guards, programmable patterns, GADT equalities, and
  evaluation behavior. Exhaustiveness of arbitrary Boolean predicates is
  undecidable in general.
- Structural patterns, Boolean guards, pattern guards, and view patterns can
  be elaborated into one ordered guard-tree representation containing
  evaluation, constructor tests, bindings, sequencing, choice, and selected
  right-hand sides.
- The checker computes refinement descriptions of covered, uncovered,
  accessible, and divergent inputs. A separate inhabitation step turns those
  descriptions into useful witnesses.
- The term-reasoning component is deliberately extensible. The base system
  does not prove arithmetic partitions such as positive/zero/negative integers
  exhaustive, though a stronger solver could.
- The implementation fixed numerous GHC coverage issues. On the selected
  performance-regression suite, most cases improved; for ordinary programs,
  coverage time remained a small portion of desugaring time.

## Relevance

Catena should introduce a guard-tree or equivalent typed decision IR before
coverage analysis and backend lowering. That shared semantic form can preserve
top-to-bottom fallthrough while allowing structural patterns, Boolean
conditions, and later extensions to elaborate independently.

The paper also supports a strict separation between the guard language and the
coverage oracle. Admitting a guard expression does not require the compiler to
prove every proposition it expresses.

## Limits

The formalism and implementation target lazy Haskell and its unusually rich
pattern language. Catena's proposed first release excludes many of those
features and can use a smaller tree. The published checker is not a proof that
an SMT-backed guard language will be predictable, nor does it address BEAM
selective receive or explicit effect rows.

## Derived work

- [Clause Guards](../20-notes/clause-guards.md)
- [How Should Catena Design Clause Guards?](../40-inquiries/how-should-catena-design-clause-guards.md)
- [Clause Guards map](../10-maps/clause-guards.md)
