---
title: "Erlang/OTP Support, Compatibility, Deprecations, and Removal"
kind: source
created: "2026-08-24"
published: null
citation_key: null
container: "Erlang/OTP System Documentation"
edition: null
isbn: null
doi: null
url: "https://www.erlang.org/doc/system/misc.html"
accessed: "2026-08-24"
tags:
  - erlang
  - compatibility
  - deprecation
  - abi
aliases:
  - "OTP compatibility strategy"
  - "OTP deprecation policy"
---

# Erlang/OTP Support, Compatibility, Deprecations, and Removal

## Reference

Erlang/OTP, "Support, Compatibility, Deprecations, and Removal," *Erlang
System Documentation*, current online edition accessed 2026-08-24.
[Official strategy page](https://www.erlang.org/doc/system/misc.html).
The page identifies itself as introduced in Erlang/OTP 21 and was served
as OTP 29.0.5 when consulted. Two companion pages were read alongside
it: [Upcoming Potential
Incompatibilities](https://www.erlang.org/doc/upcoming_incompatibilities.html)
and [Deprecations](https://www.erlang.org/doc/deprecations.html).

## Research question or contribution

How does the target runtime manage compatibility across releases —
which surfaces are promised stable, which are refused, and through what
deprecation and removal process?

## Method

The strategy chapter and both companion lists were read for the
compatibility tiers, the escape-hatch policy, and the
deprecation-removal process. No OTP source code was consulted.

## Findings

- **Compatibility is tiered by surface, not uniform.** The chapter
  assigns different handling to different parts: the Erlang
  distribution communicates "across at least two preceding and two
  subsequent releases"; compiled BEAM code, NIF libraries, and drivers
  load "on at least two subsequent releases" and *never* previous ones;
  APIs are "compatible between releases"; compiler warnings may be
  newly issued between releases; command-line arguments and build
  procedures may change incompatibly at any release.
- **Incompatibility has explicit escape hatches**, even on promised
  surfaces: security issues (possibly in a patch), bug fixes ("We will
  not be bug-compatible" — a fix may itself be incompatible, possibly
  in a patch), and severe legacy design issues (only in a subsequent
  release, never a patch).
- **Risk is graded**: peripheral, trace, and debug functionality is at
  greater risk of incompatible change or removal than the language
  itself and core operational libraries.
- **Deprecation does not imply removal** unless the notice explicitly
  says so. Deprecations are documented, highlighted in release notes,
  and optionally warned by the compiler.
- **Removal is gradual**: functionality is deprecated for at least one
  release, with an explicit scheduled-removal announcement, before it
  is removed. The companion pages carry the concrete lists — e.g.
  `erlang:fun_info/1,2`'s `{pid,_}` element (announced OTP 27, removed
  OTP 30) and the `re` engine switch (OTP 28).
- Upcoming incompatibilities are announced one or more releases ahead
  on a dedicated page — for instance `0.0 =:= -0.0` becoming `false`
  and the `maybe` atom requiring quoting, both announced with compiler
  warnings available *before* the change landed.

## Relevance

This is the target-runtime precedent for G028, and it validates the
layered stance Catena selected before this evidence was gathered.
Erlang's own policy refuses a uniform compatibility promise: it
distinguishes wire (distribution), binary (BEAM/NIF), source-API, and
tooling surfaces exactly as Catena's four layers do, and it expressly
declines bug-compatibility — the same reasoning behind Catena's
"the deterministic kernel is the behavior contract" absence. Its
deprecation-then-announced-removal process is the lifecycle-record
discipline Catena's C008 already fixes in identifier form. The one
surface Erlang promises and Catena will not is binary compatibility
(BEAM loads two releases forward): for Catena that is a deliberate
0.x-era absence — companion binaries are deterministic outputs, not a
compatibility surface — and Erlang's own "never previous releases"
asymmetry shows even the target treats binary compat as a bounded
engineering accommodation rather than a language property.

## Limits

The chapter is a vendor strategy statement about a mature runtime with
annual-ish major releases, not a formal contract; "strive to remain as
compatible as possible, even in cases where we give no compatibility
guarantees" is explicit about this. Its release-counting promises
(two releases) presuppose OTP's release cadence and have no Catena
counterpart. NIF, driver, and distribution mechanics are target
machinery whose Catena analogues, if any, belong to P093/G094/G095 and
G091/G092.

## Derived work

- [Catena API and ABI Compatibility](../20-notes/catena-api-and-abi-compatibility.md)
- [How Should Catena Define API and ABI Compatibility?](../40-inquiries/how-should-catena-define-api-and-abi-compatibility.md)
- [API and ABI Compatibility map](../10-maps/api-and-abi-compatibility.md)
