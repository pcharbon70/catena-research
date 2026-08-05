---
title: "Edition Selection and Applicability"
kind: specification
created: "2026-08-05"
status: normative
spec_version: "0.1.7"
tags:
  - compatibility
  - language-design
  - specification
  - versioning
aliases:
  - "Catena 0.1.7 language selection"
---

# Edition Selection and Applicability

## Status and authority

This chapter and its three siblings are the normative Catena 0.1.7 editions
and feature-lifecycle slice. They extend the cumulative 0.1.1 through 0.1.6
language without changing a package until it selects a new manifest format or
language revision.

The repository [Specification Authority](../../SPECIFICATION-AUTHORITY.md)
governs status and conflicts. The authorized immutable implementation record
supports promotion but remains evidence rather than authority.

## Version axes

Catena keeps four independent identities:

1. an **edition** is an end-user compatibility track in exact `major.minor`
   form;
2. a **language revision** is one exact cumulative semantic boundary in
   `major.minor.patch` form;
3. an artifact **version** selects the schema and canonical encoding of one
   persisted format; and
4. a compiler-package version identifies an implementation release.

The major and minor components of a language revision MUST equal its selected
edition. Numeric resemblance MUST NOT make an artifact version or compiler
release select language semantics.

Edition `0.1` is an active prototype edition. Revisions `0.1.1` through
`0.1.7` are published in cumulative order. C008 introduces the selection and lifecycle contract at revision
`0.1.7`; C007 is a document-authority milestone rather than a language
revision.

## Package selection

A version 0.1.7 `catena-package-manifest` MUST contain `edition`,
`language_revision`, and `previews`. `edition` MUST name a retained edition,
`language_revision` MUST name a published revision of that edition, and
`previews` MUST be a duplicate-free sorted list accepted by the lifecycle
rules in
[Feature Lifecycle and Compatibility](feature-lifecycle-and-compatibility.md#preview-selection).

> **Normative definition.**

```json
{
  "format": "catena-package-manifest",
  "version": "0.1.7",
  "edition": "0.1",
  "language_revision": "0.1.7",
  "previews": []
}
```

The selection applies to every module compiled in that package. A module
frontend schema MAY differ from the language revision, but its decoded forms
MUST be checked against the package selection. A construct introduced after
the selected revision is `EDN001` even when a newer frontend schema can encode
it. If a module transport also carries an explicit language selection, all
three fields MUST equal the package selection; a contradiction is `EDN001`.

Dependency manifests do not inherit a consumer's selection. Each package is
checked under its own recorded selection.

## Standalone and interactive selection

A tool invocation without a package manifest uses the compiler's current
edition and revision with no previews. The tool MUST report that resolved
selection in structured success output and every emitted artifact. It MUST
NOT describe an implicit selection as user-authored configuration.

A legacy frontend whose artifact version already fixed historical semantics
MAY imply the matching historical revision for compatibility, but the tool
MUST issue the `EDN002` advisory and report the inferred selection.

## Cumulative applicability

For a selected revision, all normative stable slice rules introduced at an
earlier or equal revision in the same edition apply. A later rule replaces,
deprecates, or removes an earlier rule only when the lifecycle registry names
the affected feature, boundary revision, governing headings, and migration
record.

When two otherwise applicable chapters conflict without that record, the
specification is defective and the disputed behavior has no conforming
interpretation. An implementation MUST NOT choose the numerically larger rule
as an implicit winner.

Preview rules apply only when the exact preview name is enabled for the
selected revision. Withdrawn and removed rules do not apply at or after their
recorded transition, while compilation at an earlier retained revision keeps
its historical rule set.

## Retention

A conforming current compiler MUST accept every published stable revision of
every retained edition. An exact pin MUST NOT float to a later revision.
Changing the current default MUST NOT change a package with an explicit pin.

No stable edition or revision may disappear from the registry through an
ordinary compiler update. Retirement requires a separately approved normative
policy defining notice, archival compiler availability, verification of old
artifacts, and migration. Version 0.1.7 defines no retirement.

## Prototype compatibility boundary

Within edition 0.1, a later patch revision MAY contain a documented breaking
language change. The change MUST occur at a revision boundary and satisfy the
migration and deprecation rules in the sibling chapters. A package observes
the change only after selecting that revision.

The versioned JSON frontend is a temporary toolchain input rather than Catena
source syntax. Its punctuation, object layout, and transport details are not
end-user source-compatibility promises. Normative static and dynamic semantics
at a selected revision remain binding despite that exclusion.

## Research route (non-normative)

The four-axis model and alternative analysis are developed in
[Language Editions and Feature Lifecycle](../../20-notes/language-editions-and-feature-lifecycle.md).
Package-local selection and retained historical support are informed by the
[Rust Edition Guide source note](../../30-sources/rust-project-edition-guide.md).
