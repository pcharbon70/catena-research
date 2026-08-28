---
title: "C037 Resource Observability"
kind: journal
created: "2026-08-26"
tags:
  - catena
  - conformance
  - observability
  - identity
  - specification
  - testing
aliases:
  - "C037 observability evidence"
---

# C037 Resource Observability

## Observations

Checklist item G037 is complete as C037 and normative source-only
language revision `0.1.33`, the fourth Section 4 partial to close and
the deferred-exclusion sweep's completion. The completed boundary
fixes: the six-way classification — allocation addresses, sharing,
garbage collection, and object identity (except process identity)
unobservable; stack use observable only through completion versus
the tail guarantee; finalization declared absent with its gate
(resource-scope and foreign eras); semantic identity — equal values
interchangeable, representation never changing meaning, storage
observing nothing; the two-clause identity rule — process identity
the only identity-bearing value (fresh per spawn, kernel operations
only, never comparable), closing C032's and C035's deferrals; and
the debugging-channel statement — tools observe the implementation
from outside program semantics (G124's channel). Zero new diagnostic
families and no new public API.

Three implementation decisions worth recording. First, the
**rationale conversation preceded the slice**: the developer asked
why non-observability was chosen and whether debugging suffers —
the answer (semantic sufficiency: `equal` is complete; compiler
freedom: sharing, unboxing, deduplication, CPS, GC movement;
determinism and portability; and debugging observing the
implementation, not the language) is recorded in the synthesis as
the contract's "why" rather than left as folklore. Second, the
**identity witness composes the C010 spawn shape**: two `spawn Echo`
calls produce two `Echo` processes with distinct pids in the outcome
record, each terminating with an empty mailbox after consuming its
own message — fresh identity per spawn observed through
kernel-legitimate means only (the outcome record), never by
comparing handles with `equal`, the very operation the contract
forbids; process receive bodies must return Unit per the kernel (the
first draft's `(var message)` body failed typing — the fixture's
`(unit)` shape is the legal spelling). Third, the **classifier
correction**: the first draft asserted records (`%{label: 1}`) are
non-comparable — wrong under C035, whose structural recursion
includes records with comparable contents; the corrected witness
asserts a record containing a closure is non-comparable while a
record of integers compares, which is exactly the semantic-identity
claim (contents observable, allocation never).

The sibling compiler implementation is commit
[`734aafeb3d1739af7d85b021a8fc7b1569b39c20`](https://github.com/pcharbon70/catena/commit/734aafeb3d1739af7d85b021a8fc7b1569b39c20)
on branch `agent/c037-observability`, pending compiler PR and research
promotion following the established publication order (the PR links
are backfilled at publication).

## Evidence

The compiler registers revision `0.1.33` (`LanguageVersion` feature
`resource_observability`, static-meaning lifecycle change with
migration note) and adds the `guides/language/observability.md`
guide; the evidence is `c037_observability_test.exs`.

Focused verification:

```text
mix test test/catena/c037_observability_test.exs \
  test/catena/c037_traceability_coverage_test.exs
Result: 9 passed
```

Complete compiler verification during implementation:

```text
mix format --check-formatted
mix clean
mix compile --warnings-as-errors
mix test
Result: 444 passed
mix escript.build
git diff --check
```

The focused corpus covers exact selection, lifecycle registration, and
pinned predecessor defaults; distinct-site constructor-value equality
agreeing on evaluator and BEAM; a let-bound closure applied twice
yielding equal results regardless of allocation; the two-spawn
process-identity witness (distinct pids, terminated, mailboxes
consumed); handle and closure non-comparability with
records-of-integers comparable (the corrected classifier partition);
the absence matrix (no address, identity, shared, gc, finalize, or
stack-depth entry points); the stack boundary (non-tail recursion at
10,000 depth completing on BEAM — completion is the only
observation); and determinism.

Archive verification after the complete connected bundle and indexes:

```text
python3 validate_archive.py
python3 -m unittest test_validate_archive.py
git diff --check
```

Results are recorded in the promotion commit.

## Version and boundary decision

C037 consumes `0.1.33` for the classification, the identity rule,
the finalization absence, and the debugging-channel statement; it
adds no JSON AST version, kernel S-expression version, interface
version, artifact version, signature domain, typing rule, runtime
behavior, BEAM representation, manifest field, public API name, or
diagnostic family, and amends no retained revision. Every
predecessor API retains its exact selection. The next unused
semantic patch is `0.1.34`.

## Threads

- G080s/G084 own resource scopes, cleanup, and handle operations
  beyond the kernel's; G085 message-copy details; G095 foreign
  finalization; G124 debugging tools consuming the trace anchors.

## Follow-ups

Section 4's remaining partials: G038 (compile-time evaluation, gated
by C034's entry rule) and P041 (structural records and variants —
Section 5's edge). The decision route is preserved in the
[observability synthesis](../20-notes/catena-resource-observability.md)
and the [topic map](../10-maps/resource-observability.md).
