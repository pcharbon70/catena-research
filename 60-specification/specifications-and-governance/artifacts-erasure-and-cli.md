---
title: "Assurance Artifacts, Erasure, and CLI"
kind: specification
created: "2026-08-03"
status: normative
spec_version: "0.6"
tags:
  - beam-vm
  - governance
  - specification
aliases:
  - "Catena 0.6 assurance manifest"
---

# Assurance Artifacts, Erasure, and CLI

## Package build transaction

A governed package build is a transaction:

1. decode all module, package, bundle, and trust-root inputs;
2. type check and independently verify every module;
3. evaluate examples and compiler conformance checks;
4. lower runtime definitions through Erlang/OTP 29 Abstract Format;
5. hold every BEAM module, interface, companion module, and sidecar in memory
   or an implementation-owned temporary directory;
6. compute artifact digests and the complete candidate transition payload;
7. replay trust and lifecycle history and evaluate every applicable policy;
8. emit the external-signer payload and verify supplied signatures; then
9. atomically place final outputs only after the requested action succeeds.

Failure before step 9 MUST leave no new or partially replaced final output.
Declared output paths MUST remain within the manifest directory unless an
explicit tool-level output root contains them. Absolute paths, `..` escape,
symlink escape, output collision, and input overwrite are `ART001`.

## Assurance manifest

`catena-assurance-manifest` version `0.6` contains at least:

- package and profile identity;
- compiler, frontend, specification, OTP, and canonicalization versions;
- sorted module BEAM and interface paths, sizes, and SHA-256 digests;
- semantic digests of imported interfaces that contribute inherited claims;
- companion artifact identity when present;
- claim IDs, semantic digests, resolved subjects, and dependencies;
- example and conformance outcomes;
- external attestations and explicit assumptions;
- trust-root, policy, proposal, transition, and governance-bundle digests;
- replayed lifecycle state and requested action;
- an erasure report; and
- canonical signing payload and digest.

The manifest describes artifacts but is not runtime state. Removing it after a
successfully admitted build MUST NOT change BEAM execution. Changing any bound
BEAM or interface byte MUST make later verification fail.

## Erasure rule

The 0.6 runtime profile retains no specification or governance material.
Verification-only definitions, claims, examples, evidence, policies,
approvals, histories, public keys, signatures, signing payloads, and assurance
digests MUST NOT occur in:

- executable function bodies or exports;
- literal pools;
- custom BEAM chunks;
- module attributes or compile information;
- BEAM export tables or runtime-facing module metadata; or
- companion specialization functions.

The erasure report lists verification-only definitions removed, retained
runtime definitions, and `runtime_monitors: []`. Any runtime reference to
erased material or any retained assurance term is `ERS001`.

For identical runtime input, layout, condition lowering, compiler identity,
and source path, adding fully discharged 0.6 specifications MUST produce
byte-identical BEAM modules. The comparison includes all BEAM chunks.

## CLI contract

The package compiler accepts:

> **Normative definition.**

```text
catena compile-package-ir \
  --action build|publish|activate \
  [--trust-root FILE] PACKAGE.json

catena verify-assurance \
  --trust-root FILE MANIFEST.json
```

An ungoverned package may omit both options. A governed package requires an
explicit action; `publish` and `activate` require a trust root. The compiler
prints structured JSON containing output paths, digests, decision, evidence
outcomes, and the signing payload. It does not sign.

`verify-assurance` reads artifacts rather than rebuilding them. It verifies
canonical form, digests, signatures, trust and transition chains, policy
decision, artifact sizes and hashes, and the erasure report. Success means the
manifest accurately describes the inspected artifacts under the supplied
root; it does not independently prove every external attestation true.

## Interface boundary

A 0.6 module interface MAY export claim summaries and inherited obligations as
non-runtime build artifacts. It MUST NOT export verification-only values as
ordinary callable values. The interface digest covers all summaries so that a
dependent package cannot silently discard an obligation.

## Connections (non-normative)

The [language overview](../../language-overview.md#8-verification-erasure-and-artifact-integrity)
places this artifact split in the wider compiler architecture. Exact failure
families and the byte-identity audit are specified in
[Diagnostics and Conformance](diagnostics-and-conformance.md).
