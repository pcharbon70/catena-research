---
title: "A Formalisation of Core Erlang, a Concurrent Actor Language"
kind: source
created: "2026-08-06"
authors:
  - "Péter Bereczky"
  - "Dániel Horpácsi"
  - "Simon Thompson"
published: 2024
citation_key: "bereczkyEtAl2024coreErlang"
container: "Acta Cybernetica 26(3)"
edition: null
isbn: null
doi: "10.14232/actacyb.298977"
url: "https://cyber.bibl.u-szeged.hu/index.php/actcybern/article/view/4333"
accessed: "2026-08-06"
tags:
  - actors
  - erlang
  - formal-semantics
aliases:
  - "Concurrent Core Erlang formalisation"
---

# A Formalisation of Core Erlang, a Concurrent Actor Language

## Reference

Péter Bereczky, Dániel Horpácsi, and Simon Thompson. “A Formalisation of Core
Erlang, a Concurrent Actor Language.” *Acta Cybernetica* 26, no. 3 (2024):
373–404. [DOI](https://doi.org/10.14232/actacyb.298977).

## Contribution

The work gives a machine-checked modular semantics for a concurrent Core
Erlang subset using local frame stacks, process-level behavior, and global
actor configurations.

## Findings

Separating sequential frames, process semantics, and global interleaving makes
concurrent reasoning modular. Program equivalence and scheduler-sensitive
behavior require a global relation beyond local expression evaluation.

## Relevance

Catena follows the same separation at a smaller paper-and-executable boundary:
local evaluation contexts, typed process/mailbox states, and nondeterministic
global steps.

## Limits

Core Erlang is not Catena's normative IR or backend interchange. The paper's
semantics does not supply Catena row typing, lexical handlers, or source
language decisions.

## Derived work

- [Formal Semantic Kernel Metatheory](../60-specification/formal-semantic-kernel/metatheory.md)
- [Formal Semantic Kernel map](../10-maps/formal-semantic-kernel.md)
