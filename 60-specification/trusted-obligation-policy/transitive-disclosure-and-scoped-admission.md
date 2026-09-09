---
title: "Transitive Disclosure and Scoped Admission"
kind: specification
created: "2026-09-09"
status: normative
spec_version: "0.1.71"
tags: [specification, conformance, security]
aliases: []
---

# Transitive Disclosure and Scoped Admission

## Status and authority

C127 defines exact revision `0.1.71` in edition `0.1`, without previews, under
[authority](../../SPECIFICATION-AUTHORITY.md),
[conformance vocabulary](../../CONFORMANCE-VOCABULARY.md) and
[implementation limits](../../IMPLEMENTATION-LIMITS.md). It executes the
[reviewed policy plan](../../20-notes/language-completion-plan-delivery.md#item-127-unsafe-code-policy).
The [C067 exclusions](../dynamic-and-unsafe-boundaries/the-intralanguage-exclusions.md)
remain in force: this policy introduces no source unsafe block, unchecked cast,
reflection primitive or public vocabulary (`TP-OBL-001`).

The supported delivery is a separate exact trust sidecar over verified pure
calling artifacts, closed foreign programs and admitted native packages. Retained
interface, assurance, source and native-package formats keep their original rules.
Consumers select this stronger policy explicitly; historical host APIs are not
retroactively relabeled policy-controlled. Public source integration remains P109,
general registry acquisition P130, and the unadmitted callback composition P096.
Unsupported implementation forms are refused rather than treated as obligation-free.

## Obligations and responsibility

Trusted obligations name assumptions about host behavior whose violation can
invalidate the associated guarantee. They are responsibilities of the exact
owning package and its host implementation. The [C126 trust graph](../trusted-computing-base/guarantees-assumptions-and-boundary-checks.md#guarantee-specific-graph)
continues to name shared compiler, runtime, OS and crypto dependencies.

Verified pure calling inputs contribute no foreign/native obligations. Every
contained definition satisfies the retained pure-entry condition, and the calling
artifact is reverified against its core. Foreign programs are rebuilt against
exact core, capability bindings, codecs and loaded host-module identity. They
contribute cooperative cancellation, host-code correctness, scheduler correctness
and host-closure disclosure obligations. Native packages are reverified against
signed bytes, explicit publisher policy, platform and unsafe acknowledgements;
they contribute the package kind's existing obligations plus host-closure
disclosure (`TP-OBL-002`).

Host-closure disclosure means the owning package accounts for external code and
services its implementation relies on. The graph checks the supplied dependency
closure; it cannot infer all dynamic calls inside arbitrary trusted host/native
code. A dishonest host implementation can violate this responsibility. Tests,
signatures, type annotations and obligation acknowledgements do not discharge it,
prove memory safety or prevent VM corruption (`TP-OBL-003`). Existing environmental
service authority remains governed by C106; no new environmental implementation
kind is implicitly admitted here.

## Exact dependency closure

The build input is a finite map from package name to exact semantic package
version, sorted unique dependency names and one supported checked implementation.
Package names are nonempty valid UTF-8. Versions parse as semantic versions.
Unrecognized input fields, missing dependencies, duplicate edges, cycles,
unreachable extra nodes and unsupported implementations are refused.

Each node records its owner name, version and deterministic implementation digest.
Its direct dependency map binds each dependency's full record digest. Its exposed
obligations are the union of local and transitive obligations, sorted by
owner-qualified boundary identity. A diamond reaching the same owner and exact
implementation contributes one record, preserving that owner's provenance.
The same host implementation owned by another package remains a distinct
responsibility (`TP-OBL-004`).

Foreign implementation-boundary identity binds the exact descriptor. Native
identity binds the full signed package, including publisher, signature and payload.
The admission identity additionally binds owner name, version and exact
implementation. Changing owner, version, code, signed package or underlying
admission inputs therefore requires the corresponding new grant; a package name
or previously approved publisher alone is insufficient (`TP-OBL-005`).

## Interface and artifact exposure

The canonical sidecar identifies format, revision, root, all node records and the
current reviewed trust-profile digest. Its digest covers the complete payload.
Interface construction derives this document from checked build inputs; no caller
supplies a trusted safe flag or an authoritative hand-written obligation list.

Manifest decoding checks the canonical envelope and digest for inspection only.
It does not establish transitive correctness or authority. Assurance verification
rebuilds the complete graph from exact checked inputs and compares the entire
sidecar. A rehashed omission, changed dependency, altered artifact or substituted
profile fails that binding even if the envelope decodes successfully
(`TP-OBL-006`). This sidecar is separate from retained signed governance manifests;
a digest is not a signature or permission to execute.

## Scoped admission

Trusted setup creates an owner-bound scope over one verified graph and a map of
exact owner-qualified boundary identities to sorted unique acknowledged obligations.
There is no global allow-unsafe switch, automatic grant from dependency presence,
or inference of authority from a decoded sidecar. Each admission of a named
package checks its entire exposed obligation closure; even an otherwise pure
root with a declared trusted dependency requires that dependency's grant
(`TP-OBL-007`).

A live manager stores exact opaque scope identity, owner, grants, ancestry and
revocations. Cross-owner use and forged scope identities fail. Attenuation creates
a child with a subset of its parent's identities and acknowledgements. A child
cannot enlarge authority. All scopes expire when the owning run ends or the
owner dies; escaped handles do not extend their lifetime (`TP-OBL-008`).

Revocation is monotone within the scope. It denies later admissions of the
boundary through that scope and its existing or future descendants. Revoking a
child does not revoke its parent or sibling. Admission linearizes at the manager's
successful check. A call already admitted can finish after revocation; revocation
is neither rollback nor arbitrary native preemption. Existing adapter cancellation,
timeout and mandatory cleanup retain their own meanings (`TP-OBL-009`).

## Execution

Scoped invocation selects only an implementation stored in the verified graph.
Pure execution rechecks its artifact through the retained calling adapter.
Foreign execution requires the program's named zero-argument entry, starts an
owned adapter with precisely the program's verified declarations, and invokes its
compiled capability entry. The wait bound is 5,000 milliseconds. Native execution
selects the retained one-Float service operation and starts an owned native scope
whose package is verified again. Source entry names and the native operation role
are retained internal contracts, not newly chosen language vocabulary
(`TP-OBL-010`).

Value/codec budgets, result representations, traps and resource release use their
owning C094–C098 contracts. Pure calling budgets have nodes/bytes; foreign budgets
also have depth. The native ABI retains its fixed Float validation. The policy
adds admission checks and transitive disclosure; it does not coerce host results
or erase unsafe obligations after a successful invocation.

## Limits and refusal

The exact profile admits at most 64 nodes, 256 dependency edges, 256 exposed
owner-qualified boundaries, 67,108,864 bytes in the serialized build input and
1,048,576 bytes in canonical sidecar metadata. The input-size check follows
serialization and is not a hostile-input allocation guarantee. Each package name
contains at most 128 UTF-8 bytes. The manager holds at most 64 scopes, including
the root. A grant map contains at most 256 identities; each acknowledgement list
contains at most 32 strings, each at most 128 UTF-8 bytes (`TP-OBL-011`).

Invalid graphs and declarations are refused at build/verification. Oversized
sidecars or malformed canonical envelopes fail decoding. Missing acknowledgements,
revoked identities and unknown packages fail admission. Invalid attenuation or
scope-capacity exhaustion creates no child and leaves prior grants unchanged.
The conformance document reports these exact limits and explicitly reports that
host safety has not been proved.

Graph construction rechecks and can recompile artifacts; its cost includes the
owning compiler/codec operations, serialized input size and transitive closure.
No constant-time build or universal host liveness promise follows. Runtime
admission scans the selected closure and ancestor revocations. Arbitrary host code
can bypass host-level APIs or compromise the VM; this is an explicit residual
trust boundary, not an intralanguage feature or an OS sandbox.

## Variability register

The supported implementation kinds, identity construction, closure, revocation
semantics and stated profile ceilings are fixed. Existing package/adapter
contracts own platform admission, execution limits and cleanup outcomes.
Future implementation kinds require explicit normative and checked integration;
unknown kinds never inherit pure status.

## Rationale and evidence (non-normative)

The [journal](../../50-journal/2026-09-09-trusted-obligation-policy.md) records four-way
decisions, concrete compiled and native execution, negative cases and inventory
review. The [foreign visibility routing](../dynamic-and-unsafe-boundaries/the-foreign-visibility-routing.md)
explains why trusted work is visible at typed boundaries while ordinary Catena
retains its exclusions.
