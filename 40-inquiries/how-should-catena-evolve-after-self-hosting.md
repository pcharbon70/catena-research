---
title: "How Should Catena Evolve After Self-Hosting?"
kind: inquiry
created: "2026-09-14"
status: open
tags: [catena, compiler, bootstrap, language-design, compatibility]
aliases: []
---

# How Should Catena Evolve After Self-Hosting?

## Why this matters

The initial self-hosting milestone does not settle how later compiler source
can use new language features. Requiring the original Elixir compiler to build
every future source revision directly could constrain compiler source or
require substantial duplicate implementation work. Keeping only an opaque
recent compiler would weaken recovery. The project needs an explicit middle
path before that choice becomes an accidental build-system dependency.

## Operational question

Can Catena introduce and then internally adopt representative new features
while every supported compiler revision has a declared, tested bootstrap path
and accurate independent evidence?

Measure bootstrap-specific build time, storage, contributor steps, failures,
seed promotions, and temporary compatibility code separately from feature
design, implementation, and proof maintenance. A working local binary is
insufficient: a clean builder must reconstruct the declared path without
undeclared compilers, libraries, or network inputs.

## Working hypotheses

1. Most additive features can be implemented in the existing compiler-source
   subset and tested before they are adopted internally.
2. Advancing exact Catena seeds can avoid maintaining two complete production
   compilers while preserving an immutable path to the Elixir recovery root.
3. Runtime and metadata transitions will require more coordination than surface
   features lowered to existing semantics.
4. Distinguishing reproducible packages, stage observations, semantic correctness,
   and source correspondence will prevent overclaiming bootstrap evidence.

These are research hypotheses, not adopted replacements for G141.

The user has now requested planning adoption of the recommendation. The
[evolution plan](../20-notes/self-hosted-compiler-evolution-plan.md) selects
advancing pinned Catena seeds, a conservative source floor, delayed internal
feature adoption, and retained reconstruction to Elixir. That planning choice
is settled; the hypotheses about its practical cost and reliability still need
the experiments below.

## Findings

The [synthesis](../20-notes/feature-evolution-in-a-self-hosted-catena-compiler.md)
compares eight workflows and eleven primary works. It supports the dependency
mechanism but supplies no empirical Catena effort estimate.

The [local audit](../50-journal/2026-09-14-self-hosted-feature-evolution-research.md)
confirms that current G141 support is a blocked preflight, not a completed
bootstrap. Public compiler source remains held for P109. Therefore none of the
proposed evolution experiments has yet been performed on a self-hosted Catena
compiler.

## Paths to explore

| Question | Selected planning direction | Evidence still needed |
| --- | --- | --- |
| Must original Elixir compile current source directly? | Preserve it as the immutable recovery root and permit declared Catena seed chains afterward | Explicit future normative scope and successful end-to-end reconstruction |
| When should the routine seed advance? | Promote for required facilities or fixes, with a conservative source floor | Observed promotion frequency and contributor/build costs |
| Which independent checks replace full frozen-bootstrap coverage of later features? | Keep complete shared-language evidence and add explicit extension-specific reference evidence | Per-feature coverage and an adopted successor to the present dual-suite obligation |
| What should later stages compare? | Define artifact subjects and versioned observations while preserving full provenance | Experiments with code-generation changes and distinct builder envelopes |
| How much historical reconstruction is practical? | Supply convenient seed bundles and replay the retained chain separately | Measured time/storage and successful offline recovery |
| What happens when an old host can no longer execute the root? | Retain a supported recovery environment or admit a verified transition path | A real host-transition drill with declared residual trust |

The [topic map](../10-maps/self-hosted-compiler-evolution.md) routes to the
primary evidence. The synthesis's experiments cover a surface feature, semantic
extension, runtime/interface transition, seed promotion, missing inputs,
stage drift, and interrupted activation.

## Outcome

Open for normative and empirical validation. The general seed strategy is
adopted for planning and recorded in the
[decision register](../20-notes/design-decision-register.md#self-hosted-compiler-evolution-plan-2026-09-14).
No compiler behavior, normative revision, public syntax, or G141 completion
status changed.

Resolution requires E1's explicit reconciliation with the
[current contract](../60-specification/compiler-self-hosting/staged-bootstrap-and-fixed-point-evidence.md),
followed by E3–E7's retained evidence from actual compiler source, seed promotion,
feature transitions, and recovery. Record implementation discoveries and
deviations when they occur; planning selection alone does not establish the
recommended workflow's measured cost or reliability.
