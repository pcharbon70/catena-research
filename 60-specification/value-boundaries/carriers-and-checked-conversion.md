---
title: "Value Carriers and Checked Conversion"
kind: specification
created: "2026-09-08"
status: normative
spec_version: "0.1.58"
tags:
  - specification
  - representation-independence
aliases: []
---

# Value Carriers and Checked Conversion

## Status and authority

This normative C093 contract applies to exact revision `0.1.58`. It follows the
[authority policy](../../SPECIFICATION-AUTHORITY.md),
[conformance vocabulary](../../CONFORMANCE-VOCABULARY.md) and
[implementation limits](../../IMPLEMENTATION-LIMITS.md). The
[implementation journal](../../50-journal/2026-09-08-value-boundaries.md)
records the experimental evidence and subsequent explicit promotion approval.

This boundary adds a checked pure value tree and typed data conversion;
it does not adopt final source/library vocabulary, general foreign callbacks,
remote serialization, or a stable external ABI. Retained source, interface and
signed formats keep their existing admission rules (`VB-OBL-001`).

## Representation ownership

A value's semantic type governs its admissible observations. A matching host
shape alone does not prove a type, nominal owner, authority or lifetime. Trusted
internal execution uses values produced by verified code. Checked data ingress
validates otherwise untrusted payloads against a descriptor supplied by the
trusted compiler/adapter setup, rather than deriving authority from the payload.
An incoming payload MUST NOT replace its governing descriptor (`VB-OBL-002`).

| Class | Semantic invariant | Representation owner and boundary |
| --- | --- | --- |
| Int | Mathematical integer, without implicit Bool/Float coercion. | Scalar codec and backend; native integer. |
| Bool | Exactly the two Boolean values. | Scalar codec and backend; native Boolean atoms. |
| Unit | One value, with no hidden payload. | Fixed kernel; its distinguished Unit carrier. |
| Float | Finite binary64, retaining both signed-zero bit patterns. | Numeric elaboration owns rounding; scalar codec and backend preserve bits. |
| Text | Complete valid UTF-8 representing Unicode scalars, without implicit normalization. | Text elaboration and scalar codec; native binary. |
| Character | One scalar in 0 through 0x10FFFF, excluding 0xD800 through 0xDFFF. | Text elaboration and scalar codec; native integer. |
| Bytes | A sequence of complete octets, including empty and non-UTF-8 sequences. | Text/byte elaboration and scalar codec; native binary. |
| Product | Ordered components with exact arity and recursively valid fields. | Backend/codec; native tuple. |
| Structural record | Exactly its closed field set, each field checked at its declared type. | Fixed kernel/codec; native map keyed by compiler-declared labels. |
| Structural variant | One declared alternative and its checked payload. | Fixed kernel/codec; distinguished variant tag, label and payload. |
| Nominal data | Declared type/constructor identity and instantiated fields. | Nominal layout owner; compact, uniform or fixed layout is an explicit descriptor property. |
| Closure | Verified executable body and immutable captured environment. | Backend; internal callable carrier, not a stable environment serialization. |
| Dictionary/evidence | Coherent selected implementation; verification evidence is not a source value. | C004/C006 elaboration, specialization and erasure. No ordinary data ingress schema. |
| Lexical capability identity | Bound authority identity, not an ordinary value or ambient textual lookup. | C005/C050 scope checking; no ordinary data ingress schema. |
| Service-authority descriptor | Explicit verified origin, schema and provisioning authority. | C087/C089 contract/manifest validation. A structurally similar record does not create authority. |
| Runtime handle | Governing owner, scope and live state. | C080/C084 runtime. No raw PID/reference/fun admission through the data codec. |

All primitive payloads are checked independently of a recorded type annotation.
Invalid UTF-8 is not silently repaired; arbitrary Bytes are not silently treated
as Text; an integer is not silently converted to Float (`VB-OBL-003`).

## Pure value-tree boundary

The exact selection is edition `0.1`, revision `0.1.58`, with no
previews. Its programmatic input is a retained parsed kernel tree extended with
explicit finite Float, Text, Character and Bytes literal nodes and corresponding
type atoms. This is a tree interface, not a new textual grammar. Scanned literal
meanings from C017/C018/C040 supply payloads; the tree checker independently
validates payloads even when a caller bypasses scanning.

The module is closed and pure: no imports, processes, effect declarations,
handlers, capability slots, scoped resource operations or latent function effects.
Purity includes datatype and trait metadata, not only top-level evaluation.
Existing pure function application, immutable capture, products, records,
variants, nominal construction and matching retain their kernel meaning.
No new arithmetic, ordering, literal-pattern or callback operation is inferred
from admitting a carrier. Existing integer/Boolean/Unit operations keep their
established checks (`VB-OBL-004`).

Inference, independent verification, the reference stepper and BEAM lowering
agree on these carriers. Changing an old core's annotation or literal tag does
not opt it into the new boundary. Old kernel revisions MUST reject the new
carrier types/tags. A compiled value-tree artifact records its exact frontend,
selection and tested toolchain provenance; it creates no new interface or signed
format. The exact selection and retained-format gates are part of artifact validation
(`VB-OBL-005`).

## Checked structural and nominal conversion

Scalar, product, closed record and closed variant descriptions recursively define
conversion. Native records use compiler-declared atom labels; semantic records
use the corresponding strings. Semantic variant observations carry the declared
string label; native variants use the corresponding compiler label. Payload
labels are matched against the descriptor, never interned as arbitrary new atoms.
Unknown, extra, missing or wrongly typed components reject (`VB-OBL-006`).

An ordinary nominal descriptor is derived from a verified exported type and
constructor metadata. A fixed-kernel descriptor derives its type metadata from
verified exported kernel declarations. Semantic constructor observations contain
origin/module/type-qualified constructor identity and an ordered field list.
Parameter substitution applies recursively through nested field types.

Compact nullary constructors use their declared constructor atom; non-nullary
constructors use a constructor-tagged tuple. Uniform constructors carry explicit
type identity, declaration ordinal and a field tuple. Fixed-kernel constructors
carry the kernel's constructor tag/name and field tuple. These are internal layout
contracts, not cross-version ABI promises. An ordinal is meaningful only within
its governing nominal descriptor.

All three representations preserve semantic identity and field observations.
Malformed arity, unknown constructors, wrong nominal identity and improper field
lists reject. Private or abstract constructors cannot be reconstructed through
this codec. Generalized/existential nominal data retain their established
verified internal lowering; this conversion boundary does not reify existential
evidence or admit external reconstruction (`VB-OBL-007`).

Closures pass internally only through verified typed computation. A raw host fun
is not accepted merely because its arity matches. Foreign callback admission and
calling conventions are separate contracts. Scope handles remain under their
existing owner/runtime checks; cross-owner access, use after release and use
after scope exit reject. Copying a handle's physical shape does not create a
valid handle. Evidence, resumptions and authority machinery have no ordinary
value conversion schema (`VB-OBL-008`).

## Budgets, diagnostics and limits

Each conversion explicitly receives a positive integer node budget and a
nonnegative integer payload-byte budget. A scalar or container consumes one
node. A container additionally consumes the budgets of its visited payloads.
An Int consumes the length of its unsigned base-256 magnitude (zero consumes one
byte); Bool consumes one byte; Unit zero; Float eight; Character four; Text/Bytes
their payload byte length. Labels, constructor descriptors and metadata are not
payload bytes. A variant visits only its selected payload.

Budgets describe payload validation effort, not the cost of constructing or
verifying trusted descriptors, wall-clock time, peak allocations or all BEAM
memory. Budget exhaustion produces the distinct `validation_budget_exhausted`
result. An invalid budget produces `invalid_validation_budget`. Neither is
reported as a successful conversion or silently coerced data (`VB-OBL-009`).

Malformed descriptors/types reject as `invalid_boundary_description` or
`invalid_boundary_type`. Invalid payloads reject as `payload_type_mismatch`,
`malformed_representation`, `wrong_nominal_identity`, or
`unsupported_or_malformed_nominal`, as applicable. These role names identify
adapter results; they do not select public language vocabulary.

Tree compilation inherits the published integer-literal, decoded text/byte,
callable-arity and generated-artifact limits. The checker and compiler both
apply the relevant literal limits, so direct tree submission cannot bypass
scanning limits. A per-call conversion budget is an explicit requested runtime
capacity, not a new implementation-wide portability ceiling. The
[variability register](README.md#variability-register) records the inherited
limits; exhausted capacity does not make source validity dependent on a host's
arbitrary data representation (`VB-OBL-010`).

## Rationale and evidence (non-normative)

The [CP-093 plan](../../20-notes/language-completion-plan-delivery.md#item-093-catena-to-beam-value-mapping)
chooses per-type layouts, checked ingress and scoped opaque handles. The
[representation contract](../data-and-patterns/interfaces-and-representation.md)
separates nominal identity from physical layout. The
[built-in data model](../built-in-data-model/the-twelve-way-classification.md)
provides the scalar semantic types; the
[function contract](../functions-and-calls/arity-and-application.md)
provides immutable capture. The [journal](../../50-journal/2026-09-08-value-boundaries.md)
records alternatives, verifier defects, native/reference comparisons, explicit
exclusions and the promotion evidence.
