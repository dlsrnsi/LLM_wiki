---
id: devlin-2018-bert-pre-training-of-deep
domain: machine-learning
title: "BERT, Pre-training of Deep Bidirectional Transformers for Language Understanding"
authors:
  - Jacob Devlin
  - Ming-Wei Chang
  - Kenton Lee
  - Kristina Toutanova
year: 2018
doi: 10.48550/arXiv.1810.04805
source: devlin-2018-bert-pre-training-of-deep.md
category: transformer-language-models
pdf_path: /C:/Users/dlsrnsi/OneDrive/문서/New project/papers/devlin-2018-bert-pre-training-of-deep.pdf
pdf_filename: devlin-2018-bert-pre-training-of-deep.pdf
source_collection: web-open-access
status: draft
tags: [machine-learning, bert, transformers]
---

## Summary

BERT is a bidirectional transformer encoder pretrained with masked language modeling and fine-tuned for downstream tasks.

## Key Contributions

- Establishes deep bidirectional transformer pretraining.
- Uses masked language modeling to learn from both left and right context.
- Makes downstream adaptation possible with small task-specific heads.

## Materials and Data

The paper pretrains on unlabeled natural-language corpora and evaluates on supervised NLP tasks. Its pretraining corpora are:

- BooksCorpus, about 800 million words;
- English Wikipedia, about 2.5 billion words, using text passages rather than lists, tables, and headers.

The input representation uses WordPiece tokenization with a 30,000-token vocabulary. Each example can represent either one sentence or a sentence pair using:

- `[CLS]` at the beginning for sequence-level prediction;
- `[SEP]` as a separator;
- token embeddings;
- segment embeddings distinguishing sentence A from sentence B;
- position embeddings.

The paper evaluates on 11 NLP tasks, including GLUE, SQuAD v1.1, SQuAD v2.0, and SWAG. It is included here as the main pretrain/fine-tune template inherited by DNA language models.

## Methods

BERT is a multi-layer bidirectional Transformer encoder. It keeps the downstream architecture simple: pretrain one encoder, then fine-tune all parameters with a small task-specific output layer.

### Architecture

The paper defines model size by:

- \(L\): number of Transformer layers;
- \(H\): hidden size;
- \(A\): number of self-attention heads.

The two main configurations are:

- BERTBASE: \(L=12\), \(H=768\), \(A=12\), about 110M parameters.
- BERTLARGE: \(L=24\), \(H=1024\), \(A=16\), about 340M parameters.

BERT uses bidirectional self-attention, unlike left-to-right language models where each token can only attend to previous tokens.

### Masked language modeling

BERT's central pretraining task is masked language modeling. The model randomly chooses 15% of WordPiece token positions for prediction. For a chosen token:

- 80% of the time it is replaced with `[MASK]`;
- 10% of the time it is replaced with a random token;
- 10% of the time it is left unchanged.

The final hidden state at the chosen position is used to predict the original token with cross-entropy loss. This avoids the left-to-right constraint and allows the representation to use both left and right context.

### Next sentence prediction

BERT also uses next sentence prediction to train sentence-pair representations. For sentence pair \(A,B\):

- 50% of examples use the true next sentence as \(B\), labeled `IsNext`;
- 50% use a random sentence as \(B\), labeled `NotNext`.

The `[CLS]` representation is used for this binary prediction task. This is meant to support downstream tasks that require relationships between two sequences, such as question answering and natural language inference.

### Fine-tuning

For fine-tuning, BERT initializes from the pretrained encoder and updates all parameters end-to-end. Task-specific heads are small:

- sentence classification uses the final `[CLS]` vector;
- token-level tasks use final token vectors;
- question answering predicts start and end spans over passage tokens.

For GLUE classification, the paper uses a classifier:

$$
\operatorname{softmax}(CW^\top)
$$

where \(C\) is the final hidden vector of `[CLS]` and \(W\) is a task-specific classification matrix.

## Results

BERT produced large gains across NLP benchmarks and became the template for many domain language models, including DNA sequence models.

Key reported results:

- GLUE: BERTLARGE reached a GLUE score of 80.5, compared with 72.8 for OpenAI GPT at the time reported.
- GLUE task averages improved by about 7.0 percentage points over prior state of the art for BERTLARGE in the paper's table.
- MultiNLI reached 86.7% accuracy for BERTLARGE.
- SQuAD v1.1 Test F1 reached 93.2.
- SQuAD v2.0 Test F1 reached 83.1.

For this wiki, BERT's most important result is methodological: a single bidirectional Transformer encoder pretrained on unlabeled sequences can be adapted to many downstream supervised tasks with limited task-specific architecture.

## Limitations

BERT is not genomics-specific. Genomic applications require redefining tokens, pretraining corpora, and downstream objectives.

The original pretraining tasks are also imperfect matches to biological sequence modeling. DNA models must decide how to tokenize nucleotides or k-mers, what context length is biologically meaningful, how to represent reverse complements or haplotypes, and whether masked-token prediction is sufficient for causal variant interpretation.

## Related Papers

- [[vaswani-2017-attention-is-all-you-need]] - Method connection: BERT is built on transformer encoders.
- [[genomics/genomic-foundation-models/dalla-torre-2025-nucleotide-transformer-building-and]] - Method connection: Nucleotide Transformer adapts transformer pretraining to DNA sequences.
- [[genomics/fine-mapping/lee-2026-genomic-language-based-finemapping]] - Method connection: GLFM uses a BERT-style masked pretraining and fine-tuning workflow for genotype sequences.
