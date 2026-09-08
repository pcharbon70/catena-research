---
title: "OTP Compatibility Implementation"
kind: journal
created: "2026-09-08"
tags:
  - language-design
  - compatibility
  - beam-vm
aliases: []
---

# OTP Compatibility Implementation

## Starting point and evidence boundary

C089 merged through [compiler PR 138](https://github.com/pcharbon70/catena/pull/138)
and [research PR 88](https://github.com/pcharbon70/catena-research/pull/88).
Compiler `rewrite` synchronized at `2deac985fda3f782e1585cd1c2e42f63d14e1785`;
research `main` synchronized at `ab7aa4dccd7d9d2653ecce15539df3ce856a6e83`.
Both feature branches were deleted after synchronization. Work proceeds on
`codex/otp-compatibility` without any scheduled continuation.

The [CP-099 plan](../20-notes/language-completion-plan-delivery.md#item-099-otp-compatibility-policy)
selects a tested matrix, feature checks and exact provenance, and rebuilds when
support changes. The existing [OTP compatibility source](../30-sources/erlang-otp-compatibility-and-upgrading.md)
was rechecked against the official page on 2026-09-08; that moving page identifies
OTP 29.0.6. Its existence is not Catena evidence for that version. Local execution
uses the pinned 29.0.4 installation.

## Measured host

The OTP release file reports `29.0.4`; ERTS reports `17.0.4`; Elixir reports
`1.20.2`. Application versions are compiler `10.0.3`, stdlib `8.0.3`, and kernel
`11.0.3`. The platform is `x86_64-pc-linux-gnu`, OS `unix/linux`, eight-byte words,
JIT emulator and optimized build. Installation paths, machine identity and
scheduler count are not artifact identity fields.

## Implementation decisions

| Decision | Four alternatives explored | Recommended and selected |
| --- | --- | --- |
| OC-I01 | A: support only the measured exact row initially; B: claim all OTP 29 patches; C: track whichever latest page exists; D: infer support from BEAM loadability. | **A.** The oldest and newest supported patch are presently the same row; additional rows need their own full semantic and artifact evidence. |
| OC-I02 | A: combine exact version/platform fields with required facility probes; B: inspect major version only; C: compile and hope; D: silently downgrade runtime behavior. | **A.** Compiler export availability, aliases, monotonic time and monitored spawning are checked before compiler output. |
| OC-I03 | A: bind full fingerprint and digest into every produced artifact and verify on Catena loading paths; B: record only the source revision; C: trust a filename; D: add a hash without checking it. | **A.** Source retention is separate from binary reuse. Untagged historical binaries require a rebuild. |
| OC-I04 | A: centralize entry and supervision loading through the checked OTP boundary; B: validate only CLI files; C: bypass checks for library calls; D: catch rejection as a generic match exception. | **A.** A regression exposed entry launch matching blindly on successful loading; it now returns the explicit diagnostic. |
| OC-I05 | A: active local facility probes with exact private-message cleanup; B: infer aliases from release numbers; C: assume a callback exists because a module loaded; D: use external network availability as a runtime probe. | **A.** Repeated probes leave no messages in the caller mailbox. Runtime facilities are checked independently from source parsing. |
| OC-I06 | A: execute a produced artifact in a separate VM and test mismatched profiles with explicit fixtures; B: call this physical cross-host coverage; C: claim uninstalled runtime versions passed; D: omit loader tests. | **A.** Separate-VM evidence is real execution on the one measured host. Other rows remain unsupported; mismatch fixtures are policy evidence, not executions on those hosts. |
| OC-I07 | A: pin VM flavor/build as well as architecture and versions; B: assume interpreter/JIT equivalence establishes support; C: include private hostnames and paths; D: hash scheduler count into artifacts. | **A.** This keeps the claimed row honest while deployment capacity stays a separate axis. |

## Current implementation

The compiler performs host validation before its sole production compilation
boundary. Discovery documents report the tested row, observed fingerprint and
facility results. Artifacts carry provenance; entry and supervised-artifact
loading verify it before code loading. A retained host-only exception fixture
was moved through the production compiler so its trap test continues to test
entry exception handling rather than bypassing provenance.

Normative publication, final full regression and immutable publication evidence
remain pending at this workbench stage.

## Policy decisions and evidence limits

| Decision | Four alternatives explored | Recommended and selected |
| --- | --- | --- |
| OC-I08 | A: ordinary retirement after both 30 days and one subsequently published compiler release, with explicit urgent withdrawal; B: immediate silent retirement; C: indefinite support regardless of defects; D: retire every old row whenever a newer row appears. | **A.** The policy creates an actionable window without conflating runtime retirement with retained language source. No current row is scheduled for retirement. |
| OC-I09 | A: require rebuilding untagged binaries and preserve historical signed evidence; B: forge provenance on old binaries; C: accept absent provenance forever; D: rewrite old source revisions. | **A.** Newly compiled outputs get truthful toolchain fields while old evidence stays historical. |
| OC-I10 | A: register 0.1.57 as a policy revision without a new executable frontend; B: widen every syntax format; C: reuse the compiler-package release number as a language revision; D: hide artifact-policy changes from the lifecycle registry. | **A.** Source, implementation release and runtime versions stay separate axes. |
| OC-I11 | A: wait for the exact monitored probe completion without a scheduler-time cutoff; B: classify a busy VM as lacking monitoring after one second; C: discard its completion message; D: skip the required runtime probe. | **A.** The probe tests a facility and makes no new scheduling bound. |

Five dedicated profile tests pass, including real artifact execution in a
separate Elixir/ERTS VM on the same measured host. The negative host/patch cases
are explicit simulated fingerprints; no second physical host or uninstalled OTP
release is claimed. The singleton matrix is both the oldest and newest supported
patch, not a range claim.

The [normative policy](../60-specification/otp-compatibility/support-probes-and-artifacts.md)
records eight obligations, expansion evidence and retirement procedure.

## Final verification and immutable implementation

Compiler commit [`69286dcb2e12254d3ce58dd7d187aeb3ab822ee5`](https://github.com/pcharbon70/catena/commit/69286dcb2e12254d3ce58dd7d187aeb3ab822ee5)
contains the completed implementation. The final `mix test` run passed
**828 tests** on the single measured row. Production compilation with warnings
as errors, escript build, formatting and whitespace checks passed. The local
transcript is `/tmp/catena-otp-profile-regression.log`.

Archive validation passed with 609 documents, 69 directories, 183 specification
chapters and 783 obligations. The checklist records **96 complete, 29 partial,
14 gaps and 2 deferred**. C099 consumes `0.1.57` without a new executable
frontend; the next unused semantic patch is `0.1.58`. The earlier pending
workbench statement is superseded by this final verification. No automation
or scheduled continuation was used.
