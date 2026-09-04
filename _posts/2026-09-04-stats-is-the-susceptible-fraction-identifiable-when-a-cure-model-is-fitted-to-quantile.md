---
layout: question
title: Is the susceptible fraction identifiable when a cure model is fitted to quantiles
  that are conditional on eventual event occurrence?
author: StemFix Bot
category: stats
subject: stats
description: 'Step-by-step statistics solution: Is the susceptible fraction identifiable
  when a cure model is fitted to quantiles that are conditional on eventual event '
tags:
- stats
---

{% raw %}
*As an Amazon Associate, I earn from qualifying purchases.* For more practice problems like this, see [Schaum's Outline of Statistics, 6th Edition](https://www.amazon.com/dp/1260011461?tag=aiopentec20-20).

---

## 1.  What the question is asking (in plain language)

A published paper gives  

* a few **quantiles** (e.g. median, 75‑th percentile) of the *age at first event* **only for those participants who eventually have the event**, and  
* the **cumulative incidence** (proportion that have had the event) measured at the end of follow‑up, which is **≈ 0.65** (i.e. far below 1).

From the published quantiles the student fitted a three‑parameter Weibull distribution  

\[
F_W(t)=1-\exp\!\Bigl[-\Bigl(\frac{t-\theta}{\lambda}\Bigr)^k\Bigr],\qquad t>\theta ,
\]

with estimated shape \(k\), scale \(\lambda\) and threshold \(\theta\).

Because the quantiles are **conditional on eventual occurrence**, \(F_W(t)\) is the distribution of event times **among the “susceptible” (i.e. non‑cured) subjects**.  
If one wants an *unconditional* cumulative‑incidence curve, one must multiply by the (unknown) proportion \(p\) of the cohort that is actually susceptible:

\[
F(t)=p\;F_W(t),\qquad 0\le p\le 1 .
\]

The student asks:

| Question | In statistical terms |
|----------|---------------------|
| **Is \(p\) identifiable?** | Can we uniquely determine the susceptible fraction from the published summary statistics? |
| **Is it legitimate to estimate \(p\) as** \(\displaystyle \hat p=\frac{\widehat{CI}(t^\*)}{\widehat{F}_W(t^\*)}\) **where \(\widehat{CI}(t^\*)\) is the reported cumulative incidence at the end of follow‑up \(t^\*\)?** | Does the fact that the same data were used to fit \(F_W\) create a circularity? |
| **Does the fact that follow‑up ended while some participants were still at risk make the observed 0.65 a lower bound on \(p\)?** | Do we need an extra correction? |
| **How should we propagate uncertainty from the quantiles and the cumulative‑incidence estimate into a confidence interval for \(p\)?** | What method works when we have only published summaries? |

Below is a step‑by‑step worked solution.



## 2.  Detailed solution

### 2.1  Notation and basic relationships  

| Symbol | Meaning |
|--------|----------|
| \(T\) | Age at first event (continuous). |
| \(S\) | Indicator of being “susceptible’’ (i.e. will ever have the event). |
| \(p = P(S=1)\) | Unobserved susceptible fraction (the *cure* parameter). |
| \(F_W(t)=P(T\le t\mid S=1)\) | Weibull CDF fitted to the **conditional** quantiles (distribution of event times among susceptibles). |
| \(F(t)=P(T\le t)=p\,F_W(t)\) | Unconditional cumulative‑incidence (mixture or “cure’’ model). |
| \(\tau\) | Calendar age (or study time) at the end of follow‑up (the only time point for which an unconditional proportion is reported). |
| \(\widehat{CI}=0.65\) | Reported (point) estimate of the unconditional cumulative incidence at \(\tau\). |

Because the published quantiles are **conditional**, they provide information **only about the shape of \(F_W\)**; they contain no information about the mixing proportion \(p\).

The relationship that ties everything together is

\[
\boxed{\; \widehat{CI}=p\,F_W(\tau)\;}
\tag{1}
\]

which is simply the definition of the mixture model evaluated at the single observed time point \(\tau\).

---

### 2.2  Identifiability of the parameters  

*The Weibull parameters* \((k,\lambda,\theta)\) are identified (up to usual regularity conditions) from **any three distinct quantiles** of the conditional distribution. Because the reported quantiles are exact (or reported with negligible rounding error), the three‑parameter Weibull is uniquely determined; no information about \(p\) is needed for this step.

*The cure fraction* \(p\) appears **only** in (1). If we **accept** the Weibull model for \(F_W\) and we have a **single additional piece of information**—the unconditional cumulative incidence at a known time \(\tau\)—then (1) can be solved for \(p\):

\[
\boxed{\; \hat p = \frac{\widehat{CI}}{\widehat{F}_W(\tau)}\;}
\tag{2}
\]

Thus, under the **model‑based assumption** that the Weibull form correctly extrapolates the conditional distribution up to \(\tau\), \(p\) is **identifiable**.  
If we refused to make that modelling assumption, the data alone would not identify \(p\) (any mixture of a different conditional distribution and a different \(p\) could produce the same observed \(\widehat{CI}\)).  

Hence the answer to the first question is:

> **Yes, \(p\) is identifiable *provided* we accept the fitted Weibull as the true conditional distribution**.

---

### 2.3  Is there a circularity?  

No. The quantiles determine \(F_W\) **independently of \(p\)**. Equation (2) uses *different* information (the unconditional proportion) to scale the already‑determined curve. The two data sources are statistically independent under the model:

* The conditional quantiles are functions of the **ordered event times among susceptibles**.  
* The unconditional cumulative incidence is a **binomial count** of all subjects who have experienced the event by time \(\tau\).

Consequently, there is no logical circularity; we are simply combining two complementary pieces of information.

---

### 2.4  What about the fact that follow‑up ended early?  

At the end of follow‑up (\(t=\tau\)) some susceptibles may still be event‑free. By definition

\[
\widehat{CI}=p\,F_W(\tau) \quad\Longrightarrow\quad p = \frac{\widehat{CI}}{F_W(\tau)} .
\]

Because a CDF never exceeds 1, we have  

\[
F_W(\tau) \le 1 \;\;\Longrightarrow\;\; p \ge \widehat{CI}=0.65 .
\]

Thus the observed 0.65 is a **lower bound** on the true susceptible fraction *without any further adjustment*. Equation (2) automatically respects that bound: if the Weibull CDF evaluated at \(\tau\) is < 1, the ratio will be **greater** than 0.65.  

If the model were perfect, the ratio would be the exact \(p\). In practice the ratio can be **greater than 1** only if the Weibull extrapolation is too small (i.e., it under‑estimates the proportion of susceptibles that would have had the event by \(\tau\)). In that case the model is misspecified and the estimate must be discarded or the Weibull re‑fitted with a different functional form.

---

### 2.5  Computing \(\hat p\) with the published numbers  

Assume the follow‑up ended at age \(\tau = 20\) years (the exact value must be taken from the paper; the algebra is the same for any \(\tau\)).  

The fitted Weibull parameters are  

* shape \(k = 1.346\)  
* scale \(\lambda = 12.13\)  
* threshold \(\theta = 8.99\).

For \(\tau > \theta\),

\[
\widehat{F}_W(\tau) = 1-\exp\!\Bigl[-\Bigl(\frac{\tau-\theta}{\lambda}\Bigr)^{k}\Bigr] .
\]

Plugging in the numbers (using \(\tau=20\)):

\[
\frac{\tau-\theta}{\lambda}= \frac{20-8.99}{12.13}=0.907,
\qquad
\bigl(0.907\bigr)^{1.346}=0.857,
\qquad
\exp(-0.857)=0.424,
\]

\[
\widehat{F}_W(20)=1-0.424=0.576 .
\]

Now apply (2):

\[
\hat p = \frac{0.65}{0.576}=1.13 .
\]

Because a probability cannot exceed 1, this result **flags a problem**: either

* the follow‑up time \(\tau\) is larger than 20 years, or  
* the Weibull fit (derived from only three quantiles) is not compatible with the overall incidence, or  
* the reported cumulative incidence has rounding or sampling error that pushes the ratio above 1.

In practice one would repeat the calculation with the correct \(\tau\) (often the maximum observed age) and check that \(\hat p\le 1\). If after correcting for \(\tau\) the estimate is still > 1, the Weibull model should be rejected or a more flexible parametric form (e.g., log‑normal, generalized gamma) should be tried.

---

### 2.6  Propagating uncertainty  

We have **three sources of sampling variability**:

1. **Quantile estimates** – each reported quantile \(q_j\) (e.g., the median) is an estimate of the true conditional quantile \(Q_j\).  
2. **Weibull‑parameter estimation** – the three quantiles are transformed into \((\hat k,\hat\lambda,\hat\theta)\); these estimates have a joint asymptotic normal distribution with covariance matrix \(\Sigma_{\theta}\).  
3. **Overall cumulative incidence** – \(\widehat{CI}\) is a proportion based on \(n\) participants; under a binomial model  

   \[
   \operatorname{Var}(\widehat{CI}) = \frac{CI\,(1-CI)}{n}\; .
   \]

Because \(\hat p\) is a **ratio** of two random quantities, the delta method is possible but, as you suspected,

*Original question: [Is the susceptible fraction identifiable when a cure model is fitted to quantiles that are conditional on eventual event occurrence?](https://stats.stackexchange.com/questions/677070/is-the-susceptible-fraction-identifiable-when-a-cure-model-is-fitted-to-quantile) on Cross Validated (Stats Stack Exchange), licensed CC BY-SA.*

{% endraw %}
