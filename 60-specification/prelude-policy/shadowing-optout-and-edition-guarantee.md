---
title: "Shadowing, Opt-Out, and the Edition Guarantee"
kind: specification
created: "2026-08-24"
status: normative
spec_version: "0.1.22"
tags:
  - prelude
  - specification
aliases:
  - "Catena prelude precedence and guarantee"
---

# Shadowing, Opt-Out, and the Edition Guarantee

## Status and authority

This chapter is the normative Catena 0.1.22 prelude precedence, opt-out,
and edition-guarantee contract. It is governed by
[Specification Authority](../../SPECIFICATION-AUTHORITY.md),
[Catena Conformance Vocabulary](../../CONFORMANCE-VOCABULARY.md), and
[Catena Implementation Limits and Portability](../../IMPLEMENTATION-LIMITS.md).
It executes, without amending, the precedence of
[Shadowing and Ambiguity](../namespaces-and-shadowing/shadowing-and-ambiguity.md)
and applies [Prelude Selection and Admission](prelude-selection-and-admission.md).

The rules apply only to source-language revision `0.1.22`.

## Precedence

The prelude origin participates in the unchanged C021 precedence table
(`PL-OBL-006`):

1. A binding in the innermost enclosing scope wins over every import
   and over the prelude origin.
2. A module-level local declaration wins over every import and over the
   prelude origin.
3. Otherwise, an unqualified name supplied by both the prelude origin
   and an explicit import origin rejects as `NSP004`, naming every
   colliding origin including the prelude; resolution is by
   qualification (`PreludePackage.name` or the import's qualification).
4. Two explicit imports colliding remains the unchanged C021 rule.
5. Prelude-vs-prelude cannot occur: one selection per package.

Shadowing never crosses categories and inner scopes shadow the prelude
exactly as they shadow imports. There is no weaker tier (an import does
not silently shadow a prelude name) and no stronger tier (the prelude
does not shadow an import) (`PL-OBL-006`). No shadowing warning or
denial specific to the prelude exists in this revision.

## Opt-out

Opting out is the absent or `null` `prelude` field (`PL-OBL-007`).
With no selection, no prelude origin exists: no name resolves from a
prelude, no qualification names one, and no diagnostic may suggest one.
No `none` sentinel, per-name hiding list, or exclusion event exists; a
tool that wants no prelude writes nothing. A package that selected a
prelude in one revision and removes the field in the next has changed
its own scope only, under the ordinary C008 revision semantics.

## The edition guarantee

Edition `0.1` guarantees: every in-scope name comes from a local
declaration, an explicit import, or an explicitly selected prelude; no
name is ever implicitly in scope (`PL-OBL-008`). This guarantee is
checkable — a resolution context built from a manifest without a
`prelude` field MUST resolve no name from any prelude origin.

A future edition naming a default prelude MUST do so through a C008
lifecycle record that names the package, the requirement, the
migration, and the affected revisions; it MUST NOT enter through
compiler behavior, tooling convention, or silence (`PL-OBL-008`).
Until such a record exists, every conforming implementation resolves
bare selections exactly as this chapter states. Freezing prelude
contents (G101) adds to this guarantee without weakening it.

## Deliberately separate work

Prelude contents and the edition-record decision remain G101 and future
edition work; scaffolding defaults remain G121; the compatibility
meaning of a prelude version bump remains G028/G136.

## Rationale and evidence (non-normative)

The [prelude synthesis](../../20-notes/catena-prelude-policy.md) records
the Haskell ambiguity-transfer and frozen-core costs and why ordinary
qualification discharges what `hiding` would.
