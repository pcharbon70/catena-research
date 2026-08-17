---
title: "Canonical Kernel Syntax"
kind: specification
created: "2026-08-06"
status: normative
spec_version: "0.1.8"
tags:
  - formal-semantics
  - parsing
  - specification
aliases:
  - "Catena kernel S-expressions"
---

# Canonical Kernel Syntax

## Input envelope

One kernel input contains exactly one module. It is UTF-8 whose decoded
characters are restricted to horizontal tab, line feed, carriage return when
immediately followed by line feed, and printable ASCII. A byte-order mark,
lone carriage return, non-ASCII character, malformed UTF-8, or trailing form
is invalid.

Spaces, tabs, LF, and CRLF separate tokens and otherwise have no meaning.
Parentheses delimit every compound form. Comments and layout-sensitive
structure do not exist. Metadata strings use JSON string escapes but are not
term-level text literals.

The header is:

> **Normative definition.**

```text
(module ModuleName
  (edition 0.1)
  (revision 0.1.8)
  (origin "origin")
  declaration*)
```

All three header fields are mandatory and occur once in that order. A command
or package selection, when supplied, MUST equal the written edition and
revision.

## Tokens and names

An integer token is `0` or an optional `-` followed by a nonzero decimal digit
and zero or more decimal digits. It denotes a mathematical integer and has no
overflow. `true` and `false` are the only Boolean tokens.

Value, field, operation, and type-variable names match
`[a-z][A-Za-z0-9_]*`. Module, nominal type, constructor, trait, effect,
handler, and process-entry names match `[A-Z][A-Za-z0-9_]*`. A qualified name
contains one or more valid capitalized names separated by `.`. The grammar
uses qualified names only for imported process entries. A keyword in form-head
position cannot be redeclared in that position.

Lexical value bindings may shadow outer lexical value bindings. A module-level
declaration or export may not duplicate a name in its namespace. Constructor
names are unique across the module. Parameters, fields, methods, operations,
and handler clauses are unique within their owning declaration. Imports are
explicit and digest-backed; this kernel imports public process-entry evidence,
not unqualified values or wildcard namespaces.

## Module forms

The closed declaration grammar is:

> **Normative definition.**

```text
declaration ::= (export value value-name)
              | (export type TypeName)
              | (export process ProcessName)
              | (import ModuleName "interface-digest")
              | data-declaration
              | trait-declaration
              | instance-declaration
              | effect-declaration
              | handler-declaration
              | process-declaration
              | definition

process-declaration ::=
  (process ProcessName
    (mailbox type)
    (params (value-name type)*)
    expression)

definition ::=
  (def value-name (signature type (uses effect-entry*)) expression)

data-declaration ::=
  (data TypeName (params type-variable*) constructor+)
constructor ::= (constructor ConstructorName (fields type*))

trait-declaration ::=
  (trait TraitName (parameter type-variable) trait-method+)
trait-method ::= (method value-name type)

instance-declaration ::=
  (instance TraitName type instance-method+)
instance-method ::= (method value-name value-name)

effect-declaration ::= (effect EffectName effect-operation+)
effect-operation ::= (operation value-name (params type*) type)

handler-declaration ::=
  (handler HandlerName
    (effect EffectName)
    (input type)
    (output type)
    (return value-name expression)
    handler-operation*)
handler-operation ::=
  (operation value-name
    (params (value-name type)*)
    (resume value-name)
    expression)
```

The interface digest is exactly 64 lowercase hexadecimal digits. The origin
is a nonempty metadata string. Data declarations are regular positional
algebraic data only. Traits have one parameter, instances have a closed head,
and instance methods name module definitions. Handlers have no value
parameters and contain exactly one clause for each operation of their named
effect; this completeness requirement is static rather than syntactic.

There is no condition declaration in this kernel. Conditions occur only in
the optional `when` position of a clause. GADTs, named constructor fields,
trait dependencies, default methods, laws, derivation, handler arguments,
capability aliases, and public effect or handler imports are outside this
closed grammar. An unknown declaration, extra field, missing field, or
wrong-order form is invalid rather than ignored.

## Types and expressions

The closed type grammar is:

> **Normative definition.**

```text
type ::= Int | Bool | Unit | (Tuple type*) | (Process type)
       | (Record row) | (Variant row) | (Fn type effect-row type)
       | TypeName | (TypeName type*) | type-variable

row ::= (row (field field-name type)* (tail type-variable)?)
effect-row ::= (effects effect-entry*)
effect-entry ::= Process | EffectName
```

A row tail, when present, is last. Row labels are unique. Tuple and regular
data arities may be zero. The same effect entry grammar is used by `effects`
and `uses`; ordinary effect occurrences retain multiplicity, while the
reserved Process entry denotes the single host effect.

The closed expression grammar is:

> **Normative definition.**

```text
expression ::= integer | true | false | (unit) | (var value-name)
             | (fn (value-name type) expression)
             | (call expression expression+)
             | (let value-name expression expression)
             | (sequence expression expression)
             | (tuple expression*)
             | (record (field field-name expression)*)
             | (select expression field-name)
             | (update expression field-name expression)
             | (extend expression field-name expression)
             | (restrict expression field-name)
             | (inject field-name expression)
             | (construct ConstructorName expression*)
             | (match expression clause+)
             | (annotate expression type)
             | (trait-call TraitName value-name expression+)
             | (request EffectName value-name expression*)
             | (handle HandlerName expression)
             | (resume value-name expression)
             | (spawn qualified-process-name expression*)
             | (self)
             | (send expression expression)
             | (receive clause+)
             | (trap expression)
             | (unary-operator expression)
             | (binary-operator expression expression)

unary-operator ::= not | negate
binary-operator ::= and | or | equal | not_equal
                  | less | less_equal | greater | greater_equal
                  | add | subtract | multiply

clause ::= (case pattern expression)
         | (case pattern (when condition-expression) expression)

pattern ::= _ | integer | true | false | (wildcard) | (bind value-name)
          | (tuple pattern*) | (variant field-name pattern)
          | (constructor ConstructorName pattern*)
          | (as pattern value-name) | (or pattern pattern pattern*)
```

`condition-expression` is an effect-free Boolean expression built only from
integer and Boolean literals, bound variables, unary and binary operators,
tuples, and annotations over that same core. Named condition calls, ordinary
calls, requests, process operations, matches, records, and constructors are
not permitted in a condition position. Structural record patterns and a Unit
literal pattern are not present; selection provides record elimination and a
binder or wildcard matches Unit.

The grammar admits all structural pattern shapes, but the 0.1.8 coverage
decision is deliberately head-bounded: an unguarded binder or wildcard is
exhaustive for any scrutinee; otherwise all Boolean values, all labels of a
closed structural variant, or all constructors of a regular nominal type must
appear as unguarded top-level heads. A variant label or constructor contributes
only when every payload pattern below that head is irrefutable. Integer, tuple,
and open-variant matches therefore require an unguarded catch-all. Complementary
nested constructor-product alternatives are not combined by this kernel.

## Parser limits

An implementation may refuse an otherwise valid input only through a
published implementation limit and its distinct diagnostic. The bootstrap
profile accepts at least 20,000 syntax nodes and nesting depth 1,024. Reaching
either bound reports `SYN003` and publishes no successful output.

## Source locations

Every token and compound form has a half-open source span. Byte offsets are
zero based; line and column numbers are one based. CRLF counts as one line
break. Elaboration MUST preserve the span of the source form that selected or
created each executable core node.

## Relationship to future source syntax

This syntax is a versioned conformance and semantic-kernel input. It does not
settle the full-file ergonomic grammar tracked separately by G014 through
G020. C013 now governs only the pre-lexical source-text envelope. A future
frontend may elaborate to the same typed core only after its own versioned
rules and migration record exist.

Its parsed forms are assigned meaning by
[Static Semantics and Elaboration](static-semantics-and-elaboration.md) and
[Sequential Dynamics](sequential-dynamics.md).
