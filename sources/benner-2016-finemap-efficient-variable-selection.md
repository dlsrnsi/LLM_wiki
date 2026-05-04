---
id: benner-2016-finemap-efficient-variable-selection
domain: genomics
title: "FINEMAP, efficient variable selection using summary data from genome-wide association studies"
authors: Christian Benner; Chris C. A. Spencer; Aki S. Havulinna; Veikko Salomaa; Samuli Ripatti; Matti Pirinen
year: 2016
doi: 10.1093/bioinformatics/btw018
category: fine-mapping
pdf_path: /C:/Users/dlsrnsi/OneDrive/문서/New project/papers/benner-2016-finemap-efficient-variable-selection.pdf
pdf_filename: benner-2016-finemap-efficient-variable-selection.pdf
source_collection: web-open-access
status: draft
---

## One-line Summary

FINEMAP performs Bayesian fine-mapping from GWAS summary statistics by efficiently searching high-posterior causal SNP configurations.

## Key Contributions

- Frames fine-mapping as a high-dimensional variable selection problem.
- Uses shotgun stochastic search to avoid exhaustive enumeration over all causal configurations.
- Produces posterior probabilities over causal configurations and SNP-level posterior inclusion probabilities.

## Methodology and Architecture

FINEMAP uses summary association statistics and an LD correlation matrix to evaluate candidate causal configurations under a Bayesian regression model.

The base model is:

$$
y=X\beta+\epsilon,\qquad \epsilon\sim N(0,\sigma^2I_n)
$$

where \(X\) is a standardized genotype matrix and \(y\) is a centered phenotype. FINEMAP replaces repeated individual-level likelihood calculations with summary-statistic quantities:

$$
R=n^{-1}X^\top X,\qquad
\hat{z}\approx n^{1/2}\sigma^{-1}X^\top y
$$

Here \(R\) is the LD matrix and \(\hat{z}\) is the vector of standardized SNP association statistics. In the full-rank model:

$$
\hat{\beta}=n^{-1/2}\sigma R^{-1}\hat{z},
\qquad
\operatorname{Var}(\hat{\beta})=n^{-1}\sigma^2R^{-1}
$$

A causal model is encoded by:

$$
c=(c_1,\ldots,c_m),\qquad c_j\in\{0,1\}
$$

with \(c_j=1\) indicating that SNP \(j\) is causal. If \(k=\sum_j c_j\), FINEMAP assigns:

$$
p(c)=\frac{p_k}{\binom{m}{k}}
$$

so the prior mass \(p_k\) over models with \(k\) causal SNPs is spread uniformly across all size-\(k\) configurations. Effect sizes use:

$$
p(\beta\mid c)=N(\beta\mid0,s_\beta^2\sigma^2D_c)
$$

where \(D_c\) has \(c_j\) on its diagonal.

For a selected causal set \(C\), the model integrates over \(\beta\) and computes a Bayes factor against the null using the causal-subset LD matrix \(R_{CC}\):

$$
\operatorname{BF}(c:\mathrm{NULL})
=
\frac{
N(\hat{z}_C\mid0,R_{CC}+ns_\beta^2R_{CC}R_{CC})
}{
N(\hat{z}_C\mid0,R_{CC})
}
$$

The unnormalized posterior is:

$$
p^\*(c\mid y,X)=\frac{p_k}{\binom{m}{k}}\operatorname{BF}(c:\mathrm{NULL})
$$

and normalization is performed over the set of configurations actually evaluated by the search. SNP-level posterior inclusion probabilities are obtained by summing posterior mass over all evaluated configurations containing the SNP:

$$
\Pr(c_j=1\mid y,X)=\sum_{c\in\mathcal{C}^\*}\mathbf{1}(c_j=1)p(c\mid y,X)
$$

Because exhaustive enumeration over \(\sum_{k=0}^{K}\binom{m}{k}\) models is infeasible, FINEMAP uses shotgun stochastic search. It proposes neighboring configurations by adding, deleting, or swapping one causal SNP, scores neighbors by posterior weight, and concentrates computation on high-posterior regions.

## Key Results and Benchmarks

The paper reports that in simulated regions with hundreds to thousands of SNPs and multiple causal SNPs, only a small fraction of top configurations can cover most posterior probability, motivating stochastic search. It is a direct statistical baseline for GLFM.

Evaluation uses genotype data from 18,834 FINRISK individuals in a 500 kb PCSK9-region window with 1,920 polymorphic SNPs after filtering near-perfectly correlated pairs. Simulations vary the number of SNPs (\(m=750,1000,1250,1500\)) and the maximum number of causal variants (\(K=3\) or \(K=5\)), and also fix \(m=150\) while varying \(K=1,\ldots,5\). Causal SNPs are chosen to have correlated proxies, stressing the high-LD setting.

The paper reports that FINEMAP is thousands of times faster than CAVIARBF in settings where exhaustive search is feasible, and more accurate when exhaustive methods must restrict the number of causal variants for computational reasons.

## Limitations and Future Work

FINEMAP remains driven by summary association and LD structure. It does not learn sequence-context representations or model hidden representation trajectories. Posterior quality depends on the match between GWAS summary statistics and the LD matrix, and highly collinear SNPs can create instability in causal-subset matrix operations.
