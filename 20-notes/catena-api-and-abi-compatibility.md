---
title: "Catena API and ABI Compatibility"
kind: note
created: "2026-08-24"
maturity: developing
tags:
  - catena
  - language-design
  - compatibility
  - api
  - abi
  - packages
aliases:
  - "Catena compatibility model"
---

# Catena API and ABI Compatibility

## Executive conclusion

Catena's compatibility contract at `0.1.24` is layered, interface-
centered, and honest about what it refuses. Two layers carry real
rules: **source compatibility** (a source file that checked under a
retained revision keeps checking under that exact revision — revisions
are immutable, acceptance is cumulative-forward, and every semantic
change since C013 has been a compatible addition per C008's registry)
and **type/interface compatibility** (a consumer validates against a
producer's later interface iff no breaking change occurred, decided by
a strict diff matrix). Two layers are principled declared absences:
**behavior** — the deterministic kernel *is* the behavior contract;
there is no separate behavioral-compatibility promise and no
bug-compatibility (OTP's own "we will not be bug-compatible" is the
precedent) — and **BEAM ABI** — representation is not a compatibility
surface (C023 maintained); companion binaries are deterministic
outputs; any future layout-stability contract belongs to a later era
with named owners.

Version meanings: at 1.0+, a breaking interface change requires a
SemVer **major** increment; below 1.0, the Cargo-style rule C025
already fixed for operators applies — **minor** signals breaking,
patch is additive-only. Edition bumps (0.1 → 0.2) are the
language-level breaking-change instrument through C008 lifecycle
records. Nothing about a representation change, a recomputation of a
digest, or a rebuild requires any bump by itself.

The strict matrix: removing or renaming any export, type constructor,
trait, handler, or instance; any signature change; and widening an
exported effect row (new requests) are breaking. Additions of any of
these are minor-compatible. Entry additions are minor; entry removals
and result-type changes are breaking. Prelude and dependency
requirement bumps are ordinary version bumps classified by the same
matrix. Re-export facades close as a formal exclusion — a forwarding
definition is already expressible and transparent; anything
identity-preserving enters only through a future lifecycle record.

The executable deliverable is `Catena.Package.Compat`: `diff/2`
classifies old-vs-new decoded interfaces into breaking/minor/patch
with itemized reasons, and `validate_claim/3` checks a claimed bump
against the actual classification (`CMP001` under-bump, `CMP002`
malformed shapes, `CMP003` unclassifiable drift).

## Scope and method

The operational target is independent agreement on the four layers'
stances, the major-version meaning, the breaking matrix, the
facade/digest/entry/prelude deferral resolutions, and the deliverable.
Primary comparative evidence is the [OTP compatibility
strategy](../30-sources/erlang-otp-compatibility-and-upgrading.md)
(the target runtime's tiered promises and refusals), over the shipped
C002 transparent/abstract interfaces, C008 lifecycle classification,
C023 representation exclusions, C024 joint digests, C025 SemVer and
lockfile machinery, C026 prelude bumps, and C027 entry sets. Source
claims stay distinct from Catena proposals below.

## Relation to the current corpus

[C008's lifecycle model](../60-specification/editions-and-feature-lifecycle/feature-lifecycle-and-compatibility.md)
already classifies every language change by affected dimension
(source acceptance, static meaning, dynamic behavior, diagnostics,
interfaces, artifacts) and its chapter explicitly says this "does not
finish G028's detailed public API/ABI rules." This slice is that
finishing, for the package-API side; edition mechanics remain C008's.

[C002's interfaces](../60-specification/data-and-patterns/interfaces-and-representation.md)
are the layer the matrix lives in: digest-verified, deterministic,
carrying exports with schemes and effect rows, nominal type
identities, traits, handlers, and instances. Cross-package
interoperation already happens only through them.

[C023's exclusions](../60-specification/abstraction-boundaries/authority-and-representation-exclusions.md)
pre-decided the ABI layer: "a future layout-stability or ABI contract
— any rule under which a representation choice becomes a compatibility
surface — is owned by G028." This slice's answer is *not yet*: the
exclusion converts from "undecided owner" to "decided absence with
named future consumers" (P093 representation, G094 calling
convention, G095 foreign terms, G092 hot upgrade).

[C024's joint digests](../60-specification/module-dependency-cycles/scc-admission-and-resolution.md)
and [C025's bundle digests and lockfile](../60-specification/package-identity-and-dependencies/resolution-and-lockfile.md)
are identity and cache keys, not compatibility surfaces: a digest
change says "something differs," never "this is breaking." Version
skew — consumers on different producer versions — is resolved by
C025's single-version-per-name resolution and exact-pin replay, which
this slice inherits without modification.

## Comparative evidence and inference

### OTP: tiered promises, honest refusals

The [OTP strategy](../30-sources/erlang-otp-compatibility-and-upgrading.md)
assigns different compat handling per surface — distribution two
releases each way, compiled code two forward and never back, APIs
stable, warnings addable, CLI and build tooling free — and expressly
declines bug-compatibility with patch-level escape hatches for
security and bug fixes. Three inferences for Catena: first, tiering is
the honest shape (a uniform "everything is compatible" promise is a
fiction even a 30-year runtime declines); second, declining
bug-compatibility is respectable *because* the deterministic semantics
is the contract — Catena's kernel makes this stronger, not weaker;
third, announced-in-advance deprecation with compiler warnings before
the change is the process C008 lifecycle records already give Catena
in identifier form. The one OTP promise Catena declines is binary
compatibility: OTP's own never-backward asymmetry shows it is an
engineering accommodation of a mature runtime, not a language
property, and 0.x Catena has no binary consumers to honor.

### Why additions-only-below-major is right even in 0.x

Catena's nominal identities embed *origin*, not version
(C002/C025), and two simultaneously-present versions of one package
would fork every type identity. That is why resolution is
single-version-per-name: there is no side-by-side coexistence in which
"breaking but tolerable" could live. A breaking change therefore must
be *visible in the version number* — minor-as-breaking under Cargo's
0.x convention (already fixed by C025's operators), major at 1.0+. The
alternative — trusting that no consumer ever pins both versions — is
exactly the ambiguity SemVer 0.x exists to remove.

### Why effect-row widening is breaking

A consumer of `f : a -> b handles {}` that itself handles nothing
cannot type-check against `f : a -> b handles {Ask}` — the producer
now issues requests the consumer never agreed to answer. Narrowing is
the mirror image and is minor-compatible: a producer that handles more
imposes nothing on consumers. This asymmetry follows directly from
C005's row semantics and C010's completion rule, and it is why the
matrix keys on rows, not on the `uses` annotation's surface form.

## Selected model

> **Normative definitions (placed in the candidate chapters).**

### Layers

| Layer | Stance |
| --- | --- |
| Source | Retained revisions are immutable; a file that checked keeps checking under its exact revision; acceptance is cumulative-forward per C008 |
| Type/interface | Real rules: the strict diff matrix over decoded interfaces |
| Behavior | Declared absence: the kernel is the contract; no bug-compatibility |
| BEAM ABI | Declared absence: representation is not a surface; binaries are deterministic outputs |

### Breaking matrix (interface diff)

| Change | Class |
| --- | --- |
| Remove or rename an export, type constructor, trait, handler, or instance | breaking |
| Change any export's scheme | breaking |
| Widen an export's effect row | breaking |
| Narrow an export's effect row | minor |
| Add an export, type constructor, trait, handler, or instance | minor |
| Change representation/layout of any type | never breaking alone |
| Add an entry | minor |
| Remove an entry or change its result type | breaking |
| Prelude/dependency requirement bump | classified by the target version under this matrix |
| Joint or bundle digest change | identity only — no class |

### Claim validation

`validate_claim(old_interface, new_interface, claimed)` returns the
classification, or `CMP001` when the actual class exceeds the claim's
allowance (breaking under a minor/patch claim; minor under a patch
claim), `CMP002` for malformed shapes, `CMP003` for drift the matrix
cannot classify. Under 0.x the Cargo rule applies to the claim; at
1.0+ SemVer proper.

### Rejected alternatives

- **Behavioral contract** — unenforceable; the kernel already is the
  contract.
- **Minimal ABI now** — the runtime era hasn't designed its
  boundaries; contradicts C023's deliberate exclusion.
- **New versioning scheme** — contradicts C025 SemVer and Hex.
- **Removals-only breaking** — silent signature drift is what
  digest-verified interfaces exist to catch.
- **Manifest facade mechanism** — no consumer demand; contradicts C002
  transparency and C021 collisions.
- **Instance additions breaking** — punishes safe evolution.
- **Normative-only deliverable** — the archive's rejected pattern.

## What C028 adds to the design

Section 3 — names, modules, packages, separate compilation — is
*complete*: the last outstanding item closes. Package authors gain a
checkable rule for what their version numbers must say (the claim
validator is the executable form); G121's tooling gains a lintable
gate for release automation; G101+ gains the semantics prelude bumps
must obey; G116/P125 migration engines gain the classification input
they will consume; and the G092/G094/G095 consumers gain a named
predecessor that says exactly what they may build on.

## Remaining questions and falsification criteria

G116/P125 own migration engines; G130 owns registry retirement, yanks,
and compromised versions; G092 owns hot upgrade; P093/G094/G095 own
representation, calling-convention, and foreign-term contracts; G121
owns tooling defaults; G136 owns the long-term edition policy that
succeeds the 0.x convention.

The model should be revisited if the 1.0 era shows the Cargo 0.x
rule confusing for the ecosystem (the remedy is the C008 edition
record that names the switch, not silent reinterpretation), or if
binary consumers emerge and demand a layout-stability contract (the
remedy is a new slice with P093/G094 as co-designers, not amending
the absence).

## Connections

- The [resolved compatibility inquiry](../40-inquiries/how-should-catena-define-api-and-abi-compatibility.md)
  records the question, hypotheses, and outcome.
- The [API and ABI Compatibility map](../10-maps/api-and-abi-compatibility.md)
  routes through the OTP precedent, the shipped contracts, and the
  future owners.
- The API and ABI Compatibility Specification (candidate, then
  normative at promotion, in `60-specification/api-and-abi-compatibility/`)
  will define the contract this note argues for.
- [Catena Package Identity and Dependencies](catena-package-identity-and-dependencies.md)
  fixes the SemVer machinery whose meaning side this slice completes.
- [Catena Abstraction Boundaries](catena-abstraction-boundaries.md)
  fixed the representation exclusions this slice converts to decided
  absence.
- [Catena Entry Points](catena-entry-points.md) fixed the entry sets
  this matrix classifies.

## Sources

- [Erlang/OTP Support, Compatibility, Deprecations, and Removal](../30-sources/erlang-otp-compatibility-and-upgrading.md)
- [Semantic Versioning](../30-sources/preston-werner-2013-semantic-versioning.md)
- [Hex packages](../30-sources/hex-project-2026-packages.md)
- [Feature Lifecycle and Compatibility](../60-specification/editions-and-feature-lifecycle/feature-lifecycle-and-compatibility.md)
- [Authority and Representation Exclusions](../60-specification/abstraction-boundaries/authority-and-representation-exclusions.md)
- [Resolution and Lockfile](../60-specification/package-identity-and-dependencies/resolution-and-lockfile.md)
