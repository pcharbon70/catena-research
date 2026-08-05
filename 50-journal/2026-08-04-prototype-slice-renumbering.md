---
title: "Prototype Slice Renumbering"
kind: journal
created: "2026-08-04"
tags:
  - catena
  - compilers
  - provenance
  - specification
aliases:
  - "Catena 0.1 patch migration"
---

# Prototype Slice Renumbering

## Question

Can the six implemented Catena prototype slices be redesignated as patches on
the `0.1` language line without changing their static or dynamic semantics,
while keeping every protocol, digest, signature, and historical claim honest?

## Decision

The approved canonical mapping is:

| Boundary | Retired identifier | Canonical identifier |
| --- | --- | --- |
| C001 type system | `0.1` | `0.1.1` |
| C002 data and patterns | `0.2` | `0.1.2` |
| C003 clause conditions | `0.3` | `0.1.3` |
| C004 traits and categorical operations | `0.4` | `0.1.4` |
| C005 effects and handlers | `0.5` | `0.1.5` |
| C006 specifications and governance | `0.6` | `0.1.6` |

The retired values are not compatibility aliases. Future prototype semantic
slices use the next unused `0.1.n` patch. The compiler package remains version
`0.1.0`; package-release version and accepted language version are separate.

This decision establishes prototype slice numbering only. It does not resolve
[C008 editions and feature lifecycle](../00-inbox/language-specification-completeness-checklist.md#1-specification-form-and-conformance).

## Contract impact

The hard cutover changes JSON AST and interface discriminators, condition
evidence, package manifests, standard hierarchy origin and digest, BEAM compile
metadata, claim identities, trust roots, governance bundles, assurance
manifests, and every signed domain separator. Unsigned AST inputs can be
renumbered mechanically. Interfaces and BEAM files must be rebuilt. Signed
governance artifacts must be regenerated and re-signed; changing their version
text would invalidate both their canonical digest and signature.

The Elixir implementation centralizes the sequence in
`Catena.LanguageVersion`. The implementation continues to lower only through
OTP 29 Erlang Abstract Format and `compile:noenv_forms/2`; no runtime language
meaning or target changes in this migration.

## Historical provenance

The C001 through C006 journals retain the two-component identifiers that their
cited immutable commits actually accepted and emitted. Those commits remain
semantic evidence for their bounded features, but they are not evidence that
the new protocol strings or derived bytes existed at those hashes. Each
historical journal carries an amendment linking back to this record.

The current three-component contracts require a fresh cross-slice compiler
conformance identity before the renumbered executable claim is published. The
original feature commits must not be amended or replaced.

## Method

The migration is implemented on matching `agent/renumber-prototype-slices`
branches in the research and compiler repositories. Verification covers:

- exact three-component frontmatter and one canonical patch per specification
  area;
- acceptance of AST `0.1.1` through `0.1.6` and rejection of every retired
  AST identifier;
- rejection of retired interface, package, trust-root, governance, and
  assurance identifiers;
- the `catena://standard/0.1.4` identity and refreshed canonical digest;
- the `catena:<kind>:0.1.6` signature domains;
- updated BEAM compile metadata and unchanged feature thresholds; and
- the complete existing compiler and archive validation suites.

## Result

The complete pre-authorization working-tree run passed on Erlang/OTP 29.0.4
(ERTS 17.0.4) and Elixir 1.20.2. After explicit user authorization, the
compiler migration was committed as immutable identity
`b7e0df841debd1d277da25bb8de65d6e865d9756`.

The compiler passed:

> **Non-normative evidence.**

```bash
mix format --check-formatted
mix clean
mix compile --warnings-as-errors
mix test
mix escript.build
git diff --check
```

The full suite reported 112 passing tests. It accepts all six canonical AST
versions, rejects all six retired AST values, rejects retired interface and
package values, rejects retired trust-root, governance, and assurance values,
checks all six signature-domain kinds, and verifies the new canonical standard
digest `c841bf5b4cbdbf8969ccf5375bc327ae106eb222671595b29ea49acd5b2f1013`.
The complete compiler sequence was rerun after the commit and left its working
tree clean, so these results apply to that exact identity.

The research archive passed:

> **Non-normative evidence.**

```bash
python3 -m unittest test_validate_archive.py
python3 validate_archive.py
git diff --check
```

The focused suite reported 10 passing tests. Archive validation checked 182
completed documents, 17 directories, 1,432 local links, 81 source notes, 45
specification chapters, and 53 classified fenced blocks without error.

## Promotion state

The user authorized the immutable compiler commit on 2026-08-04. Commit
`b7e0df841debd1d277da25bb8de65d6e865d9756` is the renumbered cross-slice
compiler conformance identity. Its post-commit validation passed, and the
changed canonical standard digest and signature domains are recorded above.

The normative document authority and temporary slice convention are defined
by the [Specification Authority](../SPECIFICATION-AUTHORITY.md).
