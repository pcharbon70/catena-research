---
title: "Interface Graph Rendering and Doctests"
kind: specification
created: "2026-09-10"
status: normative
spec_version: "0.1.92"
tags: [specification, documentation, tooling, interfaces]
aliases: []
---

# Interface Graph Rendering and Doctests

## Status and authority

P119 defines its retained-input documentation tool at revision `0.1.92` under
[authority](../../SPECIFICATION-AUTHORITY.md), [conformance vocabulary](../../CONFORMANCE-VOCABULARY.md),
and [implementation limits](../../IMPLEMENTATION-LIMITS.md). It executes the
[P119 plan](../../20-notes/language-completion-plan-delivery.md#item-119-documentation-tool)
over C016 attachments, verified interfaces, P117 diagnostics, and G122's
bounded runner. Public-source examples remain held for P109, so P119 remains
partial (`DC-OBL-001`).

## Graph authority and visibility

A public documentation graph MUST be derived from a successfully verified
interface and MUST bind its exact interface digest. It MUST NOT infer exported
symbols from a BEAM artifact, filename, comment text, or unverified record
(`DC-OBL-002`).

The graph MUST represent exported types, values, traits and their laws,
instances and their law status, effects, handlers, and erased claim references
when those records occur in the verified interface. Nodes MUST be sorted by
stable fully qualified identity and MUST retain their complete portable
interface details (`DC-OBL-003`).

The default view MUST contain interface-visible records only. Documentation
targeting a hidden or unknown identity MUST be rejected. An internal view MAY
include explicitly supplied private records only after separate authorization;
such records MUST be marked internal and MUST NOT silently enter the public
view (`DC-OBL-004`).

A symbol without an attachment MUST render an explicit no-documentation state.
An attachment with an empty body, a duplicate target, a body larger than
65,536 bytes, more than 4,096 graph nodes, a duplicate identity, or a duplicate
rendered anchor MUST be rejected (`DC-OBL-005`).

## Links and deterministic rendering

Every `[[fully.qualified.symbol]]` link MUST resolve either to a node in the
same graph or to a node in an explicitly supplied, successfully verified
dependency interface. Unknown targets, forged dependency interfaces, duplicate
dependency modules, and links that cross an undeclared package boundary MUST be
rejected (`DC-OBL-006`).

Rendering MUST be deterministic for the exact graph. It MUST emit stable
symbol headings and anchors, kind and identity, normalized documentation, and
portable semantic details. Local links MUST use local anchors; dependency
links MUST identify the dependency module and anchor (`DC-OBL-007`).

C016 documentation bodies remain CommonMark source. This renderer MUST reject
active raw HTML rather than passing it to an active renderer. It MUST preserve
ordinary Markdown text and explicit doctest fences without treating other code
blocks as executable (`DC-OBL-008`).

## Explicit retained-input doctests

Only a fence whose complete info string is `catena doctest` MUST opt into
execution. Its body MUST be a JSON tool envelope that binds the current
interface digest, selects retained `json` or `kernel` input, contains the
retained input, declares an empty effect list, and states an expected success
or stable diagnostic identity (`DC-OBL-009`).

The documentation tool MUST execute every selected example through the G122
bounded runner with an explicit deterministic seed and exact subject digest.
It MUST distinguish passing, failing, stale, malformed, crashed, exhausted,
and host-timeout evidence according to that runner rather than treating a
timeout as language divergence (`DC-OBL-010`).

Environmental services MUST be denied to this retained-input doctest profile.
A nonempty effect declaration, stale subject digest, malformed envelope,
unexpected result, or runner failure MUST fail documentation construction and
MUST NOT produce a passing graph (`DC-OBL-011`).

## Artifact, reporting, and conformance

The graph MUST identify format, revision, module, interface digest, sorted
nodes, finite doctest results, public-source status, and a canonical digest over
all preceding fields. Rendering MUST reject a graph whose digest no longer
matches its contents (`DC-OBL-012`).

The conformance profile MUST publish graph authority, symbol kinds, visibility,
HTML, link, doctest, environmental-service, public-source, node-count, and
body-size policies (`DC-OBL-013`).

An implementation claiming this P119 slice MUST exercise deterministic local
rendering, verified cross-package links, explicit passing doctests, missing
documentation, hidden and internal views, raw HTML, unresolved links, forged
interfaces, stale examples, effect refusal, duplicate anchors, lifecycle
selection, production build, trust inventory, and the complete suite
(`DC-OBL-014`).

P119 MUST remain partial until P109 supplies the public parser and real
public-source doctest examples. Retained JSON and kernel envelopes are tooling
protocols and MUST NOT establish Catena's public vocabulary or grammar
(`DC-OBL-015`).

## Rationale and evidence (non-normative)

The [implementation journal](../../50-journal/2026-09-10-documentation-tool.md)
records eighteen four-way decisions and compiler PRs 180–182. The verified
interface is the narrow authority that already contains the semantic views a
documentation consumer needs, while the held grammar remains untouched.
