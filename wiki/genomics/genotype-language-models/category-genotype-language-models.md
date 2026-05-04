# Genotype Language Models

- [[huang-2026-genobert-a-language-model-for]] - Genotype BERT model for reference-free imputation and LD dependency learning.

## Comparative Summary

This sub-domain is for models that treat genotype or haplotype state sequences as language-model inputs. It is distinct from [[genomics/genomic-foundation-models/category-genomic-foundation-models]], where most models read reference or multispecies DNA sequence.

The key comparison for GLFM is that [[huang-2026-genobert-a-language-model-for]] learns LD structure to reconstruct missing genotypes, while [[genomics/fine-mapping/lee-2026-genomic-language-based-finemapping]] uses a BERT-style genotype encoder as the representation backbone for causal fine-mapping. Both are closer to genotype language modeling than DNABERT-style reference-sequence modeling.

## Comparison Table

| Paper | Input object | LD usage | Main output | Link to GLFM |
|---|---|---|---|---|
| [[huang-2026-genobert-a-language-model-for]] | Phased genotype tokens | Learned with attention and relative genomic positional bias | Imputed genotypes | Closest genotype-BERT comparison |
| [[genomics/fine-mapping/lee-2026-genomic-language-based-finemapping]] | Genotype/LD locus sequence | Infused into BERT-style representation and perturbation analysis | Causal SNP score/ranking | Fine-mapping use of genotype LM |
