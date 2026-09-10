# Catena Specification Authority

This policy defines how to identify and interpret Catena's normative language
specification. It governs documents and conformance evidence; it is not a
Catena language edition and does not add source syntax, static semantics, or
runtime behavior. The companion
[Catena Conformance Vocabulary](CONFORMANCE-VOCABULARY.md) defines requirement
words, behavior classes, variability declarations, and implementation-profile
obligations inside the normative material identified here. The companion
[Catena Implementation Limits and Portability](IMPLEMENTATION-LIMITS.md)
policy defines portable minima, finite-resource reporting, and exhaustion
obligations without adding language semantics.

## Authority classes

Only a document under [`60-specification/`](60-specification/README.md) with
both `kind: specification` and `status: normative` is a normative language
chapter. Its declarative prose, tables, grammar, equations, judgments, and
explicit conformance obligations define what conforming programs and
implementations must do, except where material is visibly marked
non-normative.

The following are not normative language definitions:

- specification chapters whose status is `draft` or `candidate`;
- directory READMEs, maps, notes, source notes, inquiries, and journals;
- rationale, proof sketches, evidence reports, connections, and illustrative
  examples marked non-normative inside a normative chapter;
- templates, guides, the language tour, and repository documentation;
- executable reference evaluators, compiler implementations, tests, generated
  artifacts, and recorded conformance runs.

This document is authoritative for document classification and conflict
handling, while `CONFORMANCE-VOCABULARY.md` is authoritative for conformance
wording and behavior classification, and `IMPLEMENTATION-LIMITS.md` is
authoritative for the cross-implementation portability floor. All three are
repository governance rather than normative Catena language chapters.
`AGENTS.md`, the specification template, and the archive validator implement
these policies.

## Status and applicability

Frontmatter is the status source of truth. Descriptive text in an index or
guide cannot promote a chapter. Promotion requires changing the chapter to
`status: normative` together with the evidence and indexes required by the
repository workflow.

A chapter applies only within the scope and exclusions stated by its
specification area. A larger `spec_version` does not automatically replace an
older rule. Normative C008 defines cumulative same-edition applicability and
requires an explicit lifecycle and migration record for replacement,
deprecation, or removal. A later chapter therefore overrides an earlier
chapter only when normative text explicitly states that relationship.

If two apparently applicable normative chapters disagree and neither contains
that relationship, the specification is defective. The disputed behavior has
no conforming interpretation until the conflict is repaired.

## Prototype slice identifiers

`spec_version` uses exact `major.minor.patch` syntax. The current prototype
language line is `0.1`; its registered semantic boundaries are:

| Boundary | Version | Status |
| --- | --- | --- |
| C001 type system | `0.1.1` | normative |
| C002 data and patterns | `0.1.2` | normative |
| C003 clause conditions | `0.1.3` | normative |
| C004 traits and categorical operations | `0.1.4` | normative |
| C005 effects and handlers | `0.1.5` | normative |
| C006 specifications and governance | `0.1.6` | normative |
| C008 editions and feature lifecycle | `0.1.7` | normative |
| C010 formal semantic kernel | `0.1.8` | normative |
| C013 source text | `0.1.9` | normative |
| C014 identifiers | `0.1.10` | normative |
| C015 whitespace and layout | `0.1.11` | normative |
| C016 comments and documentation comments | `0.1.12` | normative |
| C017 literal grammar | `0.1.13` | normative |
| C018 numeric literal semantics | `0.1.14` | normative |
| C019 operators and punctuation | `0.1.15` | normative |
| C020 files and modules | `0.1.16` | normative |
| C021 namespaces and shadowing | `0.1.17` | normative |
| C022 imports and exports | `0.1.18` | normative |
| C023 abstraction boundaries | `0.1.19` | normative |
| C024 module dependency cycles | `0.1.20` | normative |
| C025 package identity and dependencies | `0.1.21` | normative |
| C026 prelude policy | `0.1.22` | normative |
| C027 entry points and application structure | `0.1.23` | normative |
| C028 API and ABI compatibility | `0.1.24` | normative |
| C029 values and evaluation | `0.1.25` | normative |
| C030 evaluation order | `0.1.26` | normative |
| C031 bindings and sequencing | `0.1.27` | normative |
| C032 functions and calls | `0.1.28` | normative |
| C033 conditionals and branching | `0.1.29` | normative |
| C035 equality and ordering | `0.1.30` | normative |
| C034 recursion and termination | `0.1.31` | normative |
| C036 runtime failure taxonomy | `0.1.32` | normative |
| C037 resource observability | `0.1.33` | normative |
| C038 compile-time evaluation | `0.1.34` | normative |
| C040 built-in data model | `0.1.35` | normative |
| C041 structural records and variants | `0.1.36` | normative |

Governance milestones C007, C009, and C012 apply across the normative corpus
and do not occupy language revisions. Normative C010 occupies `0.1.8`, and
normative C013 occupies `0.1.9`; normative C014 occupies `0.1.10`; normative
C015 occupies `0.1.11`; normative C016 occupies `0.1.12`; normative C017
occupies `0.1.13`; normative C018 occupies `0.1.14`; normative C019
occupies `0.1.15`; normative C020 occupies `0.1.16`; normative C021
occupies `0.1.17`; normative C022 occupies `0.1.18`; normative C023 occupies `0.1.19`; normative C024 occupies `0.1.20`; normative C025 occupies `0.1.21`; normative C026 occupies `0.1.22`; normative C027 occupies `0.1.23`; normative C028 occupies `0.1.24`; normative C029 occupies `0.1.25`; normative C030 occupies `0.1.26`; normative C031 occupies `0.1.27`; normative C032 occupies `0.1.28`; normative C033 occupies `0.1.29`; normative C035 occupies `0.1.30`; normative C034 occupies `0.1.31`; normative C036 occupies `0.1.32`; normative C037 occupies `0.1.33`; normative C038 occupies `0.1.34`; normative C040 occupies `0.1.35`; normative C041 occupies `0.1.36`; a
later semantic slice begins at `0.1.37`. Each later
prototype semantic slice uses
the next unused `0.1.n` patch until an approved policy replaces this
convention.
This sequence identifies language slices and the Catena protocol boundaries
that name them. It is independent of compiler-package releases and third-party
dependency versions. It also does not make a larger patch automatically
applicable or authoritative.

The normative 0.1.7 chapters distinguish edition, language revision, artifact
format, and compiler-package release, and define applicability within the
retained `0.1` edition.

The previous two-component identifiers remain visible only where a historical
record describes bytes emitted by an immutable compiler commit. They are not
current language or protocol aliases. C008 defines the end-user edition,
compatibility, deprecation, preview, and migration policy.

The [selective-receive correction](60-specification/selective-receive-correction/waiting-and-scan-cost-amendment.md)
occupies `0.1.49` after C082 `0.1.48`. Its explicit replacement of the
conflicting C086 waiting/cost rule applies at `0.1.49` and inherited later
same-edition selections; it does not retroactively amend `0.1.46`.

The [closed capability-kernel target](60-specification/closed-capability-kernel/identity-rows-and-comprehension-target.md)
occupies `0.1.50`. Its explicit replacement of the dormant comprehension
target does not reinterpret old source, interfaces or signed formats.

The [owned-resource target](60-specification/resource-scopes/owned-lifetime-and-mandatory-cleanup.md)
occupies `0.1.51`. Its explicit cleanup replacement applies only to that
compound target; retained formats and foreign admission remain unchanged.

The [process-lifetime target](60-specification/process-lifetimes/owned-tasks-and-managed-relationships.md)
occupies `0.1.52`. It adds explicit owned children and managed relationships
without changing raw spawn or admitting general time, supervision or foreign
ownership.

The [cancellation/time target](60-specification/cancellation-and-time/deadlines-waits-and-cancellation.md)
occupies `0.1.53`. It fills prior timeout reservations only within that compound
target and preserves exact `0.1.52` admission, old interfaces and signed formats.

The [outcome contract](60-specification/outcome-contracts/values-sequencing-and-validation.md) occupies `0.1.54`. It adds explicit ordinary library meanings without a new executable frontend or persisted format.

The [local protocol contract](60-specification/local-protocol-contracts/schemas-sessions-and-outcomes.md) occupies `0.1.55`. It adds an exact checked library-application boundary and preserves old kernel interfaces and signed formats.

The [typed supervision contract](60-specification/typed-supervision/checked-trees-and-lifecycle.md) occupies `0.1.56`, admitting checked static worker descriptions and a narrow owned OTP lifecycle adapter while preserving existing interface and signed formats.

The [OTP compatibility policy](60-specification/otp-compatibility/support-probes-and-artifacts.md) occupies `0.1.57`. It binds new artifacts to tested toolchains without adding an executable frontend or changing retained source/interface formats.

The [value-boundary contract](60-specification/value-boundaries/carriers-and-checked-conversion.md) occupies `0.1.58`. It admits an exact pure value-tree target and checked representation conversion while preserving retained source, interface and signed formats.
The [calling-convention contract](60-specification/calling-conventions/checked-calls-and-artifact-identity.md) occupies `0.1.59`. It adds exact build-bound calling sidecars, staged checked closures, synchronous data callbacks and retained lifecycle call descriptions; historical inputs and persisted interface/signed formats remain distinct.
The [Erlang type-boundary contract](60-specification/erlang-type-boundary/typed-conversion-and-preservation.md) occupies `0.1.60`. It adds explicit typed codecs, full-carrier validation and verified nominal sequence bridges without adding a dynamic type or new persisted/executable format.

The [foreign-adapter milestone](60-specification/foreign-adapters/authority-calls-and-callback-lifetime.md) occupies `0.1.61`. It adds explicit trusted grants, scoped pure callbacks and a checked capability-program artifact. P096 retains its later surface and broader callback gates.

The [native-value role contract](60-specification/native-value-roles/typed-admission-and-native-identity.md) occupies `0.1.62`. It adds registered borrowed process-send and fresh-reference roles and a complete native-kind inventory. No retained artifact or persisted format is widened.
The [native service contract](60-specification/native-services/signed-loading-and-owned-execution.md) occupies `0.1.63`, with separate signed native envelope format `1`, explicit native trust and owned port/NIF execution. It does not widen retained Catena artifact or governance formats.
The [debugging metadata contract](60-specification/debugging-metadata/verified-origins-and-redacted-frames.md) occupies `0.1.64`, including a debug executable/artifact profile and externally verified source/evidence sidecars. Retained interfaces and signed-governance formats are unchanged.



The [collection protocol contract](60-specification/collection-protocols/finite-families-and-owned-pulls.md) occupies `0.1.65`, using a separate ordinary nominal package, checked finite operations and owned pulls. Retained source, executable, interface and signed formats are unchanged.

The [text/binary contract](60-specification/text-binary-model/units-unicode-and-checked-binary-operations.md) occupies `0.1.66`, including explicit index units, pinned Unicode operations and a checked text-program artifact. Historical source, interface and signed formats are unchanged.

## Normative and non-normative material

Normative chapter content is normative by default. A plain declarative rule is
binding even when it does not use an uppercase requirement word. Requirement
force, invalidity, implementation-defined choices, bounded unspecified
presentation, implementation limits, explicit failures, and the prohibition
on undefined behavior follow the
[Catena Conformance Vocabulary](CONFORMANCE-VOCABULARY.md).

Use visible rendered labels rather than hidden comments:

- End a non-normative section heading with `(non-normative)`.
- Introduce an exact grammar, judgment, schema, state transition, or other
  defining fenced block with `> **Normative definition.**`.
- Introduce an example that imposes an acceptance, rejection, diagnostic, or
  observable-result obligation with
  `> **Normative conformance example.**`.
- Introduce an enumerated, profiled implementation-defined choice with
  `> **Normative implementation-defined choice.**`.
- Introduce a bounded presentation or internal-strategy equivalence class with
  `> **Normative unspecified presentation.**`.
- Introduce local explanatory material with one of
  `> **Non-normative example.**`, `> **Non-normative rationale.**`,
  `> **Non-normative note.**`, `> **Non-normative diagram.**`, or
  `> **Non-normative evidence.**`.

A fenced block in a specification chapter must either follow the applicable
definition, conformance-example, or non-normative callout or appear inside a
section marked non-normative. That label applies to the immediately following
block. The two variability labels instead apply to the immediately following
paragraph or table and carry the additional requirements in the conformance
policy. Non-normative material may explain a rule but cannot add a requirement,
narrow or widen its domain, resolve an ambiguity, or override normative text.

Source notation is an illustrative example unless a normative chapter
explicitly classifies it as a normative definition or conformance example.
Commands used to reproduce a compiler run and diagrams used to explain a
pipeline are evidence or explanation, not language semantics.

## References and traceability

A conflict report, test description, compiler comment, or evidence record must
identify the governing rule with a document link and heading anchor, for
example `syntax-and-safety.md#evaluation`. A chapter-only citation is
insufficient when more than one heading could govern the behavior.

This policy does not assign a permanent identifier to every individual rule.
Checklist item C011 (formerly P011) delivered exhaustive rule-to-test
traceability through the `AREA-OBL-NNN` obligation identifiers; any later stable
rule identifier scheme extends it.

## Conflict resolution

The normative specification is the sole authority when artifacts disagree:

| Disagreement | Required interpretation and action |
| --- | --- |
| Normative chapter versus compiler | The compiler is non-conforming for that rule; repair it and add regression evidence. |
| Normative chapter versus test | The test is incorrect or stale; repair it without changing the rule implicitly. |
| Normative chapter versus executable reference | The reference implementation is incorrect or incomplete; it has no fallback authority. |
| Compiler versus test or reference | Consult the cited normative heading; none of the executable artifacts wins by itself. |
| Two applicable normative chapters | Block the affected conformance claim until normative text explicitly resolves applicability or replacement. |
| Normative silence or ambiguity | Record a specification gap; no compiler, test, guide, or reference behavior may silently fill it. |

A formal semantic definition written in a normative chapter is part of the
specification. A program that implements or approximates that definition is
executable evidence and remains independently fallible.

While a conflict is open, a project may report the observed behavior and the
disagreement, but it must not claim conformance for the disputed rule.

## Repair and promotion workflow

1. Cite the exact normative document and heading, the conflicting artifact,
   and the observable disagreement.
2. Determine whether the defect is in an implementation, test, executable
   reference, explanatory document, or the normative text itself.
3. Repair non-normative artifacts to agree with unchanged normative text, or
   approve an explicit normative replacement before treating changed language
   behavior as accepted.
4. Update affected conformance cases, reference paths, compiler behavior,
   guides, indexes, and evidence records together.
5. Run archive validation and every affected implementation suite before
   restoring a conformance claim.

Compiler behavior alone never changes Catena. Passing tests demonstrate
evidence against specified obligations; they do not promote a candidate,
settle an ambiguity, or amend a normative chapter.

## Deliberately separate work

This policy leaves the following questions open:

- C008 defines editions, compatibility, deprecation, and replacement
  lifecycle; future edition retirement and broader API/ABI policy remain
  separately tracked.
- C012 defines which implementation limits may vary, their portable minima,
  and machine-readable reporting; C009 defines their behavior class.
- C011 (formerly P011) connects every normative rule to executable evidence
  through its permanent obligation identifiers.

Those items may extend this policy, but evidence must continue to remain
distinct from language authority.

C105 uses `0.1.67` for the [numeric library](60-specification/numeric-library/checked-arithmetic-and-explicit-rounding.md), including checked arithmetic, explicit rounding and exact executable adoption.

C106 uses `0.1.68` for [environmental effects](60-specification/environmental-effects/explicit-authority-and-closed-launches.md), explicitly amending C027/C082 for a typed authority parameter while retaining closed effects and historical entry rules.

C101 uses `0.1.69` for the [minimum prelude](60-specification/minimum-prelude/explicit-minimum-and-component-identity.md), including exact component assembly, ordinary foundations and explicit selection without new public vocabulary.

C126 uses `0.1.70` for the [trusted computing base](60-specification/trusted-computing-base/guarantees-assumptions-and-boundary-checks.md), disclosing guarantee-specific dependencies and executable source/data inventory without claiming a proof-verified compiler.

C127 uses `0.1.71` for [trusted obligation policy](60-specification/trusted-obligation-policy/transitive-disclosure-and-scoped-admission.md), a separate exact sidecar and scoped admission contract retaining C067 exclusions.

C131 uses `0.1.72` for [secret capabilities](60-specification/secret-capabilities/sealed-values-and-protected-delivery.md), with sealed credential delivery and protected observations.

C128 uses `0.1.73` for [reproducible builds](60-specification/reproducible-builds/exact-inputs-and-canonical-packages.md), an exact input and canonical full-output packaging contract.

C130 uses `0.1.74` for [signed registry and immutable acquisition](60-specification/supply-chain-policy/signed-registry-and-immutable-acquisition.md), separating authenticated immutable content from availability, replay and governance decisions.

C129 uses `0.1.75` for [aggregate budgets and runtime admission](60-specification/resource-exhaustion/aggregate-budgets-and-runtime-admission.md), with transactional compiler ceilings, explicit bounded queues, and declared host-fatal residuals.
C091 uses `0.1.76` for [typed authenticated distribution](60-specification/distribution/typed-authenticated-transport.md), with exact endpoint identity, bounded schema-directed frames, mutual authentication, compatibility refusal, and explicit partition uncertainty.
C085 uses `0.1.77` for [integrated message semantics](60-specification/message-semantics/values-capacity-and-transport.md), composing local send, checked immutable values, bounded admission, native send authority, and remote delivery outcomes.
C090 uses `0.1.78` for [scheduler observability](60-specification/scheduler-observability/policy-classes-and-visible-limits.md), with nondeterministic scheduling, unobservable reductions, deployment priorities, classified foreign work, and bounded blocking admission.
C092 uses `0.1.79` for [checked hot code upgrade](60-specification/hot-code-upgrade/checked-migration-and-activation.md), with exact preflight identity, explicit quiescence, bounded typed migration, one draining generation, and limited rollback.
C116 uses `0.1.80` for [long-term evolution](60-specification/long-term-evolution/historical-replay-and-migration.md), with exact historical interpreters, deterministic adjacent migration, immutable input retention, and explicit nonportable replay outcomes.
C121 uses `0.1.81` for the [build system and package manager](60-specification/build-system/project-graphs-acquisition-and-offline-builds.md), with exact workspace graphs, verified acquisition, transitive content-addressed caching, offline retained compilation, constrained generators, and transactional publication.
C136 uses `0.1.82` for the [bounded compatibility suite](60-specification/compatibility-suite/layered-matrix-and-edition-policy.md), with separate source, interface, dependency, data, toolchain, historical-signature, and runtime-upgrade oracles and explicit finite claim scope.
C133 uses `0.1.83` for [integrated reference observations](60-specification/reference-evaluator/common-observations-and-bounded-models.md), adapting independent semantic machines into one bounded value, terminal, event, lifetime, exhaustion, and unsupported-result contract without claiming proof.
