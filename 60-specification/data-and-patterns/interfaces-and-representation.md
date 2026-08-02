---
title: "Interfaces and Representation"
kind: specification
created: "2026-08-02"
status: normative
spec_version: "0.2"
tags:
  - algebraic-data-types
  - beam-vm
  - representation-independence
  - specification
aliases:
  - "Catena ADT interfaces and BEAM layouts"
---

# Interfaces and Representation

## Deterministic module interface

Successful 0.2 compilation MUST produce a deterministic `.cati.json` module
interface beside the `.beam`. Checking without compilation MAY consume
interfaces but MUST NOT write artifacts.

An interface contains:

- format and language-slice versions;
- canonical origin and module name;
- nominal type identities, kinds, and analyzed parameter variance;
- public value schemes;
- transparent constructor identities, schemes, ordinal and field metadata;
- abstract type identities without constructors; and
- a lowercase SHA-256 digest of the canonical interface payload.

Object keys are recursively sorted for canonical encoding. Consumers MUST
verify the digest before trusting an interface and MUST reject tampering with
`A005`. Cryptographic signatures and governance attestations are separate from
this integrity checksum.

An interface MUST NOT expose a datatype's chosen runtime layout. In
particular, it contains no BEAM tag atom, tuple shape, boxing decision, niche,
or coercion instruction.

## Separate compilation

The compiler API accepts already decoded interface objects. The bootstrap CLI
accepts repeatable `--interface FILE.cati.json` arguments and verifies each
before compilation.

A transparent imported type supplies its constructor family for construction,
pattern typing, and closed coverage. An abstract imported type supplies only a
nominal kinded identity. Clients can pass abstract values and use wildcard or
binder patterns, but cannot name hidden constructors.

An origin/module/type disagreement is nominal incompatibility even if two
interfaces describe the same constructor shape. Layout equality never repairs
an identity mismatch.

## Source-semantic value

The semantic value of a constructor is:

```text
NominalValue(constructor identity, payload values in declaration order)
```

Neither the source language nor the reference evaluator exposes a physical
tag. Pattern selection compares semantic constructor identity.

## Required BEAM layouts

A conforming bootstrap compiler supports these two layouts:

```text
uniform = {:catena_adt, type_id_atom, constructor_index, payload_tuple}

compact nullary = qualified_constructor_atom
compact payload = {qualified_constructor_atom, field_1, ..., field_n}
```

The qualified compact atom includes canonical nominal type identity and
constructor name. `constructor_index` and payload order follow declaration
order.

Compact is the default production layout. Uniform is the reference layout.
Every 0.2 conformance program MUST check and execute under both layouts. The
two raw Erlang terms need not compare equal; observation through typed Catena
construction and matching MUST agree.

## Typed layout boundary

Layout selection occurs only after typed-core verification. A typed layout
mapping connects semantic constructor IDs to physical forms. The backend MUST
not reconstruct nominal meaning from spelling or tuple arity.

The verifier MUST reject inconsistent arity, type identity, constructor
ordinal, payload type, branch dispatch, or layout coercion. Such rejection is
`L001` and denotes an implementation failure rather than a source type error.

Only OTP 29's `compile:noenv_forms/2` may generate `.beam` content in the
bootstrap path. Core Erlang text, BEAM assembly, and direct binary construction
are not alternate production paths.

## Dynamic and evolution boundary

An untrusted Erlang term MUST NOT become a typed Catena ADT solely because it
has a matching tuple or atom shape. The later G095 boundary must define
validation and failure.

Version 0.2 promises source representation independence, not stable ABI or
wire compatibility. A stable external schema requires an explicit future
contract. Closed transparent datatypes also provide no `non_exhaustive`
evolution marker; an evolving API should export an abstract type and observer
functions.

The representation rationale follows
[Leroy 1992](../../30-sources/leroy-1992-unboxed-objects.md) and the
[ADT synthesis](../../20-notes/algebraic-data-types.md).
