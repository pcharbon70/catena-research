---
title: "How Should Catena Handle Imports and Exports?"
kind: inquiry
created: "2026-08-22"
status: resolved
tags:
  - catena
  - imports
  - exports
  - language-design
  - modules
aliases:
  - "Catena import inquiry"
---

# How Should Catena Handle Imports and Exports?

## Why this matters

C021 fixed how names resolve once they are in scope, but nothing yet says
how names cross module boundaries: what an export admits, what an import
brings into scope, whether wildcards or renaming exist, and what happens
when an import is unused. Until those are fixed, independent
implementations could disagree about visibility defaults, about whether
`Json.Null` requires an import of `Json`, and about which names a
`.cati.json` interface may carry — disagreements that would leak into
P109's declaration grammar, G025's package assembly, and every
cross-module diagnostic.

The C010 kernel already legislated its bounded boundary: explicit
per-category `(export ...)` forms, digest-backed imports with no
wildcards, and qualified names for imported entries. G022 must generalize
that boundary to the whole language without amending C021's precedence
model or C002's abstraction contract.

## Operational question

Choose a bounded 0.1.18 boundary in which independent implementations agree
on:

- what an export declaration admits and the visibility default for
  undeclared names;
- what an import declaration brings into scope — qualification rights,
  unqualified admission, wildcards, renaming, and re-exports;
- which imports are valid against a module's digest-bound export set;
- how unused imports are diagnosed; and
- the failure classes and stable diagnostics of every rejection.

The answer must compose with C021's precedence and `NSP004` collision
rules, C002's transparent/abstract type export, C008's exact-revision
interfaces, and C020's flat module names without deciding module
cycles, G025 package identity and re-export assembly, G026 prelude
contents, G027 entry modules, or P109 surface punctuation.

## Working hypotheses

- Nothing is exported without an explicit export declaration: private by
  default, generalizing the kernel's export forms; type exports carry
  C002's transparent or abstract mode.
- An import admits the module for two-segment qualification against its
  digest-bound export set, plus an explicit possibly-empty name list
  admitting selected exported names unqualified; the empty list means
  qualified-only access.
- No wildcards, no renaming, no re-exports in 0.1.18 — each exclusion is
  declared, with re-exports deferred to G025 package assembly.
- Importing a name not in the export set, or a module that is not known,
  is static invalidity; duplicate exports reuse `NSP001`.
- Unused admitted names or wholly unused imports produce a deny-able
  `IMP001` warning, not an error.

## Paths to explore

- [Haskell 2010 import and export findings](../30-sources/marlow-2010-haskell-language-report.md)
  supply explicit import lists, the empty qualified-only form,
  always-available qualification, mention-time clash errors, and the
  declined `hiding`/alias/re-export machinery.
- [The SML Definition](../30-sources/milner-et-al-1997-definition-standard-ml.md)
  supplies signature-controlled export surfaces and the open/qualification
  split.
- [Erlang/OTP modules](../30-sources/erlang-otp-modules-and-code-loading.md)
  supply the import-nothing, qualify-everything contrast.
- [The Rust Reference](../30-sources/rust-project-2026-crates-and-modules.md)
  supplies `pub use` re-export evidence for the G025 deferral.
- The [C010 kernel](../60-specification/formal-semantic-kernel/canonical-kernel-syntax.md)
  fixes the explicit export and digest-backed import precedent;
  [C002 interfaces](../60-specification/data-and-patterns/interfaces-and-representation.md)
  fix transparency and abstraction; [C021](../60-specification/namespaces-and-shadowing/README.md)
  fixes precedence and collisions.

## Findings

- Haskell's empty import list `import A()` imports nothing unqualified
  while `A.x` qualification remains available — precisely Catena's
  qualified-only admission — and its mention-time clash errors match
  C021's reference-time `NSP004` exactly.
- Haskell's public-by-default exports (all local definitions when the
  list is omitted) and implicit Prelude are both models Catena declines
  in favor of the kernel's explicitness; its `hiding`, `as`, and
  `module M` re-export forms are the specific machinery the exclusions
  reject.
- The kernel's import form is already qualified-entry admission with
  digest binding; generalizing it needs only the explicit unqualified
  name list, which is the one surface the kernel deliberately deferred.
- The synthesis
  [Catena Imports and Exports](../20-notes/catena-imports-and-exports.md)
  develops the full model and falsification criteria; the
  [topic map](../10-maps/imports-and-exports.md) routes the evidence.

## Outcome

Resolved as C022 and source-only language revision `0.1.18`. Catena fixes
private-by-default explicit exports carrying C002 transparency modes with
`EXP001` undeclared rejection; import admission through two-segment
qualification against digest-bound export sets plus explicit
possibly-empty unqualified name lists with `IMP002`/`IMP003` validation;
the declared exclusion of wildcards, hiding, renaming, aliases, and
re-exports; and the deny-able `IMP001` unused-import warning whose
qualified references never satisfy unqualified admissions. The rules are
defined in the
[normative imports specification](../60-specification/imports-and-exports/README.md).

G022 is complete through the
[imports synthesis](../20-notes/catena-imports-and-exports.md),
[topic map](../10-maps/imports-and-exports.md), and
[C022 evidence record](../50-journal/2026-08-22-c022-imports-and-exports.md).
C024 has since admitted module recursion; G025 retains package identity and
re-export assembly; G026 retains prelude contents; G027 retains entry
modules; P109 retains the concrete `use`/`export` punctuation; P117
retains warning prose quality.
