---
title: "Native Value Role Implementation"
kind: journal
created: "2026-09-09"
tags: [language-design, foreign-boundary, beam-vm]
aliases: []
---

# Native Value Role Implementation

## Starting point and scope

The P096 executed milestone merged through
[compiler PR 143](https://github.com/pcharbon70/catena/pull/143) and
[research PR 93](https://github.com/pcharbon70/catena-research/pull/93).
Both integration branches were synchronized before deleting their feature
branches. Compiler `rewrite` was `cc039c57aacc3b92a2ea44fd26cd3c7304bf17dc`;
research `main` was `a2015ab993f7ad3fcf3fe6ab3f434f8eb4fa5036`.
This work uses `codex/native-value-roles`. Session-wide user approval covers
`0.1.62`; no continuation is scheduled.

The [CP-097 plan](../20-notes/language-completion-plan-delivery.md#item-097-beam-native-values)
selects typed native roles, selective equality and checked data mappings. The
original forks are in the [decision register](../20-notes/design-decision-register.md).
The [normative C097 inventory](../60-specification/native-value-roles/typed-admission-and-native-identity.md)
completes the native-kind admission/exclusion gate without selecting public
source vocabulary or claiming G098's native loader is complete.

## Implementation decisions

| Decision | Four alternatives explored | Recommended and selected |
| --- | --- | --- |
| NV-I01 | A: one dynamic host-term type; B: registered opaque roles; C: JSON-encode native identity; D: exclude every native kind. | **B.** Reuses immutable data codecs and exposes identity only through explicit authority. |
| NV-I02 | A: accept arbitrary PID wrappers; B: trusted local-PID grant plus mailbox codec and registry token; C: infer mailbox types from one message; D: spawn a new actor for every conversion. | **B.** Checks our outgoing messages without pretending to prove arbitrary native receiver behavior. |
| NV-I03 | A: kill every supplied PID at scope exit; B: borrowed send authority with scope-owned wrapper lifetime; C: immortal send handles; D: unlink all ownership. | **B.** Ends the granted authority while preserving the independently owned target. |
| NV-I04 | A: expose liveness as send success; B: preserve Unit even for dead targets; C: retry dead sends; D: throw on a pre-send liveness check. | **B.** Matches C010 and avoids a racy invented delivery acknowledgement. |
| NV-I05 | A: admit every raw reference; B: create fresh scope-owned correlation references; C: stringify references; D: make reference equality a pure primitive. | **B.** Supplies useful correlation identity through matching host declarations without generic native ingress. |
| NV-I06 | A: transfer every operation; B: transfer only process send authority; C: prohibit all cross-process use; D: transfer scope control with each handle. | **B.** Keeps reference/host-call control local and permits checked process communication. |
| NV-I07 | A: universal native equality; B: exclude handle comparison and check declared role operations; C: compare wrapper fields; D: disable equality for all data. | **B.** Preserves C035's type-directed data semantics and avoids pointer observations in pure laws. |
| NV-I08 | A: reopen binary/map semantics; B: reuse C095 closed codecs; C: trust raw keys and UTF-8; D: convert every binary to text. | **B.** Retains complete bounds, exact record fields and distinct Bytes/Text meanings. |
| NV-I09 | A: raw host fun admission; B: use P096's verified scoped callback role; C: immortal callback table; D: erase captured values. | **B.** Existing executable ownership/type checks are the correct native fun boundary. |
| NV-I10 | A: admit ports by shape; B: explicitly exclude open/closed ports until G098's service contract; C: silently close supplied ports; D: infer trust from executable names. | **B.** The native-kind gate allows justified exclusion; packaging and cleanup remain the next owner's work. |
| NV-I11 | A: widen historical 0.1.61 scopes; B: require exact 0.1.62 for native roles while retaining old declarations; C: relabel old artifacts; D: accept any newest revision. | **B.** Makes the semantic addition explicit and preserves old profile boundaries. |
| NV-I12 | A: allow opaque values as record substitutes; B: separate value-shape recognition from registered authority; C: make classification perform network/process queries; D: expose raw identity for validation. | **B.** The classifier stays structural, while every use checks its live registry. |

## Execution and boundaries

`Foreign.NativeValue` defines exact role descriptions, explicit scope setup,
indexed opaque handles and checked send authority. The existing foreign manager
owns the registry. Only 0.1.62 declarations accept matching native-role arguments;
0.1.61 setup refuses both those declarations and native grants. The `Type` and
kernel checker entry points expose sidecar role judgments, and `Values` excludes
native handles from comparison. Retained kernel source is not widened.

Witnesses send typed Int messages through a borrowed PID, transfer only send
permission to another process, pass a fresh reference to a granted host argument,
and refuse copied/forged/wrong-role handles. A reference used as a process handle
must return an explicit refusal; review corrected a pattern-mismatch fallthrough
before its first passing test run so it cannot return registry contents.

Dead-target sends return Unit. Scope exit expires handles without killing the
borrowed PID. Reference handles fail after scope exit and cannot transplant into
another scope. A one-megabyte binary round-trips under its declared bound; a
smaller bound, invalid UTF-8 and unsupported/extra map keys are refused. A small
local `cat` process supplies live and closed port witnesses; neither is admitted,
and the fixture closes the port. Raw fun admission remains refused; the P096
callback suite continues to exercise the admitted alternative.

## Verification

The first combined native-role and foreign-adapter run passed 20 tests. Exact
selection and expired-reference witnesses were then added. Final full-suite,
production and archive checks are recorded before commit.

Final validation passed **887 compiler tests**. After adding explicit grant/send
capacity witnesses, the seven native-role tests passed again. Production
`MIX_ENV=prod mix compile --warnings-as-errors` and
`MIX_ENV=prod mix escript.build` passed. Archive validation passed with 625
documents, 74 directories, 121 source notes, 188 specification chapters and
836 obligations (741 traced, 74 partial, 21 untraced). Both diffs passed
`git diff --check`. Checklist counts are 100 complete, 26 partial, 13 gaps
and two deferred items.

Compiler implementation commit: `73be7baee5ac1eea2a431e62bd59bbb64337c93d`.
