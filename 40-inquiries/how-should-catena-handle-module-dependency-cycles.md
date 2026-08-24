---
title: "How Should Catena Handle Module Dependency Cycles?"
kind: inquiry
created: "2026-08-24"
status: open
tags:
  - catena
  - language-design
  - modules
  - separate-compilation
aliases:
  - "Catena module cycles inquiry"
---

# How Should Catena Handle Module Dependency Cycles?

## Why this matters

C022 fixed imports as digest-bound admissions: a module checks against the
computed interface digest of each dependency. That model is inherently
acyclic — a cycle would need A's digest inside B's and B's inside A's —
while C002's recursive groups already make *value-level* mutual recursion
ordinary inside one module. Until the cross-module question is answered,
implementations could disagree about whether A and B may reference each
other, what checking unit a cycle forms, when module "initialization"
happens, and how separate-compilation caches behave — disagreements that
would leak into G025's package assembly, P109's declaration grammar, and
every multi-module diagnostic.

## Operational question

Decide, for edition 0.1:

- whether module import graphs may contain cycles, and if so what the
  unit of checking, resolution, and caching is;
- how cross-module references resolve inside a cycle without circulating
  computed digests;
- what initialization, inference, and separate compilation mean across
  cycles;
- what the sanctioned alternative is when a cycle is not semantically
  necessary; and
- stable diagnostics for every rejection the design still contains.

The answer must compose with C022's digest-bound imports, C002's
intra-module recursion, C010's module-level loading semantics, and
C008's digest-addressed caches without amending them outside cycles.

## Working hypotheses

- Module recursion exists: each maximal strongly-connected component is
  one checking and caching unit.
- Inside an SCC, cross-module references resolve against members'
  declared export signatures — already mandatory in the retained AST and
  typed core — so no digests circulate within the component; across SCC
  boundaries, imports stay digest-bound exactly as C022 fixed them; the
  whole SCC receives one joint digest.
- Initialization is definition-only with per-SCC loading and no
  top-level evaluation; inference checks each member against declared
  signatures inside the SCC and digests outside; the SCC is the atomic
  cache unit, so rebuilding any member rebuilds its SCC.
- The normative alternative to convenience cycles is dependency
  inversion: take the collaborator as a higher-order value.
- A single stable `CYC001` reports SCC-internal violations — regime
  mixing and signature gaps — at the closing event, transactionally.

## Paths to explore

- [Haskell 2010 mutually-recursive-module findings](../30-sources/marlow-2010-haskell-language-report.md)
  supply the adopted alternative and its stated price: explicit
  signatures on exported values, group-level compilation.
- [The SML Definition](../30-sources/milner-et-al-1997-definition-standard-ml.md)
  and [Erlang/OTP modules](../30-sources/erlang-otp-modules-and-code-loading.md)
  supply the non-recursive-structure and acyclic-loading contrasts.
- [The C010 kernel](../60-specification/formal-semantic-kernel/canonical-kernel-syntax.md)
  fixes the digest-bound import form whose circularity motivates the
  signature regime.
- [Import Declarations and Admission](../60-specification/imports-and-exports/import-declarations-and-admission.md)
  fixes the cross-SCC regime cycles must leave unchanged.

## Findings

- Haskell's chapter 5 makes mutual recursion a specified module feature
  and its section 5.7 names the exact cost Catena must pay: exported
  values need explicit signatures and the compilation unit grows to the
  recursive group. Catena's retained AST already demands signatures, so
  the marginal price is the SCC unit itself.
- BEAM modules have no top-level evaluation: loading is the only
  initialization, which makes per-SCC loading a small, well-founded rule
  rather than an initialization-order problem like strict-language
  module systems face.
- The digest model is only impossible *inside* a cycle; keeping digests
  at SCC boundaries preserves every C008 cache and C022 validation rule
  unchanged for acyclic graphs, which become degenerate one-module SCCs.
- The synthesis
  [Catena Dependency Cycles](../20-notes/catena-dependency-cycles.md)
  develops the full model and falsification criteria; the
  [topic map](../10-maps/module-dependency-cycles.md) routes the
  evidence.

## Outcome

Open. Resolution requires candidate normative chapters admitting SCCs
with their resolution regimes and consequences; a sibling compiler with
abstract-event SCC grouping and a real cross-module SCC compilation path
with joint digest, tagged executable evidence; and the C013–C023
promotion workflow.
