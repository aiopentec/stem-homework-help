---
layout: question
title: Understanding confidence interval for VIF/tolerance when looking at multicollinearity
author: StemFix Bot
category: stats
subject: stats
description: 'Step-by-step statistics solution: Understanding confidence interval
  for VIF/tolerance when looking at multicollinearity'
tags:
- stats
---

{% raw %}
*As an Amazon Associate, I earn from qualifying purchases.* For more practice problems like this, see [Schaum's Outline of Statistics, 6th Edition](https://www.amazon.com/dp/1260011461?tag=aiopentec20-20).

---

## 1. What the student is asking (in plain language)

The student fitted a linear mixed‑effects model that contains a predictor called **Eyes**.  
To check whether any of the predictors are highly collinear, the software printed a table that includes:

| Term | VIF | VIF 95 % CI (adjusted) | Tolerance | Tolerance 95 % CI |
|------|-----|-----------------------|-----------|-------------------|
| Eyes | 1.00| [1.00, ∞]            | 1.00      | [0.00, 1.00]      |

The student is surprised to see that the confidence interval (CI) for the VIF stretches to infinity (and the CI for tolerance stretches down to 0).  
**Question:** Does an infinite (or unbounded) confidence interval mean that there is “uncertainty” about multicollinearity, or does it tell us something else?

---

## 2. Step‑by‑step explanation

### 2.1. What are VIF and tolerance?

| Quantity | Definition | Interpretation |
|----------|------------|----------------|
| **VIF (Variance Inflation Factor)** | \( \displaystyle \text{VIF}_j = \frac{1}{1-R_j^{2}} \) where \(R_j^{2}\) is the coefficient of determination when regressing predictor \(X_j\) on **all** the other predictors. | A VIF of 1 means no linear relationship with the other predictors. Larger values indicate that the variance of the estimated coefficient for \(X_j\) is inflated because of multicollinearity. Rough rules of thumb: VIF > 5 (or 10) may be worrisome. |
| **Tolerance** | \( \displaystyle \text{Tol}_j = 1 - R_j^{2} = \frac{1}{\text{VIF}_j} \) | Tolerance near 0 (e.g., < 0.1) signals a problem; tolerance close to 1 signals little or no collinearity. |

Thus VIF and tolerance are *deterministic* functions of the sample‑based \(R_j^{2}\). If we could observe the exact population correlation structure, the VIF would be a fixed number (not a random variable). The CI reflects **sampling variability** of the estimated \(R_j^{2}\).

### 2.2. How are confidence intervals for VIF/tolerance obtained?

Most statistical packages compute a CI for VIF (or tolerance) by:

1. **Fit the auxiliary regression** \(X_j = \beta_0 + \sum_{k\neq j}\beta_k X_k + \varepsilon\).
2. **Obtain the residual sum of squares** and the corresponding \(R_j^{2}\) (or equivalently the error variance estimate \(s^{2}\)).
3. **Treat the residual variance estimate** as a scaled chi‑square random variable:
   \[
   \frac{(n-p) \, s^{2}}{\sigma^{2}} \sim \chi^{2}_{n-p},
   \]
   where \(n\) = total observations, \(p\) = number of predictors (including the intercept) in the auxiliary regression.
4. **Derive a CI for the error variance** \(\sigma^{2}\) by inverting the chi‑square quantiles:
   \[
   \frac{(n-p) s^{2}}{\chi^{2}_{\alpha/2,\,n-p}} \le \sigma^{2} \le \frac{(n-p) s^{2}}{\chi^{2}_{1-\alpha/2,\,n-p}} .
   \]
5. **Transform the CI for \(\sigma^{2}\) into a CI for \(R_j^{2}\)** (or directly for tolerance). The relationship between the error variance and \(R_j^{2}\) is
   \[
   R_j^{2}=1-\frac{\sigma^{2}}{\text{Var}(X_j)} .
   \]
6. Finally **invert** the VIF–tolerance relationship:
   \[
   \text{VIF}= \frac{1}{\text{Tolerance}}.
   \]

When the **point estimate** of \(R_j^{2}\) is *exactly zero* (i.e., the auxiliary regression finds **no linear relationship** between \(X_j\) and the other predictors), we have:

* \( \hat{R}_j^{2}=0 \)
* \( \widehat{\text{Tolerance}} = 1-0 = 1\)
* \( \widehat{\text{VIF}} = 1/1 = 1\)

### 2.3. Why does the CI become unbounded (∞ for VIF, 0 for tolerance)?

The CI for a proportion (here, \(R_j^{2}\) or tolerance) is based on the variability of the estimate. If the **sample estimate** lies at the boundary of the possible parameter space (0 or 1), the usual (Wald‑type) CI may “run off the edge”.

Consider tolerance as an estimate of a probability that lies in \([0,1]\). If the point estimate is exactly 1, any plausible lower limit must be ≥ 0, but there is **no upper bound** beyond 1. When we convert that interval to VIF, the upper bound becomes \(1 / (\text{lower bound of tolerance})\). If the lower bound of tolerance is **exactly 0**, the corresponding VIF upper bound is \(1/0 = \infty\).

In practice, the software often uses the **F‑distribution** to build a CI for VIF directly (e.g., `vifci` in *car* package). The formula for the lower and upper limits of VIF is

\[
\text{VIF}_{\text{lower}} = \frac{\text{VIF}}{F_{1-\alpha/2,\,df_{1},\,df_{2}}}, \qquad
\text{VIF}_{\text{upper}} = \frac{\text{VIF}}{F_{\alpha/2,\,df_{1},\,df_{2}}}
\]

where the denominator involves an F‑quantile. If the **degrees of freedom** for the auxiliary regression are small (or the residual variance is zero), the lower F‑quantile can be **zero**, leading to an infinite upper bound for VIF.

**Bottom line:** The infinite upper bound does **not** indicate that the predictor is “somewhat” collinear. It is a *mathematical consequence* of the fact that the estimated VIF equals its theoretical minimum (1). Because the estimate sits at the boundary, the usual method cannot produce a finite upper confidence limit.

### 2.4. What does this tell us about multicollinearity for *Eyes*?

* **Point estimate:** VIF = 1, tolerance = 1 → *perfectly* non‑collinear with the other predictors.
* **Confidence interval:**  
  * VIF 95 % CI = \([1,\,\infty)\)  
  * Tolerance 95 % CI = \([0,\,1]\)

Interpretation:

| Parameter | Meaning of CI |
|-----------|----------------|
| VIF | We are **certain** that the true VIF is **at least** 1 (the minimum possible). The data do not give us enough information to place a finite upper limit; mathematically the interval must extend to infinity. |
| Tolerance | Likewise, the true tolerance is **at most** 1 and could be as low as 0. Because the estimate is right at the upper boundary, the lower bound is forced to 0. |

In practical terms, the result tells us **there is no evidence of multicollinearity** involving *Eyes*. The infinite upper bound is a technical artifact, not a warning sign.

### 2.5. When does an infinite CI arise in other situations?

* **Exact zero residual variance** in the auxiliary regression (perfect prediction) → VIF = ∞, tolerance = 0 (the opposite extreme).
* **Very small sample size** relative to the number of predictors → the F‑distribution quantile in the denominator can be zero (or numerically very close), producing an unbounded interval.
* **Perfect separation** in logistic regression (analogous situation) leads to infinite standard errors and unbounded CIs.

---

## 3. Final answer

*The confidence interval \([1,\infty)\) for the VIF (and \([0,1]\) for tolerance) does **not** indicate uncertainty about the presence of multicollinearity. It simply reflects the fact that the point estimate of VIF is at its theoretical minimum (1). Because the estimate lies on the boundary of the permissible range, the usual method for constructing a confidence interval cannot produce a finite upper bound, so it reports “infinity”. In substantive terms, there is **no evidence of multicollinearity** for the predictor *Eyes*; the infinite upper limit is a mathematical artifact, not a diagnostic concern.*

---

## 4. Common mistakes when interpreting VIF/tolerance confidence intervals

| Mistake | Why it’s wrong | Correct approach |
|---------|----------------|------------------|
| **Thinking “∞” means “high multicollinearity”.** | An infinite upper bound occurs when the VIF estimate is at its minimum (1), not when it is large. | Remember that VIF ≥ 1; only values **much larger** than 1 raise concern. |
| **Assuming the CI gives a range of likely VIF values.** | The interval is derived from an asymptotic (Wald) approximation that breaks down at the boundary; the lower bound is reliable, the upper bound may be infinite. | Use the point estimate (VIF = 1) as the practical indicator; treat the infinite bound as “cannot be bounded given the data”. |
| **Ignoring the sample‑size effect.** | With few observations relative to predictors, the CI may be very wide or infinite even when the point estimate is modest. | Check the degrees of freedom of the auxiliary regression; if they are small, consider collecting more data or reducing the number of predictors. |
| **Confusing VIF with correlation coefficient.** | VIF is a function of the *multiple* R² from regressing one predictor on *all* others, not a simple pairwise correlation. | Examine the auxiliary regression or a correlation matrix to understand which predictors contribute to any collinearity. |
| **Using the CI to decide whether to drop a variable.** | Because the CI can be unbounded, the decision rule “drop if CI includes > 5” is meaningless. | Base the decision on the **point estimate** and substantive knowledge; a VIF of 1 is as low as it gets. |

---

*Original question: [Understanding confidence interval for VIF/tolerance when looking at multicollinearity](https://stats.stackexchange.com/questions/677326/understanding-confidence-interval-for-vif-tolerance-when-looking-at-multicolline) on Cross Validated (Stats Stack Exchange), licensed CC BY-SA.*

{% endraw %}
