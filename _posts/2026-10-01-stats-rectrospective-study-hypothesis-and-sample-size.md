---
layout: question
title: Rectrospective study hypothesis and sample size
author: StemFix Bot
category: stats
subject: stats
description: 'Step-by-step statistics solution: Rectrospective study hypothesis and
  sample size'
tags:
- stats
---

{% raw %}
*As an Amazon Associate, I earn from qualifying purchases.* For more practice problems like this, see [Schaum's Outline of Statistics, 6th Edition](https://www.amazon.com/dp/1260011461?tag=aiopentec20-20).

---

## 1. What the student is really asking  

A sponsor wants to run a **retrospective (observational) comparison** of two chemotherapy regimens  

| Group | Expected 2‑year OS (or PFS) |
|------|-----------------------------|
| Experimental drug | **≈ 90 %** survivors |
| Standard of care (SoC) | **≈ 95 %** survivors |

*The experimental drug is believed to be **slightly less effective** (lower survival) but possibly **better tolerated** and to give a higher **quality‑of‑life (QoL)**.*

The sponsor would like to

1. **Demonstrate non‑inferiority (NI)** of the experimental drug with respect to survival (OS/PFS).  
   *Acceptable NI margin = 5–7 %* (i.e. they would accept the experimental drug being up to 5–7 % worse than SoC).

2. **If the NI claim fails**, still test whether QoL is better.

The student is stuck because, with survival rates of 90–95 %, the **event rate is very low**. Standard sample‑size formulas for a binary endpoint (difference in proportions) or for a hazard ratio (HR) give **enormous required sample sizes** (often “practically infinite”). They ask:

* How can we justify an analysis when the required sample is unrealistic?  
* Which effect measure should be used (risk difference, HR, …)?  
* How to present confidence intervals, power, and sensitivity analyses?  
* How to handle subgroup analyses if the overall NI test fails but QoL looks better?

Below is a step‑by‑step worked solution that addresses each of these points.

---

## 2. Step‑by‑step solution  

### 2.1 Clarify the scientific question & the statistical framework  

| Goal | Statistical formulation |
|------|--------------------------|
| **Primary efficacy** | *Is the experimental drug **not clinically worse** than SoC for survival?*  → **Non‑inferiority test** on a survival‑type parameter. |
| **Secondary benefit** | *Is QoL better with the experimental drug?* → **Super‑ superiority test** on a QoL endpoint (mixed model). |
| **Design** | Retrospective cohort (observational). Causal‑inference methods (propensity scores, inverse‑probability weighting, doubly‑robust estimators, etc.) will be used to adjust for confounding. |

Because the study is retrospective we **cannot control the sample size**; we must work with the data we have and be transparent about the limits of inference.

---

### 2.2 Choose an appropriate estimand for survival  

When the event (death or progression) is rare, the **hazard ratio (HR)** is often unstable because it is estimated from very few failures. Several alternatives are more suitable:

| Estimand | What it measures | Why it can be preferable here |
|----------|------------------|-------------------------------|
| **Risk difference (RD) at a fixed time** *t* (e.g., 2 years) | \(\Delta(t)=S_E(t)-S_C(t)\) where \(S_E, S_C\) are survival probabilities. | Directly reflects the absolute difference the sponsor cares about (5 % margin). Uses the *cumulative* endpoint, not the instantaneous hazard. |
| **Risk ratio (RR) at time *t*** | \(\frac{S_E(t)}{S_C(t)}\) | Interpretable but still a proportion; confidence limits can be wide with few events. |
| **Restricted Mean Survival Time (RMST) difference** | \(\text{RMST}_E(\tau)-\text{RMST}_C(\tau)=\int_0^{\tau} [S_E(u)-S_C(u)]du\) | Summarizes the *area under the survival curve* up to a clinically relevant horizon \(\tau\) (e.g., 2 years). Works even when proportional‑hazards assumption fails. |
| **Cumulative incidence / incidence rate difference** | \(\frac{d_E}{\text{person‑time}_E} - \frac{d_C}{\text{person‑time}_C}\) | Uses *events per person‑time*; can be more efficient if follow‑up times differ. |

**Recommendation:**  
*Primary analysis*: **Risk difference (or RMST difference) at a prespecified time point** (e.g., 2 years).  
*Secondary (exploratory) analysis*: HR from a Cox model *only* to illustrate the pattern, but **do not base the NI claim on the HR**.

---

### 2.3 Define the non‑inferiority hypothesis  

Let  

* \(p_E = S_E(t)\) = survival proportion in experimental group at time \(t\).  
* \(p_C = S_C(t)\) = survival proportion in control (SoC) group at time \(t\).  

The **NI margin** \(\delta\) is the largest *worse* absolute difference we are willing to accept (e.g., \(\delta = -0.05\) for a 5 % margin).

\[
\begin{aligned}
H_0 &: p_E - p_C \le -\delta \quad\text{(experimental is inferior)}\\
H_1 &: p_E - p_C > -\delta \quad\text{(experimental is non‑inferior)}
\end{aligned}
\]

*Note*: The margin must be **clinically justified** (e.g., based on historical data, regulatory guidance, or a pre‑specified “preserve a fraction of the effect” rule).  

---

### 2.4 Estimation and confidence‑interval (CI) approach  

1. **Estimate** the survival probabilities at \(t\) using the **Kaplan–Meier (KM) estimator** (or a weighted KM if using IPTW).  
2. **Compute the risk difference** \(\hat\Delta = \hat p_E - \hat p_C\).  
3. **Obtain a 95 % (or one‑sided 97.5 %) confidence interval** for \(\Delta\).  
   * Use the **standard error of the difference** from the two KM curves (e.g., Greenwood’s formula + delta method).  
   * With IPTW or propensity‑score matching, use **robust (sandwich) variance estimators** or **bootstrap** to capture the extra variability introduced by weighting/matching.  

**Decision rule** (one‑sided 2.5 % level, usual for NI):

*If the lower bound of the (one‑sided) CI > \(-\delta\), declare non‑inferiority.*  

Equivalently, with a two‑sided 95 % CI, **non‑inferiority holds if the entire CI lies to the right of \(-\delta\)**.

*Why CI rather than a p‑value?*  
In NI trials the CI method is preferred because it directly shows whether the pre‑specified margin is excluded, whereas a p‑value depends on the (often arbitrary) α level.

---

### 2.5 Why the “infinite” sample‑size problem occurs  

If you plug the *expected* survival rates (90 % vs 95 %) into the classic **binary‑outcome** sample‑size formula for a risk‑difference NI test:

\[
n \approx \frac{(z_{1-\alpha}+z_{1-\beta})^2 \bigl[p_C(1-p_C)+p_E(1-p_E)\bigr]}{(\delta + p_E - p_C)^2}
\]

the denominator \((\delta + p_E - p_C)^2\) becomes **very small** because the true difference (5 %) is *close* to the NI margin (e.g., 5 %). If the margin equals the expected difference, the required \(n\) → ∞.  

**Interpretation:** With a *tight* NI margin, the trial must be **large enough to rule out even a tiny excess of failures**. When the event rate is low, the variance of the estimated proportion is tiny, so you need many subjects to get a precise estimate.

**What to do?**  

| Option | When it helps | How to implement |
|--------|---------------|------------------|
| **Enlarge the NI margin** (e.g., 7 % instead of 5 %) | If a 7 % loss of survival is clinically acceptable. | Re‑run the sample‑size calculation and justify the new margin with clinicians and regulators. |
| **Choose a later time point** (e.g., 5 years) | When survival curves separate more over longer follow‑up, increasing the absolute difference. | Estimate expected survival at that horizon; recompute margin accordingly. |
| **Use a *relative* margin** (e.g., HR ≤ 1.25) | If the regulatory body accepts a relative margin rather than an absolute one. | Compute the HR from historical data; set the NI margin as the upper bound of the 95 % CI for HR. |
| **Switch to RMST difference** | RMST incorporates the whole survival curve and can be more efficient when events are rare. | Specify a τ (e.g., 2 years) and a clinically meaningful RMST difference (e.g., 0.1 year). Use the RMST‑difference sample‑size formula. |
| **Accept a higher α (e.g., 0.10 one‑sided)** | When the study is exploratory and a false‑negative is less concerning than a false‑positive. | Document the rationale; adjust the CI accordingly. |
| **Combine endpoints** (e.g., a composite of death + grade ≥ 3 toxicity) | If the experimental drug’s safety advantage is important. | Define the composite, estimate its event rate, and power the NI test on that outcome. |

If **none of the above** yields a realistic sample size, you must acknowledge that *the data are insufficient to prove NI* and treat the analysis as **exploratory**. Present the point estimate, the confidence interval, and a clear statement of the limitation.

---

### 2.6 Power and post‑hoc calculations  

* **Pre‑study power** (before data collection) is *theoretical* – it tells you how many subjects you would need to have a high chance of concluding NI *if* the true difference equals the anticipated one.  

* **Post‑hoc power** (computed after seeing the data) is generally **not informative**. It merely reflects the observed p‑value and can be misleading.  

**What you should report instead:**

1. **Observed effect size** (risk difference or RMST difference).  
2. **Exact (or robust) confidence interval** for that effect.  
3. **Sample‑size/precision plot**: show the width of the CI as a function of sample size (or number of events) to illustrate how much data would be needed for a definitive NI claim.  
4. **“Design‑effect” calculations**: e.g., “With 500 patients per arm we would have 80 % power to rule out a 7 % NI margin; our sample of 120 per arm gives 30 % power, so the CI is correspondingly wide.”  

These items convey the *information content* of the data without the false impression that a low post‑hoc power validates the result.

---

### 2.7 Sensitivity analyses for the primary survival endpoint  

Because the study is retrospective, you must test how robust the NI conclusion (or lack thereof) is to modeling choices:

| Sensitivity analysis | Purpose |
|----------------------|---------|
| **Different adjustment methods** (IPTW, propensity‑score matching, doubly‑robust regression) | Assess dependence on the causal‑inference approach. |
| **Vary the NI margin** (5 %, 6 %, 7 %) | Show how the conclusion changes with a clinically plausible range. |
| **Alternative time horizons** (1 yr, 2 yr, 3 yr) | Evaluate whether the NI claim is sensitive to the chosen follow‑up point. |
| **RMST vs risk difference** | Demonstrate that the conclusion holds under a different estimand. |
| **Competing‑risk framework** (if death competes with progression) | Ensure the PFS estimate is not biased by differential mortality. |
| **Unmeasured confounding bias analysis** (e.g., E‑value, Rosenbaum bounds) | Quantify how strong an unmeasured confounder would need to be to overturn the NI conclusion. |
| **Multiple imputation for missing QoL data** | Verify that missingness does not drive the QoL results. |

Report the **point estimate and CI** for each sensitivity scenario in a table; the primary conclusion should be based on the *pre‑specified* analysis, but the sensitivity results provide credibility.

---

### 2.8 Quality‑of‑Life (QoL) analysis  

Assuming the survival NI test fails (CI includes values worse than the margin) but the QoL endpoint shows a **statistically and clinically meaningful improvement**, proceed as follows:

1. **Primary QoL model**: Use a **linear mixed‑effects model (LMM)** or **generalized estimating equations (GEE)** for the repeated QoL scores (baseline and end‑of‑follow‑up). Include treatment, time, and treatment × time interaction, plus covariates used in the survival adjustment (propensity scores, baseline prognostics).  

2. **Estimate the treatment effect** (difference in change from baseline). Provide 95 % CI and a **minimal clinically important difference (MCID)** to contextualize the magnitude.

3. **Pre‑specified subgroup analyses** (e.g., stage, age) are permissible *only if* they were **listed in the analysis plan** before looking at

*Original question: [Rectrospective study hypothesis and sample size](https://stats.stackexchange.com/questions/677314/rectrospective-study-hypothesis-and-sample-size) on Cross Validated (Stats Stack Exchange), licensed CC BY-SA.*

{% endraw %}
