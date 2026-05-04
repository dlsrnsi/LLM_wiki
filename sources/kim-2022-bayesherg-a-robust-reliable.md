---
id: kim-2022-bayesherg-a-robust-reliable
domain: drug-discovery
title: "BayeshERG: a robust, reliable and interpretable deep learning model for predicting hERG channel blockers"
authors: Hyunho Kim, Minsu Park, Ingoo Lee, Hojung Nam
year: 2022
doi: 10.1093/bib/bbac211
category: admet-safety
pdf_path: "C:/Users/dlsrnsi/OneDrive/문서/New project/papers/kim-2022-bayesherg-a-robust-reliable.pdf"
pdf_filename: kim-2022-bayesherg-a-robust-reliable.pdf
source_collection: external
status: draft
---

## One-line Summary

BayeshERG is a graph-based Bayesian deep learning model designed to predict hERG channel blockers while improving robustness, reliability, and interpretability.

## 1. Document Information

Published in Briefings in Bioinformatics in 2022. The paper addresses cardiotoxicity risk caused by unintended hERG channel inhibition.

## 2. Key Contributions

- Frames hERG blockage prediction as a safety-critical drug development problem.
- Proposes a Bayesian graph deep learning approach for small-molecule hERG blocker prediction.
- Emphasizes uncertainty, reliability, and interpretability rather than only classification accuracy.
- Positions interpretability as important for practical use in drug safety assessment.

## 3. Methodology and Architecture

### Materials and Datasets

- Pretraining set: 304,045 molecules with hERG inhibition percentage at 10 uM after filtering inorganic molecules, label-inconsistent molecules, and molecules duplicated in the fine-tuning set.
- Fine-tuning set: 14,322 molecules, including 8,488 positives and 5,834 negatives. Literature-derived IC50 data were cleaned by SMILES duplicates; compounds with pIC50 >= 5 were labeled positive.
- External test set 1: 44 molecules from Ryu et al., with 30 positives and 14 negatives using an IC50 threshold of 10 uM.
- External test set 2: FDA-approved drugs from Siramshetty et al., evaluated at both 1 uM and 10 uM thresholds after removing molecules unsuitable for fair comparison.
- Experimental validation library: Korea Chemical Bank, about 130,000 compounds.

### Model Architecture

BayeshERG is a graph neural network with three main components:

1. Directed message passing neural network (D-MPNN) encodes molecular graphs by updating edge hidden states and aggregating them into atom representations.
2. Global multihead attentive pooling (GMHAP) adds a dummy global node connected to all atoms, applies multihead self-attention, and extracts the updated global node as the molecule representation.
3. A multilayer perceptron predicts hERG blocking probability.

The Bayesian layer is implemented with MC-dropout. Dropout remains active at test time, producing multiple prediction samples. The mean prediction is used as the calibrated output, and predictive variance estimates uncertainty. The authors distinguish epistemic uncertainty, which should shrink with more training data, from aleatoric uncertainty, which reflects irreducible data noise.

### Training Procedure

- Pretraining used scaffold splitting at a 9:1 train/validation ratio and optimized mean absolute error on inhibition percentage.
- Fine-tuning transferred D-MPNN and GMHAP parameters from the pretrained model.
- Fine-tuning used scaffold splitting at 8:1:1 for train/validation/test and optimized cross-entropy.
- Baselines included RF, SVM, D-MPNN variants with or without MC-dropout, GMHAP, and transfer learning.

### Evaluation

Prediction metrics included ACC, BAC, MCC, F1, SEN, SPE, NPV, PPV, AUC, and AUPR. Calibration metrics included expected calibration error (ECE) and maximum calibration error (MCE). External comparison covered ML-based and DL-based public hERG predictors.

## 4. Key Results and Benchmarks

### Internal Performance

- Adding GMHAP, MC-dropout, and transfer learning improved graph-based model performance.
- Conventional ML baselines were competitive on the easier scaffold-split test-all set but degraded on the stricter test-rev set, suggesting memorization of similar scaffolds.
- BayeshERG had the best calibration behavior among compared internal variants.
- Reported calibration values for the proposed transferred BayeshERG were ECE 0.064 on Test-all and 0.096 on Test-rev, with MCE 0.118 and 0.186.

### External Performance

- On external test set 1, BayeshERG had balanced SEN and SPE compared with models that were biased toward one class.
- Compared with DL baselines, BayeshERG achieved the best performance in all main metrics on external test set 1; the paper highlights SEN 0.833 and SPE 0.857.
- On external test set 2, BayeshERG remained high-ranking at both 10 uM and 1 uM thresholds, indicating robustness to threshold changes.
- Additional external tests from Karim et al. showed BayeshERG with the lowest rank sum in one dataset and second-lowest in another.

### Interpretability and Experimental Validation

- Attention analysis sampled 1,000 true positives and 1,000 true negatives from the fine-tuning set.
- Some attention heads behaved locally and others globally; locally focused heads were enriched in positive hERG blocker samples, whereas globally focused heads were enriched in negative samples.
- KCB screening selected compounds with BayeshERG score > 0.95 and structural distinctness from known positives.
- Patch-clamp validation of 12 selected compounds identified one strong hERG blocker (IC50 < 1 uM) and three moderate blockers (1 uM < IC50 < 10 uM).
- The strong blocker was reportedly missed as a nonblocker by most public prediction tools.

## 5. Limitations and Future Work

The paper focuses on a specific safety endpoint, hERG blockage. Generalization to broader ADMET endpoints requires separate validation. In deployment, high-confidence incorrect predictions would be especially important to audit.

## 6. Related Work

- [[drug-discovery/reviews/kim-2020-artificial-intelligence-in-drug]] - Broad review context for ADMET prediction in AI drug discovery.

## 7. Glossary

- hERG: Human ether-a-go-go-related gene ion channel; unintended blockage can cause cardiotoxicity.
- ADMET: Absorption, distribution, metabolism, excretion, and toxicity.
- Bayesian deep learning: Deep learning that models predictive uncertainty.
