---
layout: post
title: Help me understand the Bayesian kernel density estimation (Sibisi and Skilling,
  1996)
author: StemFix Bot
category: stats
tags:
- stats
---

{% raw %}
*As an Amazon Associate, I earn from qualifying purchases.* For more practice problems like this, see [Schaum's Outline of Statistics, 6th Edition](https://www.amazon.com/dp/1260011461?tag=aiopentec20-20).

---

## 1.  What the question is asking (in plain language)

The student is trying to understand the **Bayesian kernel‑density estimator** introduced by
Sibisi & Skilling (1996, 1997).  

The basic idea is  

\[
f(x)=\int \phi(x')\,K(x,x')\,dx' \qquad\text{(eq. 2)}
\]

* \(K(x,x')\) is a *fixed* smoothing kernel (Gaussian, Epanechnikov, …).  
* \(\phi(x)\) is an **unknown latent density** that lives on the same space as the data.  
* By discretising the space into \(M\) non‑overlapping cells \(\{\mathcal C_i\}\) we can write  

\[
\Phi_i=\int_{\mathcal C_i}\phi(x)\,dx ,\qquad i=1,\dots ,M,
\]

so that the continuous integral becomes the matrix equation  

\[
\mathbf f = K\;\boldsymbol\Phi .
\]

The question is:  

1. **What prior should we put on the vector \(\boldsymbol\Phi\)?**  
2. **How do we obtain the posterior for \(\boldsymbol\Phi\) after observing data?**  
3. **Why does the kernel, not the prior on \(\boldsymbol\Phi\), provide the smoothness?**  

The answer is that a **Dirichlet prior** (or, in the limiting case, a flat prior) is the natural choice because the \(\Phi_i\) are non‑negative and must sum to one.  With a multinomial likelihood the posterior is again Dirichlet, and the posterior mean plugged into \(K\) gives the Bayesian kernel‑density estimate.  When we take the empirical distribution \(\Phi_i=1/N\) we recover the ordinary (non‑Bayesian) kernel density estimator.

Below is a **step‑by‑step derivation** of the posterior, the predictive density, and the link to the standard KDE.

---

## 2.  Detailed derivation

### 2.1  Discretising the latent density  

*Partition of the observation space*  
Let the support of the data be split into \(M\) cells \(\mathcal C_i\) (they can be equal‑width bins, a Voronoi tessellation, etc.). Define  

\[
\Phi_i = \int_{\mathcal C_i}\phi(x)\,dx ,\qquad
\Phi_i\ge 0,\qquad
\sum_{i=1}^M\Phi_i = 1 .
\]

Collect them into the column vector \(\boldsymbol\Phi=(\Phi_1,\dots ,\Phi_M)^{\!\top}\).

*Discretised kernel*  
Define the matrix  

\[
K_{ji}= \int_{\mathcal C_j}K(x,x_i)\,dx,
\]

where \(x_i\) is a representative point (e.g. the centre) of cell \(\mathcal C_i\).  Then  

\[
f_j \equiv \int_{\mathcal C_j} f(x)\,dx = \sum_{i=1}^M K_{ji}\,\Phi_i .
\]

In compact form:  

\[
\mathbf f = K \,\boldsymbol\Phi . \tag{1}
\]

### 2.2  Likelihood for the observed sample  

Assume we have an i.i.d. sample \(\{x^{(n)}\}_{n=1}^N\).  Let  

\[
n_j = \#\{n: x^{(n)}\in \mathcal C_j\},\qquad
\sum_{j=1}^M n_j = N .
\]

Given a latent density \(\boldsymbol\Phi\), the probability that a single observation lands in cell \(j\) is \(\Phi_j\).  Because the observations are independent, the vector of cell counts follows a **multinomial distribution**:

\[
p(\mathbf n \mid \boldsymbol\Phi) =
\frac{N!}{\prod_{j=1}^M n_j!}\;
\prod_{j=1}^M \Phi_j^{\,n_j}. \tag{2}
\]

(Here \(\mathbf n = (n_1,\dots ,n_M)\).)

### 2.3  Prior on \(\boldsymbol\Phi\)  

The \(\Phi_i\) are probabilities, i.e. they lie on the \((M-1)\)-simplex.  The **conjugate prior** for the multinomial is the **Dirichlet distribution**:

\[
p(\boldsymbol\Phi\mid\boldsymbol\alpha)=
\frac{1}{B(\boldsymbol\alpha)}\;
\prod_{i=1}^M \Phi_i^{\,\alpha_i-1},
\qquad
\alpha_i>0,
\tag{3}
\]

with normalising constant  

\[
B(\boldsymbol\alpha)=\frac{\prod_{i=1}^M\Gamma(\alpha_i)}
{\Gamma\!\left(\sum_{i=1}^M\alpha_i\right)} .
\]

A *flat* (non‑informative) prior corresponds to \(\alpha_i = 1\) for all \(i\), i.e. the **uniform Dirichlet**.

### 2.4  Posterior for \(\boldsymbol\Phi\)

Apply Bayes’ rule (up to a constant that does not depend on \(\boldsymbol\Phi\)):

\[
p(\boldsymbol\Phi \mid \mathbf n) \;\propto\;
p(\mathbf n \mid \boldsymbol\Phi)\;p(\boldsymbol\Phi).
\]

Insert (2) and (3):

\[
\begin{aligned}
p(\boldsymbol\Phi \mid \mathbf n) 
&\propto
\Bigl[ \prod_{j=1}^M \Phi_j^{\,n_j}\Bigr]\;
\Bigl[ \prod_{i=1}^M \Phi_i^{\,\alpha_i-1}\Bigr] \\
&= \prod_{i=1}^M \Phi_i^{\,(\alpha_i+n_i)-1}.
\end{aligned}
\]

Hence the posterior is again Dirichlet, with **updated parameters**

\[
\boxed{\;\alpha_i^{\text{post}} = \alpha_i + n_i\;},\qquad i=1,\dots ,M .
\]

In words: the prior “pseudo‑counts’’ \(\alpha_i\) are simply added to the observed cell counts.

### 2.5  Posterior mean of \(\boldsymbol\Phi\)

The Dirichlet mean is well‑known:

\[
\mathbb{E}[\Phi_i\mid\mathbf n]=
\frac{\alpha_i+n_i}{\displaystyle \sum_{k=1}^M(\alpha_k+n_k)}.
\]

With a flat prior (\(\alpha_i=1\)) this reduces to the **empirical frequencies**:

\[
\mathbb{E}[\Phi_i\mid\mathbf n]=\frac{n_i}{N}.
\]

### 2.6  Bayesian kernel‑density estimate  

Recall (1): \(\mathbf f = K\boldsymbol\Phi\).  The **posterior predictive density** (the expectation of \(f\) under the posterior for \(\boldsymbol\Phi\)) is

\[
\boxed{\;
\hat{\mathbf f}
= K\,\mathbb{E}[\boldsymbol\Phi\mid\mathbf n]
= K \,\frac{\boldsymbol\alpha+\mathbf n}
          {\sum_{k}(\alpha_k+n_k)}\; }.
\]

If we choose the uniform prior (\(\alpha_i=1\)) and replace the denominator by \(N\) (ignoring the additive “\(M\)” which is negligible for large \(N\)), we obtain

\[
\hat{\mathbf f}\; \approx\;
\frac{1}{N}\, K\mathbf n .
\]

In the continuous limit, \(\mathbf n\) becomes a sum of Dirac deltas at the data points, and the matrix product \(K\mathbf n/N\) is exactly the **standard kernel density estimator (KDE)**:

\[
\boxed{\;
\hat f(x)=\frac1N\sum_{n=1}^{N} K\bigl(x,x^{(n)}\bigr)\; }.
\]

Thus the ordinary KDE appears as the **posterior mean** of the Bayesian model when the prior on \(\boldsymbol\Phi\) is flat (or when we set \(\Phi_i=1/N\) a priori).

### 2.7  Where does the smoothness come from?  

* The kernel matrix \(K\) spreads each cell’s mass over a neighbourhood determined by the kernel’s bandwidth and shape.  
* The prior on \(\boldsymbol\Phi\) only enforces that the cell masses are non‑negative and sum to one; it does **not** impose any spatial regularisation.  
* Consequently, **all smoothing is supplied by the kernel**, exactly as Sibisi & Skilling state.

If one wishes to enforce additional smoothness on \(\phi(x)\) itself, one would have to place a *process* prior (e.g. a Gaussian process) on the log‑density, but that is **outside** the Dirichlet‑\(\Phi\) construction.

---

## 3.  Final answer (summary)

| Symbol | Meaning |
|--------|----------|
| \(K(x,x')\) | Fixed smoothing kernel, normalised in the first argument |
| \(\phi(x)\) | Latent density (unknown) |
| \(\Phi_i = \int_{\mathcal C_i}\phi(x)dx\) | Mass of \(\phi\) in cell \(i\) |
| \(\mathbf f = K\boldsymbol\Phi\) | Discrete version of \(f(x)=\int\phi K\) |
| \(\mathbf n\) | Observed cell counts, \(n_i\) in cell \(i\) |
| Prior on \(\boldsymbol\Phi\) | Dirichlet\((\alpha_1,\dots ,\alpha_M)\); uniform prior = \(\alpha_i=1\) |
| Posterior on \(\boldsymbol\Phi\) | Dirichlet\((\alpha_i+n_i)\) |
| Posterior mean | \(\displaystyle \hat\Phi_i = \frac{\alpha_i+n_i}{\sum_k(\alpha_k+n_k)}\) |
| Bayesian KDE (posterior predictive) | \(\displaystyle \hat f(x)=\sum_{i=1}^M K(x,x_i)\,\hat\Phi_i\) |
| Ordinary KDE | Obtained when \(\alpha_i=1\) (flat prior) and \(\hat\Phi_i\approx n_i/N\) ⇒ \(\displaystyle \hat f(x)=\frac1N\sum_{n=1}^{N}K(x,x^{(n)})\) |

Hence:

* **Prior:** Dirichlet (uniform = flat).  
* **Posterior:** Dirichlet with parameters \(\alpha_i+n_i\).  
* **Predictive density:** kernel matrix times posterior mean of \(\Phi\).  
* **Smoothness:** supplied solely by the kernel \(K\); the Dirichlet prior only guarantees a proper probability vector.

---

## 4.  Common mistakes when working with this model

| Mistake | Why it’s wrong | How to avoid it |
|---------|----------------|-----------------|
| **Treating \(\Phi_i\) as independent Gaussian variables.** | The \(\Phi_i\) must be non‑negative and sum to one; a Gaussian prior cannot enforce these constraints. | Use a Dirichlet (or other simplex‑constrained) prior. |
| **Forgetting the normalising constant of the Dirichlet.** | When writing the posterior you may drop the constant, but later when computing marginal likelihoods it is needed. | Keep \(B(\boldsymbol\alpha)\) in symbolic form; it cancels in many calculations but is required for model comparison. |
| **Using a kernel that is not normalised.** | The derivation assumes \(\int K(x,x')dx = 1\) for each \(x'\); otherwise \(\mathbf f\) will not be a density. | Verify or explicitly normalise the kernel before building \(K\). |
| **Confusing the cell‑based KDE with the continuous KDE.** | The discrete formulation approximates the integral; with coarse cells the estimate can be biased. | Choose a fine partition (large \(M\)) or work directly with the continuous sum \(\frac1N\sum K(x,x^{(n)})\). |
| **Setting the Dirichlet hyper‑parameters to zero.** | \(\alpha_i=0\) gives an *improper* prior that places zero mass on any cell with no observations, leading to a degenerate posterior. | Use at least \(\alpha_i=1\) (uniform) or a small positive value (e.g., 0.5) for a weakly‑informative prior. |
| **Assuming the posterior mean is the same as the maximum‑a‑posteriori (MAP)

*Original question: [Help me understand the Bayesian kernel density estimation (Sibisi and Skilling, 1996)](https://stats.stackexchange.com/questions/300906/help-me-understand-the-bayesian-kernel-density-estimation-sibisi-and-skilling) on Cross Validated (Stats Stack Exchange), licensed CC BY-SA.*

{% endraw %}
