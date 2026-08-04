#!/usr/bin/env python3
"""Focused tests for Catena Research archive validation."""

import unittest
from pathlib import Path

from validate_archive import (
    specification_authority_link_errors,
    specification_structure_errors,
)


class SpecificationStructureTests(unittest.TestCase):
    def assert_valid(self, body: str) -> None:
        errors, _count = specification_structure_errors("chapter.md", body)
        self.assertEqual([], errors)

    def test_accepts_normative_definition_and_marked_connections(self) -> None:
        self.assert_valid(
            """# Example

## Rule

The result is exact.

> **Normative definition.**

```text
result ::= value
```

## Connections (non-normative)

This section explains the research route.

```mermaid
flowchart LR
  A --> B
```
"""
        )

    def test_accepts_normative_and_non_normative_examples(self) -> None:
        self.assert_valid(
            """# Example

## Rules

> **Normative conformance example.**

```text
accepted => 1
```

> **Non-normative example.**

```catena
sample()
```
"""
        )

    def test_rejects_unclassified_fenced_block(self) -> None:
        errors, count = specification_structure_errors(
            "chapter.md",
            "# Example\n\n## Rules\n\n```text\nx\n```\n",
            line_offset=10,
        )
        self.assertEqual(1, count)
        self.assertTrue(any("fenced block" in error for error in errors))
        self.assertTrue(any("chapter.md:15:" in error for error in errors))

    def test_rejects_unmarked_rationale_heading(self) -> None:
        errors, _count = specification_structure_errors(
            "chapter.md", "# Example\n\n## Rationale\n\nBecause it is useful.\n"
        )
        self.assertTrue(any("section heading" in error for error in errors))

    def test_rejects_unmarked_illustrative_cue(self) -> None:
        errors, _count = specification_structure_errors(
            "chapter.md", "# Example\n\n## Rules\n\nFor example, this is explanatory.\n"
        )
        self.assertTrue(any("illustrative material" in error for error in errors))

    def test_non_normative_section_scope_ends_at_peer_heading(self) -> None:
        errors, _count = specification_structure_errors(
            "chapter.md",
            """# Example

## Note (non-normative)

```text
explanation
```

## Rules

```text
unclassified
```
""",
        )
        self.assertEqual(1, len(errors))
        self.assertIn("fenced block", errors[0])

    def test_requires_authority_link_from_specification_index(self) -> None:
        authority = Path("/archive/SPECIFICATION-AUTHORITY.md")
        errors = specification_authority_link_errors(
            "60-specification/example/README.md", set(), authority
        )
        self.assertEqual(1, len(errors))
        self.assertEqual(
            [],
            specification_authority_link_errors(
                "60-specification/example/README.md",
                {authority.resolve()},
                authority,
            ),
        )


if __name__ == "__main__":
    unittest.main()
