---
id: visscher-2017-10-years-of-gwas-discovery
domain: genomics
title: "10 Years of GWAS Discovery, Biology, Function, and Translation"
authors:
  - Peter M. Visscher
  - Naomi R. Wray
  - Qian Zhang
  - Pamela Sklar
  - Mark I. McCarthy
  - Matthew A. Brown
  - Jian Yang
year: 2017
doi: 10.1016/j.ajhg.2017.06.005
source: visscher-2017-10-years-of-gwas-discovery.md
category: gwas-reviews
pdf_path: /C:/Users/dlsrnsi/OneDrive/문서/New project/papers/visscher-2017-10-years-of-gwas-discovery.pdf
pdf_filename: visscher-2017-10-years-of-gwas-discovery.pdf
source_collection: web-open-access
status: draft
tags: [genomics, gwas, review]
---

## Summary

This review describes the first decade of GWAS discoveries and the biological, functional, and translational questions that follow from association mapping.

## Key Contributions

- Summarizes how GWAS produced many robust trait-associated loci.
- Frames the transition from association discovery to biological mechanism.
- Provides background for why statistical and representation-based fine-mapping are needed.

## Materials and Data

This is a review rather than a new dataset paper. Its evidence base is the first decade of human GWAS results across common diseases, quantitative traits, genomic traits, and downstream statistical analyses.

The paper treats SNP-array GWAS as a broad experimental design, not only as a catalog of significant SNPs. The reviewed evidence includes:

- genome-wide SNP-trait association studies using common SNP arrays;
- imputed association studies using reference haplotype panels;
- copy-number variant association studies;
- genome-wide LD analyses;
- SNP heritability estimation from unrelated individuals;
- genetic correlation and pleiotropy analyses;
- polygenic risk score studies;
- Mendelian randomization analyses;
- GWAS integrated with expression, methylation, and other molecular trait data.

For this wiki, the most important material is the GWAS-to-causal-interpretation gap. GWAS identifies trait-associated loci through LD-tagged variants, but the associated variant is often not itself the causal molecular perturbation. This makes fine-mapping, functional annotation, molecular QTL integration, and sequence/context modeling necessary follow-up layers.

## Methods

The paper explains GWAS as an association design that depends on the relationship between observed genotyped variants and unobserved causal variants. Statistical power depends on:

- cohort sample size;
- causal effect-size distribution;
- causal allele frequency;
- LD between measured markers and causal variants;
- genotyping or sequencing coverage;
- phenotype heterogeneity and measurement precision.

LD is central because common SNP arrays do not directly measure every causal variant. The paper emphasizes LD measured by squared correlation \(r^2\), because the sample size required to detect association scales with imperfect tagging. If a typed SNP only weakly tags a causal variant, more samples are required. Imputation can recover information by predicting untyped variants from haplotypes in sequenced reference panels, but it is still constrained by allele frequency, LD, and reference-panel quality.

The review also distinguishes array GWAS, imputed GWAS, exome sequencing, and whole-genome sequencing. SNP arrays are efficient for common variation; WGS can directly observe rare variants but still needs very large sample sizes unless effect sizes are large. For very rare variants, burden tests over genes or functional units may be more powerful than single-variant tests.

The paper is not an algorithm paper, but it organizes the post-GWAS analysis toolbox into several methodological families:

- controlling population structure and relatedness in association testing;
- detecting additional loci from GWAS summary statistics;
- estimating and partitioning SNP heritability;
- estimating genetic correlations and pleiotropy;
- using Mendelian randomization to test causal relationships;
- integrating molecular traits to move from locus association to target gene and function.

## Results

The review's major conclusion is that GWAS produced robust, replicable discoveries at large scale, but also revealed that most complex traits are highly polygenic.

Key results and claims relevant to this wiki:

- By the first decade of GWAS, roughly 10,000 strong SNP-trait associations had been reported across complex traits, diseases, and genomic traits.
- Larger sample sizes repeatedly converted weak polygenic signal into genome-wide-significant locus discovery. The paper gives schizophrenia and height as examples where increasing cohorts produced many more loci.
- Most complex traits appear to involve many loci of small effect, so individual associated SNPs usually explain only a small fraction of phenotypic variance.
- Pleiotropy is pervasive: the same variants or loci can affect multiple traits, so "one gene, one function, one trait" is usually the wrong mental model for complex-trait genetics.
- Common genotyped and imputed SNPs tag a substantial fraction of additive genetic variance, often estimated around one-third to two-thirds depending on trait and design.
- GWAS is powerful for locus discovery, but target-gene identification and causal mechanism require downstream interpretation because associated loci often implicate genes that are not simply the nearest gene.

For GLFM and the fine-mapping pages, the important takeaway is that GWAS creates a locus-level discovery problem. Fine-mapping methods such as [[genomics/fine-mapping/benner-2016-finemap-efficient-variable-selection]] and [[genomics/fine-mapping/wang-2020-simple-new-approach-to-variable]] address the next step: distributing causal probability among correlated candidate variants.

## Limitations

The paper is a broad review, so it does not provide a new causal fine-mapping algorithm, benchmark, or representation-learning model. It also predates later large-scale genomic foundation models. Its role in this wiki is to document why the downstream causal-variant prioritization problem exists after association discovery.

The review also makes clear that GWAS interpretation is limited by LD, sample size, phenotype definition, ancestry composition, imputation accuracy, and the difficulty of moving from statistical association to molecular mechanism.

## Related Papers

- [[genomics/fine-mapping/lee-2026-genomic-language-based-finemapping]] - Problem connection: GLFM targets the causal variant interpretation problem that remains after GWAS locus discovery.
