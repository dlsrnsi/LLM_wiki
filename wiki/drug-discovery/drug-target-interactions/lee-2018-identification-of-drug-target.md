---
id: lee-2018-identification-of-drug-target
domain: drug-discovery
title: "Identification of drug-target interaction by a random walk with restart method on an interactome network"
authors: Ingoo Lee, Hojung Nam
year: 2018
doi: 10.1186/s12859-018-2199-x
source: lee-2018-identification-of-drug-target.md
category: drug-target-interactions
pdf_path: "C:/Users/dlsrnsi/OneDrive/문서/New project/papers/lee-2018-identification-of-drug-target.pdf"
pdf_filename: lee-2018-identification-of-drug-target.pdf
source_collection: external
status: draft
tags: [dti, network, random-walk-with-restart]
---

## Summary

This paper predicts drug-target interactions using global topology from an interactome network. Random walk with restart lets the model use information beyond immediate network neighbors.

## Key Contributions

- Moves beyond direct guilt-by-association features.
- Uses random walk with restart for topology-weighted features.
- Reports improved prediction performance compared with unweighted or direct-neighbor approaches.

## Materials and Data

The model uses three networks: a HIPPIE PPI network with 14,086 proteins and 153,749 PPIs; a DrugBank-derived DDI network with 3,609 drugs and 77,713 edges between drugs sharing targets; and 8,838 DrugBank DTIs as positives. The independent PubChem test set contains 6,533 positives and 6,892 negatives.

Drug features are 1,024-bit PaDEL fingerprints. Protein features are 1,287 sequence-derived descriptors. Each DTI is represented by concatenating weighted drug and protein vectors.

## Methods

Random walk with restart runs separately on the drug-drug and protein-protein networks. For each seed node, RWR produces affinity scores to graph-near nodes. These scores weight the feature vectors, creating topology-aware features that include direct and indirect neighbors while preserving the seed node according to restart probability. Weighted drug and protein vectors are concatenated into a 2,311-dimensional DTI vector and classified with cubic kNN.

## Results

The best restart probability was c = 0.25. RWR weighting made drugs sharing targets more similar in feature space; in the AURKA example, average Euclidean distance among three AURKA-binding drugs decreased from 0.4271 to 0.1580 after weighting.

On the independent PubChem test, the method reached AUC 0.675 +/- 0.018 versus 0.628 +/- 0.026 for a guilt-by-association baseline, with paired t-test p = 6.17e-6. On a restricted seen-drug/seen-target comparison, NRWRH slightly outperformed this method, but this method retains the advantage of feature-based prediction for drugs or targets not seen in training.

Qualitatively, the model recovered many kinase inhibitor-kinase interactions. For pazopanib, it correctly predicted 168 of 169 positive DTI pairs with scores above 0.8.

## Limitations

The method depends on the coverage and reliability of PPI/DDI networks. It also requires hand-crafted drug and protein features, and its independent-test performance remains modest compared with later sequence-learning approaches.

## Related Papers

- [[lee-2019-deepconv-dti-prediction-of-drug]] - Method connection: both predict DTIs, but this paper uses topology-weighted hand-crafted features while DeepConv-DTI replaces protein descriptors with CNN-learned sequence motifs.
- [[lee-2022-sequence-based-prediction-of-protein]] - Method/result connection: HoTS extends the DTI prediction line by adding explicit binding-region supervision and reports stronger DTI evaluation.
