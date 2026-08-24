---
title: "Cycle Diagnostics and Conformance"
kind: specification
created: "2026-08-24"
status: candidate
spec_version: "0.1.20"
tags:
  - conformance
  - diagnostics
  - modules
  - separate-compilation
  - specification
  - testing
aliases:
  - "Catena 0.1.20 cycles conformance"
---

# Cycle Diagnostics and Conformance

## Status and authority

This chapter is the normative Catena 0.1.20 cycle diagnostic, abstract
frontend, and conformance contract. It is governed by
[Specification Authority](../../SPECIFICATION-AUTHORITY.md),
[Catena Conformance Vocabulary](../../CONFORMANCE-VOCABULARY.md), and
[Catena Implementation Limits and Portability](../../IMPLEMENTATION-LIMITS.md).
It applies [SCC Admission and Resolution](scc-admission-and-resolution.md)
and [Checking, Initialization, and Caching](checking-initialization-and-caching.md).

## Stable diagnostics

| ID | Required meaning |
| --- | --- |
| `CYC001` | an SCC-internal violation: a digest-bound import presented for a component companion (regime mixing), or a component member exporting a name without the declared signature intra-component resolution requires (signature gap) |

No cycle shape is itself an error. Unknown modules, unexported import
names, and duplicate admissions remain `IMP003`/`IMP002`/`NSP001` under
C021/C022. An exact-selection mismatch remains `EDN001`.

`CYC001` fires at the event that closes the violation and is
transactional: no environment, interface, or artifact for the affected
action is published (`CY-OBL-005`). Its details carry the violating edge
(regime mixing: importing module, target module, presented digest) or
the violating member and missing signature (signature gap: module,
category, spelling). Diagnostic prose can improve only within the
bounded presentation rules of the repository conformance vocabulary.

## Abstract public boundaries

**SCC grouping** extends the C021/C022 environment builder: provide-module
events carry an optional `dependencies` name-list and optional declared
`signatures`; the builder accepts an optional current-module identity so
import edges attach to the consumer; the builder partitions the combined
graph into components, applies the two regimes, and rejects `CYC001`
violations at the closing event (`CY-OBL-003`). The optional fields are
backward-compatible: a stream without them builds exactly the C022
environment.

**Component compilation** is the concrete boundary: one operation
accepts all member programs of a component, builds each member's
provisional interface from its declared exports and definition
signatures, checks every member against its companions' provisional
interfaces and outside digest-bound interfaces, compiles the members,
cross-verifies each computed interface against its provisional one, and
returns the members' binaries, interfaces, and one joint digest — or
exactly one diagnostic (`CY-OBL-006`, `CY-OBL-010`).

The bootstrap evidence names these the SCC grouping of
`Catena.build_namespace_environment/2` (event grammar extended at
`0.1.20`) and `Catena.compile_scc/2` with the record
`Catena.Scc.Result`. These Elixir names are evidence API names, not
required names for every implementation.

## Determinism

Equal event streams and known-module sets produce equal component
partitions, resolutions, or diagnostics; equal component inputs produce
equal binaries, interfaces, and joint digests (`CY-OBL-010`). The joint
digest is a deterministic hash over sorted member names and member
interface digests; member order in the input affects nothing.

## Conformance obligations

| ID | Obligation | Required executable evidence |
| --- | --- | --- |
| `CY-OBL-001` | apply cycle behavior only at exact 0.1.20 and register the stable lifecycle addition | exact selection, registry, and lifecycle tests |
| `CY-OBL-002` | admit cycles: multi-module components group and resolve; no cycle shape is an error | SCC grouping and self-loop tests |
| `CY-OBL-003` | enforce the two regimes: signature resolution inside components, digest admission across, with backward-compatible optional fields | intra- and cross-component resolution tests |
| `CY-OBL-004` | keep acyclic behavior byte-identical to C022, including degenerate single-member components | acyclic regression and digest-equivalence tests |
| `CY-OBL-005` | reject regime mixing and signature gaps as `CYC001` at the closing event, transactionally | both `CYC001` reason tests |
| `CY-OBL-006` | compute deterministic joint component digests over sorted members and member interfaces | joint-digest and member-order-permutation tests |
| `CY-OBL-007` | record the dependency-inversion alternative as the sanctioned non-cyclic restructuring | inversion-shape compilation tests |
| `CY-OBL-008` | confirm definition-only initialization with per-component loading and per-member inference | component execution and per-member checking tests |
| `CY-OBL-009` | make the component the atomic cache unit: rebuilding any member re-digests the component | member-change re-digest tests |
| `CY-OBL-010` | compile genuine multi-module components end-to-end — checking against companions' signatures, executing, both layouts, deterministic joint digest — deterministically | two- and three-module SCC compilation and execution tests |

Every obligation has at least one tagged passing test. The sibling
compiler gates the complete `CY-OBL-*` set against unknown and uncovered
identifiers before C024 conformance is claimed.

## Required evidence sets

Positive evidence includes abstract grouping of pairs, self-loops, and
three-module rings; intra-component resolution through declared
signatures; cross-component digest admission from inside a component; a
real two-module mutually-referencing component compiling and executing
A→B→A under both layouts with a joint digest invariant to member order; a
three-module component; an inversion-shaped program compiling without a
component; and degenerate acyclic compilation digested identically to
C022.

Negative evidence includes digest-presented companion imports and
signature-gap exports rejected as `CYC001` at the closing event with no
partial output; a companion consumed as an outside digest interface
rejected; and outside modules rejected as `IMP003` when unknown.

Exclusion evidence demonstrates that streams without the optional fields
build the C022 environment unchanged, that no pre-declared interface file
is consumed, and that predecessor APIs retain their exact selections and
defaults.

## Revision and persistence separation

Revision `0.1.20` admits cyclic module graphs and adds `CYC001` and the
SCC grouping grammar; it adds no JSON AST version, kernel
S-expression version, artifact version, signature domain, typing rule,
runtime behavior, or BEAM representation beyond C002/C022's
(`CY-OBL-001`). Interfaces gain the joint digest as a new deterministic
field of the component result without changing member interface formats.

The source-text decoder accepts cumulative revisions `0.1.9` through
`0.1.20`; every predecessor API retains its exact selection, with the
namespace resolver's grammar advancing to accept both event shapes. The
next unused semantic patch is `0.1.21`.

## Rationale and evidence (non-normative)

The design route is preserved in the
[cycles synthesis](../../20-notes/catena-dependency-cycles.md), the
[open inquiry](../../40-inquiries/how-should-catena-handle-module-dependency-cycles.md),
and the [topic map](../../10-maps/module-dependency-cycles.md). The C024
evidence record will preserve the sibling-compiler commands and archive
validation.
