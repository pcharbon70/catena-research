---
title: "How Should Catena Define API and ABI Compatibility?"
kind: inquiry
created: "2026-08-24"
status: resolved
tags:
  - catena
  - compatibility
  - api
  - abi
  - language-design
aliases:
  - "G028 API and ABI compatibility inquiry"
---

# How Should Catena Define API and ABI Compatibility?

## Purpose

G027's journal named G028 as Section 3's last item: "Define source,
type, behavior, and BEAM-level compatibility, including what changes
require a major version." Six shipped slices left deferred promises
here — C022/C025 re-owned re-export facades to "the G028 era," C023
excluded stable layout/ABI with G028 as owner, C024 required joint
digests be treated as compatibility boundaries, C025 left
version-increment meanings and version-skew, C026 left prelude-bump
meanings, and C027 left entry-set changes. This inquiry resolves what
compatibility Catena promises, for which layers, at which version
meanings.

## Operational definitions

- **Source compatibility** — whether a source file that checked under
  revision *A* still checks under revision *B* without edits.
- **Type/interface compatibility** — whether a consumer compiled
  against a producer's decoded semantic interface still validates
  against the producer's later interface.
- **Behavior compatibility** — whether a recompiled program computes
  the same values and traps.
- **BEAM ABI compatibility** — whether previously compiled binaries
  remain loadable and callable across producer changes.
- **Breaking change** — a producer or language change that invalidates
  a consumer or source file that previously checked, per the matrix.

## Hypotheses

1. Detailed rules for source and type/interface compatibility, with
   principled declared absence for behavior (the deterministic kernel
   is the behavior contract) and BEAM ABI (representation is not a
   surface, per C023), deliver the checklist's letter truthfully.
   *(Recommended: the interface is the only cross-package contract the
   corpus actually verifies, and C023 already excluded stable
   representation.)*
2. SemVer major = breaking at 1.0+, the already-fixed Cargo 0.x rule
   (minor signals breaking) below 1.0, and edition bumps as the
   language-level equivalent through C008 lifecycle records — no new
   versioning scheme. *(Recommended: C025 fixed the operator side; this
   fixes the meaning side.)*
3. A strict interface diff matrix — removals, renames, signature
   changes, and effect-row widening breaking; additions minor;
   representation never breaking alone — is decidable from decoded
   interfaces alone. *(Recommended: digest-verified interfaces exist
   precisely to catch shape drift.)*
4. Re-export facades close as a formal exclusion: forwarding
   definitions are already expressible; silent facades contradict C002
   transparency and C021's `NSP004` model. *(Recommended: no ecosystem
   evidence demands identity-preserving facades yet.)*
5. An executable deliverable — `diff/2` classification plus claim
   validation against the claimed SemVer bump — is achievable without
   source parsing or behavior claims.

## Paths explored

- **Full four-layer rules including a behavioral contract** — rejected:
  behavior cannot be checked across producers, and "the kernel is the
  contract" is stronger than an unenforceable promise.
- **Minimal BEAM ABI contract now** — rejected: the runtime era
  (G084+) has not designed process/calling boundaries; C023's exclusion
  was deliberate.
- **Catena-specific versioning scheme** — rejected: contradicts C025's
  shipped SemVer grammar and the Hex transport profile.
- **Removals-only breaking** — rejected: matches nothing in the corpus.
- **Minimal manifest facade mechanism** — rejected: cross-package
  export wiring with no consumer demand.
- **Over-strict matrix (instance additions breaking)** — rejected:
  penalizes safe evolution; additions are what minors are for.

## Findings

All five hypotheses held; the developer chose the recommended option on
every fork (seven of seven, no overrides). The [OTP compatibility
strategy](../30-sources/erlang-otp-compatibility-and-upgrading.md)
— fetched during this slice — independently validates the layered
stance: Erlang itself refuses a uniform promise, tiers its surfaces
(distribution, binary, API, tooling), expressly declines
bug-compatibility, and deprecates before removing. Catena's
declared-absence layers are the same discipline with 0.x honesty.

One framing decision emerged during planning: the checklist says
"BEAM-level compatibility" — the truthful 0.x answer names the
companion-binary stance (deterministic outputs, never a surface) and
the target-runtime fact (OTP's own two-release-forward, never-backward
rule) as context rather than promising either.

## Outcome

Resolved as C028 at revision `0.1.24`: the contract lives in the
[API and ABI Compatibility Specification](../60-specification/api-and-abi-compatibility/README.md),
the reasoning in
[Catena API and ABI Compatibility](../20-notes/catena-api-and-abi-compatibility.md),
and the forks in the [design decision
register](../20-notes/design-decision-register.md). Migration engines
(G116/P125), registry retirement and yanks (G130), hot upgrade
(G092), representation/calling-convention/foreign-term contracts
(P093/G094/G095), and tooling defaults (G121) remain open with their
owners.
