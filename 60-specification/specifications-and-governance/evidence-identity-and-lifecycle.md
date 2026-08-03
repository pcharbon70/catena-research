---
title: "Evidence, Identity, Trust, and Lifecycle"
kind: specification
created: "2026-08-03"
status: normative
spec_version: "0.6"
tags:
  - cryptography
  - governance
  - provenance
  - specification
aliases:
  - "Catena 0.6 trust and transition protocol"
---

# Evidence, Identity, Trust, and Lifecycle

## Honest evidence records

Every evidence record has a unique identifier, kind, exact claim identifier,
result, and the fields required by its producer class. Compiler-derived
conformance and example evidence records the claim semantic digest, resolved
subject, complete artifact-digest set, and compiler identity. An external
attestation signs a payload containing those bindings plus its producer role,
tool identity, and logical validity window. An assumption records the claim
digest, subject, reason, and validity window; the exact assumption record is
then bound into a separately signed approval. These kinds are not
substitutable unless a policy explicitly names the accepted kind.

Revoked, out-of-window, malformed, duplicate, wrong-subject, wrong-artifact,
wrong-claim, or wrong-tool evidence is invalid. Reproducibility fields describe
how to repeat an observation but do not strengthen the result.

## Canonical signed values

Signed protocol values use the JSON Canonicalization Scheme in RFC 8785 with a
stricter Catena profile:

- object names are unique and sorted by unsigned UTF-16 code units;
- strings contain valid Unicode scalar values and are preserved without
  normalization;
- only integers in `-9007199254740991..9007199254740991` are admitted;
- floats, negative zero, NaN, infinities, duplicate names, invalid Unicode,
  and noncanonical supplied signed payloads are rejected; and
- no insignificant whitespace is present in canonical bytes.

Digests are lowercase hexadecimal SHA-256. Public keys and signatures are
lowercase hexadecimal Ed25519 values implementing RFC 8032. A signature covers
one domain-separated payload:

```text
"catena:<payload-kind>:0.6\n" || JCS(payload)
```

`payload-kind` is one of `root`, `delegation`, `evidence`, `approval`,
`transition`, or `manifest`; a signature from one domain MUST NOT verify in
another.

The canonicalization basis is
[RFC 8785](../../30-sources/rundgren-et-al-2020-json-canonicalization-scheme.md),
and the signature basis is
[RFC 8032](../../30-sources/josefsson-liusvaara-2017-eddsa.md).

## Offline trust root

`catena-trust-root` version `0.6` contains:

- a package namespace and positive logical sequence;
- a map of principal IDs to Ed25519 public keys;
- normal and recovery role memberships with positive thresholds;
- scoped delegations with action, subject, profile, and sequence bounds;
- revoked principal, delegation, and evidence identifiers; and
- a hash-chained root history.

Private keys are external to the compiler. The compiler emits canonical
payload bytes and their digest, and verifies supplied signatures. It MUST NOT
generate, import, escrow, or write signing private keys.

## Rotation, revocation, and recovery

A normal root change increments the logical sequence by exactly one and is
signed by the old normal threshold and the new normal threshold. This preserves
a chain of continuity and prevents one compromised old or newly introduced key
from unilaterally rewriting authority.

The initial root predeclares a separate recovery role and threshold. A
recovery change increments the sequence by exactly one, cites the prior root
digest, uses the recovery domain and threshold, and may replace compromised
normal authority. Recovery authority cannot be introduced by the root it is
being used to recover.

Revocation takes effect at its recorded logical sequence. Later signatures by
the revoked identity do not count. Version 0.6 uses no wall-clock truth:
freshness and validity are inclusive logical sequence windows.

These continuity and threshold rules adapt the established root-rotation
pattern described by the
[Update Framework specification](../../30-sources/the-update-framework-specification.md)
to an offline language-governance setting; Catena does not adopt that system's
repository or transport protocol.

## Lifecycle state machine

The complete 0.6 transition relation is:

```text
Draft      -> Proposed
Proposed   -> Accepted | Rejected | Withdrawn
Accepted   -> Active | Withdrawn
Active     -> Deprecated
Deprecated -> Superseded
```

`Rejected`, `Withdrawn`, and `Superseded` are terminal. No implicit reset,
backward edge, or state edit exists.

## Immutable transition history

Each transition records positive sequence, prior transition digest, old and
new state, action, subject, proposal digest, claim and artifact digests,
evidence set, active policy digest, approvals, and decision explanation. Its
digest covers every field except the digest and signatures themselves.

Every transition is signed by the active normal-role threshold. For
`activate`, the final transition MUST be the contiguous `Accepted -> Active`
edge at the current logical sequence, and every decision, policy, evidence,
approval, claim, subject, and artifact binding MUST exactly reproduce the
compiler's decision. A merely well-signed but differently bound transition is
denied.

Replay begins at `Draft`. Sequences MUST be contiguous, each prior digest MUST
match, and every edge MUST appear in the state machine. Reordering, deletion,
insertion, replay against another artifact, or mutation of evidence, policy, or
approvals invalidates the chain.

A historical transition is verified against the most recent trust-root state
whose sequence is not later than that transition. Rotation or revocation does
not retroactively invalidate an earlier authorized event, and authority added
later cannot validate an earlier event.
