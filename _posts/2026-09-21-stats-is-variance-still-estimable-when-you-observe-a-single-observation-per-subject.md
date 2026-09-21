---
layout: question
title: Is variance still estimable when you observe a single observation per subject?
author: StemFix Bot
category: stats
subject: stats
description: 'Step-by-step statistics solution: Is variance still estimable when you
  observe a single observation per subject?'
tags:
- stats
---

{% raw %}
*As an Amazon Associate, I earn from qualifying purchases.* For more practice problems like this, see [Schaum's Outline of Statistics, 6th Edition](https://www.amazon.com/dp/1260011461?tag=aiopentec20-20).

---

## 1.  What the problem is asking (in plain language)

We have a two‑level (hierarchical) model  

* **Population level** – each subject *i* has its own “true” success probability  

\[
\theta_i\;\stackrel{\text{iid}}{\sim}\; \text{Beta}(\alpha,\beta),\qquad i=1,\dots ,n .
\]

* **Individual level** – we observe binary outcomes  

\[
y_{ij}\mid\theta_i \;\stackrel{\text{iid}}{\sim}\; \text{Bernoulli}(\theta_i),\qquad j=1,\dots ,k .
\]

The researcher only cares about the **population‑level mean**  

\[
\mu = \mathbb{E}[\theta_i]=\frac{\alpha}{\alpha+\beta}
\]

and the **population‑level variance**  

\[
\sigma^2 = \operatorname{Var}(\theta_i)=\frac{\alpha\beta}{(\alpha+\beta)^2(\alpha+\beta+1)} .
\]

Two sampling designs are considered  

| Design | How many observations per subject? |
|--------|-------------------------------------|
| **Case 1** | exactly **one** observation (k = 1) |
| **Case 2** | several observations (k ≥ 2) |

**Question:**  
*Can we estimate \(\mu\) and \(\sigma^2\) from the data in each design?*  
If yes, give a concrete estimator (method‑of‑moments or MLE) and explain why it works; if not, explain why it fails.

---

## 2.  Full solution – step by step

### 2.1  Useful facts about the Beta‑Bernoulli hierarchy  

Because the Bernoulli trials are conditionally independent given \(\theta_i\),

\[
\begin{aligned}
\mathbb{E}[y_{ij}] &= \mathbb{E}_{\theta_i}\big[\,\mathbb{E}[y_{ij}\mid\theta_i]\,\big]
                   = \mathbb{E}[\theta_i] = \mu ,\\[4pt]
\operatorname{Var}(y_{ij}) &= \mathbb{E}\big[\operatorname{Var}(y_{ij}\mid\theta_i)\big]
                         + \operatorname{Var}\big(\mathbb{E}[y_{ij}\mid\theta_i]\big)  \\
                         &= \mathbb{E}[\theta_i(1-\theta_i)] + \operatorname{Var}(\theta_i)  \\
                         &= \mu(1-\mu) + \sigma^2 .
\end{aligned}
\]

Thus the **marginal** distribution of a single observation \(y_{ij}\) is a *Beta‑Bernoulli* (also called a *Bernoulli‑Beta* mixture). Its mean is \(\mu\) and its variance is \(\mu(1-\mu)+\sigma^2\).

If we have **more than one** observation from the same subject we can form the subject‑specific average  

\[
\bar y_i=\frac1k\sum_{j=1}^k y_{ij}.
\]

Conditional on \(\theta_i\), \(\bar y_i\) is the average of \(k\) i.i.d. Bernoulli\((\theta_i)\) variables, so  

\[
\mathbb{E}[\bar y_i\mid\theta_i]=\theta_i,\qquad
\operatorname{Var}(\bar y_i\mid\theta_i)=\frac{\theta_i(1-\theta_i)}{k}.
\]

Unconditionally,

\[
\begin{aligned}
\mathbb{E}[\bar y_i] &= \mu ,\\[4pt]
\operatorname{Var}(\bar y_i) 
    &= \underbrace{\frac{\mu(1-\mu)}{k}}_{\text{within‑subject (sampling) variance}}
       + \underbrace{\sigma^2}_{\text{between‑subject variance}} .
\end{aligned}
\tag{1}
\]

Equation (1) shows that *with several repetitions per subject* the total variance of the subject means splits cleanly into a known part that shrinks as \(k\) grows and an unknown part \(\sigma^2\). This is the key to estimating the population variance.

---

### 2.2  Estimating the mean \(\mu\)

Regardless of the design, the **sample overall proportion** is an unbiased estimator of \(\mu\):

\[
\hat\mu \;=\; \frac{1}{nk}\sum_{i=1}^n\sum_{j=1}^k y_{ij}
            \;=\; \frac{1}{n}\sum_{i=1}^n\bar y_i .
\]

- **Case 1 (k = 1):** this reduces to the usual sample mean of the \(n\) binary outcomes.  
- **Case 2 (k ≥ 2):** the same formula uses all observations, so it is still the MLE and the method‑of‑moments estimator of \(\mu\).

Thus the population mean **can always be estimated**; the estimator’s variance is \(\frac{\mu(1-\mu)}{nk}\).

---

### 2.3  Estimating the variance \(\sigma^2\)

#### 2.3.1  Case 2 (k ≥ 2) – we **can** estimate \(\sigma^2\)

From (1) we have  

\[
\operatorname{Var}(\bar y_i)=\frac{\mu(1-\mu)}{k}+\sigma^2 .
\]

Replace the unknown quantities by their sample analogues:

* Sample variance of the subject means  

\[
S_{\bar y}^2 \;=\; \frac{1}{n-1}\sum_{i=1}^n (\bar y_i-\hat\mu)^2 .
\]

* Plug in \(\hat\mu\) for \(\mu\) in the within‑subject term.

Then a **method‑of‑moments estimator** of the population variance is

\[
\boxed{\;
\hat\sigma^2 \;=\; S_{\bar y}^2 \;-\; \frac{\hat\mu\,(1-\hat\mu)}{k}\;
}
\qquad\text{(if the RHS is negative, set it to 0).}
\]

**Why it works:**  
The sample variance \(S_{\bar y}^2\) estimates \(\operatorname{Var}(\bar y_i)\). Subtracting the known within‑subject contribution \(\mu(1-\mu)/k\) leaves an estimate of the between‑subject component \(\sigma^2\).

**MLE alternative (optional):** The joint likelihood of the data under the Beta–Binomial model is

\[
L(\alpha,\beta)=\prod_{i=1}^n\binom{k}{s_i}\,
   \frac{B(\alpha+s_i,\;\beta+k-s_i)}{B(\alpha,\beta)},
\quad
s_i=\sum_{j=1}^k y_{ij},
\]

where \(B(\cdot,\cdot)\) is the beta function. Maximising this likelihood for \((\alpha,\beta)\) and then converting to \((\mu,\sigma^2)\) via the formulas above gives the same estimators (asymptotically) as the method‑of‑moments version.

#### 2.3.2  Case 1 (k = 1) – we **cannot** estimate \(\sigma^2\)

When \(k=1\) we only observe one Bernoulli draw per subject, i.e. we only have the marginal observations \(y_i\). Their variance is

\[
\operatorname{Var}(y_i)=\mu(1-\mu)+\sigma^2 .
\tag{2}
\]

Both \(\mu\) and \(\sigma^2\) appear **together**; there is no way to separate the “within‑subject” Bernoulli variance \(\mu(1-\mu)\) from the “between‑subject” variance \(\sigma^2\). In fact the mapping

\[
(\mu,\sigma^2)\;\longrightarrow\;\operatorname{Var}(y_i)=\mu(1-\mu)+\sigma^2
\]

is **not injective**: many different pairs \((\mu,\sigma^2)\) produce the same marginal distribution of the data. Consequently the likelihood (or any moment equation) is flat in the direction of \(\sigma^2\); the parameter is **non‑identifiable**.

*What you can estimate:* the **total** variance \(\mu(1-\mu)+\sigma^2\) via the sample variance of the binary outcomes, and the mean \(\mu\) via the sample proportion. But you cannot recover \(\sigma^2\) separately without additional information (e.g., repeated measurements, a prior distribution, or external data).

---

### 2.4  Summary of estimators

| Design | Estimable? | Estimator of \(\mu\) | Estimator of \(\sigma^2\) |
|--------|------------|----------------------|---------------------------|
| **Case 1 (k = 1)** | \(\mu\): **yes**  <br> \(\sigma^2\): **no** (non‑identifiable) | \(\displaystyle \hat\mu = \frac{1}{n}\sum_{i=1}^n y_i\) | – |
| **Case 2 (k ≥ 2)** | both **yes** | same \(\hat\mu\) (using all data) | \(\displaystyle \hat\sigma^2 = S_{\bar y}^2 - \frac{\hat\mu(1-\hat\mu)}{k}\) (method‑of‑moments)  <br> or MLE via beta‑binomial likelihood |

---

## 3.  Final answer

* The **population mean** \(\mu\) can be estimated from *any* design by the overall sample proportion of successes.  
* The **population variance** \(\sigma^2\) can be estimated **only when each subject contributes at least two observations**. With \(k\ge 2\) the method‑of‑moments estimator  

\[
\boxed{\hat\sigma^2 = \frac{1}{n-1}\sum_{i=1}^n (\bar y_i-\hat\mu)^2 \;-\; \frac{\hat\mu(1-\hat\mu)}{k}}
\]

is unbiased (up to the usual small‑sample bias correction) and coincides asymptotically with the MLE.  

* With a single observation per subject (\(k=1\)) the variance component \(\sigma^2\) is **not identifiable**; the data only inform the sum \(\mu(1-\mu)+\sigma^2\). Therefore no estimator of the between‑subject variance exists without further assumptions.

---

## 4.  Common mistakes

| Mistake | Why it’s wrong | How to avoid it |
|---------|----------------|-----------------|
| **Treating the sample variance of the raw \(y_i\) as an estimate of \(\sigma^2\).** | The sample variance mixes within‑subject Bernoulli variability and between‑subject variability (see Eq. 2). | Use the variance of the *subject means* and subtract the known within‑subject term \(\mu(1-\mu)/k\). |
| **Assuming the beta parameters \(\alpha,\beta\) (or equivalently \(\sigma^2

*Original question: [Is variance still estimable when you observe a single observation per subject?](https://stats.stackexchange.com/questions/677226/is-variance-still-estimable-when-you-observe-a-single-observation-per-subject) on Cross Validated (Stats Stack Exchange), licensed CC BY-SA.*

{% endraw %}
