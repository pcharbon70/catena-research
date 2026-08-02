---
title: "Condition Predicates and Interfaces"
kind: specification
created: "2026-08-02"
status: normative
spec_version: "0.3"
tags:
  - compilers
  - pattern-matching
  - specification
  - type-inference
aliases:
  - "Catena verified condition predicates"
---

# Condition Predicates and Interfaces

## Declaration contract

The version 0.3 declaration shape is:

```catena
condition positive(value: Int) -> Bool = value > 0
```

A condition predicate MUST:

- have an explicit, monomorphic, first-order signature;
- accept only `Bool` and `Int` parameters in 0.3;
- return exactly `Bool` with an empty effect;
- have a body checked wholly by the
  [condition-safe judgment](syntax-and-safety.md);
- be called directly and fully applied; and
- belong to an acyclic dependency graph.

Declarations in one module may refer forward to other condition declarations.
The compiler checks the complete dependency graph before accepting any member.
Self recursion and mutual recursion are invalid. Ordinary program recursion is
unchanged; it simply cannot be reached from condition core.

## Canonical identity and core

A condition exported from module `M` under name `p` has the canonical identity
`M.p` within the 0.3 bootstrap contract. Package identity and dependency
resolution remain governed by the broader unresolved module system; a later
format may strengthen this identity without weakening evidence checks.

The compiler normalizes each accepted body into a core containing only:

- Boolean and integer literals;
- named parameter references;
- the exact unary and binary operations defined by 0.3; and
- calls naming canonical condition identities with normalized arguments.

Source paths, inferred types already enforced by checking, formatting, and
backend-specific Erlang operators are absent from canonical condition core.
The normalization is deterministic.

## Dependency and expansion evidence

Each exported condition carries:

- evidence format version `0.3`;
- canonical condition identity;
- ordered parameter names;
- a canonical portable body after transitive predicate inlining;
- sorted direct dependency identities;
- an `expanded_core` copy that MUST equal that canonical body in interface
  version 0.3;
- a native-lowerability marker; and
- a SHA-256 digest over the canonical evidence payload.

The transitive body lets a consumer recheck and inline the predicate without
executing dependency compiler code. The dependency list retains provenance and
makes changes auditable even though dependency calls have been removed from
the exported body. A consumer MUST recompute the evidence digest, check the
body against the exported type scheme, require `core` and `expanded_core` to
agree, and reject malformed, missing, nonportable, or inconsistent evidence.

Evidence is semantic metadata, not a license to trust arbitrary producer
claims. The consumer rechecks the closed representation and its native
operation set before it affects acceptance or receive lowering.

## Module interfaces

Version 0.3 `.cati.json` interfaces extend value entries with an optional
`condition` object. Non-condition values retain only their ordinary type
scheme. Interface serialization is canonical and the whole interface remains
protected by its own SHA-256 digest.

Version 0.2 interfaces remain readable. They cannot supply condition evidence,
so a value exported only by a 0.2 interface cannot be imported as a condition.
The runtime ADT layout remains absent from both interface versions.

## Explicit imports

Unqualified predicate use requires an explicit import:

```text
import condition Rules.positive as positive
```

The import names one exported condition and one local alias. Wildcard condition
imports, implicit discovery, type-directed selection, and import-order
selection are outside 0.3. Duplicate aliases are invalid.

An ordinary value import does not become condition-safe merely because its
scheme ends in `Bool`. Conversely, an imported condition retains an ordinary
function scheme for type checking, while its evidence separately authorizes
condition use and inlining.

## Budget

Direct normalization and transitive inlining MUST terminate under a declared
deterministic node budget. A conforming implementation MUST support at least
20,000 condition-core nodes. Exceeding the supported bound reports `CND007` as
an implementation limit; it never silently drops verification or accepts an
opaque call.

## Connections

The interface extends the layout-free module contract in
[Interfaces and Representation](../data-and-patterns/interfaces-and-representation.md).
Backend consumption is specified in [BEAM Lowering](beam-lowering.md).
