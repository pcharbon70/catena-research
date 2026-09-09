---
title: "Language Completion"
kind: map
created: "2026-09-06"
tags:
  - catena
  - language-design
  - specification
  - conformance
aliases: []
---

# Language Completion

## Scope

This map connects the language's completion ledger to the detailed decisions,
implementation order, and observed evidence. It separates a complete bounded
contract from whole-language usability, integration and release readiness.
Public vocabulary and the final grammar remain held for later joint design.

## Start here

1. The [checklist](../00-inbox/language-specification-completeness-checklist.md)
   is the current status ledger; the
   [audit](../50-journal/2026-09-06-checklist-completion-audit.md) explains its
   baseline corrections and source identities.
2. The [completion plan](../20-notes/language-completion-plan.md) defines the
   objective, category-theory constraints, dependencies, milestones and gates.
3. The [decision register](../20-notes/design-decision-register.md#language-completion-plan-2026-09-06)
   preserves four alternatives per decision and identifies the agent's
   recommended selections under the user's delegation.

## Trails

- [Foundations, items 001–046](../20-notes/language-completion-plan-foundations.md)
  retains established semantics and adds concrete integration and regression
  decisions without treating completed work as missing.
- [Semantics and runtime, items 047–092](../20-notes/language-completion-plan-semantics.md)
  begins with comprehension evidence and receive consistency, then defines
  resource, cancellation, process and distributed-runtime admission gates.
- [Interoperability and delivery, items 093–141](../20-notes/language-completion-plan-delivery.md)
  connects checked foreign values and useful libraries to tools, security,
  reproducibility, integrated validation and self-hosting.
- [Category theory](category-theory-for-programming.md),
  [combinators](combinators-for-algebraic-data-and-categorical-programming.md)
  and [effects](algebraic-effects-and-handlers.md) give the design grounds:
  lawful composition needs explicit operational behavior and evidence.
- The [execution journal](../50-journal/2026-09-06-language-completion-plan.md)
  records what has actually been implemented and tested; the
  [conformance registry](conformance-traceability.md) remains the rule-to-test
  inventory rather than a substitute for behavioral witnesses.

- [Erlang type boundary](../60-specification/erlang-type-boundary/README.md) completes C095 with explicit typed conversion, bounded whole-carrier checks and verified nominal list roles.
- [Calling conventions workbench](../50-journal/2026-09-09-calling-conventions.md) records C094 completion at 0.1.59: verified call/artifact identity, staged closures, typed synchronous callbacks and retained lifecycle adapters.
- [Value boundaries](../60-specification/value-boundaries/README.md) completes C093 with typed scalar/structural/nominal conversion, verified closure capture and explicit authority exclusions.

## Open questions

The [completion inquiry](../40-inquiries/how-can-catena-complete-its-language-definition.md)
owns cross-item dependencies, proof disposition and the held public adoption
gate. Focused inquiries continue to own their individual research questions;
this plan does not resolve them merely by choosing a direction.

- [Foreign adapter milestone](../60-specification/foreign-adapters/README.md) — P096 executed authority/lifetime work; its public-surface and broader callback gates remain open.

- [Native value roles](../60-specification/native-value-roles/README.md) — C097 complete native-kind admission inventory, registered identity and explicit native-service exclusions.

- [Collection protocols](../60-specification/collection-protocols/README.md) — C102 executes the library contracts with semantic key order, explicit outcomes and owned pull cleanup.

- [Text and binary operations](../60-specification/text-binary-model/README.md) — C104 supplies explicit index units, pinned Unicode, typed conversion and compiled adoption while vocabulary remains held.

- [C105 numeric library](../60-specification/numeric-library/README.md) — checked arithmetic, explicit conversion/decimal rounding and verified executable adoption.

- [C106 environmental effects](../60-specification/environmental-effects/README.md) — explicit service authority closes launch effects and owns adapter cleanup.

- [C101 minimum prelude](../60-specification/minimum-prelude/README.md) — explicit catalog selection assembles the pure minimum and separately granted services.

- [C126 trusted computing base](../60-specification/trusted-computing-base/README.md) — named enforcement and residual dependencies with mutation-tested boundaries.

- [C131 secret capabilities](../60-specification/secret-capabilities/README.md) — sealed transformations, scoped delivery and explicit host trust.
- [C127 trusted obligation policy](../60-specification/trusted-obligation-policy/README.md) — artifact-derived transitive trust with owner-qualified admission and revocation.
