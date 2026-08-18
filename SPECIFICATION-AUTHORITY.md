# Catena Specification Authority

This policy defines how to identify and interpret Catena's normative language
specification. It governs documents and conformance evidence; it is not a
Catena language edition and does not add source syntax, static semantics, or
runtime behavior. The companion
[Catena Conformance Vocabulary](CONFORMANCE-VOCABULARY.md) defines requirement
words, behavior classes, variability declarations, and implementation-profile
obligations inside the normative material identified here. The companion
[Catena Implementation Limits and Portability](IMPLEMENTATION-LIMITS.md)
policy defines portable minima, finite-resource reporting, and exhaustion
obligations without adding language semantics.

## Authority classes

Only a document under [`60-specification/`](60-specification/README.md) with
both `kind: specification` and `status: normative` is a normative language
chapter. Its declarative prose, tables, grammar, equations, judgments, and
explicit conformance obligations define what conforming programs and
implementations must do, except where material is visibly marked
non-normative.

The following are not normative language definitions:

- specification chapters whose status is `draft` or `candidate`;
- directory READMEs, maps, notes, source notes, inquiries, and journals;
- rationale, proof sketches, evidence reports, connections, and illustrative
  examples marked non-normative inside a normative chapter;
- templates, guides, the language tour, and repository documentation;
- executable reference evaluators, compiler implementations, tests, generated
  artifacts, and recorded conformance runs.

This document is authoritative for document classification and conflict
handling, while `CONFORMANCE-VOCABULARY.md` is authoritative for conformance
wording and behavior classification, and `IMPLEMENTATION-LIMITS.md` is
authoritative for the cross-implementation portability floor. All three are
repository governance rather than normative Catena language chapters.
`AGENTS.md`, the specification template, and the archive validator implement
these policies.

## Status and applicability

Frontmatter is the status source of truth. Descriptive text in an index or
guide cannot promote a chapter. Promotion requires changing the chapter to
`status: normative` together with the evidence and indexes required by the
repository workflow.

A chapter applies only within the scope and exclusions stated by its
specification area. A larger `spec_version` does not automatically replace an
older rule. Normative C008 defines cumulative same-edition applicability and
requires an explicit lifecycle and migration record for replacement,
deprecation, or removal. A later chapter therefore overrides an earlier
chapter only when normative text explicitly states that relationship.

If two apparently applicable normative chapters disagree and neither contains
that relationship, the specification is defective. The disputed behavior has
no conforming interpretation until the conflict is repaired.

## Prototype slice identifiers

`spec_version` uses exact `major.minor.patch` syntax. The current prototype
language line is `0.1`; its registered semantic boundaries are:

| Boundary | Version | Status |
| --- | --- | --- |
| C001 type system | `0.1.1` | normative |
| C002 data and patterns | `0.1.2` | normative |
| C003 clause conditions | `0.1.3` | normative |
| C004 traits and categorical operations | `0.1.4` | normative |
| C005 effects and handlers | `0.1.5` | normative |
| C006 specifications and governance | `0.1.6` | normative |
| C008 editions and feature lifecycle | `0.1.7` | normative |
| C010 formal semantic kernel | `0.1.8` | normative |
| C013 source text | `0.1.9` | normative |
| C014 identifiers | `0.1.10` | normative |
| C015 whitespace and layout | `0.1.11` | normative |
| C016 comments and documentation comments | `0.1.12` | normative |

Governance milestones C007, C009, and C012 apply across the normative corpus
and do not occupy language revisions. Normative C010 occupies `0.1.8`, and
normative C013 occupies `0.1.9`; normative C014 occupies `0.1.10`; normative
C015 occupies `0.1.11`; normative C016 occupies `0.1.12`; a later semantic
slice begins at `0.1.13`. Each later
prototype semantic slice uses
the next unused `0.1.n` patch until an approved policy replaces this
convention.
This sequence identifies language slices and the Catena protocol boundaries
that name them. It is independent of compiler-package releases and third-party
dependency versions. It also does not make a larger patch automatically
applicable or authoritative.

The normative 0.1.7 chapters distinguish edition, language revision, artifact
format, and compiler-package release, and define applicability within the
retained `0.1` edition.

The previous two-component identifiers remain visible only where a historical
record describes bytes emitted by an immutable compiler commit. They are not
current language or protocol aliases. C008 defines the end-user edition,
compatibility, deprecation, preview, and migration policy.

## Normative and non-normative material

Normative chapter content is normative by default. A plain declarative rule is
binding even when it does not use an uppercase requirement word. Requirement
force, invalidity, implementation-defined choices, bounded unspecified
presentation, implementation limits, explicit failures, and the prohibition
on undefined behavior follow the
[Catena Conformance Vocabulary](CONFORMANCE-VOCABULARY.md).

Use visible rendered labels rather than hidden comments:

- End a non-normative section heading with `(non-normative)`.
- Introduce an exact grammar, judgment, schema, state transition, or other
  defining fenced block with `> **Normative definition.**`.
- Introduce an example that imposes an acceptance, rejection, diagnostic, or
  observable-result obligation with
  `> **Normative conformance example.**`.
- Introduce an enumerated, profiled implementation-defined choice with
  `> **Normative implementation-defined choice.**`.
- Introduce a bounded presentation or internal-strategy equivalence class with
  `> **Normative unspecified presentation.**`.
- Introduce local explanatory material with one of
  `> **Non-normative example.**`, `> **Non-normative rationale.**`,
  `> **Non-normative note.**`, `> **Non-normative diagram.**`, or
  `> **Non-normative evidence.**`.

A fenced block in a specification chapter must either follow the applicable
definition, conformance-example, or non-normative callout or appear inside a
section marked non-normative. That label applies to the immediately following
block. The two variability labels instead apply to the immediately following
paragraph or table and carry the additional requirements in the conformance
policy. Non-normative material may explain a rule but cannot add a requirement,
narrow or widen its domain, resolve an ambiguity, or override normative text.

Source notation is an illustrative example unless a normative chapter
explicitly classifies it as a normative definition or conformance example.
Commands used to reproduce a compiler run and diagrams used to explain a
pipeline are evidence or explanation, not language semantics.

## References and traceability

A conflict report, test description, compiler comment, or evidence record must
identify the governing rule with a document link and heading anchor, for
example `syntax-and-safety.md#evaluation`. A chapter-only citation is
insufficient when more than one heading could govern the behavior.

This policy does not assign a permanent identifier to every individual rule.
Checklist item C011 (formerly P011) delivered exhaustive rule-to-test
traceability through the `AREA-OBL-NNN` obligation identifiers; any later stable
rule identifier scheme extends it.

## Conflict resolution

The normative specification is the sole authority when artifacts disagree:

| Disagreement | Required interpretation and action |
| --- | --- |
| Normative chapter versus compiler | The compiler is non-conforming for that rule; repair it and add regression evidence. |
| Normative chapter versus test | The test is incorrect or stale; repair it without changing the rule implicitly. |
| Normative chapter versus executable reference | The reference implementation is incorrect or incomplete; it has no fallback authority. |
| Compiler versus test or reference | Consult the cited normative heading; none of the executable artifacts wins by itself. |
| Two applicable normative chapters | Block the affected conformance claim until normative text explicitly resolves applicability or replacement. |
| Normative silence or ambiguity | Record a specification gap; no compiler, test, guide, or reference behavior may silently fill it. |

A formal semantic definition written in a normative chapter is part of the
specification. A program that implements or approximates that definition is
executable evidence and remains independently fallible.

While a conflict is open, a project may report the observed behavior and the
disagreement, but it must not claim conformance for the disputed rule.

## Repair and promotion workflow

1. Cite the exact normative document and heading, the conflicting artifact,
   and the observable disagreement.
2. Determine whether the defect is in an implementation, test, executable
   reference, explanatory document, or the normative text itself.
3. Repair non-normative artifacts to agree with unchanged normative text, or
   approve an explicit normative replacement before treating changed language
   behavior as accepted.
4. Update affected conformance cases, reference paths, compiler behavior,
   guides, indexes, and evidence records together.
5. Run archive validation and every affected implementation suite before
   restoring a conformance claim.

Compiler behavior alone never changes Catena. Passing tests demonstrate
evidence against specified obligations; they do not promote a candidate,
settle an ambiguity, or amend a normative chapter.

## Deliberately separate work

This policy leaves the following questions open:

- C008 defines editions, compatibility, deprecation, and replacement
  lifecycle; future edition retirement and broader API/ABI policy remain
  separately tracked.
- C012 defines which implementation limits may vary, their portable minima,
  and machine-readable reporting; C009 defines their behavior class.
- C011 (formerly P011) connects every normative rule to executable evidence
  through its permanent obligation identifiers.

Those items may extend this policy, but evidence must continue to remain
distinct from language authority.
