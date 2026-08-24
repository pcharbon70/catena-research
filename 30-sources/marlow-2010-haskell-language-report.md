---
title: "Haskell 2010 Language Report"
kind: source
created: "2026-08-01"
authors:
  - "Simon Marlow (editor)"
published: 2010
citation_key: "marlow2010Haskell2010"
container: null
edition: "Haskell 2010"
isbn: null
doi: null
url: "https://www.haskell.org/definition/haskell2010.pdf"
accessed: "2026-08-01"
tags:
  - comprehensions
  - files
  - floats
  - namespaces
  - language-design
  - layout
  - literals
  - modules
  - operators
  - pattern-matching
  - syntax
  - whitespace
aliases:
  - "Haskell 2010 Report"
---

# Haskell 2010 Language Report

## Reference

Simon Marlow, ed., *Haskell 2010 Language Report* (2010).
[Official report](https://www.haskell.org/definition/haskell2010.pdf).

## Research question

How does Haskell give layout, ordered clause guards, and list comprehensions
precise translations, and what do those translations imply for lexical and
semantic structure?

## Method

The report is the language definition. Sections 2.7 and 10.3 specify layout;
Sections 3.11, 3.13, and 3.17 give syntax, informal behavior, and translation
rules for list comprehensions, case alternatives, and pattern matching. The
numeric-literal findings below come from Sections 6.4 and 6.4.1, re-read
2026-08-21 for Catena's numeric literal work. The fixity findings come from
Section 4.4.2, read 2026-08-21 for Catena's operator work.

## Findings

### Layout

- Layout-sensitive contexts begin after selected keywords when an explicit
  opening brace is absent. The next lexeme's indentation establishes the
  context column.
- Equal indentation inserts a semicolon, lesser indentation closes one or more
  implicit contexts, and greater indentation continues the current item.
- Explicit braces push a distinct zero context in which the surrounding
  implicit layout rule is suspended.
- The specification fixes one-based columns, eight-column tab stops, and a
  one-column width for every Unicode character. It warns against programs whose
  meaning depends on non-space display width.
- A parser-prefix test can trigger an implicit closing brace when the next
  token would otherwise make the prefix invalid. Layout therefore is not a
  purely local whitespace rewrite.
- EOF closes remaining implicit contexts but is an error in an unclosed
  explicit context.

### Clause guards

- A guarded case alternative may contain a sequence of Boolean guards,
  pattern guards, and local declarations.
- Guards in a sequence are evaluated in order. A false Boolean guard or failed
  pattern guard falls through; bindings from successful earlier steps are
  available to later steps and the body.
- The report reduces guarded alternatives to nested case and conditional
  expressions. This gives guards a kernel meaning rather than making them a
  special backend facility.
- The translation preserves source alternative order and ultimately raises a
  no-match error if every alternative fails.
- Guard evaluation affects strictness. A structurally irrefutable pattern may
  still force values when its guard evaluates them.

### List comprehensions

- A list comprehension contains a result expression followed by one or more
  qualifiers. Qualifiers are list generators, local declarations, or arbitrary
  expressions of type `Bool`.
- Generators are evaluated as nested, depth-first traversals. Bindings from an
  earlier qualifier are visible in later qualifiers and the result.
- A generator pattern mismatch silently skips that source element. This makes
  pattern selection part of generator semantics rather than an ordinary match
  failure.
- A false Boolean qualifier contributes no result. Local declarations scope
  over the remaining qualifiers and result.
- The kernel translation maps a generator through a fresh pattern-matching
  function and `concatMap`, maps a false filter to the empty list, and nests a
  local declaration around the remaining comprehension.
- Generator bindings are lambda-bound and monomorphic, while local `let`
  declarations can be generalized. Surface similarity therefore does not make
  the two binders statically interchangeable.

### Numeric literals and numeric classes

- An integer literal denotes the application of `fromInteger` to the
  corresponding `Integer` value, and a floating literal denotes the
  application of `fromRational` to an exact `Rational` value. Unsuffixed
  literals therefore have the overloaded typings `(Num a) => a` and
  `(Fractional a) => a`.
- The report introduces this indirection expressly so one spelling can denote
  values of any suitable numeric type, and refers overloading ambiguity to
  the default-declaration mechanism of Section 4.3.4. Overloaded literals
  and defaulting are one coupled design.
- The Prelude fixes `Integer` as arbitrary precision and `Int` as a bounded
  implementation-defined integer type. `Double` should cover IEEE double
  precision and `Float` is implementation-defined.
- For fixed-precision numeric types, the results of exceptional conditions
  such as overflow or underflow are undefined in the report: an
  implementation may error, truncate, or return a special value.
- `toRational` converts with full precision, and the `RealFloat` class
  exposes radix, digits, range, decoding, and IEEE predicates
  (`isNaN`, `isInfinite`, `isNegativeZero`, `isIEEE`) for implementations
  that support such numbers.

### Fixity declarations

- A fixity declaration has the form `fixity [integer] ops` where `fixity` is
  one of `infixl`, `infixr`, or `infix`. It may appear anywhere a type
  signature appears, including top level and class bodies, at most once per
  operator, and only in the same declaration sequence as the operator's
  definition.
- The integer level ranges from 0 to 9; level 0 binds least tightly and
  level 9 most tightly. If the digit is omitted, level 9 is assumed.
- Any operator lacking a fixity declaration defaults to `infixl 9`.
- The Prelude's own operators are given their precedences by a fixity table
  (Table 4.1) covering levels 9 down to 0 — for example `!!` and `.` at 9,
  exponentiation at 8 right-associative, multiplication and addition at 7
  and 6, cons at 5 right-associative, comparisons at 4 non-associative,
  Boolean conjunction at 3 right-associative, and application helpers `$`
  at 0.

## Relevance

The report demonstrates compositional paths from layout and rich expression
surfaces to explicit structure. Its offside translation is evidence that
semantic indentation requires column, tab, delimiter-stack, EOF, and parser
interaction rules; Catena avoids those costs by making indentation
non-semantic.

It also makes clear that clause guards, comprehension filters, generator
patterns, and local declarations have related syntax but different failure and
binding roles.

The list translation supplies an extensional model for Catena's pure
comprehensions. Catena should not inherit silent pattern filtering without an
explicit marker, and its strict effectful semantics require a more direct
operational account than Haskell's non-strict `concatMap` equation.

The numeric sections are Catena's primary comparative evidence for a
different literal policy: overloaded `fromInteger`/`fromRational` literals
require defaulting to stay usable, while Catena's C001 inference contract has
no numeric defaulting and C004 rejects ambiguous constraints. The report's
admission that fixed-precision overflow and underflow are undefined is also
the precise behavior class Catena's conformance vocabulary prohibits, making
Haskell the contrast case for C018's monomorphic typing, explicit conversion
boundary, and statically decided overflow.

The fixity sections supply the rejected alternative for operator design:
user-declared `infixl`/`infixr`/`infix` levels with a silent `infixl 9`
default for undeclared operators. That extensibility couples the grammar to
declaration processing, makes every operator's precedence a resolved name
rather than a token fact, and motivated Catena's fixed ladder with no user
fixity in 0.1.15. The report's own Prelude table also shows comparisons
declared non-associative at level 4, agreeing with Rust's rejection of
comparison chains and supporting Catena's non-associative comparison level.

### Namespaces and shadowing

- Section 1.4 fixes exactly six name kinds: variables and constructors
  denoting values; type variables, type constructors, and type classes in
  the type system; and module names. Variables and type variables begin
  lowercase or underscore; the other four kinds begin uppercase.
- The only same-scope collision constraint is that an identifier must not
  name both a type constructor and a class in the same scope; otherwise one
  spelling may simultaneously name a module, a class, and a constructor.
- Chapter 5 locates name control in modules: a module has a name space
  consisting of a top-level declaration set, imports bring entities from
  other modules' export lists, and unqualified use of an imported name is
  subject to the module's import form.
- Haskell 2010 rejects unqualified names only when they are ambiguous under
  the active imports; qualified names (`Module.name`) always resolve.
- `let`-bound and lambda-bound variables shadow outer bindings of the same
  name; innermost binding wins, and no warning is defined by the report.
- The report leaves error-message quality for undefined programs explicitly
  implementation-dependent, including name-resolution failures.

For Catena, Haskell's namespace section is the closest published model of
the chosen design: fixed name kinds, two spelling classes, per-kind
environments, silent deterministic shadowing, and qualification as the
ambiguity escape. The differences Catena adopts are deliberate: Haskell's
class/type-constructor collision ban generalizes into Catena's per-category
duplicate invalidity; and Haskell's import-form machinery (qualified-only,
hiding, renaming) belongs to Catena's G022 rather than to resolution itself.

### Modules and file binding

- A Haskell program is a collection of modules; each module has a `module
  ModuleName [exports] where ...` header followed by declarations.

### Import and export declarations

- Chapter 5 gives imports four shapes: an omitted import specification
  imports every exported entity; an explicit parenthesized list imports
  only the named entities and must name only entities the imported module
  exports; `hiding(...)` imports everything except the named entities; and
  an empty list `()` imports nothing unqualified.
- The `qualified` keyword brings only qualified names into scope; without
  it both the qualified and unqualified names arrive, so any import always
  enables `M.name` qualification.
- An `as` clause gives the import a local qualifier; several modules may
  share one qualifier provided no name becomes ambiguous.
- Import lists are cumulative across declarations and their order is
  irrelevant.
- Export lists name exported entities; a datatype may be exported without
  its constructors (abstract), with an explicit constructor sublist, or
  with `T(..)` for all in-scope constructors; the `module M` export form
  re-exports everything imported from M. If the export list is omitted,
  all locally defined values, types, and classes are exported, but never
  imported ones.
- Name clashes between imports are errors only when the clashing name is
  actually mentioned unqualified; unmentioned collisions are legal, and
  qualification resolves any mentioned one. Multiple import routes for one
  entity resolve to that single entity.
- The Prelude is imported automatically into every module unless imported
  explicitly, and may be shadowed only through explicit imports.

### Mutually recursive modules and separate compilation

- Chapter 5 states that modules may reference other modules via explicit
  import declarations and that "modules may be mutually recursive"; the
  introduction to the module chapter adds that, because of this, "modules
  allow a program to be partitioned freely without regard to
  dependencies," and shows a three-module `Main`/`A`/`B` example whose
  concatenation into one uniquely-named module is the stated semantics.
- Section 5.7 concedes the cost: "Depending on the Haskell
  implementation used, separate compilation of mutually recursive modules
  may require that imported modules contain additional information so
  that they may be referenced before they are compiled. Explicit type
  signatures for all exported values may be necessary to deal with mutual
  recursion. The precise details of separate compilation are not defined
  by this report."

For Catena's cycle work, these two passages are the primary
adopted-alternative evidence: recursion across modules is a real,
specified language feature (not an implementation accident), and the
report itself identifies the exact price — exported values need explicit
signatures and the compilation unit must grow to the recursive group. The
contrast cases are Standard ML, whose structures are not recursively
bindable, and Erlang, whose compile-time dependencies are acyclic with
module-level code replacement at runtime.

For Catena's import work, Haskell supplies the exact machinery being
adopted and the exact machinery being declined: adopted are explicit
import lists (whose empty form matches Catena's qualified-only admission
precisely), always-available qualification, order-independent cumulative
imports, and mention-time ambiguity errors — which C021's `NSP004`
already legislates; declined are `hiding`, `as` aliases, the `module M`
re-export form (deferred to package assembly), public-by-default exports
(Catena requires explicit export declarations), and the implicit Prelude
(G026).
- The module's name is declared by the header. The report's module chapter
  states that module names are used to locate the module's interface and
  object files, and the toolchain convention pairs `module M` with the file
  `M.hs`.
- A module header may be omitted, in which case the module is named `Main`
  — a defaulting of module identity for scripts.
- Modules may be hierarchically named (`A.B.C`), and the hierarchy maps to
  directory structure in tooling conventions.

For Catena's file work, Haskell shows the declared-header model where the
name lives in the file content, paired with a tooling-level filename
convention — the same pairing Catena adopts, except Catena makes the
basename match a language rule with static invalidity rather than a loader
expectation, and rejects implicit `Main`-style defaulting in favor of
explicit no-module files.

## Limits

Haskell is non-strict and pure, while Catena is proposed to be strict with
explicit effect rows. Haskell's bottom and strictness considerations therefore
do not map directly to Catena's proposed total guard fragment or its
left-to-right effect traces. The report defines extensional language behavior,
not stack safety, allocation, fusion constraints, or modern coverage-checker
precision.

## Derived work

- [Clause Guards](../20-notes/clause-guards.md)
- [How Should Catena Design Clause Guards?](../40-inquiries/how-should-catena-design-clause-guards.md)
- [Clause Guards map](../10-maps/clause-guards.md)
- [List Comprehensions](../20-notes/list-comprehensions.md)
- [How Should Catena Specify List Comprehensions?](../40-inquiries/how-should-catena-specify-list-comprehensions.md)
- [List Comprehensions map](../10-maps/list-comprehensions.md)
- [Catena Whitespace, Layout, and Line Continuation](../20-notes/catena-whitespace-layout-and-line-continuation.md)
- [Resolved layout inquiry](../40-inquiries/how-should-catena-treat-whitespace-and-line-breaks.md)
- [Whitespace, Layout, and Line Continuation map](../10-maps/whitespace-layout-and-line-continuation.md)
- [Catena Numeric Literal Semantics](../20-notes/catena-numeric-literal-semantics.md)
- [How Should Catena Define Numeric Literal Semantics?](../40-inquiries/how-should-catena-define-numeric-literal-semantics.md)
- [Numeric Literal Semantics map](../10-maps/numeric-literal-semantics.md)
- [Catena Operators and Punctuation](../20-notes/catena-operators-and-punctuation.md)
- [How Should Catena Fix Operators and Punctuation?](../40-inquiries/how-should-catena-fix-operators-and-punctuation.md)
- [Operators and Punctuation map](../10-maps/operators-and-punctuation.md)
- [Catena Files and Modules](../20-notes/catena-files-and-modules.md)
- [How Should Catena Relate Files to Modules?](../40-inquiries/how-should-catena-relate-files-to-modules.md)
- [Files and Modules map](../10-maps/files-and-modules.md)
- [Catena Namespaces and Shadowing](../20-notes/catena-namespaces-and-shadowing.md)
- [How Should Catena Organize Namespaces and Shadowing?](../40-inquiries/how-should-catena-organize-namespaces-and-shadowing.md)
- [Namespaces and Shadowing map](../10-maps/namespaces-and-shadowing.md)
- [Catena Imports and Exports](../20-notes/catena-imports-and-exports.md)
- [How Should Catena Handle Imports and Exports?](../40-inquiries/how-should-catena-handle-imports-and-exports.md)
- [Imports and Exports map](../10-maps/imports-and-exports.md)
- [Catena Dependency Cycles](../20-notes/catena-dependency-cycles.md)
- [How Should Catena Handle Module Dependency Cycles?](../40-inquiries/how-should-catena-handle-module-dependency-cycles.md)
- [Module Dependency Cycles map](../10-maps/module-dependency-cycles.md)
