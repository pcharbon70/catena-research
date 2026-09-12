---
title: "2026-09-12 Editor Protocol"
kind: journal
created: "2026-09-12"
tags: [specification, tooling, diagnostics]
aliases: []
---

# 2026-09-12 Editor Protocol

## Scope

Execute G123's grammar-independent portion at `0.1.96` while retaining the P109
public-source and transport hold. CP-123-1..3 select shared compiler services
with immutable snapshots, versioned cancellable results with stable diagnostic
identities, and identity-based transactional rename. This slice makes those
choices executable against retained JSON without defining public language
vocabulary.

## Implementation decisions

| Decision | Four alternatives | Recommended and selected |
| --- | --- | --- |
| LS-I01 Input | A public source; B checked or malformed retained JSON; C arbitrary BEAM terms; D editor-specific AST | B: retained JSON exercises shared checking and partial diagnostics without choosing P109 grammar. |
| LS-I02 Analysis | A separate editor checker; B reuse `Catena.check_json`; C regex inference; D host-language introspection | B: one compiler authority prevents editor/compiler disagreement. |
| LS-I03 Snapshot identity | A URI only; B URI, monotonic version, and SHA-256; C timestamp; D process reference | B: exact freshness survives repeated names and concurrent observations. |
| LS-I04 Changes | A mutate in place; B create immutable newer snapshots; C accept equal versions; D reconstruct history implicitly | B: version transitions and preimages remain explicit. |
| LS-I05 Partial input | A refuse all malformed bytes; B retain compiler diagnostics but withhold semantic queries; C silently repair; D invent placeholder declarations | B: useful uncertainty remains compiler-authored and visible. |
| LS-I06 Requests | A positional calls; B identity, method, parameters, and exact snapshot envelope; C global mailbox; D ambient current document | B: results are attributable to one request and preimage. |
| LS-I07 Cancellation | A kill shared analysis; B record bounded request identities before dispatch; C ignore cancellation; D cancel an entire URI | B: cancellation is deterministic without mutating compiler work. |
| LS-I08 Diagnostic identity | A message text; B canonical digest of diagnostic and snapshot fields; C list index; D random UUID | B: repeated results are stable and cannot cross snapshot identity. |
| LS-I09 Symbol identity | A source spelling alone; B digest module, kind, and name; C retained path only; D allocation order | B: semantic operations select a declared entity rather than a text match. |
| LS-I10 Completion | A all names; B exported symbols only; C keywords; D compiler internals | B: existing visibility is respected while P107 vocabulary remains held. |
| LS-I11 Completion filter | A fuzzy host-dependent ranking; B deterministic Unicode prefix; C regex; D no filter | B: a small portable rule needs no vocabulary or ranking policy. |
| LS-I12 Hover | A source excerpt; B checked type, uses, kind, identity, and visibility; C documentation scrape; D runtime value | B: the compiler's semantic facts are authoritative and bounded. |
| LS-I13 Navigation | A line/column guess; B retained-JSON path plus URI and symbol identity; C filename search; D no navigation | B: exact available coordinates are reported without fabricating public coordinates. |
| LS-I14 Semantic tokens | A lexical color names; B symbol kind and visibility at retained paths; C host parser tokens; D public token legend | B: current semantic classification is useful while P109 owns source positions and legends. |
| LS-I15 Rename selection | A text under cursor; B canonical symbol identity; C every matching string; D export index | B: C066-style identity prevents unrelated-name edits. |
| LS-I16 New-name validation | A any string; B existing Catena identifier rules; C host regex; D ASCII only | B: rename cannot create an identifier the compiler rejects. |
| LS-I17 Rename collisions | A overwrite; B reject any other top-level canonical name; C suffix automatically; D warn only | B: a preview cannot silently alter binding identity. |
| LS-I18 Occurrences | A global text replacement; B reject names with unresolved expression occurrences; C change declaration only regardless of uses; D infer by spelling | B: conservative refusal is honest until P109 supplies resolved source occurrences. |
| LS-I19 Preview | A mutate immediately; B exact nonmutating plan with edits and result bytes; C prose suggestion; D editor callback | B: reviewable preimage-bound plans align with P125's transaction model. |
| LS-I20 Plan verification | A trust plan digest; B recompute the complete expected plan and exact-compare; C trust result digest; D accept editor-provided edits | B: a self-consistent forged result cannot obtain edit authority. |
| LS-I21 Formatting | A define public layout now; B return an explicit P109 hold; C reserialize JSON as public source; D call a host formatter | B: G118 infrastructure does not authorize missing public productions. |
| LS-I22 Limits and trust | A unbounded unclassified helper; B fixed published bounds in `tools-profile`; C editor-defined limits; D silently truncate | B: exhaustion and trusted placement are inspectable conformance facts. |

Every recommendation was selected under the user's delegated decision
authority. No recommendation was overridden.

## Executed evidence

Compiler [PR 192](https://github.com/pcharbon70/catena/pull/192) merged feature
commit `3230fde` as merge commit `ffc251b` into `rewrite`. Seven direct service
cases cover immutable snapshots, shared semantic results, exported completion,
partial retained input, stable diagnostics, monotonic changes, stale requests,
bounded request cancellation, exact rename application, stale and forged plan
refusal, collision and unresolved-occurrence refusal, and explicit P109 holds.

The complete 1,181-test suite, production compilation with warnings as errors,
escript construction, reviewed trust-inventory verification, and
`git diff --check` pass. The approved trust update classifies
`lib/catena/tool/language_service.ex` in `tools-profile` and binds its final
source digest.

The [normative contract](../60-specification/editor-protocol/immutable-retained-input-language-service.md)
makes the implemented boundary durable. G123 stays partial because public
incremental parsing and recovery, source coordinates, public edit application,
formatting rules, and transport require P109.
