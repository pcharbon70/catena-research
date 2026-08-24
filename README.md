# Catena

> A category theory-inspired functional programming language for the BEAM VM

## Etymology

**Catena** (Latin): literally "chain" or "series of connected links."

Figuratively, a catena represents an unbroken sequence of related elements,
each linked to form a coherent whole. In logic and mathematics, it describes a
chain of reasoning where each step follows necessarily from the last. This
reflects the language's emphasis on composition—where functions, types, and
effects are chained together through category-theoretic principles to build
reliable, fault-tolerant systems.

## Overview

Catena is a research project exploring the design of a programming language
that unifies category theory's mathematical rigor with the BEAM VM's legendary
fault tolerance and concurrency capabilities. The language aims to make
abstract mathematical concepts practical and accessible while leveraging the
proven strengths of Erlang's runtime.

Those mathematical foundations are intended to shape Catena's guarantees and
composition, not become prerequisite vocabulary for ordinary programmers.

For a consolidated view of the proposed language architecture, read the
[Catena Language Overview](language-overview.md).

## Research archive

This repository is a research and exploratory archive: a place for ideas to
develop without losing their provenance, relationships, or open questions.

Start at the [home map](10-maps/home.md). The current language-accessibility
work begins with
[An Approachable Vocabulary for Catena](20-notes/approachable-language-vocabulary.md).
The normative compatibility model begins with
[Language Editions and Feature Lifecycle](20-notes/language-editions-and-feature-lifecycle.md).
The normative C010 route begins at the
[Formal Semantic Kernel map](10-maps/formal-semantic-kernel.md) and its exact
[0.1.8 specification](60-specification/formal-semantic-kernel/README.md).
The normative C013 source boundary begins at the
[Source Text Encoding and Normalization map](10-maps/source-text-encoding-and-normalization.md)
and its exact [0.1.9 specification](60-specification/source-text/README.md).
The normative C014 name boundary begins at the
[Identifier and Name Security map](10-maps/identifier-and-name-security.md)
and its exact [0.1.10 specification](60-specification/identifiers/README.md).
The normative C015 layout boundary begins at the
[Whitespace, Layout, and Line Continuation map](10-maps/whitespace-layout-and-line-continuation.md)
and its exact
[0.1.11 specification](60-specification/whitespace-and-layout/README.md).
The normative C016 comment boundary begins at the
[Comments and Documentation Comments map](10-maps/comments-and-documentation-comments.md)
and its exact
[0.1.12 specification](60-specification/comments-and-documentation-comments/README.md).
The normative C017 atomic literal boundary begins at the
[Literal Grammar map](10-maps/literal-grammar.md) and its exact
[0.1.13 specification](60-specification/literal-grammar/README.md).
The normative C018 numeric meaning boundary begins at the
[Numeric Literal Semantics map](10-maps/numeric-literal-semantics.md) and its
exact [0.1.14 specification](60-specification/numeric-literal-semantics/README.md).
The normative C019 operator and punctuation boundary begins at the
[Operators and Punctuation map](10-maps/operators-and-punctuation.md) and
its exact
[0.1.15 specification](60-specification/operators-and-punctuation/README.md).
The normative C020 file-to-module boundary begins at the
[Files and Modules map](10-maps/files-and-modules.md) and its exact
[0.1.16 specification](60-specification/files-and-modules/README.md).
The normative C021 namespace boundary begins at the
[Namespaces and Shadowing map](10-maps/namespaces-and-shadowing.md) and
its exact
[0.1.17 specification](60-specification/namespaces-and-shadowing/README.md).
The normative C022 import/export boundary begins at the
[Imports and Exports map](10-maps/imports-and-exports.md) and its exact
[0.1.18 specification](60-specification/imports-and-exports/README.md).
The normative C023 abstraction boundary begins at the
[Abstraction Boundaries map](10-maps/abstraction-boundaries.md) and its
exact
[0.1.19 specification](60-specification/abstraction-boundaries/README.md).
The normative C024 dependency-cycles boundary begins at the
[Module Dependency Cycles map](10-maps/module-dependency-cycles.md) and
its exact
[0.1.20 specification](60-specification/module-dependency-cycles/README.md).
The normative C025 package boundary begins at the
[Package Identity and Dependencies map](10-maps/package-identity-and-dependencies.md)
and its exact
[0.1.21 specification](60-specification/package-identity-and-dependencies/README.md).
The normative C026 prelude boundary begins at the
[Prelude Policy map](10-maps/prelude-policy.md) and its exact
[0.1.22 specification](60-specification/prelude-policy/README.md).

Repository-wide authoring and maintenance conventions are defined in
[`AGENTS.md`](AGENTS.md).

The versioned normative definition lives in the
[language specification](60-specification/README.md). Research notes explain
why a design was selected; specification chapters define what conforming
implementations and programs must do.

[Specification Authority](SPECIFICATION-AUTHORITY.md) defines exactly which
documents are normative, how examples and rationale are marked, and what to do
when the specification, compiler, reference paths, or tests disagree.
[Catena Conformance Vocabulary](CONFORMANCE-VOCABULARY.md) defines the five
canonical requirement words, failure and variability classes, the absence of
undefined behavior, and implementation-profile obligations across those
normative documents.
[Catena Implementation Limits and Portability](IMPLEMENTATION-LIMITS.md)
defines portable minima, finite-resource classifications, deterministic
machine-readable disclosure, exhaustion behavior, and runtime-capacity
boundaries across claimed implementations.

## Structure

- [`00-inbox/`](00-inbox/README.md) — unprocessed captures
- [`10-maps/`](10-maps/README.md) — curated paths through subjects and
  questions
- [`20-notes/`](20-notes/README.md) — ideas developed in the author's own words
- [`30-sources/`](30-sources/README.md) — reading notes and bibliographic
  records
- [`40-inquiries/`](40-inquiries/README.md) — active questions and research
  workbenches
- [`50-journal/`](50-journal/README.md) — dated observations and exploratory
  writing
- [`60-specification/`](60-specification/README.md) — versioned normative
  language rules and conformance obligations
- [`90-archive/`](90-archive/README.md) — inactive or superseded material worth
  retaining
- [`assets/`](assets/README.md) — images, PDFs, diagrams, datasets, and other
  attachments
- [`templates/`](templates/README.md) — starting points for documents and
  directory indexes

Folders describe what a document is doing. Links, maps, and tags describe what
it is about. Each directory README is a complete local inventory; maps remain
selective conceptual paths.

## Frontmatter

Every completed knowledge document begins with YAML frontmatter:

```yaml
---
title: "A human-readable title"
kind: note
created: "2026-07-31"
maturity: seed
tags:
  - example-topic
aliases: []
---
```

[`frontmatter.schema.json`](frontmatter.schema.json) is the authoritative
machine-readable metadata contract. Current document kinds are:

- `note` — an idea, argument, model, or synthesis; also requires `maturity`
- `source` — a work being read, watched, heard, or consulted
- `inquiry` — an active research question; also requires `status`
- `map` — a curated route through related material
- `journal` — a dated observation or research-session record
- `specification` — a versioned normative language chapter; also requires
  `status` and an exact `major.minor.patch` `spec_version`

Use lowercase kebab-case tags and YAML lists for both `tags` and `aliases`.
Use `[]` for an intentionally empty list and `null` for an unknown nullable
value. Do not add an `updated` field by hand; Git records revision history.

Controlled lifecycle values:

```text
maturity: seed | developing | stable
status:   open | paused | resolved
specification status: draft | candidate | normative
```

## Prototype slice numbering

Catena's current language line is `0.1`. The completed C001 through C006
semantic slices are `0.1.1` through `0.1.6`, and normative C008 is `0.1.7`.
C007, C009, and C012 are repository-governance milestones rather than language
revisions. Normative C010 uses `0.1.8` for the exact formal semantic kernel;
normative C013 uses `0.1.9` for strict source-text decoding; normative C014
uses `0.1.10` for identifiers and standalone qualified names; normative C015
uses `0.1.11` for whitespace, separators, and line continuation; normative
C016 uses `0.1.12` for comments and documentation comments; normative C017
uses `0.1.13` for atomic literal grammar and decoding; normative C018 uses
`0.1.14` for numeric literal semantics; normative C019 uses `0.1.15` for
operators and punctuation; normative C020 uses `0.1.16` for the
file-to-module relationship; normative C021 uses `0.1.17` for namespaces
and shadowing; normative C022 uses `0.1.18` for imports and exports; normative C023
uses `0.1.19` for abstraction boundaries; normative C024 uses `0.1.20`
for module dependency cycles; normative C025 uses `0.1.21` for package
identity and dependency resolution; normative C026 uses `0.1.22` for the
prelude; and
the next
unused semantic patch is `0.1.23`. C008 defines package-local editions,
exact revisions, previews, compatibility, and migration. These identifiers
are distinct from the sibling compiler's package release, external tool
versions, and the historical labels preserved in conformance journals.

The former `0.1` through `0.6` slice identifiers are retired protocol values,
not aliases. The renumbering hard cutover did not itself define end-user
editions, compatibility promises, deprecation, or migration policy. Normative
C008 now defines those relationships at revision `0.1.7`, supported by its
authorized immutable promotion record.

## Working rhythm

1. Capture temporary material in `00-inbox/`.
2. During review, promote useful material using the closest template.
3. Give every durable document a meaningful body link or place it on a map.
4. Develop maps when clusters emerge; do not predict subject folders.
5. Move dormant or superseded work to `90-archive/` without erasing context.
6. Update every affected directory index and run validation in the same
   change.

Templates contain braced placeholders that must be replaced after copying.
They are scaffolds, not completed archive documents.

## Validation

Install the validation dependencies once, then validate the whole archive:

```bash
python3 -m pip install -r requirements-validation.txt
python3 validate_archive.py
git diff --check
```

The validator checks frontmatter, schema conformance, placeholders, filenames,
local links, directory README structure and inventories, conceptual
connections, duplicate source identifiers, specification authority,
conformance vocabulary, implementation-limit policy links, variability
registers, and visible content labels.
Run its focused unit tests with:

```bash
python3 -m unittest test_validate_archive.py
```

## Repository files

- [`AGENTS.md`](AGENTS.md) — authoring, research, organization, and handoff
  instructions
- [`CONFORMANCE-VOCABULARY.md`](CONFORMANCE-VOCABULARY.md) — canonical
  requirement words, behavior classes, variability, limits, traps, and
  implementation profiles
- [`frontmatter.schema.json`](frontmatter.schema.json) — authoritative metadata
  schema
- [`IMPLEMENTATION-LIMITS.md`](IMPLEMENTATION-LIMITS.md) — portable minima,
  implementation and evidence bounds, machine-readable reporting, runtime
  capacity, and exhaustion obligations
- [`language-overview.md`](language-overview.md) — consolidated language
  layers, compiler architecture, runtime artifacts, and open design boundaries
- [`SPECIFICATION-AUTHORITY.md`](SPECIFICATION-AUTHORITY.md) — normative
  document classification, rendered content labels, references, and conflict
  handling
- [`requirements-validation.txt`](requirements-validation.txt) — pinned Python
  dependencies used by the validator
- [`test_validate_archive.py`](test_validate_archive.py) — focused unit tests
  for deterministic archive and specification-structure checks
- [`validate_archive.py`](validate_archive.py) — deterministic archive
  validation
