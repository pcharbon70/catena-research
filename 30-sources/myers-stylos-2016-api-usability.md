---
title: "Improving API Usability"
kind: "source"
created: "2026-09-12"
authors: ["Brad A. Myers","Jeffrey Stylos"]
published: 2016
citation_key: "myersstylos2016apiusability"
container: "Communications of the ACM 59(6), 62–69"
doi: "10.1145/2896587"
url: "https://doi.org/10.1145/2896587"
accessed: "2026-09-12"
tags: ["language-design","syntax","usability"]
aliases: []
---

# Improving API Usability

## Reference

Brad A. Myers, Jeffrey Stylos. Improving API Usability. Communications of the ACM 59(6), 62–69, 2016. [Canonical source](https://doi.org/10.1145/2896587); [text consulted](https://www.cs.cmu.edu/~NatProg/papers/p62-myers-CACM-API_Usability.pdf).

Reading locations: Examples of Problems and Methods for Improving API Usability, pp. 65–68.

## Method

The authors synthesize their API-usability research and other studies into design methods and examples. This is a research overview, not one new controlled experiment.

## Findings

Discoverability, placement, parameter consistency, documentation, and recognizable distinctions matter alongside identifier choice. Minimal APIs can still force difficult coordination work.

## Limits

Many examples concern object-oriented APIs. Particular placement results cannot be transferred quantitatively to Catena's module and trait model.

## Relevance

Evaluate a name at its call site, in completion, and in diagnostics. Preserve one discoverable interface for each behavior rather than presenting several formal and friendly aliases.

## Derived work

[Grammar and Vocabulary for Approachable Catena](../20-notes/grammar-and-vocabulary-for-approachable-catena.md) distinguishes these findings from Catena-specific recommendations.
