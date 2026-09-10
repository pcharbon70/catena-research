---
title: "2026-09-10 Hot Code Upgrade"
kind: journal
created: "2026-09-10"
tags: [specification, concurrency, runtime, compatibility]
aliases: []
---

# 2026-09-10 Hot Code Upgrade

## Scope

Execute [G092](../20-notes/language-completion-plan-semantics.md#item-092-hot-code-upgrade-g092)
from C090 merge `747d6340c271f8d60a15dcf15f71d3be37e54823`.
Revision `0.1.79` is covered by the user's session-wide approval. CP-092-1..7
retain their recommended selections.

## Implementation decisions

| Decision | Four alternatives | Recommended and selected |
| --- | --- | --- |
| HU-I01 Upgrade point | A quiescent; B arbitrary frame; C restart only; D inferred | A: it gives a checkable state boundary. |
| HU-I02 Descriptor identity | A mutable tags; B exact artifact/interface/schema/evidence digests; C filenames; D timestamps | B: immutable identities make preflight reproducible. |
| HU-I03 Interface change | A any SemVer; B C028 nonbreaking classifier; C byte equality only; D unchecked | B: the existing semantic contract decides compatibility. |
| HU-I04 Migration execution | A arbitrary I/O; B bounded pure checked callback; C host cast; D resumption reuse | B: failures remain precommit and state-typed. |
| HU-I05 State bound | A unbounded; B 16 MiB maximum with selected lower limit; C record count; D heap guess | B: serialized bytes are measurable and discloseable. |
| HU-I06 Time bound | A infinite; B positive limit up to 5 seconds; C reductions exposed; D wall-clock success promise | B: exhaustion is explicit without exposing scheduler accounting. |
| HU-I07 Coexistence | A unlimited; B active plus one draining; C immediate purge; D closure rewriting | B: it matches the target ceiling and bounds retention. |
| HU-I08 Quiescence blockers | A ignore; B capability/resumption/frame/child/resource inventory; C layout only; D operator judgment | B: semantic authority cannot migrate by representation. |
| HU-I09 Drain messages | A drop; B queue in order until commit; C deliver to mixed code; D reject silently | B: admitted messages survive the controlled pause. |
| HU-I10 Precommit rollback | A snapshot restore; B rerun init; C undo effects; D terminate | A: the exact old state remains available. |
| HU-I11 Postcommit rollback | A automatic; B explicit reverse migration; C restore stale bytes; D unsupported always | B: state conversion is checked while external history stays honest. |
| HU-I12 OTP adapter | A raw load/purge; B managed suspend/change/resume; C relup as language semantics; D no adapter | B: it is the narrow documented process transition. |
| HU-I13 Distributed admission | A global instant; B nodes report exact old/new set; C accept any version; D rely on TLS | B: coordination is explicit without an atomicity fiction. |
| HU-I14 Evidence | A mutable latest; B exact digest plus lifecycle/trust record; C log text; D tests alone | B: governance survives reproduction and review. |

## Verification route

Exercise compatible migration, every quiescence blocker, wrong artifacts and
interfaces, third node version, message arrival during drain, second-upgrade
refusal, failed and exhausted migration, snapshot restoration, explicit reverse
migration, missing reverse migration, and the actual OTP system-message path.

## Results

Compiler [PR 161](https://github.com/pcharbon70/catena/pull/161) merged feature
commit `97ab35d` as `7ee602f815f92bd05591987519be7597b7ef66b1`
into `rewrite`. The complete suite passes 1,063 tests; production compilation,
escript construction, trust audit, and diff checks pass. The
[normative contract](../60-specification/hot-code-upgrade/checked-migration-and-activation.md)
promotes G092 to C092 without promising arbitrary live-frame replacement,
network-wide atomic activation, or reversal of external effects.
