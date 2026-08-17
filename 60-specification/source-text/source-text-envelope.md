---
title: "Source-Text Envelope"
kind: specification
created: "2026-08-17"
status: normative
spec_version: "0.1.9"
tags:
  - parsing
  - specification
  - unicode
aliases:
  - "Catena source decoding"
---

# Source-Text Envelope

## Status and authority

This chapter is the normative Catena 0.1.9 boundary between source-file bytes
and the logical character stream consumed by future lexical grammar. Its
authority follows the repository
[Specification Authority](../../SPECIFICATION-AUTHORITY.md); conformance terms
and invalidity follow the
[Catena Conformance Vocabulary](../../CONFORMANCE-VOCABULARY.md).

The chapter applies only to the 0.1.9 source-text frontend. It does not replace
the retained JSON inputs for revisions 0.1.1 through 0.1.7 or the exact ASCII-
bounded [0.1.8 kernel S-expression](../formal-semantic-kernel/canonical-kernel-syntax.md#input-envelope).
Passing this envelope establishes decodable source text, not a grammatically
valid Catena program.

## UTF-8 byte domain

One source input is a finite byte sequence interpreted only as UTF-8. It is
well formed exactly when it can be partitioned into the one-to-four-byte
sequences for Unicode scalar values defined by Unicode Standard 17.0, section
3.9, definition D92 and table 3-7. Overlong sequences, encoded surrogate code
points, values above U+10FFFF, isolated continuation bytes, invalid leading or
continuation ranges, and truncated sequences are malformed.

A decoder does not guess a locale encoding, honor a coding cookie, fall back
to UTF-16 or UTF-32, or replace malformed bytes with U+FFFD. An input that
contains the well-formed UTF-8 encoding of U+FFFD contains that scalar; this is
distinct from replacement decoding.

All well-formed Unicode scalar values, including unassigned code points and
noncharacters, pass this envelope except for the leading-BOM rule below.
Whether a scalar can form an identifier, whitespace, a comment, a literal, or
another token belongs to the applicable later lexical chapter.

## Byte-order marks and signatures

The UTF-8 encoding `EF BB BF` at byte offset zero is a prohibited byte-order
mark and makes the source invalid. UTF-8 has no byte-order choice, so the
signature supplies no information to this exact-encoding protocol.

A leading UTF-16BE, UTF-16LE, UTF-32BE, or UTF-32LE signature is not an
alternate accepted source encoding. It is invalid under the UTF-8-only rule.

U+FEFF at any logical scalar position after the beginning is preserved as an
ordinary scalar by this envelope. Later lexical rules decide whether that
scalar is admitted in its context; it is never stripped or reinterpreted as a
midstream signature.

## Logical newlines

An LF byte and a CR byte immediately followed by LF each decode to one logical
U+000A LINE FEED. LF and CRLF can occur in the same input. A final logical
newline is optional. A CR not immediately followed by LF is invalid.

U+0085 NEXT LINE, U+2028 LINE SEPARATOR, and U+2029 PARAGRAPH SEPARATOR are
ordinary scalars at this layer and do not increment the source line. Later
lexical rules can admit or reject them in particular token classes, but cannot
retroactively treat them as 0.1.9 logical newlines.

The logical text is the decoded scalar sequence with every CRLF replaced by
one LF. No other scalar or byte sequence changes.

## Normalization boundary

The source-text decoder does not test for or transform NFC, NFD, NFKC, or
NFKD. Canonically or compatibility-equivalent scalar sequences remain
distinct logical sequences. In particular, combining marks retain their
written order and precomposed and decomposed spellings are not collapsed.

This preservation rule prevents whole-file normalization from changing
comments, literal contents, or original source locations before their token
classes exist. The future identifier chapter can define identifier-specific
normalization or comparison while retaining mappings to these original
scalars. The future literal chapter independently defines whether literal
values preserve, reject, or normalize their contents.

## Source units and locations

The decoder produces, in order, one source unit for each logical scalar. Each
unit records the scalar and a half-open span into the original byte sequence.
An LF-derived unit spans its one original byte; a CRLF-derived LF unit spans
both original bytes. The decoder also records a zero-width end-of-input span.

Byte offsets are zero based. Line and column numbers are one based. A logical
newline advances the line by one and resets the column to one. Every other
Unicode scalar advances the column by one, including a tab, combining mark,
variation selector, noncharacter, or supplementary-plane scalar. Columns are
not byte counts, UTF-16 code-unit counts, grapheme-cluster counts, terminal
cells, or editor tab stops.

For malformed input, the diagnostic span begins at the first byte of the
first rejected sequence. A truncated sequence spans its remaining bytes. A
recognized unsupported leading encoding signature spans that signature. The
line and column at the rejection point are computed only from the accepted
logical prefix.

## Empty input and downstream validity

The empty byte sequence satisfies this source-text envelope and produces an
empty logical stream with an end-of-input span at byte zero, line one, column
one. A later module grammar is responsible for rejecting an empty stream when
a complete Catena source file requires declarations or a module header.

## Excluded lexical decisions

Revision 0.1.9 defines no identifier repertoire or equality, reserved word,
whitespace class beyond logical newline formation, comment delimiter, literal
escape, numeric spelling, operator, punctuation, layout, recovery, module
header, or file-to-module relation. Those exclusions are owned by G014
through G020 and do not weaken this byte-decoding contract.

## Rationale and evidence (non-normative)

The [source-text synthesis](../../20-notes/catena-source-text-encoding-and-normalization.md)
compares rejection, replacement, BOM, normalization, and position models. Its
primary evidence route includes the [Unicode 17 encoding-form rules](../../30-sources/unicode-consortium-2025-unicode-standard-17.md),
[RFC 3629](../../30-sources/yergeau-2003-utf-8.md), and
[Unicode normalization forms](../../30-sources/whistler-2025-unicode-normalization-forms.md).
