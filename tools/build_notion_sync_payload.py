from __future__ import annotations

import hashlib
import json
import re
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
WIKI_ROOT = ROOT / "wiki"
OUTPUT = ROOT / "data" / "notion-sync-payload.json"
CONFIG = ROOT / "data" / "notion-sync.yml"


FRONTMATTER_RE = re.compile(r"\A---\s*\n(.*?)\n---\s*\n?", re.DOTALL)


def notion_title_property() -> str:
    if not CONFIG.exists():
        return "Title"

    in_properties = False
    for line in CONFIG.read_text(encoding="utf-8").splitlines():
        stripped = line.strip()
        if stripped == "properties:":
            in_properties = True
            continue
        if in_properties and line and not line.startswith((" ", "\t")):
            break
        if in_properties and stripped.startswith("title:"):
            return stripped.split(":", 1)[1].strip() or "Title"
    return "Title"


def parse_scalar(value: str) -> object:
    value = value.strip()
    if not value:
        return ""
    if value in {"[]", "{}"}:
        return [] if value == "[]" else {}
    if value.startswith('"') and value.endswith('"'):
        return value[1:-1]
    if value.startswith("'") and value.endswith("'"):
        return value[1:-1]
    if value.isdigit():
        return int(value)
    return value


def parse_frontmatter(text: str) -> tuple[dict[str, object], str]:
    match = FRONTMATTER_RE.match(text)
    if not match:
        return {}, text

    metadata: dict[str, object] = {}
    for line in match.group(1).splitlines():
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        metadata[key.strip()] = parse_scalar(value)

    return metadata, text[match.end() :]


def first_heading(markdown: str) -> str | None:
    for line in markdown.splitlines():
        if line.startswith("# "):
            return line[2:].strip()
    return None


def infer_page_type(relative_path: str, metadata: dict[str, object]) -> str:
    path = Path(relative_path)
    name = path.name
    parts = path.parts

    if relative_path == "main.md":
        return "root"
    if len(parts) == 2 and name.endswith("-main.md"):
        return "domain-main"
    if name.startswith("category-"):
        return "category"
    if "overviews" in parts:
        return "overview"
    if "concepts" in parts:
        return "concept"
    if metadata.get("id"):
        return "paper"
    return "note"


def infer_domain_subdomain(relative_path: str, metadata: dict[str, object]) -> tuple[str, str]:
    parts = Path(relative_path).parts
    domain = str(metadata.get("domain") or (parts[0] if len(parts) > 1 else ""))
    sub_domain = str(metadata.get("category") or "")

    if not sub_domain and len(parts) >= 3:
        sub_domain = parts[1]
    if not sub_domain and len(parts) == 2 and parts[1].startswith("category-"):
        sub_domain = parts[0]

    return domain, sub_domain


def build_page(path: Path) -> dict[str, object]:
    text = path.read_text(encoding="utf-8")
    metadata, body = parse_frontmatter(text)
    relative_path = path.relative_to(WIKI_ROOT).as_posix()
    title = str(metadata.get("title") or first_heading(body) or path.stem)
    page_type = infer_page_type(relative_path, metadata)
    domain, sub_domain = infer_domain_subdomain(relative_path, metadata)
    sync_hash = hashlib.sha256(text.encode("utf-8")).hexdigest()
    title_property = notion_title_property()
    properties: dict[str, object] = {
        title_property: title,
        "Page Type": page_type,
        "Domain": domain,
        "Sub-domain": sub_domain,
        "Wiki Path": f"wiki/{relative_path}",
        "Sync Hash": sync_hash,
    }
    if metadata.get("id"):
        properties["Paper ID"] = str(metadata["id"])
    if metadata.get("year"):
        properties["Year"] = metadata["year"]
    if metadata.get("status"):
        properties["Status"] = str(metadata["status"])

    return {
        "title": title,
        "relative_path": relative_path,
        "absolute_path": str(path),
        "page_type": page_type,
        "properties": properties,
        "content": body.strip() + "\n",
    }


def main() -> None:
    pages = [
        build_page(path)
        for path in sorted(WIKI_ROOT.rglob("*.md"))
        if ".obsidian" not in path.parts
    ]
    payload = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "source_root": str(WIKI_ROOT),
        "page_count": len(pages),
        "pages": pages,
    }
    OUTPUT.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Wrote {OUTPUT} with {len(pages)} pages.")


if __name__ == "__main__":
    main()
