---
title: "Structured Explanations and Repairs"
kind: specification
created: "2026-09-10"
status: normative
spec_version: "0.1.91"
tags: [specification, diagnostics, tooling, source-location]
aliases: []
---

# Structured Explanations and Repairs

## Status and authority

P117 defines its semantic diagnostic contract at revision `0.1.91` under
[authority](../../SPECIFICATION-AUTHORITY.md), [conformance vocabulary](../../CONFORMANCE-VOCABULARY.md),
and [implementation limits](../../IMPLEMENTATION-LIMITS.md). It executes the
[P117 plan](../../20-notes/language-completion-plan-delivery.md#item-117-diagnostic-contract)
over existing diagnostic families and P100 origins. Public parse-recovery
coverage remains held for P109, so P117 remains partial (`DX-OBL-001`).

## Identity and locations

A diagnostic MUST retain its stable family identifier, severity, message,
machine path, primary half-open span, deterministic details, and structured
fixes. Related locations MUST be an ordered list of labeled half-open spans in
the same original UTF-8 coordinate model and MUST contain at most eight entries
(`DX-OBL-002`).

Every source-bound span MUST align to Unicode scalar boundaries and fit the
identified preimage. Split scalars, reversed ranges, forged related locations,
and stale preimages MUST be rejected (`DX-OBL-003`).

## Explanations and provenance

Inferred and expected types MUST be normalized to source-level structural
forms. A presentation MUST include its complete digest and truncation status;
visible text MUST be bounded to 512 bytes. Raw solver identities MUST NOT be
the sole user explanation (`DX-OBL-004`).

Constraint provenance MUST be a unique ordered list of at most 32 steps. Each
step MUST identify the causal relation and applicable machine path. Type
mismatches MUST identify inferred and expected presentations plus the equality
constraint that failed (`DX-OBL-005`).

Non-exhaustive matches MUST retain a concrete missing-pattern witness and the
normalized scrutinee type. Redundant clauses MUST distinguish an
unsatisfiable guard, a guard covered by prior clauses, and a structurally
covered pattern (`DX-OBL-006`).

Generated-code attribution MUST identify the generated node, verified source
span, and SHA-256 digest of the node identity, one zero byte, and the exact
source bytes in that span. Missing or forged generation
evidence MUST NOT be presented as handwritten source (`DX-OBL-007`).

> **Variability — additional detail:** An implementation may expose a bounded
> technical view after the required source-level explanation, provided it does
> not change diagnostic identity or imply a different cause.

## Repair edits

> **Normative unspecified presentation.**

The `unspecified` applicability class is bounded unspecified presentation. Its
serialized label is fixed; only consumer display wording can vary, and it
carries no machine-safety claim. Every offered edit MUST state
`machine_applicable`, `maybe_incorrect`, or `unspecified`, MUST bind the complete
source preimage digest, MUST use UTF-8-aligned half-open byte endpoints, and
MUST carry valid UTF-8 replacement text. Edits in one diagnostic MUST be
sorted and nonoverlapping (`DX-OBL-008`).

A compiler MUST report edits without applying them. A stale digest,
overlapping range, split scalar, invalid replacement, or unknown applicability
MUST invalidate the repair contract and MUST leave source unchanged.
Transactional application remains P125 (`DX-OBL-009`).

> **Variability — repair availability:** A conforming producer may omit a
> repair when it cannot justify one; omission is preferable to an ungrounded
> machine-applicable edit.

## Reports, bounds, and conformance

Machine reports MUST preserve related locations, explanation fields, and
causal provenance through secret redaction and serialization. Empty optional
lists MUST remain explicit, and old diagnostic consumers MAY ignore added
fields without changing the diagnostic's semantic identity (`DX-OBL-010`).

The conformance profile MUST publish revision, location, cause, type-text,
applicability, coordinate, generated-origin, and parse-coverage policies.
Exhausting a presentation or provenance bound MUST truncate with an exact
digest or reject the extra record; it MUST NOT silently emit unbounded output
(`DX-OBL-011`).

An implementation claiming the P117 semantic slice MUST exercise Unicode
related spans, normalized short and truncated long types, causal provenance,
missing-pattern witnesses, guard-redundancy classifications, generated-origin
refusal, stale and split-scalar edits, overlap and cardinality bounds,
lifecycle selection, production build, trust inventory, and the complete
suite (`DX-OBL-012`).

P117 MUST remain partial until P109 supplies real public parse and recovery
diagnostics over incomplete programs, with the same identity, location,
provenance, and bound rules. Retained semantic inputs establish no claim about
that held grammar (`DX-OBL-013`).

## Rationale and evidence (non-normative)

The [implementation journal](../../50-journal/2026-09-10-diagnostic-contract.md)
records nineteen four-way decisions and compiler PRs 177–179. The contract gives
all existing semantic frontends one consumer-stable explanation shape while
keeping the missing public-source evidence visible.
