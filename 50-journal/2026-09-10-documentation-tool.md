---
title: "2026-09-10 Documentation Tool"
kind: journal
created: "2026-09-10"
tags: [specification, documentation, tooling, interfaces]
aliases: []
---

# 2026-09-10 Documentation Tool

## Scope

Execute P119's retained-input portion at `0.1.92` while retaining the P109
public-source hold. CP-119-1..3 select a verified interface graph, explicit
isolated doctests, and visibility-aware output.

## Implementation decisions

| Decision | Four alternatives | Recommended and selected |
| --- | --- | --- |
| DC-I01 Authority | A comments; B verified interface; C BEAM introspection; D filenames | B: exported semantic identity is already checked. |
| DC-I02 Node identity | A heading text; B module/kind/name identity; C source line; D list index | B: identities remain stable across rendering. |
| DC-I03 Semantic views | A values only; B all interface symbol families; C raw compiler structs; D prose | B: types, traits, laws, effects and claims remain linked. |
| DC-I04 Public visibility | A all declarations; B interface records only; C docs decide; D BEAM exports | B: the interface is the public boundary. |
| DC-I05 Internal view | A always expose; B explicit authorization and internal marking; C forbid forever; D filename flag | B: useful inspection cannot silently publish private APIs. |
| DC-I06 Missing docs | A omit symbol; B explicit placeholder; C fail build; D invent summary | B: complete inventories remain honest. |
| DC-I07 Empty attachment | A accept silently; B reject explicit empty body; C substitute name; D inherit neighbor | B: missing and malformed documentation stay distinct. |
| DC-I08 Anchors | A renderer counters; B canonical identity slug; C random IDs; D headings alone | B: links are reproducible. |
| DC-I09 Local links | A text search; B fully qualified identity resolution; C URLs only; D guessed nearest name | B: ambiguity fails rather than choosing a target. |
| DC-I10 External links | A any string; B verified declared dependency interfaces; C network lookup; D forbid all | B: cross-package identity has an explicit authority chain. |
| DC-I11 Output | A host HTML; B deterministic Markdown plus portable details; C terminal text; D BEAM docs | B: reviewable output needs no active renderer. |
| DC-I12 Raw HTML | A execute; B reject active raw HTML; C strip silently; D trust package | B: preserve C016's inert safety boundary. |
| DC-I13 Opt-in | A every fence; B exact `catena doctest`; C heading convention; D filename | B: only explicit examples execute. |
| DC-I14 Envelope | A public syntax only; B subject-bound retained JSON/kernel protocol; C Elixir callback; D shell | B: examples run now without choosing grammar. |
| DC-I15 Runner | A direct unbounded call; B G122 bounded runner; C external CI only; D compiler process | B: seed, timeout, cleanup and evidence stay explicit. |
| DC-I16 Effects | A ambient services; B deny all environmental services; C inherit build; D user shell | B: documentation cannot acquire hidden authority. |
| DC-I17 Failure | A keep graph with warning; B fail construction; C ignore example; D retry nondeterministically | B: stale or failing documentation cannot appear verified. |
| DC-I18 Bounds | A unlimited; B 4,096 nodes and 65,536 body bytes; C host memory; D truncate identities | B: construction remains finite without corrupting identity. |

## Executed evidence

Compiler [PR 180](https://github.com/pcharbon70/catena/pull/180) merged feature
commit `2d9c480` as merge commit
`dd1848fdc60f426fca118313291641c26abcce8b` into `rewrite`. Six focused cases
cover deterministic rendering, local links, verified cross-package links,
passing subject-bound doctests, hidden targets, unauthorized internal views,
active HTML, unresolved links, forged interfaces, stale examples,
environmental-effect refusal, empty attachments and duplicate anchors. The
complete 1,149-test suite passes. Production warnings-as-errors compilation,
escript building, trust inventory verification, and `git diff --check` pass.

Corrective compiler [PR 181](https://github.com/pcharbon70/catena/pull/181)
merged feature commit `ce38024` as merge commit
`d39a8e7af9869ec9778cbb361f9b714b64da04b4` into `rewrite`. It
fixes dependency uniqueness to track module identities separately from symbol
identities and adds direct assertions for duplicate-module refusal and the
missing-documentation placeholder. The complete suite remains 1,149 passing.

Evidence compiler [PR 182](https://github.com/pcharbon70/catena/pull/182)
merged feature commit `ef2b182` as merge commit
`b216b7d0f05016ee432166af1043706519ed2559` into `rewrite`. It directly tampers
with a completed documentation graph and verifies render-time canonical-digest
refusal.

The [normative contract](../60-specification/documentation-tool/interface-graph-rendering-and-doctests.md)
makes the retained-input work durable. P119 stays partial because the public
parser and public-source examples remain P109 work.
