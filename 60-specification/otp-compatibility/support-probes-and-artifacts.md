---
title: "OTP Support, Probes and Artifact Compatibility"
kind: specification
created: "2026-09-08"
status: normative
spec_version: "0.1.57"
tags:
  - specification
  - compatibility
  - beam-vm
aliases: []
---

# OTP Support, Probes and Artifact Compatibility

## Status and authority

This chapter completes C099 at `0.1.57` under the
[authority policy](../../SPECIFICATION-AUTHORITY.md),
[conformance vocabulary](../../CONFORMANCE-VOCABULARY.md) and
[implementation-limit policy](../../IMPLEMENTATION-LIMITS.md).
It defines the tested implementation/toolchain policy and applies to newly
produced artifacts and Catena loading paths. It introduces no executable
frontend, source spelling, interface format or signed-document format
(`OC-OBL-001`).

Language revisions, compiler-package releases, runtime support rows and binary
build identities are separate axes. Historical language selections remain
available through their retained frontends. Historical binaries without the
new provenance require rebuilding; preserved evidence is not silently retagged.
The [API/ABI policy](../api-and-abi-compatibility/README.md) continues to separate
source compatibility from binary reuse.

## Tested support matrix

A support claim names a complete successful matrix row. The initial matrix has
exactly one active row (`OC-OBL-002`):

| Field | Supported value |
| --- | --- |
| OTP release | 29.0.4 |
| ERTS | 17.0.4 |
| Elixir | 1.20.2 |
| Compiler application | 10.0.3 |
| Standard library application | 8.0.3 |
| Kernel application | 11.0.3 |
| System architecture | x86_64-pc-linux-gnu |
| OS family/type | unix/linux |
| Word size | 8 bytes |
| Emulator flavor | jit |
| Build mode | opt |

The oldest and newest supported patch are both 29.0.4. Another OTP 29 patch,
platform, VM flavor or compiler version is not supported merely because its
major version matches or OTP can load the binary. The bootstrap target remains
OTP 29 Erlang Abstract Format through the sole production compiler boundary.

This row records version and platform identity, not cryptographic attestation
of an installation. Hostnames, installation paths and scheduler counts are not
fingerprint fields. Deployment capacity and scheduler configuration retain their
separate policy owners.

## Observations and required facilities

Before production compilation, the implementation observes the exact release
file, runtime version, Elixir version, application versions and platform fields.
An unavailable release field does not default to a supported version.
A fingerprint outside the matrix returns `OTP001` before output production
(`OC-OBL-003`).

The implementation also checks that `compile:noenv_forms/2` is exported, that
process aliases can carry a private local reply and be disposed, that monotonic
nanosecond time is available, and that a spawned monitored process can terminate
with its matching completion notification. Every required facility must pass;
a missing facility returns `OTP002`. Version agreement alone is insufficient.
Private probe messages are consumed exactly and do not reach application
receives. A waiting probe does not establish a wall-clock fairness promise
(`OC-OBL-003`).

The language and conformance discovery documents report supported rows,
observed fields, individual probe results, whether the observed host is supported,
and the canonical fingerprint digest. Equal observations produce equal reports.
Reports do not add untested rows or silently select fallback implementations
(`OC-OBL-004`).

## Artifact provenance and loading

Every newly produced BEAM artifact records its full toolchain fingerprint and
a SHA-256 digest of canonical JSON for that fingerprint in compile metadata.
Those fields accompany, rather than replace, language selection and frontend
metadata. Compilation remains deterministic for the same source, options and
supported toolchain (`OC-OBL-005`).

Catena's loader first reads the artifact's declared module and provenance,
checks the current host against the support matrix, requires exact fingerprint
agreement, and verifies the digest. Missing, malformed or mismatched provenance
returns `OTP003` with a rebuild requirement. A mismatched module cannot be loaded
through a caller-supplied different identity. Compatibility failure occurs before
code loading (`OC-OBL-006`).

Entry launch and the supervised-artifact adapter use this loading boundary.
They return its diagnostic rather than raising an accidental pattern-match
exception. Direct raw OTP code loading is not a Catena compatibility claim.
Fingerprint agreement does not authenticate an arbitrary BEAM file or prove it
came from checked source; existing verified-artifact and trust boundaries remain
necessary where their contracts require them.

An untagged historical artifact is rebuilt from its retained source on a supported
row. Signed evidence tied to the old artifact remains historical; new binary
hashes require new corresponding evidence. A new support row does not silently
make an old row's artifacts reusable. Cross-row reuse requires an explicit later
compatibility rule and evidence, or a rebuild on the selected row.

## Expansion and retirement

Adding a supported row requires a reviewed matrix change with exact host
observations, all facility probes, the full semantic/conformance test matrix,
deterministic artifact production and load/execute evidence on that row.
The evidence must identify the compiler commit, runtime fields and results.
Failures, unavailable hosts or a vendor's general forward-compatibility statement
cannot substitute for an actual successful run (`OC-OBL-007`).

For every support set, its oldest and newest supported patch need this evidence;
a singleton row satisfies both endpoints without implying an interval between
untested releases. Artifact transfer to an independently started compatible VM
must execute successfully; mismatched-host rejection needs explicit negative
witnesses. Simulated mismatch fixtures are labeled as such and do not count as
running another platform. General physical-host/distribution guarantees remain
outside this local artifact policy.

An ordinary retirement announcement identifies the affected row, replacement,
reason, migration instructions, earliest removal date and earliest compiler
release that can remove it. Removal waits at least 30 calendar days and at least
one subsequently published compiler-package release after the announcement;
both conditions apply. The initial row has no scheduled retirement. Language
source retention is not revoked merely by retiring a runtime row
(`OC-OBL-008`).

An urgent security or correctness withdrawal can take effect immediately only
through an explicit reviewed withdrawal record identifying the defect,
unsupported behavior and rebuild/replacement path. It is not a silent fallback
or an unannounced reinterpretation of historical evidence. Adding a newer patch
never automatically retires an older active row. Hot code upgrades and live state
migration remain separately specified facilities.

## Variability and limits

All new behavior is fixed by this chapter; no new variability is introduced.
The [register](README.md#variability-register) records inherited compiler,
artifact, process and allocation limits. Resource exhaustion is not permission
to publish unsupported output or change language semantics. No new portable
scheduler, memory or process-count floor is introduced. The measured matrix is
an explicit supported target set.

## Rationale and evidence (non-normative)

The [CP-099 plan](../../20-notes/language-completion-plan-delivery.md#item-099-otp-compatibility-policy)
selects evidence-gated support and artifact provenance. The
[OTP compatibility source](../../30-sources/erlang-otp-compatibility-and-upgrading.md)
distinguishes host compatibility surfaces and exceptions. Catena's prototype
policy is intentionally narrower than OTP's vendor compatibility strategy.
The [implementation journal](../../50-journal/2026-09-08-otp-compatibility.md)
records measured fields, alternatives, actual separate-VM execution and the
limits of simulated negative-host evidence.
