---
title: "Catena Conformance Vocabulary and Behavior Classes"
kind: note
created: "2026-08-05"
maturity: developing
tags:
  - governance
  - language-design
  - program-semantics
  - specification
aliases:
  - "Catena conformance model"
  - "Catena behavior taxonomy"
---

# Catena Conformance Vocabulary and Behavior Classes

## Executive conclusion

Catena should use a small uppercase requirement vocabulary—`MUST`, `MUST NOT`,
`SHOULD`, `SHOULD NOT`, and `MAY`—and a separate behavior taxonomy. Requirement
words state normative force. Behavior classes say what kind of obligation or
variation a rule creates. Conflating the two would make every optional source
form look implementation-defined and make every failure sound like a runtime
trap.

The resulting policy gives invalid inputs deterministic failure, permits only
bounded presentation variation without profiling, requires every real
implementation-defined choice to be enumerated and published, distinguishes
resource refusal from semantic invalidity, and treats runtime failure as
explicit behavior. Catena has no undefined behavior: silence is a
specification defect, not an implementation license.

## Scope and operational standard

The question is not merely which words sound conventional. A useful model must
let a reader decide, for any normative sentence:

1. whether the rule binds programs, implementations, or both;
2. whether a rejected input is malformed, ill-formed, or limited;
3. whether implementations can differ and where that choice is disclosed;
4. which observations remain invariant; and
5. whether a runtime failure has defined effects and extent.

The model succeeds only if the current 0.1.1–0.1.7 corpus can be audited
without inventing accidental implementation-defined semantics, if validator
tests catch forbidden ambiguity, and if the bootstrap compiler can truthfully
publish its choices and recommendation deviations.

## Evidence from requirement-word standards

[RFC 2119](../30-sources/bradner-1997-rfc-2119.md) supplies the useful force
distinction among absolute requirements, recommendations with understood
exceptions, and genuinely optional behavior. Its larger synonym set is less
useful for Catena: allowing both `MUST` and `SHALL`, or both `MAY` and
`OPTIONAL`, increases prose variation without adding meaning.

[RFC 8174](../30-sources/leiba-2017-rfc-8174.md) resolves the capitalization
ambiguity: uppercase words receive the specialized standards meaning;
lowercase words remain ordinary English; and normative prose need not contain
a keyword at all. Catena adopts all three points. This preserves direct
declarative rules such as “evaluation proceeds left to right” without forcing
mechanical `MUST` insertion into every sentence.

Catena narrows recommendations further. A `SHOULD` can guide diagnostic
quality, implementation technique, performance, or maintainability. It cannot
make acceptance, safety, runtime values, order, effects, or artifact meaning
optional. Each deviation belongs in the implementation profile, making a
recommendation auditable instead of aspirational.

## Evidence from language specifications

[WG14 N1570](../30-sources/wg14-2011-n1570.md) usefully distinguishes
implementation-defined values, unspecified values, traps, translation limits,
and conformance obligations. It also demonstrates the risk Catena rejects: C
can assign undefined behavior to violated requirements outside constraints and
even to omitted behavior definitions. That model supports optimization and a
wide implementation range, but it is incompatible with Catena's safety and
governance goals. Catena borrows the distinctions, not the undefined-behavior
escape hatch.

The [WebAssembly Core Specification](../30-sources/rossberg-2026-webassembly-core-specification.md)
shows a different useful decomposition: binary/text well-formedness,
declarative validation, explicit execution rules, explicit traps, and a
separate account of implementation limitations. Its traps abort a specified
computation; they do not mean that anything can happen. WebAssembly still
allows implementation-specific errors and some explicitly nondeterministic or
host-defined outcomes, so Catena must state its own narrower boundaries.

## The two-layer model

### Normative force

`MUST` and `MUST NOT` mark absolute requirements and prohibitions. `SHOULD` and
`SHOULD NOT` mark profile-audited quality or technique recommendations. `MAY`
grants a permission. Plain declarative rules are equally binding. Uppercase
synonyms are prohibited so the corpus has one spelling per force.

### Behavior class

Required behavior fixes a result or obligation. Invalid behavior covers
inputs and actions that must fail transactionally; malformed and ill-formed
are diagnostic subcategories. Implementation-defined behavior is an
enumerated observable choice published in a profile. Unspecified presentation
is a bounded equivalence class that cannot affect semantics, stable diagnostic
identity, governance, or artifact identity. Implementation limits refuse
otherwise valid input under a distinct diagnostic. Runtime failures and traps
are explicit semantic outcomes.

This separation explains why a `MAY` does not automatically create an
implementation-defined choice. “Named fields MAY be written in any order” is
a source-program permission with fixed evaluation semantics. “The compiler
MAY consume interfaces during checking” is an optional tool path. “The backend
MAY use a verified direct fold lowering” is a technique whose observations are
already constrained. A true implementation-defined choice would instead let
an implementation select among multiple observable language outcomes and
would need the dedicated callout and profile entry.

## Invalidity and output transactions

The current specifications use “invalid” broadly for type, scope, coverage,
evidence, signature, lifecycle, and policy failures. C009 makes the shared
consequence precise: the affected input or action fails and cannot publish a
successful final output. “Malformed” identifies a structural/decoding failure;
“ill-formed” identifies a decoded input that violates a formation or semantic
constraint. Neither subcategory permits continued arbitrary compilation or
execution.

Stable diagnostic families remain owned by each specification area. The
central policy does not flatten useful distinctions such as `M001`, `T009`,
`CND005`, or `GOV004`; it supplies their common failure contract.

## Variability and implementation profiles

Area-level variability registers make optional clauses reviewable without
moving authority out of chapters. The bootstrap profile then records actual
implementation dispositions: optional export-signature suggestions are
absent, legacy selection inference and interface consumption are enabled,
compact ADT layout is the default with explicit uniform mode, GADT equality
coverage is enabled, generated folds use the ordinary verified lowering path,
and selection metadata and claim summaries are emitted.

The same profile records all five substantive current recommendations and any
deviation. This is valuable even with zero implementation-defined choices: it
separates conformance requirements from implementation quality debt. A
machine-readable profile is deliberately deferred until the first real
implementation-defined choice creates a selection that tooling must inspect.

## Rejected alternatives

- Importing all BCP 14 synonyms would produce multiple spellings for the same
  force and complicate validation.
- Treating lowercase requirement words as keywords would make ordinary
  explanatory prose ambiguous.
- Calling every `MAY` implementation-defined would misclassify programmer
  permissions, explicit CLI options, metadata, and semantics-preserving
  techniques.
- Using broad “unspecified behavior” would allow variation to leak into
  acceptance, runtime semantics, diagnostics, or artifacts.
- Treating specification silence as undefined behavior would let the compiler
  become accidental language authority.
- Rewriting programmer diagnostics in formal conformance terminology would
  weaken the established behavior-first vocabulary.

## Falsification criteria and open work

The model fails if two conforming implementations can disagree on acceptance,
safety, runtime values/order/effects, stable diagnostic identity, governance,
or artifact identity under a clause labelled only unspecified presentation.
It also fails if a `SHOULD` deviation changes observable language semantics or
if an invalid action can leave a successful output.

G012 still needs to decide which implementation limits may vary and the
portable minima for future language areas. C011 (formerly P011) delivered
exhaustive rule-to-test traceability. P117, P125, and G138 retain diagnostic
provenance, migration application, and performance work exposed by the current
recommendation audit.

## Connections

- [Catena Conformance Vocabulary](../CONFORMANCE-VOCABULARY.md) is the adopted
  repository policy.
- [How Should Catena Classify Conformance Behavior?](../40-inquiries/how-should-catena-classify-conformance-behavior.md)
  records the bounded resolution.
- [Catena Conformance Vocabulary map](../10-maps/catena-conformance-vocabulary.md)
  routes through evidence, policy, audit, and implementation profile.
- [C009 Conformance Vocabulary](../50-journal/2026-08-05-c009-conformance-vocabulary.md)
  records the corpus and validator results.
