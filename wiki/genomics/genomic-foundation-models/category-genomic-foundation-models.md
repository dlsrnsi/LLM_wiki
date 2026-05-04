# Genomic Foundation Models

- [[ji-2021-dnabert-pre-trained-bidirectional-encoder]] - BERT-style k-mer language model for DNA sequences.
- [[dalla-torre-2025-nucleotide-transformer-building-and]] - DNA transformer foundation models for human genomics.

## Comparative Summary

This category contains the genomic language-model context for GLFM. [[ji-2021-dnabert-pre-trained-bidirectional-encoder]] is the direct BERT-style precedent: it tokenizes DNA into k-mers, pretrains with masked language modeling, and fine-tunes on regulatory prediction tasks. [[dalla-torre-2025-nucleotide-transformer-building-and]] is a later larger-scale foundation-model family for human genomics.

Compared with both, [[genomics/fine-mapping/lee-2026-genomic-language-based-finemapping]] changes the object and objective. DNABERT and Nucleotide Transformer learn from DNA sequence context; GLFM models genotype loci, injects LD into attention, fine-tunes on phenotype prediction, and performs SNP-level causal scoring.

## Comparison Table

| Paper | Sequence object | Pretraining idea | Downstream target | Link to GLFM |
|---|---|---|---|---|
| [[ji-2021-dnabert-pre-trained-bidirectional-encoder]] | DNA k-mers | BERT-style MLM | Promoters, TFBSs, splice sites | Genomic BERT precedent |
| [[dalla-torre-2025-nucleotide-transformer-building-and]] | DNA sequences | Transformer foundation models | Human genomics prediction tasks | Larger foundation-model context |
| [[genomics/fine-mapping/lee-2026-genomic-language-based-finemapping]] | Genotype/LD locus sequence | LD-aware BERT-style MLM | Causal SNP fine-mapping | Task-specific extension |
