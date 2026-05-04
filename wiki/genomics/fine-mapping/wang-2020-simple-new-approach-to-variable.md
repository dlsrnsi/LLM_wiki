---
id: wang-2020-simple-new-approach-to-variable
domain: genomics
title: "A simple new approach to variable selection in regression, with application to genetic fine mapping"
authors:
  - Gao Wang
  - Abhishek Sarkar
  - Peter Carbonetto
  - Matthew Stephens
year: 2020
doi: 10.1111/rssb.12388
source: wang-2020-simple-new-approach-to-variable.md
category: fine-mapping
pdf_path: /C:/Users/dlsrnsi/OneDrive/문서/New project/papers/wang-2020-simple-new-approach-to-variable.pdf
pdf_filename: wang-2020-simple-new-approach-to-variable.pdf
source_collection: web-open-access
status: draft
tags: [genomics, fine-mapping, susie]
---

## Summary

SuSiE is a sparse regression fine-mapping approach that represents the total effect as a sum of single-effect vectors.

## Key Contributions

- Introduces the sum-of-single-effects model.
- Provides a practical Bayesian fitting procedure.
- Produces posterior inclusion probabilities and credible sets for fine-mapping.

## Materials and Data

The paper targets sparse regression settings where predictors are highly correlated and scientific interpretation depends on which variable is selected. Genetic fine-mapping is the main application: predictors are nearby variants in LD, the response is a molecular or organismal trait, and the goal is to identify credible sets of candidate causal variants rather than only maximize prediction accuracy.

The paper uses several types of evidence:

- toy regression examples showing why selecting one variable from a highly correlated group can be misleading;
- simulations designed to mimic realistic genetic fine-mapping studies;
- comparisons with existing variable-selection and fine-mapping methods;
- an application to fine-mapping genetic variants influencing alternative splicing in human cell lines.

The key data condition is high correlation among candidate variables. In this regime, a method should be able to say "one of these correlated variables is likely causal" rather than arbitrarily selecting one and hiding uncertainty.

## Methods

SuSiE, short for Sum of Single Effects, rewrites sparse regression as a sum of simple one-effect regression components. The mathematical design goal is to represent several causal signals while keeping each signal interpretable as a probability distribution over candidate variables.

### Regression setup

SuSiE starts from the standard Gaussian linear model:

$$
y = Xb + e,\qquad e\sim N_n(0,\sigma^2I_n)
$$

where:

- \(y\in\mathbb{R}^n\): phenotype or response vector
- \(X\in\mathbb{R}^{n\times p}\): genotype/predictor matrix
- \(b\in\mathbb{R}^p\): sparse coefficient vector
- \(e\): Gaussian residual noise

In genetic fine-mapping, columns of \(X\) are variants in a locus, and correlations among columns represent LD. The inferential target is not only a point estimate of \(b\), but uncertainty over which variables carry non-zero effects.

### Single-effect regression

The building block is a single-effect regression model. It assumes that exactly one variable has a non-zero effect:

$$
y = Xb + e
$$

with:

$$
b = \gamma\theta
$$

where:

- \(\gamma=(\gamma_1,\ldots,\gamma_p)\) is a one-hot vector
- \(\gamma\sim\operatorname{Mult}(1,\pi)\)
- \(\theta\sim N(0,\sigma_0^2)\)

If \(\gamma_j=1\), then variable \(j\) is the one selected variable and:

$$
b_j=\theta,\qquad b_{j'}=0\ \text{for}\ j'\neq j
$$

The posterior under this single-effect model has:

$$
\gamma\mid X,y,\sigma^2,\sigma_0^2
\sim \operatorname{Mult}(1,\alpha)
$$

where:

$$
\alpha_j=\Pr(\gamma_j=1\mid X,y,\sigma^2,\sigma_0^2)
$$

is the posterior inclusion probability for variable \(j\) in the one-effect model. Conditional on variable \(j\) being selected:

$$
\theta\mid \gamma_j=1,X,y,\sigma^2,\sigma_0^2
\sim N(\mu_{1j},\sigma_{1j}^2)
$$

The paper summarizes this fitting operation as:

$$
\operatorname{SER}(X,y;\sigma^2,\sigma_0^2)
=
(\alpha,\mu_1,\sigma_1^2)
$$

### Sum-of-single-effects model

SuSiE generalizes the one-effect model by summing \(L\) single-effect vectors:

$$
b=\sum_{\ell=1}^{L}b_\ell
$$

Each component \(b_\ell\) is itself a single-effect vector:

$$
b_\ell=\gamma_\ell\theta_\ell
$$

with:

$$
\gamma_\ell\sim\operatorname{Mult}(1,\pi),\qquad
\theta_\ell\sim N(0,\sigma_{0\ell}^2)
$$

The full model is:

$$
y = X\sum_{\ell=1}^{L}b_\ell + e,\qquad
e\sim N_n(0,\sigma^2I_n)
$$

This lets the model represent up to \(L\) non-zero effects, while each component remains interpretable as one putative signal. In fine-mapping language, each component can correspond to one causal signal, and the probability vector \(\alpha_\ell\) distributes that signal across correlated variants.

### Variational approximation and IBSS

The exact posterior over all \(L\) single-effect vectors is difficult because the components interact through the shared residual. SuSiE uses a factorized variational approximation:

$$
q(b_1,\ldots,b_L)=\prod_{\ell=1}^{L}q_\ell(b_\ell)
$$

Each factor \(q_\ell\) is updated as a single-effect regression fit to the residual left after subtracting the expected contribution of all other effects. For component \(\ell\), define:

$$
r_\ell
=
y-\sum_{\ell'\neq \ell}X\,\mathbb{E}_q[b_{\ell'}]
$$

Then update:

$$
q_\ell
\leftarrow
\operatorname{SER}(X,r_\ell;\sigma^2,\sigma_{0\ell}^2)
$$

This coordinate-ascent algorithm is Iterative Bayesian Stepwise Selection. One pass updates \(\ell=1,\ldots,L\); repeated passes continue until the variational objective stabilizes.

For each component and variable:

$$
\mathbb{E}_q[(b_\ell)_j]=\alpha_{\ell j}\mu_{\ell j}
$$

so the posterior mean of the full regression coefficient is:

$$
\bar{b}_j
=
\sum_{\ell=1}^{L}\alpha_{\ell j}\mu_{\ell j}
$$

### Posterior inclusion probabilities and credible sets

Because the variational posterior factorizes across effects, the probability that variable \(j\) is not selected by any component is:

$$
\prod_{\ell=1}^{L}(1-\alpha_{\ell j})
$$

Therefore SuSiE's variable-level posterior inclusion probability is:

$$
\operatorname{PIP}_j
=
1-\prod_{\ell=1}^{L}(1-\alpha_{\ell j})
$$

For a component \(\ell\), SuSiE constructs a credible set by sorting variables by \(\alpha_{\ell j}\) and taking the smallest set \(S_\ell\) whose cumulative posterior mass reaches a target level \(\rho\):

$$
\sum_{j\in S_\ell}\alpha_{\ell j}\geq \rho
$$

In fine-mapping, this credible set is interpreted as a set of variants likely to contain the causal variant for that signal. The method often evaluates credible-set purity using correlations among variables, because a credible set that mixes weakly correlated variants may be less biologically coherent.

### Methodological contrast with FINEMAP

SuSiE does not enumerate full causal configurations. Instead, it decomposes the regression problem into \(L\) probabilistic single-effect components and fits them by iterative residual updates. FINEMAP directly searches the posterior over binary causal configurations; SuSiE approximates the multi-effect posterior through a structured variational family.

## Results

The paper reports that SuSiE produces interpretable credible sets and performs well in fine-mapping-like settings with sparse effects and highly correlated predictors.

Key results and claims:

- SuSiE directly reports one credible set per inferred effect component, making uncertainty easier to interpret than a raw posterior over many models.
- IBSS has the simplicity of stepwise selection but returns a distribution over variables at each step rather than a single selected variable.
- Simulations designed to mimic genetic fine-mapping show improved performance over existing approaches for identifying effect variables and producing useful credible sets.
- In the alternative-splicing application, SuSiE is used to fine-map genetic variants influencing splicing in human cell lines, illustrating the method on real molecular trait data.
- The method is especially useful when multiple correlated variants compete to explain the same association signal.

In GLFM, SuSiE functions as a statistical fine-mapping baseline: it uses association/regression structure to handle LD, while GLFM attempts to use learned genotype context and perturbation behavior to improve causal prioritization.

## Limitations

SuSiE does not learn sequence representations or use transformer-style contextual modeling. It addresses LD through statistical regression structure rather than learned attention.

The model assumes that the total sparse effect can be well approximated by at most \(L\) single-effect components. If \(L\) is too small, some signals may be missed; if \(L\) is too large, extra components need to be pruned or interpreted carefully. The variational posterior is also an approximation, so it trades exact Bayesian model averaging for deterministic scalability and interpretable credible sets.

## Related Papers

- [[lee-2026-genomic-language-based-finemapping]] - Method/result connection: GLFM compares against SuSiE and tries to recover causal variants that are masked by LD proxy compensation.
- [[benner-2016-finemap-efficient-variable-selection]] - Method connection: both are statistical fine-mapping baselines for causal SNP inference.
