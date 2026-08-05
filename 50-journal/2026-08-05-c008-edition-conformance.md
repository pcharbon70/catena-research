---
title: "C008 Edition and Feature-Lifecycle Conformance"
kind: journal
created: "2026-08-05"
tags:
  - beam-vm
  - compatibility
  - migration
  - provenance
  - specification
aliases:
  - "C008 immutable implementation evidence"
---

# C008 Edition and Feature-Lifecycle Conformance

## Status

This record identifies the authorized immutable implementation evidence used
to promote Catena language revision `0.1.7` and checklist item C008. On
2026-08-05, after the candidate implementation and pre-commit checks were
presented, the user explicitly requested that the work be committed and a pull
request created. That request authorized creation of the immutable compiler
commit required by the
[promotion gate](../60-specification/editions-and-feature-lifecycle/migration-diagnostics-and-conformance.md#promotion-gate).

The compiler commit was created once and was not amended. The complete and
focused suites were then rerun against that exact identity before the four
edition-and-lifecycle chapters were promoted together.

## Observations

The sibling compiler implements edition `0.1`, exact retained revisions
`0.1.1` through `0.1.7`, package-wide selection, an immutable feature and
compatibility registry, named preview infrastructure with no current preview,
structured migration diagnostics, selection-bearing interfaces and artifacts,
version-aware governance and signature domains, and runtime erasure of the
selection machinery.

The focused suite also exercises boundaries found during implementation:

- newer frontend transport can select every retained older semantic revision
  while emitting selection-bearing 0.1.7 artifacts;
- C002 match clauses do not falsely require C003 clause conditions;
- C006 verification-only definitions remain available at 0.1.7;
- explicit module selection cannot contradict package selection;
- applying legacy selection fields suppresses `EDN002` without changing
  module, interface, companion, assurance, or signing-payload bytes;
- an ordinary stable feature cannot jump directly to removed, while a modeled
  security or soundness emergency succeeds only with the complete structured
  emergency record;
- interface, specialization, BEAM metadata, assurance, approval, trust-root,
  and signature identities reject selection substitution; and
- generated Erlang Abstract Format function bodies contain no edition or
  preview dispatch.

## Immutable identity

Evidence was observed in `/home/ducky/code/catena`:

```text
compiler branch: agent/complete-g008-editions
compiler commit: 8ef7835d1d7f9b2ab14843ac7817798d58eb2bd4
compiler parent: d662a843ebc8c2bf19fcbd190dfe9fea386c238f
compiler tree: 97fd76b971f0061a206f680af828c407c8c30a14
research branch: agent/complete-g008-editions
research baseline commit: c80db4c244c41fa64958ecde9475993912198d02
Elixir: 1.20.2 compiled with Erlang/OTP 29
Erlang/OTP: 29.0.4, ERTS 17.0.4
Python: 3.12.12
target: BEAM only through OTP 29 Erlang Abstract Format
```

The immutable compiler identity is
[`8ef7835d1d7f9b2ab14843ac7817798d58eb2bd4`](https://github.com/pcharbon70/catena/commit/8ef7835d1d7f9b2ab14843ac7817798d58eb2bd4).

## Evidence

Commands rerun after the immutable compiler commit:

```bash
elixir --version
mix clean
mix compile --warnings-as-errors
mix format --check-formatted
mix test
mix test test/catena/c008_editions_lifecycle_test.exs --trace
mix escript.build
./catena language-info > /tmp/catena-c008-language-info-a.json
./catena language-info > /tmp/catena-c008-language-info-b.json
cmp /tmp/catena-c008-language-info-a.json \
  /tmp/catena-c008-language-info-b.json
sha256sum /tmp/catena-c008-language-info-a.json \
  _build/dev/lib/catena/ebin/Elixir.Catena.LanguageSelection.beam \
  _build/dev/lib/catena/ebin/Elixir.Catena.LanguageVersion.beam \
  _build/dev/lib/catena/ebin/Elixir.Catena.LanguageLifecycle.beam \
  _build/dev/lib/catena/ebin/Elixir.Catena.LanguageInfo.beam \
  _build/dev/lib/catena/ebin/Elixir.Catena.Assurance.beam
test "$(rg -l ':compile\.noenv_forms' lib | wc -l)" -eq 1
rg -n ':compile\.noenv_forms' lib/catena/otp/compiler.ex
git diff --check
```

Commands run in `/home/ducky/code/catena-research` after this record and every
affected index were updated:

```bash
python3 validate_archive.py
python3 -m unittest -v test_validate_archive.py
git diff --check
```

Observed result:

```text
Compiling 53 files (.ex)
Generated catena app
Complete suite: 128 passed
Focused C008 suite: 16 passed
Generated escript catena with MIX_ENV=dev
Repeated language-info outputs: byte-identical
Language registry: 1 edition, 7 revisions, 7 features, 7 changes, 0 previews
Sole production call: lib/catena/otp/compiler.ex:48
Archive: 194 documents, 18 directories, 1506 local links, 84 source notes
Specification structure: 49 chapters, 56 classified fenced blocks
Archive validator unit suite: 10 passed
```

Stable SHA-256 observations from the post-commit run:

| Artifact | SHA-256 |
| --- | --- |
| `catena language-info` JSON | `255f6ae776bd64675c07598371d7e617bea30013d40c7edd989dd87b4aa6c0cf` |
| `Elixir.Catena.LanguageSelection.beam` | `8a1ea5ab6a09f407b525dd90ef23e2fa6da4cfba45e10f5f3b5f400e5f38276e` |
| `Elixir.Catena.LanguageVersion.beam` | `40c056162df6bc19460159d8b7769b671db7ac8d1f8b1bc124c6c93285d230b6` |
| `Elixir.Catena.LanguageLifecycle.beam` | `036099d7cc70d992d14355cd450c23054394e14cee2d4068aef64c008d0cfbe7` |
| `Elixir.Catena.LanguageInfo.beam` | `c5b7c7f52ec48ff3607681f289c703875bad273e1c7024cdb14c488671449128` |
| `Elixir.Catena.Assurance.beam` | `24c10164f3352a1c311515ea5045a968a56bb8ce3b8aecc0ddc8bc81b59badb4` |

Two consecutive `mix escript.build` invocations produced hashes
`a7f18d413bcb588a3428ad0c8b85ddfc100a7e017930804ef9d05b41bd8906bb`
and `f62bc68627d1a8a37ae2148a6aa173df4f0539d641019e698281d650262f7bc3`.
Archive inspection showed minute-varying ZIP timestamps even though the
listed BEAM payloads were unchanged. The escript wrapper is therefore not
claimed as byte-reproducible evidence. This limitation does not weaken the
exact Git tree, stable semantic metadata, module hashes, or conformance test
results, but reproducible release packaging remains future release-engineering
work.

## Result

The authorized immutable identity satisfies the bounded C008 promotion gate.
All four 0.1.7 chapters are normative, checklist C008 is complete, and the
[edition inquiry](../40-inquiries/how-should-catena-version-editions-and-language-features.md)
is resolved for this bounded slice.

## Threads

The [edition and feature-lifecycle map](../10-maps/language-editions-and-feature-lifecycle.md)
connects this evidence to the synthesis, primary sources, inquiry, and
normative chapters. Compiler self-hosting remains the independent G141
milestone rather than part of this promotion.

## Follow-ups

- Publish the immutable compiler and coordinated research commits without
  replacing their tested identities.
- Track reproducible escript packaging with the broader release-engineering
  and reproducible-build work rather than reopening C008's language contract.
