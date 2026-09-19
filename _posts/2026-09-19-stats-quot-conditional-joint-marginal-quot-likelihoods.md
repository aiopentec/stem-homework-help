---
layout: question
title: '&quot;Conditional / Joint / Marginal&quot; Likelihoods'
author: StemFix Bot
category: stats
subject: stats
description: 'Step-by-step statistics solution: &quot;Conditional / Joint / Marginal&quot;
  Likelihoods'
tags:
- stats
---

{% raw %}
*As an Amazon Associate, I earn from qualifying purchases.* For more practice problems like this, see [Schaum's Outline of Statistics, 6th Edition](https://www.amazon.com/dp/1260011461?tag=aiopentec20-20).

---

## 1.  What the student is asking (in plain language)

The student has two “likelihood” functions:

| Situation | Data that are observed | Likelihood that is written down |
|-----------|-----------------------|---------------------------------|
| **All pairs** \((x_i ,y_i)\) are observed | \(\{(x_i ,y_i)\}_{i=1}^{n}\) | \(L_{\text{cond}}(\theta)=\displaystyle\prod_{i=1}^{n} p(y_i\mid x_i,\theta)\) |
| **Some \(x\)’s are missing** – we only see \(\{(x_i ,y_i)\}_{i=1}^{n}\) and \(\{y_j\}_{j=1}^{m}\) | \(\{(x_i ,y_i)\}_{i=1}^{n}\) plus “unpaired’’ \(y\)’s | \(L_{\text{joint}}(\theta)=\displaystyle\prod_{i=1}^{n} p(x_i ,y_i\mid\theta)\;\prod_{j=1}^{m} p(y_j\mid\theta)\) |

The questions are:

1. **When is it legitimate to maximise the *conditional* likelihood \(L_{\text{cond}}(\theta)\) instead of the *joint* likelihood \(L_{\text{joint}}(\theta)\)?**  
2. **If we maximise the two different likelihoods, do we obtain different estimators or different asymptotic behaviour (consistency, normality, efficiency)?**

Below we answer these questions step‑by‑step, beginning with the most fundamental definition of a likelihood.

---

## 2.  Likelihood – the basic definition

Let  

* \(\mathbf{Z}=(Z_1,\dots ,Z_N)\) be the **random vector that we actually observe** (the *sample*).  
* \(\theta\in\Theta\) be the **unknown parameter** that governs the distribution of \(\mathbf{Z}\).

The **likelihood function** is simply the probability (or density) of the observed data, regarded as a function of \(\theta\):

\[
L(\theta\mid\mathbf{z})\;=\;p_{\theta}(\mathbf{Z}=\mathbf{z}) .
\]

Everything that follows is just a consequence of this definition:

* If the data are **independent and identically distributed (i.i.d.)**, the likelihood factorises into a product of the individual densities.  
* If part of the data are *latent* (unobserved), the likelihood is the **marginal** of the complete‑data density, i.e. we integrate (or sum) out the missing pieces.

The likelihood is *not* a probability distribution in \(\theta\); it is only a function that we maximise to obtain a point estimate (the **maximum‑likelihood estimator, MLE**).

---

## 3.  Conditional vs. joint likelihood – when each is appropriate

### 3.1  Fixed (non‑random) covariates  

In many regression problems the covariates \(x_i\) are **treated as fixed design points**. In that case the distribution of the data does **not** involve \(\theta\) through the \(x\)’s. Formally

\[
p_{\theta}(x_i,y_i)=p(x_i)\,p_{\theta}(y_i\mid x_i),\qquad p(x_i)\text{ does not depend on }\theta .
\]

Because the factor \(p(x_i)\) is constant with respect to \(\theta\), maximising the **full joint likelihood**  

\[
L_{\text{joint}}(\theta)=\prod_{i=1}^{n}p_{\theta}(x_i,y_i)
\]

is *exactly* the same as maximising the **conditional likelihood**  

\[
L_{\text{cond}}(\theta)=\prod_{i=1}^{n}p_{\theta}(y_i\mid x_i).
\]

Hence, **when covariates are fixed (or their distribution is known and does not contain \(\theta\)), we are free to work with the conditional likelihood**. The resulting MLE is consistent, asymptotically normal, and efficient under the usual regularity conditions.

### 3.2  Random covariates whose distribution involves \(\theta\)

If the covariates themselves are *random* and their distribution depends on \(\theta\) (e.g. a joint model for \((X,Y)\) with a parametric family for \(X\)), then  

\[
p_{\theta}(x_i,y_i)=p_{\theta}(x_i)\,p_{\theta}(y_i\mid x_i)
\]

contains \(\theta\) in the first factor. Dropping that factor (i.e. using the conditional likelihood) would **miss part of the information** and would typically lead to a **misspecified likelihood**. The estimator obtained by maximising only the conditional part would **generally be inconsistent** for the true \(\theta\) unless a special circumstance holds (e.g. the true \(\theta\) only appears in the conditional distribution).

Thus, **when the distribution of the covariates depends on the parameter, you must use the joint likelihood** (or a correctly marginalised version of it).

### 3.3  Missing data – the observed‑data likelihood

Now suppose we have two kinds of observations:

* **Complete cases** \((x_i,y_i), i=1,\dots,n\).  
* **Incomplete cases** where only \(y_j\) is observed, \(j=1,\dots,m\).

Let \(X\) be the random covariate and \(Y\) the response. The **complete‑data** density is \(p_{\theta}(x,y)\). The **observed‑data likelihood** is obtained by **integrating out** the missing covariates:

\[
\begin{aligned}
L_{\text{obs}}(\theta)
&= \prod_{i=1}^{n} p_{\theta}(x_i , y_i)\;
   \prod_{j=1}^{m} \underbrace{\int p_{\theta}(x , y_j)\,dx}_{\displaystyle =\,p_{\theta}(y_j)} .
\end{aligned}
\]

If the covariate distribution does not involve \(\theta\) (fixed design or known distribution), then  

\[
p_{\theta}(y_j)=\int p(y_j\mid x,\theta)\,p(x)\,dx,
\]

which is exactly the term the student wrote as \(p(y_j\mid\theta)\).  

**The EM algorithm is a computational device to maximise this observed‑data likelihood** when the integrals have no closed form. EM works by iteratively replacing the missing \(X\)’s with their conditional expectations given the current parameter guess (the *E‑step*) and then maximising the *complete‑data* log‑likelihood (the *M‑step*).

### 3.4  When can we still use the conditional likelihood with missing data?

If the missingness mechanism is **Missing Completely At Random (MCAR)** **and** the covariate distribution does not involve \(\theta\), then the conditional likelihood based only on the complete cases,

\[
L_{\text{cond,complete}}(\theta)=\prod_{i=1}^{n} p_{\theta}(y_i\mid x_i),
\]

is proportional to the *full* observed‑data likelihood up to a factor that does **not** depend on \(\theta\). Consequently the maximiser is the same.  

If the missingness is **Missing At Random (MAR)** but the distribution of the covariates depends on \(\theta\), the proportionality no longer holds and the conditional likelihood will be misspecified.

---

## 4.  Consequences for the estimator \(\hat\theta\)

| Situation | Likelihood used | Is it the *correct* likelihood? | Consistency? | Asymptotic variance |
|-----------|----------------|--------------------------------|--------------|----------------------|
| Fixed covariates, **all** pairs observed | \(L_{\text{cond}}\) (or \(L_{\text{joint}}\)) | Yes (they are proportional) | Yes, under standard regularity | Achieves the Cramér‑Rao lower bound (efficient) |
| Random covariates, distribution depends on \(\theta\) | \(L_{\text{cond}}\) only | **No** – ignores information in \(p_{\theta}(x)\) | Generally **inconsistent** (biased in the limit) | Larger than the efficient variance |
| Random covariates, distribution independent of \(\theta\) (or design fixed) | Either \(L_{\text{cond}}\) or \(L_{\text{joint}}\) | Yes (proportional) | Yes | Same efficient variance |
| Missing covariates (some \(y\) only) – MCAR or MAR with known missingness mechanism, covariates independent of \(\theta\) | Observed‑data likelihood (the product shown in 3.3) – maximised by EM | Yes | Yes (MLE is consistent) | Efficient (same as if we had observed the missing \(x\)’s) |
| Missing covariates, covariate distribution depends on \(\theta\) | Using only the conditional likelihood on complete cases | **No** (misspecified) | Inconsistent unless extra assumptions hold | Not efficient |

**Key point:** *If the likelihood you maximise is the *true* likelihood of the data you actually observed, the resulting MLE inherits the usual large‑sample properties (consistency, asymptotic normality, efficiency). If you drop a factor that depends on \(\theta\) you are no longer maximizing the true likelihood, and the estimator may be biased and inefficient.*

---

## 5.  Short, formal answer to the original questions

1. **When may we use the conditional likelihood?**  
   - When the covariates are **non‑random (fixed design)** *or* their distribution is known and does **not** involve the parameter \(\theta\).  
   - In the missing‑data setting, this is allowed only if the missingness is MCAR (or MAR with a known mechanism) **and** the covariate distribution does not depend on \(\theta\). In that case the conditional likelihood based on the complete cases is proportional to the full observed‑data likelihood, so both give the same maximiser.

2. **Do the two likelihoods lead to different estimators or asymptotics?**  
   - **If the ignored part of the joint density does not contain \(\theta\)**, the two likelihoods differ only by a multiplicative constant; they have the **same maximiser** and the same asymptotic distribution.  
   - **If the ignored part does contain \(\theta\)** (random covariates, missing data with a \(\theta\)-dependent covariate model, or a missingness mechanism that depends on \(\theta\)), the conditional likelihood is *misspecified*. Maximising it generally yields a **different, inconsistent estimator** with a larger asymptotic variance than the true MLE obtained from the joint (observed‑data) likelihood.

---

## 6.  Common mistakes & how to avoid them

| Mistake | Why it is wrong | How to correct it |
|---------|----------------|-------------------|
| **Treating the covariates as “known constants” while they are actually random and \(\theta\)-dependent.** | Dropping \(p_{\theta}(x)\) removes information, leading to bias. | Write the full joint density first; check whether any factor depends on \(\theta\). |
| **Using the conditional likelihood with missing covariates without accounting for the missing‑data mechanism.** | The observed‑data likelihood is the marginal over the missing part; the conditional likelihood on complete cases is not proportional to it unless MCAR holds. | Explicitly derive the observed‑data likelihood (integrate out the missing \(x\)’s) and maximise that (EM is a convenient algorithm). |
| **Assuming that “more data = higher likelihood” irrespective of what is observed.** | Likelihood is a function of *the data that are actually observed*, not of what could have been observed. | Keep the

*Original question: [&quot;Conditional / Joint / Marginal&quot; Likelihoods](https://stats.stackexchange.com/questions/677213/conditional-joint-marginal-likelihoods) on Cross Validated (Stats Stack Exchange), licensed CC BY-SA.*

{% endraw %}
