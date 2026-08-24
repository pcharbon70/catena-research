---
title: "Catena Entry Points"
kind: note
created: "2026-08-24"
maturity: developing
tags:
  - catena
  - language-design
  - entry-points
  - applications
  - packages
aliases:
  - "Catena application structure model"
---

# Catena Entry Points

## Executive conclusion

A Catena package declares zero or more **entries** in its manifest:
named, zero-argument, total, effect-closed exported functions with
declared result types. A package with entries is an executable
candidate — exactly one entry may carry the launch marker; a package
with none is a library, derived, with no kind flag. Launching an entry
means invoking its function to completion under the ordinary strict
kernel semantics: startup is invocation, nothing more. The entry's
returned value *is* the shutdown result; a failed launch reports the
trap identity. No supervision tree, no spawned processes, no exit-code
mapping, no implicit host handler — those belong to G084, G089, G121.

Every entry is effect-closed: all requests handled before return,
exactly as C010 already demands of process entries. This resolves
G082's question — which requests an application entry may leave
unhandled — by answer *none, statically*: an entry that would leave a
request unhandled is invalid before anything runs.

The executable deliverable wires the shipped pieces: the manifest
decoder (format 0.1.7, backward-compatible optional field, the
`dependencies`/`prelude` precedent) gains `entries`; and a launch
operation verifies the named entry against the compiled package's
interface, invokes it, and reports `{:ok, value}` or the failure. The
existing `roots` field keeps its compilation role — template
specializations the linker emits — untouched.

## Scope and method

The operational target is independent agreement on root shape,
top-level effects, startup, shutdown results, the library distinction,
diagnostics, and the deliverable — made executable through the manifest
field and the launch operation. Primary comparative evidence is the
[OTP applications analysis](../30-sources/erlang-otp-applications.md)
(the target-runtime precedent, useful and heavyweight directions), over
the shipped C010 kernel completion rules, C005 handler semantics, C024
component identity, C025 package machinery, and C026's zero-implicit-
names guarantee. Source claims stay distinct from Catena proposals
below.

## Relation to the current corpus

[C010's process-entry rule](../60-specification/formal-semantic-kernel/canonical-kernel-syntax.md)
already demands that ordinary effects are handled before a process entry
returns. An application entry is the same rule one level up: nothing
escapes. The kernel also fixes strict evaluation and trap semantics,
which is all "invocation" needs to be well-defined.

[C026's edition guarantee](../60-specification/prelude-policy/prelude-selection-and-admission.md)
— no name implicitly in scope — forces an entry convention that is
declared, not positional or reserved. A reserved `main` would be exactly
the kind of name nobody asked for.

[C025's package machinery](../60-specification/package-identity-and-dependencies/resolution-and-lockfile.md)
gives entries a home: the manifest, whose optional-field pattern
(`dependencies`, then `prelude`) is now established. An entry is
package-local metadata, resolved and locked with the package it belongs
to; no cross-package negotiation exists.

The linker's existing `roots` (template + export + types + instances)
are *compilation* roots — the points the companion module specializes.
Entries are orthogonal: a declared language-level invocation surface.
Neither implies the other, and the field names keep them apart.

Six shipped chapters deferred entry-point selection here; each
deferral resolves into this mechanism.

## Comparative evidence and inference

### OTP: the target precedent, both directions

[OTP applications](../30-sources/erlang-otp-applications.md) confirm two
choices and mark one boundary. Confirmed: the unit is package-shaped
(an application is a directory with a resource file), and the
library/executable distinction is *derived* — a library application
"cannot be started or stopped" and simply omits the callback module,
exactly as a Catena library simply omits entries. Marked boundary: OTP
startup is supervision-tree-first — `start/2` must return a supervisor
pid, and stopping terminates the tree in reverse start order. Catena
0.1 adopts neither: invocation-only is honest about the runtime layer
not yet being designed (G084/G089/G121 own it), and the OTP model
becomes the *future integration surface* — a later slice can map a
supervising entry onto `start/2` without having prejudiced it.

### Why effect-closure is forced, not chosen

The corpus leaves no room for an alternative. An implicit host handler
would be a silent default with no digest-bound identity — the exact
machinery C022 rejected for imports and C026 rejected for the prelude.
Manifest-named handlers per entry would drag handler-selection syntax
and cross-package wiring into this slice. Closure against the C001
interface's `uses` field — which already records effect rows per export
— makes the check static, cheap, and faithful to shipped data.

### Why `main` is wrong for Catena specifically

A reserved name is the one kind of entry declaration C026's guarantee
cannot accommodate: `main` would be a name in every package's export
namespace whether or not anyone declared it, or else a special
positional slot outside the namespace system. Multi-entry packages
(tests, tools, daemons in one artifact) would need widening later.
Named entries cost nothing more and represent all of them.

## Selected model

> **Normative definitions (placed in the candidate chapters).**

### Entry declarations

```json
"entries": [
  { "name": "run", "result": "Test::Report", "launch": true },
  { "name": "self_check", "result": "Core::Bool" }
]
```

- The field is optional; absent or `[]` means a library.
- Each entry names an existing export of arity zero whose row is empty
  (effect-closed) and whose result type is recorded as declared.
- At most one entry carries `"launch": true`. A package with entries
  and no marked launch is a multi-tool artifact; launching names the
  entry explicitly.
- Malformed shapes, unknown export names, non-zero arity, non-closed
  rows, duplicate names, and multiple launch markers reject as `ENT001`
  at manifest decode or package validation; launching an unknown entry
  name rejects as `ENT002`; a launch that traps reports `ENT003`.

### Startup and shutdown

Launching runs the entry's compiled function to completion under the
C010 strict semantics. The launch report is either
`{:ok, value}` — completed, with the entry's returned value as the
shutdown result — or `{:error, report}` — failed, with the trap
identity from the kernel's failure taxonomy. No supervision, spawning,
scheduling, exit codes, or graceful-stop protocol exists at this layer.

### Rejected alternatives

- **Reserved `main`** — a name nobody declared; blocks multi-entry
  packages.
- **Implicit host handler** — silent default, no digest-bound identity.
- **OTP `start/2` startup** — couples 0.1 to undesigned supervision.
- **Exit-code mapping** — presupposes G121's host boundary.
- **Explicit `kind` field** — a consistency obligation carrying
  information entries already encode.
- **Declared full absence** — untruthful while the linker compiles
  roots.
- **Entries + CLI now** — tooling is G121's; the C026 line, kept.

## What C027 adds to the design

The checklist's Section 3 program-box closes its executable half: a
program is a package with entries, a library is a package without, and
launching is invocation. G121's tooling gains a precise target (`catena
run <entry>` is a thin wrapper over the launch operation, later);
G028's compatibility analysis gains entry-set changes as an explicit
axis; G084/G089 gain a clean predecessor — supervision composes *over*
completed entries rather than competing with them; and the OTP
integration path stays open without being prejudiced.

## Remaining questions and falsification criteria

G084/G089 own supervision, restart, and process lifetime; G088 owns
cancellation and deadlines; G121 owns the CLI and host-process
boundary; G028 owns whether adding or removing an entry is a breaking
change; G091/G092 own distribution and upgrades.

The model should be revisited if the G084 era shows that real
applications overwhelmingly need startup concurrency (the remedy is a
supervising entry over a runtime slice, not reopening invocation), or
if G121's host integration makes value-only reports insufficient (the
remedy is an exit-code *profile* at the tooling layer, not a language
change).

## Connections

- The [resolved entry-points inquiry](../40-inquiries/how-should-catena-define-entry-points-and-application-structure.md)
  records the question, hypotheses, and outcome.
- The [Entry Points map](../10-maps/entry-points.md) routes through the
  OTP precedent, the shipped contracts, and remaining owners.
- The [Entry Points Specification](../60-specification/entry-points/README.md)
  defines the normative `0.1.23` contract this note argued for.
- [Catena Package Identity and Dependencies](catena-package-identity-and-dependencies.md)
  fixes the manifest and identity machinery entries ride.
- [Catena Prelude Policy](catena-prelude-policy.md) fixes the
  zero-implicit-names guarantee entries obey.

## Sources

- [Erlang/OTP Applications](../30-sources/erlang-otp-applications.md)
- [Canonical Kernel Syntax](../60-specification/formal-semantic-kernel/canonical-kernel-syntax.md)
- [Resolution and Lockfile](../60-specification/package-identity-and-dependencies/resolution-and-lockfile.md)
- [Prelude Selection and Admission](../60-specification/prelude-policy/prelude-selection-and-admission.md)
