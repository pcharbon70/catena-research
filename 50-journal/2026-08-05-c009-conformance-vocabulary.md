---
title: "C009 Conformance Vocabulary"
kind: journal
created: "2026-08-05"
tags:
  - governance
  - language-design
  - specification
aliases:
  - "C009 conformance vocabulary evidence"
---

# C009 Conformance Vocabulary

## Observations

Checklist item C009 completes repository governance, not a semantic language
slice. The root
[Catena Conformance Vocabulary](../CONFORMANCE-VOCABULARY.md) defines five
canonical requirement words—`MUST`, `MUST NOT`, `SHOULD`, `SHOULD NOT`, and
`MAY`—and the required, invalid, implementation-defined, bounded unspecified
presentation, implementation-limit, and explicit runtime-failure classes.
Plain declarative normative rules remain binding. Uppercase aliases are
prohibited, while lowercase words keep their ordinary English meaning.

The policy states that Catena has no undefined behavior. Invalidity requires
failure without successful output publication at the affected boundary;
specification silence is a defect; and future foreign or unsafe facilities
must define rejection, failure, or trapping rather than create an arbitrary
behavior escape. No current normative chapter declares an
implementation-defined choice.

The model was developed in the
[synthesis](../20-notes/catena-conformance-vocabulary-and-behavior-classes.md)
and [resolved inquiry](../40-inquiries/how-should-catena-classify-conformance-behavior.md),
with a [topic map](../10-maps/catena-conformance-vocabulary.md) routing through
primary notes on [RFC 2119](../30-sources/bradner-1997-rfc-2119.md),
[RFC 8174](../30-sources/leiba-2017-rfc-8174.md),
[WG14 N1570](../30-sources/wg14-2011-n1570.md), and the
[WebAssembly Core Specification](../30-sources/rossberg-2026-webassembly-core-specification.md).
Bibliographic metadata and claims were checked against the official RFC
Editor, WG14, and WebAssembly editions on 2026-08-05.

## Corpus audit

The audit excluded directory READMEs, because their variability registers
summarize chapter rules rather than add normative requirements. It reviewed
every uppercase `MAY` and `SHOULD` occurrence and every case-insensitive use of
`invalid`, `malformed`, or `ill-formed` in the 49 current normative chapters.

| Specification area | `MAY` occurrences | `SHOULD` occurrences | Invalidity terms |
| --- | ---: | ---: | ---: |
| Clause conditions | 0 | 1 | 10 |
| Data and patterns | 6 | 1 | 17 |
| Editions and feature lifecycle | 8 | 1 | 6 |
| Effects and handlers | 1 | 0 | 9 |
| Specifications and governance | 3 | 0 | 21 |
| Traits and categorical operations | 2 | 0 | 6 |
| Type system | 2 | 2 | 5 |
| **Total** | **22** | **5** | **74** |

The 22 `MAY` occurrences comprise source/package permissions, explicit tool or
layout paths, optional non-runtime metadata, and bounded implementation
techniques. None changes an unreported observable choice, so none is
implementation-defined. Every permission is represented in its area's
variability register. The type-variable and constraint-order allowance is now
visibly labelled as bounded unspecified presentation and preserves
alpha-equivalence, typed core, stable diagnostic identity, and artifact
identity.

The five substantive `SHOULD` recommendations have explicit bootstrap-profile
dispositions:

- secondary diagnostic spans are not implemented and remain tracked by P117;
- task-facing clause-condition wording currently deviates and remains tracked
  by P117;
- shared pattern matrices are a current performance deviation tracked by
  G138;
- original Catena source locations remain unavailable until source parsing and
  location work tracked by P117 and the source-file gaps; and
- the stale-preview removal edit is not implemented and remains tracked by
  P125.

Each invalidity occurrence names a malformed or ill-formed input/action with a
specified rejection path, a diagnostic or conformance-test category, or an
unreachable invalid-evidence/value fallback. None grants arbitrary
continuation, suppresses the required diagnostic family, or permits successful
transactional output.

## Evidence

Archive enforcement added focused tests for canonical words, prohibited
uppercase aliases, non-normative and quotation exemptions, undefined-behavior
rejection, labelled implementation-defined and unspecified-presentation
callouts, bounded presentation, policy links, and area variability registers.
The verification commands were:

```text
python3 -m unittest -v test_validate_archive.py
python3 validate_archive.py
git diff --check
```

The focused validator suite reported 20 passing tests. Complete archive
validation passed after the policy, research bundle, journal, maps, and indexes
were connected.

The sibling compiler repository added a human-readable, versioned
`CONFORMANCE.md` profile format 1 and linked it from the root README,
contributor guide, guide index, diagnostics guide, and feature-development
workflow. The profile records compiler release `0.1.0`, Elixir `1.20.2`,
Erlang/OTP `29.0.4`, BEAM-only targeting, edition `0.1`, revisions `0.1.1`
through `0.1.7`, zero implementation-defined choices, zero vendor extensions,
all current implementation-scoped optional paths and recommendation
dispositions, bounded diagnostic and type-variable presentation, and the
current 20,000-step limits and conservative analysis cutoff.

The documentation-only compiler branch is based on
`b0f4f14f2878215ab94dbbd508d3c02ceba23d32`. It was checked with:

```text
asdf exec mix format --check-formatted
asdf exec mix clean
asdf exec mix compile --warnings-as-errors
asdf exec mix test
asdf exec mix escript.build
git diff --check
```

The compiler rebuilt 53 files without warnings, reported 128 passing tests,
and generated the escript successfully. The generated escript was removed
after verification. No compiler source, test, AST, interface, artifact,
signature domain, CLI contract, BEAM lowering, or runtime behavior changed.

## Result

C009 is complete. Final validation reported 202 completed documents, 18
directories, 1,633 local links, 88 source notes, 49 specification chapters,
and 56 classified specification fenced blocks.

Because this milestone only governs how existing and future normative prose is
interpreted, it does not create language revision `0.1.8`. The next semantic
slice still receives `0.1.8`. C009 also requires no immutable semantic compiler
commit or implementation promotion gate; the compiler work is descriptive
documentation and remains uncommitted pending separate authorization.

## Threads

- C012 now supplies the general portability policy, configurable
  implementation-limit contract, and machine-readable compiler profile.
- P117 remains responsible for source locations, secondary spans, and
  diagnostic wording quality.
- P125 remains responsible for richer migration edits.
- G138 remains responsible for pattern-matrix sharing and related performance
  work.

## Follow-ups

The first real implementation-defined choice must enumerate its bounded domain
in normative text and appear in both compiler profile forms before any
compiler can claim that choice. C012 introduced deterministic
`catena conformance-info` earlier because portable limits already create a
tooling-discovery need; human-readable format 1 remains the explanatory
profile.
