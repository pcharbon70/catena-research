---
title: "Inquiries"
kind: map
created: "2026-07-31"
tags:
  - archive-navigation
  - directory-index
aliases:
  - "Inquiries index"
---

# Inquiries (`40-inquiries`)

## Purpose

Inquiries are active research workbenches organized around answerable
questions.

## What belongs here

Put open questions, provisional hypotheses, evidence paths, findings, and
resolution criteria here. Promote conclusions that become independently useful
to `20-notes`.

## Index

### Subdirectories

- None yet.

### Documents

- [Should Catena Admit Type Aliases and Newtypes?](should-catena-admit-type-aliases-and-newtypes.md)
  — resolves G062: aliases excluded with arrival conditions,
    opaque routed to C022/C023, newtypes the nominal single-field
    ADT with explicit-only deriving and no cost promises at
    `0.1.41`.
- [How Should Int and Float Relate Across Operators?](how-should-int-and-float-relate-across-operators.md)
  — resolves G061: closed-set instantiation over {Int, Float}, no
    dispatch, float arithmetic witnessed via annotations, division
    routed to G105 at `0.1.40`.
- [Which Pattern Contexts Admit Refutable Patterns?](which-pattern-contexts-admit-refutable-patterns.md)
  — resolves P044 and D046: the three context classes with
    per-context rules and reservations at `0.1.38`.
- [How Should Catena Decode and Normalize Source Text?](how-should-catena-decode-and-normalize-source-text.md)
  — resolves C013 with strict UTF-8, BOM rejection, LF/CRLF logical newlines,
  no whole-file normalization, scalar columns, and original-byte spans.
- [How Should Catena Handle Comments and Documentation Comments?](how-should-catena-handle-comments-and-documentation-comments.md)
  — resolves C016 with nested slash comments, lossless layout integration,
  forward declaration documentation, CommonMark/raw-HTML rules, and explicit
  future doctest opt-in.
- [How Should Catena Spell and Decode Literals?](how-should-catena-spell-and-decode-literals.md)
  — resolves C017 with a bounded atomic set, exact numeric components, cooked
  and raw decoding, scalar/byte separation, provenance, active limits, and
  explicit exclusions.
- [How Should Catena Define Numeric Literal Semantics?](how-should-catena-define-numeric-literal-semantics.md)
  — resolves C018 with monomorphic `Int`/finite-`Float` domains, correct
  rounding, static overflow refusal, negation elaboration, and the
  decimal-component digit limit measured against IEEE, BEAM, Haskell, and
  Rust evidence.
- [How Should Catena Fix Operators and Punctuation?](how-should-catena-fix-operators-and-punctuation.md)
  — tests a closed semantic-mapped token set, a fixed precedence ladder with
  rejected comparison chains, concrete C015 capabilities and frames, and
  reserved-spelling rejection against Rust, OCaml, and Haskell evidence.
- [How Should Catena Relate Files to Modules?](how-should-catena-relate-files-to-modules.md)
  — tests at-most-one module per `.cat` file, declared-name basename
  verification, ASCII module words, and first-line generated markers
  against Erlang, Rust, and Haskell evidence.
- [How Should Catena Organize Namespaces and Shadowing?](how-should-catena-organize-namespaces-and-shadowing.md)
  — tests per-category namespaces with spelling classes, flat constructor
  uniqueness, deterministic shadowing, type-variable scoping, and
  local-over-imported precedence against Haskell and SML evidence.
- [How Should Catena Handle Imports and Exports?](how-should-catena-handle-imports-and-exports.md)
  — tests private-by-default exports, qualification-plus-list admission,
  the exclusion of wildcards, renaming, and re-exports, and deny-able
  unused-import warnings against Haskell, SML, Erlang, and Rust
  evidence.
- [How Should Catena Draw Its Abstraction Boundaries?](how-should-catena-draw-its-abstraction-boundaries.md)
  — tests the declared absence of stable-layout opt-in and split
  constructor authority, and the smart-constructor invariant idiom,
  against the shipped C002/C022 contracts and Leroy/SML evidence.
- [How Should Catena Handle Module Dependency Cycles?](how-should-catena-handle-module-dependency-cycles.md)
  — tests SCC admission with declared-signature resolution, joint
  digests, and definition-only initialization against Haskell's recursive
  modules and the digest-import circularity.
- [How Should Catena Define Package Identity and Dependency Resolution?](how-should-catena-define-package-identity-and-dependency-resolution.md)
  — tests the manifest dependencies field, SemVer with exact/caret/tilde
  operators, single-version resolution, `catena.lock` replay, and
  registry-neutral bundle-digest identity against SemVer and Hex
  evidence.
- [How Should Catena Define Its Prelude Policy?](how-should-catena-define-its-prelude-policy.md)
  — tests opt-in manifest selection, ordinary-origin precedence,
  absent-means-out opt-out, and the zero-implicit-names edition
  guarantee against the shipped C021/C022/C025 contracts and the
  declined Haskell model.
- [How Should Catena Define Entry Points and Application Structure?](how-should-catena-define-entry-points-and-application-structure.md)
  — tests named entry exports, effect-closure, invocation-only startup,
  return-is-shutdown, and derived libraries against the C010 completion
  rule, the C026 guarantee, and the OTP application precedent.
- [How Should Catena Define API and ABI Compatibility?](how-should-catena-define-api-and-abi-compatibility.md)
  — tests layered compat stances, the strict diff matrix,
  minor-as-breaking under 0.x, and the re-export exclusion against the
  shipped interface, lifecycle, and package contracts and the OTP
  strategy precedent.
- [What Are Catena's Values and Strictness?](what-are-catenas-values-and-strictness.md)
  — tests the closed value grammar with Float, uniform
  first-classness, and the strictness invariant against the C010
  kernel calculus, C005's affine resumptions, and C018's Float.
- [When Does Each Subexpression Evaluate?](when-does-each-subexpression-evaluate.md)
  — tests the closed ordered-forms table with typed-core completions,
  the entry rule, and trace observability against the C010 kernel
  backbone and the C002/C003/C004/C005 fragments.
- [How Should Catena Define Bindings and Sequencing?](how-should-catena-define-bindings-and-sequencing.md)
  — tests non-recursive binding structure, definitions-only recursion,
  the sequencing idiom, and deny-able `BS001` against the kernel's let
  rules, C021 shadowing, C024's SCC, and C022's IMP001 precedent.
- [What Is Catena's Function and Call Model?](what-is-catenas-function-and-call-model.md)
  — tests semantic-unary currying, free partial application, lexical
  immutable capture, let-bound local functions, and the elevated tail
  guarantee against the kernel rules and shipped curried-value
  evidence.
- [What Is Catena's Branching Model?](what-is-catenas-branching-model.md)
  — tests match as the only branch form, the conditional sugar
  promise, the consolidated rule table, and the statement-form absence
  against C002, C003, C010, and the C029–C032 siblings.
- [Which Values Compare, and How?](which-values-compare-and-how.md)
  — tests the comparable set with structural recursion, bit-exact
  float equality, monomorphic comparison, and the guard split against
  C003's fragment, C018's finite floats, C029's grammar, and the OTP
  signed-zero precedent.
- [How Does Catena Separate Recursion from Termination?](how-does-catena-separate-recursion-from-termination.md)
  — tests the unrestricted program stance, the cited separation
  table, and the G038 entry rule against the kernel's permission,
  C029's divergence clause, and the three shipped meta-level regimes.
- [What Counts as Runtime Failure?](what-counts-as-runtime-failure.md)
  — tests the single trap outcome with kinded reasons, the six-way
  mapping, kernel-verbatim observability, and the per-producer gate
  against C010's trap rules, C029's terminal contract, and C034's
  divergence exclusion.
- [What May Programs Observe of Resources?](what-may-programs-observe-of-resources.md)
  — tests the six-way non-observability classification, semantic
  identity, the two-clause identity rule, and the finalization gate
  against the kernel's resource-observability paragraph and the
  C029/C032/C035 deferrals.
- [What Executes During Compilation?](what-executes-during-compilation.md)
  — tests the absence-plus-gate stance, the derivations-as-generation
  classification, and the cited restriction table against C034's gate
  and the three shipped bounded meta-evaluators.
- [Which Types Are Built In?](which-types-are-built-in.md)
  — tests the twelve-way classification, the C018-pattern elaboration
  of Text, Character, and Bytes, and the content-based comparability
  entries against C017's scanner kinds and the C029/C033/C035 entry
  rules.
- [What Are Structural Records and Variants?](what-are-structural-records-and-variants.md)
  — tests the consolidated operation table, kernel rows verbatim, and
  the semantic-map clause against the kernel calculus, C002's nominal
  exclusions, C030's order rows, and C037's maps.
- [How Do Collections Construct and Update?](how-do-collections-construct-and-update.md)
  — tests the six-topic routing, miss-as-value bounds failures, and
  the complexity exclusion against C040's classification, C041's
  boundary, C035's set, C036's taxonomy, and C037's invisibility.
- [How Should Catena Define and Secure Identifiers?](how-should-catena-define-and-secure-identifiers.md)
  — resolves C014 with Unicode 17 XID, filtered NFC, role-neutral case,
  qualification, keywords, security profiles, and confusable warnings.
- [How Should Catena Treat Whitespace and Line Breaks?](how-should-catena-treat-whitespace-and-line-breaks.md)
  — resolves C015 with non-semantic indentation, narrow layout whitespace,
  newline/semicolon separation, and token-capability continuation.
- [How Should Catena Integrate Its Formal Semantic Kernel?](how-should-catena-integrate-its-formal-semantic-kernel.md)
  — records the resolved C010 contract, executable correspondence, bounded
  concurrency evidence, immutable compiler identity, and normative promotion.
- [How Should Catena Bound Implementation Limits?](how-should-catena-bound-implementation-limits.md)
  — resolves C012 with portable minima, finite-resource classifications,
  common diagnostic details, deterministic profile output, and a
  deployment-defined mailbox-capacity boundary.
- [How Should Catena Classify Conformance Behavior?](how-should-catena-classify-conformance-behavior.md)
  — records the resolved C009 distinction among normative force, invalidity,
  profiled choices, bounded presentation, limits, explicit traps, and the
  prohibition on undefined behavior.
- [How Should Catena Achieve Exhaustive Rule-to-Test Traceability?](how-should-catena-achieve-exhaustive-rule-to-test-traceability.md)
  — resolved as C011; the scheme gives every MUST/MUST NOT obligation a permanent
  identifier, a normative heading anchor, and tagged compiler evidence. It now
  covers twenty-two normative areas plus the C012 implementation-limits policy.
- [How Should Catena Design Clause Guards?](how-should-catena-design-clause-guards.md)
  — records the normative implemented 0.1.3 semantic core while retaining open
  usability, performance, trait, recursion, and public receive questions.
- [How Should Catena Expose Mathematical Structure Without Mathematical Jargon?](how-should-catena-expose-mathematical-structure-without-mathematical-jargon.md)
  — tests capability names, operation selection, transfer, diagnostics, and
  the semantic audit needed before Catena stabilizes its learning vocabulary.
- [How Should Catena Specify Algebraic Data Types?](how-should-catena-specify-algebraic-data-types.md)
  — records the resolved C002 decisions for declaration elaboration,
  constructor typing, coverage, abstraction, GADTs, derivation, interfaces,
  and layout independence.
- [How Should Catena Specify Its Initial Categorical Hierarchy?](how-should-catena-specify-its-initial-categorical-hierarchy.md)
  — tests the agreed seventeen-class set through kinding, coherent evidence,
  laws, operational contracts, derivation rules, instances, and inference
  diagnostics.
- [How Should Catena Integrate Specifications and Governance Into the Language?](how-should-catena-integrate-specifications-and-governance-into-the-language.md)
  — tests the semantic kernel, evidence distinctions, authority policy,
  lifecycle protocol, provenance, security, performance, and public vocabulary.
- [How Should Catena Version Editions and Language Features?](how-should-catena-version-editions-and-language-features.md)
  — carries the settled package-local edition, exact-revision, preview,
  compatibility, migration, and artifact model through normative C008's
  executable evidence and immutable promotion record.
- [How Should Catena Specify List Comprehensions?](how-should-catena-specify-list-comprehensions.md)
  — resolved as C047–C058: the eager list-to-list `for ... yield`
    contract at `0.1.39`, with token-level surface adoption
    transferring to P109 and D059's neighbors staying deferred.
- [Which Algebraic-Effect Semantics Should Catena Adopt?](which-algebraic-effect-semantics-should-catena-adopt.md)
  — tests whether lexical capabilities, duplicate-label rows, deep open
  handlers, affine resumptions, and optimized backends form one sound and
  usable design.
- [What Should a Greenfield Catena Type System Guarantee?](what-should-a-greenfield-catena-type-system-guarantee.md)
  — investigates the formal contract and annotation boundaries for an
  inference-first language designed without inherited Catena constraints.
- [Which Combinators Should Catena Provide and Derive?](which-combinators-should-catena-provide-and-derive.md)
  — tests a minimal law-bearing core, class and datatype derivation, strict
  execution contracts, focused domain libraries, naming, and compiler
  representations.

## Maintaining this index

Index every direct inquiry, describe its present focus, and keep `status`
aligned with the actual state of the research.
