# Fine Mapping

- [[lee-2026-genomic-language-based-finemapping]] - GLFM draft; LD-aware genomic language model for causal SNP fine-mapping.
- [[benner-2016-finemap-efficient-variable-selection]] - FINEMAP; Bayesian variable selection from GWAS summary statistics.
- [[wang-2020-simple-new-approach-to-variable]] - SuSiE; sum-of-single-effects regression for credible sets.

## Comparative Summary

This sub-domain now contains one model-development draft and two statistical fine-mapping baselines. [[lee-2026-genomic-language-based-finemapping]] differs from [[benner-2016-finemap-efficient-variable-selection]] and [[wang-2020-simple-new-approach-to-variable]] because it models a genotype locus as a sequence and learns contextual representations, whereas FINEMAP and SuSiE operate as statistical variable-selection methods driven by association statistics and LD.

FINEMAP searches high-posterior causal configurations. SuSiE decomposes sparse effects into a sum of single-effect components and returns credible sets. GLFM instead uses LD-aware transformer pretraining, LoRA phenotype fine-tuning, and leave-one-SNP-out representation trajectory ablation, then redistributes inflated proxy scores using DTW and curvature-divergence couplings.

## Comparison Table

| Paper | Main input | Core method | Output | Role for GLFM |
|---|---|---|---|---|
| [[benner-2016-finemap-efficient-variable-selection]] | GWAS summary statistics + LD | Bayesian configuration search | Posterior causal configurations and PIPs | Statistical baseline |
| [[wang-2020-simple-new-approach-to-variable]] | Regression data or summary fine-mapping setup | Sum of single effects | PIPs and credible sets | Statistical baseline |
| [[lee-2026-genomic-language-based-finemapping]] | Genotype sequence + LD + phenotype | LD-aware BERT, LoRA, trajectory ablation, redistribution | Causal SNP ranking | New representation-based method |

## Main Takeaway

GLFM's main hypothesis is that LD is not only a confounder to correct statistically, but also a structural signal that can guide representation learning. This makes it methodologically connected to transformer and BERT papers, but its evaluation target remains fine-mapping AUPR against causal SNP labels.

