---
title: "C025 Package Identity and Dependencies"
kind: journal
created: "2026-08-24"
tags:
  - catena
  - conformance
  - packages
  - specification
  - testing
aliases:
  - "C025 package evidence"
---

# C025 Package Identity and Dependencies

## Observations

Checklist item G025 is complete as C025 and normative source-only
language revision `0.1.21`. The completed boundary fixes the manifest
`dependencies` field; the SemVer 2.0.0 version grammar and precedence
vendored exactly (pre-release ordering, numeric-below-alphanumeric
identifiers, longer-list-above-prefix, build excluded); the
exact/caret/tilde requirement grammar with the Cargo-style 0.x caret
rule and Hex's pre-release operand restriction; single-version
highest-satisfying order-independent resolution with `PKG003` requirer
lists; `PKG002` package-graph cycle rejection; byte-deterministic
generated `catena.lock` records that replay as exact pins with `PKG005`
stale/tamper separation; and registry-neutral SHA-256 bundle digests
binding manifest semantics plus member interface digests plus C024
component joint digests, with hex.pm recorded as the bootstrap transport
profile.

Two implementation notes. First, the SemVer precedence comparison had
the classic empty-pre-release bug in both directions during development
— `1.0.0-alpha` versus `1.0.0` and the shorter-prefix rule — caught by
the boundary tables before commit; the final comparator decides
release-versus-pre-release first and only then compares identifier lists,
which also yields the correct longer-list-above-prefix behavior. Second,
the engine deliberately shares nothing with the compiler's compilation
path beyond `CanonicalJCS`: the manifest decoder gained only an optional
`dependencies` object, so every previously valid manifest is unchanged
and the namespace resolver's required revision stays at 0.1.20 — C025
extends no existing grammar in place, the first slice since C019 with
that property.

The sibling compiler implementation is commit
[`dcd7da056ba1317fcd7df1df8716981ff8363e1d`](https://github.com/pcharbon70/catena/commit/dcd7da056ba1317fcd7df1df8716981ff8363e1d),
merged into the `rewrite` integration line by compiler PR
[#101](https://github.com/pcharbon70/catena/pull/101) at merge commit
[`45b6641`](https://github.com/pcharbon70/catena/commit/45b66414071276097a7571bbf1f8661a635cb4d0).
The merge retained the tested tree exactly (tree `6bf6dc5`), and the
compiler PR was merged before this research promotion, following the
established publication order.

## Evidence

The compiler adds `Catena.Package.Deps` with `parse_version/1`,
`parse_requirement/1`, `satisfies?/2`, `resolve/2`,
`generate_lockfile/2`, `replay_lockfile/3`, and `bundle_digest/1`; the
optional `dependencies` object in the 0.1.7 manifest decoder; and the
`guides/language/packages.md` guide.

Focused verification:

```text
mix test test/catena/c025_package_deps_test.exs \
  test/catena/c025_traceability_coverage_test.exs
Result: 11 passed
```

Complete compiler verification during implementation:

```text
mix format --check-formatted
mix clean
mix compile --warnings-as-errors
mix test
Result: 323 passed
mix escript.build
git diff --check
```

The focused corpus covers exact selection, lifecycle registration, and
pinned predecessor defaults (including the resolver's unchanged 0.1.20
pin); the version grammar matrix (seven malformed forms) and the full
precedence battery (release-below, prefix, alphanumeric, numeric
magnitude, build equality); the requirement matrix rejecting comparators,
Hex `~>`, compounds, operand build metadata, and partial operands; the
satisfaction boundary tables including `^0.1.2`/`^0.0.3`/`~1.2.3` edges
and same-triple pre-release restriction with build-tolerant exact
matches; diamond resolution to the joint-window maximum with root and
environment permutation invariance and repeat equality; pair and
three-package `PKG002` cycles with path text; `PKG003` with both
requirers listed and `PKG004` unknown names and `PKG005` build-duplicate
environments; lock double-generation byte-equality with format and
selection fields; replay exactness, re-lock rejection with the `missing`
list, tamper rejection naming all packages, and malformed-lock
`PKG001`; bundle-digest stability under complete field reordering; and
manifest-decoder integration carrying `dependencies` alongside full
0.1.7 required fields with C024 component digests flowing into locks.

Archive verification after the complete connected bundle and indexes:

```text
python3 validate_archive.py
python3 -m unittest test_validate_archive.py
git diff --check
```

Results are recorded in the promotion commit; 353 completed documents
were checked across 32 directories with 3,725 local links, 94
specification chapters, 487 traceability obligations, and all 26
validator unit tests passing.

## Version and boundary decision

C025 consumes `0.1.21` for the dependency grammar, resolution, lockfile,
identity, and `PKG001`–`PKG005`. The SemVer package axis is distinct
from language revisions and compiler releases; the manifest extension is
optional and backward-compatible; and no kernel, retained-JSON,
interface, artifact, or signed-format version changes. Every predecessor
API retains its exact selection. The next unused semantic patch is
`0.1.22`.

## Threads

- G121 must build fetch/lock/publish tools on this engine; G128 must
  consume bundle digests for reproducible builds; G130 must layer
  signing and the threat model; G028 owns compatibility meanings of
  version increments and the re-export facades this area re-owned; G026
  and G027 retain prelude and entry-point decisions; the Hex hypothesis
  note is now normatively profiled and can be archived with this slice.

## Follow-ups

Plan G026 next — the prelude becomes one more resolution origin over
the fixed C021/C022 machinery — or G027; P109 remains the surface
capstone.
