#!/usr/bin/env python3
"""Focused tests for Catena Research archive validation."""

import json
import unittest
from pathlib import Path

import jsonschema

from validate_archive import (
    ROOT,
    PROTOTYPE_SPECIFICATION_VERSIONS,
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


class SpecificationVersionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        schema = json.loads((ROOT / "frontmatter.schema.json").read_text(encoding="utf-8"))
        cls.validator = jsonschema.Draft202012Validator(
            schema, format_checker=jsonschema.FormatChecker()
        )

    def metadata(self, version: str) -> dict[str, object]:
        return {
            "title": "Version Example",
            "kind": "specification",
            "created": "2026-08-04",
            "status": "draft",
            "spec_version": version,
            "tags": [],
            "aliases": [],
        }

    def test_accepts_exact_three_component_slice_version(self) -> None:
        self.assertEqual([], list(self.validator.iter_errors(self.metadata("0.1.7"))))

    def test_rejects_two_component_and_extended_versions(self) -> None:
        for version in ("0.7", "0.1.7-preview", "0.01.7", "0.1.07"):
            with self.subTest(version=version):
                self.assertNotEqual(
                    [], list(self.validator.iter_errors(self.metadata(version)))
                )

    def test_current_areas_use_the_canonical_patch_sequence(self) -> None:
        self.assertEqual(
            {
                "type-system": "0.1.1",
                "data-and-patterns": "0.1.2",
                "clause-conditions": "0.1.3",
                "traits-and-categorical-operations": "0.1.4",
                "effects-and-handlers": "0.1.5",
                "specifications-and-governance": "0.1.6",
                "editions-and-feature-lifecycle": "0.1.7",
            },
            PROTOTYPE_SPECIFICATION_VERSIONS,
        )


if __name__ == "__main__":
    unittest.main()
