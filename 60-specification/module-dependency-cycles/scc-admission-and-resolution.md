---
title: "SCC Admission and Resolution"
kind: specification
created: "2026-08-24"
status: normative
spec_version: "0.1.20"
tags:
  - modules
  - separate-compilation
  - specification
aliases:
  - "Catena SCC admission"
---

# SCC Admission and Resolution

## Status and authority

This chapter is the normative Catena 0.1.20 cycle-admission and
resolution contract. It is governed by
[Specification Authority](../../SPECIFICATION-AUTHORITY.md),
[Catena Conformance Vocabulary](../../CONFORMANCE-VOCABULARY.md), and
[Catena Implementation Limits and Portability](../../IMPLEMENTATION-LIMITS.md).
It extends, and does not amend, the digest-bound admission of
[Import Declarations and Admission](../imports-and-exports/import-declarations-and-admission.md)
and preserves the intra-module recursive groups of
[C002](../data-and-patterns/declarations-and-nominal-identity.md).

The rules apply only to source-language revision `0.1.20`. They do not
reinterpret retained JSON ASTs, kernel S-expressions, interfaces,
artifacts, or signed formats.

## Cycle admission

A module import graph MAY contain cycles (`CY-OBL-002`). No cycle shape
— self-loop, pair, or longer ring — carries a separate rule, and no
cycle is itself an error. The maximal strongly-connected components of
the graph partition it into checking units: each component, including a
single-module component, is the unit of checking, resolution, and
caching under this area.

## The two resolution regimes

For references crossing a module boundary, the applicable regime is
fixed by component membership (`CY-OBL-003`).

*Intra-component.* A reference from one member of a component to another
resolves against the companion's declared export signatures — the
explicit per-definition signatures the retained frontends already
require. An import event whose target module belongs to the same
component as the importing module MUST present an empty digest;
presenting a digest-bound import for a companion is regime mixing,
reported as `CYC001` at that event. A module participating in a
multi-member component MUST declare the signature of every name it
exports for intra-component resolution; a gap is reported as `CYC001`
when the event stream closes the component (`CY-OBL-005`). No computed
interface digest exists for a member until its component finishes
checking.

*Cross-component.* An import of a module outside the importing module's
component is digest-bound and C022-validated, byte-for-byte: known-module
admission, export-set validation, qualification rights, and listed
unqualified admission all apply unchanged (`CY-OBL-004`). A component's
members are known modules to outsiders individually.

## Joint component digest

When a component finishes checking, its members' computed interfaces
yield one joint digest: a deterministic hash over the sorted member
names and each member's interface digest (`CY-OBL-006`). The joint
digest binds the component as one cache and compatibility unit for
C008-addressed consumers; outsiders import against member interfaces
exactly as C022 fixed, and the joint digest adds the component identity
without replacing any member identity.

## The degenerate acyclic case

A module with no cyclic import relationships forms a single-member
component whose behavior is byte-identical to C022: intra-component
rules are vacuous, all imports are cross-component digest admissions,
and its joint digest is derived from its sole interface. Every acyclic
conformance corpus remains conforming without change (`CY-OBL-004`).

## The inversion alternative

When a dependency cycle expresses mutual use rather than genuine mutual
definition, the sanctioned restructuring is dependency inversion: the
reusable module takes the collaborator as an explicit higher-order value
(`serve : (Request -> Reply) -> Config -> Result`), keeping the graph a
DAG (`CY-OBL-007`). Components exist for mutual definition; inversion is
the recommended tool for mutual use. This subsection is a normative
recommendation of structure, not a static rule: inversion violations are
not diagnosable.

## Deliberately separate work

Package assembly over components, lockfile representation of joint
digests, and package identity remain G025. Joint-digest ABI and
compatibility treatment remains G028. The concrete recursive `use`
surface remains P109. Pre-declared standalone interface files are the
declined alternative and remain undesigned. Entry-point selection across
components remains G027.

## Rationale and evidence (non-normative)

The [cycles synthesis](../../20-notes/catena-dependency-cycles.md)
derives the design from the digest circularity, the Haskell recursion
evidence with its named price, and the SML/Erlang contrasts. The
[resolved inquiry](../../40-inquiries/how-should-catena-handle-module-dependency-cycles.md)
and [topic map](../../10-maps/module-dependency-cycles.md) preserve the
decision route.
