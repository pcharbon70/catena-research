---
title: "Exact Inputs and Canonical Packages"
kind: specification
created: "2026-09-09"
status: normative
spec_version: "0.1.73"
tags: [specification, conformance, security]
aliases: []
---

# Exact Inputs and Canonical Packages

## Status and authority

C128 defines revision `0.1.73` under [authority](../../SPECIFICATION-AUTHORITY.md),
[conformance vocabulary](../../CONFORMANCE-VOCABULARY.md) and
[implementation limits](../../IMPLEMENTATION-LIMITS.md). It executes the
[reviewed reproducibility plan](../../20-notes/language-completion-plan-delivery.md#item-128-reproducible-builds).
Reproducibility means identical complete output bytes under the exact admitted
input and toolchain envelope. It does not mean cross-toolchain identity, semantic
correctness, authentic registry acquisition or native safety (`RB-OBL-001`).

This separate packaging protocol consumes retained `0.1.6` and `0.1.7` package
manifests with the build action and no governance evaluation. It introduces no
public language vocabulary or new source frontend. General build workflows remain
P121, registry authentication P130, and new signed-event issuance its existing
governance contract. Unsupported actions are refused.

## Input envelope

An envelope contains the exact manifest filename, every supplied input file byte,
explicit public environment map, ordered generator declarations, complete expected
output paths, generated-input digest map and observed toolchain. Its format,
revision and canonical digest bind all these fields. Files are encoded as base64
without changing their original bytes; their names are logical relative paths.
Reverification rebuilds the envelope and compares every field, not merely its
caller-supplied digest (`RB-OBL-002`).

The toolchain binds the supported OTP/ERTS/Elixir/compiler/runtime/platform
fingerprint, every loaded Catena application module's implementation identity and
the configured implementation-limit profile. Altered compiler, toolchain or limits
fail verification against the running implementation. The envelope's digest is
the cache identity; this profile always builds without reading a result cache.
An apparent cache hit is not a substitute for independent rebuild verification
(`RB-OBL-003`).

Every supplied lockfile, imported interface and acquired dependency content byte
belongs to the input identity, including supplied files not read by the selected
manifest. Changing such bytes changes the key. The retained linker still checks
interfaces and package semantics. Hash inclusion alone does not validate registry
signatures, resolve dependencies or prove a supplied lock is semantically correct;
those remain the acquiring/resolving contract's obligations (`RB-OBL-004`).

## Generators and environment

Generators form an ordered finite list. Each names a fresh output path and an
ordered list of parts. A part is exactly one explicit literal, a previously supplied
or generated file, or a key in the explicit public environment map. Generation
concatenates these bytes. Unknown fields, missing inputs, output collisions and
unsupported generator forms fail planning. Generated inputs and declaration order
are bound by the envelope (`RB-OBL-005`).

Generators do not invoke a shell, host callback, clock, network service or ambient
environment lookup. The declared environment is an explicit map used by these
closed operations; it is not inherited from the build process. Compilation uses
the retained OTP no-environment compilation boundary. Changes to undeclared
compiler environment or timezone do not become valid build inputs. A future
arbitrary generator requires its own exact authority and reproducibility contract.

Marked C131 secret inputs/references are refused anywhere in the envelope setup.
Secret-dependent builds are excluded; secrets are not converted into public
content digests. Trusted host code is responsible for not relabeling raw credential
bytes as public input. Existing fixed signed bytes supplied as files are bound
like other inputs. Creating a fresh signed event, timestamp or approval is a
separate operation with different inputs, not an ignored nondeterministic field
(`RB-OBL-006`). Governance evaluation/issuance is not admitted by this profile.

## Independent build roots

A build verifies the envelope before exclusively creating a new root directory.
An existing directory is refused without changing its contents. Materialization
writes only declared/generated regular files under the root. The manifest resides
at its root; all source, interface and output paths are normalized relative paths.
Paths contain only ASCII letters, digits, underscores, hyphens and dots separated
by single slashes; dot and dot-dot components, absolute paths, backslashes and
empty components are refused (`RB-OBL-007`).

Compiler-facing paths use the fixed logical prefix `catena://build/` and the
relative source or manifest path. Physical materialization paths remain host
locations, not emitted compiler path identity. Explicit origins already present
in source/interface bytes remain those exact declared inputs; the build does not
silently rewrite semantic provenance (`RB-OBL-008`).

The retained package linker compiles all declared modules and the companion,
produces every interface and assurance sidecar and checks the owning language
rules. All expected outputs are read as bounded regular files. Output paths are
unique and cannot overlap input files. Build errors produce no archive result.
The temporary root is removed on normal completion or handled failure; privileged
host interference or abrupt process/VM death can leave temporary data requiring
host cleanup (`RB-OBL-009`).

## Canonical full-output archive

The archive is canonical JSON containing its exact format/revision, input-envelope
digest and the complete sorted output-file sequence. Each entry contains path,
base64 bytes, SHA-256 content digest, mode 420 (octal 0644) and timestamp zero.
These are archive metadata, independent of source filesystem creation order,
umask or modification time. Empty file sequences have a canonical representation;
an empty language package still emits its companion and assurance output
(`RB-OBL-010`).

Decoding requires exact canonical re-encoding. Unknown fields, reordered or
duplicate paths, changed mode/time, invalid bytes or mismatched digest fail.
Successful decoding establishes canonical integrity only. Full assurance
verification rebuilds the package in another fresh root and compares the entire
archive. A substituted output with recomputed hashes can decode yet fails exact
rebuild comparison (`RB-OBL-011`).

## Publication and interruption

Staging verifies the complete archive, creates an exclusive random sibling file
and writes it synchronously. It returns an owner-bound staging record with exact
archive digest and final path. The published destination remains unchanged.
Commit checks owner, sibling staging path, regular file status, exact content
digest and canonical archive validity before one same-directory rename. Cancellation
removes the owned stage. Corrupt or incomplete staging cannot replace the prior
archive (`RB-OBL-012`).

Owner death before commit can leave an orphaned stage but leaves the destination
unchanged. Normal readers see the old or new complete file under the supported
host filesystem's rename semantics. Host interference, concurrent external file
mutation and crash/power-loss durability remain filesystem/host trust; this
protocol does not claim directory fsync or distributed atomic publication.

## Limits and variability register

The exact profile caps 256 supplied/generated files and 256 output files, 16 MiB
per file and 64 MiB aggregate bytes in each file set. It admits 64 generators,
64 parts per generator and 64 explicit environment entries. Environment keys are
1–64 ASCII bytes matching an uppercase letter followed by uppercase letters,
digits or underscores; values are valid UTF-8 with at most 65,536 bytes. Logical
paths contain 1–240 ASCII bytes. Canonical archive decoding caps 96 MiB
(`RB-OBL-013`).

Capacity or malformed input causes explicit refusal; no file content is truncated.
Base64 decoding and serialization perform host allocations before all aggregate
checks, and compilation retains its owning phase limits. No hostile-input memory
floor or universal host liveness follows. These fixed limits and exclusions are
machine-reported. No configurable archive timestamp, file order or permission
variation is admitted by this profile.

## Rationale and evidence (non-normative)

The [journal](../../50-journal/2026-09-09-reproducible-packages.md) records four-way
decisions, independent full-output runs, substituted archive refusal and real
staging interruption. The [OTP support contract](../otp-compatibility/support-probes-and-artifacts.md)
owns supported compiler/runtime identity. The
[secret contract](../secret-capabilities/sealed-values-and-protected-delivery.md)
explains why public reproducibility manifests do not contain credential hashes.
