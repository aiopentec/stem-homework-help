---
layout: post
title: "Empirical Bayes (In)Admissibility"
author: StemFix Bot
category: stats
tags: [stats]
---

{% raw %}
*As an Amazon Associate, I earn from qualifying purchases.* For more practice problems like this, see [Schaum's Outline of Statistics, 6th Edition](https://www.amazon.com/dp/1260011461?tag=aiopentec20-20).

---

## 1.  What the question is really asking  

A practitioner wants to use **empirical Bayes (EB)** – i.e. choose a parametric prior, estimate its hyper‑parameters from the data, and then plug those estimates into the usual Bayes rule (posterior mean, posterior median, …).  

For a *pure* Bayes analysis with a **proper** prior we know that the resulting estimator is **admissible** (no other estimator has uniformly smaller risk under the usual quadratic loss).  

The student asks:

* **When does an EB estimator keep this admissibility property?**  
* **What practical checks can we apply, without doing a full‑blown minimax‑theory proof, to be confident that our plug‑in EB rule will not become inadmissible?**  

In other words: give a **step‑by‑step, “cook‑book’’** set of conditions / diagnostics that a practitioner can follow when building a hierarchical model and estimating its hyper‑parameters, so that the final estimator remains admissible (or at least is not obviously inadmissible).

---

## 2.  Full worked answer  

Below we develop the answer in **four layers**  

| Layer | Content | Take‑away |
|------|---------|-----------|
| **A** | General theory – why Bayes → admissible, why EB may break it | Proper priors are safe; plug‑in can destroy propriety |
| **B** | Classic normal‑means example – the “gotcha’’ that shows EB can be inadmissible | The James–Stein estimator (EB‑MLE) is inadmissible; shows what to avoid |
| **C** | Sufficient (and essentially necessary) conditions that guarantee admissibility of an EB rule | Proper hyper‑prior, consistency of the hyper‑parameter estimator, *integrated* (mixed) prior still proper, monotone risk, positive‑part shrinkage, etc. |
| **D** | Practical, step‑by‑step checklist for a practitioner | Concrete actions you can perform before you accept an EB estimator |

---

### A.  Why a *proper* Bayes rule is admissible  

* **Quadratic loss** (the usual setting in Empirical Bayes work).  
* **Theorem (Wald, 1947; Brown, 1971)** – If the prior distribution \(\pi(\theta)\) is **proper** (i.e. integrates to 1) and the Bayes rule \(\delta_\pi\) is the posterior mean (or any Bayes decision rule) under that prior, then \(\delta_\pi\) is **admissible**.  

*Proof sketch* – Suppose another estimator \(\delta'\) had uniformly smaller risk. Then the Bayes risk of \(\delta'\) would be strictly smaller than that of \(\delta_\pi\); but \(\delta_\pi\) minimizes Bayes risk by definition. Contradiction. ∎  

Consequences:

1. **Any fixed proper prior → admissible estimator**.  
2. **If we replace the prior by a data‑dependent “plug‑in’’ prior, we may lose propriety** – the resulting rule is no longer a Bayes rule for a fixed prior, so the theorem does not apply.

---

### B.  A concrete counter‑example: Normal means, marginal‑MLE EB  

#### Model  

*Observations*: \(X_i\mid\theta_i \stackrel{\text{i.i.d.}}{\sim} N(\theta_i,\,\sigma^2)\),   \(i=1,\dots,p\).  
*Goal*: estimate the vector \(\theta=(\theta_1,\dots,\theta_p)\) under total squared error loss  

\[
L(\theta,\delta)=\|\delta-\theta\|^2 .
\]

#### Hierarchical prior (the usual “normal‑means’’ EB set‑up)  

\[
\theta_i \mid \tau \;\sim\; N(0,\tau^2), \qquad \tau>0 .
\]

*If \(\tau\) were known*, the Bayes rule would be the **ridge (shrinkage) estimator**

\[
\delta_{\tau}(X)=\Bigl(1-\frac{\sigma^2}{\sigma^2+\tau^2}\Bigr)X .
\]

Because the prior is proper for every \(\tau>0\), each \(\delta_\tau\) is admissible.

#### Empirical Bayes (plug‑in)  

The most common EB recipe is **marginal maximum‑likelihood** (MMLE) for \(\tau\):

\[
\hat\tau^2_{\text{MMLE}}=\max\Bigl\{0,\; \frac{\|X\|^2-p\sigma^2}{p}\Bigr\}.
\]

Plugging \(\hat\tau\) into \(\delta_{\tau}\) gives

\[
\boxed{\;
\delta_{\text{JS}}(X)=\Bigl(1-\frac{(p-2)\sigma^2}{\|X\|^2}\Bigr)_{+}\,X\;}
\]

(the *positive‑part* James–Stein estimator).  
If we **omit** the “positive‑part’’ and allow the shrinkage factor to become negative we obtain the **classical James–Stein estimator**  

\[
\delta_{\text{JS-raw}}(X)=\Bigl(1-\frac{(p-2)\sigma^2}{\|X\|^2}\Bigr) X .
\]

**What happens?**  

* The raw James–Stein estimator **dominates** the usual estimator \(X\) (so \(X\) is inadmissible for \(p\ge 3\)).  
* However, \(\delta_{\text{JS-raw}}\) is **inadmissible** itself: the *positive‑part* version strictly improves its risk for every \(\theta\).  
* The reason is that the **plug‑in prior** obtained by inserting \(\hat\tau\) into the normal prior is *improper* (its mixing distribution over \(\tau\) puts positive mass at \(\tau=0\) with infinite density). Hence Wald’s theorem no longer guarantees admissibility.

> **Lesson:** *Even in the simplest, textbook EB set‑up, a naïve plug‑in estimator can be inadmissible.*  

---

### C.  Sufficient conditions that **guarantee** admissibility of an EB rule  

The following list collects results that have been proved in the literature (Brown 1971; Strawderman 1974; Berger & Strawderman 2005; Ghosh & Mukherjee 2020, etc.).  They are **sufficient** (and, in many settings, essentially necessary) for admissibility of a plug‑in EB estimator under squared error loss.

| Condition | What it means in practice | Why it matters |
|-----------|---------------------------|----------------|
| **C1. Proper prior family** \(\{\pi_\eta(\theta):\eta\in\mathcal H\}\) with \(\int \pi_\eta(\theta)\,d\theta =1\) for every \(\eta\). | Choose a hierarchical prior that is *proper* for each fixed hyper‑parameter (e.g. normal, t, beta, gamma with strictly positive shape/scale). | Guarantees each fixed‑\(\eta\) Bayes rule is admissible (Wald). |
| **C2. *Uniform* admissibility of the fixed‑\(\eta\) Bayes rule** – i.e. the Bayes rule \(\delta_\eta\) is admissible **for every** \(\eta\in\mathcal H\). | Verify the standard admissibility results (e.g. for normal means any proper normal prior; for Poisson means any proper Gamma prior; for binomial any proper Beta prior). | If any \(\delta_\eta\) were inadmissible, the plug‑in could inherit that problem. |
| **C3. The hyper‑parameter estimator \(\hat\eta\) is *independent* of the part of the data used for the Bayes rule, or at least **asymptotically independent**.** | Split the sample: use a *training* subsample \(\mathcal D_1\) to compute \(\hat\eta\) (e.g. via marginal MLE, method‑of‑moments, cross‑validation) and a *testing* subsample \(\mathcal D_2\) to form the Bayes rule \(\delta_{\hat\eta}(\mathcal D_2)\). | Then the overall estimator is a **two‑stage Bayes rule** for the *mixed* prior \(\int \pi_\eta(\theta) \, \hat\pi(\eta\,|\,\mathcal D_1)d\eta\), which is proper if \(\hat\pi\) is a bona‑fide posterior. |
| **C4. The *mixed* prior \(\tilde\pi(\theta)=\int \pi_\eta(\theta)\,\hat\pi(\eta)\,d\eta\) is proper.** | After estimating \(\hat\eta\) (or after having a posterior \(\hat\pi(\eta)\) from a proper hyper‑prior), integrate out \(\eta\). Verify \(\int \tilde\pi(\theta)d\theta =1\). In practice this holds automatically when: <br>• The hyper‑prior is proper, <br>• The marginal posterior for \(\eta\) is proper (e.g. MCMC draws from a proper posterior). | A proper mixed prior restores Wald’s theorem: the *plug‑in Bayes rule* is the Bayes rule for \(\tilde\pi\), thus admissible. |
| **C5. Consistency (or at least *risk‑consistency*) of \(\hat\eta\).** | As the sample size \(n\to\infty\), \(\hat\eta\overset{P}{\to}\eta_0\) (the true hyper‑parameter) **or** the risk of \(\delta_{\hat\eta}\) converges to the Bayes risk for \(\eta_0\). | If \(\hat\eta\) drifts wildly, the mixed prior may put too much mass on pathological values (e.g. \(\tau=0\) in the normal‑means case) leading to inadmissibility. |
| **C6. Monotone shrinkage factor bounded between 0 and 1** (for normal‑

*Original question: [Empirical Bayes (In)Admissibility](https://stats.stackexchange.com/questions/373869/empirical-bayes-inadmissibility) on Cross Validated (Stats Stack Exchange), licensed CC BY-SA.*
{% endraw %}
