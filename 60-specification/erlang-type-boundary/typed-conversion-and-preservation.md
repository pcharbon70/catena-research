---
title: "Typed Conversion and Preservation"
kind: specification
created: "2026-09-09"
status: normative
spec_version: "0.1.60"
tags:
  - specification
  - foreign-boundary
  - representation-independence
aliases: []
---

# Typed Conversion and Preservation

## Status and authority

This normative C095 boundary applies to exact edition `0.1`, revision `0.1.60`,
without previews. It follows the [authority policy](../../SPECIFICATION-AUTHORITY.md),
[conformance vocabulary](../../CONFORMANCE-VOCABULARY.md), and
[implementation limits](../../IMPLEMENTATION-LIMITS.md), and discharges C067's
[visible typed boundary requirement](../dynamic-and-unsafe-boundaries/the-foreign-visibility-routing.md#the-cross-edge-requirement).

A codec is an explicit descriptor carrying the exact selection and schema.
Verification reconstructs it and requires exact equality; extra fields and
altered selections or descriptions are invalid. This revision adds no dynamic
type, textual declaration, executable frontend, serialized interface or signed
format. Existing code and nominal layouts retain their selected revisions
(`ET-OBL-001`).

## Trusted descriptions and admitted meanings

The compiler/adapter setup supplies the governing schema and resource budgets.
An arriving payload MUST NOT select or alter its own type, layout, declaration,
authority or validation bounds. Shapes are not nominal identity proofs.
Conversion never invents a nominal declaration from a host term (`ET-OBL-002`).

| Codec family | Admission and semantic result |
| --- | --- |
| Closed data | C093 primitives, products, closed records and closed variants. Record labels are explicit compiler metadata, and their fields are recursively checked. |
| Declared nominal | A re-derived exported nominal description, including qualified type/constructor identity, instantiated fields and explicit compact, uniform or fixed layout. |
| Declared sequence | An explicit mapping from a proper Erlang list to a verified unary-parameter nominal declaration with exactly one empty constructor and one head/tail constructor. |

Primitive checks retain C093's
[carrier invariants](../value-boundaries/carriers-and-checked-conversion.md#representation-ownership):
Int is distinct from Bool and Float; Float is finite binary64 with its sign bit
preserved; Text is valid UTF-8 without repair or normalization; Character is a
Unicode scalar; Bytes contains whole octets; Unit has its distinguished carrier.
Products require exact arity, records their exact closed field set, and variants
a declared tag with a checked payload. Unknown, missing, extra and malformed
components are expected conversion failures (`ET-OBL-003`).

Nominal descriptions are reconstructed from verified core and the named export.
Constructor visibility, arity, identity, generic substitution and the exclusion
of GADT/existential reconstruction retain C093's
[checked nominal relation](../value-boundaries/carriers-and-checked-conversion.md#checked-structural-and-nominal-conversion).
No native constructor-looking tuple supplies authority to alter that relation
(`ET-OBL-004`).

Arbitrary maps are not automatically nominal collections. A native map is
admitted here only through the selected closed record relation. Raw PIDs, ports,
references, host funs and authority-bearing wrappers have no generic data-codec
admission. Their existing typed owners remain C080/C084/C094 and their further
foreign roles P097/G098. No equality, reflection or transfer permission follows
from a similar tuple or map shape (`ET-OBL-005`).

## Declared sequence relation

The setup names both constructor identities explicitly; their source spellings
are irrelevant. The declaration has one type parameter and exactly two
transparent, non-GADT, non-existential constructors. The empty constructor has
no fields. The other has two fields: the instantiated element type, followed
by exactly the instantiated sequence type. Reversed roles, additional
constructors, private constructors and different field types are invalid.
This relation introduces no built-in list type or final collection vocabulary.

Decoding an empty Erlang list yields the verified empty constructor. Decoding
a cons checks its head at the instantiated element type and converts the rest
to the same nominal sequence. Encoding reverses this relation. An improper
list or malformed nominal tail rejects the whole conversion; a successful
prefix is never returned (`ET-OBL-006`).

The external encoding and Catena runtime carrier are distinct. A sequence's
wire encoding is an Erlang list; its Catena carrier is produced by the selected
nominal layout owner. The explicit native conversion and both backend literal
helpers use that Catena carrier. The independent verifier entry checks it
against the same re-derived codec. A wire list is not silently substituted for
a fixed/compact/uniform constructor representation (`ET-OBL-007`).

## Whole-carrier budgets and expected failure

Each conversion has exactly three explicit bounds: a positive node count,
a nonnegative scalar-payload byte count and a nonnegative maximum depth.
Preflight walks the complete incoming carrier before typed conversion and the
complete converted result before reporting success. Metadata present in either
carrier counts too; the two representations can require different budgets.
The same supplied bounds apply independently to both passes.

Root depth is zero. A tuple or map is one node; every tuple element and map
key/value is visited at depth plus one. Every list cons is one node, its head
is visited at depth plus one, and its tail retains the list's depth; the empty
list is one node. A scalar is one node. Binary bytes count their byte length;
integers count unsigned base-256 magnitude bytes, with zero occupying one;
Float counts eight bytes; atoms count their UTF-8 name bytes. Bitstrings with
partial octets and raw native authority carriers are unsupported. The typed
relation independently validates the permitted scalar meanings.

A tuple or map whose direct children cannot fit the remaining node budget is
refused before materializing a child list. Binary byte charging precedes UTF-8
scanning. Recursive nominal decoding retains C093's semantic budget checks in
addition to this complete-carrier preflight. Bounds do not authorize coercion,
unchecked interiors or partial success (`ET-OBL-008`).

Conversion reports success with the semantic or encoded value, or expected
failure with a conversion-failure classification, reason and direction. Reasons
distinguish invalid codec/selection, payload or constructor mismatch, improper
sequence, unsupported carrier and exhaustion of each explicit bound. Invalid
setup is refused before payload conversion. Allocation and generated-code
capacity retain the standing implementation-limit policy. Foreign execution
exceptions remain C036/P096's visible trap responsibility; they are not converted
into successful data (`ET-OBL-009`).

## Preservation obligation

For an admitted schema and valid declared metadata, successful decoding produces
a value of the declared semantic type, never a dynamically inferred type.
Successful re-encoding preserves the external value's declared observations,
including nominal constructor/field observations, exact integer meaning, Text
scalars, Bytes octets and finite Float bits. Native conversion similarly
preserves the selected Catena layout. These claims require each participating
representation to fit its explicit bounds. Map field order is not an extra
semantic observation (`ET-OBL-010`).

## Variability register

The contract is deterministic. The node, byte and depth bounds are programmatic
adapter inputs, not hidden implementation thresholds. Existing finite allocation
and generated-code limits apply. There is no additional observable variability
or relaxed native-ingress rule.

## Preservation argument and evidence (non-normative)

The proof argument proceeds by the declared schema. Scalar checks establish the
base cases; exact container shape plus recursive checks establish products and
sums. The existing nominal codec establishes qualified constructor identity and
field substitution. The sequence role check establishes the two inductive
constructors; each decoded head has the instantiated element type and each
converted tail has the same declared sequence type. Complete failure propagation
prevents an unchecked suffix from being published.

The [implementation journal](../../50-journal/2026-09-09-erlang-type-boundary.md)
records a bounded generated preservation corpus, malformed suffix and metadata
witnesses, exact depth/size thresholds, both backend owners and independent
Erlang execution. This is an argument with executable evidence, not a new
machine-checked whole-language proof.

The [NIF API source note](../../30-sources/erlang-otp-nif-float-construction.md)
and isolated fixture correct an earlier conjecture: the documented
`enif_make_double` API refuses non-finite values. Four finite patterns retain
their bits; positive infinity, negative infinity and NaN are refused by both
the documented NIF constructor and ETF decoding. Catena's finite-value check
remains explicit. These observations do not claim that arbitrary native memory
corruption is constrained by a language-level codec; G098 retains native trust
and isolation policy.
