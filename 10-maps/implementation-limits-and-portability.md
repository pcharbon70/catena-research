---
title: "Implementation Limits and Portability"
kind: map
created: "2026-08-17"
tags:
  - conformance
  - governance
  - specification
aliases:
  - "C012 implementation-limits map"
---

# Implementation Limits and Portability

## Scope

This map connects Catena's portable minimum contract, target-runtime evidence,
existing normative budget owners, machine-readable implementation disclosure,
runtime capacity, and C012 executable evidence. C012 is repository governance
across the normative corpus, not language revision `0.1.9`.

## Start here

- [Catena Implementation Limits and Portability](../20-notes/catena-implementation-limits-and-portability.md)
  develops the model, derives the floors, separates refusal from inconclusive
  evidence, and records rejected alternatives.
- [How Should Catena Bound Implementation Limits?](../40-inquiries/how-should-catena-bound-implementation-limits.md)
  records the operational question and bounded resolution.
- [Catena Implementation Limits and Portability policy](../IMPLEMENTATION-LIMITS.md)
  is the repository governance contract and owns `IL-OBL-001` through
  `IL-OBL-012`.
- [C012 Implementation Limits](../50-journal/2026-08-17-c012-implementation-limits.md)
  records the coordinated compiler commit, profile command, boundary tests,
  and archive validation.

## Trails

### Portable floors and the BEAM target

[Erlang/OTP 29 System Limits](../30-sources/erlang-otp-29-system-limits.md)
provides the arity-255 target ceiling. The synthesis follows the actual
effect-directed lowering to derive a 253-explicit-argument Catena floor rather
than copying that ceiling. The generated-module floor is enforced at the sole
OTP binary-generation boundary documented by
[Erlang/OTP 29 Compiler Recommendations for Language Implementors](../30-sources/erlang-otp-29-compiler-recommendations-language-implementors.md).

### Existing compiler refusals

The [data-and-patterns](../60-specification/data-and-patterns/README.md),
[clause-condition](../60-specification/clause-conditions/README.md),
[trait](../60-specification/traits-and-categorical-operations/README.md), and
[specification-and-governance](../60-specification/specifications-and-governance/README.md)
registers preserve their local 20,000-step rules and diagnostic ownership.
C012 supplies their common portable-floor, disclosure, and structured-detail
contract.

### Evidence bounds

Condition fact analysis, kernel reference execution, and schedule exploration
remain evidence activities. The
[formal semantic kernel](../60-specification/formal-semantic-kernel/README.md)
owns their semantic meaning; C012 ensures that `unknown`, `budget_exhausted`,
and `exhausted` cannot be promoted into source rejection or proof.

### Runtime capacity and mailboxes

[Erlang/OTP 29 Runtime Resource Controls](../30-sources/erlang-otp-29-runtime-resource-controls.md)
connects message storage to process heaps, garbage collection, emulator
configuration, and distribution pressure. The existing
[OTP process-semantics note](../30-sources/erlang-otp-29-processes.md) preserves
the ordering and selective-receive observations. C012 classifies capacity as
deployment-defined and carries quotas, failure, supervision, and backpressure
to G068 and G129.

### Disclosure and traceability

[Catena Conformance Vocabulary](../CONFORMANCE-VOCABULARY.md) defines the
implementation-limit behavior class. The
[Conformance Traceability map](conformance-traceability.md) registers the
twelve C012 obligations and their compiler evidence. The sibling compiler's
human-readable profile and `catena conformance-info` consume one executable
registry.

## Open questions

The bounded C012 inquiry is resolved, and C017 now activates the decoded
literal payload floor as `LIM004`; see the [literal map](literal-grammar.md).
G068 and G129 must
define concrete capacity and failure protocols. G126–G131 remain responsible
for threat models, the trusted computing base, unsafe boundaries,
reproducibility, denial of service, and supply-chain operations. Aggregate
source size, cancellation, memory accounting, and large-project performance
also remain outside the C012 floor set.
