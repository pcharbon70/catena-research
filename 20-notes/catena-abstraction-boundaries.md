---
title: "Catena Abstraction Boundaries"
kind: note
created: "2026-08-23"
maturity: developing
tags:
  - abstraction
  - catena
  - language-design
  - modules
aliases:
  - "Catena abstraction model"
---

# Catena Abstraction Boundaries

## Executive conclusion

Edition 0.1 should draw the abstraction boundary in one straight line:
representation is never observable, and authority over constructors is
never split. No stable-layout opt-in exists — a datatype's uniform or
compact representation stays an implementation freedom checked by
both-layout conformance, and any future layout-stability contract belongs
to the ABI/compatibility slice (G028) together with the foreign
boundaries it would serve. The transparent/abstract pair remains the
complete authority vocabulary: constructors are exported for construction
and matching together, or hidden entirely.

The sanctioned tool for datatype invariants is the pattern the corpus has
converged on all along: export the type abstract, export validating
constructor functions whose failure is visible in their result type, and
export observers. Clients hold abstract values opaquely, reach their
contents only through the observers, and satisfy coverage with a
wildcard remainder. Selective construction-only or matching-only
authority, and views that translate hidden representations into public
constructor shapes, stay declared future work with named owners.

This closes P023 with confirmations of shipped rules plus one blessed
idiom — no acceptance change, no new diagnostics, no amendments to C002
or C022.

## Scope and method

The operational target is independent agreement that the two open
sub-questions have exactly the declared answers, that the answers are
already implied by the normative corpus, and that the invariant idiom is
sanctioned with its coverage consequence stated. The evidence base is the
existing corpus: [Leroy 1992](../30-sources/leroy-1992-unboxed-objects.md)
on representation independence versus specialization, the
[SML Definition](../30-sources/milner-et-al-1997-definition-standard-ml.md)
on signature-controlled abstraction, the
[ADT synthesis](algebraic-data-types.md) on smart constructors and views,
and the shipped [C002](../60-specification/data-and-patterns/interfaces-and-representation.md)
and [C022](../60-specification/imports-and-exports/export-declarations-and-visibility.md)
contracts.

## Relation to the current corpus

C002 fixes the load-bearing rule: an interface MUST NOT expose a
datatype's chosen runtime layout; layout selection happens after typed
core; compact is production default and uniform the reference; conformance
programs check and execute under both; `L001` classifies layout coercion
as implementation failure. Its closing boundary — "promises source
representation independence, not stable ABI or wire compatibility. A
stable external schema requires an explicit future contract" — is the
sentence this slice completes by naming the owner.

C022 fixes the vocabulary: export events for types carry exactly
`transparent` or `abstract`, and anything else is `EXP001`. The
construction/matching question therefore has a shipped two-element answer
space; this slice declares it complete rather than extending it.

The [ADT synthesis](algebraic-data-types.md) already separates
abstraction, programmable matching, and stable layout as distinct
features; names smart constructors as the first invariant tool — a plain
`type Email = Email String` wrapper "does not itself ensure validity if
`Email` remains publicly constructible" — and lists the questions views
must answer before admission. The [greenfield type-system
synthesis](catena-greenfield-type-system.md) records that constructor
export controls matching authority in the nominal design.

## Comparative evidence and inference

### SML: abstype's lesson, signatures' technique

Standard ML's `abstype` and its signature system demonstrate both halves:
abstraction delivered through signatures is a mature, checkable boundary,
and the language once needed a dedicated abstype construct only because
its default export story was less disciplined. Catena's private-by-default
exports (C022) plus abstract type export deliver the same boundary without
a second construct. The inference: nothing about invariant-bearing types
requires new machinery — it requires using the shipped machinery.

### Leroy: independence versus stability

Leroy's unboxed-objects analysis shows representation choice is an
optimization freedom that uniform-representation boundaries protect, and
that making a representation observable converts an optimization into a
compatibility surface. The inference for the stable-layout question: an
opt-in is not a small feature but a contract class of its own — exactly
why G028 should own it, with P093/G094/G095 as its consumers, rather than
a per-datatype attribute riding on export declarations.

### The synthesis corpus: smart constructors over authority splits

The ADT synthesis's argument is decisive for the authority question:
splitting construction from matching forces the signature language to
distinguish the two, forces coverage to treat unseen constructors as an
unknown remainder, and duplicates what abstract-plus-smart-constructors
already delivers — validating construction with typed failure, and
matching mediated by exported observers. Selective exposure buys nothing
until views (with their own totality, cost, and completeness questions)
are designed.

## Selected model

### The boundary, in three sentences

1. Representation is never observable in edition 0.1; both-layout
   conformance is mandatory; `L001` remains the classification for layout
   coercion; a future layout-stability contract is G028's with the
   foreign boundaries as consumers.
2. Constructor authority is exactly the C022 transparency pair:
   transparent exports construction and matching together; abstract hides
   both.
3. Invariants are built with abstract types plus validating constructor
   functions returning typed failures, plus observers; clients satisfy
   coverage with a wildcard remainder under C002's coverage rules.

### The sanctioned idiom

```text
export type Email                       -- abstract
export parse : String -> Result EmailError Email
export domain : Email -> String
```

`parse` validates before producing an `Email`; the `Result` return makes
failure explicit and typed; `domain` is the observer through which
clients read. No client can construct or destructure an `Email` by
spelling — only by `parse`. The wrapper-with-public-constructor
anti-pattern is rejected by construction.

### What the idiom promises and costs

Promises: invariant holds by typing, not convention; failure is in the
type; the representation may change freely (representation independence
is what makes refactoring safe). Cost: pattern matching on abstract
values is unavailable by design — observers plus wildcard are the
client's vocabulary, and coverage treats the unseen as an unknown
remainder per C002.

## Rejected alternatives

- **Stable layout opt-in now:** converts an optimization freedom into an
  ABI surface before G028/G095 exist to govern it; contradicts C002's
  stated intent.
- **Construction-only authority:** half of a views system without its
  checks; changes coverage semantics; extends the just-shipped C022 enum
  for no demonstrated need.
- **Matching-only authority (views now):** admits representation
  translation with totality, cost, and disjointness unanswered — the
  corpus's own deferral questions stand.
- **`non_exhaustive` markers:** C002 already assigns evolving APIs to
  abstract export with observers; a marker adds a second evolution
  mechanism.
- **Trusting wrapper types:** public constructors make wrapper
  "invariants" advisory; the synthesis already rejects this.

## What C023 adds to the design

The boundary becomes auditable: a reviewer can point at a stable-layout
spelling and know it is not Catena, at a construction-only export and
know it is not Catena, and at an invariant-bearing type and know the
idiom it should follow. G028 receives an unambiguous starting rule —
representation is currently non-observable, and any ABI slice starts by
deciding when that stops being true — and the standard library (G101+)
receives its invariant pattern pre-approved.

## Remaining questions and falsification criteria

G028 must design any layout-stability or ABI contract; D046/G040 must
design views or pattern-level selective exposure if ever admitted; P093
must map representations to BEAM under the same non-observability; G095
must keep foreign terms from becoming typed values by shape.

The model should be revisited if G028's ABI work cannot proceed without
per-datatype layout opt-in (then G028 extends the vocabulary with its own
lifecycle record), or if a demonstrated library need shows observers
cannot express a decomposition views could — that would reopen D046, not
this slice.

## Connections

- The [resolved abstraction inquiry](../40-inquiries/how-should-catena-draw-its-abstraction-boundaries.md)
  records the operational question and evidence trail.
- The [Abstraction Boundaries map](../10-maps/abstraction-boundaries.md)
  routes through the shipped contracts and remaining owners.
- The [Abstraction Boundaries Specification](../60-specification/abstraction-boundaries/README.md)
  defines the normative 0.1.19 contract.
- The [C023 evidence record](../50-journal/2026-08-23-c023-abstraction-boundaries.md)
  records the sibling implementation and verification.
- [Algebraic Data Types](algebraic-data-types.md) supplies the
  smart-constructor and views framing this slice canonizes.
- [Catena Imports and Exports](catena-imports-and-exports.md) fixes the
  transparency vocabulary confirmed complete here.

## Sources

- [Unboxed Objects and Polymorphic Typing](../30-sources/leroy-1992-unboxed-objects.md)
- [The Definition of Standard ML (Revised)](../30-sources/milner-et-al-1997-definition-standard-ml.md)
- [Interfaces and Representation](../60-specification/data-and-patterns/interfaces-and-representation.md)
- [Export Declarations and Visibility](../60-specification/imports-and-exports/export-declarations-and-visibility.md)
