---
title: "Generalising Monads to Arrows"
kind: source
created: "2026-07-31"
authors:
  - "John Hughes"
published: 2000
citation_key: "hughes2000GeneralisingMonadsArrows"
container: "Science of Computer Programming 37(1–3): 67–111"
edition: null
isbn: null
doi: "10.1016/S0167-6423(99)00023-4"
url: "https://www.cse.chalmers.se/~rjmh/Papers/arrows.pdf"
accessed: "2026-07-31"
tags:
  - arrows
  - category-theory
  - combinator-libraries
  - program-structure
aliases:
  - "Hughes on arrows"
---

# Generalising Monads to Arrows

## Reference

John Hughes, “Generalising Monads to Arrows,” *Science of Computer
Programming* 37, nos. 1–3 (2000): 67–111.
[DOI and publisher record](https://doi.org/10.1016/S0167-6423(99)00023-4),
[author manuscript](https://www.cse.chalmers.se/~rjmh/Papers/arrows.pdf), and
[author bibliography](https://www.cse.chalmers.se/~rjmh/pubs.htm).

## Research question

Can the compositional benefits of monadic libraries be retained when a
computation cannot be represented as an ordinary function from an earlier
result to the next computation?

## Method

Hughes abstracts a binary computation type with operations corresponding to
lifting pure functions, sequential composition, and acting on one component
of a pair. He states laws and reconstructs useful combinators. Efficient
parsing, graphical interfaces, and active web pages serve as non-monadic case
studies.

## Findings

- Monadic bind hands an unrestricted host-language function the earlier
  result. A library cannot inspect that function to recover static information
  before a result exists.
- An arrow makes both input and output explicit while keeping the computation
  representation abstract. The library can preserve a static description
  alongside its dynamic behavior.
- `arr`, composition, and `first`, governed by laws, recover a broad generic
  programming interface. Ordinary functions and Kleisli arrows of monads are
  instances, but they are not the only instances.
- The additional generality is useful for combinator libraries whose topology
  or analysis must remain available independently of runtime values.

## Relevance

Arrows identify a real boundary in Catena's abstraction ladder: dynamic
value-dependent composition is sometimes too powerful because it hides
structure. They are relevant to static parsers, circuits, dataflow graphs, and
reactive networks, but that does not make an `Arrow` trait a core-language
requirement.

## Limits

The case studies establish expressibility, not a general usability or
performance advantage. The interface and its laws are more difficult to
teach than ordinary functions or applicatives, and arrow notation adds
surface complexity. Many applications need only the weaker applicative
interface introduced later.

## Derived work

- [Category Theory for Programming](../20-notes/category-theory-for-programming.md)
- [How Should Catena Specify Its Initial Categorical Hierarchy?](../40-inquiries/how-should-catena-specify-its-initial-categorical-hierarchy.md)
- [Category Theory for Programming map](../10-maps/category-theory-for-programming.md)
