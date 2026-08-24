---
title: "Checking, Initialization, and Caching"
kind: specification
created: "2026-08-24"
status: normative
spec_version: "0.1.20"
tags:
  - modules
  - separate-compilation
  - specification
aliases:
  - "Catena SCC consequences"
---

# Checking, Initialization, and Caching

## Status and authority

This chapter is the normative Catena 0.1.20 consequence contract for
dependency cycles. It is governed by
[Specification Authority](../../SPECIFICATION-AUTHORITY.md),
[Catena Conformance Vocabulary](../../CONFORMANCE-VOCABULARY.md), and
[Catena Implementation Limits and Portability](../../IMPLEMENTATION-LIMITS.md).
It applies [SCC Admission and Resolution](scc-admission-and-resolution.md)
and confirms, without amending, the machinery of
[C001](../type-system/type-system-overview.md),
[C002](../data-and-patterns/declarations-and-nominal-identity.md),
[C008](../editions-and-feature-lifecycle/README.md), and
[C010](../formal-semantic-kernel/canonical-kernel-syntax.md).

The rules apply only to source-language revision `0.1.20`.

## Initialization

A module contributes declarations and definitions only; Catena has no
top-level evaluation, per the unchanged C010 module semantics. Loading a
component loads its members; because no member executes anything at load
time, no intra-component initialization order exists (`CY-OBL-008`). The
order in which independent components load is unobservable to programs
and follows the deployment's resolution order.

## Inference and checking

Checking a component checks each member independently: against its
companions' declared export signatures for intra-component references,
and against digest-bound interfaces for cross-component imports
(`CY-OBL-008`). There is no joint inference across members: C001's
per-module inference, C002's recursive groups and constructor typing,
and C022's admission validation apply per member exactly as shipped. The
declared signatures are what make independent checking sound in a cycle:
each member's interface to its companions is fixed by declaration, not
by the other's computed result.

## Separate compilation and caching

The component is the atomic unit of separate compilation and caching
(`CY-OBL-009`). Caches are digest-addressed component units under C008:
rebuilding any member of a component rebuilds and re-digests the whole
component, producing a new joint digest; an acyclic rebuild is the
degenerate single-member case and behaves exactly as C008 fixed. A
consumer checked against a member interface of a previous component
build is incompatible with the re-digested component under the unchanged
C008 substitution rules.

## Why signatures, not digests, break the circle

A C022 import binds the consumer's check to the producer's computed
digest. In a cycle, each member's digest depends on an interface that
references the other's not-yet-computed digest-bearing interface, so no
per-member digest can exist before checking completes. Resolving
intra-component references against declared signatures removes the
circle: each member's interface is fixed before either is computed, and
digestes return only at the component boundary as the joint digest.
Pre-declared interface files would also break the circle but require a
new standalone format and digest domain that no slice owns; that
alternative is declined here.

## Deliberately separate work

Lockfiles and package-level rebuild policy remain G025/G121. Joint-digest
ABI evolution is subsequently fixed by C028's declared absence. Build-tool cache formats remain G121.

## Rationale and evidence (non-normative)

The [cycles synthesis](../../20-notes/catena-dependency-cycles.md)
records the Haskell section 5.7 evidence — exported values need explicit
signatures and the compilation unit grows to the recursive group — and
why definition-only modules make initialization the smallest clause.
