---
id: brixi-2026-genome-modelling-and-design-across
domain: genomics
title: "Genome modelling and design across all domains of life with Evo 2"
authors:
  - Garyk Brixi
  - Matthew G. Durrant
  - Jerome Ku
  - Mohsen Naghipourfar
  - Michael Poli
  - Gwanggyu Sun
  - Evo 2 Core Team
year: 2026
doi: 10.1038/s41586-026-10176-5
source: brixi-2026-genome-modelling-and-design-across.md
category: genomic-foundation-models
pdf_path: /C:/Users/dlsrnsi/OneDrive/문서/New project/papers/brixi-2026-genome-modelling-and-design-across.pdf
pdf_filename: brixi-2026-genome-modelling-and-design-across.pdf
source_collection: web-open-access
status: draft
tags: [genomics, foundation-models, evo2, long-context]
---

## Summary

Evo 2 is a large generalist biological foundation model trained on genome sequences across all domains of life, with single-nucleotide resolution and a 1M-token context window.

## Key Contributions

- Scales genomic sequence modeling to trillions of tokens and 1M-token context.
- Trains on OpenGenome2, spanning bacteria, archaea, eukarya, and phage.
- Supports zero-shot variant-effect prediction and genome-scale generation.
- Provides an open model/data/code release.

## Materials and Data

The paper uses OpenGenome2, containing more than 8.8 trillion nucleotides. Evo 2 7B is trained on 2.4 trillion tokens, while Evo 2 40B is trained on 9.3 trillion tokens.

## Methods

### Inputs and Representations

Evo 2 models DNA at single-nucleotide resolution. It emphasizes long genomic context rather than k-mer or BPE sequence compression.

### Model / Algorithm / Workflow

The paper uses a large biological sequence model with a two-phase training strategy that expands context length up to 1M base pairs. Training and midtraining include data curation and weighting strategies for functional genomic elements and long-sequence composition.

### Training, Inference, or Search Procedure

The model is used for zero-shot prediction, interpretability analysis, and genome-scale generation. It is not tuned as a fine-mapping model.

### Baselines and Evaluation Protocol

Evaluation includes variant-effect prediction, mechanistic interpretability of learned biological features, and generated-sequence naturalness/coherence.

## Results

Evo 2 predicts functional impacts of genetic variation, including noncoding pathogenic mutations and BRCA1 variants, without task-specific fine-tuning. It learns representations associated with exon-intron boundaries, transcription factor binding sites, protein structural elements, and prophage regions. It can generate mitochondrial, prokaryotic, and eukaryotic sequences with improved naturalness and coherence.

## Limitations

Evo 2 is not LD-aware or genotype-aware in the GLFM sense. It is valuable as current genomic foundation model context, but it does not directly solve GWAS fine-mapping or genotype-imputation tasks.

## Related Papers

- [[nguyen-2023-hyenadna-long-range-genomic-sequence]] - Method/scale connection: both emphasize long-context single-nucleotide genome modeling.
- [[genomics/fine-mapping/lee-2026-genomic-language-based-finemapping]] - Method contrast: Evo 2 is a generalist genome model; GLFM is a locus-level genotype/LD model for fine-mapping.
