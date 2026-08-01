---
title: "How Should Catena Integrate Specifications and Governance Into the Language?"
kind: inquiry
created: "2026-08-01"
status: open
tags:
  - catena
  - formal-methods
  - governance
  - language-design
  - specification
aliases:
  - "How should Catena govern language specifications?"
  - "Language-integrated specification inquiry"
---

# How Should Catena Integrate Specifications and Governance Into the Language?

## Why this matters

Catena needs a way to state more than types. Functions have behavioral
obligations, categorical capabilities have laws, datatypes have invariants,
effects have protocols, concurrent actors have temporal guarantees, and public
language features have compatibility and acceptance decisions.

Leaving these claims in prose separates them from implementations and makes
their evidence difficult to audit. Treating all evidence as a Boolean
“verified” result is worse: tests, finite model searches, proofs, signed build
records, and approvals justify different conclusions.

The language also needs governance without confusing technical truth with
organizational authority. A proof cannot appoint a release owner, an approval
cannot prove a law, and a signature cannot make a false observation true.

## Operational question

The inquiry is:

> Can Catena define a typed specification graph, evidence model, authorization
> policy, and lifecycle protocol that preserve the exact meaning and trust
> boundary of every claim while remaining usable in ordinary functional
> programs?

A satisfactory answer requires a prototype in which:

1. a project with no declarations remains an ordinary Catena project;
2. every declared specification is checked and every governed scope is
   explicit;
3. unmet gates block the governed action without silently governing unrelated
   work;
4. claims resolve to typed language subjects and survive safe source movement;
5. each evidence method has an exact success meaning, scope, and trusted base;
6. ordinary type inference and effect checking remain predictable;
7. higher-order and effectful boundaries allocate obligations correctly;
8. finite testing and modeling cannot be mistaken for deductive proof;
9. external evidence is cryptographically bound to the exact claim and
   artifact;
10. authority policy is deterministic, terminating, explainable, and
   analyzable;
11. invalid, stale, unauthorized, and out-of-order transitions are rejected;
12. current governed state can be replayed from immutable history;
13. policy replacement and emergency recovery have explicit trust roots; and
14. programmers can understand diagnostics without formal-methods vocabulary.

## Working hypotheses

### H0: adoption is optional and enforcement is scoped

Catena projects should not need governance declarations to compile ordinary
programs. Every declaration is still type-checked, and every artifact or action
placed under policy is enforced without an informal bypass. Missing evidence
may leave a draft locally buildable while blocking publication or activation.
Governance reaches other modules and dependencies only through an explicit
coverage rule or interface obligation.

### H1: one graph can connect several honest evidence regimes

Claims should be independent of the method used to support them. A rule may be
challenged by examples, generated properties, a bounded model, or a deductive
proof, but the result type must retain which method ran. One graph can connect
these records without coercing them into one confidence scale.

### H2: the compiler should own semantics and linking, not every observation

The compiler should own claim elaboration, name and type resolution, pure
checking, policy semantics, and transition validation. External tools can
produce signed evidence envelopes. A producer result is admitted only under
policy and, where possible, rechecked by a small consumer-side kernel.

### H3: governance state should be replayed, not edited

Draft, proposal, acceptance, activation, deprecation, and replacement should be
typed transitions. The apparent current state is a validated fold over signed
events. A source declaration that asks for an unjustified state should fail.

### H4: authorization requires a restricted sublanguage

General Catena expressions are too powerful for policy because effects,
divergence, ambient state, and opaque libraries impede analysis and
reproduction. Policy should be total, terminating, side-effect free, bounded,
and return both a decision and structured reasons.

### H5: approachable vocabulary can preserve formal distinctions

Terms such as “needs,” “promises,” “example,” “property,” “evidence,”
“approve,” and “activate” may let programmers use the feature without first
learning proof or category-theory terminology. This remains a usability
hypothesis, not evidence.

### H6: start with traceability, contracts, properties, and lifecycle

The first implementation should not begin with an ambitious universal prover.
A typed graph, deterministic scenarios, first-order contracts, generated
properties, signed evidence, and a small lifecycle policy exercise the core
architecture. Temporal models and deductive proof can then extend it without
changing the meaning of earlier evidence.

## Paths to explore

### Core semantic model

- Define kinds for claim, method, evidence, policy, decision, approval, and
  transition.
- Decide which are compile-time values, proof-only values, serializable
  protocol values, or nominal declarations.
- Define subject identity across package versions, module movement, aliases,
  and replacement.
- Specify a canonical, versioned intermediate representation and semantic
  digest.
- Prove that specification elaboration preserves ordinary program typing and
  effects.

### Contracts

- Define first-order caller and implementation obligations.
- Extend monitoring to higher-order functions, callbacks, handlers, and
  resumptions.
- Decide how monitored contracts interact with tail calls and BEAM stack
  behavior.
- Define static, monitored, assumed, and rejected checking modes.
- State whether contract predicates must be pure and total.

The starting evidence is
[Meyer 1992](../30-sources/meyer-1992-applying-design-by-contract.md) and
[Findler and Felleisen 2002](../30-sources/findler-felleisen-2002-contracts-higher-order-functions.md).

### Executable evidence

- Derive generators and shrinkers from ordinary ADTs without exposing hidden
  constructors.
- Record seeds, distributions, discards, coverage, and replay information.
- Build deterministic scenario capabilities for clocks, networks, schedulers,
  files, and process mailboxes.
- Define equivalence and observation for effectful programs.
- Test whether generated properties remain useful for recursive and
  higher-order data.

The starting evidence is
[Claessen and Hughes 2000](../30-sources/claessen-hughes-2000-quickcheck.md).

### Bounded, temporal, and deductive verification

- Choose a relational kernel and make every finite scope part of the result
  type.
- Define state invariants, safety, liveness, fairness, and refinement for
  selected actor protocols.
- Develop proof obligations for frames, recursion, effects, abstraction, and
  imported assumptions.
- Choose a certificate format and small checker.
- Measure solver stability, certificate size, and counterexample quality.

The starting evidence is
[Jackson 2002](../30-sources/jackson-2002-alloy.md),
[Lamport 1994](../30-sources/lamport-1994-temporal-logic-actions.md),
[Leino 2010](../30-sources/leino-2010-dafny.md), and
[Necula 1997](../30-sources/necula-1997-proof-carrying-code.md).

### Lifecycle

- Model the proposal lifecycle as a typed transition system.
- Define rejection, withdrawal, expiration, deprecation, supersession, and
  recovery without ambiguous backward transitions.
- Make evidence and approval invalidation depend on semantic digests.
- Determine which transitions are local build facts and which require durable
  external events.
- Model hot-code upgrade compatibility and active-version exclusivity.

[Strom and Yemini 1986](../30-sources/strom-yemini-1986-typestate.md)
provides the language-level transition precedent but does not solve
multi-actor persistent governance.

### Authorization and governance of governance

- Define principals, roles, resources, actions, scoped delegation, thresholds,
  conflicts, expiration, and revocation.
- State deny/default and conflict-combination semantics.
- Produce policy evaluation traces suitable for diagnostics.
- Analyze policy equivalence and privilege expansion.
- Design bootstrap and recovery ceremonies.
- Require an active policy to authorize its own replacement.

The starting evidence is
[Cutler et al. 2024](../30-sources/cutler-et-al-2024-cedar.md).

### Provenance

- Canonicalize evidence envelopes and domain-separate signatures.
- Bind claims, source, semantic IR, binaries, toolchains, inputs, outputs,
  environments, and actors.
- Define freshness, replay resistance, revocation, and event ordering.
- Decide whether a transparency log is required and how offline use works.
- Distinguish recheckable certificates from trusted attestations.
- Specify how thresholds respond to partial credential compromise.

The starting evidence is
[Torres-Arias et al. 2019](../30-sources/torres-arias-et-al-2019-in-toto.md)
and [Necula 1997](../30-sources/necula-1997-proof-carrying-code.md).

### Usability and vocabulary

- Test whether programmers distinguish example, property, bounded model,
  proof, attestation, and approval after short explanations.
- Test operation selection from diagnostics and evidence summaries.
- Compare “needs/promises” with precondition/postcondition terminology without
  teaching both as mandatory synonyms.
- Measure how much declaration overhead ordinary modules incur.
- Keep formal details available in an evidence inspector without making them
  the default error vocabulary.

This path should follow the
[approachable vocabulary proposal](../20-notes/approachable-language-vocabulary.md).

### Security and operations

- Threat-model compromised workers, signers, approvers, policy authors, and
  dependencies.
- Test cross-artifact evidence substitution, replay, downgrade, stale approval,
  and emergency-path abuse.
- Bound policy and checker resource use.
- Measure incremental invalidation, build latency, runtime monitor overhead,
  evidence storage, and transition-validation cost.
- Specify degraded behavior when identity, revocation, or log services are
  unavailable.

## Prototype experiments

### Experiment A: typed claim graph

Build a small elaborator for functions, ADTs, effects, claims, methods, and
evidence. Mutate identifiers, paths, display names, types, and implementations.
The graph should preserve evidence only for changes whose semantic digest is
provably unchanged.

### Experiment A2: adoption and scope boundary

Compile the same small project with no declarations, one local contract, a
module-level policy, a publication-only policy, and a workspace policy. Verify
that:

- the undeclared project has no governance overhead;
- malformed declarations always fail;
- missing publication evidence does not masquerade as success;
- local draft work remains possible when publication alone is governed;
- unrelated modules remain outside scope; and
- explicit interface obligations show exactly why governance propagated.

### Experiment B: responsibility at higher-order effect boundaries

Implement monitored contracts over callbacks and one algebraic effect handler.
Generate violations by callers, callees, callback producers, callback
consumers, handlers, and resumptions. Each diagnostic must identify the
correct promise and boundary.

### Experiment C: evidence honesty

Run one rule through an example, generated property, finite model, and proof
checker. The UI must report distinct conclusions and prevent policy from
silently treating a weaker method as a stronger one.

### Experiment D: adversarial promotion model

Model a release policy with authors, reviewers, owners, thresholds,
delegations, revocation, replacement, and emergency recovery. Search bounded
histories for single-actor activation, post-revocation approval, policy
downgrade, approval replay, and activation without evidence.

### Experiment E: provenance substitution

Create valid evidence for artifact A and attempt to attach it to artifact B,
to a changed claim, to an older policy, and to a replayed transition. Every
substitution should fail for a specific typed reason.

### Experiment F: programmer comprehension

Give representative programmers six tasks:

1. state a local function promise;
2. choose between an example and a property;
3. explain a finite-model result;
4. identify why evidence became stale;
5. repair an insufficient-approval diagnostic; and
6. distinguish technical evidence from release authority.

Record prediction, completion, repair success, and terminology confusion.

## Findings

The current synthesis is
[Language-Integrated Specifications and Governance](../20-notes/language-integrated-specifications-and-governance.md).
It provisionally recommends:

- a typed specification graph rather than comments or disconnected test
  names;
- distinct evidence types rather than one confidence status;
- a pure and terminating specification/policy core;
- signed external attestations with explicit trust;
- certificate checking where practical;
- typed and append-only lifecycle transitions;
- separate technical evidence and authorization decisions;
- a compiler-owned semantic IR with external evidence producers; and
- staged implementation beginning with traceability, contracts, properties,
  and lifecycle.

These are design hypotheses. No Catena calculus, prototype, security analysis,
performance evaluation, or user study yet validates the combined system.

## Outcome

Open. Resolution requires:

- a normative core calculus and executable reference semantics;
- proof that specification elaboration preserves the program type-and-effect
  system;
- adversarial validation of the lifecycle and authority model;
- a prototype evidence and provenance pipeline;
- performance measurements on representative projects; and
- comprehension and diagnostic-repair evidence from programmers.

Follow the
[Language-Integrated Specifications and Governance map](../10-maps/language-integrated-specifications-and-governance.md)
for the curated route through the evidence and related Catena work.
