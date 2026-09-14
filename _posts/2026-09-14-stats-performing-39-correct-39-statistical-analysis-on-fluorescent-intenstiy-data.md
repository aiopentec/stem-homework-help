---
layout: question
title: Performing &#39;correct&#39; statistical analysis on fluorescent intenstiy
  data
author: StemFix Bot
category: stats
subject: stats
description: 'Step-by-step statistics solution: Performing &#39;correct&#39; statistical
  analysis on fluorescent intenstiy data'
tags:
- stats
---

{% raw %}
*As an Amazon Associate, I earn from qualifying purchases.* For more practice problems like this, see [Schaum's Outline of Statistics, 6th Edition](https://www.amazon.com/dp/1260011461?tag=aiopentec20-20).

---

## 1.  What the student is asking (in plain language)

The student has fluorescence‑intensity measurements from *many* individual cells.  
For each experimental condition (different drug concentrations) they have  

| level | biological replicate (n = 3) | # of cells per replicate (≈ 1 000–5 000) |
|------|------------------------------|----------------------------------------|
| 0 µM (control) | 3 | thousands |
| 1 µM | 3 | thousands |
| … | … | … |

The questions are:

| # | Question |
|---|----------|
| i) | Do I really need a mixed‑effects model, or can I just do a Kruskal‑Wallis test on the data? |
| ii) | I want to compare every drug level to the control and also compare the drug levels to each other. How should I do that? |
| iii) | Do I have to worry about the fact that the cell‑to‑cell values are not normally distributed? |

The student suspects that the distribution of the cell‑level intensities is far from normal and wonders how to incorporate the “random variation that arises on a cell‑cell basis”.

---

## 2.  Step‑by‑step solution  

Below we walk through the whole analysis pipeline, from data‑exploration to inference, and we give R code that can be run directly.

### 2.1  Understand the experimental hierarchy  

```
cell   →   belongs to   →   biological replicate (the experimental unit)   →   belongs to   →   drug concentration
```

* **Fixed effect** we are interested in: *drug concentration* (a categorical factor, or numeric if you want a dose‑response trend).  
* **Random effect** we must account for: *biological replicate* (the three independent cultures).  
* The individual cells are *observations* that are **nested** within a replicate. They are **not** independent experimental units; they share the same “batch” noise.

If we ignore the nesting and treat every cell as an independent observation we commit **pseudoreplication** and dramatically underestimate the variability, leading to far‑too‑optimistic p‑values.

### 2.2  Look at the raw distribution  

```r
library(ggplot2)
ggplot(df, aes(x = intensity)) +
  geom_histogram(bins = 50) +
  facet_grid(~ concentration) +
  theme_minimal()
```

Typical fluorescence intensities are right‑skewed (many low values, a long tail of bright cells). A log‑transformation (or a square‑root) usually makes the distribution much closer to symmetric.

```r
df$log_intensity <- log(df$intensity + 1)   # +1 avoids log(0)
ggplot(df, aes(x = log_intensity)) +
  geom_histogram(bins = 50) +
  facet_grid(~ concentration) +
  theme_minimal()
```

*If the transformed data look roughly normal (check with QQ‑plots), a linear mixed‑effects model is appropriate.*  
If they still look very non‑normal, a **generalised linear mixed model (GLMM)** with a Gamma (or log‑normal) family can be used directly on the raw intensities.

### 2.3  Choose a statistical model  

#### 2.3.1  Linear mixed‑effects model on log‑transformed data  

```r
library(lme4)
mod_lmm <- lmer(log_intensity ~ concentration + (1 | replicate), data = df)
summary(mod_lmm)
```

* `concentration` is a **fixed effect** (factor with 4–6 levels).  
* `(1 | replicate)` is a **random intercept** that allows each biological replicate to have its own baseline fluorescence.  

#### 2.3.2  GLMM on the raw (positive) intensities  

If you prefer to stay on the original scale:

```r
library(glmmTMB)
mod_glmm <- glmmTMB(intensity ~ concentration + (1 | replicate),
                    family = Gamma(link = "log"),
                    data = df)
summary(mod_glmm)
```

The Gamma family with a log link models the same right‑skewed shape that the data have, without any transformation.

### 2.4  Test the overall effect of drug concentration  

Both `lmer` and `glmmTMB` fit a **full model** that contains `concentration`.  
To obtain a *global* test (is there any difference among the concentrations?) we compare it with a reduced model that omits the term.

```r
# LMM version
mod_null <- lmer(log_intensity ~ 1 + (1 | replicate), data = df, REML = FALSE)
anova(mod_null, mod_lmm)      # likelihood‑ratio test
```

```r
# GLMM version
mod_null_glmm <- update(mod_glmm, . ~ . - concentration)
anova(mod_null_glmm, mod_glmm)   # chi‑square test
```

A significant χ² (or F) tells you that at least one concentration differs from the others.

### 2.5  Pairwise (or trend) comparisons  

The `emmeans` package (estimated marginal means) gives you the **adjusted** means for each concentration **after accounting for the random replicate effect**, and lets you test any contrast you like.

```r
library(emmeans)

# for the LMM (log‑scale)
emm <- emmeans(mod_lmm, ~ concentration)
pairs(emm, adjust = "holm")               # all pairwise comparisons, Holm‑adjusted

# control vs each dose only
contrast(emm, method = "trt.vs.ctrl", ref = "0") %>% 
  summary(adjust = "holm")
```

If you want a **dose‑response trend** (e.g., linear increase with concentration) treat `concentration` as a numeric covariate:

```r
mod_trend <- lmer(log_intensity ~ as.numeric(conc) + (1|replicate), data = df)
summary(mod_trend)    # test of the slope
```

### 2.6  Checking model assumptions  

* **LMM (log‑data)** – residuals should be roughly normal and homoscedastic.

```r
plot(resid(mod_lmm), fitted(mod_lmm))
qqnorm(resid(mod_lmm)); qqline(resid(mod_lmm))
```

* **GLMM (Gamma)** – look at the *scaled* Pearson residuals.

```r
simulationOutput <- simulateResiduals(mod_glmm, n = 250)
plot(simulationOutput)
```

If diagnostics show major violations (e.g., over‑dispersion, heavy tails), you can:

* add a random slope for concentration (`(concentration|replicate)`),  
* use a **negative‑binomial** or **Tweedie** family (available in `glmmTMB`), or  
* resort to a **non‑parametric permutation test** that respects the nesting (see 2.7).

### 2.7  A non‑parametric alternative that respects the hierarchy  

When the number of replicates is tiny (n = 3), a **permutation test** that shuffles the *replicate* labels rather than individual cells is a safe fallback.

```r
library(permute)

# Compute the mean intensity per replicate per concentration
rep_means <- aggregate(intensity ~ replicate + concentration, df, mean)

# Permutation test: randomly re‑assign concentration labels within each replicate
set.seed(123)
perm_test <- function(B = 5000){
  obs_F <- aov(intensity ~ concentration, data = rep_means)$`F value`[1]
  perm_F <- replicate(B, {
    perm <- rep_means
    perm$concentration <- shuffle(perm$concentration,
                                  control = how(within = Within(type = "free"),
                                                blocks = ~ replicate))
    aov(intensity ~ concentration, data = perm)$`F value`[1]
  })
  pval <- mean(perm_F >= obs_F)
  list(observed_F = obs_F, p = pval)
}
perm_test()
```

The test compares the observed F‑statistic (from a standard one‑way ANOVA on the **replicate means**) to the distribution obtained by permuting the concentration labels *within* each replicate, thus preserving the correlation among cells from the same replicate.

### 2.8  What to report  

| Item | What to write |
|------|---------------|
| **Model** | “A linear mixed‑effects model was fitted to log‑transformed fluorescence intensity, with drug concentration as a fixed effect and a random intercept for biological replicate.” |
| **Global test** | “The overall effect of concentration was significant, χ²(3) = 12.4, *p* = 0.006.” |
| **Pairwise contrasts** | “Compared with the control, 1 µM, 5 µM, and 10 µM gave adjusted mean differences of +0.28, +0.53, and +0.71 log‑units respectively (Holm‑adjusted *p* = 0.04, 0.001, <0.001).” |
| **Assumption checks** | “Residual QQ‑plot showed no deviation from normality after log‑transformation; the random‑intercept variance was 0.12 (SD = 0.35).” |
| **If GLMM used** | “A Gamma GLMM with log link gave a concentration effect χ²(3) = 10.9, *p* = 0.012, with similar pairwise results.” |
| **If permutation used** | “A permutation test on replicate means gave *p* = 0.018, confirming the mixed‑model result.” |

---

## 3.  Final answer (concise)

* **Yes, you need a mixed‑effects model (or an equivalent permutation test) because the cells are nested within only three independent biological replicates.** Treating each cell as an independent observation (e.g., a Kruskal‑Wallis on all cells) would be pseudoreplication and give misleading p‑values.  

* **Model choice**  
  * Log‑transform the intensities and fit a **linear mixed‑effects model** `log_intensity ~ concentration + (1|replicate)`.  
  * Or, fit a **Gamma GLMM** `intensity ~ concentration + (1|replicate)` if you prefer to stay on the original scale.  

* **Testing**  
  * Perform a likelihood‑ratio (or Wald) test for the overall concentration effect.  
  * Use `emmeans` (or `lsmeans`) for pairwise contrasts versus control and for all‑pair comparisons, applying a multiple‑testing correction (Holm, Tukey, etc.).  

* **Distribution concerns** – the right‑skewed cell‑level data violate normality; a log‑transform (or a Gamma GLMM) resolves this. After transformation, residuals are approximately normal, satisfying the model assumptions.  

* **If you truly cannot rely on the normality of the transformed data**, a **restricted permutation test on the replicate means** is a non‑parametric alternative that respects the hierarchical design.

Thus, the *correct* statistical workflow is:

1. Examine distribution → log‑transform if needed.  
2. Fit a mixed‑effects model with a random intercept for replicate.  
3. Test the global concentration effect (LRT).  
4. Conduct adjusted pairwise or trend contrasts with `emmeans`.  
5. Check residual diagnostics; if they fail, either switch to a Gamma GLMM or run a permutation test on replicate means.

---

## 4.  Common mistakes (and how to avoid them)

| Mistake | Why it’s wrong | How to avoid it |
|---------|----------------|-----------------|
| **Treating each cell as an independent observation** (e.g., running `kruskal.test(intensity ~ concentration)` on all cells). | Inflates sample size, ignores that cells from the same replicate share the same biological noise → p‑values far too small. | Always include `replicate` as a random effect (or collapse to replicate means before any test). |
| **Running a Kruskal‑Wallis on the raw cell data and reporting the result.** | Same pseudoreplication problem; the test also assumes independence. | Use a mixed model or a permutation test that respects the nesting. |
| **Discarding the huge number of cells and analysing only the three replicate means**. | Throws away most of the information (the within‑replicate variability) and reduces power. | Keep the cell‑level data and let the random‑effect term model the between‑replicate variability. |
| **Forgetting to check model assumptions after a log‑transform.** | A badly behaved residual distribution can invalidate inference. | Plot residuals

*Original question: [Performing &#39;correct&#39; statistical analysis on fluorescent intenstiy data](https://stats.stackexchange.com/questions/677168/performing-correct-statistical-analysis-on-fluorescent-intenstiy-data) on Cross Validated (Stats Stack Exchange), licensed CC BY-SA.*

{% endraw %}
