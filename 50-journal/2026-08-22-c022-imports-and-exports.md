---
title: "C022 Imports and Exports"
kind: journal
created: "2026-08-22"
tags:
  - catena
  - conformance
  - imports
  - exports
  - specification
  - testing
aliases:
  - "C022 import evidence"
---

# C022 Imports and Exports

## Observations

Checklist item G022 is complete as C022 and normative source-only language
revision `0.1.18`. The completed boundary fixes private-by-default
explicit exports with C002 transparency modes, import admission through
two-segment qualification against digest-bound export sets plus explicit
possibly-empty unqualified name lists, the declared exclusions of
wildcards, hiding, renaming, aliases, and re-exports, and the deny-able
`IMP001` unused-import warning.

Two semantic decisions emerged during implementation testing. First,
abstract-event strictness: an import event carrying keys beyond
`event`/`module`/`digest`/`names` — an `as:` alias or `hiding:` list — is
rejected as `invalid_event`, so the declared exclusions are executable
rather than notional. Second, unused-admission counting: a *qualified*
reference `Json.Null` does not satisfy the unqualified admission of
`Null`, because admitting a name unqualified and never using it
unqualified is precisely the removable admission the warning exists to
report; the module itself still counts as used through its qualified
reference.

The sibling compiler implementation is commit
[`02da5c178ad5d797e55bdb3290cd950fbf7f4f31`](https://github.com/pcharbon70/catena/commit/02da5c178ad5d797e55bdb3290cd950fbf7f4f31),
merged into the `rewrite` integration line by compiler PR
[#98](https://github.com/pcharbon70/catena/pull/98) at merge commit
[`10487cb`](https://github.com/pcharbon70/catena/commit/10487cb09be1b0cd00f80d820aa87cf25ca75a3ab).
The merge retained the tested tree exactly (tree `90572b3`), and the
compiler PR was merged before this research promotion, following the
established publication order.

## Evidence

The compiler extends `Catena.Namespace` with export, provide-module, and
import-module events; `EXP001`/`IMP002`/`IMP003` validation; strict
event-key whitelisting; the
`Catena.Namespace.check_unused_imports/2` analysis and its
`Catena.Namespace.ImportWarning` record; `IMP001` in the warning
registry; and exact 0.1.18 registration pinning every predecessor default
(identifiers 0.1.10 through file units 0.1.16), with the namespace
resolver's required revision advancing to 0.1.18 with its grammar
extended — the first in-place extension, per the chapter's declared
event-grammar rule. A `guides/language/imports.md` guide ships with it.

Focused verification:

```text
mix test test/catena/c022_import_exports_test.exs \
  test/catena/c022_traceability_coverage_test.exs
Result: 10 passed
```

Complete compiler verification during implementation:

```text
mix format --check-formatted
mix clean
mix compile --warnings-as-errors
mix test
Result: 295 passed
mix escript.build
git diff --check
```

The focused corpus covers exact selection, lifecycle registration,
`IMP001`'s presence in the warning registry, and pinned predecessor
defaults; export events with transparency modes and their misuses;
`EXP001` undeclared exports and duplicate reuse of `NSP001`; admission
with unqualified, qualified, and empty qualified-only lists including
full-export-set qualification; private names never resolving through
qualification; `IMP002` wrong-category and unexported names, `IMP003`
unknown modules, and duplicate import rejection; strict exclusion of
wildcard, alias, hiding, and re-export event shapes; local-over-imported
precedence and order-flipped `NSP004` unchanged; the unused-import
warning matrix (unused name, wholly unused module, all-used silence,
qualified-not-counting semantics) in stable order; and deterministic
environments, resolutions, and warnings.

Archive verification after the complete connected bundle and indexes:

```text
python3 validate_archive.py
python3 -m unittest test_validate_archive.py
git diff --check
```

Results are recorded in the promotion commit; 328 completed documents
were checked across 29 directories with 3,402 local links, 86
specification chapters, 458 traceability obligations, and all 26
validator unit tests passing.

## Version and boundary decision

C022 consumes `0.1.18` because it changes static meaning and adds a
diagnostic family and warning. The source decoder now accepts cumulative
source revisions through 0.1.18. Every predecessor API retains its exact
selection; no new implementation limit is introduced.

The retained JSON AST remains closed at 0.1.7, the exact kernel remains
0.1.8, and interface, artifact, signed-format, and compiler-package
versions do not change. The next unused semantic patch is `0.1.19`.

## Threads

- G024 must decide module recursion over these admission rules; G025 must
  design package identity, re-export assembly, and duplicate-module
  rejection (the Hex publishing hypothesis note waits there); G026 must
  design the prelude as one more origin; G027 must select entry modules;
  P109 must fix the concrete `use`/`export` punctuation that emits these
  events; P117 owns `IMP001` prose quality.

## Follow-ups

Plan G024 or G025 against the fixed admission boundary; the
provided-module event is the seam where package assembly plugs in, and
digest verification obligations remain C006/C008 property throughout.
