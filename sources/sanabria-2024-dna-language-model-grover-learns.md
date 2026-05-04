---
id: sanabria-2024-dna-language-model-grover-learns
domain: genomics
title: "DNA language model GROVER learns sequence context in the human genome"
authors: Melissa Sanabria; Jonas Hirsch; Pierre M. Joubert; Anna R. Poetsch
year: 2024
doi: 10.1038/s42256-024-00872-0
category: genomic-foundation-models
pdf_path: /C:/Users/dlsrnsi/OneDrive/문서/New project/papers/sanabria-2024-dna-language-model-grover-learns.pdf
pdf_filename: sanabria-2024-dna-language-model-grover-learns.pdf
source_collection: web-open-access
status: draft
---

## One-line Summary

GROVER trains a BERT-style DNA language model using a human-genome BPE vocabulary selected by next-k-mer prediction, then analyzes what the learned tokens encode.

## 1. Document Information

Nature Machine Intelligence 2024 article.

## 2. Key Contributions

- Builds a frequency-balanced BPE vocabulary on the human genome.
- Selects the vocabulary using next-k-mer prediction rather than a biology-specific task.
- Trains a BERT-style masked-token model named GROVER.
- Interprets token embeddings and genomic-region embeddings.
- Reports strong performance on genome element identification and protein-DNA binding tasks.

## 3. Materials and Data

The vocabulary and pretraining are based on the human genome. The paper compares GROVER against fixed k-mer models, Nucleotide Transformer, HyenaDNA, and DNABERT-2 on next-k-mer prediction and downstream genome biology tasks.

## 4. Methodology and Architecture

GROVER uses BPE to form variable-length DNA tokens. Multiple vocabularies from 100 to 5,000 BPE cycles are tested, and cycle 600 is selected. The model is a 12-layer BERT architecture trained with masked token prediction and cross-entropy loss.

The paper uses next-k-mer prediction as intrinsic validation to avoid choosing a vocabulary based on one downstream biological task. It also analyzes trained embeddings with PCA/UMAP and correlations with token frequency, GC content, AG content, token length, repeats, transcription, and replication timing.

## 5. Key Results and Benchmarks

GROVER's 600-cycle BPE vocabulary contains 601 tokens and a median token frequency around 400,000, with average token length about 4.07. GROVER reaches 21% masked-token top-1 accuracy and 75% top-60 accuracy. For next-6-mer prediction, GROVER reaches 2% accuracy, while DNABERT-2 is reported at 0.6% and fixed k-mer/NT-style models remain below 0.4% in the paper's comparison. GROVER also outperforms compared models on fine-tuning tasks for genome element identification and protein-DNA binding.

## 6. Limitations and Future Work

GROVER is human-reference sequence based and does not explicitly model genotype variation, LD, or fine-mapping. Its analysis shows that token frequency remains an important learned feature, so context learning must be interpreted with care.

## 7. Related Work

- [[genomics/genomic-foundation-models/zhou-2024-dnabert-2-efficient-foundation-model]] - Method connection: both use BPE, but GROVER focuses on human-genome vocabulary interpretability.
- [[genomics/fine-mapping/lee-2026-genomic-language-based-finemapping]] - Method contrast: GROVER studies DNA token grammar; GLFM studies genotype/LD context for causal SNP prioritization.

## 8. Glossary

- GROVER: Genome Rules Obtained Via Extracted Representations.
- Next-k-mer prediction: Intrinsic task for testing sequence-context learning independent of the original tokenizer.
