---
title: "Catena Source-Text Encoding and Normalization"
kind: note
created: "2026-08-17"
maturity: developing
tags:
  - language-design
  - parsing
  - unicode
  - utf-8
aliases:
  - "Catena C013 source-text design"
---

# Catena Source-Text Encoding and Normalization

## Executive conclusion

Catena should begin its ergonomic-source work with a deliberately small and
strict boundary: UTF-8 bytes become a logical Unicode scalar stream, LF and
CRLF become one logical newline form, every logical scalar retains a span into
the original bytes, and nothing else is normalized. A leading UTF-8 BOM,
alternate Unicode encoding signature, malformed UTF-8, or lone carriage
return is rejected rather than repaired.

This is enough to make source ingestion portable, testable, and safe without
prematurely deciding identifiers, layout, comments, literals, punctuation, or
module grammar. It also prevents later lexical design from inheriting an
accidental Elixir `String` behavior as language semantics.

## Question and scope

G013 asks which byte sequences are source text, how Unicode normalization
works, which line endings count as newlines, and what happens to invalid
input. An operational answer must let two implementations agree on:

- acceptance or rejection of any finite byte sequence;
- the ordered logical scalar sequence for accepted input;
- the original byte range and language line/column for each logical scalar;
- stable failure categories for rejected input; and
- which questions remain for later lexical layers.

It does not need to recognize a Catena token or prove that the resulting text
is a module. That separation is important: an empty byte sequence can be valid
text while still being invalid under a future file grammar.

## Relation to the current corpus

The [canonical 0.1.8 kernel syntax](../60-specification/formal-semantic-kernel/canonical-kernel-syntax.md)
already has an exact input envelope, but it intentionally accepts only tab,
LF, CRLF, and printable ASCII after UTF-8 decoding. Its name regexes and JSON-
escaped metadata strings exist for formal conformance input, not for future
programmer-facing source. Reusing that restriction would turn a deliberately
small semantic notation into the ergonomic language by accident.

The C006 [canonical evidence rules](../60-specification/specifications-and-governance/evidence-identity-and-lifecycle.md)
preserve valid Unicode strings without normalization because signatures bind
exact canonical JSON bytes. That supports distinguishing preservation from
equivalence, but signed protocol strings are not source tokens.

C008 supplies exact revision selection and migration records. C009 supplies
invalidity and prohibits undefined behavior. C011 supplies permanent
rule-to-test identifiers. C012 requires an explicit owner before a new finite
resource dimension can become an implementation limit. C013 can therefore
define source decoding without adding an aggregate source-size floor.

## Evidence model

The [Unicode 17 conformance chapter](../30-sources/unicode-consortium-2025-unicode-standard-17.md)
gives a closed byte grammar for UTF-8 and separates scalar validity from
assignment or suitability. This supports accepting unassigned scalars and
noncharacters at the encoding layer while allowing a later token grammar to
reject them in identifiers or whitespace.

[RFC 3629](../30-sources/yergeau-2003-utf-8.md) adds two useful protocol
observations: invalid sequences have security consequences, and a BOM is
unnecessary where the protocol already fixes UTF-8. Its distinction between a
leading signature and embedded U+FEFF gives Catena a precise, non-magical BOM
rule.

[UAX #15](../30-sources/whistler-2025-unicode-normalization-forms.md) shows why
whole-file normalization is not a passive validation step. It can decompose,
compose, or reorder scalar sequences, changing bytes and scalar positions and,
under compatibility forms, erasing content distinctions.

## Selected source envelope

### One encoding

UTF-8 is the only source encoding. It is self-synchronizing, preserves ASCII
bytes, covers every Unicode scalar, and has a stable exact well-formedness
table. Supporting UTF-16, UTF-32, platform code pages, or coding cookies would
add encoding detection, byte-order state, and multiple offset models before
Catena has a lexer.

Malformed input is rejected at the first bad sequence. The decoder does not
replace bytes with U+FFFD because replacement would collapse distinct invalid
inputs into one accepted logical stream and could move a token boundary. A
literal U+FFFD encoded correctly is ordinary input, which makes the difference
observable and testable.

### BOM policy

A leading UTF-8 BOM is rejected, not ignored or stripped. This keeps byte zero
stable, avoids a hidden pre-lexical character deletion, and aligns with a
protocol that already mandates UTF-8. Detected UTF-16 and UTF-32 signatures
receive the malformed-or-unsupported-encoding diagnostic.

U+FEFF elsewhere is preserved at the source-envelope layer. Treating every
occurrence as a BOM would violate the signature's positional meaning and make
concatenation non-local. Later token rules can still reject this invisible
format character outside literal or comment contexts.

### Logical newlines

LF and CRLF are the two accepted serialized newline forms. Both decode to one
logical LF; they can be mixed; and a final newline is optional. Lone CR is
rejected rather than silently repaired. NEL, LINE SEPARATOR, and PARAGRAPH
SEPARATOR remain scalars instead of line boundaries.

This choice gives Unix and Windows files identical logical line structure
without making editor display behavior part of semantics. Treating every
Unicode line-separator character as a newline would create surprising token
boundaries and would make future literal and comment rules harder to state.

### Preserve, do not normalize

C013 performs no Unicode normalization. This does not mean Catena has chosen
code-point equality for identifiers; it means the encoding layer is the wrong
place to choose identifier equality. G014 can require identifier NFC, compare
normalized identifier keys, or select a restricted repertoire while still
pointing diagnostics at the original spelling.

The distinction is especially important for future literals and comments.
Normalizing an entire file would change data a programmer may intend to
preserve exactly. Even NFC can reorder combining marks or replace a decomposed
sequence, while NFKC can erase compatibility distinctions.

## Position model

One decoded scalar becomes one source unit. Its half-open span uses original
zero-based byte offsets and one-based lines and columns. CRLF becomes one LF
unit whose span covers two bytes. All other scalars advance the column by one.

Scalar columns are preferable to byte columns because non-ASCII input should
not make a single character advance by two to four language columns. They are
preferable to UTF-16 units because Catena is not exposing a UTF-16 protocol.
Grapheme clusters and display cells are unsuitable because their segmentation
or width depends on more Unicode properties, surrounding text, fonts, editor
settings, and tab stops. Tools can calculate display columns without changing
the language span.

The decoder also records a zero-width end-of-input span. This gives later
lexers an exact location for unterminated tokens or missing final forms without
inventing a sentinel character.

## Public implementation boundary

The sibling compiler represents the result as original bytes, LF-normalized
logical text, ordered scalar/span units, an end-of-input span, and exact
selection. `Catena.decode_source_text/2` is reusable by the future lexer.
`catena check-source-text` exposes a narrow user-facing check and reports only
counts and selection; it does not echo source contents or claim grammatical
validity.

The language registry must separate retained revisions from frontend and
artifact capabilities. Otherwise adding 0.1.9 to the ordered revision list
would accidentally let a JSON input compile under 0.1.9 or let an interface
claim 0.1.9 semantics. Explicit JSON, kernel, source-text, compilation, and
interface revision sets prevent that leakage.

## Rejected alternatives

### Accept and strip one UTF-8 BOM

This improves compatibility with some editors but makes byte zero conditional
and silently deletes an encoded scalar before lexing. A precise rejection with
`SRC002` has one repair and keeps the format simpler.

### Normalize the whole file to NFC

This gives canonically equivalent strings a common representation, but it also
changes comments and future literal payloads and complicates every original-
byte location. Identifier-specific normalization achieves the likely naming
benefit without broad content mutation.

### Require the whole file already be NFC

This preserves bytes but still makes comments and literals subject to an
unnecessary global restriction. It also forces a Unicode normalization
implementation into the first decoder even though C013 otherwise needs only
stable UTF-8 scalar rules.

### Accept CR, NEL, LINE SEPARATOR, and PARAGRAPH SEPARATOR

Broad newline acceptance looks Unicode-friendly but introduces more
cross-platform spellings and invisible structure before layout and comment
rules exist. LF and CRLF cover the dominant source-file conventions and give
one unambiguous logical newline.

### Use grapheme or display columns

These are attractive for UI caret placement but are unstable as a language
coordinate: tabs, combining sequences, emoji segmentation, East Asian width,
and editor rendering all need extra policy. Scalar columns remain deterministic
and tools can add a display projection.

## Falsification and follow-up

The design fails if two conforming decoders disagree on accepted bytes,
logical scalars, or coordinates; if malformed input reaches a lexer through
replacement; if CRLF loses its original two-byte span; if canonical-equivalent
source is silently collapsed; or if 0.1.9 leaks into an interface or compiled
artifact.

C013 does not settle Unicode identifier security, normalization-based name
equality, whitespace, comments, literals, layout, formatter round trips,
source-size denial of service, or source spans through typed-core elaboration.
Those remain explicit G014–G020, P117, G118, and wider operational work.

## Connections

- [Source Text Encoding and Normalization map](../10-maps/source-text-encoding-and-normalization.md)
  routes through evidence, the decision, normative rules, and executable
  conformance.
- [How Should Catena Decode and Normalize Source Text?](../40-inquiries/how-should-catena-decode-and-normalize-source-text.md)
  records the resolved operational question.
- [Source Text Specification](../60-specification/source-text/README.md) is the
  controlling 0.1.9 contract.
- [C013 Source-Text Encoding and Normalization](../50-journal/2026-08-17-c013-source-text-encoding-and-normalization.md)
  records the coordinated implementation evidence.

## Sources

- [The Unicode Standard, Version 17.0: Conformance and Encoding Forms](../30-sources/unicode-consortium-2025-unicode-standard-17.md)
- [RFC 3629: UTF-8, a Transformation Format of ISO 10646](../30-sources/yergeau-2003-utf-8.md)
- [Unicode Standard Annex #15: Unicode Normalization Forms](../30-sources/whistler-2025-unicode-normalization-forms.md)
