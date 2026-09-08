---
title: "Erlang/OTP 29 Supervision"
kind: source
created: "2026-09-08"
authors:
  - "Ericsson AB"
published: "OTP 29"
citation_key: "erlangOtp29supervision"
container: "Erlang/OTP System Documentation"
edition: "29.0.4"
url: "https://github.com/erlang/otp/blob/OTP-29.0.4/system/doc/design_principles/sup_princ.md"
accessed: "2026-09-08"
tags:
  - actors
  - beam-vm
  - erlang
aliases: []
---

# Erlang/OTP 29 Supervision

## Reference

Ericsson AB. “Supervisor Behaviour.” *Erlang/OTP System Documentation*,
OTP 29.0.4. [Pinned documentation](https://github.com/erlang/otp/blob/OTP-29.0.4/system/doc/design_principles/sup_princ.md).
Implementation cross-check: [`supervisor.erl`](https://github.com/erlang/otp/blob/OTP-29.0.4/lib/stdlib/src/supervisor.erl),
particularly `add_restart` and `can_restart`. Both retrieved 2026-09-08.

## Findings

The three static strategies restart the failed child, all children, or the
failed child and later siblings. Child policy still governs whether failure
initiates a restart. Permanent children restart even after normal completion;
transient children restart after abnormal exit; temporary children never
restart, including after collateral sibling shutdown. Startup follows declared
order and termination reverses it. Startup waits for child start acknowledgments.

Restart intensity bounds attempts within a rolling period. Exceeding the bound
terminates children and supervisor. The pinned implementation uses monotonic
integer seconds and retains timestamps equal to the window threshold. Finite
shutdown first signals shutdown, waits, then forcibly kills a child that has not
terminated. A finite timeout for a nested supervisor can kill it before its
descendants terminate; the documentation recommends an unbounded supervisor
shutdown allowance for that host configuration.

## Relevance and limits

G089 needs an explicit typed policy subset and a narrow lifecycle adapter.
These are OTP rules, not automatic Catena language authority. Catena's bounded
cleanup requirement needs its own treatment of nested supervisors; merely
copying an arbitrary child-spec map would not establish cleanup guarantees.
The source supplies no static capability freshness, typed payload guarantee,
or fairness proof.

## Derived work

- [Supervision plan](../20-notes/language-completion-plan-semantics.md#item-089-supervision-g089) — selected policy inventory and gate.
- [Supervision workbench](../50-journal/2026-09-08-typed-supervision.md) — local model and adapter experiments.
