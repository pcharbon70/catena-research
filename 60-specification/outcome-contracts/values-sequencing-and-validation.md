---
title: "Outcome Values, Sequencing and Validation"
kind: specification
created: "2026-09-08"
status: normative
spec_version: "0.1.54"
tags:
  - specification
  - algebraic-data-types
aliases: []
---

# Outcome Values, Sequencing and Validation

## Status and authority

This chapter defines C103 at `0.1.54` under the
[authority policy](../../SPECIFICATION-AUTHORITY.md),
[conformance vocabulary](../../CONFORMANCE-VOCABULARY.md) and
[implementation-limit policy](../../IMPLEMENTATION-LIMITS.md).
It supplies outcome library meanings through ordinary algebraic datatypes and
C004 categorical specialization. It introduces no new executable frontend,
source spelling, implicit import, hierarchy method, or persisted format.
The temporary role labels used by the executable package are not adopted
public vocabulary. The existing [prelude policy](../prelude-policy/README.md)
continues to require explicit selection (`OV-OBL-001`).

The [exception boundary](../exception-boundary/README.md) continues to separate
expected failure values, handler escape and terminal traps. This chapter
supplies the previously reserved outcome contents, without changing that
boundary or the owned-process completion contract.

## Type shapes and separation

An optional value has exactly two constructors: absence, with no payload; or
presence, carrying one value of its parameter type. A dependent outcome has
failure carrying one error and success carrying one value. An independent
validation outcome has invalidity carrying a nonempty ordered error sequence
and validity carrying one value. All three are distinct nominal ordinary
library types, with ordinary construction, pattern matching and parameter
substitution. There is no subtyping or automatic coercion among them
(`OV-OBL-002`).

The error sequence consists of one required head and a finite ordinary
sequence as its tail. Converting a possibly empty sequence to this nonempty
shape returns absence for empty input and presence otherwise. Constructing
invalidity from an empty sequence is a static type error, rather than a
successful validation or a fabricated error. A dependent error can itself
contain any well-typed value, including an empty sequence; its failure tag
still denotes failure. Nested presence of absence and success of failure
retain both constructors (`OV-OBL-002`, `OV-OBL-006`).

No new implicit comparison operation is introduced. Payload comparison, when
requested through an admitted comparison operation, retains its existing type
and evidence requirements. The ordering promised here is evaluation and error
sequence order, not a universal ordering of arbitrary errors or functions.

## Mapping and dependent sequencing

Mapping a presence or successful/valid outcome invokes the supplied pure
callback exactly once and wraps its result in the same success-side family.
Mapping absence, failure or invalidity invokes it zero times and preserves the
failure-side payload. Embedding wraps a value on the success side. Mapping
obeys identity and composition over pure total finite observations
(`OV-OBL-003`).

Dependent sequencing is provided for optional and dependent outcomes only.
It invokes its callback once on success/presence; that callback returns the
same outcome family. Failure/absence skips the callback entirely. Sequencing
obeys associativity and embedding's left and right identity laws on the same
pure total domain. It does not flatten nested outcomes except through this
explicit operation (`OV-OBL-003`).

Binary mapping receives the callback, first subject, then second subject,
using the standing left-to-right argument evaluation rule. Both subject
expressions are evaluated before the operation. Optional binary mapping is
absent if either subject is absent. Dependent binary mapping retains the
first failure, otherwise the second failure, otherwise invokes the curried
combination callback once with the first then second payload. This eager
operation does not skip evaluation of the second subject expression; callers
use dependent sequencing to skip dependent work (`OV-OBL-004`).

## Independent accumulation

Independent binary mapping retains the first error sequence followed by the
second when both inputs are invalid. One invalid input retains its errors;
two valid inputs invoke the combination callback exactly once. Error order
and multiplicity are preserved; no deduplication, sorting, parallel evaluation
or completion-time ordering is performed. Error concatenation is associative
(`OV-OBL-005`).

Optional and dependent outcomes provide the existing Mapper, MultiMapper,
ValueEmbedder, Chainable and Workflow capabilities. Independent validation
provides Mapper, MultiMapper and ValueEmbedder. It does not provide Chainable
or Workflow: a fail-fast chain would disagree with its accumulating binary
mapping. A compiler MUST NOT synthesize such an instance merely because a
success constructor exists (`OV-OBL-005`).

The dependent and independent error parameters are fixed when their unary
categorical constructors are selected. Instances retain the existing
trait-or-type ownership and coherence requirements. Law tests are bounded
executable evidence, not permission to reorder observable effects.

## Explicit elimination and conversion

Each family has a total eliminator with a handler for each side. Exactly the
selected handler runs. The absence handler receives the empty product, used
only as a thunk argument. There is no partial unwrap operation in this
contract (`OV-OBL-006`).

The following conversions are explicit operations:

- Optional to dependent: preserve presence; on absence invoke the supplied
  empty-product-to-error callback once to construct failure.
- Dependent to optional: preserve success; deliberately discard the error
  of failure to produce absence.
- Dependent to independent: preserve success; wrap one failure error into a
  singleton nonempty sequence.
- Independent to dependent: preserve validity; retain the entire nonempty
  error sequence as one failure payload.
- Dependent error mapping: transform a failure payload exactly once; preserve
  success without invoking the error callback.

No operation catches a trap, interprets an unhandled effect, observes another
process's death, restarts a process, or cancels a task automatically
(`OV-OBL-007`). A named foreign adapter must first satisfy the separately
admitted foreign boundary before its validated expected-failure value can use
these conversions. This chapter admits no arbitrary host exception adapter
or raw foreign value inspection.

## Execution, diagnostics and limits

The explicitly selected package binds its datatype declarations, operation
bodies and coherent dictionaries to a canonical content digest, and pins the
existing categorical hierarchy digest. Package corruption or a hierarchy
mismatch is rejected before compilation. The ordinary source artifact and
categorical companion are deterministic for the same inputs. Their retained
`0.1.4` format and uniform package layout do not claim a new `0.1.54` executable
frontend (`OV-OBL-001`, `OV-OBL-008`).

Wrong constructor payloads, non-exhaustive handlers and incoherent instances
use the existing datatype, pattern and trait diagnostics. No new language
error namespace is required. Failure to resolve independent Workflow evidence
is a trait diagnostic. Raw host calls to package implementation functions are
outside the typed application boundary (`OV-OBL-002`, `OV-OBL-005`).

Successful mapping and sequencing add constant work beyond the callback.
Error concatenation takes linear time and allocation in the combined error
count in the selected implementation, preserves every error, and is stack
safe. These guarantees do not claim that repeated growing-left concatenation
is linear in total history. Foreign boundaries and general collection
builders remain separately owned (`OV-OBL-008`).

## Variability and limits

All new behavior is fixed by this chapter; no new variability is introduced. Finite allocation inherits the
[runtime capacity policy](../../IMPLEMENTATION-LIMITS.md#runtime-and-mailbox-capacity).
Capacity exhaustion retains its existing classification; it is not silently
converted into an expected failure value. No universal maximum error count or
new portable capacity floor is introduced. The area's
[register](README.md#variability-register) records this inheritance.

## Rationale and evidence (non-normative)

The [planned choices](../../20-notes/language-completion-plan-delivery.md#item-103-outcome-types)
select ordinary outcomes, separate dependent and independent combination,
and explicit adapters. The
[combinator synthesis](../../20-notes/combinators-for-algebraic-data-and-categorical-programming.md)
explains why operational callback counts accompany algebraic laws.
The [implementation journal](../../50-journal/2026-09-08-outcome-contracts.md)
records alternatives, compiler defects exposed by polymorphic library code,
reference/BEAM agreement and publication evidence.
