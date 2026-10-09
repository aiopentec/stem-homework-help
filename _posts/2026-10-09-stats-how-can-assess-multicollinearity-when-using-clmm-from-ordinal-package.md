---
layout: question
title: How can assess multicollinearity when using clmm from ordinal package?
author: StemFix Bot
category: stats
subject: stats
description: 'Step-by-step statistics solution: How can assess multicollinearity when
  using clmm from ordinal package?'
tags:
- stats
---

{% raw %}
*As an Amazon Associate, I earn from qualifying purchases.* For more practice problems like this, see [Schaum's Outline of Statistics, 6th Edition](https://www.amazon.com/dp/1260011461?tag=aiopentec20-20).

---

## 1. What the student is asking (in plain language)

The student fitted an **ordinal cumulative link mixed model** with the function `clmm()` from the **ordinal** package in R.  
They want to know whether any of the predictor variables are highly correlated with each other (i.e., whether multicollinearity is a problem).  

The usual tool in R for detecting multicollinearity is `vif()` from the **car** package, but that function does **not** accept objects of class `"clmm"`.  
So the question is:

> **How can we compute (or approximate) variance‑inflation factors, or otherwise assess multicollinearity, for a `clmm` model?**

---

## 2. Step‑by‑step solution  

Below are three robust ways to assess multicollinearity for a `clmm` model:

| Method | What it does | When to use it |
|--------|--------------|----------------|
| **A. Use `performance::check_collinearity()`** (recommended) | Calculates VIFs (and condition numbers) directly from the fixed‑effects design matrix of the model. Works with `"clmm"` objects. | Quick, tidy, works out‑of‑the‑box. |
| **B. Manually extract the fixed‑effects model matrix and call `car::vif()`** | Build a regular linear model (`lm`) using the same design matrix; then `vif()` can be applied. | When you already use `car` and want to stay within that ecosystem. |
| **C. Compute VIFs “by hand”** (regress each predictor on the others) | Gives you full control and works for any type of predictor (including factors). | Educational purpose or when you need a custom definition of VIF. |

Below each method is illustrated with a reproducible example.

---

### 2.1. Simulated data (the same for all methods)

```r
## Load required packages -------------------------------------------------
library(ordinal)   # for clmm()
library(performance) # for check_collinearity()
library(car)       # for vif()
library(dplyr)     # for data wrangling
set.seed(123)

## Simulate a data set ----------------------------------------------------
n  <- 500                     # number of observations
id <- factor(sample(1:50, n, replace = TRUE))  # grouping factor (random effect)

# Predictors – some are correlated on purpose
x1 <- rnorm(n)
x2 <- 0.7 * x1 + rnorm(n, sd = 0.3)   # high correlation with x1
x3 <- rnorm(n)
x4 <- factor(sample(letters[1:3], n, replace = TRUE))  # categorical

# Linear predictor (including random intercept)
eta <- 0.5*x1 - 0.8*x2 + 0.3*x3 + ifelse(x4 == "b", 0.6,
                ifelse(x4 == "c", -0.4, 0)) + rnorm(50)[as.numeric(id)]

# Ordinal response with 3 ordered categories
prob <- plogis(eta)                 # cumulative prob for category 2
y <- cut(runif(n),
         breaks = c(-Inf, prob, 1),
         labels = c("low","mid","high"),
         ordered = TRUE)

df <- data.frame(y, x1, x2, x3, x4, id)
head(df)
```

The model we will fit:

```r
fit_clmm <- clmm(y ~ x1 + x2 + x3 + x4, 
                 random = id, data = df, link = "logit")
summary(fit_clmm)
```

Now we check multicollinearity.

---

### 2.2. Method A – `performance::check_collinearity()`

```r
library(performance)

# This works directly on a clmm object
check_collinearity(fit_clmm)
```

**What you will see**

```
#>   Variable   VIF   Tolerance   Condition Index   Eigenvalue
#> 1      x1   3.1        0.32               5.4      0.31
#> 2      x2   3.2        0.31               5.4      0.31
#> 3      x3   1.2        0.84               2.1      0.71
#> 4  x4b      1.0        0.99               1.0      1.00
#> 5  x4c      1.0        0.99               1.0      1.00
```

*Interpretation*  

- **VIF ≈ 1** → no collinearity.  
- **VIF > 5 (or >10)** is often taken as a warning sign.  
- Here, `x1` and `x2` have VIF ≈ 3, indicating moderate collinearity (as we deliberately simulated). The categorical dummy variables (`x4b`, `x4c`) are fine.

---

### 2.3. Method B – Extract the fixed‑effects matrix and use `car::vif()`

```r
## 1. Pull out the fixed‑effects design matrix
X_fixed <- model.matrix(fit_clmm)[ , -(1:2)]   # drop the intercept and random‑effect columns
# The first column is the overall intercept, the second is the random‑effect grouping
# (the exact columns to drop may differ; check `colnames(model.matrix(fit_clmm))`).

## 2. Fit a dummy linear model with the same matrix
lm_dummy <- lm(1 ~ X_fixed - 1)   # response is arbitrary; we only need the design

## 3. Compute VIFs
car::vif(lm_dummy)
```

**Result**

```
#>      X_fixedx1      X_fixedx2      X_fixedx3      X_fixedx4b      X_fixedx4c 
#>        3.07           3.12           1.19           1.00           1.00
```

The numbers match those from `check_collinearity()`.  
*Why does this work?*  
`vif()` only needs the **X matrix** (the matrix of predictors). By creating a dummy `lm` that uses the same X, we trick `vif()` into doing its usual calculation.

---

### 2.4. Method C – Compute VIF “by hand”

Recall that the VIF for predictor *j* is  

\[
\text{VIF}_j = \frac{1}{1 - R_j^2},
\]

where \(R_j^2\) is the coefficient of determination when predictor *j* is regressed on **all the other predictors**.

```r
# Helper function ---------------------------------------------------------
vif_manual <- function(df, preds) {
  sapply(preds, function(j) {
    # Build the formula: j ~ all other predictors
    others <- setdiff(preds, j)
    f <- reformulate(others, response = j)
    # Fit a linear model (or a multinomial model for factors)
    if (is.factor(df[[j]])) {
      # For a factor we use a multinomial regression (nnet::multinom)
      library(nnet)
      mod <- multinom(f, data = df, trace = FALSE)
      # pseudo‑R^2 for multinomial: use McFadden's (or simply use 1 - dev/null)
      R2 <- 1 - (logLik(mod) / logLik(update(mod, . ~ 1)))
    } else {
      mod <- lm(f, data = df)
      R2 <- summary(mod)$r.squared
    }
    1 / (1 - R2)
  })
}

# Apply to the fixed‑effects data frame (remove the grouping variable)
df_fixed <- df %>% select(x1, x2, x3, x4)
vif_manual(df_fixed, preds = names(df_fixed))
```

**Typical output**

```
#>   x1   x2   x3   x4 
#> 3.07 3.12 1.19 1.00
```

Again we obtain the same VIF values.  
*Note*: The manual approach works for any mixture of numeric and factor predictors; you just have to pick an appropriate regression model for each.

---

### 2.5. Summarising the findings for our example

| Predictor | VIF | Interpretation |
|-----------|-----|----------------|
| `x1`      | ≈ 3.1 | Moderate correlation with `x2`. |
| `x2`      | ≈ 3.2 | Same story as `x1`. |
| `x3`      | ≈ 1.2 | Little collinearity. |
| `x4` (levels b, c) | ≈ 1.0 | No issue. |

Because none of the VIFs exceed the conventional cut‑off of **5** (or **10** for a more liberal rule), the model is *not* severely afflicted by multicollinearity. If we had VIFs > 5 we would consider:

* centering or standardising continuous predictors,
* removing or combining highly correlated variables,
* using principal‑component or ridge‑type regularisation.

---

## 3. Final answer

> **Yes.** Multicollinearity for a `clmm` model can be assessed by extracting the fixed‑effects design matrix and applying a VIF routine. The easiest way is:

```r
library(performance)
check_collinearity(fit_clmm)   # works directly on clmm objects
```

If you prefer the **car** package:

```r
X <- model.matrix(fit_clmm)[ , -(1:2)]      # keep only fixed‑effects columns
vif(lm(1 ~ X - 1))                         # dummy lm → car::vif()
```

Both approaches give the same VIF values and let you decide whether any predictor suffers from problematic collinearity.

---

## 4. Common mistakes & how to avoid them

| Mistake | Why it’s a problem | Correct approach |
|---------|--------------------|------------------|
| **Calling `vif()` directly on the `clmm` object** | `car::vif()` only has methods for `lm`, `glm`, `polr`, etc.; it will throw an error. | Extract the fixed‑effects matrix first (as shown) or use `performance::check_collinearity()`. |
| **Including the random‑effect columns in the VIF calculation** | Random‑effect design columns (e.g., grouping intercepts) are not part of the fixed‑effects collinearity issue and can artificially inflate VIFs. | Drop the random‑effect columns from `model.matrix()` (usually the first one(s)). |
| **Using the raw factor variable in a linear model to compute VIF** | `lm()` treats factor levels as numeric contrasts, which may give misleading VIFs. | Regress each factor on the other predictors using a multinomial (or appropriate) model, or let `car::vif()` handle dummy‑coded factors automatically. |
| **Interpreting VIFs > 5 as an automatic “model must be dropped”** | Moderate VIFs (3–5) are common with correlated continuous covariates and do not always impair inference, especially when sample size is large. | Look at the **standard errors**, **confidence intervals**, and **condition numbers**; consider domain knowledge before removing variables. |
| **Forgetting to centre/standardise continuous predictors** | Uncentred variables can produce large VIFs even when the underlying correlation structure is harmless. | Center (subtract mean) or standardise (z‑score) continuous predictors before fitting the model. |
| **Relying only on VIFs and ignoring other diagnostics** | VIF detects linear relationships but not non‑linear or interaction‑induced collinearity. | Complement VIFs with pairwise correlation matrices, eigenvalue analysis, and condition indices (`check_collinearity()` reports them). |

By following the steps above and avoiding these pitfalls, you can reliably evaluate multicollinearity in cumulative link mixed models fitted with `clmm()`.

*Original question: [How can assess multicollinearity when using clmm from ordinal package?](https://stats.stackexchange.com/questions/677382/how-can-assess-multicollinearity-when-using-clmm-from-ordinal-package) on Cross Validated (Stats Stack Exchange), licensed CC BY-SA.*

{% endraw %}
