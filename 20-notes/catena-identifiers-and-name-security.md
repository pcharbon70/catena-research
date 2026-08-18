---
title: "Catena Identifiers and Name Security"
kind: note
created: "2026-08-17"
maturity: developing
tags:
  - identifiers
  - language-design
  - security
  - unicode
aliases:
  - "C014 identifier synthesis"
---

# Catena Identifiers and Name Security

## Executive conclusion

Catena 0.1.10 should make international names ordinary without letting a host
Unicode library silently define the language. The bounded design pins Unicode
17, admits `XID_Start XID_Continue*`, requires the UTS #39 General Security
Profile and Highly Restrictive script level, requires source spelling already
in NFC, treats case as significant but semantically role-neutral, and reports
confusable skeleton collisions as deny-able warnings.

Qualification is lexical only: nonempty identifier segments join with ASCII
`.` and no whitespace. Name resolution, namespaces, shadowing, imports, and
exports remain G021/G022. The sibling compiler can therefore provide useful
executable evidence without inventing the missing whole-source lexer.

## Scope and operational standard

G014 is complete when independent implementations can agree, for any finite
standalone candidate name, on:

- whether each segment is a permitted identifier;
- its exact canonical identity and case relationship;
- whether its spelling satisfies the normalization and script policies;
- whether a spelling is a keyword or an escaped identifier;
- how qualification divides it into segments; and
- whether two distinct names in one supplied comparison domain deserve the
  same confusable warning.

This standard does not require implementations to know what a name denotes.
That separation prevents lexical policy from prematurely fixing the namespace
and module system.

## Relation to the current corpus

[C013 source text](../60-specification/source-text/README.md) already produces
a strict Unicode scalar stream with original-byte spans and deliberately
preserves composed and decomposed spellings. C014 consumes that stream and
applies normalization only to identifier segments. Comments, literals, and
other future tokens remain unchanged.

The current data, pattern, condition, and effect chapters use names such as
`Option.Some`, `Rules.positive`, and `console.ask`. Those examples establish
ASCII dot as the least-surprising qualification separator, but they do not yet
define resolution. Retained JSON and the exact 0.1.8 kernel use intentionally
narrow ASCII name grammars; changing them would alter existing protocols rather
than implement ergonomic source identifiers.

## Repertoire and versioning

[UAX #31](../30-sources/davis-leroy-2025-unicode-identifiers-syntax.md)
provides `XID_Start` and `XID_Continue`, designed for stable language
identifiers and normalization closure. Catena adds no initial underscore:
underscore remains available after the first scalar, and the single `_`
spelling remains free for pattern work. Digits likewise continue but do not
start a name.

Property-based acceptance must be versioned. Following a host library would
make the same Catena revision accept different programs under different OTP or
ICU releases. Version 0.1.10 therefore pins Unicode 17 property, normalization,
script, and confusable data. A future Unicode update is a visible language
revision even when XID growth is backward compatible, because security status
and confusable data can change.

## Normalization and equality

Names are case-sensitive exact scalar strings after the validity checks.
Because source must already be NFC, identity never needs a hidden normalized
key: the displayed segment, linker spelling, and compiler identity agree.
`é` is valid while `e` plus combining acute is rejected when NFC would compose
it. The diagnostic supplies the exact NFC source edit over the original-byte
span.

This selects filtered normalized identifiers under UAX31-R6 rather than the
equivalent-normalized R4 path preferred by
[UTS #55](../30-sources/leroy-davis-2024-unicode-source-code-handling.md).
The tradeoff is deliberate. R4 is friendlier to input methods, but accepting
two spellings while retaining exact source locations creates separate display
and comparison forms at the first lexical milestone. R6 keeps the model
auditable; the mandatory repair fix carries the usability burden explicitly.

Compatibility normalization is rejected. NFKC would erase distinctions such
as mathematical presentation forms and compatibility characters more broadly
than a case-sensitive language needs. The General Security Profile already
excludes risky compatibility and technical characters from ordinary names.

## Case and semantic roles

Capitalization conventions may remain helpful style, but case cannot select
the value, type, constructor, trait, effect, handler, or module namespace.
Uncased scripts cannot express an upper/lower distinction, and UTS #55 warns
against making case the sole carrier of semantics. Declaration and use syntax
therefore determine role. `value` and `Value` remain distinct identifiers in
the same comparison domain; neither spelling inherently denotes a particular
kind of entity.

This differs from current JSON/kernel regular expressions that use ASCII case
as a structural protocol discriminator. Those exact formats remain unchanged;
later ergonomic parsing elaborates context-classified names into the existing
semantic roles.

## Security is layered

[UTS #39](../30-sources/davis-suignard-2025-unicode-security-mechanisms.md)
supplies three different controls, and they should retain different effects:

1. Intersect XID with `Identifier_Status=Allowed`. A restricted scalar makes
   the segment invalid.
2. Require the Highly Restrictive script level per segment. A disallowed mix,
   such as Latin plus Cyrillic, is invalid, while single-script names and the
   listed Latin/Japanese, Latin/Korean, and Latin/Bopomofo combinations remain
   available.
3. Compute a pinned internal confusable skeleton for otherwise-valid names.
   Equal skeletons for distinct canonical names produce a warning, not name
   equality or automatic rejection.

The final distinction matters. False positives and legitimate whole-script
similarity make unconditional rejection too strong. Conversely, silently
ignoring a collision defeats review. A stable warning that existing project
policy can promote gives closed default behavior and a strict deployment path.

The compiler cannot infer lexical scopes before G021. Its audit API therefore
accepts an explicit comparison domain and returns warnings in input order.
Later name resolution supplies actual domains without changing the skeleton
algorithm or diagnostic identity.

## Keywords and escapes

Version 0.1.10 freezes the words already established by the corpus:
`as`, `condition`, `derives`, `effect`, `exists`, `false`, `fn`, `forall`,
`handle`, `handler`, `import`, `let`, `match`, `or`, `request`, `resume`,
`returns`, `true`, `type`, `uses`, `when`, `where`, and `with`.

They are hard keywords rather than contextual parser guesses. A backtick pair
turns one otherwise-valid segment into an identifier, so `` `type` `` has the
canonical identity `type`. Backticks add no arbitrary character escape and do
not bypass NFC, XID, security, or script rules. Escaping an ordinary nonkeyword
is valid and has the same identity, allowing generators to use one safe rule.

Future revisions may add keywords without permanently making the spelling
unnameable. Such additions remain visible source-acceptance changes, while the
escape supplies a local migration.

## Qualification boundary

A qualified name is `segment ("." segment)*`. Empty segments, leading or
trailing dots, repeated dots, and whitespace around the dot are invalid in the
standalone form. Each segment is independently normalized and security-
checked; escapes apply per segment.

The dot is not part of identifier identity. The sequence of segment identities
is the qualified identity, and the confusable key joins their individual
skeletons with the same separator. G019 still decides how dot interacts with
other punctuation in a complete token stream. G021 and G022 decide which
prefixes name modules, which namespaces are searched, and how qualification
affects ambiguity.

## Alternatives rejected

- **ASCII-only identifiers** are simple but contradict the Unicode source
  foundation and exclude ordinary names in most writing systems.
- **Unrestricted XID** leaves invisible, uncommon, and deceptive characters
  available without a language-level security baseline.
- **Capitalization-defined roles** preserves familiar examples but prevents
  uncased scripts from expressing all language entities.
- **Exact decomposed/composed distinction** violates canonical-equivalence
  expectations and creates visually identical distinct names.
- **Silent normalization** separates source spelling from binding identity and
  complicates exact diagnostics and generated symbols.
- **Confusable collisions as errors** overstates a heuristic; warnings with
  policy promotion preserve review control.
- **Whole-source scanning in C014** would have guessed the then-unresolved
  whitespace, comment, literal, and operator boundaries in G015–G019.

## Falsification and follow-up

The design should be revisited if NFC rejection proves materially hostile to
ordinary input even with automatic fixes, if the General Security Profile
excludes modern identifiers Catena users need, or if warning volume makes the
confusable signal unusable. Such evidence should name concrete scripts,
spelling workflows, and collision sets rather than assume all Unicode policy
has one usability/security point.

C015 now supplies the abstract whitespace/layout event boundary, and C016 adds
comments without changing identifier identity. G017–G020 must integrate these
standalone names into a real lexer and file grammar.
G021/G022 must supply comparison domains and resolution. P117 must
carry secondary spans and cross-file collision explanations; G118 must define
safe display and formatting. None may weaken the pinned 0.1.10 identity rules
silently.

## Connections

- [Identifier and Name Security map](../10-maps/identifier-and-name-security.md)
  provides the conceptual route.
- [Resolved identifier inquiry](../40-inquiries/how-should-catena-define-and-secure-identifiers.md)
  records the bounded decision.
- [Identifier Specification](../60-specification/identifiers/README.md) defines
  the normative rules and conformance obligations.
- [C014 evidence record](../50-journal/2026-08-17-c014-identifiers-and-name-security.md)
  preserves the executable method and result.

## Sources

The design combines [UAX #31 identifier syntax](../30-sources/davis-leroy-2025-unicode-identifiers-syntax.md),
[UTS #39 security mechanisms](../30-sources/davis-suignard-2025-unicode-security-mechanisms.md),
[UTS #55 source-code guidance](../30-sources/leroy-davis-2024-unicode-source-code-handling.md),
and the existing [UAX #15 normalization note](../30-sources/whistler-2025-unicode-normalization-forms.md).
