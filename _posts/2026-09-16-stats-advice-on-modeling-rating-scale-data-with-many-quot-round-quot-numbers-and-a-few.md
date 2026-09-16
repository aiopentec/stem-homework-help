---
layout: question
title: Advice on modeling rating scale data with many &quot;round&quot; numbers and
  a few in between?
author: StemFix Bot
category: stats
subject: stats
description: 'Step-by-step statistics solution: Advice on modeling rating scale data
  with many &quot;round&quot; numbers and a few in between?'
tags:
- stats
---

{% raw %}
*As an Amazon Associate, I earn from qualifying purchases.* For more practice problems like this, see [Schaum's Outline of Statistics, 6th Edition](https://www.amazon.com/dp/1260011461?tag=aiopentec20-20).

---

## 1.  What the student is asking (in plain language)

A tasting panel scored many fruit samples on a **0–15** scale, with the possibility of recording scores to the **nearest 0.1**.  
In reality the panelists almost always used “round” numbers:

* 72 % of the scores end in **.0**  
* 13 % end in **.5**  
* the remaining ~15 % are spread over the other nine decimal places.

The student wants to analyse these scores with a **mixed‑effects model** (panelists and/or fruits are random effects).  

Two ideas have been suggested:

1. **Scale to (0, 1)**, add a tiny constant to avoid exact zeros, and fit a **Beta GLMM** (perhaps with a hurdle for the zeros).
2. **Round the data** to the nearest whole number or 0.5 and fit a **cumulative‑logit (proportional‑odds) ordinal GLMM**.

The question is: **Which approach (if any) is appropriate, and what other modelling options should be considered?**  

Below is a step‑by‑step worked solution that evaluates the options, explains why a third “latent‑continuous‑with‑rounding” model is often the most sensible, and shows how to fit it in R (or in a Bayesian framework).  

---

## 2.  Step‑by‑step reasoning and modelling guide  

### Step 1 – Understand the measurement process  

| What the panelists see | What they record | What we observe |
|------------------------|------------------|-----------------|
| A **continuous** sensory intensity that could in principle take any value between 0 and 15 | A **decision rule**: they choose a value on a 0‑15 scale, but they tend to pick “round” numbers (0, 0.5, 1, 1.5, …) because that is easier for them. | A **discrete** set of numbers, heavily clustered at the round values. |

Statistically we can think of an *unobserved latent continuous* variable \(Y^\ast\) that the panelist actually perceives, and a *rounding rule* that maps \(Y^\ast\) to the recorded score \(Y\).  
If we ignore the rounding rule and treat the recorded scores as truly continuous, we will mis‑represent the measurement error and inflate apparent “precision”.  

**Key point:** the data are *ordinal* (they have a natural order) **and** they are *rounded* versions of an underlying continuous sensation.

---

### Step 2 – Examine the data (diagnostics)

```r
library(ggplot2)
ggplot(df, aes(x = score)) + 
  geom_histogram(binwidth = 0.1, colour = "black", fill = "lightblue") +
  labs(title = "Histogram of raw scores (0–15, step = 0.1)",
       x = "Score", y = "Count")
```

* Look at the **frequency of each decimal part** (the table the student already produced).  
* Check for **excess zeros** – here the zero‑frequency is 7 % (0.0 is a round value, not a true zero‑inflation problem).  
* Plot **panelist‑by‑panelist** histograms to see whether the tendency to use round numbers is consistent across people.

If the pattern of rounding is similar for all panelists, a *single* rounding mechanism can be assumed; if it varies, you may need panelist‑specific thresholds (more complex, see later).

---

### Step 3 – Why the two proposed options are not ideal  

| Option | How it treats the data | Problems |
|--------|------------------------|----------|
| **Beta GLMM on (score/15)** (maybe with hurdle) | Assumes the response is a *continuous proportion* on \((0,1)\) with a smooth density. | • The Beta distribution cannot generate the massive spikes at .0, .5, .1, … <br>• Adding a constant (e.g., 0.1) to avoid zeros is arbitrary and changes the scale. <br>• A hurdle for zeros is unnecessary because 0 is just another round value, not a “structural zero”. |
| **Round to nearest integer / 0.5 and fit a proportional‑odds ordinal GLMM** | Treats the outcome as *ordinal* with a modest number of categories (16 or 31). | • Rounding discards information about the *exact* decimal part for the 15 % of observations that are not round. <br>• The proportional‑odds model assumes **equal spacing of the underlying latent thresholds**, which may be violated when the data are heavily rounded (the latent thresholds are not equally spaced). <br>• The model does not explicitly acknowledge the rounding mechanism, so standard errors can be biased. |

Both approaches *ignore the measurement process* (i.e., the rounding) and therefore risk biased inference, especially for fixed‑effect estimates that are of primary interest (e.g., differences among fruit varieties).

---

### Step 4 – A more principled model: **Latent‑continuous with rounding (a “rounded” or “censored” model)**  

#### 4.1  Conceptual model  

1. **Latent variable** \(Y_{ij}^\ast\) (continuous, e.g., Normal) represents the true sensory intensity for observation \(i\) of panelist \(j\).  

   \[
   Y_{ij}^\ast = \mathbf{x}_{ij}^\top\beta + \mathbf{z}_{ij}^\top b_j + \varepsilon_{ij},
   \qquad \varepsilon_{ij}\sim N(0,\sigma^2)
   \]

   *\(\mathbf{x}_{ij}\)* = fixed‑effect covariates (variety, replicate, etc.)  
   *\(\mathbf{z}_{ij}\)* = design matrix for random effects (panelist, fruit, etc.)  

2. **Rounding rule**: the observed score \(Y_{ij}\) is the result of rounding \(Y_{ij}^\ast\) to the nearest 0.1, but with a *bias* toward multiples of 0.5. A simple way to encode this is to define **cut‑points** \(c_k\) that separate the observed categories.

   For a standard “round‑to‑nearest‑0.1” rule the cut‑points are at …, \(-0.05, 0.05, 0.15, 0.25, \dots, 14.95, 15.05\).  

   To capture the extra preference for .0 and .5 we can **inflate** the widths of the intervals around those values (e.g., make the interval \([0.45,0.55]\) a little wider). This is equivalent to estimating **unequal thresholds**.

3. **Likelihood**:  

   \[
   \Pr(Y_{ij}=k) = \Phi\!\bigl(\frac{c_{k+1}-\eta_{ij}}{\sigma}\bigr)
                - \Phi\!\bigl(\frac{c_{k}  -\eta_{ij}}{\sigma}\bigr),
   \]
   where \(\eta_{ij}= \mathbf{x}_{ij}^\top\beta + \mathbf{z}_{ij}^\top b_j\) and \(\Phi\) is the standard normal CDF.

   This is precisely a **cumulative probit model** (or logit if you use the logistic CDF) **with unequal thresholds**, i.e. an **ordinal mixed model** that *explicitly* models the spacing of the categories.  

   When the thresholds are *estimated* rather than forced to be equally spaced, the model automatically accounts for the “spikes” at .0, .5, etc.

#### 4.2  Implementation options  

| Platform | Typical function | How to specify unequal thresholds |
|----------|------------------|-----------------------------------|
| **R – `ordinal` package** | `clmm` (cumulative link mixed model) | Use `threshold = "flexible"` (default) → thresholds are estimated freely. |
| **R – `brms` (Bayesian)** | `brm` with `family = cumulative("logit")` or `"probit"` | Set `threshold = "flexible"`; the model will estimate a separate cut‑point for each observed score. |
| **R – `glmmTMB`** | `glmmTMB(..., family = truncated_poisson(...))` not needed here. | Not directly suited for ordinal with flexible thresholds. |
| **Stata / SAS / SPSS** | `gsem` or `proc mixed` with `link=logit` | Provide the full list of cut‑points. |

**Why this works:**  
- The *latent* variable is continuous, so all the usual GLMM machinery (random effects, covariates, heteroskedasticity) is available.  
- The *unequal thresholds* absorb the irregular spacing created by the panelists’ rounding bias.  
- No arbitrary constant is added, and zeros are treated just like any other category.

#### 4.3  Example in R (frequentist)

```r
library(ordinal)   # for clmm()
# Assume df has columns:
#   score   : observed rating (0, 0.1, …, 15)
#   variety : factor for fruit variety
#   panel   : factor for panelist (random effect)
#   replicate : numeric or factor for replicate

# Convert to an ordered factor (necessary for clmm)
df$score_ord <- ordered(df$score, levels = sort(unique(df$score)))

# Fit cumulative probit mixed model with flexible thresholds
fit <- clmm(score_ord ~ variety + (1|panel) + (1|replicate),
            data = df,
            link = "probit",          # or "logit"
            threshold = "flexible")   # default, but explicit

summary(fit)
```

*Output interpretation*  
- **Fixed‑effects** (`variety`): differences on the latent scale (in probit units).  
- **Random‑effects variance** (`panel`, `replicate`): how much panelists / replicates deviate from the overall latent mean.  
- **Threshold estimates** (`theta1`, `theta2`, …): the cut‑points that map the latent variable onto the observed rating categories. Large gaps between successive thresholds will correspond to the “spikes” at .0, .5, etc.

#### 4.4  Example in R (Bayesian with `brms`)

```r
library(brms)

# Define the formula
form <- bf(score_ord ~ variety + (1|panel) + (1|replicate))

# Fit cumulative probit model with flexible thresholds
fit_bayes <- brm(formula = form,
                 data    = df,
                 family  = cumulative("probit"),
                 prior   = c(set_prior("normal(0,5)", class = "b"),
                             set_prior("student_t(3,0,2)", class = "sd")),
                 iter    = 4000, warmup = 1000, chains = 4,
                 control = list(adapt_delta = 0.95))

summary(fit_bayes)
```

The Bayesian approach gives full posterior distributions for thresholds, making it easy to check whether the intervals around .0 and .5 are indeed larger than the others.

#### 4.5  Model checking  

1. **Posterior predictive checks / simulated residuals**  
   - In `brms`: `pp_check(fit_bayes, ndraws = 100)`.  
   - In `ordinal`: `residuals(fit, type = "pearson")` and plot vs. fitted.  

2. **Compare to naive models**  
   - Fit a simple Gaussian LMM (`lmer(score ~ ... )`).  
   - Fit the Beta GLMM the student suggested (`glmmTMB(score/15 ~ ... , family = beta)`).  
   - Use AIC, BIC, or LOO‑CV (for Bayesian) to see which model predicts the observed distribution best.  

   You will typically find that the *latent‑continuous‑with‑rounded* model has dramatically lower deviance and reproduces the spikes.

3. **Check proportional‑odds assumption** (if you used a logit link).  
   - `nominal_test(fit)` in `ordinal` or `brms::hypothesis()` can test whether thresholds are parallel.  
   - If violated, you can relax it by allowing **varying slopes across thresholds** (`clmm2` in `ordinal` or `brms` with `gr()` interaction).

---

### Step 5 – When (and how) to use the other two ideas  

| Situation | Recommended model | Rationale

*Original question: [Advice on modeling rating scale data with many &quot;round&quot; numbers and a few in between?](https://stats.stackexchange.com/questions/677145/advice-on-modeling-rating-scale-data-with-many-round-numbers-and-a-few-in-betw) on Cross Validated (Stats Stack Exchange), licensed CC BY-SA.*

{% endraw %}
