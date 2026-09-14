---
title: "Parsing Expression Grammars: A Recognition-Based Syntactic Foundation"
kind: "source"
created: "2026-09-12"
authors: ["Bryan Ford"]
published: 2004
citation_key: "ford2004parsingexpressiongrammars"
container: "POPL 2004, 111–122"
doi: "10.1145/964001.964011"
url: "https://pdos.csail.mit.edu/~baford/packrat/popl04/"
accessed: "2026-09-12"
tags: ["language-design","syntax","usability"]
aliases: []
---

# Parsing Expression Grammars: A Recognition-Based Syntactic Foundation

## Reference

Bryan Ford. Parsing Expression Grammars: A Recognition-Based Syntactic Foundation. POPL 2004, 111–122, 2004. [Canonical source](https://pdos.csail.mit.edu/~baford/packrat/popl04/); [text consulted](https://pdos.csail.mit.edu/papers/parsing:popl04.pdf).

Reading locations: Sections 1–3, especially prioritized choice and the formal recognition rules.

## Method

The paper develops PEG recognition semantics and relationships to earlier top-down parsing formalisms.

## Findings

Prioritized choice is ordered: swapping alternatives can change the language. A deterministic parse follows the recognizer's rules; it does not establish that a human reader expects that parse.

## Limits

PEG formalism is not a usability result or automatic error-recovery solution. Parser correctness and source comprehension require separate evidence.

## Relevance

Publish grammar disambiguation and regression witnesses. Neither zero parser conflicts nor a successful parser generation is a sufficient readability claim.

## Derived work

[Grammar and Vocabulary for Approachable Catena](../20-notes/grammar-and-vocabulary-for-approachable-catena.md) distinguishes these findings from Catena-specific recommendations.
