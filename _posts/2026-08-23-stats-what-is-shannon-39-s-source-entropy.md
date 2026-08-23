---
layout: post
title: What is Shannon&#39;s source entropy?
author: StemFix Bot
category: stats
tags:
- stats
render_with_liquid: false
---

*As an Amazon Associate, I earn from qualifying purchases.* For more practice problems like this, see [Schaum's Outline of Statistics, 6th Edition](https://www.amazon.com/dp/1260011461?tag=aiopentec20-20).

---

## 1.  What the question is asking (in plain language)

A student has seen two different formulas that are both called **“source entropy”**:

* In a paper on symbolic dynamics the authors write  

\[
H_{\text{source}}=\lim_{k\to\infty}\frac{1}{k}\,H_k ,
\]

  where \(H_k\) is *Shannon’s entropy* of the length‑\(k\) blocks that the source generates.

* In another reference the same term is said to be “the same as Shannon’s entropy”.

The student is unsure:

* What exactly does “source entropy’’ mean?
* Is it the entropy of the input process \(\{X_n\}\), the output process \(\{Y_n\}\), or something else?
* How does the limit‑formula relate to the ordinary Shannon entropy of a single random variable?

Below we answer these questions step‑by‑step.

---

## 2.  Detailed answer (all steps shown)

### 2.1  Basic definitions

1. **Random process (source).**  
   A *discrete‑time* source is a sequence of random variables  
   \[
   \{X_n\}_{n=1}^{\infty},\qquad X_n\in\mathcal A,
   \]
   where \(\mathcal A\) is a *finite* alphabet (e.g. \(\{0,1\}\) or \(\{a,b,c\}\)).  
   The joint law of the whole sequence is denoted \(P_{X_1X_2\ldots}\).

2. **Block of length \(k\).**  
   For any \(k\ge 1\) the random vector  
   \[
   X_1^k:=(X_1,X_2,\dots ,X_k)
   \]
   is called a *block* (or *word*) of length \(k\).

3. **Block (or \(k\)-letter) entropy.**  
   The Shannon entropy of the block is  
   \[
   H_k \;:=\; H(X_1^k)
        \;=\;-\sum_{a_1^k\in\mathcal A^k}
               P\bigl(X_1^k=a_1^k\bigr)\,
               \log_2 P\bigl(X_1^k=a_1^k\bigr).
   \]
   This is just the ordinary Shannon entropy, but applied to the **joint** distribution of \(k\) consecutive symbols.

4. **Entropy rate (source entropy).**  
   The *entropy rate* (also called *Shannon source entropy*) of the source is defined as  
   \[
   H_{\text{source}}
   \;:=\;\lim_{k\to\infty}\frac{1}{k}\,H_k,
   \tag{1}
   \]
   provided the limit exists (it always exists for a stationary ergodic source; see below).

### 2.2  Why the limit is needed

*For a single symbol* the entropy \(H_1\) measures the uncertainty of one draw from the source.  
If the symbols are **independent and identically distributed (i.i.d.)**, then the joint distribution factorises,
\[
P(X_1^k=a_1^k)=\prod_{i=1}^{k}P(X_i=a_i),
\]
and consequently
\[
H_k = k\,H_1 \;\;\Longrightarrow\;\;
\frac{1}{k}H_k = H_1 .
\]
Thus for an i.i.d. source the limit (1) simply returns the ordinary Shannon entropy of one symbol.

*If the symbols are correlated* (e.g. a Markov chain, a chaotic symbolic dynamics, or any source with memory) the block entropy grows **sub‑linearly**:  
\[
H_k = k\,H_{\text{source}} + o(k).
\]
Dividing by \(k\) and taking the limit removes the “redundancy’’ that comes from correlations, leaving the average amount of *new* information per symbol. This is why (1) is called the **entropy rate**.

### 2.3  Existence of the limit

For a **stationary** source (the joint distribution is invariant under time shifts) the sequence \(\{H_k\}\) is **sub‑additive**:
\[
H_{k+\ell} \le H_k + H_\ell .
\]
Fekete’s lemma then guarantees that the limit
\[
\lim_{k\to\infty}\frac{1}{k}H_k = \inf_{k\ge1}\frac{1}{k}H_k
\]
exists (possibly infinite). If the source is also **ergodic**, the limit equals the almost‑sure per‑symbol information rate (the Asymptotic Equipartition Property).

### 2.4  Relation to the input \(X_n\) and the output \(Y_n\)

* **Source entropy** always refers to the *generating source*—the stochastic process that *produces* the symbols. In the notation of the question this is \(\{X_n\}\).  
  The output \(\{Y_n\}\) is obtained after the symbols pass through a channel (which may add noise, quantisation, etc.). The output has its own entropy rate, generally **different** from the source entropy.

* If the paper mentions a *discretisation bin* \(k\), it usually means that a continuous‑valued signal has been **symbolised** by partitioning its range into \(k\) bins. After the discretisation the process is a discrete‑alphabet source, and (1) is applied to the resulting symbolic sequence.

* The formula used by Jun Chen that “is the same as Shannon’s entropy’’ most likely refers to the **special case** of an i.i.d. source, where the entropy rate collapses to the ordinary Shannon entropy of one symbol:
  \[
  H_{\text{source}} = H(X_1) .
  \]

### 2.5  Concrete examples

| Source type | Block probabilities | Block entropy \(H_k\) | Entropy rate \(H_{\text{source}}\) |
|-------------|---------------------|----------------------|------------------------------------|
| **i.i.d. binary** with \(P(X=0)=p\) | \(P(0)^k, P(1)^k\) | \(k\,[-p\log p-(1-p)\log(1-p)]\) | \(-p\log p-(1-p)\log(1-p)\) (single‑symbol entropy) |
| **First‑order Markov** on \(\{0,1\}\) with transition matrix \(T\) | \(P(X_1)T^{k-1}\) | grows ≈ \(k\,H_{\text{rate}}+C\) | \(H_{\text{rate}} = -\sum_{i,j}\pi_i T_{ij}\log T_{ij}\) ( \(\pi\) = stationary distribution ) |
| **Chaotic logistic map** symbolised by a 2‑bin partition | Empirical frequencies of length‑\(k\) words | Computed numerically; typically \(H_k/k\) converges to the **metric entropy** of the map | Same limit = metric (Kolmogorov‑Sinai) entropy, which is the source entropy of the symbolic dynamics |

These examples illustrate that the limit in (1) captures the *average* information per symbol *after* any statistical dependence has been accounted for.

### 2.6  Summary of the answer to the student’s questions

* **What is “source entropy”?**  
  It is the **entropy rate** of the source process \(\{X_n\}\), defined by the limit (1). It measures the average amount of new information generated **per symbol** by the source.

* **Is it the entropy of \(X\) or \(Y\)?**  
  It is the entropy of the **input/source** process \(\{X_n\}\). The output \(\{Y_n\}\) has its own (generally different) entropy rate.

* **Why does the formula look different from ordinary Shannon entropy?**  
  Ordinary Shannon entropy applies to a *single* random variable. The source entropy is the *asymptotic* per‑symbol entropy of a *sequence* of variables; the limit removes any redundancy caused by memory. For memoryless (i.i.d.) sources the two coincide.

---

## 3.  Final answer (clearly stated)

> **Source entropy** (also called **entropy rate**) of a discrete‑alphabet random process \(\{X_n\}\) is  
> \[
> H_{\text{source}}
> \;=\;\lim_{k\to\infty}\frac{1}{k}\,H\!\bigl(X_1,\dots ,X_k\bigr),
> \]
> i.e. the average Shannon information per symbol that the source produces.  
> For an i.i.d. source this limit equals the ordinary Shannon entropy of a single symbol, but for sources with memory it is *smaller* than the single‑symbol entropy because correlations reduce the amount of *new* information per step.  
> The quantity refers to the input process \(\{X_n\}\); the output \(\{Y_n\}\) would have its own (generally different) entropy rate.

---

## 4.  Common mistakes (and how to avoid them)

| Mistake | Why it’s wrong | How to fix it |
|---------|----------------|---------------|
| **Confusing block length \(k\) with the number of discretisation bins.** | In the limit formula \(k\) is the *word length* (how many consecutive symbols are considered), not the resolution of a quantiser. | Keep the two notions separate: “bins’’ → alphabet size; “\(k\)” → block length. |
| **Assuming \(H_{\text{source}} = H_1\) for any source.** | Only true for memoryless (i.i.d.) sources. Correlations make \(H_k < k H_1\). | Compute \(H_k\) for a few values of \(k\); check whether \(H_k/k\) stabilises to a value smaller than \(H_1\). |
| **Neglecting stationarity/ergodicity.** | The limit may fail to exist or may depend on the starting time if the process is non‑stationary. | Verify (or assume) that the source is stationary (probabilities do not change with time). For ergodic sources the limit is guaranteed and equals the AEP constant. |
| **Mixing up source entropy with channel capacity or mutual information.** | Those are *different* information‑theoretic quantities (capacity = max mutual information over input distributions; mutual information = reduction of uncertainty due to the channel). | Remember: **source entropy** = intrinsic randomness of the source; **channel capacity** = max rate at which that randomness can be reliably transmitted. |
| **Using natural logarithms but reporting bits without conversion.** | Entropy units depend on the logarithm base (bits for base‑2, nats for base‑e). | State the base explicitly; if you switch bases, multiply by \(\log_2 e\) (or its inverse). |

By keeping these points in mind, you can correctly interpret and compute the source (entropy‑rate) of any discrete‑alphabet stochastic process.

*Original question: [What is Shannon&#39;s source entropy?](https://stats.stackexchange.com/questions/33361/what-is-shannons-source-entropy) on Cross Validated (Stats Stack Exchange), licensed CC BY-SA.*
