---
title: "How Should Catena Draw Its Abstraction Boundaries?"
kind: inquiry
created: "2026-08-23"
status: resolved
tags:
  - catena
  - abstraction
  - language-design
  - modules
aliases:
  - "Catena abstraction inquiry"
---

# How Should Catena Draw Its Abstraction Boundaries?

## Why this matters

C002 made module boundaries representation-free: transparent constructor
export and fully abstract type export both hide the runtime layout, and
C022 fixed the export-event vocabulary that names those two modes. Two
sub-questions of the abstraction boundary remain open: whether any
datatype can opt into a stable observable layout, and whether construction
and matching authority can ever be split. Until both are answered,
implementations could disagree about whether a compact/uniform choice is
ABI, whether a client may destructure what it can build, and what the
sanctioned pattern for datatype invariants is — disagreements that would
leak into G028 compatibility policy, P093 representation mapping, and
every library that needs invariant-bearing types.

## Operational question

Decide, for edition 0.1:

- whether any stable-layout opt-in exists, and if not, who owns any
  future layout-stability contract;
- whether the binary transparent/abstract authority vocabulary is
  complete, and if so, what the sanctioned invariant idiom is and what
  its coverage consequences are; and
- which future owners (G028, D046, G040, P093, G094, G095) hold the
  excluded capabilities.

The answer must preserve C002's interface contract, C022's export-event
enum, both-layout conformance, and `L001`'s classification unchanged.

## Working hypotheses

- No stable-layout opt-in exists in edition 0.1: representation
  independence stays absolute, both-layout conformance stays mandatory,
  and any future layout-stability contract belongs to the G028
  ABI/compatibility slice together with the foreign boundaries.
- The binary transparent/abstract vocabulary is complete: constructors
  are construct-and-match together or hidden entirely.
- The Result-returning smart-constructor-over-abstract-type pattern is
  the sanctioned invariant idiom, with wildcard-plus-observers as the
  client-side coverage consequence.
- Selective construction/matching authority and views remain declared
  future work owned by D046/G040.

## Paths to explore

- [Interfaces and Representation](../60-specification/data-and-patterns/interfaces-and-representation.md)
  fixes the layout-free contract and anticipates an explicit future
  schema contract.
- [Export Declarations and Visibility](../60-specification/imports-and-exports/export-declarations-and-visibility.md)
  fixes the transparency enum the boundary rides on.
- [Algebraic Data Types](../20-notes/algebraic-data-types.md) frames
  smart constructors as the first invariant tool and views as deferred.
- [Leroy 1992](../30-sources/leroy-1992-unboxed-objects.md) and the
  [SML Definition](../30-sources/milner-et-al-1997-definition-standard-ml.md)
  supply the representation-independence and signature-abstraction
  precedents.

## Findings

- C002's own closing boundary already states that version 0.1.2 promises
  source representation independence, not stable ABI, and that a stable
  external schema requires an explicit future contract — the exclusion
  is consolidation of shipped intent, not a new decision.
- The ADT synthesis pre-answered the authority split: admitting selective
  exposure would force signature-level construction/matching distinction
  and a coverage remainder for unseen constructors; smart constructors
  over abstract types deliver invariants without any of that surface.
- The compiler already proves the load-bearing half: abstract types hide
  constructors through digest-bound interfaces in the C002 executable
  corpus, and C022 validates the transparency enum exactly.
- The synthesis
  [Catena Abstraction Boundaries](../20-notes/catena-abstraction-boundaries.md)
  develops the model and falsification criteria; the
  [topic map](../10-maps/abstraction-boundaries.md) routes the evidence.

## Outcome

Resolved as C023 and source-only language revision `0.1.19`. Catena
confirms the transparent/abstract pair as the complete
constructor-authority vocabulary with no stable-layout form on any
frontend (both-layout conformance mandatory, `L001` unchanged, G028
owning any future layout-stability contract); excludes selective
construction/matching authority and views as declared future work owned
by D046/G040; and sanctions the abstract-type-plus
validating-constructor-plus-observer invariant idiom with typed failure
and wildcard-plus-observers coverage. The rules are defined in the
[normative abstraction specification](../60-specification/abstraction-boundaries/README.md).

P023 is complete through the
[abstraction synthesis](../20-notes/catena-abstraction-boundaries.md),
[topic map](../10-maps/abstraction-boundaries.md), and
[C023 evidence record](../50-journal/2026-08-23-c023-abstraction-boundaries.md).
G028 retains any ABI or layout-stability contract; D046/G040 retain views
and selective exposure; P093 retains BEAM representation mapping under
non-observability; G095 retains foreign-term validation.
