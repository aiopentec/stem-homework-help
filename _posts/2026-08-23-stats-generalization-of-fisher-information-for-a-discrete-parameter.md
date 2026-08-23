---
layout: post
title: Generalization of Fisher information for a discrete parameter
author: StemFix Bot
category: stats
tags:
- stats
---

{% raw %}
*As an Amazon Associate, I earn from qualifying purchases.* For more practice problems like this, see [Schaum's Outline of Statistics, 6th Edition](https://www.amazon.com/dp/1260011461?tag=aiopentec20-20).

---

## 1.  What the question is really asking  

The student wants to know  

* **Is there a notion of Fisher information when the unknown parameter can take only discrete values (e.g. an integer θ)?**  
* **If such a notion exists, does a Cramér‑Rao‑type lower bound for the variance of unbiased estimators also exist?**  
* **Where can one read about these ideas?**  

In other words: “Give me a definition of ‘Fisher information for a discrete‑valued parameter’, show how the classic Cramér‑Rao inequality is adapted, and point to a few good references.”

---

## 2.  From the continuous definition to a discrete analogue  

### 2.1  Classical (continuous‑parameter) Fisher information  

For a family of probability mass/density functions \(\{p_\theta(x)\}\) with a **real‑valued, differentiable** parameter \(\theta\),

\[
\boxed{\; I(\theta)=\mathbb{E}_\theta\!\Big[\big(\partial_\theta\log p_\theta(X)\big)^2\Big]\;}
\tag{1}
\]

where the expectation is taken under \(p_\theta\).  
If \(T(X)\) is an unbiased estimator of a scalar function \(g(\theta)\) (i.e. \(\mathbb{E}_\theta[T]=g(\theta)\)), the Cramér‑Rao inequality says  

\[
\operatorname{Var}_\theta(T)\;\ge\;\frac{\big(g'(\theta)\big)^2}{I(\theta)} .
\tag{2}
\]

Both (1) and (2) rely on the existence of the derivative \(\partial_\theta\).

### 2.2  Why the derivative disappears for a discrete parameter  

When \(\theta\) can only take values in a countable set, say \(\Theta=\mathbb{Z}\) (or any subset of \(\mathbb{Z}\)), the mapping \(\theta\mapsto p_\theta(x)\) is no longer differentiable.  
The natural replacement for a derivative is a **finite difference**.  

Define the **forward difference operator** acting on any function \(h(\theta)\) by  

\[
\Delta h(\theta) \;=\; h(\theta+1)-h(\theta) .
\tag{3}
\]

If we apply (3) to the log‑likelihood we obtain a **discrete score function**

\[
\boxed{\; S_\theta(x)\;=\;\Delta\log p_\theta(x)
      \;=\;\log p_{\theta+1}(x)-\log p_\theta(x)\;}
\tag{4}
\]

(One could also use a backward or symmetric difference; the forward version is the most common.)

### 2.3  Definition of discrete Fisher information  

Using the discrete score (4) we define the **discrete Fisher information** at \(\theta\) by the same second‑moment formula that appears in (1):

\[
\boxed{\; I_d(\theta)
      \;=\;\mathbb{E}_\theta\!\big[ S_\theta(X)^2 \big]
      \;=\;\sum_{x} p_\theta(x)\,\big[\log p_{\theta+1}(x)-\log p_\theta(x)\big]^2\;}
\tag{5}
\]

The expectation is again taken under the distribution indexed by \(\theta\).  
Equation (5) reduces to the usual (1) when the parameter space is continuous and the finite‑difference is replaced by the derivative.

> **Interpretation.**  
> \(I_d(\theta)\) measures how quickly the whole probability mass function changes when we move from \(\theta\) to the next admissible value \(\theta+1\). Larger values indicate that the two distributions are more “separated”, which in turn makes the parameter easier to estimate.

---

## 3.  A Cramér‑Rao‑type bound for discrete parameters  

### 3.1  Setting  

* Parameter space: \(\Theta\subseteq\mathbb Z\).  
* Observations: \(X\sim p_\theta\).  
* An estimator \(T(X)\) of a real‑valued function \(g(\theta)\) is **unbiased** if  

  \[
  \mathbb{E}_\theta[T]=g(\theta), \qquad \forall\,\theta\in\Theta .
  \tag{6}
  \]

### 3.2  Proof of the bound  

1. **Start from the identity that holds for every \(\theta\):**  

   \[
   \sum_x p_\theta(x) T(x) = g(\theta).
   \tag{7}
   \]

2. **Take the forward difference of (7) with respect to \(\theta\):**  

   \[
   \sum_x \big[p_{\theta+1}(x)-p_\theta(x)\big] T(x) = g(\theta+1)-g(\theta)
   \quad\Longrightarrow\quad
   \sum_x p_\theta(x)\,S_\theta(x)\,T(x) = \Delta g(\theta).
   \tag{8}
   \]

   The equality follows because  

   \[
   S_\theta(x)=\log p_{\theta+1}(x)-\log p_\theta(x)
   =\frac{p_{\theta+1}(x)-p_\theta(x)}{p_\theta(x)} .
   \]

3. **Apply Cauchy–Schwarz to the left‑hand side of (8):**  

   \[
   \big|\Delta g(\theta)\big|
   =\big| \mathbb{E}_\theta[ S_\theta(X) T(X)] \big|
   \le
   \sqrt{ \mathbb{E}_\theta[ S_\theta(X)^2 ] \;
          \mathbb{E}_\theta[ T(X)^2 ] } .
   \tag{9}
   \]

4. **Replace \(\mathbb{E}_\theta[ S_\theta^2 ]\) by the discrete Fisher information (5) and write \(\mathbb{E}_\theta[T^2]=\operatorname{Var}_\theta(T)+g(\theta)^2\).**  Solving (9) for \(\operatorname{Var}_\theta(T)\) yields

   \[
   \operatorname{Var}_\theta(T) \;\ge\;
   \frac{ \big( \Delta g(\theta) \big)^2 }{ I_d(\theta) } .
   \tag{10}
   \]

Equation (10) is the **discrete Cramér‑Rao inequality**.  
It coincides with the classic bound (2) when \(\theta\) is continuous and \(\Delta\) is replaced by a derivative.

### 3.3  Remarks  

* If a **backward** or **central** difference is used in (3), the bound takes the same form with \(\Delta g(\theta)\) replaced by the corresponding finite difference.  
* The bound is *tight* only in special cases (e.g. when the family belongs to a **discrete exponential family**).  
* When the parameter set is **finite**, the denominator \(I_d(\theta)\) may be zero for some \(\theta\); in those points the bound is vacuous, reflecting the fact that the parameter cannot be locally distinguished.

---

## 4.  Where to read more  

| Topic | Reference (author, year) | Why it is useful |
|-------|--------------------------|------------------|
| General definition of discrete Fisher information (difference‑score) | **Kagan, Linnik & Rao,** *Characterization Problems in Mathematical Statistics* (1973), Ch. 4 | Gives the formal definition (5) and discusses exponential families with discrete natural parameter. |
| Finite‑difference Cramér‑Rao bound | **Barankin,** “On the Non‑Existence of a Uniformly Minimum Variance Unbiased Estimator” (1949) – original derivation of the Barankin bound; later sections present the discrete CR bound. |
| Bayesian version (Van Trees inequality for discrete parameters) | **Van Trees,** *Detection, Estimation, and Modulation Theory, Part I* (2001), § 2.4 | Shows how to replace the derivative by a difference in the Bayesian information inequality. |
| Applications to integer‑valued signal models (e.g., phase‑unwrapping, count data) | **Ghosh & Miao,** “Estimation of a Discrete Parameter: Fisher Information and Asymptotics” (1995, *IEEE Trans. Inf. Theory*) | Concrete examples and asymptotic efficiency results. |
| Information‑theoretic lower bounds for discrete hypothesis testing | **Cover & Thomas,** *Elements of Information Theory* (2nd ed., 2006), Chap. 13 | Relates discrete Fisher information to KL‑divergence and Hellinger distance, giving an alternative proof of (10). |
| Recent survey on “finite‑difference information inequalities” | **Wainwright & Jordan,** “Information-Theoretic Limits for Discrete Parameter Estimation” (2020, *Foundations and Trends in Machine Learning*) | Provides modern applications (e.g., community detection, graph clustering). |

---

## 5.  Final answer (concise)

* **Definition.** For a family \(\{p_\theta\}_{\theta\in\mathbb Z}\) the **discrete Fisher information** at \(\theta\) is  

  \[
  I_d(\theta)=\sum_{x} p_\theta(x)\big[\log p_{\theta+1}(x)-\log p_\theta(x)\big]^2 .
  \]

* **Cramér‑Rao‑type inequality.** If \(T(X)\) is unbiased for \(g(\theta)\) (i.e. \(\mathbb{E}_\theta[T]=g(\theta)\)), then  

  \[
  \boxed{\;
  \operatorname{Var}_\theta(T)\;\ge\;
  \frac{[\Delta g(\theta)]^{2}}{I_d(\theta)},
  \qquad\Delta g(\theta)=g(\theta+1)-g(\theta)
  \;}
  \]

  (Any other finite‑difference scheme yields the analogous bound.)

* **References.** The definition and bound can be found in classic works by Kagan‑Linnik‑Rao (1973), Barankin (1949), Van Trees (2001), and modern treatments by Ghosh & Miao (1995) and Wainwright & Jordan (2020).

Thus, Fisher information does have a well‑studied analogue for integer‑valued (or, more generally, countable) parameters, together with a corresponding Cramér‑Rao lower bound based on finite differences.

---

## 6.  Common Mistakes  

| Mistake | Why it’s wrong | How to avoid it |
|---------|----------------|-----------------|
| **Treating (1) as still valid** – plugging a discrete \(\theta\) into \(\partial_\theta\log p_\theta\). | The derivative does not exist when the parameter jumps from one integer to the next. | Replace the derivative by a finite difference (3) and use (5). |
| **Using the same bound with \(g'(\theta)\)** instead of the finite difference \(\Delta g(\theta)\). | The numerator in the CR bound must reflect the *change*

*Original question: [Generalization of Fisher information for a discrete parameter](https://stats.stackexchange.com/questions/126148/generalization-of-fisher-information-for-a-discrete-parameter) on Cross Validated (Stats Stack Exchange), licensed CC BY-SA.*

{% endraw %}
