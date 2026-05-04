# Genomic Foundation Models

- [[ji-2021-dnabert-pre-trained-bidirectional-encoder]] - BERT-style k-mer language model for DNA sequences.
- [[dalla-torre-2025-nucleotide-transformer-building-and]] - DNA transformer foundation models for human genomics.
- [[zhou-2024-dnabert-2-efficient-foundation-model]] - Efficient BPE-tokenized multi-species DNA foundation model and GUE benchmark.
- [[nguyen-2023-hyenadna-long-range-genomic-sequence]] - Long-context attention-free DNA model at single-nucleotide resolution.
- [[schiff-2024-caduceus-bi-directional-equivariant-long]] - Bidirectional, reverse-complement equivariant Mamba DNA foundation model.
- [[sanabria-2024-dna-language-model-grover-learns]] - Human-genome BPE/BERT model focused on sequence grammar and token interpretability.
- [[chen-2025-bmfm-dna-a-snp-aware]] - SNP-aware DNA foundation model that encodes genetic variation during pretraining.
- [[brixi-2026-genome-modelling-and-design-across]] - Evo 2; generalist genome-scale foundation model across all domains of life.

## Comparative Summary

This category contains the genomic language-model context for GLFM. [[ji-2021-dnabert-pre-trained-bidirectional-encoder]] is the direct BERT-style precedent: it tokenizes DNA into k-mers, pretrains with masked language modeling, and fine-tunes on regulatory prediction tasks. [[zhou-2024-dnabert-2-efficient-foundation-model]] improves the DNABERT line with BPE tokenization, ALiBi, and a standardized benchmark. [[dalla-torre-2025-nucleotide-transformer-building-and]] is a larger transformer foundation-model family for human genomics.

[[nguyen-2023-hyenadna-long-range-genomic-sequence]] and [[schiff-2024-caduceus-bi-directional-equivariant-long]] address long-range context by moving away from dense attention, while [[sanabria-2024-dna-language-model-grover-learns]] focuses on interpretable BPE vocabulary learning in the human genome. [[chen-2025-bmfm-dna-a-snp-aware]] is a bridge toward variant-aware modeling, but still differs from genotype/LD language models because it encodes variant possibilities in sequence rather than phased genotype states. [[brixi-2026-genome-modelling-and-design-across]] represents the current generalist scale frontier, but it remains a sequence model rather than a fine-mapping model.

Compared with these models, [[genomics/fine-mapping/lee-2026-genomic-language-based-finemapping]] changes the object and objective. Most pages here learn from DNA sequence context; GLFM models genotype loci, injects LD into attention, fine-tunes on phenotype prediction, and performs SNP-level causal scoring.

## Not Yet Ingested

- GENA-LM - PDF download from Oxford was blocked. DOI: <u>10.1093/nar/gkae1310</u>. Add when a local PDF is available.

## Comparison Table

| Paper | Sequence object | Pretraining idea | Downstream target | Link to GLFM |
|---|---|---|---|---|
| [[ji-2021-dnabert-pre-trained-bidirectional-encoder]] | DNA k-mers | BERT-style MLM | Promoters, TFBSs, splice sites | Genomic BERT precedent |
| [[dalla-torre-2025-nucleotide-transformer-building-and]] | DNA sequences | Transformer foundation models | Human genomics prediction tasks | Larger foundation-model context |
| [[zhou-2024-dnabert-2-efficient-foundation-model]] | DNA BPE tokens | Efficient BPE + Transformer MLM | GUE genome tasks | Efficient DNABERT successor |
| [[nguyen-2023-hyenadna-long-range-genomic-sequence]] | Single nucleotides | Long convolution next-token prediction | Long-context genomics tasks | Long-context sequence contrast |
| [[schiff-2024-caduceus-bi-directional-equivariant-long]] | Single nucleotides | Bidirectional RC-equivariant MLM | Variant effect and regulatory tasks | DNA-specific inductive bias contrast |
| [[sanabria-2024-dna-language-model-grover-learns]] | Human-genome BPE tokens | BERT-style masked token prediction | Genome element and protein-DNA binding tasks | Token grammar/vocabulary contrast |
| [[chen-2025-bmfm-dna-a-snp-aware]] | SNP-aware DNA tokens | ModernBERT MLM with variant encoding | Variant-aware genomic prediction | Variant-aware bridge |
| [[brixi-2026-genome-modelling-and-design-across]] | Single nucleotides across all domains of life | Large-scale genome pretraining | Variant effect, generation, interpretation | Generalist scale frontier |
| [[genomics/genotype-language-models/huang-2026-genobert-a-language-model-for]] | Phased genotype tokens | Masked genotype recovery | Genotype imputation | Closest genotype-BERT comparison |
| [[genomics/fine-mapping/lee-2026-genomic-language-based-finemapping]] | Genotype/LD locus sequence | LD-aware BERT-style MLM | Causal SNP fine-mapping | Task-specific extension |
