#!/usr/bin/env python3
"""Validate the Catena Research archive's structural invariants."""

from __future__ import annotations

import copy
import json
import re
import sys
from collections import defaultdict
from pathlib import Path
from urllib.parse import unquote, urlsplit

try:
    import jsonschema
    import yaml
except ModuleNotFoundError as error:
    print(
        f"Missing validation dependency: {error.name}. "
        "Run `python3 -m pip install -r requirements-validation.txt`.",
        file=sys.stderr,
    )
    raise SystemExit(2) from error


ROOT = Path(__file__).resolve().parent
SCHEMA_PATH = ROOT / "frontmatter.schema.json"
SPECIFICATION_ROOT = ROOT / "60-specification"
SPECIFICATION_AUTHORITY_PATH = ROOT / "SPECIFICATION-AUTHORITY.md"
CONFORMANCE_VOCABULARY_PATH = ROOT / "CONFORMANCE-VOCABULARY.md"
IMPLEMENTATION_LIMITS_PATH = ROOT / "IMPLEMENTATION-LIMITS.md"
ARCHIVE_DIRECTORIES = {
    "00-inbox",
    "10-maps",
    "20-notes",
    "30-sources",
    "40-inquiries",
    "50-journal",
    "60-specification",
    "90-archive",
    "assets",
    "templates",
}
IGNORED_NAMES = {
    ".DS_Store",
    ".git",
    ".mypy_cache",
    ".pytest_cache",
    ".ruff_cache",
    "__pycache__",
}
REQUIRED_README_HEADINGS = {
    "Purpose",
    "What belongs here",
    "Index",
    "Maintaining this index",
}
KNOWLEDGE_FILENAME = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*\.md$")
JOURNAL_FILENAME = re.compile(r"^\d{4}-\d{2}-\d{2}(?:-[a-z0-9]+(?:-[a-z0-9]+)*)?\.md$")
PLACEHOLDER = re.compile(
    r"\{(?:title|question|YYYY-MM-DD|author|directory title|directory-name|"
    r"MAJOR\.MINOR\.PATCH)\}"
)
MARKDOWN_LINK = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")
SPECIFICATION_CONTENT_LABEL = re.compile(
    r"^> \*\*(?:Normative definition|Normative conformance example|"
    r"Non-normative (?:example|rationale|note|diagram|evidence))\.\*\*(?:\s+.*)?$"
)
IMPLEMENTATION_DEFINED_CALLOUT = (
    "> **Normative implementation-defined choice.**"
)
UNSPECIFIED_PRESENTATION_CALLOUT = (
    "> **Normative unspecified presentation.**"
)
SPECIFICATION_BEHAVIOR_CALLOUTS = {
    IMPLEMENTATION_DEFINED_CALLOUT: "implementation-defined",
    UNSPECIFIED_PRESENTATION_CALLOUT: "unspecified-presentation",
}
UPPERCASE_REQUIREMENT_ALIAS = re.compile(
    r"\b(?:REQUIRED|SHALL(?: NOT)?|RECOMMENDED|NOT RECOMMENDED|OPTIONAL)\b"
)
UNDEFINED_BEHAVIOR = re.compile(r"\bundefined behavior\b", re.IGNORECASE)
IMPLEMENTATION_DEFINED_TERM = re.compile(
    r"\bimplementation[- ]defined\b", re.IGNORECASE
)
UNSPECIFIED_TERM = re.compile(r"\bunspecified\b", re.IGNORECASE)
UNSPECIFIED_PRESENTATION_TERM = re.compile(
    r"\bunspecified presentation\b", re.IGNORECASE
)
BOUNDED_TERM = re.compile(r"\bbounded\b", re.IGNORECASE)
NON_NORMATIVE_HEADING_ROLE = re.compile(
    r"(?:\brationale\b|^connections$|^proof (?:outline|status)$|"
    r"^proof and evidence status$|^evidence route$)",
    flags=re.IGNORECASE,
)
ILLUSTRATIVE_CUE = re.compile(r"\b(?:for example|illustrative)\b", re.IGNORECASE)
NON_NORMATIVE_HEADING_SUFFIX = " (non-normative)"
FENCE_START = re.compile(r"^(`{3,}|~{3,})")
PROTOTYPE_SPECIFICATION_VERSIONS = {
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
    "equality-and-ordering": "0.1.30",
    "recursion-and-termination": "0.1.31",
    "runtime-failure-taxonomy": "0.1.32",
    "resource-observability": "0.1.33",
    "compile-time-evaluation": "0.1.34",
    "built-in-data-model": "0.1.35",
    "structural-records-and-variants": "0.1.36",
    "collection-construction-and-update": "0.1.37",
    "pattern-contexts": "0.1.38",
    "list-comprehensions": "0.1.39",
    "numeric-relationships": "0.1.40",
    "aliases-and-newtypes": "0.1.41",
    "name-resolution": "0.1.42",
    "dynamic-and-unsafe-boundaries": "0.1.43",
}


class StringDateLoader(yaml.SafeLoader):
    """A safe YAML loader that does not coerce ISO dates to Python dates."""


StringDateLoader.yaml_implicit_resolvers = copy.deepcopy(
    yaml.SafeLoader.yaml_implicit_resolvers
)
for initial, resolvers in list(StringDateLoader.yaml_implicit_resolvers.items()):
    StringDateLoader.yaml_implicit_resolvers[initial] = [
        (tag, expression)
        for tag, expression in resolvers
        if tag != "tag:yaml.org,2002:timestamp"
    ]


def relative(path: Path) -> str:
    """Return a stable repository-relative display path."""

    try:
        value = path.resolve().relative_to(ROOT)
    except ValueError:
        return str(path)
    return "." if value == Path(".") else value.as_posix()


def is_ignored(path: Path) -> bool:
    """Return whether a path is repository machinery rather than archive data."""

    try:
        parts = path.resolve().relative_to(ROOT).parts
    except ValueError:
        parts = path.parts
    return any(part in IGNORED_NAMES or part.startswith(".") for part in parts)


def visible_children(directory: Path) -> list[Path]:
    """Return direct archive children, excluding repository machinery."""

    return sorted(
        (
            child
            for child in directory.iterdir()
            if not is_ignored(child) and child.name != "README.md"
        ),
        key=lambda child: child.name,
    )


def archive_directories() -> list[Path]:
    """Return the root and every non-generated archive directory."""

    return [
        ROOT,
        *sorted(
            (
                path
                for path in ROOT.rglob("*")
                if path.is_dir() and not is_ignored(path)
            ),
            key=lambda path: path.as_posix(),
        ),
    ]


def completed_markdown_files() -> list[Path]:
    """Return completed knowledge documents and directory READMEs."""

    files: list[Path] = []
    for top_name in sorted(ARCHIVE_DIRECTORIES):
        top = ROOT / top_name
        if not top.is_dir():
            continue
        for path in sorted(top.rglob("*.md")):
            if is_ignored(path):
                continue
            if top_name == "templates" and path.name != "README.md":
                continue
            if top_name == "00-inbox" and path.name != "README.md":
                continue
            files.append(path)
    return files


def parse_frontmatter(path: Path) -> tuple[dict[str, object], str]:
    """Parse one completed Markdown file into metadata and body."""

    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        raise ValueError("missing opening YAML frontmatter delimiter")
    end = text.find("\n---\n", 4)
    if end < 0:
        raise ValueError("missing closing YAML frontmatter delimiter")
    metadata = yaml.load(text[4:end], Loader=StringDateLoader)
    if not isinstance(metadata, dict):
        raise ValueError("frontmatter must be a YAML mapping")
    return metadata, text[end + 5 :]


def link_destination(raw: str) -> str:
    """Remove optional Markdown angle brackets and link titles."""

    value = raw.strip()
    if value.startswith("<"):
        close = value.find(">")
        return value[1:close] if close >= 0 else value[1:]
    return value.split(maxsplit=1)[0]


def local_link_target(source: Path, raw: str) -> tuple[Path, str] | None:
    """Resolve a Markdown destination, returning None for external links."""

    destination = link_destination(raw)
    parsed = urlsplit(destination)
    if parsed.scheme or parsed.netloc:
        return None
    decoded_path = unquote(parsed.path)
    target = source if not decoded_path else (source.parent / decoded_path)
    return target.resolve(), unquote(parsed.fragment)


def github_heading_anchors(markdown: str) -> set[str]:
    """Approximate GitHub's heading IDs, including duplicate suffixes."""

    anchors: set[str] = set()
    occurrences: defaultdict[str, int] = defaultdict(int)
    for line in markdown.splitlines():
        match = re.match(r"^#{1,6}\s+(.+?)\s*#*\s*$", line)
        if not match:
            continue
        heading = re.sub(r"<[^>]+>", "", match.group(1))
        heading = re.sub(r"[`*_~]", "", heading).strip().lower()
        slug = re.sub(r"[^\w\- ]", "", heading, flags=re.UNICODE)
        slug = re.sub(r"\s+", "-", slug)
        suffix = occurrences[slug]
        occurrences[slug] += 1
        anchors.add(slug if suffix == 0 else f"{slug}-{suffix}")
    return anchors


def specification_structure_errors(
    display_path: str, body: str, line_offset: int = 0
) -> tuple[list[str], int]:
    """Validate rendered authority labels in one specification chapter."""

    errors: list[str] = []
    active_non_normative_level: int | None = None
    previous_nonempty = ""
    fence_marker = ""
    fenced_blocks = 0

    for body_line_number, line in enumerate(body.splitlines(), start=1):
        line_number = body_line_number + line_offset
        stripped = line.strip()

        if fence_marker:
            if stripped.startswith(fence_marker):
                fence_marker = ""
            continue

        heading = re.match(r"^(#{1,6})\s+(.+?)\s*#*\s*$", line)
        if heading:
            level = len(heading.group(1))
            heading_text = heading.group(2).strip()
            if (
                active_non_normative_level is not None
                and level <= active_non_normative_level
            ):
                active_non_normative_level = None

            is_non_normative = heading_text.casefold().endswith(
                NON_NORMATIVE_HEADING_SUFFIX
            )
            role_text = (
                heading_text[: -len(NON_NORMATIVE_HEADING_SUFFIX)]
                if is_non_normative
                else heading_text
            )
            if NON_NORMATIVE_HEADING_ROLE.search(role_text) and not is_non_normative:
                errors.append(
                    f"{display_path}:{line_number}: non-normative section heading "
                    "must end with '(non-normative)'"
                )
            if is_non_normative:
                active_non_normative_level = level
            previous_nonempty = stripped
            continue

        fence = FENCE_START.match(stripped)
        if fence:
            fenced_blocks += 1
            if (
                active_non_normative_level is None
                and SPECIFICATION_CONTENT_LABEL.fullmatch(previous_nonempty) is None
            ):
                errors.append(
                    f"{display_path}:{line_number}: specification fenced block must "
                    "follow a visible authority callout or appear in a "
                    "non-normative section"
                )
            fence_marker = fence.group(1)
            continue

        if (
            active_non_normative_level is None
            and ILLUSTRATIVE_CUE.search(line)
            and SPECIFICATION_CONTENT_LABEL.fullmatch(stripped) is None
            and SPECIFICATION_CONTENT_LABEL.fullmatch(previous_nonempty) is None
        ):
            errors.append(
                f"{display_path}:{line_number}: illustrative material must use a "
                "visible normative or non-normative callout"
            )

        if stripped:
            previous_nonempty = stripped

    return errors, fenced_blocks


def specification_vocabulary_errors(
    display_path: str, body: str, line_offset: int = 0
) -> list[str]:
    """Validate conformance vocabulary in normative chapter material."""

    errors: list[str] = []
    active_non_normative_level: int | None = None
    fence_marker = ""
    scan_fence = False
    previous_nonempty = ""
    pending_label: tuple[str, int] | None = None
    labeled_lines: list[tuple[int, str]] = []

    def finish_labeled_block() -> None:
        nonlocal pending_label, labeled_lines
        if pending_label is None:
            return

        label, label_line = pending_label
        text = " ".join(line for _line_number, line in labeled_lines)
        if not text:
            errors.append(
                f"{display_path}:{label_line}: conformance behavior callout "
                "must label the immediately following paragraph or table"
            )
        elif label == "implementation-defined":
            if IMPLEMENTATION_DEFINED_TERM.search(text) is None:
                errors.append(
                    f"{display_path}:{label_line}: implementation-defined callout "
                    "must label an implementation-defined choice"
                )
            if UNSPECIFIED_TERM.search(text):
                errors.append(
                    f"{display_path}:{label_line}: implementation-defined callout "
                    "cannot label unspecified behavior"
                )
        else:
            if (
                UNSPECIFIED_PRESENTATION_TERM.search(text) is None
                or BOUNDED_TERM.search(text) is None
            ):
                errors.append(
                    f"{display_path}:{label_line}: unspecified-presentation callout "
                    "must label bounded unspecified presentation"
                )
            if IMPLEMENTATION_DEFINED_TERM.search(text):
                errors.append(
                    f"{display_path}:{label_line}: unspecified-presentation callout "
                    "cannot label an implementation-defined choice"
                )

        pending_label = None
        labeled_lines = []

    def scan_normative_text(
        text: str, line_number: int, behavior_labeled: bool = False
    ) -> None:
        if UPPERCASE_REQUIREMENT_ALIAS.search(text):
            errors.append(
                f"{display_path}:{line_number}: uppercase requirement alias is "
                "prohibited; use MUST, MUST NOT, SHOULD, SHOULD NOT, or MAY"
            )
        if UNDEFINED_BEHAVIOR.search(text):
            errors.append(
                f"{display_path}:{line_number}: Catena normative text must not "
                "specify undefined behavior"
            )
        if behavior_labeled:
            return
        if IMPLEMENTATION_DEFINED_TERM.search(text):
            errors.append(
                f"{display_path}:{line_number}: implementation-defined choice "
                "requires a visible normative callout"
            )
        if UNSPECIFIED_TERM.search(text):
            errors.append(
                f"{display_path}:{line_number}: unspecified behavior requires a "
                "visible bounded unspecified-presentation callout"
            )

    for body_line_number, line in enumerate(body.splitlines(), start=1):
        line_number = body_line_number + line_offset
        stripped = line.strip()

        if fence_marker:
            if stripped.startswith(fence_marker):
                fence_marker = ""
                scan_fence = False
            elif scan_fence and stripped:
                scan_normative_text(stripped, line_number)
            continue

        heading = re.match(r"^(#{1,6})\s+(.+?)\s*#*\s*$", line)
        if heading:
            finish_labeled_block()
            level = len(heading.group(1))
            heading_text = heading.group(2).strip()
            if (
                active_non_normative_level is not None
                and level <= active_non_normative_level
            ):
                active_non_normative_level = None
            if heading_text.casefold().endswith(NON_NORMATIVE_HEADING_SUFFIX):
                active_non_normative_level = level
            previous_nonempty = stripped
            continue

        fence = FENCE_START.match(stripped)
        if fence:
            if active_non_normative_level is None:
                finish_labeled_block()
                scan_fence = previous_nonempty.startswith(
                    "> **Normative definition.**"
                ) or previous_nonempty.startswith(
                    "> **Normative conformance example.**"
                )
            fence_marker = fence.group(1)
            continue

        if active_non_normative_level is not None:
            continue

        behavior_label = SPECIFICATION_BEHAVIOR_CALLOUTS.get(stripped)
        if behavior_label is not None:
            finish_labeled_block()
            pending_label = (behavior_label, line_number)
            previous_nonempty = stripped
            continue

        # Markdown block quotations are source material or explanatory callouts,
        # not chapter-authored normative prose. Behavior labels above are the
        # only blockquotes that affect this check.
        if stripped.startswith(">"):
            finish_labeled_block()
            previous_nonempty = stripped
            continue

        if not stripped:
            if labeled_lines:
                finish_labeled_block()
            continue

        scan_normative_text(stripped, line_number, pending_label is not None)

        if pending_label is not None:
            labeled_lines.append((line_number, stripped))
            previous_nonempty = stripped
            continue

        previous_nonempty = stripped

    finish_labeled_block()
    return errors


def specification_authority_link_errors(
    display_path: str, indexed_targets: set[Path], authority_path: Path
) -> list[str]:
    """Require a specification index to expose the authority policy."""

    if authority_path.resolve() in indexed_targets:
        return []
    return [f"{display_path}: missing link to SPECIFICATION-AUTHORITY.md"]


def conformance_vocabulary_link_errors(
    display_path: str, indexed_targets: set[Path], vocabulary_path: Path
) -> list[str]:
    """Require a specification index to expose the conformance vocabulary."""

    if vocabulary_path.resolve() in indexed_targets:
        return []
    return [f"{display_path}: missing link to CONFORMANCE-VOCABULARY.md"]


def implementation_limits_link_errors(
    display_path: str, indexed_targets: set[Path], limits_path: Path
) -> list[str]:
    """Require a specification index to expose the implementation-limit policy."""

    if limits_path.resolve() in indexed_targets:
        return []
    return [f"{display_path}: missing link to IMPLEMENTATION-LIMITS.md"]


def variability_register_errors(display_path: str, markdown: str) -> list[str]:
    """Require an area index to summarize its permitted variability."""

    if re.search(r"^## Variability register\s*$", markdown, flags=re.MULTILINE):
        return []
    return [f"{display_path}: missing section ## Variability register"]


TRACEABILITY_REGISTRY = ROOT / "10-maps" / "conformance-traceability.md"
OBLIGATION_ROW = re.compile(r"^\|\s*([A-Z]+-OBL-[^\s|]+)")
OBLIGATION_ID = re.compile(r"^[A-Z]{2}-OBL-\d{3}$")
OBLIGATION_STATUS_TOKENS = ("untraced", "partial", "traced")


def traceability_registry_errors(
    display_path: str, markdown: str
) -> tuple[list[str], dict[str, int]]:
    """Check the conformance-traceability obligation registry.

    The registry is non-normative. This check guards its internal integrity
    only: each obligation row carries a well-formed, unique identifier and a
    recognized status. Per-area completeness is reported as counts, not
    enforced, so the registry can grow one area at a time. ``untraced`` is
    tested before ``traced`` because the latter is a substring of the former.
    """

    errors: list[str] = []
    counts: dict[str, int] = defaultdict(int)
    seen: dict[str, int] = {}

    for line_number, line in enumerate(markdown.splitlines(), start=1):
        match = OBLIGATION_ROW.match(line)
        if not match:
            continue
        identifier = match.group(1)
        if not OBLIGATION_ID.fullmatch(identifier):
            errors.append(
                f"{display_path}:{line_number}: malformed obligation identifier "
                f"{identifier!r} (expected AREA-OBL-NNN)"
            )
            continue
        counts["traceability_obligations"] += 1
        if not any(token in line for token in OBLIGATION_STATUS_TOKENS):
            errors.append(
                f"{display_path}:{line_number}: obligation {identifier!r} row "
                "missing a status (traced, partial, or untraced)"
            )
        elif "untraced" in line:
            counts["traceability_untraced"] += 1
        elif "partial" in line:
            counts["traceability_partial"] += 1
        else:
            counts["traceability_traced"] += 1
        seen[identifier] = seen.get(identifier, 0) + 1

    for identifier, occurrences in sorted(seen.items()):
        if occurrences > 1:
            errors.append(
                f"{display_path}: duplicate obligation identifier "
                f"{identifier!r} ({occurrences} rows)"
            )

    return errors, counts


def validate() -> tuple[list[str], dict[str, int]]:
    """Run all checks and return errors plus summary counts."""

    errors: list[str] = []
    counts: defaultdict[str, int] = defaultdict(int)

    try:
        schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
        jsonschema.Draft202012Validator.check_schema(schema)
    except (OSError, json.JSONDecodeError, jsonschema.SchemaError) as error:
        return [f"{relative(SCHEMA_PATH)}: invalid JSON Schema: {error}"], counts

    validator = jsonschema.Draft202012Validator(
        schema, format_checker=jsonschema.FormatChecker()
    )
    records: dict[Path, tuple[dict[str, object], str]] = {}

    for top_name in sorted(ARCHIVE_DIRECTORIES):
        if not (ROOT / top_name).is_dir():
            errors.append(f"{top_name}/: missing canonical archive directory")

    for path in completed_markdown_files():
        counts["completed_documents"] += 1
        try:
            metadata, body = parse_frontmatter(path)
        except (OSError, ValueError, yaml.YAMLError) as error:
            errors.append(f"{relative(path)}: {error}")
            continue
        records[path.resolve()] = (metadata, body)
        for schema_error in sorted(
            validator.iter_errors(metadata), key=lambda item: list(item.absolute_path)
        ):
            location = ".".join(str(part) for part in schema_error.absolute_path)
            location = location or "<root>"
            errors.append(
                f"{relative(path)}: frontmatter {location}: {schema_error.message}"
            )

        h1 = re.search(r"^#\s+(.+?)\s*$", body, flags=re.MULTILINE)
        title = str(metadata.get("title", ""))
        if h1 is None:
            errors.append(f"{relative(path)}: missing H1")
        elif path.name == "README.md":
            if not h1.group(1).replace("`", "").startswith(title):
                errors.append(
                    f"{relative(path)}: H1 {h1.group(1)!r} does not match title {title!r}"
                )
        elif h1.group(1) != title:
            errors.append(
                f"{relative(path)}: H1 {h1.group(1)!r} does not match title {title!r}"
            )

        if path.name != "README.md":
            kind = metadata.get("kind")
            if kind == "journal":
                filename_pattern = JOURNAL_FILENAME
            else:
                filename_pattern = KNOWLEDGE_FILENAME
            if not filename_pattern.fullmatch(path.name):
                errors.append(
                    f"{relative(path)}: filename does not follow the convention for {kind}"
                )

            top_name = path.relative_to(ROOT).parts[0]
            destinations = {
                "map": "10-maps",
                "note": "20-notes",
                "source": "30-sources",
                "inquiry": "40-inquiries",
                "journal": "50-journal",
                "specification": "60-specification",
            }
            expected = destinations.get(kind)
            if (
                top_name not in {"90-archive", "assets"}
                and expected
                and top_name != expected
            ):
                errors.append(
                    f"{relative(path)}: kind {kind!r} belongs in {expected}/"
                )

            if kind == "specification":
                counts["specification_documents"] += 1
                raw_text = path.read_text(encoding="utf-8")
                frontmatter_end = raw_text.find("\n---\n", 4) + 5
                line_offset = raw_text[:frontmatter_end].count("\n")
                structure_errors, fenced_blocks = specification_structure_errors(
                    relative(path), body, line_offset=line_offset
                )
                errors.extend(structure_errors)
                counts["specification_fenced_blocks"] += fenced_blocks
                if metadata.get("status") == "normative":
                    errors.extend(
                        specification_vocabulary_errors(
                            relative(path), body, line_offset=line_offset
                        )
                    )

    # Template placeholders must not leak into completed Markdown.
    for path in sorted(ROOT.rglob("*.md")):
        if is_ignored(path):
            continue
        if path.parent == ROOT / "templates" or path == ROOT / "AGENTS.md":
            continue
        if path.parent == ROOT / "00-inbox" and path.name != "README.md":
            continue
        for line_number, line in enumerate(
            path.read_text(encoding="utf-8").splitlines(), start=1
        ):
            if PLACEHOLDER.search(line):
                errors.append(
                    f"{relative(path)}:{line_number}: unresolved template placeholder"
                )

    # Resolve local Markdown and asset links, including heading fragments.
    links_by_source: defaultdict[Path, set[Path]] = defaultdict(set)
    incoming_from_conceptual: defaultdict[Path, set[Path]] = defaultdict(set)
    markdown_sources = sorted(ROOT.rglob("*.md"))
    for path in markdown_sources:
        if is_ignored(path):
            continue
        text = path.read_text(encoding="utf-8")
        for line_number, line in enumerate(text.splitlines(), start=1):
            for raw in MARKDOWN_LINK.findall(line):
                resolved = local_link_target(path, raw)
                if resolved is None:
                    continue
                target, fragment = resolved
                counts["local_links"] += 1
                if link_destination(raw).startswith("/"):
                    errors.append(
                        f"{relative(path)}:{line_number}: local link must be relative: {raw}"
                    )
                    continue
                if not target.exists():
                    errors.append(
                        f"{relative(path)}:{line_number}: missing local link target: {raw}"
                    )
                    continue
                links_by_source[path.resolve()].add(target)
                if target.suffix.lower() == ".md" and fragment:
                    anchors = github_heading_anchors(target.read_text(encoding="utf-8"))
                    if fragment not in anchors:
                        errors.append(
                            f"{relative(path)}:{line_number}: missing heading fragment "
                            f"#{fragment} in {relative(target)}"
                        )

                source_record = records.get(path.resolve())
                source_is_conceptual = (
                    path == ROOT / "README.md"
                    or (
                        source_record is not None
                        and path.name != "README.md"
                        and source_record[0].get("kind") == "map"
                    )
                )
                if source_is_conceptual:
                    incoming_from_conceptual[target].add(path.resolve())

    # Check every directory README's shape and direct-child inventory.
    for directory in archive_directories():
        counts["directories"] += 1
        readme = directory / "README.md"
        if not readme.is_file():
            errors.append(f"{relative(directory)}: missing README.md")
            continue
        text = readme.read_text(encoding="utf-8")
        headings = set(re.findall(r"^##\s+(.+?)\s*$", text, flags=re.MULTILINE))
        for missing in sorted(REQUIRED_README_HEADINGS - headings):
            if directory != ROOT:
                errors.append(f"{relative(readme)}: missing section ## {missing}")
        if directory != ROOT:
            if not re.search(r"^###\s+Subdirectories\s*$", text, flags=re.MULTILINE):
                errors.append(f"{relative(readme)}: missing ### Subdirectories")
            if not re.search(
                r"^###\s+(?:Documents|Files|Templates)\s*$",
                text,
                flags=re.MULTILINE,
            ):
                errors.append(
                    f"{relative(readme)}: missing ### Documents, ### Files, or ### Templates"
                )

        indexed_targets = links_by_source.get(readme.resolve(), set())
        for child in visible_children(directory):
            expected = (child / "README.md").resolve() if child.is_dir() else child.resolve()
            if expected not in indexed_targets:
                errors.append(
                    f"{relative(readme)}: unindexed direct child {child.name!r}"
                )

    # Specification areas must expose the authority and vocabulary contracts,
    # a variability register, and one coherent version/status boundary.
    # READMEs are indexes, not language authority.
    if not SPECIFICATION_AUTHORITY_PATH.is_file():
        errors.append("SPECIFICATION-AUTHORITY.md: missing authority policy")
    else:
        authority_target = SPECIFICATION_AUTHORITY_PATH.resolve()
        specification_readmes = [SPECIFICATION_ROOT / "README.md"]
        specification_readmes.extend(
            child / "README.md"
            for child in sorted(SPECIFICATION_ROOT.iterdir())
            if child.is_dir() and not is_ignored(child)
        )
        for readme in specification_readmes:
            if readme.is_file():
                errors.extend(
                    specification_authority_link_errors(
                        relative(readme),
                        links_by_source.get(readme.resolve(), set()),
                        authority_target,
                    )
                )

    if not CONFORMANCE_VOCABULARY_PATH.is_file():
        errors.append("CONFORMANCE-VOCABULARY.md: missing conformance policy")
    else:
        vocabulary_target = CONFORMANCE_VOCABULARY_PATH.resolve()
        specification_readmes = [SPECIFICATION_ROOT / "README.md"]
        specification_readmes.extend(
            child / "README.md"
            for child in sorted(SPECIFICATION_ROOT.iterdir())
            if child.is_dir() and not is_ignored(child)
        )
        for readme in specification_readmes:
            if readme.is_file():
                errors.extend(
                    conformance_vocabulary_link_errors(
                        relative(readme),
                        links_by_source.get(readme.resolve(), set()),
                        vocabulary_target,
                    )
                )

        for area in sorted(
            child
            for child in SPECIFICATION_ROOT.iterdir()
            if child.is_dir() and not is_ignored(child)
        ):
            readme = area / "README.md"
            if readme.is_file():
                errors.extend(
                    variability_register_errors(
                        relative(readme), readme.read_text(encoding="utf-8")
                    )
                )

    if not IMPLEMENTATION_LIMITS_PATH.is_file():
        errors.append("IMPLEMENTATION-LIMITS.md: missing implementation-limit policy")
    else:
        limits_target = IMPLEMENTATION_LIMITS_PATH.resolve()
        specification_readmes = [SPECIFICATION_ROOT / "README.md"]
        specification_readmes.extend(
            child / "README.md"
            for child in sorted(SPECIFICATION_ROOT.iterdir())
            if child.is_dir() and not is_ignored(child)
        )
        for readme in specification_readmes:
            if readme.is_file():
                errors.extend(
                    implementation_limits_link_errors(
                        relative(readme),
                        links_by_source.get(readme.resolve(), set()),
                        limits_target,
                    )
                )

    if SPECIFICATION_AUTHORITY_PATH.is_file():
        for area in sorted(
            child
            for child in SPECIFICATION_ROOT.iterdir()
            if child.is_dir() and not is_ignored(child)
        ):
            chapters = [
                records[path.resolve()]
                for path in sorted(area.glob("*.md"))
                if path.name != "README.md" and path.resolve() in records
            ]
            if not chapters:
                errors.append(f"{relative(area)}: specification area has no chapters")
                continue

            versions = {metadata.get("spec_version") for metadata, _body in chapters}
            statuses = {metadata.get("status") for metadata, _body in chapters}
            if len(versions) != 1:
                errors.append(
                    f"{relative(area)}: specification chapters must share one "
                    "spec_version"
                )
            expected_version = PROTOTYPE_SPECIFICATION_VERSIONS.get(area.name)
            if expected_version is not None and versions != {expected_version}:
                errors.append(
                    f"{relative(area)}: prototype specification version must be "
                    f"{expected_version!r}"
                )
            if len(statuses) != 1:
                errors.append(
                    f"{relative(area)}: specification chapters must share one status"
                )
            if not any(
                re.search(r"^## Status and authority\s*$", body, flags=re.MULTILINE)
                for _metadata, body in chapters
            ):
                errors.append(
                    f"{relative(area)}: specification area lacks a chapter with "
                    "## Status and authority"
                )

    # Require conceptual connections beyond automatic directory inventories.
    completed_paths = set(records)
    for path, (metadata, _body) in sorted(
        records.items(), key=lambda item: relative(item[0])
    ):
        if path.name == "README.md":
            continue
        outgoing = {
            target
            for target in links_by_source.get(path, set())
            if target == ROOT / "README.md" or target in completed_paths
        }
        if not outgoing and not incoming_from_conceptual.get(path):
            errors.append(
                f"{relative(path)}: no conceptual body link or incoming map link"
            )

    # Cross-document identifiers must remain unique.
    identifiers: dict[str, defaultdict[str, list[Path]]] = {
        key: defaultdict(list) for key in ("citation_key", "doi", "url")
    }
    for path, (metadata, _body) in records.items():
        if metadata.get("kind") != "source":
            continue
        counts["source_documents"] += 1
        for key, values in identifiers.items():
            value = metadata.get(key)
            if value:
                values[str(value).casefold()].append(path)
    for key, values in identifiers.items():
        for value, paths in sorted(values.items()):
            if len(paths) > 1:
                joined = ", ".join(relative(path) for path in sorted(paths))
                errors.append(f"duplicate {key} {value!r}: {joined}")

    if TRACEABILITY_REGISTRY.is_file():
        traceability_errors, traceability_counts = traceability_registry_errors(
            relative(TRACEABILITY_REGISTRY),
            TRACEABILITY_REGISTRY.read_text(encoding="utf-8"),
        )
        errors.extend(traceability_errors)
        counts.update(traceability_counts)

    return sorted(set(errors)), counts


def main() -> int:
    errors, counts = validate()
    if errors:
        print(f"Archive validation failed with {len(errors)} error(s):")
        for error in errors:
            print(f"- {error}")
        return 1

    summary = (
        "Archive validation passed: "
        f"{counts['completed_documents']} completed documents, "
        f"{counts['directories']} directories, "
        f"{counts['local_links']} local links, and "
        f"{counts['source_documents']} source notes checked; "
        f"{counts['specification_documents']} specification chapters and "
        f"{counts['specification_fenced_blocks']} classified fenced blocks checked"
    )
    obligations = counts.get("traceability_obligations", 0)
    if obligations:
        summary += (
            f"; {obligations} traceability obligations "
            f"({counts.get('traceability_traced', 0)} traced, "
            f"{counts.get('traceability_partial', 0)} partial, "
            f"{counts.get('traceability_untraced', 0)} untraced)"
        )
    print(summary + ".")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
