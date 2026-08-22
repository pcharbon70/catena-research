---
title: "Shadowing and Ambiguity"
kind: specification
created: "2026-08-22"
status: normative
spec_version: "0.1.17"
tags:
  - namespaces
  - specification
  - shadowing
aliases:
  - "Catena shadowing rules"
---

# Shadowing and Ambiguity

## Status and authority

This chapter is the normative Catena 0.1.17 scope, shadowing, and
ambiguity-resolution contract. It is governed by
[Specification Authority](../../SPECIFICATION-AUTHORITY.md),
[Catena Conformance Vocabulary](../../CONFORMANCE-VOCABULARY.md), and
[Catena Implementation Limits and Portability](../../IMPLEMENTATION-LIMITS.md).
It applies [Namespace Inventory and Spelling](namespace-inventory-and-spelling.md)
and preserves the kernel's lexical shadowing rule unchanged.

The rules apply only to source-language revision `0.1.17`.

## Scope model

Scopes nest deterministically (`NS-OBL-007`):

- the module scope contains all module-level declarations;
- each declaration introduces a declaration scope for its parameters,
  fields, operations, or clauses per its uniqueness domain;
- each quantifier introduces a type-variable scope;
- each value binder introduces an expression scope.

A declaration is visible from its introduction to the end of its scope,
including nested scopes, subject to shadowing below. No visibility rule
of this chapter depends on declaration order between sibling scopes.

## Shadowing

An inner scope's binding of a spelling in one category hides every outer
binding of that spelling in the same category for the inner scope's
region; resolution always takes the innermost visible binding
(`NS-OBL-007`). Shadowing is permitted in every program category and is
silent: 0.1.17 defines no shadowing warning or denial, leaving warning
quality to the diagnostic-contract owner (P117) as a non-semantic
addition.

Shadowing never crosses categories: an inner `values` binding does not
hide an outer `types` binding of the same spelling, and vice versa
(`NS-OBL-002` refers).

## Same-scope duplicates

Two bindings of one spelling in one category within one scope are static
invalidity reported as `NSP001`, including two module-level declarations,
two fields of one type, two operations of one effect, or two type
variables of one quantifier (`NS-OBL-004`).

## Type variables

A quantifier introduces a type-variable scope whose names shadow
`types`, `traits`, `effects`, `handlers`, `entries`, and `modules`
bindings of the same spelling for the quantified region (`NS-OBL-008`).
Type variables never resolve as values; value names never resolve as type
variables; and a type variable never shadows another type variable of the
same quantifier — that is the duplicate rule above. After the quantified
region ends, an outer binding of the shadowed spelling is visible again.

## Cross-origin precedence

For one unqualified spelling in one program category, resolution
precedence is fixed (`NS-OBL-009`):

1. a binding in the innermost enclosing scope wins;
2. otherwise a module-level local declaration wins over every import;
3. otherwise, when two or more import origins supply the same spelling in
   the same category and no local binding exists, the reference is
   ambiguous — static invalidity reported as `NSP004`, naming every
   colliding origin;
4. a future prelude origin follows import precedence under G026 and is
   never a silent default.

A reference with no binding and no import in scope is unbound — static
invalidity reported as `NSP003` (`NS-OBL-010`). Resolution is a pure
function of the scope structure, the declaration events, and the import
sets; it MUST NOT depend on the order in which independent origins were
imported, on inferred types (G066), or on implementation choice.

An import colliding with a module-level local declaration in the same
category is not itself an error: the local declaration wins, and the
collision becomes visible only through the precedence rule. Import-set
syntax and its diagnostics remain G022's.

## Determinism

Given equal scope-event streams and equal import sets, every resolution
and every rejection is equal across conforming implementations
(`NS-OBL-013` refers). Diagnostics identify the offending spelling, its
category, and — for ambiguity — every colliding origin.

## Deliberately separate work

Import/export syntax and unused-import diagnostics remain G022. Module
recursion and initialization order remain G024. Prelude contents remain
G026. Type-directed resolution remains G066. Binder and declaration
surface syntax remains P109.

## Rationale and evidence (non-normative)

The [namespaces synthesis](../../20-notes/catena-namespaces-and-shadowing.md)
records the Haskell innermost-wins precedent, the OCaml order-based
contrast that motivated order-independent precedence, and the kernel rule
this chapter preserves.
