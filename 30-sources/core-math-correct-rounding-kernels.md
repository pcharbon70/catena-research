---
title: "CORE-MATH Correct-Rounding Kernels"
kind: source
created: "2026-09-09"
authors: ["CORE-MATH project"]
url: "https://core-math.gitlabpages.inria.fr/"
accessed: "2026-09-09"
tags: [numerics, floats]
aliases: []
---

# CORE-MATH Correct-Rounding Kernels

## Reference

CORE-MATH project, [project overview](https://core-math.gitlabpages.inria.fr/)
and [FAQ](https://core-math.gitlabpages.inria.fr/faq.html), accessed 9 September 2026.
The overview is a maintained project page, not a dated paper.

## Contribution

The project supplies mathematical-function implementations intended for integration
into existing libraries. The overview lists MIT-licensed functions by floating-point
format and links selected implementations to proofs or integration evidence.
Its FAQ distinguishes language-binding requirements from assuming that every
ordinary C mathematical function is correctly rounded.

## Relevance

CP-105-6 identifies this project as an upstream lead. Our synthesis is that a
function's availability does not establish Catena's finite-domain behavior,
compiler/platform compatibility or independent local validation. C105 initially
admits exact basic arithmetic and an independently checked algebraic square root.
Transcendentals remain absent until NL-T01 is satisfied.

## Limits

This session read the overview and FAQ, not every linked implementation or proof.
No upstream function is vendored or certified by these observations.

## Derived work

- [Numeric contract](../60-specification/numeric-library/checked-arithmetic-and-explicit-rounding.md#mathematical-functions-and-admission) — the explicit admission gate.
- [Implementation journal](../50-journal/2026-09-09-numeric-library.md) — local decisions and evidence.
