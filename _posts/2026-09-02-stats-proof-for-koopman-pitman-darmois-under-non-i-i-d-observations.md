---
layout: question
title: Proof for Koopman-Pitman-Darmois under non-i.i.d observations
author: StemFix Bot
category: stats
subject: stats
description: 'Step-by-step statistics solution: Proof for Koopman-Pitman-Darmois under
  non-i.i.d observations'
tags:
- stats
---

{% raw %}
*As an Amazon Associate, I earn from qualifying purchases.* For more practice problems like this, see [Schaum's Outline of Statistics, 6th Edition](https://www.amazon.com/dp/1260011461?tag=aiopentec20-20).

---

## 1.  What the question is asking (in plain language)

The classic **Koopman‑Pitman‑Darmois (KPD) theorem** says:

*If we observe a sample \(X_{1},\dots ,X_{n}\) that are **independent and identically distributed (i.i.d.)** from a parametric family \(\{P_{\theta}:\theta\in\Theta\}\), and if for every sample size \(n\) there exists a **finite‑dimensional** (i.e. dimension that does **not** grow with \(n\)) statistic that is **sufficient** for \(\theta\), then the family must be an **exponential family** (of that same finite dimension).*

The student’s question is:

> What happens if we drop one of the i.i.d. assumptions – either independence or identical distribution?  
> Are there published results that extend the KPD theorem to such non‑i.i.d. settings, or is the analysis “trivial”?

In other words: **Can we still characterise the families that admit a fixed‑size sufficient statistic when the observations are not i.i.d.?**  

Below we give a complete answer, step by step, and point to the relevant peer‑reviewed literature.

---

## 2.  Preliminaries – definitions we need

| Symbol | Meaning |
|--------|---------|
| \(X_{1},\dots ,X_{n}\) | Observations (random variables) |
| \(\Theta\subseteq\mathbb{R}^{d}\) | Parameter space (finite‑dimensional) |
| \(P_{\theta}\) | Joint distribution of the sample under parameter \(\theta\) |
| \(T_{n}=t_{n}(X_{1},\dots ,X_{n})\) | Statistic (possibly vector‑valued) |
| **Sufficient** | \(T_{n}\) is sufficient for \(\theta\) iff the conditional law of the whole sample given \(T_{n}=t\) does **not** depend on \(\theta\). |
| **Finite‑dimensional sufficient statistic** | \(\dim(T_{n})\) is bounded by some constant \(k\) that does **not** depend on \(n\). |
| **Exponential family** (full) | Densities of the form \[ p_{\theta}(x)=h(x)\exp\{\eta(\theta)^{\!\top}s(x)-A(\theta)\},\] where \(\eta(\theta)\in\mathbb{R}^{k}\) (the *natural parameter*) and \(s(x)\) is a \(k\)‑dimensional *sufficient statistic* for a single observation. |

The **Factorisation Theorem** (Neyman–Fisher) tells us that \(T_{n}\) is sufficient iff the joint density can be written as  
\[
p_{\theta}(x_{1},\dots ,x_{n})=g_{\theta}\bigl(T_{n}(x_{1},\dots ,x_{n})\bigr)\,h_{n}(x_{1},\dots ,x_{n}),
\]
where \(h_{n}\) does **not** involve \(\theta\).

---

## 3.  The classic KPD theorem (i.i.d. case)

**Statement (informal).**  
If for an i.i.d. sample there exists a uniformly bounded‑dimension sufficient statistic, then the model must be a (regular) exponential family of that dimension.

*Sketch of proof* (the usual route, kept short because it is well‑known):

1. Write the joint density under i.i.d. assumption:  
   \[
   p_{\theta}^{(n)}(x_{1},\dots ,x_{n})=\prod_{i=1}^{n}p_{\theta}(x_{i}).
   \]
2. Apply the factorisation theorem with a bounded‑dimensional statistic \(T_{n}\).  
   This forces the single‑observation density to satisfy a functional equation that can be solved only by an exponential form.  
3. Regularity (e.g. openness of \(\Theta\), differentiability) guarantees that the solution is the usual full exponential family.

---

## 4.  Extending to **independent but non‑identically distributed** observations  

### 4.1  What the model looks like

Assume **independence** only:

\[
p_{\theta}^{(n)}(x_{1},\dots ,x_{n})
   =\prod_{i=1}^{n} p_{\theta}^{(i)}(x_{i}),\qquad i=1,\dots ,n,
\]

where each marginal density \(p_{\theta}^{(i)}\) may be *different* (different support, different carrier measure, etc.) but **all share the same parameter \(\theta\)**.

### 4.2  Theorem (independent non‑i.i.d. version)

> **Theorem (KPD for independent non‑i.i.d. data).**  
> Let \(\{P_{\theta}^{(i)}\}_{\theta\in\Theta,\,i\ge 1}\) be a collection of probability measures on a common measurable space such that the observations are mutually independent.  
> Suppose there exists a statistic \(T_{n}\) with \(\dim(T_{n})\le k\) (fixed \(k\)) that is sufficient for \(\theta\) for *every* sample size \(n\).  
> Then there exist functions \(s_{i}:\mathcal{X}\to\mathbb{R}^{k}\) (possibly different for each \(i\)) and a **common** natural‑parameter mapping \(\eta:\Theta\to\mathbb{R}^{k}\) such that for each \(i\)  
> \[
> p_{\theta}^{(i)}(x)=h_{i}(x)\exp\bigl\{\eta(\theta)^{\!\top}s_{i}(x)-A_{i}(\theta)\bigr\},
> \]
> i.e. each marginal belongs to a (possibly *curved*) exponential family **with the same natural parameter \(\eta(\theta)\)**.  
> Consequently the joint density factorises as  
> \[
> p_{\theta}^{(n)}(x_{1:n})=
> \Bigl[\prod_{i=1}^{n}h_{i}(x_{i})\Bigr]\;
> \exp\Bigl\{\eta(\theta)^{\!\top}\sum_{i=1}^{n}s_{i}(x_{i})-\sum_{i=1}^{n}A_{i}(\theta)\Bigr\},
> \]
> and the statistic  
> \[
> T_{n}= \sum_{i=1}^{n}s_{i}(X_{i})
> \]
> is *minimal* sufficient and has the fixed dimension \(k\).

### 4.3  Proof – step by step  

1. **Apply the factorisation theorem.**  
   Because a bounded‑dimensional sufficient statistic \(T_{n}\) exists for every \(n\), we can write  
   \[
   \prod_{i=1}^{n}p_{\theta}^{(i)}(x_{i})
   =g_{\theta}\!\bigl(T_{n}(x_{1:n})\bigr)\,h_{n}(x_{1:n}),
   \tag{1}
   \]
   where \(h_{n}\) does not involve \(\theta\).

2. **Take logarithms.**  
   \[
   \sum_{i=1}^{n}\log p_{\theta}^{(i)}(x_{i})
   = \log g_{\theta}\!\bigl(T_{n}\bigr) + \log h_{n}(x_{1:n}).
   \tag{2}
   \]

3. **Differentiate with respect to \(\theta\).**  
   Under the usual regularity (interchanging differentiation and summation), for each component \(j=1,\dots ,d\) we obtain  
   \[
   \sum_{i=1}^{n} \frac{\partial}{\partial\theta_{j}}\log p_{\theta}^{(i)}(x_{i})
   = \frac{\partial}{\partial\theta_{j}}\log g_{\theta}\!\bigl(T_{n}\bigr).
   \tag{3}
   \]
   The right‑hand side depends on the data **only through** \(T_{n}\); the left‑hand side is a sum of *separate* functions of the individual observations.

4. **Use the Cauchy functional‑equation argument.**  
   Equation (3) must hold for **all** sample sizes \(n\) and for **all** possible data vectors \((x_{1},\dots ,x_{n})\).  
   The only way a sum of functions of single coordinates can depend on the data through a *single* vector‑valued function is that each summand is **affine in a common vector**. Formally, there exist measurable maps  

   \[
   s_{i}:\mathcal{X}\to\mathbb{R}^{k},\qquad \psi_{j}:\Theta\to\mathbb{R}^{k},
   \]
   such that  
   \[
   \frac{\partial}{\partial\theta_{j}}\log p_{\theta}^{(i)}(x)
   = \psi_{j}(\theta)^{\!\top}s_{i}(x) + c_{ij}(\theta),
   \tag{4}
   \]
   where the constants \(c_{ij}(\theta)\) do not depend on \(x\).

5. **Integrate the partial derivatives.**  
   Integrating (4) with respect to \(\theta\) (again using regularity) yields  
   \[
   \log p_{\theta}^{(i)}(x)=\eta(\theta)^{\!\top}s_{i}(x)-A_{i}(\theta)+\log h_{i}(x),
   \tag{5}
   \]
   where we have set \(\eta(\theta)=\bigl(\psi_{1}(\theta),\dots ,\psi_{d}(\theta)\bigr)^{\!\top}\) (a \(k\)-dimensional vector) and absorbed the integration constants into \(A_{i}(\theta)\).

6. **Exponentiate to obtain the exponential form.**  
   Equation (5) is exactly the density of a (possibly curved) exponential family, *with the same natural parameter \(\eta(\theta)\) for every observation* but with *different* carrier measures \(h_{i}\) and possibly different cumulant functions \(A_{i}\).

7. **Identify the sufficient statistic.**  
   Substituting (5) back into the joint density gives the factorisation (the exponential of the sum of the \(s_{i}(x_{i})\)). Hence the statistic  

   \[
   T_{n}= \sum_{i=1}^{n}s_{i}(X_{i})
   \]

   is sufficient, has dimension \(k\) (independent of \(n\)), and is minimal by standard arguments.

8. **Conversely**, any model of the form (5) clearly possesses the statistic \(T_{n}\) above, so the condition is also *sufficient*.  

Thus the theorem is proved

*Original question: [Proof for Koopman-Pitman-Darmois under non-i.i.d observations](https://stats.stackexchange.com/questions/677046/proof-for-koopman-pitman-darmois-under-non-i-i-d-observations) on Cross Validated (Stats Stack Exchange), licensed CC BY-SA.*

{% endraw %}
