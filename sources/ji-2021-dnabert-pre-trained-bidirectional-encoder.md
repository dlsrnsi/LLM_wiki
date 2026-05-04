---
id: ji-2021-dnabert-pre-trained-bidirectional-encoder
domain: genomics
title: "DNABERT, pre-trained Bidirectional Encoder Representations from Transformers model for DNA-language in genome"
authors: Yanrong Ji; Zhihan Zhou; Han Liu; Ramana V. Davuluri
year: 2021
doi: 10.1093/bioinformatics/btab083
category: genomic-foundation-models
pdf_path: /C:/Users/dlsrnsi/OneDrive/문서/New project/papers/ji-2021-dnabert-pre-trained-bidirectional-encoder.pdf
pdf_filename: ji-2021-dnabert-pre-trained-bidirectional-encoder.pdf
source_collection: user-provided
status: draft
---

## One-line Summary

DNABERT adapts BERT pretraining to DNA sequences using k-mer tokenization, masked language modeling, and fine-tuning for regulatory sequence prediction tasks.

## Document Information

- Journal: Bioinformatics
- DOI: 10.1093/bioinformatics/btab083
- Raw import: `papers/btab083.pdf`

## Key Contributions

- Treats DNA as a language-like sequence with k-mer tokens.
- Uses transformer self-attention to capture global sequence context.
- Pretrains on unlabeled human genome sequence and fine-tunes on specific regulatory prediction tasks.
- Provides attention-based interpretation for nucleotide-level importance and semantic relationships.

## Methodology and Architecture

DNABERT follows BERT's pretrain-and-fine-tune pattern but modifies it for DNA. Sequences are tokenized into k-mers, with k = 3, 4, 5, or 6, plus special tokens such as CLS, SEP, MASK, PAD, and UNK. The model uses a BERT-base style transformer encoder with 12 layers, 768 hidden units, and 12 attention heads.

Pretraining uses self-supervised masked language modeling on human genome sequences. Instead of masking independent tokens, DNABERT masks contiguous k-length spans to avoid trivial inference from overlapping k-mers. The model is then fine-tuned for promoter prediction, transcription factor binding site prediction, and splice site prediction.

## Key Results and Benchmarks

The paper reports that one pretrained transformer can be fine-tuned for multiple regulatory element tasks, including promoter, splice-site, and TFBS prediction. DNABERT is designed to work well in data-scarce settings and supports cross-organism transfer from human-genome pretraining.

The paper also emphasizes interpretability: attention patterns can highlight important subregions, conserved motifs, and candidate functional variants.

## Limitations and Future Work

DNABERT models DNA sequence context but does not explicitly model LD, genotype dosage, or causal fine-mapping objectives. Its interpretability is attention-based rather than causal ablation-based.

## Related Work

- BERT: pretraining and fine-tuning framework.
- Transformer: self-attention backbone.
- Nucleotide Transformer: later larger-scale DNA foundation model.
- GLFM: downstream fine-mapping method motivated by genomic language modeling but adapted to genotype/LD structure.
