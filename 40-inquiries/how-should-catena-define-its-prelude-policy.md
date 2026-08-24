---
title: "How Should Catena Define Its Prelude Policy?"
kind: inquiry
created: "2026-08-24"
status: resolved
tags:
  - catena
  - language-design
  - prelude
  - packages
aliases:
  - "Catena prelude inquiry"
---

# How Should Catena Define Its Prelude Policy?

## Why this matters

C021 fixed how names resolve and explicitly promised that "a future
prelude origin follows import precedence under G026 and is never a
silent default." C022 declined Haskell's implicit Prelude for ordinary
imports and shipped the origin machinery. C025 made packages nameable,
digest-bound, resolvable, and lock-pinnable. Yet nothing defines how a
package says "I want a prelude," what opt-out means, or what an edition
guarantees — and eight shipped chapters defer exactly those questions to
G026. Until it closes, every future standard-library design (G101) has
no admission mechanism to target, and tooling (G121) cannot know whether
any name arrives implicitly.

## Operational question

Choose a bounded 0.1.22 boundary in which independent implementations agree
on:

- how a package selects a prelude and what absence means;
- the prelude origin's precedence relative to locals, imports, and other
  origins;
- opt-out behavior and whether any per-name exclusion exists;
- what edition 0.1 guarantees about implicit names, and how any future
  edition-level default would enter; and
- stable diagnostics and lockfile treatment for prelude selections.

The answer must compose with C021's precedence and collision rules, C022's
import admission, and C025's package identity without amending them, and
must not decide G101's contents, P102's protocols, G121's tooling
defaults, or G027's entry points.

## Working hypotheses

- A manifest's optional `prelude` field names a package and requirement;
  present = that package's exports become an import-class origin,
  absent or `null` = no prelude origin.
- The prelude follows ordinary import precedence exactly: locals win;
  prelude-vs-import unqualified collisions reject as `NSP004` naming
  both origins; no weaker or stronger tier exists.
- Opt-out is the absent/`null` field; no sentinel, no per-name hiding.
- Edition 0.1 guarantees zero implicit names; any future default prelude
  enters through a lifecycle record, never silently.
- A prelude package is any valid C025 package — resolvable,
  digest-bound, and lock-pinned like any dependency — including one with
  zero exports; contents remain G101.

## Paths to explore

- [Haskell 2010 Prelude sections 5.6–5.6.2](../30-sources/marlow-2010-haskell-language-report.md)
  supply the fully-specified declined model: automatic-unless-explicit,
  empty-import exclusion, `hiding` disambiguation, syntax-frozen core.
- [Shadowing and Ambiguity](../60-specification/namespaces-and-shadowing/shadowing-and-ambiguity.md)
  fixes the precedence the prelude rides and pre-commits "never a silent
  default."
- [Import Declarations and Admission](../60-specification/imports-and-exports/import-declarations-and-admission.md)
  fixes the origin class and its diagnostics.
- [Resolution and Lockfile](../60-specification/package-identity-and-dependencies/resolution-and-lockfile.md)
  fixes the package identity, resolution, and lock treatment a prelude
  selection reuses.
- [Canonical Kernel Syntax](../60-specification/formal-semantic-kernel/canonical-kernel-syntax.md)
  fixes the explicitness stance (only explicit digest-backed imports).

## Findings

- The shipped corpus already selected the model in normative prose:
  C021's precedence promise plus C022's declination leave opt-in-via-
  selection as the only consistent admission; this inquiry consolidates
  rather than amends.
- Haskell's sections 5.6–5.6.2 demonstrate the cost of the alternative:
  implicit-unless-explicit admission creates ambiguity-transfer duties
  (`hiding(null)` pushes resolution onto importers) and a syntax-frozen
  core that special forms bypass regardless of imports — both mechanisms
  Catena declines; ordinary qualification already resolves what hiding
  would.
- C025's `dependencies` field supplies the exact shape precedent: an
  optional manifest object validated at decode, resolvable, lockable.
  A `prelude` sibling reuses it with one package instead of a map.
- Zero-implicit-names is truthful for 0.1 today (the standard library
  does not exist), so the edition guarantee strengthens rather than
  amends when G101 freezes contents.
- The synthesis
  [Catena Prelude Policy](../20-notes/catena-prelude-policy.md)
  develops the full model and falsification criteria; the
  [topic map](../10-maps/prelude-policy.md) routes the evidence.

## Outcome

Resolved as C026 and source-only language revision `0.1.22`. Catena
fixes the optional manifest `prelude` field (one package, one
requirement, absent/`null` = no origin); admission as an ordinary
import-class origin under unchanged C021 precedence with `NSP004`
collisions naming both origins; absent/`null` as the complete opt-out;
the zero-implicit-names edition guarantee with a lifecycle-record path
for any future default; `PRE001` for malformed selections; and prelude
selections resolving and locking as ordinary C025 dependencies,
including zero-export packages, with contents remaining G101's. The
rules are defined in the
[normative prelude specification](../60-specification/prelude-policy/README.md).

G026 is complete through the
[prelude synthesis](../20-notes/catena-prelude-policy.md),
[topic map](../10-maps/prelude-policy.md), and
[C026 evidence record](../50-journal/2026-08-24-c026-prelude-policy.md).
G101 retains contents; P102 retains protocols; G121 retains
scaffolding; G028/G136 retain compatibility meanings.
