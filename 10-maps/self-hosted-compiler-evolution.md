---
title: "Self-Hosted Compiler Evolution"
kind: map
created: "2026-09-14"
tags: [catena, compiler, bootstrap, language-design]
aliases: []
---

# Self-Hosted Compiler Evolution

## Scope

How a compiler written in Catena can acquire new features, adopt those features
in its own source, and remain reproducible and recoverable. This map connects
engineering practice to G141 without treating a research recommendation as
implemented language policy.

## Start here

1. [Self-Hosted Compiler Evolution Plan](../20-notes/self-hosted-compiler-evolution-plan.md)
   adopts the recommended seed strategy through ten recorded decisions and
   E0–E7 work packages; only planning is complete.
2. [Feature Evolution in a Self-Hosted Catena Compiler](../20-notes/feature-evolution-in-a-self-hosted-catena-compiler.md)
   explains the central dependency, compares eight workflows, and recommends
   advancing exact Catena seeds with a retained chain to Elixir.
3. [The current G141 contract](../60-specification/compiler-self-hosting/staged-bootstrap-and-fixed-point-evidence.md)
   defines the initial transition and blocked preflight; it remains the
   authority for the milestone.
4. [The open evolution inquiry](../40-inquiries/how-should-catena-evolve-after-self-hosting.md)
   tracks normative and empirical validation of the selected direction.

## Trails

### Teaching a feature before using it

- [Thompson's compiler example](../30-sources/thompson-1984-reflections-on-trusting-trust.md)
  makes the implementation/self-adoption distinction concrete.
- [Rust's bootstrap stages](../30-sources/rust-project-2026-compiler-bootstrap-stages.md)
  help trace builder and library dependencies.
- [Go's bootstrap requirements](../30-sources/go-project-2026-source-bootstrap-requirements.md)
  provide a model for publishing an advancing source floor.

### Managing difficult transitions

- [OCaml's bootstrap instructions](../30-sources/ocaml-project-2026-compiler-bootstrap.md)
  address primitive and format transitions.
- [Rust's initial-sequence redesign](../30-sources/xu-2025-rust-bootstrap-sequence.md)
  explains the distinction between libraries used by the compiler and those
  it builds for programs.
- [Zig's 2022 transition](../30-sources/kelley-2022-zig-bootstrap.md)
  exposes the tradeoff between duplicated compiler maintenance, convenient
  seed artifacts, and source reconstruction.
- [Nanopass compiler development](../30-sources/keep-et-al-2013-nanopass-compiler-development.md)
  connects pass boundaries to implementation structure and measured tradeoffs.

### Knowing what a successful bootstrap proves

- [GCC's stage comparison](../30-sources/gcc-project-2026-bootstrap-builds.md)
  motivates specifying the comparison pair.
- [The CakeML backend](../30-sources/tan-et-al-2019-verified-cakeml-backend.md)
  and [minimal verified bootstrap](../30-sources/myreen-2021-minimalistic-verified-bootstrap.md)
  distinguish mechanized correctness from ordinary self-compilation.
- [Diverse double-compiling](../30-sources/wheeler-2009-diverse-double-compiling.md)
  addresses source–executable correspondence under explicit assumptions.

### Returning to Catena

- [The completion map](language-completion.md) locates G141 among its language,
  tooling, and release dependencies.
- [Reproducible builds](../60-specification/reproducible-builds/README.md) and
  [OTP compatibility](../60-specification/otp-compatibility/README.md) constrain
  the input envelopes and artifacts used in a bootstrap.
- [The research journal](../50-journal/2026-09-14-self-hosted-feature-evolution-research.md)
  records the local audit and reading provenance.

## Open questions

The [inquiry](../40-inquiries/how-should-catena-evolve-after-self-hosting.md)
owns routine seed promotion, recovery-chain replay, stage comparison, and
independent evidence after compiler source grows beyond the frozen bootstrap.
Planning direction is adopted; normative policy and real compiler experiments
remain pending.
