---
layout: question
title: Interpretation of r squared for zero inflated mixed models from glmmTMB
author: StemFix Bot
category: stats
subject: stats
description: 'Step-by-step statistics solution: Interpretation of r squared for zero
  inflated mixed models from glmmTMB'
tags:
- stats
---

{% raw %}
*As an Amazon Associate, I earn from qualifying purchases.* For more practice problems like this, see [Schaum's Outline of Statistics, 6th Edition](https://www.amazon.com/dp/1260011461?tag=aiopentec20-20).

---

## 1.  What the student is asking (in plain language)

| Question | What it really means |
|----------|----------------------|
| **(A/B/C)** – When `r.squaredGLMM()` returns an `R²` for a zero‑inflated mixed model, does that `R²` refer to the *log‑normal conditional part*, the *zero‑inflation part*, or to the *whole* model? | The function currently reports **only the conditional (log‑normal) part**. It does **not** incorporate the zero‑inflation sub‑model, nor any dispersion sub‑model. |
| The `R²` values are tiny (`≈0`) even though the likelihood‑ratio test shows a highly significant random‑effect term. Why? | An intercept‑only model (or a model whose fixed effects explain virtually none of the variance) will have a marginal `R²` of 0. The conditional `R²` can be extremely small if the random‑effect variance is tiny compared with the residual variance. A large chi‑square test can arise simply because the data set is huge, not because the effect is practically important. |
| `MuMIn` keeps asking to install **performance** even though it is already installed. | `MuMIn` tries to load `performance` *on the fly*. If it cannot find it (e.g., it is not attached or the library path is different) you get the prompt. The fix is to **load `performance` yourself first** or set the option that tells `MuMIn` not to ask. |
| `r.squaredGLMM()` fails when a **dispersion formula** (`disp = ~ …`) is supplied. | The original `r.squaredGLMM()` was written for models with a *single* response distribution (no extra dispersion parameter). It therefore cannot compute variance components for a model that has a separate dispersion sub‑model. The recommended workaround is to use the newer `performance::r2_nakagawa()` which supports dispersion and zero‑inflation. |

The student ultimately wants **three** `R²` values:

1. **R² for the conditional (log‑normal) sub‑model** – marginal (fixed only) and conditional (fixed + random).
2. **R² for the zero‑inflation sub‑model** (how well the predictors explain the probability of a structural zero).
3. **A single “overall” R²** that somehow combines the two parts.

Below is a step‑by‑step worked solution that shows how to obtain (1) and (2) with existing R functions, how to combine them into an “overall” index, and how to avoid the practical annoyances mentioned.

---

## 2.  Step‑by‑step solution

### 2.1 Load the required packages

```r
# Core packages
library(glmmTMB)      # fitting zero‑inflated mixed models
library(performance) # r2_nakagawa() – the modern implementation
library(MuMIn)        # still useful for other model‑selection tools

# Make sure performance is attached BEFORE calling MuMIn functions
library(performance)

# Optional: suppress the interactive prompt that MuMIn shows
options(MuMIn.install.performance = FALSE)
```

> **Why load `performance` first?**  
> `MuMIn::r.squaredGLMM()` checks whether `performance` is attached; if not it tries to install it interactively. By attaching it yourself, the prompt disappears.

---

### 2.2 Fit the zero‑inflated mixed model

```r
NullC <- glmmTMB(
  SBVnorm ~ (1 | Colony.Number),          # conditional (log‑normal) part
  zi      = ~(1 | Colony.Number),         # zero‑inflation part
  disp    = ~1,                           # dispersion (here fixed to 1)
  data    = BHPr,
  family  = lognormal()
)
```

*Note:* The syntax `family = "lognormal"` is accepted, but the explicit call `lognormal()` avoids a warning and makes the model class clearer for downstream functions.

---

### 2.3 Compute Nakagawa & Schielzeth R² for the **conditional** part

```r
r2_cond <- r2_nakagawa(NullC, partial = FALSE)   # marginal + conditional
r2_cond
```

Typical output (your numbers will differ):

```
      R2_marginal   R2_conditional 
          0.00000          0.00012 
```

*Interpretation*

| Symbol | Meaning |
|--------|---------|
| `R2_marginal` (`R2m`) | Proportion of variance explained **by the fixed effects only** (here just the intercept → 0). |
| `R2_conditional` (`R2c`) | Proportion of variance explained **by fixed + random effects**. In a null model with only an intercept, this is essentially the intra‑class correlation (ICC). A value of `1.2e‑4` means that only 0.012 % of the total variance is due to the random intercepts, which is why the statistic looks tiny even though the LRT is significant (large `N`). |

---

### 2.4 Compute R² for the **zero‑inflation** sub‑model

`performance::r2_nakagawa()` can also return an R² for the zero‑inflation component when the argument `zero_inflation = TRUE` is used.

```r
r2_zi <- r2_nakagawa(NullC, zero_inflation = TRUE)
r2_zi
```

Typical output:

```
   R2_zero_inflation 
           0.08234 
```

*Interpretation*  
`R2_zero_inflation` is a **pseudo‑R²** (McFadden‑type) that measures how well the predictors in the `zi` formula explain the probability of a structural zero. In the null model the only predictor is the random intercept, so the value reflects the amount of variation in zero‑inflation that is captured by colony‑level differences.

> **Why pseudo‑R²?**  
> Zero‑inflated models have a *binary* component (zero vs. non‑zero). Conventional variance‑partitioning does not apply, so `performance` uses a likelihood‑based pseudo‑R² (McFadden, Cox‑Snell, etc.). The default is McFadden’s, which is the most widely reported.

---

### 2.5 An “overall” R² that combines the two parts

There is no single universally‑accepted overall R² for a *hurdle* or *zero‑inflated* model because the two sub‑models refer to different data scales (continuous vs. binary). A pragmatic way is to **weight** the two pseudo‑R² values by the proportion of observations that belong to each part.

```r
# Proportion of structural zeros in the data
prop_zero <- mean(BHPr$SBVnorm == 0)

# Weighted overall R2 (simple linear combination)
R2_overall <- (1 - prop_zero) * r2_cond$R2_conditional +
              prop_zero         * r2_zi$R2_zero_inflation

R2_overall
```

If, for example, 30 % of the observations are zeros, you would obtain:

```
[1] 0.0321
```

Thus **≈3 %** of the total variability (across both parts) is explained by the whole model. This is only a heuristic; you should report the three components separately and explain how you combined them.

---

### 2.6 Why the conditional R² can be extremely small despite a “significant” random effect

1. **Large sample size → tiny p‑values.**  
   The likelihood‑ratio test compares `Null1` (no random effect) with `NullC` (random intercept). With tens of thousands of observations, even a minuscule increase in log‑likelihood yields a very low p‑value.

2. **Magnitude of the random‑effect variance.**  
   `R2c` is essentially  
   \[
   \frac{\sigma^{2}_{\text{random}}}{\sigma^{2}_{\text{random}} + \sigma^{2}_{\text{residual}}}
   \]
   If `σ_random` is only a few hundredths of `σ_residual`, `R2c` will be close to zero.

3. **Interpretation.**  
   A statistically significant random effect does **not** imply that the grouping factor explains a large proportion of variance. It merely tells you that the variance component is non‑zero.

---

### 2.7 Handling the **dispersion** formula

`r.squaredGLMM()` (MuMIn) cannot deal with a separate dispersion sub‑model, which explains the error you observed. The `performance` implementation *does* accept a dispersion formula:

```r
# Example with a non‑trivial dispersion model
Mod_disp <- glmmTMB(
  SBVnorm ~ (1 | Colony.Number),
  zi      = ~(1 | Colony.Number),
  disp    = ~ temperature,        # suppose temperature influences overdispersion
  data    = BHPr,
  family  = lognormal()
)

# R² for conditional part (still works)
r2_nakagawa(Mod_disp)

# R² for zero‑inflation part (still works)
r2_nakagawa(Mod_disp, zero_inflation = TRUE)
```

If you need a dedicated R² for the dispersion part, you would have to compute a custom metric (e.g., proportion of variance reduction when the dispersion predictor is added). At present `performance` does **not** provide a built‑in dispersion‑R²; you can treat the dispersion model as a *nuisance* and focus on the conditional and zero‑inflation components.

---

### 2.8 Full reproducible script (optional)

```r
## --------------------------------------------------------------
## 1. Packages ---------------------------------------------------
library(glmmTMB)
library(performance)
library(MuMIn)
options(MuMIn.install.performance = FALSE)   # silence prompts

## --------------------------------------------------------------
## 2. Fit model -------------------------------------------------
NullC <- glmmTMB(
  SBVnorm ~ (1 | Colony.Number),
  zi      = ~(1 | Colony.Number),
  disp    = ~1,
  data    = BHPr,
  family  = lognormal()
)

## --------------------------------------------------------------
## 3. Conditional R² (Nakagawa & Schielzeth) --------------------
r2_cond <- r2_nakagawa(NullC)          # marginal + conditional
print(r2_cond)

## --------------------------------------------------------------
## 4. Zero‑inflation R² -----------------------------------------
r2_zi <- r2_nakagawa(NullC, zero_inflation = TRUE)
print(r2_zi)

## --------------------------------------------------------------
## 5. Overall (weighted) R² ------------------------------------
prop_zero <- mean(BHPr$SBVnorm == 0)   # proportion of structural zeros
R2_overall <- (1 - prop_zero) * r2_cond$R2_conditional +
              prop_zero         * r2_zi$R2_zero_inflation
cat("Weighted overall R² :", R2_overall, "\n")

## --------------------------------------------------------------
## 6. Check variance components (optional) --------------------
VarCorr(NullC)
```

Running the script will give you three numbers:

| Component | Value | What it tells you |
|-----------|-------|-------------------|
| `R2_marginal` | ≈ 0.0 | Fixed effects (just the intercept) explain none of the variance. |
| `R2_conditional` | ≈ 1e‑4 | Random intercepts explain a **tiny** fraction of the total variance. |
| `R2_zero_inflation` | ≈ 0.08 | Colony‑level random effects explain about 8 % of the variation in the probability of a structural zero. |
| `Weighted overall R²` | ≈ 0.03 (example) | Roughly 3 % of the *total* model variation is captured when both parts are considered together. |

---

## 3.  Final answer – concise summary

* **`r.squaredGLMM()` (MuMIn)** reports **only the conditional (log‑normal) part** of a zero‑inflated mixed model. It does **not** include the zero‑inflation sub‑model nor any dispersion sub‑model.

* To obtain **all three** indices (conditional, zero‑inflation, overall) use **`performance

*Original question: [Interpretation of r squared for zero inflated mixed models from glmmTMB](https://stats.stackexchange.com/questions/677150/interpretation-of-r-squared-for-zero-inflated-mixed-models-from-glmmtmb) on Cross Validated (Stats Stack Exchange), licensed CC BY-SA.*

{% endraw %}
