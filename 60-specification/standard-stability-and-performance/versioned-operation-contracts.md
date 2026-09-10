---
title: "Versioned Operation Contracts"
kind: specification
created: "2026-09-10"
status: normative
spec_version: "0.1.87"
tags: [specification, standard-library, compatibility, performance]
aliases: []
---

# Versioned Operation Contracts

## Status and authority

P108 defines revision `0.1.87` under [authority](../../SPECIFICATION-AUTHORITY.md),
[conformance vocabulary](../../CONFORMANCE-VOCABULARY.md), and
[implementation limits](../../IMPLEMENTATION-LIMITS.md). It executes the
[P108 plan](../../20-notes/language-completion-plan-delivery.md#item-108-stability-and-performance-policy)
over C004 operation semantics, C028 interface compatibility, and the completed
P101–P106 standard packages. It introduces no public source vocabulary; P109
retains that decision (`SP-OBL-001`).

## Operation contract inventory

Every conforming standard operation MUST have one stable internal identity and
one package revision. Its machine-readable record MUST state its governing law
contract, accepted-input requirements, evaluation order, callback
multiplicity, failures, worst-case time and auxiliary-space class, stack bound,
stability tier, and representation promise (`SP-OBL-002`).

The inventory MUST be canonical, sorted by unique operation identity,
digest-bound, and complete for every operation a selected minimum standard
package exposes. Missing, duplicate, malformed, reordered, or altered records
MUST be rejected (`SP-OBL-003`).

Package revisions identify the standard contract that owns an operation. A
language revision does not silently rewrite that package's laws, order,
failures, or costs; a changed contract requires an explicit later package and
lifecycle decision (`SP-OBL-004`).

## Stability tiers and compatible replacement

Language rules, semantic interfaces, standard package contracts, and empirical
measurements are distinct stability tiers. Implementations MUST NOT promote a
lower tier into a higher one by observation or documentation alone
(`SP-OBL-005`).

A compatible replacement MUST preserve operation identity, laws, order,
callback multiplicity, failure behavior, stack bound, and every representation
promise, and MUST NOT strengthen accepted-input requirements (`SP-OBL-006`).

A replacement MAY improve its time or space class. It MUST NOT replace a
published bound with a worse class. A changed semantic field, stronger input
requirement, or worse bound is a breaking package-contract change subject to
C028's version rule (`SP-OBL-007`).

Changing private algorithms, allocation layout, module names, or BEAM code is
compatible when all published contracts remain satisfied (`SP-OBL-008`).

## Complexity and callback meaning

`constant`, `logarithmic`, `linear`, `n-log-n`, and `quadratic` describe
worst-case asymptotic upper bounds in the operation's declared input-size unit.
`implementation-bounded` means the operation crosses a service or arithmetic
boundary whose portable cost is instead controlled by explicit resource
limits. It is not a promise of constant time (`SP-OBL-009`).

Time and auxiliary-space classes exclude the returned value's unavoidable
storage unless the operation record says otherwise. Implementations MUST count
all validation, ordering, conversion, and callback dispatch required by the
operation (`SP-OBL-010`).

Callback categories mean no callback, at most one on a present/success value,
once for each visited input, once for each collision, or once per visited input
through the first explicit stop. A replacement MUST NOT invoke more callbacks,
change their order, or evaluate after an explicit stop (`SP-OBL-011`).

All standard collection operations at this revision have constant host-call
stack use for accepted finite inputs. Resource exhaustion remains C129's
reported outcome and MUST NOT be disguised as a weaker stack contract or a
partial success (`SP-OBL-012`).

## Representation and measurement boundary

The revision publishes no standard-value representation promise and no stable
BEAM ABI. Interface and package identity, laws, and necessary asymptotic
guarantees are observable; layout, sharing, node shapes, and allocation counts
are not (`SP-OBL-013`).

A performance observation MUST bind the exact operation, contract digest,
compiler, OTP release, operating system, architecture, ordered input sizes,
semantic work units, and elapsed nanoseconds. Its canonical digest MUST cover
the complete record (`SP-OBL-014`).

Elapsed time is empirical evidence for the recorded toolchain only. One or many
observations MUST NOT create a portable wall-clock, constant-factor, ABI, or
representation guarantee. G138 owns broader measured envelopes
(`SP-OBL-015`).

Malformed toolchain identities, unknown operations, duplicate or unordered
sizes, negative measurements, oversized sample sets, altered digests, and any
observation claiming portability MUST be rejected (`SP-OBL-016`).

## Profile and conformance

An implementation claiming P108 MUST publish the policy revision, inventory
size, public-source hold, ABI stance, wall-clock stance, and measurement
normativity stance in its conformance profile (`SP-OBL-017`).

Conformance evidence MUST cover canonical inventory validation; identical and
improved replacements; changed laws, order, callbacks, failures, requirements,
stack or representation promises; time and space regressions; empty, large,
and worst-shaped inputs; observation binding and tamper refusal; lifecycle
selection; trust classification; and the absence of inferred constant-time or
ABI promises (`SP-OBL-018`).

## Rationale and evidence (non-normative)

The [implementation journal](../../50-journal/2026-09-10-standard-stability-and-performance.md)
records the planned forks, eighteen four-way implementation decisions, and
compiler verification. The policy deliberately exposes the contracts clients
need while leaving implementation strategy free and G138's empirical envelope
as a separate deliverable.

