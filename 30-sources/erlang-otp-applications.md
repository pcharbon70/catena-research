---
title: "Erlang/OTP Applications"
kind: source
created: "2026-08-24"
published: null
citation_key: null
container: "Erlang/OTP System Documentation"
edition: null
isbn: null
doi: null
url: "https://www.erlang.org/doc/design_principles/applications.html"
accessed: "2026-08-24"
tags:
  - erlang
  - applications
  - entry-points
aliases:
  - "OTP applications"
---

# Erlang/OTP Applications

## Reference

Erlang/OTP, "Applications," *Erlang System Documentation*, current online
edition accessed 2026-08-24.
[Official documentation](https://www.erlang.org/doc/design_principles/applications.html).

The page is living documentation; it identified itself as OTP 29.0.5 when
consulted.

## Research question or contribution

How does the target runtime define application identity, startup,
shutdown, and the distinction between executable and library components?

## Method

The OTP design-principles applications chapter was read for the callback
contract, the application resource file, start types, and the controller's
loading and stopping behavior. Adjacent runtime modules (`application`,
`app`) were not separately fetched; this note records only the design
chapter's claims.

## Findings

- An OTP application is "a component that can be started and stopped as
  a unit." Two artifacts define one: a callback module and an
  application resource file (`.app`).
- The callback contract is `start(StartType, StartArgs) -> {ok, Pid} |
  {ok, Pid, State} | {error, Reason}` and `stop(State)`. `start/2` is
  expected to create the supervision tree by starting the top
  supervisor; `StartType` is `normal` except in distributed
  takeover/failover.
- A library application "that cannot be started or stopped does not need
  any application callback module" — the library/executable distinction
  is made by the presence of the `mod` key in the resource file.
- The `.app` file names the callback module and start arguments
  (`mod`), the introduced modules, registered names, and the
  applications that must be started first (`applications` — a startup
  dependency list).
- Starting an application: the controller loads the resource file,
  checks that all dependency applications run, creates an application
  master that becomes the group leader of the application's processes,
  and calls `start/2`. Stopping tells the top supervisor to shut down;
  the tree terminates in reverse start order; then `stop/1` runs.
- Start types — `temporary`, `transient`, `permanent` — define what
  happens to the rest of the system when the application terminates.
- Configuration (`env`) can be overridden by system configuration files
  and command-line arguments.

## Relevance

This is the target-runtime precedent for G027's questions, in both its
useful and its heavyweight directions. Useful: the unit is
package-shaped; the library/executable distinction is derived (callback
module present or not) rather than an explicit kind flag — matching
Catena's chosen derivation by entries-present. Startup dependency
ordering exists (the `applications` key), which Catena already achieves
through C025 dependency resolution. Heavyweight: OTP startup is
supervision-tree-first — `start/2` must return a top-supervisor pid, and
shutdown is tree termination. Catena's 0.1 deliberately does not adopt
that: entries are effect-closed value-returning functions, invocation is
completion, and supervision remains with G084/G089/G121. The OTP model is
therefore the future integration surface, not the 0.1 semantic.

## Limits

The chapter specifies OTP conventions, not Catena semantics. OTP's start
types, group-leader tracking, configuration layering, and distributed
takeover are runtime machinery whose Catena counterparts (if any) belong
to later runtime slices and tooling.

## Derived work

- [Catena Entry Points](../20-notes/catena-entry-points.md)
- [How Should Catena Define Entry Points and Application Structure?](../40-inquiries/how-should-catena-define-entry-points-and-application-structure.md)
- [Entry Points map](../10-maps/entry-points.md)
