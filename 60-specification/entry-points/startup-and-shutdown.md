---
title: "Startup and Shutdown"
kind: specification
created: "2026-08-24"
status: normative
spec_version: "0.1.23"
tags:
  - entry-points
  - specification
aliases:
  - "Catena launch semantics"
---

# Startup and Shutdown

## Status and authority

This chapter is the normative Catena 0.1.23 launch, startup, and
shutdown contract. It is governed by
[Specification Authority](../../SPECIFICATION-AUTHORITY.md),
[Catena Conformance Vocabulary](../../CONFORMANCE-VOCABULARY.md), and
[Catena Implementation Limits and Portability](../../IMPLEMENTATION-LIMITS.md).
It applies the entry declarations of
[Entry Declarations](entry-declarations.md)
over the evaluation and completion rules of
[Canonical Kernel Syntax](../formal-semantic-kernel/canonical-kernel-syntax.md)
and [Sequential Dynamics](../formal-semantic-kernel/sequential-dynamics.md).

The rules apply only to source-language revision `0.1.23`. They do not
reinterpret retained manifests, interfaces, artifacts, or signed formats.

## Launch

Launching a package entry means invoking the named entry's exported
function with no arguments and evaluating it to completion under the
ordinary strict kernel semantics (`EN-OBL-006`). Launch is the whole of
application startup in 0.1.23:

> **Normative definition.**

```text
launch( package, entry-name ) = report ;
report = { completed, value } | { failed, trap } ;
```

- The entry MUST be declared in the package's manifest; a launch naming
  an undeclared entry rejects as `ENT002` (`EN-OBL-008`).
- Launching introduces no names into any scope, binds no handlers,
  installs no implicit runtime interpreter, and spawns no process. The
  evaluation is the unchanged kernel evaluation of the export's body.
- A package whose entry carries the launch marker of
  [Entry Declarations](entry-declarations.md) names the preferred entry
  for a single-entry launch; a launch MAY name any declared entry
  explicitly (`EN-OBL-005`).

## Return is shutdown

An entry's completion is its shutdown (`EN-OBL-007`):

- **Completed** — when the entry's function returns a value, the launch
  report is `{ completed, value }` with the returned value as the
  shutdown result. The value is the entry's declared `result` type's
  value; nothing further is executed, terminated, or drained.
- **Failed** — when the evaluation traps, the launch report is
  `{ failed, trap }` with the trap identity under the kernel failure
  taxonomy of
  [Actors, Messages, and Failures](../formal-semantic-kernel/actors-messages-and-failures.md),
  reported as `ENT003`. No value accompanies a failure.

No exit-code mapping, termination signal, graceful-stop protocol, or
post-return hook exists at this layer. A host or tool that needs
process-level exit behavior derives it from the report under its own
profile; that derivation remains G121's and changes nothing here.

## Determinism

Equal packages, equal entry names, and equal inputs produce equal
launch reports (`EN-OBL-010`). Launching is deterministic and
side-effect-free outside the evaluation it performs; repeating a launch
of a total, effect-closed entry reproduces its report.

## Excluded machinery

The following are deliberately absent from 0.1.23 and owned elsewhere;
implementations MUST NOT use this chapter's boundary to claim them
(`EN-OBL-010`):

- supervision trees, restart policies, and child specifications
  (G084/G089);
- process spawning, scheduling, and lifetime per launch (G084);
- cancellation, timeouts, and deadlines around a launch (G088);
- distribution, clustering, and takeover (G091/G092);
- CLI `run` commands, exit-code profiles, and signal handling (G121);
- concurrency across entries (G084).

An OTP-application integration — mapping a supervising entry onto a
target application callback — is future work over this contract, not
part of it.

## Rationale and evidence (non-normative)

The [entry-points synthesis](../../20-notes/catena-entry-points.md)
records why invocation-only was selected over OTP `start/2` startup and
spawn-per-entry, what the [OTP applications
analysis](../../30-sources/erlang-otp-applications.md) contributes, and
the falsification criteria that would reopen the model. The [topic
map](../../10-maps/entry-points.md) routes the decision.
