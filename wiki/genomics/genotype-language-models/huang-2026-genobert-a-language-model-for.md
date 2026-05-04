---
id: huang-2026-genobert-a-language-model-for
domain: genomics
title: "GenoBERT: A Language Model for Accurate Genotype Imputation"
authors:
  - Lei Huang
  - Chuan Qiu
  - Kuan-Jui Su
  - Anqi Liu
  - Yun Gong
  - Weiqiang Lin
  - Lindong Jiang
  - Chen Zhao
  - Meng Song
  - Jeffrey Deng
  - Qing Tian
  - Zhe Luo
  - Ping Gong
  - Hui Shen
  - Chaoyang Zhang
  - Hong-Wen Deng
year: 2026
doi: 10.48550/arXiv.2604.00058
source: huang-2026-genobert-a-language-model-for.md
category: genotype-language-models
pdf_path: /C:/Users/dlsrnsi/OneDrive/문서/New project/papers/huang-2026-genobert-a-language-model-for.pdf
pdf_filename: huang-2026-genobert-a-language-model-for.pdf
source_collection: web-open-access
status: draft
tags: [genomics, genotype-language-models, imputation, ld]
---

## Summary

GenoBERT is a BERT-style genotype language model for reference-free genotype imputation. It is the closest current comparison point for GLFM's BERT encoder because it reads genotype states and explicitly targets LD dependency learning.

## Key Contributions

- Treats phased genotype segments as language-model sequences.
- Uses masked genotype recovery for imputation.
- Adds relative genomic positional bias to attention.
- Combines attention with a 1D CNN bottleneck for local genotype patterns.
- Benchmarks across missingness, ancestry, and MAF settings.

## Materials and Data

The paper evaluates on the Louisiana Osteoporosis Study and 1000 Genomes Project datasets. Missingness levels range from 5% to 50%. Evaluation is stratified by ancestry and minor allele frequency, including rare and ultra-rare variants.

## Methods

### Inputs and Representations

Each SNP segment is encoded as phased genotype tokens: Ref|Ref, Ref|Alt, Alt|Ref, Alt|Alt, and missing/masked states. `[CLS]`, `[SEP]`, and `[PAD]` tokens are added as needed.

### Model / Algorithm / Workflow

The architecture stacks Transformer encoder blocks with multi-head attention, RoPE, residual scaling, and a 1D CNN bottleneck. Optional parameter sharing follows ALBERT-like design choices.

### Training, Inference, or Search Procedure

Training masks SNP genotypes and asks the model to reconstruct them from context. This directly turns LD structure into the prediction signal.

### Baselines and Evaluation Protocol

Baselines include Beagle5.4, SCDA, BiU-Net, and STICI. Metrics include imputation \(r^2\), F1, ancestry-stratified performance, and missingness robustness.

### Relative Genomic Positional Bias

GenoBERT computes a bias matrix from actual genomic coordinates within each SNP segment and adds it to attention logits:

$$
\operatorname{Attention}^{(l,h)}
=
\operatorname{Softmax}\left(
\frac{Q^{(h)}K^{(h)T}}{\sqrt{d/H}}+\beta_{l,h}B_s
\right)V^{(h)}
$$

This helps the model distinguish similar genotype patterns from different genomic regions and gives attention direct access to genomic distance.

## Results

GenoBERT reports \(r^2 \approx 0.98\) up to 25% missingness and \(r^2 > 0.90\) even at 50% missingness. It outperforms Beagle5.4, SCDA, BiU-Net, and STICI overall. A 128-SNP window, roughly 100 kb, is validated by LD-decay analyses as sufficient for local correlation structure.

## Limitations

GenoBERT is an imputation model, not a fine-mapping model. It learns LD for genotype reconstruction, but it does not use phenotype labels or output causal SNP probabilities. Its rare underperformance appears in extremely weak-LD settings, motivating LD-adaptive attention and population-aware modeling.

## Related Papers

- [[genomics/fine-mapping/lee-2026-genomic-language-based-finemapping]] - Strong method connection: both use BERT-style genotype representations; GenoBERT optimizes imputation, GLFM optimizes fine-mapping.
- [[genomics/genomic-foundation-models/chen-2025-bmfm-dna-a-snp-aware]] - Method connection: both move beyond reference-only DNA sequence toward variant/genotype-aware modeling.
