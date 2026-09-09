---
title: "Explicit Minimum and Component Identity"
kind: specification
created: "2026-09-09"
status: normative
spec_version: "0.1.69"
tags: [specification, prelude, standard-library, conformance]
aliases: []
---

# Explicit Minimum and Component Identity

## Status and authority

C101 defines edition `0.1`, exact semantic revision `0.1.69`, without previews,
under [authority](../../SPECIFICATION-AUTHORITY.md),
[conformance vocabulary](../../CONFORMANCE-VOCABULARY.md) and
[implementation limits](../../IMPLEMENTATION-LIMITS.md). It executes the
[reviewed minimum-prelude plan](../../20-notes/language-completion-plan-delivery.md#item-101-minimum-prelude).
The minimum is an explicit assembly of ordinary library components and existing
checked operation contracts. It introduces no primitive type, implicit import,
public vocabulary, general-purpose source parser or new retained interface/BEAM
format (`MP-OBL-001`).

## Minimum semantic inventory

The following families form the pure minimum. Their referenced normative owners
retain their types, constructors, method ABI, laws, failure behavior and execution
order. Inclusion does not broaden their admitted domains (`MP-OBL-002`).

| Family | Minimum contents | Governing contract |
| --- | --- | --- |
| Core values | Int, finite Float, Bool, Unit, Character, Text, Bytes; products, variants, functions and ordinary nominal data | [C040 data model](../built-in-data-model/README.md) and [C093 value boundary](../value-boundaries/README.md) |
| Foundations | Polymorphic identity, constant, forward composition, product construction and two projections | Rules below |
| Categorical hierarchy | The existing 17 capabilities, exact minimal methods, parents and coherent evidence; existing List map and fold instances | [C004 hierarchy](../traits-and-categorical-operations/standard-hierarchy-and-vocabulary.md) and [operational rules](../traits-and-categorical-operations/operational-semantics.md) |
| Outcomes | Optional absent/present; dependent failure/success; independent accumulating validation; sequences and nonempty error sequences; mapping, embedding, folding, chaining where lawful, binary mapping, error mapping and explicit conversions | [C103 outcomes](../outcome-contracts/values-sequencing-and-validation.md) |
| Collections | Finite sequence, keyed map, unique set, fold-step and pull-step roles; ordinary constructors/eliminators, strict construction, lookup/update, ordered mapping/folding and owned pull protocols | [C102 collections](../collection-protocols/finite-families-and-owned-pulls.md) |
| Text and binary | Distinct byte/scalar/grapheme index roles, explicit offsets, measurement/slicing, Unicode normalization, strict encodings and checked binary operations | [C104 text and binary](../text-binary-model/units-unicode-and-checked-binary-operations.md) |
| Numeric library | Ordinary Decimal construction/elimination, exact checked Int arithmetic, Euclidean division, finite binary64 operations, explicit rounding/conversions, decimal contexts, exact formatting/parsing and square root | [C105 numerics](../numeric-library/checked-arithmetic-and-explicit-rounding.md) |

Collection Keyed and Unique representations stay abstract. Outcome, collection,
text-index and Decimal nominal identities remain those of their original modules;
assembling the minimum neither clones nor renames their types. A trait's inclusion
is not evidence that every container has that trait: dependent sequencing and
independent accumulation retain C103's different lawful structures.

The separately selectable environmental contract contains C106's eight service
roles: I/O, filesystem, network, time, randomness, environment, logging and process.
Its authority remains [explicit and owned](../environmental-effects/explicit-authority-and-closed-launches.md).
It is never a pure instance, implicit compiler input or consequence of importing
a pure component (`MP-OBL-003`).

## Ordinary foundation meaning

Foundation operations are ordinary polymorphic functions with empty effect rows.
Identity returns its argument. Constant takes a value and a second argument and
returns the first value; ordinary strict evaluation still evaluates both arguments
before a saturated call. Product construction returns its two values in order;
first and second projection return the corresponding product component.

Forward composition takes a pure function from a to b, a pure function from b to c,
and an a value. It invokes the first function once, passes the resulting b to the
second function once, and returns the c. Partial application follows C032's
[function contract](../functions-and-calls/README.md). Identity on either side and
associativity hold in the pure, total domain; product projection/construction
obeys its two projection equations. No law permits duplication, reordering or
suppression of observable callbacks or failures outside that domain (`MP-OBL-004`).

These functions are delivered as ordinary checked JSON definitions in an internal
foundation module. Internal role labels do not add public names or new trait
instances. The existing categorical method ABI, including left-to-right compose,
is unchanged.

## Exact package and component selection

The internal minimum catalog has format catena-minimum-standard, semantic contract
0.1.69, package identity catena-minimum at package version 0.1.0, the retained
hierarchy digest, five component identities, environmental-contract metadata,
primitive inventory and explicit exclusions. Each component identity contains its
original semantic contract, origin, module, value/type export inventory and content
digest. Its complete canonical payload is SHA-256 bound. Verification compares
the supported catalog and all component content; merely recomputing a hash after
changing a field cannot authorize a different package (`MP-OBL-005`).

The ordinary component versions are foundation 0.1.69, outcomes 0.1.54, collections
0.1.65, text 0.1.66 and numeric 0.1.67. Every component binds the original hierarchy
0.1.4. Package version 0.1.0, semantic contract 0.1.69, component contracts and
compiler release identity are distinct axes. This assembly does not reinterpret
old exact artifacts.

The separate selection manifest has exactly format, version, package,
package_version, digest and services fields. Its format is catena-minimum-selection,
version is 0.1.69 and the package/version/digest must select the supported catalog.
Services is an explicit Boolean controlling availability of the environmental
entry contract; true grants no authority. An absent selection or null selects
nothing. Extra fields, an unknown digest/version, malformed services, a missing
selected package or duplicate matching packages refuse selection. Resolution
returns either the exact verified context or a boundary error (`MP-OBL-006`).

## Prelude dependency and names

The minimum can be selected through the existing C026
[prelude dependency mechanism](../prelude-policy/prelude-selection-and-admission.md#the-prelude-field)
with its exact package version. It resolves as an ordinary C025 dependency. Its
bundle digest includes the catalog/component digests and all five compiled
interface digests. Lock generation is deterministic; exact replay verifies the
resolved content and rejects a changed lock, substituted package or opt-out
mismatch. This profile uses exact lock bytes for replay rather than accepting
alternative serializations (`MP-OBL-007`).

The catalog root exports no flattened value/type spellings. Its selected component
interfaces are available explicitly to the retained checker; component-qualified
types and constructors and explicit constructor aliases use their ordinary
admission rules. It does not place each component's values into a global source
environment. Conflicting aliases fail under the retained checker. Existing C026
unqualified import precedence for an actual exporting prelude origin is unchanged.
No special tier, silent preference or directory-dependent lookup is added.

Opt-out supplies no standard component interfaces or libraries. Empty ordinary
programs still compile, and built-in language types remain built-in. An opted-out
program cannot use a standard nominal type merely because its package is shipped
with the compiler. Selecting the catalog likewise does not make an unqualified
foundation function an implicit source name (`MP-OBL-008`).

## Checked executable delivery

Selected components compile under their retained ordinary-language profile and
uniform layout. Their interfaces are decoded and checked against the retained
hierarchy digest before supplying them to an application. The compilation result
contains the component binaries/interfaces and application binary/metadata with
its explicit selection and catalog digest; compilation performs no module loading
or host service action. Failure publishes no successful assembly result.

This delivery supports actual ordinary nominal-data transformation and validation
applications through explicit selected interfaces. Foundation functions and
component APIs are compiled ordinary exports callable through their existing
checked call contracts. It does not invent a new general source value-import form
or automatically link every public spelling (`MP-OBL-009`).

Selected text/numeric operation programs delegate checking, lowering and invocation
to their exact existing artifact owners. Both preparation and invocation verify
selection; opting out cannot reuse an artifact to bypass selection. Environmental
entry preparation additionally requires services selected, and invocation still
requires a live explicit C106 authority bundle. Missing services, wrong operation
schemas or an unverified component artifact refuse execution before successful
publication. Component compilers and their exact artifacts retain all input/output,
lifetime and full compiler-identity obligations (`MP-OBL-010`).

## Bounds, costs and exclusions

Selection JSON has at most 16,384 bytes and the supplied catalog candidate list
at most 64 entries. The supported catalog contains exactly five ordinary modules
and eight environmental roles; these are fixed profile/schema bounds, not
extensible runtime registries. Invalid contexts, catalogs, selections or lock bytes
are boundary errors. Inherited C012 source, inference and generated-code limits,
C095 carrier limits and each selected operation's resource contract apply.

Catalog verification processes all pinned component data. Library assembly compiles
all five components; lock creation also compiles their interfaces before deriving
bundle identity. These are explicit work and allocation costs, not constant-time
lookup promises. Foundation functions add constant non-callback work; composition
adds the actual work of both callbacks, and partial applications retain their
captured values. Existing collection traversal, Unicode, numerical and service
costs remain those of their owners (`MP-OBL-011`).

Public naming and source grammar remain P107/P109. Effectful foreign callbacks
remain P096; general comprehension syntax remains D059; transcendental admission
remains NL-T01; library-wide stability/performance policy remains P108; source
release readiness remains G141. A working minimum does not close those owners or
claim whole-language composition and release evidence.

## Variability register

The supported catalog, component identities, pure foundation semantics, zero
implicit names and exact lock replay are fixed. Selection, opt-out and the services
Boolean are explicit inputs. Manifest/candidate bounds are fixed above; inherited
source, carrier and component limits apply. No ambient authority or host-dependent
categorical law is introduced.

## Rationale and evidence (non-normative)

The [implementation journal](../../50-journal/2026-09-09-minimum-prelude.md) records
four-way decisions, exact catalog/component identities, actual applications and
refusal tests. The [combinator synthesis](../../20-notes/combinators-for-algebraic-data-and-categorical-programming.md)
explains the small compositional foundation. Component law and operational evidence
remain linked through their existing normative owners and conformance records.
