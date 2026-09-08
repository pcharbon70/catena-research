---
title: "Language Completion Plan and First Implementation"
kind: journal
created: "2026-09-06"
tags:
  - catena
  - language-design
  - conformance
  - testing
  - decision-log
aliases: []
---

# Language Completion Plan and First Implementation

## Observations

The user requested a detailed plan covering the complete checklist, at least
four explored alternatives for each decision, and autonomous selection of
the answer the agent would recommend. The user also authorized beginning
implementation after planning, while holding public language vocabulary.
The [plan](../20-notes/language-completion-plan.md) records this scope and
its dependency order; the
[decision register](../20-notes/design-decision-register.md#language-completion-plan-2026-09-06)
distinguishes these delegated selections from historical per-fork user choices.

The research baseline is `d93a655eae07c9e0dc539eff07487c4326d05eea`;
the sibling compiler baseline is
`d7e0fcc484d3e1c3b4a292d4d3e703ddcc330535`. Both working trees were clean
when planning began. The previous audit PR is separate from this work; the
research working branch is `codex/language-completion-plan`.

Initial source inspection found that the comprehension elaborator's
`fn_type/3` annotates every generated worker arrow with an empty latent
effect row. The existing evidence test inspects generated text containing
`(uses Ask)` but never checks or executes a performed request. This is a
specific implementation hypothesis at planning time. The subsequent
experiments below distinguish its confirmed symptoms from the deeper
normative target dependency.

## Planning gate

The plan has a hub and three item volumes, linked through the
[language completion map](../10-maps/language-completion.md). Planning is
complete only when all 001–141 item sections, four-option decisions,
dependencies and acceptance gates are present, the register preserves every
fork, and the archive validates. Implementation results will be recorded
below only after that gate passes.

**M0 passed before implementation began:** 141 unique item sections, 392
unique decisions and 1,568 alternatives. The volumes contain 92, 137 and
151 decisions respectively; the hub adds 12. Every completed item has at
least two decisions and every unfinished item at least three. All rows
identify a selected recommendation and occur verbatim once in the decision
register. Archive validation passed with 581 completed documents, 60
directories, 6,584 local links and the unchanged 713-obligation ledger;
`git diff --check` passed.

Independent planning review corrected circular foreign-call/capability
dependencies, separated service-authority descriptors from lexical capability
names, and added explicit choices for duplicate keys, integer division,
transcendental admission, cleanup failures, child lifetimes and supervisor
restart limits. The vocabulary hold, human usability evidence and unproved
composition lemma remain real gates. No compiler implementation or checklist
completion was claimed from the planning result.

## Evidence

Baseline inspection used `git status --short` in both repositories and read
the current checklist, audit, governing policies, focused research and
compiler sources. The first slice was applied to the actual sibling
checkout after its clean baseline was rechecked; the final verification
and working-tree source identities below make these observations reproducible.

## First implementation findings

The initial performed-request comprehension fails kernel checking with
`T002`, “definition effects do not match its uses row”: its pure `xs`
context is assigned declared `["Log"]` while its actual row is empty.
The original generated-string assertion therefore does not establish a
well-typed effectful module. Annotating workers alone cannot finish the repair.

The normative dependency is between
[C005 hybrid row equality](../60-specification/effects-and-handlers/capabilities-rows-and-selection.md#hybrid-row-equality),
which coalesces repeated use of one concrete capability identity, and
[C010's exact row grammar](../60-specification/formal-semantic-kernel/canonical-kernel-syntax.md#types-and-expressions),
which retains ordinary occurrences. C010
[removes one occurrence when handling](../60-specification/formal-semantic-kernel/static-semantics-and-elaboration.md#functions-schemes-recursion-and-effects).
C047 nevertheless names that exact kernel as
[its lowering target](../60-specification/list-comprehensions/elaboration-and-lowering.md#the-qualifier-tree-target)
while requiring C005
[effect-row union and repetition](../60-specification/list-comprehensions/evaluation-effects-and-execution.md#effect-rows).

For a worker performing `q > 0` escaping requests and recursively using an
ordinary row with multiplicity `m`, the current checker requires at least
`m = q + m`. No finite nonnegative `m` satisfies that equation. Concrete
probes with 0–4 declared occurrences all reject with `T002`, “function effect
rows are incompatible.” The new `kernel_effect_row_boundary_test.exs`
retains these samples and proves that two ordinary requests still require
two occurrences. The equation is the argument for arbitrary finite `m`;
five samples alone are not such a proof.

This limitation concerns escaping ordinary effects. Fully locally handled
requests have an empty residual row, and reserved Process effects coalesce.
Moving an enclosing handler into each iteration is not a general solution:
it changes handler lifetime, state, return and abort scope. CP-I04 and CP-I05
therefore preserve the current exact revision and select a versioned kernel
refinement as the next semantic dependency. No normative text or language
revision changes in this first implementation.

The independent backend defects disagree with the existing
[function/partial-application contract](../60-specification/formal-semantic-kernel/static-semantics-and-elaboration.md#functions-schemes-recursion-and-effects)
and [handler dynamics](../60-specification/formal-semantic-kernel/sequential-dynamics.md#traits-and-handlers):

- Valid multi-level global forwarding returns 42 in the reference but loses
  the installed handler on BEAM. A declining handler should return 99 and
  discard the pending trap/addition, but forwarding also loses that handler.
- Valid curried calls return an intermediate closure on BEAM instead of
  delivering it to the next continuation and producing 42.
- Valid function aliases return 42 in the reference but trap with an
  unhandled request on BEAM. Their declared callable arity exceeds their
  syntactic lambda count, exposing both classification and worker adaptation.

The repair uses verified ordinary evaluation and callable result rows to
select CPS. Callable values follow each immediate arrow's checked effect
row, preserving the convention across construction contexts and polymorphic
result instantiation. Private value factories preserve definition lookup
and application stages where a saturated worker would delay effects or
traps. Only a complete syntactic lambda chain retains that shortcut;
public export arities remain unchanged. CP-I09 replaces the intermediate
CP-I06 residual-worker adapter, and CP-I10 refines CP-I08's representation
choice; their original alternatives remain recorded below.

Independent review caught a pure-callback `badarity` regression despite
the intermediate full suite's 612 passing tests. It also reproduced an
older early-stage request escaping its partial-application handler. New
regressions cover both, plus global/anonymous callbacks, callbacks stored
in records or returned by functions, polymorphic callable results,
declines and traps before later argument evaluation, and definition lookup
before its first argument. Pure and Process-only paths without effect
control retain direct lowering. Forged typed-core effects still reject
with `I001`; no verifier or effect-row normalization changes are made.

The new `c047_effects_completion_test.exs` uses the existing comprehension
input shape. It performs real locally handled requests in every expression
role. Both execution paths return `[110, 310, 320]` for nested traversal with
an empty inner source and a false filter, with this independently derived
request trace:

```text
100, 201, 311, 411, 511, 312, 202, 203, 331, 431, 531, 332, 432, 532
```

The outer source occurs once; inner sources occur once per outer prefix;
filter 312 performs its request while skipping its binding/yield suffix;
source 202 evaluates but has no elements. Eight first/last source, filter,
binding and yield traps stop at the expected prefix, and a trap in the
would-be false filter propagates. An empty outer list still performs its
source request. A separate local decline case returns a replacement filter
value and continues traversal, explicitly demonstrating its narrower scope.
These are 12 tests, not evidence for a whole-comprehension handler abort.

The stepper exposes actual request events. Compiled BEAM executes a pure
fixture observer called by the handler; test-only OTP tracing records calls
and arguments in an isolated trace session. A delivered-message barrier
finishes collection before worker and module cleanup. There are no sleeps,
production logging hooks, or invented compiler trace events. The
[OTP trace API](https://www.erlang.org/doc/apps/kernel/trace.html)
was checked against the installed OTP 29 interface. Pure existing examples
now execute on BEAM as well as the stepper; the old generated-row assertion
is named as a structural check, and coverage tags are described as an
inventory rather than a completion proof.

P050/P053/P057 and `LC-OBL-005`/`LC-OBL-008`/`LC-OBL-012` remain partial.
The checklist retains 85 complete, 36 partial, 18 gaps and two deferrals;
the obligation ledger retains 614 traced, 78 partial and 21 untraced. The
remaining gate is the versioned target, independently checked row threading,
and general enclosing-handler observations, not another vocabulary choice.

## Implementation decisions

These refinements instantiate CP-053-5 after the planning gate. They are
agent-selected recommendations under the same delegation, recorded before
the dependent implementation. The names below are dormant compiler metadata,
not new Catena source vocabulary.

| Decision | Four explored alternatives | Selected recommendation |
| --- | --- | --- |
| CP-I01 | A: keep fragment rows beside their expressions using qualifier `uses`, `yield_uses`, and an optional fourth context-tuple field, retaining pure legacy inputs; B: maintain an index-keyed external row table, centralized but fragile under qualifier edits; C: introduce a general expression-inference API, automatic but a larger kernel interface change; D: reuse one aggregate row everywhere, small but imprecise and vulnerable to recursive self-justification. | **A, recommended and agent-selected.** It realizes the existing typed qualifier-tree contract with local evidence and preserves the old pure-input shape. The aggregate `uses` row must equal the union of qualifier and yield rows. |
| CP-I02 | A: independently check explicitly annotated fragments in nonrecursive probes before emitting workers, while leaving legacy pure inputs' existing validation stage intact; B: move all old typing failures into elaboration immediately, simpler but broadens compatibility changes; C: check only the recursive generated module, easy but overdeclared recursive rows can justify themselves; D: trust supplied fragment rows, fastest but not conformance evidence. | **A, recommended and agent-selected.** Probe definitions are temporary checking artifacts, omitted from emitted code; diagnostics retain the source qualifier/context path and existing family. Closure construction and the final reverse pass stay pure. |
| CP-I03 | A: invoke each intermediate curried CPS stage's continuation with the next closure, retaining the final caller's handler environment; B: force eager saturation, losing valid partial applications; C: box every function behind generic runtime dispatch, broadening the representation change; D: omit the partial-call witness, leaving an observed defect in valid programs. | **A, recommended and agent-selected.** A valid curried forwarding program returns a closure instead of its expected integer on BEAM while the reference evaluator returns the integer. Repair continuation delivery without changing the language's calling convention. |
| CP-I04 | A: preserve C010's multiplicity contract, repair valid backend forwarding and add real locally handled comprehension observations now, then require an explicit kernel refinement before general escaping-effect workers; B: deduplicate ordinary family names in the existing kernel, breaking its normative multiplicity and distinct-capability contract; C: advertise locally handled tests as general effect completion, overstating both abort scope and row support; D: stop all implementation until a complete new kernel exists, delaying independently valid repairs and evidence. | **A, recommended and agent-selected.** The first implementation remains bounded and the comprehension items remain partial. CP-I01 and CP-I02 are deferred before code changes: their row representation and validation probes must be revisited after the kernel's capability-identity interface is settled. No annotation alone solves a recursive exact row that must contain itself plus another ordinary occurrence. |
| CP-I05 | A: deduplicate ordinary family names in retained C010, violating multiplicity and identity distinctions; B: specify a new kernel revision with C005-compatible capability identities, recursive row checking, explicit comprehension-target applicability and independent verification; C: retarget to the earlier identity-aware C005 core, reusing effects but requiring data, trap, recursion and origin compatibility work; D: encode requests as pure data or unroll known lists, useful experimentally but insufficient for arbitrary-list fused workers. | **B, recommended and agent-selected for the next semantic slice.** Preserve exact `0.1.8`; settle the new row, handler-subtraction, interface and verifier contracts before adapting the elaborator. This journal proposes the direction, not an already normative revision. Allocate the next unused semantic patch at that slice's start; no patch is consumed here. |
| CP-I06 | A: classify ordinary latent rows on the checked callable result spine and adapt residual callable expressions to the declared worker arity, preserving handler/continuation forwarding; B: resolve only syntactic aliases to ultimate globals, missing let-produced or partially applied callables; C: CPS-convert every function-valued definition, broadening the pure-path change; D: leave a known valid alias failure open, limiting the repair despite an independently reproducible defect. | **A, recommended and agent-selected.** An effectful function alias checks and returns 42 in the reference but traps with an unhandled request on BEAM. Classification alone is insufficient because the existing worker counts only syntactic lambda parameters. Preserve checked arity while evaluating the residual callable once and applying remaining arguments in order. |
| CP-I07 | A: after the trace worker exits, delete the current generated module and then purge its old code; B: purge, delete and purge again, correct but redundant for the fresh fixtures; C: only delete the module, leaving old code resident; D: retain the existing purge-then-delete order, preserving a demonstrated cleanup defect. | **A, recommended and agent-selected.** Independent review reproduced retained old code after the previous order. Apply the correction to the new and newly changed execution helpers; test fixture cleanup must not leave compiled code behind. |
| CP-I08 | A: choose callable value representation from verified callable result-spine types across both lowering modes, using unary values for pure/Process-only callables and CPS values for ordinary latent effects, with type-directed application stages; B: generate direct and CPS versions of every reachable global, requiring reachability analysis and escaping-value wrappers; C: adapt recursively at every calling boundary, including higher-order results and containers, substantially enlarging the adapter surface; D: narrow classification or special-case ignored function values, hiding one regression while restoring the valid alias failures. | **A, recommended and agent-selected.** Independent review found that a pure callback created in CPS was passed as a three-argument function to a direct caller expecting one argument. The reviewed program returned 42 before the patch but failed with `badarity` after it. Keep representation determined by checked type rather than construction context, and add cross-mode callback/container regressions before accepting the repair. |
| CP-I09 | A: use private value factories to evaluate actual unary function stages, preserving public callable arity and retaining a saturated shortcut only where the checked expression justifies equivalent evaluation; B: change every public callable to a unary ABI, breaking the established export contract; C: reject effects before the final curried stage, contradicting admitted function types; D: defer the observed staging defect and limit the patch to final-stage effects, honest but leaving a concrete violation in the same calling boundary. | **A, recommended and agent-selected.** A first-stage request handled during partial application is incorrectly delayed until the returned function is called outside that handler. Preserve source evaluation stages, including effects or traps before later argument evaluation, without changing source syntax, effect-row semantics or public exports. This is an implementation correction to the existing unary application contract. |
| CP-I10 | A: choose each callable stage's representation from its immediate effect row, handling any returned callable at its own stage; B: specialize representation by the fully instantiated result spine, adding runtime-convention specialization to polymorphic calls; C: box all polymorphic callable results behind generic dispatch, broadening the representation and erasure change; D: reject polymorphic functions returning callables, withdrawing admitted function composition. | **A, recommended and agent-selected.** Refine CP-I08's representation rule: a pure stage returning abstract `a` must keep the same unary convention when `a` instantiates to an effectful function. The returned function carries its own convention. Definition-body CPS classification can still inspect the result spine; value representation must remain invariant under result-type instantiation. |

The implementation workspace is an exact `git archive` of the pinned sibling
commit at `/tmp/catena-completion-implementation.ay5Dvp`. Changes were developed
and tested there, then applied to the actual sibling checkout after verifying
that its baseline and unrelated changes had not moved. Final checks ran in
`/home/ducky/code/catena` on `codex/language-completion-plan`. The research
checkout uses the same branch name. Both change sets remain uncommitted;
no new PR, push or normative promotion is part of this slice.

## Final implementation verification

The compiler toolchain was Elixir `1.20.2` and Erlang/OTP `29.0.4`
(ERTS `17.0.4`), matching `.tool-versions`. The untouched compiler baseline,
run from `/tmp/catena-completion-baseline.43hi124l` with
`mix test --seed 0`, passed **587 tests**. Initial focused regressions
reproduced forwarding failures, lost continuations and alias failures before
repair; independent review then reproduced the callback and early-stage
failures described above.

The final sibling checkout passed these commands:

```bash
mix format --check-formatted
mix clean
mix compile --warnings-as-errors
mix test --seed 0
mix escript.build
git diff --check
```

The full result is **624 passed**: 23 new backend call/handler tests,
12 new comprehension request/failure tests, two exact-row boundary tests,
and the 587 pre-existing tests. The existing pure comprehension helper now
also executes its examples on BEAM. Clean production compilation passed
with warnings treated as errors; the test suite still emits existing
fixture warnings. The final targeted run passed 67 tests; an independent
review reran all 23 backend regressions with seed `969468` and confirmed that
both its original callback and staging probes now return 42 on reference
and BEAM. No further concrete defect was found within that reviewed boundary.

All 11 intended compiler files were byte-compared with the tested snapshot
after application. The compiler's README, language tour, conformance profile,
comprehension guide and OTP-lowering guide now state the implemented scope
and remaining effect-row dependency. Generated escript output was removed
when newly created, or the pre-existing artifact restored; only intended
source, test and documentation changes remain in Git status.

Because the implementation is uncommitted, these SHA-256 identities bind
its executable evidence to the working-tree files instead of pretending
that the baseline commit contains the new code:

| Compiler-relative file | SHA-256 |
| --- | --- |
| `lib/catena/kernel/backend.ex` | `6e3c88f27fab8b222468c7a6cfeb93e13c41131525eb5734d4952846c2596456` |
| `test/catena/c047_effects_completion_test.exs` | `42fc016ca501438717a25936239129a900a7a1b91a470b52e0e72884f32eef2b` |
| `test/catena/c047_list_comprehensions_test.exs` | `542368f24fcef3ed4473666bdbf705ea728c84602094f4ba7fdef54e44d81742` |
| `test/catena/c047_traceability_coverage_test.exs` | `da362fd75df704a8cbfc5d752d5ff4fab4cdcda5eeefa56211dea3131db1177a` |
| `test/catena/kernel_effect_row_boundary_test.exs` | `c0c58220d8e99540ad4e6ae52c84b70eb944a9105ece595e74f1e5751cae4670` |
| `test/catena/kernel_transitive_effects_test.exs` | `2ea10444afb4ac9c9653014b49c291548f8e933c593649980bb1cfcfc58f7bdb` |

The research bundle includes the hub, three plan volumes, decision-register
entry, completion map/inquiry and this journal. Directory inventories and
active comprehension notes/maps/inquiries/traceability notices were updated
atomically. The final planning check still verifies 141 items, 392 original
decisions and 1,568 alternatives; this journal separately records ten
implementation refinements with four alternatives each. No checkbox or
obligation status was promoted from the bounded new witnesses.

Final archive validation passed: 581 completed documents, 60 directories,
6,597 local links, 118 source notes, 174 specification chapters and 103
classified fenced blocks. All 713 obligation statuses retain the totals
reported above. The research `git diff --check` also passed.

## Reproducing the planning gate

Run from the research repository root. This checks the audited baseline
rather than treating later completion-prefix changes as new item identities.
It also checks the verbatim register copies, so the selected alternatives
cannot silently diverge between the volumes and their decision record.

```bash
python3 validate_archive.py
git diff --check
```

The coverage check used for M0 is reproduced in full:

```python
from pathlib import Path
from collections import Counter
import re

root = Path.cwd()
notes = root / '20-notes'
volumes = [
    ('language-completion-plan-foundations.md', 1, 46),
    ('language-completion-plan-semantics.md', 47, 92),
    ('language-completion-plan-delivery.md', 93, 141),
]
# The coverage standard is assessed against the audited planning baseline.
import subprocess
baseline = subprocess.check_output(
    ['git', 'show', 'd93a655:00-inbox/language-specification-completeness-checklist.md'],
    cwd=root, text=True,
)
statuses = {int(n): s for s, n in re.findall(r'^- \[[ x]\] \*\*([CPGD])(\d{3}) —', baseline, re.M)}
all_rows = []
seen_items = []
for filename, first, last in volumes:
    body = (notes / filename).read_text()
    sections = list(re.finditer(r'^## Item (\d{3}) — (.+)$', body, re.M))
    numbers = [int(m[1]) for m in sections]
    assert numbers == list(range(first, last + 1)), (filename, numbers)
    seen_items.extend(numbers)
    for i, match in enumerate(sections):
        section = body[match.end():sections[i + 1].start() if i + 1 < len(sections) else len(body)]
        rows = re.findall(r'^\| CP-\d{3}-\d+ \|.*$', section, re.M)
        number = int(match[1])
        assert len(rows) >= (2 if statuses[number] == 'C' else 3), (number, len(rows))
        assert all(row.startswith(f'| CP-{number:03d}-') for row in rows), number
        for row in rows:
            # Volume tables enumerate A–D within the alternatives cell.
            cells = re.split(r'(?<!\\)\|', row)
            assert len(cells) == 9 or all(re.search(r'\b' + option + r'\s*:', row) for option in 'ABCD'), row
            assert 'recommend' in row.lower() and 'select' in row.lower(), row
        assert 'depend' in section.lower() or 'interface inputs' in section.lower(), number
        assert 'implement' in section.lower() or re.search(r'^1\.', section, re.M), number
        assert any(word in section.lower() for word in ['evidence', 'acceptance']), number
        assert any(word in section.lower() for word in ['gate', 'closure']), number
        all_rows.extend(rows)
assert seen_items == list(range(1, 142))
hub = (notes / 'language-completion-plan.md').read_text()
hub_rows = re.findall(r'^\| CP-G\d+ \|.*$', hub, re.M)
assert len(hub_rows) >= 11
for row in hub_rows:
    assert len(re.split(r'(?<!\\)\|', row)) == 8, row
    assert 'recommended; selected' in row, row
all_rows.extend(hub_rows)
ids = [re.search(r'CP-(?:\d{3}-\d+|G\d+)', row)[0] for row in all_rows]
assert len(ids) == len(set(ids)), Counter(ids)
register = (notes / 'design-decision-register.md').read_text()
for row in all_rows:
    assert register.splitlines().count(row) == 1, row
assert len(re.findall(r'^\| CP-(?:\d{3}-\d+|G\d+) \|', register, re.M)) == len(all_rows)
print(f'Plan validation passed: 141 unique items, {len(all_rows)} unique decisions, four alternatives and a selected recommendation per decision; every row preserved verbatim in the decision register.')
print('Per-volume decisions:', {name: len(re.findall(r'^\| CP-', (notes / name).read_text(), re.M)) for name, _, _ in volumes})
```

## Follow-ups

- Specify CP-I05's versioned capability-identity kernel target, including
  recursive rows, subtraction, interfaces and independent verification;
  revisit CP-I01/CP-I02 only after that prerequisite is settled. Then
  implement general 050/053/057 workers and enclosing-handler witnesses.
- Keep the [receive inquiry](../40-inquiries/how-does-selective-receive-complete.md)
  open until its explicit normative repair and evidence are complete.
- Keep the [cross-item inquiry](../40-inquiries/how-can-catena-complete-its-language-definition.md)
  open through runtime integration, public adoption and release validation.
