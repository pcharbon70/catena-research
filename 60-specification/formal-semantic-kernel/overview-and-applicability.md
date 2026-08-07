---
title: "Formal Semantic Kernel Overview and Applicability"
kind: specification
created: "2026-08-06"
status: normative
spec_version: "0.1.8"
tags:
  - catena
  - formal-semantics
  - specification
aliases:
  - "Catena 0.1.8 kernel boundary"
---

# Formal Semantic Kernel Overview and Applicability

## Status and authority

This chapter and its six siblings are the normative Catena 0.1.8 formal
semantic kernel. The explicitly authorized immutable compiler identity and
post-commit evidence that satisfied their promotion gate are recorded in the
[C010 conformance journal](../../50-journal/2026-08-06-c010-formal-semantic-kernel.md#immutable-compiler-identity).

Revision 0.1.8 adds a separate exact semantic-kernel input without removing or
reinterpreting any 0.1.1 through 0.1.7 input. Earlier exact revisions retain
their former JSON boundaries and behavior. The kernel grammar is a bounded
conformance language, not a new spelling for every construct admitted by those
older frontends. Earlier rules are premises only for the forms this area
explicitly enumerates; this area does not silently narrow an older revision.

## Integrated boundary

The 0.1.8 kernel includes:

- annotated unary functions, rank-1 schemes, value/effect-restricted local
  generalization, strict calls, and named general recursion;
- regular positional nominal data, structural patterns, inline portable
  conditions, and bounded head-coverage checking;
- unique structural record and variant rows plus multiplicity-preserving
  ordinary effect rows;
- single-parameter traits, closed non-overlapping instance heads, explicit
  selected evidence, and evidence erasure;
- named ordinary effects, statically selected deep handlers, effect-free
  handler clauses, and affine resumptions;
- a canonical versioned S-expression semantic module;
- local typed processes with spawn, self, send, and selective receive; and
- explicit process-local traps.

The relationship to the broader retained areas is exact:

| Retained area | Executable 0.1.8 kernel subset |
| --- | --- |
| C001 types | Rank-1 explicit signatures and typed lambdas; local schemes only under the stated value/effect restriction |
| C002 data and patterns | Regular positional data and top-level Boolean, closed-variant, or constructor coverage; no GADTs or named fields |
| C003 conditions | Inline portable `when` expressions; no named condition declarations or condition calls |
| C004 traits | One parameter and closed exact instance heads; no dependencies, hierarchy, laws, derivation, or open constraints |
| C005 effects | Named operations and named deep handlers with affine resume; no handler arguments, capability aliases, public handler imports, or outer clause effects |
| C006–C008 governance and lifecycle | Exact selection and artifact metadata only; governed claims and package manifests remain on their retained inputs |

Every accepted kernel module MUST elaborate into the unified typed core,
pass inference-independent verification, and have the small-step meaning
defined by this area. An executable implementation, test, or reference machine
does not supply a rule omitted here.

## Deliberate exclusions

The 0.1.8 kernel has no ergonomic layout-sensitive source frontend, comments,
documentation syntax, strings, floats, binaries, collection literals,
macros, arbitrary compile-time execution, application package syntax,
foreign values or calls, cleanup scopes, exception catching, timeouts,
cancellation, links, monitors, exit trapping, supervision, process priority,
distribution, or hot code upgrade.

Those exclusions are version boundaries, not permission to accept an
unstated form. A later revision must define its grammar, static obligations,
dynamics, failure, representation, compatibility, and conformance evidence.

## Host boundary

The only runtime-interpreted effect introduced by this slice is the reserved
`Process` effect. It is available inside a named process entry, may appear in
ordinary function effect rows, and cannot be declared or handled by a program.
Every ordinary algebraic effect at a process-entry boundary must already be
handled. An ordinary residual effect at a public value boundary remains
explicit in that value's interface; executing a request without a selected
handler reaches the specified unhandled-effect trap. The general
application-entry and host-effect policy remains separate from this bounded
rule.

## Connections (non-normative)

The design and evidence trail begin at the
[Formal Semantic Kernel map](../../10-maps/formal-semantic-kernel.md). The
older areas remain authoritative for details not replaced here.
