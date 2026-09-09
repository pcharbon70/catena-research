---
title: "2026-09-09 Minimum Prelude"
kind: journal
created: "2026-09-09"
tags: [specification, conformance, standard-library]
aliases: []
---

# 2026-09-09 Minimum Prelude

## Scope

Completed [C101](../20-notes/language-completion-plan-delivery.md#item-101-minimum-prelude)
after C102–C106, preserving [C026](../60-specification/prelude-policy/README.md)
and the public-vocabulary hold. Semantic revision 0.1.69 is session-approved.
The executable gates pass; the public-vocabulary hold remains explicit.

## Implementation decisions

CP-101-1..3 retain their recommended selections. Every implementation fork below
explores four alternatives; the selected answer is the agent's recommendation.

| Decision | Alternatives | Selected recommendation | Reason |
| --- | --- | --- | --- |
| MP-I01 Package shape | A one merged module; B versioned catalog pinning existing ordinary modules plus pure foundation; C signatures only; D ambient prelude | B | Preserve nominal identities and existing ABI while adding a usable explicit minimum. |
| MP-I02 Selection | A automatic import; B exact package/version/digest manifest; C current directory inference; D host environment default | B | Absence selects nothing and wrong content cannot masquerade as the standard package. |
| MP-I03 Naming | A new public vocabulary; B retained internal role labels and existing method ABI; C mathematical names everywhere; D host module names in source | B | Keep the user’s vocabulary hold while testing semantics. |
| MP-I04 Foundations | A new primitives; B ordinary polymorphic identity/composition/constant/product operations; C native callbacks only; D omit compositional functions | B | Core category laws have executable ordinary-language witnesses. |
| MP-I05 Component inclusion | A every research feature; B pure foundation, categorical hierarchy, outcomes, collections, text and numerics, with environmental services separately gated; C only arithmetic; D only traits | B | Cover small functional applications without treating host authority as a pure import. |
| MP-I06 Identity verification | A trust self-declared digest; B exact catalog and dependency content plus compiler-built interfaces; C trust file names; D accept first matching version | B | Prevent rehashed forged catalogs and transitive mismatches. |
| MP-I07 Imports | A import every spelling unqualified; B ordinary explicit per-module imports with retained conflict checks; C silently prefer the prelude; D flatten modules and rename collisions | B | Preserve zero implicit names and ordinary name resolution. |
| MP-I08 Executable adoption | A inventory only; B compile ordinary selected modules and source applications plus checked text/numeric/environment entry dispatch; C duplicate all semantic engines; D interpret JSON without compilation | B | Reuse established meanings while requiring selected content for actual applications. |
| MP-I09 Opt-out | A minimal hidden fallback; B empty selected package set and no standard interfaces; C reject empty applications; D compiler-reserved names | B | Opt-out is observable and does not remove core built-ins. |
| MP-I10 Evidence | A signatures certify delivery; B inherited family laws plus new composition/import/application tests; C broad speed claims; D host documentation | B | Separate new assembly behavior from already tested component laws. |
| MP-I11 Resource costs | A constant overhead claim; B whole manifest bounds and explicit compilation/catalog work; C unlimited untrusted descriptions; D time-based admission | B | Bound inputs and state honest validation/rebuild costs. |
| MP-I12 Revision axes | A rewrite old hierarchy identity; B semantic69 catalog with package0.1.0 and retained component versions; C equate package and semantic patches; D unstable latest aliases | B | Preserve retained interfaces and lock exact content without conflating versions. |

## Execution and acceptance

Build the digest-bound catalog and ordinary foundation module; validate exact
selection and component interfaces; compile data transformation, validation and
capability-using programs; verify opt-out, missing packages, digest tampering and
conflicting imports; compare laws and retained behavior. Record final compiler
and archive checks, then commit/PR/merge and synchronize before the next gap.


## Decisions refined during implementation

| Decision | Four alternatives considered | Recommended and selected |
| --- | --- | --- |
| MP-I13 Prelude dependency | A separate resolver forever; B feed exact component/interface identity into C025/C026 and verify lock replay; C trust default replay digest callback; D infer the package from disk | B: use the established dependency engine with actual content verification. |
| MP-I14 Root names | A flatten colliding component names; B empty root export set plus explicit component interfaces; C rename nominal types; D give prelude a stronger precedence | B: preserve C026's ordinary origin rules and existing nominal identities. |
| MP-I15 Retained source adoption | A add generic value-import syntax now; B selected nominal interfaces plus compiled ordinary exports and existing checked text/numeric/environment entries; C copy all package definitions into applications; D claim signatures are applications | B: execute real data/validation/service applications without broadening the user's held grammar. |
| MP-I16 Lock replay | A accept any self-consistent JSON; B regenerate the exact deterministic lock and validate content digests; C accept version only; D fetch a newer compatible version silently | B: exact assembly identity remains reproducible and opt-out cannot reuse a selected lock. |

## Local executable evidence

The catalog resolves five ordinary modules without changing their nominal
identities or the existing categorical hierarchy. The new foundation compiles
under retained JSON 0.1.4. Over 61 integer inputs, identity and composition agree
with independent arithmetic, both identity laws and associativity hold, product
projections return their inputs, and instrumented callbacks occur once in order.
The ordinary reference evaluator agrees on foundation identity.

Two actual source applications compile against the selected component interfaces:
minimum-transform maps absent to zero and present n to twice n; minimum-validation
maps absent to dependent failure 404 and present n to dependent success n. The
executed BEAM results agree with explicit structural expectations. Opt-out cannot
compile those nominal inputs, but an empty program compiles. A selected catalog
does not make an unqualified identity name available. Conflicting explicit
constructor aliases are refused.

A retained numeric body adds two before checked Int-to-Float conversion; compiled
and reference paths both produce success 9.0 for input 7. Selected Unicode text
measurement reports two graphemes for an accented scalar sequence followed by an
emoji and refuses malformed UTF-8. An environmental application writes the bytes
selected through a supplied I/O device only when both its contract and actual
authority are supplied. Contract selection without authority fails.

The exact catalog rejects rehashed changed contents, malformed selections, missing
or duplicate packages and forged contexts. The existing dependency engine binds
all five interface digests and component content; exact replay succeeds, changed
lock bytes and selected/opted-out mismatch fail. Component law suites remain the
owners of collection, outcome, Unicode and numeric semantics; the new tests verify
assembly and application behavior rather than merely repeating signatures.

## Verification and provenance

Commands are `mix test`, `MIX_ENV=prod mix compile --warnings-as-errors`,
`MIX_ENV=prod mix escript.build`, `python3 validate_archive.py` and
`git diff --check`. Final counts and merged compiler provenance follow after the
final coherent run. The catalog digest is
`23cf7e16671d6ee78ac843a2ec3d0a846699aef95bf9de32e8a63c2b0a681c1e`;
the ordinary foundation digest is
`cd45595a7be2f6cdec132b2423c949fed9f4c969470f57441fe6ea05e2ada378`.
These content identities are separate from the compiler commit and package 0.1.0.

The [normative minimum](../60-specification/minimum-prelude/explicit-minimum-and-component-identity.md)
fixes the family inventory and execution boundaries. Public naming/grammar,
effectful foreign callbacks, generalized comprehension, transcendental admission,
performance-wide policy and full release readiness retain their separate owners.

Final verification passed **978 compiler tests**, production compilation with
warnings as errors and the production escript build. Archive validation passed
**651 documents, 81 directories, 126 sources, 195 specification chapters and
911 obligations** (816 traced, 74 partial, 21 untraced). Both repositories passed
`git diff --check`. Checklist totals are **107 complete, 20 partial, 12 gaps and
2 deferred**. Compiler merge provenance is recorded below once merged.

Compiler implementation commit `0475c82e27ef615b392ad7968cf69bb580e6ed3e`
merged through [compiler PR 151](https://github.com/pcharbon70/catena/pull/151)
as `e637a8e47a71decd6c72b0e0274ae3b4247568ae`. Compiler `rewrite` was
synchronized with origin before deleting the feature branch.
