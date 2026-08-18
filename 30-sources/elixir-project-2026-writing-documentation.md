---
title: "Elixir 1.20 Writing Documentation"
kind: source
created: "2026-08-18"
authors:
  - "Elixir Project"
published: "1.20.3"
citation_key: "elixirProject2026WritingDocumentation"
container: "Elixir Documentation"
edition: "1.20.3"
isbn: null
doi: null
url: "https://hexdocs.pm/elixir/writing-documentation.html"
accessed: "2026-08-18"
tags:
  - documentation
  - doctest
  - elixir
  - language-design
  - markdown
aliases:
  - "Elixir writing documentation"
---

# Elixir 1.20 Writing Documentation

## Reference

Elixir Project, “Writing Documentation,” *Elixir Documentation*, version
1.20.3, accessed 2026-08-18.
[Official guide](https://hexdocs.pm/elixir/writing-documentation.html).

## Contribution

The guide treats documentation as first-class API material, distinguishes it
from implementation comments, uses Markdown, and explains ExUnit doctests.

## Findings

- `@moduledoc`, `@doc`, and `@typedoc` attach documentation explicitly to
  language subjects; documentation is not interchangeable with source
  comments.
- Documentation is written in Markdown and can carry tooling metadata.
- Function documentation belongs to a function and arity rather than to each
  individual clause.
- ExUnit doctests execute examples only through an explicit test-suite
  declaration, parsing samples marked with the `iex>` prompt.

## Relevance

Elixir shows the useful semantic separation: ordinary comments serve source
maintainers, while documentation becomes structured metadata for API tools.
It also demonstrates that executable examples are a testing feature with an
explicit harness, not an automatic consequence of every code block.

Catena keeps the separation and explicit execution principle, but uses
forward-attaching documentation comments and the exact fenced-code label
`catena doctest` instead of Elixir attributes and IEx prompts.

## Limits

Elixir's documentation attachment is attribute-based and its Markdown dialect
is tool-defined rather than the version-pinned CommonMark profile selected for
Catena. ExUnit.DocTest behavior does not define Catena example evaluation,
effects, environment, or future runner isolation.

## Derived work

- [Catena Comments and Documentation Comments](../20-notes/catena-comments-and-documentation-comments.md)
- [Resolved comments inquiry](../40-inquiries/how-should-catena-handle-comments-and-documentation-comments.md)
- [Comments and Documentation Comments map](../10-maps/comments-and-documentation-comments.md)
