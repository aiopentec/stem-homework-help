---
layout: question
title: Significant treatment &#215; year interaction but no significant pairwise comparisons
  in a repeated-measures ANCOVA using lmer
author: StemFix Bot
category: stats
subject: stats
description: 'Step-by-step statistics solution: Significant treatment &#215; year
  interaction but no significant pairwise comparisons in a repeated-measures ANCOVA
  using'
tags:
- stats
---

{% raw %}
*As an Amazon Associate, I earn from qualifying purchases.* For more practice problems like this, see [Schaum's Outline of Statistics, 6th Edition](https://www.amazon.com/dp/1260011461?tag=aiopentec20-20).

---

## 1.  What the student is asking – in plain language  

The student fitted a **repeated‑measures ANCOVA** (implemented with `lmer`) that contains  

* a **treatment** factor (e.g., drug vs. placebo)  
* a **year** factor (e.g., measurements taken in 2018, 2019, 2020)  
* the **baseline value** as a covariate  
* the **treatment × year** interaction  

The ANOVA‐style test for the interaction is **significant** ( \(F(8,481.31)=2.14,\;p=0.031\) ), while the overall main effect of treatment is **not** significant ( \(p=0.674\) ).  

Next the student used the `emmeans` package to look at **pairwise comparisons of the two treatments within each year**, applying Tukey’s multiplicity adjustment. **None of those within‑year contrasts is significant** (all \(p>0.05\)).

The question:  

> *Can we have a significant treatment × year interaction but no significant pairwise treatment differences in any single year? Is this a logical/ statistical contradiction, or could it happen by chance?*  

---

## 2.  Step‑by‑step reasoning  

Below we walk through the logic of the tests, why the pattern the student observed is **possible**, and what it means for interpretation.

### Step 1 – Write down the model  

Let  

\[
Y_{ijk}= \text{outcome for subject }i\text{ in year }j\text{ under treatment }k
\]

The linear mixed model (simplified, ignoring random slopes for clarity) is  

\[
Y_{ijk}= \beta_0 + \beta_{\text{trt}}\,\text{Trt}_{k}
          + \beta_{\text{yr}}\,\text{Year}_{j}
          + \beta_{\text{bl}}\,\text{Baseline}_{i}
          + \beta_{\text{trt·yr}}\,(\text{Trt}_{k}\times\text{Year}_{j})
          + b_i + \varepsilon_{ijk},
\]

* \(b_i\sim N(0,\sigma_b^2)\)  (random intercept for repeated measures)  
* \(\varepsilon_{ijk}\sim N(0,\sigma^2)\)  

The **fixed‑effect** parameters of interest are  

* \(\beta_{\text{trt}}\) – overall (averaged across years) treatment effect  
* \(\beta_{\text{trt·yr}}\) – the interaction (how the treatment effect changes with year)  

### Step 2 – Hypotheses that are being tested  

| Test | Null hypothesis \(H_0\) | Alternative \(H_A\) |
|------|--------------------------|---------------------|
| **Overall treatment main effect** | \(\beta_{\text{trt}} = 0\) (same average effect across all years) | \(\beta_{\text{trt}}\neq0\) |
| **Treatment × year interaction** | All interaction contrasts are 0 (the treatment effect is the same in every year) | At least one year shows a different treatment effect |

The interaction **F‑test** is a *joint* test of **all** 8 (for 4 years × 2 treatment levels) interaction contrasts simultaneously. It pools information across years, which gives it more power to detect a systematic pattern, even if the effect in any *single* year is modest.

### Step 3 – Why a significant interaction does **not** guarantee a significant simple effect  

1. **Joint vs. individual tests**  
   * The interaction F‑test evaluates whether the **vector** of interaction coefficients differs from 0.  
   * Each simple‑effect test (treatment difference within a given year) looks at **one** component of that vector.  
   * A joint test can be significant while every individual component fails to reach the α‑level because the **overall evidence** (the sum of squared t‑statistics) is enough, but each t‑statistic on its own is not large enough.

2. **Multiple‑testing penalty**  
   * The `emmeans(..., adjust = "tukey")` procedure corrects for *all* pairwise contrasts performed (here 4 years × 1 contrast = 4 tests).  
   * The correction inflates the critical p‑value (≈ 0.05/√(k) for Tukey). Even if an unadjusted t‑test gave, say, \(p=0.07\), after Tukey adjustment the p‑value will be larger, making the result non‑significant.

3. **Statistical power**  
   * Power to detect an effect in a single year depends on the **sample size within that year**, the residual variance, and the magnitude of the true effect.  
   * If the true treatment effect is modest and/or the per‑year sample size is small, the within‑year contrasts will be under‑powered, whereas the interaction test gains power by borrowing strength across years.

4. **Direction of effects**  
   * The interaction can be driven by **different directions** in different years (e.g., treatment better than control in 2018, worse in 2020). The overall average main effect may be near zero (hence non‑significant), yet the *pattern of change* across years yields a significant interaction. In that case, each individual contrast could be non‑significant because the effect size in any single year is diluted by sampling error.

### Step 4 – A simple numeric illustration  

Suppose we have 4 years and the true treatment differences (Treatment – Control) are  

| Year | True difference |
|------|-----------------|
| 1    |  +0.30 |
| 2    |  +0.10 |
| 3    |  -0.10 |
| 4    |  -0.30 |

The average difference across years is **0**, so the main effect is truly zero.  
If each year has only ~30 subjects, the standard error of a single‑year contrast might be ≈ 0.25. The *t*‑statistics are then  

\[
t = \frac{0.30}{0.25}=1.20,\;
\frac{0.10}{0.25}=0.40,\;
\frac{-0.10}{0.25}=-0.40,\;
\frac{-0.30}{0.25}=-1.20,
\]

none of which reaches the usual critical value ≈ 2.0 (p > 0.05).  

However, the **interaction F‑statistic** is based on the sum of squares of those four contrasts:

\[
\chi^2 = \sum t_i^2 = 1.20^2+0.40^2+(-0.40)^2+(-1.20)^2 = 2.88.
\]

With 3 df for the interaction (4 years − 1), the corresponding p‑value is about **0.04** – i.e., significant.  

Thus the pattern is **exactly** what we see in the student’s data: the global test picks up a systematic change across years, while none of the individual year‑specific tests is strong enough on its own.

### Step 5 – What the results *mean* for the study  

* **Interpretation** – The treatment effect *depends* on year. In some years the treatment may be better, in others worse, but the evidence for a consistent difference in any single year is weak.  
* **Reporting** –  
  1. State that the interaction is statistically significant (report F, df, p).  
  2. Note that the overall treatment main effect is non‑significant.  
  3. Explain that follow‑up simple‑effect tests (pairwise comparisons within each year) did not survive Tukey adjustment, which is expected when the interaction is modest and the per‑year sample sizes are limited.  
  4. Consider visualising the interaction (e.g., plot estimated marginal means by year and treatment with confidence bands). The plot often reveals the direction of the change, even if individual contrasts are not significant.  

### Step 6 – Optional further analyses  

1. **Contrast the interaction directly** – Instead of testing each year separately, test *pre‑planned* contrasts that reflect the hypothesised pattern (e.g., “treatment effect in early years vs. late years”). These contrasts have higher power because they aggregate information across years.  
2. **Bayesian or hierarchical modeling** – A hierarchical approach can shrink year‑specific effects toward a common mean, providing more stable estimates when per‑year data are sparse.  
3. **Increase power** – If the research question truly requires detection of a treatment difference within a specific year, increase the sample size for that year or combine adjacent years when scientifically justified.

---

## 3.  Final answer  

Yes, it is **statistically possible and perfectly reasonable** to obtain

* a **significant treatment × year interaction** (the effect of treatment varies across years), **and**  
* **non‑significant pairwise treatment comparisons** within each individual year after a Tukey adjustment.

The interaction test pools information across all years and can detect a systematic pattern even when each single‑year contrast lacks the power to be significant on its own. The Tukey correction further raises the threshold for significance, making it even harder for individual contrasts to reach the 0.05 level.

Therefore, the student’s results do not contradict one another; they simply reflect limited power for the simple effects and a genuine variation of the treatment effect over time.

---

## 4.  Common mistakes in this kind of analysis  

| Mistake | Why it’s wrong | How to avoid it |
|---------|----------------|-----------------|
| **Interpreting a significant interaction as evidence that the treatment works in *some* year** without checking the direction or magnitude of the simple effects. | The interaction only tells you the *differences* among years, not that any specific year shows a clinically relevant effect. | Plot the estimated marginal means; examine planned contrasts that correspond to the scientific hypothesis. |
| **Testing simple effects *without* adjusting for multiple comparisons** and then concluding “no effect” because all p‑values > 0.05. | Ignoring the multiplicity inflates Type I error; conversely, using a very strict correction (e.g., Tukey) can be overly conservative when the number of tests is large. | Choose an adjustment appropriate to the number and logical dependency of tests (Tukey for all pairwise, Dunnett if comparing each year to a control, or pre‑specify a small set of orthogonal contrasts). |
| **Relying only on the main‑effect p‑value when the interaction is significant**. | The main‑effect estimate averages across years and can be near zero even if the treatment is important in some years. | When the interaction is significant, focus on the interaction and on simple effects; the main‑effect becomes a nuisance parameter. |
| **Assuming the interaction test is more “powerful” than the simple‑effect tests**. | Power depends on the true pattern. If the true effect is present in only one year, the simple‑effect test is more powerful; if the effect follows a smooth trend across years, the joint test wins. | Align the statistical test with the a priori scientific expectation (trend vs. isolated effect). |
| **Not checking model assumptions (e.g., sphericity, correct random‑effects structure)** before interpreting the F‑test. | Violated assumptions can inflate or deflate the F‑statistic, leading to misleading significance. | Inspect residual plots, compare models with different random‑effects specifications, use Kenward‑Roger or Satterthwaite df approximations as appropriate. |

---

*Original question: [Significant treatment &#215; year interaction but no significant pairwise comparisons in a repeated-measures ANCOVA using lmer](https://stats.stackexchange.com/questions/676999/significant-treatment-%c3%97-year-interaction-but-no-significant-pairwise-comparisons) on Cross Validated (Stats Stack Exchange), licensed CC BY-SA.*

{% endraw %}
