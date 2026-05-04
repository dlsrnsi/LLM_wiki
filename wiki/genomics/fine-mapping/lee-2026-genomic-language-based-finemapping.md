---
id: lee-2026-genomic-language-based-finemapping
domain: genomics
title: "Genomic Language-based Finemapping Approach (GLFM)"
authors:
  - Ingoo Lee
  - Trey Ideker
year: 2026
doi: unpublished
source: lee-2026-genomic-language-based-finemapping.md
category: fine-mapping
pdf_path: /C:/Users/dlsrnsi/OneDrive/문서/New project/papers/lee-2026-genomic-language-based-finemapping.pdf
pdf_filename: lee-2026-genomic-language-based-finemapping.pdf
source_collection: google-drive
status: draft
tags: [genomics, fine-mapping, genomic-language-models, linkage-disequilibrium]
---

## Summary

GLFM is a draft method for causal SNP fine-mapping. It treats a genomic locus as a genotype-token sequence and uses a BERT-style encoder whose attention is biased by local LD structure. After phenotype fine-tuning, GLFM estimates causal SNP evidence by leave-one-SNP-out ablation over both output prediction and layerwise representation trajectories.

## Key Contributions

- Adds an LD-derived learned log-prior directly into transformer self-attention.
- Uses masked language modeling for genotype-sequence pretraining.
- Uses LoRA to fine-tune the pretrained encoder for continuous phenotype prediction.
- Scores SNPs by combining phenotype sensitivity and [CLS] representation-trajectory divergence.
- Redistributes evidence from proxy SNPs using DTW trajectory similarity and compensation curvature-divergence.

## Materials and Data

- Source document: Google Drive draft `GLFM`.
- Evaluation setting: simulated loci across heritability, sample size, and LD regimes.
- Simulation grid: h2 in {0.01, 0.05, 0.10, 0.20, 0.30}, N in {100, 1,000, 10,000, 100,000}, r2 in {0.2, 0.4, 0.6, 0.8}, with three replicates per condition.
- Baselines: [[benner-2016-finemap-efficient-variable-selection]] and [[wang-2020-simple-new-approach-to-variable]].

## Methods

Each SNP is encoded as dosage information over homozygous reference, heterozygous, and homozygous alternate genotype states. A BERT-style transformer processes the locus sequence. GLFM injects an LD log-prior into self-attention, with learnable amplitude/selectivity parameters and a root-mean-r2 gate so weak or uninformative LD does not dominate attention.

Training happens in three stages. First, the encoder is pretrained with masked language modeling and a depth-smoothness regularizer on LD-prior parameters. Second, LoRA adapts the model to continuous phenotype prediction from the [CLS] representation while most encoder weights remain frozen. Third, SNP-level causal evidence is computed by masking each SNP and measuring the product of phenotype sensitivity and layerwise [CLS] trajectory divergence.

The post-hoc redistribution step targets high-LD proxy compensation. It transfers evidence using two pairwise couplings: dynamic time warping similarity between SNP representation trajectories, and curvature-divergence changes induced by ablating one SNP and observing another SNP's trajectory.

## Results

Across 240 simulation runs, the draft reports that the full GLFM + DTW + CV pipeline achieved mean AUPR 0.492, compared with 0.407 for SuSiE and 0.408 for FINEMAP. Internal ablations show a stepwise gain: ablation-only GLFM reached 0.445, +DTW reached 0.469, and +DTW+CV reached 0.492.

The reported advantage increases with LD strength. Relative to SuSiE, the mean AUPR advantage grows from 0.018 at r2 = 0.2 to 0.143 at r2 = 0.8. Relative to FINEMAP, it grows from 0.011 to 0.151. The draft reports the largest single-condition gain at h2 = 0.01, N = 1,000, r2 = 0.6, where AUPR increased from 0.122 for ablation-only to 0.264 for the full model.

## Limitations

The manuscript is still incomplete: the abstract is unwritten and several figure/title notes are provisional. Evaluation is simulation-based, so real GWAS locus validation is still needed. The score redistribution and hyperparameter selection procedure needs careful clarification for deployment without causal labels.

## Related Papers

- [[benner-2016-finemap-efficient-variable-selection]] - Method/result connection: FINEMAP is one of GLFM's statistical fine-mapping baselines.
- [[wang-2020-simple-new-approach-to-variable]] - Method/result connection: SuSiE is the second statistical baseline and provides the credible-set/PIP contrast to GLFM's representation trajectory scoring.
- [[machine-learning/transformer-language-models/vaswani-2017-attention-is-all-you-need]] - Method connection: GLFM uses transformer self-attention as its sequence-modeling backbone.
- [[machine-learning/transformer-language-models/devlin-2018-bert-pre-training-of-deep]] - Method connection: GLFM follows the BERT-style masked pretraining and fine-tuning pattern.
- [[genomics/genomic-foundation-models/dalla-torre-2025-nucleotide-transformer-building-and]] - Method connection: both use transformer-style genomic sequence representation learning, but GLFM adds LD-aware attention and causal SNP ablation.
- [[genomics/genotype-language-models/huang-2026-genobert-a-language-model-for]] - Strong method connection: both use BERT-style genotype representations and LD context; GenoBERT optimizes masked genotype imputation, while GLFM uses the encoder for phenotype fine-tuning and causal SNP scoring.
- [[genomics/genomic-foundation-models/zhou-2024-dnabert-2-efficient-foundation-model]] - Method contrast: DNABERT-2 improves sequence-tokenized DNA language modeling; GLFM shifts the language object from DNA sequence to genotype/LD locus sequence.
- [[genomics/genomic-foundation-models/chen-2025-bmfm-dna-a-snp-aware]] - Method connection: both move beyond reference-only sequence modeling by incorporating genetic variation.
