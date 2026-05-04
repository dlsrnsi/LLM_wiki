---
id: schiff-2024-caduceus-bi-directional-equivariant-long
domain: genomics
title: "Caduceus: Bi-Directional Equivariant Long-Range DNA Sequence Modeling"
authors:
  - Yair Schiff
  - Chia-Hsiang Kao
  - Aaron Gokaslan
  - Tri Dao
  - Albert Gu
  - Volodymyr Kuleshov
year: 2024
doi: 10.48550/arXiv.2403.03234
source: schiff-2024-caduceus-bi-directional-equivariant-long.md
category: genomic-foundation-models
pdf_path: /C:/Users/dlsrnsi/OneDrive/문서/New project/papers/schiff-2024-caduceus-bi-directional-equivariant-long.pdf
pdf_filename: schiff-2024-caduceus-bi-directional-equivariant-long.pdf
source_collection: web-open-access
status: draft
tags: [genomics, foundation-models, mamba, reverse-complement]
---

## Summary

Caduceus adapts Mamba-style long-range sequence modeling to DNA by adding bidirectionality and reverse-complement equivariance.

## Key Contributions

- Introduces BiMamba as a bidirectional extension of Mamba.
- Introduces MambaDNA for reverse-complement equivariance.
- Builds Caduceus-PS and Caduceus-Ph as DNA foundation model variants.
- Shows benefits on long-range variant effect prediction.

## Materials and Data

Pretraining uses the human reference genome with base-level tokenization. Downstream tasks include regulatory sequence benchmarks and variant effect prediction, especially cases requiring long-range context.

## Methods

### Inputs and Representations

Caduceus uses nucleotide/base-pair tokens. The model treats reverse-complement symmetry as an architectural property rather than only a data augmentation trick.

### Model / Algorithm / Workflow

BiMamba processes a sequence forward and backward with shared projections. MambaDNA adds reverse-complement processing with shared parameters, producing a block whose output transforms consistently under reverse complement.

### Training, Inference, or Search Procedure

Caduceus-PS uses RC-equivariant language modeling under masked language modeling. Caduceus-Ph uses RC data augmentation during pretraining and post-hoc conjoining during downstream inference.

### Baselines and Evaluation Protocol

The paper compares against HyenaDNA, CNNs, and other sequence models on genomic benchmarks and long-range variant effect prediction.

## Results

Caduceus outperforms similar-size SSM models and is reported to outperform models up to 10x larger on some long-range tasks when those models lack bidirectionality or RC equivariance. Its strongest relevance here is showing that DNA-specific inductive biases can materially improve foundation-model behavior.

## Limitations

Caduceus is not genotype- or LD-aware. It models DNA sequence context and reverse-complement symmetry, but not population LD, genotype imputation, phenotype fine-tuning, or causal SNP scoring.

## Related Papers

- [[nguyen-2023-hyenadna-long-range-genomic-sequence]] - Architecture connection: both use attention-free long-context sequence modeling.
- [[genomics/fine-mapping/lee-2026-genomic-language-based-finemapping]] - Method contrast: Caduceus encodes DNA strand/context priors; GLFM encodes LD-aware genotype context.
