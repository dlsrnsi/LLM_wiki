---
id: nguyen-2023-hyenadna-long-range-genomic-sequence
domain: genomics
title: "HyenaDNA: Long-Range Genomic Sequence Modeling at Single Nucleotide Resolution"
authors: Eric Nguyen; Michael Poli; Marjan Faizi; Armin W. Thomas; Callum Birch Sykes; Michael Wornow; Aman Patel; Clayton Rabideau; Stefano Massaroli; Yoshua Bengio; Stefano Ermon; Stephen A. Baccus; Christopher Ré
year: 2023
doi: 10.48550/arXiv.2306.15794
category: genomic-foundation-models
pdf_path: /C:/Users/dlsrnsi/OneDrive/문서/New project/papers/nguyen-2023-hyenadna-long-range-genomic-sequence.pdf
pdf_filename: nguyen-2023-hyenadna-long-range-genomic-sequence.pdf
source_collection: web-open-access
status: draft
---

## One-line Summary

HyenaDNA is an attention-free long-context genomic foundation model that processes DNA at single-nucleotide resolution with context lengths up to 1 million tokens.

## 1. Document Information

arXiv 2023 paper introducing HyenaDNA for long-range genomic sequence modeling.

## 2. Key Contributions

- Replaces quadratic self-attention with Hyena implicit long convolutions.
- Uses single-nucleotide tokens rather than k-mers or learned DNA words.
- Scales context length up to 1 million nucleotides.
- Introduces sequence-length warm-up for ultralong sequence training.
- Demonstrates soft prompting/in-context-style adaptation for genomic tasks.

## 3. Materials and Data

The model is pretrained on the human reference genome using next-nucleotide prediction. Downstream evaluation covers 29 genomic tasks, including Nucleotide Transformer benchmark tasks, GenomicBenchmarks tasks, long-range species classification, and chromatin profile prediction.

## 4. Methodology and Architecture

HyenaDNA is a decoder-only sequence model built from Hyena operators. A Hyena operator combines implicit long convolutions and data-controlled gating, evaluated in subquadratic time through FFT-style convolution.

Unlike many DNA language models, HyenaDNA tokenizes DNA at the single-nucleotide level using A, C, G, T, N and special tokens. This preserves SNP-level resolution while allowing long context.

Training uses next nucleotide prediction. For ultralong contexts, the paper introduces sequence length warm-up: training begins on shorter windows and gradually increases sequence length. Downstream adaptation includes full fine-tuning and soft prompt tuning, where learned prompt tokens are injected into the long context while the pretrained model is frozen.

## 5. Key Results and Benchmarks

HyenaDNA reports context lengths up to 1M nucleotides, up to 500x longer than dense-attention genomic FMs. At sequence length 1M, HyenaDNA is reported as 160x faster than a Transformer counterpart. On Nucleotide Transformer benchmark tasks, it reaches state-of-the-art on 12 of 18 datasets while using far fewer parameters and less pretraining data. On GenomicBenchmarks, it surpasses previous state-of-the-art on 7 of 8 datasets, with large gains on enhancer identification.

## 6. Limitations and Future Work

HyenaDNA is sequence-only and reference-genome based. It does not explicitly model LD, phased genotype tokens, or causal fine-mapping. Its long-context advantage is architectural, not a direct population-genetic LD prior.

## 7. Related Work

- [[genomics/genomic-foundation-models/dalla-torre-2025-nucleotide-transformer-building-and]] - Benchmark connection: HyenaDNA is evaluated against NT-style tasks.
- [[genomics/genomic-foundation-models/zhou-2024-dnabert-2-efficient-foundation-model]] - Method contrast: DNABERT-2 improves Transformer tokenization; HyenaDNA avoids attention and k-mer tokenization for long context.
- [[genomics/fine-mapping/lee-2026-genomic-language-based-finemapping]] - Method contrast: HyenaDNA addresses long-range sequence context; GLFM addresses LD-aware genotype-context fine-mapping.

## 8. Glossary

- Hyena operator: Long-convolution sequence operator with data-controlled gating.
- Single-nucleotide resolution: Modeling each nucleotide as a token.
