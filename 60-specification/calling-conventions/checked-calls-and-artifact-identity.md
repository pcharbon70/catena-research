---
title: "Checked Calls and Artifact Identity"
kind: specification
created: "2026-09-09"
status: normative
spec_version: "0.1.59"
tags:
  - specification
  - functions
  - representation-independence
aliases: []
---

# Checked Calls and Artifact Identity

## Status and authority

This is the normative C094 contract for exact revision `0.1.59`, under the
[authority policy](../../SPECIFICATION-AUTHORITY.md),
[conformance vocabulary](../../CONFORMANCE-VOCABULARY.md), and
[implementation limits](../../IMPLEMENTATION-LIMITS.md). It applies at the exact selection stated below.
The [workbench](../../50-journal/2026-09-09-calling-conventions.md) records
the implementation evidence and explicit approval of this revision.

The selection is edition `0.1`, revision `0.1.59`, with no previews. Its inputs
are verified retained ordinary core, exact `0.1.8` or `0.1.58` kernel core,
and the checked supervision descriptions admitted by C089. It does not turn a
retained core into a different core revision. A calling artifact over ordinary
or kernel core records the new calling frontend and exact selection. A calling
sidecar over a retained C089 lifecycle artifact binds that artifact without
relabeling its historical frontend or revision (`CV-OBL-001`).

The contract implements the call-shape choices in the
[reviewed plan](../../20-notes/language-completion-plan-delivery.md#item-094-calling-conventions).
General foreign declarations and asynchronous callbacks remain P096, recursive
foreign data codecs G095, full stack tooling P100, and public vocabulary P109.
No cross-build binary ABI, serialized closure environment, live-upgrade promise,
or new textual declaration is established.

## Call classes and admission

| Class | Shape and checks | Execution boundary |
| --- | --- | --- |
| Internal direct call | Verified callee, typed arguments, source written arity; hidden worker arguments remain compiler-owned. | Existing ordinary/kernel lowering. |
| Internal curried call | One semantic argument at each function stage; latent effects belong to that stage. | Existing direct or CPS closure lowering. |
| Saturated checked entry | Exact exported BEAM arity; all data arguments checked before entry; return type is the residual type after consuming that written arity. | New checked entry adapter. |
| Scoped partial entry | Verified factory evaluates the actual source function expression; each subsequent call consumes one stage. | Owner-local closure scope. |
| Higher-order pure parameter | A live handle from the same scope with exactly the declared function type. Raw host funs are refused. | The already verified immutable function value is passed to compiled code. |
| Effectful call | Direct wrappers and private CPS workers preserve declared effects; a CPS closure stage adds handlers and continuation to its one explicit argument. | Existing checked handlers execute inside compiled code. The generic data/closure adapter refuses unprovided initial or latent effects. |
| Historical process entry | Exported spawn symbol and explicit parameter count come from verified core and actual generated exports; result is the typed opaque process carrier. | C010's retained process boundary. No data-codec PID admission is added. |
| Managed process entry | Checked fresh zero-argument worker, actual exported start symbol, native managed-start result. | C089's verified lifecycle artifact and managed owner. |
| Foreign OTP lifecycle call | Two checked arguments: supervision flags and child specifications; linked-supervisor result. | The retained managed lifecycle invokes its fixed OTP wrapper. |
| OTP supervisor callback | One checked pair of flags and child specifications; supervisor-initialization result. | The existing lifecycle callback, under OTP supervision. |
| Synchronous data callback | Explicit scope authority; one checked pure data argument and checked pure data result; live owner-local handle required on every entry. | An adapter-created native unary fun; invocation failure is visible. |
| General foreign call or asynchronous callback | No ambient module/function lookup, cross-process callback transfer, untyped fun ingress or inferred effect authority. | Not admitted here; P096 owns the additional contract. |

The inventory is an admission contract, not a promise that every internal type
has a general foreign codec. The new data entry adapter supports Int, Bool,
Unit, finite Float, Text, Character, Bytes, products, closed records and closed
variants using C093's checks. Unsupported nominal, open-row, polymorphic,
authority or resource types are refused by this adapter before entry; their
internal calling behavior and separate checked conversion owners remain intact
(`CV-OBL-002`).

## Descriptor and executable identity

An ordinary/kernel call descriptor is derived from independently verified core
and the actual emitted Erlang forms. It records source module/origin, exported
entry symbols and BEAM arities, the full semantic function spine, each stage's
parameter/effects/result, native stage arity and hidden-argument count, entry
factories, actual generated functions, and their recorded source origins.
Written BEAM arity and full curried arity are distinct observations. Private
CPS workers are not exported merely to make their arity callable (`CV-OBL-003`).

The sidecar binds deterministic core and form digests, the retained interface
digest when one exists, every loaded Catena compiler module's executable identity,
and the tested OTP toolchain fingerprint. Its own digest excludes only its digest
field. Compilation cross-checks the supplied description against the exact forms,
compiler and toolchain and records the sidecar digest in the new artifact's
compile information. Retained interfaces gain a separate sidecar-building entry;
their serialized bytes are not extended (`CV-OBL-004`).

Artifact admission rebuilds the expected artifact from the verified core and
options and compares the complete result. Copied metadata, a rewritten binary
digest, matching module names, or an apparently matching signature are
insufficient. Wrong identities and unsupported descriptors fail before entry.
The lifecycle sidecar analogously re-derives its checked description, actual
exported child entries, manifest and exact retained binary (`CV-OBL-005`).

The host/compiler setup is trusted and payloads are untrusted. These checks do
not sandbox arbitrary hostile BEAM code running in the same VM. A scope checks
the loaded module's identity before each action and refuses subsequent entry
when code has been replaced. Concurrent hostile code loading is outside that
host model; no transactional code-pinning or live-upgrade claim follows.

## Application stages and lifetime

Factories preserve the source evaluation that produces a function value.
A partial application evaluates its argument and executes that application
stage immediately. It MUST NOT postpone a stage's trap or effect merely because
another argument is still needed. Saturated-call specialization is valid only
where the existing backend has established the inert lambda prefix. Immutable
captures and the
[semantic unary model](../functions-and-calls/arity-and-application.md)
remain unchanged (`CV-OBL-006`).

A scope belongs to its creating process. It stores verified closure values in a
private registry indexed by fresh references. A host fun, guessed reference,
wrong-type handle, handle from another scope or process, revoked handle or
expired scope does not establish a callable value. Scope exit removes the
registry even on abrupt completion. Handles count against an explicit positive
maximum, defaulting to 1,024. A call that would produce another handle beyond
the maximum refuses before executing that stage. Revocation releases a boundary
handle, not immutable function values that verified code has already captured
(`CV-OBL-007`).

The synchronous callback adapter requires explicit harness-supplied authority;
a payload cannot enable it. Every callback invocation rechecks its owner,
liveness, argument type and executable binding. It converts the checked result
back to the native carrier at the declared type. A callback retains its scope
requirement after being passed to foreign code. Creation and entry are visible
foreign-boundary trace events. General callback scheduling, transport,
cooperative cancellation and broader provisioning remain P096/P106
(`CV-OBL-008`).

The retained supervision adapter keeps C089's fresh-generation provisioning,
managed ownership, shutdown bounds and verified artifact checks. The sidecar
adds call-shape/build identity; it does not admit arbitrary child functions or
replace its
[checked lifecycle rules](../typed-supervision/checked-trees-and-lifecycle.md)
(`CV-OBL-009`).

## Failures, frames and limits

Invalid arguments, arities, descriptors, identities, scope owners, lifetimes,
unsupported types and missing authority are explicit boundary refusals.
Validation uses C093's explicit node and byte budgets. Saturated arguments are
validated as one product sharing one budget. A returned data value is checked
at the residual result type before being reported as successful. In an Erlang
callback position, a boundary refusal becomes the explicit callback-boundary
trap. Execution reports retain the original failure kind and reason; a Catena
trap crossing a callback remains that trap (`CV-OBL-010`).

The lowerers record source ownership while grouping actual generated functions.
A frame explanation is admitted only against the verified corresponding artifact.
It retains the complete supplied technical stack and maps exact recorded
module/function/arity entries to their source owner, origin and available span.
Unmapped host or anonymous frames and missing frontend spans remain unmapped or
missing. An optimized-away tail frame is not invented (`CV-OBL-011`).

The existing proper-tail-call guarantee is preserved. Generated closures,
wrappers and worker functions obey the inherited explicit/generated arity and
module-size limits. In particular, the portable 253-explicit-argument floor
remains compatible with a CPS worker's two additional arguments at generated
arity 255. Compiler verification and decoded-literal limits remain in force
when the calling artifact adds factories (`CV-OBL-012`).

## Variability register

This contract is deterministic and introduces no observable variability.
Closure-handle and data-validation budgets are explicit inputs, not hidden
implementation thresholds. Compiler arity, module-size and finite-allocation
boundaries inherit the standing implementation-limit policy. The exact tested
build and toolchain are admission requirements, not a discretionary
compatibility promise.

## Evidence (non-normative)

The [implementation workbench](../../50-journal/2026-09-09-calling-conventions.md)
records choices and commands. Compiler tests `calling_descriptor`,
`calling_scope`, `calling_metadata`, `calling_callback` and `calling_lifecycle`
exercise the new sidecars and adapters. The complete existing kernel,
effect, value-boundary, arity, recursion and supervision suites retain the
underlying call semantics. Independent Erlang fixtures execute both directions
of the checked boundary. General foreign completion is not inferred from these
narrow witnesses.

The user explicitly approved this revision and subsequent revision updates in
the same implementation session. Exact-selection and complete regression
results are recorded in the workbench.
