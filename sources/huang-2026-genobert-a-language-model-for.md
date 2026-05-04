---
id: huang-2026-genobert-a-language-model-for
domain: genomics
title: "GenoBERT: A Language Model for Accurate Genotype Imputation"
authors: Lei Huang; Chuan Qiu; Kuan-Jui Su; Anqi Liu; Yun Gong; Weiqiang Lin; Lindong Jiang; Chen Zhao; Meng Song; Jeffrey Deng; Qing Tian; Zhe Luo; Ping Gong; Hui Shen; Chaoyang Zhang; Hong-Wen Deng
year: 2026
doi: 10.48550/arXiv.2604.00058
category: genotype-language-models
pdf_path: /C:/Users/dlsrnsi/OneDrive/문서/New project/papers/huang-2026-genobert-a-language-model-for.pdf
pdf_filename: huang-2026-genobert-a-language-model-for.pdf
source_collection: web-open-access
status: draft
---

## One-line Summary

GenoBERT is a transformer genotype language model for reference-free genotype imputation, designed to capture short- and long-range LD dependencies from phased genotype tokens.

## 1. Document Information

arXiv 2026 paper focused on genotype imputation.

## 2. Key Contributions

- Tokenizes phased genotype states as language-model tokens.
- Uses self-attention to capture short- and long-range LD dependencies.
- Introduces relative genomic positional bias based on SNP coordinates.
- Benchmarks against Beagle5.4, SCDA, BiU-Net, and STICI.
- Evaluates across missingness levels, ancestry groups, and MAF bins.

## 3. Materials and Data

The paper benchmarks on the Louisiana Osteoporosis Study and 1000 Genomes Project datasets. Missing genotype ratios range from 5% to 50%. Evaluation spans ancestry groups and allele-frequency ranges, including rare and ultra-rare variants.

## 4. Methodology and Architecture

GenoBERT represents each sample as genotype segments. Phased genotype states are encoded as discrete tokens: Ref|Ref, Ref|Alt, Alt|Ref, Alt|Alt, and missing/masked states. The model uses Transformer encoder blocks with multi-head attention, RoPE positional embeddings, optional parameter sharing, residual scaling, and a 1D CNN bottleneck for local genomic patterns.

Its most GLFM-relevant component is Relative Genomic Positional Bias (RGPB). For a segment, SNP genomic coordinates are standardized into a bias vector. Pairwise relative genomic distances form a bias matrix that is added to attention logits with layer/head-specific coefficients:

$$
\operatorname{Attention}^{(l,h)}
=
\operatorname{Softmax}\left(
\frac{Q^{(h)}K^{(h)T}}{\sqrt{d/H}}+\beta_{l,h}B_s
\right)V^{(h)}
$$

This gives attention direct access to genomic distance while the genotype tokens encode haplotype/LD content.

## 5. Key Results and Benchmarks

GenoBERT reports high imputation accuracy at practical sparsity levels, with \(r^2 \approx 0.98\) up to 25% missingness and \(r^2 > 0.90\) even at 50% missingness. It reports the highest overall accuracy compared with Beagle5.4, SCDA, BiU-Net, and STICI. The paper validates a 128-SNP context window, roughly 100 kb, through LD-decay analyses as sufficient to capture local correlation structure.

## 6. Limitations and Future Work

GenoBERT is optimized for genotype imputation, not causal fine-mapping. Good LD reconstruction does not automatically imply causal SNP identification. The paper notes weaker performance in extremely weak-LD settings and suggests LD-adaptive attention and population-aware modeling as future directions.

## 7. Related Work

- [[genomics/fine-mapping/lee-2026-genomic-language-based-finemapping]] - Strong method connection: both are genotype language models that care about LD; GenoBERT uses LD for imputation, while GLFM uses genotype/LD representations for fine-mapping.
- [[genomics/genomic-foundation-models/chen-2025-bmfm-dna-a-snp-aware]] - Variant-modeling connection: BMFM-DNA encodes SNP variation in DNA sequences; GenoBERT directly tokenizes phased genotypes.

## 8. Glossary

- Genotype imputation: Predicting missing genotypes from observed genotype context.
- RGPB: Relative Genomic Positional Bias.
- LD: Linkage disequilibrium, correlation structure among variants.
