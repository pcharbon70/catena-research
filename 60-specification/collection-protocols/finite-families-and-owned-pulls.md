---
title: "Finite Families and Owned Pulls"
kind: specification
created: "2026-09-09"
status: normative
spec_version: "0.1.65"
tags: [specification, collections, conformance]
aliases: []
---

# Finite Families and Owned Pulls

## Status and authority

This C102 contract applies to edition `0.1`, semantic revision `0.1.65`, without
previews, under the [authority policy](../../SPECIFICATION-AUTHORITY.md),
[conformance vocabulary](../../CONFORMANCE-VOCABULARY.md), and
[implementation limits](../../IMPLEMENTATION-LIMITS.md). It completes the
[reviewed collection gate](../../20-notes/language-completion-plan-delivery.md#item-102-collection-protocols)
through an explicit standard package and checked operation descriptors.
Role names here identify internal contracts; they do not adopt public vocabulary,
implicit imports, generalized comprehension syntax, or implicit lazy evaluation.
Retained source, interface, executable and signed formats are unchanged
(`CL-OBL-001`).

This chapter supplies the library contracts delegated by
[C042](../collection-construction-and-update/README.md). It preserves C035's
[comparable set](../equality-and-ordering/the-comparable-set.md), C004's
[operational laws](../traits-and-categorical-operations/operational-semantics.md),
C103's [outcome separation](../outcome-contracts/values-sequencing-and-validation.md),
and C080's [mandatory cleanup](../resource-scopes/owned-lifetime-and-mandatory-cleanup.md).
Records remain structural products, not keyed collections.

## Finite families and order

The explicit package declares ordinary nominal Sequence, Keyed, Unique, PullStep
and FoldStep roles. Sequence is an empty-or-head/tail family. Keyed and Unique
have abstract construction and expose ordered sequence views. PullStep is
end-with-state or yield-with-item-and-state. FoldStep is continue-or-stop with
an accumulator. The package binds its complete content and canonical categorical
hierarchy; changing content and recomputing a digest does not authorize a new
package. It compiles using the retained ordinary `0.1.4` frontend and uniform
nominal layout. The package and existing comprehension List remain distinct;
conversion between their sequence carriers is explicit.

The checked finite-operation descriptor binds exact revision, family, value
codec and ordering evidence. Its external payload profile uses C095 closed-data
codecs. Ordinary compiler-established categorical methods remain polymorphic;
that does not widen this external callback boundary to arbitrary nominal,
effectful or resource-capturing values.

Lists preserve input order and repetition. Maps and sets enumerate strictly
ascending semantic keys. Admitted key kinds are Int, finite Float, Text,
Character and Bytes, with C035 order and equality. Boolean comparability does
not supply ordering. Ordering evidence is a closed derivation for one admitted
kind, not an arbitrary comparator or a sample-based law certificate. Unsupported
kinds, changed evidence and noncanonical imported sequences are refused.
Float identity retains both signed zeros; negative zero precedes positive zero.
Text order is scalar-content order, not locale collation (`CL-OBL-002`).

## Construction, lookup and update

Construction validates the complete input carrier and element types before
building. A strict map or set builder examines keys in input order. Its first
repeated key yields C103 dependent failure containing that key and the zero-based
index of its second occurrence; it never silently keeps, replaces or combines a
duplicate. Success contains the canonical nominal collection. List construction
returns success with the input sequence. Complete result bounds include the
outcome wrapper (`CL-OBL-003`).

Keyed lookup returns C103 optional presence or absence. List indexing is
zero-based Int; negative and out-of-range indexes are absence. Existing-key
replacement returns optional presence of a new map, or absence if no key exists.
The original map remains unchanged. This operation does not insert a missing key.
Set transformation applies its checked pure function in source-key order and
uses strict target construction, so collisions remain typed failures.

The explicit ordered combining builder invokes a checked pure binary operation
only when a key repeats, in original input order, with old value before new
value. It sorts only the final distinct keys. Purity alone does not establish
associativity. Separately admitted lawful evidence covers mathematical Int sum,
minimum and maximum: each is associative and commutative; min/max do not claim
an identity for empty input. Arbitrary or modified law evidence is refused.
No Float associativity is inferred from mathematical real arithmetic
(`CL-OBL-004`).

## Mapping, folds and traversal

Sequence and partially applied Keyed have Mapper and Reducible dictionaries.
Keyed mapping preserves keys and order, transforming values only; its categorical
reduction visits values in key order. Explicit entry folds visit key/value pairs.
Unique has no unconstrained Mapper dictionary, since a mapping can collapse keys.
Identity and composition preserve shape and element results for pure total
functions. Divergence and terminal traps retain their ordinary semantics.

The checked operation boundary requires a verified compiled pure unary callback,
including exact input/output codecs and immutable checked captures. A tuple
adapts binary operations and accumulator/element steps. Raw host functions and
compiled effectful stages cannot claim purity. Ordinary typed dictionaries use
the compiler-established pure method ABI; raw host test harnesses are not a
purity proof (`CL-OBL-005`).

Mapping and folds traverse left to right, or ascending keys. Early-stop folds
invoke no callback after the first stop. Complete finite input validation still
precedes the first callback. Traversal explicitly selects optional, dependent or
independent validation. Its callback wire variant has success and failure roles;
optional failure carries Unit, the others carry the declared error type. This is
an explicit C095-to-C103 adapter, not an implicit outcome coercion.

Optional/dependent traversal stops at its first failure. Independent validation
visits every input and accumulates one error per failed callback in traversal
order, returning a nonempty error sequence when invalid. Success preserves list
shape or map keys. Empty traversal returns the corresponding successful empty
collection. A callback trap is never collected as an expected error and stops
execution immediately (`CL-OBL-006`).

## Owned pull protocol

An owned pull session takes a checked initial state, item/state codecs, exact
trusted P096 pull and release declarations, explicit grants and finite bounds.
Both declarations use the retained `0.1.61` authority boundary. Pull accepts
state and returns the explicit end/yield wire variant; release accepts state
and returns Unit. Both must already be granted before session entry. There is
no ambient host lookup, native handle ingress, implicit acquisition, or inference
of release authority from a function name (`CL-OBL-007`).

The session starts without pulling. Each next request invokes at most one pull.
A successful yield records its returned state before exposing optional item
presence. End records its state, releases once and caches terminal absence;
subsequent next requests do not invoke the source. Explicit close, body return,
body trap and owner death attempt release with the last accepted state. Repeated
close does not repeat release. Public handles are owner-scoped, expire with the
session and supply no admitted transferable process authority.

A bounded collection consumer stops at its item cap without pulling one extra
item to discover whether a suffix exists, then closes. A checked pure early-stop
consumer similarly closes immediately after stop. An abandoned iterator therefore
releases even when no item was requested. Streams are explicit owned pull
computations, distinct from eager finite values (`CL-OBL-008`).

A failed or timed-out pull closes further pull admission. A timeout requests
cooperative cancellation and does not accept a later returned state. Release
uses the last accepted state. A trusted source must make that state sufficient
to release its resource even after interrupted work; authority and nominal state
shape alone do not prove a host resource implementation correct. P096's external
side effects remain possible: cancellation is not rollback.

One operation slot is reserved for release. Release is attempted once; a failed
attempt is cached, not retried. Scope cleanup waits for the typed release and
nested foreign-scope cleanup. Missing confirmation is a mandatory cleanup trap,
subject to C080's primary/secondary failure precedence. A logical process stop
is not evidence of external-resource reclamation (`CL-OBL-009`).

## Costs, bounds and failure

Let n be input cardinality, p completed/attempted pulls, S the complete carrier
size, K key comparison/identity cost, and F total callback work. These bounds
separate collection work from codec validation, arbitrary callback computation,
compiler verification and finite-resource exhaustion.

| Operation | Collection work and storage |
| --- | --- |
| Sequence construction, mapping and reduction | O(n) structural work; mapping/construction allocate O(n); reduction's loop is tail recursive apart from callback work. |
| Strict keyed construction | O(n log(n + 1)) key comparisons/identity-map operations with scalar costs charged separately; O(n) retained entries. |
| Checked lookup/index | O(n) scan, following complete O(S) validation; no constant-time dictionary promise. |
| Existing-key replacement | O(n log(n + 1)) bound from scan and canonical sort; O(n) new structure. |
| Ordered or lawful combining | At most n duplicate checks and n−1 combining calls, then canonical sort; O(n) retained distinct entries plus callback values. |
| Mapping/fold/traversal | O(n) structural work plus F; outcome accumulation is linear, not repeated append; whole result validation adds its carrier cost. |
| Pull session | One host operation per admitted next and at most one release; latest state/item plus P096's O(p) retained call/event evidence, bounded by the step cap. |
| Bounded stream collection | O(p) list construction plus final complete-carrier validation, O(p) retained items; no unbounded constant-space claim. |

Every external finite input, returned complete result and callback conversion
uses explicit C095 node/byte/depth bounds. Tuple/map children increase depth;
list tails use the standing C095 rule. Nominal Sequence depth grows with
cardinality. Carrier preflight is not promised constant-stack: its resource
usage and maximum depth remain charged. Large tail-safe structural folds do not
remove that conversion boundary. Limit refusal is distinct from typed lookup
absence and duplicate failure. Callback work has no newly invented termination
bound; inherited runtime resource rules apply.

Pull timeout defaults to 1000 milliseconds and admits 1–1,000,000. Step cap
defaults to 1024 and admits 1–1,000,000 attempted pulls, including end. Bounded
collection caps admit 0–1,000,000 items. Unknown or duplicate options are refused.
A public wait includes 100 milliseconds of dispatch allowance. Scope release
allows twice the pull timeout plus 200 milliseconds; its private reply wait is
twice the timeout plus 100 milliseconds. Exhausted steps refuse further admission;
exhausted conversion/collection bounds return a classified limit error, and
mandatory cleanup still runs. Finite bounds are explicit caller budgets, not a
new reduction of the repository's portable source/code minima (`CL-OBL-010`).

## Variability register

The operation family, codecs, closed ordering/combining evidence and traversal
mode are explicit inputs. Pull timeout, attempted-step cap and collection item
cap have the fixed ranges/defaults above. Node/byte/depth budgets use C095;
source/core/compiler/resource policies remain applicable. Clock scheduling can
exhaust a configured wait; no variable key order, hidden comparator, automatic
retry or unreported partial successful collection is admitted.

## Rationale and evidence (non-normative)

The [implementation journal](../../50-journal/2026-09-09-collection-protocols.md)
records the four-option decisions, compiled ordinary package/dictionaries,
independent algebraic/structural models and owned-source traces. The earlier
[collection synthesis](../../20-notes/catena-collection-operations.md) explains
why categorical laws, operational order, typed misses and costs are separate
contracts. Public vocabulary remains a later adoption gate.
