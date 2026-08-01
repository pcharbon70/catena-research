---
title: "Monads for Functional Programming"
kind: source
created: "2026-07-31"
authors:
  - "Philip Wadler"
published: 1995
citation_key: "wadler1995MonadsFunctionalProgramming"
container: "Advanced Functional Programming, Lecture Notes in Computer Science 925: 24–52"
edition: null
isbn: "978-3-540-59451-2"
doi: "10.1007/3-540-59451-5_2"
url: "https://homepages.inf.ed.ac.uk/wadler/papers/marktoberdorf/baastad.pdf"
accessed: "2026-07-31"
tags:
  - effects
  - functional-programming
  - monads
  - program-structure
aliases:
  - "Wadler on monadic programming"
---

# Monads for Functional Programming

## Reference

Philip Wadler, “Monads for Functional Programming,” in *Advanced Functional
Programming*, Lecture Notes in Computer Science 925 (1995), 24–52.
[DOI](https://doi.org/10.1007/3-540-59451-5_2),
[author manuscript](https://homepages.inf.ed.ac.uk/wadler/papers/marktoberdorf/baastad.pdf),
and [bibliographic record](https://dblp.org/rec/conf/afp/Wadler95.html).

## Contribution

Wadler translates the semantic monad structure into a practical method for
organizing functional programs. The tutorial develops common combinators and
applies them to evaluator construction, state-like array updates, and parsing.

## Method

Three extended examples are written first in direct specialized styles and
then factored through monadic operations. The evaluator case varies the
computational behavior while retaining the expression traversal; the array
and parser cases demonstrate state and nondeterministic sequencing.

## Findings

- A shared sequencing interface factors repetitive plumbing out of functional
  code while leaving the control dependency visible in the type.
- Generic combinators can be reused across otherwise different notions of
  computation.
- The evaluator examples show a modularity benefit: changing the monad changes
  how a computation behaves without rewriting every recursive clause.
- A convenient `do`-like notation is elaboration over the core operations, not
  the definition of a monad.

## Relevance

This paper bridges Moggi's semantics and actual library design. For Catena,
the useful design unit is the small lawful interface plus syntax that does not
hide which abstraction is being sequenced. Monadic libraries remain valuable
even if native algebraic handlers provide the default mechanism for language
effects.

## Limits

The work is tutorial and example driven. It does not compare comprehension,
maintenance, or runtime cost against modern direct effects, applicative
interfaces, or handlers. Transformer composition, cancellation, resource
safety, and instance coherence are outside its scope.

## Derived work

- [Category Theory for Programming](../20-notes/category-theory-for-programming.md)
- [Algebraic Effects and Handlers](../20-notes/algebraic-effects-and-handlers.md)
- [How Should Catena Specify Its Initial Categorical Hierarchy?](../40-inquiries/how-should-catena-specify-its-initial-categorical-hierarchy.md)
- [Category Theory for Programming map](../10-maps/category-theory-for-programming.md)
