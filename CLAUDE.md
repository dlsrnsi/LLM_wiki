# LLM Wiki - For Research

A personal knowledge base of academic papers, following the LLM Wiki pattern:

```text
Original PDF -> sources/*.md (LLM summary) -> wiki/{domain}/{sub-domain}/*.md (final page)
```

**Language policy**: All wiki content is in English. Conversation can be in any language.

---

## The Four Rules

These rules are the core of the system. They prevent hallucination and keep every claim traceable.

1. **No web search.** Never use web search or web fetch to fill gaps. The point of this wiki is that every answer is grounded in papers we actually have.
2. **Answer from the wiki first.** Use `data/`, `sources/`, and `wiki/` as the only sources of truth.
3. **If the wiki is insufficient, re-read the PDF.** Go to the PDF listed in `data/papers.yml`, extract more detail with `pypdf`, then update the source and wiki pages.
4. **If the wiki has no paper on the topic, say so.** Tell the user: "I don't have a paper on this - please give me the PDF." Do not improvise.

These rules apply to every response, including overview pages: cite only papers that exist in the wiki.

---

## Repository Structure

```text
.
+-- CLAUDE.md
+-- README.md
+-- index.md
+-- data/
|   +-- categories.yml
|   +-- papers.yml
|   +-- ingest-log.yml
+-- papers/
|   +-- {paper-id}.pdf
|   +-- My_papers/              # user drop-zone / raw imports
+-- sources/
|   +-- {paper-id}.md
+-- wiki/
    +-- main.md
    +-- {domain}/
        +-- {domain}-main.md
        +-- {sub-domain}/
        |   +-- category-{sub-domain}.md
        |   +-- {paper-id}.md
        +-- overviews/
        +-- concepts/
        +-- other/
```

## Data Structure

`data/papers.yml` is the registry and source of truth for ingested papers. Every paper entry must include:

- `id`: canonical stem shared by PDF, source summary, and wiki page
- `title`, `authors`, `year`, `doi`
- `domain`, `category`
- `pdf`, `source`, `wiki`
- `status`: `stub`, `draft`, or `reviewed`
- `raw_imports`: original user-provided files, when known

`data/categories.yml` defines category names, descriptions, and folder paths.

`data/ingest-log.yml` records ingest batches, added IDs, and duplicates.

`index.md` is only the project-level catalog. `wiki/main.md`, domain pages, and category pages are navigation/synthesis surfaces. Category pages are named `category-{sub-domain}.md` so Obsidian graph nodes remain distinct. Do not treat any of these navigation pages as the canonical database.

## Wiki Organization Rules

The wiki must remain friendly to both Obsidian visualization and future RAG-style retrieval.

User-mandated rules for this project:

- The wiki structure may change organically as papers are added, but the `domain -> sub-domain -> paper` hierarchy must be preserved.
- Prefer structures that make Obsidian graph visualization readable: stable folders, semantic clusters, unique hub names, and minimal hub-to-paper clutter.
- When a new paper is added to a sub-domain that already has papers, update that sub-domain's comparative summary.
- Create paper-to-paper links only when the connection is grounded in methods, materials/data, evaluation, or results.
- Do not add paper links to `wiki/main.md` or `{domain}-main.md`; `main.md` links only to domain pages, and domain main pages link only to sub-domain/category pages.
- Structure notes for future RAG use so that knowledge can be retrieved by domain, sub-domain, metadata, materials/data, methods, results, limitations, and explicit evidence-grounded links.

1. Preserve the `domain -> sub-domain -> paper` structure. The current domain is `drug-discovery`.
2. Let sub-domains evolve organically as new papers arrive. Add, split, merge, or rename sub-domains when the collection demands it, but keep the domain layer stable.
3. Optimize for Obsidian graph visualization:
   - avoid generic page names such as `index.md`;
   - keep category hubs named `category-{sub-domain}.md`;
   - keep folders aligned with semantic clusters;
   - maintain Graph color groups when folders move or new sub-domains are added.
4. `wiki/main.md` must link only to domain pages. Do not list papers or "start here" paper links there.
5. `wiki/{domain}/{domain}-main.md` must link only to sub-domain/category pages. Do not list individual papers there.
6. When adding a paper to a sub-domain that already has papers, update `wiki/{domain}/{sub-domain}/category-{sub-domain}.md` with a comparative summary.
7. Add paper-to-paper links only when there is a concrete connection in methods, materials/data, evaluation, or results. Do not add broad topic-only links.
8. Paper notes should support RAG extraction. Keep consistent sections for summary, materials/data, methods, results, limitations, and related papers with explicit rationale for links.
9. `data/papers.yml` remains the canonical registry. The wiki folder is for reading, visual graph navigation, and retrieval-oriented knowledge extraction.

## Paper Note Quality Standard

Do not create skeletal paper notes. A new paper note should be detailed enough that a future RAG query can answer concrete questions about what data were used, what method was proposed, how it was evaluated, and what the main findings were without reopening the PDF for basic facts.

Minimum density for normal research papers:

- `Materials and Data`: name the datasets, sources, cohorts, compounds/proteins/variants/tasks, sample sizes, train/validation/test splits, filtering rules, assay conditions, and external validation sets when the paper reports them.
- `Methods`: describe the actual model/algorithm/workflow, not just the high-level topic. Include architecture components, input representations, losses/objectives, priors, equations, training or inference procedure, baselines, and evaluation protocol where applicable.
- `Results`: include concrete metrics, benchmark numbers, ablation results, external validation results, qualitative findings, and the authors' strongest empirical claims. Do not write only "the method performed well."
- `Limitations`: record data limitations, modeling assumptions, failure modes, scope limits, and what the paper does not prove.
- `Related Papers`: add links only for method/material/evaluation/result connections, and explain the connection in the bullet.

Extra requirements by paper type:

- Statistical/mathematical methods: write the core notation and equations in detail. Include likelihoods, priors, posterior quantities, optimization or search procedures, and how reported probabilities or scores are computed.
- Deep learning papers: record input encoding, model blocks, pretraining/fine-tuning scheme, objective/loss, hyperparameters when reported, baselines, and interpretability analyses.
- Review papers: summarize the taxonomy, data/resource families, method families, major conclusions, and recurring bottlenecks. Do not treat reviews as empty background pages.
- Application or screening papers: capture the full experimental/computational workflow from input data to validation, including library sizes, filtering steps, hit criteria, assay setup, and hit/validation results.
- Background/citation papers added to support another paper must still be independently useful. At minimum, explain why the citation matters, its materials/tasks, method, key results, and limitations.

Quality gate before finishing an ingest:

1. Re-read the PDF if any of `Materials and Data`, `Methods`, or `Results` is only one short paragraph.
2. Prefer concrete numbers from the paper over generic summaries.
3. If a section is genuinely not applicable, say why. Do not leave it empty.
4. Update both `sources/{paper-id}.md` and `wiki/{domain}/{sub-domain}/{paper-id}.md` to the same evidence level; the source tier can be more extraction-like, and the wiki tier can be more readable/synthetic.
5. Run `python tools\validate_wiki.py` after changes.

## File Naming Convention

All three tiers (PDF, source, wiki) share the same stem:

```text
{first-author-lastname}-{year}-{first-5-title-words}.{ext}
```

- Lowercase, special chars stripped, spaces become hyphens
- Year is 4 digits
- Consortium papers use the consortium name

Example: `pollard-2006-an-rna-gene-expressed-during.pdf`

## Categories

This wiki currently focuses on AI for drug discovery, especially drug-target interaction prediction, protein or peptide sequence models, binding-site interpretation, virtual screening, and safety prediction. Start small and split a category when it passes about 500 files.

| Category | Includes |
|---|---|
| `drug-target-interactions` | DTI prediction models, protein sequence models for target interaction, network-based DTI |
| `binding-sites-virtual-screening` | Binding-region prediction, pharmacophore modeling, docking, virtual screening |
| `admet-safety` | Toxicity, hERG, ADMET, safety-related prediction models |
| `peptide-function` | Antimicrobial peptide and peptide function prediction |
| `reviews` | Survey and review papers |
| `concepts` | Key methods, algorithms, theories, and reusable explanations |
| `overviews` | Synthesis pages spanning multiple papers |
| `other` | Cross-cutting or uncategorized papers |

Classify by method or evidence type where possible, not only by topic.

---

## Adding a New Paper

### Step 1 - Copy PDF to canonical `papers/`

Use `papers/My_papers/` as the raw drop-zone. After identifying metadata, copy each unique PDF to:

```text
papers/{paper-id}.pdf
```

Do not delete user-provided raw files unless explicitly asked.

### Step 2 - Extract text

Use `pypdf`:

```powershell
python tools\extract_pdf_text.py papers\{paper-id}.pdf
```

### Step 3 - Write `sources/{paper-id}.md`

```yaml
---
id: paper-id
domain: drug-discovery
title: "Paper Title"
authors: Author List
year: YYYY
doi: DOI
category: sub-domain
pdf_path: /full/path/to/papers/{paper-id}.pdf
pdf_filename: {paper-id}.pdf
source_collection: external
status: draft
---

## One-line Summary
## 1. Document Information
## 2. Key Contributions
## 3. Materials and Data
## 4. Methodology and Architecture
### Inputs and Representations
### Model / Algorithm / Workflow
### Training, Inference, or Search Procedure
### Baselines and Evaluation Protocol
## 5. Key Results and Benchmarks
## 6. Limitations and Future Work
## 7. Related Work
## 8. Glossary
```

### Step 4 - Write `wiki/{domain}/{sub-domain}/{paper-id}.md`

```yaml
---
id: paper-id
domain: drug-discovery
title: "Paper Title"
authors: Author list
year: YYYY
doi: DOI
source: {paper-id}.md
category: sub-domain
pdf_path: /full/path/to/papers/{paper-id}.pdf
pdf_filename: {paper-id}.pdf
source_collection: external
status: draft
tags: []
---

## Summary
## Key Contributions
## Materials and Data
## Methods
### Inputs and Representations
### Model / Algorithm / Workflow
### Training, Inference, or Search Procedure
### Baselines and Evaluation Protocol
## Results
## Limitations
## Related Papers
- [[sub-domain/page]] - method/material/result connection only
```

### Step 5 - Update the registries

Update these files in this order:

1. `data/papers.yml`
2. `data/ingest-log.yml`
3. `wiki/{domain}/{sub-domain}/category-{sub-domain}.md`
4. `index.md`

If the sub-domain already has at least one paper, update the category page with a comparative summary that explains how the new paper differs in methods, materials/data, evaluation, and results.

---

## PDF Management Rules

- Always copy PDFs into canonical `papers/{paper-id}.pdf`; never symlink.
- Keep user-provided raw files in `papers/My_papers/`.
- `pdf_path` always points to the canonical PDF in `papers/`.
- `pdf_filename` must match `basename(pdf_path)`.
- `data/papers.yml` must record any known raw imports.

## Knowledge Compounding

The most valuable pages are `wiki/drug-discovery/overviews/` pages that synthesize across papers. When a question is answered well, save the answer:

> Save this as an overview page in `wiki/drug-discovery/overviews/`.

Over time the wiki becomes a searchable, cross-referenced knowledge graph.

## Browsing

Use Obsidian to open the `wiki/` folder as a vault when visual navigation, backlinks, graph view, and full-text search are useful. Start from `wiki/main.md`. Obsidian reads markdown files directly and works well with `[[wikilinks]]`.
