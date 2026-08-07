# Repository instructions

These instructions apply to the entire repository. This is a Markdown research
archive, not a conventional software project. Preserve room for exploratory
thought while keeping provenance, navigation, and document structure reliable.

Follow an explicit user request when it conflicts with this file. Otherwise,
use these conventions for every document and organizational change.

## Archive principles

- Folders describe what a document is doing; maps, links, and tags describe
  what it is about.
- Prefer a small stable top-level structure over speculative subject folders.
- Preserve provenance. Separate a source's claims, our synthesis, local
  experimental evidence, and unresolved questions.
- Keep navigation useful at two levels: directory READMEs are complete local
  inventories, while maps are selective conceptual paths.
- Treat `frontmatter.schema.json` as the authoritative metadata contract.
- Keep related changes atomic: a new, moved, renamed, or archived document and
  every affected index, link, and map change together.

## Canonical structure

```text
00-inbox/       Unprocessed, temporary captures
10-maps/        Curated paths through subjects and questions
20-notes/       Ideas and syntheses in the author's own words
30-sources/     Reading notes and bibliographic records
40-inquiries/   Active questions and research workbenches
50-journal/     Dated observations and research-session evidence
60-specification/ Versioned normative language rules and conformance obligations
90-archive/     Inactive or superseded material worth retaining
assets/         Images, PDFs, diagrams, datasets, and attachments
templates/      Starting points for documents and directory indexes
```

Do not add or rename a top-level directory unless the user asks or a repeated,
demonstrated need makes the existing structure inadequate. Organize subjects
through tags, links, and maps first.

## Sources of truth

Use these files for different decisions:

1. `SPECIFICATION-AUTHORITY.md` defines language-document authority, content
   labels, and conflict handling.
2. `CONFORMANCE-VOCABULARY.md` defines requirement words, behavior classes,
   variability declarations, and implementation-profile obligations.
3. `frontmatter.schema.json` defines valid metadata fields and values.
4. `templates/` defines the minimum starting structure for each artifact.
5. The root `README.md` explains the archive to human readers.
6. Each directory's `README.md` describes and inventories that directory.
7. `10-maps/` provides curated thematic navigation.
8. `validate_archive.py` performs the deterministic structural checks.

If documentation and the filesystem disagree, inspect the intended change and
bring them back into sync. Never preserve a stale index merely because it was
previously committed.

## Directory README invariant

Every archive directory, including a future nested directory, must contain a
`README.md`. Create it from `templates/directory-readme.md` as part of creating
the directory.

Directory READMEs must:

- Use valid frontmatter with `kind: map`. The root README is the exception.
- Use a human-readable title and an H1 that identifies the directory.
- Include `## Purpose`, `## What belongs here`, `## Index`, and
  `## Maintaining this index`.
- Under `## Index`, list `### Subdirectories` and then `### Documents`,
  `### Files`, or `### Templates`, as appropriate.
- Inventory every direct child directory and file except the README itself.
- Link entries relatively and explain their role; a filename alone is not an
  adequate description.
- State `None yet` or an equivalent explicit empty state for empty categories.
- Link each nested directory through its README rather than its bare path.
- Treat the root README as the inventory of top-level archive directories and
  repository-facing files, even though it has a broader guide structure.

Whenever content is added, moved, renamed, archived, or removed:

1. update the README in its old directory, if applicable;
2. update the README in its new directory;
3. update affected maps and meaningful body links;
4. verify that no stale link or inventory entry remains.

Do not index `.git`, generated caches, editor state, or other repository
machinery.

## Frontmatter contract

Every durable knowledge document and directory README begins with YAML
frontmatter that validates against `frontmatter.schema.json`.

All completed documents require:

```yaml
---
title: "A human-readable title"
kind: note
created: "2026-07-31"
tags: []
aliases: []
---
```

Additional requirements depend on `kind`:

- `note` requires `maturity: seed | developing | stable`.
- `inquiry` requires `status: open | paused | resolved`.
- `source` may use `authors`, `published`, `citation_key`, `container`,
  `edition`, `isbn`, `doi`, `url`, and `accessed`.
- `specification` requires `status: draft | candidate | normative` and a
  `spec_version` in exact `major.minor.patch` form.
- `map` and `journal` use the common fields unless the schema changes.

The current Catena prototype language line is `0.1`. C001 through C006 use
patches `0.1.1` through `0.1.6`, and semantic milestone C008 uses `0.1.7`.
Repository-governance milestones C007 and C009 add no language revision.
Normative C010 uses `0.1.8`; the next unused semantic patch is `0.1.9` unless
an approved versioning policy explicitly replaces this temporary convention.
Compiler-package releases, external software versions, and historical
artifact observations are separate version axes.

Conventions:

- Quote dates in `YYYY-MM-DD` form so YAML parsers preserve strings.
- Use the archive document's creation date, not its subject's publication date.
- Use lowercase kebab-case tags and YAML lists for tags and aliases.
- Search existing tags before introducing one. Reuse an established tag when
  a new value would only be a synonym or spelling variant.
- Use `[]` for an intentionally empty list and `null` for an unknown nullable
  value.
- Quote strings containing punctuation, URLs, or YAML-sensitive syntax.
- Keep searchable facts in frontmatter. Put summaries, arguments, quotations,
  evidence, and relationships in the body.
- Make the first H1 match the frontmatter title in meaning and capitalization.
- Do not add an `updated` date by hand; Git records revision history.

Exceptions:

- The root `README.md`, `AGENTS.md`, `SPECIFICATION-AUTHORITY.md`,
  `CONFORMANCE-VOCABULARY.md`, `validate_archive.py`, its tests, and validation
  requirements are repository documentation or tooling and do not use archive
  frontmatter.
- Placeholder files in `templates/` are not valid completed documents until
  copied and filled. `templates/README.md` is completed and must validate.
- A transient inbox capture may begin incomplete, but it must have valid
  frontmatter before promotion to the durable archive.
- Binary assets do not use frontmatter; document them in `assets/README.md` or
  a nearby Markdown file.

## Document roles and templates

| Artifact | Destination | Template | Intended result |
| --- | --- | --- | --- |
| Directory index | Any archive directory's `README.md` | `templates/directory-readme.md` | An exhaustive local inventory |
| Conceptual map | `10-maps/` | `templates/map.md` | A selective, explained route through related work |
| Note | `20-notes/` | `templates/note.md` | An idea, argument, model, or synthesis |
| Source note | `30-sources/` | `templates/source.md` | A bibliographic record with evidence-focused analysis |
| Inquiry | `40-inquiries/` | `templates/inquiry.md` | A live question, hypotheses, findings, and outcome |
| Journal entry | `50-journal/` | `templates/journal.md` | A dated observation or reproducible research-session record |
| Specification chapter | `60-specification/` | `templates/specification.md` | A versioned normative rule set with conformance obligations |

Copy the closest template, replace every placeholder, and adapt its headings
only as the material requires. Do not edit a template merely to customize one
new document.

If a metadata field or document kind changes:

1. update `frontmatter.schema.json` first;
2. update every affected template;
3. migrate completed documents when necessary;
4. update the root README and `templates/README.md`;
5. update `validate_archive.py` if the invariant changed;
6. validate the complete archive.

Do not add a document kind when an existing role plus links or tags expresses
the same work.

## Producing normative specification chapters

- Follow `SPECIFICATION-AUTHORITY.md` for document status, applicability,
  rendered content labels, citations, and conflict handling.
- Follow `CONFORMANCE-VOCABULARY.md` for the five canonical keywords,
  behavior classes, variability callouts, invalidity, limits, explicit traps,
  and the prohibition on undefined behavior.
- Treat a `kind: specification` chapter as language authority only when its
  frontmatter says `status: normative`.
- In a normative chapter, rules are normative by default. Mark rationale,
  proof sketches, evidence reports, connections, notes, diagrams, and
  illustrative examples visibly as non-normative.
- Classify every fenced block with the prescribed callout unless it is already
  inside a section whose heading ends with `(non-normative)`.
- Give every implementation-defined choice or bounded unspecified presentation
  the prescribed visible callout, and keep the area's variability register in
  sync with every `MAY`, `SHOULD`, `SHOULD NOT`, presentation allowance, and
  implementation limit.
- Cite a governing rule by relative document link and heading anchor. Do not
  let a compiler, executable reference, test, or guide supply behavior that
  normative text leaves silent or ambiguous.

## Filenames and paths

- Use lowercase kebab-case Markdown filenames.
- Name conceptual notes and maps for their subject, not their creation date.
- Name inquiries as concise questions in kebab case.
- Name journal entries `YYYY-MM-DD.md`; add a short suffix when a date needs
  more than one entry.
- Prefer `<lead-author>-et-al-<year>-<short-title>.md` for multi-author source
  notes and `<author>-<year>-<short-title>.md` for single-author sources.
- Use stable, descriptive asset names and retain meaningful extensions.
- Use relative Markdown links for local documents and assets.
- Before renaming or moving a file, find and update every incoming local link.
- Use frontmatter aliases for useful former titles, not as a substitute for
  repairing links.

## Producing ordinary documents

Before creating a document:

1. read the root README, this file, the destination README, the relevant
   template, and `frontmatter.schema.json`;
2. search the archive for an existing document that already serves the need;
3. choose the role based on the work the document performs, not merely topic;
4. use the current local date and purposeful existing tags where possible;
5. add a meaningful body connection or place the document on a relevant map;
6. update the destination README in the same change.

Write for a thoughtful reader. Prefer clear claims, explicit uncertainty, and
explanations of why links matter. Avoid empty boilerplate headings: develop a
section, remove it, or state concisely what remains unknown.

## Producing research and deep dives

A deep dive should preserve both the evidence trail and the resulting model.
Unless the user requests another artifact shape, create or update this connected
bundle:

1. one synthesis note in `20-notes/`;
2. one source note in `30-sources/` for each substantively used primary work;
3. an inquiry in `40-inquiries/` when the central question remains open;
4. a topic map in `10-maps/` that explains the route through the work;
5. the home map when the topic belongs at the archive entry point;
6. journal evidence for material local experiments;
7. every affected directory README.

### Research method

- Define the question, scope, terminology, and an operational standard for
  claims such as “understands,” “better,” or “reliable.”
- Search current sources when facts, software, papers, standards, or product
  behavior may have changed. Do not rely on model memory for unstable claims.
- Prefer primary papers, proceedings, official specifications, and official
  project documentation. Use surveys to locate primary evidence or context.
- Record exact authorship, title, year, venue, DOI or canonical URL, and access
  date when available. Never invent missing metadata.
- Read enough of a source to support the claim for which it is cited. Search
  snippets and abstracts are not evidence for detailed claims.
- Distinguish reported results from interpretation. Label extrapolation,
  proposals, and cross-source synthesis.
- Compare evidence across approaches and include negative results, limitations,
  evaluation weaknesses, and unresolved questions.
- Paraphrase by default. Use only short quotations with precise locations and
  respect copyright restrictions.
- Put citations close to the claims they support and link local source notes
  where they help the reader follow the evidence trail.
- Preserve local experimental method, versions, commands, output, and artifacts
  in a journal entry; do not leave a feasibility claim reproducible only from
  memory.

### Source-note shape

Adapt the source template to the work, normally using:

- `## Reference` for the complete citation and canonical link;
- `## Research question`, `## Contribution`, or a similar specific heading;
- `## Method` when the work presents empirical or formal evaluation;
- `## Findings` for results actually supported by the work;
- `## Relevance` for why it matters to the archive's question;
- `## Limits` for scope, assumptions, and evaluation weaknesses;
- `## Derived work` for notes, inquiries, maps, or experiments it informs.

Do not copy an abstract as a substitute for analysis. Avoid source notes for
works mentioned only incidentally.

### Synthesis-note shape

Use structure proportionate to the topic. A substantial deep dive often needs:

- an executive conclusion;
- scope, method, and definitions;
- technical or historical foundations;
- a taxonomy of relevant approaches;
- comparison of what evidence supports and does not support;
- a proposed model or implications when warranted;
- tradeoffs, limitations, and falsification criteria;
- research priorities or open questions;
- an annotated route to source notes;
- connections to the topic map and active inquiry.

Do not force this outline when another structure explains the topic better.
Preserve the separation among evidence, inference, and proposal.

## Maps, inquiries, and lifecycle

- Maps are curated explanations, not file dumps. Group links into meaningful
  trails and explain their relationship.
- The home map remains selective. Add major active inquiries, topic maps, and
  developed syntheses; do not mirror every directory index.
- Inquiries state why a question matters, operational definitions, provisional
  hypotheses, paths to explore, findings, and an outcome.
- Promote independently useful conclusions from inquiries or journals to notes.
- Move dormant or superseded work to `90-archive/` rather than silently
  deleting valuable context. Record why and link replacements.
- Do not call a note `stable` or an inquiry `resolved` merely because a writing
  pass is complete; evidence must support the lifecycle state.

## Assets

- Store an asset locally only when the archive needs a durable lawful copy.
  Prefer a canonical external link when duplication adds no value.
- Record provenance, creator, source URL, license, and the document using the
  asset when available.
- Create a descriptive subdirectory with its own README when an asset group
  becomes large enough to need one.
- Never leave an unreferenced asset without an index description.

## Verification checklist

Before reporting archive work complete:

1. inspect `git status` and preserve unrelated user changes;
2. run `python3 validate_archive.py` from the repository root;
3. verify external citations introduced by the change against primary sources;
4. run `git diff --check`;
5. review the complete diff for stale paths, accidental rewrites, and unrelated
   changes.

The validator checks:

- that the JSON Schema parses and completed frontmatter validates;
- that no braced template placeholder leaks outside `templates/`;
- lowercase kebab-case knowledge-document filenames;
- local Markdown file and heading-fragment links;
- required directory README headings and complete direct-child inventories;
- at least one conceptual connection for every durable document;
- duplicate citation keys, DOIs, and canonical source URLs.
- specification authority and conformance-vocabulary links, variability
  registers, canonical keywords, prohibited behavior classes, non-normative
  exemptions, visible callouts, illustrative cues, and fenced-block
  classifications.

If the validator's behavior and these instructions disagree, repair both in
the same change rather than silently bypassing a check.

## Git and handoff

- Do not commit, push, open a pull request, or publish unless the user asks.
- When asked to commit, stage only the intended archive changes and use a terse
  message describing the content.
- Before pushing, report and resolve validation failures.
- In the final handoff, summarize documents created or changed, maps and
  indexes updated, validation performed, and whether changes remain uncommitted.
