---
title: "Authority and Representation Exclusions"
kind: specification
created: "2026-08-23"
status: candidate
spec_version: "0.1.19"
tags:
  - abstraction
  - specification
aliases:
  - "Catena authority and representation exclusions"
---

# Authority and Representation Exclusions

## Status and authority

This chapter is the normative Catena 0.1.19 abstraction-boundary
exclusion contract. It is governed by
[Specification Authority](../../SPECIFICATION-AUTHORITY.md),
[Catena Conformance Vocabulary](../../CONFORMANCE-VOCABULARY.md), and
[Catena Implementation Limits and Portability](../../IMPLEMENTATION-LIMITS.md).
It confirms, and does not amend, the contracts of
[Interfaces and Representation](../data-and-patterns/interfaces-and-representation.md)
and
[Export Declarations and Visibility](../imports-and-exports/export-declarations-and-visibility.md).

The rules apply within the retained `0.1` edition at revision `0.1.19`
and change no accepted input.

## The authority vocabulary is complete

Constructor authority over a nominal datatype is exactly the pair of
modes C022 fixes (`AB-OBL-002`):

- **transparent** — the type is exported together with its constructor
  surface; every exported constructor is available for construction and
  for pattern matching, with no separation;
- **abstract** — the type is exported without its constructors; neither
  construction nor matching by constructor spelling is available outside
  the defining module.

Edition 0.1 defines no construction-only, matching-only, partial, or
per-constructor authority mode. An export event whose type transparency
is neither `transparent` nor `abstract` is C022 `EXP001`; no other
authority-bearing form exists on any frontend. Selective exposure and
view-based decomposition are declared future work owned by D046 and G040;
admitting either requires an explicit later semantic revision from that
owner, and this chapter reserves no spelling for them.

## Representation is never observable

No datatype declaration, export, interface field, or other source form in
edition 0.1 makes a datatype's runtime representation observable
(`AB-OBL-003`). In particular:

- no stable-layout attribute, export mode, interface entry, or pragma
  pins a datatype to the uniform or compact representation as an
  observable contract;
- both-layout conformance remains mandatory: conforming programs check
  and execute under both C002 layouts;
- layout selection remains a post-verification implementation freedom,
  and layout coercion remains `L001` implementation failure;
- an interface MUST NOT expose a chosen layout, per the unchanged C002
  rule.

A future layout-stability or ABI contract — any rule under which a
representation choice becomes a compatibility surface — is owned by G028,
together with the representation (P093), calling-convention (G094), and
foreign-term (G095) boundaries that would consume it. Until that owner
delivers, every appearance of a stable-layout form in any frontend is
invalid input, not a semantics.

## Evolving APIs

C002's rule stands: a datatype whose constructor surface may evolve is
exported abstract with observer functions; closed transparent datatypes
provide no exhaustiveness evolution marker. Edition 0.1 adds no
`non_exhaustive` or similar marker, and no such marker is reserved.

## Deliberately separate work

Any ABI, wire, or serialization contract (G028, G025/G128); views,
pattern synonyms, and selective exposure (D046/G040); structural record
and variant abstraction (G040/G041); foreign-term validation (G095);
BEAM representation mapping (P093).

## Rationale and evidence (non-normative)

The [abstraction synthesis](../../20-notes/catena-abstraction-boundaries.md)
derives both exclusions from the shipped corpus and Leroy's
representation-independence analysis. The
[open inquiry](../../40-inquiries/how-should-catena-draw-its-abstraction-boundaries.md)
and [topic map](../../10-maps/abstraction-boundaries.md) preserve the
decision route.
