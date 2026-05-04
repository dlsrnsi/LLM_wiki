---
id: kang-2022-ai-based-prediction-of-new
domain: drug-discovery
title: "AI-based prediction of new binding site and virtual screening for the discovery of novel P2X3 receptor antagonists"
authors: Koon Mook Kang, Ingoo Lee, Hojung Nam, Yong-Chul Kim
year: 2022
doi: 10.1016/j.ejmech.2022.114556
category: binding-sites-virtual-screening
pdf_path: "C:/Users/dlsrnsi/OneDrive/문서/New project/papers/kang-2022-ai-based-prediction-of-new.pdf"
pdf_filename: kang-2022-ai-based-prediction-of-new.pdf
source_collection: external
status: draft
---

## One-line Summary

The paper uses HoTS binding-region prediction, cavity search, pharmacophore modeling, docking, and in vitro screening to propose and validate a new P2X3 receptor antagonist discovery workflow.

## 1. Document Information

Published in European Journal of Medicinal Chemistry in 2022. The study targets the P2X3 receptor and focuses on AI-assisted hit identification.

## 2. Key Contributions

- Applies the HoTS model to predict candidate ligand-binding regions on the P2X3 receptor sequence.
- Converts predicted binding regions into a putative binding site through cavity search.
- Builds pharmacophore queries from the proposed binding site.
- Compares virtual screening approaches using pharmacophore/docking signals and HoTS interaction prediction.
- Screens selected compounds experimentally and reports antagonistic activity against P2X3R.

## 3. Methodology and Architecture

### Materials and Inputs

- Target: human P2X3 receptor, using the canonical P2X3_HUMAN sequence (UniProt P56373).
- Known ligands: 18 known hP2X3R antagonists were used to validate HoTS model choice and binding-region predictions.
- Structural templates: hP2X3R structures from RCSB PDB, including AF-219/Gefapixant-bound hP2X3R (PDB 5YVE) and ATP-bound hP2X3R (PDB 5SVK).
- Compound library: Korea Chemical Bank (KCB), 150,023 compounds.
- Experimental system: hP2X3R-expressing HEK293 stable cells, Fluo-4 calcium dye, and alpha,beta-MeATP agonist stimulation.

### Computational Workflow

1. HoTS binding-region prediction was run on hP2X3R with known antagonists to identify candidate binding-region clusters.
2. Three predicted clusters were mapped onto the hP2X3R trimer structure: a known antagonist-region cluster, an ion-channel vestibule/gate cluster, and a novel head/upper-body intersubunit cavity.
3. Cavity feasibility was assessed by short MD simulations of closed and open receptor states. The novel cavity was treated as potentially antagonist-relevant because its volume was larger in the closed state and smaller in the open state.
4. BLU-5937 derivatives were docked with CDOCKER into the novel site and known antagonist site. BLU-2 binding mode in the novel site was used as the pharmacophore seed.
5. Receptor-ligand pharmacophore generation produced 11 initial features and 20 candidate queries. Queries were validated against 16 BLU compounds and 800 DUD-E decoys using enrichment factor, ROC AUC, and active-compound FitValue.
6. Q12 was selected as the best pharmacophore query.
7. Two screening branches were run in parallel:
   - Pharmacophore-LibDock cascade: KCB compounds filtered by molecular properties, screened by Q12, then rescored by LibDock.
   - HoTS-DTI screening: all KCB compounds represented as Morgan/circular fingerprints and paired with the P2X3_HUMAN sequence.
8. Each branch selected 500 compounds for cell-based screening.

### Experimental Assay

The in vitro assay measured calcium influx in hP2X3R-expressing HEK293 cells. Cells were loaded with Fluo-4 dye, treated with compounds, stimulated with alpha,beta-MeATP, and measured with a FlexStation 3 plate reader. Hits were called using a cutoff of at least 50% inhibition at 25 uM.

## 4. Key Results and Benchmarks

### Binding-Site and Pharmacophore Results

- HoTS predicted three structurally interpretable P2X3R binding-region clusters.
- The novel cavity was located between the head domain of one subunit and upper body domain of an adjacent subunit.
- MD simulation estimated the novel cavity volume as larger in the closed state than the open state; the reported mean closed-state cavity volume was 115.23 A3 versus 32.96 A3 in the open state.
- BLU compound docking to the novel site gave consistent scaffold poses with RMSDs below 0.4 A, whereas docking to the known antagonist site was less consistent and scored worse.
- Q12 was selected as the optimized pharmacophore query because it gave the best enrichment behavior among generated queries.

### Screening and Biological Results

- KCB library size: 150,023 compounds.
- Molecular-property filtering reduced the pharmacophore branch to 97,301 compounds.
- Q12 screening selected 2,346 compounds with FitValue above 3.2 for LibDock rescoring.
- LibDock selected the top 500 compounds for in vitro testing.
- HoTS-DTI independently ranked 150,023 KCB compounds and selected the top 500 for in vitro testing.
- The HoTS branch identified 10 hits (HoTS-1 to HoTS-10).
- The Pharmacophore-LibDock branch identified 6 hits (PD-1 to PD-6).
- Several hits showed low micromolar IC50 values; HoTS-1, HoTS-2, and HoTS-4 shared a 2-chloro-6-morpholinopurinone core and had IC50 values in the 3.07-8.72 uM range.
- The total hit rate was reported as about 10-fold higher than prior random KCB screening.

### Binding-Mode Results

- All hit compounds had -CDOCKER interaction energy above 40 kcal/mol at the novel putative binding site.
- HoTS-3, HoTS-9, and PD-1 had -CDOCKER interaction energy above 60 kcal/mol.
- Lys113 and Asp76 were frequent polar-interaction residues; Lys65 appeared important for nonpolar interactions.
- HoTS-1, HoTS-2, and HoTS-4 interacted with Lys65, Lys113, and Asp76 and showed consistent novel-site binding modes.

## 5. Limitations and Future Work

The method depends on the reliability of predicted binding regions and on downstream structure-based assumptions made during cavity and pharmacophore construction. Follow-up work would need broader prospective validation across additional targets and chemical libraries.

## 6. Related Work

- [[drug-discovery/drug-target-interactions/lee-2022-sequence-based-prediction-of-protein]] - HoTS is the binding-region and DTI model used as the AI component.
- [[drug-discovery/drug-target-interactions/lee-2019-deepconv-dti-prediction-of-drug]] - Earlier sequence-based DTI modeling from the same research line.

## 7. Glossary

- P2X3 receptor: A purinergic receptor investigated as a drug target.
- HoTS: Highlights on Target Sequences, a model for predicting protein binding regions and DTIs.
- Pharmacophore: An abstract pattern of molecular features used to search for compounds likely to bind a target.
- Virtual screening: Computational prioritization of compounds before experimental testing.
