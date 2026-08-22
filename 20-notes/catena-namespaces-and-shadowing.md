---
title: "Catena Namespaces and Shadowing"
kind: note
created: "2026-08-22"
maturity: developing
tags:
  - catena
  - language-design
  - namespaces
  - shadowing
aliases:
  - "Catena namespace model"
---

# Catena Namespaces and Shadowing

## Executive conclusion

Catena should organize names into fixed per-category namespaces partitioned
by the two spelling classes the kernel already fixes: lowercase-initial
spellings bind value-class categories (values, fields, operations, type
variables) and uppercase-initial spellings bind capitalized-class
categories (types, constructors, traits, effects, handlers, process
entries, modules). The same spelling in different namespaces never
collides; the same spelling twice in one namespace and one scope is static
invalidity.

Shadowing is deterministic and silent: an inner scope's binding of a name
hides every outer binding of that name in that namespace, last binder
wins, and no warning exists in this revision. Type variables form their
own quantifier-scoped namespace that may shadow type and trait names
inside its quantifier and never touches values. Constructors form one flat
per-module namespace with `Module.member` qualification as the ambiguity
escape. Local declarations beat imports; two imports colliding on one
unqualified spelling in one category are rejected with both origins named.

Governed specification identities live in their own categories and never
participate in program-name resolution. A qualified reference is exactly
two segments over C020's flat module names; deeper chains are reserved
spellings.

The executable deliverable follows the C015/C020 pattern: an abstract
scope-event resolver that consumes declaration, import-set, and reference
events and yields resolutions or stable diagnostics — testable before
P109's declaration grammar exists.

This closes G021 without deciding G022 import/export syntax, G024 cycles,
G026 prelude contents, G066 type-directed resolution, or P109 surface
grammar.

## Scope and method

The operational target is independent agreement on the namespace inventory,
uniqueness domains, the scope and shadowing model, type-variable
interaction, cross-origin precedence, governance separation, and
qualification depth. Primary comparative evidence comes from the expanded
[Haskell 2010 namespace findings](../30-sources/marlow-2010-haskell-language-report.md)
and [SML Definition namespace findings](../30-sources/milner-et-al-1997-definition-standard-ml.md),
with the [Erlang](../30-sources/erlang-otp-modules-and-code-loading.md) flat-atom
and [OCaml open-shadowing](../30-sources/ocaml-5-4-expressions-and-pattern-guards.md)
models as contrasts. Source claims stay distinct from Catena proposals
below.

## Relation to the current corpus

The [C010 kernel](../60-specification/formal-semantic-kernel/canonical-kernel-syntax.md)
fixes the bounded precedent: the two spelling classes, per-namespace
duplicate rejection at module level, flat constructor uniqueness across
the module, per-declaration uniqueness for parameters, fields, methods,
operations, and handler clauses, lexical value shadowing, and digest-backed
imports without wildcard namespaces. C021 generalizes that law to every
category the whole language has, amending nothing.

[C014 identifiers](../60-specification/identifiers/README.md) fix spelling
and NFC identity; C019 makes `.`-joined qualified names single tokens; and
[C020](../60-specification/files-and-modules/README.md) fixes flat,
uppercase-initial module names — so a two-segment qualified reference has
an exact spelling meaning already, and this slice fixes its resolution
meaning. The [ADT synthesis](algebraic-data-types.md) already requires
post-resolution constructor identity to carry nominal identity, type
scheme, arity, and parent datatype; the namespace layer delivers the
resolution that produces it.

[C006 governance](../60-specification/specifications-and-governance/README.md)
types its own identities (claims, evidence, assumptions, decisions,
actors, trust roots); keeping them out of program namespaces preserves
that typing. The [conformance
vocabulary](../CONFORMANCE-VOCABULARY.md) requires every ambiguity outcome
to be deterministic invalidity or a fixed precedence — never
implementation choice.

## Comparative evidence and inference

### Haskell: six name kinds, two classes, qualification as the escape

Haskell's report fixes six name kinds with two spelling classes and only
one same-scope collision ban (type constructor versus class); everything
else may share a spelling across namespaces. Modules control namespaces,
unqualified ambiguous use is rejected, and qualified names always resolve.
`let` shadowing is innermost-wins with no report-defined warning. The
inference for Catena: per-category namespaces with spelling classes are a
proven low-friction model, and the one Haskell ban generalizes into
Catena's simpler rule — duplicates rejected per category rather than one
special pair. Haskell's import forms (qualified-only, hiding, renaming)
are deliberately left to Catena's G022.

### Standard ML: environments per namespace, status per binding

The SML Definition carries a separate environment for each namespace and
records identifier status per binding, so resolution never depends on
spelling alone; constructors enter the enclosing scope's constructor
namespace, flat, with structure qualification as the escape; inner `let`
bindings shadow outer ones. The inference: flat constructor namespaces
with qualification scale, per-category environments are the deep
specification technique, and Catena's kernel already legislated exactly
this shape. Catena declines SML's generative structures — module
machinery no slice has designed.

### Erlang and OCaml: the contrasts

Erlang's flat atom namespace makes every collision a global one — the
model Catena's categories exist to avoid. OCaml's `open` re-shadows by
declaration order, making resolution order-dependent; Catena's
local-beats-imported precedence with rejection on import collision keeps
resolution a function of the scope structure alone, matching C001's
determinism discipline.

## Selected model

### Namespace inventory

| Category | Class | Uniqueness domain |
| --- | --- | --- |
| values | lowercase | scope; duplicates in same scope invalid |
| fields | lowercase | owning declaration |
| operations | lowercase | owning effect/handler declaration |
| type variables | lowercase | quantifier scope; may shadow types/traits |
| types | uppercase | module |
| constructors | uppercase | module, flat across types |
| traits | uppercase | module |
| effects | uppercase | module |
| handlers | uppercase | module |
| process entries | uppercase | module |
| modules | uppercase | package (cross-file duplicates are G025's) |
| specifications/governance identities | their own | per C006 typing; never in program resolution |

A spelling-class violation — a lowercase spelling binding a capitalized
category or the reverse — is static invalidity at the declaration event.

### Scope model and shadowing

Scopes nest: module scope contains declaration scopes (quantifiers,
clauses, handlers), which contain expression scopes introduced by binders.
An inner binding of a name in a category hides all outer bindings of that
name in that category; resolution always takes the innermost visible
binding. Shadowing is silent in 0.1.17. A same-scope duplicate in one
category is invalid regardless of spelling identity class.

### Type variables

A quantifier introduces a type-variable scope whose names shadow type and
trait names for the quantified region; duplicate type variables in one
quantifier are invalid; type variables never resolve as values, and value
names never resolve as type variables.

### Precedence and imports

For one unqualified spelling in one category: local declarations win over
imports; two imports from different origins colliding in one category are
invalid until qualified, with both origins reported; a future prelude is
another import origin under G026, never a silent default. Resolution is a
function of (scope structure, declaration events, import sets) — never of
declaration order between independent origins.

### Qualification

A qualified reference is exactly two segments, `Module.member`, where the
first segment resolves as a module and the second in that module's
exported category namespaces (export selection is G022's). Three-or-more
segment chains are reserved spellings rejected with a stable diagnostic
until a later revision admits nesting or member access with evidence.

### Governance separation

Claim, evidence, assumption, decision, actor, and trust-root identities
resolve only inside their own categories and never as program names;
program names never collide with them and vice versa.

### Abstract resolver

A conforming implementation exposes a scope-event processor — declare
(category, spelling, scope), open/close scope, import set (origin,
category, exported spellings), quantifier scope — building resolution
environments, and a reference resolver returning nominal identity or one
diagnostic. Neither parses source; the events come from P109's grammar or
tests.

## Rejected alternatives

- **Single flat namespace (Erlang-style):** maximizes collisions; forces
  constructor names to fight type names for spellings everyone uses.
- **Spelling-free categories (Scala-style):** discards the kernel's fixed
  spelling classes and the tokenizer's name-class information.
- **Per-type constructor namespaces:** the ADT synthesis already showed
  post-resolution identity carries the parent type, so per-type hiding
  buys nothing while breaking the kernel's flat-uniqueness rule.
- **Order-based import priority (OCaml open-style):** makes resolution
  order-dependent; contradicts C001 determinism.
- **Shadowing warnings now:** pre-judges a usability question with no
  evidence; P117 can add deny-able warnings later without semantic change.
- **Forbidding shadowing:** contradicts the kernel's normative allowance.
- **Arbitrary qualification depth:** commits to hierarchical modules no
  slice has designed; two segments is what C020 flat names support.

## What C021 adds to the design

Name resolution becomes a specified function instead of an implementation
accident: P109's grammar gets the scope model it must elaborate into,
G022's imports get the precedence and collision rules they must feed, and
every future diagnostic that mentions a name has stable categories and
origins to cite. The kernel's bounded namespace law is consolidated
corpus-wide with zero amendments.

## Remaining questions and falsification criteria

G022 must fix import/export syntax, visibility defaults, renaming,
wildcard exclusion confirmation, and unused-import diagnostics; G024 must
decide module recursion knowing resolution is order-independent; G025 must
enforce package-level module-name uniqueness; G026 must design the prelude
as an origin; G066 must confirm no resolution becomes type-directed; P109
must emit the events this resolver consumes.

The model should be revisited if G022's design needs precedence beyond
local-versus-imported, if G025's package assembly requires hierarchical
module names, or if usability evidence shows silent shadowing materially
harms real code — the last would add P117 warnings, not semantic change.

## Connections

- The [resolved namespace inquiry](../40-inquiries/how-should-catena-organize-namespaces-and-shadowing.md)
  records the operational question and evidence trail.
- The [Namespaces and Shadowing map](../10-maps/namespaces-and-shadowing.md)
  routes through evidence, constraints, and remaining owners.
- The [Namespaces and Shadowing Specification](../60-specification/namespaces-and-shadowing/README.md)
  defines the normative 0.1.17 contract.
- The [C021 evidence record](../50-journal/2026-08-22-c021-namespaces-and-shadowing.md)
  records the sibling implementation and verification.
- [Catena Files and Modules](catena-files-and-modules.md) fixes the flat
  module names two-segment qualification rides on.
- [Algebraic Data Types](algebraic-data-types.md) fixes the
  post-resolution constructor identity this layer produces.

## Sources

- [Haskell 2010 Language Report](../30-sources/marlow-2010-haskell-language-report.md)
- [The Definition of Standard ML (Revised)](../30-sources/milner-et-al-1997-definition-standard-ml.md)
- [Erlang/OTP Modules and Code Loading](../30-sources/erlang-otp-modules-and-code-loading.md)
- [OCaml 5.4 Expressions and Pattern-Matching Guards](../30-sources/ocaml-5-4-expressions-and-pattern-guards.md)
