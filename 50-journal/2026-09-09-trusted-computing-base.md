---
title: "2026-09-09 Trusted Computing Base"
kind: journal
created: "2026-09-09"
tags: [specification, conformance, security]
aliases: []
---

# 2026-09-09 Trusted Computing Base

## Scope

Execute [G126](../20-notes/language-completion-plan-delivery.md#item-126-trusted-computing-base)
over the compiler at C101 merge e637a8e47a71decd6c72b0e0274ae3b4247568ae.
The user approved all revision updates for this session; the planned exact contract
is 0.1.70. The disclosure and boundary gate are complete; no proof-verified compiler is claimed.

## Implementation decisions

CP-126-1..3 retain their recommended choices. Each fork below lists four options;
the selected answer is the agent's recommendation.

| Decision | Alternatives | Selected recommendation | Reason |
| --- | --- | --- | --- |
| TC-I01 Guarantees | A flat trusted list; B guarantee-specific dependency graph; C claim verifier eliminates trust; D list crypto only | B | Separate acceptance, lowering, execution, authority, erasure, identity and library evidence. |
| TC-I02 Inventory scope | A lib only; B compiler sources, privileged helpers, generators and external host components; C tests only; D package manifests only | B | Generated tables and helper interpreters can alter claimed behavior. |
| TC-I03 Boundary gate | A regex only; B Elixir AST call inventory plus Python AST helper inventory; C execute source to discover effects; D trust file names | B | Inspect syntax without evaluating repository source as the scanner input. |
| TC-I04 New paths | A silently classify by broad directory; B exact owned path inventory and failure on added/removed sources; C ignore new files; D assume test coverage | B | New privileged code cannot disappear under a generic directory exemption. |
| TC-I05 Call identity | A line numbers; B normalized target/arity/expression fingerprints with multiplicity; C function names only; D whole-file hashes only | B | Catch changed privileged call expressions without treating whitespace as semantics. |
| TC-I06 Dynamic dispatch | A ignore apply and callbacks; B inventory dynamic calls and reflection as trust boundaries; C forbid all functions; D assume all callbacks pure | B | Static typing and descriptor validation remain separately necessary. |
| TC-I07 Independent verification | A call inference twice; B corrupt core and evidence tests plus exact artifact revalidation; C signature means correct; D no mutation tests | B | Demonstrate actual refusal rather than naming a second pass independent. |
| TC-I08 Lowering fault | A assume verifier checks BEAM; B mutate accepted generated forms and show raw OTP accepts while exact artifact gate refuses; C hide undetected faults; D compare only hashes | B | Make residual backend trust and the narrower artifact guarantee falsifiable. |
| TC-I09 Host ingress | A trust tags; B codec and authority forgery witnesses; C unrestricted ETF; D universal coercion | B | The complete admitted type and live authority identity are separate boundaries. |
| TC-I10 Proof claims | A equate typechecking with machine proof; B inventory checked predicates, bounded evidence and shared helpers explicitly; C claim all theorem text is executable; D omit proofs entirely | B | No general proof-kernel or verified-compiler claim is inferred. |
| TC-I11 Runtime residuals | A worker kill is OS rollback; B explicit ERTS, native-code and OS dependencies; C test host compromise by destructive actions; D ignore runtime | B | Record VM crashes, helper failure and compromised build-host limits without unsafe experiments. |
| TC-I12 Maintenance | A regenerate automatically in every build; B explicit reviewed inventory update plus failing CI tests; C never change baseline; D ignore changed generators | B | An inventory change is a review event, not automatic approval of new authority. |

## Acceptance route

Inspect actual compiler, verifier, serializer, artifact, crypto, foreign, helper and
generator paths; build the guarantee graph and executable privilege inventory;
mutate representative core/evidence/lowering/ingress; record both detected and
undetected fault classes. Validate the full suite and archive before changing the
checkbox, then commit, PR, merge and synchronize in the user's requested order.


## Refined implementation decisions

| Decision | Four alternatives considered | Recommended and selected |
| --- | --- | --- |
| TC-I13 Call granularity | A privileged-name regex only; B all remote/dynamic calls, selected runtime locals and generated remote forms; C line-number allowlist; D skip callbacks | B: normalize complete expressions and record multiplicity while explicitly retaining semantic-review limits. |
| TC-I14 Inventory size | A embed every expanded call expression; B per-source digest, count and target histogram; C counts alone; D omit larger files | B: keep the reviewed machine profile compact while fingerprints still bind the complete normalized call multiset. |
| TC-I15 Native/config source growth | A scan only current .ex files; B include source/build trees and refuse unknown source formats; C ignore src/c_src; D trust all future native code | B: a new native compiler path requires explicit admission and ownership before its inventory can pass. |
| TC-I16 Build literals | A call syntax alone; B whole mix.exs/mix.lock hashes plus call inventory; C trust dependency version strings; D ignore build metadata | B: literal dependency changes can alter host code without adding a call expression. |

## Inspected trust dependencies

Both structural verifiers recheck core without invoking the main inference entry,
but share Type/Data/Row/Coverage helpers. OTP.Compiler owns production compilation;
the native transport additionally loads its explicitly admitted native module.
Foreign sessions, call wrappers and service managers perform declared dynamic
calls. Canonical encoders, crypto/root policy, ordinary package descriptions,
Unicode tables and their generators remain named dependencies. There is no general
package-registry client or executable proof kernel for every research theorem.
The [integrated theorem](../60-specification/progress-and-preservation/the-integrated-theorem.md#the-composition-lemma)
still owns an undischarged composition obligation.

## Mutation evidence

Core type and effect-evidence corruption are refused by the relevant verifier.
A well-typed changed literal 43 is accepted and evaluates to 43, demonstrating that
core checking does not establish fidelity to original source 42. A deliberately
altered Erlang function returning 99 compiles and executes through OTP; substituting
those bytes into the original exact calling artifact is refused by deterministic
rebuild. A signature over an unsupported correctness claim verifies cryptographically;
changing the signed bytes fails verification. Malformed UTF-8 in a nested foreign
carrier and forged authority tags are refused separately.

The source gate detects new raw compiler calls, dynamic foreign calls, callbacks,
generated remote forms and unclassified/missing paths. Python input containing a
raising statement and an OS call is parsed without execution. New Erlang source
under src is refused as an unclassified format. Changing literal dependencies in
mix.exs changes its data fingerprint. By contrast, changing true to false in a
branch guard while preserving call syntax leaves the inventory unchanged; the
suite records that undetected semantic difference rather than claiming a sandbox.

## Verification and provenance

The full compiler suite passed **987 tests**, including nine new trust-boundary
cases. `mix run scripts/check_trust_inventory.exs`, production compilation with
warnings as errors, escript generation and `git diff --check` passed. The reviewed
profile covers **184 sources, 17,211 recorded call expressions, 23 data/build
inputs, 11 components and 12 guarantee families**. Its canonical digest is
`cd8c009a2515ea5e5cc8e5703194a6cf1f07db42d5638a12b2ab4d0d65d61362`.

Archive validation passed with 654 documents, 82 archive directories, 126 source
records, 196 specification chapters and 922 obligations (827 traced, 74 partial,
21 untraced). Checklist totals become 108 complete, 20 partial, 11 gaps and two
deferred. Compiler [PR 152](https://github.com/pcharbon70/catena/pull/152) merged feature
`2727555fbba9d1529e6b60f95cebfac0a9f5cfb4` as
`02d626e26039521596e979a253ab37c98a2498b7`. The compiler rewrite branch was
synchronized with origin before deleting the local and remote feature branch.

The [normative trust contract](../60-specification/trusted-computing-base/guarantees-assumptions-and-boundary-checks.md)
owns the distinctions among guarantee, enforcement, tested refusal and residual
trust. No destructive native-crash or compromised-host experiment is needed to
acknowledge those explicit limits.
