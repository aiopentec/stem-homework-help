---
layout: post
title: Negative deviance explained by GAM with betareg in R
author: StemFix Bot
category: stats
tags:
- stats
---

{% raw %}
*As an Amazon Associate, I earn from qualifying purchases.* For more practice problems like this, see [Schaum's Outline of Statistics, 6th Edition](https://www.amazon.com/dp/1260011461?tag=aiopentec20-20).

---

## 1. What the student is asking (in plain language)

The student is fitting a **generalized additive model (GAM)** with a **beta‐distributed response** (the proportion of cyanobacteria cover) using the `mgcv::gam()` function:

```r
g6 = gam(cyano/100 ~ s(SEGLOWFLOW) + s(SEGJANAIRT) + 
         s(LOCHAB) + s(LOCSED) + s(T2PastoralHeavy) + 
         s(SEDO) + s(USDAYSRAIN) + s(USAVGSLOPE) + 
         s(USHARDNESS),
         data = nati1,
         family = betar(link = "logit"))
```

When the model is fitted they receive two concerning messages:

1. **Warning:**  
   ```
   In object$family$saturated.ll(G$y, wts, theta) :
     saturated likelihood may be inaccurate
   ```

2. **Summary output:**  

   ```
   R‑sq.(adj) = 0.0871   Deviance explained = -29.9%
   -REML = -2370.5  Scale est. = 1   n = 463
   ```

The **negative “deviance explained”** and the **warning about an inaccurate saturated likelihood** make the student doubt whether the model is valid, even though the diagnostic plots look reasonable and predictions appear sensible.

The question therefore is:

> **Why does the GAM with a beta family produce a negative deviance‑explained value and a warning about the saturated likelihood, and what should be done to fix (or at least understand) the problem?**



---

## 2. Step‑by‑step explanation

### 2.1  Recall what the beta family does

* The response must be **strictly between 0 and 1**.  
  The beta distribution is defined only on the open interval \((0,1)\); values exactly equal to 0 or 1 are **not allowed**.

* `betar(link = "logit")` in **mgcv** is a wrapper around `betar` from the **betareg** package.  
  It uses the log‑odds link \(\eta = \log\frac{\mu}{1-\mu}\) where \(\mu\) is the mean of the beta distribution.

* The **log‑likelihood** of a beta model contains terms of the form  
  \(\log y\) and \(\log (1-y)\). If any observation is 0 or 1, these terms become \(-\infty\) and the likelihood is undefined.

### 2.2  What the warning means

`object$family$saturated.ll()` computes the **log‑likelihood of the saturated model** (a model that fits each observation perfectly).  
When any \(y_i = 0\) or \(y_i = 1\) the saturated log‑likelihood is \(-\infty\).  

`mgcv` therefore issues the warning:

```
saturated likelihood may be inaccurate
```

because it had to replace the exact \(-\infty\) with a very large negative number (or it could not compute it at all).  
Consequences:

| Situation | Effect on deviance / R² |
|-----------|--------------------------|
| No 0/1 values | Saturated log‑likelihood finite → deviance is computed correctly |
| One or more 0/1 values | Saturated log‑likelihood = –∞ (or numerically unstable) → deviance becomes *larger* than the model deviance → **negative deviance explained** |

Hence the warning is **directly linked** to the negative deviance‑explained value.

### 2.3  How deviance‑explained is computed in `mgcv`

For a model with log‑likelihood \(\ell_{\text{model}}\) and saturated log‑likelihood \(\ell_{\text{sat}}\) :

\[
\text{Deviance} = -2(\ell_{\text{model}} - \ell_{\text{sat}})
\]

and

\[
\text{Deviance explained} = 1 - \frac{\text{Deviance}_{\text{model}}}{\text{Deviance}_{\text{null}}}
\]

If \(\ell_{\text{sat}}\) is set to a *very* small (i.e., large‑negative) number because of 0/1 observations, the **model deviance** can become *greater* than the null deviance, producing a **negative** proportion explained.

### 2.4  Typical causes of 0/1 values in a proportion variable

| Cause | Example |
|-------|---------|
| **Exact zero** – e.g., sites where cyanobacteria were not detected at all. |
| **Exact one** – e.g., sites where the measured cover was 100 % (the user divided by 100, so the stored value becomes 1). |
| **Rounding** – the original data may have been stored with limited precision (e.g., 0.00, 0.01, …). |
| **Missing data coded as 0 or 1** – sometimes `NA`s are replaced by 0/1 before modelling. |

Even a **single** such observation is enough to trigger the warning.

### 2.5  Verify the presence of 0/1 values

```r
# Check how many exact 0 or 1 values are in the response
sum(nati1$cyano == 0)   # raw percentages before division by 100
sum(nati1$cyano == 100)

# After division
y <- nati1$cyano/100
sum(y == 0)
sum(y == 1)
```

If any of the sums above are > 0, the problem is confirmed.

### 2.6  Strategies to handle boundary values

| Strategy | How to implement | When it is appropriate |
|----------|------------------|------------------------|
| **Add a small constant (shrinkage)** | `y_adj <- (y * (n-1) + 0.5) / n`  (where *n* is the sample size) or `y_adj <- (y*(N-1)+0.5)/N` | When 0/1 values are genuine measurements but you are willing to treat them as “very small” or “very close to 1”. |
| **Transform to a (0,1) interval with `betar`’s built‑in option** | `family = betar(link = "logit", link.phi = "log")` **plus** `y_adj <- (y*(n-1)+0.5)/n` before modelling. | Same as above; the transformation must be done **outside** `gam`. |
| **Use a zero‑one‑inflated beta model** | Fit with `betareg::betareg()` using `type = "zeroOneInflatedBeta"` or with `gamlss::gamlss()` (`family = BEINF`). | When you have a *real* mixture of exact zeros/ones and values in (0,1) and you want to model the two processes separately. |
| **Model the data as a binomial proportion** | If the denominator (e.g., number of pixels surveyed) is known, use `cbind(successes, failures)` with a binomial family. | When the response truly comes from counts of successes/trials rather than a continuous proportion. |
| **Remove the offending rows** | `nati1 <- subset(nati1, cyano > 0 & cyano < 100)` | Only if the 0/1 observations are known to be errors or outliers. |

**Most common practical fix** (especially for ecological cover data) is the *shrink‑toward‑the‑interior* transformation:

```r
# Number of observations
N <- nrow(nati1)

# Transform to (0,1) interval
nati1$cyano_adj <- (nati1$cyano/100 * (N - 1) + 0.5) / N

g6_adj <- gam(cyano_adj ~ s(SEGLOWFLOW) + s(SEGJANAIRT) +
              s(LOCHAB) + s(LOCSED) + s(T2PastoralHeavy) +
              s(SEDO) + s(USDAYSRAIN) + s(USAVGSLOPE) + s(USHARDNESS),
              data = nati1,
              family = betar(link = "logit"))
summary(g6_adj)
```

After this transformation the warning disappears and the **deviance‑explained** becomes a *positive* value (often modest for ecological data; values around 0.1–0.3 are common).

### 2.7  Re‑examine the model after fixing the data

1. **Check the warning again** – it should be gone.  
2. **Look at the new deviance‑explained** – it will now be between 0 and 1.  
3. **Inspect residuals** (`gam.check(g6_adj)`) – they should still look reasonable.  
4. **Interpret the smooth terms** – the magnitude and shape of each `s()` term are unchanged (apart from a tiny scaling effect caused by the transformation).

### 2.8  Why the adjusted R‑squared (`R‑sq.(adj)`) stayed small

Even after fixing the boundary problem, the adjusted R‑squared may still be low (e.g., ~0.09) because:

* The predictors explain only a small portion of the variability in cyanobacteria cover.
* The beta distribution has **two parameters** (mean and precision). `mgcv` with `betar` models only the **mean** (the precision is estimated as a single scalar). If precision varies a lot across sites, the model cannot capture that variation, reducing pseudo‑\(R^2\).

If you need a richer model of the **precision** (often denoted \(\phi\)), consider a **beta‑regression with a varying precision parameter**, e.g.:

```r
library(betareg)
fit <- betareg(cyano/100 ~ s(SEGLOWFLOW) + ... | 1, data = nati1)
```

or a **GAMLSS** model (`family = BE`) where both \(\mu\) and \(\sigma\) can have smooth terms.

---

## 3. Final answer (summary)

* The warning **“saturated likelihood may be inaccurate”** occurs because the response variable contains exact 0 or 1 values, which are outside the support of the beta distribution.
* The presence of such values makes the **saturated log‑likelihood \(-\infty\)**, causing the **deviance explained** to become negative.
* **Fix** the problem by moving the data away from the boundaries (e.g., the *shrink‑to‑interior* transformation) **or** use a model that explicitly handles zeros and ones (zero‑one‑inflated beta, binomial, or GAMLSS).
* After the correction, the warning disappears, deviance‑explained becomes positive, and the model diagnostics can be interpreted as usual.

---

## 4. Common mistakes when fitting beta‑GAMs (or any beta regression)

| Mistake | Why it matters | How to avoid / correct |
|---------|----------------|------------------------|
| **Leaving 0 or 1 values in the response** | Beta density is undefined at the boundaries → infinite log‑likelihood → warning & negative deviance. | Check `any(y == 0 | y == 1)`; either transform, remove, or use a zero‑inflated beta model. |
| **Dividing by 100 after the check** | If you check for 0/100 *before* division, you may miss 0/1 after scaling. | Perform the check on the *scaled* variable (`y = cyano/100`). |
| **Assuming `betar` automatically handles boundary values** | `betar` behaves like `betareg`; it does *not* internally adjust 0/1. | Explicitly adjust the data or choose a family that does (e.g., `BEINF`). |
| **Interpreting negative deviance explained as “good fit”** | Negative values indicate the model fits **worse** than the null. | After fixing boundaries, re‑compute; a positive deviance explained is required for a sensible pseudo‑\(R^2\). |
| **Forgetting that precision is constant** | `mgcv::betar` estimates a *single* precision parameter; heteroskedasticity is ignored. | If precision varies, use `betareg` with a formula for the precision term or a GAMLSS model. |
| **Using default `link = "logit"` when data are heavily skewed** | The logit link may produce convergence problems for extreme proportions. | Try `loglog` or `cloglog` links, or re‑scale the response to avoid extreme values. |
| **Not checking for over‑/under‑dispersion** | The beta model assumes variance \(\propto \mu(1-\mu)\); violations lead to poor fit. | Examine residual deviance, plot Pearson residuals vs. fitted values, or fit a quasi‑beta model if needed. |

By ensuring that the response lies strictly inside \((0,1)\) and choosing a model that matches the data‑generating process, the beta‑GAM will produce reliable diagnostics and a meaningful deviance‑explained statistic.

*Original question: [Negative deviance explained by GAM with betareg in R](https://stats.stackexchange.com/questions/223858/negative-deviance-explained-by-gam-with-betareg-in-r) on Cross Validated (Stats Stack Exchange), licensed CC BY-SA.*

{% endraw %}
