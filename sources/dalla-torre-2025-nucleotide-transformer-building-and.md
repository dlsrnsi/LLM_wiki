---
id: dalla-torre-2025-nucleotide-transformer-building-and
domain: genomics
title: "Nucleotide Transformer, building and evaluating robust foundation models for human genomics"
authors: Hugo Dalla-Torre; Liam Gonzalez; Javier Mendoza-Revilla; Nicolas Lopez Carranza; Adam Henryk Grzywaczewski; Francesco Oteri; Christian Dallago; Evan Trop; Bernardo P. de Almeida; Hassan Sirelkhatim; Guillaume Richard; Marcin Skwark; Karim Beguir; Marie Lopez; Thomas Pierrot
year: 2025
doi: 10.1038/s41592-024-02523-z
category: genomic-foundation-models
pdf_path: /C:/Users/dlsrnsi/OneDrive/문서/New project/papers/dalla-torre-2025-nucleotide-transformer-building-and.pdf
pdf_filename: dalla-torre-2025-nucleotide-transformer-building-and.pdf
source_collection: web-open-access
status: draft
---

## One-line Summary

Nucleotide Transformer builds and evaluates transformer foundation models pretrained on DNA sequences for human genomics tasks.

## Key Contributions

- Trains a family of DNA foundation models at multiple scales.
- Evaluates transfer to molecular phenotype prediction and variant-related tasks.
- Provides a genomics-specific foundation-model reference for GLFM's language-model motivation.

## Methodology and Architecture

The paper uses transformer language-model pretraining on nucleotide sequences, then evaluates learned representations on downstream genomics tasks.

The paper pretrains transformer DNA language models on 6-kb unannotated genomic sequences. Model/dataset variants include Human reference 500M, 1000G 500M, 1000G 2.5B, and Multispecies 2.5B. Training data include the human reference genome, 3,202 genetically diverse human genomes, and 850 genomes from diverse species.

Downstream evaluation uses 18 curated genomic prediction datasets covering splice sites, promoters, histone modifications, enhancers, chromatin features, and regulatory elements. Transfer is evaluated in two modes:

- probing, where the foundation model is frozen and selected-layer embeddings are fed into logistic regression or small MLP predictors;
- fine-tuning, where the language-model head is replaced by a task head and a parameter-efficient update changes about 0.1% of model parameters.

The paper uses tenfold cross-validation for the main curated benchmark. It also analyzes embeddings, attention maps, and zero-shot variant scores to inspect whether the model learned genomic elements without direct supervision.

## Key Results and Benchmarks

The paper reports that DNA foundation models can transfer to genomics prediction tasks where annotated data are limited, supporting the broader premise that sequence pretraining can encode useful biological context.

Important reported results: probing matched BPNet baselines in 5 tasks and exceeded them in 8 of 18 tasks; fine-tuned NT models matched baselines in 6 tasks and surpassed them in 12 of 18 tasks; Multispecies 2.5B had the strongest overall benchmark performance among compared foundation models, with mean MCC around 0.755 across categories; chromatin feature classification was close to DeepSEA; splice-site prediction reached top-k accuracy around 95% and PR-AUC around 0.98; enhancer activity prediction was close to DeepSTARR.

## Limitations and Future Work

Nucleotide Transformer is not a causal fine-mapping method. It does not inject locus-specific LD into attention or perform SNP-level causal ablation.
