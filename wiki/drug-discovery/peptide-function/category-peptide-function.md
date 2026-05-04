# Peptide Function

- [[lee-2022-amp-bert-prediction-of-antimicrobial]] - BERT-based antimicrobial peptide classification.

## Comparative Summary

This category currently has one peptide-focused paper. [[lee-2022-amp-bert-prediction-of-antimicrobial]] is adjacent to the small-molecule DTI papers, but its input and discovery object are different: it classifies peptide sequences as antimicrobial or non-antimicrobial using a protein language model.

Compared with [[drug-discovery/drug-target-interactions/lee-2019-deepconv-dti-prediction-of-drug]], AMP-BERT uses transformer pretraining rather than training sequence motifs mostly from task-specific DTI labels. Compared with [[drug-discovery/drug-target-interactions/lee-2022-sequence-based-prediction-of-protein]], its attention analysis is about peptide structural motifs such as disulfide-bond cysteines, alpha-helices, and beta-strands, rather than ligand binding regions on target proteins.

## Comparison With Sequence Models

| Paper | Sequence object | Model style | Interpretability target |
|---|---|---|---|
| [[drug-discovery/drug-target-interactions/lee-2019-deepconv-dti-prediction-of-drug]] | Target protein sequence | CNN over residue windows | Local motifs and binding-site enrichment |
| [[drug-discovery/drug-target-interactions/lee-2022-sequence-based-prediction-of-protein]] | Target protein sequence grids | CNN + transformer + BR supervision | Binding regions for ligand interaction |
| [[lee-2022-amp-bert-prediction-of-antimicrobial]] | Peptide sequence | ProtBERT-BFD fine-tuning | AMP structural motifs and residue attention |

## Main Takeaway

AMP-BERT shows how the same broad idea, biological sequences as language-like inputs, can support peptide drug discovery rather than small-molecule target interaction prediction.
