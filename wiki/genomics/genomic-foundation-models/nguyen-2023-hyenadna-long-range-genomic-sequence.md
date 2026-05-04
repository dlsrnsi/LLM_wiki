---
id: nguyen-2023-hyenadna-long-range-genomic-sequence
domain: genomics
title: "HyenaDNA: Long-Range Genomic Sequence Modeling at Single Nucleotide Resolution"
authors:
  - Eric Nguyen
  - Michael Poli
  - Marjan Faizi
  - Armin W. Thomas
  - Callum Birch Sykes
  - Michael Wornow
  - Aman Patel
  - Clayton Rabideau
  - Stefano Massaroli
  - Yoshua Bengio
  - Stefano Ermon
  - Stephen A. Baccus
  - Christopher Ré
year: 2023
doi: 10.48550/arXiv.2306.15794
source: nguyen-2023-hyenadna-long-range-genomic-sequence.md
category: genomic-foundation-models
pdf_path: /C:/Users/dlsrnsi/OneDrive/문서/New project/papers/nguyen-2023-hyenadna-long-range-genomic-sequence.pdf
pdf_filename: nguyen-2023-hyenadna-long-range-genomic-sequence.pdf
source_collection: web-open-access
status: draft
tags: [genomics, foundation-models, long-context, hyena]
---

## Summary

HyenaDNA is a long-context genomic foundation model that replaces attention with Hyena implicit convolutions, enabling single-nucleotide modeling up to million-token contexts.

## Key Contributions

- Processes DNA at single-nucleotide resolution instead of k-mer aggregation.
- Extends context length up to 1M nucleotides.
- Uses a Hyena operator with subquadratic scaling rather than self-attention.
- Introduces sequence-length warm-up and soft prompting for genomic adaptation.

## Materials and Data

HyenaDNA is pretrained on the human reference genome with next-nucleotide prediction. It is evaluated on 29 downstream genomics tasks, including Nucleotide Transformer tasks, GenomicBenchmarks, species classification, chromatin profile prediction, and embedding analyses.

## Methods

### Inputs and Representations

Input tokens are individual nucleotides: A, C, G, T, N, plus special tokens. This preserves the resolution needed for SNPs and mutations.

### Model / Algorithm / Workflow

The architecture is decoder-only and stacks Hyena operators. Each Hyena operator combines long convolutions and element-wise gates. The convolution filters are parameterized implicitly and can be evaluated efficiently, reducing the long-context cost relative to dense attention.

### Training, Inference, or Search Procedure

Pretraining uses next-nucleotide prediction. Sequence length warm-up gradually increases context length during training, improving stability and speed for ultralong sequences. For downstream adaptation, the paper explores full fine-tuning and soft prompt tuning.

### Baselines and Evaluation Protocol

Baselines include Transformer-style genomic foundation models and prior task-specific models on standard genomic benchmarks.

## Results

HyenaDNA reports up to 1M-token context, up to 500x longer than previous dense-attention genomic FMs. It is reported as up to 160x faster than a Transformer at 1M sequence length. On NT benchmark tasks, it reaches state-of-the-art on 12 of 18 datasets; on GenomicBenchmarks, it surpasses previous state-of-the-art on 7 of 8 datasets.

## Limitations

HyenaDNA is not LD-aware in the fine-mapping sense. It learns sequence context from the reference genome and does not directly model phased genotype matrices, association statistics, or causal SNP probability.

## Related Papers

- [[dalla-torre-2025-nucleotide-transformer-building-and]] - Benchmark connection: HyenaDNA is compared on NT-style genomics tasks.
- [[zhou-2024-dnabert-2-efficient-foundation-model]] - Method contrast: both address scalability, but DNABERT-2 improves Transformer tokenization while HyenaDNA replaces attention.
- [[genomics/fine-mapping/lee-2026-genomic-language-based-finemapping]] - Method contrast: HyenaDNA models long sequence context; GLFM models genotype/LD context for causal prioritization.
