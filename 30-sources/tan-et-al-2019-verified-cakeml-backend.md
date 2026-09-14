---
title: "The Verified CakeML Compiler Backend"
kind: source
created: "2026-09-14"
authors: ["Yong Kiam Tan","Magnus O. Myreen","Ramana Kumar","Anthony Fox","Scott Owens","Michael Norrish"]
published: 2019
citation_key: "tanetal2019verifiedcakemlbackend"
container: "Journal of Functional Programming 29, e2"
doi: "10.1017/S0956796818000229"
url: "https://doi.org/10.1017/S0956796818000229"
accessed: "2026-09-14"
tags: [compiler, bootstrap, language-design]
aliases: []
---

# The Verified CakeML Compiler Backend

## Reference

Yong Kiam Tan, Magnus O. Myreen, Ramana Kumar, Anthony Fox, Scott Owens, Michael Norrish. The Verified CakeML Compiler Backend. Journal of Functional Programming 29, e2, 2019. [Canonical source](https://doi.org/10.1017/S0956796818000229); [text consulted](https://cakeml.org/jfp19.pdf).

Reading locations: Sections 11.1–11.3, especially translation extensions, symbolic evaluation, and validation-assisted register allocation.

## Method

Mechanized compiler correctness and proof-producing bootstrap construction.

## Findings

The bootstrap requires both a source implementation theorem and verified compilation. Extending supported word operations and managing proof-time computation required additional translation and validation work.

## Limits

The proof has stated semantics, resource, FFI, and linking boundaries. It is not a proof or effort estimate for Catena.

## Relevance

Treat new-feature implementation, proof maintenance, and executable bootstrap construction as separate work streams.

## Derived work

[Feature Evolution in a Self-Hosted Catena Compiler](../20-notes/feature-evolution-in-a-self-hosted-catena-compiler.md) separates source evidence from Catena recommendations.
