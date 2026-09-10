---
title: "2026-09-10 Diagnostic Contract"
kind: journal
created: "2026-09-10"
tags: [specification, diagnostics, tooling, source-location]
aliases: []
---

# 2026-09-10 Diagnostic Contract

## Scope

Execute P117's semantic portion at `0.1.91` while retaining the P109 parse
hold. CP-117-1..3 select structured records, bounded causal explanations, and
shared semantic coverage before grammar-specific cases.

## Implementation decisions

| Decision | Four alternatives | Recommended and selected |
| --- | --- | --- |
| DX-I01 Record evolution | A replace IDs; B add optional structured fields; C strings only; D raw exceptions | B: existing identity remains stable. |
| DX-I02 Related spans | A unlimited; B eight labeled spans; C primary only; D paths only | B: bounded context serves consumers. |
| DX-I03 Coordinates | A bytes only; B half-open bytes plus scalar lines/columns; C UTF-16 only; D host offsets | B: reuse C013 exact coordinates. |
| DX-I04 Type form | A solver IDs; B normalized source-level structure; C prose only; D host types | B: users see stable language concepts. |
| DX-I05 Long types | A unbounded; B bounded text plus full digest; C drop type; D arbitrary cut | B: output stays finite and identifiable. |
| DX-I06 Causes | A nearest error only; B unique causal steps; C full solver dump; D guessed cause | B: bounded provenance explains the mismatch. |
| DX-I07 Cause bound | A unlimited; B 32; C one; D host memory | B: enough context with deterministic cost. |
| DX-I08 Missing matches | A generic message; B concrete witness and type; C all values; D no check | B: existing coverage evidence becomes actionable. |
| DX-I09 Redundancy | A one reason; B distinguish guard false/fact coverage/pattern coverage; C remove warnings; D solver text | B: the repair depends on the cause. |
| DX-I10 Generated origins | A pretend handwritten; B node/digest/span; C omit; D host file | B: P100 identity remains authoritative. |
| DX-I11 Edit preimage | A offsets only; B SHA-256 source binding; C timestamp; D filename | B: stale edits fail deterministically. |
| DX-I12 Edit coordinates | A arbitrary bytes; B UTF-8 scalar boundaries; C line text search; D UTF-16 | B: repairs cannot split source scalars. |
| DX-I13 Edit overlap | A last wins; B sorted nonoverlapping; C merge guesses; D apply sequentially | B: one diagnostic has one unambiguous patch. |
| DX-I14 Applicability | A Boolean; B three existing applicability classes; C always safe; D prose | B: consumers preserve confidence. |
| DX-I15 Application | A compiler writes; B report only; C auto-save; D shell command | B: C008 and P125 boundaries remain intact. |
| DX-I16 Serialization | A drop new fields; B preserve through Report and redaction; C host structs; D log only | B: machine consumers receive the contract. |
| DX-I17 Parse behavior | A invent grammar errors; B explicit P109 hold; C block semantics; D regex parser | B: the current work makes no vocabulary choice. |
| DX-I18 Invalid records | A best effort; B explicit invalid contract; C crash; D silently omit | B: consumers never trust malformed evidence. |
| DX-I19 Trust placement | A unaudited helper; B tools-profile inventory; C external service; D compiler plugin | B: the shared contract remains in audited source. |

## Executed evidence

Compiler [PR 177](https://github.com/pcharbon70/catena/pull/177) merged feature
commit `0540e9a` as merge commit
`e7c73ff3947a093e646368e0317ee42dbfe6e0b3` into `rewrite`.
The implementation extends diagnostic reports and adds a bounded contract
validator, normalized type presentation, causal unification evidence, missing
coverage witnesses, guard-redundancy reasons, generated-origin checks, and
preimage-bound nonoverlapping edits. Compiler
[PR 178](https://github.com/pcharbon70/catena/pull/178), merge
`ff32913df7d43551f330a6fa38575613c223a485`, adds direct overlap,
well-formed-origin, forged-origin, and guard-class assertions. Compiler
[PR 179](https://github.com/pcharbon70/catena/pull/179), merge
`204aced480deaaa9e953cc2341605c232720be89`, makes generated-origin validation
recompute SHA-256 over the node identity and exact source slice.
Six focused cases and the complete 1,143-test suite pass. Production
warnings-as-errors compilation, escript building, trust inventory
verification, and `git diff --check` pass.

The [normative contract](../60-specification/diagnostic-contract/structured-explanations-and-repairs.md)
makes the semantic work durable. P117 stays partial because no retained input
can establish P109's future parse/recovery diagnostics.
