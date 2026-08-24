---
title: "Catena Prelude Policy"
kind: note
created: "2026-08-24"
maturity: developing
tags:
  - catena
  - language-design
  - prelude
  - packages
aliases:
  - "Catena prelude model"
---

# Catena Prelude Policy

## Executive conclusion

A Catena package selects a prelude explicitly in its manifest: an
optional `prelude` field naming one package and one requirement. When
present, that package's exports enter scope as an ordinary import-class
origin — locals still win, and a prelude name colliding with another
import's name unqualified rejects as `NSP004` with both origins named
until qualified, exactly as C021 promised. When the field is absent or
`null`, no prelude origin exists at all: that is the whole of opt-out.
No sentinel spelling, no per-name hiding, no weaker or stronger
precedence tier.

Edition 0.1's guarantee is precise and negative: **no name is ever
implicitly in scope.** Every in-scope name comes from a local
declaration, an explicit import, or an explicitly selected prelude. Any
future edition that names a default prelude does so through a lifecycle
record under C008 — never silently. A prelude package is any valid C025
package — resolved, digest-bound, and lock-pinned like any dependency,
including one with zero exports — so G101 freezes contents on this
mechanism instead of inventing one.

The executable deliverable wires three shipped pieces: the manifest
decoder gains the optional `prelude` object; the environment builder
(extended to 0.1.22) injects the named origin at import precedence; and
`Catena.Package.Deps` resolves and locks the prelude selection as an
ordinary dependency with a marked requirer.

This closes G026 without deciding G101's contents, P102's collection
protocols, G121's tooling defaults, G027's entry points, or G028's
compatibility meanings of prelude version bumps.

## Scope and method

The operational target is independent agreement on selection, precedence,
opt-out, the edition guarantee, diagnostics, and lockfile treatment —
made executable through the manifest field, the builder origin, and
dependency resolution. Primary comparative evidence is the expanded
[Haskell Prelude findings](../30-sources/marlow-2010-haskell-language-report.md)
(the fully-specified declined model), over the shipped C021/C022/C025
contracts and the C010 kernel's explicitness stance. Source claims stay
distinct from Catena proposals below.

## Relation to the current corpus

[C021's shadowing chapter](../60-specification/namespaces-and-shadowing/shadowing-and-ambiguity.md)
pre-commits the design: precedence is local > imports with
reference-time `NSP004` rejection naming all origins, and "a future
prelude origin follows import precedence under G026 and is never a
silent default." Executing that sentence is this slice's core; nothing
in the precedence model changes.

[C022's import admission](../60-specification/imports-and-exports/import-declarations-and-admission.md)
fixes the origin class — digest-bound or signature-resolved, export-set
validated, listed unqualified admission — and its synthesis explicitly
declined Haskell's implicit Prelude. The prelude origin is an ordinary
member of that class, differentiated only by being named in the
manifest rather than an import event.

[C025's package machinery](../60-specification/package-identity-and-dependencies/resolution-and-lockfile.md)
supplies everything a prelude needs to be real: a name, a SemVer
requirement, resolution into an environment, a bundle digest, and a
lockfile pin. The `dependencies` field is the shape precedent — an
optional manifest object, validated at decode, backward-compatible.

The [C010 kernel](../60-specification/formal-semantic-kernel/canonical-kernel-syntax.md)
admits only explicit digest-backed imports — the deepest precedent that
nothing enters scope unannounced.

## Comparative evidence and inference

### Haskell: the complete alternative, priced

Haskell's sections 5.6–5.6.2 specify automatic-unless-explicit Prelude
admission, `import Prelude()` exclusion, per-name `hiding`, and a
semantics-frozen core that special syntax bypasses regardless of
imports. Three costs are visible in the report itself: every module that
redefines a Prelude name with `hiding` transfers the disambiguation duty
to all importers; the empty-import exclusion is a special case rather
than an ordinary selection; and the frozen core makes the Prelude part
of the language definition rather than a library. Catena's inference:
opt-in selection plus ordinary qualification achieves the ergonomics
without any of the three, and a prelude as an ordinary versioned package
keeps library and language axes separate — exactly the separation C008
and C025 already mandate.

### Rust: the shadowing tier, declined in advance

Rust's prelude sits below explicit imports — an explicit `use` silently
shadows a prelude name. C021's precedence table has no such tier, and
adding one would make an import silently change a prelude name's
meaning — the ambiguity Catena rejects everywhere else. The ordinary
origin keeps one rule.

### Why zero-implicit-names is the right 0.1 guarantee

The standard library does not exist yet, so any 0.1 "default prelude"
would be empty-by-fiat — a named artifact with no contents, edging
toward the silent default the corpus forswore. Guaranteeing zero
implicit names is truthful now, gives G101 a clean upgrade path
(introduce contents + a lifecycle record naming a default, together),
and gives tooling (G121) a firm rule: no scaffold may inject scope.

## Selected model

### Selection

> **Normative definition (to be placed in the candidate chapter).**

```text
prelude = { "package": name, "requirement": requirement } ;
```

- One prelude per package. The field is optional; absent or `null`
  selects none.
- The name follows C025's package-name spelling; the requirement follows
  C025's exact/caret/tilde grammar; both validate at manifest decode,
  with malformed shapes rejected as `PRE001`.
- An unknown prelude package in the environment rejects as `PKG004`; an
  unsatisfiable requirement rejects as `PKG003` — the C025 families,
  unchanged.

### Admission and precedence

When the prelude selection resolves, the prelude package's export set
enters the resolution context as an origin in the import class. The
precedence table from C021 executes verbatim:

1. a local binding wins;
2. otherwise, a prelude name and an explicitly imported name colliding
   unqualified reject as `NSP004`, naming both origins — resolution is
   by qualification;
3. prelude-vs-prelude cannot occur (one selection per package).

Opt-out is the absent/`null` field; no other exclusion mechanism
exists. A colliding name is resolved by qualifying either origin, the
same repair as every other collision in the language.

### The edition guarantee

Edition 0.1 guarantees: every in-scope name comes from a local
declaration, an explicit import, or an explicitly selected prelude; no
name is implicitly in scope. A future edition naming a default prelude
does so through a C008 lifecycle record that names the package,
requirement, and migration; it never enters silently. This guarantee is
upgrade-not-amend: freezing contents (G101) or naming a default (a
future edition record) adds to it without weakening it.

### Lockfile and identity

The prelude selection participates in dependency resolution as an
ordinary dependency whose requirer is recorded as the prelude marker
(`<prelude>`), is pinned in `catena.lock` with its exact version and
bundle digest, and replays as an exact pin. Lockfile bytes remain
deterministic; no separate prelude section exists in the lock.

### Rejected alternatives

- **Automatic-unless-explicit (Haskell):** contradicts C021's "never a
  silent default" and C022's declination; needs amending records.
- **Shadowing tier (Rust):** a second precedence class C021 doesn't
  define; silently changes meaning on import.
- **`none` sentinel:** two spellings for one state.
- **Per-name hiding:** reintroduces the C022-rejected mechanism and
  ambiguity transfer.
- **Empty default prelude in 0.1:** a named-but-empty artifact before
  G101; edges toward silent defaults.
- **Normative-only mechanism:** the archive's rejected pattern.
- **Tooling scaffold defaults (G121):** would blur the language/tooling
  line just drawn; a scaffold may pre-fill the field, never imply it.

## What C026 adds to the design

The standard-library program (G101+) gains its admission target, tooling
(G121) gains a firm zero-implicit-names rule, and the eight shipped
chapters' deferrals to G026 resolve into one mechanism. Most
importantly, the edition guarantee makes "what does a bare program see?"
a question with a permanent, checkable answer: nothing that was not
asked for.

## Remaining questions and falsification criteria

G101 must freeze contents and decide whether any future edition names a
default prelude through a lifecycle record; G121 may scaffold the field
but never imply selection; G028/G136 own the compatibility meanings of
prelude version bumps; P102 owns collection protocols the prelude may
re-export.

The model should be revisited if G101's usability evidence shows
opt-in-everywhere materially harms adoption (the remedy is an edition
record naming a default, not silent admission), or if lockfile
representation of prelude requirers proves ambiguous for tooling.

## Connections

- The [open prelude inquiry](../40-inquiries/how-should-catena-define-its-prelude-policy.md)
  records the operational question and evidence trail.
- The [Prelude Policy map](../10-maps/prelude-policy.md) routes through
  the Haskell model, the shipped contracts, and remaining owners.
- [Catena Namespaces and Shadowing](catena-namespaces-and-shadowing.md)
  fixes the precedence the prelude rides.
- [Catena Package Identity and Dependencies](catena-package-identity-and-dependencies.md)
  fixes the identity and lock machinery the prelude reuses.

## Sources

- [Haskell 2010 Language Report](../30-sources/marlow-2010-haskell-language-report.md)
- [Shadowing and Ambiguity](../60-specification/namespaces-and-shadowing/shadowing-and-ambiguity.md)
- [Import Declarations and Admission](../60-specification/imports-and-exports/import-declarations-and-admission.md)
- [Resolution and Lockfile](../60-specification/package-identity-and-dependencies/resolution-and-lockfile.md)
- [Canonical Kernel Syntax](../60-specification/formal-semantic-kernel/canonical-kernel-syntax.md)
