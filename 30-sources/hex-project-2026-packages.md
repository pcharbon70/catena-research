---
title: "Hex Package Manager: Packages and Requirements"
kind: source
created: "2026-08-24"
authors:
  - "Hex Project"
published: null
citation_key: "hexProject2026Packages"
container: "Hex Documentation"
edition: null
isbn: null
doi: null
url: "https://hexdocs.pm/elixir/Version.html"
accessed: "2026-08-24"
tags:
  - erlang
  - packages
  - versioning
aliases:
  - "Hex version requirements"
---

# Hex Package Manager: Packages and Requirements

## Reference

Hex Project, “Version” (Elixir standard-library module implementing Hex's
version and requirement conventions) and the hex.pm package documentation,
accessed 2026-08-24.
[Version module documentation](https://hexdocs.pm/elixir/Version.html);
[hex.pm](https://hex.pm/).

## Research question or contribution

What version grammar, requirement operators, and pre-release matching rules
does the BEAM ecosystem's package manager expect, and what must a Catena
package declare to interoperate with it?

## Method

The `Version` module documentation — which defines the exact grammar Hex
dependencies use — was read for the version schema, requirement operator
set, the `~>` pessimistic operator's translation table, and the
`:allow_pre` matching rule. The registry-facing behavior (names, tarball
checksums, publishing) is taken from the existing
[Hex publishing hypothesis](../00-inbox/package-publishing-hypothesis-hex.md)
capture and not re-verified against registry documentation in this pass.

## Findings

- Versions follow the SemVer 2.0.0 schema: three numeric components of at
  most 14 digits each, optional dot-separated pre-release identifiers, and
  optional dot-separated build metadata.
- Pre-releases are strictly less than their corresponding releases;
  numeric pre-release identifiers compare numerically; alphanumeric ones
  lexically; build metadata is ignored in comparison.
- Requirements support `==`, `>`, `>=`, `<`, `<=`, a bare version meaning
  exact equality, and `and`/`or` combinations.
- The pessimistic operator `~>` sets an upper bound one step above its
  operand: `~> 2.1.2` admits `>= 2.1.2 and < 2.2.0`, and `~> 2.1` admits
  `>= 2.1.0 and < 3.0.0`; its operand may omit the patch component.
- `~>` never includes pre-release versions of its upper bound.
- Hex sets `:allow_pre` to false by default: a pre-release version does
  not match a requirement unless the requirement's own operand is a
  pre-release.
- Hex packages are published as tarballs with an outer checksum, and the
  registry resolves the same operator grammar over package names and
  these versions.

## Relevance

This is the transport profile Catena's package layer targets. Catena's
adopted exact/caret/tilde requirement set maps onto this world: tilde is
Catena's upper-bounded step operator by a different spelling than Hex's
`~>`, exact pins are Hex's `==`, and Catena's caret follows the
Cargo-style 0.x rule rather than any Hex operator — a deliberate choice
recorded in the package synthesis. The `:allow_pre false` default is the
behavior Catena adopts: pre-release versions satisfy requirements only
when the requirement itself names a pre-release. Package names and
tarball checksums interoperate directly with hex.pm per the inbox
hypothesis.

## Limits

The `Version` module defines Elixir's conventions, which Hex consumes;
Hex's own registry additionally layers publishing, retirement, and
checksums not specified here. Hex's documentation does not define caret
semantics at all, and its `~>` differs from both Cargo's `~` and npm's
`^` in exactly the pre-1.0 region where Catena must make an explicit
choice rather than inherit ambiguity.

## Derived work

- [Catena Package Identity and Dependencies](../20-notes/catena-package-identity-and-dependencies.md)
- [How Should Catena Define Package Identity and Dependency Resolution?](../40-inquiries/how-should-catena-define-package-identity-and-dependency-resolution.md)
- [Package Identity and Dependencies map](../10-maps/package-identity-and-dependencies.md)
