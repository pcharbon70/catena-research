---
title: "2026-09-12 Compiler Self-Hosting"
kind: journal
created: "2026-09-12"
tags: [specification, compiler, bootstrap]
aliases: []
---

# 2026-09-12 Compiler Self-Hosting

## Scope

Execute G141's grammar-independent preflight at `0.1.98` while retaining the
P109 compiler-source hold. CP-141-1..4 select a staged late-0.x port, pure passes
before integrated compiler passes, stage-zero/one/two comparisons, and a pinned
Elixir recovery root. This slice defines and enforces the milestone blockers; it
does not create a `bootstrap/` directory or claim a self-hosted compiler.

## Implementation decisions

| Decision | Four alternatives | Recommended and selected |
| --- | --- | --- |
| SH-I01 Timing | A rewrite now; B staged port after the source subset works; C Elixir forever; D change VM first | B: the milestone follows usable public source and preserves scope. |
| SH-I02 Port shape | A all passes together; B pure passes first; C wrappers; D excluded features | B: small differential boundaries make each dependency reviewable. |
| SH-I03 Stages | A self-compilation once; B stage zero, one, and two; C filenames; D trust source claims | B: exact builders and outputs support a meaningful fixed-point test. |
| SH-I04 Recovery | A delete Elixir; B retain pinned stage zero and rollback; C opaque stage two only; D download ambient tools | B: recovery and bootstrap trust remain explicit. |
| SH-I05 Target | A new VM; B BEAM through OTP 29 Abstract Format; C direct BEAM bytes; D interpreter only | B: self-hosting changes implementation language, not the target contract. |
| SH-I06 Source timing | A invent syntax; B hold compiler source for P109; C encode source as Elixir; D call retained JSON public source | B: actual Catena authorship requires the approved language. |
| SH-I07 Subset proof | A compiler first; B ordinary programs demonstrate required ADTs, capabilities, diagnostics, packages, and OTP calls; C assume expressiveness; D bypass modules | B: prerequisites are exercised outside circular compiler claims. |
| SH-I08 Port order | A backend first; B canonical JSON, SCC, rows/unification, parser, checker, verifier, backend; C alphabetical; D arbitrary parallel port | B: pure dependencies precede integrated passes. |
| SH-I09 Pass identity | A module name; B exact source/interface/artifact digests; C timestamp; D Git branch | B: each differential boundary names immutable inputs and outputs. |
| SH-I10 Stage one | A Elixir wrapper; B stage zero compiles Catena compiler source; C copy stage zero; D download binary | B: stage one must originate from actual Catena source. |
| SH-I11 Stage two | A reuse stage one bytes; B stage one recompiles the same source and inputs; C change source; D omit builder identity | B: the second build tests the self-produced compiler. |
| SH-I12 Comparison | A filenames; B exact bytes inside P128 or declared semantic oracle; C startup success; D file size | B: the comparison matches the reproducibility envelope honestly. |
| SH-I13 Further stage | A never; B require when the oracle cannot classify one-time drift; C always ten stages; D ignore drift | B: unexplained instability remains blocked without arbitrary repetition. |
| SH-I14 Fixed-point claim | A proves correctness; B proves only scoped repeatability; C proves no malicious bootstrap; D proves portability | B: circular agreement has a precise limited meaning. |
| SH-I15 Suites | A unit tests only; B conformance, differential, compatibility, packaging, and application corpus; C stage-two smoke test; D benchmark only | B: both implementations face the same broad evidence. |
| SH-I16 Suite binding | A prose result; B bind implementation, source, corpus, revision, target, and result; C CI URL; D pass count | B: retained evidence can be replayed against exact subjects. |
| SH-I17 Offline build | A network allowed; B clean retained-input rebuild; C cached stage two only; D undeclared downloads | B: the bootstrap follows reproducible acquisition rules. |
| SH-I18 Residual services | A hide Elixir calls; B inventory crypto, filesystem, process, and OTP formatting only; C allow any host library; D no host services | B: host mechanisms stay explicit without retaining compiler passes. |
| SH-I19 Identity drift | A warn; B refuse before comparison or publication; C rename output; D accept signed filename | B: altered bootstrap or stage inputs cannot inherit evidence. |
| SH-I20 Rollback | A documentation only; B real interrupted-upgrade and stage-zero rebuild drill; C restore stage-two copy; D no rollback | B: recovery is demonstrated under the failure it addresses. |
| SH-I21 Distribution | A stage two alone; B complete signed immutable bootstrap bundle; C install script downloads latest; D source without toolchain | B: another host receives the evidence and recovery inputs. |
| SH-I22 Preflight | A create empty `bootstrap/`; B canonical blocked package at 0.1.98; C claim partial stages; D leave checklist Gap | B: executable blockers advance the plan without fabricating Catena source. |

Every recommendation was selected under the user's delegated decision
authority. No recommendation was overridden.

## Executed evidence

Compiler [PR 195](https://github.com/pcharbon70/catena/pull/195) merged feature
commit `b03f627` as merge commit `c3a30d0` into `rewrite`. Six direct preflight
cases exercise the exact blocked assessment, canonical package digest, wrapper
and fake-stage refusal, target drift, hidden residual compiler-pass refusal,
port-order truncation, premature fixed-point and rollback claims, lifecycle,
and conformance publication.

The complete 1,194-test suite, production compilation with warnings as errors,
escript construction, reviewed trust-inventory verification, and
`git diff --check` pass. The preflight is classified in `tools-profile`. It
retains the Elixir recovery root and deliberately does not create the future
`bootstrap/` source tree.

The [normative contract](../60-specification/compiler-self-hosting/staged-bootstrap-and-fixed-point-evidence.md)
makes the milestone and its evidence requirements durable. G141 stays partial
until P109 permits actual Catena compiler source, the required passes are
ported, stages are built and compared, both implementations pass every suite,
offline reproducibility succeeds, residual services are audited, and rollback
is demonstrated.
