---
id: lee-2026-genomic-language-based-finemapping
domain: genomics
title: "Genomic Language-based Finemapping Approach (GLFM)"
authors: Ingoo Lee; Trey Ideker
year: 2026
doi: unpublished
category: fine-mapping
pdf_path: /C:/Users/dlsrnsi/OneDrive/문서/New project/papers/lee-2026-genomic-language-based-finemapping.pdf
pdf_filename: lee-2026-genomic-language-based-finemapping.pdf
source_collection: google-drive
status: draft
---

## One-line Summary

GLFM is a draft genomic language model for causal SNP fine-mapping that combines LD-aware BERT-style pretraining, phenotype fine-tuning with LoRA, trajectory ablation, and post-hoc score redistribution.

## Document Information

- Source: Google Drive document `GLFM`.
- Draft status: abstract still says "To be written"; title and correspondence footnotes are marked as provisional.
- Main cited baselines: FINEMAP and SuSiE.

## Key Contributions

- Injects a learned LD-derived log-prior into transformer self-attention.
- Fine-tunes the pretrained encoder for continuous phenotype prediction.
- Scores candidate causal SNPs by both phenotype-output sensitivity and layerwise representation-trajectory perturbation.
- Redistributes scores from LD proxies back toward plausible causal SNPs using DTW trajectory similarity and compensation curvature-divergence.

## Methodology and Architecture

GLFM represents each SNP as dosage tokens and processes a locus with a BERT-style transformer. LD structure is encoded as a learned log-prior bias in self-attention, with a locus-level root-mean-r2 gate to suppress uninformative uniform LD priors.

Training has three stages: masked language model pretraining with LD-aware attention, phenotype prediction fine-tuning with LoRA while most encoder weights remain frozen, and post-hoc causal SNP scoring by leave-one-SNP-out ablation.

## Key Results and Benchmarks

The draft reports 240 simulation runs across heritability, sample-size, and LD grids. The full GLFM + DTW + CV pipeline reports mean AUPR 0.492, compared with 0.407 for SuSiE and 0.408 for FINEMAP. Ablation-only GLFM reports mean AUPR 0.445, +DTW reports 0.469, and +DTW+CV reports 0.492.

The largest gains are described in high-LD regimes. The draft also notes an exception: at extremely weak signal with large sample size and lower LD, association-based methods can outperform GLFM.

## Limitations and Future Work

- Draft manuscript; abstract and some figure notes are incomplete.
- Evaluation is simulation-based.
- The self-supervised language-model framing needs validation on real GWAS/fine-mapping loci.
- Post-hoc redistribution uses simulation labels during grid search as written, so deployment-time calibration needs clarification.

## Related Work

- FINEMAP: Bayesian variable selection baseline.
- SuSiE: sum-of-single-effects fine-mapping baseline.
- Transformer/BERT: architecture and pretraining foundation.
- Nucleotide Transformer/DNABERT: genomic language model context.
