---
title: "API and ABI Compatibility Diagnostics and Conformance"
kind: specification
created: "2026-08-24"
status: normative
spec_version: "0.1.24"
tags:
  - conformance
  - diagnostics
  - compatibility
  - specification
  - testing
aliases:
  - "Catena 0.1.24 compatibility conformance"
---

# API and ABI Compatibility Diagnostics and Conformance

## Status and authority

This chapter is the normative Catena 0.1.24 compatibility diagnostic,
abstract frontend, and conformance contract. It is governed by
[Specification Authority](../../SPECIFICATION-AUTHORITY.md),
[Catena Conformance Vocabulary](../../CONFORMANCE-VOCABULARY.md), and
[Catena Implementation Limits and Portability](../../IMPLEMENTATION-LIMITS.md).
It applies [Compatibility Layers and Versions](compatibility-layers-and-versions.md)
and [Breaking Change Matrix](breaking-change-matrix.md).

## Stable diagnostics

| ID | Required meaning |
| --- | --- |
| `CMP001` | a version claim below the matrix's required class: a breaking diff claimed as minor or patch, or a minor diff claimed as patch |
| `CMP002` | malformed compatibility input: an undecodable interface, a non-object entry shape, or a malformed claimed version |
| `CMP003` | unclassifiable drift: interface content that differs outside every matrix row or that a conforming classifier cannot assign |

All other compatibility-adjacent failures reuse existing families
unchanged: SemVer grammar failures are C025's `PKG001` family;
selection failures remain `EDN001` (`CP-OBL-009`). Failure is
transactional; diagnostics carry the offending shape and the itemized
diff reasons. Diagnostic prose can improve only within the bounded
presentation rules.

## Abstract public boundaries

Two boundaries gain compatibility wiring (`CP-OBL-001`):

- **Interface diff** — a diff operation takes two decoded semantic
  interfaces and returns the ordered itemized change list and its
  classification (breaking, minor, patch, identical), or `CMP002` for
  malformed inputs and `CMP003` for unclassifiable drift.
- **Claim validation** — a validation operation takes two decoded
  interfaces and a claimed version pair, classifies the diff, and
  returns the verdict with reasons, or `CMP001` when the claim is
  below the required class. It reuses C025's vendored SemVer grammar
  and precedence for the claim side.

Implementations MUST NOT use these boundaries to claim behavioral
compatibility, BEAM ABI stability, migration, or any excluded
machinery (`CP-OBL-010`). The bootstrap evidence adds no new public
API names beyond the diff and claim-validation operations.

## Determinism

Equal interfaces and equal claims produce equal itemized diffs,
classifications, verdicts, or diagnostics; classification is order-,
locale-, and tool-independent (`CP-OBL-010`). The classifier is total
over decodable interfaces: it never crashes on well-formed input and
reports `CMP003` rather than guessing.

## Conformance obligations

| ID | Obligation | Required executable evidence |
| --- | --- | --- |
| `CP-OBL-001` | apply compatibility behavior only at exact 0.1.24 and register the stable lifecycle addition | exact selection, registry, and lifecycle tests |
| `CP-OBL-002` | fix one stance per layer: source rules, interface matrix, behavior absence, ABI absence | layer-stance and absence tests |
| `CP-OBL-003` | keep retained revisions immutable with cumulative-forward acceptance | revision-pinning tests |
| `CP-OBL-004` | classify every matrix row correctly from decoded interfaces with itemized reasons | full-matrix tests |
| `CP-OBL-005` | enforce version-meaning claims: major-as-breaking at 1.0+, minor-as-breaking under 0.x, with `CMP001` under-claims | claim-matrix tests |
| `CP-OBL-006` | report unclassifiable drift as `CMP003` and malformed input as `CMP002`, never guessing | drift and shape tests |
| `CP-OBL-007` | resolve the C022–C027 deferrals: facade exclusion, digest identity-only, lock-replay skew, prelude-bump classification, entry-set rows | deferral-resolution tests |
| `CP-OBL-008` | keep representation changes, digest recomputation, and warning additions never breaking alone | non-breaking tests |
| `CP-OBL-009` | emit stable diagnostics: `CMP001`–`CMP003` plus reused families with unchanged identities | every diagnostic family test |
| `CP-OBL-010` | keep the classifier deterministic, interface-only, and outside behavior/ABI/migration/tooling claims | repeated-result and exclusion tests |

Every obligation has at least one tagged passing test. The sibling
compiler gates the complete `CP-OBL-*` set against unknown and
uncovered identifiers before C028 conformance is claimed.

## Required evidence sets

Positive evidence includes every matrix row classified in both
directions where applicable (row widening breaking, narrowing minor);
identical interfaces classified identical; additive-only diffs minor
at patch claims below 1.0 and minor claims at 1.0+; breaking diffs
satisfying minor claims under 0.x and major claims at 1.0+; entry-set
and prelude-bump classification; and determinism across repeated
classification.

Negative evidence includes `CMP001` for every under-claim direction;
`CMP002` for undecodable interfaces, malformed shapes, and invalid
claimed versions; `CMP003` for drift outside every row; and reused
`PKG001`/`EDN001` identities unchanged.

Exclusion evidence demonstrates that the classifier parses no source,
claims no behavior, promises no ABI, and that representation-only
changes and digest recomputations never produce a breaking class.

## Revision and persistence separation

Revision `0.1.24` adds the layer stances, version meanings, the
matrix, the facade exclusion, the diff and claim-validation
operations, and `CMP001`–`CMP003`; it adds no JSON AST version,
kernel S-expression version, interface version, artifact version,
signature domain, typing rule, runtime behavior, or BEAM
representation, and no manifest field (`CP-OBL-001`, `CP-OBL-010`).

The source-text decoder accepts cumulative revisions `0.1.9` through
`0.1.24`; every predecessor API retains its exact selection. The next
unused semantic patch is `0.1.25`.

## Rationale and evidence (non-normative)

The design route is preserved in the
[compatibility synthesis](../../20-notes/catena-api-and-abi-compatibility.md),
the [resolved inquiry](../../40-inquiries/how-should-catena-define-api-and-abi-compatibility.md),
and the [topic map](../../10-maps/api-and-abi-compatibility.md). The
C028 evidence record will preserve the sibling-compiler commands and
archive validation.
