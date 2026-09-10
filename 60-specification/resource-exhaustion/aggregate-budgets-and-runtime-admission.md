---
title: "Aggregate Budgets and Runtime Admission"
kind: specification
created: "2026-09-10"
status: normative
spec_version: "0.1.75"
tags: [specification, conformance, implementation-limits, runtime]
aliases: []
---

# Aggregate Budgets and Runtime Admission

## Status and authority

C129 defines revision `0.1.75` under [authority](../../SPECIFICATION-AUTHORITY.md),
[conformance vocabulary](../../CONFORMANCE-VOCABULARY.md), and
[implementation limits](../../IMPLEMENTATION-LIMITS.md). It executes the
[reviewed resource-exhaustion plan](../../20-notes/language-completion-plan-delivery.md#item-129-resource-exhaustion).
This revision adds checked compiler and runtime APIs without choosing the future
surface-language vocabulary owned by P109 (`RX-OBL-001`).

The compiler contract covers each check or compilation transaction and each
package publication transaction. The runtime contract covers only an explicitly
created bounded queue. Raw local send retains C010 and C085 ownership; distributed
transport remains G091. Operating-system, emulator, scheduler, storage, and
host-fatal failure remain outside recoverable language behavior.

## Aggregate compiler input

Every compiler transaction MUST account for the complete supplied source set
before semantic checking. It admits at least 128 source files and 16,777,216
aggregate source bytes. The bootstrap implementation configures 256 files and
67,108,864 bytes. File count is the number of supplied logical source and
interface files after path de-duplication; bytes are the sum of their exact
stored or submitted byte lengths (`RX-OBL-002`).

After decoding, the transaction MUST account for the whole syntax or semantic
input tree. Maps, lists, tuples, structures, keys, and leaves each contribute
their recursively visited nodes. The portable minimum is 100,000 nodes and the
bootstrap configuration is 200,000. This aggregate check supplements every
per-parser depth and node check; it does not reinterpret malformed input or an
inconclusive evidence bound (`RX-OBL-003`).

Single-source JSON and kernel checking and compilation apply source-byte and
decoded-tree accounting. Strongly connected component compilation applies the
same limits to all member sources and their decoded trees. Package compilation
also counts its manifest, module sources, interfaces, governance document, and
external trust root before loading them (`RX-OBL-004`).

## Publication and diagnostics

A package publication transaction MUST prepare its complete output set and
account for its aggregate bytes before committing any final output. The portable
minimum is 16,777,216 output bytes and the bootstrap configuration is 67,108,864.
Refusal leaves every previously published output unchanged and publishes no
partial replacement (`RX-OBL-005`).

`LIM006` reports aggregate file-count exhaustion, `LIM007` aggregate source-byte
exhaustion, `LIM008` aggregate decoded-node exhaustion, and `LIM009` aggregate
output-byte exhaustion. Each report contains `limit_id`, `minimum_supported`,
`configured`, `observed`, and `unit` as required by the implementation-limit
policy. The exact threshold succeeds; the next unit is refused. Invalid budget
API input is refused without being disguised as exhaustion (`RX-OBL-006`).

Compiler refusal occurs before the affected successful check, compilation, or
publication result exists. It is neither a Catena value nor a proof that the
source is semantically invalid. A higher configured bound cannot weaken any
language rule (`RX-OBL-007`).

## Explicit bounded runtime queues

A bounded queue is created with positive message and encoded-byte capacities and
one overload policy. The bootstrap ceilings are 65,536 messages and 67,108,864
bytes. Each admitted payload counts one message and its deterministic Erlang
external-size estimate. That estimate defines admission accounting; it does not
claim to measure resident heap, shared subterms, garbage-collector work, or node
memory (`RX-OBL-008`).

Any holder of the unforgeable queue handle can offer a payload. Only the creating
owner can take, inspect, or close it. Accepted payloads leave the queue in
per-admission FIFO order. A forged handle is refused. P085 remains responsible
for restricting public message payloads to Catena-sendable values before this
admission layer (`RX-OBL-009`).

Under `reject`, an offer that would exceed either selected capacity returns an
explicit overloaded result, increments the rejection observation, and leaves all
admitted payloads intact. It cannot report success, silently discard an admitted
payload, retarget it, or reorder the queue (`RX-OBL-010`).

Under `terminate`, the exceeding offer returns explicit capacity exhaustion, the
queue terminates with that reason, and the owner receives one queue-identity-bound
exit observation. Its already admitted payloads are then discarded by the
declared terminal policy. The result does not claim that they were processed
(`RX-OBL-011`).

Owner death cancels the queue. Explicit close reports the count and encoded bytes
discarded and terminates normally. Closing while full or after rejected offers
therefore provides an observable, bounded cleanup path. Queue ownership does not
transfer implicitly (`RX-OBL-012`).

## Denial of service and residual failure

The bounded queue prevents one admitted queue from growing beyond its selected
logical count and encoded-byte estimate. It does not reserve physical memory,
make scheduling fair, bound producer CPU, constrain raw BEAM mailboxes, or keep a
node alive after emulator or operating-system exhaustion. Deployments MUST apply
process, node, distribution, container, and storage controls when those threats
matter. A host-fatal termination can prevent Catena cleanup and supplies no
recoverable Catena result (`RX-OBL-013`).

Raw local send is unchanged. A component requiring overload feedback MUST route
through an explicit admitted capacity service rather than infer a hidden quota
from raw mailbox behavior. Remote admission, acknowledgements, retries, and
partition behavior remain outside this revision (`RX-OBL-014`).

## Profile and conformance

The machine-readable profile MUST expose all four aggregate compiler limits,
transactional output status, runtime ceilings, byte-accounting method, overload
policies, raw-send status, silent-loss prohibition, and absence of host-fatal
recovery. Tests MUST cover each exact threshold and next-unit refusal, aggregate
small inputs, public compiler integration, bounded rejection and FIFO retention,
several producers, owner-only consumption, termination observation, cancellation
under pressure, owner death, and profile disclosure (`RX-OBL-015`).

## Rationale and evidence (non-normative)

The [implementation journal](../../50-journal/2026-09-10-resource-exhaustion.md)
records fourteen four-way decisions and executable evidence. The
[runtime resource-control source note](../../30-sources/erlang-otp-29-runtime-resource-controls.md)
supports separating logical admission from VM memory and host survival. The
contract consequently gives code a checked overload boundary while stating where
deployment controls remain necessary.
