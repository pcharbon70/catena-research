---
title: "Catena Implementation Limits and Portability"
kind: note
created: "2026-08-17"
maturity: developing
tags:
  - conformance
  - governance
  - language-design
  - specification
aliases:
  - "Catena implementation-limit model"
  - "C012 portability model"
---

# Catena Implementation Limits and Portability

## Executive conclusion

Catena needs finite implementations without letting resource accidents become
language semantics. The workable contract has three distinct layers:

1. language rules decide whether an input is valid and what it means;
2. a repository-governed portable floor says how much of an otherwise valid
   resource dimension every conforming implementation supports; and
3. an implementation profile publishes the actual configured boundary and its
   exhaustion result.

This model completes the implementation-limit class introduced by C009. It
adopts explicit bootstrap floors of 253 callable arguments, 4,096 integer
digits, 65,536 decoded literal bytes when such literals exist, and 1,048,576
bytes per generated BEAM module. It also centralizes the existing 20,000-step
compiler budgets and 1,024-level kernel parser depth. Evidence-only bounds stay
inconclusive, and mailbox capacity remains deployment-defined because OTP
offers interacting heap, queue-storage, distribution, and operating-system
controls rather than one portable message count.

The durable decision is the root
[Catena Implementation Limits and Portability policy](../IMPLEMENTATION-LIMITS.md).
C012 is governance plus executable conformance behavior; it does not create
language revision `0.1.9`.

## Question, scope, and operational standard

The question is not whether implementations have finite memory. They do. The
design question is which finite dimensions can legitimately refuse an
otherwise valid Catena input, how much every conforming implementation must
support, what observations exhaustion produces, and what tooling can discover
before attempting a build.

A successful policy must let a reader answer six questions for every bound:

1. Is this a source validity rule, an implementation refusal, an evidence
   cutoff, a runtime capacity, or not yet applicable?
2. What value is measured, at which pipeline boundary, and in which unit?
3. What portable minimum must every conforming implementation accept?
4. What value did this implementation configure?
5. What stable diagnostic or inconclusive result occurs at exhaustion?
6. Can failure leave any successfully published output?

The model is falsified if a compiler reports a type, coverage, proof, policy,
or runtime result merely because a resource budget ended; if two compiler
documents disagree about the configured limit; if an input below the portable
floor is refused for that dimension; or if runtime pressure silently changes
message targeting, live-target delivery, or per-sender order.

## Relation to the current corpus

[Catena Conformance Vocabulary](../CONFORMANCE-VOCABULARY.md) already separates
an implementation limit from invalid input: the input is otherwise valid and
the refusal uses a distinct limit diagnostic. Before C012, however, that policy
left the set of variable limits and their portability contract to G012. The
normative areas then supplied local facts without one cross-area model:

- [data and patterns](../60-specification/data-and-patterns/README.md) promises
  at least 20,000 usefulness steps and reserves `M004`;
- [clause conditions](../60-specification/clause-conditions/README.md) separates
  a 20,000-step normalization refusal (`CND007`) from conservative fact
  analysis returning `unknown`;
- [traits](../60-specification/traits-and-categorical-operations/README.md)
  gives trait resolution and package specialization distinct 20,000-step
  limits (`TRT008` and `TRT007`);
- [specifications and governance](../60-specification/specifications-and-governance/README.md)
  bounds exact examples and aggregate policy evaluation (`EVD003` and
  `GOV002`);
- the [formal semantic kernel](../60-specification/formal-semantic-kernel/README.md)
  bounds parsing, reference execution, and schedule exploration while
  assigning different meanings to parser refusal and unfinished exploration;
  and
- [C010 actor semantics](../60-specification/formal-semantic-kernel/actors-messages-and-failures.md)
  fixes local message order and receive behavior but deliberately excludes a
  full deployment-capacity and supervision policy.

The sibling compiler disclosed these values in prose, but production modules
also held separate constants. That made the intended limits visible yet left
drift possible. C012 turns the scattered values into a common governance
contract and one executable compiler registry without rewriting the local
normative rules that own each diagnostic.

## Target-runtime evidence

The [OTP 29 system-limit note](../30-sources/erlang-otp-29-system-limits.md)
records the hard target fact that a function accepts at most 255 arguments.
Catena's current effect-directed CPS worker adds handler state and a
continuation. A source function with 253 explicit arguments therefore produces
the worst-case arity-255 worker. Publishing 255 as the Catena source floor
would work only for pure direct lowering and would make portability depend on
an optimization or effect classification.

The 253 floor is consequently derived from the complete lowering, not copied
from the target ceiling. It is high enough to avoid practical source pressure,
low enough to cover every current callable lowering, and directly testable at
the boundary pair 253/254.

The [OTP runtime-control note](../30-sources/erlang-otp-29-runtime-resource-controls.md)
shows why the same reasoning does not yield a mailbox count. Messages differ
in size, can be stored on or off the process heap, can contribute differently
to maximum-heap checks, and can encounter distribution backpressure or host
memory pressure. A count chosen here would either be false portability or a
new runtime admission design. C012 therefore publishes the capacity as
deployment-defined and carries explicit semantic constraints forward to G068
and G129.

## Choosing bootstrap floors

### Callable arity: 253

The measured value is the maximum explicit source arity after the compiler has
normalized its callable representation. Both JSON and kernel paths must reject
source arity 254 as `LIM001` even where a particular pure backend path could
fit. Generated forms receive a second check at the real OTP ceiling so a
lowering bug cannot create arity 256 behind a valid source boundary.

This choice intentionally values predictable cross-feature portability over
two extra arguments for pure functions. A later backend may remove the hidden
arguments, but that optimization alone does not lower or raise the portable
floor.

### Integer magnitude: 4,096 decimal digits

The current compiler already accepts arbitrary-precision integers through
both retained JSON and exact kernel inputs. Unbounded literal decoding permits
cheap adversarial amplification, while a small machine-word floor would
contradict the implemented mathematical-integer model. Four thousand
ninety-six decimal digits is a generous portable baseline and a crisp decoded
value boundary.

The measurement excludes a leading minus sign. C017 now defines bases and
separators and measures every based spelling by the decimal digits in its
mathematical value. Floating-point rules and fixed-width arithmetic remain
G018. The retained frontends and C017 scanner accept 4,096 digits and report
`LIM002` at 4,097.

### Decoded literal payload: 65,536 bytes

C012 originally reserved this floor while no string or binary term literal
existed. C017 now activates it as `LIM004`: text is measured in decoded UTF-8
payload bytes and byte literals in decoded octets, after escape processing.
Text remains unnormalized and non-interpolating, so neither transformation is
part of the measurement. This activation demonstrates why reserving the
dimension prevented a later feature from inheriting an undocumented compiler
default.

### Generated module: 1 MiB

A generated-module size limit protects the final OTP boundary from pathological
output amplification. Measuring the completed binary before publication makes
the rule independent of source syntax and internal form count. One MiB is a
minimum support guarantee, not a recommended module size and not a promise that
all source inputs whose output would be smaller survive other checks.

The bootstrap uses `LIM003` for the first byte beyond its configured limit. The
check belongs at the sole OTP compiler boundary so JSON compilation, kernel
compilation, package specialization, and later callers cannot bypass it.

## Existing budgets: preserve meaning, centralize values

C012 does not reinterpret every 20,000-step number as the same algorithm. It
centralizes the value and common diagnostic fields while preserving ownership:

| Activity | Meaning at exhaustion |
| --- | --- |
| Pattern coverage | compiler refusal `M004`, not evidence of non-exhaustiveness or redundancy |
| Condition normalization | compiler refusal `CND007`, not evidence that the condition is unsafe |
| Trait resolution | compiler refusal `TRT008`, not proof that an implementation is absent |
| Package specialization | build refusal `TRT007`, not permission for runtime dictionaries |
| Exact example evaluation | evidence refusal `EVD003`, not a counterexample |
| Governance policy evaluation | `GOV002` plus conservative denial, not an ordinary evaluated policy denial |
| Kernel parser | `SYN003`, distinct from malformed syntax |

Condition fact construction, reference execution, and schedule exploration
are different. Their results are evidence about a program, so exhaustion must
remain `unknown`, `budget_exhausted`, or `exhausted`. Treating those outcomes
as source rejection would make acceptance depend on a testing budget rather
than the normative language.

## One executable registry and one profile

The compiler now places active limits in `Catena.ImplementationLimits`.
Production checks, common diagnostic details, conformance tests, and
`catena conformance-info` consume the same registry. Human-readable
`CONFORMANCE.md` explains the release but is not a second configuration
source.

The profile includes empty implementation-defined and extension collections,
not only nonempty variability. It also reports permissions,
recommendations, bounded presentation, evidence bounds, and mailbox
constraints. That wider shape follows C009: a tool inspecting portability
should not need a different command when Catena eventually introduces its
first real implementation-defined choice.

The common refusal fields—limit ID, portable minimum, configured value,
observed value, and unit—support automation without freezing diagnostic prose.
They also make boundary tests precise and expose a compiler configured below
the corpus minimum.

## Transactionality and hostile input

Limit checking is part of the existing transactional failure model. An
oversized integer is rejected after decoding the JSON number but before typed
elaboration. Source arity is checked before backend work and again after the
kernel has flattened nested lambdas. Generated arity is checked before OTP
compilation, and BEAM bytes are checked before the compiler returns a
successful artifact.

This layered placement is deliberate. Measuring too early can miss elaborated
or generated amplification; measuring only at the end wastes resources and
can turn an anticipated source refusal into an opaque backend failure. The
checks do not replace general denial-of-service work: aggregate file size,
parser token amplification, memory behavior, concurrency quotas, and hostile
package graphs remain in G126–G131 and the whole-language performance program.

## Rejected alternatives

- **Copy every OTP maximum into Catena.** Most target ceilings are irrelevant
  until the language exposes a corresponding form, and several depend on word
  size, configuration, or operating-system resources.
- **Promise no portable minima.** Profiles would disclose incompatibility only
  after implementations had already fragmented, leaving packages unable to
  choose a useful baseline.
- **Make every limit fixed forever.** Implementations should be able to support
  more than the baseline and tune evidence exploration; the invariant is the
  floor and specified exhaustion, not identical resource provision.
- **Use one generic “resource exhausted” diagnostic.** It would erase the
  repair and ownership distinction among source arity, parser depth, coverage,
  evidence, artifacts, and governance.
- **Treat evidence exhaustion as invalidity.** This would manufacture semantic
  conclusions from incomplete search.
- **Set a numeric mailbox floor now.** OTP exposes no stable message-count
  capacity independent of message size, storage strategy, process heap,
  distribution, and host policy.
- **Wait for an implementation-defined choice before machine-readable
  output.** C012 already introduces portable automation needs and benefits
  from testing profile determinism before such choices exist.

## What this brings to the design

The policy gives package authors a real portability baseline, compiler authors
a measurable contract, and conformance tests exact boundary pairs. It prevents
finite-resource behavior from masquerading as type or semantic evidence,
preserves transactional artifact guarantees under resource refusal, and makes
deployment capacity visible without prematurely standardizing an operations
policy.

It also clarifies future design work. C017 activates the inherited payload
contract as `LIM004`; G068 and G129 own explicit capacity and failure semantics rather
than a silent mailbox cap; G126–G131 can build threat, TCB, reproducibility,
unsafe, and supply-chain policy on top of stable resource classifications; and
later semantic slices remain separate from this governance milestone.

## Falsification criteria and remaining work

The design needs revision if 253 explicit arguments cannot be lowered through
every current callable path, if boundary tests disagree across frontends, if
the generated-module check can be bypassed, if profile bytes are unstable for
one compiler build, or if a supposedly inconclusive evidence cutoff changes
source acceptance.

C012 does not close aggregate source-size policy, memory accounting, parser
time complexity, compiler cancellation, distributed delivery, supervision,
backpressure, or hostile dependency graphs. Those remain explicit work rather
than hidden qualifications on this milestone.

## Connections

- [How Should Catena Bound Implementation Limits?](../40-inquiries/how-should-catena-bound-implementation-limits.md)
  records the operational question and resolution.
- [Implementation Limits and Portability map](../10-maps/implementation-limits-and-portability.md)
  routes through sources, policy, corpus owners, and executable evidence.
- [Conformance Traceability](../10-maps/conformance-traceability.md) registers
  `IL-OBL-001` through `IL-OBL-012`.
- [C012 Implementation Limits](../50-journal/2026-08-17-c012-implementation-limits.md)
  records the coordinated compiler identity and verification.

## Sources

- [Erlang/OTP 29 System Limits](../30-sources/erlang-otp-29-system-limits.md)
- [Erlang/OTP 29 Runtime Resource Controls](../30-sources/erlang-otp-29-runtime-resource-controls.md)
- [Erlang/OTP 29 Processes](../30-sources/erlang-otp-29-processes.md)
