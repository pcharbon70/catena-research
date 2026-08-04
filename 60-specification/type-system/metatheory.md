---
title: "Type-System Metatheory"
kind: specification
created: "2026-08-01"
status: normative
spec_version: "0.1.1"
tags:
  - catena
  - principal-types
  - program-semantics
  - specification
aliases:
  - "Catena 0.1.1 type-system proof obligations"
---

# Type-System Metatheory

## Normative claims

For the principal core, Catena 0.1.1 claims:

1. **Soundness:** inferred schemes are derivable in the declarative judgment.
2. **Completeness:** every declaratively typable principal-core term is
   accepted, modulo explicit resource limits reported as such.
3. **Principality:** the inferred scheme is at least as general as every other
   valid scheme for the same environment.
4. **Elaboration preservation:** the elaborated explicit core has the inferred
   value type and effect.
5. **Coherence:** an accepted trait use has one evidence meaning independent of
   import and solver order.
6. **Termination:** kinding, unification, row solving, trait resolution,
   associated-type normalization, and core verification terminate on
   well-formed finite input.

For the advanced profile, Catena claims soundness, elaboration preservation,
scope safety for rigid variables and equalities, affine resumption use, and
termination. It does not claim global inference completeness or principal
types.

## Proof outline (non-normative)

The written argument decomposes by solver boundary:

- standard substitution, weakening, and generalization lemmas for rank-1 HM;
- kind preservation and decreasing row normalization for unique and duplicate
  row theories;
- evidence typing plus non-overlap, ownership, coverage, and decreasing
  contexts for trait coherence and termination;
- skolem non-escape and ordered-context reasoning for predicative higher rank;
- branch-local equality substitution and rigid existential scope for GADTs;
- a use-count invariant for affine resumptions; and
- induction over elaboration followed by independent core verification.

### Lemma 1: substitution

If `C ; Γ, x:s ⊢ e : t ! efx` and a value `v` has an instance of `s`, then
substituting `v` for free occurrences of `x` preserves `t`, `efx`, and all
residual constraints after applying the induced type substitution. The proof
is by induction on the typing derivation. The `let` case alpha-renames
quantified variables; the handler case preserves capability identity rather
than equating labels.

### Lemma 2: most-general unifiers

Occurs-checked constructor unification returns an idempotent most-general
substitution. Unique-row unification additionally preserves accumulated lacks
constraints; duplicate-effect unification preserves occurrence multiplicity
and capability identity. In each variable-binding case, any other solution
factors through the returned binding. Row alignment is a permutation of equal
labels followed by the same variable-binding argument.

### Lemma 3: safe closing

`close` quantifies exactly the variables free in the inferred type and
constraints but not in the substituted environment. If the expression is
expansive, closing is permitted only after the empty-effect and no-affine-
allocation premises are derived. Duplicating an instance of the resulting
scheme therefore duplicates a value, not an already performed effect or a
linear resource. If those premises cannot be derived, the monomorphic rule is
the only applicable rule.

### Lemma 4: solver termination and coherence

Value-row solving reduces the number of unmatched known labels or binds an
unbound tail after an occurs check. Effect-row normalization reduces a finite
work list while retaining duplicates. Trait resolution reduces the
constructor measure required of every instance context. Non-overlap gives at
most one head; ownership and consistency make that selection invariant under
imports. Induction over the decreasing resolution tree therefore gives
termination and a unique evidence term up to erased administrative structure.

### Lemma 5: scoped advanced checking

Skolemization replaces every checked universal or existential binder with a
fresh rigid constant. Since unification never binds a rigid constant and the
escape check forbids it in the result environment, it cannot leave its scope.
The same induction applies to GADT equalities because each equality is added
only to one branch context. Disabling generalization in that context prevents
a local equality from being packaged into a supposedly general scheme.

### Lemma 6: affine resumption safety

Core verification assigns a use count of zero or one to every resumption
token. Structural induction on a handler clause shows that no accepted branch
duplicates or stores the token. Lowering preserves the token at its single
resume site; an atomic compare-and-exchange changes its runtime state from
fresh to consumed, so even an unchecked second call cannot invoke the captured
continuation twice.

### Theorem: profile guarantees

For the principal core, induction on Algorithm W uses Lemma 2 at applications,
Lemma 3 at lets, and the induction hypotheses for subterms to establish
soundness. The reverse induction on a declarative derivation chooses the same
most-general unifiers and closing rule, establishing completeness; the
factorization part of Lemma 2 establishes principality. Lemma 4 extends the
argument to residual row and trait constraints. For the advanced profile,
induction on the bidirectional derivation plus Lemmas 5 and 6 establishes
soundness and scope safety without a principality claim. Finally, induction on
the elaboration derivation constructs the explicit core typing derivation,
which the independent verifier checks before lowering.

Effect-aware generalization narrows the classic generalization theorem: a
binding is generalized only when the conditions in
[Principal Inference and Generalization](principal-inference-and-generalization.md)
establish that duplicating its value cannot duplicate an effect or affine
resource.

## Evidence status (non-normative)

The written decomposition and executable model jointly support this
specification slice; they are not a mechanized proof. The conformance suite
must compare inference with a separately implemented declarative checker on a
bounded generated term space, permute solver schedules, test negative scope
and ambiguity cases, verify elaborated core, and run generated BEAM artifacts.

## Falsification and conformance

A counterexample to any numbered claim makes the affected chapter
non-conforming and requires demotion or repair. Passing bounded tests does not
establish an unbounded theorem. These limits and the executable requirements
are specified in
[Diagnostics and Conformance](diagnostics-and-conformance.md).
