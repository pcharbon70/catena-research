---
title: "C007 Normative Document Authority"
kind: journal
created: "2026-08-03"
tags:
  - governance
  - specification
aliases:
  - "C007 specification authority evidence"
---

# C007 Normative Document Authority

## Observations

Checklist item C007 is a repository-governance completion rather than a Catena
language edition. The new
[Specification Authority](../SPECIFICATION-AUTHORITY.md) makes a chapter
normative only when it is under `60-specification/` with
`kind: specification` and `status: normative`. Executable references, compiler
behavior, tests, implementation records, guides, research, rationale, and
illustrative examples remain evidence or explanation rather than fallback
language definitions. The
[language specification index](../60-specification/README.md) exposes that
policy from every versioned specification area.

The six existing specification areas contain 45 normative chapters. Their 53
chapter-level fenced blocks now identify exact definitions, conformance
examples, explanatory examples, diagrams, or executable evidence with visible
rendered labels. The additional reproduction block in the type-system index is
also visibly marked as non-normative evidence. Mixed sections were split so
normative limits and falsification obligations do not inherit the status of
rationale or proof sketches.

The sibling compiler repository changes only documentation. No Catena source
form, JSON AST, typed core, diagnostic, interface, assurance artifact, BEAM
lowering, runtime behavior, or compiler test was changed. C007 therefore does
not create version 0.1.7 and requires no immutable compiler conformance commit.

## Evidence

The research archive validation used:

```text
python3 -m unittest test_validate_archive.py
python3 validate_archive.py
git diff --check
```

The focused validator suite reported seven passing tests. Before this journal
entry was added, complete validation reported 180 completed documents, 17
directories, 1,390 local links, 81 source notes, 45 specification chapters,
and 53 classified specification fenced blocks with no errors. Final validation
with this indexed entry reported 181 completed documents, 17 directories,
1,396 local links, 81 source notes, 45 specification chapters, and 53
classified specification fenced blocks.

The sibling compiler was checked from the documentation-only C007 branch based
on merged rewrite commit `a78bf164481a`, using Elixir 1.20.2 compiled with
Erlang/OTP 29 and ERTS 17.0.4:

```text
asdf exec mix format --check-formatted
asdf exec mix clean
asdf exec mix compile --warnings-as-errors
asdf exec mix test
asdf exec mix escript.build
git diff --check
```

The compiler rebuilt 49 files without warnings, reported 108 passing tests,
and generated the escript successfully. Its changes are limited to the root
README, contributor policy, guide index, feature workflow, and diagnostics and
testing guide.

## Result

C007 is complete. Normative text is the sole language authority. An executable
artifact disagreement blocks the affected conformance claim; it does not
select a winner. Two apparently applicable normative chapters also block until
an explicit normative applicability or replacement statement resolves the
conflict. A larger version number has no automatic precedence.

Conflict reports and implementation obligations cite a document and heading.
The current policy intentionally does not assign permanent identifiers to
every rule.

## Threads

- [G008](../00-inbox/language-specification-completeness-checklist.md#1-specification-form-and-conformance)
  remains responsible for editions, compatibility, and lifecycle rules.
- G009 remains responsible for the complete conformance vocabulary.
- P011 remains responsible for exhaustive rule-to-test traceability and any
  permanent per-rule identifiers.

## Follow-ups

Do not treat this governance completion as semantic implementation evidence.
Future specification areas must link the authority policy, include a status
and authority overview, and preserve the visible content labels enforced by
the archive validator.
