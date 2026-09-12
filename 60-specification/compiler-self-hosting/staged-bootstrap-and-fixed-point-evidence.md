---
title: "Staged Bootstrap and Fixed-Point Evidence"
kind: specification
created: "2026-09-12"
status: normative
spec_version: "0.1.98"
tags: [specification, compiler, bootstrap]
aliases: []
---

# Staged Bootstrap and Fixed-Point Evidence

## Status and authority

G141 defines its late-0.x self-hosting milestone and preflight at revision
`0.1.98` under [authority](../../SPECIFICATION-AUTHORITY.md),
[conformance vocabulary](../../CONFORMANCE-VOCABULARY.md), and
[implementation limits](../../IMPLEMENTATION-LIMITS.md). It executes the
[G141 plan](../../20-notes/language-completion-plan-delivery.md#item-141-compiler-self-hosting)
without inventing Catena compiler source before P109. The preflight, an Elixir
wrapper, or a claimed fixed point does not make the compiler self-hosted. G141
remains partial (`SH-OBL-001`).

## Meaning and target

Self-hosting MUST mean that actual parser, checker, verifier, and backend
compiler passes are implemented in Catena and can rebuild the compiler. Calling
an Elixir compiler pass through a Catena wrapper MUST NOT count as a Catena
implementation of that pass (`SH-OBL-002`).

The compiler MUST continue to target only BEAM through the OTP 29 Erlang
Abstract Format boundary. Self-hosting MUST NOT change the target VM, introduce
a direct BEAM assembler, or widen the runtime target (`SH-OBL-003`).

The Elixir bootstrap MUST remain a pinned, audited, reproducible stage-zero
recovery root. Its exact source, toolchain, dependencies, host assumptions, and
artifact identity MUST be retained with the bootstrap evidence. First success
MUST NOT delete or replace the recovery root (`SH-OBL-004`).

## Required language subset and port order

Before compiler source is admitted, ordinary Catena programs MUST demonstrate
parser and module ADTs, pure transformations, file and process capabilities,
structured diagnostics, packages, and typed OTP interoperability. Public
compiler source MUST remain held while P109 is incomplete (`SH-OBL-005`).

Porting MUST proceed through canonical JSON, strongly connected components,
row and unification operations, parser, checker, verifier, and backend in that
order. Each admitted group MUST expose a differential interface against the
retained implementation before a dependent group is admitted (`SH-OBL-006`).

Self-hosting work MUST preserve C140's excluded-feature inventory. A compiler
pass MUST NOT obtain admission by using impredicativity, unrestricted
inference, existential escape, or another excluded form (`SH-OBL-007`).

## Stages and comparisons

Stage zero MUST compile the exact Catena compiler source into stage one. Stage
one MUST compile the same source and declared inputs into stage two. Each stage
record MUST bind builder artifact, compiler source, complete declared inputs,
output artifact, target, and toolchain by exact digest (`SH-OBL-008`).

When reproducible bytes are required by P128's declared envelope, stage one and
stage two MUST be byte-identical. When byte identity is explicitly inapplicable,
the comparison MUST name a separately versioned semantic oracle, bind both
artifacts, and exercise equivalent compiler observations. A filename, timestamp,
or successful invocation is not a stage comparison (`SH-OBL-009`).

A fixed point establishes repeatability only for the compared inputs, builders,
target, and observations. It MUST NOT be reported as proof that stage zero was
free of a malicious bootstrap or that the compiler is semantically correct
(`SH-OBL-010`).

An unexplained stage drift MUST block the milestone. A further comparison stage
MUST be produced when the selected oracle cannot distinguish one-time bootstrap
drift from a stable result (`SH-OBL-011`).

## Cross-implementation evidence

The retained and Catena implementations MUST both run the complete conformance,
differential, historical compatibility, packaging, and representative
application corpus suites. Every suite result MUST bind implementation,
compiler source, test corpus, language revision, target, and result artifact.
A passing subset MUST NOT stand for an omitted suite (`SH-OBL-012`).

Clean offline builds MUST reproduce every required bootstrap stage from retained
declared inputs. Altered bootstrap, compiler-source, dependency, stage, test, or
target identities MUST be rejected before comparison or publication
(`SH-OBL-013`).

Residual host services MUST be limited to explicitly inventoried cryptography,
filesystem, process, and OTP Abstract Format facilities. Any retained Elixir
compiler-pass dependency MUST keep the affected pass and the G141 milestone
blocked (`SH-OBL-014`).

## Recovery and distribution

The toolchain MUST perform a real interrupted-upgrade and rollback drill. The
drill MUST demonstrate that an incomplete stage cannot replace the active
compiler and that the pinned stage-zero path can rebuild a usable verified
toolchain from retained inputs (`SH-OBL-015`).

A distributed self-hosting bundle MUST contain or immutably acquire stage zero,
declared bootstrap inputs, Catena compiler source, stage artifacts, comparison
evidence, suite evidence, residual-service inventory, and rollback instructions.
Acquisition MUST obey P130's signed immutable registry rules and MUST NOT fetch
an undeclared bootstrap (`SH-OBL-016`).

## Preflight, limits, and conformance

The preflight MUST publish the retained stage-zero role, target, P109 and source
holds, absent stages, port order, suite families, evidence families, residual
services, comparison rule, wrapper exclusion, fixed-point limitation, rollback
requirement, and every blocker. Its canonical digest MUST identify the exact
preflight package (`SH-OBL-017`).

This milestone has zero variability dispositions. An implementation MUST NOT
weaken a blocker because of unavailable source, resources, host services, or
evidence. Exhaustion leaves the milestone blocked. The preflight fixes seven
port groups, five suite families, six evidence families, four residual-service
classes, and eight blockers (`SH-OBL-018`).

An implementation claiming revision `0.1.98` MUST exercise valid preflight
assessment, wrapper and fake-stage refusal, target and residual-service drift,
port-order truncation, premature fixed-point and rollback claims, lifecycle
selection, production compilation, trust-inventory verification, and its
complete regression suite. Completing G141 additionally requires every stage,
comparison, suite, reproducibility, residual-service, distribution, and rollback
obligation above (`SH-OBL-019`).

## Rationale and evidence (non-normative)

The [implementation journal](../../50-journal/2026-09-12-self-hosting.md)
records twenty-two four-way implementation decisions and compiler
[PR 195](https://github.com/pcharbon70/catena/pull/195). The executable preflight
prevents absence from being mistaken for completion and preserves a precise path
to a real Catena-authored compiler after public source adoption.
