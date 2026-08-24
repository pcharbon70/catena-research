---
title: "Entry Declarations"
kind: specification
created: "2026-08-24"
status: normative
spec_version: "0.1.23"
tags:
  - entry-points
  - specification
aliases:
  - "Catena entry declarations"
---

# Entry Declarations

## Status and authority

This chapter is the normative Catena 0.1.23 entry-declaration contract.
It is governed by
[Specification Authority](../../SPECIFICATION-AUTHORITY.md),
[Catena Conformance Vocabulary](../../CONFORMANCE-VOCABULARY.md), and
[Catena Implementation Limits and Portability](../../IMPLEMENTATION-LIMITS.md).
It extends, without amending, the package manifest of
[Edition Selection and Applicability](../editions-and-feature-lifecycle/edition-selection-and-applicability.md)
and the optional-field structure of
[Manifest Dependencies and Versions](../package-identity-and-dependencies/manifest-dependencies-and-versions.md),
and it presupposes the export model of
[Import Declarations and Admission](../imports-and-exports/import-declarations-and-admission.md).

The rules apply only to source-language revision `0.1.23`. They do not
reinterpret retained manifests, interfaces, artifacts, or signed formats.

## The entries field

A `catena-package-manifest` MAY carry an `entries` array (`EN-OBL-002`):

> **Normative definition.**

```text
entries = { "entries": [ entry ] } ;
entry   = { "name": export-name, "result": type-reference
          , "launch": ( true ) } ;
```

- `name` is one exported function name of the declaring package, under
  the value-name spelling of
  [Identifier Syntax and Equivalence](../identifiers/identifier-syntax-and-equivalence.md).
- `result` is one type reference naming the export's result type.
- `launch` is optional; when present it MUST be `true` and at most one
  entry in the array MAY carry it.

An absent field, an explicit `null`, and an empty array all declare a
library; the three states are indistinguishable (`EN-OBL-004`). No
`kind`, `type`, or other discriminator field exists.

## Entry validity

Every declared entry MUST name an existing export of the declaring
package that is a zero-argument, total, effect-closed function whose
recorded result type is the declared `result` (`EN-OBL-003`):

- **Zero-argument** — the export's parameter list is empty.
- **Effect-closed** — the export's recorded effect row is empty: every
  effect request the body can perform is handled before return, the
  same completion rule
  [Canonical Kernel Syntax](../formal-semantic-kernel/canonical-kernel-syntax.md)
  fixes for process entries. A non-empty row is static invalidity
  reported as `ENT001`; no implicit host handler exists and no entry
  may leave a request unhandled. This is the 0.1.23 answer to the
  deferred G082 question.
- **Result recorded** — the declared `result` MUST equal the export's
  recorded result type; a mismatch is static invalidity reported as
  `ENT001`.

A malformed shape — a non-array `entries`, a non-object entry, a
missing or non-string `name` or `result`, a `launch` that is not
`true`, a duplicated `name`, an export that does not exist, a
non-zero-argument export, a non-closed row, a `result` mismatch, or a
second `launch` marker — is static invalidity reported as `ENT001`
(`EN-OBL-003`). Manifest framing failures outside these shapes remain
`PKG001`; selection failures remain `EDN001`.

## Libraries and executables

A package that declares at least one entry is an executable candidate;
a package that declares none is a library (`EN-OBL-004`). The
distinction is derived from the `entries` array alone. A library is
fully valid: nothing requires any entry, and a library manifest with
`entries` absent, `null`, or `[]` is indistinguishable from one that
never mentioned the field.

Exactly one entry MAY carry the launch marker (`EN-OBL-005`). The
marker records which entry a single-entry launch prefers; it creates no
name, admits no scope, and changes no export. A package with several
entries and no marked launch is valid — launching names the entry
explicitly under
[Startup and Shutdown](startup-and-shutdown.md).

## Relation to compilation roots

The manifest's compilation roots — the template specializations a
package build emits — are unaffected. Entries are a language-level
invocation surface over existing exports; roots are build outputs.
Neither implies the other, and no rule of this chapter changes root
validation or emission (`EN-OBL-010`).

## Zero-implicit-names interaction

Declaring or launching entries introduces no name into any scope: an
entry references an existing export, and the launch operation of
[Startup and Shutdown](startup-and-shutdown.md) binds nothing. The
C026 guarantee — no name is ever implicitly in scope — extends over
this area unchanged (`EN-OBL-010`).

## Deliberately separate work

Supervision, restart, and process lifetime remain G084/G089.
Cancellation and deadlines remain G088. The CLI, `run` tooling, and
host-process boundary remain G121. Distribution and upgrades remain
G091/G092. Compatibility meanings of entry-set changes remain G028.
Exit-code and signal profiles remain G121 over the report defined here.

## Rationale and evidence (non-normative)

The [entry-points synthesis](../../20-notes/catena-entry-points.md)
compares named entry exports with a reserved `main` and an OTP
`start/2` startup model, records the [OTP applications
analysis](../../30-sources/erlang-otp-applications.md) of derived
libraries, and explains why effect-closure is forced by the shipped
kernel and prelude contracts. The [resolved
inquiry](../../40-inquiries/how-should-catena-define-entry-points-and-application-structure.md)
and [topic map](../../10-maps/entry-points.md) preserve the decision
route.
