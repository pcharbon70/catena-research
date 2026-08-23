---
title: "Smart-Constructor Idiom and Conformance"
kind: specification
created: "2026-08-23"
status: normative
spec_version: "0.1.19"
tags:
  - abstraction
  - conformance
  - specification
  - testing
aliases:
  - "Catena 0.1.19 abstraction conformance"
---

# Smart-Constructor Idiom and Conformance

## Status and authority

This chapter is the normative Catena 0.1.19 invariant-idiom and
conformance contract. It is governed by
[Specification Authority](../../SPECIFICATION-AUTHORITY.md),
[Catena Conformance Vocabulary](../../CONFORMANCE-VOCABULARY.md), and
[Catena Implementation Limits and Portability](../../IMPLEMENTATION-LIMITS.md).
It applies [Authority and Representation Exclusions](authority-and-representation-exclusions.md)
over the unchanged contracts of C002 and C022.

## The sanctioned invariant idiom

The sanctioned way to give a nominal datatype an invariant in edition 0.1
is (`AB-OBL-004`):

1. export the type abstract, so its constructors are unavailable for
   construction and matching outside the defining module;
2. export one or more validating constructor functions whose failure is
   visible in their result type — the shape
   `parse : String -> Result EmailError Email` — so every invalid input
   is rejected by typing before any value exists; and
3. export observer functions through which clients read the value's
   contents.

A datatype with an exported transparent constructor surface enforces no
invariant by spelling: a plain wrapper around a public constructor is
advisory, not an invariant, and MUST NOT be presented as one
(`AB-OBL-004`).

> **Normative conformance example.**

```text
export type Email
export parse : String -> Result EmailError Email
export domain : Email -> String
```

A client obtains an `Email` only through `parse`; a failed validation
produces the typed `EmailError` alternative; `domain` is the read path;
and no client can construct or destructure an `Email` by spelling.

## Coverage consequence

A match over an abstract-typed scrutinee outside the defining module has
no constructor alternatives to draw on: clients satisfy C002 coverage
with a wildcard binder plus the exported observers
(`AB-OBL-005`). The defining module's private matches are ordinary
transparent matches under the unchanged C002 rules.

## No new machinery

The idiom introduces no construct, diagnostic, export mode, or interface
field. It is a required reading of C002 abstract export plus typed
failure returns; its normative content is that this reading is the
sanctioned one, and that the alternatives of
[Authority and Representation Exclusions](authority-and-representation-exclusions.md)
are not available substitutes.

## Conformance obligations

| ID | Obligation | Required executable evidence |
| --- | --- | --- |
| `AB-OBL-001` | apply abstraction-boundary behavior only at exact 0.1.19 and register the stable lifecycle addition | exact selection, registry, and lifecycle tests |
| `AB-OBL-002` | keep the transparent/abstract pair the complete authority vocabulary on every frontend | transparency-enum closure tests on export events and persisted interfaces |
| `AB-OBL-003` | admit no stable-layout form on any frontend; keep both-layout conformance mandatory | stable-layout spelling rejection tests and unchanged both-layout executions |
| `AB-OBL-004` | sanction the abstract-type-plus-validating-constructor-plus-observer idiom and reject public-constructor wrappers as invariants | idiom-program compilation with typed-failure validation and wrapper anti-pattern rejection |
| `AB-OBL-005` | enforce the wildcard-plus-observers coverage consequence for abstract scrutinees outside the defining module | abstract match coverage tests |
| `AB-OBL-006` | keep abstract constructors unconstructible and unmatchable through digest-bound interfaces | cross-module abstract round-trip tests |
| `AB-OBL-007` | preserve source-only and persisted-format separation and claim no later phase | registry, pinned-predecessor, forged-format, and absent-phase tests |

Every obligation has at least one tagged passing test. The sibling
compiler gates the complete `AB-OBL-*` set against unknown and uncovered
identifiers before C023 conformance is claimed.

## Required evidence sets

Positive evidence includes an idiom module — abstract type, validating
constructor returning a typed failure, observer — compiling and executing
through the ordinary compiler path; invalid inputs rejected by the typed
failure; observers reading constructed values; abstract matches covered
by wildcard; and both-layout execution of the idiom program.

Negative evidence includes stable-layout spellings rejected on the export
event grammar, the retained JSON AST, and interface decoding;
transparency values outside the pair rejected as `EXP001`; construction
or matching of an abstract constructor outside its module rejected;
private-constructor wrappers presented as invariants rejected in review
material; and non-`transparent`/`abstract` authority forms rejected as
invalid events.

Exclusion evidence demonstrates that this area adds no frontend surface:
no new acceptance, diagnostic, interface field, or artifact, and that
predecessor APIs retain their exact selections and defaults.

## Revision and persistence separation

Revision `0.1.19` adds no accepted input, typing rule, runtime behavior,
interface version, artifact version, or signature domain
(`AB-OBL-001`, `AB-OBL-007`). Its content is the two exclusions, the
completeness of the authority vocabulary, and the sanctioned idiom, with
executable evidence that the shipped compiler already enforces exactly
this boundary.

The source-text decoder accepts cumulative revisions `0.1.9` through
`0.1.19`; every predecessor API retains its exact selection. The next
unused semantic patch is `0.1.20`.

## Rationale and evidence (non-normative)

The [abstraction synthesis](../../20-notes/catena-abstraction-boundaries.md)
records the smart-constructor argument, the wrapper anti-pattern, and the
Leroy/SML grounding. The C023 evidence record will preserve the
sibling-compiler commands and archive validation.
