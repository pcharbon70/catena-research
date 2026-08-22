---
title: "How Should Catena Organize Namespaces and Shadowing?"
kind: inquiry
created: "2026-08-22"
status: open
tags:
  - catena
  - language-design
  - namespaces
  - shadowing
aliases:
  - "Catena namespace inquiry"
---

# How Should Catena Organize Namespaces and Shadowing?

## Why this matters

Every name in a Catena program — value, type, constructor, trait, effect,
handler, process entry, module, specification identity, field, operation,
type variable — must have one deterministic answer to "what does this
spelling denote here?" Until namespace structure is fixed, independent
implementations could disagree about whether `Vec` and `vec` collide,
whether a constructor shadows a type, whether an imported name hides a
local one, and what `A.B.C` means. Those disagreements would leak into
every later surface: P109's declaration grammar, G022's imports, G026's
prelude, and every diagnostic that names a name.

The C010 kernel already legislated its own bounded namespace law (two
spelling classes, per-namespace duplicate rejection, flat constructor
uniqueness, lexical value shadowing, digest-backed imports without
wildcards), and the C014/C019/C020 stack fixed spelling and qualification
mechanics. G021 must extend that law to the whole language without
amending it.

## Operational question

Choose a bounded 0.1.17 boundary in which independent implementations agree
on:

- the complete namespace category inventory and which spelling class each
  admits;
- uniqueness domains — what may duplicate what across categories, modules,
  and declarations;
- the scope model: which scopes exist, what shadowing is permitted, and
  what stays deterministic;
- how type variables interact with type, trait, and value namespaces;
- how local declarations, imports, and the future prelude compete for one
  unqualified spelling, and what happens on collision;
- where specification and governance identities live;
- how deep a qualified reference goes; and
- stable diagnostics for every rejection.

The answer must compose with the kernel's fixed rules, C014 identifier
spelling, C019's `.`-separated qualified-name tokens, and C020's flat
module names without deciding G022 import/export syntax, G024 cycles,
G026 prelude contents, G066 type-directed resolution, or P109 surface
grammar.

## Working hypotheses

- Per-category namespaces with the two spelling classes as a hard surface
  partition: lowercase-initial binds value-class categories only;
  uppercase-initial binds capitalized-class categories only.
- Constructors form one flat per-module namespace; qualification is the
  ambiguity escape, per the ADT synthesis.
- Inner scopes shadow outer bindings deterministically and silently;
  same-scope same-category duplicates are static invalidity.
- Type variables have their own quantifier-scoped namespace and may shadow
  type and trait names inside their quantifier; they never touch the value
  namespace.
- Local declarations beat imports; two imports colliding on one
  unqualified spelling in a category are static invalidity requiring
  qualification, with both origins named.
- Specification and governance identities live in their own categories and
  never participate in program-name resolution.
- A qualified reference is exactly two segments; deeper chains are
  reserved spellings.

## Paths to explore

- [Haskell 2010 namespace findings](../30-sources/marlow-2010-haskell-language-report.md)
  supply the six-name-kind model with spelling classes, silent shadowing,
  and qualification as the escape.
- [The SML Definition's namespace findings](../30-sources/milner-et-al-1997-definition-standard-ml.md)
  supply per-category environments, identifier status, flat constructor
  namespaces, and cross-namespace independence.
- [The C010 kernel](../60-specification/formal-semantic-kernel/canonical-kernel-syntax.md)
  fixes the bounded precedent this question must generalize.
- [Catena Identifiers and Name Security](../20-notes/catena-identifiers-and-name-security.md)
  and [Catena Files and Modules](../20-notes/catena-files-and-modules.md)
  fix spelling, qualification mechanics, and flat module names.

## Findings

- Haskell's section 1.4 is the closest published model: six name kinds,
  two spelling classes, one explicit same-scope collision ban
  (type-constructor versus class), everything else free to share spelling
  across namespaces. Its modules chapter locates ambiguity resolution in
  qualification, exactly Catena's chosen escape.
- The SML Definition carries separate environments per namespace with
  identifier status recorded per binding — resolution never depends on
  spelling alone — and keeps constructor namespaces flat at scope level,
  matching the kernel's "unique across the module" rule.
- The kernel's own law is already 80% of the answer: extending its two
  classes, duplicate rejection, shadowing, and no-wildcard stance corpus-
  wide is consolidation, not amendment.
- The synthesis
  [Catena Namespaces and Shadowing](../20-notes/catena-namespaces-and-shadowing.md)
  develops the full model and falsification criteria; the
  [topic map](../10-maps/namespaces-and-shadowing.md) routes the evidence.

## Outcome

Open. Resolution requires candidate normative chapters covering the
inventory, shadowing and ambiguity, and diagnostics; a sibling compiler
abstract scope-event resolver with tagged executable evidence; and the
C013–C020 promotion workflow.
