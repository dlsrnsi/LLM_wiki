---
id: kim-2020-artificial-intelligence-in-drug
domain: drug-discovery
title: "Artificial Intelligence in Drug Discovery: A Comprehensive Review of Data-driven and Machine Learning Approaches"
authors: Hyunho Kim, Eunyoung Kim, Ingoo Lee, Bongsung Bae, Minsu Park, Hojung Nam
year: 2020
doi: 10.1007/s12257-020-0049-y
source: kim-2020-artificial-intelligence-in-drug.md
category: reviews
pdf_path: "C:/Users/dlsrnsi/OneDrive/문서/New project/papers/kim-2020-artificial-intelligence-in-drug.pdf"
pdf_filename: kim-2020-artificial-intelligence-in-drug.pdf
source_collection: external
status: draft
tags: [review, ai-drug-discovery, machine-learning]
---

## Summary

This review maps AI and machine learning methods onto the drug discovery pipeline. It covers target identification, hit identification, ADMET prediction, lead optimization, and drug repositioning.

## Key Contributions

- Gives the current wiki its broad drug discovery frame.
- Organizes AI applications by discovery stage.
- Summarizes data sources and discusses limitations and future directions.

## Materials and Data

This is a review paper, so the material base is not a single dataset. Instead, the review catalogs database families: omics and disease resources for target identification; ligand, structure, and DTI resources for hit identification; ADMET endpoint databases; molecular corpora for generative lead optimization; and drug/disease/side-effect/expression resources for repositioning.

## Methods

The review method is a structured survey of the drug discovery pipeline. It divides AI-guided discovery into target identification, hit identification, ADMET prediction, lead optimization, and drug repositioning, then compares representative computational approaches and databases for each stage.

## Results

The review's main result is a pipeline map:

- Target identification uses statistical omics, networks, and ML to connect genes/proteins to disease.
- Hit identification uses structure-based, ligand-based, and chemogenomic methods to prioritize compounds.
- ADMET prediction filters compounds for pharmacokinetic and safety risk, including toxicity endpoints such as hERG.
- Lead optimization increasingly uses generative RNNs, autoencoders, and reinforcement learning to suggest improved molecules.
- Drug repositioning uses networks, ML, deep learning, side effects, expression signatures, and disease resources to find new indications.

The recurring bottleneck is data: heterogeneous formats, inconsistent assay labels, biased coverage, and limited interpretability. This makes the review a useful anchor for the other pages: DeepConv-DTI and HoTS sit in hit/DTI prediction, BayeshERG sits in ADMET/safety, and the P2X3R paper is a concrete hit-identification workflow.

## Limitations

As a broad review, this paper is not a benchmark and does not validate a new method. Its conclusions should be used as pipeline context, not as direct evidence that one model outperforms another.

## Related Papers

No direct paper-to-paper method/result link is recorded here. The review is connected through category and overview pages that map papers onto drug discovery pipeline stages.
