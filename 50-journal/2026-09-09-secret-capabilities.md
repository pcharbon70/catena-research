---
title: "2026-09-09 Secret Capabilities"
kind: journal
created: "2026-09-09"
tags: [specification, conformance, security]
aliases: []
---

# 2026-09-09 Secret Capabilities

## Scope

Execute [P131](../20-notes/language-completion-plan-delivery.md#item-131-secrets-and-capabilities)
from C127 compiler merge 5c85d0b21a322c98f09145431bc7d24514e3719c.
The exact revision 0.1.72 is covered by the user's session-wide approval.
The completed contract is [C131](../60-specification/secret-capabilities/sealed-values-and-protected-delivery.md).

## Implementation decisions

CP-131-1..3 retain their recommendations. Each implementation fork considers four
alternatives and selects the agent's recommendation.

| Decision | Four alternatives | Recommended and selected |
| --- | --- | --- |
| SC-I01 Representation | A ordinary strings; B opaque vault references; C hashes as secrets; D compiler-held signing keys | B: keep credential bytes outside ordinary program values. |
| SC-I02 Sensitivity propagation | A redact final logs only; B keep transformations and recipient replies sealed; C infer arbitrary string similarity; D expose derived values | B: sensitivity follows every supported transformation, including nested replies. |
| SC-I03 Retrieval | A ambient environment reads; B explicit supplied providers and scoped lookup; C global credentials singleton; D embed bytes in manifests | B: credential lookup is an explicit authority-controlled operation. |
| SC-I04 Recipient admission | A arbitrary callbacks; B exact verified foreign descriptors or restricted environmental process/network grants; C any URL; D blanket VM trust | B: transport has a named checked boundary; recipient behavior remains trusted. |
| SC-I05 Process transport | A argv secrets; B private stdin through approved snapshot executables; C inherited environment; D temporary plaintext file | B: reuse C106 ownership and explicit process environment without publishing credential bytes. |
| SC-I06 Observations | A print payload hashes; B redacted handles and payload-free audit status; C log returned exceptions; D remove all diagnostics | B: low-entropy credentials must not acquire public guessing oracles through manifests. |
| SC-I07 Crash handling | A normal server state reports; B sensitive processes plus redacted status and closed failure labels; C catch only RuntimeError; D assume no crashes | B: inspect the full worker/manager path, with host compromise explicitly excluded. |
| SC-I08 Authority narrowing | A global revoke; B owner-bound subset scopes with ancestor revocation; C bearer string labels; D no attenuation | B: inherit the capability discipline established by C106/C127. |
| SC-I09 Cancellation | A kill then claim cleanup; B cancel owning adapters and publish only after cleanup evidence; C expose partial reply; D ignore pending jobs | B: suppress sensitive outcomes and preserve unconfirmed-cleanup failures. |
| SC-I10 Native access | A assume types sandbox NIFs; B retain explicit foreign/native trust and refuse arbitrary secret-native forms; C share all VM credentials; D call every native package safe | B: no secrecy guarantee from malicious admitted native code or the VM administrator. |
| SC-I11 Artifacts | A public digests of secret bytes; B reject secret-reference artifact inputs and redact observation-only metadata; C serialize vault state; D silently write plaintext | B: artifact identity remains exact and public, while secret material stays external. |
| SC-I12 Bounds | A unlimited vault; B finite scopes/objects/jobs/bytes and checked transformation growth; C truncate secrets; D timeouts alone | B: explicit refusal preserves whole-value meaning and bounded cleanup. |
| SC-I13 Host-state defenses | A process sensitivity alone; B combine OTP sensitivity, status redaction and constrained recipient transport; C promise OS sandboxing from BEAM; D disable all runtime reporting | B: complementary controls with independently stated residual limitations. |
| SC-I14 Public adoption | A invent new source vocabulary; B internal checked host boundaries now, source/build adoption at their existing gates; C label old raw strings safe; D defer all implementable transport | B: respect the user vocabulary hold while producing executable protection. |

| SC-I15 Reply lineage | A relabel replies with delivery scope only; B retain every originating scope in replies and projections; C revoke the entire vault; D prohibit replies | B: parent delivery cannot launder a revoked child's credential. |
| SC-I16 Unmarked context observations | A redact markers only; B fixed diagnostics and trace events throughout the secret scope; C hash raw messages; D retain exception paths | B: errors can contain transformed unmarked bytes. |
| SC-I17 Compiled integration | A raw byte results; B checked Unit entry with private invocation reference indices; C invent public syntax; D host-only demonstration | B: executable capability integration respects the vocabulary hold. |
| SC-I18 Network protection | A arbitrary plaintext endpoints; B explicit loopback broker only; C claim loopback authenticates peers; D ambient HTTP credentials | B: local broker trust is explicit; remote authenticated transport needs separate admission. |
| SC-I19 Cleanup evidence | A timer mock only; B real stalled worker and seven-second force deadline; C claim kill proves cleanup; D suppress release failure | B: the exercised deadline produces unconfirmed cleanup. |
| SC-I20 Host inspection | A promise hostile-VM secrecy; B separate protected observations from privileged state inspection; C rely only on Inspect; D claim memory erasure | B: sys.get_state and malicious native code remain outside the guarantee. |
| SC-I21 Artifact refusal | A redact identity bytes silently; B fixed refusal before public secret-marker serialization; C publish secret hashes; D embed provisioning inputs | B: preserve public identity semantics without credential guessing oracles. |

## Evidence and investigation

The existing C106 process service snapshots approved executables, supplies an
explicit environment, transports input privately and owns process-group cleanup.
Its session currently retains raw arguments/results for ordinary service calls;
a secret-delivery path therefore needs explicit observation protection across
those managers and workers, rather than just redacting the final caller result.
The foreign session likewise stores typed results and traps.

The [OTP resource-controls source](../30-sources/erlang-otp-29-runtime-resource-controls.md)
now records the documented sensitive-process behavior. The
[server status source](../30-sources/erlang-otp-29-server-status-redaction.md)
provides the separate crash/status formatting mechanism. Neither implies protection
from a compromised host, arbitrary admitted native code or secure erasure of all
copies in VM memory.

## Verification route

Use synthetic sentinel credentials, never real user credentials. Exercise exact
recipient transport, denied/forged/expired handles, attenuation, revocation,
transformed and nested results, cancellation, crashes and owner death. Inspect
public diagnostics, trace/history, audit/status output and artifact paths; verify
that all successful secret-dependent results remain sealed. Record cleanup limits
and actual tests before claiming completion.

## Results

The compiler suite passed **1,015 tests**, including 17 new secret-capability
tests. The new cases execute a compiled capability entry, a real approved process
with credential stdin and a real loopback TCP broker. They cover denied/forged/
cross-owner handles, narrowing, expiry, owner death, child revocation, sealed
base64/hex/concatenation, nested recipient replies, cancelled/crashing workers,
status/diagnostic/trace protection and public artifact refusal. All credentials
are synthetic test sentinels. Authorized recipient observations intentionally
contain those bytes; public Catena observations do not.

Two investigation failures produced concrete regressions: a vault crash reason
initially escaped through mandatory cleanup failure, and completed recipient
replies initially dropped origin lineage. Closed failure labels and reply sealing
now preserve the intended guarantees. The real suspended-worker test takes at
least 6.5 seconds and returns unconfirmed cleanup after the seven-second deadline;
it does not treat forced termination as release evidence.

The reviewed trust baseline now covers **190 source files and 23 data inputs**,
with digest `791c772618912ee9438fd8312b542a47580ca99ee5af797c832341ae431318e6`.
Three new vault/transport files belong to runtime; the checked program belongs
to lowering. Changed observation, adapter, assurance and conformance call sites
were reviewed, and the erasure/diagnostic guarantee records secret tests plus
explicit host/OTP/recipient trust. Syntax-only unchanged literal or guard edits
remain outside the C126 scanner's semantic claims.

Validation commands are `mix test`, `MIX_ENV=prod mix compile --warnings-as-errors`,
`MIX_ENV=prod mix escript.build`, `mix run scripts/check_trust_inventory.exs`,
`python3 validate_archive.py` and `git diff --check` in their owning repositories.
The full suite retains historical test-only unused-helper warnings and intentional
trap logging; these do not indicate a production compiler warning.

## Remaining integration boundaries

General source/build adoption remains with P109/P121. Arbitrary secret-native ABI
forms and authenticated remote transport are not admitted here. The host can
inspect private VM state or deliberately unwrap provisioning inputs; approved
recipients can misuse delivered credentials. The contract supplies no OS sandbox,
secure erasure or whole-host noninterference theorem. These limitations are
reported in the normative contract and machine profile, not hidden by a checkbox.

## Delivery

Compiler [PR 154](https://github.com/pcharbon70/catena/pull/154) merged feature
`92d524adcc26013141706fedbc00c0f7b4400a10` as
`20ae238e6b018d3c39d300aa4a8a8f23d89502aa`. The compiler returned to `rewrite`,
synced with origin, then deleted the feature branch locally and remotely.
Production compilation with warnings as errors, escript construction, actual
machine conformance output and the trust audit passed. Archive validation passed
661 documents, 84 directories, 127 source notes, 198 specification chapters and
946 traced-status obligations (851 traced, 74 partial, 21 untraced).
