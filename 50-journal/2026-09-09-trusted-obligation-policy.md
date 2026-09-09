---
title: "2026-09-09 Trusted Obligation Policy"
kind: journal
created: "2026-09-09"
tags: [specification, conformance, security]
aliases: []
---

# 2026-09-09 Trusted Obligation Policy

## Scope

Execute [P127](../20-notes/language-completion-plan-delivery.md#item-127-unsafe-code-policy)
following C126's compiler merge 02d626e26039521596e979a253ab37c98a2498b7.
Revision 0.1.71 is covered by the user's session-wide revision approval.
The admitted-boundary policy is complete. Public vocabulary and intralanguage unsafe forms
remain excluded. Registry acquisition remains P130 and callback composition P096;
this policy covers the already admitted exact foreign/native artifacts.

## Implementation decisions

CP-127-1..3 retain their recommendations. The following four-way forks record
implementation decisions; each selected option is the agent's recommendation.

| Decision | Four alternatives considered | Recommended and selected |
| --- | --- | --- |
| TP-I01 | A source unsafe block / B retained exclusions + boundary policy / C blanket safe package / D ban interop | B. |
| TP-I02 | A mutate legacy signed formats / B separate exact 0.1.71 sidecars / C comments / D unversioned flags | B. |
| TP-I03 | A caller declares obligations / B derive from verified pure/foreign/native artifacts / C trust signatures as truth / D infer arbitrary host behavior | B. |
| TP-I04 | A flat direct imports / B bounded exact dependency DAG + provenance union / C first-path wins / D drop unused dependencies | B. |
| TP-I05 | A package name identity / B name/version plus exact implementation and dependency digests / C publisher alone / D local path | B. |
| TP-I06 | A global unsafe flag / B owner-bound scoped policy with exact boundary grants and obligation acknowledgements / C auto-admit deps / D env-variable authority | B. |
| TP-I07 | A pretend revocation rolls back / B deny future dispatch and retain existing adapter cleanup / C kill arbitrary NIF / D ignore revoke | B. |
| TP-I08 | A mutable exposed scope fields / B monitored GenServer ledger with opaque exact scope and child attenuation / C process dictionary / D global singleton | B. |
| TP-I09 | A silent graph cycles / B refuse cycles/missing/unreachable nodes, duplicate edges and capacity excess / C collapse cycles / D infinite recursion | B. |
| TP-I10 | A tests remove obligations / B checks vs trusted assertions and host closure disclosure explicitly separate / C no evidence / D signature claims safety | B. |
| TP-I11 | A all historical paths implicitly upgraded / B explicit scoped admission APIs with retained historical contracts and exact sidecars / C break old programs / D silently synthesize grants | B. |
| TP-I12 | A closure callback can execute arbitrary code as pure / B pure entry only through rebuilt verified artifact; foreign/native through owner APIs / C accept function payload / D trust nominal tags | B. |

## Refined implementation decisions

| Decision | Four alternatives considered | Recommended and selected |
| --- | --- | --- |
| TP-I13 Owner-qualified identity | A boundary bytes alone; B boundary plus owning package/version/exact implementation; C publisher alone; D package name only | B: replacement or reassignment requires a new explicit grant, while diamond paths to the same owner deduplicate. |
| TP-I14 Native identity | A description digest alone; B full signed package including publisher and payload; C file path; D platform name | B: changing an admitted signer or bytes changes the boundary identity. |
| TP-I15 Admission timing | A return a perpetual universal safe flag; B linearize each admission at the policy ledger then recheck with the owning adapter; C lock the VM during calls; D kill already dispatched native work | B: revocation denies subsequent admissions and does not claim rollback or preemption of admitted work. |
| TP-I16 Closed graph limits | A unlimited recursion and metadata; B 64 nodes, 256 edges/boundaries, 64 MiB serialized inputs and 1 MiB sidecars; C truncate provenance; D silently ignore distant dependencies | B: refuse oversize/invalid graphs without losing transitive obligations. |

## Acceptance route

Build exact pure/foreign/native inputs and a bounded dependency graph. Bind the
sidecar to verified artifacts; exercise diamond closure, rehashed omissions,
replacement identities, scoped attenuation, revocation and actual compiled/native
execution. Host closure declarations remain trusted responsibilities: a syntax or
signature check cannot discover every hidden operation in arbitrary host code.
Record limits and tests before promoting the checklist.

## Evidence

The eleven policy cases passed, including actual compiled pure and foreign
applications, a signed native Float service, and a compiled Int application whose
trusted BEAM adapter converts its bounded test input to Float, calls that service
and returns the resulting Int. The transitive application is denied before entry
when its native dependency grant is missing. This uses the retained Int capability
profile; it does not claim direct Float source support in that older profile.

Other cases cover diamond closure, altered binaries/core, rehashed sidecar
omissions, package owner/version replacement, native package replacement,
acknowledgement bounds, cyclic/missing/duplicate/unreachable nodes, scope capacity,
forged/cross-owner scopes, ancestor revocation, child-local revocation, escaped
handles and owner death. Existing C067 exclusion tests remain active.

The full compiler suite passed 998 tests. Production compilation with warnings
as errors, escript build, trust inventory audit and diff checks passed. The
reviewed inventory change admits two sources under identity/governance and five
single-call integration hooks, and adds the policy dependency/checks/residuals to
the foreign/native guarantee. Existing data hashes are unchanged. The profile has
186 sources, 17,408 recorded calls and 23 data inputs, with digest
`530972c673ca52794473e38dc8ea36b66333c8e2fddfe236392f9412d24781fc`.

Archive validation passed with 657 documents, 83 directories, 126 source notes,
197 specification chapters and 933 obligations (838 traced, 74 partial,
21 untraced). Checklist totals are 109 complete, 19 partial, 11 gaps and two deferred. Compiler [PR 153](https://github.com/pcharbon70/catena/pull/153) merged feature
`fd0b89cc939bc31fee46a2a70150d5752ac4a344` as
`5c85d0b21a322c98f09145431bc7d24514e3719c`. The rewrite branch was synchronized
with origin before the local and remote feature branch were deleted.
