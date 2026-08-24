---
title: "Feature Lifecycle and Compatibility"
kind: specification
created: "2026-08-05"
status: normative
spec_version: "0.1.7"
tags:
  - compatibility
  - language-design
  - migration
  - specification
aliases:
  - "Catena 0.1.7 preview lifecycle"
---

# Feature Lifecycle and Compatibility

## Lifecycle registry

Every language feature tracked by this slice has one immutable lowercase
kebab-case identifier. An entry records its state at revision boundaries, its
first available revision, governing specification headings, replacement when
present, and migration record. A withdrawn or removed identifier MUST NOT be
reused for another meaning.

The registry is finite, deterministically ordered, and exposed through the
language-information interface. Compiler-private flags are not language
features and MUST NOT appear as package previews.

## States and transitions

The only states are `preview`, `stable`, `withdrawn`, `deprecated`, and
`removed`.

> **Normative definition.**

```text
preview -> stable
preview -> withdrawn
stable -> deprecated
deprecated -> removed
```

No other ordinary transition is valid. Every transition occurs at one
published language revision, and state lookup uses the package's exact
selected revision. Repeated publication of the same state is not a
transition.

A preview is fully specified and implemented for its bounded contract but is
impermanent. Stable behavior belongs to the cumulative language without an
opt-in. Withdrawn means a preview did not become stable. Deprecated behavior
remains valid with a diagnostic. Removed behavior is invalid only at or after
its removal revision.

## Preview selection

A package enables previews by exact name in its manifest. Each name MUST be in
state `preview` at the package's selected revision. An unknown name, a preview
from another revision, a withdrawn name, or a removed name is `PRV001`.

A name that is already stable or deprecated is not a valid preview opt-in,
because those states are selected through the language revision. The
diagnostic SHOULD offer removal of the stale manifest entry when that edit is
semantics-preserving.

Version 0.1.7 publishes no feature in preview state. Its empty preview set is
intentional; implementations MUST NOT add vendor preview names to the Catena
registry.

## Deprecation and removal

Use of a deprecated feature emits `DEP001` and remains compilable by default.
A package diagnostic policy or an applicable governance policy MAY deny that
diagnostic, in which case the build fails before final outputs are committed.

Within edition 0.1, removal of a stable feature requires at least one earlier
published revision in which it was deprecated and migration guidance was
available. A direct `stable` to `removed` transition is the sole exception to
the ordinary state graph. It is valid only for an immediate soundness or
security removal with an explicit normative emergency record stating its
basis, affected rules, reason, exposure, replacement or containment, and
migration consequences. The compiler validates that record as part of the
immutable feature history.

After language revision 1.0.0, removal or incompatible reinterpretation of a
stable feature requires a major revision. Compatible stable additions use a
minor revision; compatible corrections use a patch revision. A minor revision
opens the matching `major.minor` edition while retained earlier editions remain
selectable.

## Compatibility dimensions

C008 classifies a revision change as `breaking`, `compatible-addition`, or
`compatible-correction` for the declared language contract. The change record
MUST identify which of source acceptance, static meaning, dynamic behavior,
diagnostics, interfaces, or artifacts is affected.

This classification does not finish the detailed public API/ABI rules; those are
subsequently fixed by C028. It
also does not make implementation performance, undocumented JSON ordering, or
temporary source punctuation part of the stable contract.

## Package-local interoperation

Packages from different retained editions MAY be dependencies of one build.
They interoperate only through decoded, digest-verified semantic interfaces.
The consumer MUST understand the interface schema, nominal identities, types,
effects, traits, claims, and required previews used by the producer.

A consumer missing any public required preview receives `PRV002`. A private
preview use that does not reach an exported signature, exported semantic
evidence, or inherited public obligation MUST NOT appear in the interface.

Edition selection is resolved at compile time. Generated runtime code MUST NOT
query an edition registry, dispatch on an edition, or require a preview runtime
flag. Different selections MAY produce different compile metadata and artifact
digests.

## Evidence route (non-normative)

The [JEP 12 source note](../../30-sources/buckley-2018-preview-features.md)
motivates explicit opt-in and artifact marking, while the
[Semantic Versioning source note](../../30-sources/preston-werner-2013-semantic-versioning.md)
supplies the post-1.0 numeric convention. Catena's named previews, public-use
propagation, and retained exact pins are local design choices.
