---
id: sanabria-2024-dna-language-model-grover-learns
domain: genomics
title: "DNA language model GROVER learns sequence context in the human genome"
authors:
  - Melissa Sanabria
  - Jonas Hirsch
  - Pierre M. Joubert
  - Anna R. Poetsch
year: 2024
doi: 10.1038/s42256-024-00872-0
source: sanabria-2024-dna-language-model-grover-learns.md
category: genomic-foundation-models
pdf_path: /C:/Users/dlsrnsi/OneDrive/문서/New project/papers/sanabria-2024-dna-language-model-grover-learns.pdf
pdf_filename: sanabria-2024-dna-language-model-grover-learns.pdf
source_collection: web-open-access
status: draft
tags: [genomics, foundation-models, grover, tokenization]
---

## Summary

GROVER is a BERT-style DNA language model built around a human-genome BPE vocabulary selected for sequence-context learning and interpretability.

## Key Contributions

- Uses BPE to create a frequency-balanced human-genome vocabulary.
- Selects the 600-cycle BPE vocabulary using next-k-mer prediction.
- Analyzes what learned token embeddings encode.
- Shows that human-genome token embeddings relate to sequence content, frequency, length, repeats, and functional annotations.

## Materials and Data

GROVER is trained on the human genome. It is compared against fixed k-mer BERT models, Nucleotide Transformer, HyenaDNA, and DNABERT-2. Downstream evaluation includes genome element identification and protein-DNA binding tasks.

## Methods

### Inputs and Representations

DNA is tokenized with BPE. The selected 600-cycle vocabulary has 601 tokens, mostly variable-length k-mer-like tokens with a median frequency around 400,000 and average token length about 4.07.

### Model / Algorithm / Workflow

The model uses 12 BERT-style Transformer blocks and masked-token prediction. The paper uses next-k-mer prediction to choose a vocabulary without optimizing for one downstream biology task.

### Training, Inference, or Search Procedure

GROVER is trained with cross-entropy loss to predict masked tokens. Token and region embeddings are then analyzed to infer what the model learned.

### Baselines and Evaluation Protocol

Baselines include fixed k-mer BERT models, Nucleotide Transformer, HyenaDNA, and DNABERT-2.

## Results

GROVER reaches 21% masked-token top-1 accuracy and 75% top-60 accuracy. In next-6-mer prediction, GROVER reaches 2% accuracy, compared with 0.6% for DNABERT-2 and below 0.4% for fixed k-mer/NT-style models in the reported comparison. Embedding analyses show strong relationships with token frequency, GC content, AG content, token length, repeats, transcription, and replication timing.

## Limitations

GROVER is not genotype-aware or LD-aware. It is useful for understanding sequence grammar and tokenization, but it does not address phased genotype representation, LD dependency learning, or fine-mapping.

## Related Papers

- [[zhou-2024-dnabert-2-efficient-foundation-model]] - Method connection: both use BPE tokenization, but GROVER emphasizes human-genome vocabulary interpretability.
- [[genomics/fine-mapping/lee-2026-genomic-language-based-finemapping]] - Method contrast: GROVER is a DNA grammar model; GLFM is a genotype/LD representation model for fine-mapping.
