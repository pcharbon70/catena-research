---
title: "2026-09-10 Message Semantics"
kind: journal
created: "2026-09-10"
tags: [specification, concurrency, runtime, foreign-boundary]
aliases: []
---

# 2026-09-10 Message Semantics

## Scope

Execute [P085](../20-notes/language-completion-plan-semantics.md#item-085-messages-capacity-and-transport-p085)
after C091 compiler merge `c04d047edcee4aa62e4f3028bb85f31fbd6e50a3`.
Revision `0.1.77` is covered by the user's session-wide approval. CP-085-1..5
retain their recommended selections.
Compiler PR [159](https://github.com/pcharbon70/catena/pull/159) merged feature
commit `ffe6ccc0cb795b46f0b3243f4e196077efe9b069` as
`2a5592f73d1488a7b9ddda0b7bbdb286e476f61a` into `rewrite`.

## Implementation decisions

Each implementation fork compares four alternatives and selects the
recommendation.

| Decision | Four alternatives | Recommended and selected |
| --- | --- | --- |
| MS-I01 Integration shape | A rewrite kernel send; B one checked boundary composing existing contracts; C documentation only; D host send everywhere | B: composition closes the gap without changing established local semantics or public vocabulary. |
| MS-I02 Message descriptor | A payload selects type; B trusted exact codec; C runtime shape guessing; D arbitrary ETF | B: the declared codec owns type and nominal identity before any payload is inspected. |
| MS-I03 Snapshot | A enqueue original unchecked term; B checked encode/decode round trip; C deep-copy every byte manually; D serialize a closure | B: the existing bidirectional codec validates the whole immutable observation and rejects unsupported carriers. |
| MS-I04 Physical storage | A require copies; B permit unobservable copy or sharing; C expose pointer equality; D share mutable buffers | B: semantics stay representation-independent while BEAM immutable data can remain efficient. |
| MS-I05 Checked local result | A processing acknowledgement; B Unit after validation and send; C target liveness Boolean; D implicit retry | B: it preserves C010 and avoids a racy or blocking promise. |
| MS-I06 Invalid local payload | A send then diagnose; B reject before send; C coerce; D silently drop with Unit | B: the receiver observes nothing and the caller receives the codec failure. |
| MS-I07 Capacity ordering | A count before validation; B validate before queue accounting; C queue then roll back; D bypass capacity for invalid values | B: rejected types consume no message/byte capacity and cannot perturb admitted work. |
| MS-I08 Producer order | A global deterministic sender order; B per-sender order with cross-sender interleaving; C no order; D sort payloads | B: it retains actor semantics without importing scheduler timing into meaning. |
| MS-I09 Foreign mutation | A share mutable host object; B convert to a checked semantic snapshot; C trust host annotations; D forbid all foreign data | B: later host mutation cannot alter the admitted message while useful immutable data remains supported. |
| MS-I10 Native handle transfer | A ordinary data codec; B registered send-only authority; C raw PID; D prohibit useful process integration | B: scope, role, codec and operation budgets remain checked for every send. |
| MS-I11 Remote integration | A pretend Unit means delivery; B inherit C091's three outcomes; C exactly-once; D permanent remote ban | B: the outcome communicates only facts supported before, during, or after transport admission. |
| MS-I12 Evidence | A new tests only; B focused composition plus retained subsystem and full-suite evidence; C prose cross-links only; D benchmark | B: the closure depends on each older contract continuing to pass as well as the new integration cases. |

## Verification route

Exercise checked local success and dead-target Unit, invalid-payload non-send,
binary snapshot observations, validation before capacity accounting, overload
without admitted loss, two concurrent producers with per-sender order, profile
composition, retained native authority and lifetime, retained distribution
partition/duplicate/skew cases, C010 send, and C086 receive ordering.

## Results

The compiler adds one internal checked message boundary over retained codecs and
capacity queues, plus exact lifecycle and conformance disclosure. Five focused
integration tests pass with the retained message, resource, native, distribution,
version, and trust suites as part of 1,052 compiler tests. Production compilation
with warnings as errors, escript construction, and the reviewed trust-boundary
audit pass. The [normative contract](../60-specification/message-semantics/values-capacity-and-transport.md)
promotes P085 to C085.
