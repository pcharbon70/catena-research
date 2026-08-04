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
0.1.6 profile erases claims, verification definitions, and build-time policy
before BEAM code generation. A signed sidecar manifest preserves provenance;
runtime monitors are deliberately deferred rather than silently retained.

The topic is a fresh language-design investigation grounded in independent
primary work on contracts, verification, models, semantics, typestate,
authorization, provenance, and proof certificates.

## Start here

- [Catena 0.1.6 Specification and Governance Specification](../60-specification/specifications-and-governance/README.md)
  freezes the bounded normative contract: semantic JSON forms,
  typed rules and examples, additive policy, offline Ed25519 roots,
  hash-chained lifecycle, staged package output, and complete BEAM erasure.
- [C006 Executable Specification and Governance Conformance](../50-journal/2026-08-03-c006-executable-specification-governance-conformance.md)
  records the authorized historical compiler identity, exact environment,
  independent-oracle and adversarial results, erasure evidence, and artifact
  digests that promoted the C006 semantics under the retired identifier. The
  [renumbering record](../50-journal/2026-08-04-prototype-slice-renumbering.md)
  owns the fresh `0.1.6` protocol-evidence gate.
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

### Canonical bytes, signatures, and root continuity

[RFC 8785](../30-sources/rundgren-et-al-2020-json-canonicalization-scheme.md)
defines reproducible JSON bytes and rejects ambiguous input such as duplicate
object names. [RFC 8032](../30-sources/josefsson-liusvaara-2017-eddsa.md)
supplies Ed25519 algorithms and independent vectors. The
[Update Framework specification](../30-sources/the-update-framework-specification.md)
shows why distinct-key thresholds and old-plus-new authorization are necessary
for a continuous root rotation.

Catena 0.1.6 combines these only as a bounded offline protocol. Canonical bytes
and signatures bind statements; policy and lifecycle rules decide whether
their signers have authority for the exact action.

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
tracks the full workbench. Normative 0.1.6 answers the bounded core-calculus,
digest, offline-root, action-gate, and total-erasure questions. The hardest
remaining questions are:

- Which public parser syntax best exposes the fixed semantic forms?
- Which local development actions remain available when publication or
  activation evidence is incomplete?
- What erasure theorem and performance evidence generalize beyond the 0.1.6
  byte-identity and artifact-inspection checks?
- How do contracts wrap handlers, resumptions, callbacks, and process
  messages?
- Can one IR serve executable, bounded, temporal, and deductive claims without
  erasing their meanings?
- How should cross-organization identity, archived evidence, transparency,
  schema migration, and future-compiler interpretation extend the offline 0.1.6
  protocol?
- Which certificates can a small kernel recheck, and which external producers
  remain explicitly trusted?
- Can ordinary programmers distinguish all evidence kinds and repair
  governance failures from the default diagnostics?
- Does language integration remain simpler than a stable language IR consumed
  by a separately deployed governance protocol?

The map should remain open until generalized formal semantics, representative
performance evaluation, long-term protocol evolution, and a vocabulary study
provide evidence beyond the bounded reference evaluator, implementation, and
adversarial corpus recorded for 0.1.6.
