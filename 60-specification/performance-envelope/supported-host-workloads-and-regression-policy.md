---
title: "Supported-Host Workloads and Regression Policy"
kind: specification
created: "2026-09-10"
status: normative
spec_version: "0.1.88"
tags: [specification, performance, conformance, benchmarking]
aliases: []
---

# Supported-Host Workloads and Regression Policy

## Status and authority

G138 defines revision `0.1.88` under [authority](../../SPECIFICATION-AUTHORITY.md),
[conformance vocabulary](../../CONFORMANCE-VOCABULARY.md), and
[implementation limits](../../IMPLEMENTATION-LIMITS.md). It executes the
[G138 plan](../../20-notes/language-completion-plan-delivery.md#item-138-performance-envelope)
over P108 operation contracts, P129 resource accounting, P135 optimizer
validity, and P099's exact tested host. Public vocabulary remains P109's
decision (`PE-OBL-001`).

## Workload coverage and identity

A conforming envelope MUST cover direct calls, curried calls, trait operations,
ADTs, pattern matching, guards, comprehensions, handlers, process messages,
resource scopes, foreign conversion, erasure, BEAM code size, compilation, and
diagnostic provenance (`PE-OBL-002`).

Every workload MUST have a stable identifier, family, ordered unique nonnegative
input sizes, tested implementation, and semantically equivalent baseline. The
workload digest MUST bind identifier, family, and size (`PE-OBL-003`).

The report MUST bind the exact P108 contract digest, P099 compiler/OTP/ERTS/OS/
architecture fingerprint and digest, deterministic seed, repetition count,
warmup count, timeout, every raw sample, and a canonical report digest
(`PE-OBL-004`).

## Measurement protocol

Each size MUST run the declared warmup before scored repetitions. The report
MUST retain all successful monotonic-time samples and publish minimum, median,
maximum, baseline, relative-baseline, and nonnegative observed memory-delta
fields (`PE-OBL-005`).

The median is the scored statistic. Relative ratios MUST use integer parts per
million so the signed evidence profile contains no floating-point value.
Absolute time and process-wide memory deltas are empirical host observations,
not portable language limits (`PE-OBL-006`).

Cold compile and code-size workloads MUST build fresh stable identities. Warm
runtime workloads MUST keep compilation outside timed regions. A report MUST
state its warmup count rather than silently combine cold and warm observations
(`PE-OBL-007`).

Empty, large, and adverse shapes MUST be represented across the suite.
Scheduler contention, retained memory, and service boundaries MUST remain
visible as separate workload or evidence fields; implementations MUST NOT
delete an unfavorable sample to improve the reported envelope (`PE-OBL-008`).

## Semantic gate and negative results

The candidate and baseline result digests MUST be equal for every scored
repetition. A different value, terminal, event projection, callback count, or
other declared observation is a semantic mismatch and MUST NOT receive a speed
classification (`PE-OBL-009`).

A timeout is `timeout`; an exception or malformed run is `failure`; unequal
results are `semantic-mismatch`; only complete equal observations are
`measured`. Reports MUST retain every outcome, including negative results
(`PE-OBL-010`).

Optimizer-off and optimizer-on comparisons MUST first satisfy P135's
observation-preservation gate. Faster code with a different semantic digest is
a correctness failure, never a win (`PE-OBL-011`).

The envelope's aggregate semantic flag is true if and only if every row is
measured. Missing required families, duplicate identities or sizes, invalid
bounds, unknown hosts, and altered digests MUST be rejected (`PE-OBL-012`).

## Regression policy and claims

Two envelopes are comparable only when their supported-host and P108 contract
digests match. Rows are paired by workload identity and size; new rows remain
new and missing or nonmeasured rows remain excluded (`PE-OBL-013`).

A measured row is a regression when its median exceeds the previous median by
the declared ratio. The threshold MUST be at least one, MUST be reported by the
calling gate, and MUST NOT override semantic exclusion (`PE-OBL-014`).

Passing envelopes establish only the measured supported-host range. They MUST
NOT be reported as portable latency, throughput, allocation, constant-factor,
scaling-proof, or hardware promises. P108's asymptotic and stack contracts
remain the portable guarantees (`PE-OBL-015`).

An implementation claiming G138 MUST publish families, bounds, comparison
method, semantic-gate requirement, negative-result policy, portability stance,
and public-source hold. Conformance MUST include a complete retained raw report,
semantic mismatch and timeout fixtures, artificial regression detection,
tamper refusal, lifecycle selection, trust audit, and the full suite
(`PE-OBL-016`).

## Rationale and evidence (non-normative)

The [implementation journal](../../50-journal/2026-09-10-performance-envelope.md)
records sixteen four-way choices and the first 45-row OTP 29/Linux/x86-64
envelope. Measurements are evidence about this exact host and run; the rules
above govern how future runs can be compared without turning noise into
language semantics.

