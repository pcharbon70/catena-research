---
title: "Syntax-Independent Document Algebra"
kind: specification
created: "2026-09-11"
status: normative
spec_version: "0.1.94"
tags: [specification, formatting, tooling, source-text]
aliases: []
---

# Syntax-Independent Document Algebra

## Status and authority

G118 defines its preparatory formatter foundation at revision `0.1.94` under
[authority](../../SPECIFICATION-AUTHORITY.md),
[conformance vocabulary](../../CONFORMANCE-VOCABULARY.md), and
[implementation limits](../../IMPLEMENTATION-LIMITS.md). It executes the
[G118 plan](../../20-notes/language-completion-plan-delivery.md#item-118-formatter)
without choosing Catena's public vocabulary or grammar. Public-source tree
construction, canonical production layouts, source edits, and whole-formatter
idempotence remain held for P109, so G118 remains partial (`FM-OBL-001`).

## Document algebra

The preparatory printer MUST accept only a validated, syntax-independent
document made from text, breakable line, hard line, concatenation, nonnegative
nesting, grouping, and verbatim-origin nodes. Text nodes MUST contain valid
Unicode without a line break. Concatenations MUST be nonempty. Group and nest
nodes MUST contain exactly one child (`FM-OBL-002`).

A group MUST render each breakable line as one space when its flattened
Unicode-scalar width fits the remaining line width. Otherwise it MUST render
breakable lines as newlines followed by the active nesting indentation. A hard
line MUST always render as a newline followed by that indentation. The choice
MUST be deterministic for identical document, width, and revision
(`FM-OBL-003`).

Width MUST be measured in Unicode scalar values. The default width MUST be
100 scalar values, and an accepted requested width MUST be an integer from 1
through 240 inclusive. Nesting MUST use ASCII space bytes and MUST NOT exceed
240 spaces per nest node (`FM-OBL-004`).

## Verbatim origins and preservation

A verbatim node MUST identify an exact tokenizer token by its bytes, original
source byte span, and role. Its role MUST be `comment`, `literal`, or `token`
and MUST agree with the tokenizer's classification. A forged, mismatched, or
out-of-range origin MUST be rejected before rendering (`FM-OBL-005`).

The formatter MUST copy each verbatim node's source bytes exactly. A comment
attachment MUST be either absent or an opaque byte string of at most 256
bytes; literals and other tokens MUST have no attachment. Formatting MUST
preserve comment attachment identity and literal bytes without decoding,
normalizing, or selecting alternative delimiters (`FM-OBL-006`).

Every rendered verbatim node MUST produce one source-map entry containing its
role, attachment, exact original byte half-open span, and exact output byte
half-open span. The bytes selected by both spans MUST be equal
(`FM-OBL-007`).

## Preview identity and mutation boundary

A preview MUST bind format name, revision, width and width unit, exact Base64
preimage and result bytes, SHA-256 digests of both, complete source map,
applicability, and public-source status. It MUST carry a canonical digest over
all preceding fields. Repeated previews of identical validated inputs MUST be
byte-equivalent as canonical data (`FM-OBL-008`).

Previewing MUST NOT mutate an input. Revision `0.1.94` MUST report
`machine-applicable-after-p109` applicability and `held-for-p109`
public-source status. Applying a valid, authorized, nonstale preview MUST
produce the explicit `public-source-formatting-held-for-p109` outcome and MUST
NOT overwrite the source (`FM-OBL-009`).

Application MUST require explicit authorization and an exact current preimage
digest. Missing authorization or a stale preimage MUST produce
`format-not-authorized-or-stale` without mutation. Preview validity MUST NOT
constitute authorization (`FM-OBL-010`).

This revision fixes rendering of an already constructed document only. It MUST
NOT claim semantic-tree preservation, public-source round trips, formatter
idempotence over parsed programs, atomic source edits, or source compatibility.
Those obligations require P109's lossless public parser and production
identity (`FM-OBL-011`).

## Limits and variability

One preview is limited to 65,536 document nodes, nesting depth 64, 16,777,216
input bytes, and 16,777,216 output bytes. The output bound MUST be established
before allocating the complete rendered result. Exceeding width, structure,
input, output, or attachment bounds MUST produce the distinct
`format-limit-exceeded` implementation-limit outcome and MUST NOT mutate an
input (`FM-OBL-012`).

This formatter foundation has zero variability dispositions and exposes no
style options. Implementations MUST NOT describe a host formatter, local
preference, or incidental rendering choice as conforming canonical output
(`FM-OBL-013`).

## Conformance

The conformance profile MUST publish revision, input kind, public-source
status, width unit and fixed widths, every structural and byte limit, comment
and literal preservation, source mapping, edit-application status, and the
empty style-option inventory (`FM-OBL-014`).

An implementation claiming this revision MUST exercise wide and narrow group
selection, nesting, Unicode scalar width, hard lines, block and trailing
comments, multiline comment bytes, raw literal bytes, attachment identity,
exact source maps, deterministic previews, forged origins, altered previews,
invalid widths, excessive depth, unauthorized application, stale preimages,
the P109 application hold, lifecycle selection, production compilation,
trust-inventory verification, and its complete regression suite
(`FM-OBL-015`).

## Rationale and evidence (non-normative)

The [implementation journal](../../50-journal/2026-09-11-formatter.md)
records twenty four-way implementation decisions and compiler PRs
[186](https://github.com/pcharbon70/catena/pull/186) and
[187](https://github.com/pcharbon70/catena/pull/187). A document algebra is
useful before grammar adoption because it makes layout, preservation, mapping,
limits, and preview identity executable while leaving every public production
for joint design at P109.
