---
title: "Grammar and Vocabulary Research"
kind: journal
created: "2026-09-12"
tags:
  - catena
  - language-design
  - syntax
  - usability
aliases: []
---

# Grammar and Vocabulary Research

## Scope and outcome

This session investigates how grammar, API vocabulary, teaching, and tools
can make Catena's mathematical and effect structure approachable. It produces
[Grammar and Vocabulary for Approachable Catena](../20-notes/grammar-and-vocabulary-for-approachable-catena.md)
and sixteen new source notes, connected to the existing
[design map](../10-maps/approachable-catena-language-design.md) and
[vocabulary inquiry](../40-inquiries/how-should-catena-expose-mathematical-structure-without-mathematical-jargon.md).

The work is research. It makes no normative language revision, selects no
final public spellings, changes no compiler code, and supplies no human-study
results. P107, P109, and G137 retain their existing unfinished status.
The twelve four-way GV comparisons in the synthesis are unexecuted research
recommendations, not new selections in the implementation decision register.

## Literature method and provenance

The reading starts from Catena's existing vocabulary proposal, category
and effect research, completion plan, and normative constraints. External
search follows four questions: what empirical syntax studies actually
measure; how prior knowledge changes expectations; what approachable
language implementations do with calls and effects; and how diagnostics
and formatting contribute to the experience.

The retained set contains syntax experiments and a replication, elicitation
of non-programmer solutions, a linguistic design essay, misconception and
comment-comprehension studies, API-usability guidance, formal language work,
official Elixir/Koka/Effekt/Gleam/Swift documentation, and firsthand Elixir/Elm
design articles. Search included recent 2025–2026 work; publication and
access dates are recorded separately. In particular, the comments paper
was published in March 2026 despite the 2025 component in its DOI.

Substantive claims use full relevant sections rather than search snippets.
The source notes record the passages consulted and distinguish participant
observations from formal results and language-designer recommendations.
This is a focused synthesis without a preregistered systematic-search
protocol; no database-completeness or exhaustive screening claim is made.
Popularity claims and unsupported rankings of syntax are not treated as
experimental findings.

Important accessible full-text routes include:

- [Stefik and Siebert manuscript](https://www.vidarholen.net/~vidar/An_Empirical_Investigation_into_Programming_Language_Syntax.pdf), especially task methods, results, and limitations.
- [Pane and colleagues' final article](https://john.pane.net/pdf/PaneRatanamahatanaMyers2001.pdf), following an author-hosted manuscript lead.
- [Gordon's author-hosted article](https://csgordon.github.io/publications/onward24/onward24.pdf), including pragmatics and acquisition; this mirror was used when another host failed certificate validation.
- [Lu and Krishnamurthi manuscript](https://cs.brown.edu/people/sk/Publications/Papers/Published/lk-smol-tutor/paper.pdf), including the mixed results and limitations.
- [Myers and Stylos manuscript](https://www.cs.cmu.edu/~NatProg/papers/p62-myers-CACM-API_Usability.pdf), for API-use design considerations.
- [Barik and colleagues manuscript](https://www.microsoft.com/en-us/research/wp-content/uploads/2019/10/barik_fse18.pdf), distinguishing preference and explanation analysis from measured repair performance.
- [Ford's paper](https://pdos.csail.mit.edu/papers/parsing:popl04.pdf), for prioritized-choice recognition semantics.

Downloaded reading copies and generated parser files were temporary under
`/tmp`; no external paper was added to archive assets. Canonical links,
bibliographic notes, and immutable Catena source links preserve the durable
provenance. No participant recruitment or recording took place.

## Historical repository inspection

The sibling repository was inspected through Git object reads. No historical
checkout replaced its active `rewrite` branch. The research repository was
initially clean on `main`; research edits use
`codex/grammar-vocabulary-research`. The sibling repository was clean on
`rewrite` when inspected.

Both commands below identified the same local historical commit:

```sh
git -C /home/ducky/code/catena log -1 --format='%H %cs %s' main
git -C /home/ducky/code/catena log -1 --format='%H %cs %s' archive/poc-v1
```

Observed output for each:

```text
20159d7cb2ae7e1dbb9e09bbd41b10a0ea57d793 2026-07-31 Merge pull request #63 from pcharbon70/agent/delimited-resumptions-phase-8
```

These observations identify the inspected local references, not a claim about
every remote branch at a later date. The
[immutable tree](https://github.com/pcharbon70/catena/tree/20159d7cb2ae7e1dbb9e09bbd41b10a0ea57d793)
anchors the following input records.

| Historical path | Bytes | SHA-256 |
| --- | --- | --- |
| `src/compiler/parser/catena_parser.yrl` | 47461 | `ed8438d63a6da70053292b1a0948a365ca1d0a093ea83aeca8df889d10356895` |
| `src/compiler/lexer/catena_lexer.xrl` | 12183 | `beb3b2e2e8f33b8cc1628b3af0bd35acde28b1d749148b6e74246b5e22e1fca0` |
| `guides/language/02_values_and_transforms.md` | 7297 | `ab863e26b88df4015c7e2695f3ce088e7a504d35c79ac24e23bd548dbfbb5e0c` |
| `guides/language/04_composition_and_context.md` | 9114 | `ef2685df914629fd67c756f2491a0ceac99c749ca30554e8274e1c8f00116a86` |
| `guides/language/06_effects_and_handlers.md` | 9695 | `aff0f5b696c3ce5997340c79e45c529a9326860302e328be0092779dec864808` |

The guides supply the Parcel Relay teaching sequence, ordinary curried
application, composition, explicit effect requests, and handler examples.
The lexer and grammar independently expose punctuation, associativity,
whitespace treatment, and admitted productions. Their presence does not
establish complete compiler/runtime support.

## Historical parser experiment

### Question and method

Does regenerating the historical grammar reproduce its documented conflict
count? This is a narrow grammar-generation experiment, not a compiler build,
semantic test suite, or proof of ambiguity.

The grammar comments at lines 139–201 claim 17 shift/reduce conflicts and
zero reduce/reduce conflicts. Source bytes were extracted with `git show`
to `/tmp/catena-syntax-history-20260912/catena_parser.yrl`. This reproduction
recipe uses the immutable commit rather than a moving branch:

```sh
mkdir -p /tmp/catena-syntax-history-20260912
git -C /home/ducky/code/catena show 20159d7cb2ae7e1dbb9e09bbd41b10a0ea57d793:src/compiler/parser/catena_parser.yrl > /tmp/catena-syntax-history-20260912/catena_parser.yrl
sha256sum /tmp/catena-syntax-history-20260912/catena_parser.yrl
erl -noshell -eval 'io:format("OTP ~s~n", [erlang:system_info(otp_release)]), halt().'
erl -noshell -eval 'io:format("~p~n", [yecc:file("/tmp/catena-syntax-history-20260912/catena_parser.yrl", [{report_errors, true}, {report_warnings, true}, return])]), halt().'
```

The commands interrogate the available system Erlang, which reported
**OTP 27**. That is the toolchain for this experiment; it is not a
restatement of the supported-host versions in later compiler milestones.

### Observations

Yecc generated `catena_parser.erl` successfully and reported:

```text
38 shift/reduce conflicts, 0 reduce/reduce conflicts
```

The above is the conflict-count result, not the complete raw tool output.
Additional warnings identified unused nonterminals `trait_extends`,
`effect_list`, and `type_list`; and unused terminals `actor`, `process`,
`case`, `exports`, `private`, and `range`.

The grammar declares `Right 160 pipe_right` at line 108.
The current [C019 pipe](../60-specification/operators-and-punctuation/precedence-and-associativity.md#the-pipe)
is left-associative. At lines 1053–1054, comments and productions require
parenthesized request arguments to avoid shift/reduce conflicts.
Handler-mode productions at lines 1085–1088 include shallow and multi-shot
forms, unlike the retained
[deep, affine contract](../60-specification/effects-and-handlers/deep-handlers-and-affine-resumptions.md).

### Interpretation and limits

The conflict-count discrepancy invalidates using the comment as reproduced
evidence. It does not show which source strings would parse incorrectly.
No claim about the original author's toolchain is possible from the local
observation alone, and the historical grammar's generated output was not
compiled or executed as a complete compiler in this session.

Likewise, lack of reduce/reduce conflicts does not prove a grammar
unambiguous to human readers or establish recovery quality. Future candidates
need explicit grouping witnesses, malformed-input cases, semantic equivalence
checks, and formatter tests. The synthesis recommends those tests; this
session does not claim they have been implemented.

## Design and authority boundary

The retained 0.1.4 trait/method names are normative for that revision.
The research treats them as the current ABI when explaining operations,
while preserving future public-vocabulary validation. Current lexical,
layout, pipe, effect, function, resource, and environmental-authority
contracts constrain candidates; historical and external syntax cannot
override them.

The G137 protocol is separately checked against the older vocabulary
inquiry. The inquiry's earlier numerical thresholds and suggested rich
participant records are research history, not permission to bypass the
normative protocol's preregistration and restricted data fields. The inquiry
and map now point to that distinction.

## Connections

- [Research synthesis](../20-notes/grammar-and-vocabulary-for-approachable-catena.md) presents findings, four-way alternatives, recommendations, and the candidate corpus.
- [Design decision register](../20-notes/design-decision-register.md) retains the already selected CP-107/CP-109 decisions and links this research without adopting its candidate recommendations.
- [Language completion plan](../20-notes/language-completion-plan-delivery.md#item-107-category-inspired-api-names) remains the implementation route.
