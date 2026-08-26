#!/usr/bin/env python3
"""Focused tests for Catena Research archive validation."""

import json
import unittest
from pathlib import Path

import jsonschema

from validate_archive import (
    ROOT,
    PROTOTYPE_SPECIFICATION_VERSIONS,
    conformance_vocabulary_link_errors,
    implementation_limits_link_errors,
    specification_authority_link_errors,
    specification_structure_errors,
    specification_vocabulary_errors,
    traceability_registry_errors,
    variability_register_errors,
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
                "formal-semantic-kernel": "0.1.8",
                "source-text": "0.1.9",
                "identifiers": "0.1.10",
                "whitespace-and-layout": "0.1.11",
                "comments-and-documentation-comments": "0.1.12",
                "literal-grammar": "0.1.13",
                "numeric-literal-semantics": "0.1.14",
                "operators-and-punctuation": "0.1.15",
                "files-and-modules": "0.1.16",
                "namespaces-and-shadowing": "0.1.17",
                "imports-and-exports": "0.1.18",
                "abstraction-boundaries": "0.1.19",
                "module-dependency-cycles": "0.1.20",
                "package-identity-and-dependencies": "0.1.21",
                "prelude-policy": "0.1.22",
                "entry-points": "0.1.23",
                "api-and-abi-compatibility": "0.1.24",
                "values-and-evaluation": "0.1.25",
                "evaluation-order": "0.1.26",
                "bindings-and-sequencing": "0.1.27",
                "functions-and-calls": "0.1.28",
                "branching": "0.1.29",
            },
            PROTOTYPE_SPECIFICATION_VERSIONS,
        )


class SpecificationVocabularyTests(unittest.TestCase):
    def assert_valid(self, body: str) -> None:
        self.assertEqual([], specification_vocabulary_errors("chapter.md", body))

    def test_accepts_canonical_keywords_and_plain_declarative_rules(self) -> None:
        self.assert_valid(
            """# Example

## Rules

Implementations MUST reject the input. They SHOULD explain the failure and
MAY include technical detail. Successful output is transactional.
"""
        )

    def test_rejects_uppercase_requirement_aliases(self) -> None:
        for alias in (
            "REQUIRED",
            "SHALL",
            "SHALL NOT",
            "RECOMMENDED",
            "NOT RECOMMENDED",
            "OPTIONAL",
        ):
            with self.subTest(alias=alias):
                errors = specification_vocabulary_errors(
                    "chapter.md", f"# Example\n\n## Rules\n\nThe behavior is {alias}.\n"
                )
                self.assertTrue(any("requirement alias" in error for error in errors))

    def test_ignores_non_normative_sections_and_quotations(self) -> None:
        self.assert_valid(
            """# Example

## Rules

The result is exact.

> A source says SHALL, OPTIONAL, and undefined behavior.

## Rationale (non-normative)

Historical standards say SHALL and undefined behavior. Their behavior is
implementation-defined or unspecified.
"""
        )

    def test_scans_normative_fences_and_ignores_non_normative_fences(self) -> None:
        errors = specification_vocabulary_errors(
            "chapter.md",
            """# Example

## Rules

> **Normative definition.**

```text
the result is OPTIONAL and has undefined behavior
```

> **Non-normative example.**

```text
historical text says SHALL and unspecified behavior
```
""",
        )
        self.assertTrue(any("requirement alias" in error for error in errors))
        self.assertTrue(any("undefined behavior" in error for error in errors))
        self.assertFalse(any(":14:" in error for error in errors))

    def test_rejects_undefined_behavior(self) -> None:
        errors = specification_vocabulary_errors(
            "chapter.md", "# Example\n\n## Rules\n\nThis has undefined behavior.\n"
        )
        self.assertTrue(any("undefined behavior" in error for error in errors))

    def test_rejects_unlabelled_variability_classes(self) -> None:
        for phrase in ("implementation-defined behavior", "unspecified behavior"):
            with self.subTest(phrase=phrase):
                errors = specification_vocabulary_errors(
                    "chapter.md", f"# Example\n\n## Rules\n\nThis is {phrase}.\n"
                )
                self.assertTrue(any("visible" in error for error in errors))

    def test_accepts_visible_behavior_callouts(self) -> None:
        self.assert_valid(
            """# Example

## Choices

> **Normative implementation-defined choice.**

The byte order is implementation-defined: an implementation selects either
little endian or big endian and publishes the selection in its profile.

> **Normative unspecified presentation.**

Fresh display names are bounded unspecified presentation: names can differ
only by alpha-renaming and cannot change the accepted typed core.
"""
        )

    def test_rejects_unbounded_unspecified_presentation(self) -> None:
        errors = specification_vocabulary_errors(
            "chapter.md",
            """# Example

## Choices

> **Normative unspecified presentation.**

The result uses unspecified presentation.
""",
        )
        self.assertTrue(any("must label bounded" in error for error in errors))


class SpecificationConformanceIndexTests(unittest.TestCase):
    def test_requires_vocabulary_link_from_specification_index(self) -> None:
        vocabulary = Path("/archive/CONFORMANCE-VOCABULARY.md")
        self.assertEqual(
            1,
            len(
                conformance_vocabulary_link_errors(
                    "60-specification/example/README.md", set(), vocabulary
                )
            ),
        )
        self.assertEqual(
            [],
            conformance_vocabulary_link_errors(
                "60-specification/example/README.md",
                {vocabulary.resolve()},
                vocabulary,
            ),
        )

    def test_requires_variability_register_from_area_index(self) -> None:
        self.assertEqual(
            ["area/README.md: missing section ## Variability register"],
            variability_register_errors("area/README.md", "# Area\n"),
        )
        self.assertEqual(
            [],
            variability_register_errors(
                "area/README.md", "# Area\n\n## Variability register\n\nNone.\n"
            ),
        )

    def test_requires_implementation_limits_link_from_specification_index(self) -> None:
        limits = Path("/archive/IMPLEMENTATION-LIMITS.md")
        self.assertEqual(
            1,
            len(
                implementation_limits_link_errors(
                    "60-specification/example/README.md", set(), limits
                )
            ),
        )
        self.assertEqual(
            [],
            implementation_limits_link_errors(
                "60-specification/example/README.md",
                {limits.resolve()},
                limits,
            ),
        )


class TraceabilityRegistryTests(unittest.TestCase):
    def test_accepts_well_formed_rows_and_counts_status(self) -> None:
        body = (
            "# Registry\n\n"
            "| ID | Obligation | Status |\n"
            "| --- | --- | --- |\n"
            "| CC-OBL-001 | first | traced |\n"
            "| CC-OBL-002 | second | partial |\n"
            "| CC-OBL-003 | third | untraced |\n"
        )
        errors, counts = traceability_registry_errors("map.md", body)
        self.assertEqual([], errors)
        self.assertEqual(3, counts["traceability_obligations"])
        self.assertEqual(1, counts["traceability_traced"])
        self.assertEqual(1, counts["traceability_partial"])
        self.assertEqual(1, counts["traceability_untraced"])

    def test_counts_untraced_separately_from_traced(self) -> None:
        body = "| CC-OBL-010 | gap | untraced |\n"
        _errors, counts = traceability_registry_errors("map.md", body)
        self.assertEqual(1, counts["traceability_untraced"])
        self.assertEqual(0, counts.get("traceability_traced", 0))

    def test_rejects_malformed_identifier(self) -> None:
        body = "| CC-OBL-1 | bad | traced |\n"
        errors, _counts = traceability_registry_errors("map.md", body)
        self.assertTrue(any("malformed obligation identifier" in e for e in errors))

    def test_rejects_duplicate_identifier(self) -> None:
        body = (
            "| CC-OBL-001 | first | traced |\n"
            "| CC-OBL-001 | duplicate | traced |\n"
        )
        errors, _counts = traceability_registry_errors("map.md", body)
        self.assertTrue(any("duplicate obligation identifier" in e for e in errors))

    def test_rejects_row_missing_status(self) -> None:
        body = "| CC-OBL-001 | first | done |\n"
        errors, _counts = traceability_registry_errors("map.md", body)
        self.assertTrue(any("missing a status" in e for e in errors))


if __name__ == "__main__":
    unittest.main()
