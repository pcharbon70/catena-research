---
title: "2026-09-12 Interactive Environment"
kind: journal
created: "2026-09-12"
tags: [specification, tooling, effects, resources]
aliases: []
---

# 2026-09-12 Interactive Environment

## Scope

Execute G120's grammar-independent portion at `0.1.95` while retaining the
P109 public-REPL hold. CP-120-1..3 select explicit capabilities, immutable
successive generations, and bounded redacted history. This slice implements
the owned retained-input session boundary that is valid before public input
syntax, editing, recovery, and display rules exist.

## Implementation decisions

| Decision | Four alternatives | Recommended and selected |
| --- | --- | --- |
| IS-I01 Input | A public source; B checked retained JSON or kernel; C raw Elixir; D arbitrary BEAM terms | B: existing checked formats exercise semantics without choosing P109 grammar. |
| IS-I02 Owner | A any caller; B creating process only; C global server; D bearer token alone | B: one process supplies a clear authority and lifetime root. |
| IS-I03 Capability declaration | A ambient host services; B explicit duplicate-free closed set; C pure only; D infer from runtime calls | B: interactive work obeys the same environmental authority contract. |
| IS-I04 Effect admission | A execute then observe; B require a closed verified row contained in the session set; C trust names; D ignore effects | B: denied authority cannot start. |
| IS-I05 Load validation | A retain bytes unchecked; B run the matching checker before retention; C type-check on first call; D accept compiler crashes | B: every generation has checked-core authority. |
| IS-I06 Source identity | A filename; B SHA-256 of exact submitted bytes; C timestamp; D module name | B: generation evidence remains bound to its input. |
| IS-I07 Replacement | A mutate active core; B explicit replacement creates a new generation; C reset silently; D hot-patch workers | B: replacement is visible and does not impersonate C092 upgrade. |
| IS-I08 Numbering | A random IDs; B module-local monotonic integers from zero; C timestamps; D one global counter | B: exact selection is simple and deterministic. |
| IS-I09 Retention | A unbounded; B newest 32 per module; C active only; D disk cache | B: earlier selection is useful within a declared finite bound. |
| IS-I10 Selection | A always newest; B active by default with exact retained override; C oldest; D source digest prefix | B: ordinary use is convenient while reproduction stays exact. |
| IS-I11 Evaluator | A production BEAM compilation; B bounded reference evaluator; C host eval; D symbolic result only | B: existing independent semantics provide deterministic preparatory execution. |
| IS-I12 Fuel | A wall time only; B positive steps, default 100,000 and maximum 10,000,000; C unbounded; D reductions | B: semantic exhaustion remains portable and explicit. |
| IS-I13 Async work | A block every call; B monitored per-job worker; C unmanaged task; D global pool without ownership | B: completion, failure, interruption, and close are observable per job. |
| IS-I14 Handles | A bare reference; B owner/session/reference tuple; C worker PID; D mutable registry name | B: misuse across sessions or owners fails before control. |
| IS-I15 Wait race | A lose early results; B retain terminal results for later wait; C poll worker; D rerun evaluation | B: completion before wait has the same result as completion after wait. |
| IS-I16 Interrupt | A send and claim success; B kill and confirm termination before cancellation; C cooperative flag only; D abandon worker | B: successful interruption means owned work is gone. |
| IS-I17 Close | A stop immediately; B terminate and confirm every pending worker, or return retryable timeout; C detach workers; D wait forever | B: cleanup is mandatory, bounded, and honestly reported. |
| IS-I18 Owner death | A orphan session; B session observes owner death and terminates children; C transfer ownership silently; D persist globally | B: the creating scope remains the lifetime root. |
| IS-I19 History | A unbounded full values; B newest 256 classified metadata entries; C none; D external shell history | B: useful evidence has a fixed memory bound. |
| IS-I20 Value policy | A always retain values; B redact by default with session opt-in and per-evaluation sensitivity override; C stringify; D hash every value | B: ordinary and sensitive observations have explicit disclosure. |
| IS-I21 Governance | A REPL success grants approval; B refuse governed claims pending external admission; C approve local users; D omit status | B: evaluation evidence does not manufacture authority. |
| IS-I22 Trust placement | A unclassified helper; B reviewed tools-profile component; C source authority; D runtime guarantee | B: session boundary calls remain inventoried without defining syntax. |

Every recommendation was selected under the user's delegated decision
authority. No recommendation was overridden.

## Executed evidence

Compiler [PR 188](https://github.com/pcharbon70/catena/pull/188) merged feature
commit `eb04f30` as merge commit `1bb1da4` into `rewrite`. Five focused cases
exercise retained input, immutable replacement, exact generation selection,
bounded evaluation, completed and interrupted jobs, confirmed close cleanup,
redacted and opted-in history, owner checks, governance refusal, lifecycle,
profile publication, and the P109 hold.

Corrective compiler [PR 189](https://github.com/pcharbon70/catena/pull/189)
publishes the 1,000-millisecond cleanup-confirmation limit and directly
exercises owner-death termination.

Compiler [PR 190](https://github.com/pcharbon70/catena/pull/190) directly
exercises effect-capability denial, generation pruning, exact oldest-retained
selection, history truncation, dropped-entry accounting, and the maximum
evaluation budget. Eight focused cases and the complete 1,174-test suite pass.

Compiler [PR 191](https://github.com/pcharbon70/catena/pull/191) directly
verifies that running generation-zero work survives active replacement and
that per-evaluation sensitivity overrides enabled value capture. Production
compilation with warnings as errors,
escript construction, reviewed trust-inventory verification, and
`git diff --check` pass. The approved trust update classifies
`lib/catena/tool/session.ex` in `tools-profile` and binds its final source
digest.

The [normative contract](../60-specification/interactive-environment/owned-retained-input-sessions.md)
makes the implemented boundary durable. G120 stays partial because public
input parsing, recovery, editing, display, and command syntax require P109.
