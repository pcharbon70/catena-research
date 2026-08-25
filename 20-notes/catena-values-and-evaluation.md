---
title: "Catena Values and Evaluation"
kind: note
created: "2026-08-24"
maturity: developing
tags:
  - catena
  - language-design
  - values
  - evaluation
  - strictness
aliases:
  - "Catena value model"
---

# Catena Values and Evaluation

## Executive conclusion

Catena's value model at `0.1.25` is the C010 kernel's calculus,
elevated to a language invariant and completed for the one form the
kernel grammar predates: Float. **Values** are a closed ten-form list —
integers, Booleans, Unit, Floats, tuples of values, closures, nominal
constructor values, records of values, variant injections carrying a
value, and opaque process handles. **Non-values** are a closed list
too: evidence, handler declarations, capability names, resumptions
(affine, C005), traps, effect rows, and signatures — forms that exist
in programs but are never fully-evaluated first-class data. Every
value is **uniformly first-class**: bindable, passable, returnable,
and storable, with no tiers and no per-type restrictions; what storing
a process handle lets you observe belongs to G037/G085, not to the
value grammar.

**Strictness** is a language invariant: every subexpression evaluates
at most once, to a value or a terminal trap, before it is used. The
kernel's `and`/`or` right-operand skips are the named exceptions.
Any future lazy or short-circuit form requires a C008 edition record
naming it — the same gate the prelude guarantee uses.

A completed evaluation has exactly two terminal outcomes — a value or
a trap. A suspended algebraic request is neither: it is a pending
continuation the handler calculus owns, and under C010's completion
rule no process entry returns with one live.

The executable deliverable is `Catena.Values`: a total classifier over
typed-core and kernel terms implementing the closed grammar, plus
property evidence over the shipped stepper — every terminal is a value
or a trap. The slice is definitional: **zero new diagnostic families**,
because no new invalid inputs exist.

## Scope and method

The operational target is independent agreement on the value grammar,
the non-value list, first-classness, the strictness invariant, and the
terminal-outcome contract — made executable through the classifier.
Primary evidence is internal: the [C010 kernel's value and order
rules](../60-specification/formal-semantic-kernel/sequential-dynamics.md),
[C005's handler and resumption semantics](../60-specification/effects-and-handlers/deep-handlers-and-affine-resumptions.md),
and [C018's Float](../60-specification/numeric-literal-semantics/README.md).
No external precedent does work here the kernel has not already done;
the corpus elevates its own calculus. Source claims stay distinct from
Catena proposals below.

## Relation to the current corpus

The [kernel's value paragraph](../60-specification/formal-semantic-kernel/sequential-dynamics.md)
fixes nine forms and five non-values inside the exact 0.1.8
S-expression boundary. That grammar is the calculus this slice
elevates; the kernel chapters are frozen and untouched, because
revising them would amend a retained revision — the discipline every
slice since C013 has kept.

[C018's Float](../60-specification/numeric-literal-semantics/README.md)
is the one language form the kernel grammar predates. A closed list
that omitted it would be knowingly incomplete; this slice adds it as
the tenth value form, with finite-binary64 semantics unchanged.

[C005's affine resumptions](../60-specification/effects-and-handlers/deep-handlers-and-affine-resumptions.md)
force the resumption non-value entry: a one-shot continuation is
runnable state, not data — classifying it as a value would make an
affine resource copyable.

[C010's trap taxonomy](../60-specification/formal-semantic-kernel/actors-messages-and-failures.md)
already fixes traps as explicit terminal failures, which licenses the
value-or-trap terminal contract; the stepper's `{:value, …} |
{:trap, …}` outcomes are its executable form.

[C028's compatibility matrix](../60-specification/api-and-abi-compatibility/breaking-change-matrix.md)
consumes the closed grammar indirectly: interface schemes describe
value types, and decidable value membership is what keeps scheme
comparison meaningful. P035's equality will consume the classifier
directly.

## Comparative evidence and inference

### Why closed beats open

An open grammar — "every inhabited type's canonical inhabitant is a
value" — would cover future types automatically, but it prices
decidability: P035 equality needs to know exactly which forms compare;
C028 needs stable scheme semantics; G037 needs a precise observable
surface. A closed list with an explicit G040 rule (each new type
enters the language *with* its value status, in its own slice) keeps
membership decidable while never silently widening.

### Why uniform first-classness

Tiered first-classness — passable-but-not-storable handles, or
functions restricted from records — encodes observability policy in
the value grammar, which is the wrong layer: what storing a process
handle lets a program observe is a semantics question G037 (allocation
observability) and G085 (message semantics) own. The kernel treats
handles as opaque values; this slice states that uniformly and defers
the consequences to their owners by name.

### Why strictness needs a gate

The kernel is strict; the language says so once, at the invariant
level, with the two named exceptions. Without an explicit gate, a
future `lazy` or short-circuit form would be a compatible addition by
C008's default classification — silently weakening every
reasoning tool that assumes evaluate-before-use. The prelude
guarantee's mechanism (any exception requires an edition record) is
reused verbatim.

## Selected model

> **Normative definitions (placed in the candidate chapters).**

### The value grammar

```text
value ::= integer | boolean | unit | float
        | tuple(value, ...)          -- recursively values
        | closure                    -- code with environment
        | constructor-value          -- nominal, fully applied
        | record(value, ...)         -- label-to-value map
        | injection(label, value)    -- variant payload is a value
        | process-handle             -- opaque identity
```

Non-values, closed: evidence, handler declarations, capability names,
resumptions, traps, effect rows, signatures.

### First-classness

One class. Every value may be bound, passed, returned, and stored.
Exclusions named, not tiered: observability of handle storage (G037,
G085), equality between values (P035), rendering (G110/G118).

### The strictness invariant

Every subexpression evaluates at most once, to a value or a terminal
trap, before use. Exceptions: `and` skips its right operand when the
left value is false; `or` skips when the left value is true. Any future
exception requires a C008 edition record naming the form and its
migration.

### Terminal outcomes

A completed evaluation is a value or a trap. Suspended requests are
pending continuations, not terminal; no process entry returns with one
live (C010 completion rule, unchanged).

### Rejected alternatives

- **Extend kernel chapters in place** — amends retained 0.1.8.
- **Open canonical-forms grammar** — prices decidability.
- **Kernel list verbatim** — knowingly incomplete post-C018.
- **Tiered first-classness** — observability policy at the wrong layer.
- **Merge with P030** — couples the grammar to binding details.
- **Normative-only** — rejected pattern.

## What C029 adds to the design

Section 4 opens on a fixed foundation: every later item — G031
bindings, G032 calls, G033 branching, P035 equality, G036 failure —
consumes the closed grammar and the invariant rather than restating
them. G040 gains its entry rule; P035 gains its classifier; G110/G118
gain the distinction between what renders and what is.

## Remaining questions and falsification criteria

G031–G033 own binding, call, and branch semantics; P030 owns per-form
order; P035 owns equality and ordering; G036 owns the failure taxonomy
beyond traps; G037 owns allocation observability; G038 owns
compile-time evaluation; G040 owns each future type's value status;
P109 owns all surface syntax.

The model should be revisited if G084's runtime work demands
non-uniform handle treatment (the remedy is a G037/G085 observability
contract, not value tiers), or if the 1.0 era considers lazy forms
(the remedy is the edition record the gate already requires).

## Connections

- The [resolved values inquiry](../40-inquiries/what-are-catenas-values-and-strictness.md)
  records the question, hypotheses, and outcome.
- The [Values and Evaluation map](../10-maps/values-and-evaluation.md)
  routes through the kernel calculus, the shipped contracts, and the
  future owners.
- The [Values and Evaluation Specification](../60-specification/values-and-evaluation/README.md)
  defines the candidate — then normative at promotion — `0.1.25`
  contract this note argues for.
- [Catena Numeric Literal Semantics](catena-numeric-literal-semantics.md)
  fixes the Float this slice admits as a value.
- [Catena API and ABI Compatibility](catena-api-and-abi-compatibility.md)
  consumes decidable value membership through its scheme semantics.

## Sources

- [Sequential Dynamics](../60-specification/formal-semantic-kernel/sequential-dynamics.md)
- [Canonical Kernel Syntax](../60-specification/formal-semantic-kernel/canonical-kernel-syntax.md)
- [Actors, Messages, and Failures](../60-specification/formal-semantic-kernel/actors-messages-and-failures.md)
- [Deep Handlers and Affine Resumptions](../60-specification/effects-and-handlers/deep-handlers-and-affine-resumptions.md)
- [Numeric Literal Semantics Specification](../60-specification/numeric-literal-semantics/README.md)
