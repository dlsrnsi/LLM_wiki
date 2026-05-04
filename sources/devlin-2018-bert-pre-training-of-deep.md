---
id: devlin-2018-bert-pre-training-of-deep
domain: machine-learning
title: "BERT, Pre-training of Deep Bidirectional Transformers for Language Understanding"
authors: Jacob Devlin; Ming-Wei Chang; Kenton Lee; Kristina Toutanova
year: 2018
doi: 10.48550/arXiv.1810.04805
category: transformer-language-models
pdf_path: /C:/Users/dlsrnsi/OneDrive/문서/New project/papers/devlin-2018-bert-pre-training-of-deep.pdf
pdf_filename: devlin-2018-bert-pre-training-of-deep.pdf
source_collection: web-open-access
status: draft
---

## One-line Summary

BERT pretrains deep bidirectional transformer encoders with masked language modeling and next-sentence prediction, then fine-tunes for downstream tasks.

## Key Contributions

- Introduces bidirectional transformer encoder pretraining.
- Uses masked language modeling to condition on both left and right context.
- Establishes the pretrain-then-fine-tune pattern reused by many domain language models.

## Methodology and Architecture

BERT uses a multi-layer transformer encoder. Pretraining masks input tokens and trains the model to recover them from context. Fine-tuning adds task-specific heads with minimal architectural changes.

The two main model sizes are BERTBASE with \(L=12\), \(H=768\), \(A=12\), about 110M parameters, and BERTLARGE with \(L=24\), \(H=1024\), \(A=16\), about 340M parameters. Inputs combine WordPiece token embeddings, segment embeddings, and position embeddings, with `[CLS]` for sequence-level outputs and `[SEP]` for separation.

Masked language modeling chooses 15% of WordPiece positions for prediction. Of those selected positions, 80% are replaced by `[MASK]`, 10% by a random token, and 10% are left unchanged. The model predicts the original token from bidirectional context using cross-entropy.

Next sentence prediction samples sentence pair \(A,B\), where \(B\) is the true next sentence 50% of the time and a random sentence 50% of the time. The `[CLS]` representation is used for the binary IsNext/NotNext task.

Fine-tuning updates all pretrained parameters. Classification uses the final `[CLS]` vector; token-level tasks use final token vectors; question answering predicts answer span start and end positions.

## Key Results and Benchmarks

The paper reports state-of-the-art NLP results at the time across multiple benchmarks. In this wiki, BERT is the direct modeling precedent for DNABERT, Nucleotide Transformer, and GLFM's BERT-style genotype encoder.

Reported results include GLUE score 80.5 for BERTLARGE, MultiNLI accuracy 86.7%, SQuAD v1.1 Test F1 93.2, and SQuAD v2.0 Test F1 83.1. The key reusable result is the pretrain/fine-tune recipe: one bidirectional encoder pretrained on unlabeled sequences can be adapted to many supervised tasks with small output heads.

## Limitations and Future Work

BERT is a natural-language model, not a genomics model. Domain transfer requires redesigning tokens, pretraining corpora, and objectives.
