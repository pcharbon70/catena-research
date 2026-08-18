---
title: "Catena Comments and Documentation Comments"
kind: note
created: "2026-08-18"
maturity: developing
tags:
  - catena
  - comments
  - documentation
  - language-design
  - syntax
aliases:
  - "Catena comment model"
---

# Catena Comments and Documentation Comments

## Executive conclusion

Catena should use the familiar slash family: `//` line comments, nestable
`/* ... */` block comments, and the outer documentation forms `///` and
`/** ... */`. Ordinary comments are lexical trivia, but they are not allowed
to erase source structure: a line comment leaves its terminating C013 logical
LF outside the comment, and every logical LF inside a block comment is passed
through C015's layout classifier.

Documentation is declaration metadata rather than an alternate ordinary
comment. Adjacent outer documentation comments combine and attach only to the
next parser-supplied documentable declaration. Their normalized body is
CommonMark 0.31.2 source. Raw HTML is preserved for faithful tools but cannot
be executed unsanitized; only the exact trimmed fence info string `catena
doctest` opts into a future runner.

## Relation to the current corpus

[C013 source text](../60-specification/source-text/README.md) already owns byte
decoding, LF/CRLF normalization, scalar preservation, and original-byte spans.
Comment scanning consumes that logical-unit stream, so it neither recognizes
physical CR independently nor performs Unicode normalization or escape
processing.

[C015 layout](../60-specification/whitespace-and-layout/README.md) already owns
the `soft`, `separator`, and `blank` classification of logical LF. C016 closes
the ownership question deferred by `LY-OBL-011`: comments are transparent
trivia for token adjacency, while their logical LFs appear at their exact
source positions in the same classifier. This retains multi-line block
comments without treating them as opaque horizontal spaces.

[C014 identifiers](../60-specification/identifiers/README.md) and G019's future
token grammar determine when `/`, `*`, or another scalar is already inside a
different token. C016 therefore defines a scanner invoked only at a
lexer-supplied outside-token position; it does not make `/` a complete
whole-source token or settle operator precedence.

The broader corpus distinguishes user-facing API contracts from internal
notes, but it had not fixed a documentation carrier. C016 makes that
distinction concrete without choosing module/file ownership (G020), complete
declaration grammar (P109), generated documentation format, symbol-link syntax,
or the future doctest execution environment (G119).

## Evidence comparison

### Rust: precise lexical edges and forward documentation

The [Rust comments reference](../30-sources/rust-project-2026-rust-comments.md)
defines the same basic slash family, nested block balancing, and carefully
distinguishes `///` and `/** ... */` from `////`, `/***`, and `/**/`. Those edge
rules avoid maximal-prefix disagreement between implementations.

Rust also provides inner `//!` and `/*! ... */` documentation. Catena rejects
that second attachment direction. A single forward rule is easier to audit,
keeps documentation independent of file/module ownership, and makes a missing
target a stable source error rather than contextual reinterpretation.

### Swift: nested blocks as editing support

The [Swift lexical structure](../30-sources/swift-project-2026-lexical-structure.md)
independently shows the editing value of nested multiline comments: a region
can be commented out even when it already contains block comments. Catena
adopts balanced nesting for every `/*` found inside a block comment. The
outermost opener alone selects ordinary versus documentation classification;
nested documentation-looking openers do not split or reclassify the outer
comment.

### ECMAScript: line boundaries cannot disappear

The [ECMAScript comment rules](../30-sources/ecma-international-2026-ecmascript-comments.md)
keep a line comment's terminating line break as a separate lexical input and
make a multiline comment containing a line break visible to parsing. Catena
uses the first rule directly and strengthens the second: it preserves every
logical LF individually, including consecutive blank lines and original-byte
spans, then delegates their meaning to C015.

### Elixir: documentation and comments have different jobs

The [Elixir documentation guide](../30-sources/elixir-project-2026-writing-documentation.md)
treats documentation as API metadata, ordinary comments as source-maintainer
material, Markdown as document content, and doctests as an explicit testing
feature. Catena adopts those separations but uses documentation-comment
attachment rather than module attributes. It also makes execution opt-in at
the fenced block rather than treating all examples or prompts as executable.

### CommonMark: pin syntax and add a separate trust policy

The [CommonMark 0.31.2 specification](../30-sources/macfarlane-2024-commonmark-specification.md)
gives documentation a stable parsing profile and treats fenced info strings as
metadata rather than execution instructions. Its raw HTML behavior requires a
separate safety rule: source preservation is useful, but a documentation
renderer must sanitize or escape before output reaches an executable HTML
context.

## Selected lexical model

A line comment starts with `//` and stops immediately before logical LF or at
EOF. `///` is documentation only when the opener contains exactly three
slashes; `////` begins an ordinary line comment. A block comment starts with
`/*`, every nested `/*` increments a balance depth, and every `*/` decrements
it. EOF at nonzero depth is invalid.

`/**` selects documentation only when it is not followed by `*` or `/`.
Consequently `/** text */` is documentation, while `/***` and the empty `/**/`
are ordinary. `//!` and `/*!` have no special status. Comment contents admit
every scalar already accepted by C013, including comment-like Unicode text;
there are no comment escapes or normalization transformations.

The nesting depth is not a language-level numeric limit. An implementation
can scan it iteratively, and any resource refusal remains governed by the
cross-cutting implementation-limit policy rather than a semantic nesting
maximum.

## Layout integration

Removing a comment from the significant token stream does not concatenate
forms across its line boundaries. For layout purposes, the comment contributes
its logical LF events in source order at the comment's position. A block
comment with three logical LFs therefore contributes three classifiable events,
not one synthetic newline. A line comment contributes none internally and
leaves its terminator for the surrounding stream.

This model makes comment removal predictable:

- a same-line block comment behaves as horizontal trivia;
- a block-comment LF can be soft after an incomplete token or within a
  continued frame;
- a block-comment LF can be a hard separator after a complete token; and
- repeated internal LFs retain blank-line structure.

The result is lossless enough for diagnostics and future concrete-syntax
tools: original units, normalized documentation body units, complete comment
span, and classified line-break records remain distinguishable.

## Documentation attachment and normalization

Documentation attaches only to the next documentable declaration marker
supplied by the parser. Horizontal whitespace and exactly one logical LF can
separate the documentation group from that target. Adjacent documentation
comments form one group and their bodies join with one logical LF. A blank
line, ordinary comment, semicolon, significant token, non-documentable
construct, missing required LF, or EOF breaks attachment and is invalid as
`DOC001`.

Line documentation drops its three-slash delimiter and one optional immediately
following ASCII space. Block documentation drops its delimiters, one optional
adjacent ASCII space at each edge, whitespace-only edge lines, and the longest
common exact SPACE/TAB margin across nonblank lines. Remaining scalars and
spans are preserved. In particular, a decorative leading `*` is content, not
an implicit margin marker.

## Markdown, HTML, and doctests

The normalized body carries the profile label `commonmark-0.31.2`. This fixes
parsing but does not require C016's compiler boundary to render HTML. Raw HTML
remains in the source body so non-HTML tools do not lose content. Any renderer
that produces an executable environment must sanitize or escape it; direct
unsanitized execution is never conforming.

Fenced code is ordinary documentation unless the fence's trimmed info string
is exactly `catena doctest`. Labels such as `catena`, `doctest`, `Catena
doctest`, or `catena doctest extra` do not opt in. C016 records that policy but
does not execute examples. G119 still owns runner selection, effects,
isolation, expected-output syntax, budgets, failure reporting, and build
integration.

## Rejected alternatives

- **Non-nesting block comments** make region commenting fragile and add no
  useful language property.
- **Erasing all comment-internal newlines** silently changes C015 separation
  and loses blank-line/source-span evidence.
- **Collapsing a multiline comment to one synthetic LF** is less lossless and
  can change hard/blank classification.
- **Inner documentation comments** couple C016 to unresolved enclosing-file
  and module ownership.
- **Attaching across blank lines or ordinary comments** hides accidental stale
  documentation and makes formatter edits change metadata targets subtly.
- **Unversioned Markdown** makes rendering behavior drift with tooling.
- **Executing every Catena-looking fence** turns explanatory fragments into
  ambient code execution and prevents examples that are intentionally partial.

## Connections

- [Resolved comments inquiry](../40-inquiries/how-should-catena-handle-comments-and-documentation-comments.md)
  records the operational decision.
- [Comments and Documentation Comments map](../10-maps/comments-and-documentation-comments.md)
  routes through the evidence and normative result.
- [Comments and Documentation Comments Specification](../60-specification/comments-and-documentation-comments/README.md)
  defines the normative 0.1.12 contract.
- [C016 evidence record](../50-journal/2026-08-18-c016-comments-and-documentation-comments.md)
  records the sibling implementation and verification.

## Sources

- [Rust Comments](../30-sources/rust-project-2026-rust-comments.md)
- [Swift Lexical Structure](../30-sources/swift-project-2026-lexical-structure.md)
- [ECMAScript Comments](../30-sources/ecma-international-2026-ecmascript-comments.md)
- [Elixir Writing Documentation](../30-sources/elixir-project-2026-writing-documentation.md)
- [CommonMark 0.31.2](../30-sources/macfarlane-2024-commonmark-specification.md)
