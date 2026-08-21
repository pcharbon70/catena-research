---
title: "Literal Forms and Boundaries"
kind: specification
created: "2026-08-18"
status: normative
spec_version: "0.1.13"
tags:
  - literals
  - specification
  - syntax
aliases:
  - "Catena atomic literal grammar"
---

# Literal Forms and Boundaries

## Status and authority

This chapter is the normative Catena 0.1.13 atomic-literal and numeric-token
grammar. It is governed by
[Specification Authority](../../SPECIFICATION-AUTHORITY.md),
[Catena Conformance Vocabulary](../../CONFORMANCE-VOCABULARY.md), and
[Catena Implementation Limits and Portability](../../IMPLEMENTATION-LIMITS.md).
It consumes the preserving logical units and original-byte spans defined by
the [Source-Text Envelope](../source-text/source-text-envelope.md).

The rules apply only to source-language revision `0.1.13`. They do not
reinterpret retained JSON AST literals, exact 0.1.8 kernel terms, interfaces,
artifacts, or signed formats.

## Atomic literal set

The atomic literal kinds are Boolean, integer, decimal float, text, character,
and bytes (`LT-OBL-002`). Their forms are:

| Kind | Forms |
| --- | --- |
| Boolean | the exact keywords `true` and `false` |
| Integer | unsigned binary, octal, decimal, or hexadecimal |
| Float | unsigned decimal with a fractional part or exponent |
| Text | cooked double-quoted or raw double-quoted |
| Character | cooked single-quoted, decoding to one Unicode scalar |
| Bytes | cooked or raw prefixed double-quoted |

An atomic literal is one token. A leading `+` or `-` is not part of a numeric
literal. The grammar defines no byte-character form. `NaN`, `Infinity`,
numeric suffixes, hexadecimal floats, and uppercase base or string prefixes
are not literal forms.

List, tuple, record, map, set, and other collection notation is compound
syntax rather than one atomic literal. Atom or symbol notation is not part of
0.1.13. Unit punctuation, field labels, interpolation, and complete
file-token composition are outside this area (`LT-OBL-002`, `LT-OBL-012`).

## Boolean literals

`true` decodes to the Boolean true value and `false` decodes to the Boolean
false value. A spelling is a Boolean literal only when the next logical scalar
is not an identifier-continuation scalar under C014. Thus `true_value` is one
identifier candidate rather than a Boolean followed by an identifier.

## Numeric token grammar

> **Normative definition.**

```ebnf
binary-digit        = "0" | "1" ;
octal-digit         = "0" | "1" | "2" | "3" | "4" | "5" | "6" | "7" ;
decimal-digit       = "0" | "1" | "2" | "3" | "4" | "5" | "6" | "7" | "8" | "9" ;
nonzero-digit       = "1" | "2" | "3" | "4" | "5" | "6" | "7" | "8" | "9" ;
hexadecimal-digit   = decimal-digit | "a" | "b" | "c" | "d" | "e" | "f"
                    | "A" | "B" | "C" | "D" | "E" | "F" ;

binary-digits       = binary-digit, { [ "_" ], binary-digit } ;
octal-digits        = octal-digit, { [ "_" ], octal-digit } ;
decimal-digits      = decimal-digit, { [ "_" ], decimal-digit } ;
hexadecimal-digits  = hexadecimal-digit, { [ "_" ], hexadecimal-digit } ;

decimal-integral    = "0" | nonzero-digit, { [ "_" ], decimal-digit } ;
binary-integer      = "0b", binary-digits ;
octal-integer       = "0o", octal-digits ;
decimal-integer     = decimal-integral ;
hexadecimal-integer = "0x", hexadecimal-digits ;
integer-literal     = binary-integer | octal-integer | decimal-integer
                    | hexadecimal-integer ;

exponent-sign       = "+" | "-" ;
exponent            = ( "e" | "E" ), [ exponent-sign ], decimal-digits ;
float-literal       = decimal-integral, ".", decimal-digits, [ exponent ]
                    | decimal-integral, exponent ;
```

The optional underscore in each digit production is the only numeric
separator. It occurs between two valid digits and cannot lead, trail, repeat,
or touch a prefix, decimal point, exponent marker, or exponent sign. A decimal
integral component other than `0` begins with a nonzero digit. These rules
apply equally to integer and float integral components (`LT-OBL-003`).

Binary, octal, and hexadecimal prefixes use lowercase letters. Hexadecimal
digits accept either case. Floats are decimal only. Both sides of a decimal
point contain at least one digit. An exponent contains at least one digit
after its optional internal sign.

## Numeric maximal boundary

Once `0b`, `0o`, or `0x` has been recognized, an immediately adjacent ASCII
letter, digit, or underscore participates in that numeric candidate. A scalar
that is not valid for the selected base makes the candidate malformed rather
than beginning an adjacent identifier. A dot immediately following a based
integer is a malformed unsupported based-float candidate.

For decimal forms, an immediately adjacent exponent marker begins an exponent
and is malformed if its digits are absent. An identifier-continuation scalar
immediately following a completed numeric spelling makes the numeric candidate
malformed. A dot joins a decimal float only when followed by a decimal digit;
`1.` therefore scans as integer `1` followed by punctuation owned by G019. A
dot followed immediately by underscore after a decimal integral component is
a malformed fractional spelling.

These boundary rules prevent an implementation from accepting a valid prefix
of a malformed numeric token and silently changing the program's value
(`LT-OBL-003`, `LT-OBL-009`).

## Exact numeric result

Integer decoding returns the base, the digit sequence with separators removed,
and the exact nonnegative mathematical integer value. Decimal-float decoding
returns base 10, separator-free integral digits, an optional separator-free
fractional component, an exponent sign in the closed set `none`, `plus`, or
`minus`, and an optional separator-free exponent component. It does not round
or select a runtime numeric type (`LT-OBL-003`, `LT-OBL-010`).

## Deliberately separate work

Integer and float runtime types, defaulting, coercion, rounding, overflow,
exceptional floating-point values, and the elaboration of negative numeric
expressions are fixed by the normative 0.1.14
[Numeric Literal Semantics](../numeric-literal-semantics/README.md) area.
G019/P109 own composition with operators and
punctuation. Compound and BEAM-native data forms remain under their existing
G040/G042/P093/G097 owners. Future numeric forms require an explicit later
revision rather than recovery under this grammar.

## Rationale and evidence (non-normative)

The [literal synthesis](../../20-notes/catena-literal-grammar.md) compares
Python, Rust, and Swift lexical designs and explains the deliberately small
atomic set. The
[resolved inquiry](../../40-inquiries/how-should-catena-spell-and-decode-literals.md)
and [topic map](../../10-maps/literal-grammar.md) preserve the wider decision
route.
