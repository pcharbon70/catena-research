---
title: "Guarantees, Assumptions, and Boundary Checks"
kind: specification
created: "2026-09-09"
status: normative
spec_version: "0.1.70"
tags: [specification, conformance, security]
aliases: []
---

# Guarantees, Assumptions, and Boundary Checks

## Status and authority

C126 defines the trusted-computing-base disclosure contract at edition `0.1`,
exact semantic revision `0.1.70`, without previews, under
[authority](../../SPECIFICATION-AUTHORITY.md),
[conformance vocabulary](../../CONFORMANCE-VOCABULARY.md) and
[implementation limits](../../IMPLEMENTATION-LIMITS.md). It executes the
[reviewed trust-base plan](../../20-notes/language-completion-plan-delivery.md#item-126-trusted-computing-base).
It introduces a maintained trust profile and development boundary gate. It changes
no retained program's evaluation, syntax or artifact interpretation and claims
neither a proof-verified compiler nor an OS sandbox (`TC-OBL-001`).

## Guarantee-specific graph

A conformance claim identifies the guarantee it concerns, the components whose
correctness it depends on, the checks that support it and the residual assumptions
those checks do not establish. A single undifferentiated trusted list is
insufficient. The maintained graph covers the following guarantee families
(`TC-OBL-002`).

| Guarantee | Enforcement dependencies | Residual trust that remains explicit |
| --- | --- | --- |
| Source and static acceptance | Decoders, lexical/name rules, inference, type/effect/trait/coverage judgments and structural verifiers | Faithful source interpretation and shared semantic helpers |
| Elaboration and execution correspondence | Core verification, lowering, calling wrappers, OTP compilation and reference comparison | Backend correctness, OTP/ERTS and common-mode compiler/oracle defects |
| Lexical effects and resource lifetime | Slot identity/non-escape, affine resumptions, managed owners, cancellation and cleanup | Scheduler, OS and external adapters; no universal fairness or rollback |
| Artifact and package identity | Canonical encoding, hashes, interfaces, exact rebuild and lock replay | Serializers, build tools, inputs and uncompromised host |
| Governance authenticity and admission | Signature verification, key thresholds, revocation and policy lifecycle | Key custody, configured roots and native crypto; authenticity is not semantic truth |
| Proof and law evidence | Checked predicates/evidence, derived structure and law/conformance suites | Distinct promised/tested/derived evidence levels and unresolved formal composition |
| Erasure and diagnostic provenance | Erased lowering, origin mapping and sidecar checks | Lowering/serialization fidelity and observation host |
| Foreign and native ingress | Whole-carrier codecs, authority ownership and native package admission | NIFs/drivers, approved executables, ERTS and OS isolation |
| Standard operations | Ordinary packages, operation engines, independent numerical/Unicode evidence and laws | Generators, primary tables, primitive operations and finite evidence coverage |
| Reference and differential observations | Separate evaluators, bounded explorers and comparison relations | Shared type/value/codec helpers and bounded search scope |
| Resource and deployment limits | Source/carrier limits, finite workers and mandatory cleanup | Fatal OS/VM exhaustion, scheduling and external availability |
| Maintained trust boundaries | Source/call/data inventory, review and mutation witnesses | Scanner, source parsers, baseline approval and CI host |

The graph assigns every inventoried production source to exactly one maintenance
component. A guarantee can depend on several components, and a component can
support several guarantees. Component names express maintenance ownership, not
claims of process isolation. The graph includes compiler frontends, inference and
evidence construction, core verifiers, lowerers, runtime managers, references,
serializers/governance, foreign/native boundaries, standard libraries, tooling and
build/inventory machinery. External dependencies name Elixir, OTP/ERTS/crypto,
Python, native code, OS services, generated-data inputs and build/root provisioning.

## Independent checks and their limits

The ordinary and kernel core verifiers rederive structural conditions without
calling the main inference entry point. Their independence is limited: they share
Type, Data, Row, Coverage and related semantic helpers with inference. Their
acceptance establishes the stated core conditions, not source fidelity, backend
correctness or a universal implementation proof (`TC-OBL-003`).

A well-typed alternative literal remains well typed. Valid Erlang forms with the
wrong result remain valid input to OTP. Exact artifact rebuilding from the
original core detects substituted forms/binaries under its existing contract,
but build and rebuild using the same defective lowerer can agree incorrectly.
The maintained evidence includes both detected and undetected fault classes;
reports do not replace these distinctions with an unqualified verified label
(`TC-OBL-004`).

The [integrated theorem](../progress-and-preservation/the-integrated-theorem.md#the-composition-lemma)
remains conditional on its named component and composition obligations. There is
no general executable proof kernel discharging every prose theorem in this
bootstrap. Bounded condition checking, coherent evidence, test results, derived
structure and promised laws retain their individual meanings. This contract does
not close P133–P136 or turn reference agreement into a proof (`TC-OBL-005`).

## Authenticity and ingress

Governance signatures bind specified bytes to authorized identities under their
existing [evidence lifecycle](../specifications-and-governance/evidence-identity-and-lifecycle.md).
Even a valid signature over a false correctness claim establishes only the
signature's authenticity conditions. Trust roots, thresholds, revocation,
semantic evidence and policy admission remain distinct checks. The profile names
crypto implementation and key provisioning as residual dependencies (`TC-OBL-006`).

Foreign value admission checks the complete declared carrier through C095's
[typed conversion boundary](../erlang-type-boundary/typed-conversion-and-preservation.md).
Opaque authority additionally needs a live owner/issuer identity under C106;
a nominal tag or type annotation alone is not authority. Native package signatures
and platform checks do not prove native memory safety. Native VM corruption,
unresponsive host services and compromised build/OS state remain outside what
these checks establish (`TC-OBL-007`). General registry acquisition remains P130;
governance trust roots are not a substitute for that future registry boundary.

## Executable source and data inventory

The development gate inventories files under lib, scripts, src, c_src and config,
Python helpers under priv and bootstrap mix.exs. Elixir/Python sources are parsed;
other source formats are refused until an inspection method is explicitly admitted.
It separately hashes package descriptions, Unicode sources and generated data
under priv, excluding its own self-describing trust-profile directory. Whole
mix.exs and any mix.lock bytes are hashed so literal dependency changes also
require review. Newly added or removed source
paths, changed inventoried call expressions and changed inventoried data require
an explicit reviewed inventory update (`TC-OBL-008`).

Elixir inspection parses source without evaluating the inspected module. It
records remote calls, dynamic function calls, selected local runtime operations,
alias/import/require/use declarations and emitted remote-call forms. Python
inspection likewise parses without importing or executing the inspected file,
and records calls and imports. Each source record contains call multiplicity,
target counts and a digest of normalized call expressions. Normalization excludes
source positions and comments; changed call arguments remain visible.

An inventory match is a syntactic assertion, not semantic equivalence, complete
information-flow analysis or an authorization verdict. In particular, changing a
control-flow guard while preserving all recorded call syntax can leave the
inventory unchanged. Macros, generators, source parsers, scanner code and the
trusted checkout/CI environment remain dependencies. Mutation evidence explicitly
exercises this limitation (`TC-OBL-009`).

## Profile and maintenance

The machine profile identifies its format, version, exact disclosure contract,
component/source assignments, guarantee dependency graph, call summaries, data
digests, external assumptions and excluded claims. The complete canonical payload
is SHA-256 bound. Profile verification checks supported identity, assignment
coverage/uniqueness and references; a rehashed forged graph cannot replace the
supported baseline. Conformance information exposes the profile digest,
guarantee identities, source/data counts and assumptions, with proof-verified
compiler and runtime-sandbox flags false (`TC-OBL-010`).

The audit command checks and reports; it does not regenerate or approve its own
baseline. A deliberate update reviews changed source/authority paths, affected
guarantee dependencies, residual assumptions and tests before updating ownership,
call/data evidence and the canonical digest in the same change. A new direct OTP
compiler call, foreign dispatch or unclassified production file fails the current
baseline. It cannot be made conforming merely by suppressing the test.

## Bounds and reporting

Each parsed source has a fixed maximum of 2,000,000 bytes. Parsing occurs only
after reading that source, so this ceiling does not promise to prevent every
prior allocation. The scanner is a development check over a trusted checkout,
not a hostile-repository sandbox. Actual source/call/data counts are disclosed
by the profile, not treated as universal language limits (`TC-OBL-011`).

Invalid source syntax, oversized source and unreadable files return inventory
boundary errors. Path differences distinguish unclassified source, missing source
and changed boundary calls; the same comparison mechanism reports changed data
identity. Audit failure refuses a claim that the checkout matches the reviewed
boundary. It does not change ordinary language runtime failure classes or
retroactively invalidate retained artifacts.

Work scales with total source syntax, normalized call-expression size and hashed
data. Nested expressions can be included in more than one call fingerprint;
linearity in file bytes is not promised. Core verification, compilation,
cryptography, native execution and whole-language proof obligations retain their
own costs and trust assumptions. Mutation tests are finite witnesses, not a
complete security evaluation or a universal fault-detection guarantee.

## Variability register

Graph identity, source coverage, call/data comparison and excluded claims are
fixed for the supported profile. A reviewed new profile is an explicit change.
The source ceiling is fixed at 2,000,000 bytes; inherited compiler/carrier/runtime
limits remain under their owners. External host dependencies and incomplete
proof obligations are disclosed assumptions, not permission for arbitrary
language behavior.

## Rationale and evidence (non-normative)

The [journal](../../50-journal/2026-09-09-trusted-computing-base.md) records the actual
source inventory and detected/undetected mutations. The
[governance synthesis](../../20-notes/language-integrated-specifications-and-governance.md)
explains why signatures, tests and proofs establish different facts. The
[greenfield type-system synthesis](../../20-notes/catena-greenfield-type-system.md)
provides the architecture behind structural checking and evidence separation.
