---
id: kang-2022-ai-based-prediction-of-new
domain: drug-discovery
title: "AI-based prediction of new binding site and virtual screening for the discovery of novel P2X3 receptor antagonists"
authors: Koon Mook Kang, Ingoo Lee, Hojung Nam, Yong-Chul Kim
year: 2022
doi: 10.1016/j.ejmech.2022.114556
source: kang-2022-ai-based-prediction-of-new.md
category: binding-sites-virtual-screening
pdf_path: "C:/Users/dlsrnsi/OneDrive/문서/New project/papers/kang-2022-ai-based-prediction-of-new.pdf"
pdf_filename: kang-2022-ai-based-prediction-of-new.pdf
source_collection: external
status: draft
tags: [virtual-screening, binding-sites, hots, p2x3]
---

## Summary

This paper is a prospective-style application of AI-guided binding-site prediction to drug discovery. It uses HoTS to identify candidate binding regions on P2X3R, converts those regions into a putative binding site, builds pharmacophore queries, screens compounds, and tests selected compounds experimentally.

## Key Contributions

- Connects sequence-based interpretability to structure-based screening.
- Uses HoTS binding-region predictions to guide P2X3R cavity and pharmacophore design.
- Compares HoTS interaction prediction with pharmacophore and docking-based screening logic.
- Provides a concrete example of an AI model feeding a hit-identification workflow.

## Materials and Data

- Target sequence: P2X3_HUMAN, UniProt P56373.
- Structures: hP2X3R AF-219/Gefapixant-bound and ATP-bound structures from PDB.
- Library: 150,023 compounds from Korea Chemical Bank.
- Known antagonist set: 18 hP2X3R antagonists for HoTS model selection and binding-region prediction.
- Assay: Fluo-4 calcium influx assay in hP2X3R-expressing HEK293 cells.

## Methods

HoTS was used to predict binding regions on P2X3R. The model suggested three clusters: a known antagonist-site cluster, an ion-channel vestibule/gate cluster, and a novel intersubunit cavity between the head and upper-body domains. The novel cavity was evaluated by short MD simulations of closed/open receptor states, then used for CDOCKER docking of BLU-5937 derivatives.

BLU-2's predicted receptor-ligand interactions seeded pharmacophore generation. Eleven features were generated, twenty pharmacophore queries were tested, and Q12 was chosen using enrichment factor, ROC AUC, and FitValue behavior against 16 active BLU compounds and 800 DUD-E decoys.

Two screening branches were run: a Q12 pharmacophore plus LibDock cascade, and a HoTS-DTI ranking over KCB using Morgan fingerprints paired with the P2X3 sequence.

## Results

The pharmacophore branch filtered 150,023 KCB compounds to 97,301 by molecular properties, selected 2,346 compounds by Q12 FitValue above 3.2, and sent the top 500 after LibDock rescoring to biological testing. The HoTS branch independently selected 500 compounds from all 150,023 KCB compounds.

The two branches produced 16 total hits: 10 HoTS hits and 6 Pharmacophore-LibDock hits. HoTS-1, HoTS-2, and HoTS-4 shared a 2-chloro-6-morpholinopurinone core and had IC50 values of 3.07-8.72 uM. The authors report roughly a 10-fold higher hit ratio than prior random KCB screening.

Docking analysis supported the novel-site hypothesis: all hits had -CDOCKER interaction energy above 40 kcal/mol, with HoTS-3, HoTS-9, and PD-1 above 60 kcal/mol. Lys113 and Asp76 were frequent polar interaction residues, while Lys65 contributed nonpolar interactions.

## Limitations

The screening workflow is target-specific and depends on the reliability of HoTS-predicted binding regions, docking assumptions, pharmacophore query design, and the KCB compound library. The hits are early antagonists and require follow-up optimization and broader selectivity/safety validation.

## Related Papers

- [[drug-discovery/drug-target-interactions/lee-2022-sequence-based-prediction-of-protein]] - Method connection: this paper uses HoTS binding-region/DTI outputs as the starting point for P2X3R cavity selection and virtual screening.
