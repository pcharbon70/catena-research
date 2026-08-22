---
title: "Catena Imports and Exports"
kind: note
created: "2026-08-22"
maturity: developing
tags:
  - catena
  - imports
  - exports
  - language-design
  - modules
aliases:
  - "Catena import model"
---

# Catena Imports and Exports

## Executive conclusion

Catena modules should export nothing by default: an explicit export
declaration — carrying a category, a spelling, and for types C002's
transparent or abstract mode — is the only way a name reaches another
module. An import admits the named module for two-segment qualification
against its digest-bound export set, plus one explicit possibly-empty list
of exported names admitted unqualified; the empty list is qualified-only
access. There are no wildcards, no renaming, and no re-exports in 0.1.18 —
each exclusion is declared, with re-exports owned by package assembly
under G025.

Importing a name outside the export set, or an unknown module, is static
invalidity. Duplicate exports fall under C021's `NSP001`. Unused admitted
names and wholly unused imports produce a deny-able `IMP001` warning over
the C021 environment, not an error.

The executable deliverable extends the C021 abstract resolver: export and
import events feed the environment, qualification is
visibility-filtered, and a separate analysis operation reports unused
imports. Testable before P109's declaration grammar exists.

This closes G022 without deciding G024 module cycles, G025 package
identity and re-export assembly, G026 prelude contents, G027 entry
modules, or P109 surface punctuation.

## Scope and method

The operational target is independent agreement on export admission and
visibility defaults, import admission shapes, export-set validation,
unused-import diagnostics, and every failure class. Primary comparative
evidence comes from the expanded
[Haskell 2010 chapter 5 findings](../30-sources/marlow-2010-haskell-language-report.md),
with the [SML](../30-sources/milner-et-al-1997-definition-standard-ml.md)
signature model, [Erlang](../30-sources/erlang-otp-modules-and-code-loading.md)
qualification-only contrast, and [Rust](../30-sources/rust-project-2026-crates-and-modules.md)
re-export evidence framing the declined alternatives. Source claims stay
distinct from Catena proposals below.

## Relation to the current corpus

The [C010 kernel](../60-specification/formal-semantic-kernel/canonical-kernel-syntax.md)
fixes the bounded precedent: `(export value ...)`, `(export type ...)`,
`(export process ...)` declarations, and `(import ModuleName
"interface-digest")` that "imports public process-entry evidence, not
unqualified values or wildcard namespaces". C022 generalizes the export
forms to every program category and adds the one surface the kernel
deferred — the explicit unqualified name list — without amending the
digest binding, which stays C006/C008 property consumed opaquely here.

[C002 interfaces](../60-specification/data-and-patterns/interfaces-and-representation.md)
already define transparent constructor export versus fully abstract type
export; the export event's transparency mode names that choice rather
than re-specifying it. [C021](../60-specification/namespaces-and-shadowing/README.md)
fixes local-over-imported precedence and reference-time `NSP004`
ambiguity; imports only feed more origins into that fixed model.
[C020](../60-specification/files-and-modules/README.md) fixes flat
uppercase-initial module names, which is what qualification names. The
[warning machinery](../60-specification/editions-and-feature-lifecycle/README.md)
already supports deny-able warning identities (`DEP001`, `EDN002`,
`IDN007`); `IMP001` joins that set.

## Comparative evidence and inference

### Haskell: the explicit-list machinery, adopted and declined

Haskell's chapter 5 supplies almost the whole design space. Adopted:
explicit import lists that must name only exported entities; the empty
list `import A()` that admits nothing unqualified while `A.x` remains
usable — exactly Catena's qualified-only admission; qualification
available from every import; cumulative, order-independent imports; and
clashes that err only when the ambiguous name is mentioned, matching
C021's reference-time rejection. Declined: `hiding(...)` (a second way to
spell every import), `as` aliases (a second way to spell every module),
`module M` re-exports (package assembly, G025), public-by-default exports
(Catena keeps the kernel's explicit-only exports), and the implicit
Prelude (G026 will design an origin, not a silent default).

### Standard ML: signatures as the deep model

SML controls exports through signatures matched against structures — the
surface a module presents is itself a named, checkable artifact. Catena's
digest-bound export set is the same idea with the interface as the
artifact (`.cati.json` under C008): the export declaration fills the
interface, the digest pins it, and the import validates against it. SML's
`open` — dumping a structure's exports unqualified into scope — is the
wildcard Catena declines.

### Erlang and Rust: the extremes

Erlang imports nothing and qualifies everything: maximal explicitness at
a constant call-site tax. Rust's `pub use` makes re-exporting routine,
which is precisely why Catena defers re-exports to G025 where a package's
public surface over its dependencies can be designed once, with the Hex
publishing hypothesis as context, instead of growing organically per
module.

## Selected model

### Exports

An export declaration event carries a category, a spelling, and — for the
`types` category — a transparency mode, `transparent` or `abstract`,
naming C002's contract. Only declared names are exported; every other
module-level declaration is private. An export naming a name the module
does not declare is `EXP001`. Two export declarations of one spelling in
one category are C021 `NSP001` duplicates. The exported set plus its
digest is the module's interface identity under C008; this layer consumes
the digest opaquely and adds no verification rule.

### Imports

An import declaration event carries a module name, its interface digest,
and an explicit possibly-empty list of (category, spelling) pairs. The
effect is fixed:

- the module is admitted for two-segment qualification against its
  export set — every exported name resolves as `Module.member`;
- each listed name is admitted unqualified into its category, joining
  C021's import origins under local-over-imported precedence and
  reference-time `NSP004`;
- a listed name absent from the export set is `IMP002`; an unknown
  module is `IMP003`;
- importing one name twice from one module is a duplicate `NSP001`;
- importing the same module through two imports is cumulative and
  order-independent, per the Haskell precedent.

No wildcard, `hiding`, renaming, alias, or re-export form exists in
0.1.18; each is a declared exclusion with its future owner named.

### Unused imports

An analysis over the built environment and the reference set reports:
each admitted unqualified name never referenced in its category
(`IMP001`, naming module and name), and each imported module with
neither a qualified nor any unqualified use (`IMP001`, naming the
module). `IMP001` is a warning — deny-able through the existing
`validate_denied_diagnostics` machinery — never an error, and never a
resolution failure. Prose quality remains P117's.

### Abstract public boundary

The C021 environment builder consumes the new events: export events
record visibility; import events validate against known export sets and
admit names. A new `check_unused_imports` operation takes the
environment plus the referenced (category, spelling, qualified) set and
returns warnings only — never errors. Neither operation parses source;
P109's grammar will emit the events.

## Rejected alternatives

- **Public-by-default exports (Haskell omitted list):** leaks internals
  by accident and bloats every interface digest.
- **Unqualified-everything imports (Haskell omitted spec):** maximizes
  `NSP004` pressure and contradicts the kernel's explicit admission.
- **Qualification-only imports (Erlang):** constant call-site tax; the
  explicit list gives opt-in short names safely.
- **Wildcards and `hiding` (Haskell/SML `open`):** two more ways to spell
  every boundary; collisions become surprises rather than decisions.
- **Renaming and aliases:** a second spelling for every name, before any
  demonstrated need; collisions already resolve by qualification.
- **Re-exports now (Rust `pub use`):** forces digest-chain and package
  identity design into this slice; G025 owns it.
- **Unused imports as errors:** hostile to development order and unlike
  every surveyed language.

## What C022 adds to the design

Module boundaries become real: a `.cati.json` interface reflects exactly
what modules declare, imports are validated against digest-bound export
sets before name resolution runs, and unused dependencies surface as
deniable warnings. P109 receives the semantic shape its `use`/`export`
surface must elaborate; G025 receives single-module boundaries to
assemble into packages; G026 receives the origin model a prelude must
follow.

## Remaining questions and falsification criteria

G024 must decide module recursion over these admission rules; G025 must
design package identity, re-export assembly, and duplicate-module
rejection; G026 must design the prelude as an import origin with opt-out;
G027 must select entry modules; P109 must fix the concrete `use`/`export`
punctuation; P117 owns `IMP001` prose quality.

The model should be revisited if G025's package assembly requires
re-export identity this slice cannot carry, if G026's prelude cannot be
expressed as one more origin, or if real code shows the explicit list's
verbosity materially harms development — the remedy would be a later
revision adding one form, not reopening admission semantics.

## Connections

- The [open import inquiry](../40-inquiries/how-should-catena-handle-imports-and-exports.md)
  records the operational question and evidence trail.
- The [Imports and Exports map](../10-maps/imports-and-exports.md) routes
  through evidence, constraints, and remaining owners.
- [Catena Namespaces and Shadowing](catena-namespaces-and-shadowing.md)
  fixes the precedence and collision rules imports feed.
- [Catena Files and Modules](catena-files-and-modules.md) fixes the flat
  module names imports name.

## Sources

- [Haskell 2010 Language Report](../30-sources/marlow-2010-haskell-language-report.md)
- [The Definition of Standard ML (Revised)](../30-sources/milner-et-al-1997-definition-standard-ml.md)
- [Erlang/OTP Modules and Code Loading](../30-sources/erlang-otp-modules-and-code-loading.md)
- [The Rust Reference: Crates and Modules](../30-sources/rust-project-2026-crates-and-modules.md)
