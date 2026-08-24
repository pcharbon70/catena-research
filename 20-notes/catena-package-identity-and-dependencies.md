---
title: "Catena Package Identity and Dependencies"
kind: note
created: "2026-08-24"
maturity: developing
tags:
  - catena
  - language-design
  - packages
  - versioning
aliases:
  - "Catena package model"
---

# Catena Package Identity and Dependencies

## Executive conclusion

A Catena package declares its dependencies in the manifest it already
has: an optional `dependencies` object mapping a package name to a
requirement string, with absence meaning dependency-free. Versions are
SemVer 2.0.0 — grammar and precedence vendored exactly, pre-release and
build metadata parsed, build excluded from ordering. Requirements are
three forms only: an exact pin (`1.2.3`), caret (`^`, admitting the
compatibility window with the Cargo-style 0.x rule so `^0.1.2` admits
`0.1.x` but not `0.2`), and tilde (`~`, admitting the same patch line).

Resolution fixes one version per package name per build: the highest
version satisfying every requirement in the graph, computed
order-independently; an empty intersection is static invalidity naming
every conflicting requirer and its requirement. A generated,
never-hand-edited `catena.lock` records each resolved package's exact
version, admitting requirement, requirers, SHA-256 bundle digest, member
interface digests, component joint digests, and the resolved selections;
a present matching lockfile replays as exact pins without re-resolution,
and regeneration from identical inputs is byte-identical. Package
identity is (name, version, SHA-256 bundle digest) computed over
canonical JCS of the manifest's semantic fields plus member interface
digests plus C024 joint digests — registry-neutral, so identical content
has identical identity, with hex.pm recorded as the bootstrap transport
profile whose tarball checksum must equal the bundle digest. Re-exports
stay excluded and are re-owned by the G028 compatibility era.

The executable deliverable is a library engine — vendored SemVer,
requirement satisfaction, the resolver, lockfile generation and replay,
and bundle digests — with no CLI, since G121 owns build tools.

This closes G025 without deciding G121 build and fetch tooling, G130
supply-chain signing and threat modeling, G028 compatibility and
re-export facades, G026 prelude contents, or G027 entry points.

## Scope and method

The operational target is independent agreement on the declaration form,
the version grammar and operators, conflict resolution, the lockfile,
identity and integrity, and the transport profile — made executable as a
pure dependency engine over a provided package environment. Primary
comparative evidence comes from the
[SemVer 2.0.0 grammar and precedence](../30-sources/preston-werner-2013-semantic-versioning.md)
and
[Hex version requirements](../30-sources/hex-project-2026-packages.md),
with the [Hex publishing hypothesis](../00-inbox/package-publishing-hypothesis-hex.md)
supplying the registry direction and Elixir's own `Version`/`Mix`
ecosystem as the working precedent. Source claims stay distinct from
Catena proposals below.

## Relation to the current corpus

[The C008 manifest](../60-specification/editions-and-feature-lifecycle/edition-selection-and-applicability.md)
already fixes what a package *is* selection-wise: `edition`,
`language_revision`, `previews`, modules, interfaces, roots, output. The
`dependencies` field extends that record without touching its selection
semantics, and dependency manifests still do not inherit a consumer's
selection — each package builds under its own recorded revision.

[C024 components](../60-specification/module-dependency-cycles/scc-admission-and-resolution.md)
produce joint digests that the lockfile now records, making a component's
cache identity part of the package's reproducible build. [C006
canonicalization](../60-specification/specifications-and-governance/claims-examples-and-checking.md)
supplies strict JCS and SHA-256 — the same machinery, applied to package
semantic fields rather than governance payloads. The
[compiler's manifest decoder and linker](../language-overview.md) already
validate and build multi-module packages; both extend.

C010's nominal identity (`origin::module::name`) is the deep reason
resolution must pick one version per name: two live versions of one
package would duplicate every type origin unless origins carried versions,
which no slice supports.

## Comparative evidence and inference

### SemVer: the grammar is given; the operators are not

SemVer 2.0.0's sections 9–11 are a complete, unambiguous version grammar
and precedence — including the subtle rules (pre-release below release,
numeric identifiers below alphanumeric, longer identifier lists above
shorter prefixes, build ignored). Catena vendors it exactly. But the
specification deliberately defines no requirement syntax, and ecosystems
diverge exactly where versions are most fragile: the pre-1.0 window.
Catena's caret follows Cargo (`^0.1.2` = `>=0.1.2 <0.2.0`) rather than
any other rule, recorded as a choice.

### Hex: the transport profile and the pre-release default

Hex's `~>` supplies the pessimistic upper bound Catena spells `~`, and —
the valuable precedent — Hex sets `:allow_pre` false: pre-releases match
only requirements that name pre-releases. Catena adopts that default: a
`^1.2.3` requirement never silently admits `1.3.0-rc.1`. The registry
itself (names, tarballs, outer checksums) is transport, and the inbox
hypothesis already directs Catena there; identity itself stays
registry-neutral so a second registry changes nothing.

### Why not npm-style side-by-side

npm permits multiple versions of one package in a build by namespacing
installs per requirer. On the BEAM there is no such namespacing: modules
load into one namespace, and Catena's type identities would fork. The
one-version rule is target-mandated, not taste.

## Selected model

### Declaration

`dependencies` is an optional manifest object; each key is a package
name (ASCII lowercase-initial word, hyphen-separated segments — the
ecosystem convention), each value one requirement string. Absence of the
field means the package is dependency-free. The field is advisory to the
compiler's per-package checking — resolution happens before compilation
— so it changes no accepted module input.

### Grammar

> **Normative definition (to be placed in the candidate chapter).**

```text
version     = major "." minor "." patch [ "-" pre ] [ "+" build ] ;
requirement = exact | caret | tilde ;
exact       = version ;
caret       = "^" version ;
tilde       = "~" version ;
```

Precedence is SemVer's, with build metadata excluded. A requirement's
operand must be a full `x.y.z` version (pre-release allowed, build not).

### Satisfaction

- exact `v`: the version equals `v` ignoring build metadata.
- `^x.y.z` where `x > 0`: `>=x.y.z` and `< (x+1).0.0`.
- `^0.y.z` where `y > 0`: `>=0.y.z` and `< 0.(y+1).0`.
- `^0.0.z`: `>=0.0.z` and `< 0.0.(z+1)`.
- `~x.y.z`: `>=x.y.z` and `< x.(y+1).0`.
- A pre-release version satisfies a requirement only if the operand
  itself is a pre-release on the same `[major.minor.patch]` triple.

### Resolution

The resolver takes a root manifest and a package environment (name →
available versions with metadata) and walks the graph breadth-first,
gathering every requirement per name. For each name the resolved version
is the highest available version satisfying *all* gathered requirements;
if none exists, `PKG` conflict invalidity listing each requirer and its
requirement. Cycles in the package graph (distinct from C024 *module*
cycles) are rejected — package dependencies form a DAG; a package cannot
transitively depend on itself. The result is order-independent: any
permutation of the environment or traversal yields identical resolution.

### Lockfile

`catena.lock` is generated JCS JSON: per package — name, exact resolved
version, the requirement that admitted it, requirers, bundle digest,
member interface digests, component joint digests — plus the resolved
edition/revision selections. Replay: a lockfile whose recorded versions
all satisfy the manifest's requirements is an exact-pin resolution, used
without re-resolution; any mismatch between lockfile and manifest is
`PKG` invalidity (re-lock), and a failed digest check is tamper
`PKG` invalidity. Regeneration from the same environment and manifest is
byte-identical.

### Identity

`bundle_digest = SHA-256(JCS({manifest semantic fields, sorted member
interface digests, sorted component joint digests}))`. Package identity
is the triple (name, version, bundle digest). hex.pm publishing profiles
this identity: the tarball checksum recorded at install must equal the
bundle digest of the canonical content.

### Re-exports

Excluded, with C022's deferral note updated to point at the G028
compatibility era rather than G025. A facade's digest chain (does the
facade's interface bind its own surface or the forwarded one?) is a
compatibility-policy question that era will own.

## Rejected alternatives

- **Separate deps file:** two synchronized records with no tooling need.
- **Exact pins only:** no intersection semantics, weakening the conflict
  clause.
- **Full Hex operator set:** bigger grammar, no corpus request.
- **Side-by-side versions:** forks nominal identity; no BEAM namespacing.
- **First-found resolution:** order-dependent — violates determinism.
- **No lockfile:** no reproducibility anchor; fails two checklist
  clauses.
- **Tarball-checksum identity:** transport-coupled; rebuild-sensitivity.
- **Signed lockfile now:** duplicates C006 without its lifecycle; G130
  owns the threat model.
- **Minimal re-export form now:** drags facade digest-chain semantics
  into this slice.
- **Normative-only delivery:** the archive's rejected pattern.

## What C025 adds to the design

Multi-package Catena programs become declarable, resolvable, and
reproducible: G121 gets a specification-backed engine to build tooling
on, G128 gets its reproducibility anchor, G130 gets registry-neutral
integrity to protect, and the Hex hypothesis becomes a recorded profile
rather than an inbox wish.

## Remaining questions and falsification criteria

G121 must build fetch/lock commands on this engine; G128 must consume
bundle digests for reproducible builds; G130 must layer signing and
threat analysis; G028 must eventually design re-export facades and
version-skew compatibility; G027 selects entry modules from resolved
packages.

The model should be revisited if the ecosystem demonstrates pre-1.0
caret pain (the rule is a recorded choice, changeable by revision), if
Hex's checksum model proves incompatible with canonical bundle digests
in practice, or if G028's compatibility work requires identity beyond
(name, version, digest).

## Connections

- The [open package inquiry](../40-inquiries/how-should-catena-define-package-identity-and-dependency-resolution.md)
  records the operational question and evidence trail.
- The [Package Identity and Dependencies map](../10-maps/package-identity-and-dependencies.md)
  routes through grammar, resolution, lockfile, and identity evidence.
- [Language Editions and Feature Lifecycle](language-editions-and-feature-lifecycle.md)
  fixes the manifest the dependencies field extends.
- [Catena Dependency Cycles](catena-dependency-cycles.md) fixes the
  component joint digests the lockfile records.

## Sources

- [Semantic Versioning 2.0.0](../30-sources/preston-werner-2013-semantic-versioning.md)
- [Hex Package Manager: Packages and Requirements](../30-sources/hex-project-2026-packages.md)
- [Package Publishing Hypothesis: Hex Registry](../00-inbox/package-publishing-hypothesis-hex.md)
