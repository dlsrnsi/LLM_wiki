# Drug-Target Interactions

- [[lee-2018-identification-of-drug-target]] - Random walk with restart on an interactome network for DTI prediction.
- [[lee-2019-deepconv-dti-prediction-of-drug]] - CNN model over raw protein sequences for DTI prediction.
- [[lee-2022-sequence-based-prediction-of-protein]] - HoTS model for binding-region and DTI prediction.

## Comparative Summary

These three papers form the main methodological progression in the current drug discovery wiki. [[lee-2018-identification-of-drug-target]] starts from graph topology: it uses PPI/DDI networks and random walk with restart to make hand-crafted drug/protein features topology-aware. [[lee-2019-deepconv-dti-prediction-of-drug]] shifts the representation problem to deep learning by replacing protein descriptors with CNN-learned local sequence motifs. [[lee-2022-sequence-based-prediction-of-protein]] extends that sequence-modeling line by explicitly training binding-region prediction before DTI prediction.

The key difference is what each model treats as the important evidence. The 2018 RWR model trusts network neighborhood structure. DeepConv-DTI trusts local sequence motifs discovered by convolution. HoTS trusts binding-region supervision and transformer attention over protein grids. As a result, HoTS is the most directly connected to downstream virtual screening because it can suggest where a compound may bind, not just whether a DTI exists.

## Comparison Table

| Paper | Main input | Core method | Output | Best use |
|---|---|---|---|---|
| [[lee-2018-identification-of-drug-target]] | Drug/protein descriptors plus PPI/DDI topology | RWR-weighted features + cubic kNN | DTI score | Network-informed DTI prediction, including new drugs/targets with features |
| [[lee-2019-deepconv-dti-prediction-of-drug]] | Raw protein sequence + Morgan fingerprints | CNN motif extraction + dense DTI classifier | DTI probability | Broad sequence-based DTI prediction across protein classes |
| [[lee-2022-sequence-based-prediction-of-protein]] | Protein sequence grids + compound fingerprints | BR pretraining + transformer attention | Binding regions and DTI probability | Interpretable DTI prediction and screening handoff |

## Links Across Categories

- [[drug-discovery/binding-sites-virtual-screening/kang-2022-ai-based-prediction-of-new]] applies HoTS to P2X3R hit discovery.
- [[drug-discovery/reviews/kim-2020-artificial-intelligence-in-drug]] provides the broader drug discovery pipeline context.
