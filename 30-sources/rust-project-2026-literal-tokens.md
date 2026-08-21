---
title: "The Rust Reference: Literal Tokens and Expressions"
kind: source
created: "2026-08-18"
authors:
  - "Rust Project"
published: null
citation_key: "rustProject2026LiteralTokens"
container: "The Rust Reference"
edition: null
isbn: null
doi: null
url: "https://doc.rust-lang.org/reference/tokens.html"
accessed: "2026-08-18"
tags:
  - bytes
  - characters
  - floats
  - language-design
  - literals
  - rust
  - syntax
  - text
aliases:
  - "Rust literal tokens"
---

# The Rust Reference: Literal Tokens and Expressions

## Reference

Rust Project, “Tokens” and “Literal expressions,” *The Rust Reference*,
accessed 2026-08-18; the literal-expression typing and conversion rules were
re-read 2026-08-21 for Catena's numeric literal work.
[Official token reference](https://doc.rust-lang.org/reference/tokens.html);
[official literal-expression reference](https://doc.rust-lang.org/reference/expressions/literal-expr.html).

## Research question

How does a production language separate character, string, byte, raw, integer,
and float token forms while keeping raw delimiters and escape validity exact?

## Method

The official token and literal-expression chapters were read for lexical
productions, raw delimiter matching, escape forms, byte restrictions, suffix
handling, and the distinction between token spelling and expression value.
Compiler behavior and community tutorials were not used as authority.

## Findings

- Rust separates character, string, raw string, byte, byte string, and raw
  byte string tokens rather than treating them as one generic quoted form.
- A raw string begins with `r`, a count of hashes, and a quote, and ends with a
  quote followed by the same hash count. Its body does not process escapes.
- Raw byte strings use the corresponding byte prefix and restrict their raw
  body to ASCII.
- Cooked forms use a specified escape repertoire; byte-oriented escapes and
  Unicode-oriented escapes have distinct domains.
- Integer tokens admit binary, octal, decimal, and hexadecimal bases and
  underscores. Float tokens use decimal point and exponent forms. Rust also
  has suffix and byte-character choices that are independent of the core
  delimiter mechanism.
- The literal-expression chapter performs additional semantic conversion
  after token recognition, showing that lexical spelling and typed value are
  separable specification layers.
- An unsuffixed integer literal takes the type uniquely determined by
  context; if the context under-constrains the type it defaults to `i32`, and
  if the context over-constrains it the literal is a static type error. An
  unsuffixed floating literal resolves the same way and defaults to `f64`.
- An integer literal's value is determined by radix and suffix stripping and
  conversion as if by `u128::from_str_radix`; a value that does not fit
  `u128` is a compiler error, and the final cast to the expression's type is
  covered by the `overflowing_literals` lint, which defaults to deny.
- A floating literal's value is converted as if by `f64::from_str` or
  `f32::from_str`. `inf` and `NaN` are not literal tokens, and a literal
  large enough to be evaluated as infinite triggers `overflowing_literals`.
- Rust's reference states that `-1.0` is negation applied to the literal
  expression `1.0`, not a single negative literal, matching the
  token/operator separation Catena fixed in C017.

## Relevance

The exact-hash rule supplies direct primary evidence for Catena's raw
delimiter. The byte/text split helps state direct-ASCII byte content without
confusing it with UTF-8 source. Rust's separation between token recognition and
literal expression meaning also supports closing C017 before G018 selects
runtime numeric types.

Catena uses these mechanisms selectively. It excludes byte-character tokens,
suffixes, cooked source-line continuation, and Rust-specific value types from
0.1.13.

For numeric meaning, Rust supplies the worked example of a typed-literal
layer above exact tokens: static rejection of out-of-range values before
runtime, no `inf`/`NaN` spellings, and negation as an operator. Its
`i32`/`f64` inference defaults, however, are exactly the numeric defaulting
that Catena's C001 contract excludes, and Rust's suffix mechanism is a
surface Catena deliberately does not have, so the same evidence supports
C018's monomorphic typing and its static overflow diagnostic without
supporting defaulting.

## Limits

Rust's type system, suffixes, numeric inference, escape details, and source
grammar differ from Catena. The reference describes Rust, not an empirical
comparison of programmer usability or implementation complexity. Catena's
arbitrary hash count and exact diagnostic families are local proposals that
need their own normative and executable evidence.

## Derived work

- [Catena Literal Grammar](../20-notes/catena-literal-grammar.md)
- [Resolved literal inquiry](../40-inquiries/how-should-catena-spell-and-decode-literals.md)
- [Literal Grammar map](../10-maps/literal-grammar.md)
- [Literal Grammar Specification](../60-specification/literal-grammar/README.md)
- [Catena Numeric Literal Semantics](../20-notes/catena-numeric-literal-semantics.md)
- [How Should Catena Define Numeric Literal Semantics?](../40-inquiries/how-should-catena-define-numeric-literal-semantics.md)
- [Numeric Literal Semantics map](../10-maps/numeric-literal-semantics.md)
