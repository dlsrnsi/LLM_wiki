---
id: lee-2022-sequence-based-prediction-of-protein
domain: drug-discovery
title: "Sequence-based prediction of protein binding regions and drug-target interactions"
authors: Ingoo Lee, Hojung Nam
year: 2022
doi: 10.1186/s13321-022-00584-w
source: lee-2022-sequence-based-prediction-of-protein.md
category: drug-target-interactions
pdf_path: "C:/Users/dlsrnsi/OneDrive/문서/New project/papers/lee-2022-sequence-based-prediction-of-protein.pdf"
pdf_filename: lee-2022-sequence-based-prediction-of-protein.pdf
source_collection: external
status: draft
tags: [dti, binding-regions, hots, transformer]
---

## Summary

HoTS predicts both binding regions and drug-target interactions from protein sequences and ligands. The core idea is that learning to identify binding regions improves DTI prediction and makes the model more interpretable.

## Key Contributions

- Adds binding-region prediction as an explicit training objective.
- Uses transformer-based modeling and object detection for sequence-region prediction.
- Reports improved DTI performance after binding-region pretraining.
- Provides interpretable attention to protein regions relevant to ligand binding.

## Materials and Data

BR training used scPDB v2017 and PDBBind v2018, producing 23,278 complexes and 6,143 proteins. BR tests used COACH and HOLO4K after removing overlapping complexes. DTI training used DrugBank, KEGG, and IUPHAR: 12,814 compounds, 3,789 proteins, 36,152 positives, and 72,304 generated negatives. PubChem BioAssay provided independent DTI tests.

## Methods

HoTS maps binding information from 3D complexes onto UniProt sequences, expands binding-site residues into sequence binding regions, and trains a sequence-level object-detection task. Protein sequences are encoded by CNN motif extraction, pooled into grids, and processed with transformer blocks together with a compound token derived from Morgan fingerprints. The BR head predicts center, width, and confidence; the DTI head uses the compound token to predict interaction probability.

Training happens in two phases: BR pretraining first, then DTI fine-tuning with alternating BR and DTI updates. Focal loss handles the class imbalance of sparse binding regions.

## Results

BR validation AP reached 62.28%, while DTI validation reached AUROC 0.8542 and AUPR 0.8232. On COACH, HoTS achieved top-(n+2) BR success of 85.26 +/- 0.8% for unseen complexes and 81.4 +/- 0.9% for unseen proteins. On HOLO4K, top-(n+2) success was 79.1 +/- 0.4% and 71.7 +/- 0.6%, respectively.

For DTI prediction, HoTS with BR pretraining outperformed MONN, DeepConv-DTI, TransformerCPI, and HoTS without BR pretraining on PubChem test sets. The advantage was strongest on proteins sharing SCOPe-family motifs with the BR training set.

Attention analysis supported the mechanism: compound-token attention was higher on BR grids than non-BR grids, with KS-test p-values below 1e-53 on COACH and below 1e-100 on HOLO4K.

## Limitations

HoTS still uses Morgan/circular fingerprints for compounds and does not model full 3D conformational context at prediction time. It also predicts interaction likelihood and binding regions, not drug action type such as agonism or antagonism.

## Related Papers

- [[lee-2019-deepconv-dti-prediction-of-drug]] - Method connection: HoTS builds on sequence motif extraction but adds transformer attention and supervised binding-region prediction.
- [[drug-discovery/binding-sites-virtual-screening/kang-2022-ai-based-prediction-of-new]] - Method/result connection: the P2X3R paper uses HoTS binding-region and DTI predictions to define a binding cavity and select compounds for experimental screening.
