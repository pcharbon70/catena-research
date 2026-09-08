---
title: "Erlang/OTP 29 Time and Process BIFs"
kind: source
created: "2026-09-08"
authors:
  - "Ericsson AB"
published: "2026"
citation_key: "erlangOtp29TimeProcessBifs"
container: "Erlang/OTP ERTS documentation"
edition: "29.0.4"
url: "https://raw.githubusercontent.com/erlang/otp/OTP-29.0.4/erts/preloaded/src/erlang.erl"
accessed: "2026-09-08"
tags:
  - beam-vm
  - erlang
  - actors
aliases: []
---

# Erlang/OTP 29 Time and Process BIFs

## Reference

Ericsson AB. *Erlang BIFs and predefined types*, OTP 29.0.4.
[Version-pinned documentation and declarations](https://raw.githubusercontent.com/erlang/otp/OTP-29.0.4/erts/preloaded/src/erlang.erl), accessed 2026-09-08.

## Findings

The `spawn_opt` documentation admits link and monitor options and returns the
monitor reference with the PID. `unlink/1` guarantees that the removed link
cannot subsequently affect the caller, while warning that trapping callers
can already have received an exit message. Monotonic time has a local origin,
can repeat between calls, and supports explicit unit conversion.

## Relevance and limits

These contracts support the release-helper lifecycle and deadline arithmetic
in the [resource-lifetime experiment](../50-journal/2026-09-08-resource-lifetime.md).
They do not establish realtime scheduling, cleanup after VM loss, or permission
to move a process-affine foreign resource. Catena's lifetime contract must
supply those admission boundaries itself. The companion
[process note](erlang-otp-29-processes.md) covers signal and mailbox ordering.
