---
title: "Kernel BEAM, Diagnostics, and Conformance"
kind: specification
created: "2026-08-06"
status: normative
spec_version: "0.1.8"
tags:
  - beam-vm
  - conformance
  - diagnostics
  - specification
aliases:
  - "Catena 0.1.8 conformance gate"
---

# Kernel BEAM, Diagnostics, and Conformance

## Fixed BEAM representation

The bootstrap 0.1.8 backend uses one physical representation:

> **Normative definition.**

```text
Int / Bool / Unit       = Erlang integer / true-or-false atom / :unit
tuple                   = Erlang tuple
regular constructor     = {:catena_constructor, ConstructorAtom, fields_tuple}
record                  = Erlang map keyed by validated field atoms
variant(label, payload) = {:catena_variant, label_atom, payload}
Process M handle        = local BEAM pid
trap(reason)            = :erlang.error({:catena_trap, reason})
```

Record field order is not observable. Interfaces contain row and process
types but no map, tuple, PID, or worker-layout facts. A source program cannot
inspect these forms through Erlang operations because 0.1.8 has no foreign
boundary.

Ordinary public values retain their established source-name and written-arity
exports. A public process entry `P` with arity `n` has a deterministic hidden
spawn export `__catena_spawn_P/n`; its worker entry is private. Imported spawn
sites use only digest-verified 0.1.8 process-interface evidence.

Backend generation remains Erlang Abstract Format followed by OTP 29
`compile:noenv_forms/2`. Process-only functions may use the direct calling
path. A function with ordinary algebraic effects retains effect-directed CPS.
Both paths preserve proper tail position and Process observations.

The declared nonempty module origin supplies the Abstract Format file
attribute and compiler source metadata. A local filesystem path is diagnostic
context only and MUST NOT alter interface identity or BEAM artifact bytes.

## Interface 0.1.8

The separate 0.1.8 interface contains three sorted sections. `types` records
each exported regular datatype's parameters, constructors, and positional
field types. `values` records each exported value's type, effect row, and
written function arity. `processes` records each exported process entry's
stable origin-qualified identity, source name, parameter types, closed mailbox
type, arity, and spawn symbol. Its canonical digest covers every field. Older
valid interfaces remain decodable and contain no inferred process entries.

A 0.1.8 import makes only the digest-verified public process entries
available to `spawn`. Imported values, constructors, and unqualified type
names are not brought into the kernel environment. The imported type section
is nevertheless checked so a process signature cannot smuggle a malformed or
unknown nominal type into its mailbox or parameters.

A missing, duplicate, malformed, wrong-origin, wrong-arity, wrong-mailbox, or
digest-substituted process entry is invalid. A failed decode or compile writes
no successful interface or BEAM output.

## Stable diagnostics

| ID | Meaning |
| --- | --- |
| `SYN001` | invalid encoding, byte, token, string, or delimiter |
| `SYN002` | unknown, malformed, misplaced, or wrong-arity kernel form |
| `SYN003` | published parser node or nesting implementation limit |
| `PRC001` | invalid process declaration, parameter, result, or mailbox signature |
| `PRC002` | non-sendable type at a process boundary |
| `PRC003` | invalid process operation context, target, message, or residual effect |
| `PRC004` | missing, forged, or incompatible process-entry interface evidence |

Unique-row failures retain `T005`; match and receive failures retain their
applicable `M...` and `CND...` identities. A compiler-produced core rejected
by the verifier remains `I001`. Runtime `trap` is not a compile diagnostic.

Every syntax or static diagnostic caused by a kernel source form has a primary
source span. A standalone malformed-interface result or forged-core internal
result has no source form and may be document-level. Related declarations and
constraints SHOULD carry secondary spans. Default messages lead with source
concepts such as record, variant, process, message, receive, or trap.

## Required executable evidence

The C010 corpus includes:

- successful exact-envelope cases plus rejected encoding, newline, metadata
  escape, delimiter, trailing-form, unknown-form, duplicate-export, node-limit,
  and depth-limit cases;
- record operations, open-row extension rejection, closed/open variant
  coverage, regular constructors, local generalization, forged evidence,
  fixed-layout, and strict-order cases;
- one source fixture combining value rows, a trait call, a handled ordinary
  effect, a process entry, spawn, send, and receive;
- sendability, process-context rejection, interface substitution, and
  forged-core attacks;
- self, per-sender order, permitted cross-sender outcomes, skipped-message
  preservation, dead-target send, return, trap, and quiescence;
- proper-tail-call stress cases;
- generated closed-term progress, result-type, and reference/BEAM agreement
  checks;
- bounded all-schedule reference exploration and focused reference/BEAM
  observations; and
- exact-selection, backward-interface, deterministic artifact, erasure, and
  sole-OTP-compiler-boundary checks.

The reference explorer stops after 20,000 transitions or 20,000 distinct
configurations. Exhaustion is an inconclusive evidence result and cannot
establish conformance or a semantic counterexample.

## Promotion record (non-normative)

All seven chapters were promoted together after archive validation, the
complete retained compiler suite, focused C010 and adversarial suites,
warning-free compilation, formatted sources, an escript build, inspected
artifacts, and repeated deterministic outputs passed against the explicitly
authorized immutable compiler commit.

The commit, parent, tree, toolchain, commands, counts, representative artifact
hashes, and post-commit results are recorded in the
[C010 conformance journal](../../50-journal/2026-08-06-c010-formal-semantic-kernel.md#immutable-compiler-identity).

## Evidence route (non-normative)

The design rationale and source trail are in
[Catena's Formal Semantic Kernel](../../20-notes/catena-formal-semantic-kernel.md).
The promotion run and immutable compiler identity are recorded in the linked
dated journal.
