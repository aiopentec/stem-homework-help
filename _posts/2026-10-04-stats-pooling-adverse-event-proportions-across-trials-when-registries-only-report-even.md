---
layout: question
title: 'Pooling adverse-event proportions across trials when registries only report
  events above a threshold: is this estimator and interval defensible?'
author: StemFix Bot
category: stats
subject: stats
description: 'Step-by-step statistics solution: Pooling adverse-event proportions
  across trials when registries only report events above a threshold: is this estimator
  a'
tags:
- stats
---

{% raw %}
*As an Amazon Associate, I earn from qualifying purchases.* For more practice problems like this, see [Schaum's Outline of Statistics, 6th Edition](https://www.amazon.com/dp/1260011461?tag=aiopentec20-20).

---

## 1. What the student is really asking  

The student wants a single “overall” estimate (and a 95 % confidence/credible interval) of how often a particular adverse event (e.g. nausea) occurs for a drug, **across many clinical trials**.  
The data that can be used are the **per‑arm event tables that are posted on ClinicalTrials.gov**.  

Two practical problems make the naïve pooling approach questionable:

| Problem | What it means for the analysis |
|--------|--------------------------------|
| **Reporting threshold** – an arm only reports the event if the *observed* proportion exceeds a trial‑specific cut‑off (≈ 5 %). Arms that have a lower true rate are silently omitted. | The set of observed proportions is **selected**: low‑rate arms are missing, so the naïve mean will be biased upward. |
| **Heterogeneous trials** – arms differ in patient population, drug dose, follow‑up time, and sample size. Very large trials dominate a simple sample‑size weighted mean. | Between‑trial variability (heterogeneity) must be accounted for; otherwise the interval will be too narrow and the point estimate will be driven by a few huge trials. |

The student’s current algorithm is:

1. Compute a proportion for every arm: \(\hat p_{ij}=y_{ij}/n_{ij}\) (events / participants).  
2. Collapse arms **within each trial** by taking the **unweighted mean** of the arm proportions, producing one trial‑level value \(\bar p_i\).  
3. Pool the trial‑level values with **weights proportional to total trial sample size** (optionally down‑weighted by a confidence factor).  
4. Build a 95 % interval on the **log‑odds** scale, adding a heterogeneity variance component, then back‑transform.  

The student asks:

1. Is this weighting + heterogeneity approach reasonable, or should a standard random‑effects meta‑analysis (e.g. a GLMM on the logit scale) be used?  
2. Is it defensible to collapse arms to an **unweighted** within‑trial mean, or should we keep each arm as a separate (clustered) observation?  
3. How can the **reporting threshold** be handled (e.g. left‑censoring at 5 %)?  
4. Given the mixture of populations, should a single pooled estimate be reported or something else?  

Below is a step‑by‑step worked solution that addresses each of these points.

---

## 2. Step‑by‑step solution  

### 2.1 Notation  

| Symbol | Meaning |
|--------|---------|
| \(i = 1,\dots, K\) | trial index |
| \(j = 1,\dots, J_i\) | arm index within trial \(i\) |
| \(n_{ij}\) | number of participants randomised to arm \(j\) of trial \(i\) |
| \(y_{ij}\) | number of participants in that arm who experienced the adverse event |
| \(\hat p_{ij}=y_{ij}/n_{ij}\) | observed proportion (naïve estimate of the true arm‑level probability) |
| \(\theta_{ij}= \operatorname{logit}(p_{ij}) = \log\!\big(p_{ij}/(1-p_{ij})\big)\) | log‑odds for arm \(j\) of trial \(i\) |
| \(\mu\) | overall (average) log‑odds across trials (the quantity we ultimately want) |
| \(\tau^2\) | between‑trial variance on the log‑odds (heterogeneity) |
| \(c_i\) | trial‑specific reporting cutoff (e.g. 0.05). If \(\hat p_{ij}<c_i\) the arm is not reported. |

### 2.2 Why a **random‑effects meta‑analysis of logit‑transformed proportions** is preferable  

| Feature | Simple weighted‑mean + added variance | Random‑effects GLMM (logit) |
|---------|--------------------------------------|-----------------------------|
| Accounts for binomial sampling variability of each arm | Only approximately (via a variance term derived from \(p(1-p)/n\)). | Exact binomial likelihood \(y_{ij}\sim\text{Bin}(n_{ij},p_{ij})\). |
| Handles **different arm sizes** naturally | Weights by \(n_{ij}\); large trials dominate, possibly masking heterogeneity. | Each arm contributes a likelihood term; the model “knows” the \(n_{ij}\). |
| Allows **within‑trial clustering** (multiple arms per trial) | Collapsing arms to a trial‑level mean loses information and imposes an arbitrary unweighted average. | Can include a random effect for trial \(i\) that simultaneously captures all its arms (clustered data). |
| Provides a **principled estimate of \(\tau^2\)** (DerSimonian‑Laird, REML, Bayes…) | Adding an ad‑hoc heterogeneity term is not tied to a likelihood. | \(\tau^2\) is estimated from the same likelihood that fits the data. |
| Gives **correct standard errors** for the pooled estimate | Approximate; may be too narrow if heterogeneity is large. | Exact (or at least asymptotically exact) via the fitted model. |
| Extensible to **censoring** (left‑censoring at 5 %) | No natural way. | Can incorporate a *censored* binomial likelihood (or a Tobit‑type model). |

Hence, for a **descriptive summary** the standard random‑effects meta‑analysis on the logit scale (either a frequentist GLMM with a binomial–normal hierarchy, or a Bayesian hierarchical model) is **clearly better** than the ad‑hoc weighting scheme.

#### 2.2.1 Frequentist formulation  

The model is  

\[
\begin{aligned}
y_{ij}\mid p_{ij} &\sim \text{Binomial}(n_{ij},p_{ij})\\[4pt]
\operatorname{logit}(p_{ij}) &= \mu + u_i , \qquad u_i \sim N(0,\tau^2),
\end{aligned}
\]

where \(u_i\) is a **trial‑level random effect** shared by all arms of trial \(i\).  
The likelihood is the product of binomial terms, and \((\mu,\tau^2)\) are estimated by restricted maximum likelihood (REML) or via the DerSimonian–Laird (DL) moment estimator (the DL estimator is the classic “random‑effects meta‑analysis” but is less efficient for binary data).  

Standard software (R: `lme4::glmer`, `metafor::rma.glmm`, Stata `melogit`, SAS `PROC GLIMMIX`) can fit this model and provide a pooled estimate on the logit scale, its standard error, and a 95 % confidence interval:

\[
\hat\mu \pm 1.96\; \widehat{\operatorname{SE}}(\hat\mu).
\]

Back‑transform to the proportion scale:

\[
\hat p_{\text{overall}} = \operatorname{logit}^{-1}(\hat\mu) = \frac{e^{\hat\mu}}{1+e^{\hat\mu}} .
\]

The interval on the proportion scale is obtained by back‑transforming the logit limits.

#### 2.2.2 Bayesian formulation (optional)  

A Bayesian hierarchical model lets us **propagate uncertainty** about \(\tau^2\) and to incorporate prior knowledge (e.g., that adverse‑event rates are usually low). A minimal model:

\[
\begin{aligned}
y_{ij} &\sim \text{Binomial}(n_{ij},p_{ij})\\
\operatorname{logit}(p_{ij}) &= \mu + u_i\\
u_i &\sim N(0,\tau^2)\\
\mu &\sim N(0,10^2)\\
\tau &\sim \text{Half‑Cauchy}(0,2.5).
\end{aligned}
\]

Posterior draws of \(\mu\) give the pooled log‑odds, which are transformed as above. The 95 % credible interval is simply the 2.5‑th and 97.5‑th percentiles of the transformed draws.

### 2.3 Should arms be **collapsed** to an unweighted within‑trial mean?  

**No –** collapsing arms discards information about the relative sample sizes of the arms and imposes an *equal* weight on each arm regardless of how many participants contributed to it.  

**Better approach:** keep each arm **as a separate observation** but **model the correlation** among arms belonging to the same trial. In the GLMM above the random intercept \(u_i\) does exactly that: it induces a compound‑symmetry correlation among all arms in trial \(i\).  

If one really wishes a single trial‑level estimate (e.g. when only a summary table is available), the **inverse‑variance weighted average of the arm log‑odds** is appropriate:

\[
\hat\theta_i = \frac{\sum_{j=1}^{J_i} w_{ij}\,\hat\theta_{ij}}{\sum_{j=1}^{J_i} w_{ij}},\qquad
w_{ij}= \frac{1}{\widehat{\operatorname{Var}}(\hat\theta_{ij})},
\]

where \(\hat\theta_{ij}=\operatorname{logit}(\hat p_{ij})\) and the variance can be approximated by the delta‑method:

\[
\widehat{\operatorname{Var}}(\hat\theta_{ij}) \approx \frac{1}{y_{ij}}+\frac{1}{n_{ij}-y_{ij}} .
\]

This still respects arm size and yields a trial‑level summary that can be entered into a **second‑stage** random‑effects meta‑analysis. However, the one‑stage GLMM (arm‑level model) is simpler and statistically more efficient.

### 2.4 Handling the **reporting threshold** (left‑censoring)  

When an arm is **not reported** because its observed proportion falls below a known cut‑off \(c_i\) (e.g., 0.05), the data are *censored*:

\[
y_{ij}\;\text{is unknown but we know}\; \frac{y_{ij}}{n_{ij}} < c_i .
\]

There are three practical ways to incorporate this information.

#### 2.4.1 Treat censored arms as **interval‑censored** binomial observations  

For a censored arm we know that the **true count** lies in \(\{0,1,\dots,\lfloor c_i n_{ij}\rfloor\}\). The likelihood contribution is the *cumulative* binomial probability:

\[
L_{ij}^{\text{cens}}(\,p_{ij}\,) = \Pr\!\big(Y_{ij}\le \lfloor c_i n_{ij}\rfloor \mid n_{ij},p_{ij}\big)
= \sum_{y=0}^{\lfloor c_i n_{ij}\rfloor}\binom{n_{ij}}{y} p_{ij}^{y}(1-p_{ij})^{n_{ij}-y}.
\]

In a GLMM framework you can supply this likelihood directly (e.g., `glmmTMB` in R with `family=binomial` and `cens = "left"`). In a Bayesian model you add a `binomial_lcdf` term.

#### 2.4.2 Impute a **conservative bound**  

If full interval‑censoring is too cumbersome, a pragmatic alternative is to **impute** the event count at the threshold (e.g., set \(y_{ij}=c_i n_{ij}\)). This yields a *worst‑case* (largest plausible) estimate for the event rate; the pooled estimate will be **biased upward**, but you can present it together with a **sensitivity analysis** that sets \(y_{ij}=0\) (best‑case) and compares the two extremes.

#### 2.4.3 Explicit **selection model** (advanced)  

One can model the probability that an arm is reported as a function of its (latent) rate, e.g.

\[
\Pr(\text{reported}_{ij}=1 \mid p_{ij}) = \mathbf{1}\{p_{ij}\ge c_i\}.
\]

In a Bayesian framework you jointly model the binomial outcome and the reporting indicator, which yields a *truncated* likelihood. This is statistically rigorous but requires custom Stan or JAGS code and is often overkill for a descriptive summary.

**Recommendation:** Use the interval‑censored likelihood (2.4.1) if the software permits; otherwise perform a **sensitivity analysis** (2.4.2) and be explicit that the pooled proportion is a **lower bound** for the true average event rate because low‑rate arms are missing.

### 2.5 What to report given the **heterogeneous populations**?  

The goal is a *descriptive* cross‑trial summary for a single drug–event pair. Two complementary presentations are advisable:

| Presentation | When to use | How to compute |
|--------------|-------------|----------------|
| **Overall pooled proportion** (single number) | When the audience needs a quick, high‑level view (e.g., a product label). | Fit the one‑stage random‑effects GLMM on all arms (including censored arms if possible). Report \(\hat p_{\text{overall}}\) with its 95 % CI. |
| **Subgroup‑specific pools

*Original question: [Pooling adverse-event proportions across trials when registries only report events above a threshold: is this estimator and interval defensible?](https://stats.stackexchange.com/questions/677339/pooling-adverse-event-proportions-across-trials-when-registries-only-report-even) on Cross Validated (Stats Stack Exchange), licensed CC BY-SA.*

{% endraw %}
