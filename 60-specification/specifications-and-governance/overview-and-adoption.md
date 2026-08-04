---
title: "Specification and Governance Overview and Adoption"
kind: specification
created: "2026-08-03"
status: normative
spec_version: "0.1.6"
tags:
  - governance
  - specification
aliases:
  - "Catena 0.1.6 assurance boundary"
---

# Specification and Governance Overview and Adoption

## Status and authority

This chapter and its five siblings are the normative Catena 0.1.6 assurance
slice. They extend the normative 0.1.1 through 0.1.5 language slices without
changing an ungoverned program's meaning. `MUST`, `MUST NOT`, `SHOULD`, and
`MAY` state conformance requirements.

The [conformance gate](diagnostics-and-conformance.md#promotion-gate) was
satisfied for the C006 semantic boundary by the authorized immutable compiler
commit and reproducible evidence recorded in the
[C006 conformance journal](../../50-journal/2026-08-03-c006-executable-specification-governance-conformance.md).
That run used the retired `0.1` through `0.6` protocol identifiers and is not
evidence for the exact renumbered strings. The fresh cross-slice gate is
recorded in
[Prototype Slice Renumbering](../../50-journal/2026-08-04-prototype-slice-renumbering.md).
The research [synthesis](../../20-notes/language-integrated-specifications-and-governance.md)
and [inquiry](../../40-inquiries/how-should-catena-integrate-specifications-and-governance-into-the-language.md)
retain unresolved work beyond this deliberately small spine.

Document status, content labels, rule references, and conflict handling follow
the repository
[Specification Authority](../../SPECIFICATION-AUTHORITY.md). That policy is
separate from the Catena declarations and governed actions specified by this
0.1.6 language slice.

## Adoption boundary

Specification and governance adoption is optional per package and occurs at
two explicit boundaries. A package with no 0.1.6 declarations or manifest uses
the ordinary 0.1.1–0.1.5 pipeline, emits no assurance manifest, loads no trust
root, and produces the same BEAM bytes it produced before 0.1.6. Declaring 0.1.6
rules adopts typed checking and an assurance sidecar for `build`; naming a
governance bundle separately adopts organizational policy. A
specification-only package may build without inventing an authority structure,
but it cannot report `publish` or `activate` as successful.

Once a package declares a specification:

- every rule and example MUST be well formed, type checked, evaluated, and
  reported honestly; and
- verification material MUST satisfy the erasure and artifact-binding rules.

Once a package names a governance bundle:

- every policy whose scope matches the requested action MUST be enforced;
- malformed, missing, stale, unauthorized, or contradictory material MUST
  fail closed for that action;
- an implementation MUST NOT offer an ignore or force switch that reports a
  governed action as successful; and
- narrower scope MUST NOT weaken policy inherited from a broader scope.

`build`, `publish`, and `activate` are distinct governed actions. Policy may
allow a local build while rejecting publication or activation.

## Three protocol artifacts

Version 0.1.6 defines exactly three canonical JSON artifacts:

1. `catena-trust-root` version `0.1.6` identifies offline Ed25519 principals,
   roles, thresholds, delegations, recovery authority, and root history;
2. `catena-governance-bundle` version `0.1.6` contains policies, evidence,
   approvals, and lifecycle transitions for one package; and
3. `catena-assurance-manifest` version `0.1.6` binds the validated semantic graph
   and governance result to exact emitted artifacts.

The package manifest remains the build entry point. A 0.1.6 manifest names its
selected profile and assurance output and may name a governance bundle.
Private signing keys are never package inputs.

## Public and internal vocabulary

The programmer-facing concepts are `rule`, `example`, `evidence`,
`attestation`, `assumption`, `policy`, `approval`, and lifecycle action. The
implementation may use formal terminology internally, but diagnostics MUST
state what was checked, what was missing, which actor or evidence was counted,
and which action was blocked.

## Guarantees

The bounded 0.1.6 slice provides:

- stable claim identifiers and formatting-insensitive semantic digests;
- typed parameterized rules and exact executable examples;
- compiler-derived conformance evidence, signed external attestations, and
  explicitly authorized assumptions without conflating them;
- a deterministic 20,000-step pure checker;
- package, module, language-subject, action, output, interface, and named-profile
  governance subjects;
- a closed, terminating, explainable policy algebra;
- offline Ed25519 trust with thresholds, scoped delegation, rotation,
  revocation, and predeclared recovery;
- hash-chained, sequence-ordered lifecycle transitions;
- fail-before-publish package staging and exact artifact binding; and
- complete removal of specification and governance material from emitted
  `.beam` code.

## Deliberate exclusions

Version 0.1.6 does not freeze public parser punctuation, runtime contracts or
monitors, generated property testing, bounded model checking, proof
certificates, temporal specifications, network services, wall-clock expiry,
transparency logs, hardware-key protocols, package-manager transport,
cross-format migrations, or interpretation by future compiler versions.

Those exclusions keep long-term evolution item G116 open. They do not permit
an implementation to invent an alternate runtime profile or signature format
under version `0.1.6`.

## BEAM boundary

The compiler remains an Elixir bootstrap targeting Erlang/OTP 29 Abstract
Format. Version 0.1.6 does not authorize Rust or Python compiler components,
Core Erlang, direct BEAM assembly, or an alternate virtual machine.
