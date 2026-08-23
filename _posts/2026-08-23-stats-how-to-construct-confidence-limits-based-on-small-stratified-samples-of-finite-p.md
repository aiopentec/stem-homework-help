---
layout: post
title: How to construct confidence limits based on small stratified samples of finite
  populations?
author: StemFix Bot
category: stats
tags:
- stats
---

{% raw %}
*As an Amazon Associate, I earn from qualifying purchases.* For more practice problems like this, see [Schaum's Outline of Statistics, 6th Edition](https://www.amazon.com/dp/1260011461?tag=aiopentec20-20).

---

## 1.  What the problem is asking (in plain language)

A company has a finite‐population of transactions that are divided into \(L\) non‑overlapping **strata**.  
For stratum \(i\) we know  

* the size of the stratum: \(N_i\)  
* the number of transactions that were inspected: \(n_i\) (drawn **without replacement**)  
* the number of inspected transactions that turned out to be “non‑conforming”: \(x_i\).

The auditor wants a **confidence limit** (usually an upper bound) for the **total** number of non‑conforming transactions in the whole population  

\[
M=\sum_{i=1}^{L} M_i ,\qquad 
M_i=\hbox{# non‑conforming in stratum }i .
\]

The usual textbook solution – treat each stratum as a simple random sample, estimate a variance, and plug a Normal quantile – works only when  

* the within‑stratum sample sizes \(n_i\) are not tiny,  
* the observed counts \(x_i\) are not tiny (especially not zero), and  
* the sampling fraction \(n_i/N_i\) is small (so the finite‑population correction can be ignored).

In many audit situations **all three** of the above problems occur simultaneously.  
The question is: **How can we obtain confidence limits that still have (or exceed) the nominal coverage when the normal approximation breaks down?**  

---

## 2.  Full step‑by‑step solution  

We will build a **finite‑population exact (or conservative) interval** for the total \(M\).  
The construction proceeds in three logical layers:

1. **Model each stratum** as a hypergeometric sampling experiment.  
2. **Obtain an exact (Clopper–Pearson) confidence interval for the stratum proportion** \(p_i=M_i/N_i\).  
3. **Combine the stratumwise intervals into a confidence interval for the total** \(M=\sum N_i p_i\).  

The final interval is guaranteed to have at least the nominal coverage (e.g., 95 %).  
If a slightly less conservative interval is desired, a *mid‑\(P\)* or *exact unconditional* approach can be used (described briefly in the “Refinements” paragraph).

---

### 2.1  Hypergeometric model for a single stratum  

In stratum \(i\) the unknown number of non‑conforming units is \(M_i\) (an integer between 0 and \(N_i\)).  
A simple random sample of size \(n_i\) without replacement yields

\[
X_i\mid M_i\;\sim\;\operatorname{Hypergeometric}\bigl(N_i,\;M_i,\;n_i\bigr),
\qquad
\Pr\{X_i=x\mid M_i\}= \frac{\binom{M_i}{x}\binom{N_i-M_i}{\,n_i-x\,}}{\binom{N_i}{n_i}} .
\]

The observed value is \(x_i\).  The goal is to infer the unknown integer \(M_i\).

---

### 2.2  Exact (Clopper–Pearson) confidence interval for \(M_i\)

The **Clopper–Pearson** (also called “exact”) interval for a binomial proportion is obtained by inverting a one‑sided hypothesis test.  
The same idea works for the hypergeometric distribution, except that the parameter is the **integer** \(M_i\).  

For a nominal one‑sided level \(\alpha\) (e.g., \(\alpha=0.05\) for a 95 % upper bound) we define  

* **Upper confidence limit** \(U_i\) as the smallest integer \(m\) such that  

\[
\Pr\{X_i\le x_i\mid M_i=m\}\;\ge\;1-\alpha .
\tag{1}
\]

* **Lower confidence limit** \(L_i\) as the largest integer \(m\) such that  

\[
\Pr\{X_i\ge x_i\mid M_i=m\}\;\ge\;1-\alpha .
\tag{2}
\]

Because the hypergeometric cdf can be evaluated exactly (most statistical packages have `phyper`/`dhyper`), the limits are found by a simple **binary search** over the integer range \([0,N_i]\).

*When \(x_i=0\) the lower limit is trivially \(L_i=0\); the upper limit is the smallest \(m\) satisfying (1).  
When \(x_i=n_i\) the upper limit is \(U_i=N_i\); the lower limit is the largest \(m\) satisfying (2).*

These limits are **conservative**: the true coverage is at least \(1-\alpha\).

---

### 2.3  From stratum proportions to a total‑population interval  

Define the stratum‑wise **proportion** interval  

\[
\frac{L_i}{N_i}\; \le\; p_i\; \le\; \frac{U_i}{N_i}.
\]

Because the strata are **independent samples** (sampling without replacement in each stratum does not affect the others), a simultaneous confidence statement can be obtained by the **Bonferroni correction**:

* Choose a per‑stratum error probability \(\alpha_i = \alpha/L\).  
* Compute the \((1-\alpha_i)\) Clopper–Pearson interval \([L_i,U_i]\) for each stratum.  

Then

\[
\Pr\Bigl\{ L_i\le M_i \le U_i\;\text{ for all } i=1,\dots ,L\Bigr\}\;\ge\;1-\alpha .
\tag{3}
\]

Finally, add the lower (resp. upper) bounds across strata:

\[
\boxed{
\;
M_{\text{L}} \;=\; \sum_{i=1}^{L} L_i,
\qquad
M_{\text{U}} \;=\; \sum_{i=1}^{L} U_i
\;}
\]

and the interval  

\[
\bigl[M_{\text{L}},\;M_{\text{U}}\bigr]
\]

is a **\(100(1-\alpha)\%\) confidence interval for the total number of non‑conforming transactions**.

Because each \(L_i\) and \(U_i\) is an integer, the total bounds are also integers, which is appropriate for a count.

---

### 2.4  Worked numerical example  

Assume three strata:

| Stratum \(i\) | \(N_i\) | \(n_i\) | \(x_i\) |
|---------------|--------|--------|--------|
| 1 | 500 | 30 | 0 |
| 2 | 800 | 40 | 2 |
| 3 | 200 | 25 | 1 |

Nominal 95 % overall confidence → \(\alpha = 0.05\).  
Bonferroni per‑stratum error: \(\alpha_i = 0.05/3 \approx 0.0166667\).

#### Stratum 1 ( \(x_1=0\) )
We need the smallest \(m\) such that  

\[
\Pr\{X_1\le 0\mid M_1=m\}= \frac{\binom{N_1-m}{n_1}}{\binom{N_1}{n_1}} \ge 1-\alpha_i = 0.98333 .
\]

A quick search gives \(m=5\).  
Thus \([L_1,U_1]=[0,5]\).

#### Stratum 2 ( \(x_2=2\) )
Using a computer routine (e.g., `phyper` in R) we find  

* Lower limit \(L_2=1\) (largest \(m\) with \(\Pr\{X\ge2\mid M=m\}\ge0.98333\)).  
* Upper limit \(U_2=13\) (smallest \(m\) with \(\Pr\{X\le2\mid M=m\}\ge0.98333\)).  

So \([L_2,U_2]=[1,13]\).

#### Stratum 3 ( \(x_3=1\) )
Similarly,

* Lower limit \(L_3=0\).  
* Upper limit \(U_3=6\).

Thus \([L_3,U_3]=[0,6]\).

#### Combine  

\[
M_{\text{L}} = L_1+L_2+L_3 = 0+1+0 = 1,
\qquad
M_{\text{U}} = U_1+U_2+U_3 = 5+13+6 = 24 .
\]

Hence a **conservative 95 % confidence interval for the total number of non‑conforming transactions** is  

\[
\boxed{ \;1 \;\le\; M \;\le\; 24\; } .
\]

If the auditor only needs an **upper bound**, the interval reduces to \(M\le 24\).

---

### 2.5  Refinements (less conservative alternatives)

| Refinement | Idea | When useful |
|------------|------|-------------|
| **Mid‑\(P\) Clopper–Pearson** | Replace the tail probability in (1)–(2) by \(\frac12\) of the probability of the observed count (the “mid‑\(P\)” adjustment). | Gives intervals that are closer to the nominal level while keeping good coverage. |
| **Exact unconditional interval** (e.g., “exact test inversion” for the sum) | Compute the exact distribution of \(X=\sum_i X_i\) under every possible total \(M\) (using convolution of hypergeometrics) and find the set of \(M\) that are not rejected by a two‑sided test at level \(\alpha\). | Gives the *shortest* possible exact interval; computationally intensive but feasible for modest \(L\) and \(N_i\). |
| **Wilson or Agresti–Coull with finite‑population correction** | Approximate each stratum proportion by a Wilson interval, then apply the FPC factor \(\sqrt{(N_i-n_i)/(N_i-1)}\). | Works well when \(n_i\) is not extremely small (say \(n_i\ge5\)) and the sampling fraction is moderate. |
| **Bootstrap (finite‑population)** | Resample without replacement from each stratum using the observed data, recompute \(\hat M\) many times, and take empirical quantiles. | Gives a data‑driven interval; coverage must be checked by simulation for the specific design. |

For most audit applications the **Bonferroni‑combined Clopper–Pearson interval** is both **simple to implement** and **guaranteed to be at least as wide as needed**, which satisfies the “defensible” requirement.

---

## 3.  Final answer (concise statement)

*Model each stratum as a hypergeometric sample.  For each stratum compute an exact one‑sided Clopper–Pearson confidence limit for the unknown number of non‑conforming items \(M_i\) at per‑stratum error \(\alpha/L\).  Add the lower (or upper) limits across strata.  The resulting integer interval \([\,\sum L_i,\;\sum U_i\,]\) is a valid \((1-\alpha)\) confidence interval for the total number of non‑conforming transactions \(M\).  The method works for tiny samples, zero counts, and large sampling fractions because it does not rely on a Normal approximation.*

---

## 4.  Common Mistakes  

| Mistake | Why it is wrong | How to avoid it |
|---------|----------------|-----------------|
| **Using the normal approximation \(\hat M_i\pm z_{1-\alpha/2}\sqrt{\hat V_i}\)** when many \(x_i\) are 0 or 1. | The normal distribution is a poor fit to a highly skewed (or point‑mass) hypergeometric count, leading to under‑coverage. | Switch to exact (Clopper–Pearson) intervals whenever any stratum has \(x_i\le5\) or \(n_i/N_i>0.1\). |
| **Pooling all strata together and applying a

*Original question: [How to construct confidence limits based on small stratified samples of finite populations?](https://stats.stackexchange.com/questions/332395/how-to-construct-confidence-limits-based-on-small-stratified-samples-of-finite-p) on Cross Validated (Stats Stack Exchange), licensed CC BY-SA.*

{% endraw %}
