---
id: chen-2025-bmfm-dna-a-snp-aware
domain: genomics
title: "BMFM-DNA: A SNP-aware DNA foundation model to capture variant effects"
authors: Hongyang Li; Sanjoy Dey; Bum Chul Kwon; Michael Danziger; Michal Rosen-Tzvi; Jianying Hu; James Kozloski; Ching-Huei Tsou; Bharath Dandala; Pablo Meyer
year: 2025
doi: 10.48550/arXiv.2507.05265
category: genomic-foundation-models
pdf_path: /C:/Users/dlsrnsi/OneDrive/문서/New project/papers/chen-2025-bmfm-dna-a-snp-aware.pdf
pdf_filename: chen-2025-bmfm-dna-a-snp-aware.pdf
source_collection: web-open-access
status: draft
---

## One-line Summary

BMFM-DNA compares reference-only and SNP-aware DNA foundation models, arguing that encoding sequence variation during pretraining improves downstream genomic prediction.

## 1. Document Information

arXiv 2025 paper from IBM Research.

## 2. Key Contributions

- Introduces BMFM-DNA-REF and BMFM-DNA-SNP.
- Encodes variants from dbSNP into pretraining sequences.
- Uses ModernBERT for masked language modeling on DNA.
- Evaluates promoter, splice, TFBS, MPRA, and SNP-disease association tasks.

## 3. Materials and Data

Pretraining uses GRCh38 and dbSNP. BMFM-DNA-REF samples 1-10 kb sequences from the reference genome and reverse complements them, producing 9,982,678 samples and roughly 60 billion nucleotides. BMFM-DNA-SNP samples variant-encoded sequences using a dbSNP-derived genome-wide variation frequency matrix.

Fine-tuning datasets include promoter detection, core promoter detection, TF binding site prediction, splice site prediction, lenti-MPRA promoter activity prediction, and SNP-disease association prediction using GWAS Catalog and ClinVar.

## 4. Methodology and Architecture

BMFM-DNA uses ModernBERT and masked language modeling. BMFM-DNA-SNP maps variant possibilities at a genomic position into special characters, enabling one token position to represent biallelic variation rather than only reference sequence.

The paper trains BPE tokenizers with 4,096 tokens and compares reference-only versus SNP-aware pretraining. It also explores SNP imputation strategies for promoter detection.

## 5. Key Results and Benchmarks

The paper reports that incorporating SNP variation improves all fine-tuning tasks relative to reference-only DNA language modeling. It frames variant-aware pretraining as necessary because many disease-associated variants lie in non-coding regions and are ignored by reference-only language models.

## 6. Limitations and Future Work

The authors state that current benchmarks are limited for fully evaluating SNP-aware foundation models. BMFM-DNA is variant-aware but not explicitly LD-aware: it encodes sequence variation but does not directly model phased genotype correlations or fine-mapping posterior structure.

## 7. Related Work

- [[genomics/genomic-foundation-models/zhou-2024-dnabert-2-efficient-foundation-model]] - Benchmark/method connection: BMFM-DNA uses DNABERT-2/GUE-style tasks and BPE tokenization ideas.
- [[genomics/genotype-language-models/huang-2026-genobert-a-language-model-for]] - Variant/genotype connection: BMFM-DNA encodes variant possibilities in DNA sequences; GenoBERT tokenizes phased genotypes for imputation.
- [[genomics/fine-mapping/lee-2026-genomic-language-based-finemapping]] - Method connection: both move beyond reference-only DNA sequence by modeling variant/genotype context.

## 8. Glossary

- SNP-aware pretraining: Pretraining that includes sequence variation rather than only reference bases.
- dbSNP: Database of nucleotide variants.
