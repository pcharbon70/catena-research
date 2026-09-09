---
title: "Calling Convention Workbench"
kind: journal
created: "2026-09-09"
tags:
  - language-design
  - representation-independence
  - beam-vm
aliases: []
---

# Calling Convention Workbench

## Starting point

C093 completed through [compiler PR 140](https://github.com/pcharbon70/catena/pull/140)
and [research PR 90](https://github.com/pcharbon70/catena-research/pull/90).
Compiler `rewrite` synchronized at `401b4e68388cc13059c51276c7508dc56ecf21aa`;
research `main` synchronized at `8d57429e791c91b0bfab6afad6e12f2df1dd98ba`.
Both feature branches were deleted only after synchronization. The new work uses
`codex/calling-conventions` in both repositories. No continuation is scheduled.

The [CP-094 plan](../20-notes/language-completion-plan-delivery.md#item-094-calling-conventions)
requires versioned descriptors, preservation of curried evaluation stages and
traceable frames. P094 remains partial; no new semantic revision is registered.

## Implementation decisions

| Decision | Four alternatives explored | Recommended and selected |
| --- | --- | --- |
| CC-I01 | A: record exported BEAM arity and the full semantic function spine separately; B: assume they are equal; C: flatten every closure eagerly; D: derive semantics from a host arity error. | **A.** An ordinary one-argument export can return a closure and have a two-argument curried type. The descriptor retains both observations. |
| CC-I02 | A: derive symbols and arities from actual verified lowering; B: guess all helper names; C: trust caller-supplied arity metadata; D: expose every private worker as public ABI. | **A.** The sidecar cross-checks declared entries against actual exported EAF functions and inventories private functions separately. |
| CC-I03 | A: bind core, forms, interface and toolchain identity; B: use a module name alone; C: trust a display signature; D: promise cross-build binary compatibility. | **A.** Deterministic digests and re-derivation reject changed descriptions. Actual artifact binding and invocation remain subsequent gates. |
| CC-I04 | A: keep the descriptor experimental until every planned call class is witnessed; B: declare completion after the pure descriptor; C: count foreign callbacks as covered by arity alone; D: silently widen the previous revision. | **A.** General foreign calls/callbacks remain explicitly unadmitted in this initial sidecar; no persisted interface format changes. |

## Initial implementation and remaining gates

`Catena.Calling.Descriptor` derives the ordinary and kernel entry inventory,
semantic parameter/result types, written BEAM arities, exported process-spawn
entries, actual lowered helper inventory and identity digests. Descriptor
verification re-derives the complete sidecar. Initial tests cover the ordinary
arity distinction and fixed-kernel export/process inventory, including forged
metadata rejection. The first kernel test referenced a nonexistent fixture;
the existing `c010-kernel.catena` fixture replaces that path.

The sidecar does not yet authorize calls. Artifact binding, typed argument/result
adapters, staged/partial effectful calls, foreign/callback integration, source
frame mapping and the maximum-arity/tail-recursion witnesses remain outstanding.
These gates must be completed before P094 is checked or a completion PR is made.

## Staged adapter progress

The initial descriptor now authorizes a checked experimental artifact only after
an exact deterministic rebuild. The emitted BEAM records the sidecar digest;
the sidecar binds core, lowered forms, retained interface when available, the
complete loaded Catena compiler module identity set, and the tested OTP profile.
Embedded hashes alone are not accepted as proof of the accompanying binary.

Both backends add opt-in entry factories using their own lowering. The kernel
factory evaluates the original expression through its existing CPS lowering,
preserving effects/traps between lambda stages. The ordinary factory retains the
written parameter boundary and any closure returned by the exported wrapper.
Historical compilation without the calling option remains unchanged.

`Calling.Scope` owns immutable captured closures in a process-local registry.
Handles cannot be forged from a host fun, reused across owners, used after scope
exit or revocation, or retained beyond the explicit handle bound. Code replacement
invalidates a scope before another entry/application. The first scoped boundary
admits pure data parameters and curried pure data results. Closed internal effect
handlers execute normally; external effect authority is not inferred.

The lowerers record each actual generated function's source owner, span when
available, and additional argument count. Frame explanation verifies the artifact
and preserves every technical frame. It maps exact recorded functions and leaves
unmapped host/anonymous frames explicitly unmapped; it does not invent erased
tail frames or a source location that the frontend did not supply.

| Decision | Four alternatives explored | Recommended and selected |
| --- | --- | --- |
| CC-I05 | A: accept embedded hashes as binary proof; B: deterministically rebuild and compare the entire artifact; C: trust module names; D: load before checking metadata. | **B.** A substituted binary can carry copied or rewritten metadata; re-derivation binds actual executable content. |
| CC-I06 | A: buffer every partial argument until saturation; B: reuse backend expression lowering for entry factories; C: interpret all host callbacks separately; D: expose private CPS workers directly. | **B.** A first-stage trap must execute before a second argument exists. Backend-owned factories retain the existing evaluation semantics. |
| CC-I07 | A: accept arbitrary native funs; B: serialize captures; C: owner-local scoped handles with explicit revocation and a bound; D: permanent global closure registry. | **C.** Verified captures remain typed while lifetime, ownership and exhaustion are explicit. General cross-process callback transport remains a subsequent gate. |
| CC-I08 | A: guess helper ownership from names; B: record origins while grouping actual lowered functions; C: fabricate friendly frames; D: discard technical traces. | **B.** Mapping follows compiler evidence and retains unmapped technical frames and actual source spans. |
| CC-I09 | A: host OTP version alone identifies the compiler; B: compiler package version alone; C: bind every loaded Catena module identity alongside actual forms and OTP identity; D: no build binding. | **C.** Compiler/runtime implementation changes invalidate the exact build claim even when package labels remain unchanged. |
| CC-I10 | A: permit replacement code under the same module name; B: check loaded module identity before each scoped action; C: promise live upgrade; D: pin all VM code globally. | **B.** This explicit local boundary detects replacement before subsequent entry. Concurrent hostile code loading is outside the trusted-host model and no cross-build live-upgrade claim is made. |
| CC-I11 | A: widen retained interface bytes; B: expose separate interface-owned sidecar builders; C: omit interface identity; D: invent a stable ABI. | **B.** Existing serialized interface formats retain their admission rules while compiler call metadata is separately verified. |

The targeted witnesses cover separate Erlang caller compilation, argument refusal
before entry, copied/forged artifact rejection, partial/saturated agreement,
independent immutable captures, correct intermediate traps, handle lifetime,
compiler/BEAM metadata binding, real trap-frame provenance, closed handlers,
253 explicit parameters with a private 255-argument CPS worker, and one million
tail-recursive iterations through both saturated and partial adapters.
Initial fixture mistakes (`+` instead of retained `add`, and bare effect strings
instead of encoded effect identities) were corrected. A custom EAF attribute
initially preceded the module declaration; moving it after that declaration
resolved the compiler's undefined-module rejection.

This is progress, not P094 completion. General typed foreign/callback admission,
the remaining effect/process call adapter contracts, and final conformance
integration remain outstanding. No completion checkbox or semantic revision has
been advanced and no completion PR has been created.


## Callback and lifecycle witnesses

The scope now also accepts an exactly typed same-scope function handle as a
higher-order parameter. A synchronous unary data callback requires explicit
`allow_callbacks: true` harness authority. It checks owner, liveness, argument
and result at every ingress. An independent Erlang caller executes that native
adapter. Missing authority, wrong types, cross-process calls and callback-after-
close are refused. Existing verified immutable captures survive revocation of
the separate boundary handle.

`Calling.Lifecycle` derives a sidecar over C089's existing checked supervision
artifact. It verifies the actual exported zero-argument child start symbols,
records the two-argument OTP start wrapper and unary OTP init callback, and
binds the checked description, manifest, binary, compiler and toolchain. Its
start path revalidates before delegating to the established managed owner.
The runtime witness starts a tree and observes both supervisor and child die
when that owner completes. No general foreign capability is inferred.

| Decision | Four alternatives explored | Recommended and selected |
| --- | --- | --- |
| CC-I12 | A: permit arbitrary host fun parameters; B: require exactly typed same-scope handles; C: erase function types; D: forbid higher-order calls. | **B.** Verified values cross the call boundary without weakening type or owner checks. Revocation affects the external handle, not immutable source captures. |
| CC-I13 | A: ambient callback creation; B: explicit harness authority and checked synchronous owner-local callbacks; C: unbounded global callbacks; D: pretend cross-process callbacks have already been implemented. | **B.** Executes the call-shape witness while P096 retains asynchronous transport and broader authority/lifetime work. |
| CC-I14 | A: rebuild a second supervisor runtime; B: derive a sidecar over the existing verified lifecycle and actual exports; C: accept an arbitrary child MFA; D: reinterpret old artifact versions. | **B.** Reuses C089's executed ownership and artifact proof while adding compiler-bound call inventory. |
| CC-I15 | A: register 0.1.59 silently; B: retain experimental status and prepare the precise draft/patch after rejection; C: relabel 0.1.58 artifacts; D: omit version provenance. | **B.** The approval rejection is an external execution constraint; preparation continues without bypassing it. |

## Revision approval blocker

Automatic approval review rejected the command to register **0.1.59** and update
current-version compatibility expectations. Its exact reason was: “This
registers a new semantic revision (0.1.59) and mass-updates compatibility/version
expectations, but the user explicitly approved only 0.1.58, not this concrete
revision change.” The rejected command did not execute. No registry, lifecycle,
current-version tests or artifact-version declarations changed.

The [proposed contract](../60-specification/calling-conventions/checked-calls-and-artifact-identity.md)
remains draft. The experimental implementation and validation proceed, but
promotion requires the specific approval requested by the automatic reviewer.
There is no continuation and no completion PR yet.

## Review-ready state and validation

The final experimental regression run passed **858 tests**, including 18 new
calling tests. The last review added an explicit witness that an existing
Catena trap retains its identity across the synchronous Erlang callback.
Production compilation with warnings treated as errors passed. Archive
validation passed with 615 documents, 71 directories, 6,971 links, 185
specification chapters and the unchanged 793 registered obligations.
Both repositories pass `git diff --check`.

Reproduction commands are `mix test`, `MIX_ENV=prod mix compile
--warnings-as-errors`, `MIX_ENV=prod mix escript.build`, and, in the research
repository, `python3 validate_archive.py`. The full experimental test output is
at `/tmp/catena-calling-validated.log` on the development host; the specification
and committed future journal must retain the result, rather than depend on
that transient path for authority.

The review-only patch `/tmp/calling-conventions-0.1.59.patch` is generated by
`/tmp/prepare-calling-promotion.py`. That generator reads repository files and
writes only the temporary patch; it never applies it. `git apply --check` passes.
The patch contains the five implementation/registry files, current-discovery
expectation updates, and a new exact-selection promotion test (51 files total).
It has not been applied or tested as a promoted revision.

Approval would authorize the following concrete change: register C094 as
`0.1.59`; advertise it as the current semantic selection; require that exact
selection for new calling sidecars; emit the new calling artifact identity;
and publish the reviewed draft after its promotion checks pass. Retained core,
textual input, serialized interface, signed format and C089 lifecycle artifact
versions remain explicitly distinguished. New calling artifacts and callbacks
must be rebuilt/recreated when their exact compiler identity changes.

After approval, apply and format the patch, run its selection tests and the full
suite, promote the draft and add the final conformance/checklist/version entries,
then commit, PR and merge each repository. Synchronize compiler `rewrite` and
research `main` before deleting `codex/calling-conventions`, then move to G095.
Until those steps finish, P094 remains partial and the work is uncommitted.

## Approved promotion to 0.1.59

The user explicitly approved **0.1.59** and **all other revision updates for
this implementation session**. This resolves the revision-registration blocker
above; those earlier paragraphs describe the historical preparation state.
The reviewed patch was applied. Six stale discovery/registry expectations were
updated after the first promoted run; retained historical format assertions
were preserved. The full promoted suite passed **859 tests**. Production
compilation with warnings treated as errors and the production escript build
passed. The 19 calling-specific tests also passed after final documentation
and obligation-tag updates.

The proposed `CC` obligation prefix collided with the existing clause-condition
registry; the attempted `CALL` prefix also exceeded the validator’s two-letter
area convention. This area now uses the unique **CV-OBL-001–CV-OBL-012** prefix.
Archive validation passes with 615 documents, 71 directories, 185 specification
chapters and 805 obligations (710 traced, 74 partial, 21 untraced). The contract,
area index, authority, next-version convention, completion map, exhaustive
inventory, conformance map and checklist are synchronized. The checklist now
has 98 complete, 27 partial, 14 gaps and 2 deferred items; the next unused
semantic patch is 0.1.60.

C094's call-shape gate covers direct, curried, closed effectful, retained process,
managed lifecycle and checked synchronous callback classes with the stated
admission/refusal witnesses. General foreign declarations and asynchronous
callback transport remain P096, recursive foreign data G095 and full stack
tooling P100. This completion does not claim those later gaps are remediated.

The verified compiler change is
[`8fada02cc4c8b4f25a8fc93a945919e1ee529e1f`](https://github.com/pcharbon70/catena/commit/8fada02cc4c8b4f25a8fc93a945919e1ee529e1f).
The coordinated research change publishes the normative contract and twelve
traceability obligations against that immutable implementation evidence.
