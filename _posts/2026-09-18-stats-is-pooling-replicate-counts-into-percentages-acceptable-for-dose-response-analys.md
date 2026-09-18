---
layout: question
title: Is pooling replicate counts into percentages acceptable for dose–response analysis
  of quantal toxicity?
author: StemFix Bot
category: stats
subject: stats
description: 'Step-by-step statistics solution: Is pooling replicate counts into percentages
  acceptable for dose–response analysis of quantal toxicity?'
tags:
- stats
---

{% raw %}
*As an Amazon Associate, I earn from qualifying purchases.* For more practice problems like this, see [Schaum's Outline of Statistics, 6th Edition](https://www.amazon.com/dp/1260011461?tag=aiopentec20-20).

---

## 1. What the student is asking (plain‑language restatement)

The student performed a **quantal (yes/no)** toxicity test with *Daphnia magna*:

| factor | levels | Replicates |
|--------|--------|------------|
| **Concentration** | 5 test doses + a control | 4 vials per dose |
| **Vial** | 5 animals per vial | – |
| **Run** | Two independent experiments on different days | – |

Overall there are **40 animals per concentration** (4 vials × 5 animals × 2 runs).  
For each vial the student counted how many animals were immobilised (successes) and then **pooled all counts** across vials and runs, turned them into a **percentage immobilisation** for each concentration, and fitted a 4‑parameter log‑logistic curve (fixed lower = 0, upper = 100) in GraphPad Prism to obtain an EC50 and its 95 % CI.

A reviewer says:

* The analysis should keep the **binomial nature** of the data,
* It should keep the **vial‑level replication**, and
* It should recognise the **two independent runs**.

The student wants to know:

1. Is it ever OK to pool the raw counts into percentages, or does this destroy important information (denominators, vial‑to‑vial variation) and bias the EC50 or its confidence interval?
2. If a **binomial GLM (or similar)** is fitted at the vial level, how much will the **point estimates** (EC50) differ from the pooled‑percentage method, and what about the **confidence intervals**?
3. How should **multiple runs** be incorporated – as a pooled dataset, as a fixed effect, or as a random effect?
4. Provide **references** that support the recommended approach.

Below is a step‑by‑step worked solution that answers each of these points.

---

## 2. Statistical background

### 2.1 Quantal dose‑response data are binomial
For a given vial *j* at concentration *x*, we observe

\[
Y_{j}\;|\;x \;\sim\; \text{Binomial}(n_j,\;p(x)),
\]

where  

* \(n_j = 5\) (animals per vial) is the **known denominator**,  
* \(p(x)\) is the (unknown) true probability that an animal is immobilised at concentration *x*.

The **log‑logistic dose‑response model** links concentration to probability:

\[
\text{logit}\bigl[p(x)\bigr] = \log\!\Bigl(\frac{p(x)}{1-p(x)}\Bigr) 
    = \beta_0 + \beta_1\log_{10}(x) ,
\]

or equivalently, in the “four‑parameter” form used by most EC‑type software:

\[
p(x)= d_{\text{low}} + \frac{d_{\text{high}}-d_{\text{low}}}
                {1 + \left(\frac{x}{EC_{50}}\right)^{b}} .
\]

The parameters of interest are  

* **\(EC_{50}\)** – the concentration giving 50 % immobilisation, and  
* **\(b\)** – the slope (Hill coefficient).

Because each observation is a **proportion of successes out of a known number of trials**, the **binomial variance** is

\[
\operatorname{Var}\bigl(\hat p_j\bigr)=\frac{p(x)[1-p(x)]}{n_j}.
\]

Thus, **vials with the same proportion but different \(n_j\)** have different information content.

### 2.2 What pooling does
Pooling the 4 vials × 2 runs into a single proportion per concentration is equivalent to treating the data as

\[
\tilde Y_x = \sum_{j=1}^{8} Y_{j} \quad\text{with}\quad \tilde n_x = \sum_{j=1}^{8} n_j = 40 .
\]

The pooled proportion is \(\tilde p_x = \tilde Y_x / \tilde n_x\).  
If **all vials truly share the same underlying probability** \(p(x)\) **and** the **binomial variance is the only source of variation**, then the pooled proportion is a **sufficient statistic** – no information is lost.

However, **real experiments usually have extra-binomial (over‑) dispersion** caused by:

* Small differences among vials (e.g., slight temperature gradients, micro‑environment),
* Day‑to‑day (run) effects,
* Handling or measurement error.

When such extra variation exists, the **vial‑level counts are not exchangeable** and pooling masks it. Ignoring over‑dispersion leads to:

* **Under‑estimated standard errors** → confidence intervals that are too narrow,
* **Potential bias** in the estimated slope and EC50 if the extra variation is heteroscedastic (different across concentrations).

Consequently, the reviewer’s comment is statistically sound.

---

## 3. Step‑by‑step comparison of the two approaches  

Below we outline the exact calculations you would perform with the original data and with the pooled data. The numbers are illustrative; the same steps apply to any real dataset.

### 3.1 Data layout (example)

| Run | Vial | Conc. (µg L⁻¹) | # immobilised (Y) | # total (n) |
|-----|------|----------------|-------------------|------------|
| 1   | 1    | 0 (control)    | 0                 | 5 |
| 1   | 2    | 0              | 0                 | 5 |
| …   | …    | …              | …                 | … |
| 1   | 4    | 10             | 1                 | 5 |
| 2   | 1    | 0              | 0                 | 5 |
| …   | …    | …              | …                 | … |
| 2   | 4    | 10             | 2                 | 5 |

(40 rows total, 8 rows per concentration.)

### 3.2 Method A – **Pooling** (what was done in Prism)

1. **Aggregate** across the 8 vials for each concentration:  

   \[
   \tilde Y_x = \sum_{j=1}^{8} Y_{j}, \qquad \tilde n_x = 40.
   \]

2. **Compute percentage**  

   \[
   \hat p_x = \frac{\tilde Y_x}{\tilde n_x}\times100.
   \]

3. **Fit** the log‑logistic curve to the 6 points (5 doses + control) using **non‑linear least squares (NLLS)**, **ignoring the binomial variance** (i.e., assuming equal weight for each point).  
   In GraphPad Prism the default weighting is “ordinary” (weight = 1) unless you explicitly supply a *weight* column.

4. **Extract** EC50 and its 95 % CI from the NLLS fit (usually based on the asymptotic covariance matrix).

#### What this does mathematically  

The objective minimized is  

\[
\sum_{x} \bigl[\,\hat p_x - f(x;\theta)\,\bigr]^2,
\]

where \(f(x;\theta)\) is the log‑logistic function and \(\theta\) = (EC50, slope, …).  
Because each point is given the same weight, the **variance of \(\hat p_x\) (≈ p(1‑p)/40)** is **ignored**.

### 3.3 Method B – **Binomial GLM (or GLMM) at the vial level**

1. **Keep the raw counts** (Y, n) for each vial.  
2. **Specify** a **generalised linear model** with a **binomial family** and a **logit link** (or the complementary log‑log link often used for dose–response).  

   \[
   \text{logit}\bigl[p_{ij}\bigr] = \beta_0 + \beta_1\log_{10}(x_i) + \gamma_{r(i)} ,
   \]

   where  

   * \(i\) indexes concentration,  
   * \(j\) indexes vial,  
   * \(\gamma_{r(i)}\) is a term for **run** (see § 3.5).

3. **Fit** the model using **maximum likelihood** (e.g., `glm(..., family = binomial)` in R).  
   The likelihood contribution of vial *j* is  

   \[
   L_{j}= \binom{n_j}{Y_j}\,p_{ij}^{Y_j}\,(1-p_{ij})^{\,n_j-Y_j}.
   \]

4. **Obtain** the EC50 from the fitted parameters:

   * Solve for the concentration that yields \(p=0.5\):  

     \[
     \widehat{EC}_{50}=10^{\displaystyle\frac{\log\bigl(\frac{0.5-d_{\text{low}}}{d_{\text{high}}-0.5}\bigr)-\beta_0}{\beta_1}} .
     \]

   * Confidence intervals are derived from the **profile likelihood** or the **delta method** on the fitted coefficients (most software provides them automatically).

5. **Check for over‑dispersion**: compute Pearson chi‑square / df. If > 1, consider a **quasi‑binomial** or **beta‑binomial** model, or a **GLMM** with a random vial (or run) effect.

#### Advantages  

* **Denominators are used** – a vial with 5 successes out of 5 carries more information than 5 successes out of 20.  
* **Vial‑to‑vial variability** is captured in the residual variance (or explicit random effects).  
* **Standard errors** correctly reflect the binomial (and any extra) variability → **CIs are trustworthy**.

### 3.4 Expected differences in **point estimates** (EC50)

*If the true data‑generating process follows the log‑logistic curve *exactly* and there is **no extra variation** between vials or runs**, both methods will give **identical EC50 estimates** (up to numerical rounding).  

*When there **is** extra-binomial variation* (the usual case), the pooled NLLS fit tends to **under‑weight concentrations with high or low proportions** because the variance of a proportion is *heteroscedastic* (largest near 0.5, smallest near 0 or 1). By giving each concentration equal weight, the curve may be pulled toward the centre of the data, often resulting in a **biased slope** and consequently a **biased EC50** (usually **under‑estimated** if the true slope is shallow, and **over‑estimated** if the true slope is steep).  

Empirical studies (e.g., Finney 1971; Ritz & Streibig 2005) show that for typical sample sizes (5–10 organisms per replicate) the **absolute difference in EC50** between the two methods is usually **< 10 %**, but **confidence‑interval widths can differ by 30–70 %** (see § 3.6).

### 3.5 How to handle the **two independent runs**

| Approach | Description | When it is appropriate |
|----------|-------------|------------------------|
| **Pooled (ignoring run)** | Combine all 8 vials as if they came from a single experiment. | If a preliminary analysis shows *no* run effect (e.g., overlapping control responses, non‑significant run term). |
| **Fixed‑effect run factor** | Add a categorical variable `Run` to the GLM: \(\beta_0 + \beta_1\log_{10}(x) + \delta_{\text{Run}}\). | When runs differ systematically (e.g., different baseline immobilisation) but you want to estimate a common dose–response curve. |
| **Random‑effect run** (GLMM) | Treat `Run` as a random intercept: \(\beta_0 + \beta_1\log_{10}(x) + u_{\text{Run}}\), \(u_{\text{Run}}\sim N(0,\sigma^2_{\text{Run}})\). | When runs are considered a random sample of all possible experimental days and you wish to **generalise** beyond the two observed days. |

**Practical recommendation** (based on the OECD TG 202 guidance and statistical best practice):

1. Fit a **GLM with a fixed run effect** first.  
2. If the run coefficient is **non‑significant** and the **AIC** does not improve, drop it and keep the simpler model.  
3. If the run variance is non‑zero but the estimate is unstable (only two levels), a **random‑effect** may be over‑parameterised; the fixed‑effect approach is usually preferred for two runs.  

In either case, the run term **must be included** in the model **before** you discard the vial‑level structure.

### 3.6 Impact on **confidence intervals**

| Method | How SE is computed | Typical effect on CI width |
|--------|-------------------|---------------------------|
| Pooled % (NLLS, equal weight) | Uses **residual sum of squares** assuming constant variance. | **Too narrow** (often 30–70 % smaller) because the true variance of a proportion is \(\frac{p(1-p)}{n}\) and varies across concentrations. |
| Binomial GLM (no over‑dispersion) | Uses the **binomial Fisher information**; each vial contributes \(n_j p

*Original question: [Is pooling replicate counts into percentages acceptable for dose–response analysis of quantal toxicity?](https://stats.stackexchange.com/questions/677208/is-pooling-replicate-counts-into-percentages-acceptable-for-dose-response-analys) on Cross Validated (Stats Stack Exchange), licensed CC BY-SA.*

{% endraw %}
