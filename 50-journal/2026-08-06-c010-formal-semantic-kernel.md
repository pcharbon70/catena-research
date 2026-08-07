---
title: "C010 Formal Semantic Kernel Conformance"
kind: journal
created: "2026-08-06"
tags:
  - concurrency
  - formal-semantics
  - provenance
  - specification
aliases:
  - "C010 candidate conformance record"
  - "C010 formal semantic kernel promotion record"
---

# C010 Formal Semantic Kernel Conformance

## Observations

The coordinated implementation and archive now establish normative C010 at
revision 0.1.8: an exact S-expression semantic module, structural row terms,
a reserved Process effect, named typed process entries, local actor dynamics,
explicit traps, an independently checked core, a reference stepper and
explorer, and fixed OTP 29 lowering.

The pre-commit gate exposed and repaired several places where a plausible
implementation was weaker than the intended boundary. Self-send now preserves
the updated mailbox, local generalization is independently rederived, open-row
extension requires evidence the bounded core does not claim to have, nested
refutable payload patterns do not establish head coverage, unhandled effects
trap explicitly, record and variant values agree across the reference and
BEAM paths, and a local filesystem path no longer changes BEAM line-table
bytes. The declared module origin is the stable artifact provenance.

On 2026-08-07 the user explicitly authorized the immutable compiler commit.
The complete post-commit gate passed against that identity, so all seven C010
chapters became normative together, the inquiry became resolved, and P010 was
renamed and completed as C010.

## Evidence

### Pre-commit compiler candidate

The uncommitted compiler work is based on parent
`a8cfbb46d2315a3f82ca5528424d50f0188fd623`. That parent is context only, not
an immutable identity for these changes. The gate used Erlang/OTP 29
(`erts-17.0.4`), Elixir 1.20.2 compiled for OTP 29, and compiler 10.0.3.

The following commands passed from `/home/ducky/code/catena`:

```text
asdf exec mix format --check-formatted
asdf exec mix clean
asdf exec mix compile --warnings-as-errors
asdf exec mix test
asdf exec mix escript.build
git diff --check
```

The complete suite reported 145 passing tests. The focused C010 file accounts
for 17 of those tests and covers the exact parser boundary, independent core
verification, local generalization, rows, effects and affine resumptions,
actors and scheduling, process interfaces, traps, limits, generated progress
checks, and reference/BEAM agreement.

The built CLI checked and compiled the shared C010 fixture from two distinct
filesystem paths. Both paths produced identical files; the loaded module's
`main/0` returned `{2, true, 5}`. Its compile information named specification
0.1.8, frontend `kernel-sexpr-0.1.8`, edition 0.1, revision 0.1.8, and no
previews. SHA-256 results were:

```text
40c47f8e62c739f951f8a6df88c83cc6cb0ab052c55ae7fb2e35a7eb649d2fb7  C010Fixture.beam
27b9779f5ef6e753beb69519de69bf1f69aaeb84b074a5ca776b5f0c2c63e6d8  C010Fixture.cati.json
```

A deliberately truncated fixture exited with `SYN001` and wrote neither
`C010Fixture.beam` nor `C010Fixture.cati.json`.

### Archive promotion

The archive validation commands are:

```text
python3 validate_archive.py
python3 -m unittest -v test_validate_archive.py
git diff --check
```

The post-promotion validator accepted 220 completed documents, 19 directories,
1,723 local links, 94 source notes, 56 specification chapters, and 64
classified fenced blocks. The focused validator suite reported 20 passing
tests, and `git diff --check` passed.

### Primary-source audit

The source metadata and substantive uses were checked on 2026-08-06 against
the [MIT Press Agha record](https://mitpress.mit.edu/9780262511414/actors/),
the [Acta Cybernetica publisher record](https://cyber.bibl.u-szeged.hu/index.php/actcybern/article/view/4333),
the [OTP-29.0.4 process documentation](https://github.com/erlang/otp/blob/OTP-29.0.4/system/doc/reference_manual/ref_man_processes.md),
the [University of Glasgow Fowler record](https://eprints.gla.ac.uk/298712/),
Plotkin's [author-hosted paper](https://homepages.inf.ed.ac.uk/gdp/publications/sos_jlap.pdf),
and the [Wright–Felleisen publisher record](https://www.sciencedirect.com/science/article/pii/S0890540184710935).
The OTP note is pinned to the exact 29.0.4 tag rather than the mutable current
documentation. No unsupported bibliographic or semantic claim was found.

### Immutable compiler identity

The user explicitly authorized the immutable commit on 2026-08-07. The
identity is:

| Field | Value |
| --- | --- |
| Repository | `pcharbon70/catena` |
| Commit | [`ef8bcf85adde84fed4a7cab3a533eb8399fbe67a`](https://github.com/pcharbon70/catena/commit/ef8bcf85adde84fed4a7cab3a533eb8399fbe67a) |
| Parent | `a8cfbb46d2315a3f82ca5528424d50f0188fd623` |
| Tree | `738b2652dfce2eec4139ec194d579b981813eff7` |
| Commit subject | `Add C010 formal semantic kernel` |

The exact post-commit commands were:

```text
asdf current
asdf exec elixir --version
asdf exec mix format --check-formatted
asdf exec mix clean
asdf exec mix compile --warnings-as-errors
asdf exec mix test
asdf exec mix escript.build
git diff --check
```

They ran with Erlang/OTP 29.0.4 (`erts-17.0.4`), Elixir 1.20.2 compiled for
OTP 29, and compiler 10.0.3. Warning-free compilation succeeded, all 145 tests
passed, the escript built, and the committed worktree remained clean.

Two compilations of the same fixture with distinct diagnostic source paths
produced byte-identical BEAM and interface results. The post-commit hashes
remained:

```text
40c47f8e62c739f951f8a6df88c83cc6cb0ab052c55ae7fb2e35a7eb649d2fb7  C010Fixture.beam
27b9779f5ef6e753beb69519de69bf1f69aaeb84b074a5ca776b5f0c2c63e6d8  C010Fixture.cati.json
```

The loaded `C010Fixture.main/0` returned `{2, true, 5}`. A post-commit CLI run
against a truncated fixture reported `SYN001` and produced neither successful
artifact.

### Promotion result

The immutable identity satisfies the C010 promotion gate. All seven 0.1.8
chapters carry `status: normative`, the integration inquiry carries
`status: resolved`, and checklist item C010 is complete. This promotion does
not widen the bounded grammar or claim ergonomic source syntax, behavioral
mailbox protocols, fairness, supervision, distribution, time, cleanup, or
machine-checked metatheory.

## Threads

- [Formal Semantic Kernel map](../10-maps/formal-semantic-kernel.md)
- [Kernel synthesis](../20-notes/catena-formal-semantic-kernel.md)
- [Kernel inquiry](../40-inquiries/how-should-catena-integrate-its-formal-semantic-kernel.md)
- [Normative specification](../60-specification/formal-semantic-kernel/README.md)

## Follow-ups

- Begin any later semantic slice at the next unused revision, `0.1.9`.
- Keep ergonomic source syntax, richer process protocols, supervision,
  distribution, time, cleanup, and machine-checked metatheory in their
  separately identified work rather than widening C010 implicitly.
