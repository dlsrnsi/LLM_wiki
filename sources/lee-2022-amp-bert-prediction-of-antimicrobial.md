---
id: lee-2022-amp-bert-prediction-of-antimicrobial
domain: drug-discovery
title: "AMP-BERT: Prediction of antimicrobial peptide function based on a BERT model"
authors: Hansol Lee, Songyeon Lee, Ingoo Lee, Hojung Nam
year: 2022
doi: 10.1002/pro.4529
category: peptide-function
pdf_path: "C:/Users/dlsrnsi/OneDrive/문서/New project/papers/lee-2022-amp-bert-prediction-of-antimicrobial.pdf"
pdf_filename: lee-2022-amp-bert-prediction-of-antimicrobial.pdf
source_collection: external
status: draft
---

## One-line Summary

AMP-BERT fine-tunes a BERT-style model to classify antimicrobial peptides and uses attention analysis to interpret residues associated with peptide function.

## 1. Document Information

Published in Protein Science in 2022. The study addresses antimicrobial peptide prediction as an alternative route for antimicrobial discovery.

## 2. Key Contributions

- Proposes AMP-BERT, a BERT-based classifier for AMP versus non-AMP peptide sequences.
- Uses fine-tuning to extract structural and functional information from peptide sequences.
- Compares AMP-BERT against other machine learning and deep learning AMP prediction methods.
- Uses attention mechanisms for interpretable residue-level analysis.

## 3. Methodology and Architecture

### Materials and Datasets

- Fine-tuning dataset: benchmark AMP dataset from Veltri et al. with 1,778 AMP positives from APD3 and 1,778 non-AMP negatives from UniProt cytoplasmic proteins after excluding antimicrobial/antibiotic/antiviral/antifungal/effector/excreted annotations.
- External positive test set: DRAMP sequences filtered by CD-HIT at 90% identity and excluding APD3-sourced sequences, resulting in 2,065 AMP positives.
- External negative test set: non-AMP sequences from AmPEP/UniProt filtered by CD-HIT at 90%, length <= 110 aa, matched to the positive length distribution, and excluding >=90% identity to negative training samples, resulting in 1,908 negatives.
- Total external test set: 3,973 sequences.
- ACEP comparison subset: 2,640 sequences with available PSSM information.
- Pretrained model: ProtBERT-BFD, pretrained on about 2.1 billion protein sequences from BFD.

### Tokenization and Model

Each peptide is treated as a protein-language sentence. Residues are tokenized as single amino-acid tokens using the 20 standard IUPAC amino acids plus X for unknown residues. A CLS token is placed at the beginning, a SEP token at the end, and PAD tokens are used up to a fixed length of 200 tokens. Each token is embedded into a 1,024-dimensional vector.

AMP-BERT fine-tunes ProtBERT-BFD for binary AMP/non-AMP classification. Instead of global average pooling over all residue embeddings, it extracts the CLS token embedding as the whole-sequence representation, passes it through a fully connected layer and sigmoid function, and classifies probabilities >= 0.5 as AMP.

### Training and Evaluation

- Optimizer: AdamW.
- Loss: binary cross-entropy.
- Hyperparameter search used a 9:1 train/validation split.
- Best setting: learning rate 5e-5, 15 epochs, no warm-up steps, 0.1 weight decay.
- Validation: five-repeated 10-fold cross-validation over the 3,556 fine-tuning sequences.
- Final model: retrained on all fine-tuning samples for 15 epochs and evaluated on the 3,973-sequence external test set.
- Metrics: ACC, AUROC, AUPR, sensitivity, specificity, and F1.

### Baselines

- CTD + RF: composition/transition/distribution descriptors with random forest.
- AMPscanner: amino-acid sequence features with convolutional and BiLSTM layers.
- ACEP: PSSM, amino-acid sequence, and AAC features trained with convolutional, LSTM, attention, and dense layers; evaluated on the PSSM-available subset.

## 4. Key Results and Benchmarks

### External Test Performance

On the 3,973-sequence external test set:

- CTD + RF: SN 0.6536, SP 0.5980, F1 0.6495, ACC 0.6300, AUROC 0.6735, AUPR 0.6586.
- AMPscanner: SN 0.8412, SP 0.6347, F1 0.7722, ACC 0.7420, AUROC 0.7884, AUPR 0.7621.
- AMP-BERT: SN 0.8760, SP 0.6352, F1 0.7917, ACC 0.7604, AUROC 0.8183, AUPR 0.7866.

On the PSSM-available subset:

- ACEP: SN 0.8740, SP 0.6107, F1 0.7670, ACC 0.7398, AUROC 0.8101, AUPR 0.7411.
- AMP-BERTsub: SN 0.8941, SP 0.6330, F1 0.8049, ACC 0.7610, AUROC 0.8445, AUPR 0.7984.

### Attention and Structural Interpretation

- Attention analyses focused on known AMP structural features rather than only classification scores.
- Siamycin II (DRAMP18350) and Leaf cyclotide 1 (DRAMP00875) were used as disulfide-bond examples; middle BERT layers attended strongly around cysteine residues involved in bridges.
- EcAMP1 (DRAMP00387) and gamma-1-purothionin/Defensin-like protein 1 (DRAMP00434) were used as secondary-structure examples; layer/head analyses aligned attention with alpha-helical and beta-strand regions.
- The authors argue that fine-tuning allows AMP-BERT to learn structural patterns relevant to peptide function, including disulfide bridges, alpha-helices, beta-strands, and hydrophobic cores.

## 5. Limitations and Future Work

The paper is focused on sequence-based classification. Experimental validation and broader biological context remain necessary before predicted peptides can be treated as therapeutic leads.

## 6. Related Work

- [[drug-discovery/reviews/kim-2020-artificial-intelligence-in-drug]] - Review context for AI-enabled discovery workflows.

## 7. Glossary

- AMP: Antimicrobial peptide.
- BERT: Transformer encoder architecture originally developed for language modeling and adapted here to peptide sequences.
- Attention: A model mechanism that can indicate which positions influence prediction.
