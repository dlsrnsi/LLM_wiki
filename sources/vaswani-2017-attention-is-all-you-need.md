---
id: vaswani-2017-attention-is-all-you-need
domain: machine-learning
title: "Attention Is All You Need"
authors: Ashish Vaswani; Noam Shazeer; Niki Parmar; Jakob Uszkoreit; Llion Jones; Aidan N. Gomez; Lukasz Kaiser; Illia Polosukhin
year: 2017
doi: 10.48550/arXiv.1706.03762
category: transformer-language-models
pdf_path: /C:/Users/dlsrnsi/OneDrive/문서/New project/papers/vaswani-2017-attention-is-all-you-need.pdf
pdf_filename: vaswani-2017-attention-is-all-you-need.pdf
source_collection: web-open-access
status: draft
---

## One-line Summary

This paper introduces the Transformer architecture based on self-attention, replacing recurrence and convolution for sequence modeling.

## Key Contributions

- Introduces multi-head self-attention.
- Uses positional encoding to represent token order.
- Establishes the encoder-decoder transformer architecture that later underlies BERT and many genomic language models.

## Methodology and Architecture

The Transformer uses scaled dot-product attention, multi-head attention, residual connections, layer normalization, feed-forward sublayers, and positional encodings.

The encoder and decoder each use \(N=6\) stacked layers. Encoder layers contain multi-head self-attention and a feed-forward sublayer. Decoder layers add encoder-decoder attention and use masked self-attention to preserve autoregressive generation.

Scaled dot-product attention is:

$$
\operatorname{Attention}(Q,K,V)
=
\operatorname{softmax}\left(\frac{QK^\top}{\sqrt{d_k}}\right)V
$$

Multi-head attention projects queries, keys, and values into multiple learned subspaces:

$$
\operatorname{MultiHead}(Q,K,V)
=
\operatorname{Concat}(\operatorname{head}_1,\ldots,\operatorname{head}_h)W^O
$$

where:

$$
\operatorname{head}_i=\operatorname{Attention}(QW_i^Q,KW_i^K,VW_i^V)
$$

The base model uses \(d_{model}=512\), \(h=8\), \(d_k=d_v=64\), and feed-forward inner dimension \(d_{ff}=2048\). Positional encodings add sinusoidal position information:

$$
PE_{(pos,2i)}=\sin(pos/10000^{2i/d_{model}})
$$

$$
PE_{(pos,2i+1)}=\cos(pos/10000^{2i/d_{model}})
$$

Training uses Adam with warmup and inverse-square-root decay:

$$
lrate=d_{model}^{-0.5}\min(step\_num^{-0.5},step\_num\cdot warmup\_steps^{-1.5})
$$

## Key Results and Benchmarks

The paper demonstrates strong machine translation performance with improved parallelism compared with recurrent sequence models.

The paper evaluates on WMT 2014 English-German and English-French. Reported scores include 27.3 BLEU for Transformer base on English-German, 28.4 BLEU for Transformer big on English-German, and 41.8 BLEU for Transformer big on English-French. The base model trained in about 12 hours on 8 P100 GPUs; the big English-French model trained for 3.5 days.

## Limitations and Future Work

The paper is a general NLP architecture paper, not a genomics or fine-mapping method. In this wiki it is included as architecture background for BERT-style models.
