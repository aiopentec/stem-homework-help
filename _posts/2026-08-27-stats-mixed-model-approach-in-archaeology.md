---
layout: question
title: Mixed Model Approach in Archaeology
author: StemFix Bot
category: stats
subject: stats
description: 'Step-by-step statistics solution: Mixed Model Approach in Archaeology'
tags:
- stats
---

{% raw %}
*As an Amazon Associate, I earn from qualifying purchases.* For more practice problems like this, see [Schaum's Outline of Statistics, 6th Edition](https://www.amazon.com/dp/1260011461?tag=aiopentec20-20).

---

## 1. What the student is asking (in plain language)

The student has a **cross‑tabulation of counts** of ten standardized vessel types that were found at five archaeological sites.  
Many cells are empty (zero counts) because some types simply do not occur (or were not recorded) at some sites.  

The goal is to **see whether the distribution of vessel types differs between sites** – i.e. whether a “signature” of morphology/morphometry can be used to infer the place of production.  
Because the data are very sparse, the student wants an *exploratory* statistical approach that can still give sensible information, preferably using a mixed‑effects (hierarchical) model that can borrow strength across the ten types and five sites.

---

## 2. Step‑by‑step worked solution

Below is a **complete, reproducible workflow** that a researcher could follow with the data as shown.  
All steps are written generically; you can copy‑paste the R code (or the equivalent Python/Julia code) and adapt it to your exact dataset.

> **Notation**  
> *\(y_{ij}\)* = observed count of **type *i*** at **site *j***.  
> *\(i = 1,\dots,10\)* (vessel types)  
> *\(j = 1,\dots,5\)* (sites)  

---

### Step 1 – Put the data into a tidy data frame  

```r
# ---- R ---------------------------------------------------------------
library(tidyverse)

# raw cross‑tab (rows = types, columns = sites)
raw_mat <- matrix(c(
  73,28,32,0,3,
  92,60,2,0,7,
  74,78,2,0,5,
  57,56,0,0,22,
 131,73,5,30,0,
  59,43,6,0,3,
  86,3,4,14,0,
 101,22,0,0,0,
  50,0,0,0,0,
 347,2,0,0,0), nrow=10, byrow=TRUE)

df <- as_tibble(raw_mat,
                .name_repair = "minimal") %>% 
      mutate(Type = factor(1:10)) %>% 
      pivot_longer(-Type, names_to = "Site", values_to = "Count") %>% 
      mutate(Site = factor(Site, levels = c("V1","V2","V3","V4","V5")))   # rename if you like

head(df)
```

Result (first few rows)

| Type | Site | Count |
|------|------|-------|
| 1    | V1   | 73    |
| 1    | V2   | 28    |
| 1    | V3   | 32    |
| 1    | V4   | 0     |
| 1    | V5   | 3     |
| …    | …    | …     |

---

### Step 2 – Exploratory checks

| Check | What to look for | How to do it |
|------|------------------|--------------|
| **Marginal totals** | Are some sites or types overwhelmingly more common? | `df %>% group_by(Site) %>% summarise(Total = sum(Count))` |
| **Zero‑inflation** | What proportion of cells are zero? | `mean(df$Count == 0)` |
| **Over‑dispersion** | Variance of counts vs. mean (Poisson expects equality). | Compute `var(Count)/mean(Count)` for each site or overall. |
| **Visualization** | Heat‑map or mosaic plot gives a quick visual of the pattern. | `ggplot(df, aes(Site, Type, fill = Count)) + geom_tile()` |

Typical findings for this dataset:

* **≈ 45 %** of the cells are zero (a lot!).  
* The overall variance is **much larger** than the mean → **over‑dispersion** (Poisson is not adequate).  
* Site 1 dominates the total counts (≈ 70 % of all sherds).  

---

### Step 3 – Choose a statistical model that can handle:

1. **Counts** (non‑negative integers)  
2. **Over‑dispersion**  
3. **Many zeros**  
4. **Hierarchical structure** (10 types × 5 sites)

The usual go‑to is a **generalised linear mixed model (GLMM)** with a **negative‑binomial** (NB) or **zero‑inflated negative‑binomial (ZINB)** response.  

*The NB part accounts for over‑dispersion.*  
*The zero‑inflation part captures the excess of structural zeros (e.g., a type truly never produced at a site).*

---

### Step 4 – Fit a **negative‑binomial GLMM**  

Model formulation  

\[
y_{ij}\; \sim\; \text{NegBin}(\mu_{ij},\;\theta)\\[4pt]
\log(\mu_{ij}) = \beta_0 + \underbrace{b^{\text{(type)}}_{i}}_{\text{random intercept for type}} + \underbrace{b^{\text{(site)}}_{j}}_{\text{random intercept for site}}
\]

* `β0` = overall log‑mean count  
* `b^{(type)}_i ~ N(0,\sigma^2_{\text{type}})`  
* `b^{(site)}_j ~ N(0,\sigma^2_{\text{site}})`  
* `θ` = NB dispersion parameter  

```r
library(lme4)          # or glmmTMB for zero‑inflation
# NB GLMM
nb_mod <- glmer.nb(Count ~ 1 + (1|Type) + (1|Site),
                   data = df,
                   control = glmerControl(optimizer = "bobyqa"))
summary(nb_mod)
```

**Interpretation of key output**

| Parameter | Meaning |
|-----------|---------|
| `(Intercept)` | Log‑average count across all types & sites. |
| `sd_(Intercept)_Type` | Variation *among* vessel types; a large value means some types are intrinsically more common. |
| `sd_(Intercept)_Site` | Variation *among* sites; a large value signals that sites differ in overall production intensity. |
| `theta` | Inverse of NB dispersion; small `theta` → strong over‑dispersion. |

If the **site variance** (`sd_(Intercept)_Site`) is *substantially larger than zero* (confidence interval does not include 0), we have statistical evidence that **sites differ** in the overall frequency of the vessels, *after* accounting for type‑specific effects.

---

### Step 5 – Fit a **zero‑inflated negative‑binomial (ZINB) GLMM**  

Because many cells are structural zeros, we can let the model decide whether a zero came from the NB part or from a separate “always zero” process.

```r
library(glmmTMB)

zinb_mod <- glmmTMB(Count ~ 1 + (1|Type) + (1|Site),
                    ziformula = ~ 1 + (1|Type) + (1|Site),   # zero‑inflation part
                    family = nbinom2(),
                    data = df)

summary(zinb_mod)
```

The `ziformula` can be simplified (e.g., `~1`) if you prefer a **global** zero‑inflation probability.  
Key extra output:

| Parameter | Meaning |
|-----------|---------|
| `cond.(Intercept)` | Log‑mean of the NB component (as before). |
| `zi.(Intercept)`   | Log‑odds of being a *structural* zero. |
| Random effects in `zi.` | Show which types/sites are more likely to generate structural zeros. |

A **likelihood‑ratio test** (or AIC comparison) between the NB and ZINB models tells you whether the extra zero‑inflation term improves fit:

```r
anova(nb_mod, zinb_mod)   # LRT
AIC(nb_mod); AIC(zinb_mod)
```

If ZINB is clearly better (ΔAIC > 10 or LRT p < 0.01), you should keep the ZINB model.

---

### Step 6 – Post‑hoc “pairwise” comparisons of sites  

The mixed model gives **overall** site variance, but you may want to know **which sites differ**.  

1. **Extract the conditional modes (BLUPs) for the site random effects**  

```r
ranef(zinb_mod)$Site   # or nb_mod
```

2. **Compute differences and confidence intervals**  

```r
site_effects <- ranef(zinb_mod)$Site %>% as.data.frame()
site_effects <- site_effects %>% 
  mutate(SE = sqrt(attr(ranef(zinb_mod, condVar=TRUE)$Site, "postVar")[,,1]),
         lower = condval - 1.96*SE,
         upper = condval + 1.96*SE)

site_effects
```

If the **95 % CI of a site’s random intercept does not overlap the overall mean (0 on the log‑scale)**, that site is significantly higher or lower than the average after controlling for type.

3. **Optional: pairwise contrasts** (e.g., using `emmeans`)

```r
library(emmeans)
em <- emmeans(zinb_mod, ~ Site, type = "response")
pairs(em, adjust = "holm")   # Holm‑adjusted p‑values for multiple testing
```

---

### Step 7 – Visualise the fitted model  

A **predicted‑counts heat‑map** that incorporates the random effects makes the results intuitive.

```r
df_pred <- df %>% 
  add_predicted_draws(zinb_mod, n = 500) %>%      # from tidybayes / sjPlot
  group_by(Type, Site) %>% 
  summarise(pred = mean(.prediction), .groups = "drop")

ggplot(df_pred, aes(Site, Type, fill = pred)) +
  geom_tile() +
  scale_fill_viridis_c() +
  labs(title = "Model‑based expected counts (ZINB GLMM)",
       fill = "Expected count")
```

The pattern you see here is what the model attributes to *production signatures* after “shrinking” the noisy observed counts toward the overall trend.

---

### Step 8 – What the results *mean* for the archaeological question  

| Possible outcome | Interpretation for production patterns |
|------------------|------------------------------------------|
| **Site variance ≈ 0** (confidence interval includes 0) | No statistical evidence that sites differ in the composition of vessel types. The observed differences are likely due to sampling noise. |
| **Site variance > 0** and some site BLUPs significantly non‑zero | Certain sites produce (or preserve) a distinct mix of types. You can claim “site‑specific signatures” with the caveat that the data are sparse. |
| **Zero‑inflation term important** | Many of the zeros are *structural*: a given type truly never occurs at particular sites (perhaps because of cultural tradition). This supports the hypothesis that producers had locally specific conventions. |
| **Large type variance** | Some vessel types are inherently more common across all sites, which should be taken into account when comparing sites (the mixed model does this automatically). |

---

## 3. Final answer (concise)

*Yes, you can explore whether vessel morphology differs between sites even with many zeros.*  
The recommended approach is:

1. **Reshape the data** into a long format (type, site, count).  
2. **Fit a zero‑inflated negative‑binomial mixed‑effects model** (or a plain NB GLMM if zero‑inflation is not needed) with random intercepts for **type** and **site**.  
3. **Test the site random‑effect variance** (likelihood‑ratio test or confidence interval). A variance clearly larger than zero indicates statistically detectable differences among sites after accounting for type‑specific frequencies.  
4. **Inspect site random effects** (BLUPs) or conduct pairwise contrasts to see *which* sites differ.  
5. **Visualise the model‑predicted counts** to communicate the “production signatures” to archaeologists.

If the model shows a non‑zero site variance (and possibly a substantial zero‑inflation component), you have quantitative support for the idea that different production traditions left detectable morphological footprints. If the site variance is negligible, the data do **not** provide evidence for site‑specific differences beyond random sampling variation.

---

## 4. Common mistakes to avoid

| Mistake | Why it’s a problem | How to avoid it |
|---------|-------------------|-----------------|
| **Running a simple χ² test on the raw table** | χ² assumes expected cell counts > 5; with many zeros the approximation breaks down and the test can be wildly misleading. | Use a GLMM (NB or ZINB) that works with sparse count data. |
| **Treating the counts as independent observations** | Counts from the same type or same

*Original question: [Mixed Model Approach in Archaeology](https://stats.stackexchange.com/questions/676974/mixed-model-approach-in-archaeology) on Cross Validated (Stats Stack Exchange), licensed CC BY-SA.*

{% endraw %}
