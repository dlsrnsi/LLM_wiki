---
id: lee-2019-deepconv-dti-prediction-of-drug
domain: drug-discovery
title: "DeepConv-DTI: Prediction of drug-target interactions via deep learning with convolution on protein sequences"
authors: Ingoo Lee, Jongsoo Keum, Hojung Nam
year: 2019
doi: 10.1371/journal.pcbi.1007129
source: lee-2019-deepconv-dti-prediction-of-drug.md
category: drug-target-interactions
pdf_path: "C:/Users/dlsrnsi/OneDrive/문서/New project/papers/lee-2019-deepconv-dti-prediction-of-drug.pdf"
pdf_filename: lee-2019-deepconv-dti-prediction-of-drug.pdf
source_collection: external
status: draft
tags: [dti, cnn, protein-sequence]
---

## Summary

DeepConv-DTI predicts drug-target interactions by learning local residue patterns directly from raw protein sequences. It is an important step from hand-crafted protein descriptors toward learned sequence representations in DTI prediction.

## Overview Figure

![[drug-discovery/assets/deepconv-dti-figure-1.png]]

Figure 1 summarizes the full DeepConv-DTI workflow: training DTI dataset generation from DrugBank, KEGG, and IUPHAR; CNN-based protein sequence modeling with drug fingerprints; hyperparameter optimization using MATADOR and predicted negative DTIs; and independent DTI prediction using PubChem BioAssay and KinaseSARfari.

## Key Contributions

- Applies CNNs to protein sequences for DTI prediction.
- Captures local amino-acid subsequence patterns with convolution filters.
- Reports better performance than previous descriptor-based and deep learning DTI models.
- Shows that pooled convolution outputs can reveal binding-site-related protein regions.

## Materials and Data

Training DTIs came from DrugBank, KEGG, and IUPHAR, producing 11,950 compounds, 3,675 proteins, and 32,568 positive DTIs after identifier cleanup. Ten negative DTI sets were randomly generated. Hyperparameters were tuned on MATADOR positives plus credible negatives. Independent tests used PubChem BioAssay and KinaseSARfari.

## Methods

Drugs are represented as 2,048-bit Morgan fingerprints. Proteins are represented by raw amino acid sequences padded to length 2,500. A trainable embedding layer converts residues to vectors, then 1D CNN filters scan local residue windows. Global max-pooling takes the strongest signal for each filter, which lets the model find motifs regardless of position. Drug and protein representations are concatenated for binary DTI prediction.

Regularization includes L2 penalty, spatial dropout on the embedding layer, and batch normalization. Hyperparameters were selected by external validation, yielding AUPR 0.832 and AUC 0.852.

## Results

DeepConv-DTI outperformed CTD and Smith-Waterman protein descriptors on independent PubChem datasets, including new-compound, new-target, and new-DTI subsets. It also outperformed MFDR, DeepDTI, DeepDTA, and DL-CPI under common DTI train/test comparisons.

For interpretability, pooled convolution outputs were compared with 7,179 sc-PDB Vertebrata entries. Random null distributions were generated 10,000 times per entry. Binding-site coverage by convolution results was significant for 14.6%, 30.3%, and 42.2% of entries at the 1%, 5%, and 10% levels. Learned protein features for 1,527 training proteins also roughly separated GPCRs, nuclear receptors, ion channels, kinases, and proteases in t-SNE.

## Limitations

DeepConv-DTI learns from sequence and fingerprints but does not explicitly train on binding-region labels. Its binding-site interpretation comes from post-hoc convolution activation analysis, which is less direct than later binding-region-supervised models.

## Related Papers

- [[lee-2022-sequence-based-prediction-of-protein]] - Method/result connection: HoTS reuses sequence motif extraction ideas but adds binding-region pretraining and reports improved DTI performance.
- [[lee-2018-identification-of-drug-target]] - Method connection: both are DTI predictors, but DeepConv-DTI replaces topology-weighted descriptors with CNN sequence features.
