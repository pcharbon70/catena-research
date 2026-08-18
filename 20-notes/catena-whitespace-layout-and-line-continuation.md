---
title: "Catena Whitespace, Layout, and Line Continuation"
kind: note
created: "2026-08-17"
maturity: developing
tags:
  - catena
  - language-design
  - layout
  - syntax
  - whitespace
aliases:
  - "Catena layout model"
---

# Catena Whitespace, Layout, and Line Continuation

## Executive conclusion

Catena should use an explicit, indentation-insensitive block model with an
Elixir-like distinction between expression separators and continued lines.
ASCII space and tab are horizontal trivia. C013 logical LF and semicolon are
the two separator spellings. A line break becomes soft only because a token or
delimiter context says that the surrounding form is incomplete; its column
never decides program structure.

The key design device is a token-capability boundary. G015 fixes the layout
algorithm without guessing G019's operator inventory: tokens can require a
left or right expression, and opening delimiters identify either a continued
context or an expression-block context. Later lexical work assigns those
capabilities to concrete tokens.

## Relation to the current corpus

[C013 source text](../60-specification/source-text/README.md) already turns LF
and CRLF into one logical LF while preserving exact original-byte spans. It
deliberately leaves U+0085, U+2028, U+2029, tabs, and every other scalar
unclassified. G015 must consume that stream rather than define a second newline
decoder.

[C014 identifiers](../60-specification/identifiers/README.md) fix standalone
name spelling but explicitly defer whole-source boundaries. Whitespace can now
separate real tokens without changing the Unicode, NFC, security, keyword, or
qualification decisions behind those names.

The broader research corpus uses indentation to make provisional examples
readable, but it repeatedly says punctuation remains open. In particular, the
[list-comprehension synthesis](list-comprehensions.md) rejects semantics that
depend on layout accidents. Existing examples also use multiline records,
matches, handlers, and comprehensions in ways that need predictable
continuation without committing their complete grammar in G015.

## Evidence comparison

### Elixir: explicit structure with grammar-aware lines

The [Elixir syntax and Unicode reference](../30-sources/elixir-project-2026-elixir-syntax-and-unicode.md)
provides the closest BEAM-facing model. Indentation is presentation. Newlines
and semicolons separate expressions, while explicit `do`/`end` and delimiter
syntax establish structure. Multiline calls and operator expressions continue
because their grammar is incomplete, not because the next line is indented.

Catena adopts that separation of concerns, but not Elixir's complete concrete
syntax. G015 reserves semicolon as an explicit separator and defines abstract
continuation capabilities. G019 still chooses operators, precedence, and
delimiter spellings.

### Python and Haskell: the cost of semantic columns

The [Python lexical reference](../30-sources/python-software-foundation-2026-python-lexical-analysis.md)
shows a deterministic indentation stack and useful implicit joining inside
brackets. It also needs tab expansion, inconsistent-mixing errors, INDENT and
DEDENT tokens, and special blank-line behavior. Those mechanisms are justified
when columns define suites; they are needless state when Catena can use
explicit structure.

The expanded [Haskell 2010 source note](../30-sources/marlow-2010-haskell-language-report.md)
shows a more grammar-coupled offside translation. Indentation can insert braces
and semicolons, explicit and implicit layout contexts interact, and a parser
error can close a layout context. This is precise but makes lexical layout
depend on grammar and fixed column conventions.

Catena rejects both column-driven models. It therefore needs no tab stops,
mixed-indentation error, INDENT/DEDENT token, or display-width rule.

### Rust: free-form whitespace is not enough

The [Rust whitespace note](../30-sources/rust-project-2026-rust-whitespace.md)
demonstrates the simplest alternative: whitespace only separates tokens and
has no semantic significance. That is a useful indentation principle, but
Catena's approachable examples need a documented account of newline-separated
forms and multiline continuation. Treating every newline exactly like one
space would leave that boundary to undocumented parser behavior.

## Selected model

### Narrow layout whitespace

Outside tokens, comments, and literals, Catena recognizes only ASCII space,
ASCII horizontal tab, and the logical LF supplied by C013. Tabs are ordinary
trivia and advance the already-defined scalar column by one. No tab-stop
expansion exists because indentation is not interpreted.

The narrow set prevents nonbreaking spaces, visual direction marks, and
Unicode line-separator characters from silently changing token separation.
Future literal and comment specifications can retain such scalars inside the
tokens they own.

### Hard separators

A hard logical LF or semicolon separates complete sibling forms. Blank logical
lines are retained for tooling but do not create empty expressions. End of file
can finish a complete final form without a final LF.

Semicolon is always hard. Unlike a physical LF, it cannot disappear because an
operator or delimiter requests continuation. This makes same-line separation
visible and prevents a punctuation error from silently joining two forms.

### Token capabilities

A token may request continuation before itself, after itself, both, or neither.
A leading pipeline-like token would request a left expression; an assignment
or infix token at the end of a line would request a right expression. G015
defines those meanings without asserting that any particular operator exists.

An opening delimiter also identifies its line policy:

- a **continued frame** treats contained line breaks as soft, as in a future
  multiline argument or collection form;
- a **block frame** permits hard separators between contained expressions.

The innermost frame controls the delimiter rule. Token requirements can still
make one line soft inside a block. Delimiter families must close in stack
order, but their concrete characters or keywords belong to later grammar work.

### Lossless classification

The layout engine should preserve tokens, whitespace runs, line breaks,
semicolons, and original-byte spans. Each logical LF receives one of three
classifications:

- `soft` when it continues the surrounding form;
- `separator` for the first hard LF in a gap after content; or
- `blank` when it precedes content or follows another hard separator.

This is enough for a later parser to discard trivia while a formatter or
diagnostic tool retains the original layout.

## Failure boundaries

Unsupported layout whitespace is invalid source rather than an alias for a
space. A mismatched or unclosed delimiter context is invalid. A semicolon or
end of input cannot interrupt a token that requires a right expression, and a
token requiring a left expression cannot begin after a hard separator.

G015 does not diagnose every missing separator because only a concrete grammar
can decide where one complete expression ends and another begins. The later
parser consumes the hard-separator events and owns that syntax diagnostic.

## Rejected alternatives

- **Semantic indentation** would make tabs, column calculation, dedentation,
  and generated-source layout part of the language without evidence that they
  improve Catena's semantic forms.
- **Newline-only separation** would forbid compact sibling forms even though a
  visible semicolon can express them without ambiguity.
- **Open-delimiter-only continuation** would reject readable operator layouts
  such as a trailing assignment or leading pipeline.
- **A backslash continuation marker** would add punctuation and edge cases
  while the grammar already knows when a form is incomplete.
- **Settling the operator table in G015** would collapse the G019 research
  boundary and turn a layout decision into an unreviewed precedence design.

## Connections

- [Resolved layout inquiry](../40-inquiries/how-should-catena-treat-whitespace-and-line-breaks.md)
  records the operational question and final choice.
- [Whitespace, Layout, and Line Continuation map](../10-maps/whitespace-layout-and-line-continuation.md)
  routes through the evidence and normative result.
- [Whitespace and Layout Specification](../60-specification/whitespace-and-layout/README.md)
  defines the normative 0.1.11 rules.
- [C015 evidence record](../50-journal/2026-08-17-c015-whitespace-and-layout.md)
  records the sibling implementation and verification.

## Sources

- [Elixir Syntax and Unicode](../30-sources/elixir-project-2026-elixir-syntax-and-unicode.md)
- [Python Lexical Analysis](../30-sources/python-software-foundation-2026-python-lexical-analysis.md)
- [Haskell 2010 Language Report](../30-sources/marlow-2010-haskell-language-report.md)
- [Rust Whitespace](../30-sources/rust-project-2026-rust-whitespace.md)
