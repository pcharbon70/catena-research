---
title: "Erlang Passive TCP Sockets"
kind: source
created: "2026-09-09"
authors: ["Erlang/OTP contributors"]
published: null
url: "https://www.erlang.org/doc/apps/kernel/gen_tcp.html"
accessed: "2026-09-09"
tags: [effects, implementation]
aliases: []
---

# Erlang Passive TCP Sockets

## Reference

Erlang/OTP contributors, [Erlang Passive TCP Sockets](https://www.erlang.org/doc/apps/kernel/gen_tcp.html), continuously maintained official documentation, accessed 9 September 2026. No publication year is inferred.

## Research question

Owned passive transport for explicit environmental services.

## Findings

The gen_tcp documentation defines socket ownership, active/passive delivery, explicit connect options and passive recv with a requested length. IPv4/IPv6 addresses can be supplied directly. These APIs provide the local transport mechanism.

## Relevance and limits

C106 supplies numeric endpoints and explicit binary/passive/packet options. External peers, DNS-free alias policy, request deadlines and typed error mapping are local contract choices. This is documentation evidence, not an independent performance or security evaluation. Only the relevant API sections were used.

## Derived work

The [C106 journal](../50-journal/2026-09-09-environmental-effects.md) records local experiments and decisions; the [normative amendment](../60-specification/environmental-effects/explicit-authority-and-closed-launches.md) owns Catena behavior.
