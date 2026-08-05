---
title: "Language Editions and Feature Lifecycle"
kind: note
created: "2026-08-05"
maturity: developing
tags:
  - compatibility
  - language-design
  - migration
  - specification
aliases:
  - "Catena edition model"
  - "Catena feature lifecycle"
---

# Language Editions and Feature Lifecycle

Catena needs version names that answer different questions without making a
programmer reverse-engineer compiler history. An edition says which language
compatibility track a package chose. A language revision fixes one exact point
on that track. An artifact version says how a persisted JSON object is
encoded. A compiler-package version says which implementation was installed.
Using one field for all four would make reproducibility, migration, and
signature verification ambiguous.

## Executive conclusion

The initial edition is `0.1`. C001 through C006 form cumulative revisions
`0.1.1` through `0.1.6`, and normative C008 defines `0.1.7`; C007 governs
document authority rather than adding a language revision. Every package
using the new manifest format states `edition`, exact `language_revision`, and
a list of named `previews`. The compiler continues to accept every published
stable revision rather than silently moving a package to later semantics.

The 0.1 edition is a prototype: its normative rules are real at each selected
revision, but a later 0.1 patch may contain a documented breaking change.
Temporary JSON frontend shapes and unsettled Catena source punctuation are not
promised as end-user source compatibility. After 1.0, revisions use the
ordinary Semantic Versioning meanings.

## The four identities

An edition is a `major.minor` compatibility track. It is selected per package,
so dependencies can move independently. A language revision is the exact
`major.minor.patch` semantic boundary. Its major and minor components must
match the selected edition. Exact pins prevent an installed compiler from
quietly changing the meaning of a build.

Artifact formats retain their existing `version` field. A 0.1.7 package
manifest, interface, assurance record, or language-information document has a
0.1.7 serialization contract even when it describes code pinned to an earlier
language revision. Compiler releases remain separately versioned because bug
fixes and implementation packaging do not themselves amend Catena.

This split also repairs applicability. A package at revision
`0.1.7` receives the cumulative stable rules introduced by C001 through C006
and C008. A later chapter does not win merely because its number is larger:
replacement or removal must appear in the lifecycle record. A conflict without
that relationship remains a specification defect.

## Package-local editions and interoperation

Edition choice belongs to the package rather than the dependency graph. A
consumer does not force all dependencies to migrate. Modules communicate
through normalized, layout-free semantic interfaces, and an importer checks
that it understands the interface format and every public preview requirement.
This takes the package-local interoperability lesson from the
[Rust Edition Guide](../30-sources/rust-project-edition-guide.md) without
adopting Rust's calendar labels or treating Rust as Catena authority.

Edition-neutral does not mean unchecked. A dependency whose semantic interface
cannot be represented, whose revision is unsupported, or whose required
preview is absent must be rejected before lowering. The runtime does not
select editions: the compiler resolves the choice and emits ordinary BEAM
code plus descriptive compile metadata.

## Previews and stable features

“Preview” is the public word for a named, specification-complete capability
that is deliberately impermanent. It is disabled unless the package lists its
identifier, and the exact language revision fixes which preview definition is
in force. This follows the explicit opt-in and artifact-marking lessons in
[JEP 12](../30-sources/buckley-2018-preview-features.md), while Catena chooses
individual names and no runtime flag.

Every feature uses one state machine:

- Preview becomes Stable or Withdrawn.
- Stable may become Deprecated and then Removed.
- A name is never reused after withdrawal or removal.

Stabilization removes the opt-in requirement. Withdrawal says a preview never
joined the stable language. Deprecation keeps stable behavior available while
issuing a repair-oriented diagnostic. Removal makes that behavior unavailable
only in revisions at or after the recorded boundary; an older exact pin
retains its earlier meaning.

Interfaces record only previews needed by exported semantics. A package can
experiment privately without forcing consumers to opt in, while a public
signature or exported behavior cannot hide its impermanent dependency.

## Compatibility and retention

During 0.1, breaking changes are permitted only at an explicit revision
boundary with a classified change record and migration guidance. Removing a
stable feature requires at least one previously published deprecated revision.
Only an approved soundness or security emergency can bypass that window.

After 1.0, Catena uses the compatibility meanings described by
[Semantic Versioning 2.0.0](../30-sources/preston-werner-2013-semantic-versioning.md):
major revisions may break the declared language contract, minor revisions add
compatible stable behavior, and patches make compatible corrections. An
edition follows the revision's major and minor pair.

All published stable editions and revisions remain valid compiler selections.
That is stronger than retaining a document: a conforming newer compiler must
still check the old selection. Exceptional retirement would need its own
future normative policy, not a disappearing registry entry.

## Migration as data

Every compatibility-affecting change needs a stable identifier, source and
target revision, classification, affected area, governing specification link,
human guidance, and any safe edits. Tools expose this registry as deterministic
JSON. Diagnostics may include machine-readable edits, but C008 does not apply
them to files.

An edit is marked safe only when it preserves the selected semantics without
guessing. Adding explicit edition metadata to a legacy manifest qualifies;
renaming a user binding whose intent is unknown does not. This boundary follows
the conservative migration workflow documented by the
[Rust Edition Guide](../30-sources/rust-project-edition-guide.md) and leaves
transactional edit application and source/API refactoring to P125.

## Governance and signed artifacts

Ordinary packages opt into editions and previews directly. Governed packages
may additionally constrain allowed editions, revision ranges, preview sets,
and lifecycle diagnostics. Governance narrows a valid language selection; it
cannot make an invalid selection valid.

Signed records must bind the complete selection and use the domain for their
own artifact format. A 0.1.6 record remains verifiable under its historical
domain. A 0.1.7 verifier must not try alternate domains after a failure, because
fallback would turn the version field into an attacker-controlled ambiguity.

## Falsification criteria and limits

The model fails if an exact old pin silently acquires new behavior, if a
dependency can hide a public preview, if changing edition metadata leaves a
signed artifact valid, or if runtime execution depends on a separately
installed edition service. Conformance tests must exercise each condition.

This slice does not define all source/API/ABI compatibility, general policy
schema evolution, an in-place migration engine, or the full ecosystem
compatibility suite. Those remain G028, G116, P125, and P136. It also does not
make the compiler self-hosting; that requires a separately gated language and
toolchain bootstrap.

## Research route

- [Language Editions and Feature Lifecycle map](../10-maps/language-editions-and-feature-lifecycle.md)
  connects the evidence, resolved inquiry, and normative specification.
- [How Should Catena Version Editions and Language Features?](../40-inquiries/how-should-catena-version-editions-and-language-features.md)
  records the decisions and bounded resolution.
- [Catena 0.1.7 Editions and Feature Lifecycle Specification](../60-specification/editions-and-feature-lifecycle/README.md)
  turns the bounded model into normative conformance obligations.
