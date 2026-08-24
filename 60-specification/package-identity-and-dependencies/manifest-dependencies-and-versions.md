---
title: "Manifest Dependencies and Versions"
kind: specification
created: "2026-08-24"
status: candidate
spec_version: "0.1.21"
tags:
  - packages
  - specification
  - versioning
aliases:
  - "Catena manifest dependencies"
---

# Manifest Dependencies and Versions

## Status and authority

This chapter is the normative Catena 0.1.21 dependency-declaration and
version-grammar contract. It is governed by
[Specification Authority](../../SPECIFICATION-AUTHORITY.md),
[Catena Conformance Vocabulary](../../CONFORMANCE-VOCABULARY.md), and
[Catena Implementation Limits and Portability](../../IMPLEMENTATION-LIMITS.md).
It extends, without amending, the `catena-package-manifest` of
[Edition Selection and Applicability](../editions-and-feature-lifecycle/edition-selection-and-applicability.md)
and adopts the grammar and precedence of
[Semantic Versioning 2.0.0](../../30-sources/preston-werner-2013-semantic-versioning.md).

The rules apply only to source-language revision `0.1.21`. They do not
reinterpret retained manifests, interfaces, artifacts, or signed formats.

## The dependencies field

A version 0.1.7 or later `catena-package-manifest` MAY carry a
`dependencies` object (`PK-OBL-002`). Each key is a package name; each
value is one requirement string in the grammar below. A package name is
one or more ASCII lowercase-initial segments of letters, digits, and
hyphens joined by single hyphens — `json_tools` and `catena-web` are
well-formed names. An absent `dependencies` field means the package is
dependency-free; an empty object is equivalent. Duplicate keys,
non-object values, or malformed requirements are static invalidity
reported as `PKG001` (`PK-OBL-002`).

The field changes no selection semantics: dependency manifests never
inherit a consumer's selection, per the unchanged C008 rule, and the
field is consumed before compilation — no accepted module input changes.

## Version grammar

A package version is exactly SemVer 2.0.0's version (`PK-OBL-003`):

> **Normative definition.**

```text
version = major "." minor "." patch [ "-" pre-release ] [ "+" build ] ;
```

- `major`, `minor`, and `patch` are nonnegative decimal integers without
  leading zeros (`0` itself allowed).
- `pre-release` is one or more dot-separated identifiers of ASCII
  alphanumerics and hyphens; `build` likewise.
- Precedence follows SemVer sections 10–11: numeric comparison on the
  triple; a version with pre-release has lower precedence than the same
  version without; pre-release identifiers compare pairwise with numeric
  identifiers below alphanumeric and longer lists above shorter prefixes;
  build metadata is parsed and recorded but ignored in precedence.

## Requirement grammar

A requirement is exactly one of three forms (`PK-OBL-004`):

> **Normative definition.**

```text
requirement = version | caret | tilde ;
caret       = "^" version ;
tilde       = "~" version ;
```

An operator other than `^` or `~`, a compound requirement, a missing or
partial version operand, or build metadata in an operand is static
invalidity reported as `PKG001`. An operand may carry a pre-release.

## Satisfaction

A version `v` satisfies a requirement as follows (`PK-OBL-005`):

- exact `x.y.z`: `v` equals `x.y.z`, ignoring build metadata;
- `^x.y.z` with `x > 0`: `v >= x.y.z` and `v < (x+1).0.0`;
- `^0.y.z` with `y > 0`: `v >= 0.y.z` and `v < 0.(y+1).0`;
- `^0.0.z`: `v >= 0.0.z` and `v < 0.0.(z+1)`;
- `~x.y.z`: `v >= x.y.z` and `v < x.(y+1).0`.

The caret's pre-1.0 windows follow the Cargo convention rather than Hex
or npm practice; the choice is deliberate and recorded in the
[package synthesis](../../20-notes/catena-package-identity-and-dependencies.md).

A pre-release version satisfies a requirement only when the operand
itself is a pre-release (`PK-OBL-005`): `1.3.0-rc.1` never satisfies
`^1.2.3` or `~1.2.9`, and `1.2.4-beta` satisfies only requirements whose
operand is a `1.2.4-…` pre-release. This adopts Hex's pre-1.0 matching
default.

## Deliberately separate work

Fetch, cache, and lock tooling remain G121; registry behavior, retirement,
and signing remain G130's transport layer; compatibility meanings of
version increments remain G028; build reproducibility consumption of the
lockfile remains G128.

## Rationale and evidence (non-normative)

The [package synthesis](../../20-notes/catena-package-identity-and-dependencies.md)
compares SemVer's given grammar with the ecosystem's divergent operator
conventions and records why exact/caret/tilde with the Cargo 0.x rule was
selected. The
[open inquiry](../../40-inquiries/how-should-catena-define-package-identity-and-dependency-resolution.md)
and [topic map](../../10-maps/package-identity-and-dependencies.md)
preserve the decision route.
