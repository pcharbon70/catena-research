# Catena Implementation Limits and Portability

This policy defines the repository-wide contract for finite implementation
resources, portable minima, limit disclosure, and exhaustion reporting. It is
repository governance, not a Catena language revision: it adds no source form,
typing rule, runtime value, interface field, artifact format, or BEAM calling
convention.

Read it with [Specification Authority](SPECIFICATION-AUTHORITY.md), which
identifies language authority, and the
[Catena Conformance Vocabulary](CONFORMANCE-VOCABULARY.md), which classifies an
implementation limit as a distinct refusal of otherwise valid input. A
normative language chapter still decides whether an input is valid and what it
means; this policy decides when finite implementation resources may prevent a
conforming implementation from processing that input.

## Scope and authority

This policy governs compiler, checker, evaluator, explorer, artifact, and
runtime-capacity disclosures used in a Catena conformance claim. It applies
across all language revisions unless a later approved governance policy
explicitly replaces it. A compiler profile, test, reference evaluator, or
observed runtime behavior cannot create a limit that this policy or an
applicable normative chapter does not permit.

Every finite boundary is assigned exactly one of these roles:

- an **implementation limit** refuses otherwise valid input with a distinct
  diagnostic;
- an **evidence bound** makes a bounded analysis inconclusive without changing
  source validity or establishing a semantic counterexample;
- a **runtime capacity** describes deployment resources and failure policy
  without weakening language semantics; or
- **not applicable** records that a portable dimension is reserved but the
  current language or implementation exposes no corresponding form.

Ordinary malformed or ill-formed input remains invalid under the governing
language rule. A type error, non-exhaustive match, false claim, policy denial,
or runtime trap is not an implementation limit merely because detecting or
executing it consumes resources.

## Portable minimum contract

A portable minimum is the greatest lower bound that every conforming
implementation claims to support for the named dimension. An implementation
MUST configure an applicable limit at or above the published minimum and MAY
support a larger value. It MUST NOT claim that an input exceeded the limit when
the observed dimension is at or below its configured value.

Supporting a dimension does not override another rule. A callable within the
arity floor can still be ill-typed; a small module can still contain an invalid
definition; and a bounded analysis can still produce a specified rejection.
The minimum promises only that the named resource dimension is not itself the
reason for refusal.

The dimension's measurement point, unit, applicability, configured value, and
exhaustion outcome are part of the conformance disclosure. A configurable
value below the portable minimum is non-conforming even if it is documented.
An implementation with no applicable form reports `not_applicable` and the
checklist owner that will make the dimension applicable; it does not report an
arbitrary zero.

## Bootstrap portable minima

| Dimension | Portable minimum | Measurement and applicability | Exhaustion |
| --- | ---: | --- | --- |
| Explicit callable arity | 253 arguments | Maximum explicit source arguments after the implementation's source callable representation is normalized. The floor reserves two hidden arguments for the current effect-directed CPS worker under OTP's arity-255 boundary. | `LIM001` |
| Integer literal magnitude | 4,096 decimal digits | Digits in the mathematical integer literal value, excluding a leading minus sign, in every accepted compiler input form. | `LIM002` |
| Decoded text or binary literal payload | 65,536 bytes | Decoded payload bytes for each future string, binary, or equivalent literal. The current language has no such term literal, so the bootstrap reports this dimension not applicable under G017. | Future G017 diagnostic |
| Generated BEAM module | 1,048,576 bytes | Bytes in each generated `.beam` module before successful publication. | `LIM003` |
| Pattern usefulness and coverage | 20,000 analysis steps | Existing data-and-pattern coverage boundary. | `M004` |
| Condition normalization | 20,000 nodes or steps | Existing clause-condition normalization and transitive-inlining boundary. | `CND007` |
| Trait resolution | 20,000 solver steps | Existing trait-resolution boundary. | `TRT008` |
| Package specialization | 20,000 specialization steps | Existing package-linking boundary. | `TRT007` |
| Specification example evaluation | 20,000 semantic steps | Existing per-example evaluation boundary. | `EVD003` |
| Governance policy evaluation | 20,000 policy steps | Existing aggregate policy-evaluation boundary. | `GOV002` plus a denied action |
| Kernel S-expression input | 20,000 syntax nodes and 1,024 nesting levels | Existing exact-kernel parser boundaries. | `SYN003` |

The callable floor is deliberately below the target VM's maximum. Erlang/OTP
29 permits 255 function arguments; the current Catena effect lowering adds a
handler-state and continuation argument to an effectful worker. The 253 floor
therefore covers the least favorable current lowering without treating a pure
source function and its generated worker as separate portability promises.

The integer floor concerns input magnitude, not fixed-width runtime overflow:
Catena integers in the implemented kernels are mathematical integers. The
decoded-payload floor is reserved now so G017 cannot introduce a literal form
whose basic portability begins from an undocumented implementation accident.

## Machine-readable reporting

Every claimed implementation release MUST publish a deterministic,
machine-readable conformance profile. The profile MUST include:

- a format name and version, compiler release, target, edition, and supported
  exact language revisions;
- vendor extensions and implementation-defined choices, including explicit
  empty collections;
- applicable permissions, recommendation dispositions, and bounded
  presentation choices required by the conformance vocabulary;
- every implementation limit, evidence bound, runtime capacity, and
  not-applicable reserved dimension;
- for each finite bound, its stable identifier, classification, unit, portable
  minimum, configured value, applicability, and exhaustion outcome; and
- deployment-defined mailbox capacity and its non-negotiable semantic
  constraints.

The bootstrap command is `catena conformance-info`. It emits format
`catena-conformance-info`, version `1`, as one JSON value. The human-readable
compiler `CONFORMANCE.md` explains the same release; executable values come
from the compiler's central limit registry rather than from duplicated prose.
A difference between those disclosures is a conformance defect.

Profile key order carries no meaning. Repeated execution for one compiler
build produces equal decoded content and equal encoded bytes. A build system
MAY cache the result by immutable compiler identity, but a package cannot use
the profile to select semantics that normative text has not authorized.

## Limit diagnostics and transactional failure

An implementation-limit refusal MUST carry a stable diagnostic reserved for
the affected limit. Its structured details contain:

| Field | Meaning |
| --- | --- |
| `limit_id` | Stable profile and registry identifier for the dimension. |
| `minimum_supported` | Corpus-wide portable floor. |
| `configured` | This implementation's active bound. |
| `observed` | Measured value that crossed the configured bound. |
| `unit` | Stable measurement unit. |

The implementation measures the value before publishing the affected
successful output. A refused check or compilation publishes no new final
interface, BEAM module, package, assurance record, or partial replacement at
that transaction boundary. Diagnostic prose may improve under the bounded
presentation rules, but its identifier, structured measurement, and repair
meaning remain stable.

An implementation MUST NOT relabel exhaustion as a semantic result. `M004`
does not prove a match non-exhaustive or redundant; `CND007` does not prove a
condition unsafe; `TRT008` does not prove that an instance is absent;
`EVD003` does not provide a counterexample; and `GOV002` records exhaustion
before the required conservative denial.

## Analysis refusals and evidence bounds

The fixed 20,000-step checks above are implementation limits when their
specified outcome rejects the affected compiler or governance action. The
following bounded tools instead produce evidence and MUST remain inconclusive
on exhaustion:

| Evidence activity | Bootstrap bound | Exhaustion result |
| --- | ---: | --- |
| Condition fact construction | 20,000 formula nodes | `unknown` |
| Condition fact branch search | 20,000 analysis steps | `unknown` |
| Kernel reference execution | 20,000 small steps by default | `budget_exhausted` |
| Kernel schedule exploration | 20,000 transitions and 20,000 distinct configurations | `exhausted` |

An inconclusive result cannot reject an otherwise accepted source program,
establish a proof, supply a counterexample, declare a schedule impossible, or
authorize compiler output. A caller MAY request a higher evidence budget when
the executable interface permits it. The profile still reports the default
and portable floor used by conformance evidence.

## Runtime and mailbox capacity

Catena does not assign a portable numeric mailbox-capacity minimum. OTP mailbox
storage shares finite process and node resources, can use on-heap or off-heap
message data, and can be constrained indirectly by process heap, distribution,
container, or operating-system policy. Those values belong to the deployment
profile rather than source acceptance.

Resource pressure MUST NOT silently reorder messages from one sender,
retarget a send, or discard a message addressed to a live target while
reporting the ordinary successful-send semantics. A deployment that imposes a
quota needs an explicit admission, backpressure, process-failure, or trapping
policy at the later concurrency/runtime boundary. Process death, supervision,
distributed backpressure, and concrete mailbox quotas remain owned by G068
and G129.

The already specified send-to-dead-target behavior is not changed by this
policy. Nor does this policy promise that an operating system cannot terminate
a node. It requires conformance claims to separate those external or explicit
runtime outcomes from silent semantic variation.

## Evolution and version axes

Changing only a compiler's configured bound at or above the portable minimum
changes its implementation profile and may require a compiler-package release;
it does not create a Catena language revision. Raising a portable minimum or
adding a newly applicable dimension changes this governance policy and its
conformance evidence. Lowering a portable minimum is a portability break and
requires an explicit compatibility decision rather than an incidental profile
edit.

If a future language feature introduces a new resource dimension, its
normative area defines the measurement point, failure interaction, and
diagnostic family, while this policy records any cross-implementation floor.
The feature's language revision, its artifact formats, the compiler release,
and this profile format remain separate version axes.

C012 is therefore a repository-governance milestone. It closed G012 without
consuming a language revision. Normative C013 subsequently uses `0.1.9` for
the source-text envelope without changing C012's portability classifications;
normative C014 uses `0.1.10` for identifiers without adding a resource
dimension or changing those classifications; normative C015 uses `0.1.11` for
whitespace and layout under the same fixed resource classifications; normative
C016 uses `0.1.12` for comments and documentation comments without adding a
resource dimension; `0.1.13` is the next unused semantic patch.

## Conformance obligations

The following permanent obligations connect this policy to the
[Conformance Traceability registry](10-maps/conformance-traceability.md):

- **IL-OBL-001 — Deterministic profile.** Every claimed compiler release emits
  the required deterministic machine-readable profile.
- **IL-OBL-002 — Complete registry.** Every active finite bound and reserved
  dimension appears in one executable registry and in the profile.
- **IL-OBL-003 — Classified disclosure.** Each entry declares classification,
  unit, floor, configuration, applicability, and exhaustion outcome.
- **IL-OBL-004 — Callable floor.** Source callable arity 253 is accepted and
  254 is refused as `LIM001`; generated effect workers may reach arity 255.
- **IL-OBL-005 — Integer floor.** Both current frontends accept 4,096 decimal
  digits and refuse 4,097 as `LIM002`.
- **IL-OBL-006 — Literal-payload reservation.** The 65,536-byte decoded literal
  floor is reported not applicable until G017 introduces such literals.
- **IL-OBL-007 — Module floor.** A generated BEAM module up to 1,048,576 bytes
  crosses no module-size limit; the next byte is refused as `LIM003`.
- **IL-OBL-008 — Refusal-bound distinction.** Existing compiler and governance
  refusal budgets retain their specified limit diagnostics and outcomes.
- **IL-OBL-009 — Evidence-bound distinction.** Evidence exhaustion remains
  `unknown`, `budget_exhausted`, or `exhausted`, never a semantic rejection.
- **IL-OBL-010 — Mailbox disclosure.** Mailbox capacity is deployment-defined
  and reports the live-target ordering, targeting, and delivery constraints.
- **IL-OBL-011 — Structured transactional failure.** Limit refusals report all
  common measurement fields before any successful final output is published.
- **IL-OBL-012 — Version separation.** C012 changes governance and compiler
  conformance behavior without creating language revision `0.1.9`.

## Research route

The rationale and rejected alternatives are developed in
[Catena Implementation Limits and Portability](20-notes/catena-implementation-limits-and-portability.md).
The [resolved inquiry](40-inquiries/how-should-catena-bound-implementation-limits.md),
[topic map](10-maps/implementation-limits-and-portability.md), and
[C012 evidence record](50-journal/2026-08-17-c012-implementation-limits.md)
preserve the evidence trail and coordinated compiler identity.
