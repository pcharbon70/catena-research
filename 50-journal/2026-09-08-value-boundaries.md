---
title: "Value Boundary Workbench"
kind: journal
created: "2026-09-08"
tags:
  - language-design
  - representation-independence
  - beam-vm
aliases: []
---

# Value Boundary Workbench

## Starting point

C099 merged through [compiler PR 139](https://github.com/pcharbon70/catena/pull/139)
and [research PR 89](https://github.com/pcharbon70/catena-research/pull/89).
Compiler `rewrite` synchronized at `0065b3b447f05203a8304ce1831a148e7468f01e`;
research `main` synchronized at `d2843db6502129468e97e174b4f536cb5b9d34b6`.
Both feature branches were deleted after synchronization. Work begins on
`codex/value-boundaries`; P093 remains open and no new revision is admitted yet.

The [CP-093 plan](../20-notes/language-completion-plan-delivery.md#item-093-catena-to-beam-value-mapping)
selects verified per-type layouts, checked ingress and scoped opaque handles.
The [standing nominal representation rule](../60-specification/data-and-patterns/interfaces-and-representation.md)
requires semantic observations to agree across compact and uniform layouts.

## Implementation decisions

| Decision | Four alternatives explored | Recommended and selected |
| --- | --- | --- |
| VB-I01 | A: validate literal payloads independently of recorded type annotations; B: trust an integer tag on any payload; C: let the BEAM compiler catch malformed forms; D: convert bad payloads implicitly. | **A.** A regression demonstrated that a Boolean payload annotated as an integer passed typed-core verification. Both verifier paths now check expression and pattern payloads. |
| VB-I02 | A: derive nominal adapters from verified exported types and constructor metadata; B: infer tags from display names; C: freeze compact layout as an external ABI; D: serialize every internal call. | **A.** Identity, constructor ordinal, field order and substitutions come from checked metadata; ordinary execution keeps native values internally. |
| VB-I03 | A: use the independent reference constructor observation as the bridge's semantic side; B: compare raw terms across layouts; C: treat layout equality as nominal identity; D: erase constructor identity. | **A.** Both native layouts round-trip to the same reference value, preserving nominal ownership. |
| VB-I04 | A: require an explicit per-conversion validation budget and distinguish exhaustion; B: introduce an undocumented depth cutoff; C: report exhaustion as a type mismatch; D: traverse arbitrary foreign terms without accounting. | **A.** Exhaustion is separate from malformed input; this experiment does not invent a portable global capacity floor. |
| VB-I05 | A: reject noncanonical physical shapes even if their contents resemble a constructor; B: accept both atom and singleton-tuple nullary compact values; C: normalize all host tuples heuristically; D: ignore malformed constructor payloads. | **A.** Compact nullary constructors are atoms; representation checks preserve the selected layout contract. |

| VB-I06 | A: one explicit scalar/product/record/sum codec shared by backend entry points; B: repeat host-term tests in every wrapper; C: use the heuristic value classifier as foreign admission; D: route all internal values through serialization. | **A.** `ValueBoundary.Data` separates typed validation from descriptive classification, while both backend owners expose checked literal lowering through it. |
| VB-I07 | A: distinguish Text by valid UTF-8, Bytes by arbitrary complete bytes, and Character by Unicode scalar range; B: merge all binaries into Text; C: accept any integer as Character; D: silently replace malformed encoding. | **A.** Invalid UTF-8, surrogate scalars, out-of-range scalars and partial-byte bitstrings are rejected at the corresponding type boundary. |
| VB-I08 | A: explicit node and payload-byte budgets with a separate exhaustion result; B: undocumented depth cutoff; C: report resource exhaustion as invalid data; D: permit unbounded validation. | **A.** Both scalar/structural and nominal conversion now share `ValueBoundary.Budget`, counting visited values and scalar payload bytes. The initial node-only nominal experiment was replaced before publication. |
| VB-I09 | A: preserve finite binary64 bits including signed zero; B: normalize zero signs; C: coerce integers to Float at ingress; D: accept host-specific non-finite values. | **A.** A compiled nested product preserves negative zero's exact bits. Float ingress checks the exponent field and rejects implicit Int coercion. |
| VB-I10 | A: preserve compiler-produced closures internally and reject raw foreign functions in the data codec; B: trust any host function of matching arity; C: inspect closure environments as a stable ABI; D: serialize executable closures. | **A.** A captured immutable value produces matching observations in the independent evaluator and both native layout choices. This establishes the retained internal carrier, not a general foreign callback adapter. |
| VB-I11 | A: refuse abstract constructor ingress; B: reconstruct abstract values from known physical tags; C: silently weaken abstraction to transparency; D: trust foreign constructor ordinals. | **A.** The nominal codec requires transparent constructors; abstract and existential boundaries need their own justified admission route. |
| VB-I12 | A: reuse C080's owner-scoped handle checks and reject raw handles in the data codec; B: infer ownership from tuple shape; C: accept any PID/reference; D: expose a global handle registry. | **A.** Retained resource tests demonstrate rejection after release, after scope exit and from another owner, as well as static rejection of hidden closure capture. No broader host handle admission is implied. |

| VB-I13 | A: integrate the new carriers through existing kernel inference, independent verification, stepping and lowering under an explicit experimental profile; B: count standalone EAF literals as complete language adoption; C: silently widen 0.1.8; D: build an unrelated evaluator. | **A.** `value_boundary_experiment` admits a closed pure value tree; retained kernel revisions explicitly reject the new carrier tags/types. It is not a registered language revision yet. |
| VB-I14 | A: derive fixed-kernel nominal metadata from verified exported types and share the nominal codec; B: freeze unqualified constructor atoms as semantic identity; C: reconstruct private datatypes; D: implement a separate ad hoc wire format. | **A.** `ValueBoundary.Fixed` reconstructs origin/module/type-qualified semantic identity and generic substitutions; private nominal ingress rejects. Fixed, compact and uniform layouts share payload checks and accounting. |

| VB-I15 | A: count visited payload values separately from trusted descriptor validation; B: charge inactive variant alternatives as if present in the value; C: obscure descriptor costs within the byte budget; D: promise a wall-clock or physical-memory bound. | **A.** All codecs now charge the same payload model. The candidate explicitly excludes metadata verification, wall-clock time and peak allocation from that budget. |
| VB-I16 | A: require deep purity across definitions, datatypes and trait metadata for the new tree profile; B: inspect only top-level evaluation effects; C: allow latent process effects implicitly; D: combine all resource/foreign profiles without evidence. | **A.** A latent process-effect test rejects, and literal payload checks retain the existing portable scanner limits at direct-tree entry and compilation. |

## Evidence and remaining gate

After correcting an unrelated missing export signature in the first fixture,
`/tmp/catena-value-boundary-before.log` records the actual verifier defect:
forged primitive payload verification returned `:ok`. The repaired primitive
regression and retained ADT/kernel suites passed 47 tests. The new nominal
bridge compares an actual compiled constructor result with the independent
reference evaluator in both compact and uniform layouts, including nullary
values, identity/payload rejection and distinct budget exhaustion.

The scalar/structural experiment additionally passes actual BEAM compilation
through both backend entry points, and scanned numeric/text meanings pass the
shared lowering boundary. Seven new tests cover primitive verifier rejection,
nominal layouts, scalar/structural lowering, malformed ingress, classifier
validation, scanned meanings and captured closures. The combined new boundary,
resource-handle, categorical and lexical-capability suites pass 27 tests. Earlier
boundary/value/data-model coverage passed 22 tests before the final two new tests.
Experimental literal artifacts identify their specification and frontend as
`experimental/value-boundary`; this does not silently extend a retained frontend.

## Representation inventory in progress

| Value class | Invariant and owner | Current executable witness and remaining boundary |
| --- | --- | --- |
| Int / Bool / Unit | Exact host kind; unbounded Int within explicit resources; Unit has one carrier. Scalar codec and backend own conversion. | `value_boundary_test.exs` checks forged annotations, large integers, literal lowering and distinct exhaustion. |
| Float | Finite binary64 with preserved signed zero; numeric elaborator owns rounding. | Scanned decimal meaning reaches checked lowering; compiled nested value retains negative-zero bits. |
| Text / Character / Bytes | Valid UTF-8 / Unicode scalar / complete bytes; semantic types remain distinct despite shared physical kinds. | Empty binary, invalid UTF-8, surrogate and partial-byte rejection; Text classifier repair. |
| Products / structural records / variants | Exact arity, closed field set and declared label; fixed kernel carrier with explicit semantic conversion. | Nested record/sum/product round-trip; unknown or extra fields reject. An integrated Text closure/product program agrees between the kernel stepper and native code. |
| Ordinary nominal data | Origin-qualified type/constructor identity, declaration field order, selected compact/uniform layout. | Compact and uniform values agree with the independent constructor observation; fixed-kernel generic Option/Text values agree between the stepper, codec and native execution. Abstract and existential ingress remain excluded by the experiment. |
| Closures | Verified code plus immutable captures; backend owns executable representation. | Captured closure observations agree with reference in both layouts; raw host fun admission rejects. General callback ingress remains P096. |
| Dictionaries / evidence | Coherent compiler-selected implementations; evidence is not a source value. | Retained `c004_categorical_test.exs` verifies coherent parent evidence and dictionary erasure into direct calls. No ordinary data schema admits evidence. |
| Lexical capability identities | Non-values scoped by binding, not ambient string lookups. | Retained `kernel_capability_binding_test.exs` passes; no data codec carrier admits a capability identity. |
| Service-authority descriptors | Explicit verified authority inputs, not ordinary structural data by resemblance. | Contract and manifest provenance remain with C087/C089; a consolidated boundary witness is outstanding. |
| Scoped runtime handles | Owning scope/process, liveness state and checked operations; C080/C084 runtime owns representation. | Retained resource tests reject release/exit/cross-owner reuse. Raw references, functions and PIDs reject in the data codec. |

At this experimental checkpoint P093 remained open. The promotion approval and
exact-revision verification were subsequently completed as recorded below. No public vocabulary or stable external ABI has been selected.


## Integrated experiment evidence

The first full suite passed 835 tests before the kernel integration. After that
checkpoint, the ten boundary tests pass, including typed/inference-independent
verification of Float, Text, Character and Bytes; reference/native agreement;
forged payload rejection; retained-revision rejection; Text closure capture;
and a fixed-layout generic nominal carrying Text. The fixed nominal tests also
reject private constructor ingress, improper payload lists and exhausted byte
budgets. After the literal-limit and deep-purity checks, the full suite passes 839 tests.
Production compilation with warnings as errors, production escript construction,
formatting and whitespace checks pass. Archive validation passes 612 documents,
70 directories and 6,937 local links; its 783 normative obligations remain
unchanged because the new chapter is a candidate.


## Promotion review block

The [candidate contract](../60-specification/value-boundaries/carriers-and-checked-conversion.md)
is reviewable, but no new revision has been registered. A review-only patch at
`/tmp/value-boundary-promotion.patch` proposes exact `0.1.58` admission, its
lifecycle record, explicit selection and artifact metadata, plus current-discovery
test updates. It preserves historical `0.1.57` feature records and retained
JSON/kernel source, interface and signed-format lists. The patch affects 52
compiler files, primarily repeated current-revision discovery expectations.

Automatic approval review first rejected promotion because the experimental
boundary was unfinished and the change affected compatibility. After completing
the candidate contract and the full verification above, a second review rejected
applying the prepared patch, stating that the user had not explicitly re-approved
this concrete registered-revision/compatibility change after its risks were
explained. Neither rejected command ran. No further promotion attempt will run
without that requested approval.

At that blocked checkpoint both repositories were on `codex/value-boundaries`,
changes were uncommitted, no P093 PR existed and the checkbox remained partial.
The compiler still registered `0.1.57`; only the experimental profile executed
the new tree carriers. No continuation or automation was created.


## Approved promotion — September 9

The user explicitly approved revision `0.1.58` after the review rejection was
explained. Automatic approval review then permitted the prepared patch. The
compiler registers the exact pure value-tree boundary, records its selection and
frontend in deterministic artifacts, and leaves historical interface and signed
formats unchanged. The unknown-future-revision negative test now uses `0.1.59`;
it continues to test rejection rather than rejecting the newly admitted revision.

The complete promoted compiler suite passes **840 tests**. Production compilation
with warnings as errors, production escript build, formatting and whitespace
checks pass. Twelve boundary tests include exact selection, deterministic artifact
provenance and retained interface rejection. The archive validates with 793
normative obligations: 698 traced, 74 partial and 21 untraced. The ten new VB
obligations are connected in the conformance map. The specification chapter,
area index, authority registry, version instructions, completion map and checklist
are synchronized. C093 is complete within its stated boundary; general foreign
callbacks, unsafe handles and final vocabulary keep their separate owners.

The earlier rejection records above are historical, not a current blocker.
Compiler/research commit and PR identities are recorded during the merge handoff.

Compiler implementation commit: `a4f4dc26566719f0b34596e27053b6e8182dbd05`.
The full promoted test run is recorded in `/tmp/catena-value-boundary-promoted.log`;
production evidence is in `/tmp/catena-value-boundary-promoted-build.log`.
