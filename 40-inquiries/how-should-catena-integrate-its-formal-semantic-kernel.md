---
title: "How Should Catena Integrate Its Formal Semantic Kernel?"
kind: inquiry
created: "2026-08-06"
status: resolved
tags:
  - concurrency
  - formal-semantics
  - language-design
aliases:
  - "P010 formal kernel inquiry"
---

# How Should Catena Integrate Its Formal Semantic Kernel?

## Why this matters

Catena's earlier completed slices specified substantial local behavior, but
their shared values, contexts, rows, evidence, handlers, processes, and source
input lacked one operational model. C010 resolves that gap without allowing
compiler composition to decide those interactions silently.

## Operational question

What smallest versioned calculus can compose one bounded executable subset of
the current type, data, condition, trait, and handler semantics with structural
value rows and a useful public local process boundary while supporting an
independent model, paper soundness argument, and verified BEAM lowering?

## Working hypotheses

- A strict small-step calculus with evaluation contexts is easier to audit
  across handlers and traps than separate big-step evaluators.
- A canonical S-expression module can close P010 without prejudging ergonomic
  Catena syntax.
- A closed mailbox type is sufficient for the first public process boundary;
  behavioral protocols should remain future work.
- The runtime Process effect must be visible statically but unavailable to
  user handlers.

## Paths to explore

- Compare structural operational semantics, abstract machines, and trace
  semantics for divergence and concurrency.
- Test fixed record/variant layouts against reference semantic values.
- Explore scheduler interleavings independently from BEAM scheduling.
- Try to falsify sendability, mailbox preservation, handler isolation, and
  affine resumption claims with generated and forged core.

## Findings

The [synthesis](../20-notes/catena-formal-semantic-kernel.md) selects a
unary curried sequential core, unique value rows, named deep handlers,
named process entries, `Process M`, per-sender FIFO, oldest-matching receive,
no fairness, and an explicit process-local trap. The normative
[0.1.8 area](../60-specification/formal-semantic-kernel/README.md) states the
corresponding grammar, judgments, transitions, proof claims, and gate.

The immutable compiler implementation provides that closed grammar, integrated
checker, independently structured verifier, fixed interface and BEAM lowering,
reference stepper, and bounded schedule explorer. The implementation exposes
regular positional data, inline conditions, one-parameter closed traits, and
effect-free named handler clauses rather than claiming the broader retained
frontends were re-encoded in the kernel.

## Outcome

Catena integrates the bounded kernel as a distinct exact 0.1.8 S-expression
input with one independently verified core, local CEK and global actor
dynamics, typed process interfaces, and fixed OTP 29 lowering. The explicitly
authorized immutable compiler commit and its post-commit gate satisfy the
promotion condition. The
[C010 journal](../50-journal/2026-08-06-c010-formal-semantic-kernel.md)
records that identity and evidence; broader ergonomic source syntax,
behavioral mailbox protocols, supervision, distribution, time, cleanup, and
machine-checked metatheory remain separately tracked work.
