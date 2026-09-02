---
title: "Catena Progress and Preservation"
kind: note
created: "2026-09-01"
maturity: developing
tags:
  - catena
  - metatheory
  - language-design
aliases:
  - "the composed safety theorem"
---

# Catena Progress and Preservation

## Executive conclusion

Catena's metatheory program completes the way it advanced: by
stating targets with executable evidence and routing proofs
honestly. The effects-and-failure targets close the last
component class — preservation and progress for the shipped
handler calculus and `trap` as the failure terminal. The
integrated theorem arrives as a **composed statement**: the
standing component theorems (C002 data, C003 conditions, C010
kernel, this slice's effects) plus an explicit composition lemma
whose proof obligation belongs to the formal-validation era.
Public processes and foreign values get **conditional
extensions** — true exactly when their owning slices' arrival
rules are discharged — so the theorem never claims what machinery
does not exist to support.

## Scope, method, and definitions

This note synthesizes the archive's evidence for closing P132 at
revision `0.1.45`. It reads C002's and C003's metatheory
chapters, C010's kernel metatheory, C005's resumption discipline,
C030's trace-agreement methodology, and C036's failure terminal;
it proves nothing and claims nothing unprovable.

## The component inventory

| Component | Theorem class | Standing evidence |
| --- | --- | --- |
| Data (C002) | nominal generativity, declaration atomicity, conservativity, pattern substitution, preservation, exhaustive progress | C002 metatheory chapter and corpus |
| Conditions (C003) | closed safety, predicate expansion, fallthrough, commitment, guarded progress, fact soundness, lowering equivalence, receive preservation, erasure | C003 metatheory chapter and corpus |
| Kernel (C010) | sequential preservation and progress, mailbox preservation, quiescence | kernel stepper agreement |
| Effects and failure (this slice) | handler installation, affine resume-once, return-clause, trap-as-terminal | C005 corpus, C036 fixture, C030 agreement |

## What a composed statement buys

The integrated theorem is only as strong as its composition lemma,
and the lemma is a *named proof obligation* — owned by the
type-system inquiry and Section 16's gates — not a claim. Until it
is discharged, the honest summary is: every component theorem is
stated with evidence, and no known composition counterexample
exists. That is strictly more than "each part works" and strictly
less than "the whole is proven" — the middle the corpus can
actually occupy.

## The conditionals

Public processes: C010's mailbox results stand; the extension to
G084/G085's spawn-and-lifetime machinery holds iff that slice
ships with its own preservation statement. Foreign values: C067's
rule — entry only through a visible, typed, failure-classified
boundary — means entering values are already-typed, so
preservation holds by construction of the boundary; the condition
is precisely that no other entry path exists, which C067's
exclusion enforces.

## Tradeoffs, limitations, falsification

The slice costs nothing executable and buys an honest whole: the
risk is rhetorical overreach. Falsification: any component
counterexample, any untyped entry path, or any claim that the
composition lemma is proven.

## Route to sources

- The Progress and Preservation Specification (candidate, then
  normative at promotion, in
  `60-specification/progress-and-preservation/`) will define the
  contract this note argues for.
- [Metatheory](../60-specification/data-and-patterns/metatheory.md)
  and C003's metatheory chapter — the component statements.
- [Kernel Metatheory](../60-specification/formal-semantic-kernel/metatheory.md)
  — sequential and mailbox preservation.
- [The Six Categories](../60-specification/runtime-failure-taxonomy/the-six-categories.md)
  — the failure terminal the targets name.
- The [resolved inquiry](../40-inquiries/what-progress-and-preservation-targets-remain.md)
  preserves the decision route.
