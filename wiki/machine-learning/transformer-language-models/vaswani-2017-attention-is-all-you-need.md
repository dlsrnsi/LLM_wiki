---
id: vaswani-2017-attention-is-all-you-need
domain: machine-learning
title: "Attention Is All You Need"
authors:
  - Ashish Vaswani
  - Noam Shazeer
  - Niki Parmar
  - Jakob Uszkoreit
  - Llion Jones
  - Aidan N. Gomez
  - Lukasz Kaiser
  - Illia Polosukhin
year: 2017
doi: 10.48550/arXiv.1706.03762
source: vaswani-2017-attention-is-all-you-need.md
category: transformer-language-models
pdf_path: /C:/Users/dlsrnsi/OneDrive/문서/New project/papers/vaswani-2017-attention-is-all-you-need.pdf
pdf_filename: vaswani-2017-attention-is-all-you-need.pdf
source_collection: web-open-access
status: draft
tags: [machine-learning, transformers, attention]
---

## Summary

This paper introduces the Transformer, a sequence model based on self-attention rather than recurrence or convolution.

## Key Contributions

- Introduces scaled dot-product attention and multi-head attention.
- Uses positional encodings to represent order.
- Enables highly parallel sequence modeling.

## Materials and Data

The paper evaluates sequence-to-sequence modeling, mainly machine translation. Its main datasets are:

- WMT 2014 English-German, about 4.5 million sentence pairs, encoded with byte-pair encoding and a shared source-target vocabulary of about 37,000 tokens.
- WMT 2014 English-French, about 36 million sentence pairs, using a 32,000 word-piece vocabulary.
- English constituency parsing as an additional generalization task.

This paper is included in the wiki as architectural background. It is not a genomics paper, but its self-attention mechanism is a direct ancestor of BERT, DNABERT, Nucleotide Transformer, and GLFM-style sequence/context models.

## Methods

The Transformer removes recurrence and convolution from sequence transduction. It uses an encoder-decoder architecture built from stacked self-attention, encoder-decoder attention, and position-wise feed-forward networks.

### Encoder and decoder stacks

The encoder has \(N=6\) identical layers. Each encoder layer contains:

- a multi-head self-attention sublayer;
- a position-wise feed-forward sublayer;
- residual connections around each sublayer;
- layer normalization after the residual addition.

The decoder also has \(N=6\) layers, but each decoder layer adds a third sublayer: encoder-decoder attention over the encoder outputs. Decoder self-attention is masked so that position \(i\) cannot attend to future output positions.

### Scaled dot-product attention

Attention maps queries, keys, and values to a weighted sum of values. With query matrix \(Q\), key matrix \(K\), value matrix \(V\), and key dimension \(d_k\):

$$
\operatorname{Attention}(Q,K,V)
=
\operatorname{softmax}\left(\frac{QK^\top}{\sqrt{d_k}}\right)V
$$

The scale factor \(1/\sqrt{d_k}\) prevents dot products from becoming too large in magnitude, which would push the softmax into low-gradient regions.

### Multi-head attention

Instead of applying one attention operation in the full representation space, the Transformer projects \(Q\), \(K\), and \(V\) into multiple learned subspaces:

$$
\operatorname{MultiHead}(Q,K,V)
=
\operatorname{Concat}(\operatorname{head}_1,\ldots,\operatorname{head}_h)W^O
$$

where:

$$
\operatorname{head}_i
=
\operatorname{Attention}(QW_i^Q,KW_i^K,VW_i^V)
$$

In the base model, \(h=8\), \(d_{model}=512\), and \(d_k=d_v=64\). Multi-head attention lets different heads specialize to different positions or relation types.

### Feed-forward layers and positional encoding

Each layer also has a position-wise feed-forward network:

$$
\operatorname{FFN}(x)=\max(0,xW_1+b_1)W_2+b_2
$$

with model dimension \(d_{model}=512\) and inner dimension \(d_{ff}=2048\).

Because the model has no recurrence or convolution, token order is injected through positional encodings added to token embeddings:

$$
PE_{(pos,2i)}=\sin(pos/10000^{2i/d_{model}})
$$

$$
PE_{(pos,2i+1)}=\cos(pos/10000^{2i/d_{model}})
$$

This gives each position a deterministic representation and allows relative offsets to be represented through linear transformations.

### Training objective and optimization

The model is trained for translation with teacher-forced sequence prediction. The paper uses Adam with:

$$
\beta_1=0.9,\qquad \beta_2=0.98,\qquad \epsilon=10^{-9}
$$

and a warmup learning-rate schedule:

$$
lrate=d_{model}^{-0.5}
\cdot
\min(step\_num^{-0.5},\;step\_num\cdot warmup\_steps^{-1.5})
$$

with \(warmup\_steps=4000\). Regularization includes residual dropout and label smoothing.

## Results

The Transformer achieved strong translation performance while improving parallelism over recurrent models.

Reported results include:

- WMT 2014 English-German: Transformer base reached 27.3 BLEU; Transformer big reached 28.4 BLEU.
- WMT 2014 English-French: Transformer big reached 41.8 BLEU after 3.5 days of training on 8 P100 GPUs.
- The base model trained in about 12 hours on 8 P100 GPUs, substantially faster than recurrent/convolutional competitors at similar or better quality.
- The paper highlights that self-attention has \(O(1)\) sequential operations per layer, whereas recurrent layers require \(O(n)\) sequential operations over sequence length.

For this wiki, the key result is not only BLEU. The important reusable result is that self-attention can serve as a general sequence modeling primitive that captures long-range dependencies with high parallelism.

## Limitations

This is not a genomics or fine-mapping paper. It provides the self-attention mechanism later reused by BERT and genomic foundation models.

The original Transformer also has quadratic attention cost in sequence length, \(O(n^2d)\), which becomes important for long biological sequences. Later genomics models must address tokenization, context length, memory cost, and biological objectives that are absent from machine translation.

## Related Papers

- [[devlin-2018-bert-pre-training-of-deep]] - Method connection: BERT uses transformer encoders for bidirectional masked pretraining.
- [[genomics/fine-mapping/lee-2026-genomic-language-based-finemapping]] - Method connection: GLFM uses transformer self-attention but injects an LD-aware prior.
