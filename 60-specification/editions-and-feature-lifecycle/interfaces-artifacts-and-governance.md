---
title: "Edition Interfaces, Artifacts, and Governance"
kind: specification
created: "2026-08-05"
status: normative
spec_version: "0.1.7"
tags:
  - compatibility
  - governance
  - provenance
  - specification
aliases:
  - "Catena 0.1.7 version-bound artifacts"
---

# Edition Interfaces, Artifacts, and Governance

## Selection-bearing interfaces

A version 0.1.7 `catena-interface` contains `edition`, `language_revision`,
sorted duplicate-free enabled `previews`, and sorted duplicate-free
`required_previews` in addition to its artifact `version`. Its digest covers
all five identities and the complete semantic payload.

The interface builder computes `required_previews` from exported semantics,
not from the package's enabled set alone. Import validation occurs before
trait solving, specialization, assurance aggregation, or backend lowering.

Legacy 0.1.2 through 0.1.6 interfaces retain their historical bytes and imply
edition `0.1`, language revision equal to their artifact version, and no
previews. Decoding that implication MUST NOT rewrite or redigest the artifact.

## Package and assurance artifacts

Every new 0.1.7 package result and assurance manifest records the resolved
edition, language revision, and previews. Artifact digests, dependency
digests, specialization keys, assurance identity, and any compiler cache key
MUST bind that selection. Replacing any component without recomputing and,
where applicable, reauthorizing the artifact MUST fail verification.

A 0.1.7 governed package uses 0.1.7 governance, trust-root, and assurance
formats. Historical 0.1.6 artifacts remain independently verifiable but MUST
NOT be relabeled as 0.1.7 without regeneration and new signatures.

## BEAM metadata and erasure

The OTP compile-information chunk records the frontend artifact version,
selected edition, exact language revision, sorted previews, and applicable
specification revision. These values describe the build and are covered by the
BEAM artifact digest.

Edition, revision, preview, migration, and governance selection MUST NOT cause
runtime dispatch or introduce an edition registry into executable function
bodies. Specifications, policies, signatures, and migration records remain
subject to the 0.1.6 erasure contract. Selection metadata itself MAY remain in
the non-executable compile-information chunk.

## Version-aware signature domains

Canonical signed payloads use the artifact's declared format version as part
of the domain. The verifier first validates a recognized artifact format and
its internally bound version, then constructs exactly one matching domain. It
MUST NOT retry another version domain after signature failure.

> **Normative definition.**

```text
payload(kind, format_version, signed_value) =
  "catena:" ++ kind ++ ":" ++ format_version ++ "\n" ++ jcs(signed_value)
```

The `format_version` is included in or cryptographically bound by
`signed_value`. Kind remains one of the closed 0.1.6 signing kinds unless a
later normative slice adds one. The verifier supports historical 0.1.6 domains
and the new 0.1.7 domains without cross-version fallback.

## Optional governance constraints

Ungoverned packages use their valid manifest selection directly. Governance
MAY narrow that selection but cannot admit an edition, revision, preview, or
diagnostic state rejected by the language rules.

Version 0.1.7 extends the closed policy algebra with these requirements:

- `edition` succeeds when the selected edition is in its `allowed` list;
- `language_revision` succeeds when the selected registered revision lies in
  its inclusive `from` and `to` range;
- `previews` succeeds when every selected preview is in its `allowed` list;
  and
- `diagnostics` succeeds when none of its `absent` diagnostic IDs occurred.

Each requirement consumes the ordinary shared policy budget and contributes
its selected and allowed values to the explanation tree. Unknown fields,
versions, ranges, preview names, or diagnostic IDs fail closed as `GOV002`.

Language selection joins the package, profile, action, module, subject, claim,
and artifact identities already bound by approvals and assurance output. A
change to the selection invalidates an approval for the old selection.

## Scope boundary

These additions define only the 0.1.7 transition. General policy-schema
migration, interpretation by arbitrarily newer compilers, archived evidence,
and reproducible historical decisions remain G116.

## Connections (non-normative)

The underlying 0.1.6 signed-artifact and erasure contract is defined by the
[Specifications and Governance Specification](../specifications-and-governance/README.md).
The broader architecture is summarized in the
[Catena Language Overview](../../language-overview.md).
