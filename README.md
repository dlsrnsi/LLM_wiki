# LLM Wiki

Local paper knowledge base scaffolded from the LLM Wiki gist.

## Start

1. Put new PDF files in `papers/My_papers/`.
2. Ask Codex: `Add these papers to the wiki.`
3. Ask research questions against the wiki.
4. Save strong answers as overview pages in `wiki/drug-discovery/overviews/`.
5. Open Obsidian from the `wiki/` folder and start at `main.md`.

The operating rules live in `CLAUDE.md`.

## Structure

- `data/papers.yml` is the canonical paper registry.
- `papers/*.pdf` contains canonical PDF copies named by paper id.
- `papers/My_papers/` is the raw drop-zone for user-provided files.
- `sources/*.md` contains structured source summaries.
- `wiki/main.md` is the Obsidian vault home page and links only to domain pages.
- `wiki/{domain}/{domain}-main.md` is the domain hub and links only to sub-domain/category pages.
- `wiki/{domain}/{sub-domain}/category-{sub-domain}.md` is the sub-domain hub and may compare papers inside that sub-domain.
- `wiki/{domain}/{sub-domain}/{paper-id}.md` contains readable paper notes.
- `wiki/{domain}/overviews/*.md` contains synthesis pages spanning multiple sub-domains.
- `index.md`, `main.md`, domain pages, and category pages are navigation/synthesis surfaces, not the canonical database.

## Wiki Organization Rules

- Preserve the `domain -> sub-domain -> paper` structure. The current domain is `drug-discovery`.
- The sub-domain structure should evolve organically as new papers are added. Add, split, merge, or rename sub-domains when the paper collection makes the structure more useful, but keep the domain layer stable.
- Optimize the wiki for Obsidian graph visualization: use unique page names, avoid generic `index.md` nodes, keep category hubs named `category-{sub-domain}.md`, and use folder-level grouping friendly to Graph color groups.
- Do not list papers in `wiki/main.md` or any `{domain}-main.md`. `main.md` should link only to domain pages. Domain main pages should link only to sub-domain/category pages.
- When adding a new paper to a sub-domain that already has papers, update that sub-domain's `category-*.md` with a comparative summary.
- Add paper-to-paper links only when there is a real connection in methods, materials/data, evaluation, or results. Avoid broad topic-only links.
- Structure paper notes so future RAG retrieval can extract needed knowledge from the folder hierarchy: domain, sub-domain, paper metadata, materials/data, methods, results, limitations, and explicit cross-links.
- Keep `data/papers.yml` as the canonical registry. The wiki folder is optimized for reading, visualization, and retrieval, not as the source database.

## PDF Text Extraction

```powershell
python tools\extract_pdf_text.py papers\your-paper.pdf
```

## Validate

```powershell
python tools\validate_wiki.py
```

## Notion Sync

Use Notion as a publishing and collaboration layer, not as the source of truth.

- Keep `wiki/` as the canonical knowledge base for Obsidian and RAG.
- Sync from local markdown to Notion in one direction: `wiki/ -> Notion`.
- Track Notion page IDs and sync hashes in `data/notion-sync.yml`.
- Generate a Notion-ready manifest with:

```powershell
python tools\build_notion_sync_payload.py
```

The generated `data/notion-sync-payload.json` can be used by Codex with the Notion MCP tools to create or update pages. Do not manually edit Notion content and expect it to flow back into `wiki/`; make source edits in markdown first, then sync again.
