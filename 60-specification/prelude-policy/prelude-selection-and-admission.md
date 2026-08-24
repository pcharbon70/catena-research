---
title: "Prelude Selection and Admission"
kind: specification
created: "2026-08-24"
status: normative
spec_version: "0.1.22"
tags:
  - prelude
  - specification
aliases:
  - "Catena prelude selection"
---

# Prelude Selection and Admission

## Status and authority

This chapter is the normative Catena 0.1.22 prelude-selection and
admission contract. It is governed by
[Specification Authority](../../SPECIFICATION-AUTHORITY.md),
[Catena Conformance Vocabulary](../../CONFORMANCE-VOCABULARY.md), and
[Catena Implementation Limits and Portability](../../IMPLEMENTATION-LIMITS.md).
It extends, without amending, the manifest of
[Edition Selection and Applicability](../editions-and-feature-lifecycle/edition-selection-and-applicability.md),
the resolution machinery of
[Resolution and Lockfile](../package-identity-and-dependencies/resolution-and-lockfile.md),
and the precedence of
[Shadowing and Ambiguity](../namespaces-and-shadowing/shadowing-and-ambiguity.md).

The rules apply only to source-language revision `0.1.22`. They do not
reinterpret retained manifests, interfaces, artifacts, or signed formats.

## The prelude field

A `catena-package-manifest` MAY carry a `prelude` object
(`PL-OBL-002`):

> **Normative definition.**

```text
prelude = { "package": package-name, "requirement": requirement } ;
```

- `package` is one package name under C025's spelling; `requirement`
  is one requirement string under C025's exact/caret/tilde grammar.
- At most one `prelude` selection exists per package. A second, a
  non-object value, a non-string field, or a malformed name or
  requirement is static invalidity reported as `PRE001` (`PL-OBL-003`).
- An absent field or an explicit `null` selects no prelude; the two
  states are indistinguishable (`PL-OBL-002`). No sentinel spelling and
  no per-name exclusion mechanism exists.

The field changes no selection semantics: the manifest's edition,
language revision, and previews govern exactly as C008 fixed, and a
dependency manifest still never inherits a consumer's prelude — each
package's own manifest decides its prelude alone.

## Admission as an origin

When a package's manifest carries a `prelude` selection, dependency
resolution resolves it against the package environment exactly as an
ordinary dependency: the named package must be known (`PKG004`
otherwise) and the requirement must be satisfiable together with all
other requirements on that name (`PKG003` otherwise, every requirer
listed) (`PL-OBL-004`). The resolved prelude package is recorded in
`catena.lock` like any dependency, with its exact version, admitting
requirement, requirers marked as the prelude selection, and bundle
digest; replay pins it as an exact pin (`PL-OBL-005`).

After resolution, the prelude package's exported set enters the
resolution context as an origin in the ordinary import class
(`PL-OBL-004`): every exported name is available unqualified in its
category and as `PreludePackage.name` qualification, subject to the
unchanged C022 admission validation and C021 precedence below. The
prelude origin has no weaker or stronger tier, no silent shadowing, and
no special diagnostics of its own for collisions.

## Package identity

A prelude package is any valid C025 package — including one with zero
exports (`PL-OBL-002`). Its identity is the unchanged (name, version,
SHA-256 bundle digest) triple; prelude selection confers no special
identity, exemption, or anchoring. Nothing in this chapter reserves a
name or makes any specific package a prelude; which package, if any, an
ecosolution standardizes remains G101's contents decision under this
mechanism.

## Deliberately separate work

Prelude contents and the standard-library name freeze remain G101.
Collection protocols remain P102. Tooling scaffolding that pre-fills
the field remains G121 — a tool may write the field but MUST NOT imply
selection that the manifest does not record. Entry-point defaults remain
C027. Compatibility meanings of prelude version bumps are subsequently fixed
by C028/G136.

## Rationale and evidence (non-normative)

The [prelude synthesis](../../20-notes/catena-prelude-policy.md)
compares the Haskell implicit-unless-explicit model and the Rust
shadowing tier with the corpus's shipped commitments and records why
opt-in selection on ordinary C025 machinery was selected. The
[resolved inquiry](../../40-inquiries/how-should-catena-define-its-prelude-policy.md)
and [topic map](../../10-maps/prelude-policy.md) preserve the decision
route.
