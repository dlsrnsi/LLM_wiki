---
id: ji-2021-dnabert-pre-trained-bidirectional-encoder
domain: genomics
title: "DNABERT, pre-trained Bidirectional Encoder Representations from Transformers model for DNA-language in genome"
authors:
  - Yanrong Ji
  - Zhihan Zhou
  - Han Liu
  - Ramana V. Davuluri
year: 2021
doi: 10.1093/bioinformatics/btab083
source: ji-2021-dnabert-pre-trained-bidirectional-encoder.md
category: genomic-foundation-models
pdf_path: /C:/Users/dlsrnsi/OneDrive/문서/New project/papers/ji-2021-dnabert-pre-trained-bidirectional-encoder.pdf
pdf_filename: ji-2021-dnabert-pre-trained-bidirectional-encoder.pdf
source_collection: user-provided
status: draft
tags: [genomics, dnabert, transformers, foundation-models]
---

## Summary

DNABERT adapts BERT-style transformer pretraining to genomic DNA. It tokenizes DNA into k-mers, pretrains on unlabeled human genome sequence with masked language modeling, and fine-tunes the pretrained model for regulatory sequence prediction tasks.

## Key Contributions

- Introduces a BERT-style pretrained model for DNA language.
- Uses k-mer tokenization to represent richer local nucleotide context than single-base tokens.
- Removes/changes parts of the original BERT pretraining setup to better fit DNA, including contiguous k-mer masking.
- Demonstrates fine-tuning on promoter, transcription factor binding site, and splice-site prediction.
- Uses attention patterns for interpretation of motifs and functional variant candidates.

## Materials and Data

- Pretraining corpus: unlabeled human genome sequences.
- Pretraining sequence lengths: sampled/truncated sequences up to BERT-style maximum length 512.
- Tokenization: k-mer vocabularies for k = 3, 4, 5, and 6 plus special tokens.
- Downstream tasks: promoter prediction, TFBS prediction, and splice-site prediction.
- Implementation: code and pretrained/fine-tuned models released on GitHub.

## Methods

DNABERT follows the pretraining/fine-tuning pattern from [[machine-learning/transformer-language-models/devlin-2018-bert-pre-training-of-deep]]. DNA sequences are represented as overlapping k-mer tokens. The model uses a BERT-base style transformer encoder with 12 transformer layers, 768 hidden units, and 12 attention heads.

During pretraining, contiguous spans of k-mers are masked so that the model cannot trivially recover a token from immediately overlapping neighbors. The model learns contextual DNA representations from the human genome. During fine-tuning, the pretrained encoder is adapted to task-specific labeled datasets for sequence-level or token-level prediction.

## Results

The paper reports that a single pretrained DNABERT model can be fine-tuned across multiple regulatory genomics tasks and can outperform or match task-specific methods. It emphasizes performance in data-scarce settings, where pretraining provides a useful inductive bias.

DNABERT also provides interpretability through attention visualization. Attention can highlight known binding sites, conserved motifs, and potentially functional variants in input DNA sequences.

## Limitations

DNABERT is a DNA sequence representation model, not a causal fine-mapping method. It does not explicitly include linkage disequilibrium, genotype dosage, phenotype prediction, or SNP-level causal ablation. Attention-based interpretation is useful but is not equivalent to causal evidence.

## Related Papers

- [[machine-learning/transformer-language-models/devlin-2018-bert-pre-training-of-deep]] - Method connection: DNABERT directly adapts BERT's masked pretraining and fine-tuning framework to DNA.
- [[machine-learning/transformer-language-models/vaswani-2017-attention-is-all-you-need]] - Method connection: DNABERT uses transformer self-attention to capture global sequence context.
- [[dalla-torre-2025-nucleotide-transformer-building-and]] - Method connection: both are DNA/genome transformer foundation models; Nucleotide Transformer is a later larger-scale foundation model family.
- [[genomics/fine-mapping/lee-2026-genomic-language-based-finemapping]] - Method connection: GLFM cites DNABERT as genomic language-model motivation but changes the task to LD-aware causal SNP fine-mapping.
