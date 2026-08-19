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
accessed 2026-08-18.
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

## Relevance

The exact-hash rule supplies direct primary evidence for Catena's raw
delimiter. The byte/text split helps state direct-ASCII byte content without
confusing it with UTF-8 source. Rust's separation between token recognition and
literal expression meaning also supports closing C017 before G018 selects
runtime numeric types.

Catena uses these mechanisms selectively. It excludes byte-character tokens,
suffixes, cooked source-line continuation, and Rust-specific value types from
0.1.13.

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
