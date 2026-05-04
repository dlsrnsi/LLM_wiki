---
id: zhou-2024-dnabert-2-efficient-foundation-model
domain: genomics
title: "DNABERT-2: Efficient Foundation Model and Benchmark For Multi-Species Genome"
authors:
  - Zhihan Zhou
  - Yanrong Ji
  - Weijian Li
  - Pratik Dutta
  - Ramana V. Davuluri
  - Han Liu
year: 2024
doi: 10.48550/arXiv.2306.15006
source: zhou-2024-dnabert-2-efficient-foundation-model.md
category: genomic-foundation-models
pdf_path: /C:/Users/dlsrnsi/OneDrive/문서/New project/papers/zhou-2024-dnabert-2-efficient-foundation-model.pdf
pdf_filename: zhou-2024-dnabert-2-efficient-foundation-model.pdf
source_collection: web-open-access
status: draft
tags: [genomics, foundation-models, dnabert, tokenization]
---

## Summary

DNABERT-2 is an efficient successor to DNABERT that replaces k-mer tokenization with BPE and introduces a standardized multi-species benchmark for genome foundation models.

## Key Contributions

- Reframes DNA tokenization as a major bottleneck for scalable genome foundation models.
- Uses BPE to avoid the leakage and instability problems of overlapping and non-overlapping k-mers.
- Introduces a more efficient Transformer encoder using ALiBi and FlashAttention.
- Provides GUE/GUE+ as a standardized benchmark for genome understanding.

## Materials and Data

DNABERT-2 is pretrained on multi-species genome data. Its benchmark includes 36 datasets across 9 tasks, with sequence lengths from 70 to 10,000 nucleotides. The benchmark is designed to make model comparisons fairer than prior paper-specific preprocessing pipelines.

## Methods

### Inputs and Representations

The central representation change is BPE tokenization. Overlapping k-mers can leak information during masked language modeling because neighboring k-mers expose much of a masked token. Non-overlapping k-mers reduce sequence length but can make shifted near-identical sequences tokenize very differently. BPE instead learns variable-length DNA tokens from co-occurrence statistics.

### Model / Algorithm / Workflow

DNABERT-2 uses a Transformer encoder with ALiBi positional bias, FlashAttention, low-precision layer normalization, and optional LoRA fine-tuning. ALiBi inserts distance-dependent bias into attention scores, reducing reliance on fixed learned positional embeddings.

### Training, Inference, or Search Procedure

The model is pretrained with masked language modeling and fine-tuned on GUE tasks.

### Baselines and Evaluation Protocol

The paper compares DNABERT-2 with DNABERT and larger genome foundation models using standardized GUE/GUE+ tasks.

## Results

DNABERT-2 is reported to match state-of-the-art performance with 21x fewer parameters and about 92x less GPU pretraining time. Compared with DNABERT, it is about 3x more efficient and outperforms DNABERT on 23 of 28 datasets, with an average improvement of 6 absolute points on GUE.

## Limitations

DNABERT-2 is still a sequence-only model. It improves the genomic language model backbone but does not explicitly encode LD, phased genotypes, phenotype labels, or causal SNP perturbation.

## Related Papers

- [[ji-2021-dnabert-pre-trained-bidirectional-encoder]] - Method lineage: DNABERT-2 directly addresses DNABERT's tokenization and efficiency limitations.
- [[dalla-torre-2025-nucleotide-transformer-building-and]] - Method/evaluation connection: both are genome foundation models evaluated across diverse sequence tasks.
- [[genomics/fine-mapping/lee-2026-genomic-language-based-finemapping]] - Method contrast: DNABERT-2 improves sequence-only DNA language modeling; GLFM uses genotype/LD-aware BERT representations for fine-mapping.
