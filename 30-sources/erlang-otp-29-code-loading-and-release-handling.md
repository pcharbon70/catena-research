---
title: "Erlang/OTP 29 Code Loading and Release Handling"
kind: source
created: "2026-09-10"
published: null
citation_key: null
container: "Erlang/OTP System Documentation"
edition: "29.0"
isbn: null
doi: null
url: "https://www.erlang.org/doc/system/code_loading.html"
accessed: "2026-09-10"
tags: [erlang, runtime, compatibility, concurrency]
aliases: []
---

# Erlang/OTP 29 Code Loading and Release Handling

## Reference

Erlang/OTP, “Compilation and Code Loading,” “Release Handling,” and `sys`,
online OTP 29 documentation, accessed 2026-09-10. Official pages:
[code loading](https://www.erlang.org/doc/system/code_loading.html),
[release handling](https://www.erlang.org/doc/system/release_handling.html), and
[`sys`](https://www.erlang.org/doc/apps/stdlib/sys.html).

## Research question

Which target-runtime mechanisms and limits can witness Catena's checked hot
upgrade contract without becoming language semantics?

## Method

The official pages were read for module coexistence, process transition,
failure, release ordering, and distributed coordination. The compiler then
exercised the documented system-message path on a managed `GenServer`.

## Findings

- The code server retains current and old code. Loading a third version purges
  old code and can terminate processes still executing it.
- Fully qualified calls enter current code; live old frames and closures do not
  automatically change meaning.
- OTP release handling suspends managed processes, invokes code change, and
  resumes them. Unaffected processes can continue, creating coordination races.
- `.appup` and `relup` encode deployment instructions, including cases that
  restart an application or emulator instead of performing a soft upgrade.
- Release handling is local to each node; distributed upgrades coordinate
  separate handlers and can contain mixed versions during a staged rollout.

## Relevance

The two-version ceiling supports C092's one-active/one-draining envelope. The
system-message protocol supplies a narrow adapter, while exact Catena artifact,
interface, state, capability, and evidence checks remain above it.

## Limits

These documents specify OTP mechanisms, not Catena semantics. `code_change`
can perform arbitrary host effects, release scripts can restart systems, and
the runtime cannot verify Catena purity, schemas, authority, or rollback.

## Derived work

- [Checked Migration and Activation](../60-specification/hot-code-upgrade/checked-migration-and-activation.md)
- [Hot Code Upgrade journal](../50-journal/2026-09-10-hot-code-upgrade.md)
