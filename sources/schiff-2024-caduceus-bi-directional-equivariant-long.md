---
id: schiff-2024-caduceus-bi-directional-equivariant-long
domain: genomics
title: "Caduceus: Bi-Directional Equivariant Long-Range DNA Sequence Modeling"
authors: Yair Schiff; Chia-Hsiang Kao; Aaron Gokaslan; Tri Dao; Albert Gu; Volodymyr Kuleshov
year: 2024
doi: 10.48550/arXiv.2403.03234
category: genomic-foundation-models
pdf_path: /C:/Users/dlsrnsi/OneDrive/문서/New project/papers/schiff-2024-caduceus-bi-directional-equivariant-long.pdf
pdf_filename: schiff-2024-caduceus-bi-directional-equivariant-long.pdf
source_collection: web-open-access
status: draft
---

## One-line Summary

Caduceus is a long-range DNA foundation model based on Mamba that adds bidirectionality and reverse-complement equivariance for genomic sequence modeling.

## 1. Document Information

ICML 2024 paper introducing Caduceus and the MambaDNA block.

## 2. Key Contributions

- Introduces BiMamba for bidirectional sequence modeling.
- Introduces MambaDNA for reverse-complement equivariant DNA modeling.
- Builds Caduceus as a family of RC-equivariant bidirectional DNA language models.
- Shows strong results on long-range variant effect prediction.

## 3. Materials and Data

Pretraining uses the human reference genome with character/base-pair tokenization. Downstream evaluations include Genomics Benchmarks and long-range variant effect prediction tasks where regulatory sequence context can be far from the gene or variant.

## 4. Methodology and Architecture

### Inputs and Representations

Caduceus uses base-pair-level tokenization rather than k-mers. The model is designed around two DNA-specific properties: useful information can appear upstream and downstream, and either DNA strand can be sequenced as the reverse complement.

### Model / Algorithm / Workflow

The paper extends Mamba into BiMamba by processing both the original sequence and its reverse, then flipping and adding the reverse output. It then defines MambaDNA, which processes a sequence and its reverse complement with shared parameters to enforce RC equivariance.

### Training, Inference, or Search Procedure

Caduceus-PS uses RC-equivariant embeddings, MambaDNA blocks, and an RC-equivariant language-model head for masked language modeling. Caduceus-Ph uses BiMamba plus RC augmentation and post-hoc conjoining at inference.

### Baselines and Evaluation Protocol

Baselines include HyenaDNA, CNNs, and other attention or SSM-based DNA models. Variant effect prediction is a key task because the model's pretraining likelihood can reflect sequence conservation and mutational impact.

## 5. Key Results and Benchmarks

Caduceus outperforms similarly sized SSM-based models and, on long-range tasks, can outperform models up to 10x larger that lack bidirectionality or RC equivariance. The paper reports particular strength on long-range variant effect prediction for gene-expression effects.

## 6. Limitations and Future Work

Caduceus is sequence-based rather than genotype-matrix based. It does not explicitly model LD, haplotypes, GWAS summary statistics, or causal fine-mapping posterior probabilities.

## 7. Related Work

- [[genomics/genomic-foundation-models/nguyen-2023-hyenadna-long-range-genomic-sequence]] - Architecture connection: both use attention-free long-range sequence modeling; Caduceus adds bidirectionality and RC equivariance.
- [[genomics/fine-mapping/lee-2026-genomic-language-based-finemapping]] - Method contrast: Caduceus encodes DNA-specific strand/context priors; GLFM encodes LD-aware genotype context for fine-mapping.

## 8. Glossary

- RC equivariance: Model outputs transform consistently under reverse-complement transformation.
- Mamba: Selective state-space sequence model.
