---
title: "Governed Scopes, Policy, and Authorization"
kind: specification
created: "2026-08-03"
status: normative
spec_version: "0.6"
tags:
  - authorization
  - governance
  - policy
  - specification
aliases:
  - "Catena 0.6 policy algebra"
---

# Governed Scopes, Policy, and Authorization

## Placement and coverage

Typed specification declarations live in Catena modules. Principals, roles,
policies, evidence envelopes, approvals, and transitions live in the package's
canonical governance bundle. A module declaration MUST NOT contain private key
material or silently define organizational authority.

Policy scopes may target the package, a module, any supported claim subject,
an action, an output, an interface, or a named profile. Scope matching is
additive. Every policy matching an action and subject participates, and all
participating policies MUST allow the request. A narrower policy may require
more evidence or authority but MUST NOT cancel a broader requirement.

No bundle means no policy decision for an otherwise ungoverned `build`, even
when the package uses typed rules. Once a bundle declares governed scopes, no
matching policy is `GOV001` and denies the protected action. An ungoverned
package cannot `publish` or `activate` through the 0.6 package gate.

## Closed policy algebra

A policy requirement is one of these finite data constructors:

- `all` — every child requirement succeeds;
- `any` — at least one child succeeds;
- `threshold` — at least `k` children succeed;
- `role` — at least `k` distinct, valid principals holding a named role have
  approved the exact transition payload;
- `evidence` — at least `k` distinct acceptable evidence records support the
  named claim, kind, or compiler check;
- `action` — the requested action is in a closed allowed set;
- `state` — the replayed lifecycle state is in a closed allowed set;
- `profile` — the exact named assurance profile matches;
- `sequence` — the logical event sequence lies in an inclusive integer
  window; and
- `deny` — an explicit denial with a stable reason.

The algebra has no user functions, recursion, effects, ambient I/O, dynamic
code loading, regex execution, wall clock, randomness, or network lookup. Each
node spends one unit from the shared 20,000-step policy budget. Empty `all`
succeeds, empty `any` and impossible thresholds fail, and invalid thresholds
are malformed policy.

## Distinct actors and records

A key or principal contributes at most once to one threshold, even if its
signature or role appears repeatedly. The same rule applies to evidence IDs.
Threshold children are evaluated independently but duplicate identities do not
create additional authority.

An approval binds the action, subject, prior state, proposed state, claim and
artifact digests, active policy digest, prior transition digest, sequence, and
the identifier and semantic digest of every admitted evidence record. Changing
any bound field invalidates the approval.

## Decision combination

Policy evaluation produces `allow` or `deny` plus an ordered explanation tree.
Malformed policy, budget exhaustion, unknown constructors, missing inputs, an
invalid signature, or an unrecognized subject denies. Implementations MUST NOT
silently ignore a policy they cannot interpret.

If any applicable policy explicitly denies or fails a requirement, the final
decision is deny. This is conjunction across scopes, not last-match or
most-specific-wins behavior.

## Protected actions

`build`, `publish`, and `activate` are the only actions in 0.6:

- `build` checks and stages package artifacts and may emit an unsigned
  candidate signing payload;
- `publish` authorizes making the exact staged artifacts externally available;
  and
- `activate` authorizes the lifecycle transition to `Active`.

An implementation may expose additional ungoverned tool operations, but it
MUST reject them if encoded as a governed 0.6 action.

## Dependency boundary

Governance does not automatically cross a package dependency. An imported
interface contributes only the claims, policy obligations, and artifact
digests that it explicitly exports. A consuming package cannot weaken those
obligations; it may add its own.

## Connections (non-normative)

The restricted-language rationale and wider authorization questions remain in
the [specification and governance synthesis](../../20-notes/language-integrated-specifications-and-governance.md#authorization-policy).
The trust and signature rules consumed by this policy are defined in
[Evidence, Identity, Trust, and Lifecycle](evidence-identity-and-lifecycle.md).
