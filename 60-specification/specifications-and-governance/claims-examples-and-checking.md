---
title: "Claims, Examples, and Bounded Checking"
kind: specification
created: "2026-08-03"
status: normative
spec_version: "0.6"
tags:
  - governance
  - specification
  - type-inference
aliases:
  - "Catena 0.6 claim semantics"
---

# Claims, Examples, and Bounded Checking

## Module declarations

The 0.6 semantic JSON AST MAY add `specifications` and MAY mark an ordinary
definition `verification_only: true`. A specification contains a stable local
name, one or more claims, and optional display text. A claim contains a stable
local name, a `kind`, and a typed `subject`.

Final source punctuation is outside 0.6. The JSON AST and the resulting typed
specification graph are normative; a future parser MUST elaborate to the same
graph.

## Subject resolution

A claim subject has a closed `kind` and `name`. Supported kinds are:

- exported value;
- datatype;
- trait;
- instance;
- effect family;
- handler;
- module;
- package output;
- module interface;
- governed action; and
- named assurance profile.

The compiler MUST resolve subjects against the typed module and package graph.
An unknown name, a private subject where export is required, a kind mismatch,
or an unrecognized future subject kind is `SPC001` and is invalid rather than
opaque.

## Stable identity and semantic digest

A claim identifier is:

> **Normative definition.**

```text
claim:sha256:<lowercase-hex SHA-256(
  "catena:claim-id:0.6\n" ||
  JCS({origin, module, specification_name, claim_name})
)>
```

The semantic digest is computed over the elaborated claim after deleting
source paths, byte locations, comments, and display-only labels. It includes
the resolved subject identity, claim kind, checker type and typed core,
examples, assumptions, and dependencies. Formatting and movement that leave
those meanings unchanged MUST preserve the digest; any meaning change MUST
invalidate it and all approvals or evidence bound to it.

## Claim vocabulary

Version 0.6 admits exactly:

- `rule`: a typed parameterized Boolean checker implemented by a named
  verification-only Catena definition;
- `example`: a finite exact invocation of a rule with literal arguments and
  an expected Boolean result;
- `conformance`: evidence emitted by the compiler for a successful named
  checker or artifact audit;
- `attestation`: an externally produced statement signed by an authorized
  principal; and
- `assumption`: an explicit unverified premise admitted only by policy.

An example is not a universal result. A signature is not proof of its signed
statement. An approval is not technical evidence. An assumption MUST remain
labelled as an assumption in every diagnostic and assurance manifest.

## Rule checking fragment

A rule checker MUST:

- be marked `verification_only`;
- have an explicit signature ending in `Bool`;
- accept all parameters declared by the rule;
- infer the empty effect row;
- use only version 0.6 pure Catena expressions and other pure definitions,
  excluding `request`, `handle`, and `resume` even when locally handled; and
- be unreachable from every retained runtime definition.

The ordinary type checker establishes the signature and empty-effect
requirements. A dependency-closure pass rejects a runtime-to-verification
reference as `ERS001` before lowering.

## Exact executable examples

Example arguments are JSON integers, Booleans, or recursively nested tuple
values admitted by the checker's parameter types. Floats, constructors, opaque
host terms, functions, processes, references, ports, and binaries are invalid
in 0.6. Evaluation is strict, left to right, and deterministic.

The checker has a fixed 20,000 semantic-step budget per example. A conforming
evaluator reports exactly one outcome:

- `supported`: evaluation completed with the expected Boolean;
- `counterexample`: evaluation completed with the opposite Boolean;
- `runtime_error`: a checked expression reached an evaluation fault; or
- `budget_exhausted`: the next semantic step would exceed the fixed budget.

Only `supported` satisfies an example requirement. The other outcomes remain
distinct in diagnostics and evidence.

## Assumptions

An assumption names the exact claim or claim kind it would satisfy and its
reason. It counts only when every matching active policy explicitly authorizes
that claim or kind and the approving principal holds the required assumption
role. General approval, a successful build, or an unavailable checker cannot
be converted into an assumption.

## Erasure dependency

Verification-only definitions remain in typed core long enough for examples
and independent verification. They MUST be absent from the runtime definition
set, exports, Erlang Abstract Format, interface value exports, and final BEAM
chunks. The [artifact chapter](artifacts-erasure-and-cli.md) defines the audit.
