---
id: kim-2020-artificial-intelligence-in-drug
domain: drug-discovery
title: "Artificial Intelligence in Drug Discovery: A Comprehensive Review of Data-driven and Machine Learning Approaches"
authors: Hyunho Kim, Eunyoung Kim, Ingoo Lee, Bongsung Bae, Minsu Park, Hojung Nam
year: 2020
doi: 10.1007/s12257-020-0049-y
category: reviews
pdf_path: "C:/Users/dlsrnsi/OneDrive/문서/New project/papers/kim-2020-artificial-intelligence-in-drug.pdf"
pdf_filename: kim-2020-artificial-intelligence-in-drug.pdf
source_collection: external
status: draft
---

## One-line Summary

This review organizes AI-guided drug discovery across target identification, hit identification, ADMET prediction, lead optimization, and drug repositioning.

## 1. Document Information

Published in Biotechnology and Bioprocess Engineering in 2020. The review motivates AI for drug discovery by the high cost and long timelines of drug research and development.

## 2. Key Contributions

- Surveys data-driven and machine learning approaches in drug discovery.
- Organizes AI applications by stage: target identification, hit identification, ADMET prediction, lead optimization, and drug repositioning.
- Summarizes major data sources used in each field.
- Discusses challenges, limitations, and future directions.

## 3. Methodology and Architecture

This is a review rather than a single model paper. Its method is organizational: it divides AI-guided drug discovery into stages, then reviews representative algorithms and databases for each stage.

### Review Scope

The paper covers five main drug discovery tasks:

1. Target identification
2. Hit identification
3. ADMET prediction
4. Lead optimization
5. Drug repositioning

### Materials / Data Resources Reviewed

The review emphasizes that AI drug discovery depends heavily on curated databases. Examples include:

- Target identification: DisGeNET, Comparative Toxicogenomics Database, LinkedOmics, Open Targets, HMDD, DepMap, STRING, Therapeutic Target Database.
- Hit identification: structure databases, ligand-binding databases, chemogenomic resources, and DTI resources such as DrugBank, ChEMBL, BindingDB, and related protein-ligand datasets.
- ADMET prediction: ADMET-focused datasets covering absorption, distribution, metabolism, excretion, toxicity, blood-brain barrier, Caco-2 permeability, solubility, CYP interactions, and hERG/toxicity endpoints.
- Lead optimization: molecular datasets used for generative models, including SMILES-based corpora and activity/property-labeled molecules.
- Drug repositioning: drug-centric, disease-centric, side-effect, gene-expression, and network resources.

### Method Families Reviewed

- Statistical omics analysis for target identification.
- Network-based approaches for target identification and repositioning.
- Machine learning classifiers and feature-importance models.
- Structure-based virtual screening and docking.
- Ligand-based similarity and descriptor approaches.
- Chemogenomic DTI prediction.
- Deep learning with learned representations for compounds, proteins, or both.
- Generative RNNs, autoencoders, and reinforcement learning for lead optimization.

## 4. Key Results and Benchmarks

### Target Identification

The review presents target identification as an omics integration problem. Statistical, network-based, and ML approaches are used to connect genes/proteins to diseases or phenotypes. The recurring limitation is heterogeneity: omics datasets vary in format, condition, annotation, and disease coverage.

### Hit Identification

The review separates hit identification into structure-based, ligand-based, and chemogenomic approaches. It notes that structure-based methods are powerful when target structures are available, ligand-based methods exploit similarity to known active compounds, and chemogenomic methods attempt to learn across both compound and protein spaces.

### ADMET Prediction

ADMET prediction is framed as crucial because activity without acceptable pharmacokinetics or safety is not useful. The review covers absorption, distribution, metabolism/excretion, and toxicity models, including hERG-like safety endpoints. It highlights data quality, endpoint inconsistency, and assay heterogeneity as major obstacles.

### Lead Optimization

The review covers AI-generated molecules using RNN language models, generative autoencoders, and reinforcement learning. The core result is a shift from screening existing molecules toward generating and optimizing candidate structures under property constraints.

### Drug Repositioning

Drug repositioning methods include network clustering, network propagation, machine learning, and deep learning. These methods exploit existing information about drugs, diseases, side effects, targets, expression signatures, and clinical/biological networks to propose new indications.

### Limitations and Future Directions

Across stages, the paper repeatedly returns to several bottlenecks:

- biased and incomplete biological databases;
- inconsistent assay conditions and labels;
- poor interpretability for many ML/DL predictions;
- difficulty translating computational hits into experimentally validated leads;
- need for better data integration across heterogeneous sources.

## 5. Limitations and Future Work

The review emphasizes unresolved challenges in applying AI to drug discovery, including data limitations and the need for methods that are useful across real development workflows.

## 6. Related Work

- [[drug-discovery/drug-target-interactions/lee-2019-deepconv-dti-prediction-of-drug]] - Example of sequence-based DTI prediction.
- [[drug-discovery/admet-safety/kim-2022-bayesherg-a-robust-reliable]] - Example of safety prediction.
- [[drug-discovery/binding-sites-virtual-screening/kang-2022-ai-based-prediction-of-new]] - Example of AI-assisted hit discovery and screening.

## 7. Glossary

- Hit identification: Finding compounds with initial activity against a target.
- Lead optimization: Improving potency, selectivity, pharmacokinetics, or safety of hit compounds.
- Drug repositioning: Finding new uses for known drugs.
