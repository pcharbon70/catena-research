---
title: "Evidence Gates and Release Claims"
kind: specification
created: "2026-09-10"
status: normative
spec_version: "0.1.90"
tags: [specification, conformance, release, evidence]
aliases: []
---

# Evidence Gates and Release Claims

## Status and authority

G139 defines revision `0.1.90` under [authority](../../SPECIFICATION-AUTHORITY.md),
[conformance vocabulary](../../CONFORMANCE-VOCABULARY.md), and
[implementation limits](../../IMPLEMENTATION-LIMITS.md). It executes the
[G139 plan](../../20-notes/language-completion-plan-delivery.md#item-139-release-readiness-definition)
over the normative corpus, conformance traceability, supported-host profile,
retained compatibility and performance evidence, and the formal-proof ledger.
It adds no public vocabulary or grammar and does not declare the Catena
language complete (`RR-OBL-001`).

## Release classes and claims

A release claim MUST name exactly one class: `experimental`, `complete`, or
`stable`. The class names form an increasing evidence order, but a tool MUST
NOT infer, publish, or apply an upgrade merely because a stronger class appears
eligible (`RR-OBL-002`).

An experimental claim MAY retain disclosed open specification, tooling,
usability, or proof items. It MUST identify those items and limitations and
MUST claim only the bounded experimental evidence named by its manifest. It
MUST NOT imply complete public source adoption, an integrated safety theorem,
or a stability promise (`RR-OBL-003`).

> **Variability — experimental issuance:** A conforming implementation may
> decline to issue an experimental release even when its manifest passes.

A complete claim MUST have no open applicable completion gate. Its normative
chapters, P107 vocabulary, P109 grammar, source tooling, compatibility,
performance, usability evidence, supported platforms, and integrated formal
proof MUST all satisfy this chapter. A stable claim MUST satisfy the complete
class and additionally publish a positive compatibility window and a
digest-bound support policy (`RR-OBL-004`).

## Canonical release manifest

Every assessed release MUST supply one canonical, digest-bound manifest. It
MUST identify format and manifest version, exact language revision, requested
class, normative chapters, obligation counts, platforms, evidence domains,
open items, limitations, proof records, and contradiction dispositions. List
identities MUST be unique and canonically ordered (`RR-OBL-005`).

The obligation counts MUST distinguish total, traced, partial, and untraced
obligations, and their arithmetic MUST agree. Complete and stable claims MUST
have a positive total with every obligation traced and none partial or
untraced. Experimental manifests MAY retain nonzero partial or untraced counts
when their limitation and open-item ledgers disclose the scope (`RR-OBL-006`).

Every limitation MUST have a stable identifier, status, and disposition. An
empty limitation ledger is invalid because even a fully supported release has
finite platform, resource, and proof scope. Removing a limitation requires a
new evidence identity and reviewed manifest (`RR-OBL-007`).

Manifest verification MUST recompute the canonical payload digest before
assessing any claim. An altered field, duplicate identity, malformed count,
unknown class, or incomplete required inventory MUST produce invalidity rather
than a readiness result (`RR-OBL-008`).

## Evidence and platform gates

The evidence inventory MUST contain separate compatibility, performance,
source-tooling, and usability records, each with an exact digest and `pass` or
`blocked` status. Complete and stable claims require `pass` for all four.
Experimental claims may retain `blocked` records with corresponding disclosed
open items (`RR-OBL-009`).

Every platform record MUST contain its complete tested fingerprint, the exact
fingerprint digest, and supported status. A host outside the published support
matrix or a mismatched digest MUST block every release class; host similarity
or a passing run on another row MUST NOT substitute for that witness
(`RR-OBL-010`).

The completion-gate inventory MUST include P096, P107, P109, P117, G118, P119,
G120, G123, P125, and G137. A complete or stable assessment MUST block while
any inventory member remains in `open_items`. A later normative revision may
change this inventory only with an explicit migration and corresponding
readiness-profile update (`RR-OBL-011`).

> **Variability — stronger local policy:** An implementation may require more
> evidence before issuing a release, provided it reports the additional gate
> and does not weaken any requirement here.

## Proof ledger and claim boundary

Every release manifest MUST contain a nonempty proof ledger. A proof record
MUST identify checker, pinned checker/container digest, exact source digest,
scope, status, and theorem inventory. The readiness verifier MUST accept a
proof claim only when the complete record equals an entry in its separately
reviewed proof registry; a manifest cannot admit its own proof (`RR-OBL-012`).

Revision `0.1.90` admits one Rocq 9.2 workbench record with source digest
`107a74da9b8e8a963a282f23bfb485f240259d00ef493b66e4d6aad098211024`
and container digest
`sha256:33926fb3757b2b560c3844157bd64173a26b6d338a256be1ae5eec8df2019025`.
Its exact scope is `bounded-core-not-integrated-catena`; it proves substitution,
context compatibility, progress, preservation, component interaction, and
bounded core composition. This evidence MUST NOT be reported as the integrated
Catena progress-and-preservation theorem (`RR-OBL-013`).

No integrated Catena theorem is admitted in revision `0.1.90`. Consequently,
the `complete` and `stable` classes remain blocked even if a manifest
self-asserts an `integrated-catena` record. A future proof-registry revision
MUST identify and independently check the actual admitted language relations
before it can remove this blocker (`RR-OBL-014`).

## Contradiction audit and publication

Every manifest MUST carry exact dispositions for the
`package-identifier-underscore` and `abstraction-invariant-boundary` audits.
The first resolves the former `json_tools` example in favor of the already
normative hyphen-only package grammar. The second distinguishes static result
typing from runtime validation: failure is a typed result before an abstract
value exists, rather than invalid input being rejected statically. Any missing
or unresolved disposition MUST block readiness (`RR-OBL-015`).

An implementation claiming G139 MUST publish the class inventory, gate list,
evidence domains, contradiction inventory, platform policy, proof policy,
bounded proof identity, integrated-proof status, automatic-upgrade status, and
publication behavior. Conformance MUST exercise a passing experimental
manifest with disclosed gaps; complete-class blocking; malformed arithmetic;
digest tampering; forged proof, unsupported host, unresolved contradiction,
and self-admitted integrated-proof cases; lifecycle selection; production
build; trust inventory; and the complete compiler suite. Assessment MUST
report that it performed no publication (`RR-OBL-016`).

## Rationale and evidence (non-normative)

The [implementation journal](../../50-journal/2026-09-10-release-readiness.md)
records the five planned forks, sixteen implementation forks, compiler PR 175,
and the exact limits of the proof. This chapter completes the readiness
definition while preserving the distinction between a defined gate and a
language that has passed it.
