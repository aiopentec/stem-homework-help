---
layout: question
title: Unknown start times &amp; idle gaps in survival analysis of log data — interval-censored
  model or MI?
author: StemFix Bot
category: stats
subject: stats
description: 'Step-by-step statistics solution: Unknown start times &amp; idle gaps
  in survival analysis of log data — interval-censored model or MI?'
tags:
- stats
---

{% raw %}
*As an Amazon Associate, I earn from qualifying purchases.* For more practice problems like this, see [Schaum's Outline of Statistics, 6th Edition](https://www.amazon.com/dp/1260011461?tag=aiopentec20-20).

---

## 1️⃣  What the student is really asking  

| Situation | What we observe | What we *don’t* observe | How it shows up in a survival analysis |
|-----------|----------------|------------------------|----------------------------------------|
| **Right‑censoring** | The student never solves the problem → we only know the time of the last submission. | – | Standard right‑censoring (the event “first correct submission’’ never occurs). |
| **Unknown start time** (`x`) | We see the *last* submission on the previous problem (`L`) and the *first* submission on the current problem (`R`). | The exact moment the student actually began thinking about the current problem (`S`). | `S` lies somewhere in the interval \((L,R]\). If the interval is huge (overnight break) we cannot trust it. |
| **Idle gaps** (`y`) | Two consecutive submissions on the same problem, with a long elapsed wall‑clock time. | How much of that elapsed time was spent *away* from the computer (idle) vs. actually working on the problem. | If the idle part is not removed, the recorded “time‑to‑event’’ is inflated and biases the hazard. |

The student wants to know **how to estimate the effect of a time‑varying strategy (categorical) on the hazard of solving the problem**, while dealing with the two “odd’’ censoring mechanisms above.  

Two ideas have been floated:

1. **Fit an interval‑censored survival model** (which can treat the start‑time interval properly) – but most software for interval‑censored data does **not** let you include a *time‑varying* covariate.
2. **Multiple imputation (MI)** of the unknown start times and idle periods, then run a usual Cox model – but the student is unsure whether MI is appropriate and how to do it correctly.

Below is a **complete, step‑by‑step solution** that shows why **multiple imputation combined with a counting‑process Cox model** (or a parametric analogue) is a sound approach, and how to implement it in practice.  

---

## 2️⃣  Full worked solution  

### Step 0 – Notation  

| Symbol | Meaning |
|--------|---------|
| \(i = 1,\dots,n\) | student‑problem observations |
| \(L_i\) | timestamp of the last submission on the *previous* problem (lower bound for start) |
| \(R_i\) | timestamp of the first submission on the *current* problem (upper bound for start) |
| \(S_i\) | **true** (unobserved) start time of the current problem |
| \(C_i\) | censoring indicator for the *event* (1 = solved, 0 = never solved) |
| \(T_i\) | observed wall‑clock time from the *first* submission on the current problem to the *first correct* submission (or last submission if censored) |
| \(G_{ij}\) | observed gap between submission \(j\) and \(j+1\) on the same problem |
| \(\tilde G_{ij}\) | **active** (non‑idle) part of \(G_{ij}\) – what we would like to recover |
| \(\mathbf{Z}_i(t)\) | vector of covariates that can change over *active* time (here: the strategy indicator) |
| \(h_i(t)\) | hazard of solving at active time \(t\) for observation \(i\) |
| \(M\) | number of imputed data sets (typical values: 20–50) |

---

### Step 1 – Decide what is *missing* and what is *censored*  

| Quantity | Observed? | Type of missingness |
|----------|-----------|---------------------|
| \(S_i\) (true start) | No (only interval \((L_i,R_i]\)) | **Interval‑censored latent variable** – treat as missing data that we can *impute* because the interval is known. |
| \(\tilde G_{ij}\) (active part of a long gap) | No (only the total gap \(G_{ij}\) is observed) | **Missing at random (MAR)** if we assume the size of an idle break depends only on observed information (e.g., length of the gap, time of day). |
| Event time (first correct) | Partially observed – right‑censored for some students | Standard right‑censoring – keep it as‑is in the survival model. |

Thus **all the “problematic’’ pieces are *missing* rather than *censored***, which makes MI a natural tool.

---

### Step 2 – Choose an imputation model for the unknown start time  

A convenient and often realistic assumption is that, **conditional on the observed interval**, the true start time is *uniform* over \((L_i,R_i]\).  
If you have reason to believe that students tend to start soon after the previous submission (e.g., most gaps are short), you can use a **truncated exponential** or **truncated normal** distribution that places more mass near the left endpoint.

**Imputation model 1 (uniform):**  

\[
S_i^{(m)} \sim \text{Uniform}(L_i,\,R_i) \qquad\text{for } m=1,\dots,M
\]

**Imputation model 2 (truncated exponential):**  

\[
S_i^{(m)} \mid L_i,R_i \sim \text{Exp}(\lambda) \text{ truncated to } (L_i,R_i]
\]

Choose \(\lambda\) by fitting an exponential to the *empirical* distribution of short gaps (those you deem trustworthy).  
For records flagged as “untrustworthy’’ (the Tukey‑fence outliers) you **do not** impute a start time; instead you treat them as *completely missing* and let the imputation model draw a value from the overall distribution of start‑times (the same uniform or exponential you used for the trustworthy records).

---

### Step 3 – Impute the idle portions of long gaps  

1. **Identify “long’’ gaps** – e.g., any \(G_{ij}\) that exceeds the 75th percentile plus 1.5 × IQR of all gaps *within the same problem* (the same Tukey‑fence rule used for start‑time intervals).  

2. **Model the *active* part** of a gap as a fraction of the observed gap. A simple model:  

\[
\tilde G_{ij}^{(m)} = \rho_{ij}\, G_{ij},\qquad 
\rho_{ij} \sim \text{Beta}(\alpha,\beta)
\]

Estimate \(\alpha,\beta\) from the *short* gaps (those you trust to be almost entirely active). The Beta distribution is bounded on \([0,1]\) and can capture the typical proportion of “working’’ time inside a gap.

3. **Draw** \(\rho_{ij}^{(m)}\) for each long gap, then compute \(\tilde G_{ij}^{(m)}\).  

If a gap is deemed “untrustworthy’’ (e.g., overnight), you can set \(\tilde G_{ij}^{(m)} = 0\) (i.e., treat the whole gap as idle) or let the Beta draw be near zero; the exact rule is a modeling choice, but it must be applied consistently across imputations.

---

### Step 4 – Build the *active* event time for each imputed data set  

For each imputed dataset \(m\):

1. **Compute the total active time** spent *before* the first correct submission (or censoring).  

   \[
   \text{ActiveTime}_i^{(m)} = 
   \underbrace{(T_i - (R_i - S_i^{(m)}))}_{\text{wall‑clock time after first submission}} 
   - \sum_{j\in\mathcal{L}_i} \bigl(G_{ij} - \tilde G_{ij}^{(m)}\bigr)
   \]

   where \(\mathcal{L}_i\) is the set of long gaps for observation \(i\).  
   In words: start from the observed wall‑clock interval, subtract the *unknown* part of the start interval (the time before the first submission), then subtract the *idle* parts of long gaps.

2. **Create a counting‑process representation** (the “start‑stop’’ format required for a Cox model with time‑varying covariates):  

   * **Entry time** = 0 (the moment the student actually begins *working* on the problem, i.e. after we have removed the unknown pre‑start interval).  
   * **Exit time** = \(\text{ActiveTime}_i^{(m)}\).  
   * **Event indicator** = \(C_i\) (1 if solved, 0 if right‑censored).  

   If a student changes strategy at active time \(t^\star\), split the row at \(t^\star\) and assign the appropriate strategy label to each interval. Most software (e.g., `survival::coxph` with `Surv(start, stop, event)`) will handle this automatically.

---

### Step 5 – Fit the survival model on each imputed data set  

**Model of interest (Cox proportional‑hazards with a time‑varying strategy):**

\[
h_i(t) = h_0(t)\,\exp\bigl\{\beta_{\text{strategy}}(t)\, \text{Strategy}_i(t) + \boldsymbol\gamma^\top \mathbf{X}_i \bigr\},
\]

where \(\mathbf{X}_i\) may contain baseline covariates (e.g., prior knowledge, problem difficulty).  

In R:

```r
library(survival)
fit_m <- coxph(Surv(start, stop, event) ~ strategy + X1 + X2,
               data = imp_data_m, robust = FALSE)
```

Repeat for all \(M\) imputed data sets, storing the estimate \(\hat\beta^{(m)}\) and its variance \(\hat V^{(m)}\).

---

### Step 6 – Combine the \(M\) results with Rubin’s Rules  

Let  

* \(\bar\beta = \frac{1}{M}\sum_{m=1}^M \hat\beta^{(m)}\) – pooled point estimate.  
* \(\bar V = \frac{1}{M}\sum_{m=1}^M \hat V^{(m)}\) – within‑imputation variance.  
* \(B = \frac{1}{M-1}\sum_{m=1}^M (\hat\beta^{(m)}-\bar\beta)^2\) – between‑imputation variance.  

Total variance  

\[
T = \bar V + \left(1+\frac{1}{M}\right) B .
\]

The pooled standard

*Original question: [Unknown start times &amp; idle gaps in survival analysis of log data — interval-censored model or MI?](https://stats.stackexchange.com/questions/677175/unknown-start-times-idle-gaps-in-survival-analysis-of-log-data-interval-cens) on Cross Validated (Stats Stack Exchange), licensed CC BY-SA.*

{% endraw %}
