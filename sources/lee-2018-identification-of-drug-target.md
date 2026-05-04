---
id: lee-2018-identification-of-drug-target
domain: drug-discovery
title: "Identification of drug-target interaction by a random walk with restart method on an interactome network"
authors: Ingoo Lee, Hojung Nam
year: 2018
doi: 10.1186/s12859-018-2199-x
category: drug-target-interactions
pdf_path: "C:/Users/dlsrnsi/OneDrive/문서/New project/papers/lee-2018-identification-of-drug-target.pdf"
pdf_filename: lee-2018-identification-of-drug-target.pdf
source_collection: external
status: draft
---

## One-line Summary

The paper predicts drug-target interactions by using random walk with restart to weight features from global topology in an interactome network.

## 1. Document Information

Published in BMC Bioinformatics in 2018. The paper addresses computational DTI prediction using network information.

## 2. Key Contributions

- Uses random walk with restart to capture global topology beyond directly connected nodes.
- Applies global network features to DTI prediction.
- Compares the method with a guilt-by-association approach.
- Analyzes how node connectivity affects prediction performance.

## 3. Methodology and Architecture

### Materials and Networks

- PPI network: HIPPIE database, filtered to high-confidence interactions; 14,086 proteins and 153,749 protein-protein interactions.
- DDI network: constructed from DrugBank by connecting drugs that share targets; 3,609 drugs and 77,713 drug-drug edges.
- DTI network/training positives: DrugBank known drug-target pairs; 8,838 DTIs.
- Training negatives: 20 randomly generated negative DTI sets, each with 8,838 drug-target pairs absent from known DTIs but using known drugs and targets.
- Independent test set: PubChem binding assays, with Kd <= 10 uM active pairs as positives and inactive non-binding-assay samples as negatives; 6,533 positives and 6,892 negatives across 629 target proteins and 2,635 drugs.

### Feature Representation

- Drug features: PaDEL fingerprints, 1,024-bit substructure vector.
- Protein features: primary sequence descriptors totaling 1,287 dimensions, including amino acid composition, dipeptide composition, normalized Moreau-Broto autocorrelation, Moran autocorrelation, Geary autocorrelation, and CTD-style composition/transition/distribution descriptors.
- DTI feature vector: concatenated weighted drug and protein features, total 2,311 dimensions.

### Random Walk With Restart Weighting

The method runs RWR separately over the DDI and PPI networks. For each seed drug or protein, RWR produces affinity scores to all nodes in the corresponding network. These affinity scores weight neighboring and more distant node features, so each drug/protein feature vector becomes a topology-aware mixture of its own features and features of graph-near nodes.

Restart probability controls the tradeoff between preserving the original node features and importing network-neighbor features. A low restart probability diffuses more strongly through topology; a high restart probability preserves the seed more strongly.

### Prediction Model

Weighted drug and protein vectors are concatenated and classified with cubic k-nearest neighbors. The cubic distance emphasizes feature differences after topology weighting. The restart probability was selected using independent-test performance.

## 4. Key Results and Benchmarks

### Restart Probability and Feature Weighting

- The optimized restart probability was c = 0.25 based on independent-test AUC.
- Low c improved training performance by diffusing features strongly, but too much or too little preservation of seed features hurt independent-test performance.
- In an AURKA drug example, RWR weighting made three AURKA-binding drugs more similar in feature space: average Euclidean distance decreased from 0.4271 before weighting to 0.1580 after weighting.

### Prediction Performance

- The RWR-weighted model outperformed a previous guilt-by-association weighting method on the independent test set.
- Reported independent-test AUC: 0.675 +/- 0.018 for the proposed method versus 0.628 +/- 0.026 for guilt-by-association.
- Paired t-test p-value: 6.17e-6.
- Compared with NRWRH on a restricted dataset containing only seen drugs and targets, NRWRH had AUC 0.6127 and this method had AUC 0.6025; the authors note that their method can also handle new drugs/targets via features.

### Qualitative Predictions

- Many top-ranked new predictions were kinase inhibitor-kinase pairs.
- Pazopanib was a strong case: among 169 positive pazopanib DTI pairs in the independent test set, the model correctly predicted 168 with scores above 0.8, above the 0.62 classification threshold.
- The authors attribute this to densely connected kinase target subnetworks, where topology-aware weighting makes target features more predictive.

## 5. Limitations and Future Work

Performance depends on network coverage and quality. The reported independent-test AUC indicates that generalization is harder than fitting the training network.

## 6. Related Work

- [[drug-discovery/drug-target-interactions/lee-2019-deepconv-dti-prediction-of-drug]] - Later sequence-based DTI model.
- [[drug-discovery/drug-target-interactions/lee-2022-sequence-based-prediction-of-protein]] - Later binding-region-aware DTI model.

## 7. Glossary

- Random walk with restart: A graph algorithm that repeatedly propagates from a starting node while returning to it with some probability.
- Guilt by association: Predicting function or interaction from direct neighbors in a network.
- Interactome: A network of biological interactions.
