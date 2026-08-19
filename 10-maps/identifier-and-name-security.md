---
title: "Identifier and Name Security"
kind: map
created: "2026-08-17"
tags:
  - identifiers
  - language-design
  - security
  - unicode
aliases:
  - "C014 identifier map"
---

# Identifier and Name Security

## Scope

This map connects Catena 0.1.10's Unicode repertoire, normalization, case,
keywords, qualification, security profile, confusable diagnostics, executable
evidence, and deliberately deferred namespace and whole-source work.

## Start here

- [Catena Identifiers and Name Security](../20-notes/catena-identifiers-and-name-security.md)
  develops the selected model, alternatives, corpus relationship, and
  falsification criteria.
- [How Should Catena Define and Secure Identifiers?](../40-inquiries/how-should-catena-define-and-secure-identifiers.md)
  records the bounded question and C014 resolution.
- [Identifier Specification](../60-specification/identifiers/README.md) is the
  normative 0.1.10 contract.
- [C014 verification record](../50-journal/2026-08-17-c014-identifiers-and-name-security.md)
  records the pinned data, implementation, and validation evidence.

## Trails

### Repertoire, normalization, and case

[UAX #31 Revision 43](../30-sources/davis-leroy-2025-unicode-identifiers-syntax.md)
provides Unicode 17 XID and filtered normalization. The existing
[UAX #15 note](../30-sources/whistler-2025-unicode-normalization-forms.md)
explains canonical composition and stability. [UTS #55](../30-sources/leroy-davis-2024-unicode-source-code-handling.md)
connects NFC and role-neutral case to programming-language usability.

These sources support the
[identifier syntax and equivalence rules](../60-specification/identifiers/identifier-syntax-and-equivalence.md),
including exact source fixes rather than silent normalization.

### Security and visual review

[UTS #39 Revision 32](../30-sources/davis-suignard-2025-unicode-security-mechanisms.md)
defines the General Security Profile, restriction levels, script resolution,
and confusable prototypes. The
[security chapter](../60-specification/identifiers/qualification-keywords-and-security.md)
keeps repertoire rejection, script rejection, and confusable warnings as
three distinct outcomes.

### Source and qualification boundaries

The [C013 source-text map](source-text-encoding-and-normalization.md) supplies
the strict scalar stream and original-byte spans. C014 defines standalone
segments and ASCII-dot paths but does not scan a full file. The existing
[data map](algebraic-data-types.md) and
[effect map](algebraic-effects-and-handlers.md) show why constructor,
condition, capability, and operation references need qualification without
yet selecting module lookup rules.

### Conformance and version separation

[Identifier diagnostics and conformance](../60-specification/identifiers/diagnostics-and-conformance.md)
defines `IDN001`–`IDN007` and thirteen obligations. The
[Conformance Traceability map](conformance-traceability.md) connects those
obligations to the sibling compiler's tagged C014 suite. Revision `0.1.10`
remains outside retained JSON, kernel, interface, artifact, and signature
formats.

## Open questions

C014 is resolved, C015 supplies abstract layout events, C016 supplies
comment events, and C017 supplies atomic literal boundaries. G019–G020 must
integrate identifiers and literals with concrete
punctuation, declarations, and files. G021/G022 own namespaces,
shadowing, comparison domains, resolution, imports, and exports. P117 and G118
own cross-file explanations, display-safe diagnostics, and formatting. A later
Unicode revision requires an explicit compatibility and security-data review.
