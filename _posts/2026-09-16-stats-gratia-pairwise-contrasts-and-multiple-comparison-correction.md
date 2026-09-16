---
layout: question
title: gratia pairwise contrasts and multiple comparison correction
author: StemFix Bot
category: stats
subject: stats
description: 'Step-by-step statistics solution: gratia pairwise contrasts and multiple
  comparison correction'
tags:
- stats
---

{% raw %}
*As an Amazon Associate, I earn from qualifying purchases.* For more practice problems like this, see [Schaum's Outline of Statistics, 6th Edition](https://www.amazon.com/dp/1260011461?tag=aiopentec20-20).

---

## 1.  What the student is asking (in plain language)

The student fits a **GAMM** (generalised additive mixed model) to a longitudinal biomarker and then uses **`gratia::difference_smooths()`** to plot the difference between two groups (e.g. *A – B*) together with a 95 % confidence band.  
Interpretation of the plot is usually:

* wherever the band does **not** contain 0 → the two groups differ at that age.

The student now wants to repeat the same exercise for **many biomarkers** at the same time. Because each biomarker yields a whole curve of p‑values (or confidence bands) across age, the student worries that the usual point‑wise 95 % bands will inflate the overall Type‑I error rate when many curves are examined.

The concrete questions are:

1. **Should the raw p‑values for the parametric and smooth terms be FDR‑corrected before looking at pairwise contrasts?**  
2. **Do we need to widen the 95 % confidence band to account for the fact that we are making many comparisons (multiple biomarkers, multiple group pairs)?**  
3. **Does `gratia::difference_smooths()` already provide any multiple‑testing correction?**

Below is a step‑by‑step answer that shows how to obtain *simultaneous* (family‑wise) confidence intervals for the smooth differences, how to adjust across many biomarkers, and why a simple FDR‑adjustment of the model summary is not enough.



## 2.  Worked solution – every step explained  

### 2.1  Understand the two levels of multiplicity  

| Level | What is being compared? | Typical error‑rate to control |
|------|--------------------------|--------------------------------|
| **Within‑curve** | For a single biomarker & a single pair of groups we test *many* ages (e.g. 100 grid points). | **Family‑wise error (FWER)** across the age domain → *simultaneous* confidence band. |
| **Across‑curves** | We repeat the same curve for several biomarkers (and possibly several group pairs). | **False discovery rate (FDR)** or FWER across biomarkers. |

Both levels have to be addressed, but they are handled differently.

---

### 2.2  Fit the GAMM exactly as the student already does  

```r
library(mgcv)      # GAMM fitting
library(gratia)    # utilities for smooths and contrasts
library(dplyr)

myModel <- gamm(
  scaled_biomarker ~ s(age_c, by = group_ABC, k = 5, fx = TRUE) +
                    group_ABC + sex,
  random = list(participant_id = ~ 1 + splines::ns(age_c)),
  data  = myData,
  method = "REML"
)
```

*`myModel$gam`* is the fitted `gam` object that `gratia` works with.

---

### 2.3  Obtain **simultaneous** confidence intervals for a pairwise smooth difference  

`gratia::difference_smooths()` returns **point‑wise** intervals by default (`interval = "confidence"`).  
To get **simultaneous** (family‑wise) intervals we must ask for the *simultaneous* type.  
`gratia` provides this through the argument `interval = "simultaneous"` (it calls `mgcv::confint.gam()` internally).

```r
# A vs B difference with simultaneous 95% CI
diff_AB_simul <- difference_smooths(
  myModel$gam,
  select = "s(age_c)",          # the smooth term
  comp = c("A","B"),            # explicit pair (optional)
  n = 1000,                     # fine grid over age
  interval = "simultaneous",   # <<< key argument
  level = 0.95,
  unconditional = TRUE         # use the full posterior variance
)

# Visualise
plot(diff_AB_simul) +
  labs(title = "Group A – B: simultaneous 95% CI",
       y = "Difference (A – B)", x = "Age")
```

**Why does this work?**  
The simultaneous interval is constructed by the *max‑t* method (Ramos‑Plata et al. 2023). It inflates the band just enough so that the probability that **any** point on the curve lies outside the band is ≤ α (here 0.05). Hence, if the band does not contain 0 at a given age, we can claim significance **while preserving the overall 5 % error rate for the whole curve**.

> **Tip:** `unconditional = TRUE` adds the uncertainty from the smoothing parameter estimation; this is recommended for inference.

---

### 2.4  Repeat for every biomarker (and optionally every group pair)

Assume the data are in *long* format with a column `biomarker` that identifies each outcome. One can loop over the biomarkers, fit a model for each, and store the simultaneous p‑value curve.

```r
library(purrr)

# Function that returns a data.frame of ages, estimate, SE, and simultaneous CI
get_diff_simul <- function(dat, biomarker_name) {
  # Fit GAMM for this biomarker
  fit <- gamm(
    scaled_biomarker ~ s(age_c, by = group_ABC, k = 5, fx = TRUE) +
                      group_ABC + sex,
    random = list(participant_id = ~ 1 + splines::ns(age_c)),
    data = dat,
    method = "REML"
  )
  
  # Difference A‑B with simultaneous CI
  dif <- difference_smooths(
    fit$gam,
    select = "s(age_c)",
    comp   = c("A","B"),
    n      = 1000,
    interval = "simultaneous",
    level    = 0.95,
    unconditional = TRUE
  )
  
  # Convert to tidy data.frame and tag the biomarker
  dif %>% 
    as_tibble() %>% 
    mutate(biomarker = biomarker_name,
           pair = "A_vs_B")
}

# Apply to each biomarker
diff_all <- myData %>%
  group_by(biomarker) %>%                         # split by biomarker
  group_modify(~ get_diff_simul(.x, .y$biomarker[1]))
```

`diff_all` now contains a **simultaneous** confidence band for each biomarker’s A‑B contrast.

---

### 2.5  Extract a *p‑value* curve (optional)  

`difference_smooths()` also returns a column `p.value` (point‑wise Wald test).  
If you want to control the **false discovery rate** **across biomarkers**, you can adjust these p‑values **once per age point** (or once per entire curve, see 2.6). The simplest approach:

```r
# For each age, adjust the set of p-values across biomarkers
p_adj_by_age <- diff_all %>%
  group_by(x) %>%                               # x = age grid
  mutate(p_adj = p.adjust(p.value, method = "fdr")) %>%
  ungroup()
```

Now you can plot `p_adj` and declare significance when `p_adj < 0.05`.  
Because the underlying interval is already simultaneous **within** each curve, the FDR correction only handles the *across‑biomarker* multiplicity.

---

### 2.6  Alternative: One‐step *global* FDR on the set of curves  

If you prefer a single adjustment that accounts for the whole family (all ages × all biomarkers), treat each **grid point** as an individual test and adjust the *entire* vector of p‑values:

```r
p_vec   <- diff_all$p.value
p_adj   <- p.adjust(p_vec, method = "fdr")
diff_all$p_adj_global <- p_adj
```

This is more conservative because it does not exploit the correlation across ages, but it is a perfectly valid way to keep the expected proportion of false discoveries ≤ 0.05 across the whole analysis.

---

### 2.7  Do we need to adjust the *parametric* and *smooth* terms **before** looking at contrasts?  

* No.  
  The p‑values returned by `summary(gam)` (or `summary(gamm)`) test **whether each smooth term is different from zero**. They are **not** the same hypothesis as “*Group A and B differ at a given age*”. Adjusting those p‑values does not affect the family‑wise error of the contrast curves.  
* The proper adjustment is applied **to the contrast itself** (steps 2.3–2.6).  

Therefore, you can ignore the summary‑level p‑values when the goal is to infer *pairwise smooth differences*.

---

### 2.8  Summary of the workflow  

| Step | Code fragment | What it does |
|------|---------------|--------------|
| 1️⃣ | `gamm( … )`   | Fit one GAMM per biomarker |
| 2️⃣ | `difference_smooths(..., interval = "simultaneous")` | Get a *simultaneous* 95 % band for a chosen pair of groups |
| 3️⃣ | Loop over biomarkers (e.g., `group_modify`) | Produce a tidy table of estimates and simultaneous CIs for each outcome |
| 4️⃣ | `p.adjust(..., method = "fdr")` (within each age or globally) | Control the **FDR** across the set of biomarkers (and optionally across ages) |
| 5️⃣ | Plot or flag ages where `p_adj < 0.05` (or where CI excludes 0) | Final inference – periods where the groups differ, with proper multiplicity control |

---

## 3.  Final answer – concise statements  

1. **Do not FDR‑correct the model summary p‑values**; they test a different hypothesis.  
2. **Use simultaneous confidence intervals** for each smooth difference (`interval = "simultaneous"` in `difference_smooths`). This already inflates the band to give a family‑wise error rate of 5 % **within** each biomarker‑pair curve.  
3. To handle the multiplicity **across many biomarkers (or many pairwise contrasts)**, extract the point‑wise p‑values from `difference_smooths` and apply an FDR correction (e.g., `p.adjust(method = "fdr")`). You may adjust *separately for each age* or *once for the whole vector* – both are accepted, the former being less conservative.  
4. `gratia::difference_smooths()` **does not automatically** adjust for the across‑biomarker multiple testing; you must add the FDR step yourself.  

In short:  

* **Within‑curve** → request simultaneous bands (`interval = "simultaneous"`).  
* **Across‑curves** → apply an FDR correction to the extracted p‑values.  

That combination gives you proper control of both family‑wise error (over age) and false‑discovery rate (over biomarkers).

---

## 4.  Common mistakes to avoid  

| Mistake | Why it’s wrong | How to fix it |
|--------|----------------|---------------|
| **Applying `p.adjust()` to the p‑values from `summary(gam)`** and then looking at the contrast plot. | Those p‑values test “is the smooth term ≠ 0?” not “are the two groups different at age *t*?”. | Adjust only the contrast p‑values (or use simultaneous CIs). |
| **Using the default point‑wise CI** and assuming it is already multiple‑testing‑corrected. | Point‑wise bands have a 5 % error at each grid point, but the probability of at least one false positive across the whole curve can be > 5 %. | Specify `interval = "simultaneous"` (or compute simultaneous CIs via `mgcv::confint.gam`). |
| **Running `difference_smooths()` once and then re‑using the same CI for all biomarkers**. | Each biomarker has its own fitted smooths and variance; the bands are not transferable. | Loop over biomarkers, fitting a separate GAMM and extracting its own simultaneous CI. |
| **Adjusting p‑values *after* having inspected the plots** (i.e., data‑driven selection). | This introduces “researcher degrees of freedom” and inflates Type‑I error. | Decide the correction strategy *before* visual inspection and apply it uniformly. |
| **Forgetting `unconditional = TRUE`** when constructing simultaneous intervals. | The default (conditional) intervals ignore uncertainty in smoothing‑parameter estimation, leading to anti‑conservative inference. | Set `unconditional = TRUE` (or use `gratia::smooth_estimates(..., unconditional = TRUE)`). |
| **Using a very coarse grid (`n` too small)** and thinking the simultaneous band is accurate. | The max‑t method approximates the distribution of the supremum over the grid; a coarse grid may underestimate the needed inflation. | Choose a fine

*Original question: [gratia pairwise contrasts and multiple comparison correction](https://stats.stackexchange.com/questions/677105/gratia-pairwise-contrasts-and-multiple-comparison-correction) on Cross Validated (Stats Stack Exchange), licensed CC BY-SA.*

{% endraw %}
