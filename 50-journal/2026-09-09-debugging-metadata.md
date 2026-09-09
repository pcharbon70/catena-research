---
title: "Debugging Metadata Implementation"
kind: journal
created: "2026-09-09"
tags: [language-design, compiler, conformance]
aliases: []
---

# Debugging Metadata Implementation

## Starting point and scope

C098 merged through [compiler PR 145](https://github.com/pcharbon70/catena/pull/145)
and [research PR 95](https://github.com/pcharbon70/catena-research/pull/95).
Compiler `rewrite` was `5df5a73b5ccc44a457596d83f102b1f77b03388b`;
research `main` was `8b4f9d82307ce306b9258b5c69221975b0611dc3`.
Both integration branches were synchronized before their feature branches were
deleted. This slice uses `codex/debugging-metadata`; the user's session-wide
revision approval covers `0.1.64`. No continuation is scheduled.

The [CP-100 plan](../20-notes/language-completion-plan-delivery.md#item-100-debugging-metadata)
and [original decision register](../20-notes/design-decision-register.md)
require source/runtime/evidence navigation without violating erasure. The
[normative C100 chapter](../60-specification/debugging-metadata/verified-origins-and-redacted-frames.md)
retains the public-vocabulary boundary.

## Implementation decisions

| Decision | Four alternatives explored | Recommended and selected |
| --- | --- | --- |
| DB-I01: Runtime metadata | A: embed source/evidence; B: external verified sidecar plus virtual runtime tokens; C: discard origins; D: absolute host paths. | **B.** Preserves erasure and relocation while making actual frames navigable. |
| DB-I02: Source trust | A: trust caller-edited spans; B: recheck original source and independently verify core; C: trust a sidecar checksum alone; D: infer source from function names. | **B.** Origin claims must be rebuilt from the selected trusted source bundle. |
| DB-I03: Runtime identity | A: module name alone; B: digest of runtime forms in virtual filename; C: full source digest in BEAM; D: random build identifier. | **B.** Separates different executable programs without embedding erased evidence identity. |
| DB-I04: Source-variant ambiguity | A: pretend BEAM chooses one erased variant; B: require externally selected trusted source input; C: weaken erasure; D: silently choose the newest sidecar. | **B.** Identical runtime bytes cannot identify every possible source/evidence variant. |
| DB-I05: Coordinates | A: byte columns; B: original byte ranges and Unicode-scalar columns; C: grapheme columns; D: positions in reserialized JSON. | **B.** Matches source tooling and keeps original carrier locations reproducible. |
| DB-I06: JSON locators | A: concatenate every key with a dot; B: quote non-identifier keys in bracket segments; C: discard unusual keys; D: use decoded-value equality as location. | **B.** Prevents literal dotted keys from impersonating structural descendant paths. |
| DB-I07: Coordinate scanning | A: rescan every prefix per node; B: collect ranges then resolve endpoints in one UTF-8 pass; C: store every source prefix; D: omit non-ASCII coordinates. | **B.** Avoids quadratic indexing cost and retains exact original endpoints. |
| DB-I08: Generated history | A: nearest span only; B: primary span plus bounded explicit generated chain and omitted count; C: unbounded provenance graphs; D: mark generated coordinates as user lines. | **B.** Keeps the useful source location even when optional history is truncated. |
| DB-I09: Inlining | A: unrestricted textual substitution; B: depth-bounded closed zero-argument expression substitution; C: mutate OTP internals; D: claim optimizer-elided calls still exist. | **B.** Provides executed expansion evidence without variable capture or invented physical frames. |
| DB-I10: Optimizer scope | A: claim all optimization disabled; B: compare the explicit Catena pass on/off under the same supported OTP optimizer; C: use undocumented no-copt flags as authority; D: skip optimized witnesses. | **B.** The tested claim is precise and does not depend on undocumented compiler switches. |
| DB-I11: Foreign boundary | A: synthesize an absent request stack; B: retain one actual exported-entry frame; C: retain every recursive worker frame; D: disclose the native failure object. | **B.** Reports the honest entry-definition granularity while preserving tail recursion and redaction. |
| DB-I12: Foreign authority | A: debug mode bypasses grants; B: reuse exact descriptor authorization and codecs; C: infer authority from source paths; D: expose ambient MFA lookup. | **B.** Debugging cannot broaden the admitted capability program. |
| DB-I13: Disclosure | A: unrestricted arguments; B: default redaction with an explicit complete-tuple codec and budgets; C: redact strings only; D: no structural frame information. | **B.** Preserves useful structure while refusing untyped or oversized value disclosure. |
| DB-I14: Erased evidence | A: copy checkers into debug chunks; B: external digest/locator/span references; C: lose all navigation; D: auto-fetch arbitrary evidence URLs. | **B.** Supports navigation without executable payloads or ambient file/network authority. |
| DB-I15: Stripping | A: nearest-span guessing; B: omit runtime lines and leave frames unmapped; C: pretend sidecar presence restores all runtime locations; D: silently switch back to full metadata. | **B.** Information loss stays explicit. |
| DB-I16: Versioning | A: widen 0.1.59 calling artifacts; B: exact 0.1.64 debug artifacts with retained source/interface/governance formats; C: relabel old evidence; D: implicitly select the latest debug rules. | **B.** Makes the new metadata and disclosure contract reviewable without revising historical formats. |
| DB-I17: Bounds | A: unlimited source/nodes/history; B: explicit byte/node/depth/chain limits; C: hidden machine-dependent truncation; D: fixed tiny programs only. | **B.** Build refusals and history truncation have declared, reproducible meanings. |
| DB-I18: Historical backend behavior | A: globally rewrite all annotations; B: opt-in process-local origin capture restored after lowering; C: global mutable registry; D: a separate unverified compiler copy. | **B.** Both current lowering owners participate while retained lowering remains unchanged without the new profile. |

## Implementation and evidence

`Debugging` rebuilds the sidecar from trusted original source bytes and normalized
logical paths. Both backend owners use `Debugging.Origins` only inside a bounded
build context. Kernel nodes retain actual parser spans. Ordinary JSON uses a
carrier-path index; ranges are resolved against original bytes in one UTF-8 pass.
`SourceSpan` and `Kernel.Node` supply coordinate and identity helpers.

`Debugging.Lowering` assigns virtual lowered-location tokens and bounded chains.
Its restricted inline pass retains actual callee fault spans and call sites.
The virtual filename binds emitted runtime forms, and frame mapping checks that
identity and its owning emitted function. Code from another runtime build cannot
reuse the observed location. Missing or tampered sidecars require refusal.

The sidecar binds exact BEAM bytes, compiler build, input identity and source.
It is external by design. Two sources differing only in erased checker content
produce identical BEAM bytes and different sidecars. That indistinguishability
means the original trusted source bundle is necessary for evidence provenance;
BEAM alone cannot choose an erased source variant.

`OTP.Compiler.compile_debug` emits the exact new artifact profile and supports
`no_line_info` for stripped builds. All ordinary OTP optimization remains enabled;
optimized/unoptimized witnesses here mean the additional explicit Catena inline
pass enabled/disabled, not an unverified claim about undocumented OTP switches.

The verified foreign path reuses P096 authorization and codecs. A fixed identity
return keeps one actual exported foreign-entry frame pending while the worker
runs, giving a correct entry-definition location when internal CPS requests are
tail-elided. It does not retain recursive worker frames or reconstruct a missing
request frame. `Report.debug_frames` redacts arguments, reasons and miscellaneous
host metadata by default; optional disclosure requires a checked argument-tuple
codec and complete bounds.

## Executed witnesses

`test/catena/debugging_metadata_test.exs` exercises:

- an escaped compiled closure trapping at its exact kernel expression;
- a deep-handler clause failure mapped to its exact trap span;
- zero, one and two levels of actual inlining, bounded histories and exhausted
  source/node/depth limits;
- a granted foreign failure with a retained physical entry boundary, denied
  authority before entry and secret-free default reporting;
- an ordinary JSON addition failure caused deliberately by a raw host passing
  an atom to an Int parameter, mapped to its original JSON expression; this is
  host misuse, not a counterexample to typed Catena progress;
- stripped frames, unknown host frames, explicit checked value disclosure and
  path refusal;
- tampered/missing sidecars, changed binaries and a captured stack offered to a
  different emitted program;
- Unicode scalar columns, byte/codepoint distinctions, CRLF and collision-free
  JSON paths; and
- erased-checker navigation with exactly unchanged BEAM bytes after the checker
  implementation changes.

Initial fixture failures exposed missing version registration and incorrect
handwritten JSON fixture signatures; these were repaired before passing runs.
Review additionally replaced quadratic source-prefix rescanning, bound the full
foreign input identity, and closed dotted-key locator collisions. The primary
[OTP compiler note](../30-sources/erlang-otp-29-compiler-recommendations-language-implementors.md)
records the documented source/line flags separately from these local claims.

## Verification

The combined initial debugging/foreign-adapter run passed 17 tests. The complete
regression suite later passed **898 tests** with six debugging tests. Final
checks after the last identity/coordinate refinements are recorded before commit.

Final validation passed **898 compiler tests**, production warnings-as-errors
compilation and the production escript build. Archive validation passed with
631 documents, 76 directories, 121 source notes, 190 specification chapters and
852 obligations (757 traced, 74 partial, 21 untraced). Both diffs passed
`git diff --check`. The checklist now totals 102 complete, 25 partial,
12 gaps and two deferred items.

Compiler implementation commit: `a54c7f4f9a6033e0e5472919ae0596d352d799e4`.
