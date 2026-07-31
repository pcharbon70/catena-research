# Catena Research Archive

This repository is a research and exploratory archive: a place for ideas to
develop without losing their provenance, relationships, or open questions.

Start at the [home map](10-maps/home.md).

Repository-wide authoring and maintenance conventions are defined in
[`AGENTS.md`](AGENTS.md).

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

Use lowercase kebab-case tags and YAML lists for both `tags` and `aliases`.
Use `[]` for an intentionally empty list and `null` for an unknown nullable
value. Do not add an `updated` field by hand; Git records revision history.

Controlled lifecycle values:

```text
maturity: seed | developing | stable
status:   open | paused | resolved
```

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
connections, and duplicate source identifiers.

## Repository files

- [`AGENTS.md`](AGENTS.md) — authoring, research, organization, and handoff
  instructions
- [`frontmatter.schema.json`](frontmatter.schema.json) — authoritative metadata
  schema
- [`requirements-validation.txt`](requirements-validation.txt) — pinned Python
  dependencies used by the validator
- [`validate_archive.py`](validate_archive.py) — deterministic archive
  validation
