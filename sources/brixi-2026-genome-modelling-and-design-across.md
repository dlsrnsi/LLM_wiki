---
id: brixi-2026-genome-modelling-and-design-across
domain: genomics
title: "Genome modelling and design across all domains of life with Evo 2"
authors: Garyk Brixi; Matthew G. Durrant; Jerome Ku; Mohsen Naghipourfar; Michael Poli; Gwanggyu Sun; Evo 2 Core Team
year: 2026
doi: 10.1038/s41586-026-10176-5
category: genomic-foundation-models
pdf_path: /C:/Users/dlsrnsi/OneDrive/문서/New project/papers/brixi-2026-genome-modelling-and-design-across.pdf
pdf_filename: brixi-2026-genome-modelling-and-design-across.pdf
source_collection: web-open-access
status: draft
---

## One-line Summary

Evo 2 is a large biological foundation model trained across all domains of life with single-nucleotide resolution and a 1M-token context window.

## 1. Document Information

Nature 2026 article introducing Evo 2.

## 2. Key Contributions

- Trains biological foundation models on trillions of DNA tokens across bacteria, archaea, eukarya, and phage.
- Extends genomic sequence modeling to 1M-token context at single-nucleotide resolution.
- Evaluates zero-shot variant-effect prediction, mechanistic interpretability, and genome-scale generation.
- Releases model parameters, training code, inference code, and OpenGenome2.

## 3. Materials and Data

Evo 2 uses OpenGenome2, a curated, non-redundant genomic atlas with more than 8.8 trillion nucleotides across all domains of life. The paper trains Evo 2 7B on 2.4 trillion tokens and Evo 2 40B on 9.3 trillion tokens.

## 4. Methodology and Architecture

Evo 2 is a large single-nucleotide-resolution biological sequence model. The paper emphasizes a two-phase training strategy that expands context up to 1M base pairs and data weighting/augmentation that prioritizes functional genetic elements and long-sequence composition.

The model is evaluated as a generalist predictive and generative model rather than a task-specific classifier. It is used for zero-shot variant-effect prediction, interpretability analyses of learned biological features, and generation of mitochondrial, prokaryotic, and eukaryotic-scale sequences.

## 5. Key Results and Benchmarks

Evo 2 predicts functional impacts of genetic variation, including noncoding pathogenic mutations and clinically significant BRCA1 variants, without task-specific fine-tuning. Interpretability analyses identify representations associated with exon-intron boundaries, transcription factor binding sites, protein structural elements, and prophage regions. The generative model produces genome-scale sequences with greater naturalness and coherence than earlier approaches.

## 6. Limitations and Future Work

Evo 2 is a broad biological foundation model, not a genotype/LD model or fine-mapping method. It does not directly model phased genotypes, LD matrices, GWAS summary statistics, or causal SNP posterior probabilities.

## 7. Related Work

- [[genomics/genomic-foundation-models/nguyen-2023-hyenadna-long-range-genomic-sequence]] - Architecture/scale connection: both emphasize long-context single-nucleotide modeling.
- [[genomics/fine-mapping/lee-2026-genomic-language-based-finemapping]] - Method contrast: Evo 2 is a generalist sequence model; GLFM is a genotype/LD fine-mapping model.

## 8. Glossary

- OpenGenome2: Evo 2 training dataset spanning all domains of life.
- Zero-shot variant-effect prediction: Predicting variant impact without task-specific fine-tuning.
