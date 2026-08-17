---
title: "Erlang/OTP 29 System Limits"
kind: source
created: "2026-08-17"
authors:
  - "Ericsson AB"
published: "OTP 29"
citation_key: "erlangOtp2026systemLimits"
container: "Erlang/OTP System Documentation"
edition: "29.0.4"
isbn: null
doi: null
url: "https://www.erlang.org/doc/system/system_limits.html"
accessed: "2026-08-17"
tags:
  - beam-vm
  - compiler
  - erlang
aliases:
  - "OTP 29 system boundaries"
---

# Erlang/OTP 29 System Limits

## Reference

Ericsson AB. “System Limits.” *Erlang/OTP System Documentation*, OTP 29.0.4.
[Canonical documentation](https://www.erlang.org/doc/system/system_limits.html),
accessed 2026-08-17.

## Research question

Which target-runtime boundaries constrain portable Catena source and generated
code, and which apparent limits should remain implementation or deployment
concerns rather than language semantics?

## Findings

Erlang's language specification does not assign finite maxima to every
resource, but the practical runtime does. OTP 29 documents a maximum of 255
arguments for a function and 255 minus captured environment variables for a
fun. It also documents configurable process counts and many identity, node,
tuple, binary, and address-space boundaries whose effective availability can
depend on runtime configuration or the operating system.

For Catena, the function boundary is the immediate generated-code constraint.
The bootstrap effect-directed CPS worker adds two hidden arguments—handler
state and continuation—so a portable explicit-source floor of 253 reaches the
OTP maximum in the least favorable current lowering. The wider list warns
against treating every OTP maximum as a Catena language maximum: most are
representation or deployment facts until a Catena form exposes the dimension.

## Relevance

The [implementation-limits synthesis](../20-notes/catena-implementation-limits-and-portability.md)
uses this evidence to derive the callable floor and to separate target ceilings
from corpus-wide portable minima. The root
[Implementation Limits and Portability policy](../IMPLEMENTATION-LIMITS.md)
requires the compiler to measure both explicit source arity and generated OTP
arity before successful publication.

## Limits

The document specifies OTP 29 limits, not Catena source validity, portable
floor selection, compiler diagnostics, or future OTP behavior. A documented
OTP ceiling does not prove that programs near the ceiling are practical, and
an operating-system or memory limit can be lower than an address-space-derived
maximum. Catena therefore pins the target release and tests its own smaller
portable contract.

## Derived work

- [Catena Implementation Limits and Portability](../20-notes/catena-implementation-limits-and-portability.md)
- [How Should Catena Bound Implementation Limits?](../40-inquiries/how-should-catena-bound-implementation-limits.md)
- [C012 Implementation Limits](../50-journal/2026-08-17-c012-implementation-limits.md)
