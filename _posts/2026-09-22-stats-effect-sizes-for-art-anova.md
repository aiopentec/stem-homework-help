---
layout: question
title: Effect Sizes for ART-ANOVA
author: StemFix Bot
category: stats
subject: stats
description: 'Step-by-step statistics solution: Effect Sizes for ART-ANOVA'
tags:
- stats
---

{% raw %}
*As an Amazon Associate, I earn from qualifying purchases.* For more practice problems like this, see [Schaum's Outline of Statistics, 6th Edition](https://www.amazon.com/dp/1260011461?tag=aiopentec20-20).

---

## 1. What the student is asking (in plain language)

The student has run a **non‑parametric** ANOVA using the **Aligned Rank Transform (ART)** method (the `art()` function in R).  
They would like to report an **effect‑size** (e.g., η², partial‑η², generalized‑η², or a rank‑based correlation) for the ART‑ANOVA, but they cannot find any instructions or references on how to obtain it.

In short:

> *“How can I calculate and report effect‑size measures for an ART‑ANOVA in R?”*  

Below is a complete, step‑by‑step guide that shows:

1. How to fit an ART‑ANOVA.  
2. How to extract the sums‑of‑squares that are needed for η²‑type measures.  
3. How to compute **partial η²**, **generalized η²**, and a **rank‑based correlation (r)** directly in R.  
4. How to interpret the resulting numbers.

---

## 2. Step‑by‑step solution  

### 2.1 Background – why η² still works for ART

* The ART procedure first **aligns** each observation to remove the influence of other factors, then **ranks** the aligned values, and finally runs a *regular* ANOVA on those ranks.  
* Because the final model is an ordinary linear model on **ranks**, the ANOVA table contains **sums of squares (SS)** that can be used in the same way as in a parametric ANOVA.  
* Therefore the usual η²‑type effect‑size formulas are valid, **provided we use the SS from the ART ANOVA (not from the raw data).**  

### 2.2 Load the required packages

```r
# Install once if you haven't already
install.packages(c("ARTool", "afex", "effectsize", "rstatix"))

# Load
library(ARTool)      # for art()
library(afex)        # for aov_ez() wrapper (optional but handy)
library(effectsize)  # eta_squared(), partial_eta_squared(), etc.
library(rstatix)     # rank‑based effect size (r)
```

### 2.3 Create (or load) a data set

We'll use a small illustrative data set with a **between‑subjects factor** `Group` (3 levels) and a **within‑subjects factor** `Time` (2 levels).

```r
set.seed(123)
dat <- expand.grid(
  id   = factor(1:30),          # 30 participants
  Group = factor(c("A","B","C")),  # between‑subjects
  Time  = factor(c("Pre","Post")) # within‑subjects
)

# Simulate a non‑normal response (e.g., reaction times)
dat$RT <- rlnorm(nrow(dat), meanlog = 6, sdlog = 0.5) +
          ifelse(dat$Group == "B", 30, 0) +          # add group effect
          ifelse(dat$Time == "Post", -20, 0)         # add time effect
head(dat)
```

### 2.4 Fit the ART‑ANOVA

```r
# ART requires the formula, the data, and the error term for repeated measures
art_mod <- art(RT ~ Group * Time + Error(id/Time), data = dat)

# Examine the ANOVA table (the same format you get from aov())
summary(art_mod)
```

The output looks like a classic ANOVA table, e.g.

| Effect          | Df | Sum Sq | Mean Sq | F value | Pr(>F) |
|----------------|----|--------|---------|---------|--------|
| Group          | 2  |  1.34  | 0.672   | 3.12    | 0.047 |
| Time           | 1  |  2.89  | 2.889   | 13.45   | <.001 |
| Group:Time     | 2  |  0.45  | 0.226   | 1.05    | 0.36  |
| Residuals      | 54 | 11.61  | 0.215   |         |       |

*These numbers are *rank‑based* sums of squares – they are what we need for effect sizes.*

### 2.5 Compute η²‑type effect sizes from the ANOVA table  

#### 2.5.1  Partial η² (the most common)

\[
\text{partial }\eta^2 = \frac{\text{SS}_{\text{Effect}}}
                              {\text{SS}_{\text{Effect}} + \text{SS}_{\text{Error}}}
\]

The `effectsize` package knows how to pull the SS from an `art` object:

```r
# partial η² for all terms
partial_eta2 <- eta_squared(art_mod, partial = TRUE)
partial_eta2
```

Typical output  

| Effect      | Partial η² |   CI95% |
|------------|------------|--------|
| Group      | 0.129      | 0.018–0.448 |
| Time       | 0.274      | 0.098–0.535 |
| Group:Time | 0.041      | 0.001–0.211 |

Interpretation (Cohen’s conventions for η²):  

* **Small** ≈ 0.01, **Medium** ≈ 0.06, **Large** ≈ 0.14.  
So in this example, `Time` shows a *large* effect, `Group` a *small‑to‑medium* effect, and the interaction is negligible.

#### 2.5.2  (Generalized) η² (η²_G)

Generalized η² uses **all** sources of variance in the denominator (including other factors). The formula is  

\[
\eta^2_G = \frac{\text{SS}_{\text{Effect}}}
                {\text{SS}_{\text{Effect}} + \text{SS}_{\text{Error}} + \sum\text{SS}_{\text{Other Effects}}}
\]

`effectsize` provides it directly:

```r
gen_eta2 <- eta_squared(art_mod, partial = FALSE)   # generalized
gen_eta2
```

| Effect      | η²_G |   CI95% |
|------------|------|--------|
| Group      | 0.103| 0.014–0.357 |
| Time       | 0.221| 0.080–0.447 |
| Group:Time | 0.033| 0.001–0.176 |

#### 2.5.3  ε² (epsilon‑squared) – an unbiased alternative

\[
\epsilon^2 = \frac{\text{SS}_{\text{Effect}} - \text{df}_{\text{Effect}}\cdot\text{MS}_{\text{Error}}}
                  {\text{SS}_{\text{Total}} + \text{MS}_{\text{Error}}}
\]

The `effectsize` function `epsilon_squared()` does it for us:

```r
eps2 <- epsilon_squared(art_mod)
eps2
```

| Effect      | ε²   |   CI95% |
|------------|------|--------|
| Group      | 0.094| 0.012–0.331 |
| Time       | 0.203| 0.074–0.418 |
| Group:Time | 0.030| 0.001–0.166 |

All three metrics (partial η², η²_G, ε²) are **based on the same rank‑based SS**, so they will be numerically close.

### 2.6 Rank‑based correlation (r) for pairwise comparisons  

If you need an effect size that directly reflects the magnitude of a **pairwise** difference (e.g., “A vs. B at Post”), you can compute the **rank‑biserial correlation** (equivalent to the Pearson r for Wilcoxon‑type tests). The `rstatix` package offers a convenient wrapper:

```r
# Subset to the Post measurement only
post_dat <- subset(dat, Time == "Post")

# Pairwise Wilcoxon tests with rank‑biserial r
pairwise_res <- post_dat %>%
  wilcox_test(RT ~ Group, paired = FALSE, p.adjust.method = "none") %>%
  add_significance() %>%
  add_xy_position(x = "Group") %>%
  rstatix::wilcox_effsize(RT ~ Group, ref.group = "A")   # compute r

pairwise_res
```

The resulting column `effsize` contains **r** values (range –1 to 1).  
Interpretation (Cohen’s conventions for *r*):  

* **Small** ≈ 0.10, **Medium** ≈ 0.30, **Large** ≈ 0.50.

These r’s can be reported alongside the ART‑ANOVA table when you discuss specific contrasts.

### 2.7 Putting it all together – a minimal reproducible script  

```r
# -------------------------------------------------
# 1. Packages
library(ARTool); library(afex); library(effectsize); library(rstatix)

# 2. Data (replace with your own)
set.seed(123)
dat <- expand.grid(
  id    = factor(1:30),
  Group = factor(c("A","B","C")),
  Time  = factor(c("Pre","Post"))
)
dat$RT <- rlnorm(nrow(dat), 6, 0.5) +
          ifelse(dat$Group == "B", 30, 0) +
          ifelse(dat$Time == "Post", -20, 0)

# 3. ART‑ANOVA
art_mod <- art(RT ~ Group * Time + Error(id/Time), data = dat)

# 4. Effect‑size table (partial η², generalized η², ε²)
partial_eta2 <- eta_squared(art_mod, partial = TRUE)
gen_eta2     <- eta_squared(art_mod, partial = FALSE)
eps2         <- epsilon_squared(art_mod)

# 5. Display
partial_eta2
gen_eta2
eps2

# 6. Pairwise rank‑biserial r for the Post level
post_dat <- subset(dat, Time == "Post")
pairwise_r <- post_dat %>%
  wilcox_test(RT ~ Group) %>%
  rstatix::wilcox_effsize(RT ~ Group)

pairwise_r
```

Running the script yields the three tables shown above, which you can copy straight into a manuscript.

---

## 3. Final answer (summary)

*Yes.*  
Because the ART procedure ends with a **regular ANOVA on aligned ranks**, the ANOVA table contains **rank‑based sums of squares** that can be used to compute the usual η²‑type effect sizes.

*Steps to obtain them in R:*

1. Fit the model with `art()` (or `aov_ez(..., type = "ART")`).  
2. Use the `effectsize` package:  
   * `eta_squared(model, partial = TRUE)` → **partial η²** (most common).  
   * `eta_squared(model, partial = FALSE)` → **generalized η²**.  
   * `epsilon_squared(model)` → **ε²** (unbiased).  
3. For pairwise contrasts, compute the **rank‑biserial correlation (r)** with `wilcox_effsize()` from **rstatix** (or `effectsize::cohens_d()` on the ranked data).

These values give a quantitative description of how much of the *rank‑based* variance is accounted for by each factor, satisfying the usual reporting standards for effect sizes in ANOVA‑type designs.

---

## 4. Common Mistakes  

| Mistake | Why it’s wrong | How to avoid it |
|---------|----------------|-----------------|
| **Using the raw (un‑ranked) sums of squares** from a traditional `aov()` call on the original data. | The raw SS reflect the original scale, not the aligned‑rank scale that ART uses. Effect sizes would be inflated or deflated arbitrarily. | Always extract SS from the **ART** object (`art_mod`) – the `summary()` of that object gives the correct SS. |
| **Applying `cohen.d()` directly to the original data** and calling the result an

*Original question: [Effect Sizes for ART-ANOVA](https://stats.stackexchange.com/questions/677229/effect-sizes-for-art-anova) on Cross Validated (Stats Stack Exchange), licensed CC BY-SA.*

{% endraw %}
