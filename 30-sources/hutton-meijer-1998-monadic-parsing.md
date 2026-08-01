---
title: "Monadic Parsing in Haskell"
kind: source
created: "2026-08-01"
authors:
  - "Graham Hutton"
  - "Erik Meijer"
published: 1998
citation_key: "huttonMeijer1998MonadicParsing"
container: "Journal of Functional Programming 8(4): 437–444"
edition: null
isbn: null
doi: "10.1017/S0956796898003050"
url: "https://www.cambridge.org/core/journals/journal-of-functional-programming/article/monadic-parsing-in-haskell/E557DFCCE00E0D4B6ED02F3FB0466093"
accessed: "2026-08-01"
tags:
  - combinator-libraries
  - functional-programming
  - monads
  - parsing
aliases:
  - "Hutton and Meijer on parser combinators"
---

# Monadic Parsing in Haskell

## Reference

Graham Hutton and Erik Meijer, “Monadic Parsing in Haskell,” *Journal of
Functional Programming* 8, no. 4 (1998): 437–444.
[DOI and publisher record](https://doi.org/10.1017/S0956796898003050),
[institutional record](https://nottingham-repository.worktribe.com/output/1024100/monadic-parsing-in-haskell),
and [publisher PDF](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/E557DFCCE00E0D4B6ED02F3FB0466093/S0956796898003050a.pdf/monadic-parsing-in-haskell.pdf).

## Contribution

The paper builds a recursive-descent parsing library from first-class parser
values and a small set of lawful sequencing, failure, choice, repetition, and
lexical combinators. It is a concrete demonstration that categorical
operations become useful when a datatype or abstract representation gives
them domain-specific meaning.

## Method

A parser is represented as a function from an input string to a list of parsed
values paired with unconsumed suffixes. The authors define `return` and bind,
state their monad laws, add failure and nondeterministic or deterministic
choice, and derive `sat`, `many`, separated repetition, associative expression
chains, token, and whitespace combinators. Worked examples assemble complete
parsers from those pieces.

## Findings

- `pure` parsing succeeds without consuming input; bind sequences parsers and
  lets an earlier parsed value determine the later parser.
- Associativity and unit laws permit nested sequencing to be regrouped without
  changing parser meaning.
- A zero parser and associative choice form a second algebra whose interaction
  with bind supplies useful simplification and distribution equations.
- Choice policy is operationally significant. Returning every parse expresses
  ambiguity, while the paper's deterministic choice keeps only the first
  result.
- Recursive derived combinators such as `many`, `sep_by`, and `chain_left`
  convert recurring grammar structures into reusable functions.
- Because parsers are ordinary first-class values, a library can add new
  grammar combinators without changing a fixed parser-generator language.

## Relevance

Parser combinators are a strong Catena test case. They exercise `Functor`,
`Applicative`, `Monad`, products, sums, lists, and monoidal choice, but also show
that class laws do not specify commitment, ambiguity, error selection,
backtracking, input consumption, or complexity. Those belong to the concrete
`Parser` contract.

## Limits

The authors explicitly note that hand-written recursive-descent combinators can
be less efficient than generated bottom-up parsers. The representation is
list-based and the paper does not settle left recursion, streaming input,
incremental parsing, source spans, structured errors, memoization, or modern
commit/backtracking semantics. A Catena parser library needs separate
operational laws and benchmarks in addition to its monad laws.

## Derived work

- [Combinators for Algebraic Data and Categorical Programming](../20-notes/combinators-for-algebraic-data-and-categorical-programming.md)
- [Which Combinators Should Catena Provide and Derive?](../40-inquiries/which-combinators-should-catena-provide-and-derive.md)
- [Combinators for Algebraic Data and Categorical Programming map](../10-maps/combinators-for-algebraic-data-and-categorical-programming.md)
