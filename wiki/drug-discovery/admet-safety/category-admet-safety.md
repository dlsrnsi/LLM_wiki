# ADMET and Safety

- [[kim-2022-bayesherg-a-robust-reliable]] - Bayesian graph deep learning for hERG blocker prediction.

## Comparative Summary

This category currently has one safety-focused paper. [[kim-2022-bayesherg-a-robust-reliable]] differs from the DTI and virtual screening papers because its goal is not to find active compounds for a target, but to identify compounds likely to create hERG cardiotoxicity risk. In the drug discovery pipeline, it sits after or alongside hit identification as a safety filter.

BayeshERG is methodologically close to the other deep learning papers because it uses learned molecular representations, but it adds two concerns that the activity-prediction papers treat less centrally: uncertainty calibration and substructure-level interpretability. This makes it a useful counterpart to [[drug-discovery/binding-sites-virtual-screening/kang-2022-ai-based-prediction-of-new]], where discovered hits would eventually need safety screening.

## Comparison With Other Categories

| Category | Representative paper | Prediction target | Practical decision |
|---|---|---|---|
| DTI | [[drug-discovery/drug-target-interactions/lee-2022-sequence-based-prediction-of-protein]] | Compound-target interaction and binding regions | Which target-compound pairs are plausible |
| Virtual screening | [[drug-discovery/binding-sites-virtual-screening/kang-2022-ai-based-prediction-of-new]] | P2X3R antagonist candidates | Which compounds to test experimentally |
| ADMET/safety | [[kim-2022-bayesherg-a-robust-reliable]] | hERG blocker probability and uncertainty | Which compounds may be cardiotoxic |

## Main Takeaway

BayeshERG makes the wiki less activity-only. It adds the safety side of drug discovery: a compound can look promising in screening but still be risky if hERG blockage is predicted with high confidence.
