# Catena Conformance Vocabulary

This policy defines how every normative Catena chapter expresses requirements,
classifies failure and permitted variation, and supports implementation
conformance claims. It is repository governance, not a Catena language
revision: it changes no source form, static or runtime semantics, interface,
artifact, signature, CLI, or BEAM format.

Read this policy together with
[`SPECIFICATION-AUTHORITY.md`](SPECIFICATION-AUTHORITY.md). That document says
which material is normative and how conflicts are resolved; this document says
what conformance words and behavior classes mean inside that material. A
normative chapter is binding even when it states a rule in plain declarative
prose without an uppercase keyword.

## Canonical requirement words

Catena normative text has exactly five uppercase requirement words:

| Word | Meaning |
| --- | --- |
| `MUST` | The stated behavior is an absolute conformance requirement. |
| `MUST NOT` | The stated behavior is absolutely prohibited. |
| `SHOULD` | The stated quality property or implementation technique is recommended; a conforming deviation needs a published justification. |
| `SHOULD NOT` | The stated quality property or implementation technique is discouraged; choosing it needs a published justification. |
| `MAY` | The stated form, option, metadata, or technique is permitted. Omitting it also conforms unless another rule requires it. |

Only the uppercase forms have these specialized meanings. Lowercase “must,”
“should,” and “may” retain their ordinary English meanings. The uppercase
aliases `SHALL`, `SHALL NOT`, `REQUIRED`, `RECOMMENDED`, `NOT RECOMMENDED`, and
`OPTIONAL`, and similar substitutes, are prohibited in normative material.
This deliberately uses the capitalization clarification of
[RFC 8174](30-sources/leiba-2017-rfc-8174.md) while selecting a smaller
Catena-specific keyword set than [RFC 2119](30-sources/bradner-1997-rfc-2119.md).

`SHOULD` and `SHOULD NOT` are restricted to implementation technique,
diagnostic usefulness, performance, maintainability, or another quality
property. A deviation is recorded in the implementation profile with its
rationale and tracking issue. A recommendation can never make safety,
acceptance, runtime values, evaluation order, effects, artifact meaning, or
another observable language semantic optional; those boundaries use `MUST`,
`MUST NOT`, or a plain declarative rule.

`MAY` does not by itself mean “implementation-defined.” It can grant a program
or package permission, expose an explicit implementation option, permit
optional non-semantic metadata, or allow an implementation technique. If the
choice changes behavior that this policy classifies as implementation-defined,
the chapter also follows the declaration and profile rules below.

## Behavior classes

| Class | Catena meaning |
| --- | --- |
| **Required** | The specified behavior is mandatory, whether expressed declaratively or with `MUST`. |
| **Invalid** | The affected input or action must fail without publishing successful outputs. Malformed and ill-formed inputs are invalid subcategories. |
| **Implementation-defined** | The specification enumerates allowed observable choices and each implementation publishes its selection in a conformance profile. Catena currently defines no such choices. |
| **Unspecified presentation** | A bounded presentation or internal-strategy variation need not be selected in a profile, but it cannot change acceptance, safety, runtime values, order, effects, stable diagnostic identity, governance, or artifact identity. |
| **Implementation limit** | An otherwise valid input is refused with a distinct limit diagnostic under the portable-floor and reporting contract in `IMPLEMENTATION-LIMITS.md`. |
| **Explicit runtime failure or trap** | A named runtime condition has specified abrupt behavior. It is part of Catena semantics, never a license for arbitrary behavior. |

### Invalid input and actions

Invalid is the umbrella failure class. A malformed input cannot be decoded or
does not satisfy its required grammar, schema, or structural shape. An
ill-formed input has enough structure to decode but violates a static,
formation, scope, typing, evidence, policy, or other conformance rule. A
chapter can use the narrower term when it improves diagnosis; both remain
invalid.

The applicable diagnostics chapter assigns the stable diagnostic family.
Failure leaves no newly published or partially replaced final output for the
affected action. Invalid input does not authorize a compiler, verifier,
runtime, or foreign adapter to continue with arbitrary values or effects.

### Implementation-defined choices

An implementation-defined choice is permitted only where a normative chapter:

1. uses the visible callout defined below;
2. enumerates the complete set or bounded domain of conforming choices;
3. states which observations can differ; and
4. requires the selected choice to appear in the implementation's conformance
   profile before that implementation claims conformance.

Specification silence is not an implementation-defined choice. Neither a
compiler's existing behavior nor a profile can create a choice that normative
text has not authorized.

### Unspecified presentation

Unspecified presentation is intentionally narrower than the “unspecified
behavior” classes used by some systems standards. The governing paragraph
states a finite set or equivalence relation that bounds the variation. Typical
uses include alpha-renamed type variables or ordering of equivalent
constraint explanations.

The variation cannot affect whether input is accepted, whether execution is
safe, runtime values or effects, evaluation order, stable diagnostic family,
governance decisions, or exact artifact identity. If any of those can vary,
the text must instead define one required result, define an explicit input or
configuration option, or introduce a properly profiled
implementation-defined choice.

### Implementation limits

Exceeding an implementation limit is not ordinary invalidity: the input would
otherwise satisfy the language rules. The implementation reports a diagnostic
reserved for limit exhaustion and must not relabel the refusal as a semantic
error such as non-exhaustiveness, false evidence, or policy denial. Current
bootstrap limits are disclosed in its conformance profile. Checklist item G012
is complete as C012 through
[Catena Implementation Limits and Portability](IMPLEMENTATION-LIMITS.md), which
governs the general set, portable minima, permitted variation, common
diagnostic fields, and machine-readable reporting.

### Explicit runtime failure and traps

A runtime failure or trap is specified behavior. Its governing rule identifies
the triggering condition, which effects occur before failure, and whether the
current computation or a wider runtime scope terminates. The WebAssembly Core
Specification provides useful evidence for making validation and traps
explicit, but [its model](30-sources/rossberg-2026-webassembly-core-specification.md)
does not itself define Catena behavior.

## No undefined behavior

Catena has no undefined behavior. Omission of a rule is a specification defect
and supplies no conforming interpretation. This explicitly rejects the C model
in which certain violated requirements or specification silence can leave
behavior undefined, while retaining its useful separation of documented
choices, unspecified values, and implementation limits as comparative
evidence in [WG14 N1570](30-sources/wg14-2011-n1570.md).

Invalid input must fail as defined above; it never releases an implementation
from safety or output-transaction obligations. Every runtime fault is either
outside the currently specified language boundary or is an explicit Catena
failure or trap. Any future foreign, unsafe, intrinsic, or unchecked facility
must state its rejection, failure, or trapping behavior before it can become
normative.

## Visible variability declarations

Use these rendered callouts in normative chapters:

- `> **Normative implementation-defined choice.**`
- `> **Normative unspecified presentation.**`

The label applies to the immediately following paragraph or table. An
implementation-defined paragraph enumerates the choices, observations, and
profile obligation. An unspecified-presentation paragraph contains the words
“bounded unspecified presentation” and states its bound. Directory indexes
summarize all `MAY`, `SHOULD`, presentation, and limit clauses in a
`## Variability register`; the register helps navigation but cannot alter the
chapter rule.

## Conformance profiles

Every claimed compiler release publishes a versioned implementation profile.
The profile records at least its format, compiler release, target, supported
editions and revisions, vendor extensions, implementation-defined choices,
normative `MAY` dispositions, `SHOULD` and `SHOULD NOT` deviations,
implementation limits, and bounded unspecified presentation.

The bootstrap compiler currently publishes a human-readable format-1 profile,
has zero implementation-defined choices and zero vendor extensions, and emits
the deterministic machine-readable `catena conformance-info` format required
by C012. The first normative implementation-defined choice must appear in both
profile forms with conformance tests before any compiler can claim that choice.

Profiles describe implementations; they never amend language authority. A
profile cannot excuse a violated `MUST`, weaken safety or observable semantics
through a recommendation deviation, or turn an extension into standard
Catena.

## Research route

The comparative evidence, rejected alternatives, and resulting model are
developed in [Catena Conformance Vocabulary and Behavior Classes](20-notes/catena-conformance-vocabulary-and-behavior-classes.md).
The [resolved inquiry](40-inquiries/how-should-catena-classify-conformance-behavior.md),
[topic map](10-maps/catena-conformance-vocabulary.md), and
[C009 record](50-journal/2026-08-05-c009-conformance-vocabulary.md) preserve the
decision and corpus audit. The cross-cutting limit model continues through the
[C012 policy](IMPLEMENTATION-LIMITS.md) and
[implementation-limits map](10-maps/implementation-limits-and-portability.md).
