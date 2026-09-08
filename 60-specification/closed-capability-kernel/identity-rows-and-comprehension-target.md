---
title: "Closed Capability Rows and the Comprehension Target"
kind: specification
created: "2026-09-08"
status: normative
spec_version: "0.1.50"
tags: [effects, comprehensions, specification, conformance]
aliases: []
---

# Closed Capability Rows and the Comprehension Target

## Status and authority

This chapter is governed by [Specification Authority](../../SPECIFICATION-AUTHORITY.md),
[Conformance Vocabulary](../../CONFORMANCE-VOCABULARY.md), and
[Implementation Limits](../../IMPLEMENTATION-LIMITS.md). It introduces the
stable closed-capability-kernel boundary at exact revision `0.1.50` in edition
`0.1`, under [C008 compatibility](../editions-and-feature-lifecycle/feature-lifecycle-and-compatibility.md#compatibility-dimensions).

For this selection, this chapter explicitly replaces the fixed `0.1.8` target
in [C047's qualifier-tree target](../list-comprehensions/elaboration-and-lowering.md#the-qualifier-tree-target)
with the identity-bearing core defined here. It adopts C047's list-only,
eager, left-to-right depth-first traversal, filtering, binding, yield, failure,
sequential-execution and dormant-adoption rules unchanged. Later same-edition
selections inherit this target unless explicitly amended. Exact `0.1.39` and
`0.1.8` selections and historical artifacts are not reinterpreted.

The model implements the closed, statically selected part of
[C005's hybrid rows](../effects-and-handlers/capabilities-rows-and-selection.md#hybrid-row-equality).
It does not replace C005's general open-row inference or claim new support for
row-polymorphic operations. C010's other type, data, pattern, function,
process, failure and evaluation rules remain the inherited semantic substrate.

## Input and selection

The new input is a compound compiler-internal tree, not bare historical
source. It contains the typed qualifier tree, a complete slot-to-family map,
per-fragment rows, and an ordered list of enclosing handlers. The underlying
module syntax and expression fragments use the retained kernel decoder as
quoted structural input. Its retained header identifies that decoder, not
the language selection of the compound input. A bare call to the old kernel
frontend still selects exactly `0.1.8` and retains ordinary effect multiplicity.

The new boundary selects exactly `0.1.50`, edition `0.1`, with no previews.
A different explicit selection rejects as `EDN001`. The new core carries
`0.1.50` as its version, frontend version and language revision. No public
keywords, source grammar, standard-library vocabulary or new S-expression
frontend are admitted (`CK-OBL-001`).

Every decoded effect declaration supplies one named slot in the compound
input. The slot-to-family map contains exactly those names, with nonempty
UTF-8 family identities. A family identity denotes the same nominal family
throughout the input; its operation names, parameter types and result types
agree across its slots. The initial carrier admits closed operation types
without free type or row variables. The decoder's declaration order fixes
the numeric binder position; a slot identity is the canonical encoding of
module origin, module owner and that position. Display-name changes do not
change the structural identity (`CK-OBL-002`).

## Identity rows and lexical scope

Rows contain reserved `Process` or explicit capability-slot identities.
They are closed: unsupported tails are rejected, never erased or chosen by
spelling. Repeated use of the same slot coalesces; distinct slots remain
distinct even when their families agree. The ordinary occurrence bags of
exact `0.1.8` are not valid rows in this new core (`CK-OBL-003`).

Each slot in a definition's signature or evaluated `uses` row is an abstract
parameter visible while checking that definition. A request selects its named
compatible slot statically. Function and value references preserve the slots
in their checked types and rows. Scope never supplies ambient authority for
an unmentioned slot, and runtime nesting never repairs invalid selection.

A handle binds its selected slot freshly within its handled expression; it
rejects rebinding a slot already visible at that point. It subtracts exactly
that slot from the checked expression row. A handled slot cannot remain in
any escaping result type, including a latent function row nested in data.
This closed-slot target uses C010's effect-free handler clauses and affine
resumptions; it does not expand their operation signature fragment
(`CK-OBL-004`).

Slot instantiation is simultaneous and descriptor-checked. Each source slot
exists in the substituted row. Target family and resolved type arguments agree
with the source; target identifiers are not recursively followed as new
substitution sources. Two formals selecting one actual coalesce only after
substitution; two distinct actuals remain distinct. General type-argument
unification precedes this bounded operation and is not inferred from it.

## Fragment checking and generated workers

Each qualifier carries its expression, expected type and evaluated `uses` row;
the yield carries `yield_uses`. An absent row denotes the empty row. A context
entry carries name, type, expression and an optional evaluated row. This
boundary checks context entries in order, admitting earlier entries only;
recursive or forward context dependencies reject here. This restriction does
not change the retained elaborator's input contract (`CK-OBL-005`).

Before changing generated worker arrows, the checker verifies each fragment
in a standalone nonrecursive probe with its exact lexical binders and earlier
context definitions. A generator source has the declared list type, a filter
has `Bool`, a binding has its declared value type, and a yield has the result
element type. Inferred evaluated rows equal the supplied rows. Their union
equals the aggregate comprehension row. Missing, forged or overstated rows
reject; recursive worker signatures cannot justify them retroactively.
Diagnostics identify the context, qualifier index or yield (`CK-OBL-005`).

The existing fused worker tree remains: one recursive worker per generator
depth, a shared accumulator, inline qualifiers, and a final ordering pass.
A worker's own source was evaluated by its caller. Its row therefore contains
the union of subsequent qualifier and yield rows, charged on the final arrow
that executes the worker body. Earlier curry stages and definition lookup are
pure closure construction; reversal is pure (`CK-OBL-006`).

Enclosing handlers wrap the entire entry expression in the supplied order,
first outermost. They are not copied into individual fragments. A handler
that declines resumption abandons the remaining traversal within its scope;
its return value is the handled computation's result. Traps at source,
filter, binding or yield stop at the same point on both targets. A false
filter's already performed effects remain observable (`CK-OBL-006`).

## Verification and BEAM artifacts

The verifier rederives expression types and evaluated rows independently of
inference and checks recorded annotations against those derivations. It also
checks structural slot derivation, family descriptors, lexical visibility,
subtraction and escape. Downgrading identity-bearing core to `0.1.8`, changing
its revision fields, or forging request/handler evidence rejects. Checked
capability rows select the ordinary-effect CPS calling convention, including
transitive calls and final curried stages. Runtime handler dispatch uses the
selected slot, not a family-name search (`CK-OBL-007`).

The production compiler verifies before lowering and applies the standing
source arity, generated arity and generated module limits. It emits a distinct
`0.1.50` BEAM artifact through the deterministic OTP compiler boundary. Its
compile metadata records edition `0.1`, language revision `0.1.50`, and the
closed capability-tree frontend. Compilation requires a zero-argument main
entry with no evaluated or escaping latent capabilities. Intrinsic Process
remains available and does not introduce ordinary capability authority. An unhandled
abstract computation can be checked for later enclosure, but cannot be emitted
as a complete main artifact (`CK-OBL-008`).

This revision introduces no interface or signed format. The compiler returns
no importable interface for this artifact. Implementations MUST NOT encode
capability rows into retained `0.1.8` interfaces or claim new package-linking,
public ABI, foreign callback or signed-format support from this chapter.
The old JSON and S-expression frontend lists and interface/signed-format
lists remain unchanged. The source-text decoder additionally admits
`0.1.50`, and the new capability-tree and BEAM-artifact lists identify it
separately (`CK-OBL-001`, `CK-OBL-008`).

## Lifecycle and migration

`change-0-1-50-closed-capability-kernel` has predecessor `0.1.49`, target
`0.1.50`, classification `compatible-addition`, and affected dimensions
`source-acceptance`, `static-meaning`, and `artifacts`. It introduces the
compound boundary and explicitly changes the dormant comprehension target
for its selection. There is no automatic rewrite of old source or artifacts.
Migration supplies explicit slot/family bindings, exact fragment rows and
whole-computation handlers; public source adoption remains P109.

## Diagnostics and conformance

Malformed compound metadata, inconsistent family descriptors and fragment
row mismatches use existing typing diagnostics such as `T002`. Invalid or
escaping capability scope and an incompletely handled artifact entry use
`EFX003`. Explicit selection mismatches use `EDN001`; forged core rejected at
the production boundary uses `I001`. Existing parser, pattern, effect and
backend diagnostics retain their meanings. No diagnostic family is added.

| ID | Obligation | Required evidence |
| --- | --- | --- |
| `CK-OBL-001` | exact selection, explicit target replacement and retained-format separation | registry, explicit predecessor rejection and metadata checks |
| `CK-OBL-002` | structural slot identity and compatible nominal family descriptors | deterministic identity, distinct same-family selection and descriptor rejection |
| `CK-OBL-003` | closed identity rows preserve multiplicity of distinct slots | semilattice laws, exact subtraction, simultaneous instantiation and malformed-row rejection |
| `CK-OBL-004` | lexical authority, fresh handling and no capability escape | ambient/escaping rejection and enclosing-handler execution |
| `CK-OBL-005` | independently checked fragment and context rows | understated/overstated rows, aggregate mismatch and nonrecursive context checks |
| `CK-OBL-006` | final-stage worker effects and whole-traversal handler scope | exact nested trace, empty input, false filter and first/last failures at every position |
| `CK-OBL-007` | independent verification and capability-aware CPS | forged-core rejection, recursive requests and reference/BEAM agreement |
| `CK-OBL-008` | verified fully handled entry and distinct deterministic artifact | production compile metadata, unhandled-entry rejection and predecessor boundaries |

## Variability and limits

All conforming implementations obey the same rules above. There are no new
variability or resource-limit dimensions; standing limits and failure
classifications apply. It adds no optimization permission to
reorder, parallelize, duplicate or drop a qualifier's effects.

## Rationale and evidence (non-normative)

The [completion plan](../../20-notes/language-completion-plan-semantics.md)
and [implementation journal](../../50-journal/2026-09-08-capability-kernel-integration.md)
record the alternatives, scoped choices, failing experiments and repaired
cross-target witnesses. The [comprehension inquiry](../../40-inquiries/how-should-catena-specify-list-comprehensions.md)
connects the evidence to the completion gates. This bounded executable target
does not claim a whole-language composition theorem or a general open-row solver.
