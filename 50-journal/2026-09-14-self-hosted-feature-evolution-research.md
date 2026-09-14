---
title: "Self-Hosted Feature Evolution Research"
kind: journal
created: "2026-09-14"
tags: [catena, compiler, bootstrap, language-design]
aliases: []
---

# Self-Hosted Feature Evolution Research

## Observations

The user requested a deep research study of the difficulty of adding language
features after Catena becomes self-hosted, including workflows supported by
scientific papers, articles, and blogs.

The session produced a
[synthesis](../20-notes/feature-evolution-in-a-self-hosted-catena-compiler.md),
eleven source notes, a
[topic map](../10-maps/self-hosted-compiler-evolution.md), and an
[open inquiry](../40-inquiries/how-should-catena-evolve-after-self-hosting.md).
The distinction between implementing a feature and adopting it in compiler
source is the central result. Advancing Catena seeds with a retained Elixir
reconstruction chain is a research recommendation, not a normative change.

## Repository evidence

Research baseline: `d2fad6fe460463e1125787a6eb8e34b7f988b391`, clean
`main` before this study. Work branch:
`codex/self-hosted-feature-evolution-research`.

Compiler baseline: `c3a30d09d1c64147de750da0975e4ad05ca1b64a`, clean
`rewrite`. The compiler repository was inspected read-only.

Commands were run in the corresponding repository:

```sh
git rev-parse HEAD
git status --short --branch
```

The compiler evidence files were read and hashed with:

```sh
sha256sum lib/catena/tool/self_hosting.ex test/catena/self_hosting_test.exs test/self-hosting/preflight.json
```

| File relative to the compiler repository | SHA-256 |
| --- | --- |
| `lib/catena/tool/self_hosting.ex` | `6568ac504203b7ef4788e37267da73be6a9b9be701007c6b1805530789f46725` |
| `test/catena/self_hosting_test.exs` | `d2dc1fc1f45dfbfe8510b0ee3507190151d5d8ad49bdf1620955f042f05fe285` |
| `test/self-hosting/preflight.json` | `bd885250ea90592b3b06a94ced8306d856d3a277d32bc7abf6ff1d42e6b8935d` |

Immutable [implementation source](https://github.com/pcharbon70/catena/blob/c3a30d09d1c64147de750da0975e4ad05ca1b64a/lib/catena/tool/self_hosting.ex)
reports `preflight_ready_bootstrap_absent`. Its validator requires absent
Catena source and stage evidence; its assessment returns eight blockers.
The six inspected tests check preflight validation, false claims, drift,
ordering, and lifecycle reporting. **These tests were read, not executed in
this research session.** Historical test results in the
[G141 implementation journal](2026-09-12-self-hosting.md) remain dated evidence.

No Catena self-hosting build, new-language feature experiment, compiler
benchmark, or diverse double-compiling experiment was performed. The proposed
experiments in the synthesis are future work.

## Reading method and provenance

Searches covered feature bootstrapping, compiler source floors, standard-library
staging, runtime primitive transitions, seed artifacts, compiler pass design,
verified bootstrapping, and diverse double-compiling. Selection favored original
papers and project-maintainer accounts over derivative explainers.

| Evidence group | Reading locations and use |
| --- | --- |
| Feature introduction | Thompson, Stages II–III: the escape example and limits of self-reproduction |
| Active project procedures | Rust bootstrap guide; Go source-installation bootstrap sections; OCaml BOOTSTRAP.adoc; GCC native bootstrap and comparison sections |
| Firsthand engineering articles | Xu's 2025 Rust sequence redesign, including its clarification; Kelley's 2022 Zig transition, treated as historical |
| Compiler architecture | Keep and Dybvig, §§2, 3.2–3.3, 4: intermediate languages, compatibility, and evaluation tradeoffs |
| Verified construction | Tan et al., especially §§11.1–11.3; Myreen, §§2, 7, 8, 10 |
| Independent correspondence | Wheeler, §§4.2–4.5 and 5.6.4, plus dissertation errata |

Canonical URLs, publication metadata, consulted copies, reading locations, and
source-specific limits are retained in the eleven notes linked from the
[synthesis's bibliography](../20-notes/feature-evolution-in-a-self-hosted-catena-compiler.md#sources).
Publication details were checked against project or publisher records where
available. No claims about feature-development effort were inferred from search
snippets alone.

Myreen's author PDF could not be read through the web renderer. It was fetched
to a temporary local file with `curl`, extracted using `pdftotext`, and read
there. The archive retains the canonical author link instead of duplicating the
PDF. The author URL is
[the CPP 2021 manuscript](https://www.cse.chalmers.se/~myreen/cpp2021-bootstrap-myreen.pdf).

## Interpretation and authority

The local audit identified a future policy issue in G141: preserving the
original recovery root does not itself define how later compiler source can
grow beyond that root's language support. The current exact-stage and complete
dual-suite obligations remain in force. The study proposes a follow-on design;
it neither declares those obligations satisfied nor weakens them.

At the end of the research-only pass, the
[decision register](../20-notes/design-decision-register.md#g141-feature-evolution-research-inputs)
linked the alternatives without recording them as selected planning choices.
No public vocabulary, compiler implementation, semantic revision, or checklist
checkbox was changed by that study. The subsequent planning request is recorded
below.

## Research-only archive verification

`python3 validate_archive.py` passed with 774 completed documents, 110
directories, 156 source notes, and 224 specification chapters. The tracked
diff passed `git diff --check`; each newly created file also passed
`git diff --no-index --check /dev/null` whitespace inspection. The complete
tracked diff and new documents were reviewed for scope, provenance, stale
links, and accidental changes. Maps, directory inventories, the completion
plan, checklist research link, and decision-register research entry accompany
the study. Compiler tests were not needed for these documentation changes.

## Follow-ups

Measure bootstrap overhead and recovery on real compiler source after P109 and
the required subset permit the initial port. Resolve the inquiry's source-floor,
seed-chain, coverage, comparison, and host-recovery questions before adopting
a routine post-self-hosting workflow. These actions now have work-package owners
in the adopted plan below.

## Planning adoption

The user subsequently asked to update current planning based on this study and
its recommendation. The
[Self-Hosted Compiler Evolution Plan](../20-notes/self-hosted-compiler-evolution-plan.md)
adopts the recommended seed strategy, records ten four-option planning
decisions, and defines E0–E7 dependencies, deliverables, and acceptance evidence.
SHE-01 preserves the study's original four policy alternatives; all selections
match the recommendations and are agent selections under the user's planning
request. The [register](../20-notes/design-decision-register.md#self-hosted-compiler-evolution-plan-2026-09-14)
retains the exact rows, selected options, override status, and durable links.

M9 and item 141 now distinguish the initial G141 milestone from later evolution
readiness. E0 planning is complete; the successor contract, source/seed tooling,
actual port, promotion, transition experiments, and recovery evidence are
pending. The initial `0.1.98` obligations remain in force, public source remains
held for P109, and no semantic revision is allocated.

The update also repairs planning-status references in the study, inquiry, maps,
checklist, and directory inventory. These are planning changes only; there is
no new compiler execution evidence or change to the G141 checkbox.

### Planning verification

Archive validation passed with 775 completed documents, 110 directories, 156
source notes, and 224 specification chapters. A focused consistency check
verified ten identical decision rows in the plan and register, forty
alternatives, matching recommendations and selections with no overrides, and
eight work packages with only E0 complete. Tracked and new-file whitespace
checks passed. The planning changes remain uncommitted alongside the study.
