---
id: chen-2025-bmfm-dna-a-snp-aware
domain: genomics
title: "BMFM-DNA: A SNP-aware DNA foundation model to capture variant effects"
authors:
  - Hongyang Li
  - Sanjoy Dey
  - Bum Chul Kwon
  - Michael Danziger
  - Michal Rosen-Tzvi
  - Jianying Hu
  - James Kozloski
  - Ching-Huei Tsou
  - Bharath Dandala
  - Pablo Meyer
year: 2025
doi: 10.48550/arXiv.2507.05265
source: chen-2025-bmfm-dna-a-snp-aware.md
category: genomic-foundation-models
pdf_path: /C:/Users/dlsrnsi/OneDrive/문서/New project/papers/chen-2025-bmfm-dna-a-snp-aware.pdf
pdf_filename: chen-2025-bmfm-dna-a-snp-aware.pdf
source_collection: web-open-access
status: draft
tags: [genomics, foundation-models, snp-aware, variants]
---

## Summary

BMFM-DNA tests whether DNA foundation models improve when pretraining includes SNP variation rather than only reference genome sequence.

## Key Contributions

- Builds BMFM-DNA-REF from reference sequence and reverse complements.
- Builds BMFM-DNA-SNP from variant-encoded sequences using dbSNP.
- Uses ModernBERT and BPE for masked language modeling.
- Evaluates promoter, splice, TFBS, MPRA, and SNP-disease tasks.

## Materials and Data

The reference model samples 1-10 kb sequences from GRCh38 and reverse complements them, yielding 9,982,678 samples and roughly 60 billion nucleotides. The SNP-aware model uses dbSNP-derived variation frequencies to sample variant-encoded DNA. Fine-tuning includes GUE-style tasks, lenti-MPRA promoter activity, and SNP-disease association data from GWAS Catalog and ClinVar.

## Methods

### Inputs and Representations

BMFM-DNA-SNP represents variant states with special characters so that a single position can encode possible allelic variation. BPE tokenization with 4,096 tokens is used.

### Model / Algorithm / Workflow

The model uses ModernBERT with masked language modeling. Two pretraining regimes are compared: reference-only and SNP-aware.

### Training, Inference, or Search Procedure

Both models are pretrained on sampled DNA sequences and fine-tuned on biologically meaningful tasks. The paper also experiments with SNP imputation strategies on promoter detection.

### Baselines and Evaluation Protocol

The main comparison is reference-only versus SNP-aware pretraining, with context from DNABERT-2 and GENA-LM-style genomic foundation models.

## Results

The paper reports improvements across fine-tuning tasks when sequence variation is encoded during pretraining. Its key result for GLFM is conceptual: reference-only DNA language models miss natural genetic variation, while variant-aware pretraining can improve functional prediction.

## Limitations

BMFM-DNA is SNP-aware but not fully LD-aware. It encodes variant possibilities in sequence data but does not directly model phased haplotypes, LD dependencies, GWAS association signals, or causal fine-mapping.

## Related Papers

- [[zhou-2024-dnabert-2-efficient-foundation-model]] - Method/benchmark connection: BMFM-DNA builds on BPE and GUE-style evaluation.
- [[genomics/genotype-language-models/huang-2026-genobert-a-language-model-for]] - Method connection: both move beyond reference-only sequence; GenoBERT models phased genotypes directly.
- [[genomics/fine-mapping/lee-2026-genomic-language-based-finemapping]] - Method connection: both are relevant to variant-aware genomic language modeling.
