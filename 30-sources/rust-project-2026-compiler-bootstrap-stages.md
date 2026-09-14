---
title: "Rust Compiler Bootstrap Stages"
kind: source
created: "2026-09-14"
authors: ["Rust project"]
published: null
citation_key: "rustproject2026compilerbootstrapstages"
container: "Rust Compiler Development Guide"
doi: null
url: "https://rustc-dev-guide.rust-lang.org/building/bootstrapping/what-bootstrapping-does.html"
accessed: "2026-09-14"
tags: [compiler, bootstrap, language-design]
aliases: []
---

# Rust Compiler Bootstrap Stages

## Reference

Rust project. What Bootstrapping does. Rust Compiler Development Guide. [Canonical source](https://rustc-dev-guide.rust-lang.org/building/bootstrapping/what-bootstrapping-does.html).

Reading locations: Stages, complications, and stages versus standard libraries; living documentation accessed 14 September 2026.

## Method

Official description of the compiler's staged build and contributor workflow.

## Findings

The previous compiler and matching libraries build a newer compiler. Stage-specific library and ABI relationships matter. Bootstrap flags enable implemented unstable facilities; they do not create missing implementations.

## Limits

Rust stage names and library arrangements are project-specific. The page's example version numbers are illustrative, not current-release claims.

## Relevance

Record the builder, source, and library identities for each Catena stage rather than relying on a stage number.

## Derived work

[Feature Evolution in a Self-Hosted Catena Compiler](../20-notes/feature-evolution-in-a-self-hosted-catena-compiler.md) separates source evidence from Catena recommendations.
