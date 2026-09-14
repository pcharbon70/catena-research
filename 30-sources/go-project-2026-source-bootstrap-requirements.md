---
title: "Go Source Bootstrap Requirements"
kind: source
created: "2026-09-14"
authors: ["Go project"]
published: null
citation_key: "goproject2026sourcebootstraprequirements"
container: "Go installation documentation"
doi: null
url: "https://go.dev/doc/install/source"
accessed: "2026-09-14"
tags: [compiler, bootstrap, language-design]
aliases: []
---

# Go Source Bootstrap Requirements

## Reference

Go project. Installing Go from source. Go installation documentation. [Canonical source](https://go.dev/doc/install/source).

Reading locations: Install Go compiler binaries for bootstrap; four acquisition routes; minimum-version table.

## Method

Official build requirements and source-installation procedures.

## Findings

Bootstrap minimum versions advance under a published rule. The document describes binary, cross-compiled, gccgo, and historical C-root routes, with host limitations on old toolchains.

## Limits

Historical commands and platform examples are not promises that every route works on every current host.

## Relevance

Publish an explicit seed floor and retain a tested recovery path rather than assuming any older compiler will build current sources.

## Derived work

[Feature Evolution in a Self-Hosted Catena Compiler](../20-notes/feature-evolution-in-a-self-hosted-catena-compiler.md) separates source evidence from Catena recommendations.
