---
id: lee-2022-sequence-based-prediction-of-protein
domain: drug-discovery
title: "Sequence-based prediction of protein binding regions and drug-target interactions"
authors: Ingoo Lee, Hojung Nam
year: 2022
doi: 10.1186/s13321-022-00584-w
category: drug-target-interactions
pdf_path: "C:/Users/dlsrnsi/OneDrive/문서/New project/papers/lee-2022-sequence-based-prediction-of-protein.pdf"
pdf_filename: lee-2022-sequence-based-prediction-of-protein.pdf
source_collection: external
status: draft
---

## One-line Summary

HoTS predicts protein binding regions and drug-target interactions from protein sequences and ligands, using binding-region prediction as an interpretable pretraining task.

## 1. Document Information

Published in Journal of Cheminformatics in 2022. The paper addresses both DTI prediction and interpretability.

## 2. Key Contributions

- Proposes Highlights on Target Sequences (HoTS), a model for protein binding-region and DTI prediction.
- Trains the model to predict binding regions for a protein sequence and ligand pair.
- Uses object detection with transformers for binding-region pretraining.
- Uses a compound token to attend to predicted binding regions for DTI prediction.
- Shows that explicit binding-region learning improves DTI prediction.

## 3. Methodology and Architecture

### Materials and Datasets

- Binding-region training data: scPDB v2017 and PDBBind v2018 complexes, yielding 23,278 complexes and 6,143 proteins after processing.
- Binding-region test data: COACH and HOLO4K with overlapping PDB complexes removed to prevent leakage.
- COACH BR test: 243 unseen protein-ligand complexes / 229 proteins, and 138 unseen-protein complexes / 138 proteins.
- HOLO4K BR test: 1,740 unseen protein-ligand complexes / 843 proteins, and 692 unseen-protein complexes / 425 proteins.
- DTI training data: DrugBank, KEGG, and IUPHAR; 12,814 compounds, 3,789 proteins, 36,152 positives, and 72,304 generated negatives.
- DTI validation data: MATADOR positives and Liu et al. credible negatives; 307 positives and 508 negatives.
- DTI test dataset 1: PubChem BioAssay over DGIdb druggable proteins; 21,459 compounds, 1,453 proteins, 20,391 positives and 20,391 negatives.
- DTI test dataset 2: subset with proteins in the same SCOPe families as BR training proteins; 4,991 compounds, 134 proteins, 5,001 positives and 5,001 negatives.

### Binding-Region Construction

Binding information from scPDB/PDBBind was mapped onto UniProt sequences. Non-consecutive binding-site residues were expanded to length 9 and merged into consecutive binding regions. Randomly generated BRs with IoU > 0.7 against true BRs were used during training.

### Model Architecture

HoTS combines protein sequence grids and compound tokens:

1. Protein sequences are embedded and passed through CNN layers to extract sequential motifs.
2. CNN outputs are split into grids and max-pooled, producing a sequence of protein grid encodings.
3. Compounds are represented as Morgan/circular fingerprints, radius 2 and 2,048 bits, then passed through fully connected layers into a compound token.
4. The compound token and protein grids are concatenated with positional encoding and processed by transformer blocks.
5. Protein grids predict binding-region center, width, and confidence.
6. The compound token aggregates grid information and predicts DTI probability.

The BR prediction head is inspired by object detection: it predicts center, width, and confidence over sequence grids. Focal loss addresses class imbalance because binding regions cover a small fraction of the protein sequence.

### Training Scheme

HoTS first pretrains the BR prediction model. It then adds additional transformer blocks for DTI prediction and fine-tunes on DTI data. During DTI fine-tuning, BR and DTI training are alternated; because the BR dataset is smaller, BR prediction is trained for three epochs per one DTI epoch.

### Evaluation

- BR prediction: IoU > 0.5 defines true positives; metrics include average precision, top-n success rate, and top-(n+2) success rate.
- DTI prediction: compared with MONN, DeepConv-DTI, TransformerCPI, and HoTS without BR pretraining.
- Attention: compound-token attention to BR versus non-BR grids was tested with Gumbel distributions and Kolmogorov-Smirnov tests.

## 4. Key Results and Benchmarks

### Training Results

- BR validation average precision reached 62.28%.
- DTI validation performance reached AUROC 0.8542 and AUPR 0.8232.

### Binding-Region Prediction

COACH:

- HoTS top-n success: 66.3 +/- 0.9% for unseen complexes and 59.9 +/- 1.3% for unseen proteins.
- HoTS top-(n+2) success: 85.26 +/- 0.8% for unseen complexes and 81.4 +/- 0.9% for unseen proteins.
- HoTS top-(n+2) exceeded the compared 3D methods on COACH, including P2Rank.

HOLO4K:

- HoTS top-n success: 61.4 +/- 0.7% for unseen complexes and 53.2 +/- 0.6% for unseen proteins.
- HoTS top-(n+2) success: 79.1 +/- 0.4% for unseen complexes and 71.7 +/- 0.6% for unseen proteins.
- P2Rank remained stronger on HOLO4K, but HoTS stayed competitive despite using sequence and fingerprints rather than 3D input at prediction time.

### DTI Prediction

- HoTS with BR pretraining outperformed MONN, DeepConv-DTI, TransformerCPI, and HoTS without BR pretraining on PubChem DTI test datasets.
- On DTI test dataset 1, HoTS achieved the best overall balance among sensitivity, specificity, precision, accuracy, and F1.
- On DTI test dataset 2, where proteins shared SCOPe families with the BR training set, HoTS showed an especially large advantage, supporting the claim that BR pretraining helps transfer structural-motif knowledge.

### Attention and Docking

- Compound-token attention was higher on BR grids than non-BR grids.
- COACH fitted Gumbel parameters: BR mu 0.1523 / beta 0.1093 versus non-BR mu 0.0640 / beta 0.0318.
- HOLO4K fitted Gumbel parameters: BR mu 0.2209 / beta 0.2168 versus non-BR mu 0.0549 / beta 0.0332.
- KS tests gave p < 1e-53 for COACH and p < 1e-100 for HOLO4K.
- A MARK1-Staurosporine docking example used predicted BRs to define the docking search region and recovered kinase binding motifs.

## 5. Limitations and Future Work

The approach depends on available protein-ligand complex and binding-site data for training. It predicts from sequences and ligands rather than directly modeling full 3D protein conformational context during prediction.

## 6. Related Work

- [[drug-discovery/drug-target-interactions/lee-2019-deepconv-dti-prediction-of-drug]] - Earlier CNN-based protein sequence DTI model.
- [[drug-discovery/binding-sites-virtual-screening/kang-2022-ai-based-prediction-of-new]] - Uses HoTS for P2X3 binding-site discovery and screening.

## 7. Glossary

- HoTS: Highlights on Target Sequences.
- Binding region: Protein sequence region associated with ligand binding.
- Transformer: Neural architecture using attention mechanisms to model sequence relationships.
