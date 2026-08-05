---
title: "Edition Migration, Diagnostics, and Conformance"
kind: specification
created: "2026-08-05"
status: normative
spec_version: "0.1.7"
tags:
  - compatibility
  - diagnostics
  - migration
  - specification
aliases:
  - "Catena 0.1.7 migration contract"
---

# Edition Migration, Diagnostics, and Conformance

## Change registry

Every compatibility-affecting language transition has an immutable change
record containing:

- a unique lowercase identifier;
- source and target language revisions;
- `breaking`, `compatible-addition`, or `compatible-correction`;
- affected compatibility dimensions;
- links to exact governing specification headings;
- a concise human summary and migration guidance; and
- zero or more structured edits whose applicability is stated.

Records are sorted by target revision and identifier. A compiler exposes the
same registry through its public language-information API and CLI. The
registry is derived conformance data; normative prose remains authoritative
when implementation data disagrees.

The first record uses `0.1.0` as the pre-C001 baseline source. That baseline
is not a published or selectable language revision; retained compiler
selection begins at `0.1.1`.

The 0.1.6-to-0.1.7 change record replaces the package-manifest artifact
version with `0.1.7` and adds edition `0.1`, revision `0.1.7`, and an empty
preview set. Those adoption edits are distinct from `EDN002`, which makes a
legacy selection explicit without changing its artifact version or semantics.

## Safe edit suggestions

A diagnostic edit has `kind: json-edit`, operation `add`, `replace`, or
`remove`, one JSON path, an optional value, and applicability
`machine-applicable` or `manual`.

An edit is machine-applicable only when applying it cannot change the selected
program semantics or guess user intent. C008 reports edits but MUST NOT modify
a file. Transactional application, backups, source rewrites, API refactors,
and deprecated-syntax handling remain P125.

## Legacy manifest behavior

A valid 0.1.4 or 0.1.6 package manifest without selection fields decodes as
edition `0.1`, language revision equal to its artifact version, and no
previews. Compilation emits `EDN002` with machine-applicable additions for the
three explicit fields and continues using the legacy artifact formats.

Supplying all three matching fields makes the legacy selection explicit and
suppresses `EDN002`; it does not upgrade any artifact format. Supplying only a
subset or a language revision different from the manifest version is
`EDN001`.

The advisory MUST NOT alter source files, interfaces, BEAM bytes, assurance
records, signing payloads, or output paths. A malformed legacy manifest is
still `LNK001`; inference does not repair invalid input.

## Diagnostics

Version 0.1.7 adds these stable diagnostic families:

| ID | Default severity | Meaning |
| --- | --- | --- |
| `EDN001` | error | missing, malformed, mismatched, unknown, or unsupported edition/revision selection, or a construct unavailable at that revision |
| `EDN002` | warning | a legacy artifact supplied an inferred selection and can be made explicit |
| `PRV001` | error | a named preview is unknown or unavailable in the selected revision/state |
| `PRV002` | error | an imported public interface requires a preview the consumer did not enable |
| `DEP001` | warning | selected code uses a deprecated stable feature |

Every diagnostic includes severity, stable ID, message, primary JSON path when
available, deterministic details, and ordered edits. A package may list
warning IDs under `diagnostics.deny`; a matching warning then fails the build
without changing its ID. Governance may require the same absence through the
policy rule defined in
[Edition Interfaces, Artifacts, and Governance](interfaces-artifacts-and-governance.md#optional-governance-constraints).

This bounded severity contract does not complete G009's general conformance
vocabulary or P117's full source-location and provenance model.

## Language information contract

The public compiler API and `catena language-info` command return canonical
JSON-compatible data with format `catena-language-info`, artifact version
`0.1.7`, current selection, retained editions and revisions, feature entries,
and migration changes. Lists and object fields are deterministic. The command
accepts no source path and performs no mutation.

## Conformance corpus

A conforming implementation exercises:

- every retained exact revision and rejection of invalid edition/revision
  pairs, floats, aliases, prerelease strings, and unknown pins;
- package-wide selection, standalone reporting, legacy inference, structured
  edits, and warning denial;
- every valid and invalid lifecycle edge, identifier non-reuse, stale preview
  opt-in, and revision-bound state lookup;
- private versus public preview propagation and downstream opt-in rejection;
- normalized interfaces across retained revisions and modelled future edition
  boundaries;
- exact selection binding in interface digests, specialization/cache keys,
  BEAM compile metadata, package output, assurance payloads, approvals, and
  governance context;
- historical 0.1.6 signature verification, new 0.1.7 domains, and downgrade,
  version-substitution, preview-removal, and artifact-tampering attacks;
- default deprecation warnings and project/governance promotion to failure;
  and
- absence of runtime edition dispatch, plus preservation of the 0.1.6
  specification/governance erasure guarantees.

## Promotion gate

C008 promotion required all candidate chapters and archive indexes to
validate, the complete C001–C006 plus C008 compiler suite to pass on
pinned Elixir and OTP 29, the focused lifecycle and adversarial suite to pass,
and generated artifacts to be inspected. The sole production `.beam`
creation call remains OTP 29 `compile:noenv_forms/2`.

After those checks, an explicitly authorized immutable compiler commit is
recorded with its parent, tree, environment, commands, test counts, and
artifact digests. The linked evidence record satisfies that gate; all four
chapters are therefore `normative`, the bounded inquiry is resolved, and
checklist C008 is complete.

## Evidence route (non-normative)

Conservative edit generation follows the evidence summarized in the
[Rust Edition Guide source note](../../30-sources/rust-project-edition-guide.md).
The design and its falsification criteria are developed in
[Language Editions and Feature Lifecycle](../../20-notes/language-editions-and-feature-lifecycle.md).
The authorized immutable implementation run is preserved in
[C008 Edition and Feature-Lifecycle Conformance](../../50-journal/2026-08-05-c008-edition-conformance.md).
