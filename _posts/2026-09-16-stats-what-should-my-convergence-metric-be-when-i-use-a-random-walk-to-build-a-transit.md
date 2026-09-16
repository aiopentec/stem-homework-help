---
layout: question
title: What should my convergence metric be when I use a Random Walk to build a transition
  probability matrix?
author: StemFix Bot
category: stats
subject: stats
description: 'Step-by-step statistics solution: What should my convergence metric
  be when I use a Random Walk to build a transition probability matrix?'
tags:
- stats
---

{% raw %}
*As an Amazon Associate, I earn from qualifying purchases.* For more practice problems like this, see [Schaum's Outline of Statistics, 6th Edition](https://www.amazon.com/dp/1260011461?tag=aiopentec20-20).

---

## 1.  Restating the question in plain language  

You are simulating a **discrete‑time Markov chain** (a random walk on a finite set of integer states).  
At each step you record how many times you moved from state *i* to state *j*.  
After many steps you  

1. **Normalize** those counts to obtain an *empirical transition matrix* \(\widehat P\).  
2. Compute the *stationary distribution* \(\widehat\pi\) of \(\widehat P\).  
3. Use a scalar summary of \(\widehat\pi\) (its expected value) as a prediction.

You need a **stopping rule**: after how many simulated steps should you stop because the quantities you care about have “stabilised”?  

You suggested three possible criteria  

| Criterion | What is compared | How the comparison is performed |
|-----------|------------------|---------------------------------|
| (A) Expected value of the stationary distribution | \(\mathbb{E}_{\widehat\pi}[X]\) at two successive checkpoints | \(|\mathbb{E}_{\widehat\pi^{(k)}}[X]-\mathbb{E}_{\widehat\pi^{(k-1)}}[X]|<\varepsilon\) |
| (B) Whole stationary distribution | \(\widehat\pi^{(k)}\) vs. \(\widehat\pi^{(k-1)}\) | \(\|\widehat\pi^{(k)}-\widehat\pi^{(k-1)}\|<\varepsilon\) (any vector norm) |
| (C) Whole transition matrix | \(\widehat P^{(k)}\) vs. \(\widehat P^{(k-1)}\) | \(\|\widehat P^{(k)}-\widehat P^{(k-1)}\|_{\max}<\varepsilon\) (or any matrix norm) |

Which of these (or something else) is the *right* metric for deciding when the simulation has converged?

---

## 2.  Step‑by‑step reasoning  

### 2.1  What is converging, and why does it matter?  

For a **fixed, irreducible and aperiodic** Markov chain the following limits hold (law of large numbers for Markov chains):

| Quantity | Empirical estimator | Limit (as the number of steps \(N\to\infty\)) |
|----------|--------------------|-----------------------------------------------|
| Transition probabilities \(P_{ij}\) | \(\displaystyle \widehat P_{ij}^{(N)}=\frac{\#\{X_t=i,\;X_{t+1}=j\}}{\#\{X_t=i\}}\) | True matrix element \(P_{ij}\) |
| Stationary distribution \(\pi\) | \(\displaystyle \widehat\pi_i^{(N)}=\frac{\#\{X_t=i\}}{N}\) (or the eigenvector of \(\widehat P^{(N)}\)) | Unique stationary vector \(\pi\) |
| Expected value of the stationary distribution | \(\displaystyle \widehat\mu^{(N)}=\sum_i i\,\widehat\pi_i^{(N)}\) | \(\displaystyle \mu=\sum_i i\,\pi_i\) |

All three converge **almost surely** as the walk gets longer, but they do so at *different speeds* and with *different variability*.

* The transition matrix entries are **directly** estimated from *pairwise* counts, which have variance of order \(1/N_i\) where \(N_i\) is the number of visits to state \(i\).  
* The stationary distribution is estimated from *single‑state* counts; its variance is of order \(1/N\).  
* The expected value is a **linear combination** of the stationary probabilities, so its variance is a weighted sum of the variances of the \(\widehat\pi_i\).  

Consequently, monitoring the **most “primitive”** object (the transition matrix) gives you the strongest guarantee: if the matrix is close enough to its limit, then everything derived from it (the stationary distribution and any function of it) must also be close.

### 2.2  Choosing a norm / distance  

Because we are dealing with probabilities, the natural distances are  

* **Maximum (sup‑norm) distance**  
  \[
  d_{\max}(\widehat P^{(k)},\widehat P^{(k-1)}) = \max_{i,j}\bigl| \widehat P^{(k)}_{ij}-\widehat P^{(k-1)}_{ij}\bigr|
  \]
* **\(L_1\) (total‑variation) distance** for matrices or vectors  
  \[
  d_{1}(\widehat P^{(k)},\widehat P^{(k-1)}) = \frac12\sum_{i,j}\bigl| \widehat P^{(k)}_{ij}-\widehat P^{(k-1)}_{ij}\bigr|
  \]
* **\(L_2\) (Euclidean) distance** – less interpretable for probabilities but mathematically convenient.

For a *vector* \(\pi\) you can use the same norms (the total‑variation distance for probability vectors is simply \(\frac12\sum_i|\pi_i-\pi'_i|\)).

### 2.3  Theoretical stopping rule  

A mathematically sound stopping rule is  

> **Stop the simulation at the first checkpoint \(k\) such that**  
> \[
> d(\widehat P^{(k)},\widehat P^{(k-1)}) < \varepsilon ,
> \]
> **where** \(d\) **is a chosen norm (commonly the maximum norm)** **and** \(\varepsilon\) **is a small tolerance (e.g., \(5\times10^{-3}\)).**

Why?  

1. **Uniform guarantee** – if every entry of \(\widehat P\) changes less than \(\varepsilon\), then any *continuous* function of the matrix (including the stationary distribution and any linear functional such as the expected value) changes by at most a constant times \(\varepsilon\).  
2. **Statistical control** – the bound translates into a *confidence interval* for the true matrix entries via Hoeffding or Bernstein inequalities because each entry is a sample proportion.

### 2.4  Practical considerations  

| Issue | How it affects the choice of metric |
|-------|-------------------------------------|
| **State space size** | Large \(S\) → many matrix entries; checking every entry may be expensive. Use a *subset* (e.g., the most‑frequent rows) or an *aggregate norm* like the total‑variation. |
| **Sparse visitation** | Some states are visited rarely, so their row estimates have high variance. You may ignore rows with fewer than a preset number of visits, or weight the norm by the number of visits \(N_i\). |
| **Desired output** | If you only need the expected value, you could monitor \(\widehat\mu\) *and* verify that the matrix has stabilised enough for the variance to be negligible. But this is riskier because a small change in a rarely‑visited transition can dramatically affect the stationary distribution without noticeably moving the mean. |
| **Computational cost** | Computing the stationary distribution each checkpoint (by power iteration or eigen‑decomposition) is \(O(|S|^3)\) for dense chains. Checking the matrix directly is \(O(|S|^2)\). For very large chains the matrix check is cheaper. |

### 2.5  Recommended workflow  

1. **Choose a checkpoint interval** (e.g., every 10 000 steps).  
2. **Update the count matrix** \(C\) and the row‑wise visit counts \(N_i\).  
3. **Form the empirical transition matrix**  
   \[
   \widehat P_{ij}= \frac{C_{ij}}{N_i}\quad\text{if }N_i>0,\;\;0\text{ otherwise.}
   \]
4. **Compute the distance** \(d\) between the current \(\widehat P\) and the previous one.  
5. If \(d<\varepsilon\) **and** the *minimum* row count exceeds a safety threshold (e.g., \(N_i\ge 30\) for all \(i\)), **stop**.  
6. Otherwise continue the walk.  
7. After stopping, compute the stationary distribution (by power method on \(\widehat P\) or by normalising the empirical state‑frequency vector) and any downstream quantities (expected value, etc.).

---

## 3.  Final answer  

**The most statistically sound convergence metric is the distance between successive *transition probability matrices* (criterion C).**  

*If the whole matrix has changed by less than a pre‑specified tolerance (using a maximum‑norm or total‑variation norm), then every derived quantity—including the stationary distribution and its expected value—must also be within a comparable tolerance.*  

Monitoring only the expected value (criterion A) can give a false sense of convergence because different transition matrices can share the same mean. Monitoring the stationary distribution (criterion B) is better, but it is still a *function* of the matrix; the matrix check is the strongest and cheapest guarantee.

---

## 4.  Common mistakes  

| Mistake | Why it’s a problem | How to avoid it |
|---------|-------------------|-----------------|
| **Stopping on the expected value alone** | Two very different stationary distributions can have the same mean, so the underlying model may still be inaccurate. | Always check a more fundamental object (the transition matrix) in addition to any scalar summary. |
| **Using a too‑large tolerance** | A lax \(\varepsilon\) yields a matrix that is still far from the true one, leading to biased predictions. | Choose \(\varepsilon\) based on the desired confidence level (e.g., use Hoeffding bounds to relate \(\varepsilon\) to a probability of error). |
| **Ignoring rows with few visits** | Rarely visited states have noisy estimates; they can dominate the max‑norm distance and cause premature termination. | Impose a minimum visit count per row before including its entries in the distance calculation, or weight the norm by \(N_i\). |
| **Recomputing the stationary distribution at every checkpoint** | For large state spaces this is computationally heavy and unnecessary for the convergence test. | Compute \(\widehat\pi\) only after the matrix has met the convergence criterion, or use a cheap power‑iteration estimate if you need an interim check. |
| **Assuming independence of successive steps** | The Markov chain samples are dependent, so naïve standard‑error formulas (treating them as i.i.d.) underestimate variability. | Use Markov‑chain specific concentration inequalities (e.g., Hoeffding for ergodic chains) or batch‑means to estimate variability. |

By following the matrix‑based stopping rule and being aware of these pitfalls, you obtain a reliable estimate of the transition probabilities, the stationary distribution, and any downstream predictions derived from them.

*Original question: [What should my convergence metric be when I use a Random Walk to build a transition probability matrix?](https://stats.stackexchange.com/questions/677146/what-should-my-convergence-metric-be-when-i-use-a-random-walk-to-build-a-transit) on Cross Validated (Stats Stack Exchange), licensed CC BY-SA.*

{% endraw %}
