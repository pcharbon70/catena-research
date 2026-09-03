---
title: "Clause Contexts and Receive"
kind: specification
created: "2026-08-02"
status: normative
spec_version: "0.1.3"
tags:
  - concurrency
  - pattern-matching
  - program-semantics
  - specification
aliases:
  - "Catena condition contexts"
---

# Clause Contexts and Receive

## Ordinary matches

Every ordinary `match` expression MUST be exhaustive under structural and
certified 0.1.3 facts. A condition may reject a structurally matching value, so
the compiler requires a later accepting clause unless the supported fact
theory proves that other guarded clauses cover the remainder.

The scrutinee is evaluated once. All branch bodies have one unifiable result
type. A condition contributes no effect and no body type refinement.

## Multi-clause functions

One signed multi-clause function declaration has a nonempty shared arity. Its
arguments are evaluated according to the eventual general call-order rule,
then clause selection treats the argument vector as one structural scrutinee.
Every clause has the same result type and the complete clause set MUST be
exhaustive.

The bootstrap AST elaborates a one-argument function to a match on that
argument and a multi-argument function to a match on an internal tuple of
arguments. This elaboration MUST preserve source clause order, bindings,
condition evaluation count, and exported BEAM arity.

## Selective receive harness

Version 0.1.3 specifies a typed lowering harness, not a public receive
expression. The harness requires:

- one explicit closed message type containing no free or rigid type variable;
- clauses already pattern-typed against that message type;
- only 0.1.3 conditions whose transitively expanded core is portable and
  native-lowerable; and
- no timeout, after-clause, protocol transition, or receive effect semantics.

A receive condition is evaluated while scanning candidate mailbox messages.
If the structural pattern or native condition rejects a message, that message
remains in the mailbox and scanning continues according to BEAM selective
receive semantics. A selected message is removed exactly once before its body
runs.

The harness rejects or-pattern expansion because the initial backend cannot
guarantee shared one-time condition evaluation for overlapping alternatives in
a native Erlang receive clause list. This restriction is narrower than
ordinary match syntax and reports `CND006`.

## Native-only rule

Ordinary matches and functions have both native and ordinary pure-branch
lowering. Selective receive has no semantics-preserving fallback that consumes
a message, calls arbitrary code, and re-enqueues a rejected message. Therefore
the 0.1.3 harness accepts only the portable native intersection.

An imported condition may be used in receive only when its verified expanded
core can be inlined within the deterministic budget and every resulting
operation maps to the portable native set.

## Explicitly unresolved receive semantics

This chapter does not complete selective receive as a language feature. The
0.1.46 [Selective Receive Specification](../selective-receive/README.md)
now states the language-level rule set and routes the remaining
connections:

- public syntax and effect typing;
- mailbox and message type policy;
- scan order, starvation, and fairness;
- timeout evaluation and races;
- process failure and cancellation;
- protocol evolution; and
- debugging and cost explanations.

## Connections (non-normative)

The native operation mapping is in [BEAM Lowering](beam-lowering.md). The wider
process architecture remains open in the
[Catena Language Overview](../../language-overview.md).
