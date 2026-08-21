---
title: "C013 Source-Text Encoding and Normalization"
kind: journal
created: "2026-08-17"
tags:
  - conformance
  - parsing
  - specification
  - testing
  - unicode
aliases:
  - "C013 source-text evidence"
---

# C013 Source-Text Encoding and Normalization

## Observations

Checklist item G013 is complete as C013 and normative language revision
`0.1.9`. The [Source Text Specification](../60-specification/source-text/README.md)
defines strict UTF-8, leading-BOM rejection, LF/CRLF logical newlines, lone-CR
rejection, no whole-file Unicode normalization, and original-byte scalar
locations.

The decision was developed in the
[synthesis](../20-notes/catena-source-text-encoding-and-normalization.md) and
[resolved inquiry](../40-inquiries/how-should-catena-decode-and-normalize-source-text.md).
The [topic map](../10-maps/source-text-encoding-and-normalization.md) routes
through the Unicode 17, RFC 3629, and UAX #15 primary evidence.

The bounded result is intentionally pre-lexical. Passing the source envelope
does not establish that an input contains an identifier, token, declaration,
or module. G014 through G020 retain those decisions, while P117 and G118 retain
the complete diagnostic and formatter contracts.

## Compiler evidence

The coordinated sibling-compiler implementation targets the `rewrite` branch
and adds:

- `Catena.SourceText` and scalar/span source units;
- `Catena.decode_source_text/2` with exact 0.1.9 selection;
- a single-pass strict UTF-8 decoder that preserves original bytes and emits
  LF-normalized logical text;
- `SRC001`, `SRC002`, and `SRC003` with original-byte spans and stable reasons;
- `catena check-source-text` with deterministic counts and no output files;
- explicit JSON, kernel, source-text, compilation, and interface revision sets
  so 0.1.9 cannot leak into persisted artifacts; and
- tagged `ST-OBL-001` through `ST-OBL-010` tests plus a complete coverage gate.

The source decoder accepts valid two-, three-, and four-byte scalars,
unassigned values, noncharacters, combining marks, embedded U+FEFF, U+FFFD,
mixed LF/CRLF, and empty input. It rejects overlong encodings, encoded
surrogates, out-of-range values, isolated continuations, truncated sequences,
UTF-16/UTF-32 signatures, leading UTF-8 BOM, and lone CR.

The implementation is published at immutable compiler commit
[`d4e8e5c0ad41f47ebe86d59047cdabe017762f38`](https://github.com/pcharbon70/catena/commit/d4e8e5c0ad41f47ebe86d59047cdabe017762f38)
on draft compiler PR [#89](https://github.com/pcharbon70/catena/pull/89), from
`agent/c013-source-text` into `rewrite`. The commit contains exactly the tree
for which the compiler verification below passed.

## Evidence

The complete compiler verification sequence passed in the final working tree:

```text
mix format --check-formatted        passed
mix clean                           passed
mix compile --warnings-as-errors    passed; 67 files compiled
mix test                            passed; 188 tests, 0 failures
mix escript.build                   passed
git diff --check                    passed
```

The research archive verification sequence also passed:

```text
python3 -m unittest -v test_validate_archive.py
                                      passed; 26 tests, 0 failures
python3 validate_archive.py            passed; 239 documents, 20 directories,
                                      2,313 local links, 99 source notes,
                                      58 specification chapters, 65 fenced
                                      blocks, and 340 obligations checked
git diff --check                       passed
```

The obligation total comprises 242 traced, 77 partial, and 21 untraced rows;
all ten `ST-OBL-*` rows are traced. The Unicode 17 chapter, UAX #15 Revision
57, and RFC 3629 metadata and cited claims were checked against their official
primary publications on 2026-08-17.

## Result

C013 consumes language revision `0.1.9` because it changes which source byte
sequences are accepted and exposes a new stable source-text frontend and
diagnostic family. It does not change the compiler package release, JSON AST
formats, exact 0.1.8 kernel, interfaces, signature domains, typed core, runtime
semantics, or BEAM representation.

The compiler can now validate and position future Catena source without
pretending that the full grammar exists. This gives G014–G020 one shared,
versioned character stream and prevents later lexer work from silently
choosing host-dependent decoding, normalization, or columns.

## Threads

- C014 now fixes the identifier repertoire, case, qualification, confusable,
  and identifier-specific normalization rules on top of C013.
- C015 now classifies whitespace and layout without changing C013 newline
  formation; C016 now preserves comment-owned newlines through that classifier.
- C017 now defines atomic literals and their context-specific scalar
  restrictions; G019 retains operators and punctuation, and C018 has since
  fixed numeric meaning.
- G020 must define file/module relations and any source header carrying exact
  selection.
- P117 and G118 must project original scalar spans into complete diagnostics,
  formatter trees, edits, and display locations.

## Follow-ups

Merge compiler PR [#89](https://github.com/pcharbon70/catena/pull/89) before
the research promotion PR so the executable evidence lands before the corpus
claims it on `main`. The immutable implementation commit remains the evidence
identity even if GitHub records a distinct merge commit.
