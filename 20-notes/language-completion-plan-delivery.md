---
title: "Language Completion Plan: Interoperability, Delivery, and Assurance"
kind: note
created: "2026-09-06"
maturity: developing
tags:
  - catena
  - language-design
  - specification
  - implementation
  - formal-methods
aliases:
  - "Completion plan items 093–141"
---

# Language Completion Plan: Interoperability, Delivery, and Assurance

## Scope and decision authority

This non-normative implementation plan covers every immutable checklist identity
from 093 through 141, including C140, which appears earlier in the checklist.
Baseline status comes from the [audited completion checklist](../00-inbox/language-specification-completeness-checklist.md)
at research commit `d93a655eae07c9e0dc539eff07487c4326d05eea` and the
[completion audit](../50-journal/2026-09-06-checklist-completion-audit.md).
Compiler targets were inspected at sibling commit
`d7e0fcc484d3e1c3b4a292d4d3e703ddcc330535`.

Every **selected** answer is the agent's recommended choice under the user's
explicit delegation; it is not a claim of individual developer approval.
Alternatives are evaluated against the present research and existing normative
boundaries. Selection records a plan, not an implemented behavior or completed
checkbox. Any conflict with an existing rule needs an explicit versioned
amendment before implementation. Exact semantic revision numbers are allocated
when slices land, not reserved by this planning document.

No row adopts a new public keyword, library name, declaration spelling, or grammar.
Existing names identify already-defined interfaces. New functionality is described
by meaning and first exercised through retained semantic inputs or private test
fixtures. P107's public naming and P109's grammar adoption remain held for later
user co-design. A held public tool can have a working semantic core without being
reported complete. G141 is an open late-0.x milestone, not a deferred item.

All compiler paths below are relative to `/home/ducky/code/catena`; research links
are relative to this document. Existing target files identify real integration
seams. A path explicitly labeled **new** is a proposed internal implementation
file, not an assertion that machinery already exists. The ordered steps in each
item include specification, implementation, evidence, and checkbox gates; none is
closed merely by writing its plan.

## Common execution and evidence contract

For every unfinished item: first refine the semantic contract and independent
oracle, then implement and verify typed elaboration, then connect runtime/tool
adapters, and finally record the exact source revision, compiler revision,
commands, observations, and remaining limits. Research lives here; compiler,
runtime, and tool implementation lives in the sibling repository. Keep
[authority](../SPECIFICATION-AUTHORITY.md), [behavior classes](../CONFORMANCE-VOCABULARY.md),
[resource limits](../IMPLEMENTATION-LIMITS.md), and the
[conformance registry](../10-maps/conformance-traceability.md) synchronized.

The acceptance examples below specify required observations, not tests already
passed. A positive case, a refusal/adversarial case, and a resource or semantic
boundary case are mandatory for each new behavior. Unit evidence alone cannot
substitute for a full retained-input-to-BEAM witness where execution is promised.
A reference model must not call the implementation it is checking. Reuse the
existing suite once per coherent change; add tests for new claims and regressions,
not mechanical restatements of code.

The categorical design criterion is concrete: preserve coherent evidence,
identity/composition laws in their declared pure domain, and explicit sequencing
for effects. A mathematical equation never silently authorizes a change in
callback multiplicity, order, failure, resource lifetime, or concurrency. The
[combinator synthesis](combinators-for-algebraic-data-and-categorical-programming.md),
[standard hierarchy](../60-specification/traits-and-categorical-operations/standard-hierarchy-and-vocabulary.md),
and [operational contract](../60-specification/traits-and-categorical-operations/operational-semantics.md)
provide that basis.

## Item 093 — Catena-to-BEAM value mapping

**Baseline:** P093. **Depends on:** C002/C004/C005/C010/C040; coordinate G080,
G095, and P097 before resource/foreign representations are admitted.
**Basis:** [representation boundaries](../60-specification/data-and-patterns/interfaces-and-representation.md)
and [compatibility layers](../60-specification/api-and-abi-compatibility/compatibility-layers-and-versions.md).

| Decision | Explored alternatives and tradeoffs | Selected recommendation and rationale |
| --- | --- | --- |
| CP-093-1 | A: expose current tuples/maps, cheap but freezes implementation; B: uniform tagged values everywhere, simple but allocates; C: verified per-type layouts behind interfaces, efficient but needs bridge tests; D: encode all values as binaries, portable but destroys ordinary call efficiency. | **C**, recommended and agent-selected: preserve C002 layout freedom and C010's fixed kernel layouts while making each boundary conversion explicit. |
| CP-093-2 | A: pass arbitrary host terms, convenient but unsound; B: duplicate every value on every call, safe but expensive; C: trusted internal values with checked foreign ingress, localized cost; D: serialize every internal call, isolated but impractical. | **C**, recommended and agent-selected: C067 requires checked entry, not repeated validation of already-verified pure computation. |
| CP-093-3 | A: give resources ordinary structural values, easy but exposes lifetime; B: opaque typed handles with scoped owners, more metadata; C: global IDs with unrestricted lookup, simpler but ambient; D: prohibit resources, small but unusable for real programs. | **B**, recommended and agent-selected: explicit handles compose with G080 lifetimes and preserve representation independence. |

1. Inventory primitives, nominal/structural data, closures, dictionaries, evidence,
   lexical capability identities (non-values), service-authority descriptors, and runtime handles with semantic invariant and layout owner.
2. Extend `lib/catena/values.ex`, `lib/catena/typed_core/verifier.ex`,
   `lib/catena/backend/erlang_abstract.ex`, and `lib/catena/kernel/backend.ex`;
   add one checked adapter layer rather than scattering term tests.
3. Compare both supported nominal layouts and reference observations; publish the
   representation matrix and link each row to an executable witness.

**Acceptance:** nested products/sums, finite Float, Text, and closure captures
round-trip across admitted boundaries; malformed nominal tags and foreign handles
are refused; large integers, empty binaries, deep structures, and expired handles
exercise explicit limits. **Gate:** all admitted value classes have verified
lowering and ingress/egress coverage; no stable external ABI is inferred.

## Item 094 — Calling conventions

**Baseline:** P094. **Interface inputs:** P093, C032, and the jointly designed G096 adapter descriptor. Final callback integration waits for G096; the call-shape contract does not. **Basis:**
[functions and calls](../60-specification/functions-and-calls/README.md),
[effect lowering](../60-specification/effects-and-handlers/README.md), and
[compatibility layers](../60-specification/api-and-abi-compatibility/compatibility-layers-and-versions.md).

| Decision | Explored alternatives and tradeoffs | Selected recommendation and rationale |
| --- | --- | --- |
| CP-094-1 | A: expose CPS worker arities, direct but fragile; B: versioned adapter descriptors plus ordinary wrappers, extra layer; C: one universal term-list call, flexible but erases type distinctions; D: permanent stable BEAM ABI, convenient but contradicts current scope. | **B**, recommended and agent-selected: bind calling shape to compiler/interface identity while keeping workers private. |
| CP-094-2 | A: flatten all curried calls eagerly, fast but changes partial application; B: retain semantic arity and specialize proven saturated calls, selective complexity; C: box all calls, uniform overhead; D: rely on host arity exceptions, late errors. | **B**, recommended and agent-selected: preserve C032 capture and tail-call behavior without preventing direct calls. |
| CP-094-3 | A: show generated stacks only, cheap but opaque; B: erase all stack information, private but unusable; C: map wrapper/worker frames to source origins with technical details available, metadata cost; D: fabricate source frames without provenance, friendly but misleading. | **C**, recommended and agent-selected: source explanations must remain traceable to actual generated code. |

1. Specify direct, curried, effectful, process-entry, foreign, and callback call
   classes with argument/result checks and hidden-argument accounting.
2. Integrate descriptors in `lib/catena/interface.ex`, `lib/catena/kernel/interface.ex`,
   both backend files, and `lib/catena/otp/compiler.ex`; retain proper tail calls.
3. Exercise adapter calls against a separately compiled Erlang fixture and P100's
   frame map, including compiler-identity mismatch refusal.

**Acceptance:** saturated and partial applications agree; wrong arity/type and
forged descriptors fail before entry; maximum source arity with hidden CPS
arguments and deep tail recursion remain inside published limits.
**Gate:** all call classes are specified and witnessed; no cross-build binary
compatibility promise is added accidentally.

## Item 095 — Erlang type boundary

**Baseline:** G095. **Depends on:** P093, C036/C040/C067; coordinates G096/G098.
**Basis:** [foreign visibility requirement](../60-specification/dynamic-and-unsafe-boundaries/the-foreign-visibility-routing.md)
and [Float boundary probes](../50-journal/2026-08-31-beam-float-boundary-probes.md).

| Decision | Explored alternatives and tradeoffs | Selected recommendation and rationale |
| --- | --- | --- |
| CP-095-1 | A: add a universal dynamic type, flexible but reopens C067; B: infer types from host terms, convenient but cannot establish nominal identity; C: explicit type-directed codecs, more declarations but checkable; D: disallow Erlang data, safe but defeats BEAM interoperability. | **C**, recommended and agent-selected: admit useful values through explicit contracts without widening the type system. |
| CP-095-2 | A: coerce mismatches, forgiving but loses information; B: typed conversion failure, composable but needs an error value contract; C: trap every mismatch, simple but prevents expected validation; D: accept successful prefixes, fast but unsound. | **B**, recommended and agent-selected: invalid external input is expected data; unexpected foreign execution failure still follows C036's visible trap rule. |
| CP-095-3 | A: validate only outer tags, cheap but unsound; B: recursive validation with depth/size budgets, bounded cost; C: lazy unchecked interiors, fast but delays failure into pure code; D: unrestricted recursion, complete but denial-of-service prone. | **B**, recommended and agent-selected: establish the whole admitted type before returning a Catena value and make exhaustion explicit. |
| CP-095-4 | A: admit NaN/infinity, broad host access but violates Float; B: normalize them to zero, total but silently corrupts data; C: reject non-finite input everywhere, strict and consistent; D: permit only through native paths, inconsistent. | **C**, recommended and agent-selected: preserve finite binary64 semantics across every ingress route, including NIF-produced terms. |

1. Define a codec relation for admitted primitives, products/sums, collections, and
   opaque handles; state successful conversion preservation and refusal outcomes.
2. Add **new** `lib/catena/foreign/codec.ex`, integrate
   `lib/catena/type.ex`, `lib/catena/typed_core/verifier.ex`, and both backends;
   keep arbitrary host-term inspection outside ordinary Catena code.
3. Build Erlang and isolated native fixtures that exercise each entry path.

**Acceptance:** valid nested data converts and re-encodes; wrong constructor,
improper list, malformed UTF-8, forged handle, and non-finite Float are refused;
zero-length values and depth/size thresholds behave deterministically.
**Gate:** no unchecked ingress exists, with an independently tested preservation
argument; public declaration spelling remains held by P109.

## Item 096 — Foreign calls and callbacks

**Baseline:** G096. **Interface inputs:** G080/G088 lifetime/cancellation, P094 call descriptors, G095 codecs, and P106/P131 authority transport. These contracts are co-designed, not mutually dependent completion gates. A first retained-input adapter uses explicitly supplied test-harness authority; full application provisioning follows P106.
**Basis:** [C067 foreign routing](../60-specification/dynamic-and-unsafe-boundaries/the-foreign-visibility-routing.md),
[effects](algebraic-effects-and-handlers.md), and
[exception boundary](../60-specification/exception-boundary/README.md).

| Decision | Explored alternatives and tradeoffs | Selected recommendation and rationale |
| --- | --- | --- |
| CP-096-1 | A: untyped module/function lookup, convenient but ambient; B: typed explicit declarations and capability-bound adapters, more setup; C: compiler whitelist of every foreign function, rigid; D: foreign calls only in the compiler, avoids work but prevents applications. | **B**, recommended and agent-selected: explicit semantic declarations bind types, effects, trust, and host identity without deciding syntax. |
| CP-096-2 | A: trust arbitrary foreign purity annotations, optimizable but dangerous; B: mark every call as a visible foreign effect initially, conservative; C: treat calls as pure unless they raise, unsound; D: forbid callbacks, simpler but blocks OTP integration. | **B**, recommended and agent-selected: audited pure intrinsics may be a later separately justified refinement; no hidden effect enters categorical laws. |
| CP-096-3 | A: unlimited callbacks, easy but leaks captured resources; B: callbacks owned by a resource scope with explicit revocation, bookkeeping; C: callbacks valid for one call only, safe but too restrictive; D: global callback table without ownership, convenient but ambient. | **B**, recommended and agent-selected: supports realistic asynchronous integration while G080/G088 govern lifetime and cancellation. |
| CP-096-4 | A: kill host work and claim rollback, simple but false; B: cooperative cancellation with declared completion races, explicit complexity; C: cancellation ignored, easy but poor composition; D: retry every timeout, responsive but duplicates effects. | **B**, recommended and agent-selected: cancellation reports whether work stopped, completed, or may have external effects; never invents transactional host behavior. |

1. Specify semantic descriptors for argument/result codecs, effect capabilities,
   exception mapping, scheduler behavior, callback capture, and ownership.
2. Add **new** `lib/catena/foreign/adapter.ex`; integrate `lib/catena/effect.ex`,
   `lib/catena/effect/runtime.ex`, `lib/catena/interface.ex`, and backends.
3. Exercise calls, callbacks, foreign raises, denial, cancellation, and expiry
   through retained semantic inputs before P109 surface adoption.

**Acceptance:** typed bidirectional calls preserve data and effect traces; missing
capability, wrong return type, callback-after-close, and callback reentry violations
fail visibly; completion/cancellation races have recorded allowed outcomes.
**Gate:** useful executed adapters plus a normative contract, not syntax alone;
G096 remains incomplete until its later public surface is adopted.

## Item 097 — BEAM-native values

**Baseline:** P097. **Depends on:** G095/G096, P084/P085, P093.
**Basis:** [built-in meanings](../60-specification/built-in-data-model/README.md)
and [kernel process representation](../60-specification/formal-semantic-kernel/README.md).

| Decision | Explored alternatives and tradeoffs | Selected recommendation and rationale |
| --- | --- | --- |
| CP-097-1 | A: expose all host terms under one type, powerful but unchecked; B: typed opaque wrappers for each native role, explicit conversions; C: copy all native values into JSON, simple but loses identity; D: exclude native values forever, safe but impractical. | **B**, recommended and agent-selected: preserve useful PIDs, ports, references, and fun adapters without exposing arbitrary reflection. |
| CP-097-2 | A: universal host equality, cheap but contradicts handles; B: equality only where the semantic type declares it, selective; C: pointer identity for every value, fast but representation-dependent; D: no equality anywhere, overrestrictive. | **B**, recommended and agent-selected: retain C010's handle exclusions and C035's type-directed equality. |
| CP-097-3 | A: native maps become records automatically, convenient but confuses identity; B: checked map/record and binary/text conversions, explicit cost; C: expose host keys directly, easy but untyped; D: stringify every key/value, lossy. | **B**, recommended and agent-selected: separate language meanings from host container representation. |

1. Inventory binaries, maps, local PIDs, ports, references, and funs by admitted
   role, ownership, transferability, equality, and codec failure.
2. Implement in the new foreign codec/adapter layer with integration in
   `lib/catena/values.ex`, `lib/catena/type.ex`, and `lib/catena/kernel/checker.ex`.
3. Test capability and sendability rules before exposing any wrapper in a package.

**Acceptance:** admitted native values cross only typed adapters; arbitrary host
fun, forged PID wrapper, unsupported map keys, and handle equality are refused;
large binaries, closed ports, dead processes, and reference lifetime boundaries
remain explicit. **Gate:** every native kind has an admission or justified
exclusion contract; useful admitted kinds are actually executable.

## Item 098 — NIFs and ports

**Baseline:** G098. **Depends on:** G080/G088, G095/G096, P127/P129/P130/P131.
**Basis:** [foreign routing](../60-specification/dynamic-and-unsafe-boundaries/the-foreign-visibility-routing.md),
[resource observability](../60-specification/resource-observability/README.md), and
[Float probes](../50-journal/2026-08-31-beam-float-boundary-probes.md).

| Decision | Explored alternatives and tradeoffs | Selected recommendation and rationale |
| --- | --- | --- |
| CP-098-1 | A: unrestricted NIF loading, fast but grants VM-wide trust; B: ports as default with separately admitted NIFs, overhead but isolation; C: prohibit native integration entirely, small but limits applications; D: silently convert NIFs to ports, misleading ABI. | **B**, recommended and agent-selected: make native computation usable while distinguishing VM-crashing trust from process-isolated failures. |
| CP-098-2 | A: execute every native call on normal schedulers, low overhead but blocks; B: declare scheduler class and bounded work contract per adapter, review cost; C: dirty schedulers for all calls, simple but hides blocking distinctions; D: infer class from names, unreliable. | **B**, recommended and agent-selected: operational contracts need explicit CPU/I/O/blocking behavior, not a law-based performance guess. |
| CP-098-3 | A: rely only on garbage collection, convenient but late cleanup; B: scope closure plus idempotent native finalizer fallback, complexity; C: finalizers may run arbitrary Catena effects, expressive but uncontrolled; D: never free resources, unacceptable. | **B**, recommended and agent-selected: G080 owns deterministic lifetime while fallback handles exceptional host loss without promising recoverability from VM crash. |

1. Define native package metadata, loader checks, capability requirements,
   scheduler declarations, finalization, and explicit VM-crash scope.
2. Add **new** `lib/catena/foreign/native.ex`; connect package manifest/linker,
   foreign codecs, and scope runtime. Keep unsafe obligations in artifacts.
3. Run malicious/crashing native fixtures only in disposable OS subprocesses;
   test both normal Float return and non-finite native construction refusal.

**Acceptance:** a bounded port service and admitted NIF execute; missing trust,
wrong scheduler declarations, invalid values, and unsigned native payloads are
refused; double close, abrupt subprocess death, and native timeout are covered.
**Gate:** working native paths with honest crash guarantees and reproducible
packaging; never report VM survival as guaranteed for an in-process NIF.

## Item 099 — OTP compatibility policy

**Baseline:** P099. **Depends on:** C010/P094; coordinate G092/P128/P136.
**Basis:** [OTP compatibility research](../30-sources/erlang-otp-compatibility-and-upgrading.md)
and [kernel contract](../60-specification/formal-semantic-kernel/README.md).

| Decision | Explored alternatives and tradeoffs | Selected recommendation and rationale |
| --- | --- | --- |
| CP-099-1 | A: every OTP version, broad but untested; B: OTP 29 as tested baseline with evidence-gated expansion, conservative; C: latest OTP only, simple but unstable; D: abandon OTP for custom BEAM output, violates architecture. | **B**, recommended and agent-selected: support is a tested matrix, not extrapolation from format resemblance. |
| CP-099-2 | A: version-number checks alone, cheap but miss capabilities; B: feature probes plus exact toolchain fingerprint, stronger evidence; C: compile and hope, late failures; D: bundle all OTP releases, enormous maintenance. | **B**, recommended and agent-selected: fail early on missing compiler/runtime facilities and bind artifacts to tested conditions. |
| CP-099-3 | A: indefinite binary reuse, convenient but unsupported; B: rebuild on unsupported toolchain changes and publish retirement windows, explicit cost; C: silent runtime fallback, unpredictable; D: automatic hot upgrade, conflates G092. | **B**, recommended and agent-selected: keeps binary compatibility separate from source/interface retention. |

1. Publish the current tested OTP/ERTS/Elixir matrix and expansion/retirement gate.
2. Extend `lib/catena/otp/compiler.ex`, `lib/catena/conformance_info.ex`, and
   `lib/catena/language_info.ex` with capability checks and artifact provenance.
3. Run P136's full semantic matrix before adding a supported row.

**Acceptance:** supported toolchains compile and execute the corpus; unsupported
or incomplete hosts fail before output commit; oldest/newest supported patch
and cross-host artifact loading are exercised. **Gate:** each support claim has
an exact successful run; OTP 29 remains the retained bootstrap boundary.

## Item 100 — Debugging metadata

**Baseline:** P100. **Depends on:** P093/P094, C013/C016/C113; feeds P117/G124.
**Basis:** [source text](../60-specification/source-text/README.md),
[erasure contract](../60-specification/specifications-and-governance/artifacts-erasure-and-cli.md),
and [runtime observability](../60-specification/resource-observability/README.md).

| Decision | Explored alternatives and tradeoffs | Selected recommendation and rationale |
| --- | --- | --- |
| CP-100-1 | A: embed full source/evidence in BEAM, convenient but violates erasure/privacy; B: deterministic sidecar origins plus minimal runtime locations, separate retrieval; C: discard all generated origins, small but opaque; D: absolute host paths only, simple but unreproducible. | **B**, recommended and agent-selected: navigate source and erased evidence without making it runtime-reachable. |
| CP-100-2 | A: one nearest source span, compact but loses expansion history; B: bounded origin chains with primary user location, more metadata; C: unbounded provenance graph per node, expensive; D: synthetic locations presented as user code, misleading. | **B**, recommended and agent-selected: explain generated derivations, closures, handlers, and inline sites honestly. |
| CP-100-3 | A: unrestricted locals in crash reports, rich but leaks secrets; B: policy-controlled values with default redaction, deliberate tradeoff; C: no stack data, private but impractical; D: redact only strings, bypassable. | **B**, recommended and agent-selected: structural visibility can coexist with P131's capability and secret policy. |

1. Define stable node/origin identities, path normalization, expansion frames,
   erased-evidence links, and metadata retention modes.
2. Extend `lib/catena/source_span.ex`, `lib/catena/kernel/node.ex`, both backends,
   `lib/catena/otp/compiler.ex`, and `lib/catena/report.ex`.
3. Validate optimized and unoptimized frame maps against executed failures.

**Acceptance:** closure/handler/foreign frames resolve to correct source and
optional generated details; missing or tampered sidecars cannot claim false
origins; stripped builds, inlining depth, and non-ASCII coordinates are covered.
**Gate:** source/runtime/evidence navigation is accurate without violating erasure.

## Item 101 — Minimum prelude

**Baseline:** P101. **Depends on:** C026/C004, P102/P103/P104/P105/P106.
**Basis:** [prelude policy](../60-specification/prelude-policy/README.md) and
[combinator inclusion criteria](combinators-for-algebraic-data-and-categorical-programming.md).

| Decision | Explored alternatives and tradeoffs | Selected recommendation and rationale |
| --- | --- | --- |
| CP-101-1 | A: all host services in the prelude, convenient but ambient; B: small pure compositional core with separate capability services, explicit imports; C: empty standard package, minimal but unusable; D: every categorical abstraction eagerly included, rich but burdens learning. | **B**, recommended and agent-selected: sufficient data/functions/outcomes and existing coherent traits, with effects supplied explicitly. |
| CP-101-2 | A: automatic import, terse but breaks C026; B: explicit versioned package selection and existing precedence, predictable; C: compiler-reserved standard names, simple but violates ordinary-library delivery; D: directory-dependent prelude selection, hidden behavior. | **B**, recommended and agent-selected: preserve zero implicit names and digest-bound standard evidence. |
| CP-101-3 | A: signatures alone certify delivery, cheap but weak; B: types, laws, operational tests, and application examples per exported family, more work; C: host documentation substitutes, convenient but wrong authority; D: freeze new names now, premature vocabulary choice. | **B**, recommended and agent-selected: define meanings and executable contracts now; select no additional public vocabulary. |

1. Inventory required semantic families for small functional applications and
   document exclusions with owners; retain all existing canonical method ABI.
2. Extend `priv/stdlib/catena-standard-0.1.4.json` through versioned successors,
   `lib/catena/categorical/standard.ex`, package manifests, and interface checks.
3. Compile representative data transformation, validation, and capability-using
   programs from explicit package selections.

**Acceptance:** selected/opted-out packages behave predictably; missing package,
wrong digest, or conflicting import fails; empty programs and minimal usable
applications need no accidental host names. **Gate:** useful implemented minimum
and laws are complete; any new public names await P107/P109 adoption.

## Item 102 — Collection protocols

**Baseline:** P102. **Depends on:** C004/C042, P050/P053/P057, P103/G080.
**Basis:** [collection construction](../60-specification/collection-construction-and-update/README.md)
and [categorical operational laws](../60-specification/traits-and-categorical-operations/operational-semantics.md).

| Decision | Explored alternatives and tradeoffs | Selected recommendation and rationale |
| --- | --- | --- |
| CP-102-1 | A: one universal collection trait, convenient but conflates shape/order; B: lawful families with explicit traversal and keyed contracts, more structure; C: unrelated APIs per container, simple locally but poor composition; D: adopt every host enumeration behavior, low effort but unstable. | **B**, recommended and agent-selected: preserve the weakest useful categorical structure and separate operational guarantees. |
| CP-102-2 | A: host map iteration order, fast but opaque; B: semantic key order where ordering evidence exists, deterministic cost; C: random iteration, catches assumptions but unusable default; D: insertion-order semantics for every map, convenient but extra representation promise. | **B**, recommended and agent-selected: deterministic keyed iteration can be specified through lawful key evidence; unordered operations must say so explicitly. |
| CP-102-3 | A: all collections eager, simple but limits streaming; B: eager finite collections plus explicit pull-step library protocols, controllable lifetime; C: implicit laziness everywhere, changes effects; D: unrestricted parallel traversal, fast but changes order. | **B**, recommended and agent-selected: implement usable streams/iterators without admitting D059's deferred generalized comprehension syntax. |
| CP-102-4 | A: silently keep the first duplicate, simple but hides input loss; B: silently keep the last duplicate, familiar but order-sensitive; C: strict construction returns a typed duplicate failure, explicit and predictable; D: always combine duplicates, useful but requires a chosen algebra even when none exists. | **C**, recommended and agent-selected: direct construction rejects collisions; explicit update replaces a selected key, and a separately explicit combining builder can use lawful combination evidence. |

1. Define finite list/map/set construction, typed duplicate refusal, explicit replacement/combining builders, folds,
   traversal order, early stopping, and a separate pull-step resource protocol.
2. Extend `lib/catena/standard_list.ex`, `lib/catena/categorical.ex`, standard
   package data, and **new** `lib/catena/standard/collections.ex`.
3. Compare lawful implementations with independent structural models and runtime
   traces; publish complexity by operation, not container marketing labels.

**Acceptance:** transformations obey identity/composition and defined key order;
inconsistent ordering evidence, duplicate-policy violations, and effectful pure
callbacks are refused; empty/large inputs, early stop, and abandoned iterators
exercise stack and cleanup rules. **Gate:** every promised family executes with
laws, cost, and lifetime evidence; syntax adoption remains separately held.

## Item 103 — Outcome types

**Baseline:** P103. **Depends on:** C042/C081, C004; coordinates G080/P084/P105.
**Basis:** [exception boundary](../60-specification/exception-boundary/README.md)
and [combinator synthesis](combinators-for-algebraic-data-and-categorical-programming.md).

| Decision | Explored alternatives and tradeoffs | Selected recommendation and rationale |
| --- | --- | --- |
| CP-103-1 | A: one exception channel for all failures, convenient but destroys typed composition; B: ordinary Option/Result-shaped values plus separate traps/effect escape, explicit; C: null for absence, cheap but untyped; D: process death for every failure, robust isolation but excessive. | **B**, recommended and agent-selected: preserve C081's three distinct mechanisms and C042's typed miss. |
| CP-103-2 | A: all validation fails fast, simple but hides independent errors; B: separate fail-fast sequencing and accumulating independent validation, richer contract; C: always accumulate, cannot express dependent checks; D: choose based on runtime data, unpredictable. | **B**, recommended and agent-selected: distinguish dependency from independent combination rather than pretending one law covers both. |
| CP-103-3 | A: implicit trap-to-result conversion, convenient but catches too much; B: explicit boundary adapters only for named failure classes, predictable; C: automatic process restart on Result failure, conflates supervision; D: prohibit adapters, too rigid. | **B**, recommended and agent-selected: expected failure values compose, while terminal traps remain terminal unless a later boundary explicitly defines observation. |

1. Specify semantic type shapes, ordering, mapping, dependent combination, and
   accumulation laws without selecting additional public method names.
2. Implement ordinary standard-package ADTs and coherent dictionaries through
   `lib/catena/data.ex`, `lib/catena/categorical.ex`, and the stdlib manifest.
3. Test validation pipelines and lookup/foreign conversion examples end to end.

**Acceptance:** dependent failures stop and independent errors accumulate in
specified order; no silent trap/absence/result coercion occurs; empty error
collections and nested outcomes retain law and callback-count guarantees.
**Gate:** executable APIs plus failure-class documentation; public additions
remain held until vocabulary adoption.

## Item 104 — Text and binary model

**Baseline:** P104. **Depends on:** C017/C040, G095/P102/P103; P109 owns syntax.
**Basis:** [built-in data model](../60-specification/built-in-data-model/README.md)
and [Unicode source research](../30-sources/unicode-consortium-2025-unicode-standard-17.md).

| Decision | Explored alternatives and tradeoffs | Selected recommendation and rationale |
| --- | --- | --- |
| CP-104-1 | A: byte offsets everywhere, efficient but splits Unicode; B: explicitly distinguished byte/scalar/grapheme operations, more types/contracts; C: grapheme indexes as universal O(1) integers, pleasant but false cost; D: silently normalize every Text, changes equality. | **B**, recommended and agent-selected: C040 scalar meanings remain intact while higher-level text operations state units and cost. |
| CP-104-2 | A: implicit normalization, convenient but changes values; B: explicit versioned normalization/encoding conversion, predictable; C: reject non-ASCII, too narrow; D: host-default Unicode algorithms, unstable. | **B**, recommended and agent-selected: pin algorithm data separately and keep malformed encoding an explicit typed failure. |
| CP-104-3 | A: freeze interpolation/binary-pattern syntax now, productive but violates hold; B: semantic concatenation/formatting and checked slicing first, syntax later; C: omit text composition, unusable; D: evaluate interpolated text as code, unsafe. | **B**, recommended and agent-selected: implement useful pure operations and format-value contracts without choosing punctuation or public names. |

1. Specify units, slice bounds, malformed sequences, grapheme segmentation,
   normalization, encoding, and binary-pattern matching meaning.
2. Extend `lib/catena/text.ex`, `lib/catena/unicode_data.ex`,
   `lib/catena/values.ex`, and standard package implementations; use typed failures.
3. Add Unicode conformance vectors and retained-input runtime adoption; record
   exact Unicode data version independently of source-language revision.

**Acceptance:** multi-scalar graphemes, normalization, and encoding round-trip as
specified; invalid UTF-8 and mixed index units fail; empty text, combining runs,
non-BMP scalars, and huge slices test boundaries. **Gate:** implemented text/binary
contracts with honest complexity; interpolation syntax awaits P109.

## Item 105 — Numeric library

**Baseline:** P105. **Depends on:** C018/C035/C036/C061, P103/G095/G098.
**Basis:** [numeric relationships](../60-specification/numeric-relationships/README.md)
and [recorded Float probes](../50-journal/2026-08-31-beam-float-boundary-probes.md).

| Decision | Explored alternatives and tradeoffs | Selected recommendation and rationale |
| --- | --- | --- |
| CP-105-1 | A: host badarith leaks directly, easy but unclassified; B: primitive arithmetic faults map to the reserved arithmetic trap, explicit; C: every existing arithmetic operator returns Result, composable but breaking; D: saturate all faults, total but loses meaning. | **B**, recommended and agent-selected: preserve existing primitive types and C036 classification; new checked library operations can return typed failures explicitly. |
| CP-105-2 | A: claim bit-exact host math everywhere, convenient but unsupported; B: bit-exact basic arithmetic with separately bounded transcendentals, scoped; C: require correctly-rounded transcendentals immediately, strongest but native cost; D: omit all math functions, too restrictive. | **B**, recommended and agent-selected: deliver usable math with explicit error/portability contracts; strengthen individual functions only after validated implementations. |
| CP-105-3 | A: locale-dependent printing, friendly but unreproducible; B: deterministic round-trip decimal formatting, more implementation work; C: fixed decimal precision, simple but loses values; D: expose host inspect output, unstable. | **B**, recommended and agent-selected: require parse/print preservation for finite binary64 including signed zero policy. |
| CP-105-4 | A: implicit Int/Float/decimal promotion, convenient but contradicts C061; B: explicit conversions and a library decimal type with declared rounding, more calls; C: replace all numbers with rationals, exact but costly; D: no decimal/checked arithmetic, limits practical use. | **B**, recommended and agent-selected: preserve the closed primitive relationship and provide useful financial/scaled arithmetic without a new built-in numeric tower. |
| CP-105-5 | A: truncate integer quotient toward zero, host-friendly but signed remainder surprises; B: floor quotient, useful for positive divisors but changes remainder sign with divisor; C: Euclidean quotient/remainder, uniform nonnegative remainder with explicit negative-divisor rule; D: inherit host division implicitly, cheap but leaves language meaning unstated. | **C**, recommended and agent-selected: require a = b*q + r and 0 <= r < abs(b) for b nonzero; specify zero-divisor failure separately. This is a proposed library contract, not a claim that C061 already chooses it. |
| CP-105-6 | A: expose all host transcendentals without accuracy bounds, broad but unverifiable; B: maintain a measured per-platform whitelist with declared error limits, flexible but many matrices; C: admit a limited set through independently validated correctly-rounded kernels, stronger but integration cost; D: replace transcendental results with rational approximations without a bound, exact-looking but misleading. | **C**, recommended and agent-selected: begin with only functions whose finite-domain/rounding contract and implementation can be validated independently; use the archived CORE-MATH lead to investigate candidates, verify current upstream evidence before adoption, and make no function or ULP promise before its proof/tests support it. |

1. Specify Euclidean integer quotient/remainder, primitive/checked zero and overflow/domain faults, conversion loss,
   checked arithmetic, decimal precision/rounding, and per-function math accuracy. Admit transcendental functions only through CP-105-6's validated kernel gate; unsupported functions remain absent from the initial minimum package with named follow-up work.
2. Extend `lib/catena/numeric.ex` only for literal integration; add **new**
   `lib/catena/standard/numeric.ex` for runtime operations and update both
   reference/BEAM paths. Do not mislabel the literal elaborator a numeric library.
3. Differentially test exact integer/rational models, boundary Float vectors,
   and print/parse across each supported host.

**Acceptance:** division/remainder identities and checked errors agree; zero
faults, non-finite ingress, and implicit mixed arithmetic are rejected/classified;
subnormals, signed zero, maximum finite values, halfway rounding, and very large
integers are tested. **Gate:** each numeric promise has measured evidence and
no unearned cross-platform transcendental guarantee.

## Item 106 — Environmental effects

**Baseline:** P106. **Interface inputs:** G080/G088, C005/C027/C082, and the jointly designed G095/G096/P131 boundary contracts. The entry amendment follows the minimal checked adapter; full environmental/callback integration follows explicit provisioning.
**Basis:** [top-level boundary](../60-specification/top-level-effects/the-top-level-boundary.md)
and [lexical effects research](algebraic-effects-and-handlers.md).

| Decision | Explored alternatives and tradeoffs | Selected recommendation and rationale |
| --- | --- | --- |
| CP-106-1 | A: ambient host handler, convenient but prohibited; B: explicit capability parameter to a revised effect-closed launch contract, visible amendment; C: process-global capability lookup, hidden authority; D: no environmental services, keeps current rule but cannot deliver functional applications. | **B**, recommended and agent-selected: formally amend C027/C082 before adding the channel; retained zero-argument entry revisions remain unchanged. |
| CP-106-2 | A: one all-powerful environment token, easy but coarse; B: attenuable service-specific capabilities, more declarations; C: permission strings checked only at runtime, weak typing; D: filesystem conventions imply authority, hidden behavior. | **B**, recommended and agent-selected: typed denied/limited capabilities compose with lexical handlers and least authority. |
| CP-106-3 | A: real time/randomness in every test, realistic but irreproducible; B: injectable deterministic service models plus real adapters, extra implementations; C: ban time/randomness, too limiting; D: compiler reads host environment silently, undermines reproducibility. | **B**, recommended and agent-selected: validate effect traces independently while real programs can perform I/O. |
| CP-106-4 | A: return unhandled requests to launcher, simple but breaks closure; B: entry installs handlers over explicitly supplied capabilities, more setup; C: supervisor interprets effects, conflates failure; D: implicitly rewrite effects away, unsound. | **B**, recommended and agent-selected: the revised parameter channel supplies values, never an ambient interpreter; the entry still closes its effects. |
| CP-106-5 | A: pass lexical capability names as ordinary values, convenient but violates C005/C029; B: pass opaque service-authority descriptors that authorize fresh lexical handler installation, explicit separation; C: use a global host-service registry, ambient and prohibited; D: make every capability first-class through a broad type-system amendment, much wider than this need. | **B**, recommended and agent-selected: launch parameters are typed authority data, not first-class lexical capability names or resumption values; handler installation creates lexical identities under existing effect discipline. |

1. Write the explicit versioned entry amendment and capability transport contract,
   including denied launch, shutdown, revocation, and path/network attenuation.
   Amend C027/C082 explicitly for typed service-authority parameters; preserve
   C005/C029's non-value status of lexical capability names and affine resumptions.
   A descriptor is validated authority data used to install fresh lexical handlers,
   never an escaped lexical identity.
2. Extend `lib/catena/entry.ex`, `lib/catena/effect.ex`,
   `lib/catena/package/manifest.ex`, and **new** `lib/catena/runtime/environment.ex`.
3. Deliver concrete I/O, filesystem, network, time, randomness, environment,
   logging, and process-control adapters with separate typed failure contracts.

**Acceptance:** a real application uses only supplied services; denied/expired
capabilities and unhandled requests fail; shutdown/cancellation races, empty
capability sets, and deterministic fake services agree with reference traces.
**Gate:** usable adapters and amended rules with retained-revision regression
coverage; forged descriptors, escaped lexical names, and implicit handler lookup
are negative cases. Public names and launch syntax remain held.

## Item 107 — Category-inspired API names

**Baseline:** P107, **public vocabulary held by the user**. **Depends on:** C004,
P101–P106; coordinates G137/P109. **Basis:**
[approachable vocabulary research](approachable-language-vocabulary.md) and
[existing normative hierarchy](../60-specification/traits-and-categorical-operations/standard-hierarchy-and-vocabulary.md).

| Decision | Explored alternatives and tradeoffs | Selected recommendation and rationale |
| --- | --- | --- |
| CP-107-1 | A: rename existing ABI now, premature and breaking; B: retain existing ABI and record unnamed semantic gaps, disciplined; C: expose mathematical synonyms beside every name, doubles vocabulary; D: suppress the semantic ledger, loses rigor. | **B**, recommended and agent-selected: the user explicitly holds new vocabulary; existing normative names remain historical contracts. |
| CP-107-2 | A: designer intuition chooses new terms, fast but weak evidence; B: later task-based comparative comprehension studies, slower but direct; C: popularity polling alone, easy but measures taste; D: copy another language wholesale, familiar but untested for Catena. | **B**, recommended and agent-selected: the research defines approachability through behavioral predictions and repair success. |
| CP-107-3 | A: make theory prerequisites, precise but inaccessible; B: evaluate dependency/shape/order behavior first with optional formal metadata, accessible and rigorous; C: hide effects and cost for simplicity, misleading; D: teach two naming layers simultaneously, burdens learners. | **B**, recommended and agent-selected: category theory guides laws and coherent implementation without becoming required user vocabulary. |

1. Maintain semantic operation inventory and usability tasks using existing ABI or
   neutral research labels; add no new exports or grammar tokens now.
2. Audit `priv/stdlib/catena-standard-0.1.4.json`,
   `lib/catena/categorical/standard.ex`, and diagnostics for accidental synonyms.
3. After the user releases the hold, run G137's study, choose names jointly, and
   version any ABI changes through C008/C028 rather than rewriting history.

**Acceptance:** present operations remain digest-compatible; accidental public
aliases are caught; distinctions among mapping, independent combination, and
sequencing survive transfer across containers. **Gate:** remains partial while
vocabulary selection and independent comprehension evidence are held; the
semantic inventory can be completed now without completing P107.

## Item 108 — Stability and performance policy

**Baseline:** P108. **Depends on:** C004/C028/C030, P101–P106, G138.
**Basis:** [operational contract](../60-specification/traits-and-categorical-operations/operational-semantics.md)
and [compatibility model](../60-specification/api-and-abi-compatibility/compatibility-layers-and-versions.md).

| Decision | Explored alternatives and tradeoffs | Selected recommendation and rationale |
| --- | --- | --- |
| CP-108-1 | A: promise every observed behavior forever, stable but freezes bugs; B: version types/laws/operational guarantees explicitly, accountable; C: only signatures stable, misses semantic breaks; D: no stability promise, easy but poor ecosystem foundation. | **B**, recommended and agent-selected: declared promises belong in compatibility classification; incidental layout remains internal. |
| CP-108-2 | A: fixed wall-clock limits for all hosts, impossible portability; B: asymptotic/callback/stack contracts plus measured envelopes, layered; C: only big-O, hides constants and retention; D: benchmark anecdotes, weak evidence. | **B**, recommended and agent-selected: categorical laws and operational costs require distinct testable statements. |
| CP-108-3 | A: representation permanently public, optimization constraint; B: expose only necessary semantic/complexity guarantees, flexible; C: hidden copy/share changes always acceptable, may violate resource claims; D: universal zero allocation, unrealistic. | **B**, recommended and agent-selected: state sharing or retention promises only when a real operation requires them and tests support them. |

1. Inventory each standard operation's laws, failure/order behavior, complexity,
   stack bound, and stability class; flag unsupported promises.
2. Bind contract metadata to `lib/catena/interface.ex`,
   `lib/catena/package/compat.ex`, standard package revisions, and benchmark cases.
3. Check deliberately changed implementations against compatibility and cost gates.

**Acceptance:** compatible implementation replacements preserve stated contracts;
callback duplication or strengthened requirements are classified as breaks;
empty/large/worst-shape workloads expose complexity and retention edges.
**Gate:** library-wide declarations have executable evidence and review rules;
no constant-time or ABI guarantee is inferred from one benchmark.

## Item 109 — Surface grammar capstone

**Baseline:** P109, **implementation of public grammar held by the user**.
**Depends on:** settled semantic items, P107, P117; feeds G118/P119/G120/G123/G141.
**Basis:** the [checklist's widened capstone scope](../00-inbox/language-specification-completeness-checklist.md)
and [approachable-language design map](../10-maps/approachable-catena-language-design.md).

| Decision | Explored alternatives and tradeoffs | Selected recommendation and rationale |
| --- | --- | --- |
| CP-109-1 | A: freeze a familiar grammar now, quick but violates hold; B: accumulate semantic parser obligations and keep retained inputs, slower public launch; C: treat kernel S-expressions as final language, convenient but unreviewed; D: delegate syntax to host Elixir, loses Catena identity. | **B**, recommended and agent-selected: honor semantics-first sequencing and user co-design of original vocabulary/grammar. |
| CP-109-2 | A: many unrelated parsers per tool, duplication; B: future shared lossless source tree and elaboration boundary, coherent tooling; C: discard comments and reconstruct later, lossy; D: parser performs type/effect inference, tangled authority. | **B**, recommended and agent-selected: prepare an input/output contract now without selecting concrete productions or new token meanings. |
| CP-109-3 | A: grammar completion means expressions only, under-scoped; B: one adoption matrix for programming, governance, diagnostics, and tools, explicit work; C: publicize partial grammar as complete, misleading; D: defer every semantic test until parser exists, deadlocks progress. | **B**, recommended and agent-selected: preserve the checklist's four capstone deliverables while executing semantics independently. |

1. Catalogue source-adoption obligations from all slices: modules/imports,
   declarations, values, functions, patterns, effects, processes, governance,
   source origins, comments, diagnostics, and tool recovery.
2. Now maintain interfaces around `lib/catena/tokenizer.ex`,
   `lib/catena/ast/decoder.ex`, `lib/catena/kernel/parser.ex`, and
   `lib/catena/compiler.ex`; introduce no new public productions.
3. Only after the hold is lifted, compare at least four answers for each actual
   grammar decision, jointly select them, implement a shared parser, and test the
   same semantic corpus through public source.

**Acceptance now:** semantic obligations are complete and parser-independent
fixtures remain executable; unapproved source syntax is not accepted accidentally.
**Later acceptance:** source/retained-IR equivalence, malformed/partial-program
recovery, comment round trips, and lexical boundary cases across every form.
**Gate:** remains partial until the full capstone and its tool input contract are
implemented after user co-design; a planning matrix is not grammar completion.

## Item 110 — Checking language

**Baseline:** C110, preserve completion. **Depends on:** C006/C038; integrate
P109/P116/G122. **Basis:** [claims and checking](../60-specification/specifications-and-governance/claims-examples-and-checking.md).

| Decision | Explored alternatives and tradeoffs | Selected recommendation and rationale |
| --- | --- | --- |
| CP-110-1 | A: broaden the checker during tool work, expressive but changes the completed fragment; B: preserve the pure typed fragment and exact budget, stable; C: run arbitrary host code for evidence, flexible but untrusted; D: remove bounded checking, simplifies compiler but loses guarantees. | **B**, recommended and agent-selected: integrate the completed semantics without silently admitting new evidence strength. |
| CP-110-2 | A: trust old success flags, cheap but stale; B: re-run exact examples with identity-bound evidence, reproducible; C: treat timeout as false, conflates outcomes; D: treat bounded search as proof, overclaims. | **B**, recommended and agent-selected: C006 distinguishes success, failure, invalidity, and budget exhaustion; preserve those distinctions through new tools. |

1. Pin existing checker cases before new parser/build adoption.
2. Integrate `lib/catena/specification.ex`, `lib/catena/reference/evaluator.ex`,
   and `test/catena/c006_specification_governance_test.exs` with future source maps
   and build inputs; retain the 20,000-step checking bound for its exact revision.
3. Route any stronger checker proposal to a separate future decision and revision.

**Acceptance:** pure nested examples reproduce evidence; effectful/ill-typed
checkers remain invalid; one step below/at/above budget preserves distinct
outcomes. **Gate:** C110 remains complete if integration preserves the existing
contract; no unnecessary new feature or proof claim is introduced.

## Item 111 — Enforcement modes

**Baseline:** C111, preserve completion. **Depends on:** C006; integrate P121/P130.
**Basis:** [scope and authorization rules](../60-specification/specifications-and-governance/scopes-policy-and-authorization.md).

| Decision | Explored alternatives and tradeoffs | Selected recommendation and rationale |
| --- | --- | --- |
| CP-111-1 | A: make governance compulsory for all packages, stricter but changes adoption; B: retain optional adoption and mandatory declared scopes, predictable; C: let profiles ignore failed declarations, convenient but unsound; D: inherit workspace-wide governance silently, hidden authority. | **B**, recommended and agent-selected: preserve ordinary functional programs and explicit fail-closed governed boundaries. |
| CP-111-2 | A: collapse build/publish/activate, simple but conflates authority; B: keep separate gates through build/registry tools, clear responsibility; C: infer publish approval from tests, weak authorization; D: auto-activate signed packages, signature is not a decision. | **B**, recommended and agent-selected: existing policy semantics must remain the authority when new delivery tools arrive. |

1. Inventory the three gates in project/build/registry flows and retain scoped
   inheritance semantics.
2. Route every declared gate through `lib/catena/governance/policy.ex`,
   `lib/catena/governance.ex`, and `lib/catena/package/linker.ex`.
3. Run existing positive/adversarial policy fixtures against each tool entry.

**Acceptance:** ungoverned packages build and governed actions require their own
evidence; missing/unknown policy fails closed; mixed governed dependencies and
empty scopes do not silently widen or bypass coverage. **Gate:** C111 remains
complete when all new callers preserve adoption and gate semantics.

## Item 112 — Evidence lifecycle

**Baseline:** C112, preserve completion. **Depends on:** C006; integrate P116/P130.
**Basis:** [evidence identity and lifecycle](../60-specification/specifications-and-governance/evidence-identity-and-lifecycle.md).

| Decision | Explored alternatives and tradeoffs | Selected recommendation and rationale |
| --- | --- | --- |
| CP-112-1 | A: overwrite evidence in place, simple but destroys history; B: retain immutable identity and append-only replay, more storage; C: use wall-clock freshness alone, operationally familiar but changes logical ordering; D: trust newest signature regardless of subject, unsafe. | **B**, recommended and agent-selected: new tools preserve exact claim/tool/artifact/role/sequence binding and revocation history. |
| CP-112-2 | A: test badges count as proofs, easy but false; B: preserve distinct evidence kinds and scope, explicit interpretation; C: discard failed observations, clean reports but hides evidence; D: infer approval from compiler success, conflates actors. | **B**, recommended and agent-selected: the governance synthesis explicitly separates tests, proofs, signatures, assumptions, and authorized decisions. |

1. Bind future test/build output to existing evidence identities without inventing
   new evidence semantics implicitly.
2. Extend adapters around `lib/catena/governance/lifecycle.ex`,
   `lib/catena/governance/reference.ex`, and `lib/catena/assurance.ex`.
3. Replay historical and adversarial bundles in newer delivery tools.

**Acceptance:** replacement and revocation replay identically; substituted
subjects, duplicate signatures, stale roles, and reordered history are refused;
empty histories and sequence boundaries retain historical outcomes. **Gate:**
C112 stays complete; schema evolution is P116, not a silent lifecycle rewrite.

## Item 113 — Erasure semantics

**Baseline:** C113, preserve completion. **Depends on:** C006; integrate P100/P119/G124/P128.
**Basis:** [artifact and erasure rules](../60-specification/specifications-and-governance/artifacts-erasure-and-cli.md).

| Decision | Explored alternatives and tradeoffs | Selected recommendation and rationale |
| --- | --- | --- |
| CP-113-1 | A: retain verification graph for debugger convenience, useful but violates erasure; B: external identity-bound sidecars, extra lookup but preserves runtime; C: delete all evidence, minimal but loses auditability; D: hide graph in an unlisted BEAM chunk, still retention. | **B**, recommended and agent-selected: tooling navigation need not make checking definitions runtime-reachable. |
| CP-113-2 | A: compare source text only, cheap but insufficient; B: continue byte-identical artifacts with/without discharged specifications, strong bounded evidence; C: compare selected exports, misses hidden retention; D: allow small undocumented differences, weakens guarantee. | **B**, recommended and agent-selected: the existing exact artifact test is the proper regression boundary. |

1. Trace new provenance/doc/debug consumers and route evidence retrieval outside
   executable artifacts.
2. Preserve erasure before `lib/catena/backend/erlang_abstract.ex` and package
   output construction in `lib/catena/package/linker.ex`.
3. Extend existing paired-package erasure cases to each new supported frontend.

**Acceptance:** executable outputs remain identical for paired packages;
verification-only exports/reachability and embedded governance data fail checks;
empty and large evidence graphs, stripped/debug builds, and multiple modules
preserve accounting. **Gate:** C113 remains complete only with byte-level
regression evidence; runtime monitoring is not added under this item.

## Item 114 — Artifact format

**Baseline:** C114, preserve completion. **Depends on:** C006/C008; integrate P116/P121/P128/P130.
**Basis:** [artifact rules](../60-specification/specifications-and-governance/artifacts-erasure-and-cli.md).

| Decision | Explored alternatives and tradeoffs | Selected recommendation and rationale |
| --- | --- | --- |
| CP-114-1 | A: rewrite old canonical bytes into a new format, tidy but invalidates signatures; B: retain exact readers/signing domains with versioned future envelopes, more maintenance; C: accept permissive JSON, convenient but ambiguous; D: sign pretty-printed output, unstable. | **B**, recommended and agent-selected: historical signatures bind bytes and domain identity, not an equivalent-looking object. |
| CP-114-2 | A: write artifacts as each phase succeeds, fast but partial output; B: retain staged all-or-nothing output and external signing, safer coordination; C: store private keys in compiler config, convenient but expands trust; D: skip manifest verification for local builds, inconsistent. | **B**, recommended and agent-selected: preserve the existing transaction and no-private-key compiler boundary. |

1. Inventory new artifact classes and route them through an explicit future format
   extension without altering retained C006/C008 encodings.
2. Keep `lib/catena/canonical_jcs.ex`, `lib/catena/governance/crypto.ex`,
   `lib/catena/assurance.ex`, and linker transaction checks authoritative.
3. Replay canonical/signature vectors and inject filesystem failures at commit.

**Acceptance:** signed multi-module packages verify; duplicate keys, malformed
canonical bytes, wrong domains, path escapes, and artifact substitution fail;
zero artifacts and interrupted output replacement leave no partial release.
**Gate:** C114 remains complete; extensions get separate versioned evidence.

## Item 115 — Governance identity and trust roots

**Baseline:** C115, preserve completion. **Depends on:** C006; coordinates P130.
**Basis:** [identity and lifecycle rules](../60-specification/specifications-and-governance/evidence-identity-and-lifecycle.md)
and [TUF research](../30-sources/the-update-framework-specification.md).

| Decision | Explored alternatives and tradeoffs | Selected recommendation and rationale |
| --- | --- | --- |
| CP-115-1 | A: online account identity silently replaces offline principals, convenient but changes trust; B: retain offline roots and use explicit adapters for future services, clear authority; C: trust any valid signature, misses authorization; D: trust repository membership, hidden policy. | **B**, recommended and agent-selected: registry/network identity must not redefine the completed offline protocol. |
| CP-115-2 | A: new root signs itself, easy but circular; B: preserve old-and-new thresholds and predeclared recovery, explicit continuity; C: newest timestamp wins, replay-prone; D: repeated signatures satisfy a quorum, false independence. | **B**, recommended and agent-selected: existing distinct-actor and root continuity checks remain mandatory in every integration. |

1. Document the boundary between governance principals and future package-registry
   publishers; do not infer one identity from another.
2. Reuse `lib/catena/governance/trust_root.ex`, `lib/catena/governance/crypto.ex`,
   and lifecycle replay in new artifact tooling.
3. Add integration vectors for delegated publication and compromised-key handling
   without changing retained root semantics.

**Acceptance:** valid scoped rotations/recovery replay; self-authorized roots,
repeated actors, revoked delegation, and wrong scopes fail; threshold equality
and first-root/historical-root boundaries remain exact. **Gate:** C115 stays
complete while the bounded offline trust model is preserved.

## Item 116 — Long-term evolution

**Baseline:** P116. **Depends on:** C008/C112/C114/C115; coordinates P121/P125/P136.
**Basis:** [edition lifecycle](../60-specification/editions-and-feature-lifecycle/README.md)
and [governance evidence](../60-specification/specifications-and-governance/evidence-identity-and-lifecycle.md).

| Decision | Explored alternatives and tradeoffs | Selected recommendation and rationale |
| --- | --- | --- |
| CP-116-1 | A: latest decoder reinterprets all history, small but changes decisions; B: exact-version interpreters with explicit migration records, maintenance cost; C: preserve bytes but drop interpretation, incomplete portability; D: re-sign all old evidence automatically, unauthorized identity change. | **B**, recommended and agent-selected: retain historical meaning and record any transformation as new derived evidence. |
| CP-116-2 | A: one-step lossy conversion, easy but unverifiable; B: deterministic adjacent schema migrations with provenance, composable; C: manual edits to signed bundles, unsafe; D: never evolve formats, eventually impractical. | **B**, recommended and agent-selected: small independently checkable transformations retain old artifacts and expose losses/refusals. |
| CP-116-3 | A: archive only source, compact but cannot replay tools; B: archive source, exact formats/tool identities, dependencies, and decisions, larger; C: archive only BEAM, no semantic replay; D: rely on live registries forever, fragile. | **B**, recommended and agent-selected: historical decisions need their original interpretive context, not just signature bytes. |

1. Specify a format/meaning support ledger, migration preconditions, historical
   policy dispatch, and explicit nonportable evidence outcomes.
2. Extend `lib/catena/language_version.ex`, `lib/catena/language_lifecycle.ex`,
   `lib/catena/interface.ex`, and governance readers; add **new**
   `lib/catena/artifact/migration.ex` with immutable input retention.
3. Build historical bundles offline under newer compilers and compare decisions.

**Acceptance:** supported old formats reproduce original results; unknown
versions, semantic loss, or signature rewriting fail explicitly; multi-hop
migration, revoked roots, and missing archived tools have defined outcomes.
**Gate:** replay and migration are demonstrable across retained versions; no
new compiler is presumed able to validate unknown future formats.

## Item 117 — Diagnostic contract

**Baseline:** P117. **Depends on:** C008/C010/C013, P100; P109 owns parse adoption.
**Basis:** [diagnostic research](../30-sources/barik-et-al-2018-compiler-explanations.md)
and [approachability criteria](approachable-language-vocabulary.md).

| Decision | Explored alternatives and tradeoffs | Selected recommendation and rationale |
| --- | --- | --- |
| CP-117-1 | A: plain strings as interface, simple but unstable; B: versioned structured diagnostics with stable identity and locations, richer; C: expose raw solver terms, exact but inaccessible; D: one generic failure code, small but unhelpful. | **B**, recommended and agent-selected: extend existing Diagnostic/Report structure rather than changing current families gratuitously. |
| CP-117-2 | A: nearest mismatch only, cheap but hides cause; B: bounded causal provenance with primary/secondary spans and source-level types, useful cost; C: full unbounded constraint dump, overwhelming; D: suggest repairs without evidence, potentially wrong. | **B**, recommended and agent-selected: research supports explanation plus actionable repair, with technical details available separately. |
| CP-117-3 | A: finalize parse diagnostics without grammar, speculative; B: finish semantic diagnostic schema now and defer grammar-specific cases, honest; C: block all diagnostics on P109, unnecessary; D: let each frontend invent unrelated payloads, fragmented. | **B**, recommended and agent-selected: one shared contract can serve retained inputs now and public syntax later. |

1. Specify related locations, inferred-type normalization, constraint causes,
   coverage witnesses, guard explanations, generated origins, and edit applicability.
2. Extend `lib/catena/diagnostic.ex`, `lib/catena/report.ex`,
   `lib/catena/type/infer.ex`, `lib/catena/pattern/coverage.ex`, and
   `lib/catena/condition.ex`; preserve existing machine family/path guarantees.
3. Add consumer fixtures and blinded repair tasks without introducing new vocabulary.

**Acceptance:** a type/coverage/effect failure explains both cause and source repair;
invalid related spans or stale edits are rejected; partial programs, Unicode
coordinates, long types, and provenance budgets remain bounded. **Gate:** semantic
contract can complete now; P117 stays partial until P109 parse cases are covered.

## Item 118 — Formatter

**Baseline:** G118; source-facing completion held behind P109.
**Depends on:** C015/C016, P109/P117; coordinates P125.
**Basis:** [layout](../60-specification/whitespace-and-layout/README.md),
[comment attachment](../60-specification/comments-and-documentation-comments/README.md),
and [source compatibility](../60-specification/api-and-abi-compatibility/compatibility-layers-and-versions.md).

| Decision | Explored alternatives and tradeoffs | Selected recommendation and rationale |
| --- | --- | --- |
| CP-118-1 | A: format tokens without parse structure, quick but can alter meaning; B: lossless-tree printer after grammar adoption, stronger but held; C: normalize whitespace blindly, unsafe around layout/literals; D: require hand formatting forever, poor tooling. | **B**, recommended and agent-selected: prepare the printer interface and document algebra now; choose no grammar-dependent formatting rules. |
| CP-118-2 | A: many style switches, flexible but inconsistent; B: canonical version-coupled defaults with narrow presentation settings, predictable; C: host language formatting rules, ungrounded; D: formatting changes language meaning, unacceptable. | **B**, recommended and agent-selected: deterministic output supports reproducibility and review without redefining source semantics. |
| CP-118-3 | A: rewrite comments/raw literals freely, neat but lossy; B: preserve semantic/comment attachment and literal payload exactly, constraint cost; C: discard trivia, simpler but damages docs; D: run formatter on malformed files destructively, risky. | **B**, recommended and agent-selected: C016 attachment and C017 decoding are semantic invariants, not optional style. |

1. Define a syntax-independent document layout algebra, stable width behavior,
   source mapping, and atomic edit output in **new** `lib/catena/tool/formatter.ex`.
2. Integrate comment/token inputs from `lib/catena/comment.ex` and
   `lib/catena/tokenizer.ex`; keep public printing dormant until P109.
3. After grammar adoption, add lossless parsing, round-trip checks, and versioned
   canonical examples for every production.

**Acceptance:** formatting is idempotent and preserves semantic trees/comment
attachment; invalid inputs or stale edits cannot overwrite source; narrow widths,
Unicode text, raw literal delimiters, and trailing comments are exercised.
**Gate:** preparatory printer work is partial progress only; full formatter
completion requires the approved grammar and source corpus.

## Item 119 — Documentation tool

**Baseline:** P119. **Depends on:** C016/C069/C113, P100/P107/P109/P117/G122.
**Basis:** [documentation comment rules](../60-specification/comments-and-documentation-comments/README.md)
and [law evidence tiers](../60-specification/traits-and-categorical-operations/laws-derivation-and-testing.md).

| Decision | Explored alternatives and tradeoffs | Selected recommendation and rationale |
| --- | --- | --- |
| CP-119-1 | A: render raw comments only, quick but misses symbols; B: interface-linked documentation graph with semantic views, richer; C: introspect BEAM as authority, misses erasure/types; D: generate from filenames, poor identity. | **B**, recommended and agent-selected: reuse checked symbol identities, traits/effects/laws, and separate evidence references. |
| CP-119-2 | A: execute all code blocks automatically, convenient but violates opt-in; B: explicit doctest opt-in in an isolated capability-limited runner, controllable; C: never test examples, stale risk; D: share unrestricted build authority with docs, unsafe. | **B**, recommended and agent-selected: preserve C016's inert default and G122's reproducible test semantics. |
| CP-119-3 | A: publish every hidden/private declaration, thorough but leaks APIs; B: visibility-aware public output with separate authorized internal view, extra filtering; C: omit all implementation/law views, incomplete; D: render raw HTML actively, violates current body rules. | **B**, recommended and agent-selected: attachment, visibility, and inert HTML guarantees remain binding. |

1. Build a documentation graph from `lib/catena/comment.ex`,
   `lib/catena/interface.ex`, and `lib/catena/report.ex`; add **new**
   `lib/catena/tool/documentation.ex` for deterministic rendering and links.
2. Cover types, exports, traits/implementations, effects, laws, and erased
   specification evidence; reject unresolved links rather than invent targets.
3. Implement opt-in doctests over retained semantic examples now and public source
   after P109, with denied default environmental services.

**Acceptance:** rendered symbols link correctly and opted-in examples run;
hidden APIs, active raw HTML, forged evidence, and undeclared effects are refused;
empty docs, duplicate anchors, cross-package links, and stale examples are tested.
**Gate:** rendering and doctests must actually work; extraction alone remains partial.

## Item 120 — Interactive environment

**Baseline:** G120. **Depends on:** P106/P109/P117/P121, G080/P084/G088.
**Basis:** [entry boundary](../60-specification/top-level-effects/the-top-level-boundary.md)
and [effects semantics](../60-specification/effects-and-handlers/README.md).

| Decision | Explored alternatives and tradeoffs | Selected recommendation and rationale |
| --- | --- | --- |
| CP-120-1 | A: implicit ambient host access, convenient but prohibited; B: explicit session capabilities and effect-closed evaluated units, setup cost; C: pure-only REPL forever, limited; D: execute raw Elixir, not Catena. | **B**, recommended and agent-selected: interactive convenience cannot bypass the environmental capability contract. |
| CP-120-2 | A: mutate old declarations in place, easy but changes closure meaning; B: immutable successive module generations with explicit replacement, clear lifetimes; C: silently reset all state each input, surprising; D: arbitrary hot patching, conflates G092. | **B**, recommended and agent-selected: old closures/processes retain their generation until explicitly closed; replacement is not hidden hot upgrade. |
| CP-120-3 | A: history stores every value/secret, useful but leaks; B: source/session metadata history with opt-in value capture and redaction, deliberate; C: no history, frustrating; D: assume interactive work is automatically governance-approved, false. | **B**, recommended and agent-selected: session evidence remains observational, with normal declared governance gates. |

1. Specify typed session state, capabilities, generation replacement, process
   ownership, cancellation, module load, history, and shutdown.
2. Add **new** `lib/catena/tool/session.ex` around `lib/catena/compiler.ex`,
   `lib/catena/entry.ex`, and scope runtime; exercise retained inputs first.
3. Integrate public input editing only after P109 and emit P117 diagnostics.

**Acceptance:** successive typed expressions execute with explicit effects;
invalid replacement, denied service, and unapproved governed actions fail;
stale closures, long-running children, interrupt races, and session close have
specified outcomes. **Gate:** semantic session engine is useful preparatory
work; a complete public REPL still depends on approved source grammar.

## Item 121 — Build system and package manager

**Baseline:** P121. **Depends on:** C025/C027/C028, P106/P116/P128/P130/P131;
public source adoption depends on P109. **Basis:**
[dependency contract](../60-specification/package-identity-and-dependencies/README.md)
and [artifact transactions](../60-specification/specifications-and-governance/artifacts-erasure-and-cli.md).

| Decision | Explored alternatives and tradeoffs | Selected recommendation and rationale |
| --- | --- | --- |
| CP-121-1 | A: shell scripts define the build implicitly, flexible but opaque; B: explicit project graph and profiles over the existing resolver/linker, coherent; C: resolver alone counts as package manager, incomplete; D: adopt host build semantics wholesale, loses Catena guarantees. | **B**, recommended and agent-selected: discovery and orchestration become explicit without replacing the checked dependency engine. |
| CP-121-2 | A: fetch during compilation, convenient but non-hermetic; B: separate verified acquisition from offline compilation, two phases; C: never fetch dependencies, unusable ecosystem; D: trust caches by path, vulnerable identity. | **B**, recommended and agent-selected: network authority is explicit and locked content is verified before compilation. |
| CP-121-3 | A: timestamp-only cache keys, fast but stale; B: content-addressed keys over declared inputs/toolchains/capabilities, more hashing; C: cache by package name/version only, misses changes; D: disable caching, correct but poor performance. | **B**, recommended and agent-selected: reproducibility and correct incremental builds share an explicit input contract. |
| CP-121-4 | A: arbitrary generators run with host authority, powerful but hidden effects; B: declared generator inputs/outputs in constrained execution, more setup; C: prohibit generation, limits practical builds; D: trust generated files without provenance, weak assurance. | **B**, recommended and agent-selected: code generation is a build computation whose effects and cache identity must be visible. |

1. Define project discovery precedence, profiles, workspace graphs, generator
   contracts, acquisition, cache keys, offline operation, and staged packaging.
2. Add **new** `lib/catena/package/build.ex` and acquisition/cache modules around
   `lib/catena/package/deps.ex`, `manifest.ex`, `linker.ex`, and `lib/catena/cli.ex`.
3. Build a multi-package example online-to-cache then offline, including a declared
   generator and a governed output, without changing retained package semantics.

**Acceptance:** clean/cached/offline builds produce the same declared outputs;
undeclared input/network access, corrupt cache, and missing lock content fail;
interrupted downloads, diamond graphs, profile switches, and output rollback
are covered. **Gate:** a working full build path, not just resolver tests.

## Item 122 — Testing tools

**Baseline:** G122. **Depends on:** C006/C010, P117/P121/P133/P134; coordinates G088.
**Basis:** [property-testing research](../30-sources/claessen-hughes-2000-quickcheck.md)
and [evidence distinctions](language-integrated-specifications-and-governance.md).

| Decision | Explored alternatives and tradeoffs | Selected recommendation and rationale |
| --- | --- | --- |
| CP-122-1 | A: one Boolean result for all tests, simple but hides evidence scope; B: distinct unit/property/model/concurrency/specification result kinds, richer; C: treat every passing test as proof, false; D: require an external test tool forever, fragmented. | **B**, recommended and agent-selected: preserve the meaning and finite scope of each observation. |
| CP-122-2 | A: implicit random seeds, easy but irreproducible; B: explicit seeds, typed generators, invariant-preserving shrinkers, implementation cost; C: fixed examples only, misses interactions; D: untyped byte fuzzing only, mostly invalid cases. | **B**, recommended and agent-selected: produce useful counterexamples that remain in the admitted semantic domain. |
| CP-122-3 | A: wall-clock timeout means language divergence, easy but false; B: distinguish semantic fuel, schedule bounds, and host timeout, precise; C: no timeouts, hangs builds; D: retry failures until green, hides defects. | **B**, recommended and agent-selected: C132's divergence and resource outcomes cannot be inferred from an arbitrary test deadline. |

1. Specify runner isolation, test identities, deterministic seeds, shrinking,
   time/schedule bounds, cleanup, and evidence capture without new source syntax.
2. Add **new** `lib/catena/tool/test_runner.ex` and reusable test generators around
   `lib/catena/kernel/explorer.ex`, reference evaluators, and `lib/catena/assurance.ex`.
3. Ship representative unit, law, property, schedule, and governed-evidence runs.

**Acceptance:** seeded failures reproduce and shrink while preserving types;
invalid evidence claims, undeclared effects, and stale subjects fail;
zero-test runs, budget exhaustion, orphan processes, and nonminimal shrink bounds
are reported explicitly. **Gate:** all promised testing modes execute and retain
evidence scope; public test notation awaits P109/P107.

## Item 123 — Editor protocol

**Baseline:** G123; full source integration held by P109.
**Depends on:** P100/P109/P117/G118/P119/P121.
**Basis:** [source coordinates](../60-specification/source-text/README.md)
and [diagnostic usability research](../30-sources/barik-et-al-2018-compiler-explanations.md).

| Decision | Explored alternatives and tradeoffs | Selected recommendation and rationale |
| --- | --- | --- |
| CP-123-1 | A: separate editor type checker, responsive but divergent; B: shared semantic services with immutable document snapshots, consistent; C: regex-only completion, easy but wrong identity; D: full rebuild on every keystroke forever, correct but slow. | **B**, recommended and agent-selected: cache validated intermediate results while reusing compiler authority. |
| CP-123-2 | A: publish stale diagnostics freely, fast but confusing; B: versioned results with cancellation and stable diagnostic IDs, bookkeeping; C: wait for perfect programs, unusable editing; D: repair malformed code silently, invents meaning. | **B**, recommended and agent-selected: partial information needs explicit uncertainty and document identity. |
| CP-123-3 | A: textual global rename, simple but changes unrelated names; B: identity-based rename with transactional edits, safe but requires resolution; C: compiler-generated public names in completion, leaks internals; D: ignore hidden APIs, breaks visibility. | **B**, recommended and agent-selected: use C066 resolution and P125 transactions; no new vocabulary is selected by tooling. |

1. Define an internal language-service API for snapshots, diagnostics, hover,
   completion, semantic tokens, navigation, rename, and formatting requests.
2. Add **new** `lib/catena/tool/language_service.ex` using
   `lib/catena/source_text.ex`, `namespace.ex`, `type/infer.ex`, and `report.ex`.
3. After P109, implement incremental parsing/recovery and the editor transport;
   test protocol compatibility against its then-current official specification.

**Acceptance:** edits update only affected semantic results and valid renames
preserve binding; stale responses, private completions, and overlapping edits
are refused; incomplete tokens, Unicode coordinate conversion, and canceled
requests are covered. **Gate:** service-core progress is not a complete editor
protocol until real source editing and transport work end to end.

## Item 124 — Debugging and observability

**Baseline:** G124. **Depends on:** P100/P117, G080/P084/P086/G088/G089, P131.
**Basis:** [resource observability](../60-specification/resource-observability/README.md),
[erasure rules](../60-specification/specifications-and-governance/artifacts-erasure-and-cli.md),
and [kernel process model](../60-specification/formal-semantic-kernel/README.md).

| Decision | Explored alternatives and tradeoffs | Selected recommendation and rationale |
| --- | --- | --- |
| CP-124-1 | A: expose only raw BEAM debugger state, quick but loses Catena meaning; B: source-aware adapter with optional technical frames, richer; C: custom VM debugger, huge scope; D: simulate execution instead of debugging real programs, insufficient. | **B**, recommended and agent-selected: reuse BEAM facilities while P100 supplies trustworthy source/effect/process origins. |
| CP-124-2 | A: tracing always changes no timing, appealing but impossible; B: declare observational perturbation and preserve semantic event identity, honest; C: hide dropped events, clean but false; D: retain every event forever, unbounded cost. | **B**, recommended and agent-selected: bounded traces need explicit loss, scheduling, and measurement limitations. |
| CP-124-3 | A: load erased declarations into runtime for inspection, violates C113; B: navigate evidence sidecars and redact sensitive values, separate trust; C: disable evidence navigation, incomplete experience; D: expose all mailbox/secret contents by default, unsafe. | **B**, recommended and agent-selected: debugging can be useful without changing erasure or ambient authority. |

1. Specify breakpoints, stack/handler views, process/message identity, trace loss,
   profiling attribution, crash reports, and erased-evidence navigation.
2. Add **new** `lib/catena/tool/debugger.ex` and runtime event adapters around
   `lib/catena/report.ex`, P100 metadata, and both backend origin maps.
3. Exercise actual compiled programs with closure, handler, process, foreign,
   cancellation, and failure paths; compare allowed traces to model observations.

**Acceptance:** breakpoints/stack reports identify real source events; unavailable
optimized values and erased declarations are labeled accurately; dropped-event
buffers, process death, stripped builds, and secret redaction are tested.
**Gate:** a working debug/trace path with honest limits, not a list of host tools.

## Item 125 — Migration tools

**Baseline:** P125. **Depends on:** C008/C028, P116/P117/P121; source rewrites depend on P109.
**Basis:** [migration and conformance rules](../60-specification/editions-and-feature-lifecycle/migration-diagnostics-and-conformance.md).

| Decision | Explored alternatives and tradeoffs | Selected recommendation and rationale |
| --- | --- | --- |
| CP-125-1 | A: compiler silently applies suggestions, convenient but violates C008; B: separate explicit migration command consuming structured edits, reviewable; C: manual fixes only, safe but scales poorly; D: apply all text matches, unsafe. | **B**, recommended and agent-selected: preserve report-only compiler behavior while implementing a transactional tool. |
| CP-125-2 | A: mutate files one by one, simple but leaves partial changes; B: validate preimages then atomically commit with backup/rollback, robust; C: overwrite conflicts, data loss; D: trust stale line offsets, wrong edits. | **B**, recommended and agent-selected: bind edits to source identity and resolve overlap before any final write. |
| CP-125-3 | A: syntactic success proves migration equivalence, cheap but weak; B: recheck interfaces/semantics and report unresolved behavioral changes, honest; C: regenerate governance approvals, unauthorized; D: pretend unsupported rewrites succeeded, misleading. | **B**, recommended and agent-selected: migrations may create new artifacts/evidence but cannot silently inherit old decisions. |

1. Implement retained-JSON edit application first with exact applicability,
   preimage digests, overlap checks, dry-run diff, rollback, and audit record.
2. Add **new** `lib/catena/tool/migration.ex` using `lib/catena/language_lifecycle.ex`,
   `lib/catena/diagnostic.ex`, and package transaction machinery.
3. After P109, add identity-aware source/API rewrites with parser validation and
   explicit unsupported cases; regenerate evidence without inventing approval.

**Acceptance:** applicable edits produce expected checked programs; stale,
ambiguous, overlapping, or unauthorized edits leave files unchanged; interruption,
symlink/path escape, and rollback failure have explicit outcomes. **Gate:** real
transactional migration plus future source adoption; C008 compiler remains report-only.

## Item 126 — Trusted computing base

**Baseline:** G126. **Initial inventory inputs:** C001/C005/C006/C010. Extend the inventory as G095/G098 arrive; their future completion does not block the initial trust graph. Coordinates
P127/P128/P131/P133/P134/G139. **Basis:**
[typed-core safety architecture](catena-greenfield-type-system.md),
[governance evidence distinctions](language-integrated-specifications-and-governance.md),
and [integrated theorem](../60-specification/progress-and-preservation/the-integrated-theorem.md).

| Decision | Explored alternatives and tradeoffs | Selected recommendation and rationale |
| --- | --- | --- |
| CP-126-1 | A: call the entire toolchain trusted without detail, honest but unhelpful; B: guarantee-specific trust/dependency graph, maintenance cost; C: claim an independent verifier removes all trust, false; D: list only cryptography, omits compiler/runtime risks. | **B**, recommended and agent-selected: connect each guarantee to components whose defects can violate it, including shared code and host assumptions. |
| CP-126-2 | A: duplicate the whole compiler, costly with correlated bugs; B: small independent checks at semantic/artifact boundaries, focused assurance; C: trust front-end annotations, cheap but weak; D: rely solely on signatures, authenticates bytes not correctness. | **B**, recommended and agent-selected: preserve independent core verification while explicitly documenting what backend, OTP, runtime, serializer, and foreign code remain trusted. |
| CP-126-3 | A: a prose inventory never checked, easy to stale; B: executable boundary assertions plus threat cases linked to the graph, accountable; C: claim exhaustive security from tests, unjustified; D: ban every external component, impossible on BEAM. | **B**, recommended and agent-selected: detect new privileged paths and keep trust reductions falsifiable. |

1. Inventory parser, inference, trait/effect solvers, verifiers, proof checker,
   reference evaluators, serializers, signer boundary, OTP/ERTS, native code,
   generators, registry, and OS isolation per guarantee.
2. Add **new** `docs/trusted-computing-base.md` and boundary checks in
   `test/catena/`; inspect `lib/catena/typed_core/verifier.ex`,
   `kernel/verifier.ex`, `otp/compiler.ex`, and `governance/crypto.ex`.
3. Mutation-test representative corrupt core, forged evidence, wrong lowering,
   and untrusted host ingress; record checks that do and do not detect each fault.

**Acceptance:** every advertised guarantee has named assumptions and enforcement;
a newly introduced raw OTP compiler/foreign bypass fails inventory checks;
shared helper failures, native VM crashes, and compromised build hosts remain
explicit residual trust. **Gate:** maintained graph plus executable witnesses,
without claiming the implementation is a proof-verified compiler.

## Item 127 — Unsafe-code policy

**Baseline:** P127. **Depends on:** C067, G095/G096/G098/G126/P130.
**Basis:** [intralanguage exclusions](../60-specification/dynamic-and-unsafe-boundaries/the-intralanguage-exclusions.md)
and [foreign visibility routing](../60-specification/dynamic-and-unsafe-boundaries/the-foreign-visibility-routing.md).

| Decision | Explored alternatives and tradeoffs | Selected recommendation and rationale |
| --- | --- | --- |
| CP-127-1 | A: add unrestricted intralanguage unsafe blocks, flexible but reopens C067; B: retain exclusions and name foreign/native obligations explicitly, bounded; C: mark whole packages safe by author assertion, weak; D: forbid all foreign work, too restrictive. | **B**, recommended and agent-selected: practical interoperability belongs at typed visible boundaries, not unchecked casts in ordinary programs. |
| CP-127-2 | A: hide native trust from interfaces, simple but surprises consumers; B: include transitive trusted-obligation metadata in interfaces/artifacts, extra tracking; C: let comments carry trust, not machine-checkable; D: treat successful tests as removal of unsafe status, false. | **B**, recommended and agent-selected: consumers need to know which external assumptions their guarantees depend on. |
| CP-127-3 | A: one global allow-unsafe switch, easy but coarse; B: scoped capability/policy admission by boundary identity, explicit; C: automatic admission from dependency presence, ambient; D: permanent ban after any failure, inflexible. | **B**, recommended and agent-selected: authority and responsibility can be attenuated and revoked without changing language typing. |

1. Define unsafe/trusted obligations, owners, transitive exposure, evidence scope,
   admission, and revocation while retaining all C067 source exclusions.
2. Extend `lib/catena/interface.ex`, `lib/catena/assurance.ex`,
   `lib/catena/package/manifest.ex`, and foreign/native adapter validation.
3. Compile applications with pure dependencies, admitted native dependencies, and
   deliberately denied transitive boundaries.

**Acceptance:** explicitly admitted native work runs with visible obligations;
hidden/forged trust declarations and unchecked intralanguage forms fail;
diamond dependencies, revoked adapters, and package replacement preserve scope.
**Gate:** enforceable policy through interfaces and artifacts, not a label claiming
that native execution cannot violate VM guarantees.

## Item 128 — Reproducible builds

**Baseline:** P128. **Depends on:** C006/C010/C025, P099/P121/P130/P131.
**Basis:** [artifact contract](../60-specification/specifications-and-governance/artifacts-erasure-and-cli.md)
and [package identity](../60-specification/package-identity-and-dependencies/README.md).

| Decision | Explored alternatives and tradeoffs | Selected recommendation and rationale |
| --- | --- | --- |
| CP-128-1 | A: same source implies identical binaries on all hosts, appealing but false; B: byte identity under an exact declared toolchain/input envelope, precise; C: semantic equality alone called reproducibility, weaker than packaging goal; D: current directory timestamps define identity, unstable. | **B**, recommended and agent-selected: explicitly bind compiler/OTP, dependencies, options, normalized paths, generated files, and packaging metadata. |
| CP-128-2 | A: inherit host environment, convenient but hidden input; B: allowlisted explicit environment and generator authority, constrained; C: clear everything and hope, may break tools silently; D: hash secrets into public manifests, leaks information. | **B**, recommended and agent-selected: record only permitted reproducibility inputs, with secret-sensitive operations separately classified. |
| CP-128-3 | A: compare BEAM modules only, existing evidence but incomplete; B: compare full packaged outputs in two independent clean directories, stronger; C: trust cache hits, circular; D: compare only interface digests, misses artifact differences. | **B**, recommended and agent-selected: packaging, generated metadata, and assurance sidecars all need declared byte expectations. |

1. Specify complete build-input identity, excluded nondeterministic fields,
   canonical archive ordering, permissions/timestamps, and path normalization.
2. Extend `lib/catena/package/linker.ex`, build/cache modules,
   `lib/catena/otp/compiler.ex`, and `lib/catena/assurance.ex`.
3. Build without caches in independent roots, perturb undeclared environment,
   and compare every output; classify signed-event differences separately.

**Acceptance:** exact-envelope rebuilds match full output bytes; changed locked
content/toolchain or undeclared generators invalidate keys; timezone, directory,
archive order, interrupted packaging, and empty packages exercise boundaries.
**Gate:** a reproducible packaging protocol with independent runs; cross-toolchain
identity is not promised without separate evidence.

## Item 129 — Resource exhaustion

**Baseline:** P129. **Initial contract inputs:** C012/C034/C036/C037. Co-design resource budgets with G080/G088 and implement aggregate compiler limits now; final runtime coverage follows P084/P090/P121, avoiding a completion dependency cycle.
**Basis:** [implementation limits](../IMPLEMENTATION-LIMITS.md),
[resource observability](../60-specification/resource-observability/README.md), and
[OTP resource-control research](../30-sources/erlang-otp-29-runtime-resource-controls.md).

| Decision | Explored alternatives and tradeoffs | Selected recommendation and rationale |
| --- | --- | --- |
| CP-129-1 | A: only per-node limits, simple but aggregate abuse remains; B: aggregate compiler budgets plus local floors, better accounting; C: one arbitrary global timeout, coarse and host-dependent; D: unlimited work, denial-of-service prone. | **B**, recommended and agent-selected: preserve portable minima while bounding total parse, inference, coverage, generation, and artifact work. |
| CP-129-2 | A: pretend language can prevent every VM OOM, false; B: admission controls and scoped runtime pressure policy with explicit host-fatal residuals, honest; C: kill random processes, unpredictable; D: ignore mailbox growth, misses practical exhaustion. | **B**, recommended and agent-selected: distinguish controllable refusal/cancellation from VM-wide failure beyond the language's recovery authority. |
| CP-129-3 | A: resource failure returns arbitrary partial values, fast but unsound; B: typed/refusal/trap outcomes by producer plus transactional cleanup, explicit; C: all exhaustion is static invalidity, wrong for runtime; D: hide limits in implementation, nonportable. | **B**, recommended and agent-selected: C012/C036 require visible classification and P090 supplies queue/admission semantics. |

1. Audit aggregate complexity and allocation paths; repair stale owner strings
   such as `G068/G129` in `lib/catena/implementation_limits.ex` while preserving
   historical language limits and reporting the current owning items.
2. Implement compiler budgets and runtime admission in limits, checker/coverage,
   package build, scope, and process modules; publish machine-readable units.
3. Run adversarial compiler inputs and isolated runtime pressure probes with
   measured bounds and restoration of transactional outputs.

**Acceptance:** within-floor valid programs run; above-budget work is refused or
classified without partial artifacts; exact thresholds, aggregate small inputs,
mailbox saturation, cancellation under pressure, and OS/VM fatal limits are
separated. **Gate:** deployment-relevant exhaustion behavior is exercised;
existing small bounded tests alone do not close P129.

## Item 130 — Supply-chain policy

**Baseline:** P130. **Depends on:** C006/C025, G098/C115/P116/P121/P127/P128.
**Basis:** [TUF research](../30-sources/the-update-framework-specification.md)
and [governance lifecycle](../60-specification/specifications-and-governance/evidence-identity-and-lifecycle.md).

| Decision | Explored alternatives and tradeoffs | Selected recommendation and rationale |
| --- | --- | --- |
| CP-130-1 | A: TLS plus package name is sufficient, simple but weak provenance; B: verified signed registry metadata and content digests with explicit trust roots, stronger; C: governance signatures automatically authenticate registry state, conflates protocols; D: no registries ever, limits ecosystem use. | **B**, recommended and agent-selected: adapt established update-security ideas while keeping registry authority distinct from Catena governance. |
| CP-130-2 | A: yanks delete historical identities, clean but breaks replay; B: immutable content identities with separate availability/admission status, more records; C: ignore compromised releases, preserves builds but unsafe; D: silently replace tarballs under a version, destroys integrity. | **B**, recommended and agent-selected: historical reproduction and current admission answer different questions and need separate decisions. |
| CP-130-3 | A: native dependencies need no extra evidence, convenient but wider trust; B: bind native artifacts, build provenance, platform scope, and trusted obligations, review cost; C: treat reproducible build as proof of safety, false; D: forbid all native packages, too restrictive. | **B**, recommended and agent-selected: artifact authenticity and reproducibility do not establish native correctness. |

1. Specify registry roots, delegated publishers, metadata freshness/rollback,
   content acquisition, yanks, compromise response, mirrors, and offline policy.
2. Add **new** `lib/catena/package/registry.ex`; integrate deps/build acquisition,
   assurance, trust adapters, and native package metadata.
3. Test a local fixture registry under rollback, equivocation, key rotation,
   compromised release, mirror mismatch, and offline replay scenarios.

**Acceptance:** authentic authorized content resolves and builds; forged,
replaced, stale, or wrong-platform artifacts fail; yanked-but-locked historical
builds and newly denied compromised content follow explicit separate policies.
**Gate:** an implemented registry client/admission contract and recorded attack
fixtures; no claim of adopting TUF wholesale without protocol conformance.

## Item 131 — Secrets and capabilities

**Baseline:** P131. **Depends on:** C005/C006/C082, P106/G096/G098/P121/G124.
**Basis:** [top-level capability requirement](../60-specification/top-level-effects/the-top-level-boundary.md)
and [lexically scoped effects](algebraic-effects-and-handlers.md).

| Decision | Explored alternatives and tradeoffs | Selected recommendation and rationale |
| --- | --- | --- |
| CP-131-1 | A: plain strings in manifests/environment by default, easy but leaks; B: opaque secret references delivered by explicit capabilities, extra service; C: compiler stores private keys, violates signer separation; D: no credentials supported, impractical. | **B**, recommended and agent-selected: credential transport is explicit and deny-able; retrieval is an effect rather than hidden compiler input. |
| CP-131-2 | A: redact only final logs, partial protection; B: classify sensitive values at entry and redact diagnostics/traces/history/artifacts, wider enforcement; C: erase all diagnostics, private but unusable; D: hash secrets publicly and call them hidden, leaks low-entropy values. | **B**, recommended and agent-selected: carry sensitivity through every observation surface without claiming protection against an already-compromised host. |
| CP-131-3 | A: build tools inherit full VM authority, convenient but hidden; B: constrained worker processes plus declared filesystem/network/native authority, explicit limitations; C: trust effect typing to sandbox native code, false; D: prohibit generators and foreign tools, too narrow. | **B**, recommended and agent-selected: effect types express obligations; OS isolation and host trust must enforce the external boundary separately. |

1. Specify secret handles, capability attenuation/revocation, transport/storage,
   redaction, audit events, worker isolation, and residual host trust.
2. Integrate environment/foreign/build adapters with `lib/catena/diagnostic.ex`,
   `report.ex`, `assurance.ex`, and **new** `lib/catena/runtime/secret.ex`.
3. Use sentinel credentials to inspect every output and crash/history path;
   distinguish identity metadata from actual secret bytes.

**Acceptance:** explicitly authorized services receive credentials without public
artifact leakage; denied capabilities and forged handles fail; crashes, canceled
work, revoked sessions, and transformed/nested secrets retain stated redaction.
**Gate:** concrete transport/isolation/redaction behavior is tested; no promise
of secrecy from the VM administrator or malicious admitted native code.

## Item 132 — Progress and preservation targets

**Baseline:** C132, complete **statement of targets only**. **Depends on:**
C002/C003/C010/C081; integrates P084/P085/G095/G096/P133/P134/G139.
**Basis:** [integrated theorem and open composition lemma](../60-specification/progress-and-preservation/the-integrated-theorem.md)
and [formal-validation inquiry](../40-inquiries/what-should-a-greenfield-catena-type-system-guarantee.md).

| Decision | Explored alternatives and tradeoffs | Selected recommendation and rationale |
| --- | --- | --- |
| CP-132-1 | A: treat tests as proof, easy but false; B: retain the completed target statement and separate proof ledger, honest; C: reopen target wording merely because proof is pending, confuses scope; D: remove composition obligation, weakens ambition. | **B**, recommended and agent-selected: preserve C132's bounded completion and explicitly route all undischarged lemmas to the formal program. |
| CP-132-2 | A: assume extensions inherit preservation, convenient but unsupported; B: require each public runtime/foreign slice to state and discharge its boundary obligations, accountable; C: postpone all semantics until one grand proof, deadlock; D: prove only pure examples and claim the language, under-scoped. | **B**, recommended and agent-selected: conditional extensions require actual preservation premises and evidence, not automatic theorem enlargement. |

1. Keep the existing target statements stable and inventory each component
   premise, interaction lemma, and residual assumption with current proof status.
2. Preserve `test/catena/c132_progress_preservation_test.exs` and reference/BEAM
   witnesses; link extensions to their own statement and proof artifacts.
3. Route the composition proof to P133/P134's models and G139's release ledger;
   never change a proof status because a finite test corpus passes.

**Acceptance:** current witnesses preserve values/traps/effect closure; unhandled
requests and malformed core remain rejected; divergent/resource-bounded runs are
not misclassified as theorem counterexamples without semantic analysis.
**Gate:** C132 remains complete as a statement, while unproved components and
composition remain visibly unproved until checked proof artifacts exist.

## Item 133 — Reference evaluator

**Baseline:** P133. **Depends on:** C010/C132 and each admitted semantic slice;
source elaboration waits for P109. **Basis:**
[formal kernel](../60-specification/formal-semantic-kernel/README.md) and
[composition obligation](../60-specification/progress-and-preservation/the-integrated-theorem.md).

| Decision | Explored alternatives and tradeoffs | Selected recommendation and rationale |
| --- | --- | --- |
| CP-133-1 | A: call production backend as the reference, easy but circular; B: integrate existing independent machines through a common observation contract, more adapters; C: rewrite everything into one evaluator immediately, risky; D: keep disconnected per-feature examples forever, incomplete. | **B**, recommended and agent-selected: preserve structural independence while covering cross-feature composition systematically. |
| CP-133-2 | A: model real network/time directly, realistic but nondeterministic; B: explicit abstract external responses and bounded schedules, replayable; C: ignore foreign/resources, under-scoped; D: claim every real host behavior is explored, impossible. | **B**, recommended and agent-selected: model allowed observations and declared trust assumptions, then test concrete adapters against that contract. |
| CP-133-3 | A: compare only final values, simple but misses effects; B: compare values, kinded traps, ordered events, lifetime, and permitted divergence bounds, richer; C: require identical internal machine states, overconstrains representation; D: treat timeout as equal divergence, unsound. | **B**, recommended and agent-selected: the semantic observation relation includes every promised external behavior without freezing implementation state. |

1. Inventory admitted forms against evaluator support and define a common
   observation schema, including unsupported-model outcomes rather than silent skips.
2. Extend `lib/catena/reference/evaluator.ex`, `lib/catena/effect/reference.ex`,
   `lib/catena/kernel/stepper.ex`, and `lib/catena/kernel/explorer.ex`; add
   explicit resource/foreign models and source elaboration adapters later.
3. Execute cross-feature programs and publish coverage links to every obligation.

**Acceptance:** data/conditions/effects/process/resource/foreign combinations
produce expected observations; forged core and unsupported model events fail
explicitly; schedule/fuel bounds, cancellation races, and infinite behavior are
reported with precise scope. **Gate:** integrated admitted-language coverage is
complete, with source adoption added after P109; reference agreement is not proof.

## Item 134 — Differential testing

**Baseline:** P134. **Depends on:** P133/G122, all admitted runtime boundaries;
first repair P050/P053/P057. **Basis:**
[completion audit](../50-journal/2026-09-06-checklist-completion-audit.md),
[property-testing research](../30-sources/claessen-hughes-2000-quickcheck.md), and
[effect/failure targets](../60-specification/progress-and-preservation/the-effects-and-failure-targets.md).

| Decision | Explored alternatives and tradeoffs | Selected recommendation and rationale |
| --- | --- | --- |
| CP-134-1 | A: random source bytes only, good parser stress but few valid programs; B: typed/effect-aware generators plus separate invalid mutations, focused coverage; C: fixed happy paths only, weak interactions; D: generate using production lowering, correlated defects. | **B**, recommended and agent-selected: valid semantic generation and hostile boundary cases answer different questions and both are needed. |
| CP-134-2 | A: backend output strings count as behavior evidence, cheap but inadequate; B: execute reference and BEAM paths and compare declared observations, real coverage; C: compare two modes sharing all logic, correlated; D: compare only termination, misses values/traces. | **B**, recommended and agent-selected: the reopened comprehension gaps specifically demonstrate why textual assertions are insufficient. |
| CP-134-3 | A: discard failing seeds after fixes, loses history; B: persist minimized counterexamples with source/toolchain/observation identity, durable; C: retry nondeterministic cases until pass, hides races; D: require exact scheduler interleaving across VM runs, overconstrained. | **B**, recommended and agent-selected: compare allowed trace sets and retain reproducible distinguishing witnesses. |

1. Add executable comprehension filter/ordering/failure witnesses before broad
   random generation; bind obligation IDs to actual observed assertions.
2. Build generators/shrinkers under **new** `test/support/semantic_generators.ex`
   and suites in `test/catena/`; invoke independent reference and production APIs.
3. Expand by feature-interaction matrix across layouts, optimizations, effects,
   process schedules, resources, native adapters, and later source elaboration.

**Acceptance:** seeded programs agree on values/traps/events; injected ordering,
callback-count, codec, and cancellation faults are detected; empty/deep programs,
finite schedule exhaustion, and minimized race cases retain honest bounds.
**Gate:** systematic generated/adversarial coverage and durable counterexamples;
tag presence or test count alone never establishes conformance.

## Item 135 — Optimizer validity

**Baseline:** P135. **Depends on:** C004/C030, P108/P133/P134/G138.
**Basis:** [law evidence tiers](../60-specification/traits-and-categorical-operations/laws-derivation-and-testing.md)
and [categorical operational rules](../60-specification/traits-and-categorical-operations/operational-semantics.md).

| Decision | Explored alternatives and tradeoffs | Selected recommendation and rationale |
| --- | --- | --- |
| CP-135-1 | A: unrestricted algebraic rewriting, fast but ignores effects/divergence; B: explicit rewrite inventory with machine-checkable premises, controlled; C: no optimization ever, simple but poor performance; D: profile-guided semantics guesses, unsafe. | **B**, recommended and agent-selected: categorical laws apply only with admitted evidence and operational side conditions. |
| CP-135-2 | A: trust optimizer annotations, cheap but weak; B: reverify typed core and validate rewrite certificates/premises, stronger; C: final BEAM compilation means correctness, false; D: test selected outputs only, misses preconditions. | **B**, recommended and agent-selected: preserve verify-before-lower and reject a transformation whose evidence is missing. |
| CP-135-3 | A: optimize every feature at once, broad risk; B: begin with simple proven pure rewrites and grow through measured differential cases, incremental; C: enable only in release builds without tests, dangerous; D: accept faster wrong results, defeats language purpose. | **B**, recommended and agent-selected: performance improvements must preserve order, multiplicity, traps, sharing, and termination distinctions. |

1. Inventory current specialization, layout selection, condition lowering,
   comprehension expansion, and backend transformations with explicit premises.
2. Add **new** `lib/catena/optimizer.ex` only as needed; keep certificate checking
   in `lib/catena/typed_core/verifier.ex` and `kernel/verifier.ex`; preserve a
   disabled-optimization comparison path in compiler options.
3. For each rewrite, provide a local correctness argument, positive/negative
   premise fixtures, and reference/BEAM before/after observations plus benchmarks.

**Acceptance:** admitted pure rewrites preserve observations; absent law/purity/
totality evidence refuses the rewrite; trap, divergence, zero callbacks, shared
resources, and large structures exercise counterexamples to naive equations.
**Gate:** every enabled transformation has a recorded justified domain and evidence.

## Item 136 — Compatibility suite

**Baseline:** P136. **Depends on:** C008/C025/C028, P099/P116/P121/P128; hot upgrade
coverage depends on G092. **Basis:** [compatibility layers](../60-specification/api-and-abi-compatibility/compatibility-layers-and-versions.md)
and [edition lifecycle](../60-specification/editions-and-feature-lifecycle/README.md).

| Decision | Explored alternatives and tradeoffs | Selected recommendation and rationale |
| --- | --- | --- |
| CP-136-1 | A: latest revision tests suffice, cheap but misses retention; B: exact retained revision/interface/toolchain matrix, substantial but explicit; C: rebaseline old failures as expected, hides regressions; D: promise every future OTP, unsupported. | **B**, recommended and agent-selected: compatibility must exercise historical selections and declared platform support. |
| CP-136-2 | A: tiny package pairs only, bounded but incomplete; B: generated realistic dependency graphs plus curated historical applications, broader; C: real registry popularity as correctness, weak; D: compare version strings only, ignores interfaces. | **B**, recommended and agent-selected: diamond/SCC/edition/data-evolution interactions need executable graph coverage. |
| CP-136-3 | A: all upgrades mean hot code replacement, conflates layers; B: separate source/interface/rebuild/runtime-upgrade expectations, precise; C: byte inequality means breaking change, incorrect; D: signatures silently migrate, invalidates history. | **B**, recommended and agent-selected: C028's layered stance and G092's later protocol need distinct oracles. |

1. Build a machine-readable matrix for source acceptance, interface diffs,
   dependency replay, data evolution, toolchain support, historical signatures,
   and admitted hot upgrades.
2. Extend `test/catena/c008_editions_lifecycle_test.exs`,
   `c025_package_deps_test.exs`, `c028_api_compat_test.exs`, and integrated package
   fixtures; use `lib/catena/package/compat.ex` as one checked boundary.
3. Run both positive retained cases and intentional downgrade/breaking changes;
   report unsupported combinations separately from failures and passes.

**Acceptance:** declared compatible graphs rebuild and run; unclaimed increments,
wrong editions, malformed locks, and unsupported hot upgrades fail; oldest/newest
supported hosts and wide/deep graphs meet explicit budgets. **Gate:** integrated
matrix evidence, never an ecosystem-wide claim from a few pairwise fixtures.

## Item 137 — Usability gate

**Baseline:** G137. **Depends on:** P107/P109/P117/P119/G120; semantic study
preparation can start now. **Basis:** [approachability criteria](approachable-language-vocabulary.md),
[cognitive-dimensions research](../30-sources/green-petre-1996-cognitive-dimensions.md),
and [compiler-explanation research](../30-sources/barik-et-al-2018-compiler-explanations.md).

| Decision | Explored alternatives and tradeoffs | Selected recommendation and rationale |
| --- | --- | --- |
| CP-137-1 | A: agent self-assessment counts as usability, fast but not human evidence; B: observed task study with real programmers and counterbalanced conditions, more effort; C: preference poll only, easy but weak behavior evidence; D: expert mathematical review alone, misses intended audience. | **B**, recommended and agent-selected: the research defines approachability through prediction, task completion, transfer, and repair. |
| CP-137-2 | A: recruit/contact participants automatically, convenient but unauthorized; B: prepare protocol/materials now and obtain authorization before outreach, staged; C: invent plausible participant results, unacceptable; D: abandon usability until release, too late. | **B**, recommended and agent-selected: present user authorization covers planning/implementation, not contacting people or fabricating studies. |
| CP-137-3 | A: choose thresholds after seeing results, biased; B: pilot then preregister tasks, cohort, thresholds, and exclusions before the main study, accountable; C: one successful expert proves accessibility, weak; D: require universal perfect performance, impractical. | **B**, recommended and agent-selected: nominate a six-person pilot and a 24-person main study split between general and functional programmers, then justify adequacy and limits before interpreting results. |

1. Prepare consent/data-minimization materials, neutral instructions, task scripts,
   coding rubric, error-repair tasks, and analysis plan; do not select new terms.
2. Exercise existing mapping/independent combination/sequencing/traversal semantics,
   handlers, guards, comprehensions, and diagnostics; add public-source conditions
   only after vocabulary/grammar co-design.
3. Put reproducible tasks in **new** `test/usability/` in the compiler repository,
   with compiler invocation scripts and anonymized aggregate evidence in a
   research journal after an authorized observed study.

**Acceptance:** actual participants predict behavior, complete tasks, transfer
operations across types, and repair errors against preregistered criteria;
misconceptions and unsuccessful tasks are retained, not excluded for convenience;
novice/expert differences and small-sample uncertainty are reported.
**Gate:** remains open until human evidence exists; prepared materials, agent
simulations, and imagined scores cannot close it.

## Item 138 — Performance envelope

**Baseline:** G138. **Depends on:** P108/P129/P135; profiles cover every admitted
feature and supported P099 host. **Basis:** [categorical cost obligations](../60-specification/traits-and-categorical-operations/operational-semantics.md)
and [resource observability](../60-specification/resource-observability/README.md).

| Decision | Explored alternatives and tradeoffs | Selected recommendation and rationale |
| --- | --- | --- |
| CP-138-1 | A: one microbenchmark, cheap but unrepresentative; B: operation microbenchmarks plus realistic applications and adversarial shapes, broader cost; C: compare only against interpreter speed, flattering but weak; D: promise performance before measuring, unsupported. | **B**, recommended and agent-selected: useful functional applications need evidence across compiler, runtime, code size, and diagnostics. |
| CP-138-2 | A: absolute timings from one laptop as portable limits, misleading; B: reproducible environment metadata, distributions, and relative baselines, honest; C: best run only, biased; D: average without warmup/variance, hides instability. | **B**, recommended and agent-selected: distinguish empirical envelopes from normative asymptotic/callback/stack guarantees. |
| CP-138-3 | A: optimize until all benchmarks improve, risks semantics; B: semantic conformance gate before accepting measured wins, disciplined; C: allow trace changes for speed, violates laws; D: disable provenance to make numbers look better, hides tradeoff. | **B**, recommended and agent-selected: report costs of diagnostics/provenance/effects explicitly, with separate supported modes. |

1. Define workloads for direct/curried calls, traits, ADTs, matching, guards,
   comprehensions, handlers, processes/messages, resources, foreign adapters,
   erasure, code size, compile time, and diagnostic provenance.
2. Add **new** `bench/` harnesses using compiler APIs and generated workload
   families; bind seed, OTP/ERTS/compiler identity, hardware, flags, and repetitions.
3. Compare ordinary Erlang baselines where semantically equivalent, scaling curves,
   and optimizer-off/on modes; retain raw measurements and negative results.

**Acceptance:** harnesses reproduce workload identity and detect known artificial
regressions; semantically different or timed-out runs are not scored as speedups;
empty/large/pathological data, scheduler contention, cold/warm builds, and memory
retention are reported. **Gate:** measured supported-platform envelopes and
regression policy, not invented target numbers or one favorable example.

## Item 139 — Release-readiness definition

**Baseline:** G139. **Depends on:** all admitted semantic items, P107/P109 holds,
items 126–136, G137/G138; G141 has a separate late-0.x gate.
**Basis:** [completion checklist](../00-inbox/language-specification-completeness-checklist.md),
[authority policy](../SPECIFICATION-AUTHORITY.md), and
[unproved composition obligation](../60-specification/progress-and-preservation/the-integrated-theorem.md).

| Decision | Explored alternatives and tradeoffs | Selected recommendation and rationale |
| --- | --- | --- |
| CP-139-1 | A: test count alone defines readiness, simple but misleading; B: explicit experimental/complete/stable gate profiles with no hidden gaps, accountable; C: all future features required for any release, prevents iteration; D: market a held grammar as complete, false. | **B**, recommended and agent-selected: an experimental semantic release may disclose open work; a complete public language cannot bypass held grammar, human evidence, or admitted runtime obligations. |
| CP-139-2 | A: tests discharge the composition lemma, false; B: proof ledger with exact theorem scope and checked artifacts before claiming proof, rigorous; C: erase the theorem goal, weakens research; D: call every component proven because its statement is normative, confuses authority with evidence. | **B**, recommended and agent-selected: disclose every open component/interaction proof; finite evidence supports experimentation but never an integrated safety theorem claim. |
| CP-139-3 | A: document presence marks readiness, easy but weak; B: machine-readable obligation/platform/limitation manifest checked against actual evidence, maintained; C: unchecked release checklist, stale risk; D: approve contradictory chapters if tests pass, violates authority. | **B**, recommended and agent-selected: release includes contradiction audits, coverage checks, and precise known-limit publication. |
| CP-139-4 | A: prose proof sketches alone suffice for the strongest safety claim, reviewable but easy to omit cases; B: mechanize the core and composition in a pinned proof checker, substantial work; C: bounded exploration substitutes for proof, wrong scope; D: abandon proof and assert correctness by design, unsupported. | **B**, recommended and agent-selected: use the Rocq workbench selected by CP-139-5 to encode the actual admitted relations; no successful proof is asserted by selecting its checker. |
| CP-139-5 | A: Rocq inductive judgments and kernel-checked proofs, direct fit but proof engineering work; B: Lean dependent-type development, strong alternative but separate ecosystem integration; C: Isabelle/HOL relations, mature logical approach but a different embedding choice; D: custom certificate kernel, minimal intended trust but new kernel correctness obligations. | **A**, recommended and agent-selected: start the proof workbench in Rocq with explicit inductive typing/step relations and pinned checked dependencies; this is a Catena engineering judgment from the present relational calculus, not evidence that Rocq is universally superior. |

1. Define release classes, required chapters, full source/tooling adoption,
   conformance thresholds, support matrix, usability/performance evidence,
   compatibility promises, and nonempty explicit limitation/proof ledgers.
2. Add **new** `lib/catena/release/readiness.ex` and release-manifest tests;
   consume conformance metadata, package artifacts, proof identities, and evidence.
3. Audit normative cross-references and contradictions, including recorded package
   underscore and abstraction-invariant ambiguities, before version claims; each
   finding requires an explicit disposition rather than silently choosing code.
4. Start the selected Rocq proof workbench under **new** `proof/` in the compiler
   repository. Pin a tested checker/dependency build, encode syntax and typing/step
   relations independently from production code, prove substitution/context
   compatibility and component interaction lemmas, then the composed theorem.
   Record at least four alternatives for further proof-engineering forks before
   executing them; admit no placeholder axiom or unchecked escape as a discharged
   Catena theorem.

**Checker-selection evidence:** official [Rocq inductive-type documentation](https://rocq-prover.org/doc/v9.0/refman/language/core/inductive.html)
explains inductive definitions and generated induction principles; the
[Lean elaboration reference](https://lean-lang.org/doc/reference/latest/Elaboration-and-Compilation/)
describes kernel checking; [Isabelle's project overview](https://isabelle.in.tum.de/)
identifies its generic proof-assistant/HOL approach. These pages were inspected
on 2026-09-06 for tool capabilities only. The archived
[modular actor-semantics research](../30-sources/bereczky-et-al-2024-core-erlang-formalisation.md)
supports separating local/process/global relations; it does not prove Catena
or establish a comparative winner among proof assistants.

**Acceptance:** a fully supported release manifest passes and produces a precise
claim set; absent witnesses, held source adoption, contradictory rules, unsupported
hosts, and forged proof records block the corresponding release class; experimental
releases with disclosed proof gaps cannot upgrade their labels automatically.
**Gate:** readiness definition/tool can complete before the language; declaring
an actual complete language waits for every applicable gate. Publication remains
an explicit user action, not an effect of passing this check.

## Item 140 — Excluded advanced type features

**Baseline:** C140, preserve completion. **Depends on:** C001/C068; coordinates
P101/P102/G141 without admitting excluded features as convenience shortcuts.
**Basis:** [eight exclusions and seven-point arrival gate](../60-specification/excluded-advanced-type-features/the-exclusion-table-and-gate.md).

| Decision | Explored alternatives and tradeoffs | Selected recommendation and rationale |
| --- | --- | --- |
| CP-140-1 | A: admit advanced forms to simplify one library, expedient but unsupported; B: preserve each exclusion and use existing checked encodings, constrained; C: make the exclusion permanent regardless of evidence, overstates scope; D: admit all eight together, ignores per-form gate. | **B**, recommended and agent-selected: existing higher-rank/GADT/existential profile is sufficient until repeated-use evidence justifies a separately reviewed arrival. |
| CP-140-2 | A: new optimizer or self-host code may bypass the gate, convenient but unsound; B: retain rejection/inference-boundary regressions through every frontend, consistent; C: accept unsupported forms then fail in backend, late ambiguity; D: forbid C068 too, gratuitous regression. | **B**, recommended and agent-selected: preserve the distinction between checked admitted advanced features and the eight excluded forms. |

1. Keep the exact exclusion inventory and independent seven-point arrival gate
   linked from library, parser, and self-hosting work.
2. Preserve `lib/catena/type/advanced.ex`, `lib/catena/type/parser.ex`, and
   `test/catena/c140_excluded_advanced_test.exs` across new frontend integration.
3. If actual implementation uncovers repeated need, open a per-form inquiry with
   library alternatives and evidence; do not automatically add the type feature.

**Acceptance:** signature-directed GADTs and declared existentials keep working;
impredicativity, unrestricted inference, and existential escape remain rejected;
annotation and skolem-scope boundaries retain exact diagnostics. **Gate:** C140
stays complete within current exclusions; neither planning nor self-hosting
silently changes the admitted type system.

## Item 141 — Compiler self-hosting

**Baseline:** G141, an open **late-0.x** milestone. **Depends on:** usable P101–P106,
P109/P117/P121, G095/G096, P099/P128/P133/P134/P136/G139.
**Basis:** [language completion scope](../00-inbox/language-specification-completeness-checklist.md),
[functional/type-system synthesis](catena-greenfield-type-system.md), and
[OTP Abstract Format strategy](../30-sources/erlang-otp-29-compiler-recommendations-language-implementors.md).

| Decision | Explored alternatives and tradeoffs | Selected recommendation and rationale |
| --- | --- | --- |
| CP-141-1 | A: rewrite bootstrap compiler immediately, ambitious but language/tooling incomplete; B: staged late-0.x port after required subset works, controlled; C: remain Elixir forever, avoids risk but abandons requested milestone; D: change target VM during self-hosting, unnecessary scope. | **B**, recommended and agent-selected: preserve the BEAM-only OTP 29 Abstract Format boundary and keep Elixir as the recoverable bootstrap. |
| CP-141-2 | A: port parser/checker/backend together, large unreviewable change; B: port pure compiler passes first with differential interfaces, incremental; C: wrap Elixir calls and call it self-hosted, misleading; D: use excluded type features to ease porting, bypasses C140. | **B**, recommended and agent-selected: functional transformations over ordinary ADTs exercise Catena's composition strengths without new type-system scope. |
| CP-141-3 | A: successful self-compilation alone proves correctness, circular; B: stage-zero/one/two builds with fixed-point or declared semantic checks, stronger; C: compare executable filenames, meaningless; D: trust bootstrap source without provenance, incomplete trust. | **B**, recommended and agent-selected: state exactly what stage equality establishes and retain independent reference/differential evidence. |
| CP-141-4 | A: delete Elixir bootstrap at first success, irreversible recovery risk; B: retain pinned bootstrap, provenance, reproducible stage artifacts, and rollback, larger distribution; C: distribute only an opaque stage-two binary, weak trust; D: silently download arbitrary bootstrap, supply-chain gap. | **B**, recommended and agent-selected: bootstrap trust and reproducibility are explicit release inputs, not hidden in a build script. |

1. Define the required Catena subset and demonstrate parser/module ADTs, pure
   transformations, file/process capabilities, diagnostics, packaging, and typed
   OTP interoperability using ordinary application programs first.
2. Introduce **new** `bootstrap/` in the compiler repository after P109 adoption;
   port pure units corresponding to `lib/catena/canonical_json.ex`, `scc.ex`,
   type/row/unification modules, then parser/checker/verifier/backend passes.
   Keep Elixir wrappers only for explicitly inventoried host services.
3. Build stage one with pinned Elixir stage zero, stage two with Catena stage one,
   and a further comparison stage when needed; compare compiler artifacts under
   P128's exact envelope or use an explicitly justified semantic oracle if bytes
   cannot yet match. Record every residual bootstrap component.
4. Run the full conformance, differential, historical compatibility, and package
   suites under both implementations; perform a real rollback/rebootstrap drill.

**Acceptance:** the Catena implementation rebuilds the compiler and compiles the
same application corpus; altered bootstrap/artifact identities and hidden Elixir
compiler-pass dependencies are detected; clean offline builds, stage drift,
interrupted upgrades, and rollback are exercised. **Gate:** self-hosting means
actual compiler passes are implemented in Catena with declared residual host
services; it is not a wrapper, and it does not establish freedom from a malicious
bootstrap merely by reaching a fixed point.

## Cross-item sequencing and open holds

The execution graph begins with the existing completion repairs and resource/runtime
contracts owned by the companion plan. G095's codecs and P093's representations
can then progress with P094's call descriptors. G096/G098 depend on explicit
lifetime and cancellation rules. P094/G096/P106/P131 first co-design call, lifetime, codec, and authority
interfaces. Implement a minimal checked foreign adapter over retained inputs with
explicit test-harness authority next; this does not grant an ordinary application
ambient services. Then amend P106's entry contract and implement opaque authority
provisioning, fresh lexical handler installation, and final callback/environment
integration. P127's native trust metadata is designed alongside these interfaces.

P101–P105 can implement pure standard-library semantics with current identifiers
and internal fixtures. Their new public exports remain pending P107/P109. P108,
P117, P121, items 126–136, and G138 have substantial syntax-independent work and should
run alongside semantic slices. G118/G120/G123 can build internal engines now but
cannot claim complete source tools before P109. P119 can render checked interfaces
and extracted documentation before public-source doctests exist.

The main potential cycles are resolved by contract-first boundaries: define
capability/lifetime/foreign interfaces before building adapters; establish build
input and registry trust contracts before network acquisition; write common
observations before broad differential generators; and collect parser adoption
requirements without implementing public grammar. A prerequisite can be a settled
internal contract when explicitly stated; that never changes its checklist item
to complete prematurely.

P107/P109 remain user-held design gates. G137 requires actual human observations
and authorization before participant outreach. G139 distinguishes completing a
release gate definition from passing it; incomplete experimental releases cannot
claim a complete public language. Proof development must discharge the real
component and composition obligations before any proof claim. G141 remains an
open late-0.x implementation program and follows, rather than drives, the public
language and tool contracts. D059/D083 are separate explicit feature holds; this
volume never makes them prerequisites through a library or self-hosting shortcut.

## Connections

- The [language completion checklist](../00-inbox/language-specification-completeness-checklist.md)
  remains the status ledger; this plan supplies decisions and executable closure
  criteria without pre-checking future work.
- The [design decision register](design-decision-register.md) records delegated
  selections with their provenance and later durable implementations.
- The [category-theory synthesis](category-theory-for-programming.md) and
  [combinator synthesis](combinators-for-algebraic-data-and-categorical-programming.md)
  explain the law/operational-contract split that governs implementation choices.
- The [formal-validation inquiry](../40-inquiries/what-should-a-greenfield-catena-type-system-guarantee.md)
  owns unresolved proof work; a plan, test result, or normative statement does
  not close its composition obligation.
