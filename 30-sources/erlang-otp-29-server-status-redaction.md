---
title: "Erlang/OTP 29 Server Status Redaction"
kind: source
created: "2026-09-09"
authors: ["Ericsson AB"]
published: "OTP 29"
citation_key: "erlangOtp2026serverStatusRedaction"
container: "Erlang/OTP STDLIB Reference Manual"
edition: "29.0.6"
url: "https://www.erlang.org/doc/apps/stdlib/gen_server.html"
accessed: "2026-09-09"
tags: [actors, beam-vm, erlang]
aliases: []
---

# Erlang/OTP 29 Server Status Redaction

## Reference

Ericsson AB. “gen_server.” Erlang/OTP STDLIB Reference Manual, OTP 29.0.6.
[Official callback reference](https://www.erlang.org/doc/apps/stdlib/gen_server.html#c:format_status/1),
accessed 2026-09-09.

## Research question

How can secret-bearing managers prevent incidental state/message disclosure in
ordinary OTP status and abnormal-termination reports?

## Findings

The optional `format_status/1` callback formats server status for status inspection
and abnormal-termination logging. It receives a map and returns a map with the
same keys, allowing values to be transformed. The documentation specifically
identifies removal of sensitive state as a use case. The ordinary default retains
callback state; an exception in a supplied formatter reports formatter failure
instead of falling back to exposing potentially sensitive state.

## Relevance

The [P131 investigation](../50-journal/2026-09-09-secret-capabilities.md) needs this
in addition to sensitive-process flags. Redaction should cover message and reason
fields as well as the stored state, because a credential can travel through all
three during failure.

## Limits

Formatting limits the documented status/logging surfaces. It does not constrain
arbitrary recipient logging, host-admin inspection, native memory corruption or
all VM memory copies. Runtime mutation tests remain necessary to check Catena's
actual integration.

## Derived work

- [Secret-capability journal](../50-journal/2026-09-09-secret-capabilities.md) —
  concrete manager/worker observation and cleanup investigation.
