---
layout: question
title: Can a model still be viable even with likely redundant fixed and random effects?
author: StemFix Bot
category: stats
subject: stats
description: 'Step-by-step statistics solution: Can a model still be viable even with
  likely redundant fixed and random effects?'
tags:
- stats
---

{% raw %}
*As an Amazon Associate, I earn from qualifying purchases.* For more practice problems like this, see [Schaum's Outline of Statistics, 6th Edition](https://www.amazon.com/dp/1260011461?tag=aiopentec20-20).

---

## 1. What the student is asking (in plain language)

The student wants to fit a mixed‑effects model for **total fish count** that varies over time, **by region (segment)**, and also has repeated measurements at the same **site**.  

* Each **site** is a 60‑ft circle; many observations (different seasons/years) come from the same site.  
* A **segment** is a group of adjacent sites (segment 1 = sites 1‑17, segment 2 = sites 18‑47).  

Because every site belongs to exactly one segment, the two variables are perfectly nested: *site → segment*.  
The student wonders:

* Can we keep **segment** (a fixed effect) in the model while also keeping a **random intercept for site** (`(1|fSite)`)?
* If the random intercept already captures most of the variation, does adding segment bias the estimates or make the model “wrong”?

In short: **When a fixed effect is (almost) a function of a random effect, is it still appropriate to include both?**  

---

## 2. Step‑by‑step answer  

Below we work through the conceptual and practical issues, show how to check them in R, and give a decision rule.

### Step 1 – Write the two candidate models  

| Model | Fixed part | Random part |
|-------|------------|-------------|
| **A** (full) | `total_count ~ time * segment` | `(1|fSite)` |
| **B** (reduced) | `total_count ~ time` | `(1|fSite)` |

*Model A* tries to let the temporal trend differ by segment (the `time:segment` interaction).  
*Model B* treats segment as irrelevant and lets the random site intercept soak up any site‑specific differences.

If segment adds nothing beyond the site random effect, the two models should fit the data equally well.

---

### Step 2 – Understand the statistical relationship between **segment** and **site**

| Relationship | Consequence |
|--------------|-------------|
| **Segment ⟂ Site** (independent) | Fixed and random terms capture *different* sources of variation – no problem. |
| **Segment = function(site)** (perfect nesting) | The fixed effect is **identical** to a linear combination of the random intercepts. In a linear mixed model this creates **non‑identifiability** (the likelihood is flat) and the two terms are *confounded*. |

Because each site belongs to only one segment, we have the second case: **segment is a deterministic function of site**.  

Mathematically, a random intercept for site can be written as  

\[
b_{i} \;=\; \underbrace{\beta_{\text{segment}[i]}}_{\text{fixed part}} \;+\; u_{i},
\]

where \(u_{i}\sim N(0,\sigma^{2}_{\text{site}})\). If we also include \(\beta_{\text{segment}}\) as a fixed effect, the model tries to estimate the same quantity twice.

---

### Step 3 – What does the software do?

* **lme4** (and most mixed‑model packages) will *still* fit the model, but the **fixed‑effect estimate for segment will be a linear combination of the random‑effect estimates**.  
* The variance‑covariance matrix will be **singular** (one eigenvalue essentially zero) and you will see a warning like  
  ```
  Boundary (singular) fit: see ?isSingular
  ```
* Standard errors for the segment coefficients become huge or undefined, and the likelihood surface is flat in the direction that swaps part of the segment effect into the site random intercept.

Thus the model **converges, but the parameters are not uniquely identified** – you cannot trust the numerical values.

---

### Step 4 – Formal diagnostic: check for singular fit  

```r
library(lme4)

mod.full <- lmer(total_count ~ time * segment + (1|fSite), data = shiny_toad,
                 REML = FALSE)   # use ML for comparing models
isSingular(mod.full)   # TRUE means a redundancy problem
```

If `TRUE`, the fixed‑effect term **segment** (or the interaction) is linearly dependent on the random intercept.

---

### Step 5 – Model comparison (if the fit is *not* singular)

If the nesting is *not* perfect (e.g., some sites appear in both segments across years), you can compare the two models with a likelihood‑ratio test (or AIC).

```r
mod.reduced <- lmer(total_count ~ time + (1|fSite), data = shiny_toad,
                    REML = FALSE)

anova(mod.reduced, mod.full)   # χ² test, df = number of added fixed parameters
```

*If the p‑value is large* (or ΔAIC < 2), the extra segment terms do **not** improve the model, so you should drop them.  
*If the p‑value is small* **and** the model is **not singular**, the segment effect is providing information that the site random intercept cannot capture (e.g., a common shift for all sites within a segment). In that case keeping both is fine.

---

### Step 6 – When can you legitimately keep both?

You need **variation of segment that is *not* completely explained by site**. This can happen in three ways:

| Situation | How to code |
|-----------|-------------|
| **Segments contain multiple sites** *and* some sites appear in more than one segment (e.g., a site moves or is re‑assigned). | Keep both terms; they are independent. |
| **Segment is a higher‑level grouping** (e.g., “region”) while site is a lower‑level grouping (e.g., “lake”). | Model as `(1|segment/site)` or `(1|segment) + (1|site)`. |
| **You want a *random* segment effect** (i.e., you consider segments a sample from a larger population of possible segments). | Use `(1|segment) + (1|site)` and **remove segment as a fixed effect**. |

In the present data **segment is a deterministic function of site**, so none of the above hold. The appropriate model is **either**:

* **Only a random intercept for site** (drop segment completely), **or**
* **Treat segment as the only grouping factor** (remove the site random effect and keep `segment` as a fixed effect *or* as a random effect if you view segments as a random sample).

---

### Step 7 – Recommended model for the current data  

Because each site belongs to a single segment, the simplest and most interpretable model is:

```r
mod.best <- lmer(total_count ~ time + (1|fSite), data = shiny_toad,
                 REML = TRUE)
```

*If you are interested in a *segment‑level* mean shift* (e.g., segment 2 consistently higher than segment 1), replace the random effect with a **fixed segment term** and drop the site random effect:

```r
mod.seg <- lm(total_count ~ time * segment, data = shiny_toad)  # ordinary LM
```

But **do not** include *both* `segment` (fixed) and `(1|fSite)` (random) simultaneously.

---

## 3. Final answer (concise)

*When a fixed effect (segment) is perfectly nested within a random effect (site), the two terms are **collinear** and the model becomes non‑identifiable.*  

* The mixed‑effects software will usually warn about a **singular fit**.  
* Parameter estimates for the fixed effect are not reliable; the random intercept already captures all the variation that segment could explain.  

**Therefore, you should **not** keep both a fixed segment term and a random site intercept in the same model.** Choose one of the following:

1. Keep the **random site intercept** only (drop segment).  
2. Keep **segment as a fixed (or random) effect** only (drop the site random intercept).  

If you suspect that segment contains information *beyond* the site differences, you must have sites that appear in more than one segment; otherwise the two terms are redundant.

---

## 4. Common mistakes for this type of problem  

| Mistake | Why it’s wrong | How to avoid it |
|---------|----------------|-----------------|
| **Including a fixed effect that is a deterministic function of a random effect.** | Creates a singular fit; fixed‑effect coefficients are not identifiable. | Examine the grouping structure: each level of the random effect should contain *multiple* levels of the fixed effect (or vice‑versa). |
| **Assuming a non‑significant interaction means the term can stay.** | Significance tests do not resolve identifiability; a term can be non‑significant yet still be redundant. | Check `isSingular()` and the design matrix rank (e.g., `qr(lme4::getME(mod, "X"))$rank`). |
| **Treating “segment” as a covariate when it is actually a grouping factor.** | A grouping factor should be modelled as a random effect (or as a fixed factor with separate intercepts). | Decide whether segment is a *factor* (categorical) or a *continuous* covariate; code accordingly. |
| **Comparing models with different random‑effect structures using `anova()` without refitting with ML.** | `anova()` with REML compares only fixed‑effect changes; random‑effect changes need ML. | Use `REML = FALSE` when you intend to compare models that differ in random‑effect structure. |
| **Forgetting to check for singularity after adding complex random structures.** | A complex random‑effects structure may be over‑parameterised, leading to zero variance components. | Always run `isSingular(mod)` and look at the variance‑component estimates. |

By keeping these points in mind, you can avoid over‑parameterised mixed models and interpret your results with confidence.

*Original question: [Can a model still be viable even with likely redundant fixed and random effects?](https://stats.stackexchange.com/questions/677430/can-a-model-still-be-viable-even-with-likely-redundant-fixed-and-random-effects) on Cross Validated (Stats Stack Exchange), licensed CC BY-SA.*

{% endraw %}
