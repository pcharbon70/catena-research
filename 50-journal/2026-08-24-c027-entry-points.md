---
title: "C027 Entry Points"
kind: journal
created: "2026-08-24"
tags:
  - catena
  - conformance
  - entry-points
  - specification
  - testing
aliases:
  - "C027 entry points evidence"
---

# C027 Entry Points

## Observations

Checklist item G027 is complete as C027 and normative source-only
language revision `0.1.23`. The completed boundary fixes the manifest
`entries` array (each entry names one existing zero-argument, total,
effect-closed export with a recorded result spelling and an optional
`launch: true`, at most one marker); libraries derived from zero
declared entries with absent/`null`/`[]` equivalence and no kind flag;
invocation-only launch under unchanged strict kernel semantics that
introduces no scope and spawns no process; return-is-shutdown reports
carrying the entry's value or the kernel trap identity; and stable
`ENT001`–`ENT003` diagnostics with `PKG001`/`EDN001` reused unchanged.

Two implementation decisions worth recording. First, the deliverable
validates entries against the package's compiled *typed cores* rather
than decoded interfaces: arity lives in core `parameters` (the
interface records only name, scheme, and effect row), and the cores are
already in hand at the linker's validation point, so effect-closure is
checked against the recorded `effect_row` and `verified_uses_row`
directly. Second, the `result` field compares against a canonical
rendering of the export's scheme type (`integer`, `boolean`, `v1`,
`(t) -> u`, `{t, u}`, and nominal identity `origin::module::name` with
applied arguments) rather than introducing a second type-spelling
grammar; the closed seven-form type grammar makes the renderer total,
and a mismatch is `ENT001`. Also recorded: a name matching exports in
more than one module is `ambiguous_export` `ENT001` — the manifest
carries no module qualifier, so uniqueness across the package is the
deterministic rule.

This promotion also repairs a C026 oversight found during it: the
completeness checklist's G026 item was never flipped to its completed
`C026` form (the promotion commit changed only the C025 entry's tail).
The C026 header-evidence paragraph and the full completed entry are
restored in this slice's promotion, alongside C027's own flip.

The sibling compiler implementation is commit
[`cd0e5c543ee7ddb7ca840c6657451e3b6c21d7c5`](https://github.com/pcharbon70/catena/commit/cd0e5c543ee7ddb7ca840c6657451e3b6c21d7c5),
merged into the `rewrite` integration line by compiler PR
[#103](https://github.com/pcharbon70/catena/pull/103) at merge commit
[`aeceae7`](https://github.com/pcharbon70/catena/commit/aeceae784aa0ad4b9e4f5c224bb404c5611c9b52).
The merge retained the tested tree exactly (tree `794735a`), and the
compiler PR was merged before this research promotion, following the
established publication order.

## Evidence

The compiler adds the optional `entries` field to the 0.1.7 manifest
decoder with `ENT001` shape rejection (non-array, malformed objects,
invalid names, non-`true` launch, duplicates, multiple markers); the new
`Catena.Entry` module with `library?/1`, `validate/2` (existence,
uniqueness, zero arity, effect-closure, and result-spelling equality
against compiled cores), `launch/2` (module load, invocation, and
`ENT002`/`ENT003` reports), and `render_type/1`; package-linker wiring
that captures each module's BEAM identity and exposes resolved entries
plus per-entry module binaries on the `compile_manifest` result; and
the `guides/language/entry-points.md` guide.

Focused verification:

```text
mix test test/catena/c027_entry_points_test.exs \
  test/catena/c027_traceability_coverage_test.exs
Result: 12 passed
```

Complete compiler verification during implementation:

```text
mix format --check-formatted
mix clean
mix compile --warnings-as-errors
mix test
Result: 342 passed
mix escript.build
git diff --check
```

The focused corpus covers exact selection, lifecycle registration, and
pinned predecessor defaults (the namespace resolver stays pinned at
`0.1.22`; `decode_source_text` advances to `0.1.23`); entries decode
with launch markers and absent/`null`/`[]` library equivalence; every
`ENT001` shape at decode plus the five package-validation classes
(unknown, ambiguous, non-zero-arity, non-closed, result mismatch)
against synthetic cores; multi-entry packages launching by name with
and without markers; invocation-only launch returning the entry's value
twice (determinism) and a trapping entry reported as `ENT003` with the
trap class; `ENT002` for undeclared names with the declared list;
`PKG001`/`EDN001` family identities unchanged; and compilation-root
byte-stability with and without entries.

Archive verification after the complete connected bundle and indexes:

```text
python3 validate_archive.py
python3 -m unittest test_validate_archive.py
git diff --check
```

Results are recorded in the promotion commit.

## Version and boundary decision

C027 consumes `0.1.23` for the entries field, entry validation, the
launch operation, and `ENT001`–`ENT003`. The manifest extension is
optional and backward-compatible; no kernel, retained-JSON, interface,
artifact, or signed-format version changes. Every predecessor API
retains its exact selection. The next unused semantic patch is `0.1.24`.

## Threads

- G084/G089 own supervision, restart, and process lifetime over
  completed entries; G088 owns cancellation and deadlines; G121 owns
  the CLI, exit-code profiles, and host-process boundary; G028 owns the
  compatibility meaning of entry-set changes; G091/G092 own
  distribution and upgrades.

## Follow-ups

Section 3's remainder: G028 (API/ABI compatibility, also owning
re-export facades and entry-set compatibility). P109 remains the
surface capstone.
