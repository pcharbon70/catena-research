---
title: "Identifying and Correcting Programming Language Behavior Misconceptions"
kind: "source"
created: "2026-09-12"
authors: ["Kuang-Chen Lu","Shriram Krishnamurthi"]
published: 2024
citation_key: "lukrishnamurthi2024languagebehaviormisconceptions"
container: "Proceedings of the ACM on Programming Languages 8(OOPSLA1), Article 106"
doi: "10.1145/3649823"
url: "https://cel.cs.brown.edu/paper/identifying-correcting-pl-misconceptions/"
accessed: "2026-09-12"
tags: ["language-design","syntax","usability"]
aliases: []
---

# Identifying and Correcting Programming Language Behavior Misconceptions

## Reference

Kuang-Chen Lu, Shriram Krishnamurthi. Identifying and Correcting Programming Language Behavior Misconceptions. Proceedings of the ACM on Programming Languages 8(OOPSLA1), Article 106, 2024. [Canonical source](https://cel.cs.brown.edu/paper/identifying-correcting-pl-misconceptions/); [text consulted](https://cs.brown.edu/people/sk/Publications/Papers/Published/lk-smol-tutor/paper.pdf).

Reading locations: Sections 6–8 and 11; especially the formative interpretation of tutoring results.

## Method

The authors derive misconceptions from student work and build executable alternative interpreters and a tutor. Questions distinguish competing explanations of program behavior.

## Findings

Misconceptions persist across settings. The tutoring analysis finds improvements for several misconceptions but also worsening trends for two; the authors explicitly interpret effectiveness evidence as formative.

## Limits

Multiple-choice tasks and a scope/state/higher-order-function core do not validate Catena's effects or categorical vocabulary. A matching wrong answer alone may not uniquely identify a misconception.

## Relevance

Design counterexamples for wrong mental models: a pipe that supposedly unwraps failure, an empty effect requirement mistaken for termination, or a callback assumed to run exactly once.

## Derived work

[Grammar and Vocabulary for Approachable Catena](../20-notes/grammar-and-vocabulary-for-approachable-catena.md) distinguishes these findings from Catena-specific recommendations.
