---
title: "2026-09-10 Performance Envelope"
kind: journal
created: "2026-09-10"
tags: [specification, performance, conformance, benchmarking]
aliases: []
---

# 2026-09-10 Performance Envelope

## Scope

Execute [G138](../20-notes/language-completion-plan-delivery.md#item-138-performance-envelope)
at revision `0.1.88`. CP-138-1..3 retain their recommendations: combine
operation and realistic/adverse workloads, bind honest environment and sample
distributions, and require semantic conformance before accepting a measured
win.

## Implementation decisions

| Decision | Four alternatives | Recommended and selected |
| --- | --- | --- |
| PE-I01 Harness | A external benchmark package; B small repository runner; C shell time; D prose | B: exact identities and semantic gates stay under compiler tests. |
| PE-I02 Coverage | A one microbenchmark; B fifteen required families; C compiler only; D runtime only | B: it spans compiler, runtime, library, diagnostics, and erasure. |
| PE-I03 Baseline | A no baseline; B semantically equivalent ordinary Erlang path; C interpreter only; D fastest result | B: relative cost has an explicit comparison. |
| PE-I04 Semantic gate | A final values only; B deterministic result digest before scoring; C timing implies equality; D manual review | B: different results cannot become speedups. |
| PE-I05 Terminal outcomes | A discard; B measured/timeout/failure/mismatch; C coerce zero; D retry forever | B: negative evidence remains visible. |
| PE-I06 Host identity | A hostname; B full P099 fingerprint and digest; C OTP major; D architecture only | B: comparisons bind the supported environment. |
| PE-I07 Workload identity | A source label; B id/family/size digest; C function pointer; D timestamp | B: retained rows pair deterministically. |
| PE-I08 Sizes | A one large case; B ordered empty/small/large families; C random only; D best case | B: scaling and boundary behavior remain visible. |
| PE-I09 Warmup | A hidden; B explicit count; C discard until fast; D none always | B: cold and warm evidence stays interpretable. |
| PE-I10 Statistic | A best; B median plus raw/min/max; C mean only; D percentile without samples | B: it resists single outliers while retaining evidence. |
| PE-I11 Ratio | A float; B integer parts per million; C rounded text; D omit | B: canonical signed evidence remains integer-only. |
| PE-I12 Memory | A omit; B nonnegative process memory delta as empirical; C exact allocation promise; D RSS peak only | B: retention signals remain visible without a portable claim. |
| PE-I13 Timeout | A score as fast; B retain and exclude; C delete row; D infinite wait | B: incomplete work is never a performance win. |
| PE-I14 Regression | A absolute nanoseconds; B same-host median ratio threshold at least one; C any slowdown; D subjective | B: policy is reproducible and bounded. |
| PE-I15 Optimizer | A time only; B require P135 semantic gate first; C allow trace drift; D hide mode | B: optimization cannot trade correctness for speed. |
| PE-I16 Claims | A portable targets; B exact-host empirical envelope; C scaling proof; D marketing range | B: P108 retains portable asymptotic guarantees. |

## Measured evidence

Compiler [PR 172](https://github.com/pcharbon70/catena/pull/172) merged feature
commit `0b78d93` as merge commit
`08e4fa70e445eabd00e16af73ad9b1f20ba16f71` into `rewrite`.
The retained report contains 45 measured rows: three sizes for each of fifteen
families, five scored repetitions after one warmup, with no mismatch, failure,
or timeout. Its digest is
`35efda7cbfd40ddd8e947af5863fcd77aae308ffba6843cd236c9cba0da113e7`.
Observed medians ranged from tens of nanoseconds for empty pure operations to
about 11 milliseconds for 10,000 checked foreign integer conversions. Process
message and resource wrappers showed the largest fixed relative overheads;
curried calls, handler-shaped continuations, guards, and foreign conversion
showed material relative costs. These are local observations, not targets.

Four focused cases exercise all families, mismatches, timeouts, artificial
median regression, invalid suites, tampering, lifecycle, and profile boundaries.
The complete compiler suite passes with 1,124 tests. The
[normative contract](../60-specification/performance-envelope/supported-host-workloads-and-regression-policy.md)
makes G138 complete.
