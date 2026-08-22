---
title: "The Rust Reference: Crates and Modules"
kind: source
created: "2026-08-21"
authors:
  - "Rust Project"
published: null
citation_key: "rustProject2026CratesAndModules"
container: "The Rust Reference"
edition: null
isbn: null
doi: null
url: "https://doc.rust-lang.org/reference/crates-and-source-files.html"
accessed: "2026-08-21"
tags:
  - files
  - language-design
  - modules
  - rust
aliases:
  - "Rust crates and source files"
---

# The Rust Reference: Crates and Modules

## Reference

Rust Project, “Crates and source files,” *The Rust Reference*, accessed
2026-08-21.
[Official reference](https://doc.rust-lang.org/reference/crates-and-source-files.html).

## Research question or contribution

What does the principal filename-derived module model look like, and what
does it cost?

## Method

The crates-and-source-files chapter was read for how modules bind to files,
how the crate root is located, and how `mod` declarations relate paths to
the filesystem.

## Findings

- A crate's root source file is found through the package manifest; crate
  names come from the manifest, not from file content.
- A `mod m;` declaration in a parent module loads `m.rs` or `m/mod.rs` by a
  filesystem convention — the module's identity is effectively its path
  relative to the declaring file.
- Source files have no module header: the same file text can be an inner
  module, an outer module, or the crate root depending on where the build
  places it.
- The reference documents these path conventions alongside the module
  declaration grammar, so filename binding is part of the language's source
  model.

## Relevance

Rust is the contrast case for Catena's decision: without a declared header,
a file's module identity is positional knowledge held by the build, and
tools must reproduce the path algebra to answer "what module is this
file?". Catena instead requires the module name to be declared in the file
and merely verified against the basename, keeping each file
self-describing. Rust's evidence shows the derived model is workable at
scale, so Catena's choice is a genuine trade toward determinism and
self-description rather than the only possible design.

## Limits

Rust's package manifest, crate root, and `mod`-path conventions are bound
to a package system Catena has not designed (G025), and its module grammar
is far beyond the abstract file-unit boundary of this slice.

## Derived work

- [Catena Files and Modules](../20-notes/catena-files-and-modules.md)
- [How Should Catena Relate Files to Modules?](../40-inquiries/how-should-catena-relate-files-to-modules.md)
- [Files and Modules map](../10-maps/files-and-modules.md)
