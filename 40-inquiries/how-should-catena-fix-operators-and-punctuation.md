---
title: "How Should Catena Fix Operators and Punctuation?"
kind: inquiry
created: "2026-08-21"
status: resolved
tags:
  - catena
  - language-design
  - operators
  - syntax
aliases:
  - "Catena operator inquiry"
---

# How Should Catena Fix Operators and Punctuation?

## Why this matters

C013 through C018 fixed the atoms of source — units, names, layout events,
comments, literals, and numeric meaning — but no Catena token stream exists,
because operators and punctuation have no spelling, no precedence, and no
interaction rules with the pieces that do exist. Until they are fixed,
independent implementations could disagree about whether `a-1` is one token
or three, whether `|` begins a pipe or is invalid, what `x.y.z` is, how `;`
and `,` differ, and which delimiters keep a newline soft. Those disagreements
would leak into every later parser, formatter, editor tool, and diagnostic.

C015 also left an explicit debt: its continuation engine consumes abstract
token capabilities and delimiter frames that only a concrete token grammar
can assign.

## Operational question

Choose a bounded 0.1.15 boundary in which independent implementations agree
on:

- the closed set of operator and punctuation tokens, their exact spellings,
  and their maximal-munch boundaries against every C014–C018 atom;
- which ASCII symbol sequences are reserved and how their appearance fails;
- the fixed precedence ladder and per-level associativity, including whether
  comparisons chain, where the pipe binds, and how prefix negation relates
  to binary subtraction;
- the C015 `join_before`/`join_after` capabilities and delimiter-frame
  families and modes assigned to each concrete token;
- how `.` interacts with C014 qualified names, C017 numeric spellings, and
  future field access without deciding name resolution;
- the failure classes and stable diagnostics of token- and expression-level
  rejection, with no partial or recovered output; and
- a whole-source token stream and a bounded operator-expression layer that
  make the ladder executable rather than merely introspectable.

The answer must compose with C013–C018 without deciding P109 declarations
and application syntax, G020 file structure, G022 import/export syntax,
G040 built-in data, or G061 operator trait dispatch.

## Working hypotheses

- The token set is closed and semantic-mapped: every operator token maps to
  an already-normative meaning (`+ - *` and comparisons from C003/C010,
  Boolean conjunction and disjunction, C018 negation) or is structural
  (`-> |> . , ; ( ) [ ] { }`); unassigned spellings such as `/ % ^` are
  reserved and rejected.
- Precedence is one fixed ladder with per-level associativity, no user fixity
  declarations, prefix `-` above the binary levels, and non-associative
  comparisons requiring parentheses.
- The pipe `|>` is one left-associative operator at the bottom of the ladder
  denoting application of its right operand to its left operand's value.
- Parentheses and brackets push `continued` delimiter frames; braces push a
  `block` frame; `,` and `;` separate inside and across forms respectively.
- Tokenization is deterministic, whitespace-insensitive between tokens, and
  lossless, with transactional rejection and stable diagnostics.

## Paths to explore

- [The Rust Reference: Operator Expressions and Precedence](../30-sources/rust-project-2026-operator-expressions.md)
  supplies the fixed-ladder model with rejected comparison chains.
- [OCaml 5.4 expressions](../30-sources/ocaml-5-4-expressions-and-pattern-guards.md)
  supplies the contrast: left-associative comparisons, right-associative
  `&&`/`||`, separate prefix minus, unspecified operand order.
- [The Haskell 2010 Report](../30-sources/marlow-2010-haskell-language-report.md)
  supplies the rejected user-fixity model with its `infixl 9` default.
- [Erlang/OTP expressions](../30-sources/erlang-otp-expressions-and-guard-sequences.md)
  records the target's strict word operators beside short-circuit
  `andalso`/`orelse` and "any order" operands.
- [C015 separators and continuation](../60-specification/whitespace-and-layout/separators-and-line-continuation.md)
  defines the capability and frame contracts this question must populate.
- [C014 identifiers](../60-specification/identifiers/README.md),
  [C017 literals](../60-specification/literal-grammar/README.md), and
  [C018 numeric meaning](../60-specification/numeric-literal-semantics/README.md)
  fix the atoms the token boundaries must respect.

## Findings

- Rust makes its comparison level non-associative ("Require parentheses"),
  Haskell's Prelude declares its comparisons non-associative, and OCaml —
  the outlier — parses them left-associative. Two of three primary sources
  reject comparison chains, and the OCaml behavior is precisely the silent
  `bool`-comparing surprise a rejecting rule avoids.
- Every surveyed language with a fixed ladder places unary minus above the
  multiplicative level and treats it as an operator over a positive literal
  (`-1.0` is negation of `1.0`), matching C017's unsigned tokens and C018's
  negation elaboration.
- Haskell's silent `infixl 9` default for undeclared operators demonstrates
  the failure mode of extensible fixity: precedence becomes resolved-name
  state rather than a token fact, coupling the lexer to declarations. A
  fixed table with fixity's absence declared is the low-risk answer to the
  checklist's "fixity declarations or their absence".
- The synthesis
  [Catena Operators and Punctuation](../20-notes/catena-operators-and-punctuation.md)
  develops the full model, ladder, and falsification criteria; the
  [topic map](../10-maps/operators-and-punctuation.md) routes the evidence.

## Outcome

Resolved as C019 and source-only language revision `0.1.15`. Catena fixes
the closed semantic-mapped operator and punctuation inventory with maximal
munch and `OPR001` reserved-spelling rejection; assigns every token its
C015 continuation capabilities with `paren`/`bracket` continued frames and a
`brace` block frame; fixes one precedence ladder — prefix `-` and `!`
tightest, `*`, then `+` `-`, then non-associative comparisons and
equalities whose chains are rejected as `OPR002`, then `&&`, `||`, and the
loosest left-associative `|>` — with no fixity declarations; tokenizes `->`
while excluding it from expression rules; keeps `.` qualification-only; and
rejects every failure transactionally without recovery. The rules are
defined in the
[normative operators specification](../60-specification/operators-and-punctuation/README.md).

G019 is complete through the
[operators synthesis](../20-notes/catena-operators-and-punctuation.md),
[topic map](../10-maps/operators-and-punctuation.md), and
[C019 evidence record](../50-journal/2026-08-21-c019-operators-and-punctuation.md).
P109 retains application, declaration, and clause grammar; G020 retains
file-to-module and namespace relations; G022 retains import/export syntax; G040
retains field-like access; G061 retains operator dispatch; G123 retains
editor recovery.
