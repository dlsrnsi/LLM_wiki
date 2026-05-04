---
id: benner-2016-finemap-efficient-variable-selection
domain: genomics
title: "FINEMAP, efficient variable selection using summary data from genome-wide association studies"
authors:
  - Christian Benner
  - Chris C. A. Spencer
  - Aki S. Havulinna
  - Veikko Salomaa
  - Samuli Ripatti
  - Matti Pirinen
year: 2016
doi: 10.1093/bioinformatics/btw018
source: benner-2016-finemap-efficient-variable-selection.md
category: fine-mapping
pdf_path: /C:/Users/dlsrnsi/OneDrive/문서/New project/papers/benner-2016-finemap-efficient-variable-selection.pdf
pdf_filename: benner-2016-finemap-efficient-variable-selection.pdf
source_collection: web-open-access
status: draft
tags: [genomics, fine-mapping, gwas]
---

## Summary

FINEMAP is a Bayesian fine-mapping method for identifying likely causal variants from GWAS summary statistics and LD information.

## Key Contributions

- Frames causal variant fine-mapping as Bayesian variable selection.
- Uses shotgun stochastic search to focus on high-posterior causal configurations.
- Outputs posterior probabilities for causal configurations and SNP-level inclusion.

## Materials and Data

The method is designed for GWAS summary statistics plus an LD correlation matrix estimated from either the study data or a reference panel. The required inputs are:

- single-SNP association \(z\)-scores from standard GWAS software;
- an LD matrix \(R\) for SNPs in the region;
- a maximum number of causal SNPs \(K\);
- priors over the number of causal variants and effect-size variance.

The paper evaluates FINEMAP using both simulated and real-data settings. The simulation setup uses genotype data from 18,834 individuals in the Finnish FINRISK study. The authors focus on a 500 kb region centered on rs11591147 in the PCSK9 gene on chromosome 1, containing 1,920 polymorphic SNPs after filtering SNP pairs with absolute correlation at least 0.99.

Two main simulation scenarios are used:

- Scenario A varies the number of SNPs, using \(m=750,1000,1250,1500\), and evaluates configurations with up to \(K=3\) or \(K=5\) causal SNPs.
- Scenario B fixes \(m=150\) and varies the maximum number of causal SNPs, \(K=1,2,3,4,5\).

The generated data deliberately include causal SNPs with correlated proxies, because high LD is where incomplete search or greedy conditioning can fail. The paper also analyzes summary statistics from a Parkinson's disease GWAS, making the evaluation relevant to both quantitative-trait and disease-association settings.

## Methods

FINEMAP evaluates causal SNP configurations under a Bayesian regression model using GWAS summary statistics and an LD matrix. Its main mathematical object is a binary causal-configuration vector.

### Regression and summary-statistic setup

Let:

- \(y \in \mathbb{R}^n\): centered phenotype vector
- \(X \in \mathbb{R}^{n \times m}\): genotype matrix for \(m\) SNPs, with columns standardized
- \(\beta \in \mathbb{R}^m\): SNP effect vector
- \(\epsilon \sim N(0, \sigma^2 I_n)\): residual noise

The underlying regression model is:

$$
y = X\beta + \epsilon,\qquad \epsilon \sim N(0,\sigma^2 I_n)
$$

FINEMAP is designed for the setting where individual-level \(X\) and \(y\) may not be available. Instead, it uses:

$$
R = n^{-1}X^\top X
$$

as the LD correlation matrix and a vector of standardized association statistics:

$$
\hat{z} \approx n^{1/2}\sigma^{-1}X^\top y
$$

For a candidate causal subset, the maximum-likelihood regression effects can be expressed through \(R\) and \(\hat{z}\). In the full-rank linear-model form:

$$
\hat{\beta} = (X^\top X)^{-1}X^\top y
            = n^{-1/2}\sigma R^{-1}\hat{z}
$$

and:

$$
\operatorname{Var}(\hat{\beta})=\sigma^2(X^\top X)^{-1}
                                = n^{-1}\sigma^2R^{-1}
$$

This is why FINEMAP can work from summary statistics: the likelihood can be rewritten using \(\hat{z}\) and the LD matrix rather than requiring raw genotypes for every computation.

### Causal-configuration prior

FINEMAP represents a model by a binary vector:

$$
c=(c_1,\ldots,c_m),\qquad c_j \in \{0,1\}
$$

where \(c_j=1\) means SNP \(j\) is included as causal. If:

$$
k=\sum_{j=1}^{m} c_j
$$

then \(k\) is the number of causal SNPs in that configuration. FINEMAP places a prior \(p_k\) on the number of causal SNPs and distributes that mass uniformly across configurations of the same size:

$$
p(c)=\frac{p_k}{\binom{m}{k}}
\quad\text{when}\quad
\sum_{j=1}^{m}c_j=k
$$

The effect-size prior is a Gaussian spike-and-slab style prior in which only selected SNPs receive non-zero prior variance:

$$
p(\beta\mid c)=N\left(\beta\mid 0,\;s_\beta^2\sigma^2D_c\right)
$$

where \(D_c\) is a diagonal matrix with \(c_j\) on the diagonal. If \(c_j=0\), the corresponding effect is fixed at zero through zero prior variance; if \(c_j=1\), the SNP can carry an effect with variance scaled by \(s_\beta^2\sigma^2\).

### Marginal likelihood and Bayes factor

For each configuration, FINEMAP integrates over effect sizes:

$$
p(y\mid c,X)=\int p(y\mid \beta,X)p(\beta\mid c)\,d\beta
$$

In summary-statistic form, this is evaluated through the distribution of \(\hat{z}\). If \(C=\{j:c_j=1\}\) is the selected causal set and \(R_{CC}\) is the LD submatrix for those SNPs, FINEMAP can compute a Bayes factor for configuration \(c\) against the null model using only the causal subset:

$$
\operatorname{BF}(c:\mathrm{NULL})
=
\frac{
N\left(\hat{z}_C\mid 0,\;R_{CC}+n s_\beta^2 R_{CC}R_{CC}\right)
}{
N\left(\hat{z}_C\mid 0,\;R_{CC}\right)
}
$$

The key computational point is that the expensive matrix operations scale with the number of selected causal SNPs \(k=|C|\), not the full regional SNP count \(m\). This makes the computation practical when \(m\) is large but the assumed number of causal SNPs is small.

The unnormalized posterior weight for a configuration is:

$$
p^\*(c\mid y,X)
=
\frac{p_k}{\binom{m}{k}}
\operatorname{BF}(c:\mathrm{NULL})
$$

After FINEMAP has collected a set of evaluated configurations \(\mathcal{C}^\*\), it normalizes:

$$
p(c\mid y,X)
=
\frac{p^\*(c\mid y,X)}
{\sum_{c'\in\mathcal{C}^\*}p^\*(c'\mid y,X)}
$$

### SNP-level posterior inclusion

The posterior inclusion probability for SNP \(j\) is obtained by summing over all evaluated configurations that include that SNP:

$$
\Pr(c_j=1\mid y,X)
=
\sum_{c\in\mathcal{C}^\*}
\mathbf{1}(c_j=1)p(c\mid y,X)
$$

FINEMAP can also report a SNP-level Bayes factor by comparing posterior odds to prior odds:

$$
\operatorname{BF}(c_j=1:c_j=0)
=
\frac{\Pr(c_j=1\mid y,X)/\Pr(c_j=0\mid y,X)}
{\Pr(c_j=1)/\Pr(c_j=0)}
$$

with prior inclusion probability:

$$
\Pr(c_j=1)=\sum_{k=1}^{K}\frac{k}{m}p_k
$$

### Shotgun stochastic search

Exhaustively scoring every causal configuration is infeasible because the number of possible subsets grows combinatorially:

$$
\sum_{k=0}^{K}\binom{m}{k}
$$

FINEMAP therefore uses shotgun stochastic search. Starting from a current configuration, it constructs neighboring configurations by:

- adding one causal SNP,
- deleting one causal SNP,
- or swapping one currently causal SNP for one currently non-causal SNP.

These neighbors are scored by their posterior weights, and the search moves toward configurations with high posterior support. The output is therefore not just a ranked SNP list; it is a posterior distribution over multi-SNP causal explanations, plus SNP-level inclusion probabilities derived from that distribution.

## Results

The paper's main empirical result is that most causal configurations have negligible posterior probability, so FINEMAP can approximate the posterior accurately by searching high-probability regions rather than enumerating all possible SNP subsets.

Key reported findings:

- FINEMAP is reported to be thousands of times faster than CAVIARBF in settings where CAVIARBF can still be run.
- When exhaustive methods must restrict the number of allowed causal variants for computational reasons, FINEMAP can be more accurate because it can search larger configuration spaces.
- In simulations with hundreds to thousands of SNPs and multiple causal variants, a relatively small list of high-posterior configurations can account for most posterior mass.
- FINEMAP returns both configuration-level posterior probabilities and SNP-level posterior inclusion probabilities, which makes it more informative than stepwise conditional analysis.
- The Parkinson's disease example demonstrates use on disease GWAS summary statistics rather than only simulated quantitative traits.

The computational result is the central contribution: the Bayesian model is similar in spirit to summary-statistic fine-mapping approaches such as CAVIARBF, but the shotgun stochastic search changes the feasible scale of inference.

## Limitations

FINEMAP depends on association statistics and LD quality. If the LD reference panel poorly matches the GWAS cohort, posterior probabilities can be distorted.

The method also assumes that causal signal can be represented by a sparse set of SNP effects in the analyzed region. Near-perfect collinearity can make the causal-subset LD matrix unstable, so the implementation includes handling for highly correlated SNP pairs. FINEMAP does not learn genotype-sequence representations, does not use regulatory sequence context, and does not model causal evidence through representation perturbations.

## Related Papers

- [[lee-2026-genomic-language-based-finemapping]] - Method/result connection: GLFM uses FINEMAP as a baseline and attempts to improve retrieval in high-LD regimes by modeling genotype context.
- [[wang-2020-simple-new-approach-to-variable]] - Method connection: both are statistical fine-mapping methods using regression/LD structure to infer causal variants.
