---
title: "Catena Dependency Cycles"
kind: note
created: "2026-08-24"
maturity: developing
tags:
  - catena
  - language-design
  - modules
  - separate-compilation
aliases:
  - "Catena module cycles model"
---

# Catena Dependency Cycles

## Executive conclusion

Module dependency cycles should be admitted, and the strongly-connected
component should be the unit that pays for them. Each maximal SCC of the
module import graph is one checking and caching unit: inside it,
cross-module references resolve against members' declared export
signatures — which the retained AST and typed core already require — so
no computed digests circulate within the component; across SCC
boundaries, imports stay digest-bound exactly as C022 fixed them; and the
whole SCC receives one joint digest over its members' interfaces.
Acyclic graphs are degenerate one-module SCCs and behave byte-identically
to C022.

The consequences the checklist names fall out as confirmations:
initialization is definition-only — BEAM modules have no top-level
evaluation, so loading per SCC is the whole story and no intra-SCC
initialization order exists; inference checks each member against
declared signatures inside the SCC and digest-bound interfaces outside,
with C001/C002 machinery unchanged; separate compilation caches are
digest-addressed SCC units, so rebuilding any member rebuilds and
re-digests its SCC.

One stable `CYC001` reports the two violations the design still
contains, at the event that closes them: presenting a digest-bound import
for a module inside one's own SCC (regime mixing), and exporting an
SCC-participating name without the declared signature intra-SCC
resolution needs. And the normative alternative to convenience cycles is
dependency inversion — taking the collaborator as a higher-order value —
recorded so SCCs remain for genuine mutual definition.

This closes G024 without deciding G025's package assembly (which
receives SCC units as inputs), P109's concrete `use` punctuation, or any
pre-declared standalone interface file format, which is the declined
alternative.

## Scope and method

The operational target is independent agreement on cycle admission, the
SCC unit, the two resolution regimes, the three consequence clauses, the
inversion alternative, and the remaining rejections — made executable
both at the abstract-event layer (SCC grouping in the environment
builder) and on the real compiler path (a genuine cross-module SCC
compiling and executing with a joint digest). Primary comparative
evidence comes from the expanded
[Haskell 2010 recursion findings](../30-sources/marlow-2010-haskell-language-report.md),
with [SML](../30-sources/milner-et-al-1997-definition-standard-ml.md) and
[Erlang](../30-sources/erlang-otp-modules-and-code-loading.md) as the
contrasts. Source claims stay distinct from Catena proposals below.

## Relation to the current corpus

[C022's import model](../60-specification/imports-and-exports/import-declarations-and-admission.md)
fixes digest-bound admission whose circularity is precisely what an SCC
must not attempt: the digest of A embeds A's interface, which checking B
against A requires before A exists. C022 also already classifies a known
module as "one whose export set and digest the resolution context holds;
how contexts acquire modules ... remains G025/G121" — the SCC is the
context-level grouping that answer anticipated.

[C002's recursive groups](../60-specification/data-and-patterns/declarations-and-nominal-identity.md)
make value-level mutual recursion ordinary inside a module; nothing in
this design touches them. The
[retained JSON AST](../60-specification/type-system/diagnostics-and-conformance.md)
requires an explicit signature on every definition — the property
Haskell's report says mutual recursion demands — and the typed core
carries those signatures, so intra-SCC resolution against declared
signatures is a reading of shipped machinery, not new semantics.

[C010's loading semantics](../60-specification/formal-semantic-kernel/canonical-kernel-syntax.md)
fix modules as definition collections with no top-level evaluation, and
[C008's caches](../60-specification/editions-and-feature-lifecycle/README.md)
are digest-addressed — the SCC becomes simply a coarser address.

## Comparative evidence and inference

### Haskell: recursion as a specified feature, with the price named

Haskell's chapter 5 states modules may be mutually recursive and that
this lets programs be partitioned freely; its section 5.7 concedes that
separate compilation of cycles requires additional information in
imported modules and that explicit signatures for all exported values may
be necessary, leaving precise details to implementations. The inference:
admitting cycles is a language decision with a known, payable cost, not
an implementation accident. Catena pays it by making the SCC the unit
and signatures the currency — and, unlike the report, defines the
separate-compilation details rather than deferring them.

### Standard ML and Erlang: the contrasts

SML structures are not recursively bindable: mutual reference across
structures requires functors or restructuring — the inversion idiom as a
whole language discipline. Erlang's compile-time dependencies are
acyclic, and recursion is achieved by message passing between processes —
inversion at runtime. Both show the DAG-plus-inversion life is livable;
neither shows cycles are impossible to do well. Catena takes Haskell's
side for genuine mutual definition while making inversion the normative
recommendation.

### The digest impossibility, precisely

A C022 import binds the consumer's check to the producer's *computed*
digest. In a cycle, each producer's digest depends on an interface that
references the other's not-yet-computed digest-bearing interface. The two
escapes are pre-declaration (invent a standalone signature-file format
and digest domain — P109/G025 territory) and grouping (compute each
member's interface from declared signatures, then digest the group).
Grouping requires no new format, reuses mandatory signatures, and leaves
acyclic behavior identical — which is why it is selected.

## Selected model

### Admission and the unit

A module import graph may contain cycles. The maximal strongly-connected
components partition the graph; each SCC — including a single-module
component — is the unit of checking, resolution, and caching. Cycle
shape (self-loop, pair, longer ring) carries no separate rules.

### The two regimes

*Intra-SCC*: a reference from one member to another resolves against the
companion's declared export signatures. An intra-SCC import event MUST
present an empty digest; presenting a digest for a companion is regime
mixing — `CYC001` at that event. An SCC participant MUST declare the
signature of every name it exports for intra-SCC resolution; a gap is
`CYC001` at the event that closes the component. No computed digest
exists per member until the component finishes checking.

*Cross-SCC*: imports of modules outside one's SCC stay digest-bound and
C022-validated, byte-for-byte. The SCC's joint digest is a deterministic
hash over the sorted member names and each member's computed interface
digest; consumers outside import against member interfaces exactly as
before, with the joint digest binding the component as one cache and
compatibility unit.

### The three consequences

Initialization: modules contribute definitions only; there is no
top-level evaluation, so no intra-SCC initialization order exists;
loading happens per SCC. Inference: one checking treatment per SCC — each
member checked against companions' declared signatures and outside
digests — with no joint inference across members; C001/C002 machinery
unchanged. Separate compilation: caches are digest-addressed SCC units;
rebuilding any member rebuilds and re-digests the whole SCC; an acyclic
rebuild is the degenerate case and behaves exactly as C008 fixed.

### The inversion alternative

When a cycle is convenience rather than genuine mutual definition, the
sanctioned restructuring is dependency inversion: the reusable module
takes the collaborator as an explicit higher-order value
(`serve : (Request -> Reply) -> Config -> ...`), leaving the graph a
DAG. SCC admission is for mutual *definition*; inversion is the
recommended tool for mutual *use*.

### Rejection

Both `CYC001` reasons fail at the event that closes the violation,
transactionally, with the offending edge or member in the details. No
cycle shape is itself an error.

## Rejected alternatives

- **Acyclic exclusion:** digest-native and cheapest, but declines a
  specified, payable feature the evidence supports and forces inversion
  everywhere.
- **Pre-declared interface files:** uniform, but invents a signature-file
  format and digest domain squarely inside P109/G025's undesigned
  territory.
- **Fixpoint digests:** embeds each member's digest in the others';
  requires defining canonical fixpoint iteration — fragile and unlike
  anything in the corpus.
- **Bounded cycles:** arbitrary magic numbers with no semantic
  motivation.
- **Joint inference across SCC members:** would couple C001 solving
  across modules for no need — signatures already separate the checks.

## What C024 adds to the design

Multi-module programs can be partitioned by problem shape rather than
dependency fear, while every acyclic guarantee stays untouched: G025
receives SCC units as its assembly input, P109 receives the semantics its
recursive `use` groups must elaborate, and the standard library can
define genuinely mutually recursive clusters with a documented joint
compatibility boundary.

## Remaining questions and falsification criteria

G025 must assemble packages over SCC units and define lockfile
representation of joint digests; P109 must fix the concrete surface for
SCC groups; G028 must treat the joint digest as a compatibility boundary;
the deferred pre-declared-interface alternative remains available to a
future revision if SCC units prove too coarse.

The model should be revisited if real SCCs show re-digestion costs that
materially damage build performance, if signature-gap diagnostics prove
too weak to repair cyclic groups, or if G028's ABI work needs per-member
stability inside an SCC — none of which the corpus currently evidences.

## Connections

- The [open cycles inquiry](../40-inquiries/how-should-catena-handle-module-dependency-cycles.md)
  records the operational question and evidence trail.
- The [Module Dependency Cycles map](../10-maps/module-dependency-cycles.md)
  routes through evidence, regimes, and remaining owners.
- [Catena Imports and Exports](catena-imports-and-exports.md) fixes the
  cross-SCC regime cycles leave unchanged.
- [Catena Files and Modules](catena-files-and-modules.md) fixes the flat
  module names the graph is over.

## Sources

- [Haskell 2010 Language Report](../30-sources/marlow-2010-haskell-language-report.md)
- [The Definition of Standard ML (Revised)](../30-sources/milner-et-al-1997-definition-standard-ml.md)
- [Erlang/OTP Modules and Code Loading](../30-sources/erlang-otp-modules-and-code-loading.md)
- [Canonical Kernel Syntax](../60-specification/formal-semantic-kernel/canonical-kernel-syntax.md)
- [Import Declarations and Admission](../60-specification/imports-and-exports/import-declarations-and-admission.md)
