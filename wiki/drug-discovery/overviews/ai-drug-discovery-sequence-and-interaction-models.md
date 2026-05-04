# AI Drug Discovery Sequence and Interaction Models

## Scope

This overview covers the first seven papers added to the wiki. The current collection centers on AI for drug discovery, with a strong thread through drug-target interaction prediction, binding-region interpretability, virtual screening, peptide function prediction, and safety prediction.

## Main Pattern

The collection shows a progression from network-based DTI prediction to sequence-based deep learning, then to explicitly interpretable binding-region models and downstream screening workflows.

1. [[drug-discovery/drug-target-interactions/lee-2018-identification-of-drug-target]] uses random walk with restart on HIPPIE/DrugBank-derived PPI and DDI networks to make topology-weighted DTI features. It improves independent-test AUC over a guilt-by-association baseline.
2. [[drug-discovery/drug-target-interactions/lee-2019-deepconv-dti-prediction-of-drug]] moves toward raw protein sequence modeling with CNNs. It trains on DrugBank/KEGG/IUPHAR DTIs and tests on PubChem and KinaseSARfari.
3. [[drug-discovery/drug-target-interactions/lee-2022-sequence-based-prediction-of-protein]] adds binding-region prediction through HoTS. It pretrains on scPDB/PDBBind binding regions, then fine-tunes DTI prediction on DrugBank/KEGG/IUPHAR.
4. [[drug-discovery/binding-sites-virtual-screening/kang-2022-ai-based-prediction-of-new]] applies HoTS to P2X3R binding-site discovery and virtual screening. It turns sequence-model output into a pharmacophore/docking hypothesis and validates hits experimentally.

## Data and Evaluation Thread

- Network DTI: HIPPIE PPI, DrugBank DDI/DTI, PubChem independent test.
- Sequence DTI: DrugBank, KEGG, IUPHAR, MATADOR validation, PubChem/KinaseSARfari tests.
- Binding-region DTI: scPDB/PDBBind BR pretraining, COACH/HOLO4K BR tests, PubChem DTI tests.
- Virtual screening: KCB library, HoTS-DTI ranking, Q12 pharmacophore screening, LibDock, HEK293 P2X3R calcium assay.

The collection is useful because the evaluation surface gets progressively more realistic: from network and assay benchmark tests, to explicit binding-region validation, to prospective-like compound screening.

## Adjacent Model Families

[[drug-discovery/peptide-function/lee-2022-amp-bert-prediction-of-antimicrobial]] applies transformer modeling to antimicrobial peptide classification. It is not a DTI model, but it shares the same sequence-learning theme: biological sequences can be treated as structured inputs for deep learning, and attention can be used for interpretation.

[[drug-discovery/admet-safety/kim-2022-bayesherg-a-robust-reliable]] covers safety prediction through hERG blocker classification. It broadens the collection from activity prediction to risk prediction, emphasizing uncertainty and interpretability.

AMP-BERT and BayeshERG also show two different meanings of interpretability:

- AMP-BERT uses residue-level attention to recover structural motifs such as disulfide-bond cysteines, alpha-helices, and beta-strands.
- BayeshERG uses graph attention and Bayesian uncertainty to identify substructure-level signals and quantify reliability for safety decisions.

## Main Results Snapshot

- RWR-DTI: independent PubChem AUC 0.675 +/- 0.018 versus 0.628 +/- 0.026 for guilt-by-association.
- DeepConv-DTI: external validation AUPR 0.832 and AUC 0.852; sc-PDB binding-site enrichment significant for 30.3% of entries at 5% cutoff.
- HoTS: BR validation AP 62.28%; COACH top-(n+2) BR success 85.26 +/- 0.8%; DTI validation AUROC 0.8542 and AUPR 0.8232.
- P2X3R screening: 16 hits from two sets of 500 screened compounds, including low micromolar P2X3R antagonists.
- AMP-BERT: external test ACC 0.7604, F1 0.7917, AUROC 0.8183, AUPR 0.7866.
- BayeshERG: external-test balanced performance, ECE 0.064 on Test-all, patch-clamp validation found one strong and three moderate hERG blockers among 12 tested KCB compounds.

## Review Anchor

[[drug-discovery/reviews/kim-2020-artificial-intelligence-in-drug]] provides the broad map: target identification, hit identification, ADMET prediction, lead optimization, and drug repositioning. The other papers can be placed inside that pipeline:

- DTI papers support target and interaction prediction.
- The P2X3R screening paper supports hit identification.
- BayeshERG supports ADMET and safety filtering.
- AMP-BERT supports peptide-based discovery.

## Open Questions for the Wiki

- How do sequence-only models compare with structure-aware models on the same targets?
- When does interpretability improve practical screening decisions rather than only post-hoc explanation?
- Which model outputs are actionable enough to drive wet-lab validation?
- How should uncertainty be represented in hit selection and safety filtering?
