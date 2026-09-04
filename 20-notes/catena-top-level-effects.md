---
title: "Catena Top-Level Effects"
kind: note
created: "2026-09-01"
maturity: developing
tags:
  - catena
  - effects
  - entry-points
  - language-design
aliases:
  - "the top-level boundary"
---

# Catena Top-Level Effects

## Executive conclusion

The top level of a Catena application is silent. An entry point
leaves nothing unhandled — every request its body can perform is
handled before return, or the package does not build (`ENT001`) —
and nobody interprets unhandled requests because none exist: no
ambient host handler exists or is reserved, and the launch root
does exactly one thing, invoke a total entry to completion. What
G082 adds over C027's standing answer is the home for that
statement, the interface any future capability channel (G106's)
must satisfy — explicit typed values, deny-able, never ambient —
and the routing that keeps failure interpretation (G084's
supervision) a distinct concern from effect interpretation.

## Scope, method, and definitions

This note synthesizes the archive's evidence for closing G082 at
revision `0.1.48`. It reads C027's entry chapters, C026's
zero-implicit-names rule, C067's visible-boundary discipline, and
C036/C081's failure machinery; it invents no channel and reserves
no handler.

## Why the top level is silent

Three pillars. **C027's effect-closed rule**: an entry's recorded
effect row is empty or the package rejects — the question "which
requests may an entry leave unhandled" has the empty set as its
answer, statically. **No ambient interpreter**: the runtime
provides no default handler; there is nothing to interpret an
unhandled request because there cannot be one. **Launch is
invocation only**: the launch root runs the entry under unchanged
kernel semantics to completion — return is shutdown; it opens no
scope, injects no capability, and answers no request.

## The capability interface, stated for its owner

An entry that needs the world must receive it explicitly: typed
values, through a channel G106 defines and justifies, deny-able
like every capability in the corpus. Until that slice exists, the
zero-argument and effect-closed rules bind — an application that
needs I/O today composes it as a library over explicit values
handed in by whatever host embeds the launch, and the language
stays out of the business of ambient services.

## Tradeoffs, limitations, falsification

The silent top level costs immediacy — a "hello world" needs a
host or a capability channel that does not exist yet — and buys
total determinism at the boundary: an entry's completion is a
function of nothing but itself. Falsification: any ambient
handler, any unhandled request reaching a runtime interpreter,
any capability injected without a visible channel, or any
widening of the entry form without amending C027 explicitly.

## Route to sources

- The Top-Level Effects Specification (candidate, then normative
  at promotion, in `60-specification/top-level-effects/`) will
  define the contract this note argues for.
- [Entry Declarations](../60-specification/entry-points/entry-declarations.md)
  — C027's effect-closed rule, the standing answer this elevates.
- [Startup and Shutdown](../60-specification/entry-points/startup-and-shutdown.md)
  — launch as invocation only.
- [Prelude Policy](../60-specification/prelude-policy/README.md)
  — the zero-implicit-names pillar.
- The [resolved inquiry](../40-inquiries/who-interprets-top-level-requests.md)
  preserves the decision route.
