---
title: "OCaml Compiler Bootstrap Transitions"
kind: source
created: "2026-09-14"
authors: ["OCaml project"]
published: null
citation_key: "ocamlproject2026compilerbootstrap"
container: "OCaml source repository, BOOTSTRAP.adoc"
doi: null
url: "https://github.com/ocaml/ocaml/blob/trunk/BOOTSTRAP.adoc"
accessed: "2026-09-14"
tags: [compiler, bootstrap, language-design]
aliases: []
---

# OCaml Compiler Bootstrap Transitions

## Reference

OCaml project. Bootstrapping the compiler. OCaml source repository, BOOTSTRAP.adoc. [Canonical source](https://github.com/ocaml/ocaml/blob/trunk/BOOTSTRAP.adoc).

Reading locations: Bootstrapping the compiler; adding, removing and renaming primitives; bootstrap test script.

## Method

Maintainer procedure for transitions affecting runtime primitives and compiled formats.

## Findings

Format changes can require bootstrap updates. Primitive renaming uses a temporary old-name stub; removal stops uses before removing the primitive. Source changes and refreshed bootstrap artifacts are committed separately.

## Limits

The exact commands depend on OCaml's bytecode and build architecture.

## Relevance

Use staged compatibility bridges for Catena runtime and interface transitions, with separately reviewable implementation and seed updates.

## Derived work

[Feature Evolution in a Self-Hosted Catena Compiler](../20-notes/feature-evolution-in-a-self-hosted-catena-compiler.md) separates source evidence from Catena recommendations.
