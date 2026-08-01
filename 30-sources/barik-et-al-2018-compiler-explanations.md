---
title: "How Should Compilers Explain Problems to Developers?"
kind: source
created: "2026-08-01"
authors:
  - "Titus Barik"
  - "Denae Ford"
  - "Emerson Murphy-Hill"
  - "Chris Parnin"
published: 2018
citation_key: "barikEtAl2018CompilerExplanations"
container: "Proceedings of ESEC/FSE 2018: 633–643"
edition: null
isbn: "978-1-4503-5573-5"
doi: "10.1145/3236024.3236040"
url: "https://doi.org/10.1145/3236024.3236040"
accessed: "2026-08-01"
tags:
  - compilers
  - diagnostics
  - language-design
  - usability
aliases:
  - "Barik et al. on compiler explanations"
---

# How Should Compilers Explain Problems to Developers?

## Reference

Titus Barik, Denae Ford, Emerson Murphy-Hill, and Chris Parnin, “How Should
Compilers Explain Problems to Developers?” in *Proceedings of the 26th ACM
Joint European Software Engineering Conference and Symposium on the
Foundations of Software Engineering* (ESEC/FSE 2018), 633–643.
[DOI](https://doi.org/10.1145/3236024.3236040) and
[author manuscript](https://www.microsoft.com/en-us/research/wp-content/uploads/2019/10/barik_fse18.pdf).

## Research question

Do developers prefer compiler diagnostics structured as explanations, and how
does the structure and content of compiler messages differ from explanations
that developers accept from other developers?

## Method

The authors first compare paired Jikes and OpenJDK messages for five Java
problems with 68 professional software developers. They then stratify and
qualitatively code 210 Stack Overflow question-and-accepted-answer pairs across
seven programming-language tags. Toulmin's argument model supplies components
such as claim, grounds, warrant, backing, rebuttal, and resolution.

## Findings

- When neither message offers a repair, participants significantly prefer the
  message with a proper explanatory argument over a deficient assertion.
- A concrete resolution can be preferred even when its argument structure is
  otherwise deficient. Actionability therefore competes with explanatory
  completeness rather than following from verbosity alone.
- Accepted human explanations tend toward a resolution, a simple argument, or
  an extended argument with additional evidence.
- A useful diagnostic can identify the problem, give the relevant source facts,
  connect those facts to the restriction, and offer a repair when the compiler
  can do so responsibly.
- The study treats error presentation as an explanation-design problem, not
  merely pretty-printing of the compiler's failed internal judgment.

## Relevance

Catena diagnostics should lead with the programmer's operation and source
construct, then explain the visible reason and likely repair. Internal terms
such as higher-kinded unification, negative occurrence, dictionary coherence,
or residual row constraints are supporting detail, not the claim itself.

For example, a failed generated `map` should say which field consumes the type
parameter and why that prevents changing stored values. “Cannot derive
`Functor` because the parameter is contravariant” is an internal conclusion,
not a sufficient explanation for the intended audience.

## Limits

The comparative phase uses five Java error pairs from two compilers, and the
participants were experienced professionals at one large software company.
Accepted Stack Overflow answers are a proxy for useful explanations, not a
controlled measure of comprehension or repair success. The study supports
diagnostic structure; it does not test Catena vocabulary or functional type
errors directly.

## Derived work

- [An Approachable Vocabulary for Catena](../20-notes/approachable-language-vocabulary.md)
- [How Should Catena Expose Mathematical Structure Without Mathematical Jargon?](../40-inquiries/how-should-catena-expose-mathematical-structure-without-mathematical-jargon.md)
- [Approachable Catena Language Design map](../10-maps/approachable-catena-language-design.md)
