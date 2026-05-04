"""Extract the first pages of a PDF for LLM Wiki ingestion."""

from __future__ import annotations

import argparse
from pathlib import Path

import pypdf


def extract_text(pdf_path: Path, max_pages: int, max_chars: int) -> str:
    reader = pypdf.PdfReader(str(pdf_path))
    chunks: list[str] = []

    for page in reader.pages[:max_pages]:
        text = page.extract_text()
        if text:
            chunks.append(text)

        joined = "\n".join(chunks)
        if len(joined) >= max_chars:
            return joined[:max_chars]

    return "\n".join(chunks)[:max_chars]


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Extract text from a PDF for LLM Wiki source summaries."
    )
    parser.add_argument("pdf", type=Path, help="Path to the PDF file")
    parser.add_argument("--pages", type=int, default=15, help="Max pages to extract")
    parser.add_argument("--chars", type=int, default=12000, help="Max characters to print")
    args = parser.parse_args()

    if not args.pdf.exists():
        raise SystemExit(f"PDF not found: {args.pdf}")

    print(extract_text(args.pdf, args.pages, args.chars))


if __name__ == "__main__":
    main()
