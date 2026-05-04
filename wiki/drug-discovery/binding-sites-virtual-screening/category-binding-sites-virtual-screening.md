# Binding Sites and Virtual Screening

- [[kang-2022-ai-based-prediction-of-new]] - HoTS-guided binding-site prediction and virtual screening for P2X3 receptor antagonists.

## Comparative Summary

This category currently contains one paper, but it is the strongest bridge from model development to drug discovery action. [[kang-2022-ai-based-prediction-of-new]] takes the HoTS model from [[drug-discovery/drug-target-interactions/lee-2022-sequence-based-prediction-of-protein]] and uses its predicted binding regions to propose a novel P2X3R binding cavity. The paper then converts that cavity into a pharmacophore and docking workflow, selects compounds, and validates hits experimentally.

Compared with the DTI-only papers, this work is more translational. It does not stop at ranking drug-target pairs. It asks whether a model-predicted binding region can support virtual screening and wet-lab hit discovery. Compared with [[drug-discovery/admet-safety/kim-2022-bayesherg-a-robust-reliable]], it targets activity discovery rather than safety filtering.

## Position in the Pipeline

| Stage | Related paper | Role |
|---|---|---|
| Binding-region prediction | [[drug-discovery/drug-target-interactions/lee-2022-sequence-based-prediction-of-protein]] | Provides HoTS binding-region and DTI model |
| Virtual screening | [[kang-2022-ai-based-prediction-of-new]] | Uses HoTS, pharmacophore Q12, and LibDock to select compounds |
| Experimental validation | [[kang-2022-ai-based-prediction-of-new]] | Tests selected compounds in hP2X3R HEK293 calcium assay |
| Safety filtering | [[drug-discovery/admet-safety/kim-2022-bayesherg-a-robust-reliable]] | Complementary downstream safety model, not used in this P2X3R paper |

## Main Takeaway

The P2X3R paper is the clearest example in this wiki of an AI model becoming a screening hypothesis: predicted binding regions become a cavity, the cavity becomes a pharmacophore, and the pharmacophore plus HoTS ranking leads to experimentally measured hits.
