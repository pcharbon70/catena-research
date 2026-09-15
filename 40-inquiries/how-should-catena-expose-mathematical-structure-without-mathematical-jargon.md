---
title: "How Should Catena Expose Mathematical Structure Without Mathematical Jargon?"
kind: inquiry
created: "2026-08-01"
status: open
tags:
  - api-design
  - catena
  - documentation
  - language-design
  - programming-language-education
  - usability
aliases:
  - "How should Catena validate its approachable vocabulary?"
  - "Catena vocabulary inquiry"
---

# How Should Catena Expose Mathematical Structure Without Mathematical Jargon?

## Current design scope and historical protocol

On 15 September 2026 the user accepted the research directions, released the
public-language design hold, and excluded human studies during language
development. [Catena First-Version Grammar and Vocabulary](../20-notes/catena-first-version-grammar-and-vocabulary.md)
now selects concrete candidate forms with explanations and examples.
Development checks cover semantic fidelity, ordinary programs, adversarial
grammar cases, formatting, and diagnostics. Candidate design is not normative
adoption or compiler implementation, and these checks do not establish
observed human comprehension.

The [September grammar and vocabulary study](../20-notes/grammar-and-vocabulary-for-approachable-catena.md)
extends this inquiry's evidence and design alternatives. The
[normative G137 protocol](../60-specification/usability-gate/observed-prediction-transfer-and-repair.md)
now governs any study claiming that gate: six pilot and 24 main participants,
two balanced strata, four metrics, restricted coded fields, and thresholds
preregistered after the pilot. The richer participant descriptions,
open-ended responses, and numerical targets below are earlier exploratory
proposals, not the current authorized protocol. A different exploratory
study or a protocol amendment would be needed to collect additional fields.
All participant-study paths below are retained research history and are
outside the current development scope. G137 remains unpassed; a successor
release policy is needed before changing G139's complete/stable requirements.

## Why this matters

Catena aims to make strong compositional guarantees available to programmers
who do not know category theory. That goal is not achieved merely by replacing
formal names with familiar English words. A familiar word can mislead, two
friendly names can conceal the most important distinction, and an apparently
simple API can hide effects or evaluation cost.

The design needs an exact connection between public vocabulary and the formal
model. During development, explicit examples and semantic audits expose
misleading names and hidden distinctions. Whether those choices improve human
performance remains an unanswered research question; it is not a prerequisite
for the authorized first-version design.

## Operational question

Which public capability names, operation families, diagnostics, and learning
sequence let programmers without category-theory training correctly:

- transform values inside common data types;
- distinguish independent combination, dependent sequencing, and
  structure-wide collection;
- predict shape, effect, order, termination, and cost behavior;
- transfer an operation learned on one type to an unfamiliar type;
- understand and repair capability and derivation errors; and
- write code whose behavior still satisfies Catena's formal semantic ledger?

An observed-comprehension answer would require task evidence from representative
programmers as well as a separate semantic audit. Current development answers
the design and semantic questions without making that empirical claim.

## Working hypotheses

1. A concrete-first sequence using `Option`, `Result`, lists, and trees will
   produce better transfer than introducing the generic trait hierarchy first.
2. The decision family `map`, `map2`, `and_then`, and `collect_map` will make
   dependency shape clearer than a list of seventeen capabilities.
3. Action verbs for operations and role nouns or adjectives for traits will be
   easier to interpret consistently than noun-heavy formal names.
4. Guarantee prose framed as safe refactoring will communicate obligations
   better than unexplained law names, without weakening the specification.
5. Default diagnostics organized as action, source, reason, and repair will
   enable more successful first repairs than diagnostics led by kinds,
   variance, or formal class names.
6. Some proposed names—especially `Accumulator`, `Pairable`, `Applicator`,
   `Collector`, `Pipeline`, `System`, and `ContextMapper`—will create false
   predictions and require revision, merging, or removal from the early public
   surface.
7. Not every structure in the formal ledger needs a separately named beginner-
   facing trait. Some may work better as derived interfaces, advanced
   constraints, or module operations.

These hypotheses are provisional. The candidate vocabulary is developed in
[An Approachable Vocabulary for Catena](../20-notes/approachable-language-vocabulary.md).

## Paths to explore

### Establish participant groups

Recruit at least three experience profiles:

- programmers comfortable with typed mainstream or BEAM languages but without
  functional-programming specialization;
- functional programmers who use `map` and result types but do not use formal
  category-theory vocabulary; and
- experienced functional-language users who can perform the independent
  semantic audit.

Record language background and prior exposure rather than treating “beginner”
as one undifferentiated category. Formal experts should not dominate the
vocabulary tests, and novice results should not replace the semantic audit.

### Vocabulary prediction study

For each proposed capability, show only its name, a short declaration, and two
or three candidate behaviors. Ask participants to predict:

- which values it can combine or transform;
- whether it preserves outer shape;
- whether later work depends on earlier values;
- whether it implies effects, ordering, mutation, or parallelism; and
- which operation they would search for next.

Test risky names against alternatives and a neutral placeholder. Do not show
the formal mathematical term during the task.

### Operation-selection tasks

After no more than a two-page concrete primer, ask participants to choose among
`map`, `map2`, `and_then`, and `collect_map` for unseen examples involving:

- optional values;
- fail-fast results;
- accumulating validation;
- lists and recursive trees;
- parser steps;
- effectful requests; and
- concurrent work whose independence matters.

Collect correctness, time to first choice, confidence, explanation, and
revisions after type feedback. The explanation must identify dependency and
shape without requiring a formal term.

### Transfer tasks

Teach an operation on one concrete type, then ask the participant to use it on
an unfamiliar type with the same capability. Compare concrete qualified APIs,
generic trait constraints, and a hierarchy-first explanation. Check whether
the same verb supports transfer or merely encourages surface analogy.

### Diagnostic repair study

Construct errors for:

- a `Mapper` derivation whose parameter occurs in an input position;
- a missing independent-combination implementation;
- an ambiguous generic requirement;
- an unhandled or duplicate effect capability;
- a non-exhaustive match; and
- a guarantee that cannot be trusted for optimization.

Compare a public-vocabulary diagnostic with a technically led diagnostic.
Measure first-repair success, repair time, incorrect edits, and whether users
can state the cause afterward. Technical details must remain accessible in
both conditions so the test compares presentation rather than information
removal.

### Collision and corpus audit

Search likely Catena programs, existing language ecosystems, and documentation
queries for each candidate. Identify collisions such as ordinary `pipeline`,
mutable accumulator, collection builder, operating system, or tuple pairing.
Test names in expressions, requirements, module qualification, diagnostics,
and search results—not as an isolated glossary.

### Semantic audit

For every retained public capability, record:

- its exact kind and type parameters;
- minimal and derived operations;
- parent evidence and coherence rules;
- formal laws and law-trust level;
- shape, dependency, evaluation, termination, ordering, and effect contracts;
- lawful derivation conditions for algebraic data types; and
- the diagnostics required when those conditions fail.

Reviewers familiar with the mathematical model must confirm that the public
interface neither merges observably distinct behavior nor promises behavior
not justified by the formal structure.

### Guide prototypes

Create only enough guide material to test the learning sequence:

1. values and transforms;
2. variant types and matching;
3. `map` on concrete types;
4. independent `map2`;
5. dependent `and_then`;
6. reducing and collecting structures;
7. traits and guarantees;
8. effects and handlers; and
9. processes and supervision.

Use a continuing problem domain, failing examples, and compiler explanations.
Revise the vocabulary between sessions. The prototypes become durable guides
only after the words and distinctions stabilize.

## Evaluation thresholds

The first pilot should test the method and set realistic baselines. Subject to
that calibration, the candidate vocabulary should advance only if:

- at least 80% of participants select the correct one of `map`, `map2`,
  `and_then`, and `collect_map` on unseen representative tasks after the short
  primer;
- at least 75% make a correct first repair for the core diagnostic set using
  the default public explanation;
- no retained name leads more than 20% of participants to the same material
  false prediction about shape, dependency, effect, order, mutation, or cost;
- transfer performance remains strong across at least `Option`, `Result`, one
  accumulating validation type, a list, and a recursive tree;
- participants can explain each operation choice without the formal glossary;
  and
- the semantic audit finds a complete mapping with no weakened law,
  coherence, or execution obligation.

The numeric thresholds are provisional design gates, not universal usability
claims. Report sample size, confidence intervals or raw counts, participant
background, task wording, and all exclusions. A small qualitative pilot may
discover problems but cannot establish population-level success.

## Findings

- The [grammar and vocabulary synthesis](../20-notes/grammar-and-vocabulary-for-approachable-catena.md)
  separates ratings, task performance, formal mechanisms, and engineering
  precedents. It recommends explicit dependency and effect boundaries with
  progressive formal detail, while leaving candidate spelling and comparative
  performance unresolved.
- The [historical parser experiment](../50-journal/2026-09-12-grammar-and-vocabulary-research.md#historical-parser-experiment)
  reproduces 38 shift/reduce conflicts under OTP 27 against a comment claiming
  17. This is grammar-maintenance evidence, not a human-comprehension result
  or proof of incorrect parsing.
- Cognitive dimensions provide a structured way to inspect closeness,
  consistency, hidden dependencies, abstraction gradient, and progressive
  evaluation, but they do not validate any candidate name. See
  [Green and Petre](../30-sources/green-petre-1996-cognitive-dimensions.md).
- Empirical compiler-message research supports preserving both causal
  explanation and actionable repair. See
  [Barik and colleagues](../30-sources/barik-et-al-2018-compiler-explanations.md).
- Elm provides a relevant design precedent for source-local explanations and
  contextual hints. Its project experience does not substitute for
  Catena-specific testing. Follow the
  [topic map](../10-maps/approachable-catena-language-design.md) for these
  source notes.
- The earlier candidate list contains foreseeable naming collisions. The
  first-version proposal now resolves concrete names through explained design
  choices and a semantic audit; participant studies are not required during
  development, and comprehension improvements remain unverified.

## Outcome

Open. The first-version proposal supplies the current design answer and
records concrete vocabulary, operation families, and diagnostic conventions.
Normative adoption and implementation remain pending. The empirical question
about programmer comprehension is unresolved and outside development scope;
its unresolved status does not reinstate a participant-study prerequisite.
