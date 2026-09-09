---
title: "2026-09-09 Environmental Effects"
kind: journal
created: "2026-09-09"
tags: [effects, entry-points, specification, conformance]
aliases: []
---

# 2026-09-09 Environmental Effects

## Scope and current state

Completed implementation of [C106](../20-notes/language-completion-plan-delivery.md#item-106-environmental-effects).
The semantic revision is session-approved 0.1.68. The launch amendment, real
adapters, cancellation/authority tests and compiled/reference witnesses are implemented. Existing zero-argument entries retain their
meaning. No public vocabulary is selected.

## Implementation decisions

The original CP-106-1..5 recommendations remain selected. Each implementation fork
below records four alternatives; later evidence can refine the choice explicitly.

| Decision | Question | Alternatives | Recommended | Selected | Rationale |
| --- | --- | --- | --- | --- | --- |
| EN-I01 | Entry channel | A ambient handler; B explicit authority-bundle parameter to a new closed entry wrapper; C process-global service registry; D no environment | B | B | The entry installs its own fresh lexical handlers from explicit authority values; retained zero-argument launches stay unchanged. |
| EN-I02 | Typed service input | A widen old source syntax; B unchecked host arguments; C exact 0.1.68 checked capability/value-tree profile; D encode every datum as Int | C | C | Combine already defined closed scalar carriers with lexical capability identity under a new verified boundary. |
| EN-I03 | Authority carrier | A raw lexical capability name; B caller-chosen token; C scoped opaque descriptor with explicit endpoint and private nonce; D global capability lookup | C | C | Private manager validation enforces issuer, owner, lifetime and attenuation; no lexical name or resumption becomes a value. |
| EN-I04 | Service separation | A all-powerful token; B one token per service with operation and resource subsets; C permission strings only; D infer rights from filenames | B | B | Grants can be denied and narrowed independently, including byte and lifetime limits. |
| EN-I05 | Cancellation | A block the manager during I/O; B kill the whole VM; C owned monitored workers with manager-side revocation and completion arbitration; D ignore timeouts | C | C | The manager remains responsive and gives each accepted request exactly one terminal answer. |
| EN-I06 | Scope end | A detach children; B process-global cleanup; C owner monitoring plus bounded worker/child cleanup on return, trap and death; D wait without bound | C | C | Return is shutdown and expired authority cannot revive resources. |
| EN-I07 | Filesystem authority | A string prefix followed by ordinary open; B resolve then open without race protection; C explicit root-relative path grants and descriptor-relative no-follow traversal; D unrestricted absolute paths | C | C | Path components are checked and opened relative to directory descriptors; symlink traversal is not authority. |
| EN-I08 | Filesystem helper | A assume portable openat in BEAM; B unsafe native NIF; C fixed Python/POSIX helper with explicit platform admission; D shell interpolation | C | C | Use documented directory-relative OS operations without a new in-process native dependency; unsupported hosts refuse this profile. |
| EN-I09 | Networking | A arbitrary URLs with redirects; B implicit DNS; C allowlisted numeric-IP/port TCP exchanges with finite send/receive limits; D unrestricted sockets | C | C | A concrete network service can be tested locally without hidden endpoint expansion or DNS authority. |
| EN-I10 | Process service | A arbitrary shell command; B inherited environment and PATH; C named grants for absolute executable, exact argv, explicit environment and cwd; D detached child execution | C | C | Requests choose only predeclared commands and bounded input/output; a guardian owns cancellation and child-group cleanup. |
| EN-I11 | Clock authority | A ambient current time; B explicit monotonic/wall/sleep operations; C wall time for deadlines; D compile-time host clock | B | B | Elapsed deadlines use monotonic time and wall observations remain distinct operations. |
| EN-I12 | Random authority | A implicit global PRNG; B deterministic bytes for production; C explicit bounded cryptographic-byte service and scripted fake; D arbitrary host randomness calls | C | C | Tests are reproducible while production randomness has a concrete declared source. |
| EN-I13 | Environment variables | A inherit all names; B implicit reads in compiler; C allowlisted names read through explicit service; D global mutation | C | C | Environment access is observable and does not change compiler inputs silently. |
| EN-I14 | I/O and logging | A default group leader; B implicit Logger; C explicitly granted device, bounded bytes and allowed logging levels; D ambient standard streams | C | C | Each effect uses a supplied endpoint; test devices can be isolated from the user's terminal. |
| EN-I15 | Expected failures | A raw errno and exceptions; B null; C closed per-operation result/failure schemas; D stringify every host answer | C | C | Denied, expired, cancelled, limited and service failures are typed and distinct from traps. |
| EN-I16 | Deterministic model | A arbitrary injected host callbacks; B real services in every test; C exact scripted request/response transitions under the same grant checks; D skip reference execution | C | C | Reference and compiled programs can replay identical traces while real adapters have separate integration witnesses. |
| EN-I17 | Manifest boundary | A widen retained package formats; B undocumented launch options; C separate exact environment-entry descriptor with complete reconstruction; D infer grants from imports | C | C | Program requirements are declared and checked; a declaration never creates host authority. |
| EN-I18 | Reference installation | A global host handler; B skip local handlers; C explicit environment-handler frames installed from the entry parameter; D replace requests before type checking | C | C | Normal lexical handlers retain precedence and only the new entry installs service handlers. |
| EN-I19 | Effect-result adoption | A unchecked BEAM result; B raw host terms; C closed data codecs and explicit typed success/error variants; D generic unsafe cast | C | C | The service schema must equal the source operation declaration and every result is validated before resumption. |
| EN-I20 | Operational scope | A rollback promises; B exactly-once external effects; C one local terminal answer with external effects possibly committed before interruption; D repeat cancelled operations automatically | C | C | Cancellation retires local work and authority but cannot reverse bytes already written or commands already executed. |

## Work-ahead and verification gates

1. Admit the exact checked capability/value-tree profile with independent
   verification while rejecting new scalar carriers in retained capability core.
2. Define exact operation schemas and service-specific, attenuable authority.
3. Deliver owned asynchronous requests, deterministic scripted adapters and real
   I/O, filesystem, TCP, clock, random, environment, logging and process adapters.
4. Generate a closed entry that accepts authority values and installs its own
   lexical handlers; add the explicit C027/C082 amendment and manifest boundary.
5. Compare reference and compiled traces, test denied/forged/expired authority,
   cancellation/revocation/shutdown races and actual service behavior.
6. Validate, commit, PR, merge, synchronize integration branches, delete the
   feature branches and then advance to the next eligible plan item.

## Evidence and follow-up

The existing C050 capability checker, C093 value-tree carriers, C080 resource
lifetime, C088 cancellation and C096/C098 adapters provide the starting machinery.
The retained grammar will continue to serve as a quoted decoder rather than being
silently widened. Primary OS and transport documentation is being checked as each
adapter is implemented; source notes and exact reproducible evidence will accompany
the completed contract.

## Initial executable evidence

The exact 0.1.68 checker now combines closed scalar carriers with C050 lexical
capability slots, while retained capability profiles reject those carriers.
Closed operation schemas and host grant attenuation cover all eight service
families. Scoped managers own monitored workers, arbitrate cancellation and
revocation, reject cross-owner or forged authority, and close on owner death.

Isolated integration tests have exercised explicit I/O/logging devices, bounded
random bytes, clock observations, allowlisted environment reads, relative file
reads/writes, symlink refusal, numeric-endpoint TCP exchange and cancellation of
an approved child process. Compiled entries accept an authority bundle and install
fresh handlers; scripted results and request traces agree with the reference path.
Full regression, further cleanup/race checks and the normative amendment remain
in progress. These observations are not a completion declaration.


## Further implementation decisions

All selections below are the agent's recommendations under the session's revision approval.

| Decision | Four alternatives considered | Recommended and selected |
| --- | --- | --- |
| EV-I21 Cleanup confirmation | A worker death implies cleanup; B explicit helper acknowledgement plus failure on missing confirmation; C unlimited waiting; D ignore release errors | B: preserve mandatory cleanup without claiming an unresponsive OS cooperated. |
| EV-I22 Control-channel reading | A buffered stream reads; B unbuffered exact packet reads; C poll a global file; D signals carrying command text | B: avoid a prefetched cancellation packet becoming invisible to the selector. |
| EV-I23 Executable identity | A mutable executable path throughout launch; B private bounded snapshot per invocation; C freeze all host dependencies; D permit arbitrary executable bytes from the entry | B: stable launched bytes with explicit trusted-host limits. |
| EV-I24 Empty authority | A reject pure launches; B direct lowering inside the same exact wrapper; C fabricate a dummy service; D ambient default service | B: empty authority is useful and has no synthetic privilege. |
| EV-I25 Scalar effect lowering | A widen every retained grammar; B reuse verified scalar lowering only after exact-profile verification; C serialize every scalar to Text; D disallow useful byte operations | B: preserve historical acceptance while adding checked environmental data. |
| EV-I26 Completion authenticity | A accept any completion tuple; B bind a private per-worker completion secret; C trust public request handles; D publish worker PIDs as authority | B: knowledge of a request handle is insufficient to forge its answer. |
| EV-I27 Result validation | A check only result type; B check whole carrier plus operation byte/count constraints; C silently truncate results; D trust injected models | B: fake services and real adapters cross the same explicit boundary. |
| EV-I28 Deadline arbitration | A accept any queued result after deadline; B cancellation first, then deadline before publication, then validated result; C rollback completed effects; D random arbitration | B: one terminal answer with no false transactional promise. |

## Completed local evidence

All eight real service families were exercised with explicit grants. A compiled
entry wrote through a supplied I/O device, and compiled/reference random entries
produced equal scripted results and request traces. Empty-authority launches and
ordinary local lexical handlers worked; absent authority, wrong schemas, forged
sidecars and retained-manifest reinterpretation were refused.

Real child cancellation and owner death were tested using an approved local
Python script that wrote its OS PID before sleeping. After the terminal answer or
scope-manager termination, the direct child was absent from Linux /proc. Return
and trap paths closed pending requests. These are local Linux observations, not
claims of testing every supported host or proving detached-descendant confinement.

The whole compiler suite passed **966 tests** after cleanup, completion-secret,
service-result and bundle-endpoint hardening. Scripted wrong-service failures,
oversized carriers, cross-owner/nonexistent authority, attenuation escalation,
revocation, expiry and request exhaustion have refusal witnesses. Retained
revision regression tests passed in the same run.

Primary evidence: [Python directory operations](../30-sources/python-directory-relative-os-operations.md),
[Python subprocess sessions](../30-sources/python-subprocess-session-ownership.md),
and [OTP passive TCP](../30-sources/erlang-passive-tcp-sockets.md).
The [C106 contract](../60-specification/environmental-effects/explicit-authority-and-closed-launches.md)
is the normative owner, including the explicit C027/C082 amendment. Public grammar,
managed-task composition and P096 effectful callback adoption are not claimed by
this profile.

A fault-injection test suspends an owned cooperative worker; forced termination
then produces mandatory-release failure with unconfirmed cleanup. The exact new
checker also refuses a handler-local capability escaping in a returned closure.
The helper never treats a missing acknowledgement as successful OS release.

## Final verification and provenance

Final verification passed **968 compiler tests**, production compilation with
warnings as errors, the production escript build and both repositories'
`git diff --check`. Archive validation passed **648 documents, 80 directories,
126 source notes, 194 specification chapters and 900 obligations** (805 traced,
74 partial, 21 untraced). Recounted checklist totals are **106 complete, 21 partial,
12 gaps and 2 deferred**.

Compiler implementation commit `705aa66dad9664481beb2e88bda8704c31c5e32e`
merged through [compiler PR 150](https://github.com/pcharbon70/catena/pull/150)
as `5f018fbcfcd92ed14884f35b6d91a51d3b730649`. The compiler `rewrite` branch
was synchronized with origin before deleting its feature branch. Commands were
`mix test`, `MIX_ENV=prod mix compile --warnings-as-errors`,
`MIX_ENV=prod mix escript.build`, `python3 validate_archive.py` and
`git diff --check`; the focused tests exercise the embedded helper directly.
