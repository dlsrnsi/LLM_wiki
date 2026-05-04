---
id: lee-2019-deepconv-dti-prediction-of-drug
domain: drug-discovery
title: "DeepConv-DTI: Prediction of drug-target interactions via deep learning with convolution on protein sequences"
authors: Ingoo Lee, Jongsoo Keum, Hojung Nam
year: 2019
doi: 10.1371/journal.pcbi.1007129
category: drug-target-interactions
pdf_path: "C:/Users/dlsrnsi/OneDrive/문서/New project/papers/lee-2019-deepconv-dti-prediction-of-drug.pdf"
pdf_filename: lee-2019-deepconv-dti-prediction-of-drug.pdf
source_collection: external
status: draft
---

## One-line Summary

DeepConv-DTI predicts drug-target interactions by applying convolutional neural networks to raw protein sequences to capture local residue patterns relevant to binding.

## 1. Document Information

Published in PLOS Computational Biology in 2019. The paper addresses in silico DTI prediction as a way to reduce expensive experimental screening.

## 2. Key Contributions

- Uses raw protein sequences instead of relying only on conventional hand-crafted protein descriptors.
- Applies CNN filters over amino acid subsequences of multiple lengths.
- Trains on large-scale DTI information and evaluates on an independent dataset.
- Shows that pooled convolutional features can highlight protein regions relevant to interactions.

## 3. Methodology and Architecture

### Materials and Datasets

- Training positives: DTIs from DrugBank, KEGG, and IUPHAR.
- Training set after identifier unification and filtering: 11,950 compounds, 3,675 proteins, and 32,568 DTIs.
- Negative training sets: ten randomly generated negative DTI sets, each exclusive from known positives.
- External validation set: MATADOR positives with direct protein annotations plus credible negatives from the Liu et al. method; 370 positive and 507 negative DTIs.
- Independent test set 1: PubChem BioAssay binding data, with positives from Kd < 10 uM binding assays and sampled inactive negatives; 36,456 total positive/negative samples, 21,907 drugs, 698 proteins.
- Independent test set 2: ChEMBL KinaseSARfari, with Kd < 10 uM positives; 3,835 positives, 5,520 negatives, 3,379 compounds, 389 proteins.
- Binding-site analysis set: sc-PDB, 7,179 Vertebrata entries with binding-site annotations.

### Feature Representation

- Drug input: Morgan/circular fingerprints from SMILES using RDKit, radius 2, 2,048-bit binary vector.
- Protein input: raw amino acid sequence, padded to a maximum length of 2,500 with null labels.
- Baseline protein features: CTD descriptors and normalized Smith-Waterman similarity descriptors.

### Model Architecture

DeepConv-DTI embeds amino acids into trainable vectors, applies 1D convolutions over protein sequences with multiple window sizes, and globally max-pools each filter. This design makes the protein representation insensitive to the absolute location of a motif and focuses on local residue patterns likely to participate in binding. Drug fingerprints are processed through fully connected layers. Protein and drug latent features are concatenated and passed through fully connected layers for binary DTI prediction with a sigmoid output.

Regularization used L2 penalties, spatial dropout on the embedding layer, and batch normalization. The model used ELU activations except for the sigmoid output and optimized binary cross-entropy with Adam.

### Hyperparameter and Baseline Strategy

Hyperparameters were chosen using the external validation dataset rather than training-set cross-validation, because randomly sampled negatives can bias validation. The tuned model reached AUPR 0.832 and AUC 0.852 on the external validation set. Baselines included CTD descriptors, Smith-Waterman similarity descriptors, MFDR/SAE, DeepDTI/DBN, DeepDTA/CNN, and DL-CPI.

## 4. Key Results and Benchmarks

### DTI Prediction Results

- The convolution-based protein representation outperformed CTD descriptors and normalized Smith-Waterman similarity descriptors across PubChem datasets and subsets.
- Performance was evaluated on all PubChem, new-compound, new-target, and new-DTI subsets, plus KinaseSARfari.
- Compared with MFDR, DeepDTI, DeepDTA, and DL-CPI under common train/test data, DeepConv-DTI showed better accuracy and F1 on the independent PubChem test set.
- The authors argue that DeepDTA underperformed here because it was optimized for dense kinase affinity datasets, whereas this benchmark spans multiple protein classes.

### Binding-Site Analysis

- Pooled convolution results were compared with sc-PDB binding-site annotations.
- The authors generated random convolution-result null distributions 10,000 times per sc-PDB entry and tested whether model-highlighted regions covered binding sites more than random expectation.
- At significance cutoffs of 1%, 5%, and 10%, 14.6%, 30.3%, and 42.2% of sc-PDB entries were significantly enriched for binding-site coverage.
- Case visualizations included FKBP1A with FKA (1a7x_1) and MAP kinase-activated protein kinase 2 with ADP (1ny3_1), where high convolution activations overlapped ligand-proximal regions.

### Representation Analysis

- t-SNE of learned protein features for 1,527 training proteins roughly separated major protein classes: 257 GPCRs, 44 nuclear receptors, 304 ion channels, 604 kinases, and 318 proteases.

## 5. Limitations and Future Work

The method learns from sequence and interaction data rather than explicit three-dimensional target structures. Its interpretability is limited compared with later models that directly train on binding-region objectives.

## 6. Related Work

- [[drug-discovery/drug-target-interactions/lee-2022-sequence-based-prediction-of-protein]] - Later HoTS model adds explicit binding-region prediction.
- [[drug-discovery/drug-target-interactions/lee-2018-identification-of-drug-target]] - Earlier network-based DTI prediction approach.

## 7. Glossary

- DTI: Drug-target interaction.
- CNN: Convolutional neural network.
- Protein descriptor: A feature representation of a protein used by a machine learning model.
