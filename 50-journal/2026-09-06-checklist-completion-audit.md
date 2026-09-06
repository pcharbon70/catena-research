---
title: "Checklist Completion Audit"
kind: journal
created: "2026-09-06"
tags:
  - catena
  - conformance
  - specification
  - testing
aliases: []
---

# Checklist Completion Audit

## Observations

The [completion checklist](../00-inbox/language-specification-completeness-checklist.md#audited-status-and-evidence-boundary)
is the current work-ahead ledger. This audit compares all 141 item descriptions
with normative contracts, source code, tests, and historical promotion evidence.
It does not implement missing language features, amend disputed language rules,
or introduce a semantic revision.

The research baseline is commit
`104ec412d530fc18a67aa24199e467195a3b3c98`. The sibling compiler baseline is
`d7e0fcc484d3e1c3b4a292d4d3e703ddcc330535`, whose tracked working tree was
clean and whose conformance profile supports exact revisions through `0.1.48`.
The next unused semantic patch is `0.1.49`.

The old checklist contained 89 checked items, 10 partials, 40 gaps, and two
deferrals. The corrected ledger has **85 checked items, 36 partials, 18 gaps,
and two deferrals**. Four completion claims are reopened; 22 gaps are credited
with existing bounded work. No unchecked item is newly marked complete.
These counts measure item coverage, not percentage of implementation effort.

### Comprehension evidence

The `0.1.39` [conformance contract](../60-specification/list-comprehensions/diagnostics-and-conformance.md#conformance-obligations)
and its [required evidence sets](../60-specification/list-comprehensions/diagnostics-and-conformance.md#required-evidence-sets)
require executable evidence beyond generated syntax and obligation tags.

| Reopened item | Obligation | Accomplished | Missing completion evidence |
| --- | --- | --- | --- |
| P050 filter semantics | `LC-OBL-005` | Pure false-filter behavior and rejection of non-Bool filters | An effectful false filter retains its effects; a trap or handler abort stops the remaining work, with reference/BEAM agreement |
| P053 effect order | `LC-OBL-008` | Pure traversal/value agreement and generated effect-row plumbing | Real handled requests in source/filter/binding/yield positions, exact order and multiplicity across nested generators, and immediate failure timing |
| P057 sequential execution | `LC-OBL-012` | Parallel API absence and generated branch shape | Executable effect traces showing serial source order and per-element suffix completion |

The evidence gap is visible in the compiler at the audited commit:

- `test/catena/c047_list_comprehensions_test.exs:113–134` runs a pure filter
  and checks a non-Bool rejection. Despite its test name, it does not exercise
  effectful filtering or propagation of a failure.
- Lines `206–231` inspect `(case true`, `(case false`, and `(uses Ask)` strings
  and check the absence of two parallel APIs. The value named `effectful`
  contains no performed request or handler and is not checked or executed.
- `test/catena/c047_traceability_coverage_test.exs` checks obligation tags;
  it cannot establish behaviors absent from the assertions.
- A search of the complete test tree found no other comprehension execution
  suite supplying those missing effect/failure traces.

The [original C047 journal](2026-08-31-c047-comprehensions.md#evidence)
accurately describes effect-row threading and API absence as the evidence
available at promotion. That historical run remains valid evidence for those
observations. The [reopened inquiry](../40-inquiries/how-should-catena-specify-list-comprehensions.md)
now owns the missing witnesses; the normative semantics and pure elaboration
implementation remain credited.

### Selective-receive conflict

P086 is reopened for an actual conflict in the normative text. The
[scan rules](../60-specification/selective-receive/the-receive-rule-set.md#the-rules)
say rejected messages remain queued and scanning continues. The same chapter's
[starvation statement](../60-specification/selective-receive/the-receive-rule-set.md#starvation-and-cost)
says a standing rejected prefix starves the receive (`RC-OBL-004`). These
statements disagree when a later queued message matches.

The retained [C010 receive semantics](../60-specification/formal-semantic-kernel/actors-messages-and-failures.md#selective-receive)
select the first accepted message and wait only when none is accepted.
`test/catena/c010_formal_semantic_kernel_test.exs:388–420` selects `Some 1`
behind rejected `Some 0` on the stepper and compiled BEAM. The C086 blocked
mailbox fixture proves preservation when nothing matches; it does not prove
that a rejected prefix prevents selection of a later match.

Under [Specification Authority](../SPECIFICATION-AUTHORITY.md#status-and-applicability),
compiler behavior cannot resolve a normative contradiction by itself. The
[receive inquiry](../40-inquiries/how-does-selective-receive-complete.md)
is open until the controlling starvation rule is clarified against the scan
rule and its conformance evidence is aligned. This audit does not amend those
rules. The historical [C086 promotion](2026-09-01-c086-receive.md) and successful
bounded tests remain recorded.

### Existing work credited as partial

These are status corrections, not newly implemented functionality. Each wider
item remains unchecked. The normative areas and compiler test families below
were inspected at the pinned baselines.

| Current item(s) | Existing normative and executable foundation | Remaining boundary |
| --- | --- | --- |
| P084, P085, P087, P090 | [C010 actors](../60-specification/formal-semantic-kernel/actors-messages-and-failures.md), `c010_formal_semantic_kernel_test.exs` | Public process lifetime, message capacity/remote delivery, protocol state, scheduler policy |
| P094 | [C032 functions](../60-specification/functions-and-calls/README.md), C005/C010 lowering, `c032_functions_test.exs` | Complete foreign calling/callback and runtime metadata contract |
| P097 | C010 typed local PID handles and [C040 data meanings](../60-specification/built-in-data-model/README.md), C010/C040 suites | General BEAM-native value admission and foreign exposure |
| P099, P100 | [C010 backend and diagnostics](../60-specification/formal-semantic-kernel/beam-diagnostics-and-conformance.md), C003 portable guards, C005 source paths | Multi-OTP policy and full runtime/debugger source mapping |
| P101 | [C026 prelude](../60-specification/prelude-policy/README.md), C004 hierarchy, C026/C004 suites | Minimum package contents under zero implicit names |
| P104 | C017 literal decoding and C040 Text/Character/Bytes, C017/C040 suites | Grapheme, slicing, normalization/conversion and binary-pattern APIs |
| P105 | C018 numeric domains/conversion, C035 comparison, C061 operators and their suites | Numeric library, runtime-failing producers, conversions, parsing/printing, math guarantees |
| P106 | C010 Process effect and [C082 entry boundary](../60-specification/top-level-effects/README.md), C010/C082 suites | Environmental capability channel and standard APIs |
| P108 | C004 traversal/stack contracts and C028 interface compatibility, C004/C028 suites | Library-wide API/law/cost stability policy |
| P116 | C006 historical replay and C008 retained signed formats, C006/C008 suites | General schema/policy migration and long-lived evidence portability |
| P119 | [C016 documentation attachment](../60-specification/comments-and-documentation-comments/documentation-attachment-and-markdown.md), `c016_comments_documentation_test.exs` | Rendering, navigation, API views and actual doctest execution |
| P121 | C006 package compilation/staging CLI and C025 resolver/lock engine, C006/C025 suites | Full build, fetch, cache, project and offline workflow |
| P127 | [C067 exclusions and routing](../60-specification/dynamic-and-unsafe-boundaries/README.md), `c067_dynamic_unsafe_test.exs` | Foreign/native trust obligations and artifact disclosure |
| P128 | C006/C010 deterministic artifacts and C025 lock replay, including checkout-path comparison in C010 | Complete environmental inputs and packaging/build reproducibility |
| P129 | [C012 implementation limits](../IMPLEMENTATION-LIMITS.md), C034/C038 bounded meta-evaluation and their suites | Aggregate compiler/runtime capacity, mailbox pressure and denial-of-service controls |
| P130 | C006 signed artifact provenance and C025 package integrity, C006/C025 suites | Registry, yanks, compromised releases and native supply-chain policy |
| P131 | C005 capabilities, C006 pure checking, C082 no ambient launch services and their suites | Credential handling and build/foreign ambient authority |
| P135 | C004 law restrictions, C030 observable order and C047 pure equations, C004/C030/C047 suites | General rewrite inventory, checkable premises and optimizer evidence |

P093/P102/P103/P117/P133/P134/P136 remain partial with their descriptions
updated to credit existing representation, collection, outcome, diagnostic,
reference, differential, and compatibility work. C132 remains complete only
as a statement of proof targets: its
[composition lemma](../60-specification/progress-and-preservation/the-integrated-theorem.md#the-composition-lemma)
is still unproved. P109 retains the joint grammar capstone after semantic
contracts; the final research order now agrees with that explicit scope note.

### Traceability and provenance corrections

The [registry](../10-maps/conformance-traceability.md) now classifies
`LC-OBL-005`, `LC-OBL-008`, `LC-OBL-012`, and `RC-OBL-004` as partial.
There are 713 obligations: **614 traced, 78 partial, 21 untraced**.
The prior actual row statuses were 618 traced, 74 partial, and 21 untraced.
The previous validator reported four traced rows as partial because it
searched the whole row for that word rather than reading the Status cell:
`CC-OBL-017`, `CC-OBL-018`, `SG-OBL-023`, and `FC-OBL-003` contain
"partial" or "partially" in ordinary obligation prose. The validator now
reads the final status cell, with regression coverage. Historical journal
outputs retain their recorded counts; the corrected totals above use the
actual status cells.

All 713 can have registry identities without every facet being established.
The compiler's tag gates continue to pass with the current 40 allowlisted
identifiers; allowlists and registry evidence classifications are different
measures. This audit does not alter compiler tests to disguise those gaps.

The C026 commit reference was corrected to
`484d797a33eaf580f2c43ddd0776c6675078c4f9`, verified in sibling Git history.
Other checklist corrections remove obsolete section counts and completed
items described as future work, distinguish eight C140 exclusions from its
seven-point arrival gate, and preserve C044's explicit amendment route.
Current work-owner prefixes are updated in active archive prose and affected
heading links; dated journals, snapshots, and quoted executable strings keep
their historical evidence. Owner numbers for documentation rendering, text
libraries, typed outcomes, and mailbox capacity are corrected where audited.

The compiler still publishes the historical `G068/G129` capacity-owner string
in `lib/catena/conformance_info.ex`, `lib/catena/implementation_limits.ex`,
and a C012 test. The first suffix names advanced typing in today's ledger;
it is not the mailbox owner. P129 records that cross-repository correction
for the capacity-profile work. Compiler source, binaries, and tests are
unchanged by this archive audit.

## Evidence

The compiler was tested from an exact tracked snapshot in a fresh temporary
directory, preserving the sibling checkout and its build artifacts:

```bash
audit_dir=$(mktemp -d /tmp/catena-checklist-audit.XXXXXX)
git -C ../catena archive d7e0fcc484d3e1c3b4a292d4d3e703ddcc330535 | tar -x -C "$audit_dir"
cd "$audit_dir"
elixir --version
mix compile --warnings-as-errors
mix test
```

Observed environment: Elixir 1.20.2 compiled for OTP 29; Erlang/OTP 29,
ERTS 17.0.4. Compilation passed with warnings treated as errors. The full
suite passed **587 tests**, seed `147115`, in 4.4 seconds of test execution.
Test-module compilation emitted existing unused-variable/helper and static
comparison warnings; the test run was not warning-free. The initial sandbox
attempt could not acquire Mix's local TCP filesystem lock; the identical
snapshot run succeeded with that local permission available.

Archive verification:

```bash
python3 validate_archive.py
python3 -m unittest test_validate_archive.py
git diff --check
```

Archive validation passed: 574 completed documents, 60 directories, 5,957
local links, 118 source notes, and 174 normative chapters; the registry counts
are 614 traced, 78 partial, and 21 untraced. All 29 validator unit tests and
`git diff --check` passed. The count check below also passed. A diff comparison
verified that the remaining reference-only files contain intended current work-owner
prefix or affected heading-link changes; substantive checklist, inquiry,
index, registry, and provenance corrections were reviewed separately.

New immutable compiler citations were verified against the exact local Git
objects and source lines; the audited compiler commit is contained in local
`origin/rewrite`. The web fetcher returned cache misses for GitHub, so this
run does not claim a successful independent HTTP availability check.

The core item/count audit is reproducible from the research root:

```python
from pathlib import Path
import collections
import re
import subprocess

path = "00-inbox/language-specification-completeness-checklist.md"
text = Path(path).read_text()
pattern = r"^- \[([ x])\] \*\*([CGPD])(\d{3}) — (Complete|Gap|Partial|Deferred) —"
items = re.findall(pattern, text, re.M)
assert len(items) == 141
assert {int(number) for _, _, number, _ in items} == set(range(1, 142))
words = dict(C="Complete", P="Partial", G="Gap", D="Deferred")
for checked, status, number, label in items:
    assert (checked == "x") == (status == "C")
    assert words[status] == label
assert collections.Counter(status for _, status, _, _ in items) == {
    "C": 85, "P": 36, "G": 18, "D": 2,
}
baseline = subprocess.check_output([
    "git", "show", "104ec412d530fc18a67aa24199e467195a3b3c98:" + path,
], text=True)
before = {number: status for _, status, number, _ in re.findall(pattern, baseline, re.M)}
changes = collections.Counter(
    (before[number], status) for _, status, number, _ in items
    if before[number] != status
)
assert changes == {("C", "P"): 4, ("G", "P"): 22}
```

A separate deterministic audit of the checklist verifies one occurrence of
every suffix `001`–`141`, agreement between checkbox/status word/prefix,
the complete per-section count table, and the exact intended status changes
relative to the research baseline. Link validation covers updated owner
heading fragments and reopened-inquiry connections. Successful structural
validation does not resolve the four substantive completion gaps above.

## Follow-ups

1. Supply P050/P053/P057's actual effectful reference/BEAM witnesses and fix
   any behavior those tests expose, then reassess their checkbox and registry
   statuses together.
2. Resolve P086's normative conflict through the specification-authority
   workflow and verify both rejected-prefix bypass and true waiting cases.
3. Continue the remaining runtime, interoperability, and library contracts;
   preserve P109's semantics-first capstone sequencing.
