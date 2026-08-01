---
title: "Language-Integrated Specifications and Governance"
kind: note
created: "2026-08-01"
maturity: developing
tags:
  - catena
  - formal-methods
  - governance
  - language-design
  - specification
aliases:
  - "Specifications and governance as language features"
  - "Typed specification governance"
---

# Language-Integrated Specifications and Governance

## Executive conclusion

Catena should make specifications and governance part of the language, but it
should not pretend that every useful claim can be checked in the same way.

The proposed design has four connected parts:

1. a **specification graph** of stable, typed claims attached to language
   entities;
2. **typed evidence** that states how a claim was checked, over which artifact,
   with what result and trust assumptions;
3. an **authority policy** that decides who may propose, approve, replace, or
   activate a governed artifact; and
4. an **append-only transition history** that records every accepted change and
   makes the currently active state derivable rather than mutable by fiat.

The compiler should parse, type-check, link, and explain this graph. It should
also discharge claims that fall within a defined static checker. It must not
turn a test run, bounded model search, solver response, signature, or human
approval into the same undifferentiated word, “verified.” Those observations
mean different things:

- a runtime contract reports what happened on an exercised boundary;
- a property run searches generated examples and may find a counterexample;
- a bounded model check exhausts a declared finite scope;
- a deductive proof establishes a formula relative to a formal model and
  trusted checker;
- a signature binds bytes and an asserted event to an identity;
- an approval says an authorized actor accepted responsibility; and
- a promotion event says the policy permitted a lifecycle transition.

None subsumes all the others.

The initial language feature should therefore be deliberately plural. A
`rule` describes a required behavior. An `example`,
`property`, or `scenario` supplies an executable
way to challenge it. A `proof` or bounded
`model` supplies a stronger but more specialized witness. An
`attestation` imports signed evidence from outside compilation.
A `policy` decides which evidence and approvals permit a
`decision` to move to its next state.

The public vocabulary can stay practical: “needs,” “promises,” “always,”
“example,” “evidence,” “owner,” “approve,” “activate,” and “replace.” The
compiler and tooling carry the formal distinctions underneath. Diagnostics
should explain the missing claim, evidence, authority, and repair action in
those terms.

Adoption should be optional at the project boundary and strict inside every
declared governance boundary. A project that declares no specifications or
governance policy remains an ordinary Catena project. Once a claim, artifact,
module, package, or action is placed under governance, however, the compiler
and admission tooling must enforce its declarations exactly. Missing evidence
may leave draft code locally buildable, but it cannot be silently treated as
meeting a governed publication or activation gate.

This proposal is a research direction, not a settled surface specification.
Its core idea is stronger than syntax:

> A governed claim is never just text or a status label. It has a precise
> subject, a checking meaning, typed evidence, authorized transitions, and a
> durable history.

## Scope

This note asks:

> How can a functional language make requirements, behavioral specifications,
> verification evidence, authority, and lifecycle governance into coherent
> language features that ordinary programmers can use?

The topic includes:

- function, module, datatype, effect, process, and language-semantics claims;
- runtime monitoring, generated testing, bounded analysis, temporal models,
  and deductive verification;
- stable requirement identity and traceability;
- approvals, separation of duties, thresholds, delegation, and revocation;
- promotion, deprecation, replacement, and compatibility;
- signed evidence from builds, benchmarks, and external tools;
- compiler, build, runtime, and BEAM integration; and
- approachable names and diagnostics.

It does not attempt to design a complete theorem prover, identity provider,
source-control host, or organizational constitution inside the programming
language. Those systems may supply inputs, but Catena must define exactly how
their inputs become language evidence.

## Adoption and enforcement boundary

The recommended system is **available to every project but not compulsory for
every project**. Catena should not require a specification bundle, approval
history, or organizational policy before it can compile an ordinary program.

The boundary follows six rules.

### 1. No declaration means no implicit governance

A project with no specification or governance declarations uses the ordinary
language semantics. The compiler does not invent claims, owners, approval
roles, release gates, or evidence requirements.

This rule prevents a research-oriented feature from becoming mandatory
process overhead for scripts, experiments, teaching projects, or applications
that do not need governed releases.

### 2. Every declaration has mandatory language semantics

Once source code contains a specification declaration, the compiler always
parses, resolves, and type-checks it. A project cannot keep an ill-typed claim
as “documentation only,” attach evidence to an unknown subject, or choose to
ignore a malformed policy.

Optional adoption therefore does not mean optional correctness. The feature
is optional to enter and non-optional to obey once entered.

### 3. Governance coverage is explicit and scoped

A policy must name the artifacts and actions it governs. Coverage may be
declared for:

- one claim or specification;
- a function, datatype, effect, process, or module;
- a package or workspace;
- an exported or compatibility-sensitive interface;
- a publication, deployment, migration, or activation action; or
- an explicitly named build or release profile.

Coverage is nominal and inspectable. It must not arise from a filename pattern,
ambient machine configuration, or an invisible organization-wide default.
Organization tooling may require a root project policy, but that requirement
must enter the project as an explicit, authenticated policy input.

### 4. Enforcement blocks the governed action, not unrelated work

The result depends on what is invalid or missing:

| Condition | Required behavior |
| --- | --- |
| Ill-typed claim, invalid link, malformed policy, or corrupt history | reject compilation or admission because the declared language artifact has no valid meaning |
| Failed mandatory static claim | reject the governed artifact and any action whose policy requires the claim |
| Missing external evidence or approval | keep the artifact visibly incomplete and block the governed transition |
| Draft code outside the governed action | permit ordinary checking or local execution when the active policy allows it |
| Explicit policy governing compilation itself | block compilation when that policy's gates are unmet |
| Unrelated code outside the declared scope | do not impose the governed artifact's evidence or approval requirements |

This permits a developer to edit and test a draft while preventing that draft
from being published, activated, or represented as compliant.

### 5. A governed boundary fails closed

Within its declared scope, unavailable identity services, stale evidence,
checker timeouts, missing approvals, and policy-evaluation errors do not become
success. They produce distinct typed failures or an incomplete state.

An emergency or offline path is valid only when the active policy defines it
in advance, identifies its narrower guarantees, and requires its own durable
audit evidence. A command-line “ignore governance” switch cannot create a
governed release.

### 6. Governance does not spread accidentally through dependencies

A governed package can require consumers to validate its signed manifest as a
dependency-admission condition. Importing it does not automatically govern all
of the consumer's unrelated source.

Governance propagates only through an explicit interface obligation—for
example, a plugin contract requiring an implementation proof, or a workspace
policy covering every published package. The compiler must show that
propagation path in diagnostics.

### Enforcement summary

The recommendation can be summarized as:

> Optional to adopt; mandatory to interpret; explicit in scope; fail-closed for
> governed actions; noncontagious outside declared interfaces.

This boundary is part of the language proposal, not a packaging preference.
Without it, “optional governance” could become silently unenforced, while
“mandatory governance” could burden every Catena program with an organizational
workflow it never requested.

## Operational definitions

Terms in this note have testable meanings:

- A **claim** is a proposition about a named subject, written in a supported
  claim language with declared semantics.
- A **specification** is a linked set of claims, definitions, relationships,
  and permitted evidence methods.
- **Evidence** is a typed witness or observation connected to an exact claim
  and artifact. It is not the claim itself and not an assertion of absolute
  truth.
- A **policy** is a total, terminating decision procedure over a restricted
  input schema that answers whether an actor may perform a named governance
  action.
- **Governance** is the combination of authority policy, lifecycle transition
  rules, accepted evidence, and durable decision history.
- An **approval** is an authorized actor's signed acceptance of a specific
  proposal and digest. It does not prove the proposal's technical claims.
- A **promotion** is a successful typed transition whose guards, approvals,
  and evidence requirements were satisfied under a named policy version.
- **Traceability** means the tool can traverse from a claim to its subject,
  checking method, evidence, decision, implementation, replacement, and
  relevant source location without relying on text search.
- **Reliable enforcement** means invalid links, ill-typed claims,
  unauthorized transitions, stale evidence, and unmet mandatory gates are
  rejected deterministically.

These definitions prevent common category errors. Passing tests is evidence
for a behavioral claim but not a proof of it. Authorization permits an action
but does not make the action correct. A correct signature authenticates bytes
but does not make their contents honest. A lifecycle state records a governed
decision but is not an implementation-completeness estimate.

## Evidence route

The proposal combines primary work that addresses different parts of the
problem:

- [Meyer 1992](../30-sources/meyer-1992-applying-design-by-contract.md)
  establishes executable preconditions, postconditions, invariants, and
  responsibility at component boundaries.
- [Findler and Felleisen 2002](../30-sources/findler-felleisen-2002-contracts-higher-order-functions.md)
  shows why functions require delayed monitoring and polarity-aware blame.
- [Leino 2010](../30-sources/leino-2010-dafny.md) demonstrates a
  verification-aware language in which contracts, frames, invariants,
  termination measures, ghost state, and solver obligations coexist with
  programs.
- [Claessen and Hughes 2000](../30-sources/claessen-hughes-2000-quickcheck.md)
  makes properties executable through generators while documenting the false
  confidence caused by weak distributions and finite samples.
- [Jackson 2002](../30-sources/jackson-2002-alloy.md) shows the value and the
  boundary of bounded relational analysis.
- [Lamport 1994](../30-sources/lamport-1994-temporal-logic-actions.md)
  supplies history-sensitive specifications and refinement for concurrent
  systems.
- [Roșu and Șerbănuță 2010](../30-sources/rosu-serbanuta-2010-k-semantic-framework.md)
  demonstrates that one formal language definition can be executable and can
  drive multiple semantic tools.
- [Strom and Yemini 1986](../30-sources/strom-yemini-1986-typestate.md)
  makes lifecycle-dependent operations part of compiler checking.
- [Cutler et al. 2024](../30-sources/cutler-et-al-2024-cedar.md) demonstrates a
  restricted, analyzable language for authorization decisions and policy
  equivalence questions.
- [Torres-Arias et al. 2019](../30-sources/torres-arias-et-al-2019-in-toto.md)
  separates a signed normative process layout from signed observations of
  performed steps.
- [Necula 1997](../30-sources/necula-1997-proof-carrying-code.md) shows how an
  untrusted producer can supply a witness that a smaller consumer-side kernel
  checks against its own policy.

No one source establishes the complete design. The unified model below is a
Catena proposal synthesized across those boundaries. Its usability, soundness,
security, and operational cost remain to be demonstrated.

## Why this belongs in the language

### Text cannot carry semantic responsibility

A prose requirement can be useful to people, but a compiler cannot know its
subject, scope, quantification, execution point, replacement relation, or
admissible evidence. Naming conventions and links help navigation but do not
make an obligation enforceable.

A language declaration can:

- resolve its subject through the module system;
- type-check expressions against the subject's public interface;
- determine which party owns each side of a boundary;
- elaborate into a stable intermediate representation;
- reject effects that would make a checker nondeterministic;
- generate a runtime monitor, test driver, model, or proof obligation;
- attach evidence to an exact semantic digest; and
- expose structured information to documentation and governance tooling.

### Tests alone cannot be the specification

Tests provide observations over selected executions. They are invaluable
counterexample searches, especially when generated from a property, but a test
suite has no general rule for saying which omitted cases matter. A language
feature must preserve the difference between:

- the behavioral claim;
- the input-domain and generator assumptions;
- the checking method;
- the concrete run;
- the observed result; and
- the conclusion policy is allowed to draw from that result.

### Governance is not a mutable metadata field

A field such as `status: approved` loses the reasons, policy
version, actor, evidence, proposal digest, and path by which approval occurred.
If any writer can edit it, the state is not governed.

Governed state should instead be the result of replaying authorized, signed,
append-only transitions. The source declaration may state the desired current
state, but the build should accept it only when the transition history
justifies that state.

### The compiler is a coordinator, not an omniscient judge

The compiler is well placed to validate the specification graph and run pure
decidable checks. It cannot independently know that:

- a named person controls a signing key;
- a benchmark ran on an isolated host;
- a production migration succeeded;
- a review was thoughtful;
- an external tool is honest; or
- an organizational policy should change.

Those are external facts or social decisions. The language can require typed,
signed attestations and evaluate their admission policy without claiming to
have observed the world itself.

## Three independent questions

Every governed operation must keep three questions separate:

| Question | Typical answer | What it does not establish |
| --- | --- | --- |
| Is the claim supported? | contract result, counterexample search, bounded model, proof, attestation | that an actor may activate the change |
| May this actor take this action? | policy decision over identity, role, resource, action, and context | that the technical claim is true |
| How did the artifact reach this state? | append-only transition history with digests and policy versions | that past actors or tools were trustworthy |

Conflating them creates dangerous shortcuts. An administrator should not be
able to override a failed proof by changing a status bit. A proof should not
grant its producer release authority. A valid signature should not count as
correctness evidence unless its issuer and method are permitted for that exact
claim.

## Claim kinds

A single universal formula language would either be too weak for important
claims or too powerful to analyze predictably. Catena should expose a family
of claim kinds with explicit semantics.

| Claim kind | Natural subject | Checking regime | Honest success statement |
| --- | --- | --- | --- |
| `needs` / `promises` | function boundary | static proof or runtime monitor | the obligation was proved, or no monitored violation occurred |
| `invariant` | datatype, module, resource | constructor proof, module proof, or runtime monitor | the invariant is preserved under the declared boundary |
| `property` | pure or controlled-effect behavior | generated examples | no counterexample was found in the recorded run |
| `example` | concrete behavior | direct evaluation | this exact input produced this expected observation |
| `model` | finite structural relations | bounded exhaustive search | no counterexample exists within the recorded scope |
| `always` / `eventually` | process or protocol history | temporal model checking or proof | the temporal formula holds in the declared model or proof |
| `refines` | implementation and abstract model | simulation or logical proof | the implementation model preserves declared observations |
| `conforms` | artifact and specification | method chosen by the claim | the named conformance procedure produced accepted evidence |
| `attestation` | external step or observation | signature, digest, and policy validation | an accepted issuer signed this statement over these bytes |
| `decision` | governed proposal | authorization and transition evaluation | the policy permitted this state transition |

The exact public terms require usability testing. The semantic distinctions do
not.

## Proposed language model

### Stable identity

Every durable claim and governed artifact needs an identity that survives
display-name changes and source movement. Identity should be nominal and
module-qualified, not inferred from a line number or prose title.

For example, a claim could elaborate to:

~~~text
ClaimId(
  package = "catena.parser",
  version = 1,
  name = "parse-print-round-trip"
)
~~~

Renaming a claim requires an explicit alias or replacement event. Reusing an
old identifier for an unrelated meaning is rejected.

### Typed subjects

A claim names a language entity, not a string:

~~~catena
spec Parser.RoundTrip describes Parser.parse {
  ...
}
~~~

Name resolution establishes the exact declaration, package identity,
visibility, and semantic version. If the function changes incompatibly, old
evidence does not silently follow it.

### Hypothetical surface form

The following syntax is illustrative rather than settled:

~~~catena
spec Parser.RoundTrip describes Parser {
  rule parse_after_print
    for tree in SyntaxTree
    promises parse(print(tree)) == Ok(tree)

  example empty_module {
    check parse(print(Module([]))) == Ok(Module([]))
  }

  property generated_trees supports parse_after_print {
    for tree from SyntaxTree.generate
    check parse(print(tree)) == Ok(tree)
  }
}
~~~

The compiler would elaborate this into typed claim and method records. The
`property` supports the `rule`; it is not an alias
for the rule and its successful run does not upgrade itself into proof.

### Restricted specification contexts

Claim expressions should default to a total, deterministic, pure subset:

- no ambient time, random source, filesystem, network, process mailbox, or
  mutable global state;
- explicit finite data for decidable evaluation;
- effectful observations only through named scenario fixtures;
- bounded recursion or separately checked termination for proof expressions;
- explicit quantification domains; and
- canonical serialization for digests.

This restriction is a feature. An unrestricted general-purpose expression can
diverge, depend on hidden state, and make policy outcomes irreproducible.

### Specification graph

Elaboration should produce a graph rather than flattened annotations:

~~~text
subject <- describes - claim <- supports - method <- produced-by - evidence
                             <- replaces - claim
decision <- governs - subject
decision <- requires - claim
transition <- authorized-by - policy
transition <- cites - evidence
~~~

The graph enables deterministic checks:

- every evidence record names an existing claim;
- every mandatory claim has at least one admitted method;
- every claim has a typed subject;
- every replacement preserves or explicitly changes scope;
- every promotion cites the evidence and policy it used;
- no evidence survives a semantic digest change unless a declared transport
  rule proves it still applies; and
- cycles in replacement or dependency relations are rejected.

## Behavioral contracts

### Local boundaries

For a first-order function:

~~~catena
fn withdraw(account, amount)
  needs amount > 0
  needs amount <= account.balance
  promises result.balance == account.balance - amount
~~~

`needs` assigns an obligation to the caller;
`promises` assigns one to the implementation. The language must
specify whether each clause is:

- proved statically;
- monitored in development builds;
- monitored in production builds;
- assumed at a trusted boundary; or
- rejected because no admissible method exists.

The mode is not a compiler optimization detail. It changes what the evidence
means and belongs in the specification interface.

### Higher-order boundaries

If a function accepts or returns another function, checking cannot happen only
at the outer call. Catena must preserve the contract through a wrapper and
check each obligation at the point where the nested function is eventually
used.

Effects make the polarity richer. A callback may promise both a return value
and an allowed effect row; its caller may promise to handle or propagate those
effects. Diagnostics should identify the boundary and obligation:

~~~text
Payment.retry promised to call the callback with a positive delay.
The callback was called with -10 milliseconds.
The promise belongs to Payment.retry at payment.cat:42.
~~~

The default message need not teach “positive” and “negative blame,” but the
internal semantics must retain that information.

### Datatype and module invariants

An invariant should be enforced at the smallest abstraction boundary that can
actually preserve it:

- a public constructor may prove the invariant by construction;
- an abstract module may check all exported state-changing operations;
- a deserializer may validate untrusted bytes dynamically; and
- unsafe or foreign imports must name the invariant they assume.

An invariant that clients can invalidate through exported representation
access is not a valid module guarantee.

## Executable examples and properties

### Examples are exact witnesses

An example states that one exact setup has one expected observation. Examples
are useful documentation, regression anchors, and diagnostic fixtures. They do
not generalize beyond the values they run.

### Properties generate challenges

A property should include:

- the supported claim;
- typed input generators;
- preconditions and discard behavior;
- observation and equality rules;
- sample budget and stopping policy;
- seed and replay data;
- coverage or distribution goals;
- effect sandbox, when applicable; and
- counterexample shrinking policy.

A run result should say:

~~~text
Property evidence: supported
Claim: Parser.RoundTrip.parse_after_print
Artifact: sha256:...
Generator: SyntaxTree.generate v3
Seed: ...
Accepted cases: 10,000
Discarded cases: 411
Coverage obligations: satisfied
Counterexamples: none found
~~~

The word “proved” is forbidden for this result.

### Scenarios control effects

An effectful scenario should receive explicit capabilities:

~~~catena
scenario retry_after_timeout using {
  clock: SimulatedClock,
  network: ScriptedNetwork,
  scheduler: DeterministicScheduler
} {
  ...
}
~~~

The scenario runner records the capability implementations and event trace.
Production services can supply observations through attestations, but replay
and simulation should be preferred for deterministic language evidence.

## Bounded and temporal models

### Bounded structural analysis

Relational models are useful for questions such as:

- can dependency ownership contain a cycle?
- can two active versions claim the same stable identity?
- can a threshold policy be satisfied by one compromised role?
- does any permitted promotion lack required evidence?

Every result must include its scope:

~~~text
No counterexample found for:
  principals <= 5
  roles <= 4
  claims <= 8
  transitions <= 12
~~~

The scope is part of the evidence type, not an optional log line.

### Temporal claims

Concurrent processes and governance histories need claims over executions:

- an accepted proposal is never activated before mandatory evidence exists;
- revoked authority cannot approve later transitions;
- every started replacement either completes or remains visibly pending;
- no two incompatible versions are active together; and
- every accepted request eventually receives a reply or a terminal failure.

Catena should distinguish:

- **state invariants**, true at every reachable state;
- **safety properties**, ruling out bad finite histories;
- **liveness properties**, requiring eventual progress under stated fairness
  assumptions; and
- **refinement claims**, connecting an implementation model to an abstract
  specification.

Fairness and environment assumptions must be explicit. Otherwise an
“eventually” claim can hide an impossible scheduler or cooperative
environment.

## Deductive proof and the trusted kernel

### Proof obligations

Static verification should elaborate supported contracts into obligations over
a small logical core. Features such as mutation, effects, recursion, and
abstract modules add obligations for:

- frames: which state may change;
- termination: why recursive proof computation finishes;
- handler behavior: which effects are consumed or forwarded;
- representation invariants;
- abstraction boundaries; and
- imported assumptions.

Solver automation may search for a proof, but the durable result should be a
certificate or proof object checked by a smaller, versioned kernel whenever
practical.

### Trust statement

Every proof result should expose:

~~~text
proved relative to:
  language semantics digest
  logical kernel version
  imported axioms
  abstraction assumptions
  certificate checker version
~~~

“Mathematical proof” is not a license to hide the trusted base. A false axiom,
incorrect elaboration, or semantic mismatch can validate the wrong theorem.

### Assumptions are contagious

If claim A depends on claim B as an assumption, evidence for A must retain that
dependency. Revoking B or changing its semantic digest invalidates or marks
dependent evidence stale. The tool should display the shortest assumption path
that blocks promotion.

## Governance as typed state transitions

### Separate lifecycle from evidence

Lifecycle state should not encode technical confidence. A proposal can be
accepted while carrying explicitly weak evidence, or remain unaccepted despite
a proof because the organization has not authorized activation.

A possible initial lifecycle is:

~~~text
Draft -> Proposed -> Accepted -> Active -> Deprecated -> Superseded
          |             |
          +-> Rejected  +-> Withdrawn
~~~

Exact states remain open, but each arrow must be a named constructor with
defined guards. Arbitrary assignment is impossible.

### Transition values

An accepted transition should be an immutable value:

~~~text
Transition {
  artifact_id
  from_state
  to_state
  proposal_digest
  evidence_digests
  approval_digests
  policy_digest
  actor
  timestamp_or_log_position
  signature
}
~~~

The current state is obtained by validating and replaying transitions.
Snapshots may accelerate replay but do not replace the signed history.

### Decisions and approvals

Illustrative syntax:

~~~catena
decision ParserV2 {
  changes Parser
  replaces ParserV1

  activate when {
    evidence Parser.RoundTrip.generated_trees
    evidence Parser.ProtocolModel
    approvals 2 from ParserMaintainer
    approval 1 from RuntimeOwner
  }
}
~~~

An approval binds:

- actor identity and credential;
- role derivation under a policy version;
- exact proposal and evidence-set digests;
- requested transition;
- validity interval or log position; and
- signature.

Adding evidence after approval may require reapproval because the reviewed
proposal changed. Removing or replacing evidence always does.

### Authorization policy

Governance policy should use a restricted decision language over:

~~~text
actor, action, resource, proposal, evidence summary, context
~~~

It must be total, terminating, side-effect free, and analyzable. Policy
evaluation returns a decision plus reasons, not a general computation.

Useful policy primitives include:

- role membership and scoped delegation;
- threshold approval;
- separation of author, reviewer, and activator;
- conflict-of-interest predicates;
- expiration and revocation;
- artifact ownership;
- emergency paths with stronger audit requirements; and
- rules for which issuers and methods may satisfy each claim kind.

The language should deny transitions when inputs are missing or malformed.
Default behavior must be explicit in the normative semantics.

### Governance of governance

Policy changes create a meta-level problem: who authorizes a change to the
authorization rules?

Catena needs a root policy established through an explicit bootstrap ceremony.
After bootstrap, a policy version can be replaced only through a transition
authorized by the previously active policy, unless a separately defined
recovery policy applies. Each transition records both policy versions.

This does not eliminate social trust. It makes the trust root and exceptional
paths visible.

## External evidence and provenance

### Evidence envelope

Every imported observation should use a canonical envelope:

~~~text
Evidence {
  evidence_id
  claim_id
  subject_digest
  method
  method_version
  result
  parameters
  environment
  toolchain_digests
  input_digests
  output_digests
  issuer
  policy_context
  event_position
  signature
}
~~~

Different methods add typed fields. A benchmark records warmup, repetitions,
hardware class, variance, and thresholds. A property run records seed,
generator, samples, discards, and coverage. A proof records assumptions and
certificate. A manual review records scope and exact proposal digest.

### Attestation is not truth

Validating an envelope establishes:

1. canonical bytes were signed;
2. the signature matches the declared issuer;
3. artifact and claim digests match;
4. the issuer and method are admitted by policy; and
5. freshness, threshold, and revocation rules hold.

It does not establish that the issuer was honest, the machine was
uncompromised, or the method was scientifically adequate. Those are policy and
threat-model assumptions and must remain inspectable.

### Freshness and invalidation

Evidence validity should be a function, not a permanent bit. It may become
inadmissible when:

- the subject's semantic digest changes;
- a dependency or assumption changes;
- the tool or generator version changes under a strict policy;
- a credential is revoked;
- an evidence validity interval expires;
- a vulnerability invalidates the environment; or
- the governing policy changes its admission rules.

The original record remains in history. Tooling reports that it is no longer
accepted for the current decision.

## Compiler and runtime architecture

### Compilation pipeline

A plausible pipeline is:

~~~text
parse declarations
  -> resolve typed subjects and stable identities
  -> elaborate claims into the specification IR
  -> check pure/total specification contexts
  -> generate monitors, tests, models, and proof obligations
  -> run local deterministic checkers
  -> emit an evidence plan for external work
  -> import and validate evidence envelopes
  -> evaluate governance policy
  -> validate transition history
  -> emit program, documentation, and governance manifest
~~~

The specification intermediate representation should be versioned and have a
canonical semantic digest. Tooling integrations consume this representation
instead of reparsing source comments.

### Trusted computing base

The minimum trusted base includes:

- parser and name resolver for normative declarations;
- type and effect checker;
- specification elaborator;
- canonical serializer and digest implementation;
- proof-certificate checker for supported proof formats;
- policy evaluator;
- transition-history validator;
- signature and credential verifier; and
- normative semantics that define their agreement.

Generators, solvers, model searchers, CI workers, benchmark hosts, and evidence
producers should remain outside the trusted base when their outputs can be
rechecked. When they cannot, policy must say they are trusted attestation
sources.

### BEAM boundary

The BEAM is useful for isolated concurrent evidence workers, supervision,
timeouts, and distributed execution. It should not make governance results
depend on scheduler accidents.

The initial design should:

- evaluate policy and static specification expressions deterministically at
  build or admission time;
- run effectful scenarios in supervised processes with explicit capabilities;
- record message traces and scheduler models for concurrency evidence;
- keep signed promotion history in durable storage rather than process memory;
- treat node identity as transport context, not organizational identity; and
- define hot-code upgrade compatibility through explicit version and
  refinement claims.

## Integration with Catena's other language features

### Algebraic data types

ADT declarations naturally generate specification subjects:

- constructor argument and result contracts;
- representation invariants at abstract boundaries;
- exhaustive scenario generation for finite datatypes;
- structural generators and shrinkers;
- serialization and compatibility claims; and
- lifecycle states for public schema versions.

The [ADT design](algebraic-data-types.md) remains authoritative for constructor
and matching semantics. Governance must not make hidden constructors visible
to a checker that ordinary clients cannot use.

### Algebraic effects

Contracts should describe both values and effects:

- effects an operation may perform;
- capabilities a caller must supply;
- operations a handler consumes or forwards;
- resumption multiplicity and lifecycle; and
- effect traces permitted by a scenario or temporal model.

Pure specification expressions cannot perform arbitrary effects. Controlled
scenarios receive explicit test capabilities. See the
[effect-handler synthesis](algebraic-effects-and-handlers.md).

### Categorical capabilities and laws

A declared law is a claim, not an automatically trusted truth. An instance may
support it through generated properties, parametricity, derivation from a
trusted representation, or deductive proof. The evidence method stays visible.

This gives the [categorical hierarchy](category-theory-for-programming.md) and
[combinator design](combinators-for-algebraic-data-and-categorical-programming.md)
a shared way to state:

- algebraic laws;
- evaluation order and strictness;
- short-circuit behavior;
- effect behavior;
- complexity and resource bounds; and
- conditions under which an instance or combinator is derived.

### Type inference

Ordinary specifications should type-check against inferred program types, but
proof and governance declarations must not destabilize principal inference.
Annotations may be required at specification boundaries, especially for:

- explicit quantification;
- higher-rank callbacks;
- refinement predicates;
- temporal state projections;
- overloaded law dictionaries; and
- imported external schemas.

The [greenfield type-system proposal](catena-greenfield-type-system.md)
provides the surrounding annotation and coherence policy.

### Approachable vocabulary

The public feature should follow the
[behavior-first vocabulary policy](approachable-language-vocabulary.md):

- show what the program needs or promises before naming a proof system;
- call finite observations examples, properties, or scenarios;
- say “no counterexample within 8 nodes,” not “model verified”;
- say which evidence is missing and how to produce it;
- reserve formal terminology for detailed explanations and optional theory
  material; and
- never hide execution cost, effects, scope, assumptions, or authority.

## Diagnostics and tooling

### Four-part diagnostic

A governance diagnostic should answer:

1. **What is blocked?**
2. **Which claim, evidence, or authority is missing?**
3. **Why does the active policy require it?**
4. **What can the programmer do next?**

For example:

~~~text
ParserV2 cannot move from Accepted to Active.

Required claim:
  Parser.Protocol.no-double-activation

Current evidence:
  bounded model completed for 5 actors

Active policy requires:
  a bound of at least 8 actors for public parser releases

Next:
  run catena evidence model Parser.Protocol --actors 8
  or propose a policy change through RuntimeGovernance
~~~

### Evidence explorer

Tooling should expose:

- claim source and semantic digest;
- implementations and dependents;
- accepted, rejected, stale, and missing evidence;
- evidence method, scope, assumptions, and issuer;
- active policy clause and evaluation trace;
- approvals and conflicts;
- lifecycle history;
- replacement lineage; and
- replay commands where available.

### Machine interfaces

The compiler should emit:

- canonical specification IR;
- evidence plans;
- deterministic diagnostics with stable codes;
- governance manifests;
- proof or model artifacts;
- signed transition requests; and
- documentation views.

The machine interface must not depend on scraping human-readable error text.

## Security and failure model

### Adversaries

The design should be evaluated against:

- forged or replayed evidence;
- evidence attached to a different artifact;
- compromised CI workers or signers;
- colluding approvers;
- role escalation through policy ambiguity;
- time-of-check/time-of-use races;
- downgrade to an older policy or semantic kernel;
- cyclic replacement or dependency graphs;
- denial of service through expensive claims;
- nondeterministic or effectful policy code;
- misleading success summaries that omit scope;
- unsafe assumptions hidden behind imports; and
- emergency paths that become routine bypasses.

### Required defenses

At minimum:

- domain-separated signatures and canonical serialization;
- content and semantic digests;
- explicit issuer and credential chains;
- freshness, replay, and revocation checks;
- threshold and separation-of-duty policy;
- deterministic, resource-bounded policy evaluation;
- monotonic event positions or a transparency log;
- visible assumptions and scopes;
- immutable historical records;
- explicit recovery governance; and
- no automatic coercion between evidence kinds.

### Failure must be typed

The tool should distinguish:

- claim false, with counterexample;
- claim not established;
- checker timed out;
- evidence malformed;
- evidence stale;
- evidence issuer unauthorized;
- approval insufficient;
- policy denied;
- transition history invalid; and
- trusted subsystem unavailable.

Collapsing these into “verification failed” prevents safe repair and obscures
the trust boundary.

## What the evidence supports

The primary work supports the following conclusions with reasonable strength:

- executable contracts can allocate local responsibility;
- higher-order boundaries require delayed monitoring and careful blame;
- verification-aware languages can generate substantial automated proof
  obligations when programmers provide specifications and invariants;
- generated properties and bounded models are strong counterexample-finding
  techniques whose finite scope must remain explicit;
- temporal logic is needed for concurrent histories and refinement;
- an executable semantic definition can drive multiple language tools;
- lifecycle restrictions can be part of typing rather than convention;
- restricted authorization languages can support analyzable decisions;
- signed process layouts and event records preserve artifact provenance; and
- producer-generated certificates can reduce the consumer's trusted work.

The sources do not establish:

- that these mechanisms form one sound, usable Catena language;
- that ordinary programmers will understand the proposed terms;
- that one specification IR can represent all claim kinds without semantic
  leakage;
- that solver-backed proofs will remain stable under normal refactoring;
- that governance policy can be both approachable and resistant to adversarial
  ambiguity;
- that the full pipeline will have acceptable build and runtime cost; or
- that organizational identity and revocation can be made portable across
  deployments.

## Rejected shortcuts

### One `verified` boolean

Rejected because it erases method, scope, assumptions, issuer, artifact,
freshness, and authority.

### Tests as requirements

Rejected because examples do not state the general claim and successful finite
runs do not establish universal behavior.

### Arbitrary program expressions as policy

Rejected because hidden effects, divergence, ambient authority, and analysis
intractability make governance decisions unpredictable.

### Approval as proof

Rejected because social authority and technical evidence answer different
questions.

### Signatures as truth

Rejected because a valid signer can be mistaken, malicious, or operating in a
compromised environment.

### Mutable current state without history

Rejected because it permits unauthorized rewrites and makes audit,
reproduction, and replacement lineage impossible.

### A proof engine inside the entire trusted compiler

Rejected as the only design. Prefer portable certificates and a smaller
checker where feasible; where infeasible, name the solver or verifier as a
trusted attestation source.

### Formal vocabulary as the beginner interface

Rejected because mathematical precision should shape the feature without
becoming a prerequisite for ordinary use. Friendly terms still require exact
semantics and honest evidence labels.

## Staged implementation

### Stage 0: specification IR and traceability

Implement:

- stable claim identities;
- typed subjects and relationships;
- examples and deterministic scenarios;
- semantic digests;
- source-to-claim navigation;
- machine-readable evidence envelopes; and
- complete diagnostics for dangling or stale links.

This stage tests the graph before introducing authority.

### Stage 1: contracts and generated properties

Add:

- first-order `needs`, `promises`, and
  invariants;
- explicit static, monitored, or assumed modes;
- pure property declarations;
- generators, shrinking, coverage, and replay;
- evidence import and invalidation; and
- development-build monitors.

Do not claim deductive proof yet.

### Stage 2: lifecycle and authorization

Add:

- typed proposal and activation transitions;
- restricted policy language;
- roles, delegation, thresholds, and separation of duties;
- signed approvals;
- append-only transition validation; and
- policy bootstrapping and recovery.

### Stage 3: bounded and temporal models

Add:

- relational modeling with mandatory scopes;
- deterministic process scenarios;
- temporal claims and fairness declarations;
- refinement subjects; and
- counterexample visualization.

### Stage 4: deductive verification

Add only after the semantic core is stable:

- proof-only definitions;
- frames, termination, and abstraction obligations;
- a small logical kernel;
- certificate formats;
- assumption dependency and revocation;
- solver integrations outside the trusted base where possible; and
- proof-stability and diagnostic studies.

### Stage 5: external and distributed evidence

Add:

- credential profiles;
- transparency or monotonic event logs;
- build, benchmark, deployment, and compatibility attestations;
- revocation and freshness services;
- federated policy roots; and
- cross-organization evidence transport.

## Prototype acceptance criteria

The proposal should advance only if a prototype can demonstrate:

### Adoption boundary

- a project with no declarations remains a valid ordinary Catena project;
- every declared claim and policy is parsed, linked, and checked;
- coverage is explicit at claim, module, package, interface, action, or profile
  scope;
- missing publication evidence blocks publication without falsely reporting a
  compile-time type error in unrelated draft code;
- a governed boundary fails closed when evidence or authority is unavailable;
- importing a governed dependency does not govern unrelated consumer code; and
- every propagated obligation has an inspectable policy or interface path.

### Semantic fidelity

- one normative specification IR drives checking, documentation, and evidence
  plans;
- higher-order contract wrappers assign responsibility correctly;
- every evidence summary states method, scope, assumptions, and subject digest;
- temporal and bounded claims cannot be misreported as deductive proof; and
- derived tools agree with a reference semantics on generated programs.

### Governance integrity

- unauthorized and out-of-order transitions are rejected;
- changing a proposal invalidates old approvals;
- changing a claim invalidates nontransportable evidence;
- revoked credentials cannot authorize later events;
- threshold and separation-of-duty rules resist single-actor bypass;
- policy replacement is justified by the previously active policy; and
- current state can be reproduced from history.

### Usability

- programmers without formal-methods vocabulary can predict the difference
  among example, property, model, proof, attestation, and approval;
- they can repair missing-evidence and policy-denial diagnostics;
- common function contracts require little annotation;
- advanced claim kinds do not pollute ordinary type errors; and
- evidence scope and staleness are understandable without opening raw IR.

### Performance and operations

- deterministic policy evaluation has a hard resource bound;
- incremental compilation rechecks only affected claims;
- monitor overhead is measurable and controllable by declared mode;
- evidence caching is content-addressed and safe under dependency changes;
- proof and model jobs are cancellable and reproducible; and
- transition verification remains cheap enough for local development and
  admission gates.

## Falsification criteria

The unified feature should be reconsidered if:

- the specification graph requires pervasive manual identifiers or duplicate
  declarations;
- users consistently confuse finite evidence with proof despite diagnostics;
- policy becomes general-purpose enough to be unpredictable or too restricted
  for ordinary ownership rules;
- semantic digests invalidate evidence on irrelevant refactors or retain it
  across real meaning changes;
- the trusted computing base grows to include every solver and external worker;
- governance declarations dominate ordinary source files;
- higher-order and effect contracts break tail behavior or impose unacceptable
  overhead;
- external identity assumptions cannot be made explicit and portable; or
- a simpler separation between language specifications and an external
  governance protocol provides clearer guarantees.

Falsification does not require abandoning language-integrated claims. It may
show that governance should consume a stable language IR while remaining a
separately implemented protocol with the same normative semantics.

## Research priorities

1. Define the claim, method, evidence, policy, and transition core calculi.
2. Prove that claim elaboration preserves ordinary program typing and effects.
3. Define semantic digests that distinguish meaningful changes from location
   and formatting changes.
4. Specify contract monitoring for higher-order functions, handlers,
   resumptions, and BEAM process boundaries.
5. Prototype property generators and shrinkers derived from Catena ADTs.
6. Model the lifecycle and authorization rules adversarially within finite
   scopes.
7. Define a deterministic temporal model for selected process protocols.
8. Choose a certificate-checking kernel and state its trusted assumptions.
9. Design credential, revocation, freshness, and transparency-log profiles.
10. Test the public vocabulary and diagnostics with programmers who do not use
    formal-methods terminology.
11. Measure incremental build, monitoring, evidence storage, and promotion
    costs.
12. Decide which parts are compiler primitives, standard-library values,
    build-protocol messages, and external services.

## Proposed initial position

Catena should begin with a typed specification graph, honest evidence types,
first-order contracts, executable examples and properties, and a small
deterministic governance language. It should stage temporal models and
deductive proof after the semantic and usability foundations work.

The architecture should make future strength possible without overstating
today's guarantees:

- claims remain independent of their checking methods;
- evidence remains independent of authority;
- authority remains independent of technical truth;
- lifecycle remains reconstructible from history;
- external facts remain signed attestations with explicit trust; and
- every default explanation remains readable by a programmer who has not
  studied the underlying mathematics.

## Connections

- [How should Catena integrate specifications and governance into the language?](../40-inquiries/how-should-catena-integrate-specifications-and-governance-into-the-language.md)
  turns this proposal into explicit semantic, security, usability, and
  implementation tests.
- [Language-Integrated Specifications and Governance map](../10-maps/language-integrated-specifications-and-governance.md)
  provides the curated evidence and design trails.
- [An Approachable Vocabulary for Catena](approachable-language-vocabulary.md)
  supplies the behavior-first naming and diagnostic policy.
- [A Greenfield Type System for Catena](catena-greenfield-type-system.md)
  defines the inference, annotation, effect, and coherence boundaries that
  specifications must preserve.
- [Algebraic Data Types](algebraic-data-types.md) supplies invariants,
  generators, shrinkers, and schema-evolution subjects.
- [Algebraic Effects and Handlers](algebraic-effects-and-handlers.md) supplies
  capability and trace semantics for effectful claims.
- [Category Theory for Programming](category-theory-for-programming.md) and
  [Combinators for Algebraic Data and Categorical Programming](combinators-for-algebraic-data-and-categorical-programming.md)
  supply law and operational-contract subjects.

## Sources

### Contracts and proof obligations

- [Applying Design by Contract](../30-sources/meyer-1992-applying-design-by-contract.md)
- [Contracts for Higher-Order Functions](../30-sources/findler-felleisen-2002-contracts-higher-order-functions.md)
- [Dafny: An Automatic Program Verifier for Functional Correctness](../30-sources/leino-2010-dafny.md)

### Executable, bounded, and temporal claims

- [QuickCheck: A Lightweight Tool for Random Testing of Haskell Programs](../30-sources/claessen-hughes-2000-quickcheck.md)
- [Alloy: A Lightweight Object Modelling Notation](../30-sources/jackson-2002-alloy.md)
- [The Temporal Logic of Actions](../30-sources/lamport-1994-temporal-logic-actions.md)
- [An Overview of the K Semantic Framework](../30-sources/rosu-serbanuta-2010-k-semantic-framework.md)

### Lifecycle, policy, provenance, and certificates

- [Typestate: A Programming Language Concept for Enhancing Software Reliability](../30-sources/strom-yemini-1986-typestate.md)
- [Cedar: A New Language for Expressive, Fast, Safe, and Analyzable Authorization](../30-sources/cutler-et-al-2024-cedar.md)
- [in-toto: Providing Farm-to-Table Guarantees for Bits and Bytes](../30-sources/torres-arias-et-al-2019-in-toto.md)
- [Proof-Carrying Code](../30-sources/necula-1997-proof-carrying-code.md)
