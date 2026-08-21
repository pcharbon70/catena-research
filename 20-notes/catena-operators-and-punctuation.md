---
title: "Catena Operators and Punctuation"
kind: note
created: "2026-08-21"
maturity: developing
tags:
  - catena
  - language-design
  - operators
  - syntax
aliases:
  - "Catena operator model"
---

# Catena Operators and Punctuation

## Executive conclusion

Catena's first token-grammar slice should fix a closed, semantic-mapped set
of operator and punctuation tokens, one fixed precedence ladder with no user
fixity, and the concrete assignment of C015's continuation capabilities and
delimiter frames — and deliver them through the first whole-source tokenizer
plus a bounded operator-expression layer. Every operator token denotes
something already normative: `+ - *` and the comparisons and equalities carry
their C003/C010 arithmetic and Boolean meanings, prefix `-` carries C018
negation, and `-> |> . , ; ( ) [ ] { }` are structural. Spellings with no
owner — `/ % ^ << >> & ~ !!= ++ --` and every other symbol sequence — are
reserved and rejected with a stable diagnostic rather than tokenized
hopefully.

The ladder rejects comparison chains (`a < b < c` is invalid, not
left-grouped), places the pipe `|>` as the loosest binary operator, and
treats `-` as one token with prefix (negation) and binary (subtraction)
roles. Parentheses and brackets open `continued` delimiter frames; braces
open a `block` frame; `,` separates within a frame and `;` remains C015's
hard separator.

This closes G019 without deciding P109 declaration and application grammar,
G020 file structure, G021/G022 name resolution, G040 built-in data beyond
the atoms, or G061 operator dispatch.

## Scope and method

The operational target is independent agreement on token spellings and
boundaries, the capability and frame assignments C015 requires, the
precedence ladder, and the rejection behavior — made executable through a
whole-source token stream and an operator-expression layer over atomic
operands. Primary comparative evidence comes from the official
[Rust expression-precedence reference](../30-sources/rust-project-2026-operator-expressions.md),
the expanded [OCaml manual note](../30-sources/ocaml-5-4-expressions-and-pattern-guards.md),
the expanded [Haskell fixity findings](../30-sources/marlow-2010-haskell-language-report.md),
and the [Erlang/OTP expressions note](../30-sources/erlang-otp-expressions-and-guard-sequences.md).
Source claims stay distinct from Catena proposals below.

## Relation to the current corpus

[C015 layout](../60-specification/whitespace-and-layout/separators-and-line-continuation.md)
defines `join_before`/`join_after` capabilities, `continued` and `block`
delimiter frames with named families, and soft/hard line classification —
then explicitly defers every concrete assignment to this slice. G019 pays
that debt: each token in the inventory carries its two capabilities, and
each opening delimiter names its family and mode.

[C014 identifiers](../60-specification/identifiers/README.md) fix `.` as the
qualification separator between identifier segments. C019 makes `.` a token
only in that role and in no other: it is not field access (G040/P109), not a
float dot (C017 owns `1.0` through maximal munch), and not a range or rest
operator.

[C017 literals](../60-specification/literal-grammar/README.md) fix numeric
and textual atoms including `1.` scanning as integer `1` followed by
punctuation, and C018 fixes numeric meaning including negation as an
elaboration operation awaiting a spelling. C019 supplies that spelling as
the prefix `-` operator and nothing else; patterns remain unsigned.

[C003 conditions](../60-specification/clause-conditions/syntax-and-safety.md)
and the [C010 kernel](../60-specification/formal-semantic-kernel/canonical-kernel-syntax.md)
give every proposed operator a meaning under its internal word name:
`add`, `subtract`, `multiply`, `equal`, `not_equal`, `less`,
`less_equal`, `greater`, `greater_equal`, `and`, `or`, `not`, `negate`.
C019 fixes spellings, grouping, and evaluation structure; it invents no
semantics.

The [conformance vocabulary](../CONFORMANCE-VOCABULARY.md) requires that
unknown or malformed operator input be deterministically invalid — never
silently reinterpreted — and the C013–C018 pattern fixes transactional
rejection with original-byte spans as the failure shape.

## Comparative evidence and inference

### Rust: the fixed ladder that rejects comparison chains

Rust orders its operators in one fixed table with per-level associativity,
treats `-1.0` as negation over a positive literal, evaluates operands left
to right, and marks its entire comparison level "Require parentheses" —
chains are ambiguous and rejected rather than grouped. Catena adopts the
fixed table, the prefix-minus treatment, the left-to-right operand
commitment, and the comparison rejection; it declines Rust's level
contents that have no Catena semantics yet (shifts, bitwise, ranges,
assignment, `?`).

### OCaml: the cost of left-grouped comparisons

OCaml's comparison level is left-associative, so `a = b = c` silently parses
as `(a = b) = c`, comparing a Boolean; its `&&`/`||` are right-associative
where Rust's are left; prefix and infix minus are separate functions; and
most multi-operand forms evaluate in unspecified order. OCaml therefore
demonstrates every wrong-turn option in one language — and its manual's own
`&&`/`||` reductions to `if` show that short-circuit shape is orthogonal to
associativity choice. Catena fixes `&&`/`||` left-associative with the rest
of the ladder and requires parentheses for chains.

### Haskell: extensible fixity purchases silent defaults

Haskell lets any operator be declared `infixl`/`infixr`/`infix` at levels
0–9, defaults undeclared operators to `infixl 9`, and locates operator
precedence in the declaration namespace rather than the token grammar. The
silent default is the cautionary tale: an operator's grouping depends on
declaration-processing state, so the lexer cannot be understood without the
binder. Catena's answer to "fixity declarations or their absence" is a
declared absence: one fixed table, stated normatively, changeable only by a
later revision with its own lifecycle record. Notably, Haskell's own Prelude
declares comparisons non-associative, concurring with Rust.

### Erlang: word operators and target discipline

Erlang's operators are word forms (`div`, `rem`, `andalso`, `orelse`) beside
symbol arithmetic, with strict `and`/`or` distinct from the short-circuit
forms, and it explicitly declines to fix operand order within one operator.
Catena's BEAM-ness does not inherit any of this: symbol spellings match the
C004 behavior-first vocabulary evidence, and C010's strict left-to-right
dynamics already fix operand order more strongly than the target requires.

## Selected model

### Token inventory

The 0.1.15 operator and punctuation tokens, with maximal-munch spelling:

| Class | Tokens |
| --- | --- |
| Arithmetic | `+` `-` `*` |
| Comparison | `<` `<=` `>` `>=` |
| Equality | `==` `!=` |
| Boolean | `!` `&&` `\|\|` |
| Structural | `->` `\|>` |
| Delimiters | `(` `)` `[` `]` `{` `}` |
| Separators | `,` `;` `.` |

Every token is ASCII, and munching is defined against the inventory: at
each position the lexer takes the longest inventory spelling that matches,
so `!=` is one token, `!!` is two `!` tokens (no `!!` entry exists), and a
position matching no inventory entry — `/`, `%`, `^`, a lone `=`, `&`, `~`,
`..`, `:=`, `<-`, `=>`, or any Unicode symbol scalar — is a reserved or
invalid spelling rejected with the operator diagnostic family, never
tokenized into pieces that would change meaning.

### Boundaries against the atoms

Maximal munch resolves every adjacency: `1.0e3` is one C017 float; `1.` is
integer `1` then `.`; `x.y.z` is one C014 qualified name while qualified
names are being read and `.` between a name and something else is the
separator token awaiting its G021 resolution meaning; `a-1` is three tokens
exactly like `a - 1` and `a -1` — spacing never changes the token sequence,
honoring C015's whitespace non-semantics. A `-` or `!` immediately before a
literal is still two tokens; negation is the prefix operator applying C018
elaboration.

### Precedence ladder

One fixed table, tightest to loosest, with per-level associativity:

| Level | Operators | Associativity |
| --- | --- | --- |
| 1 | atomic operands, groupings | — |
| 2 | prefix `-` `!` | applies to level 2 or above (right-recursive) |
| 3 | `*` | left |
| 4 | `+` `-` (binary) | left |
| 5 | `<` `<=` `>` `>=` | none — chaining invalid |
| 6 | `==` `!=` | none — chaining invalid |
| 7 | `&&` | left |
| 8 | `\|\|` | left |
| 9 | `\|>` | left |

Mixed comparison and equality without parentheses (`a < b == c`) is invalid
for the same chaining reason. `->` is tokenized but reserved for P109
clause structure; it participates in no 0.1.15 expression rule.

### Capabilities and frames

Binary operators (`* + - < <= > >= == != && || |>`) set both `join_before`
and `join_after`; prefix `-` and `!` set `join_after` only; `)` `]` `}` set
`join_before` only; `(` `[` `{` `,` `;` `.` set neither. `(` and `[` push
`continued` frames of families `paren` and `bracket`; `{` pushes a `block`
frame of family `brace`; `)`, `]`, `}` close their named families under
C015's innermost-frame rule, surfacing unbalanced delimiters as C015
`LAY002` diagnostics through the token stream rather than a new mechanism.

### Token stream and expression layer

A conforming implementation exposes a whole-source tokenizer over C013
source producing the lossless, ordered stream of C014–C018 atom tokens and
operator/punctuation tokens with original-byte spans, trivia retained, and
one operator-expression parser over atomic operands resolving the ladder to
a tree or exactly one diagnostic. Neither component type-checks, resolves
names, elaborates declarations, or lowers to BEAM: those remain P109 and
later slices.

### Rejection

Failures are transactional with stable identifiers: unknown or reserved
spellings, unbalanced or mismatched delimiters (via C015), capabilities
interrupted by hard separators (C015 `LAY003`), and precedence-invalid
forms such as comparison chains. No partial tree or recovered stream is
published; editor resynchronization stays G123 and formatter tolerance
G118.

## Rejected alternatives

- **User fixity declarations (Haskell/OCaml):** couples tokenization to
  declaration state and imports the silent-default failure mode; G019
  answers the checklist by declaring fixity's absence.
- **Left-associative comparisons (OCaml):** silently changes `a == b == c`
  into Boolean comparison; two of three primary sources reject chains.
- **Tokenizing unowned spellings `/ % ^ ++`:** fixes form before meaning —
  the C018 lesson — and would let a later semantics slice become a breaking
  change; reserved-and-rejected keeps every later admission a compatible
  addition.
- **Field-access or namespace `:`/`::` tokens:** field selection is G040
  data-model work and module separators await G021's namespace decisions.
- **Negative-literal folding:** reopens C017 token boundaries and C018's
  signed-literal analysis for no benefit; `-` stays an operator.
- **Error recovery with synchronization points:** partial outputs violate
  the transactional pattern and serve no current consumer.

## What C019 adds to the design

For the first time a whole Catena source file has one deterministic token
stream: names, comments, layout, literals, numeric meanings, and now
operators compose. The formatter (G118), editor protocol (G123), P109
declaration grammar, and G020 file structure all consume this contract
instead of inventing local conventions, and the C015 layout engine receives
its long-promised concrete capabilities, making multiline argument lists and
newline-separated blocks observable rather than hypothetical.

## Remaining questions and falsification criteria

P109 must fix application, grouping-of-declarations, and clause structure
that consume `->`; G020 must relate token streams to files and modules;
G021/G022 must give `.`-separated qualified names their resolution meaning;
G040 must decide whether field-like access reuses `.`; G061 must decide
whether operators become trait-dispatched; G066 must confirm that no
operator resolution depends on inferred types; G123 owns editor recovery.

The ladder should be revisited if P109's grammar forces a different `->`
binding, if G061 dispatch needs a distinct operator class boundary, or if
usability studies show the comparison-chain rejection materially harms real
code. Convenience alone does not add an operator to a closed table.

## Connections

- The [resolved operator inquiry](../40-inquiries/how-should-catena-fix-operators-and-punctuation.md)
  records the operational question and evidence trail.
- The [Operators and Punctuation map](../10-maps/operators-and-punctuation.md)
  routes through evidence, constraints, and remaining owners.
- The [Operators and Punctuation Specification](../60-specification/operators-and-punctuation/README.md)
  defines the normative 0.1.15 contract.
- The [C019 evidence record](../50-journal/2026-08-21-c019-operators-and-punctuation.md)
  records the sibling implementation and verification.
- [Catena Whitespace, Layout, and Line Continuation](catena-whitespace-layout-and-line-continuation.md)
  defines the capability and frame contracts this slice populates.
- [Catena Numeric Literal Semantics](catena-numeric-literal-semantics.md)
  fixes the negation meaning the prefix `-` spelling now carries.

## Sources

- [The Rust Reference: Operator Expressions and Precedence](../30-sources/rust-project-2026-operator-expressions.md)
- [OCaml 5.4 Expressions and Pattern-Matching Guards](../30-sources/ocaml-5-4-expressions-and-pattern-guards.md)
- [Haskell 2010 Language Report](../30-sources/marlow-2010-haskell-language-report.md)
- [Erlang/OTP Expressions and Guard Sequences](../30-sources/erlang-otp-expressions-and-guard-sequences.md)
