---
title: "C006 Executable Specification and Governance Conformance"
kind: journal
created: "2026-08-03"
tags:
  - beam-vm
  - governance
  - provenance
  - specification
aliases:
  - "C006 candidate implementation evidence"
  - "C006 executable implementation evidence"
---

# C006 Executable Specification and Governance Conformance

## Observations

The sibling Catena compiler implementation is frozen on branch
`agent/c006-spec-governance` at commit
`2f6805e166a086f7d67c2cc0f3023e9e34fe2cec`, based directly on commit
`acc28fca67ffb18746f9376bfefe81dc3479c6a1`. The user explicitly authorized
creation of the immutable compiler commit on 2026-08-03 before this archive
recorded its identity or promoted the
[version 0.6 specification and governance chapters](../60-specification/specifications-and-governance/README.md).

The Elixir implementation adds:

- JSON AST 0.6 rules, exact examples, typed claim subjects, stable claim
  identities, semantic digests, and verification-only definitions;
- an explicitly typed pure checker with deterministic 20,000-step execution,
  separate result classes, and runtime-to-verification dependency rejection;
- additive policy over package, module, subject, action, output, interface,
  and profile scopes, with a separately structured reference evaluator;
- strict JSON canonicalization, SHA-256 identities, domain-separated Ed25519
  verification, distinct-principal thresholds, scoped delegation, revocation,
  normal rotation, predeclared recovery, and historical trust-root replay;
- compiler evidence, exact signed attestations and assumptions, approval
  records, and signed hash-chained lifecycle transitions;
- staged package output, rollback on failed gates, exact artifact manifests,
  external signing payloads, and offline assurance verification; and
- complete removal of verification and governance material before Erlang
  Abstract Format, including byte-identical module and companion BEAM tests.

No Rust or Python compiler component, Core Erlang emitter, direct BEAM
assembler, private-key input, runtime assurance monitor, or alternate target VM
was introduced. The only production BEAM generation call remains
`:compile.noenv_forms/2` in `lib/catena/otp/compiler.ex`.

## Evidence

Environment observed in `/home/ducky/code/catena`:

```text
branch: agent/c006-spec-governance
baseline commit: acc28fca67ffb18746f9376bfefe81dc3479c6a1
implementation commit: 2f6805e166a086f7d67c2cc0f3023e9e34fe2cec
implementation tree: eb00cf250ed87de5f2c518d5e7717f760301bebf
authorization date: 2026-08-03
Elixir: 1.20.2 compiled with Erlang/OTP 29
Erlang/OTP: 29.0.4, ERTS 17.0.4
target: BEAM only through OTP 29 Erlang Abstract Format
```

Commands rerun after the immutable commit:

```bash
mix format --check-formatted
mix clean
mix compile --warnings-as-errors
mix test
mix test test/catena/c006_specification_governance_test.exs --trace
mix escript.build
git diff --check
test "$(rg -l ':compile\.noenv_forms' lib | wc -l)" -eq 1
rg -n ':compile\.noenv_forms' lib/catena/otp/compiler.ex
sha256sum catena \
  _build/dev/lib/catena/ebin/Elixir.Catena.Specification.beam \
  _build/dev/lib/catena/ebin/Elixir.Catena.Governance.beam \
  _build/dev/lib/catena/ebin/Elixir.Catena.Assurance.beam
```

Observed result:

```text
Compiling 49 files (.ex)
Generated catena app
Running ExUnit
Result: 108 passed
Focused C006 result: 34 passed
Generated escript catena with MIX_ENV=dev
sole production call: lib/catena/otp/compiler.ex:27
```

Artifact SHA-256 digests from that run:

| Artifact | SHA-256 |
| --- | --- |
| `catena` escript | `71cdfd4e048c6cdea7b9514caa4e8ae02ede98395e7d224d6bb2758897bedc2f` |
| `Elixir.Catena.Specification.beam` | `3dc87172c09bd2dbdc466a47e55411a006fb3d8606e5303218e089b156400cb7` |
| `Elixir.Catena.Governance.beam` | `c38d64924d114f0531fe4ba7349d310ed7c0a3964bc00a98d92edd97f776c4d3` |
| `Elixir.Catena.Assurance.beam` | `c591bef6bff82c42d2ad0b28b1152d97d35376ff26b0a6dd35f0457944ec928c` |

The focused suite covers RFC canonicalization and Ed25519 vectors; all subject
kinds and checker failures; claim stability; independent policy-oracle
agreement; shared policy budgets; additive scopes; trust rotation, recovery,
delegation, revocation, and signature-domain attacks; assumption and
attestation binding; every valid lifecycle edge and invalid replay; exact
package artifacts and imported obligations; external signing; transactional
failure; traversal and symlink attacks; artifact substitution; total erasure;
and byte-identical BEAM output. The complete run keeps C001 through C005 green.

## Result

The bounded C006 implementation satisfies every version 0.6 promotion-gate
condition. All six chapters are normative, and checklist items C006 and C110
through C115 are complete against this immutable identity.

This is executable and adversarial evidence for the bounded offline protocol,
not a mechanized proof of the wider design. Public parser punctuation remains
P109, and long-term schema and compiler evolution remains G116. Runtime
monitoring, stronger verification methods, representative performance, and
programmer-comprehension evidence remain outside version 0.6.

## Threads

The broader
[specification and governance inquiry](../40-inquiries/how-should-catena-integrate-specifications-and-governance-into-the-language.md)
remains open for generalized metatheory, retained runtime contracts, richer
evidence producers, protocol evolution, performance, and usability. The
[topic map](../10-maps/language-integrated-specifications-and-governance.md)
provides the curated route through those questions.

## Follow-ups

1. Publish the immutable compiler commit without replacing its tested identity.
2. Add pull-request and merge identities after publication and merge.
3. Preserve this implementation identity when a later language version
   supersedes 0.6.
