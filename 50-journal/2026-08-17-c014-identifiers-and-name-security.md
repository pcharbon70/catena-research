---
title: "C014 Identifiers and Name Security"
kind: journal
created: "2026-08-17"
tags:
  - conformance
  - identifiers
  - security
  - specification
  - testing
  - unicode
aliases:
  - "C014 identifier evidence"
---

# C014 Identifiers and Name Security

## Observations

Checklist item G014 is complete as C014 and normative source-only language
revision `0.1.10`. The [Identifier Specification](../60-specification/identifiers/README.md)
pins Unicode 17 XID, filtered NFC, role-neutral case, the General Security
Profile, Highly Restrictive scripts, a closed keyword set with backtick
escapes, ASCII-dot qualification, and deny-able confusable warnings.

The decision was developed in the
[synthesis](../20-notes/catena-identifiers-and-name-security.md) and
[resolved inquiry](../40-inquiries/how-should-catena-define-and-secure-identifiers.md).
The [topic map](../10-maps/identifier-and-name-security.md) routes through UAX
#31 Revision 43, UTS #39 Revision 32, UTS #55 Revision 5, and the prior UAX #15
normalization evidence.

The result remains deliberately pre-lexer. It validates standalone names and
caller-supplied comparison domains without guessing whitespace, comments,
literals, operators, scopes, imports, or module lookup.

## Compiler evidence

The coordinated sibling-compiler implementation targets the `rewrite` line
from branch `agent/c014-identifiers` and adds:

- vendored Unicode 17 source files with SHA-256 provenance and a compact
  deterministic offline table embedded in the compiler and packaged escript;
- a Unicode normalization implementation checked against the complete Unicode
  17 normalization corpus;
- `Catena.Identifier`, `Catena.QualifiedName`, and identifier-audit operations;
- public parsing and audit facade functions plus `catena check-identifiers`;
- `IDN001`–`IDN007`, original-byte spans, NFC fixes, and warning promotion;
- cumulative source-text selection through 0.1.10 without widening persisted
  or compilable formats; and
- tagged `ID-OBL-001` through `ID-OBL-013` tests plus a complete coverage gate.

The implementation accepts ASCII and secure multilingual names, including
uncased scripts and the prescribed East Asian combinations. It rejects invalid
XID positions, decomposed NFC alternatives, restricted/default-ignorable
characters, unsafe script mixtures, unescaped keywords, malformed escapes,
and malformed qualification. Distinct same-skeleton names receive one ordered
warning; exact duplicates do not.

No immutable compiler commit or pull request is recorded yet. Publication can
add those identities without changing the semantic or executable result.

## Evidence

The focused implementation pass completed with:

```text
mix format --check-formatted             passed
mix compile --warnings-as-errors         passed
mix test                                 passed; 199 tests, 0 failures
mix escript.build                        passed
./catena check-identifiers ...           passed; embedded Unicode table loaded
Unicode 17 NormalizationTest.txt NFC     passed; 0 failures
python3 validate_archive.py              passed; 250 documents, 2429 links
python3 -m unittest test_validate_archive.py
                                         passed; 26 tests, 0 failures
git diff --check                         passed in both repositories
```

The packaged-executable check caught and repaired an initial resource-path
assumption: an escript cannot read its archive path as an ordinary `priv`
directory. The compact Unicode table is now a compile-time external resource
embedded in `Catena.UnicodeData`, and a focused test executes the built escript
to protect that boundary.

## Result

C014 consumes `0.1.10` because it changes which standalone ergonomic name
spellings are accepted and exposes a new stable frontend and diagnostic
family. It does not change the compiler package release, retained JSON AST,
exact 0.1.8 kernel, interfaces, signature domains, typed core, runtime
semantics, or BEAM representation.

The compiler and specification now share a reproducible Unicode boundary
instead of relying on ambient OTP property tables. C015 now defines lexical
layout separation against a fixed name production, and G021 can later supply real
comparison domains for the already-defined confusable audit.

## Threads

- C015 supplies abstract layout events, C016 supplies comments, and C017
  supplies atomic literals; G019–G020 must integrate standalone names into
  complete source token and file rules
  without changing identity.
- G021/G022 must define namespaces, scopes, shadowing, lookup, imports, and
  which declarations share a confusable comparison domain.
- P117 and G118 must explain and display cross-file collisions safely.
- A future Unicode update requires an explicit language revision and migration
  review, even where XID growth is backward compatible.

## Follow-ups

Commit and publish the compiler and research branches when requested, then add
the immutable compiler commit and pull-request link to this record and the
completeness checklist before claiming published promotion evidence.
