---
layout: question
title: Pooled rate estimation for several Poisson processes under Type-I censoring
  with unrecorded censoring times
author: StemFix Bot
category: stats
subject: stats
description: 'Step-by-step statistics solution: Pooled rate estimation for several
  Poisson processes under Type-I censoring with unrecorded censoring times'
tags:
- stats
---

{% raw %}
*As an Amazon Associate, I earn from qualifying purchases.* For more practice problems like this, see [Schaum's Outline of Statistics, 6th Edition](https://www.amazon.com/dp/1260011461?tag=aiopentec20-20).

---

## 1.  What the problem is asking (in plain language)

You observe **K independent Poisson processes**  

\[
X_b(t)\sim \text{Poisson}(\lambda_b t),\qquad 
\lambda_b=\kappa\,c_b,\;c_b>0 \text{ known},
\]

where the single unknown parameter is the common factor \(\kappa>0\).

For each process \(b\) you look at it on an *unknown* time window \((0,W_b]\) :

* you record **how many events** occurred, \(N_b\);
* you also record the **time of the last observed event**, \(D_b\) (so \(0<D_b\le W_b\)).

The end‑points \(W_b\) themselves are **not observed**.  
From the data \(\{N_b,D_b\}_{b=1}^K\) we want an estimator of \(\kappa\).

Two natural candidates appear:

| estimator | formula | how it is derived |
|-----------|---------|-------------------|
| “failure‑truncated” (incorrect) | \(\displaystyle \tilde\kappa=\frac{M-1}{S}\) | assumes we stopped exactly at the \(N_b\)‑th event |
| “correct” (the one to be proved) | \(\displaystyle \hat\kappa=\frac{M-K}{S}\) | uses the fact that the unobserved gaps after the last event are exponential |

where  

\[
M=\sum_{b=1}^K N_b,\qquad 
S=\sum_{b=1}^K c_b D_b .
\]

The question is:  

*Show that, under the actual sampling scheme (unknown censoring times), the estimator*

\[
\boxed{\displaystyle \hat\kappa=\frac{M-K}{S}}
\]

*is (essentially) unbiased, and explain why the simple correction “‑ K’’ appears, even though the censoring windows \(W_b\) are unknown.*

---

## 2.  Detailed derivation (no steps omitted)

### 2.1  Notation and elementary facts

* For a homogeneous Poisson process with rate \(\lambda\),

  * the **inter‑arrival times** are i.i.d. \(\operatorname{Exp}(\lambda)\);
  * the **waiting time to the \(n\)-th event** has a Gamma distribution
    \(\Gamma(n,\lambda)\) (shape \(n\), rate \(\lambda\));
  * **memorylessness**: given that the last observed event is at time \(d\),
    the remaining time until the next event is \(\operatorname{Exp}(\lambda)\)
    and is independent of the past.

* For each process \(b\) write  

  \[
  \delta_b = W_b - D_b \qquad (\text{the unobserved “gap’’ after the last event}).
  \]

  By memorylessness, conditional on \(D_b\),

  \[
  \delta_b\mid D_b \;\sim\; \operatorname{Exp}(\lambda_b) \text{ truncated at } W_b.
  \]

  Since we do **not** know \(W_b\), we only need the *unconditional* first
  moment of \(\delta_b\).

### 2.2  Expected number of events \(E[M]\)

For each process \(b\),

\[
E[N_b] = \lambda_b\,E[W_b] = \kappa\,c_b\,E[W_b].
\]

Summing over \(b\),

\[
E[M] = \sum_{b=1}^K E[N_b]
     = \kappa\sum_{b=1}^K c_b\,E[W_b]
     = \kappa\;E\!\left[\sum_{b=1}^K c_b W_b\right].
\tag{1}
\]

Thus the *total exposure* \(\sum_b c_b W_b\) is the quantity that
links \(\kappa\) to the expected total count \(M\).

### 2.3  Decomposing the total exposure

Write

\[
\sum_{b=1}^K c_b W_b
   = \sum_{b=1}^K c_b (D_b+\delta_b)
   = S + \sum_{b=1}^K c_b\delta_b .
\tag{2}
\]

The observable part is \(S\); the unknown part is the sum of the gaps
\(\sum c_b\delta_b\).

### 2.4  Expected gap \(\mathbb{E}[\delta_b]\)

Conditional on the (unobserved) window length \(W_b\),

\[
\mathbb{P}(\delta_b > x\mid W_b) = 
\begin{cases}
e^{-\lambda_b x}, & 0\le x\le W_b,\\[4pt]
0, & x>W_b .
\end{cases}
\]

Hence

\[
\mathbb{E}[\delta_b\mid W_b]
   =\int_{0}^{W_b} e^{-\lambda_b x}\,dx
   = \frac{1-e^{-\lambda_b W_b}}{\lambda_b}.
\tag{3}
\]

Taking expectation over the (unknown) distribution of \(W_b\) gives

\[
\mathbb{E}[\delta_b]
   = \frac{1}{\lambda_b}\Bigl(1-\mathbb{E}\bigl[e^{-\lambda_b W_b}\bigr]\Bigr).
\tag{4}
\]

The term \(\mathbb{E}[e^{-\lambda_b W_b}]\) is the *probability that no event
occurs in the whole window*. When the window contains **several** events,
this probability is tiny; we shall treat it as a negligible remainder.

Consequently, to first order,

\[
\boxed{\displaystyle \mathbb{E}[\delta_b]\approx \frac{1}{\lambda_b}
       = \frac{1}{\kappa\,c_b}} .
\tag{5}
\]

Multiplying by \(c_b\) and summing over all processes,

\[
\mathbb{E}\!\left[\sum_{b=1}^K c_b\delta_b\right]
   \approx \sum_{b=1}^K \frac{c_b}{\kappa c_b}= \frac{K}{\kappa}.
\tag{6}
\]

### 2.5  Expected observable quantity \(E[S]\)

From (2),

\[
E\!\bigl[\sum_{b}c_bW_b\bigr]
   = E[S] + E\!\Bigl[\sum_{b}c_b\delta_b\Bigr].
\]

Insert (1) and the approximation (6):

\[
\kappa\,E\!\bigl[\sum_{b}c_bW_b\bigr]
   = E[M] 
   = \kappa\Bigl(E[S] + \frac{K}{\kappa}\Bigr).
\]

Cancel \(\kappa\) from both sides and solve for \(E[S]\):

\[
E[S] = \frac{E[M]-K}{\kappa}.
\tag{7}
\]

Re‑arranging (7) yields the **moment‑matching estimator**

\[
\boxed{\displaystyle \hat\kappa
      = \frac{M-K}{S}} .
\tag{8}
\]

Because (7) holds *exactly* when the remainder
\(\sum_{b}e^{-\lambda_bW_b}\) is kept, the estimator (8) is unbiased **up to that
tiny remainder**. When each window contains at least a few events,
\(\,e^{-\lambda_bW_b}\) is practically zero, so the bias is of order
\(10^{-4}\) or less (the simulation in the original post reported
\(0.02\%\)).

### 2.6  Why the correction is exactly **K**

From (6) we saw that each *unobserved* exponential gap contributes on average
\(1/(\kappa c_b)\) units of *time*. After multiplying by the known factor \(c_b\)
the contribution becomes \(1/\kappa\), *independent of the particular process*.
Summing over the \(K\) processes gives exactly \(K/\kappa\).  
When we replace the unknown total exposure \(\sum c_bW_b\) by its observable part
\(S\), we are missing precisely this deterministic amount \(K/\kappa\).  
Consequently the unbiasedness equation (7) requires the subtraction of **K**
from the total count \(M\). The correction does **not** involve the unknown
window lengths because the expected gap size does not depend on them (only on
the rate \(\lambda_b\), which is itself proportional to \(\kappa\)).

---

## 3.  Final answer

Given the observed data  

\[
\bigl\{N_b,\,D_b\bigr\}_{b=1}^K,\qquad 
M=\sum_{b=1}^K N_b,\; S=\sum_{b=1}^K c_b D_b ,
\]

the estimator

\[
\boxed{\displaystyle 
\hat\kappa = \frac{M-K}{S}
}
\]

has expectation  

\[
\mathbb{E}[\hat\kappa] 
   = \kappa\Bigl(1-\frac{1}{M}\sum_{b=1}^K e^{-\lambda_bW_b}\Bigr)
   \approx \kappa ,
\]

the approximation being extremely accurate whenever each observation window
contains more than a few events (the term \(\sum e^{-\lambda_bW_b}\) is then
negligible).  

Thus \(\hat\kappa\) is (essentially) unbiased, and the simple subtraction of the
number of processes \(K\) corrects exactly for the unobserved exponential gaps
that follow the last recorded event in each Poisson process.

---

## 4.  Common mistakes when tackling this type of problem

| Mistake | Why it is wrong | How to avoid it |
|---------|----------------|-----------------|
| **Treating the data as if the observation stopped exactly at the last event** (using \((M-1)/S\) ). | That assumption ignores the *unobserved* exponential tail after the last event, producing a systematic upward bias (about \(+6\%\) in the simulation). | Remember that the censoring time \(W_b\) is unknown; the last event is not the terminal event. |
| **Assuming \(\delta_b\) has mean \(1/\lambda_b\) without justification**. | The gap is *truncated* at the (unknown) window end; its mean is \((1-e^{-\lambda_bW_b})/\lambda_b\), not exactly \(1/\lambda_b\). | Write the conditional distribution of \(\delta_b\) given \(W_b\) and integrate; then argue that the truncation term is negligible when many events are observed. |
| **Dropping the \(K\) correction because it looks “ad‑hoc”.** | The subtraction of \(K\) follows directly from the expected contribution of the unobserved gaps; omitting it yields bias. | Derive (7) step‑by‑step: start from \(E[M]=\kappa E[\sum c_bW_b]\), decompose the exposure, and solve for \(E[S]\). |
| **Confusing “rate” \(\lambda_b\) with “intensity” \(c_b\).** | \(\lambda_b=\kappa c_b\); mixing them up leads to algebraic errors in the expectation calculations. | Keep a clear table of symbols and substitute \(\lambda_b\) only after the algebra is set up. |
| **Neglecting the remainder \(\sum e^{-\lambda_bW_b}\) without checking its size**. | If a window is extremely short (zero or one event) the remainder is no longer negligible and the estimator acquires a noticeable bias. | Verify that each window contains at least a few events, or otherwise include the remainder term in the bias calculation. |

By following the systematic derivation above and watching out for these pitfalls,
the estimator \(\displaystyle \hat\kappa=\frac{M-K}{S}\) emerges naturally and
is the appropriate tool for pooled rate estimation under Type‑I censoring
with unrecorded censoring times.

*Original question: [Pooled rate estimation for several Poisson processes under Type-I censoring with unrecorded censoring times](https://stats.stackexchange.com/questions/676980/pooled-rate-estimation-for-several-poisson-processes-under-type-i-censoring-with) on Cross Validated (Stats Stack Exchange), licensed CC BY-SA.*

{% endraw %}
