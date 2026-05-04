---
id: kim-2022-bayesherg-a-robust-reliable
domain: drug-discovery
title: "BayeshERG: a robust, reliable and interpretable deep learning model for predicting hERG channel blockers"
authors: Hyunho Kim, Minsu Park, Ingoo Lee, Hojung Nam
year: 2022
doi: 10.1093/bib/bbac211
source: kim-2022-bayesherg-a-robust-reliable.md
category: admet-safety
pdf_path: "C:/Users/dlsrnsi/OneDrive/문서/New project/papers/kim-2022-bayesherg-a-robust-reliable.pdf"
pdf_filename: kim-2022-bayesherg-a-robust-reliable.pdf
source_collection: external
status: draft
tags: [herg, admet, safety, bayesian-deep-learning]
---

## Summary

BayeshERG targets a practical safety problem: small molecules can unintentionally block the hERG ion channel, causing cardiotoxicity risk. The paper proposes a graph-based Bayesian deep learning model for predicting hERG channel blockers with attention to reliability and interpretability.

## Key Contributions

- Treats uncertainty and interpretability as first-class requirements for hERG prediction.
- Uses molecular graph deep learning rather than only descriptor-based modeling.
- Positions reliability as necessary for safety screening, not just a secondary metric.

## Materials and Data

- Pretraining data: 304,045 molecules with hERG inhibition percentage at 10 uM.
- Fine-tuning data: 14,322 molecules, 8,488 positives and 5,834 negatives.
- External test set 1: 30 positives and 14 negatives from Ryu et al.
- External test set 2: FDA-approved drugs from Siramshetty et al., tested under 1 uM and 10 uM thresholds.
- Experimental validation: KCB library, about 130,000 compounds, followed by automated hERG patch-clamp assays in HEK cells.

## Methods

BayeshERG encodes molecular graphs with D-MPNN, pools atom-level information with global multihead attentive pooling, and predicts hERG blockage with an MLP. MC-dropout turns the model into an approximate Bayesian neural network at inference time: multiple stochastic passes produce a mean prediction and an uncertainty estimate.

Training uses transfer learning. The model first learns from a large inhibition-percentage pretraining set, then transfers D-MPNN and GMHAP parameters into the binary blocker/nonblocker fine-tuning task.

## Results

BayeshERG improved both prediction and calibration compared with internal ablations. The transferred proposed model had ECE 0.064 on Test-all and 0.096 on Test-rev, and MCE 0.118 and 0.186. On external test set 1, it was balanced between positives and negatives; the paper highlights SEN 0.833 and SPE 0.857 against DL baselines.

The interpretability analysis found that locally focused attention heads were enriched in positive hERG blocker predictions, while globally focused heads were enriched in negatives. In the prospective validation, 12 high-score and structurally distinct KCB compounds were tested by patch clamp; one strong blocker and three moderate blockers were confirmed.

## Limitations

BayeshERG is focused on hERG blockage, so it does not cover the full ADMET space. Its prospective validation tested a small selected set of compounds, and deployment still requires careful interpretation of uncertainty and assay context.

## Related Papers

No direct paper-to-paper method/result link is recorded yet. This page is currently connected at the category and overview levels as the safety counterpart to activity-focused discovery papers.
