---
layout: post
title: Asymptotic property of tuning parameter in penalized regression
author: StemFix Bot
category: stats
tags:
- stats
render_with_liquid: false
---

*As an Amazon Associate, I earn from qualifying purchases.* For more practice problems like this, see [Schaum's Outline of Statistics, 6th Edition](https://www.amazon.com/dp/1260011461?tag=aiopentec20-20).

---

## 1.  What the student is really asking  

The student is working with a **penalised likelihood estimator**

\[
\hat\beta(\lambda)=\arg\min_{\beta}\Big\{-\ell(\beta;X,Y)+n\lambda\,p(\beta)\Big\},
\]

and has seen in the theoretical literature two *asymptotic* requirements on the
tuning constant \(\lambda\):

* **(i)  \(\lambda\to0\)** – the penalty must disappear as the sample size grows, otherwise the estimator would be biased even for the truly non‑zero coefficients.
* **(ii)  \(\sqrt{n}\,\lambda\to\infty\)** (or, more generally, \(n^{1/2}\lambda\to\infty\) or \(n^{\gamma}\lambda\to\infty\) for some \(\gamma>0\)) – the penalty must not shrink *too* fast, otherwise it cannot separate the zero coefficients from the non‑zero ones.

The student wonders:

1. **How can we “impose’’ such bounds when we only have one finite data set?**  
2. **Do common data‑driven choices of \(\lambda\) (CV, AIC, BIC, …) automatically satisfy them?**  
3. **What should we do in practice if we want to prove oracle‑type results for a new penalty?**  

Below is a step‑by‑step answer that explains why the two conditions appear, how they are linked to the way we *select* \(\lambda\) in large samples, and what concrete actions (theoretical and simulation‑based) a researcher can take.

---

## 2.  Why the two bounds are needed  

### 2.1  The penalised estimating equation  

Write the (negative) log‑likelihood as \(L_n(\beta)=-\ell(\beta;X,Y)\).  
The penalised estimator solves  

\[
\frac{\partial}{\partial\beta}\,L_n(\beta)
        + n\lambda \,\dot p(\beta)=0,
\tag{1}
\]

where \(\dot p(\beta)=\partial p(\beta)/\partial\beta\) is the sub‑gradient of the penalty.  

Assume a *fixed‑p* setting (the number of regression coefficients \(p\) does **not**
grow with \(n\)).  Let \(\beta^0\) be the true parameter and split it into

\[
\beta^0=(\beta^0_{(1)}^\top,\; \beta^0_{(0)}^\top)^\top,
\]

where \(\beta^0_{(1)}\) contains the truly non‑zero components (size \(s\)) and
\(\beta^0_{(0)}\) the truly zero components (size \(p-s\)).

### 2.2  Bias for the non‑zero coefficients  

A Taylor expansion of the likelihood gradient around \(\beta^0\) gives  

\[
\frac{\partial}{\partial\beta}L_n(\beta^0)=\underbrace{O_p(\sqrt n)}_{\text{score}}
\qquad\text{and}\qquad
\frac{\partial^2}{\partial\beta\partial\beta^\top}L_n(\beta^0)=n\,\mathcal I(\beta^0)+o_p(n),
\]

with \(\mathcal I(\beta^0)\) the Fisher information matrix.  
If \(\lambda\) does **not** go to zero, the term \(n\lambda\dot p(\beta^0_{(1)})\) would be of order
\(n\lambda\), which dominates the score term of order \(\sqrt n\).  The solution of (1) would then be pulled away from \(\beta^0_{(1)}\) and the estimator would be **asymptotically biased**.  

Hence we must have  

\[
\lambda\to0\quad\Longrightarrow\quad n\lambda=o(\sqrt n).
\tag{2}
\]

In practice (2) is expressed as \(\sqrt n\,\lambda\to0\) or, more conveniently, as the
single condition \(\lambda\to0\); the second condition below will guarantee that (2) is *not* violated.

### 2.3  Variable‑selection consistency (zero coefficients)  

For a zero component \(j\in\{s+1,\dots,p\}\) the estimating equation reduces to  

\[
\frac{\partial}{\partial\beta_j}L_n(\beta^0)+n\lambda\,\dot p_j(0)=0 .
\]

Because the likelihood gradient for a true zero coefficient is \(O_p(\sqrt n)\),
the penalty must be **large enough** to dominate this stochastic term, i.e.  

\[
n\lambda\,|\dot p_j(0)|\; \gg\; \sqrt n\quad\Longrightarrow\quad
\sqrt n\,\lambda\; \to\;\infty .
\tag{3}
\]

Condition (3) guarantees that, with probability tending to one, the solution of (1) sets those coefficients exactly to zero (or, for non‑convex penalties, shrinks them into the region where the derivative forces a zero solution).  

### 2.4  Combining (2) and (3)  

Both requirements together give the familiar **double‑asymptotic window**

\[
\boxed{\;\lambda_n\;\longrightarrow\;0
\quad\text{and}\quad
\sqrt n\,\lambda_n\;\longrightarrow\;\infty\;}
\tag{4}
\]

or, equivalently, any sequence of the form  

\[
\lambda_n = c\, n^{-\alpha},\qquad 0<\alpha<\tfrac12,
\tag{5}
\]

with a positive constant \(c\).  
The exact exponent \(\alpha\) may differ when the penalty is non‑convex (e.g. SCAD, MCP) or when the number of predictors diverges, but the *order* in (4) stays the same for the oracle property.

---

## 3.  How a data‑driven selector can satisfy (4)  

### 3.1  BIC‑type selectors  

For linear models with Gaussian errors, the *extended BIC* (EBIC) chooses  

\[
\hat\lambda = \arg\min_{\lambda\in\Lambda}\Big\{-2\ell(\hat\beta(\lambda))
          + \log(n)\,df(\lambda)
          + 2\gamma\log\binom{p}{df(\lambda)}\Big\},
\]

where \(df(\lambda)\) is the number of non‑zero estimated coefficients.
Under the usual regularity conditions (fixed \(p\), true sparsity \(s\)), it can be shown (e.g. Chen & Chen 2008; Wang, Li & Leng 2009) that  

\[
\Pr\bigl(\hat\lambda\in\{\lambda_n: \lambda_n\asymp n^{-\alpha},\;0<\alpha<\tfrac12\}\bigr)\to 1 .
\]

In words: the BIC minimiser automatically falls inside the admissible window (5) with probability approaching one, because the penalty on model size (\(\log n\)) grows more slowly than \(\sqrt n\) but faster than any constant.

### 3.2  AIC and ordinary CV  

* AIC uses a penalty \(2\,df\) which is *\(O(1)\)*, not \(\log n\).  Consequently, the selected \(\lambda\) does **not** shrink to zero fast enough to guarantee (3).  In fact, AIC tends to choose a model that is too large for variable‑selection consistency.  It can still give asymptotically optimal prediction risk, but not the oracle property.

* **\(K\)-fold cross‑validation (CV)**:  
  The CV criterion mimics prediction error, which is of order \(O(1)\).  Classical results (Shao 1993; Li 1987) show that *ordinary* CV selects a \(\lambda\) that is *asymptotically equivalent* to minimizing the prediction risk, i.e. \(\lambda_n\asymp n^{-1/2}\).  This is *borderline*: it may satisfy \(\sqrt n\lambda_n\to c\) (a finite constant) rather than \(\to\infty\).  Hence ordinary CV does **not** guarantee model‑selection consistency, although *modified* CV (e.g. “\(K\)-fold CV with a penalty term” or “stability‑selection CV”) can be tuned to produce \(\lambda\) inside the window (5).

### 3.3  Adaptive‑Lasso and SCAD  

For penalties that *depend* on a preliminary root‑\(n\) consistent estimator (adaptive Lasso) or that have a *vanishing derivative* for large coefficients (SCAD, MCP), the condition (4) can be weakened.  The literature (Fan & Li 2001; Zou 2006; Zhang 2010) shows that if the *initial* estimator satisfies \(\|\tilde\beta-\beta^0\|=O_p(n^{-1/2})\) and the final penalty uses weights \(w_j=1/|\tilde\beta_j|^\gamma\) (\(\gamma>0\)), then it suffices to take a **single** \(\lambda_n\) such that  

\[
\lambda_n\asymp n^{-1/2}\quad\text{and}\quad
\lambda_n\max_j w_j \to 0 .
\]

In practice one still selects \(\lambda\) by BIC or by a grid search; the theory guarantees that the selected value will belong to the admissible region with probability tending to one.

### 3.4  Summary of the “practical” rule  

| Selection method | Asymptotic behaviour of \(\hat\lambda\) | Model‑selection consistency? |
|------------------|----------------------------------------|------------------------------|
| BIC / EBIC       | \(\hat\lambda\asymp n^{-\alpha},\;0<\alpha<½\) | **Yes** (under regularity) |
| AIC              | \(\hat\lambda\asymp n^{0}\) (constant) | No |
| Ordinary \(K\)-fold CV | \(\hat\lambda\asymp n^{-½}\) (borderline) | No (unless modified) |
| Stability‑selection / “CV‑plus” | can be forced into the window | Yes (with extra conditions) |

Thus, the theoretical papers are *not* ignoring the fact that we have a single data set; they are stating that **any** selection rule whose asymptotic limit falls inside the window (4) will inherit the oracle properties proved under that window.

---

## 4.  How to verify the condition for a new penalty  

### 4.1  Derive the derivative behavior  

For a generic penalty \(p_\lambda(\beta)=\lambda\,\sum_{j} \rho(|\beta_j|)\) we need two facts:

1. **Near zero**: \(\rho'(0^+)=c>0\) (or \(\lim_{t\downarrow0}\rho'(t)=c\)).  
   Then (3) becomes \(\sqrt n\,\lambda c\to\infty\).

2. **Away from zero**: \(\rho'(t)\) should either be 0 (SCAD, MCP) or decay fast enough so that for the true non‑zero coefficients \(\beta_j^0\neq0\),

   \[
   \lambda\,\rho'(|\beta_j^0|)=o\!\left(n^{-1/2}\right) .
   \]

   This translates to \(\lambda=o(n^{-1/2})\), i.e. condition (2).

If the new penalty satisfies these two derivative requirements, the same proof used for Lasso/SCAD carries over.

### 4.2  Prove that a selector lands in the window  

Take the selector (e.g. BIC) and write its objective as  

\[
\mathcal{C}_n(\lambda)= -2\ell\bigl(\hat\beta(\lambda)\bigr)+\kappa_n\,df(\lambda),
\]

with \(\kappa_n\) growing at rate \(\log n\

*Original question: [Asymptotic property of tuning parameter in penalized regression](https://stats.stackexchange.com/questions/57219/asymptotic-property-of-tuning-parameter-in-penalized-regression) on Cross Validated (Stats Stack Exchange), licensed CC BY-SA.*
