---
layout: question
title: Quantum Gravity signatures high sigma?
author: StemFix Bot
category: physics
subject: physics
description: 'Step-by-step physics solution: Quantum Gravity signatures high sigma?'
tags:
- physics
---

{% raw %}
*As an Amazon Associate, I earn from qualifying purchases.* For more practice problems like this, see [Schaum's Outline of College Physics, 12th Edition](https://www.amazon.com/dp/1259587398?tag=aiopentec20-20).

---

## 1.  What the question is really asking  

The original post is a frustrated rant about **“quantum‑gravity signatures”** and the claim that some experiments have reported a **high‑σ (high‑sigma) detection** of such a signature.  
In plain language the student wants to know:

* **What does “high σ” mean?**  
* **How do you calculate the sigma (σ) significance of a possible quantum‑gravity effect?**  
* **What would be considered a convincing (i.e., statistically robust) result?**

Below is a step‑by‑step guide that shows how a physicist turns raw data into a “σ‑level” statement, illustrated with a generic quantum‑gravity‑type measurement (e.g., a tiny deviation in the speed of light for high‑energy photons, a modification of the dispersion relation, or an unexpected noise feature in a gravitational‑wave interferometer).

---

## 2.  Detailed Worked Solution  

### 2.1  Set up the hypothesis test  

| Symbol | Meaning |
|--------|---------|
| \(H_0\) | **Null hypothesis** – “no quantum‑gravity effect; the data are described entirely by the Standard Model (or classical GR)”. |
| \(H_1\) | **Alternative hypothesis** – “there is a genuine quantum‑gravity signal of magnitude \(S\)”. |
| \(x\)   | Measured quantity (e.g., a time‑delay, a phase shift, a spectral index). |
| \(\mu_0\) | Expected value of \(x\) under \(H_0\). |
| \(\sigma_{\text{tot}}\) | Total (one‑sigma) uncertainty on the measurement, including statistical + systematic contributions. |
| \(\hat S\) | Best‑fit signal strength obtained from the data (difference between the observed value and the null expectation). |

The **goal** is to quantify how far the observed data lie from the null‑hypothesis expectation, measured in units of the total uncertainty. This distance is the **sigma (σ) significance**.

---

### 2.2  Combine all sources of error  

1. **Statistical error** (\(\sigma_{\text{stat}}\)):  
   Comes from the finite number of events, photon counts, etc.  
   Usually obtained from the square‑root of the number of counts or from a fit covariance matrix.

2. **Systematic error** (\(\sigma_{\text{sys}}\)):  
   Calibration, timing offsets, detector alignment, theoretical model uncertainties, etc.

3. **Total error** (assuming the two are independent):  

\[
\sigma_{\text{tot}} = \sqrt{\sigma_{\text{stat}}^{2} + \sigma_{\text{sys}}^{2}} .
\]

*If the systematic uncertainties are correlated, one must build the full covariance matrix and invert it; the simple quadrature formula above is a good first‑order approximation.*

---

### 2.3  Compute the test statistic  

The most common test statistic for a single measured quantity is the **standardised residual** (also called the “z‑score”):

\[
z \;=\; \frac{x - \mu_0}{\sigma_{\text{tot}}}.
\]

*Interpretation*:  

* \(z = 0\) → perfect agreement with the null hypothesis.  
* \(z = +1\) → the measurement is 1‑σ above the null prediction.  
* \(z = -2\) → the measurement is 2‑σ below the null prediction, etc.

When the measurement is a **fit parameter** (e.g., the coefficient of a Lorentz‑invariance‑violating term), the same formula holds, but \(x\) is replaced by the **best‑fit value** \(\hat S\) and \(\mu_0 = 0\) (because under \(H_0\) the signal strength is zero).

\[
z \;=\; \frac{\hat S}{\sigma_{\hat S}} .
\]

---

### 2.4  Convert sigma to a p‑value (optional)  

Physicists often quote the **p‑value** (probability that a fluctuation at least as extreme as observed would occur under \(H_0\)). For a two‑sided Gaussian:

\[
p = 2\,\bigl[1-\Phi(|z|)\bigr],
\]

where \(\Phi\) is the cumulative distribution function of the standard normal distribution.  

Typical benchmarks:

| σ (one‑sided) | Two‑sided p‑value | Common jargon |
|---------------|-------------------|----------------|
| 1 | 0.317 | “not significant” |
| 2 | 0.0455 | “evidence” (≈ 2 σ) |
| 3 | 0.0027 | “strong evidence” |
| 5 | \(5.7\times10^{-7}\) | “discovery” (5 σ) |

In **high‑energy physics and quantum‑gravity searches**, a **5‑σ** result is the community standard for claiming a discovery, because it reduces the chance of a statistical fluke to less than one in a million.

---

### 2.5  Example: Time‑of‑flight delay of high‑energy photons  

Suppose a space‑based gamma‑ray telescope measures the arrival times of two photons from a distant gamma‑ray burst (GRB).  

* **Observed delay**: \(\Delta t_{\text{obs}} = 0.42 \pm 0.12\) ms (stat) \(\pm 0.08\) ms (sys).  
* **Null‑hypothesis prediction**: \(\Delta t_{0}=0\) (no quantum‑gravity dispersion).  

**Step 1 – total error**

\[
\sigma_{\text{tot}} = \sqrt{0.12^{2} + 0.08^{2}} 
                  = \sqrt{0.0144 + 0.0064}
                  = \sqrt{0.0208}
                  \approx 0.144\;\text{ms}.
\]

**Step 2 – sigma significance**

\[
z = \frac{0.42\ \text{ms} - 0}{0.144\ \text{ms}} 
  \approx 2.92 .
\]

**Step 3 – p‑value (two‑sided)**

\[
p = 2\bigl[1-\Phi(2.92)\bigr] 
  \approx 2(1-0.9982) \approx 0.0036 .
\]

**Interpretation**: The observed delay corresponds to a **~3‑σ** effect. It is intriguing, but not yet a discovery; further independent bursts and a careful treatment of possible astrophysical systematics are required.

---

### 2.6  General recipe for any quantum‑gravity search  

| Step | Action |
|------|--------|
| **1** | Write down the *observable* that a quantum‑gravity model predicts (e.g., a modification of the dispersion relation \(E^{2}=p^{2}c^{2}+m^{2}c^{4} + \eta \frac{p^{3}}{M_{\text{Pl}}}\)). |
| **2** | Obtain the *null* expectation (\(\eta=0\)) and the *signal* expectation for a given model parameter. |
| **3** | Collect the data and perform a fit that returns the best‑fit value \(\hat\eta\) and its uncertainty \(\sigma_{\hat\eta}\). |
| **4** | Compute the sigma: \(z = \hat\eta/\sigma_{\hat\eta}\). |
| **5** | If several independent data sets exist, combine them by adding inverse variances (i.e., weighted average) or by constructing a global likelihood. |
| **6** | Quote the resulting σ and, optionally, the corresponding p‑value. |
| **7** | Discuss **look‑elsewhere effect** (multiple tests on different energies, directions, etc.) – correct the σ accordingly. |
| **8** | State whether the result meets the community threshold (≥ 5 σ for a claim of discovery). |

---

## 3.  Final Answer  

**The “high‑σ” statement is simply a way of saying**:  

> *The measured quantity differs from the prediction of ordinary physics by **z** standard deviations, where  

\[
z = \frac{\text{observed – expected}}{\text{total uncertainty}} .
\]

**If \(z \ge 5\)** (≈ \(p < 6\times10^{-7}\)), the physics community would normally call the result a **discovery**; lower values (2–3 σ) are regarded as **hints** that need confirmation.

Thus, to evaluate any claimed quantum‑gravity signature you:

1. **Quantify all sources of error** and combine them into a single \(\sigma_{\text{tot}}\).  
2. **Compute the residual** (observed minus null expectation).  
3. **Divide** the residual by \(\sigma_{\text{tot}}\) to obtain the sigma level.  
4. **Interpret** the sigma using the Gaussian‑tail table (or convert to a p‑value).  

Only after a result consistently reaches the 5‑σ benchmark, survives all systematic checks, and is reproduced by independent experiments, can one claim a genuine quantum‑gravity signal.

---

## 4.  Common Mistakes  

| Mistake | Why it’s wrong | How to avoid it |
|---------|----------------|-----------------|
| **Confusing σ with p‑value** – quoting “3 σ” but interpreting it as a 3 % probability. | σ is a *distance* in units of standard deviations; the associated p‑value is the *probability* of such a fluctuation (≈ 0.27 % for 3 σ, two‑sided). | Always convert σ → p if you need a probability; keep the two concepts distinct. |
| **Neglecting systematic uncertainties** or adding them linearly instead of in quadrature. | Systematics can dominate; linear addition over‑estimates the error, quadrature under‑estimates if correlated. | Build a full covariance matrix; if you must combine them, add in quadrature only when they are independent. |
| **Ignoring the look‑elsewhere effect** (multiple independent tests inflate the chance of a fluke). | Reporting a 4 σ excess found after scanning many energies/directions is less significant than 4 σ in a single pre‑defined test. | Pre‑define the test, or apply a trials‑factor correction to the σ/p‑value. |
| **Using a Gaussian approximation for very low counts** (e.g., < 10 events). | Poisson statistics are not Gaussian in the low‑count regime, leading to biased σ. | Use exact Poisson or likelihood‑ratio methods; only use Gaussian σ when the count > ~ 30. |
| **Double‑counting data** (e.g., treating the same burst’s two photons as independent measurements). | Correlated data artificially reduce σ, making the result appear more significant. | Identify correlations; if data are not independent, treat them as a single measurement or include the correlation in the covariance. |
| **Reporting a one‑sided σ for a two‑sided test** (or vice‑versa). | A 2 σ one‑sided corresponds to a 2.5 % p‑value, not 4.5 % as for a two‑sided test. | State explicitly whether the test is one‑ or two‑sided and use the appropriate conversion. |

By staying vigilant about these pitfalls, you can correctly assess whether a claimed quantum‑gravity signature truly reaches the “high‑σ” (i.e., discovery‑level) threshold.

*Original question: [Quantum Gravity signatures high sigma?](https://physics.stackexchange.com/questions/875602/quantum-gravity-signatures-high-sigma) on Physics Stack Exchange, licensed CC BY-SA.*

{% endraw %}
