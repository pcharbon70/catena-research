---
title: "Catena Literal Grammar"
kind: note
created: "2026-08-18"
maturity: developing
tags:
  - bytes
  - catena
  - characters
  - language-design
  - literals
  - syntax
  - text
aliases:
  - "Catena atomic literal model"
---

# Catena Literal Grammar

## Executive conclusion

Catena's first literal slice should be deliberately atomic. It should fix the
token spelling and lossless decoding of Booleans, unsigned integers,
decimal-only floats, Unicode text, one-scalar characters, and byte sequences,
while leaving numeric runtime types, collection construction, atoms/symbols,
operators, and complete parsing to their existing owners.

The selected string family has static cooked text (`"..."`), static raw text
with exact arbitrary hash delimiters (`r#"..."#`), and byte counterparts
`b"..."` and `br#"..."#`. Cooked forms use a small closed escape set. Raw
forms perform no escape processing and own every internal logical LF, so those
line breaks never become C015 layout. Character literals decode to exactly one
Unicode scalar rather than one grapheme cluster.

This design closes G017 without pretending to close the lexer or numeric
model. It also makes a compatibility promise: ordinary and raw text are
permanently non-interpolating. A later interpolation feature must opt in with a
new prefix.

## Scope and method

The operational target was independent agreement on one token's boundary,
decoded payload, exact components, source provenance, and failure. The design
was tested against C013's preserving source units, C014 identifier boundaries,
C015 layout ownership, C016 comment isolation, C012 portable limits, and the
still-open G018/G019/P109 boundaries.

Primary comparative evidence came from the official [Rust literal-token
reference](../30-sources/rust-project-2026-literal-tokens.md), the expanded
[Python lexical reference note](../30-sources/python-software-foundation-2026-python-lexical-analysis.md),
and the expanded [Swift lexical-structure note](../30-sources/swift-project-2026-lexical-structure.md).
Source claims below remain distinct from Catena proposals.

## Relation to the current corpus

[C013 source text](../60-specification/source-text/README.md) already supplies
strict UTF-8, LF-normalized logical units, scalar preservation, and original-
byte spans. Literal decoding starts from those units. It does not decode bytes
again, repair Unicode, or normalize text.

[C014 identifiers](../60-specification/identifiers/README.md) supply the XID
continuation property needed to distinguish `true` from `true_value` and to
reject numeric suffixes without silently accepting a shorter number. Literal
text itself is not an identifier and therefore does not inherit NFC or script
restrictions.

[C015 layout](../60-specification/whitespace-and-layout/README.md) classifies
LF only outside token-owned content. C017 closes its deferred literal edge:
raw-literal LF is decoded payload and provenance inside one opaque token;
cooked literals cannot contain a source LF.

[C016 comments](../60-specification/comments-and-documentation-comments/README.md)
and C017 are parallel atomic scanners. Each receives a caller-supplied unit
index and never recognizes its delimiters inside the other token. G019 still
has to compose them with identifiers, whitespace, punctuation, and operators
into a maximal whole-file token stream.

[C012 implementation limits](../IMPLEMENTATION-LIMITS.md) reserved two
literal dimensions. C017 activates both: `LIM002` applies by mathematical
decimal digit count to every integer base, and `LIM004` applies to decoded
UTF-8 text bytes or decoded byte octets.

## Comparative evidence and inference

### Rust: exact raw delimiters and a useful byte/text split

The Rust Reference reports raw strings delimited by a caller-selected count of
hashes, raw byte strings with ASCII content, separate character and byte
forms, and tightly specified escapes. That is source evidence, not Catena
authority.

The Catena inference is that exact symmetric hashes solve embedded-quote
pressure without adding an escape language to raw content. Catena adopts the
mechanism and direct-ASCII raw bytes, but not Rust's full suffix, byte-
character, numeric, or cooked-line-continuation surface. Catena also declines a
language hash-count ceiling: an iterative scanner can match the opener exactly,
and a future resource refusal must be disclosed as an implementation limit
rather than hidden grammar.

### Python: flexible prefix combinations increase the state space

Python's lexical reference reports multiple string-prefix families, raw and
bytes distinctions, triple-quoted multiline forms, formatted strings with
replacement fields, based integers, decimal/exponent floats, and underscores
inside numeric digit sequences. These facilities show how quickly the cross
product of prefix, quoting, interpolation, escape, multiline, and value-kind
rules grows.

Catena adopts the evidence that separators belong between digits and that raw,
bytes, and interpolation are separate lexical dimensions. It rejects Python's
broad prefix combinations, two quote styles for text, triple quotes, implicit
adjacent literal concatenation, and interpolation inside an otherwise
ordinary text form. A small closed set gives independent scanners fewer
contextual cases and reserves syntax for later evidence.

### Swift: extended delimiters can make interpolation opt-in

Swift's lexical structure reports extended string delimiters using hashes,
with escape and interpolation recognition adjusted by the same delimiter. It
also demonstrates that nested comments and token recognition can coexist in a
precise lexical grammar.

The useful inference is compatibility-oriented: interpolation should be
lexically opt-in, not retroactively inferred from braces inside an established
string. Catena goes further by making 0.1.13 cooked and raw text permanently
static. A later prefixed form can reuse an exact-delimiter technique without
changing old source meaning.

## Selected atomic model

### Kinds and exclusions

The initial kinds are Boolean, integer, float, text, character, and bytes.
Booleans are exact `true` and `false` keywords. Integers use lowercase `0b`,
`0o`, and `0x` prefixes or ordinary decimal; hexadecimal digits are
case-insensitive. Floats are decimal with digits on both sides of a dot or an
exponent on an integral component.

Signs remain operators. There are no suffixes, hexadecimal floats,
`NaN`/`Infinity` spellings, byte characters, or uppercase prefixes. Lists,
tuples, records, maps, and other collections are syntax trees containing
atomic literals, not single literal tokens. Atoms/symbols remain tied to the
larger primitive and BEAM-value model.

### Canonical numeric spelling

Decimal integral components use either `0` or a nonzero leading digit.
Underscore is allowed once between valid digits and nowhere else. These rules
make numeric spelling canonical enough for diagnostics and migrations without
choosing runtime representation.

The scanner returns exact components rather than host floating-point values.
An integer includes its base, separator-free digits, and exact mathematical
value. A float includes separator-free integral, optional fractional, and
optional exponent digits plus an explicit exponent-sign class. G018 can then
select types and rounding without reconstructing spelling from a rounded host
number.

### Cooked text

The closed escape set is zero, tab, LF, CR, backslash, both quote characters,
two-digit hexadecimal, and braced one-to-six-digit Unicode scalar escapes.
Text/character hexadecimal escapes are ASCII-only; `\u{...}` supplies the
full Unicode scalar range. There is no unknown-escape pass-through and no
backslash source-line continuation.

This set keeps visible control characters expressible while making every
backslash either meaningful or erroneous. It avoids octal escapes, named
Unicode escapes, fixed four/eight-digit Unicode variants, and context-
dependent recovery in the first revision.

### Raw text and line ownership

Raw forms use `r`, zero or more hashes, and a double quote. The closer repeats
the quote and exact hash count. Backslashes and identifier-looking sequences
are content. Logical LF is content and remains attached to its C013 unit and
original CRLF/LF span.

Token ownership is the important integration result: a raw newline cannot
become `soft`, `separator`, or `blank` layout. By contrast, the two source
units `\n` decode to LF without creating any source line break.

### Characters and bytes

A character is one Unicode scalar. This is mechanically stable and composes
with C013 columns; grapheme segmentation and display width remain tooling
concerns. It admits a supplementary scalar and rejects an empty literal or a
base-plus-combining-mark sequence containing two scalars.

Byte forms permit direct ASCII only. `\xHH` contributes any octet, while
Unicode escapes are invalid. This makes the distinction between text scalars,
UTF-8 encoding, and arbitrary byte payloads explicit instead of copying the
source encoding accidentally.

## Lossless frontend record

One atomic result needs more than a decoded value. It preserves kind and form,
logical lexeme, all original units, the merged span, decoded payload, and
ordered pieces. Each piece identifies verbatim or escape source units, exact
span, and decoded contribution. Raw results separately enumerate token-owned
LF units.

This record supports precise diagnostics, formatting, future CST construction,
and migration without forcing the semantic compiler to retain delimiters. It
also provides a clean test oracle: CRLF can normalize logically while the
literal still points to both physical bytes.

## Rejected alternatives

- **Implicit signs** conflate prefix operators with values and make `-` token
  boundaries type-sensitive.
- **Leading-dot or trailing-dot floats** compete with future punctuation and
  increase recovery ambiguity.
- **Permissive underscores** admit many equivalent spellings and error-prone
  separator recovery.
- **Two text quote styles and triple quotes** multiply delimiter/escape cases
  without evidence that the extra forms are necessary.
- **Unknown escapes as literal backslashes** hide mistakes and make later
  escape additions change old source.
- **Grapheme-cluster characters** introduce versioned segmentation and
  variable-length value identity into a primitive token.
- **Direct Unicode in byte literals** confuses scalars with their UTF-8 byte
  encoding.
- **Interpolation in ordinary strings** prevents the language from keeping
  braces and identifier-looking text inert forever.
- **Collection literals inside G017** would silently settle data types,
  evaluation order, duplicates, patterns, and representation owned elsewhere.

## What C017 adds to the design

C017 gives every later lexer and parser one exact literal contract. It
provides deterministic decoded data for diagnostics and future elaboration,
closes the newline-ownership hole in C015, activates the reserved C012 payload
limit, and protects static text from future interpolation drift. It also
narrows G018 to numeric meaning rather than spelling and G019 to token
composition rather than literal internals.

## Remaining questions and falsification criteria

G018 must still decide integer and float types, defaulting, coercion, rounding,
overflow, exceptional values, and negative-expression elaboration. G019 must
decide concrete operator and punctuation tokens and compose all atomic
scanners. G040/G042/P093/G097 own compound and BEAM-native values.

The model should be revisited if whole-lexer construction reveals an
unavoidable token ambiguity, if real Catena programs demonstrate that the
single-line cooked plus raw-hash family is materially inadequate, or if exact
provenance cannot support formatter/CST round trips without changing the
public record. Convenience alone is not enough to reinterpret an existing
literal form.

## Connections

- [Resolved literal inquiry](../40-inquiries/how-should-catena-spell-and-decode-literals.md)
  records the bounded decision.
- [Literal Grammar map](../10-maps/literal-grammar.md) routes through evidence,
  normative rules, limits, and remaining owners.
- [Literal Grammar Specification](../60-specification/literal-grammar/README.md)
  defines the normative 0.1.13 contract.
- [C017 evidence record](../50-journal/2026-08-18-c017-literal-grammar.md)
  records the sibling implementation and verification.

## Sources

- [Rust Literal Tokens](../30-sources/rust-project-2026-literal-tokens.md)
- [Python 3.14 Lexical Analysis](../30-sources/python-software-foundation-2026-python-lexical-analysis.md)
- [Swift Lexical Structure](../30-sources/swift-project-2026-lexical-structure.md)
