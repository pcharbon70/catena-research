---
title: "BEAM Float Host-Boundary Probes"
kind: journal
created: "2026-08-31"
tags:
  - catena
  - floats
  - evidence
  - beam
aliases:
  - "float host boundary evidence"
---

# BEAM Float Host-Boundary Probes

## Observations

A design breather explored how Catena should implement floating
point and whether following IEEE 754 is the best strategy,
following C061's closed-set decision ([synthesis](../20-notes/catena-numeric-relationships.md)).
The
conversation's claims were grounded in local probes of the actual
host (Erlang/OTP 29.0.4, stdlib 8.0.3, the compiler's pinned
toolchain) plus a current-facts check of the correctly-rounded
libm landscape. The strategic conclusion: keep IEEE 754 **as the
encoding** (binary64, `roundTiesToEven`, subnormals, signed zero —
already normative since C018/C035), reject IEEE's **NaN/Inf value
space** and **exception machinery** (flags, trapping modes,
selectable rounding — they contradict the three-way partition and
the determinism guarantee), and treat the transcendental library
as the one genuinely open fork.

The empirical surprise: **the BEAM itself is finite-only at every
language-level boundary**, so C018's contract is a formalization
of what the host already enforces rather than a deviation.
Verified on this machine:

```text
elixir -e ':math.sqrt(-1.0)'            → raises ArithmeticError (badarith)
elixir -e ':math.log(0.0)'              → raises badarith (pole)
elixir -e ':math.exp(1000.0)'           → raises badarith (overflow — no +Inf)
elixir -e '1.0 / 0.0'                   → raises badarith (no ±Inf)
elixir -e ':erlang.list_to_float(~c"nan")' → ArgumentError (no textual NaN)
erl: binary_to_term(<<131,70,127,248,0,0,0,0,0,0>>) → badarg
  (NEW_FLOAT_EXT refuses to decode a NaN payload)
:erlang.float_to_binary(-0.0, [:compact]) → sign preserved
```

The C036 reserved `arithmetic` trap kind therefore maps one-to-one
onto `badarith`. The correctly-rounded landscape check found
CORE-MATH (INRIA, MIT-licensed, machine-checked proofs for several
functions, binary64 functions merging into glibc through 2.43)
plus CRlibm/RLIBM and LLVM-libc adoption — bit-exact
transcendentals are now shelf-ware if G105 wants them.

## Open edges recorded for their owning gaps

1. **G105 — runtime overflow classification**: C018 fixes *literal*
   overflow (static `NUM001`); runtime overflow and domain errors
   currently surface as host `badarith`. The rule — `trap` with
   C036's reserved arithmetic kind, or typed failure as a value per
   producer — must be fixed when the first runtime-failing
   producer (division) lands.
2. **G105/G138 — transcendental determinism**: IEEE guarantees
   correct rounding only for `+ − × ÷ √`; the math library must
   either scope the determinism promise to basic ops or adopt
   correctly-rounded implementations (CORE-MATH-style).
3. **G105 — printing/parsing round-trips**: shortest-round-trip
   formatting so `parse(print(x)) == x` holds on every target.
4. **G098 (with G095) — foreign non-finite floats**: the external
   term format provably refuses NaN/Inf payloads, but a NIF
   calling `enif_make_double` with a non-finite double can in
   principle construct one in-process; the foreign boundary must
   refuse or normalize, with a witness test.

These edges are also recorded in the owning checklist entries
(G105, G095, G098) so their slices cannot close without them.
