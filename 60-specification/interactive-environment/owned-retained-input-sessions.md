---
title: "Owned Retained-Input Sessions"
kind: specification
created: "2026-09-12"
status: normative
spec_version: "0.1.95"
tags: [specification, tooling, effects, resources]
aliases: []
---

# Owned Retained-Input Sessions

## Status and authority

G120 defines its preparatory interactive-session engine at revision `0.1.95`
under [authority](../../SPECIFICATION-AUTHORITY.md),
[conformance vocabulary](../../CONFORMANCE-VOCABULARY.md), and
[implementation limits](../../IMPLEMENTATION-LIMITS.md). It executes the
[G120 plan](../../20-notes/language-completion-plan-delivery.md#item-120-interactive-environment)
without choosing Catena's public vocabulary or grammar. Public input editing,
parsing, recovery, display syntax, and a command-line REPL remain held for
P109, so G120 remains partial (`IS-OBL-001`).

## Session authority and ownership

A session MUST have exactly one owner: the process that creates it. The owner
alone is permitted to load a module, evaluate a definition, wait for or
interrupt an evaluation, inspect history, or close the session. A job handle
MUST remain bound to its session and owner, and use by another process MUST be
rejected (`IS-OBL-002`).

Session creation MUST admit an explicit duplicate-free set of named
capabilities. An evaluated definition MUST have a closed verified effect row,
and every capability in that row MUST occur in the admitted set. An open row
or absent capability MUST be rejected before evaluation (`IS-OBL-003`).

The owner is a lifetime boundary. Owner termination MUST terminate the session
and signal termination to every pending evaluation owned by that session
(`IS-OBL-004`).

## Retained modules and generations

A load MUST accept only a checked retained JSON AST or retained semantic
kernel. The session MUST retain the checked core and an exact SHA-256 digest of
the submitted bytes. It MUST NOT treat unchecked public source as session
input at this revision (`IS-OBL-005`).

The first admitted version of a module MUST be generation zero. Loading the
same module again MUST require explicit replacement selection and MUST create
the next immutable generation. It MUST NOT mutate an earlier generation or
silently perform hot code upgrade. The newest admitted generation becomes
active while a retained earlier generation remains selectable by its exact
number (`IS-OBL-006`).

When the fixed retention bound discards an earlier generation, requesting that
generation MUST produce the distinct stale-or-unknown-generation outcome.
Evaluation MUST capture its selected checked core before work begins, so a
later replacement cannot change that running evaluation (`IS-OBL-007`).

## Evaluation, jobs, and interruption

An evaluation MUST select the active generation unless the owner supplies an
exact generation number. It MUST identify an existing definition, complete
effect admission, and run the bounded reference evaluator with a positive
step budget. Completion MUST report the value and consumed steps; budget
exhaustion MUST remain distinct from invalid input, denial, cancellation, and
worker failure (`IS-OBL-008`).

An asynchronous evaluation MUST produce an owner-bound job handle. Waiting
MUST return its terminal result, including a result completed before the wait.
No more than one pending waiter can be registered for a job. Interrupting
pending work MUST terminate its worker, confirm termination, and record
`session-interrupt` cancellation before reporting success. Interrupting a
completed job MUST report that it already completed (`IS-OBL-009`).

Closing a session MUST request termination of every pending worker and MUST
confirm their termination before reporting a closed result. If confirmation
does not arrive within the fixed cleanup bound, close MUST report the distinct
cleanup-timeout outcome and leave the session available for an explicit retry.
A successful close MUST report cancelled-job, retained-generation, retained
history, and dropped-history counts. Later use MUST report that the session is
closed or unavailable (`IS-OBL-010`).

## History and governance

History MUST use monotonically increasing session-local sequence numbers and
MUST retain only the newest fixed number of entries. It MUST report how many
older entries were dropped. Each entry MUST classify its action and outcome.
Values MUST be redacted by default. Session creation can explicitly opt into
value capture, but an evaluation marked sensitive MUST remain redacted
(`IS-OBL-011`).

Interactive checking, evaluation, and history are observational evidence; they
MUST NOT grant package publication, trust-policy, upgrade, deployment, or
other governance authority. A load presented as already governed MUST be
refused with an external-admission-required outcome (`IS-OBL-012`).

## Limits and variability

One session is limited to 16 admitted capabilities, 32 retained generations
per module, and 256 retained history entries. The default evaluation budget is
100,000 reference steps and the maximum accepted budget is 10,000,000 steps.
Cleanup confirmation is limited to 1,000 milliseconds. Exceeding an admission
or evaluation bound MUST produce the distinct interactive-session-limit
outcome before evaluation begins (`IS-OBL-013`).

This preparatory session has zero variability dispositions. An implementation
MUST NOT substitute ambient authority, mutable declarations, unbounded
history, a host evaluator, or host REPL syntax and describe the result as this
contract (`IS-OBL-014`).

## Conformance

The conformance profile MUST publish revision, admitted input kinds, the P109
public-REPL hold, ownership rule, capability rule, generation rule, evaluator,
child lifetime, history policy, governance boundary, and every fixed limit
(`IS-OBL-015`).

An implementation claiming this revision MUST exercise retained JSON and
kernel loading, active and exact old generations, explicit replacement,
effect denial, invalid capability admission, bounded evaluation, completed and
pending job races, interruption, confirmed close cleanup, owner-death cleanup,
redacted and opted-in history, governed-action refusal, lifecycle selection,
production compilation, trust-inventory verification, and its complete
regression suite (`IS-OBL-016`).

## Rationale and evidence (non-normative)

The [implementation journal](../../50-journal/2026-09-12-interactive-environment.md)
records twenty-two four-way implementation decisions and compiler PRs
[188](https://github.com/pcharbon70/catena/pull/188) and
[189](https://github.com/pcharbon70/catena/pull/189), and
[190](https://github.com/pcharbon70/catena/pull/190), and
[191](https://github.com/pcharbon70/catena/pull/191). Retained semantic input
makes session ownership, effects, generations, cancellation, and evidence
executable while leaving public productions and vocabulary for joint design at
P109.
