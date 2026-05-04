"""Validate LLM Wiki registry links and document frontmatter."""

from __future__ import annotations

import re
from pathlib import Path


def scalar(block: str, name: str) -> str | None:
    match = re.search(rf"^    {name}: (.+)$", block, re.MULTILINE)
    if not match:
        return None
    return match.group(1).strip().strip('"')


def raw_imports(block: str) -> list[str]:
    if "raw_imports:" not in block:
        return []
    raw_block = block.split("raw_imports:", 1)[1].split("\n\n", 1)[0]
    return [
        match.group(1).strip().strip('"')
        for match in re.finditer(r"^      - (.+)$", raw_block, re.MULTILINE)
    ]


def main() -> None:
    registry = Path("data/papers.yml")
    if not registry.exists():
        raise SystemExit("Missing registry: data/papers.yml")

    errors: list[str] = []
    text = registry.read_text(encoding="utf-8")
    entries = re.split(r"\n  - id: ", text)[1:]

    for entry in entries:
        paper_id = entry.split("\n", 1)[0].strip()

        domain = scalar(entry, "domain")
        if not domain:
            errors.append(f"{paper_id}: missing registry field domain")

        for field in ("pdf", "source", "wiki"):
            value = scalar(entry, field)
            if not value:
                errors.append(f"{paper_id}: missing registry field {field}")
                continue
            if not Path(value).exists():
                errors.append(f"{paper_id}: missing {field} file {value}")

        for raw_path in raw_imports(entry):
            if raw_path.startswith(("http://", "https://")):
                continue
            if not Path(raw_path).exists():
                errors.append(f"{paper_id}: missing raw import {raw_path}")

        source = scalar(entry, "source")
        if source and Path(source).exists():
            source_text = Path(source).read_text(encoding="utf-8")
            if f"id: {paper_id}" not in source_text:
                errors.append(f"{paper_id}: source frontmatter id mismatch")
            if domain and f"domain: {domain}" not in source_text:
                errors.append(f"{paper_id}: source frontmatter domain mismatch")
            if "status:" not in source_text:
                errors.append(f"{paper_id}: source missing status")

        wiki = scalar(entry, "wiki")
        if wiki and Path(wiki).exists():
            wiki_text = Path(wiki).read_text(encoding="utf-8")
            if f"id: {paper_id}" not in wiki_text:
                errors.append(f"{paper_id}: wiki frontmatter id mismatch")
            if domain and f"domain: {domain}" not in wiki_text:
                errors.append(f"{paper_id}: wiki frontmatter domain mismatch")
            if "status:" not in wiki_text:
                errors.append(f"{paper_id}: wiki missing status")

    if errors:
        raise SystemExit("\n".join(errors))

    print(f"OK: {len(entries)} papers validated")


if __name__ == "__main__":
    main()
