---
title: "Language-Integrated Specifications and Governance"
kind: map
created: "2026-08-01"
tags:
  - catena
  - formal-methods
  - governance
  - language-design
  - specification
aliases:
  - "Specification governance map"
  - "Governed language specifications"
---

# Language-Integrated Specifications and Governance

## Scope

This map routes through the design of specifications, evidence, authority, and
lifecycle as connected Catena language features. The central distinction is
that technical support, authorization, and historical provenance answer
different questions and must never collapse into one “verified” status.

Adoption is optional for a project, while the semantics of every declaration
and the gates on every explicitly governed action are mandatory. Missing
release evidence may leave draft work possible, but cannot produce a governed
release. Coverage does not spread to unrelated modules or dependencies without
an explicit policy or interface obligation.

Language integration also does not imply runtime retention. The recommended
default erases claims, proofs, ghost values, generators, and build-time policy
before BEAM code generation. A signed sidecar manifest preserves provenance;
the BEAM artifact retains only monitors or admission hooks that an explicit
profile still requires.

The topic is a fresh language-design investigation grounded in independent
primary work on contracts, verification, models, semantics, typestate,
authorization, provenance, and proof certificates.

## Start here

- [Language-Integrated Specifications and Governance](../20-notes/language-integrated-specifications-and-governance.md)
  is the main synthesis. It proposes the typed specification graph, claim and
  evidence taxonomy, restricted policy language, transition history, trust
  model, compiler pipeline, BEAM boundary, staged implementation, and
  falsification criteria.
- [How should Catena integrate specifications and governance into the language?](../40-inquiries/how-should-catena-integrate-specifications-and-governance-into-the-language.md)
  turns the proposal into semantic, security, usability, performance, and
  implementation experiments.
- [An Approachable Vocabulary for Catena](../20-notes/approachable-language-vocabulary.md)
  explains why public terms and diagnostics should describe behavior and
  repair without making formal terminology a prerequisite.

## Trails

### From interface promises to higher-order monitoring

Begin with [Applying Design by Contract](../30-sources/meyer-1992-applying-design-by-contract.md)
for caller needs, implementation promises, invariants, and responsibility at a
component boundary. Continue to
[Contracts for Higher-Order Functions](../30-sources/findler-felleisen-2002-contracts-higher-order-functions.md)
for delayed checks, wrappers, callbacks, and blame when functions cross the
boundary.

This trail informs Catena's local `needs`,
`promises`, and `invariant` claims. It leaves
effect-handler, resumption, process, and tail-behavior monitoring open.

### From claims to executable counterexample search

[QuickCheck](../30-sources/claessen-hughes-2000-quickcheck.md) shows how typed
properties, generators, distributions, and counterexamples turn a general
claim into many finite challenges.
[Alloy](../30-sources/jackson-2002-alloy.md) provides exhaustive search within
an explicit finite relational scope.

Together they support approachable, useful evidence while forbidding the word
“proof” for successful finite runs. Generator coverage, sample counts, and
model bounds belong in the evidence type.

### From local state to concurrent histories

[Typestate](../30-sources/strom-yemini-1986-typestate.md) makes permitted
operations depend on a value's current lifecycle state.
[The Temporal Logic of Actions](../30-sources/lamport-1994-temporal-logic-actions.md)
extends the view from individual state transitions to safety, liveness,
fairness, and refinement over concurrent behavior.

This trail motivates typed proposal transitions and temporal claims such as
“activation never precedes mandatory evidence” and “revoked authority cannot
approve a later event.”

### From annotations to deductive obligations

[Dafny](../30-sources/leino-2010-dafny.md) integrates contracts, frames,
invariants, termination, ghost state, and automated proof obligations in a
programming language.
[Proof-Carrying Code](../30-sources/necula-1997-proof-carrying-code.md)
separates expensive proof production from a smaller consumer-side checker.

The Catena route should expose proof assumptions and semantic digests, prefer
portable certificates where practical, and keep solvers outside the trusted
base when their results can be rechecked.

### One language meaning for many tools

[An Overview of the K Semantic Framework](../30-sources/rosu-serbanuta-2010-k-semantic-framework.md)
shows how an executable semantic definition can support parsing,
interpretation, state exploration, and analysis.

This is the route to a versioned specification IR and reference semantics
shared by the compiler, evidence runner, documentation generator, policy
evaluator, and transition validator. A shared semantics reduces drift but does
not prove that the semantics itself is correct.

### From checked specifications to erased BEAM code

The [main synthesis](../20-notes/language-integrated-specifications-and-governance.md#erasure-and-output-artifacts)
separates verification IR from runtime IR. Well-formedness, static proof, and
trusted assumption are different compiler decisions: only a discharged claim
or explicit assumption can remove a required monitor. Proofs, ghost state,
generators, policies, and evidence move to a signed sidecar manifest rather
than executable instructions.

This trail connects [Dafny](../30-sources/leino-2010-dafny.md), which keeps
verification-only material distinct from runtime state, with
[Proof-Carrying Code](../30-sources/necula-1997-proof-carrying-code.md), which
separates producer evidence from consumer checking. Catena still needs its own
type-, effect-, and semantics-preserving erasure theorem and BEAM artifact
measurements.

### Authority is not correctness

[Cedar](../30-sources/cutler-et-al-2024-cedar.md) provides the policy-language
trail: authorization logic can be readable, fast, restricted, optionally
validated, and precisely analyzable when it is not hidden in arbitrary
application control flow.

Catena governance should ask whether an actor may perform an action over a
resource under a context. It must not reinterpret an authorization decision as
technical evidence.

### Signed process evidence is not truth

[in-toto](../30-sources/torres-arias-et-al-2019-in-toto.md) separates a signed
normative process layout from signed observations of performed steps and binds
materials, products, actors, and thresholds.
[Proof-Carrying Code](../30-sources/necula-1997-proof-carrying-code.md)
provides the stronger case in which the receiver can recheck a supplied
witness.

This trail divides external evidence into:

- recheckable certificates;
- reproducible observations;
- accepted signed attestations; and
- human approvals.

Each retains its own trust boundary.

### Connections to the rest of Catena

- [Catena Type-System Design](catena-type-system-design.md) constrains how
  claims elaborate without losing principality, coherence, or effect safety.
- [Algebraic Data Types](algebraic-data-types.md) supplies invariants,
  exhaustive finite cases, generated data, shrinkers, and schema evolution.
- [Algebraic Effects and Handlers](algebraic-effects-and-handlers.md) supplies
  explicit capabilities, handler obligations, resumptions, and trace subjects.
- [Category Theory for Programming](category-theory-for-programming.md)
  supplies law-bearing capability declarations whose evidence must remain
  explicit.
- [Combinators for Algebraic Data and Categorical Programming](combinators-for-algebraic-data-and-categorical-programming.md)
  supplies law, traversal, effect, strictness, and cost claims.
- [Approachable Catena Language Design](approachable-catena-language-design.md)
  supplies the public-vocabulary and diagnostic test route.

## Open questions

The active
[specification and governance inquiry](../40-inquiries/how-should-catena-integrate-specifications-and-governance-into-the-language.md)
tracks the full workbench. The hardest unresolved questions are:

- What is the smallest claim/evidence/policy/transition calculus?
- Which syntax makes project, module, interface, action, and release-profile
  coverage explicit without burdening projects that declare no governance?
- Which local development actions remain available when publication or
  activation evidence is incomplete?
- Which constructs are always erased, which profiles retain monitors, and what
  theorem connects verification IR to emitted BEAM behavior?
- Should a production BEAM file contain no specification metadata at all, or
  an optional non-executable manifest digest under an explicit profile?
- How should the compiler demonstrate zero runtime cost for fully discharged
  claims and account for every retained check?
- Which specification expressions are total and pure by construction?
- How should semantic digests respond to refactoring and abstraction?
- How do contracts wrap handlers, resumptions, callbacks, and process
  messages?
- Can one IR serve executable, bounded, temporal, and deductive claims without
  erasing their meanings?
- What authorization rules are expressive enough while remaining total,
  analyzable, and explainable?
- How are root policy, recovery, identity, revocation, and event ordering
  established across organizations?
- Which certificates can a small kernel recheck, and which external producers
  remain explicitly trusted?
- Can ordinary programmers distinguish all evidence kinds and repair
  governance failures from the default diagnostics?
- Does language integration remain simpler than a stable language IR consumed
  by a separately deployed governance protocol?

The map should remain open until a reference semantics, prototype, adversarial
model, performance evaluation, and vocabulary study provide evidence beyond
the current synthesis.
