---
title: "How Should Catena Define Entry Points and Application Structure?"
kind: inquiry
created: "2026-08-24"
status: resolved
tags:
  - catena
  - entry-points
  - applications
  - language-design
aliases:
  - "G027 entry points inquiry"
---

# How Should Catena Define Entry Points and Application Structure?

## Purpose

G027 asks the checklist question: "Define executable and library roots,
top-level effects, application startup, and shutdown results." Until
C027, every shipped chapter that needed an entry-point notion — six of
them across files, imports, cycles, packages, and the prelude — deferred
to G027, and the package linker carried a `roots` mechanism with no
language-level story for what a *program* is. This inquiry resolves what
it means to launch a Catena package.

## Operational definitions

- **Entry** — a named, zero-argument, total, effect-closed exported
  function with a declared result type, declared in the package manifest.
- **Library** — a package that declares no entries.
- **Launch** — invoking one declared entry's function to completion under
  the ordinary strict kernel semantics.
- **Shutdown result** — the value a launched entry returns, or the trap
  identity if it fails; the launch report carries one of the two.
- **Effect-closed** — every effect request the entry's body can perform
  is handled before the entry returns, per the C010 completion rule.

## Hypotheses

1. Named entry exports carried in the manifest (distinct from the
   linker's compilation `roots`) express executables and libraries
   without a reserved name or a manifest kind flag. *(Recommended:
   composes with C026's zero-implicit-names and keeps multi-entry
   packages — tools, tests, daemons — representable.)*
2. Entries must be effect-closed: static invalidity otherwise. This
   answers G082 ("which requests an application entry point may leave
   unhandled") by closure rather than an implicit host handler.
3. Startup in 0.1 is invocation-only — no supervision, no spawning, no
   OTP coupling; that vocabulary stays with G084/G089/G121.
4. Shutdown is return-is-shutdown — the returned value is the result; no
   exit-code mapping and no graceful-stop protocol in 0.1.
5. The library/executable distinction is derived from entries-present,
   mirroring how OTP derives it from callback-module presence.

## Paths explored

- **Reserved `main` name** — familiar but reserves a name no layer ever
  reserved and blocks multi-entry packages without later widening.
- **Implicit runtime host handler** for effectful entries — expressive
  but invents exactly the silent-default machinery C022/C026 rejected,
  with no digest-bound identity.
- **OTP `start/2` application startup** — target-native but couples a
  language slice to supervision decisions owned by G084/G089
  ([OTP findings](../30-sources/erlang-otp-applications.md)).
- **Exit-code mapping** — ergonomic for CLIs but presupposes a
  host-process model G121 owns.
- **Explicit `kind: library|executable` manifest field** — creates a
  consistency obligation for information the entries list already
  carries.
- **Declared full absence** — truthful only if no mechanism existed; the
  linker's roots make a real answer cheap.

## Findings

All five hypotheses held. The developer chose the recommended option on
every fork (six of six, no overrides): named entry exports, effect-closed
entries, invocation-only startup, return-is-shutdown, derived libraries,
and a manifest-entries + launch-operation deliverable at `0.1.23`.

Two corpus facts shaped the design. First, the C001 interface's `uses`
field already records effect rows per export, so effect-closure is
checkable against shipped interface data rather than new core metadata.
Second, OTP's own library derivation (a library application is one
without a callback module) confirmed that derivation beats an explicit
kind flag on the target runtime too.

## Outcome

Resolved as C027 at revision `0.1.23`: the contract lives in the
[Entry Points Specification](../60-specification/entry-points/README.md),
the reasoning
in [Catena Entry Points](../20-notes/catena-entry-points.md), and the
forks in the [design decision register](../20-notes/design-decision-register.md).
Supervision/restart (G084), cancellation (G088), the CLI/host boundary
(G121), distribution (G091), and entry-set compatibility (G028) remain
open with their owners.
