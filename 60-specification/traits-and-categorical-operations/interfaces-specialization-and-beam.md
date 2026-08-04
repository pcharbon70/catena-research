---
title: "Interfaces, Specialization, and BEAM"
kind: specification
created: "2026-08-02"
status: normative
spec_version: "0.1.4"
tags:
  - beam-vm
  - compilers
  - specification
  - trait-constraints
aliases:
  - "Catena 0.1.4 trait erasure"
---

# Interfaces, Specialization, and BEAM

## Interface version 0.1.4

A module interface is canonical JSON bound by a SHA-256 digest. Version 0.1.4
adds trait declarations, instances, law metadata, derivation provenance,
verified specialization templates, helper closure, and the standard hierarchy
digest to the 0.1.2 and 0.1.3 type, value, and condition evidence. Decoders MUST
continue to accept valid 0.1.2 and 0.1.3 interfaces without inventing trait data.

Any byte-level semantic change alters the digest. A tampered interface, an
incomplete helper closure, duplicate template identity, or a different
standard hierarchy digest is rejected before linking.

## Standard hierarchy binding

The toolchain ships one compiled canonical standard interface. Projects do not
declare it as a package dependency, and the compiler does not hard-code its
traits. Every 0.1.4 interface records its digest. This is content binding, not
cryptographic publisher signing; publisher identity remains outside 0.1.4.

## Explicit build manifest

Package specialization is driven by a toolchain-only manifest with:

> **Normative definition.**

```text
format              = catena-package-manifest
version             = 0.1.4
companion_module    = one BEAM module name
modules             = ordered source/BEAM/interface output records
interfaces          = explicit dependency interface paths
roots               = template, concrete types, required instances, export
output              = companion BEAM path
```

The manifest is not a package manager and performs no dependency discovery,
network access, version solving, or publication. Paths are resolved relative
to the manifest. Modules compile in manifest order against only the interfaces
already made available.

## Verified templates

An exported constrained operation includes a checked template and the complete
set of helper template identities needed to instantiate it. Templates admit
arguments, literals, tuples, direct calls, evidence-selected trait calls, and
calls within the verified helper closure. Unsupported nodes are rejected;
linking never executes arbitrary compiler-host code from an interface.

## Specialization

For every root, the linker kind checks concrete types, resolves one coherent
instance for each predicate, substitutes the selected minimal methods, and
recursively specializes helper templates. The deterministic specialization
key binds:

- canonical template content;
- concrete type terms;
- resolved evidence digests;
- compiler version;
- specification version; and
- standard hierarchy digest.

Specialization has a minimum 20,000-step budget. Type-growing polymorphic
recursion is rejected. Identical inputs MUST produce byte-identical companion
BEAM output and keys.

## Erasure

The output contains ordinary direct local or remote calls. Trait predicates,
parent evidence, dictionaries, law statuses, proof objects, template graphs,
and instance identity are compile-time-only and MUST NOT appear as runtime
arguments, process state, reflection data, or dispatch tables.

One deterministic companion BEAM module contains package specializations. The
linker and ordinary module compiler both lower through Erlang Abstract Format
and OTP 29 `compile:noenv_forms/2`; no direct Core Erlang or BEAM emission is
permitted by this bootstrap profile.

## Connections (non-normative)

The erasure rule aligns with the language-wide
[specification erasure principle](../../20-notes/language-integrated-specifications-and-governance.md):
compile-time guarantees may constrain admission without becoming production
runtime payload.
