---
id: dalla-torre-2025-nucleotide-transformer-building-and
domain: genomics
title: "Nucleotide Transformer, building and evaluating robust foundation models for human genomics"
authors:
  - Hugo Dalla-Torre
  - Liam Gonzalez
  - Javier Mendoza-Revilla
  - Nicolas Lopez Carranza
  - Adam Henryk Grzywaczewski
  - Francesco Oteri
  - Christian Dallago
  - Evan Trop
  - Bernardo P. de Almeida
  - Hassan Sirelkhatim
  - Guillaume Richard
  - Marcin Skwark
  - Karim Beguir
  - Marie Lopez
  - Thomas Pierrot
year: 2025
doi: 10.1038/s41592-024-02523-z
source: dalla-torre-2025-nucleotide-transformer-building-and.md
category: genomic-foundation-models
pdf_path: /C:/Users/dlsrnsi/OneDrive/문서/New project/papers/dalla-torre-2025-nucleotide-transformer-building-and.pdf
pdf_filename: dalla-torre-2025-nucleotide-transformer-building-and.pdf
source_collection: web-open-access
status: draft
tags: [genomics, foundation-models, transformers]
---

## Summary

Nucleotide Transformer trains and evaluates transformer foundation models on DNA sequences for human genomics.

## Key Contributions

- Builds a family of nucleotide sequence foundation models.
- Evaluates transfer to genomics tasks with limited labels.
- Demonstrates that transformer pretraining can encode useful DNA sequence context.

## Materials and Data

The paper builds a family of DNA foundation models from large unlabeled genomic corpora and evaluates them on curated genomics prediction tasks.

Pretraining datasets include:

- human reference genome sequences;
- 3,202 genetically diverse human genomes from the 1000 Genomes resource;
- 850 genomes from diverse species, including multiple model organisms.

The first model set includes:

- Human reference 500M;
- 1000G 500M;
- 1000G 2.5B;
- Multispecies 2.5B.

The models are pretrained on 6-kb unannotated genomic sequences. Downstream evaluation uses 18 curated genomic datasets covering:

- splice-site prediction;
- promoter prediction;
- histone modification prediction;
- enhancer prediction;
- chromatin and regulatory element tasks.

The paper also tests larger practical benchmarks against specialized supervised models, including chromatin feature classification, splice-site prediction, and enhancer activity prediction.

## Methods

Nucleotide Transformer adapts masked language modeling to DNA sequences. Its training and evaluation pipeline follows the same broad pretrain/fine-tune logic as [[machine-learning/transformer-language-models/devlin-2018-bert-pre-training-of-deep]], but the tokens and tasks are genomic.

### Pretraining

Input DNA sequences are tokenized and masked. A Transformer language model learns to predict masked nucleotide tokens from sequence context. The learned hidden states are context-specific embeddings of DNA sequence windows.

The paper scales both model size and training diversity. One important methodological axis is whether better downstream genomics performance comes from:

- more parameters;
- more human genetic diversity;
- broader multispecies sequence diversity;
- longer effective context or perception field.

### Transfer strategies

The paper evaluates two main transfer modes:

- Probing: freeze the language model, extract embeddings from selected layers, and train simpler downstream predictors such as logistic regression or small MLPs.
- Fine-tuning: replace the language-model head with a task-specific classification or regression head and update the model for the downstream task.

Fine-tuning uses a parameter-efficient strategy that updates only about 0.1% of total model parameters. This reduces memory and storage costs and makes fine-tuning large DNA models practical on a single GPU.

The paper uses tenfold cross-validation for the curated benchmark tasks. This matters because many genomics datasets are label-limited; the benchmark is designed to measure robust transfer rather than only large supervised-data performance.

### Interpretability analyses

The paper analyzes whether pretrained models learn known genomic structure without supervised labels. It examines:

- embedding separation for intergenic, intronic, coding, and UTR regions;
- attention enrichment over genomic elements;
- layer-dependent representation quality;
- zero-shot scores for functionally important variants.

This makes the paper relevant to GLFM because both ask whether sequence models can encode biologically meaningful context beyond direct supervised labels.

## Results

The paper reports that pretrained genomic foundation models transfer well across diverse molecular phenotype tasks.

Key reported results:

- In the 18-task benchmark, probing alone matched BPNet baselines in 5 tasks and exceeded them in 8 tasks.
- Fine-tuned NT models matched baselines in 6 tasks and surpassed them in 12 of 18 tasks.
- The Multispecies 2.5B model achieved the highest overall average performance among compared foundation models in the reported benchmark, with mean MCC around 0.755 across categories.
- The paper reports that larger and more diverse models generally outperform smaller or less diverse models, and that multispecies pretraining can help even on human-derived tasks.
- Parameter-efficient fine-tuning was often more practical than exhaustive probing because probing depends heavily on layer choice, downstream model choice, and hyperparameters.
- On chromatin feature classification, the Multispecies 2.5B model reached average AUC values close to DeepSEA, around 1% lower on average in the reported comparison.
- On splice-site prediction, the model reached top-k accuracy around 95% and precision-recall AUC around 0.98, matching or outperforming several specialized splicing baselines under the tested context settings.
- On enhancer activity prediction, the model was close to DeepSTARR, slightly above for housekeeping enhancer activity and below for developmental enhancer activity in the reported comparison.

For this wiki, the important result is that DNA language-model pretraining can produce transferable genomic representations, especially when model scale and sequence diversity are increased.

## Limitations

Nucleotide Transformer does not perform fine-mapping and does not explicitly model LD structure or causal SNP ablation. It predicts molecular or regulatory labels from sequence context, whereas GLFM tries to prioritize causal variants in GWAS loci where correlated variants can act as LD proxies.

The model also inherits practical issues common to large sequence foundation models: high pretraining cost, context-length limits, layer-selection sensitivity for probing, and the need to define downstream tasks carefully so that benchmark performance corresponds to biological utility.

## Related Papers

- [[genomics/fine-mapping/lee-2026-genomic-language-based-finemapping]] - Method connection: both use transformer-style genomics representation learning, but GLFM adds LD-aware attention and causal inference machinery.
- [[machine-learning/transformer-language-models/devlin-2018-bert-pre-training-of-deep]] - Method connection: both inherit the pretrain/fine-tune language-model pattern.
