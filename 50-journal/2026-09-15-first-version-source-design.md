---
title: "First-Version Source Design"
kind: journal
created: "2026-09-15"
tags:
  - catena
  - language-design
  - syntax
  - decision-log
aliases:
  - "First grammar and vocabulary selection"
---

# First-Version Source Design

## Request and scope

The user asked for concrete first-version grammar and vocabulary based on the
[earlier vocabulary note](../20-notes/approachable-language-vocabulary.md) and
[grammar research](../20-notes/grammar-and-vocabulary-for-approachable-catena.md).
The user accepted the research directions and explicitly excluded participant
studies during language development. The former vocabulary/design hold is
released; no request to implement a parser, amend normative revisions, commit,
or publish was inferred from this design request.

The resulting [source proposal](../20-notes/catena-first-version-grammar-and-vocabulary.md)
selects concrete spellings, examples, semantics, a grammar summary, and an
adoption sequence. The [decision register](../20-notes/design-decision-register.md#first-version-source-design-2026-09-15)
records the twelve original four-way GV forks, the explicit GV-12 override,
and twenty-seven four-way concrete FV decisions selected by the agent under the
user's delegation. These are design decisions, not newly implemented language
features or independently user-approved spellings.

## Method and observations

This session synthesized local research and normative contracts; it did not
conduct a new literature search or human study. Three independent read-only
reviews examined grammar constraints, vocabulary/effect semantics, and scope
and coverage. The review checked the first complete module and the declared
assumptions of smaller example fragments against the retained semantic owners.

Material findings incorporated into the design:

- Preserve repeated unary application and interleaved argument/application
  evaluation. Constructor, operation, and handler payload arities remain distinct
  from ordinary Unit-call shorthand.
- Keep the newer seventeen-trait ABI rather than reinstating superseded names
  from the exploratory vocabulary note. Supply contextual zero-argument `value`
  method declarations for `empty` and `identity` without changing their ABI.
- Keep outcome callbacks pure, require every chain fragment to be pure, and
  distinguish eager independent combination from skipped dependent steps.
- Specify `reply` conditionally: normal reply-expression completion reaches
  one resume; a trap or divergence need not reach it.
- Preserve capability identity, affine control, pure initial handler clauses,
  resource restrictions, and explicit pending parameterized-handler integration.
- Correct resource examples so the successful body result is not an unconditional
  promise when the release deadline can expire.
- Identify source adapters for flat constructor qualification and Unit-taking
  entry spelling, without changing retained interface/entry metadata implicitly.
- Add leading brace-newline handling, EOF without a final separator, named
  explicit type application, and one expression precedence route to the grammar
  summary. It remains a design grammar, not a conflict-tested parser artifact.
- Preserve verification-only fragment restrictions and avoid inventing a compiler
  conformance checker. Keep signed governance bundles in their existing format.

The initial public-surface proposal deliberately uses closed effect/record rows
and pure anonymous functions. Full retained-schema coverage, richer row syntax,
source library adapters, and all source-tool integrations remain explicit P109
adoption work. A design completion does not close their implementation boxes.

## Local evidence and limitations

Research HEAD was `ff66dd72791fd7c7d2fdd19149c1105bbff6131e`; the sibling
compiler integration branch was `rewrite` at
`c3a30d09d1c64147de750da0975e4ad05ca1b64a`. The compiler was read, not edited.
Inspection found a retained `Module.Type.Constructor` metadata field alongside
the newer exactly-two-segment source namespace checker; the proposal requires
an identity-preserving resolution adapter rather than a schema rewrite.

The existing checklist summary was stale. A mechanical count of its 141
explicit item-status headings gave **128 Complete, 11 Partial, and 2 Deferred**,
with no Gap headings. The summary was corrected to match those bodies; no
checkbox was changed and no new whole-language implementation audit is claimed.
The next unused semantic patch was aligned with the already recorded G141
`0.1.98` milestone, giving `0.1.99` without allocating it to this note. The
later C034 amendment now owns `0.1.99`; the next unused patch is `0.1.100`.

The source snippets were reviewed as proposed examples; no public parser exists
to execute them in this session. Arithmetic/result predictions are semantic
walkthroughs, not compiler test output. Future automated parsing, lowering,
reference/BEAM comparison, formatting, and diagnostics are explicitly proposed
acceptance evidence. They do not measure observed human comprehension.

## Archive verification

Archive validation exposed an existing link-extraction bug: the proposed
generic call in a code example was treated as a Markdown link to a file named
`1`. The validator now masks fenced code and matching inline code spans while
preserving real links with code-formatted labels, destinations, and original
line numbers. Eight regression cases cover this distinction and preserve real
broken-link and README-inventory failures. The existing inline-link grammar is
retained; no general Markdown renderer was introduced. `AGENTS.md` documents
the literal-code boundary.

The validator test fixture also omitted five already-declared revision entries
from `0.1.49` through `0.1.53`. Its expected inventory was aligned with the
existing constants; no normative version was changed.

Initial design verification from the repository root:

- `python3 -m unittest test_validate_archive.py`: **37 tests passed**, including
  eight new link-extraction regressions.
- `python3 validate_archive.py`: **777 documents, 110 directories, 8,761 local
  links, and 156 source records passed**. The retained normative counts are 224
  chapters, 103 classified fenced blocks, and 1,366 obligations: 1,246 traced,
  99 partial, and 21 untraced.
- `git diff --check`: passed.
- The twelve GV and twenty-seven FV decision rows were checked for agreement
  between the proposal and register; new documents contain no footnote markers
  or trailing whitespace.

The pre-existing portable citation edits in two studies and `AGENTS.md` were
preserved. All changes remain uncommitted.

## Follow-up: optional empty effect annotations

The user questioned the empty `uses {}` notation and asked to apply the revised
recommendation. The proposal now defines omitted `uses` on an exported function
as a checked closed pure contract; private named functions may infer effects.
Explicit `uses {}` remains an optional purity assertion. Nonempty public
requirements remain declared. The check concerns residual effects, so local
handling may leave a public function pure where existing rules allow it.

Ordinary examples omit empty annotations. One intentional private-helper example
demonstrates the assertion. Bodyless trait signatures and handler contracts also
default to empty rather than inferring requirements from implementations;
verification functions retain their stronger pure-fragment restrictions.
The grammar's handler field is optional, declaration context rules and diagnostic
examples are aligned, and the formatter preserves deliberately written assertions.

The [FV-12 revision](../20-notes/design-decision-register.md#fv-12-revision-optional-empty-effect-annotations)
preserves the original alternatives and records the user-approved replacement.
The proposal explicitly identifies the future amendment to C005's mandatory
public annotation requirement. No compiler or normative chapter was changed.

Follow-up verification: `python3 validate_archive.py` passed with 777 documents
and 8,772 local links; `git diff --check` passed. All twenty-seven current FV
rows agree with the register, including the revised FV-12 row. Ordinary code
examples omit empty annotations; only the intentional private purity-assertion
example retains one. The changes remain uncommitted.

## Follow-up: transforms, totality, and laws

The user approved the recommended declaration progression: `fn`, `transform`,
`total transform`, and function-level `guarantee`. The proposal now gives each
form an exact role, examples, grammar, diagnostics, and adoption obligations.
FV-25–FV-27 preserve four alternatives and the approved recommendations in the
[decision register](../20-notes/design-decision-register.md#transform-totality-and-guarantees).

`transform` is a pure restriction over the ordinary function model, with no
second calling convention or runtime representation. `total transform` also
requires checked termination and absence of language-level traps in the
abstract semantic model; expected failure values remain normal total results.
`guarantee` links a total transform or trait schema to stable specification
claims while retaining separate evidence status and optimizer authority.

The semantic audit found a deliberate adoption conflict: C034 `0.1.31` said
termination analysis could not gate validity and any future checker was
report-only. The later normative
[0.1.99 amendment](../60-specification/opt-in-totality-validity/explicit-total-declaration-gate.md)
now gates that possibility to an explicit total declaration while preserving
ordinary recursion. Structural decrease, trap analysis, evidence through
currying, interface metadata, independent verification, diagnostics, limits,
and compatibility remain required in the later source-adoption slice; the
amendment itself adds no parser or compiler checker.

## Follow-ups

Follow the [proposal's adoption work](../20-notes/catena-first-version-grammar-and-vocabulary.md#adoption-work-and-evidence)
and [current completion plan](../20-notes/language-completion-plan.md).
G137's historical observation profile remains unpassed; a successor normative
G139 policy and readiness profile must encode the changed development scope
before different complete/stable claims are made. Human studies are not a
development dependency. Initial self-hosting still requires actual admitted
Catena source and the existing staged bootstrap evidence.
