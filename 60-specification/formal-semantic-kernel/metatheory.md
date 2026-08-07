---
title: "Formal Semantic Kernel Metatheory"
kind: specification
created: "2026-08-06"
status: normative
spec_version: "0.1.8"
tags:
  - formal-semantics
  - metatheory
  - specification
aliases:
  - "Catena integrated soundness claims"
---

# Formal Semantic Kernel Metatheory

## Normative claims

For the 0.1.8 kernel, a conforming static and dynamic model satisfies:

1. **Substitution:** value substitution, type substitution in regular data and
   signatures, and instantiation of a recorded local scheme preserve the
   integrated judgment.
2. **Scheme maximality:** a generalizable `let` records exactly the type
   variables free in its value type and absent from the environment; a binding
   outside the value/effect restriction records no quantified variables.
3. **Row soundness:** record and variant operations preserve their unique-row
   constraints; closed-row extension establishes absence; effect handling
   removes one selected ordinary occurrence and preserves multiplicity.
4. **Trait coherence:** one accepted closed trait use has one selected instance
   and definition meaning, and evidence erasure preserves observations.
5. **Handler safety:** a well-typed request either reaches its selected
   handler, remains an allowed residual ordinary effect before execution,
   reaches the explicit unhandled-effect trap, or is rejected at a process
   boundary.
6. **Affine safety:** a verified handler clause abandons its resumption or has
   one syntactic resume site; no accepted core can enter it twice.
7. **Sequential preservation:** an ordinary local step preserves type and
   residual effect, or reaches its declared explicit trap.
8. **Sequential progress:** a closed well-typed local term is a value, can
   step, is a selected request, is a process operation under a process
   context, or is an explicit trap.
9. **Mailbox preservation:** every live mailbox contains only sendable values
   of its declared closed type.
10. **Global preservation:** a global step preserves process-entry typing,
    handle typing, mailbox typing, freshness, and trace well-formedness.
11. **Global progress classification:** a closed well-typed configuration is
    terminated, trapped, quiescent, or has at least one global step.
12. **Lowering refinement:** every observed verified BEAM execution maps to a
    reference execution with the same exported root value or specified trap
    and the same source-observable send/receive order, modulo opaque process
    spelling and a permitted scheduler interleaving.

An implementation limit may refuse an otherwise valid input only with its
distinct limit result. Such a refusal is not a counterexample to these claims.

## Proof outline (non-normative)

The substitution proof proceeds simultaneously over types, local schemes,
typing, and core evidence. Unique-row extension uses its closed-row premise;
effect cases retain the selected effect, operation, and handler identities.
Trait coherence follows from closed heads and the module-wide non-overlap
check.

Sequential preservation is induction on the evaluation-context decomposition.
Handler cases use the C005 deep-resume invariant. Process cases extend the
induction to configurations: spawn uses the checked entry signature, send
uses recursive sendability, and receive uses pattern substitution plus
mailbox removal.

Global progress deliberately excludes deadlock freedom and fairness.
Quiescence handles the well-typed configuration in which no mailbox currently
contains an acceptable message.

## Evidence status (non-normative)

C010 requires the written rule and proof outline plus generated small terms,
forged-core rejection, bounded schedule exploration, and differential BEAM
evidence. It does not require proof-assistant mechanization. A generated corpus
supplements the named claims and cannot replace a missing rule or proof
argument.

## Falsification

Promotion is blocked by any well-typed closed term stuck outside the listed
progress cases, any step that changes its type or mailbox invariant, two
coherent evidence meanings, selection of a handler other than the one recorded
by the core, a second accepted resumption site, a non-sendable mailbox value,
or a verified BEAM observation outside the reference outcome set.
