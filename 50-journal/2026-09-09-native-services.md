---
title: "Native Service Implementation"
kind: journal
created: "2026-09-09"
tags: [language-design, foreign-boundary, beam-vm]
aliases: []
---

# Native Service Implementation

## Starting point and scope

C097 merged through [compiler PR 144](https://github.com/pcharbon70/catena/pull/144)
and [research PR 94](https://github.com/pcharbon70/catena-research/pull/94).
Compiler `rewrite` was `8ae9977a87e3a3dc2c9089c7055215f5c861db6e`;
research `main` was `9682a8bbe20983b595685d00b2fae67f84997fd0`.
Both were synchronized before branch deletion. This slice uses
`codex/native-services`; session-wide revision approval covers `0.1.63`.
No continuation is scheduled.

The [CP-098 plan](../20-notes/language-completion-plan-delivery.md#item-098-nifs-and-ports)
and [original decision register](../20-notes/design-decision-register.md)
require working port/NIF execution with honest crash boundaries. The
[normative contract](../60-specification/native-services/signed-loading-and-owned-execution.md)
uses a narrow Float ABI, not final public language vocabulary.

## Implementation decisions

| Decision | Four alternatives explored | Recommended and selected |
| --- | --- | --- |
| NI-I01 | A raw native loading; B signed domain-separated native package with explicit external publisher/kind/unsafe grants; C trust filename; D compiler-global whitelist. | **B.** reuse existing canonical JSON and Ed25519 verification, preserve old governance envelopes. |
| NI-I02 | A reuse old semantic/artifact version; B exact 0.1.63 semantics plus separate native package envelope version 1; C mutate old package decoder; D latest implicit selection. | **B.**  |
| NI-I03 | A load arbitrary port as a data handle; B verified executable behind compiler-owned guardian and typed eight-byte Float protocol; C shell string command; D no native services. | **B.** initial narrow ABI is explicit and functional. |
| NI-I04 | A Port.close implies child death; B guardian owns child, monitors parent EOF/deadline and kills/reaps child before exit; C kill by unowned OS PID; D leave detached work. | **B.** no OS security sandbox or descendant-escape guarantee for malicious trusted code. |
| NI-I05 | A trust ordinary scheduler for everything; B explicit os-process or dirty-cpu admission plus fixture enif_thread_type evidence; C infer flags from names; D claim runtime can prove arbitrary native scheduler honesty. | **B.** signer obligations remain attestations. |
| NI-I06 | A in-process NIF implicitly safe; B explicit VM-crash acknowledgement and disposable-VM tests; C claim BEAM worker kill stops NIF; D silently turn NIF into port. | **B.**  |
| NI-I07 | A GC-only resource cleanup; B explicit idempotent close with native resource-destructor fallback; C arbitrary Catena effects in finalizer; D never free native state. | **B.**  |
| NI-I08 | A native timeout means rollback; B bounded caller wait and possible continuing native work/external effects; C unconditional retry; D no timeout. | **B.**  |
| NI-I09 | A generic ETF wire with attacker-controlled decompression; B fixed eight-byte big-endian binary64 wire and exact finite Float codec for first ABI; C infer type from response; D silently normalize nonfinite. | **B.**  |
| NI-I10 | A execute crashing fixture in main test VM; B run native NIF probe in separate timeout-bounded OS process; C omit crash evidence; D download opaque binary. | **B.** build retained C/Erlang source locally. |
| NI-I11 | A publisher signs only filename; B bind exact payload bytes, wrapper, support fingerprint, scheduler and unsafe obligations; C sign a mutable directory; D trust a copied checksum alone. | **B.**  |
| NI-I12 | A: execute guardian from escript virtual path; B: embed source bytes and copy into private scope directory; C: download guardian on demand; D: trust PATH-provided script. | **B.** Binds the actual helper bytes and works with escript packaging. |
| NI-I13 | A: accept unlimited calls after NIF timeout; B: poison further calls and retain close; C: retry in parallel; D: free native memory immediately. | **B.** Avoids accumulating potentially continuing work or invalidating an active resource. |
| NI-I14 | A: infer reaping from pipe close; B: explicit close control, post-reap acknowledgement and guardian exit; C: inspect arbitrary OS PID; D: ignore close outcome. | **B.** Separates observed cleanup from transport disappearance. |
| NI-I15 | A: reopen NIF module for every request; B: pin exact loaded wrapper/library identity; C: identify by filename only; D: automatically hot-swap native code. | **B.** Reuses identical code and refuses unsafe replacement. |
| NI-I16 | A: define an entire public FFI vocabulary; B: explicit retained unary Float service ABI; C: admit arbitrary ETF; D: defer all execution. | **B.** Executes the planned boundary while preserving the public-vocabulary constraint. |

## Implementation and evidence

`Foreign.Native.Package` reuses canonical JCS and Ed25519 verification with a
new native-envelope domain. Manifest and linker expose separate native entry
points. Explicit external publisher/kind/unsafe grants, exact file bytes,
payload bounds and the pinned C099 host fingerprint are checked before loading.
No retained Catena executable or governance format is widened.

`Foreign.Native` wraps a private manager in C080 mandatory cleanup. Owner-only
scope operations and a distinct release token separate calls from cleanup.
The port guardian is compiled into the loader, copied into a private directory,
and run through Python 3 without shell interpolation. It owns exactly its
direct child, rejects malformed/overlapping frames and confirms shutdown only
after kill/reap. A signed service's direct-child-only promise is an attestation;
this does not implement an OS sandbox against malicious code or descendants.

The NIF wrapper/library are signed together and pinned as one loaded identity.
Bounded linked workers call its private resource. Timeout poisons further calls
but still attempts explicit close. Native work can continue after process death,
so the result records that possibility. Idempotent native close and destructor
fallback share one physical-close counter in the retained witness.

The native fixture sources are `test/fixtures/native-service.c`,
`native-service-nif.c`, and `native-service.erl`; the isolated probe is
`native-service-probe.exs`. `native_services_test.exs` builds them with `cc`
using C11, all warnings as errors and the installed OTP headers. All NIF
execution occurs in an external `timeout 20 elixir --erl "+S 2:2"` process.
The crash witness invokes native `abort()` only there and requires nonzero,
non-timeout termination. The parent compiler-test VM survives.

Local witnesses preserve +0, -0, largest finite binary64 and smallest subnormal
bits through both paths. The documented NIF constructor refuses infinity and
NaN; the port decoder refuses an infinity bit pattern. Integer/native-handle
inputs fail before native execution. Tests cover publisher/unsafe/size/kind and
payload tampering, wrong scheduler admission, port child death, monotonic port
timeout, explicit double close, scope expiry, wrong owner, private-release-token
refusal, killed-owner guardian release and temporary-directory cleanup.
The NIF observes the actual dirty-CPU scheduler, confirms one physical close
after explicit double close, demonstrates destructor fallback for an abandoned
resource, and returns the continuing-work timeout classification.

The [OTP source note](../30-sources/erlang-otp-nif-float-construction.md) records
primary API claims. Its live documentation is OTP 29.0.6; these local witnesses
run on the separately pinned OTP 29.0.4/ERTS 17.0.4/Elixir 1.20.2 row.
No new supported-host claim follows from reading newer documentation.

## Verification

Initial focused native tests passed. The first full revision-discovery update
incorrectly replaced the previous list endpoint instead of retaining it;
those test expectations were corrected. A subsequent run exposed the missing
new lifecycle entry, which was added before final verification.
Final compiler, production, archive and diff results are recorded before commit.

Final full validation passed **892 compiler tests**, production compilation with
warnings as errors, and the production escript build. The five native-service
tests passed again after adding malformed port-header and false NIF scheduler
marker witnesses. Archive validation passed with 628 documents, 75 directories,
121 sources, 189 specification chapters and 844 obligations (749 traced,
74 partial, 21 untraced). Both diffs passed `git diff --check`. The checklist
now totals 101 complete, 26 partial, 12 gaps and two deferred items.

Compiler implementation commit: `af8a82b3df106c4fd66ad822bb4680736d3dd1e7`.
