---
title: "WebAssembly Core Specification 3.0"
kind: source
created: "2026-08-05"
authors:
  - "Andreas Rossberg (editor)"
published: 2026
citation_key: "rossberg2026WebAssemblyCore3"
container: "WebAssembly Specification"
edition: "Release 3.0"
isbn: null
doi: null
url: "https://webassembly.github.io/spec/core/"
accessed: "2026-08-05"
tags:
  - language-design
  - program-semantics
  - specification
aliases:
  - "WebAssembly 3.0 core spec"
---

# WebAssembly Core Specification 3.0

## Reference

Andreas Rossberg, ed. *WebAssembly Core Specification*, Release 3.0, live
official edition accessed 2026-08-05.
[Core specification](https://webassembly.github.io/spec/core/),
[validation conventions](https://webassembly.github.io/spec/core/valid/conventions.html),
[execution conventions](https://webassembly.github.io/spec/core/exec/conventions.html),
and [implementation limitations](https://webassembly.github.io/spec/core/appendix/implementation.html).

## Research question

How can a portable low-level language separate well-formed encodings,
declarative validation, execution, explicit traps, limited nondeterminism, and
implementation resource restrictions?

## Method

The analysis follows the core specification's structure, validation,
execution, and implementation-limit chapters. It treats prose and formal rules
as the specification's paired presentations and distinguishes normative core
behavior from embedder/host behavior.

## Findings

- Binary and text grammars define well-formed representations of one abstract
  syntax.
- Declarative validation defines which modules are valid; only valid modules
  can be instantiated, even when an implementation defers function validation.
- Execution is normally deterministic, with exceptions identified explicitly.
- A trap aborts the current computation through defined reduction behavior.
- Host calls and selected numerical cases can admit explicitly bounded sets of
  outcomes rather than an unbounded “anything happens” class.
- Implementations can impose structural, decoding, validation, and runtime
  limits and report implementation-specific errors when limits are exceeded.

## Relevance

The specification demonstrates that validation failure, traps, and
implementation limits can remain distinct and explicit. Catena adapts that
discipline by requiring transactional invalidity, stable limit diagnostics,
and explicit runtime failure, while narrowing unprofiled variability to
presentation or internal strategy that cannot affect semantics or artifacts.

## Limits

WebAssembly is an embedding-oriented low-level language with host functions,
implementation-specific errors, and selected nondeterminism. Its validation,
trap extent, and resource rules do not directly define Catena's type system,
BEAM process behavior, governance actions, or output transactions.

## Derived work

- [Catena Conformance Vocabulary and Behavior Classes](../20-notes/catena-conformance-vocabulary-and-behavior-classes.md)
- [How Should Catena Classify Conformance Behavior?](../40-inquiries/how-should-catena-classify-conformance-behavior.md)
- [Catena Conformance Vocabulary map](../10-maps/catena-conformance-vocabulary.md)
