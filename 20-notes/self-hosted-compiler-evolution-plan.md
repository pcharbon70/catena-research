---
title: "Self-Hosted Compiler Evolution Plan"
kind: note
created: "2026-09-14"
maturity: developing
tags: [catena, compiler, bootstrap, language-design, compatibility, decision-log]
aliases: []
---

# Self-Hosted Compiler Evolution Plan

## Adopted planning direction and authority

The user requested that the current planning adopt the
[study and recommendation](feature-evolution-in-a-self-hosted-catena-compiler.md).
This plan selects **advancing, exactly pinned Catena seeds for routine builds,
with a conservative compiler-source floor and an immutable reconstruction chain
back to the original Elixir recovery root**. Implement a feature using the
current subset before depending on it in compiler source. Treat compiler
execution libraries and produced-program libraries as separate dependencies.

This is the delivery extension of
[item 141](language-completion-plan-delivery.md#item-141-compiler-self-hosting)
and the [M9 milestone](language-completion-plan.md#dependency-order-and-executable-milestones).
The initial G141 completion gate and subsequent evolution readiness have
separate acceptance records. Local E0–E7 work-package IDs below do not add
checklist items or change the original 392-decision baseline.

Planning adoption is complete; normative adoption and implementation are
pending. The initial
[G141 contract at 0.1.98](../60-specification/compiler-self-hosting/staged-bootstrap-and-fixed-point-evidence.md)
continues to govern its exact stages, complete dual-implementation suites,
target, provenance, residual services, and recovery. No obligation is silently
weakened by this note. E1 defines the future successor scope before any build
depends on a rolling seed or revised coverage/comparison policy.

Language implementation belongs in the sibling compiler repository. Public
compiler source remains held for P109, the BEAM through OTP Abstract Format
target remains fixed, and self-hosting does not admit excluded type features.
This planning update allocates no semantic revision and selects no public
language spelling.

## Selected decisions

The following table preserves four options per fork. SHE-01 carries the four
policy alternatives from the study in their original order; the other rows
operationalize the recommendation. The agent selected the recommended options
under the user's request to update planning, rather than claiming individual
user selection of every fork. The same rows are retained in the
[decision register](design-decision-register.md#self-hosted-compiler-evolution-plan-2026-09-14).
These are durable planning decisions; specification and implementation evidence
will be linked as each work package completes.

| Decision | Options as posed | Recommendation | Selected for planning | Override | Durable planning location |
| --- | --- | --- | --- | --- | --- |
| SHE-01 — routine seed policy | A: Freeze compiler source at the first supported subset. B: Extend Elixir for every feature required by compiler source. C: Advance exact Catena seeds and retain the Elixir reconstruction chain. D: Generate an older subset or portable snapshot from current source. | C: Preserves internal language adoption without requiring two complete production compilers. Seed snapshots supplement the retained chain; they do not replace it. | C — agent-selected under the user's planning request | None | [Work package](self-hosted-compiler-evolution-plan.md#e1-evolution-contract) |
| SHE-02 — feature self-adoption | A: Implement using the seed-compatible subset, test external inputs, then promote and adopt internally. B: Implement and self-adopt in one change using a retained two-source bridge. C: Keep all compiler source permanently at the initial language subset. D: Maintain a downlevel translator for all compiler-source additions. | A: Default to separate implementation and self-use; use B only when a concrete feature or fix requires an explicit bridge, recording that exception. | A — agent-selected under the user's planning request | None | [Work package](self-hosted-compiler-evolution-plan.md#e5-first-feature-and-self-adoption) |
| SHE-03 — promotion timing | A: Advance the seed with every compiler-package release. B: Advance when a required source facility, dependency, or compiler fix needs it; publish the exact floor and digest. C: Advance on a fixed calendar cadence. D: Give each source revision its own newly produced seed. | B: Tie promotions to demonstrated dependencies; measure their frequency before setting a cadence or lag budget. | B — agent-selected under the user's planning request | None | [Work package](self-hosted-compiler-evolution-plan.md#e4-promotion-and-recovery) |
| SHE-04 — compiler structure | A: Keep broad passes and rely on end-to-end checks for feature interactions. B: Use explicit intermediate languages, localized passes, invariants, and independent observations. C: Redesign every intermediate representation when a feature is added. D: Require every feature to disappear into the initial core immediately. | B: Localize changes while retaining type, effect, capability, and proof information until its obligations are discharged. | B — agent-selected under the user's planning request | None | [Work package](self-hosted-compiler-evolution-plan.md#e2-build-and-comparison-infrastructure) |
| SHE-05 — evolving-stage comparison | A: Always compare the first two complete packages byte for byte. B: Always compare the second and third complete packages byte for byte. C: Bind the actual builders, sources, artifact subjects, and applicable byte relation or versioned semantic oracle; add stages when needed. D: Use successful self-builds and application tests without a declared stage comparison. | C: Account for changed code generation and builder provenance. Keep P128 whole-package reproducibility separate and preserve the current G141 initial-stage obligations. | C — agent-selected under the user's planning request | None | [Work package](self-hosted-compiler-evolution-plan.md#e1-evolution-contract) |
| SHE-06 — library and runtime transitions | A: Build both the compiler and all new libraries with the oldest seed. B: Separate compiler execution dependencies from produced-program dependencies; use temporary compatibility bridges or isolated matched worlds. C: Replace compiler, libraries, and formats together with no intermediate compatible source. D: Retain every old runtime adapter indefinitely. | B: Migrate before retiring supported interfaces; refuse incompatible mixed artifacts and keep source-selection changes explicit. | B — agent-selected under the user's planning request | None | [Work package](self-hosted-compiler-evolution-plan.md#e6-semantic-and-runtime-transition-evidence) |
| SHE-07 — independent evidence after the initial port | A: Maintain complete Elixir feature parity indefinitely. B: Retain full shared-language dual coverage and require explicit independent evidence for later extensions under a successor contract. C: Build a second complete production compiler in another language. D: Require a full mechanized compiler proof before admitting every extension. | B: Preserve complete initial G141 dual suites and a mapped extension evidence obligation. An unsupported feature cannot be credited to the frozen compiler. | B — agent-selected under the user's planning request | None | [Work package](self-hosted-compiler-evolution-plan.md#e1-evolution-contract) |
| SHE-08 — recovery and distribution | A: Rebuild the entire historical chain for every developer invocation. B: Use an immutable seed bundle for routine builds and replay the full retained root-to-candidate chain for each seed promotion and release. C: Replace the historical root with a fresh translator whenever the source floor rises. D: Replace the bootstrap with an independently maintained stable-subset interpreter. | B: Retain every required bridge, toolchain, library, and recovery environment. Promotion and release gates expose broken history without imposing full replay on each edit. | B — agent-selected under the user's planning request | None | [Work package](self-hosted-compiler-evolution-plan.md#e4-promotion-and-recovery) |
| SHE-09 — development and release checks | A: Run every bootstrap stage and release suite for each edit. B: Use focused affected-pass and feature checks during development, with full applicable suites, stage comparison, offline replay, and rollback at promotion and release. C: Reuse the latest passing full-suite result without binding it to the candidate. D: Rely on manually chosen tests for each release. | B: Fast feedback is distinct from release evidence. Every promotion and release binds its exact candidate and complete required evidence. | B — agent-selected under the user's planning request | None | [Work package](self-hosted-compiler-evolution-plan.md#e7-evolution-readiness) |
| SHE-10 — adoption sequence | A: Replace the initial G141 contract with the new process before attempting the first port. B: Preserve G141's initial milestone and specify the evolution contract before the first build that depends on the new policy. C: Let build scripts settle the policy when the first incompatibility occurs. D: Postpone any compiler self-use of new facilities until a stable 1.0 release. | B: Keeps retained obligations intact, allows source-independent preparation, and prevents later bootstrap behavior from outrunning its authority. | B — agent-selected under the user's planning request | None | [Work package](self-hosted-compiler-evolution-plan.md#e1-evolution-contract) |

## Work packages and completion status

Only the planning row is complete. A document or preflight validator cannot
supply an absent compiler build or experiment.

| Work package | State | Prerequisites | Exit evidence |
| --- | --- | --- | --- |
| E0 — adopt the plan | Complete | Study and user's planning request | Selected forks, delivery sequence, current-plan links, and archive validation |
| E1 — evolution contract | Not started | E0; current G141, lifecycle, reproducibility, compatibility, and trust contracts | Explicit initial/evolution applicability, obligation register, exact comparison and coverage rules |
| E2 — build and comparison infrastructure | Not started | E1 for admitted behavior; source-independent design can proceed earlier | Manifest, source-floor, stage, comparison, and refusal tests; real-stage claims wait for E3 |
| E3 — initial self-hosted compiler | Blocked by P109 and required application evidence | Existing item-141 prerequisites; stage infrastructure | Every current G141 obligation, including actual Catena passes, dual suites, offline builds, and rollback |
| E4 — promotion and recovery | Not started | E1–E3 | First accepted routine seed, complete root-to-seed replay, interrupted activation and rollback |
| E5 — first feature and self-adoption | Not started | E4; admitted feature semantics | Feature implemented with the old subset, independently tested, promoted through E4's procedure if needed, and then adopted internally |
| E6 — semantic and runtime transition evidence | Not started | E4; E5 workflow; explicit semantic/ABI contracts for selected changes | Measured semantic and interface transitions, matched dependencies, stale-artifact refusal, and preserved recovery |
| E7 — evolution readiness | Not started | E1–E6 | Full release-candidate evidence, measured costs, coverage disposition, and contributor/recovery instructions |

E4's promotion procedure is reused for every later promotion; its first
successful execution does not preapprove future seeds. E5 can test the new
feature before promoting its compiler. Its self-adoption step waits for that
promotion, which prevents a dependency cycle between the feature and its seed.

### E1: evolution contract

Prepare an explicitly versioned successor or extension under
[specification authority](../SPECIFICATION-AUTHORITY.md#conflict-resolution).
Choose the next applicable revision when this work executes; do not reserve a
patch in advance. Record:

1. Initial G141 scope, immutable recovery-root role, routine-seed role, and
   whether a build uses a direct edge or a chain. Preserve the original
   initial-transition evidence and obligations.
2. The compiler-source floor: syntax and semantics, named feature selection,
   required compiler fixes, build tools, and library interfaces. Separate this
   floor from the language accepted for user programs and from package versions.
3. Complete edge identity: builder artifact and source provenance, input bytes,
   language selection, dependencies, host/toolchain, target, output artifacts,
   schema versions, and predecessor edges. Unknown or missing data is refusal.
4. Comparison subjects and observations. Distinguish full-package P128 replay
   with identical inputs from cross-builder stage comparison. Account explicitly
   for old-versus-new code generation, changed builder metadata, and additional
   same-source stages. Never normalize consequential fields silently.
5. Independent coverage. Keep all five initial G141 suite families under both
   implementations. For later extensions, retain the complete shared-language
   baseline and name the independent expected observations, reference model,
   differential path, or applicable theorem for each new obligation. Record
   proof limits; lack of Elixir support is not a passing result.
6. The required offline root-to-candidate reconstruction, seed promotion,
   transactional activation, host-support, distribution, and rollback evidence.
   State which failures block which claim.

Update lifecycle selection, conformance discovery, obligation traceability,
and exact applicability with that future change. A new evolution profile must
not relabel the current blocked preflight as a successful stage runner.
Completing E1 records a contract; it supplies none of E3–E7's execution evidence.

### E2: build and comparison infrastructure

Design the future compiler-repository bootstrap manifest, source-floor check,
stage runner, evidence collector, and promotion transaction using the current
build, package, signed-acquisition, and trust machinery. Keep the schema
independent of unselected public grammar. Exact filenames and field spellings
are implementation decisions for that slice, with their own four-option
journal entries.

Validate every dependency edge before building; isolate output directories,
caches, libraries, and executing VMs between stages. A fixture with new source
syntax must be passed to the newly built compiler rather than parsed by the
old seed while constructing its test harness. Stage-specific flags cannot
supply missing parser or checker implementations.

Exercise changed seed/source/library digests, missing bridges, unknown schema,
incompatible runtime metadata, source-floor violations, and contaminated
outputs. Define versioned semantic observations before using an oracle to
explain byte drift. Artificial fixtures can test these refusals but cannot
establish a real compiler fixed point.

Keep generated-source bridges outside the default workflow. Admitting one
requires its own translator, provenance, source-map, authority, and reproducible
generation contract; the existing closed generator model is insufficient.

### E3: initial self-hosted compiler

Execute the existing CP-141-1..4 plan after P109 and the required ordinary
application subset are demonstrated. Port canonical JSON, strongly connected
components, rows and unification, parser, checker, verifier, and backend in the
specified order, retaining each differential interface before adding dependents.
Do not substitute wrappers for Catena-authored compiler passes.

Pinned Elixir builds the exact initial compiler source into stage one; that
stage rebuilds the same source into stage two, with the applicable comparison
and any additional stage required by G141. Run complete conformance,
differential, historical compatibility, packaging, and representative application
suites under both implementations. Complete clean offline builds, limited
residual-host-service inventory, signed acquisition/distribution evidence, and
the real rollback drill.

G141 can become complete only on this actual evidence. The later work packages
add evolution readiness; they neither replace this initial gate nor turn
self-hosting into a prerequisite for every useful earlier compiler release.

### E4: promotion and recovery

Package the first accepted Catena seed with exact source provenance, libraries,
toolchain and host profile, build tools, source floor, and a complete
predecessor chain to the original Elixir root. Validate an ordinary build using
that seed bundle and independently rebuild the chain offline without relying
on the candidate executable as an undeclared input.

Every later seed promotion records why the current floor is insufficient.
Retain any intermediate compatible source needed to build the replacement.
A two-source bridge records its distinct A and B inputs separately; it is not
a same-source fixed-point comparison. Preserve required commits through
immutable tags or source bundles before branch deletion or squashing makes
them unreachable.

Activation is transactional. Interrupt it before and during the permitted
commit boundary, demonstrate the old or new complete active toolchain, and
reconstruct a usable toolchain from retained inputs. Missing or incompatible
recovery environments block the corresponding promotion/release claim.
Changing supported OTP or host profiles needs its existing compatibility
evidence; general BEAM portability is not a substitute.

Publish no automatic calendar rule. Measure promotion cost and frequency first.
Routine development consumes the accepted seed; promotion and release evidence
replay the entire retained root-to-candidate chain.

### E5: first feature and self-adoption

Choose an independently admitted additive feature whose implementation uses
the current subset and lowers to established semantics. This plan neither
chooses its public spelling nor creates a new semantic admission.

Use four separately reviewable steps:

1. Implement parsing/checking/lowering and diagnostics with seed-compatible
   source; identify affected intermediate languages and invariants.
2. Build the new compiler and test new-feature programs as its inputs, including
   negative, independent semantic, tool, package, and representative application
   observations. Keep compiler source at the old floor.
3. If internal use needs a new seed, run E4's complete promotion procedure on
   the new candidate and retain all evidence.
4. Adopt the feature inside compiler source, rebuild from the promoted seed,
   and exercise those compiler paths plus applicable full-stage evidence.

The repository's commit/PR workflow may package these steps differently, but
it must retain their dependency order and every source needed for recovery.
New implementation syntax inside an inactive branch is acceptable only if the
old builder's actual processing rules permit it. Prefer compatible files or
old-parseable alternatives where a bridge is needed.

### E6: semantic and runtime transition evidence

Apply the workflow to an admitted type/effect change and to a runtime,
library, or interface-schema transition. Keep their semantic design and proof
effort separate from bootstrap-specific coordination. Use existing admitted
mechanisms or future explicitly admitted changes; self-hosting supplies no
exception to C140, categorical laws, or effect/cleanup obligations.

For an interface transition, first provide compatible support where coexistence
is valid, then build the new compiler and matching produced-program dependencies,
migrate compiler self-use, and retire old uses only after supported build edges
no longer need them. If representations or authority rules cannot coexist,
use isolated matched toolchains and explicit incompatibility refusal.

For source removals or changed meanings, make the bridge support the appropriate
old and new language selections, migrate source, and promote before internal
retirement. User-language retirement remains governed by compatibility and
historical-selection rules.

Exercise stale caches, wrong libraries, obsolete metadata, removed primitives,
seed bugs, and interrupted rebuilds. Never compare two different source versions
as if they were equal-input stages. Keep the extension's complete semantic and
tooling coverage visible alongside bootstrap success.

### E7: evolution readiness

For the exact candidate, gather full applicable suites, stage-comparison
evidence, offline chain replay, mutated-input refusals, and rollback results.
Reuse E4's promotion gate whenever a newer seed is required; a release without
a seed change still needs its own candidate-bound release evidence.

Retain elapsed build time, stage count, storage, temporary compatibility code,
promotion frequency, contributor steps, and bootstrap-specific failures from
E4–E6. Separate feature-design, implementation, and proof-maintenance effort.
Set any subsequent performance or retention budget from these observations,
with a recorded decision rather than an invented estimate.

Document the normal contributor build, feature/self-adoption sequence, seed
promotion, supported host assumptions, failure diagnosis, and clean recovery.
State the independent coverage and residual trust that each release actually
has. Fixed points do not prove correctness; diverse double-compiling or a full
compiler theorem requires separate methods and evidence.

Development checks can remain focused on affected paths, but promotion and
release checks use the full declared evidence set. This is a build/test policy,
not authorization to publish a release or create a scheduled task.

## Connections and maintenance

- The [study](feature-evolution-in-a-self-hosted-catena-compiler.md) supplies
  primary-source evidence and the limitations behind these planning decisions.
- The [evolution inquiry](../40-inquiries/how-should-catena-evolve-after-self-hosting.md)
  now tracks normative details and empirical validation rather than reopening
  the selected general direction.
- The [planning adoption journal](../50-journal/2026-09-14-self-hosted-feature-evolution-research.md#planning-adoption)
  records the user's follow-up request and the scope of this update.
- The [completion checklist](../00-inbox/language-specification-completeness-checklist.md)
  remains the overall status ledger. Update E0–E7 here from observed evidence
  and link it there when relevant; a planning mark never closes G141.
