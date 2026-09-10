---
title: "2026-09-09 Reproducible Packages"
kind: journal
created: "2026-09-09"
tags: [specification, conformance, security]
aliases: []
---

# 2026-09-09 Reproducible Packages

## Scope

Execute [P128](../20-notes/language-completion-plan-delivery.md#item-128-reproducible-builds)
from compiler C131 merge `20ae238e6b018d3c39d300aa4a8a8f23d89502aa`.
Revision 0.1.73 is covered by the user's session-wide approval. The executable contract is [C128](../60-specification/reproducible-builds/exact-inputs-and-canonical-packages.md).

## Implementation decisions

CP-128-1..3 retain their recommendations.

| Decision | Four alternatives | Recommended and selected |
| --- | --- | --- |
| RB-I01 Identity | A sources only; B exact files, generators, explicit public environment and loaded compiler/toolchain; C semantic equality; D ambient filesystem metadata | B: bind the complete admitted input envelope. |
| RB-I02 Build roots | A reuse checkout; B exclusive clean materialization roots with normalized logical paths; C cache-hit comparison; D shared mutable staging | B: independent roots expose hidden directory inputs. |
| RB-I03 Generators | A arbitrary shell; B closed deterministic copy/concatenation/public-environment generation; C inherit host environment; D run unrecorded callbacks | B: explicit authority and implementation identity, without claiming general build-system coverage. |
| RB-I04 Archive | A host tar defaults; B exact canonical file envelope with sorted paths, fixed mode/time and byte payloads; C compare only BEAM; D omit assurance sidecars | B: every produced byte and metadata field has a reproducible identity. |
| RB-I05 Secret inputs | A hash credentials publicly; B refuse marked inputs and exclude credential-dependent builds from this profile; C redact hashes silently; D trust string similarity | B: retain C131's sensitivity boundary without credential guessing oracles. |
| RB-I06 Publishing | A incremental final writes; B complete staged archive and atomic replacement after verification; C ignore interruption; D delete old outputs first | B: incomplete staging cannot publish a partial archive. |
| RB-I07 Signed events | A remove signatures from identity silently; B fixed supplied signed inputs bind normally, newly issued events require a different envelope; C call all signatures deterministic; D mutate timestamps | B: historical replay and issuing new evidence are different operations. |
| RB-I08 Dependencies | A package names alone; B bind every supplied lock and acquired content byte; C registry TLS as identity; D trust prior cache key | B: registry authentication remains P130, while altered acquired inputs invalidate this build. |

| RB-I09 Assurance | A trust archive hashes; B rebuild all outputs and compare the full archive; C compare interfaces alone; D accept a matching cache label | B: rehashed substituted output still fails source-bound verification. |
| RB-I10 Host publication | A promise universal crash durability; B same-directory rename with explicit host/power-loss limits; C overwrite final bytes in place; D promise distributed transactions | B: full-file visibility and storage durability are distinct. |
| RB-I11 Compatibility | A silently rewrite every linker call; B opt-in logical paths while ordinary calls preserve behavior; C change all source origins; D ignore provenance | B: retain existing source semantics and artifact modes. |

## Verification route

Build the same explicit package in independent clean roots with differing ambient
environment/timezone and compare the entire archive, including interface and
assurance outputs. Exercise changed content/toolchain/generators, unsafe paths,
empty packages, archive ordering, fixed metadata and interrupted staging.

## Results and review

The full compiler suite passed **1,024 tests** after revision-discovery assertions
were updated. The subsequent focused suite passed **10 tests**, including one
new capacity test; the final suite therefore contains 1,025 tests. Production
compilation with warnings as errors, escript construction and the maintained
trust audit passed. Existing test-only warnings remain historical.

Independent clean roots produced identical complete archives under changed TZ,
ERL_COMPILER_OPTIONS and an undeclared environment sentinel. The compared outputs
include the actual compiled module, interface, companion BEAM and assurance
sidecar. An empty package emits the companion and assurance. A declared generator
materializes a real compiled source from explicit public input; changed generator
inputs and supplied lock bytes change the envelope key. These are local exact-
envelope experiments, not cross-toolchain or independent-compiler proofs.

A rehashed substituted BEAM archive decodes structurally but fails a fresh full
rebuild comparison. Staging cancellation, corrupt staged bytes and a real killed
owner before commit preserve the previous destination. Owner death leaves an
orphaned stage, intentionally reported as host cleanup rather than falsely
claimed deletion. Unsafe paths and existing user directories are refused.

The trust profile now assigns the new package protocol to identity/governance
and reviews the linker logical-path calls, full-rebuild assurance hook and profile
exposure. It covers **191 sources and 23 data inputs**, digest
`432e9df899367544e05e5c08b83e6389e2a253fad96af148ab1e52418d2ae596`.
The artifact-identity guarantee adds full-package comparison and interruption
witnesses while retaining explicit host/filesystem trust.

Validation commands: `mix test`,
`mix test test/catena/reproducible_package_test.exs`,
`MIX_ENV=prod mix compile --warnings-as-errors`, `MIX_ENV=prod mix escript.build`,
`mix run scripts/check_trust_inventory.exs`, `catena conformance-info`,
`python3 validate_archive.py` and `git diff --check` in their owning repositories.

## Scope limits

This is the exact reproducible packaging protocol for admitted retained build
manifests. General workflow discovery and arbitrary generators remain P121;
registry signatures/acquisition remain P130. New governance event issuance and
credential-dependent builds are excluded. The protocol binds every supplied
lock/dependency byte without claiming to authenticate or resolve it. The existing
C025/C006 contracts still own those semantics. No public language vocabulary was
introduced, and no successful rebuild proves source correctness or native safety.

## Delivery

Compiler [PR 155](https://github.com/pcharbon70/catena/pull/155) merged feature
`a01355886bb62fc1ef9eb748d7fc25131eae442e` as
`e872a922ef12a6a25e61dc71673bc9c9efc4bc7c`. The compiler returned to `rewrite`,
synced with origin and then deleted the feature branch locally and remotely.
Archive validation passed 664 documents, 85 directories, 127 source notes,
199 specification chapters and 959 obligations (864 traced, 74 partial,
21 untraced). Final machine conformance output reports revision 0.1.73's exact
reproducibility profile.
