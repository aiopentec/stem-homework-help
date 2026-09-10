---
layout: question
title: What Mixed Model do I need to use for my analysis?
author: StemFix Bot
category: stats
subject: stats
description: 'Step-by-step statistics solution: What Mixed Model do I need to use
  for my analysis?'
tags:
- stats
---

{% raw %}
*As an Amazon Associate, I earn from qualifying purchases.* For more practice problems like this, see [Schaum's Outline of Statistics, 6th Edition](https://www.amazon.com/dp/1260011461?tag=aiopentec20-20).

---

## 1.  Restating the problem in plain language  

You have ecological measurements (e.g., **sd_depth**) taken from several **countries**.  
Within each country there are two **grazing treatments** (grazed vs. ungrazed).  
Each treatment is replicated on **5 plots**, and each plot contains several **sub‑plots** (the “pseudoreplicates”).  

You want to know, for every country, whether the grazing treatment influences the response variable.  
Because the sub‑plots are not independent, you plan to use a **mixed‑effects model** with a random effect for *Plot*.  

You tried a linear mixed model (LMM) on the raw data, the residuals were clearly non‑normal, so you log‑transformed the response and refit:

```r
model <- lmer(log(sd_depth) ~ Grazing * Country + (1 | PlotID), data = sd_data)
```

The QQ‑plot now looks acceptable, but a formal Shapiro‑Wilk test on the residuals gives **p = 0.01** (i.e. rejects normality at the 5 % level).

**Questions**

1. Is the significant Shapiro‑Wilk p‑value a reason to *reject* the LMM and look for another model?  
2. If a different model is needed, which type of GLMM (distribution, link) would be appropriate?  
3. What other assumptions (besides residual normality) must be checked for LMMs or GLMMs?

---

## 2.  Step‑by‑step solution  

### Step 1 – Clarify the hierarchy and the appropriate random‑effects structure  

| Level | Description |
|-------|-------------|
| **Country** | Fixed effect (you want a separate grazing effect for each country). |
| **Grazing** | Fixed effect (treatment). |
| **Plot** | Nested within Country × Grazing (5 plots per treatment per country). Treated as a random intercept because the plots are a random sample of all possible plots. |
| **Sub‑plot (pseudoreplicate)** | Repeated measurements within a plot. If the sub‑plots are truly *replicates* (i.e. you measured the same variable on independent sub‑units), you can treat them as *observations* and let the random intercept for Plot absorb the within‑plot correlation. If you have a second level of nesting (e.g., sub‑plot IDs), you could add another random term `(1|PlotID/SubplotID)`.

**Model formula** (baseline)

```r
lmer( log(sd_depth) ~ Grazing * Country + (1 | PlotID), data = sd_data )
```

If you have a second nesting level:

```r
lmer( log(sd_depth) ~ Grazing * Country + (1 | PlotID) + (1 | PlotID:SubplotID), data = sd_data )
```

### Step 2 – Diagnose the LMM  

1. **Residual normality**  
   * Visual checks (QQ‑plot, histogram) are more informative than a single Shapiro‑Wilk test.  
   * The Shapiro‑Wilk test is *very* sensitive when you have many residuals (it will often reject even tiny deviations).  
   * With mixed models the residuals are **conditional** (i.e., after removing the fitted random effects). The test is applied to these residuals, not to the raw data.

2. **Homoscedasticity (constant variance)**  
   * Plot residuals vs. fitted values. Look for funnel shapes or systematic patterns.  

3. **Independence**  
   * Because you have a random intercept for Plot, the within‑plot correlation should be accounted for. Check the *intraclass correlation* (ICC) to see whether the random effect explains a substantial proportion of variance.  

4. **Influential observations / outliers**  
   * Use `influence.ME` or `dfbeta`‑type diagnostics.  

5. **Model convergence**  
   * Verify that the optimizer converged (`summary(model)$optinfo$conv`).  

### Step 3 – Decide whether the LMM is “good enough”

- **Rule of thumb:** If the residuals are *approximately* normal (no extreme skewness/kurtosis, QQ‑plot follows a straight line) and the variance looks roughly constant, the LMM is usually robust.  
- **Statistical evidence:** The Shapiro‑Wilk p‑value = 0.01 indicates a statistically significant departure, but practical significance matters. Compare the size of the departure to what you would see in simulated data from the fitted model.  

**Practical check (simulation):**

```r
library(simsalapar)   # or use pbkrtest, performance, etc.
set.seed(123)
sim_res <- simulate(model, nsim = 1000)   # simulate response from fitted model
# For each simulated dataset refit the model and compute a Shapiro test
pvals <- replicate(1000, {
  dsim <- simulate(model, nsim = 1)[[1]]
  msim  <- lmer( log(sd_depth) ~ Grazing * Country + (1|PlotID),
                data = transform(sd_data, sd_depth = exp(dsim)) )
  shapiro.test(resid(msim))$p.value
})
hist(pvals)   # see where 0.01 lies relative to the simulated distribution
```

If the observed p‑value is *typical* for data generated under the model, you can keep the LMM. If it is unusually low compared with the simulated distribution, the model may be misspecified.

### Step 4 – When a GLMM might be preferable  

If the residual diagnostics *clearly* show non‑normality **and** the variance is non‑constant *even after transformation*, consider a GLMM that matches the *scale* of the original (un‑logged) response.

| Original scale of `sd_depth` | Typical distribution for GLMM | Typical link function |
|------------------------------|------------------------------|-----------------------|
| Positive, right‑skewed (e.g., depth, area) | **Gamma** (shape‑scale) or **log‑normal** (via Gamma with log link) | **log** |
| Count of events (0,1,2,…) | **Poisson** (or negative binomial if over‑dispersed) | **log** |
| Proportion / 0‑1 bounded | **Binomial** (or Beta for continuous proportion) | **logit** (or log‑log) |

Because `sd_depth` is a *continuous positive* measurement, the two most common choices are:

1. **Gamma GLMM with log link**  

   ```r
   library(lme4)
   glmm <- glmer( sd_depth ~ Grazing * Country + (1 | PlotID),
                  family = Gamma(link = "log"),
                  data = sd_data )
   ```

2. **Log‑normal GLMM** (fit by modeling `log(sd_depth)` with a Gaussian LMM – which you already did).  
   In practice, the Gamma model and the log‑normal model often give very similar fitted values; the Gamma model has the advantage that you do **not** need to transform the response yourself, and the model’s variance is automatically proportional to the mean (a common feature of ecological measurements).

### Step 5 – Diagnostics for a GLMM  

1. **Conditional residuals** (`resid(model, type = "pearson")` or `"response"`).  
2. **Simulation‑based checks** (e.g., `DHARMa::simulateResiduals`). DHARMa creates *scaled* residuals that are approximately uniform under the correct model, regardless of the response distribution, and provides formal tests for:  
   * Uniformity (overall fit)  
   * Over‑/under‑dispersion  
   * Zero‑inflation (if relevant)  
   * Heteroscedasticity (plot residuals vs. fitted)  

   ```r
   library(DHARMa)
   sim <- simulateResiduals(fittedModel = glmm, n = 1000)
   plot(sim)               # residual vs. predicted, QQ, etc.
   testUniformity(sim)     # overall goodness‑of‑fit
   testDispersion(sim)     # check for over‑dispersion
   ```

3. **Random‑effect diagnostics** – still look at the BLUPs (best linear unbiased predictors) and their distribution; the random effects should be approximately normal, which can be checked with `qqnorm(ranef(glmm)$PlotID[[1]])`.

### Step 6 – Summarize the decision flow  

| Situation | Recommended action |
|-----------|--------------------|
| Residuals roughly normal after log‑transform, variance looks constant, model converges | **Keep the LMM** on `log(sd_depth)`. The Shapiro‑Wilk p‑value alone is not a reason to discard it. |
| Residuals still skewed / variance clearly heteroscedastic, even after transformation | **Fit a GLMM** (Gamma with log link is a natural choice for positive continuous data). |
| You prefer to stay in the Gaussian world and the only problem is a slight deviation from normality | Consider **robust variance estimators** (e.g., `lmerTest::lmer`, `sandwich` for fixed‑effect SEs) or **bootstrapping** for inference. |

---

## 3.  Final answer  

1. **Is the Shapiro‑Wilk p‑value (0.01) enough to reject the LMM?**  
   *No.* The test is overly sensitive with many residuals; visual inspection and simulation‑based checks are more relevant. If the QQ‑plot looks acceptable and the variance is roughly constant, the LMM on the log‑transformed response is generally fine.

2. **Do you need another model (GLMM), and which distribution?**  
   Only if the diagnostics still show strong non‑normality or heteroscedasticity after transformation. For a positive, right‑skewed continuous variable like `sd_depth`, a **Gamma GLMM with a log link** (or stay with the log‑normal LMM) is appropriate.

3. **Other assumptions to check**  

   * **Homoscedasticity** – residuals vs. fitted values.  
   * **Independence / correct random‑effect structure** – verify that the random intercept for Plot captures the within‑plot correlation (check ICC).  
   * **Random‑effect normality** – QQ‑plot of BLUPs.  
   * **Model convergence** – no warnings from `lmer`/`glmer`.  
   * For GLMMs, use simulation‑based residuals (e.g., DHARMa) to assess uniformity, dispersion, and zero‑inflation.  

If all these checks pass (or only minor deviations are present), the chosen mixed model—either the LMM on the log‑transformed response or the Gamma GLMM—can be used to test the grazing × country interaction.

---

## 4.  Common mistakes for this type of analysis  

| Mistake | Why it’s wrong | How to avoid it |
|---------|----------------|-----------------|
| **Relying solely on a p‑value from the Shapiro‑Wilk test** | The test is too sensitive; a tiny deviation can give a “significant” result even when the model is adequate. | Combine the test with visual QQ‑plots and simulation‑based checks. |
| **Forgetting to include the correct random‑effects structure** | Ignoring the nesting (plots within country × grazing) inflates Type I error and mis‑estimates variance. | Explicitly code the hierarchy, e.g., `(1|Country:Grazing:PlotID)` or `(1|PlotID)` if Plot is already nested. |
| **Treating pseudoreplicates as independent observations without a random effect** | Leads to pseudoreplication – artificially small SEs and over‑confident inference. | Add a random intercept (or slope) for the grouping factor that generated the pseudoreplicates. |
| **Log‑transforming the response but still fitting a Gaussian GLM without a random effect** | You lose the ability to model within‑plot correlation; also, you may forget to back‑transform predictions. | Use `lmer` (or `glmer` with Gaussian family) after transformation, keeping the random structure. |
| **Choosing a GLMM with the wrong family** (e.g., Poisson for continuous data) | The link/variance function will be mismatched, giving biased estimates and poor fit. | Match the family to the *scale* of the original data: Gamma for positive continuous, binomial for proportions, negative binomial for over‑dispersed counts, etc. |
| **Not checking heteroscedasticity after transformation** | Even after log‑transform the variance may still increase with the mean, violating LMM assumptions. | Plot residuals vs. fitted values; if a pattern remains, consider a variance‑function model (`nlme::varIdent`) or a GLMM with a variance that scales with the mean (e.g., Gamma). |
| **Assuming the fixed‑effect estimates are unaffected by residual non‑normality** | Severe non‑normality can affect standard errors and hypothesis tests. | Use robust SEs (bootstrapping) or a model that respects the true distribution. |

By keeping these points in mind you can decide confidently whether a linear mixed model on the log‑transformed response is sufficient, or whether a Gamma GLMM (or another appropriate GLMM) is required for your ecological grazing study.

*Original question: [What Mixed Model do I need to use for my analysis?](https://stats.stackexchange.com/questions/677129/what-mixed-model-do-i-need-to-use-for-my-analysis) on Cross Validated (Stats Stack Exchange), licensed CC BY-SA.*

{% endraw %}
