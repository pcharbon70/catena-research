---
title: "Units, Unicode and Checked Binary Operations"
kind: specification
created: "2026-09-09"
status: normative
spec_version: "0.1.66"
tags: [specification, unicode, collections, conformance]
aliases: []
---

# Units, Unicode and Checked Binary Operations

## Status and authority

C104 applies to edition `0.1`, exact semantic revision `0.1.66`, without previews,
under [authority](../../SPECIFICATION-AUTHORITY.md),
[conformance vocabulary](../../CONFORMANCE-VOCABULARY.md), and
[implementation limits](../../IMPLEMENTATION-LIMITS.md). It executes the
[reviewed text/binary plan](../../20-notes/language-completion-plan-delivery.md#item-104-text-and-binary-model).
It adds an explicit ordinary index package, checked operations and an exact
text-program artifact over retained input formats. It does not adopt public
interpolation or binary-pattern spelling. Historical source, interface and
signed formats remain unchanged (`TB-OBL-001`).

C040's [data classification](../built-in-data-model/the-twelve-way-classification.md)
continues to define Text as scalar content, Character as one scalar and Bytes
as arbitrary octets. This chapter does not change equality, implicitly normalize
values, make a grapheme a Character, or expose physical binary sharing.
C095 [conversion](../erlang-type-boundary/typed-conversion-and-preservation.md)
and C103 [outcomes](../outcome-contracts/values-sequencing-and-validation.md)
govern the explicit operation boundary.

## Index units and nominal roles

Byte, scalar and grapheme positions are distinct units. The ordinary package
provides separate nominal index types, each containing an Int offset, with
constructors and eliminators. A function expecting one index type rejects an
argument of another. Conversion from a nominal index to a checked operation
descriptor is explicit and preserves its unit and exact revision. Descriptor
verification requires complete reconstruction, including rejection of extra
fields. Negative offsets can be represented but do not designate valid slices.
No untyped Int is silently inferred to be a grapheme index (`TB-OBL-002`).

An index is a coordinate, not an authority token or a digest-bound position in
one particular string. Applying it to another value performs that operation's
bounds checks again. The package binds its complete content and C004 hierarchy;
a recomputed digest cannot authorize altered declarations.

## Measurement and slices

Text measurement explicitly chooses byte length, scalar count or default extended
grapheme count. All use the complete original value. Empty Text has zero in all
three units. Slice endpoints are half-open: first is included, last excluded.
They must use the same unit and satisfy zero ≤ first ≤ last ≤ length in that
unit. Reversed, negative and oversized endpoints produce typed bounds failure;
they are not clamped, wrapped or truncated.

Text byte slices additionally require both endpoints to be UTF-8 scalar
boundaries. Splitting a scalar is typed failure, even when the byte bounds fit.
Scalar slices can separate combining marks from a preceding scalar; grapheme
slices use the pinned segmentation boundary. Bytes slicing accepts only byte
indices and permits every octet boundary, including slices that are invalid
UTF-8. Successful slices return C103 dependent success; mixed units, bad bounds
and split scalars return their distinct dependent failures (`TB-OBL-003`).

## Pinned Unicode algorithms

Runtime text algorithms bind Unicode `17.0.0` independently of language revision,
compiler release and OTP version. Grapheme segmentation uses UAX #29 revision 47,
default extended clusters, without locale tailoring. It preserves original UTF-8
byte boundaries and handles contextual Indic, emoji, regional-indicator and
combining sequences. It does not normalize input to locate boundaries
(`TB-OBL-004`).

Normalization is explicit NFC, NFD, NFKC or NFKD under UAX #15 revision 57. The
selected form uses the pinned decomposition, combining-class and composition
exclusion data. Canonical forms preserve compatibility distinctions; compatibility
forms can erase them. The caller receives a new Text value, whose indices need
not correspond to the original. Equality and concatenation never normalize
implicitly (`TB-OBL-005`).

The compiled table binds exact source URLs and SHA-256 digests for UnicodeData,
DerivedNormalizationProps, NormalizationTest, DerivedCoreProperties,
GraphemeBreakProperty, GraphemeBreakTest and emoji-data. Its bytes have a separate
digest in the text profile. The existing identifier table and its source manifest
remain unchanged. No runtime network lookup or host-default Unicode algorithm
substitutes for this table.

## Strict encoding conversion

The admitted codecs are UTF-8, UTF-16 big/little endian and UTF-32 big/little
endian. Selection is explicit; native endianness and encoding guessing are not
options. Encoding validated Text returns Bytes. Decoding Bytes returns C103
dependent success containing Text or typed malformed-encoding failure containing
the zero-based byte offset where the first ill-formed scalar encoding begins.
A truncated scalar fails at its start. No replacement character or skipped byte
is invented.

UTF-8 rejects overlong sequences, invalid continuations, encoded surrogates and
values outside the scalar range. UTF-16 pairs a high surrogate only with its
required following low surrogate; lone/mispaired surrogates and incomplete
code units fail. UTF-32 requires complete four-byte scalar values. Noncharacters
and unassigned scalars remain valid. A BOM is ordinary U+FEFF data: it is neither
inserted, removed nor used to switch the selected byte order. Round trips preserve
every scalar, including initial U+FEFF and embedded NUL (`TB-OBL-006`).

## Pure composition and format roles

Concatenation takes an ordered finite list of validated Text values and preserves
their content exactly. Adjacent fragments can form a new grapheme across their
join; separate fragment grapheme counts are not promised additive.

Formatting takes explicit typed fragment roles: Text unchanged, Character encoded
as its scalar, Int in locale-independent decimal without grouping or a positive
sign, and Bytes in lowercase hexadecimal with two digits per byte. Fragments
are already evaluated values, visited in order. There is no arbitrary host
inspection, implicit object display, dynamic formatter lookup or evaluation of
text as code. Float formatting is absent here and belongs to P105's separately
reviewed numeric contract. These semantics support later interpolation adoption
without choosing punctuation (`TB-OBL-007`).

## Sequential binary-pattern contract

A verified descriptor has a finite ordered segment list, derived positional
capture tuple schema and whole-input consumption policy. Admitted segments are
literal Bytes, a fixed byte-count capture, an explicitly signed/unsigned integer
with bit width and endian, and a final remaining-Bytes capture. Remaining-Bytes
appears only last. Literal segments capture nothing; other segments append their
value in declaration order. There are no dynamic capture-name atoms.

Integer widths are 1–4096 bits. Big endian admits all these widths; little endian
requires a whole number of bytes. Signed capture uses two's-complement meaning.
Byte-count captures admit nonnegative Int sizes; oversized requests mismatch
without allocating the requested size. A segment can start after a preceding
bit field. Remaining-Bytes requires an octet-sized remainder; partial-bit values
are not admitted through the Bytes role.

All segments must match and consume the entire input, either directly or through
the explicit final remainder. A wrong literal, insufficient input or unconsumed
suffix returns C103 optional absence. Success contains a tuple of typed captures.
Malformed descriptors are refused before matching; a mismatch is not an exception
or malformed-encoding failure (`TB-OBL-008`).

## Retained-input compiled adoption

The exact `0.1.66` text-program artifact takes independently verified retained
core, one exported pure unary entry, a fixed operation pipeline and explicit
budgets. It admits ordinary retained JSON core, retained `0.1.8` kernel core and
C093's `0.1.58` pure value-tree core. Text/Bytes input uses that existing tree
boundary rather than pretending the historical kernel parser accepts new type
spellings. Input and initial result must have C095 closed-data schemas.

Each operation has a fixed type transition. Normalization and text slicing
produce Text; measurement produces Int; encoding produces Bytes; decoding
produces Text; byte slicing produces Bytes; binary matching produces an optional
capture tuple. Formatting accepts an exactly corresponding tuple of fragment
payload types; concatenation accepts a tuple of Text. An Int formatting step is
also admitted. Incompatible transitions, unsupported roles and mixed-unit slice
descriptors fail before compilation. Effectful entry stages cannot claim purity
(`TB-OBL-009`).

The generated wrapper first calls the actual compiled source entry and then
executes the fixed checked pipeline. Every dependent failure terminates the
pipeline without invoking later operations. Successful completion wraps the final
payload in dependent success; optional binary mismatch therefore remains a
nested optional value, not a decode error. Source traps continue to propagate.
The error payload schema is a closed structural variant: mixed-unit and split-scalar
cases carry Unit, bounds carry three Int values, and malformed encoding carries
its byte offset. Conversion/resource refusals remain distinct boundary errors.

The sidecar binds core, entry, steps, budgets, result/error schemas, compiler,
Unicode profile, lowered forms and exact BEAM bytes. Verification rebuilds the
artifact against the supplied trusted inputs. Invocation checks the complete
native argument before entry and refuses a conflicting loaded module; identical
loaded code can be reused. Module loading through this boundary is serialized.
Changing the table version, steps or sidecar cannot change the program while
retaining verified identity. No automatic imports or public names are introduced
(`TB-OBL-010`).

## Bounds and costs

C095 node, scalar-byte and depth budgets apply to input carriers, index descriptors,
pattern descriptors, callback-free formatting fragments and complete returned
outcomes. A limit refusal is not a slice failure, duplicate result, binary
mismatch or malformed encoding. Pipelines and binary patterns each admit at most
253 operations/segments; integer fields admit at most 4096 bits. These are explicit
profile bounds; inherited source integer/literal, generated arity/module and
runtime allocation rules still apply. Retained source compilation checks precede
new lowering. Unknown normalization forms and encoding/format roles are refused
rather than delegated to a host default (`TB-OBL-011`).

Let n be input scalar/byte length as appropriate, m expanded normalization length,
k pipeline/segment count, and o output size. Text validation and scalar/index
construction scan the input. Grapheme segmentation uses one pass with bounded
context state and binary-search property lookup in fixed tables; storing returned
boundaries uses O(n) space. Scalar/grapheme slicing builds those boundaries before
selecting an interval; it does not promise random-access O(1) indexing. Byte slice
output can retain the input allocation under the existing representation boundary.

Normalization decomposes using fixed tables, stably orders combining segments
in O(m log(m + 1)) worst case and composes in linear structural work. Encoding
and formatting cost input plus output work, with integer digit-generation cost
charged separately. Binary matching visits k segments and charges inspected or
captured bits/bytes separately; it never allocates an oversized requested slice
merely to discover mismatch. Artifact rebuilding and source execution are separate
costs from library operations. Caller budgets bound admitted carriers, not a new
promise that every source function terminates (`TB-OBL-012`).

## Variability register

Unicode version, UAX revisions, default extended segmentation and the absence
of automatic normalization are fixed by the profile. Units, forms, encoding,
format roles, widths, endian and signedness are explicit inputs. Pattern and
pipeline caps are 253; integer widths range 1–4096, with byte-aligned little
endian. Node/byte/depth limits use C095; existing source and runtime bounds apply.
There is no locale, native-endian, replacement-decoding or implicit display mode.

## Rationale and evidence (non-normative)

The [implementation journal](../../50-journal/2026-09-09-text-binary-model.md)
records decisions, all 766 official grapheme vectors, 20,034 normalization vectors,
the supplementary scalar invariant and compiled adoption. Primary algorithm
provenance is in the [segmentation source note](../../30-sources/hadley-2025-unicode-text-segmentation.md),
[normalization source note](../../30-sources/whistler-2025-unicode-normalization-forms.md)
and [encoding source note](../../30-sources/unicode-consortium-2025-unicode-standard-17.md).
