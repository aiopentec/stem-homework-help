---
layout: question
title: Ways to deal with extreme values in generalized additive model (GAM)?
author: StemFix Bot
category: stats
subject: stats
description: 'Step-by-step statistics solution: Ways to deal with extreme values in
  generalized additive model (GAM)?'
tags:
- stats
---

{% raw %}
*As an Amazon Associate, I earn from qualifying purchases.* For more practice problems like this, see [Schaum's Outline of Statistics, 6th Edition](https://www.amazon.com/dp/1260011461?tag=aiopentec20-20).

---

## 1.  What the student is asking (in plain language)

The student has count data that contain **one very large observation (value = 18)** while the other counts are much smaller.  
When a Generalized Additive Model (GAM) is fitted with `mgcv::gam()` the smooth term for year (`s(CYR)`) becomes highly wiggly – the model “sticks” to that single extreme point and the estimated annual trend looks **artificially high**.

The student tried two things:

| Approach | What they did | What they observed |
|----------|---------------|--------------------|
| **Lower the basis dimension** `k` (e.g. `k = 5`) for the year smooth | Forces the spline to be very smooth, i.e. it cannot follow the extreme point | The smooth looks more plausible, but `gam.check()` now reports that the effective degrees of freedom (edf) are close to the maximum (`k‑1`) and the confidence bands become huge. |
| **Leave `k` at the default (large)** and keep the wiggle | The model fits the outlier well, and the edf are well below `k‑1` | The annual trend is dominated by the single outlier and looks “above average”. |

The question is:

> **Should I deliberately reduce `k` to force a smoother trend, or is there a better way to “tame” the influence of the extreme value while still letting the model discover any real patterns?**

---

## 2.  Step‑by‑step worked solution  

Below is a systematic way to address the problem.  
All steps are illustrated with R code that you can run (replace `shiny_toad` with your own data frame).

> **Key ideas**  
> 1. **Diagnose the outlier** – is it a data‑entry error, a true extreme observation, or a measurement artefact?  
> 2. **Use a sufficiently large `k`** (so the spline has the capacity to represent the true shape) and let the **penalty** decide how wiggly the curve should be.  
> 3. **Allow the model to shrink unused basis functions** (`select = TRUE` or a shrinkage basis such as `"ts"`).  
> 4. **Check influence diagnostics** to see whether the single point is overly influential.  
> 5. If the point is genuine but highly influential, consider **robust/weighted GAMs** or a **different error distribution**.  
> 6. Only after these checks should you contemplate *manually* reducing `k` – and even then you should verify that the inference you care about does not change.

---

### 2.1  Load the required packages  

```r
library(mgcv)      # GAM fitting
library(gratia)    # tidy tools for visualising mgcv objects
library(DHARMa)    # residual diagnostics for GLMM/GAM
library(ggplot2)   # plotting
library(dplyr)     # data wrangling
```

---

### 2.2  Inspect the data – find the extreme value  

```r
shiny_toad %>% 
  summarise(
    n      = n(),
    max_y  = max(total_count),
    mean_y = mean(total_count),
    sd_y   = sd(total_count)
  )
```

If the maximum is *much* larger than `mean + 3*sd`, the observation is an **outlier**.  
Plot the raw counts vs. year to see it visually:

```r
ggplot(shiny_toad, aes(x = CYR, y = total_count)) +
  geom_point() +
  geom_line() +
  labs(title = "Total counts through years",
       y = "Count (offset by area_sampled)") +
  theme_minimal()
```

*If the point looks like a data‑entry mistake (e.g., a misplaced decimal), correct or remove it.*  
If it is a plausible biological observation, keep it but be aware that it may dominate the fit.

---

### 2.3  Fit a **baseline GAM** with a *large* basis dimension  

Give the smooth for year a generous `k` (e.g., `k = 12`).  
`k` should be **larger than the number of wiggles you might ever need**, not smaller.

```r
gam_bigk <- gam(
  total_count ~ offset(log(area_sampled)) +
    s(CYR, k = 12, bs = "tp") +      # thin‑plate regression spline (no shrinkage)
    fSeason +
    s(sal, bs = "ts", k = 5) +
    s(DO,  bs = "ts", k = 5) +
    s(ave_sav, by = fDiet_presence) +
    fDiet_presence +
    s(fSite, bs = "re"),
  data    = shiny_toad,
  family  = nb(link = "log"),
  method  = "REML",
  select  = FALSE,          # keep all smooths for now
  drop.unused.levels = FALSE
)
summary(gam_bigk)
```

*What to look for in `summary(gam_bigk)`*

| Item | Interpretation |
|------|----------------|
| **edf** for `s(CYR)` | How wiggly the spline actually is (penalised). If edf ≈ 1–2 → very smooth; if edf ≈ `k‑1` (≈ 11) → the penalty is not enough to smooth out the extreme value. |
| **p‑value** for `s(CYR)` | Tests the null hypothesis that the smooth is *linear*. A tiny p‑value is expected with many data points; it does **not** guarantee that the shape is realistic. |
| **`scale`** (NB dispersion) | Checks whether the NB family adequately captures over‑dispersion. |

If the edf for `s(CYR)` is close to `k‑1`, the model is using most of the basis functions to chase the outlier.

---

### 2.4  Diagnose influence of the extreme observation  

#### 2.4.1  Cook’s distance / dfbeta for a GAM  

```r
infl <- influence(gam_bigk, obs = TRUE)   # returns influence measures per observation
cooks <- infl$cooks.distance
dfbetas <- infl$dfbetas

# Highlight the largest values
infl_summary <- tibble(
  row = 1:nrow(shiny_toad),
  cooks = cooks,
  dfbeta_year = dfbetas[, "s(CYR)"]
) %>%
  arrange(desc(cooks))

head(infl_summary, 5)   # should show the extreme point at the top
```

If the point’s Cook’s distance is orders of magnitude larger than the rest (e.g., > 4 × mean), it is **high‑influence**.

#### 2.4.2  Visualise influence  

```r
ggplot(shiny_toad, aes(x = CYR, y = total_count)) +
  geom_point(aes(colour = cooks > 4 * mean(cooks)), size = 2) +
  scale_colour_manual(values = c("black", "red")) +
  labs(colour = "High influence?") +
  theme_minimal()
```

A red point signals the outlier.

---

### 2.5  Let the model *shrink* the smooth automatically  

Two simple ways to achieve this while **keeping a large `k`**:

#### (a) Use a *shrinkage* basis (`bs = "ts"`)

```r
gam_shrink <- gam(
  total_count ~ offset(log(area_sampled)) +
    s(CYR, bs = "ts", k = 12) +   # shrinkage thin‑plate spline
    fSeason +
    s(sal, bs = "ts", k = 5) +
    s(DO,  bs = "ts", k = 5) +
    s(ave_sav, by = fDiet_presence) +
    fDiet_presence +
    s(fSite, bs = "re"),
  data    = shiny_toad,
  family  = nb(link = "log"),
  method  = "REML",
  select  = FALSE,
  drop.unused.levels = FALSE
)
summary(gam_shrink)
```

The `"ts"` basis adds an *extra penalty* that can push the effective degrees of freedom of a smooth **toward zero** if the data do not support complexity.  
You will usually see `edf` for `s(CYR)` **well below** `k‑1` even when the extreme point is present.

#### (b) Enable *smooth selection* (`select = TRUE`)  

```r
gam_select <- gam(
  total_count ~ offset(log(area_sampled)) +
    s(CYR, k = 12) +      # any bs, e.g., "tp"
    fSeason +
    s(sal, bs = "ts", k = 5) +
    s(DO,  bs = "ts", k = 5) +
    s(ave_sav, by = fDiet_presence) +
    fDiet_presence +
    s(fSite, bs = "re"),
  data    = shiny_toad,
  family  = nb(link = "log"),
  method  = "REML",
  select  = TRUE,        # let mgcv penalise each smooth toward zero
  drop.unused.levels = FALSE
)
summary(gam_select)
```

`select = TRUE` adds an *extra smoothing parameter* that can drive an entire smooth to **zero edf** if it adds no explanatory power.  
It is a safe way to keep `k` large (so you are not *forced* to miss patterns) while still protecting against over‑fitting caused by a single outlier.

---

### 2.6  Check model diagnostics after shrinkage / selection  

```r
# 1) gam.check (traditional mgcv diagnostics)
gam.check(gam_shrink)   # or gam.check(gam_select)

# 2) DHARMa residual simulation
sim_res <- simulateResiduals(gam_shrink, n = 250)
plot(sim_res)               # tests uniformity, dispersion, outliers
testDispersion(sim_res)     # should be non‑significant for NB
testZeroInflation(sim_res)  # just in case
```

If `gam.check` now shows **edf well below `k‑1`** and the residual plots look random (no systematic pattern, no heteroscedasticity), the model is adequately smoothed **without manually lowering `k`**.

---

### 2.7  (Optional) Robust GAM – down‑weight the outlier  

If you are convinced that the extreme count is *real* but you do **not** want it to dominate the fit, you can give it a smaller weight:

```r
# Create a weight vector (e.g., 0.2 for the extreme point, 1 for the rest)
wts <- ifelse(shiny_toad$total_count == 18, 0.2, 1)

gam_robust <- gam(
  total_count ~ offset(log(area_sampled))

*Original question: [Ways to deal with extreme values in generalized additive model (GAM)?](https://stats.stackexchange.com/questions/677161/ways-to-deal-with-extreme-values-in-generalized-additive-model-gam) on Cross Validated (Stats Stack Exchange), licensed CC BY-SA.*

{% endraw %}
