---
title: "Catena Equality and Ordering"
kind: note
created: "2026-08-26"
maturity: developing
tags:
  - catena
  - language-design
  - equality
  - ordering
aliases:
  - "Catena comparison model"
---

# Catena Equality and Ordering

## Executive conclusion

Catena's comparison model at `0.1.30` is one closed comparable set,
bit-exact floats, and structural recursion. **Equality** admits Int,
Bool, and Float as primitives plus **structural recursion** over the
closed composite grammar — tuples, records (semantic maps), variant
injections, constructor values — provided every component is
comparable. **Ordering** admits Int and Float only; Bool is
equality-only. **Never comparable:** closures and process handles,
whose identity observability belongs to G037/G084.

**Float equality is bit-exact: `−0.0 ≠ 0.0`**, and float ordering is
total with `−0.0 < 0.0`. No NaN exists — C018's finite-binary64
contract guarantees it, with no NaN-producing operation in the closed
inventory — so the checklist's "floats including NaN" clause resolves
as an elevation of that guarantee rather than a semantics to define.
The target precedent is in the archive's own evidence: the
[OTP compatibility note](../30-sources/erlang-otp-compatibility-and-upgrading.md)
records OTP 27 itself moving `0.0 =:= -0.0` to `false`, and the
compiler already lowers `equal` to `=:=`.

Comparison is **monomorphic**: the equality operators unify both
operands to one type, so Int-vs-Float comparison is the existing type
error — C018's no-coercion stance elevated from literals to operators.
Strings and binaries do not exist; each G040 type enters with its
comparability in its own slice. The operators are **non-overloadable
built-ins**; an Eq/Ord trait layer is G101+/G061 library work on top
of them.

C003's clause conditions stay frozen: guards keep their Int/Bool safe
fragment, independently enforced by the condition checker — verified
in source before this slice began. The general-expression path gains
one new diagnostic, `EQN001`, for non-comparable operands.

## Scope and method

The operational target is independent agreement on the comparable set,
float semantics, monomorphism, the trait boundary, and the guard
split — made executable through the classifier extension, the widened
operator typing, and dual-target witnesses. Primary evidence is
internal: [C003's fragment](../60-specification/clause-conditions/syntax-and-safety.md),
[C018's finite floats](../60-specification/numeric-literal-semantics/README.md),
[C029's value grammar](../60-specification/values-and-evaluation/value-forms-and-first-classness.md),
the kernel's record-equality sentence, and C019's operator inventory;
plus the [OTP compatibility note](../30-sources/erlang-otp-compatibility-and-upgrading.md)
for the signed-zero precedent. Source claims stay distinct from
Catena proposals below.

## Relation to the current corpus

[C003](../60-specification/clause-conditions/syntax-and-safety.md)
fixed `a == b` and friends "with both operands either `Bool` or `Int`"
inside the closed condition fragment — and the general binary rule
inherited that restriction verbatim (`CND003` in the inference path).
C035 widens the general rule while the fragment stays: two checkers
govern a guard, and the condition checker accepts only Int/Bool, so
the widening provably cannot leak (verified at
`lib/catena/condition.ex`'s `core_type`).

[C018](../60-specification/numeric-literal-semantics/README.md)
fixed monomorphic `Int`/`Float` with no coercions and finite binary64;
C029 admitted Float as the tenth value, both signed zeros distinct
grammar members. This slice gives the tenth form its basic operations
and makes the signed-zero distinction observable through `≠`.

The [kernel](../60-specification/formal-semantic-kernel/sequential-dynamics.md)
already states records are semantic maps whose "written field order
controls effects but not value equality" — structural record equality
is kernel-normative; this slice elevates it and completes it for
tuples, variants, and constructor values over the closed grammar.

[C028's compatibility matrix](../60-specification/api-and-abi-compatibility/breaking-change-matrix.md)
treats an operator's admitted type set as interface-visible: widening
equality is a *minor* change under the matrix (additive), which is why
the comparable set enters as a new normative statement rather than an
amendment to C019's inventory.

## Comparative evidence and inference

### The signed-zero decision

Three forces converge on bit-exactness: C029's grammar already treats
the signed zeros as distinct values, so IEEE-equality would make them
equal-but-distinct — the first such pair, complicating structural
equality and hashing; no NaN exists, so IEEE's special cases buy
nothing; and the target runtime's own direction (OTP 27's `=:=`
change, recorded in our source note) plus the existing `=:=` lowering
mean the compiled behavior is already bit-exact. Convention would
require *adding* machinery to undo what the target gives for free.

### Why structural equality is an elevation

The kernel states record value equality as semantic; BEAM's `=:=`
gives structural tuple and map equality with bit-exact floats inside;
the composite grammar is closed (C029). Defining equality only over
primitives would leave tuple comparison undefined while every input
already makes the kernel's semantic-map promise. The recursion is over
the closed set — the entry rule extends it only through future slices.

## Selected model

> **Normative definitions (placed in the candidate chapters).**

### The comparable set

```text
comparable ::= integer | boolean | float
            | tuple { comparable } | record { comparable }
            | injection ( label , comparable ) | constructor-value
orderable ::= integer | float
```

Equality: both operands unify to one comparable type. Ordering: both
operands unify to one orderable type. Closures and process handles are
non-comparable — `EQN001`.

### Float semantics

Bit-exact equality (`−0.0 ≠ 0.0`); total order (`−0.0 < 0.0`); no NaN
exists (C018 finite-only, elevated).

### Guard split

C003's fragment stays: guards accept the safe operator set over
Int/Bool only, independently enforced. General expressions carry the
comparable set.

### Rejected alternatives

As enumerated in the resolved inquiry.

## What C035 adds to the design

C029's value grammar gains its first consumer-level operation; the
stdlib era's `Option`/`Result` and map/set keys get defined equality;
G061's numeric traits and G101's Eq/Ord layer gain their primitive
substrate; and the widened set is a C028 *minor* — the ecosystem
consequence recorded now, before any consumer exists.

## Remaining questions and falsification criteria

G037 owns identity observability; G040 owns each new type's
comparability entry; G061/G101 own Eq/Ord traits; P109 owns spellings
(fixed by C019's inventory); G036 owns comparison-related runtime
failure — none exists, equality being total over the closed set.

The model should be revisited if the 1.0 era demands IEEE float
equality (the remedy is an edition record — the switch is observable
and breaking), or if G040's map/set types demand hashing (a derived
from equality, entering with its own slice).

## Connections

- The [resolved equality inquiry](../40-inquiries/which-values-compare-and-how.md)
  records the question, hypotheses, and outcome.
- The [Equality and Ordering map](../10-maps/equality-and-ordering.md)
  routes through the shipped contracts and the future owners.
- The [Equality and Ordering Specification](../60-specification/equality-and-ordering/README.md)
  defines the candidate — then normative at promotion — `0.1.30`
  contract this note argues for.
- [Catena Values and Evaluation](catena-values-and-evaluation.md)
  fixes the grammar whose first operation this is.

## Sources

- [Syntax and Safety](../60-specification/clause-conditions/syntax-and-safety.md)
- [Numeric Literal Semantics Specification](../60-specification/numeric-literal-semantics/README.md)
- [Value Forms and First-Classness](../60-specification/values-and-evaluation/value-forms-and-first-classness.md)
- [Sequential Dynamics](../60-specification/formal-semantic-kernel/sequential-dynamics.md)
- [Erlang/OTP Support, Compatibility, Deprecations, and Removal](../30-sources/erlang-otp-compatibility-and-upgrading.md)
