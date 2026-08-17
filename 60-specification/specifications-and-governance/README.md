---
title: "Specification and Governance Specification"
kind: map
created: "2026-08-03"
tags:
  - archive-navigation
  - directory-index
  - governance
  - specification
aliases:
  - "Catena specification-governance index"
---

# Specification and Governance Specification (`60-specification/specifications-and-governance`)

## Purpose

These candidate chapters define Catena 0.1.6's bounded specification and
governance spine: typed rules, executable examples, honest evidence kinds,
governed subjects, additive policy, offline trust, lifecycle replay, artifact
binding, and complete erasure from executable BEAM modules.

## What belongs here

Keep the version 0.1.6 semantic JSON forms, checking rules, governance bundle,
trust-root, assurance-manifest, package gate, and conformance obligations here.
Public parser punctuation, runtime monitors, general theorem proving, temporal
models, network identity, transparency services, and schema migration remain
outside this bounded version.

Document authority and rendered content labels follow the repository
[Specification Authority](../../SPECIFICATION-AUTHORITY.md). This repository
policy is distinct from the Catena 0.1.6 governance language feature defined in
this directory.
Requirement words, behavior classes, permitted variation, limits, and profile
disclosure follow the repository
[Catena Conformance Vocabulary](../../CONFORMANCE-VOCABULARY.md).
Portable minima, finite-resource measurement, and exhaustion reporting follow
[Catena Implementation Limits and Portability](../../IMPLEMENTATION-LIMITS.md).

Every chapter is `normative`. The authorized immutable compiler commit,
independent policy-oracle agreement, adversarial and erasure tests, and
reproducible [C006 conformance journal](../../50-journal/2026-08-03-c006-executable-specification-governance-conformance.md)
satisfied the historical semantic promotion gate under retired `0.1` through
`0.6` identifiers. That evidence does not establish the exact renumbered wire
identities. The hard cutover and fresh cross-slice evidence requirement are
recorded in
[Prototype Slice Renumbering](../../50-journal/2026-08-04-prototype-slice-renumbering.md).
The chapters settle the bounded 0.1.6 semantic contract; the research inquiry
remains active for the deliberately excluded work.

## Variability register

| Governing rule | Classification and bound |
| --- | --- |
| [Claims, Examples, and Checking — Module declarations](claims-examples-and-checking.md#module-declarations) | `MAY` permits the semantic AST to add specifications and mark ordinary definitions verification-only; adoption remains explicit and typed. |
| [Artifacts, Erasure, and CLI — Interface boundary](artifacts-erasure-and-cli.md#interface-boundary) | Interfaces `MAY` export non-runtime claim summaries and inherited obligations but cannot export verification-only values. The bootstrap profile records that summaries are emitted. |
| [Claims, Examples, and Checking — Exact executable examples](claims-examples-and-checking.md#exact-executable-examples) | Each example has a fixed 20,000 semantic-step budget and reports `EVD003` separately from counterexamples and runtime errors. |
| [Scopes, Policy, and Authorization — Closed policy algebra](scopes-policy-and-authorization.md#closed-policy-algebra) | All matching policies share a fixed 20,000-step budget; exhaustion reports `GOV002` and denies rather than silently dropping policy. |
| Area result | This slice defines no implementation-defined choice, unspecified presentation, or `SHOULD` recommendation. |

## Index

### Subdirectories

- None yet.

### Documents

- [Overview and Adoption](overview-and-adoption.md) — authority, opt-in
  boundary, component formats, guarantees, and exclusions.
- [Claims, Examples, and Checking](claims-examples-and-checking.md) — typed
  subjects, claim identity, verification-only definitions, exact examples,
  assumptions, and bounded outcomes.
- [Scopes, Policy, and Authorization](scopes-policy-and-authorization.md) —
  governed subjects and actions, additive scope, closed policy combinators,
  roles, distinct actors, and fail-closed decisions.
- [Evidence, Identity, and Lifecycle](evidence-identity-and-lifecycle.md) —
  evidence distinctions, canonical signatures, offline roots, delegation,
  rotation, revocation, recovery, and immutable transitions.
- [Artifacts, Erasure, and CLI](artifacts-erasure-and-cli.md) — package
  staging, assurance manifests, BEAM binding, erasure audit, and commands.
- [Diagnostics and Conformance](diagnostics-and-conformance.md) — stable
  diagnostic families, required positive and adversarial corpus, reference
  oracle, and promotion gate.

## Maintaining this index

Version these chapters together. A lifecycle change must update the compiler
identity, conformance journal, C006-family checklist entries, active inquiry,
research map, root specification index, language overview, and affected source
notes atomically.
