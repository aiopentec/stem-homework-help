---
layout: question
title: Choosing an appropriate mixed-effects model for ordinal data
author: StemFix Bot
category: stats
subject: stats
description: 'Step-by-step statistics solution: Choosing an appropriate mixed-effects
  model for ordinal data'
tags:
- stats
---

{% raw %}
*As an Amazon Associate, I earn from qualifying purchases.* For more practice problems like this, see [Schaum's Outline of Statistics, 6th Edition](https://www.amazon.com/dp/1260011461?tag=aiopentec20-20).

---

## 1.  What the student is asking – in plain language  

The student has a **four‑level ordinal outcome** (severity score = 0, 1, 2, 3) that was measured repeatedly on the same individuals.  
The experimental design is a *randomized block split‑plot* with  

* two **groups** (e.g., treatment vs. control),  
* two **years**, and  
* three **sub‑treatments** inside each block.  

The intended mixed‑effects model was a **cumulative‑link mixed model (CLMM)**  

\[
\text{Score}\sim \text{Group}\times\text{Year}\times\text{Treatment} 
               + (1\mid\text{Block}) + (1\mid\text{Block:Treatment}) 
               + (1\mid\text{Individual\_ID}),
\]

but the fit failed (singular Hessian, non‑convergence) because the higher score categories are very sparse, especially in one group.  

The student wonders whether it would be acceptable to **treat the ordinal score as a count** and fit a **Poisson GLMM** with the same fixed‑ and random‑effects structure, because the primary scientific question is the three‑way interaction *Group × Year × Treatment*.

The question is therefore:

> **Is a Poisson GLMM a defensible alternative for an ordinal 0–3 response, or should we stay with an ordinal model (or another approach) despite the convergence problems?**  

---

## 2.  Step‑by‑step reasoning  

Below we walk through the logic that a knowledgeable statistician would use to answer the question.  
Each step is written out explicitly so that no “obvious” jumps are left out.

### Step 1 – Clarify the nature of the response variable  

| Property | Ordinal (0–3) | Poisson count |
|----------|---------------|---------------|
| **Ordering** | Yes (0 < 1 < 2 < 3) | Not required; assumes a natural ordering of counts |
| **Equal spacing** | *Not* assumed (the distance between 0 and 1 may not equal the distance between 2 and 3) | Implicitly assumes each unit increase is the same “size” |
| **Upper bound** | Fixed at 3 | No theoretical upper bound (Poisson can generate arbitrarily large counts) |
| **Distribution shape** | Often skewed, with a mass at low values, but the shape is dictated by the cumulative probabilities of the underlying latent variable | Poisson mean = variance, right‑skewed, unbounded |

Because the outcome is *bounded* and *unequally spaced*, the Poisson model **mis‑specifies the data‑generating process** unless you can argue that the numeric values truly represent counts of independent events (which they do not here).  

### Step 2 – What does a CLMM do?  

A cumulative‑link mixed model (also called a proportional‑odds mixed model) assumes that there is an unobserved continuous latent variable \(Y^*\) such that  

\[
\text{Score}=k \;\;\Longleftrightarrow\;\;
\kappa_{k-1}<Y^*\le \kappa_{k},
\qquad k=0,1,2,3,
\]

with cut‑points \(\kappa_{-1}=-\infty\) and \(\kappa_{3}=+\infty\).  

The model for the latent variable is linear:

\[
Y^* = \mathbf{x}^{\top}\boldsymbol\beta + b_{\text{Block}} + b_{\text{Block:Treatment}} + b_{\text{Individual}} + \varepsilon,
\]

where \(\varepsilon\) follows a logistic (or normal) distribution, giving a **cumulative link** (logit, probit, etc.).  

Advantages:

* Respects the ordering and boundedness.  
* Provides interpretable odds‑ratios for *cumulative* probabilities.  
* Random effects naturally model the split‑plot structure.

The main *practical* difficulty is fitting the model when some categories contain very few observations.  

### Step 3 – Diagnose why the CLMM failed  

Typical reasons for a *singular Hessian* or *non‑convergence* in CLMMs are:

| Reason | What to check | Remedy |
|--------|----------------|--------|
| **Sparse categories** (few or zero counts in some cells) | Cross‑tabulate Score × Group × Year × Treatment. Look for cells with 0 or 1 observations. | Collapse adjacent categories (e.g., combine 2 & 3) or drop interaction terms that create empty cells. |
| **Over‑parameterised random‑effects** | Compare the number of levels of each random factor to the number of observations. | Simplify random structure: maybe keep only (1|Block) and (1|Individual) and drop (1|Block:Treatment) if it is near‑singular. |
| **Separation** (perfect prediction) | Fit a simple cumulative‑logit without random effects; see if any predictor perfectly predicts a cut‑point. | Use penalised likelihood (e.g., `brglm2`, `glmnet`) or Bayesian priors to regularise. |
| **Scaling / identifiability** | Inspect the estimated cut‑points; they may be extremely far apart. | Rescale predictors (centre, standardise) or re‑parameterise the model. |

**Practical first step**: run a *plain* cumulative‑logit (no random effects) to see whether the fixed‑effects structure is estimable at all. If that works, the problem is likely the random‑effects specification.

### Step 4 – Consider alternative ordinal mixed models  

1. **`glmmTMB` with `family = cumulative(link = "logit")`**  
   *Uses Laplace approximation but often converges where `ordinal::clmm` fails.*  

2. **Bayesian ordinal mixed model (`brms` or `MCMCglmm`)**  
   *Place weakly informative priors on cut‑points and variance components. The MCMC sampler can navigate near‑singular likelihoods.*  

3. **Continuation‑ratio or adjacent‑category models** (`ordinal`, `VGAM`)  
   *If the proportional‑odds assumption is doubtful, these link functions relax it.*  

4. **Collapsing categories**  
   *If scores 2 and 3 are very rare, combine them into a single “high” category, yielding a three‑level ordinal response (0, 1, ≥ 2). This often restores identifiability.*  

### Step 5 – When (if ever) is a Poisson GLMM acceptable for ordinal data?  

A Poisson GLMM **can be defensible** only under very specific circumstances:

| Condition | Reason it may work |
|-----------|-------------------|
| The numeric values truly represent *counts* of independent events (e.g., number of lesions). | The Poisson assumption (mean = variance, unbounded support) is then appropriate. |
| The distribution of the outcome roughly follows a Poisson shape (variance ≈ mean) and the upper bound (3) is not binding (i.e., observed counts never reach the bound). | The misspecification is minor. |
| You are willing to accept *approximate* inference (e.g., use robust sandwich SEs) and you *only* need a quick test of the interaction. | May be used as a pragmatic “working” model. |

In the present case:

* The score is **designed as a severity rating**, not a count of events.  
* The maximum of 3 is an *intrinsic ceiling*; a Poisson model would assign non‑zero probability to scores ≥ 4, which is impossible.  
* The observed distribution is heavily skewed toward 0 and 1, violating the Poisson mean‑variance equality.

Hence, **the Poisson GLMM is not a defensible primary analysis**. It could be used *only* as a sensitivity check, but the interpretation of the interaction would be on a different scale (log‑mean counts) and would not respect the ordinal nature of the data.

### Step 6 – Recommended analysis workflow  

Below is a concrete, reproducible workflow (R‑style code snippets are provided for illustration; any equivalent software can be used).

1. **Inspect the data**  

   ```r
   library(dplyr)
   table(df$Score, df$Group, df$Year, df$Treatment)
   ```

   Look for empty cells.

2. **If sparsity is severe, collapse the top categories**  

   ```r
   df <- df %>%
     mutate(Score3 = ifelse(Score == 3, 2, Score))   # now 0,1,2
   ```

3. **Fit a simple cumulative‑logit without random effects**  

   ```r
   library(MASS)
   fit0 <- polr(Score3 ~ Group*Year*Treatment, data = df, Hess = TRUE)
   summary(fit0)
   ```

   *If this converges, proceed; if not, consider dropping the three‑way interaction.*

4. **Fit an ordinal mixed model with a simpler random‑effects structure**  

   ```r
   library(glmmTMB)
   fit1 <- glmmTMB(Score3 ~ Group*Year*Treatment +
                   (1|Block) + (1|Individual_ID),
                   data = df,
                   family = cumulative(link = "logit"))
   summary(fit1)
   ```

   *Check convergence warnings and the variance estimates. If any variance component is estimated as (near) zero, drop that random effect.*

5. **If glmmTMB still fails, move to a Bayesian approach**  

   ```r
   library(brms)
   prior <- c(set_prior("normal(0,5)", class = "b"),
              set_prior("student_t(3,0,10)", class = "sd"))
   fit2 <- brm(Score3 | trials(1) ~ Group*Year*Treatment +
               (1|Block) + (1|Individual_ID),
               data = df,
               family = cumulative(link = "logit"),
               prior = prior,
               iter = 4000, warmup = 1000, chains = 4,
               control = list(adapt_delta = 0.95))
   ```

   *Inspect `summary(fit2)` and the posterior of the three‑way interaction. The Bayesian model will usually converge even with sparse cells because the priors regularise the cut‑points.*

6. **Assess model fit**  

   * Posterior predictive checks (bayesplot) or residual plots (DHARMa) to ensure the ordinal structure is respected.  
   * Compare models with `loo()` or `WAIC` if multiple specifications are tried.

7. **Interpret the Group × Year × Treatment interaction**  

   * In the cumulative‑odds framework, the interaction tells you how the *log‑odds* of being at or above a given severity level differ across the three factors.  
   * Present results as **odds‑ratio plots** for each cut‑point, or compute *predicted probabilities* for the original four levels (if you kept the 0–3 coding).

### Step 7 – Summarise the final recommendation  

| Question | Answer |
|----------|--------|
| **Can I replace the CLMM with a Poisson GLMM?** | **No**, not as a primary analysis. The Poisson model ignores the bounded, unordered nature of the data and will give biased estimates and misleading inference. |
| **What should I do instead?** | 1. Reduce sparsity (collapse top categories). <br>2. Simplify the random‑effects structure. <br>3. Fit an ordinal mixed model using `glmmTMB` (or `ordinal::clmm`) or a Bayesian ordinal mixed model (`brms`). <br>4. If convergence still fails, consider penalised likelihood or a different link (continuation‑ratio). |
| **Is a Poisson GLMM ever useful here?** | Only as a **sensitivity check** (e.g., to see whether the interaction remains significant) but not for reporting final scientific conclusions. |

---

## 3.  Final answer  

A Poisson GLMM is **not a defensible alternative** for a four‑level ordinal severity score. The ordinal nature (ordered, bounded, unequal spacing) violates the assumptions of a Poisson count model, and using it would produce biased parameter estimates and misleading inference about the Group × Year × Treatment interaction.

The appropriate route is to **stay with an ordinal mixed model**, but to resolve the convergence problems by:

1. **Collapsing sparse categories** (e.g., combine scores 2 and 3).  
2. **Simplifying the random‑effects structure** (

*Original question: [Choosing an appropriate mixed-effects model for ordinal data](https://stats.stackexchange.com/questions/676991/choosing-an-appropriate-mixed-effects-model-for-ordinal-data) on Cross Validated (Stats Stack Exchange), licensed CC BY-SA.*

{% endraw %}
