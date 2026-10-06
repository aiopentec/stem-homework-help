---
layout: question
title: What makes time-series data irregular-spaced? How to code in glmmTMB?
author: StemFix Bot
category: stats
subject: stats
description: 'Step-by-step statistics solution: What makes time-series data irregular-spaced?
  How to code in glmmTMB?'
tags:
- stats
---

{% raw %}
*As an Amazon Associate, I earn from qualifying purchases.* For more practice problems like this, see [Schaum's Outline of Statistics, 6th Edition](https://www.amazon.com/dp/1260011461?tag=aiopentec20-20).

---

## 1. What the student is asking (in plain language)

The student wants to:

1. **Know whether his data are “regular‑spaced” or “irregular‑spaced” time‑series.**  
   - Is the definition based on the raw dates that appear in each row, or on the time variable he *chooses* to model (e.g., year + season)?

2. **Decide which correlation structure to use in `glmmTMB`.**  
   - Should he use an AR(1) structure (`ar1()`) that assumes equally spaced observations?  
   - Or an Ornstein‑Uhlenbeck (OU) structure (`ou()`) that can handle unequal gaps?

3. **Learn how to prepare the time variable for these structures, in particular how to use `numFactor()`** (the function that turns a numeric time vector into a “numeric factor” that `glmmTMB` can recognise as a time index).

The answer must explain the concepts, show how to check spacing, and give a concrete, reproducible `glmmTMB` model that respects the data’s temporal layout.

---

## 2. Step‑by‑step solution  

### 2.1 Define “regular” vs “irregular” spacing

| Concept | Definition | Consequence for correlation structures |
|---------|------------|----------------------------------------|
| **Regular (equally‑spaced) series** | The difference between successive time points is *exactly* the same for **all** observations that belong to the same “group” (e.g., same site). Typically measured in integer units (days, weeks, months, years). | AR(1), MA(1), ARMA, etc. can be used because the correlation only depends on the *lag* (the number of steps) and not on the actual clock time between steps. |
| **Irregular (unequally‑spaced) series** | At least one pair of successive observations within a group has a different time gap. Gaps can be 1 day, 3 days, 6 months, … | A pure AR(1) *cannot* correctly model the correlation because its formula `ρ^{lag}` assumes unit‑time steps. An OU (continuous‑time AR(1)) or a custom correlation that incorporates the actual time difference should be used. |

**Key point:** The *definition* depends on the **time variable you feed to the correlation structure**, **not** on the raw date column that might be present in the data frame. If you decide to model “year × season” as the time index and every “year‑season” combination occurs exactly once per site, then the series is *regular* on that coarser scale, even though the underlying dates are irregular.

### 2.2 Inspect the data

```r
library(dplyr)

shiny_toad <- read.csv(
  "https://raw.githubusercontent.com/NateLaS/Toadfish/main/share_version%20-%20toadfish.csv"
)

# Look at the raw date information
head(shiny_toad %>% select(Site, CYR, Season, JDay))
```

| Site | CYR | Season | JDay |
|------|-----|--------|------|
| 1    | 2013| DRY    | 1    |
| 1    | 2013| DRY    | 2    |
| …    | …   | …      | …    |

The `JDay` column (Julian day) shows the **exact day of the year** a sample was taken.  

Now compute the gaps *within each Site‑Season*:

```r
gap_df <- shiny_toad %>% 
  arrange(Site, Season, CYR, JDay) %>%               # sort chronologically
  group_by(Site, Season) %>% 
  mutate(gap = as.numeric(difftime(
    as.Date(paste(CYR, JDay, sep = "-"), format = "%Y-%j"),
    lag(as.Date(paste(CYR, JDay, sep = "-"), format = "%Y-%j")),
    units = "days"
  )))

summary(gap_df$gap)
```

If the summary shows many different values (0, 1, 2, … up to 173 days in your print‑out), the series **is irregular** on the day‑scale.

### 2.3 Decide which time scale to model

The student says: *“I’m only modeling year and season – not julian day.”*  

Two possible modelling choices:

| Option | Time index | Regularity | When it is appropriate |
|--------|------------|------------|------------------------|
| **Year × Season** (e.g., 2013‑DRY, 2013‑WET, …) | A factor with one level per **year‑season** per site | **Regular** *if* every site has at most one observation per year‑season (the table in the question shows that). | Use a **discrete AR(1)** (`ar1()`) because the lag between consecutive levels is exactly one *year‑season* step. |
| **Exact Julian dates** (or days since first observation) | Numeric (e.g., days) | **Irregular** (gaps of 0–173 days) | Use a **continuous‑time OU** (`ou()`) that incorporates the actual time differences. |

Because the model already contains the fixed effect `CYR*Season`, it is natural to treat *year‑season* as the temporal ordering. We will show both approaches, but the **simpler** and *most common* one for this data is the AR(1) on the *year‑season* index.

### 2.4 Create a numeric‑factor time index

`glmmTMB` expects a **numeric factor** (class `numFactor`) for correlation structures.  

```r
library(glmmTMB)

# 1) Create a combined factor "YearSeason"
shiny_toad <- shiny_toad %>% 
  mutate(YearSeason = interaction(CYR, Season, sep = "_"))

# 2) Convert to numeric factor (the numeric codes will be 1,2,3,… in the order they appear)
shiny_toad$YearSeason_num <- numFactor(shiny_toad$YearSeason)

# Check the levels
levels(shiny_toad$YearSeason_num)[1:6]
# [1] "2013_DRY" "2013_WET" "2014_DRY" "2014_WET" "2015_DRY" "2015_WET"
```

> **Why `numFactor`?**  
> `glmmTMB` stores the *order* of the levels as the integer codes (1, 2,…). The correlation matrix is built from those integers, so the ordering matters. `numFactor()` guarantees that the ordering is the *observed* ordering (by default alphabetical). If you need a custom ordering (e.g., chronological), first set the factor levels appropriately:

```r
shiny_toad$YearSeason <- factor(shiny_toad$YearSeason,
                                levels = sort(unique(shiny_toad$YearSeason)))
shiny_toad$YearSeason_num <- numFactor(shiny_toad$YearSeason)
```

### 2.5 Fit a model with an AR(1) correlation on the *year‑season* index  

```r
fit_ar1 <- glmmTMB(
  total_count ~ CYR * Season + (1 | Site),
  family = nbinom2,
  data   = shiny_toad,
  # correlation structure: AR(1) within each Site, ordered by YearSeason_num
  covstruct = list(
    Site = ~ ar1(YearSeason_num)   # "Site" is the grouping factor for the correlation
  )
)

summary(fit_ar1)
```

- `ar1(YearSeason_num)` tells `glmmTMB` to assume that, **within each Site**, the correlation between two observations is  

  \[
  \text{Corr}(y_{t}, y_{t+k}) = \rho^{k},
  \]

  where `k` is the *number of year‑season steps* between them (1 = adjacent seasons, 2 = skip one season, …).  

- Because the series is regular on this scale, the AR(1) assumption is justified.

### 2.6 Fit a model with an Ornstein‑Uhlenbeck (OU) correlation on exact dates  

If you decide to keep the original dates (e.g., days), you must supply the *numeric* time distance, not a factor.

```r
# 1) Create a numeric time variable: days since 1‑Jan‑2013
shiny_toad <- shiny_toad %>% 
  mutate(date = as.Date(paste(CYR, JDay, sep = "-"), format = "%Y-%j"),
         days_since_start = as.numeric(date - as.Date("2013-01-01")))

# 2) Convert to numeric factor (the values themselves are the distances)
shiny_toad$days_numfac <- numFactor(shiny_toad$days_since_start)

# 3) Fit OU model (continuous‑time AR(1))
fit_ou <- glmmTMB(
  total_count ~ CYR * Season + (1 | Site),
  family = nbinom2,
  data   = shiny_toad,
  covstruct = list(
    Site = ~ ou(days_numfac)    # OU uses the actual numeric distances
  )
)

summary(fit_ou)
```

- The OU correlation has the form  

  \[
  \text{Corr}(y_{t}, y_{s}) = \exp\!\bigl(-\alpha\,|t-s|\bigr),
  \]

  where `|t‑s|` is the absolute difference in **days** (or any time unit you chose).  
- This automatically down‑weights correlations between observations that are far apart (e.g., 173 days) and up‑weights those that are close (e.g., 1 day).

### 2.7 Which model should you use?

| Situation | Recommended structure |
|-----------|-----------------------|
| You are only interested in **year‑season** effects and each site has at most one record per year‑season (as in the table you printed). | **AR(1)** on the ordered `YearSeason_num`. It is simpler, faster, and interpretable (correlation between consecutive seasons). |
| You suspect that *within* a season the exact date matters (e.g., a rainy event in early June vs late June) **or** the gaps are highly variable. | **OU** on the exact date (`days_numfac`). |
| You need both (e.g., season‑level fixed effects *and* day‑level residual correlation). | Fit a **nested** structure: an OU within season, or include both a factor for season and an OU for days. This is more advanced and may require custom correlation matrices (beyond the basic `glmmTMB` syntax). |

### 2.8 Full reproducible script  

```r
library(dplyr)
library(glmmTMB)

# -------------------------------------------------
# 1. Load data
# -------------------------------------------------
shiny_toad <- read.csv(
  "https://raw.githubusercontent.com/NateLaS/Toadfish/main/share_version%20-%20toadfish.csv"
)

# -------------------------------------------------
# 2. Make a regular time index (Year‑Season)
# -------------------------------------------------
shiny_toad <- shiny_toad %>% 
  mutate(YearSeason = interaction(CYR, Season, sep = "_")) %>% 
  # ensure chronological ordering
  mutate(YearSeason = factor(YearSeason,
                             levels = sort(unique(YearSeason)))) %>% 
  mutate(YearSeason_num = numFactor(YearSeason))

# -------------------------------------------------
# 3. Fit AR(1) model (regular spaced on Year‑Season)
# -------------------------------------------------
fit_ar1 <- glmmTMB(
  total_count ~ CYR * Season + (1 | Site),
  family = nbinom2,
  data   = shiny_toad,
  covstruct = list(Site = ~ ar1(YearSeason_num))
)

cat("\n--- AR(1) model summary ---\n")
print(summary(fit_ar1))

# -------------------------------------------------
# 4. (Optional) Fit OU model on exact dates (irregular)
# -------------------------------------------------
shiny_toad <- shiny_toad %>% 
  mutate(date = as.Date(paste(CYR, JDay, sep = "-"), format = "%Y-%j"),
         days_since_start = as.numeric(date - as.Date("2013-01-01")),
         days_numfac = numFactor(days_since_start))

fit_ou <- glmmTMB(
  total_count ~ CYR * Season + (1 | Site),
  family = nbinom2,
  data   = shiny_toad,
  covstruct = list(Site = ~ ou(days_numfac))
)

cat("\n--- OU model summary ---\n")
print(summary(fit_ou))
```

Run the script; you will obtain two model objects (`fit_ar1` and `fit_ou`). Compare the estimated correlation parameters:

- In the AR(1) output you will see `rho` (the lag‑1 autocorrelation).  
- In the OU output you will see `alpha` (the decay rate).  

If the `rho` is close to 1 and the `alpha` corresponds to a half

*Original question: [What makes time-series data irregular-spaced? How to code in glmmTMB?](https://stats.stackexchange.com/questions/677353/what-makes-time-series-data-irregular-spaced-how-to-code-in-glmmtmb) on Cross Validated (Stats Stack Exchange), licensed CC BY-SA.*

{% endraw %}
