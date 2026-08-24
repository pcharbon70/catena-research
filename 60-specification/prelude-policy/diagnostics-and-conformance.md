---
title: "Prelude Diagnostics and Conformance"
kind: specification
created: "2026-08-24"
status: normative
spec_version: "0.1.22"
tags:
  - conformance
  - diagnostics
  - prelude
  - specification
  - testing
aliases:
  - "Catena 0.1.22 prelude conformance"
---

# Prelude Diagnostics and Conformance

## Status and authority

This chapter is the normative Catena 0.1.22 prelude diagnostic, abstract
frontend, and conformance contract. It is governed by
[Specification Authority](../../SPECIFICATION-AUTHORITY.md),
[Catena Conformance Vocabulary](../../CONFORMANCE-VOCABULARY.md), and
[Catena Implementation Limits and Portability](../../IMPLEMENTATION-LIMITS.md).
It applies [Prelude Selection and Admission](prelude-selection-and-admission.md)
and [Shadowing, Opt-Out, and the Edition Guarantee](shadowing-optout-and-edition-guarantee.md).

## Stable diagnostics

| ID | Required meaning |
| --- | --- | 
| `PRE001` | a malformed `prelude` selection: non-object value, missing or non-string `package`/`requirement`, invalid package name, invalid requirement grammar, or a duplicated selection |

All other prelude failures reuse existing families unchanged: an unknown
prelude package is `PKG004`; an unsatisfiable prelude requirement is
`PKG003` with every requirer listed; a prelude-import unqualified
collision is `NSP004` naming both origins; an exact-selection mismatch
remains `EDN001` (`PL-OBL-009`). Failure is transactional; diagnostics
carry the offending field and shape. Diagnostic prose can improve only
within the bounded presentation rules.

## Abstract public boundaries

Three shipped boundaries gain prelude wiring (`PL-OBL-001`):

- **Manifest decode** — the optional `prelude` object validates to a
  name and requirement or rejects as `PRE001`; absent and `null` both
  decode to no selection.
- **Environment construction** — `Catena.build_namespace_environment/2`
  (event grammar extended at `0.1.22`, both shapes accepted) admits a
  prelude option or event that injects the resolved prelude package's
  exports as an ordinary import-class origin; streams without it build
  the unchanged 0.1.20-compatible environment.
- **Dependency resolution** — `Catena.Package.Deps.resolve/2` treats
  the prelude selection as an ordinary dependency whose requirers are
  marked as the prelude; `generate_lockfile/2` records it with its
  exact version and bundle digest; `replay_lockfile/3` pins it as an
  exact pin under the unchanged `PKG005` rules.

Implementations MUST NOT use these boundaries to claim G101 contents,
G121 scaffolding, or any default selection (`PL-OBL-010`). The
bootstrap evidence adds no new public API names beyond the option and
event forms on the three existing operations.

## Determinism

Equal manifests and environments produce equal prelude resolutions,
lock bytes, or diagnostics; an environment built with a prelude
selection and one built without resolve exactly the names their origins
supply — nothing more (`PL-OBL-010`).

## Conformance obligations

| ID | Obligation | Required executable evidence |
| --- | --- | --- |
| `PL-OBL-001` | apply prelude behavior only at exact 0.1.22 and register the stable lifecycle addition | exact selection, registry, and lifecycle tests |
| `PL-OBL-002` | enforce the one-selection rule with absent/`null` equivalence and zero-export packages admitted | selection shape and equivalence tests |
| `PL-OBL-003` | reject malformed selections as `PRE001` with the offending shape | malformed matrix tests |
| `PL-OBL-004` | admit the resolved prelude as an ordinary import-class origin under C022 validation, reusing `PKG004`/`PKG003` | admission, unknown-name, and unsatisfiable tests |
| `PL-OBL-005` | resolve, lock, and replay the prelude selection as an ordinary dependency with marked requirers and bundle digest | lock generation and replay tests |
| `PL-OBL-006` | execute unchanged C021 precedence: locals win; prelude-import collisions reject as `NSP004` naming both origins; no tier exists | precedence and collision tests |
| `PL-OBL-007` | make absent/`null` the complete opt-out: no origin, no qualification, no suggestion | opt-out resolution tests |
| `PL-OBL-008` | guarantee zero implicit names for edition 0.1 and require a lifecycle record for any future default | no-field zero-origin tests |
| `PL-OBL-009` | emit stable diagnostics: `PRE001` plus the reused families with unchanged identities | every diagnostic family test |
| `PL-OBL-010` | keep the wiring deterministic, source-only, and outside G101/G121 phases | repeated-result and absent-phase tests |

Every obligation has at least one tagged passing test. The sibling
compiler gates the complete `PL-OBL-*` set against unknown and
uncovered identifiers before C026 conformance is claimed.

## Required evidence sets

Positive evidence includes a manifest with a `prelude` object decoding
and resolving; the prelude origin's names resolving unqualified and by
qualification; locals shadowing prelude names; locks recording the
prelude with its digest and marked requirer; replay pinning it; `null`
equivalence with absence; and a zero-export prelude package admitted.

Negative evidence includes every `PRE001` shape; an unknown prelude
package as `PKG004`; an unsatisfiable prelude requirement as `PKG003`;
a prelude-import collision as `NSP004` with both origins; and a stale
prelude pin as `PKG005`.

Exclusion evidence demonstrates that a manifest without the field
resolves no prelude name under any circumstance, that streams without
the prelude option build the unchanged environment, and that
predecessor APIs retain their exact selections and defaults.

## Revision and persistence separation

Revision `0.1.22` adds the prelude field, origin wiring, and
`PRE001`; it adds no JSON AST version, kernel S-expression version,
interface version, artifact version, signature domain, typing rule,
runtime behavior, or BEAM representation (`PL-OBL-001`, `PL-OBL-010`).
The manifest extension is optional and backward-compatible: every
previously valid manifest remains valid.

The source-text decoder accepts cumulative revisions `0.1.9` through
`0.1.22`; every predecessor API retains its exact selection, with the
namespace resolver's grammar advancing to accept both event shapes. The
next unused semantic patch is `0.1.23`.

## Rationale and evidence (non-normative)

The design route is preserved in the
[prelude synthesis](../../20-notes/catena-prelude-policy.md), the
[resolved inquiry](../../40-inquiries/how-should-catena-define-its-prelude-policy.md),
and the [topic map](../../10-maps/prelude-policy.md). The C026
evidence record will preserve the sibling-compiler commands and archive
validation.
