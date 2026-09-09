---
title: "Foreign Adapter Implementation"
kind: journal
created: "2026-09-09"
tags: [language-design, foreign-boundary, algebraic-effects]
aliases: []
---

# Foreign Adapter Implementation

## Starting point and scope

C095 merged through [compiler PR 142](https://github.com/pcharbon70/catena/pull/142)
and [research PR 92](https://github.com/pcharbon70/catena-research/pull/92).
Both integration branches were synchronized before their feature branches were
deleted. Compiler `rewrite` was `8d37d1dd4c8973e54ac5cbf651cb854bd57b0a80`;
research `main` was `954feb6408f9202fdd63cc462f8e129dbf586951`.
This work uses `codex/foreign-adapters` in both repositories. The user approved
all semantic revision updates for this session; this milestone uses `0.1.61`.
No continuation is scheduled.

The [CP-096 plan](../20-notes/language-completion-plan-delivery.md#item-096-foreign-calls-and-callbacks)
selects typed capability-bound declarations, visible foreign effects, scoped
callbacks and honest cooperative cancellation. Its original forks are in the
[decision register](../20-notes/design-decision-register.md). The
[normative milestone](../60-specification/foreign-adapters/authority-calls-and-callback-lifetime.md)
implements a retained-input adapter profile. P096 remains partial: public syntax,
full environmental provisioning and general effectful/resource-capturing callbacks
are not claimed complete.

## Implementation decisions

| Decision | Four alternatives explored | Recommended and selected |
| --- | --- | --- |
| FA-I01 | A: payload-selected MFA; B: typed descriptor plus actual host digest; C: ambient arbitrary fun; D: fixed compiler whitelist. | **B.** Keeps codec, effect, trust and identity choices in explicit setup. |
| FA-I02 | A: global Boolean permission; B: complete descriptor grants; C: ambient dictionary authority; D: infer permission from visibility. | **B.** Exact grants separate foreign invocation from data conversion. |
| FA-I03 | A: caller-process execution; B: owned BEAM worker; C: detached worker; D: fixed global worker pool. | **B.** The owner can observe and end blocking work without inventing native isolation. |
| FA-I04 | A: claim rollback after kill; B: cooperative control and explicit possible effects; C: retry every timeout; D: ignore cancellation. | **B.** Both cancellation and completion-after-request are honest outcomes. |
| FA-I05 | A: raw host fun callbacks; B: verified pure Catena entry with typed immutable captures; C: global immortal closures; D: one-shot callbacks only. | **B.** Supports retained asynchronous invocation under a concrete scope while keeping future effectful authority explicit. |
| FA-I06 | A: arbitrary overlapping reentry; B: reject overlap per registration; C: unbounded queue; D: implicit serialization. | **B.** Avoids hidden reentry and callback queue deadlocks; separate registrations remain independently usable. |
| FA-I07 | A: detach outstanding work; B: C080 bounded release plus worker termination evidence; C: report rollback; D: wait forever for voluntary host return. | **B.** Cleanup preserves prior effects and handles a stalled manager through the existing release deadline. |
| FA-I08 | A: invent source syntax; B: checked retained capability core plus explicit binding sidecar; C: forge a pure core; D: mutate old artifact formats. | **B.** The operation row remains checked and visible; public vocabulary stays open. |
| FA-I09 | A: independent capture-budget resets only; B: whole capture/argument vector preflight plus typed checks; C: unbounded captures; D: forbid captures. | **B.** Preserves useful closures without hiding aggregate validation cost. |
| FA-I10 | A: name-only lookup; B: check pinned module digest before entry; C: silently accept code upgrades; D: require immutable global preload forever. | **B.** Replaced host code invalidates its declaration while allowing explicit re-declaration. |
| FA-I11 | A: reload callback binary at every entry; B: reuse identical loaded code only after full artifact verification; C: trust the module name; D: purge unrelated code globally. | **B.** Avoids needless code-version churn during concurrent registrations and retains exact artifact checks. |
| FA-I12 | A: propagate every native exception term; B: budget diagnostic reasons and classify unrepresentable ones; C: erase every trap; D: return exceptions as successful data. | **B.** Preserves representable Catena trap identity without smuggling unchecked native handles. |
| FA-I13 | A: polling every millisecond; B: manager waiters with a bounded timer; C: unbounded synchronous wait only; D: timeout automatically cancels and retries. | **B.** Wait expiry reports pending and does not repeat effects. |

## Execution evidence

`Foreign.Descriptor`, `Control`, `Callback`, `Session` and `Adapter` implement
explicit host grants, whole-vector data checks, scoped callback publication,
owned worker execution, cooperative checkpoints and terminal outcomes.
`Foreign.Program` and `Lowering` connect a checked C050 effectful entry to its
exact host bindings, with interface-owned descriptor builders and effect-runtime
conversion. The explicit artifact uses `0.1.61`; retained codecs, calling binaries,
core and serialized interfaces keep their original version axes.

The callback profile admits pure unary results after typed data captures. Host
recipients can invoke a retained callback from another process. Overlap on one
registration is refused; revocation blocks later ingress, and scope exit releases
a caller waiting on a nonterminating pure callback. It does not admit arbitrary
host closures or captured resource/capability handles.

Tests exercise matching/denied grants, wrong arguments and results, host raises,
code replacement, forged artifacts, captured callback types, cross-process
invocation and owner denial, expiry, overlap, operation capacity, cooperative
cancellation, completion despite cancellation, owner death and stalled cleanup.
An actual compiled capability request returns 42 with a visible foreign request
and outcome trace. The scope's manager retains ordered per-operation evidence;
C080 traces bounded mandatory release separately.

## Validation and remaining gate

Initial full-suite promotion exposed stale revision-discovery expectations; they
were corrected without widening retained codecs or serialized formats. After
bounded-release integration, the focused trace assertion was updated to include
C080's existing resource events. Review also found that the compiled bridge's
outer host catch needed to preserve C080's reserved cancellation signal; a
compiled cancellation witness now checks that it survives bounded cleanup.
Diagnostic witnesses distinguish a host throw, untrappable worker kill, preserved
Catena trap and unrepresentable native-reference failure.

The full suite passed 880 tests before the final cancellation witness; the final
run, production checks and archive totals are recorded below before commit.

P096 remains partial under its reviewed gate. The milestone is useful executable
infrastructure for P097/P106/P131, not a claim of general callback effects,
application authority provisioning, native crash containment or public syntax.

Final verification passed **880 tests**, including all 13 foreign-adapter tests
and the final compiled cancellation witness. Production
`MIX_ENV=prod mix compile --warnings-as-errors` and
`MIX_ENV=prod mix escript.build` passed. Archive validation passed with 622
documents, 73 directories, 121 source notes, 187 specification chapters and
827 obligations (732 traced, 74 partial, 21 untraced). Both diffs passed
`git diff --check`. Checklist counts remain 99 complete, 27 partial, 13 gaps
and two deferred; P096 is still partial.

Compiler implementation commit: `c04ed35abbbc7b736d458f7dbbe30699ce6db457`.
