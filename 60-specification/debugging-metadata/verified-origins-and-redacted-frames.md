---
title: "Verified Origins and Redacted Frames"
kind: specification
created: "2026-09-09"
status: normative
spec_version: "0.1.64"
tags: [specification, compiler, conformance]
aliases: []
---

# Verified Origins and Redacted Frames

## Status and authority

This C100 profile applies to edition `0.1`, revision `0.1.64`, without previews,
under the [authority policy](../../SPECIFICATION-AUTHORITY.md),
[conformance vocabulary](../../CONFORMANCE-VOCABULARY.md), and
[implementation limits](../../IMPLEMENTATION-LIMITS.md). It completes the
[reviewed debugging gate](../../20-notes/language-completion-plan-delivery.md#item-100-debugging-metadata).
It adds an explicit debug artifact built from retained source inputs, not new
public language syntax. Historical source and interface decoders retain their
version sets. This profile introduces executable/artifact `0.1.64`; historical
signed-governance formats are unchanged (`DB-OBL-001`).

## Input, source and node identity

A build takes a source kind, complete source bytes and a logical relative path.
The admitted kinds are retained kernel source, ordinary JSON source, and a
retained closed-capability foreign entry. The last additionally supplies the
slot-family map, exported zero-argument entry and exact verified foreign
operation bindings. Source checking and the independent core verifier precede
lowering. Foreign input also satisfies P096's binding contract.

Logical paths use slash separators, remove dot and empty components, and preserve
case and Unicode spelling. Absolute paths, drive/URI colons, parent components,
NUL and line breaks are refused. Backslashes normalize to slashes. This is a
logical source location, not permission to access a host file. Source bytes are
not rewritten by path normalization.

Source identities bind the complete original bytes by SHA-256. Node identities
bind that source digest, source locator and half-open byte span; lowered-node
identities also bind the deterministic generated path and expansion chain.
Repeated identical builds give identical identities. Changing source bytes
changes source identity even if execution is unchanged (`DB-OBL-002`).

Kernel spans retain the parser's actual ranges. JSON value locators identify the
original carrier, not an invented public source spelling. Its spans use original
UTF-8 byte offsets and one-based Unicode-scalar columns; LF, CRLF and standalone
JSON whitespace CR delimit lines. Grapheme clusters are not columns. Split
codepoint endpoints are refused. Identifier-shaped JSON keys use dot segments;
other keys use quoted bracket segments, preventing a literal dotted key from
claiming a structural descendant's location. No normalization or reserialization
substitutes for locating the original JSON bytes (`DB-OBL-003`).

## Lowered locations and origin chains

Both backends record the source annotation associated with a lowered expression,
definition or handler. Generated forms receive deterministic positive location
tokens in emitted-form traversal order. A token identifies a lowered position;
it is not a line number in the user's source. The runtime filename has the form
`catena-debug://` followed by the module and a digest of its runtime forms.
Actual source spans and generated history live only in the external sidecar.

A mapped record contains its primary source locator/span, source-node identity,
emitted function identity, generated-operation history and explicit inline
call-site records. Details are bounded independently of the primary source
location. Truncation records an omitted-frame count; it never fabricates a
shorter complete history or replaces a known primary span with a guessed
nearby span. Where a lowering node has no precise source span, the missing
coordinate remains missing (`DB-OBL-004`).

The optional Catena inline pass substitutes only eligible closed zero-argument
expression bodies. Binding, closure and control forms are excluded from this
substitution. Depth zero disables that pass; positive depth bounds recursive
expansion. Every expansion retains the callee fault location and the corresponding
call-site history. Reaching the bound leaves the remaining call intact. OTP's
ordinary optimizer still runs in both cases on the pinned toolchain; this
profile does not claim to disable all OTP optimizations.

Runtime reports map only frames actually supplied by the runtime observation.
They do not recreate tail-elided frames. The runtime file token, module, generated
location and owning emitted function must match; compiler-generated anonymous
function names retain their enclosing emitted-function relation. A known frame
from a different emitted program cannot borrow this artifact's origins.
Unrecognized host frames stay unmapped (`DB-OBL-005`).

## Foreign entry and disclosure boundary

A debug foreign artifact preserves P096's exact grants, operation codecs, effect
bindings and mandatory cleanup. Invoking it revalidates the artifact and original
compound input, then authorizes every declaration through the live scope.
Missing host authority fails before entry. Debugging supplies no new foreign
capability.

The exported foreign-entry wrapper retains one physical boundary frame while its
worker executes. A fixed identity return outside the generated module prevents
that wrapper's worker call from becoming a tail call. Recursive workers keep
their tail-call behavior. A reported foreign failure can therefore identify the
actual entry definition, with that boundary granularity explicit; it does not
pretend to recover the eliminated internal request frame. Host frames without
a trusted sidecar have no Catena source origin. Reserved resource cancellation
continues to propagate through its existing cleanup contract.

The new report boundary defaults to redaction of arguments, native failure
reasons, extra host location fields and unknown frame data. Structural module,
function and arity remain available. Explicit value disclosure requires a
verified C095 codec for the complete argument tuple and supplied node/byte/depth
bounds. A failed conversion remains redacted. No primitive-type guess or string-only
redaction rule discloses a value (`DB-OBL-006`).

## Verification and evidence erasure

The sidecar binds source bytes, normalized source path, compound input identity,
profile, emitted forms, exact BEAM bytes and the complete loaded Catena compiler
fingerprint. Verification repeats source checking, lowering and compilation
against the trusted original input and requires complete artifact equality.
Missing, changed or substituted sidecars fail verification before source claims
are returned. Runtime stack data is an observation supplied to the reporter,
not a cryptographic attestation that a process executed those frames.

Only runtime forms contribute to the runtime filename identity. Full source and
erased evidence do not become runtime metadata. Ordinary verification-only
definitions remain absent from BEAM. Changing an erased checker's implementation
without changing runtime code produces the same BEAM bytes while changing its
external sidecar. The runtime alone consequently cannot distinguish all source
or evidence variants with identical execution; the trusted source bundle selects
the version whose sidecar is verified. This is necessary to preserve
[C006 erasure](../specifications-and-governance/artifacts-erasure-and-cli.md).

Erased checker/specification references contain a content digest, source locator
and span in the external sidecar. Navigation revalidates the artifact and input
before returning a reference. It neither embeds the checker or evidence body
into BEAM nor fetches a host path or network resource automatically
(`DB-OBL-007`).

## Retention modes and limits

Sidecar mode emits the minimal virtual file/location information needed for
verified mapping. Stripped mode asks OTP to omit runtime line information;
its reports remain unmapped, even if an external sidecar is retained. Absence
of runtime coordinates never licenses nearest-span inference.

The explicit profile accepts inline depth 0–8, chain length 1–64, a positive
lowered-node maximum at most 1,000,000, and a positive source-byte maximum.
Defaults are zero inline depth, eight chain entries, 100,000 lowered nodes and
1,048,576 source bytes. Unknown options are refused. Source size is checked
before parsing; generated node exhaustion refuses the build. JSON range
coordinates are resolved in a single UTF-8 scan. Ordinary parser, generated
arity/module and allocation limits remain in force (`DB-OBL-008`).

## Variability register

Retention mode, inline depth, chain length, lowered-node count and source-byte
limit are explicit profile inputs with the ranges and defaults above. Disclosure
uses explicit C095 conversion bounds. Runtime optimizer frame omission is
reported as missing information; generated histories are bounded with an explicit
omission count. No arbitrary source-path guess or unverified origin is permitted.
The pinned toolchain and existing finite-resource policy retain their authority.

## Rationale and evidence (non-normative)

The [implementation journal](../../50-journal/2026-09-09-debugging-metadata.md)
records decisions and executed kernel closure, handler, inline, foreign and
ordinary JSON witnesses. It distinguishes a deliberate raw-host type violation
from a well-typed Catena failure. The
[OTP compiler source note](../../30-sources/erlang-otp-29-compiler-recommendations-language-implementors.md)
supports the Abstract Format and stripped-line boundary. Source navigation is
an external tooling capability, not a new pure observation or language vocabulary.
