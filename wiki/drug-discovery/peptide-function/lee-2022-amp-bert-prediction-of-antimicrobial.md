---
id: lee-2022-amp-bert-prediction-of-antimicrobial
domain: drug-discovery
title: "AMP-BERT: Prediction of antimicrobial peptide function based on a BERT model"
authors: Hansol Lee, Songyeon Lee, Ingoo Lee, Hojung Nam
year: 2022
doi: 10.1002/pro.4529
source: lee-2022-amp-bert-prediction-of-antimicrobial.md
category: peptide-function
pdf_path: "C:/Users/dlsrnsi/OneDrive/문서/New project/papers/lee-2022-amp-bert-prediction-of-antimicrobial.pdf"
pdf_filename: lee-2022-amp-bert-prediction-of-antimicrobial.pdf
source_collection: external
status: draft
tags: [amp, bert, peptide-sequence, antimicrobial]
---

## Summary

AMP-BERT adapts a BERT-style transformer model to antimicrobial peptide classification. It treats peptide sequences as model input and uses attention analysis to interpret residues associated with antimicrobial function.

## Key Contributions

- Fine-tunes BERT for AMP versus non-AMP prediction.
- Reports best performance among evaluated methods on a curated external dataset.
- Uses attention to inspect residue-level signals.

## Materials and Data

The fine-tuning set contains 1,778 APD3 AMP positives and 1,778 UniProt-derived non-AMP negatives from Veltri et al. The external test set contains 2,065 DRAMP positives and 1,908 AmPEP/UniProt-derived negatives after CD-HIT filtering, length filtering, and removal of close training-set matches.

## Methods

AMP-BERT fine-tunes ProtBERT-BFD, a BERT model pretrained on about 2.1 billion protein sequences. Each peptide is tokenized residue-by-residue with CLS, SEP, and PAD tokens to a fixed length of 200. Token embeddings are 1,024-dimensional. The model uses the CLS embedding as the whole-peptide representation, then applies a fully connected layer and sigmoid classifier.

Training used AdamW, binary cross-entropy, learning rate 5e-5, 15 epochs, no warm-up, and weight decay 0.1. The model was checked with five-repeated 10-fold cross-validation and then retrained on all 3,556 fine-tuning sequences.

## Results

On the 3,973-sequence external test set, AMP-BERT achieved SN 0.8760, SP 0.6352, F1 0.7917, ACC 0.7604, AUROC 0.8183, and AUPR 0.7866. It outperformed CTD + RF and AMPscanner on most balanced metrics. On the 2,640-sequence PSSM-available subset, AMP-BERTsub outperformed ACEP with F1 0.8049, ACC 0.7610, AUROC 0.8445, and AUPR 0.7984.

The interpretability analysis is unusually concrete: attention patterns highlighted cysteine residues in disulfide-rich AMPs such as Siamycin II and Leaf cyclotide 1, and also matched alpha-helix/beta-strand regions in EcAMP1 and gamma-1-purothionin.

## Limitations

AMP-BERT predicts AMP versus non-AMP sequence labels, not microbial specificity, mechanism, toxicity, stability, or experimental therapeutic suitability. Structural interpretation is attention-based and limited by available peptide structure data.

## Related Papers

No direct paper-to-paper method/result link is recorded yet. This page is connected at the category and overview levels as the peptide-sequence counterpart to small-molecule DTI sequence models.
