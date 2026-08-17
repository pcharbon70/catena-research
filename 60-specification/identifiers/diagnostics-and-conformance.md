---
title: "Identifier Diagnostics and Conformance"
kind: specification
created: "2026-08-17"
status: normative
spec_version: "0.1.10"
tags:
  - conformance
  - diagnostics
  - identifiers
  - specification
  - testing
aliases:
  - "Catena 0.1.10 identifier conformance"
---

# Identifier Diagnostics and Conformance

## Status and authority

This chapter is the normative Catena 0.1.10 identifier diagnostic, public
frontend, and conformance contract. It is governed by
[Specification Authority](../../SPECIFICATION-AUTHORITY.md),
[Catena Conformance Vocabulary](../../CONFORMANCE-VOCABULARY.md), and
[Catena Implementation Limits and Portability](../../IMPLEMENTATION-LIMITS.md).
It applies the rules in
[Identifier Syntax and Equivalence](identifier-syntax-and-equivalence.md) and
[Qualification, Keywords, and Identifier Security](qualification-keywords-and-security.md).

## Stable diagnostics

| ID | Required meaning |
| --- | --- |
| `IDN001` | empty identifier, invalid XID start, invalid XID continuation, or malformed audit input |
| `IDN002` | identifier content is not NFC, with exact NFC replacement and source-edit fix |
| `IDN003` | a scalar is outside the pinned General Security Profile |
| `IDN004` | a segment fails the pinned Highly Restrictive script level |
| `IDN005` | unescaped reserved word or malformed backtick escape |
| `IDN006` | empty or malformed qualification, or a qualified path passed where one segment is required |
| `IDN007` | distinct canonical names in one supplied domain have the same pinned confusable skeleton |

Every rejection MUST identify the stable ID and primary original-byte span
(`ID-OBL-011`). `IDN002` MUST carry normalization `NFC`, the replacement text,
and one machine-applicable source edit over the identifier content. `IDN007`
MUST carry both canonical names, the skeleton, Unicode version `17.0.0`, and
warning or promoted-error severity.

Diagnostic prose and map-key presentation may improve only within the bounded
rules of the repository conformance vocabulary. Stable ID, severity class,
source span, meaning-bearing details, fix applicability, acceptance, and
canonical identity do not vary.

## Public library boundary

A conforming implementation exposes equivalent operations for:

- validating one identifier segment;
- validating one standalone qualified name; and
- validating an ordered nonempty comparison domain and returning its
  confusable warnings.

The bootstrap evidence names these operations `Catena.parse_identifier/2`,
`Catena.parse_qualified_name/2`, and `Catena.audit_identifiers/2`. Those Elixir
names are evidence API names, not required names for every implementation.

A successful identifier result includes original spelling, canonical
identity, escape state, original-byte span, participating scripts, confusable
skeleton, and exact language selection. A successful qualified result includes
the ordered segment results and their dot-joined canonical and skeleton forms.
The audit MUST stop on the first invalid name before producing a successful
domain result.

## Command-line boundary

The bootstrap command `catena check-identifiers NAME...` accepts one or more
arguments as one comparison domain. On success it writes deterministic JSON
containing status, edition, revision, Unicode version, ordered canonical name
results, segment metadata, and ordered diagnostics (`ID-OBL-012`). It writes no
interface, BEAM file, or other language artifact.

The command MUST accept the common language-selection options and repeatable
diagnostic-denial option. Invalidity or promoted `IDN007` produces a nonzero
failure and one structured diagnostic. Repeating the same command with the
same inputs and implementation produces byte-identical JSON.

## Conformance obligations

| ID | Obligation | Required executable evidence |
| --- | --- | --- |
| `ID-OBL-001` | Unicode 17 data and revision are pinned | table manifest/hashes and revision tests |
| `ID-OBL-002` | exact XID start and continuation production | multilingual positive and boundary-negative tests |
| `ID-OBL-003` | case-sensitive, role-neutral identity | case-pair and uncased-script tests |
| `ID-OBL-004` | filtered NFC with no silent normalization | full Unicode 17 normalization corpus and replacement tests |
| `ID-OBL-005` | General Security Profile filter | restricted-character tests |
| `ID-OBL-006` | Highly Restrictive segment scripts | single/permitted-combination and unsafe-mix tests |
| `ID-OBL-007` | complete closed keyword set | every bare word rejected |
| `ID-OBL-008` | valid backtick escapes preserve identity | keyword, redundant, and malformed-escape tests |
| `ID-OBL-009` | dot qualification and segment validation | positive, empty, repeated, trailing, and whitespace tests |
| `ID-OBL-010` | deterministic confusable warning and promotion | collision, noncollision, duplicate, and denial tests |
| `ID-OBL-011` | original-byte spans and exact fixes | multibyte and decomposed spelling tests |
| `ID-OBL-012` | deterministic public CLI | repeated command/result tests |
| `ID-OBL-013` | source-only persistence and version separation | frontend and forged-format tests |

Every obligation MUST have at least one tagged passing test, and the sibling
compiler MUST gate the complete `ID-OBL-*` set against unknown and uncovered
identifiers before C014 conformance is claimed.

## Required evidence sets

Positive evidence includes ASCII, Latin combining forms, Greek, Cyrillic, Han,
Devanagari, and permitted East Asian script combinations. Negative evidence
includes empty names, initial underscore and digit, punctuation, whitespace,
non-NFC spelling, restricted/default-ignorable scalars, unsafe script mixing,
keywords, malformed escapes, and malformed qualification.

Normalization evidence MUST execute the Unicode 17 `NormalizationTest.txt`
NFC invariants against the same implementation used by identifier validation.
The implementation's Unicode table MUST record the canonical source URLs and
SHA-256 hashes from which its runtime data were produced.

The exact JSON and kernel name grammars MUST remain unchanged. Tests MUST show
that `0.1.10` is absent from compilable, interface, artifact, and signed-format
revision sets (`ID-OBL-013`).

## Rationale and evidence (non-normative)

The design route is preserved in the
[identifier synthesis](../../20-notes/catena-identifiers-and-name-security.md),
[resolved inquiry](../../40-inquiries/how-should-catena-define-and-secure-identifiers.md),
and [topic map](../../10-maps/identifier-and-name-security.md). The
[C014 record](../../50-journal/2026-08-17-c014-identifiers-and-name-security.md)
records the concrete sibling-compiler commands and archive validation.
