---
title: "Erlang Type Boundary Implementation"
kind: journal
created: "2026-09-09"
tags:
  - language-design
  - representation-independence
  - beam-vm
aliases: []
---

# Erlang Type Boundary Implementation

## Starting point and scope

C094 merged through [compiler PR 141](https://github.com/pcharbon70/catena/pull/141)
and [research PR 91](https://github.com/pcharbon70/catena-research/pull/91).
Compiler `rewrite` synchronized at `1acc431cda5ea01842b6a2be372e1f08f925b4aa`;
research `main` at `083b79754925173cd0df058dbacf1819958e75a6`. Both local and
remote feature branches were deleted after synchronization. C095 uses
`codex/erlang-type-boundary` in both repositories. No continuation is scheduled.
The user explicitly approved all semantic revision updates for this session.

The [reviewed CP-095 plan](../20-notes/language-completion-plan-delivery.md#item-095-erlang-type-boundary)
selects explicit codecs, expected typed conversion failure, recursive budgets
and strict finite Float. Those forks are already recorded in the
[decision register](../20-notes/design-decision-register.md).
The [0.1.60 contract](../60-specification/erlang-type-boundary/typed-conversion-and-preservation.md)
implements those decisions without selecting public vocabulary or a dynamic type.

## Implementation decisions

| Decision | Four alternatives explored | Recommended and selected |
| --- | --- | --- |
| ET-I01 | A: duplicate the scalar/ADT rules; B: reuse C093's checked data and nominal relations; C: trust native outer tags; D: infer types from payloads. | **B.** Preserves the existing type/layout ownership and avoids inconsistent coercion rules. |
| ET-I02 | A: impose a hidden recursion cutoff; B: expose node, byte and depth bounds and preflight the complete carrier; C: check only a successful prefix; D: recurse without a bound. | **B.** Whole-carrier validation includes otherwise ignored keys and tags and rejects unsupported handles before typed conversion. |
| ET-I03 | A: count only semantic fields; B: count the complete input and output representations independently; C: estimate size from the outer tuple; D: charge after reporting success. | **B.** Foreign transport metadata costs are visible; a compact input can require a larger semantic-output budget. C093's separate semantic checks remain in force. |
| ET-I04 | A: introduce a built-in list; B: require explicit roles in a verified declared two-constructor nominal type; C: accept any constructor-shaped tuple; D: prohibit Erlang lists. | **B.** Retains C042's declaration-based collections and supports useful proper-list ingress without vocabulary decisions. |
| ET-I05 | A: use the Erlang list as every Catena carrier; B: distinguish external encoding from the selected nominal runtime layout; C: force all modules to fixed layout; D: expose layout introspection to ordinary source. | **B.** Both backend helpers and independent verification use the selected Catena carrier, while the codec separately handles the wire list. |
| ET-I06 | A: admit raw PIDs/references/funs; B: infer authority from a wrapper shape; C: preserve their existing typed owners and exclude generic data admission; D: erase handles into strings. | **C.** General native authority remains P097/G098; C094 callbacks and C084 process handles retain their checked lifetimes. |
| ET-I07 | A: trust the earlier NIF conjecture; B: read the documented constructor contract and run an isolated native fixture; C: manufacture corrupted heap terms; D: normalize infinities silently. | **B.** Tests the supported API without invoking arbitrary heap corruption and preserves finite Float semantics. |
| ET-I08 | A: let the test NIF run inside the main test VM; B: compile it and invoke it in a separate VM; C: skip native evidence; D: download a binary library. | **B.** Keeps the local witness reproducible from the small retained C/Erlang sources and isolates native execution. |
| ET-I09 | A: add broad source syntax; B: publish exact programmatic codec selection without a new executable/interface/signed format; C: relabel old core; D: hide the semantic change under 0.1.59. | **B.** Registers 0.1.60 explicitly under the user's session approval while retaining all historical format boundaries. |

## Implementation and preservation evidence

`Foreign.Codec` implements closed data, re-derived nominal and declared-sequence
relations. `Foreign.Budget` preflights nodes, scalar-payload bytes and depth for
both incoming and outgoing carriers. Setup, payload and budget failures remain
explicit, with no successful prefix. `Type.foreign_codec`, the independent
verifier entry and both backend literal helpers connect the boundary to the
existing owners. A bounded corpus of lists of length 0 through 32 exercises
external round-trip and native-layout preservation, including complete rejection
of an invalid final element.

Tests cover closed nested records/variants/products, Int/Bool/Float distinctions,
Text/Bytes/Character rejection, signed-zero bits, large integers, zero-length
binaries, exact node/byte/depth thresholds, extra/missing fields, wrong
constructors, private/forged descriptor admission, improper lists, raw handles,
compact/uniform/fixed nominal layouts and both EAF lowerers.

The proof argument is structural induction over the checked schema and verified
constructor roles, backed by the codec/native round-trip corpus. It does not
claim a new mechanized whole-language proof or general arbitrary-host-call safety.

## Native Float correction

The [NIF API note](../30-sources/erlang-otp-nif-float-construction.md) records the
primary documentation. The isolated fixture uses only `enif_make_double` and
checks four finite bit patterns: positive zero, negative zero, maximum finite
binary64 and the smallest positive subnormal. All survive native construction
and the independent Erlang-to-codec call exactly. Positive infinity, negative
infinity and a NaN payload each produce bad-argument rejection; ETF decoding
also rejects those three patterns. Independent Erlang calls additionally
round-trip a nested record containing Int, Text and Bytes.

This corrects the unverified NIF conjecture in the
[31 August probe record](2026-08-31-beam-float-boundary-probes.md).
It does not make arbitrary unsafe C writes safe and does not expand the
supported-host matrix from the tested OTP 29.0.4/ERTS 17.0.4 runtime. The live
API page identified OTP 29.0.6; source and local observation are separate evidence.

## Reproduction and validation

Run `mix test` in the compiler repository. The `foreign_native` test compiles
`test/fixtures/foreign-float-nif.c` with the installed C compiler and Erlang
headers, compiles its independent Erlang wrapper, then executes
`foreign-float-probe.exs` in a separate Elixir VM with two schedulers. Temporary
native artifacts are removed after the test; no prebuilt binary is retained.

The full suite passed **867 tests** on the first registered 0.1.60 run. Native
and generated preservation witnesses are included. After adding the explicit
private-sequence rejection witness and obligation tags, all eight focused tests
passed. `MIX_ENV=prod mix compile --warnings-as-errors` and
`MIX_ENV=prod mix escript.build` passed. Archive validation passed with 619
documents, 72 directories, 121 source notes, 186 specification chapters and
815 obligations (720 traced, 74 partial, 21 untraced). Both repository diffs
passed `git diff --check`; current checklist totals are 99 complete, 27 partial,
13 gaps and two deferred items. The old G098 NIF bypass claim was corrected
in the current checklist as well as the historical probe record.

Compiler implementation commit: `2d7ed09c247807304a3b5cdf953cdf4a69b7b277`.
