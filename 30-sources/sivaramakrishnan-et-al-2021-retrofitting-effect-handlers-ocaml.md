---
title: "Retrofitting Effect Handlers onto OCaml"
kind: source
created: "2026-07-31"
authors:
  - "K. C. Sivaramakrishnan"
  - "Stephen Dolan"
  - "Leo White"
  - "Tom Kelly"
  - "Sadiq Jaffer"
  - "Anil Madhavapeddy"
published: 2021
citation_key: "sivaramakrishnanEtAl2021OCamlHandlers"
container: "Proceedings of PLDI 2021: 16 pages"
edition: null
isbn: null
doi: "10.1145/3453483.3454039"
url: "https://anil.recoil.org/papers/2021-pldi-retroeff/"
accessed: "2026-07-31"
tags:
  - algebraic-effects
  - effect-handlers
  - runtimes
aliases:
  - "OCaml effect-handler retrofit"
---

# Retrofitting Effect Handlers onto OCaml

## Reference

K. C. Sivaramakrishnan, Stephen Dolan, Leo White, Tom Kelly, Sadiq Jaffer, and
Anil Madhavapeddy, “Retrofitting Effect Handlers onto OCaml,” in *Proceedings
of the 42nd ACM SIGPLAN International Conference on Programming Language
Design and Implementation* (PLDI 2021), 16 pages.
[DOI](https://doi.org/10.1145/3453483.3454039),
[author manuscript](https://anil.recoil.org/papers/2021-pldi-retroeff.pdf), and
[author record](https://anil.recoil.org/papers/2021-pldi-retroeff/).

## Research question

Can a mature native language add handlers and delimited continuations while
preserving direct style, low overhead for existing programs, foreign-function
compatibility, and stack-sensitive tooling?

## Method

The paper describes the Multicore OCaml runtime design in detail. Handled
computations run on heap-allocated fiber stacks linked to the ordinary stack;
performing an effect captures the relevant fiber sequence as a continuation.
The authors adapt garbage collection, exceptions, C interoperability, stack
walking, backtraces, and debugging support, and evaluate microbenchmarks and
macrobenchmarks.

## Findings

- The implementation uses one-shot continuations because its target use cases,
  including concurrency, generators, and coroutines, resume at most once.
  Attempting a second resume raises `Invalid_argument`.
- One-shot use permits stack segments to be moved and reused rather than
  copied, reducing the runtime cost of capture and resume.
- Heap-allocated fibers allow captured stacks to coexist with conventional C
  frames and the language's native calling convention.
- The runtime work extends beyond capture: GC roots, exceptions, backtraces,
  stack overflow, C callbacks, and debugger/profiler stack inspection all need
  coherent treatment.
- Across the reported macrobenchmarks that do not use effect handlers, mean
  overhead is approximately 1%.
- Handler performance is workload-specific. One state example is slower than
  idiomatic recursion, while the handler-based concurrency example is much
  faster than the compared concurrency-monad version; neither comparison is a
  universal cost model.

## Relevance

This is strong implementation evidence for Catena's proposed affine one-shot
starting point and for treating stack tooling and FFI behavior as acceptance
criteria. It demonstrates that native stack segments can preserve direct style
with low idle overhead when the runtime is designed around them.

## Limits

The implementation intentionally does not provide transparent multi-shot
copying, so it does not support the full nondeterminism-handler pattern. The
paper also explicitly leaves static effect safety to future work; the runtime
mechanism does not guarantee that every performed effect has a handler. The
results are specific to OCaml's runtime, workloads, and hardware. Catena's
lexical capability and effect-row design would add front-end and elaboration
questions outside this paper's evaluation.

## Derived work

- [Algebraic Effects and Handlers](../20-notes/algebraic-effects-and-handlers.md)
- [Which Algebraic-Effect Semantics Should Catena Adopt?](../40-inquiries/which-algebraic-effect-semantics-should-catena-adopt.md)
- [Algebraic Effects and Handlers map](../10-maps/algebraic-effects-and-handlers.md)
