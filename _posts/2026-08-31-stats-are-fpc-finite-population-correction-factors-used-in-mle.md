---
layout: question
title: Are FPC (Finite Population Correction) factors used in MLE?
author: StemFix Bot
category: stats
subject: stats
description: 'Step-by-step statistics solution: Are FPC (Finite Population Correction)
  factors used in MLE?'
tags:
- stats
---

{% raw %}
*As an Amazon Associate, I earn from qualifying purchases.* For more practice problems like this, see [Schaum's Outline of Statistics, 6th Edition](https://www.amazon.com/dp/1260011461?tag=aiopentec20-20).

---

## 1. What the question is asking (in plain language)

We have two situations  

| Situation | Population | How we draw the sample | What we want to estimate |
|-----------|------------|-----------------------|--------------------------|
| **(A) “Infinite” (or with replacement)** | An abstract, unlimited source that generates i.i.d. observations \(X\sim f(x\mid\theta)\). | \(n\) i.i.d. draws, possibly with replacement. | The *model* parameter \(\theta\). |
| **(B) Finite population** | A fixed set of \(N\) values \(\{X_{1},\dots ,X_{N}\}\). | Simple random sampling **without** replacement (SRSWOR) of size \(n\le N\). | Either a *super‑population* parameter \(\theta\) (the distribution that generated the \(N\) values) **or** a finite‑population quantity such as the population mean \(\bar X_{N}\). |

The student wonders whether, when we work with situation (B), we have to insert the *finite‑population correction* (FPC) factor \((1-n/N)\) somewhere in the maximum‑likelihood‑estimation (MLE) machinery:

* in the likelihood itself?
* in the Fisher‑information expression \(I(\theta)\)?
* in the usual large‑sample variance formula \(\operatorname{Var}(\hat\theta)\approx [\,n I(\theta)\,]^{-1}\)?

---

## 2. Step‑by‑step answer  

### 2.1 Likelihood under SRSWOR  

Suppose the \(N\) units are a *realisation* of a super‑population model  

\[
X_{k}\stackrel{\text{i.i.d.}}{\sim} f(x\mid\theta),\qquad k=1,\dots ,N .
\]

We then draw a *simple random sample without replacement* (SRSWOR) of size \(n\).  
Let the observed sample be \(\mathbf{x}=(x_{1},\dots ,x_{n})\) and let \(\mathbf{x}^{c}\) denote the (unobserved) complement of size \(N-n\).

The probability (or density) of seeing **that particular unordered set** \(\{x_{1},\dots ,x_{n}\}\) is  

\[
L_{\text{SRSWOR}}(\theta\mid\mathbf{x})
   =\frac{\displaystyle 
          \binom{N}{n}^{-1}
          \prod_{i=1}^{N} f(x_{i}\mid\theta)}
         {\displaystyle\prod_{i=1}^{N-n} \int f(y\mid\theta)\,dy},
\]

but a much cleaner way is to write the joint density **conditional on the whole population** and then *integrate out* the unobserved units.  

Because the sampling scheme is *ignorable* (it does not depend on \(\theta\)), the likelihood can be expressed as the product of the individual densities **up to a constant that does not involve \(\theta\)**:

\[
\begin{aligned}
L_{\text{SRSWOR}}(\theta\mid\mathbf{x})
   &=\Pr\bigl(\text{draw }\mathbf{x}\mid\theta\bigr) \\
   &=\frac{\displaystyle\prod_{i=1}^{n} f(x_{i}\mid\theta)}
          {\displaystyle\binom{N}{n}}  \times\; C(\theta) ,
\end{aligned}
\]

where  

\[
C(\theta)=\int\!\!\cdots\!\!\int \prod_{j=n+1}^{N} f(y_{j}\mid\theta)\,dy_{j}
\]

does **not** depend on the observed \(\mathbf{x}\) (it only involves the \(N-n\) unsampled units).  

Hence the *log‑likelihood* that matters for inference is

\[
\ell(\theta\mid\mathbf{x})
   =\sum_{i=1}^{n}\log f(x_{i}\mid\theta) \;+\; \underbrace{\text{constant w.r.t. }\theta}_{\text{ignored}} .
\]

**Conclusion 1** – *the likelihood function for SRSWOR is exactly the same as for i.i.d. sampling, apart from a \(\theta\)‑free constant.*  
Therefore the *MLE* of \(\theta\) is **identical** to the infinite‑population (with‑replacement) case:

\[
\boxed{\ \hat\theta_{\text{MLE}} = \arg\max_{\theta}\ \sum_{i=1}^{n}\log f(x_{i}\mid\theta)\ } .
\]

No FPC appears in the likelihood or in the maximisation step.

---

### 2.2 Fisher information for a sample drawn without replacement  

The (expected) Fisher information per observation is still  

\[
I(\theta) = -\,\mathbb{E}\!\left[\frac{\partial^{2}}{\partial\theta\partial\theta^{\!\top}}
                              \log f(X\mid\theta)\right].
\]

Because the log‑likelihood for the sample is a *sum* of the individual log‑densities, the information contributed by the *whole sample* is  

\[
\mathcal{I}_{n}(\theta) = n\,I(\theta).
\]

The factor \(n\) counts the **number of sampled units**, not the population size.  
Again, the FPC does **not** enter the information matrix itself.

---

### 2.3 Asymptotic variance of the MLE under SRSWOR  

For an MLE \(\hat\theta\) we usually invoke the classic result

\[
\sqrt{n}\,\bigl(\hat\theta-\theta\bigr) \;\xrightarrow{d}\; N\bigl(0,\; I(\theta)^{-1}\bigr),
\]

which yields the large‑sample variance approximation  

\[
\operatorname{Var}(\hat\theta) \approx \bigl[n I(\theta)\bigr]^{-1}.
\]

That result is derived **under the model** (i.e. treating the sample as i.i.d.).  
When the sampling fraction \(f=n/N\) is not negligible, the *design* (SRSWOR) adds a finite‑population correction to the *sampling distribution* of many statistics, **including the MLE**.  

A convenient way to see the correction is to apply a *central limit theorem for sampling without replacement* (the “finite‑population CLT”):

\[
\sqrt{n}\,(\bar X_{n}-\bar X_{N}) \;\xrightarrow{d}\;
N\!\left(0,\;(1-f)\,\sigma^{2}\right),
\]

where \(\sigma^{2}=\operatorname{Var}(X_{k})\) under the super‑population model.

If the MLE is a *smooth function* \(g\) of the sample mean (as it is for the normal mean, the Bernoulli proportion, etc.), the *delta method* shows that its asymptotic variance inherits the same multiplicative factor \((1-f)\).  
In symbols,

\[
\boxed{\;
\operatorname{Var}(\hat\theta_{\text{MLE}})\ \approx\ (1-f)\,\bigl[n I(\theta)\bigr]^{-1},
\qquad f=\frac{n}{N}.
\;}
\]

Thus the FPC **does appear** in the *variance* of the estimator, *not* in the likelihood or the information matrix.

---

### 2.4 What if the target is a **finite‑population quantity** (e.g. \(\bar X_{N}\))?  

A finite‑population quantity is **not a parameter of the super‑population model**; there is no likelihood for it in the usual sense.  
The usual estimator is the *sample mean* \(\bar X_{n}\). Its design‑based variance is

\[
\operatorname{Var}_{\text{design}}(\bar X_{n})
   = \frac{1-f}{n}\,\sigma^{2},
\]

which is exactly the familiar FPC factor.  
Because there is no likelihood for \(\bar X_{N}\), the question of “using an FPC in the MLE” does not arise.

---

## 3. Final answer  

| Target of inference | Does the **likelihood** need an FPC? | Does the **Fisher information** need an FPC? | Does the **variance formula** for the MLE need an FPC? |
|---------------------|--------------------------------------|---------------------------------------------|--------------------------------------------------------|
| **Super‑population parameter \(\theta\)** (e.g., mean, variance, regression coefficients) | **No** – the likelihood for a simple random sample without replacement is the same product \(\prod_{i=1}^{n} f(x_i\mid\theta)\) up to a \(\theta\)-free constant. | **No** – the total information is \(n I(\theta)\). | **Yes**, when the sampling fraction \(f=n/N\) is non‑negligible. The asymptotic variance becomes \((1-f)[\,n I(\theta)\,]^{-1}\). |
| **Finite‑population quantity (e.g., \(\bar X_{N}\))** | Not applicable – there is no likelihood for a fixed finite‑population parameter. | Not applicable. | **Yes** – the design‑based variance of the sample mean (or any unbiased estimator) contains the factor \((1-f)\). |

In short: **the FPC does not modify the MLE itself, but it does appear in the large‑sample variance of the estimator whenever the sampling fraction is not negligible.** For a purely model‑based (“super‑population”) analysis, you can continue to maximise the ordinary i.i.d. log‑likelihood; just remember to multiply the resulting variance by \((1-n/N)\) if you want a design‑consistent standard error.

---

## 4. Common mistakes  

| Mistake | Why it’s wrong | How to avoid it |
|---------|----------------|-----------------|
| **Adding the factor \((1-n/N)\) inside the log‑likelihood** | The sampling design is *ignorable* for the likelihood; the factor is a constant w.r.t. \(\theta\) and does not affect the maximisation. | Write the likelihood, then explicitly drop any term that does not involve \(\theta\). |
| **Using the usual variance formula \([nI(\theta)]^{-1}\) even when \(n/N\) is large** | The CLT for sampling **without** replacement includes the factor \((1-f)\). Ignoring it underestimates the standard error. | After obtaining the MLE, compute the variance as \((1-f)[nI(\theta)]^{-1}\) when the sampling fraction exceeds, say, 5 %. |
| **Treating the population mean \(\bar X_{N}\) as a model parameter and trying to write a likelihood for it** | \(\bar X_{N}\) is a deterministic function of the finite data set, not a stochastic parameter; no likelihood exists. | Dist

*Original question: [Are FPC (Finite Population Correction) factors used in MLE?](https://stats.stackexchange.com/questions/677025/are-fpc-finite-population-correction-factors-used-in-mle) on Cross Validated (Stats Stack Exchange), licensed CC BY-SA.*

{% endraw %}
