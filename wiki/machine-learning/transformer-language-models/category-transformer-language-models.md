# Transformer Language Models

- [[vaswani-2017-attention-is-all-you-need]] - Transformer architecture and self-attention.
- [[devlin-2018-bert-pre-training-of-deep]] - BERT masked pretraining and fine-tuning.

## Comparative Summary

These two papers form the method foundation for GLFM's sequence-modeling design. [[vaswani-2017-attention-is-all-you-need]] introduces self-attention and multi-head transformer layers. [[devlin-2018-bert-pre-training-of-deep]] turns transformer encoders into a pretrain/fine-tune framework with masked language modeling. [[genomics/fine-mapping/lee-2026-genomic-language-based-finemapping]] borrows this architecture family but changes the tokens, prior structure, and inference target for genotype fine-mapping.

