---
title: "Erlang/OTP NIF Float Construction"
kind: source
created: "2026-09-09"
authors:
  - "Erlang/OTP project"
published: null
citation_key: "erlang-otp-nif-float-construction"
url: "https://www.erlang.org/doc/apps/erts/erl_nif.html"
accessed: "2026-09-09"
tags:
  - beam-vm
  - floats
aliases: []
---

# Erlang/OTP NIF Float Construction

## Reference

Erlang/OTP project. *erl_nif*, ERTS NIF API documentation,
[enif_make_double](https://www.erlang.org/doc/apps/erts/erl_nif.html#enif_make_double)
and [enif_make_badarg](https://www.erlang.org/doc/apps/erts/erl_nif.html#enif_make_badarg).
The live page identified OTP 29.0.6 when read; Catena's local executable witness
uses its separately pinned OTP 29.0.4 toolchain.

## Question and findings

Does the supported NIF constructor admit NaN or infinity? The API documentation
says that `enif_make_double` rejects non-finite arguments through the bad-argument
mechanism. The bad-argument documentation explains that the NIF returns an
exception even if it subsequently tries to return another term. This is an
API contract, not a guarantee about arbitrary C memory writes.

## Relevance and limits

This corrects the archive's earlier unverified conjecture about constructing a
non-finite term through the documented API. It supports choosing refusal rather
than normalization at C095. The independent local witness is evidence about the
pinned runtime; the live documentation's version does not silently expand
Catena's supported-host matrix.

## Derived work

- [Erlang type boundary workbench](../50-journal/2026-09-09-erlang-type-boundary.md) —
  records the isolated finite/non-finite native experiment.
- [Typed Conversion and Preservation](../60-specification/erlang-type-boundary/typed-conversion-and-preservation.md) —
  keeps finite Float semantics explicit at the language boundary.
