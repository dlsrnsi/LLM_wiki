---
id: wang-2020-simple-new-approach-to-variable
domain: genomics
title: "A simple new approach to variable selection in regression, with application to genetic fine mapping"
authors: Gao Wang; Abhishek Sarkar; Peter Carbonetto; Matthew Stephens
year: 2020
doi: 10.1111/rssb.12388
category: fine-mapping
pdf_path: /C:/Users/dlsrnsi/OneDrive/문서/New project/papers/wang-2020-simple-new-approach-to-variable.pdf
pdf_filename: wang-2020-simple-new-approach-to-variable.pdf
source_collection: web-open-access
status: draft
---

## One-line Summary

SuSiE models sparse regression coefficients as a sum of single-effect vectors, producing credible sets for genetic fine-mapping.

## Key Contributions

- Introduces the sum-of-single-effects model.
- Provides an iterative Bayesian stepwise selection style fitting procedure.
- Produces posterior inclusion probabilities and credible sets that are interpretable for fine-mapping.

## Methodology and Architecture

SuSiE decomposes a sparse regression coefficient vector into a sum of single-effect components. It begins with the Gaussian regression model:

$$
y=Xb+e,\qquad e\sim N_n(0,\sigma^2I_n)
$$

where \(X\) is the predictor/genotype matrix and \(b\) is sparse.

The single-effect regression model assumes exactly one variable has a non-zero effect:

$$
b=\gamma\theta
$$

where \(\gamma\) is a one-hot vector, \(\gamma\sim\operatorname{Mult}(1,\pi)\), and \(\theta\sim N(0,\sigma_0^2)\). Its posterior has:

$$
\gamma\mid X,y,\sigma^2,\sigma_0^2\sim\operatorname{Mult}(1,\alpha)
$$

with:

$$
\alpha_j=\Pr(\gamma_j=1\mid X,y,\sigma^2,\sigma_0^2)
$$

and conditional effect posterior:

$$
\theta\mid \gamma_j=1,X,y,\sigma^2,\sigma_0^2
\sim N(\mu_{1j},\sigma_{1j}^2)
$$

SuSiE generalizes this to \(L\) effects:

$$
b=\sum_{\ell=1}^{L}b_\ell,\qquad
b_\ell=\gamma_\ell\theta_\ell
$$

with:

$$
\gamma_\ell\sim\operatorname{Mult}(1,\pi),\qquad
\theta_\ell\sim N(0,\sigma_{0\ell}^2)
$$

The full model is therefore:

$$
y=X\sum_{\ell=1}^{L}b_\ell+e
$$

Exact posterior inference is replaced by a factorized variational approximation:

$$
q(b_1,\ldots,b_L)=\prod_{\ell=1}^{L}q_\ell(b_\ell)
$$

The Iterative Bayesian Stepwise Selection update fits one component at a time. For effect \(\ell\), compute the residual after removing the expected contribution of all other effects:

$$
r_\ell=y-\sum_{\ell'\neq\ell}X\mathbb{E}_q[b_{\ell'}]
$$

Then refit that component as:

$$
q_\ell\leftarrow\operatorname{SER}(X,r_\ell;\sigma^2,\sigma_{0\ell}^2)
$$

The posterior mean coefficient for variable \(j\) is:

$$
\bar{b}_j=\sum_{\ell=1}^{L}\alpha_{\ell j}\mu_{\ell j}
$$

and the variable-level posterior inclusion probability is:

$$
\operatorname{PIP}_j=1-\prod_{\ell=1}^{L}(1-\alpha_{\ell j})
$$

For each component \(\ell\), a credible set \(S_\ell\) is formed by taking the smallest high-probability set of variables whose posterior mass reaches level \(\rho\):

$$
\sum_{j\in S_\ell}\alpha_{\ell j}\geq\rho
$$

This makes SuSiE different from configuration-search methods such as FINEMAP: it approximates multi-effect sparse regression through probabilistic single-effect components rather than enumerating binary causal configurations.

## Key Results and Benchmarks

The paper positions SuSiE as scalable, interpretable, and effective for genetic fine-mapping. GLFM uses SuSiE as an association-based baseline.

The paper reports that SuSiE performs well in simulations designed to mimic realistic fine-mapping with sparse effects and highly correlated predictors. It produces credible sets that summarize uncertainty in which variable should be selected, rather than only reporting a single best variable. The paper also demonstrates application to fine-mapping genetic variants influencing alternative splicing in human cell lines.

The most important result for this wiki is interpretability: each single-effect component yields a credible set for one putative signal, and variable-level posterior inclusion probabilities combine evidence across components.

## Limitations and Future Work

SuSiE is a statistical fine-mapping model rather than a sequence representation learner. It does not model genotype loci as language-like sequences. It assumes the sparse effect vector can be approximated by at most \(L\) single-effect components, and its posterior inference is variational rather than exact model enumeration.
