---
layout: question
title: Can per-block complementary-slackness residuals localize model-form error to
  a specific scale in a decomposed multi-scale optimization?
author: StemFix Bot
category: math
subject: math
description: 'Step-by-step mathematics solution: Can per-block complementary-slackness
  residuals localize model-form error to a specific scale in a decomposed multi-scal'
tags:
- math
---

{% raw %}
*As an Amazon Associate, I earn from qualifying purchases.* For more practice problems like this, see [Schaum's Outline of Calculus, 7th Edition](https://www.amazon.com/dp/126425833X?tag=aiopentec20-20).

---

## 1.  What the question is really asking  

*You have a huge optimisation problem that is split into several *blocks* (one block for each biological scale).  
Each block has its own primal‑dual variables and therefore its own **KKT (or complementary‑slackness) residual**.  

When the whole model gives a wrong prediction you would like to say  

> “the mistake lives in the tissue‑→‑organ block, not in the cell‑→‑tissue block”.

In other words you want to **interpret the size of the per‑block residuals as a diagnostic of model‑form error** and you would also like to know how to **separate a large residual that comes from a bad model from a large residual that simply means the iterative solver has not converged yet**.*

---

## 2.  Step‑by‑step analysis  

Below we develop the theory that tells us what a block‑wise KKT residual *means*, and we then translate this theory into practical guidelines for the “model‑error localisation” problem.

### 2.1  Write the global problem and the block structure  

Assume the whole optimisation problem can be written in the standard conic‑form

\[
\begin{aligned}
\min_{x}&\; f(x)\\[2mm]
\text{s.t. } &\; A x = b ,\\
            &\; x\in\mathcal K ,
\end{aligned}\tag{P}
\]

where  

* \(x = (x^{(1)},\dots ,x^{(S)})\) is the concatenation of the variables of the \(S\) scales,  
* \(A =\begin{bmatrix}A^{(1)}&\cdots &A^{(S)}\end{bmatrix}\) couples the blocks (the *interfaces*),  
* \(\mathcal K=\mathcal K^{(1)}\times\cdots\times\mathcal K^{(S)}\) is a product cone (non‑negativity, SOC, SDP …) that is **separable** across blocks.

The Lagrangian is  

\[
\mathcal L(x,\lambda) = f(x) + \lambda^{\!\top}(A x-b),
\]

with dual variable \(\lambda\) (one vector for the *global* equality constraints).  

The **KKT conditions** for optimality are  

\[
\begin{cases}
A x = b                     &\text{(primal feasibility)}\\[1mm]
A^{\!\top}\lambda + \nabla f(x) \in \mathcal K^{*} &\text{(dual feasibility)}\\[1mm]
x\in\mathcal K,\qquad
\langle x , A^{\!\top}\lambda + \nabla f(x)\rangle =0
&\text{(complementarity)} .
\end{cases}\tag{KKT}
\]

Because \(\mathcal K\) is a product cone, the complementarity condition **splits block‑wise**:

\[
\langle x^{(s)},\, g^{(s)}\rangle =0,\qquad  
g^{(s)}:=\bigl[\nabla f(x)+A^{\!\top}\lambda\bigr]_{(s)}\in\mathcal K^{(s)\,*},
\qquad s=1,\dots ,S .
\]

Hence we can define the **per‑block complementary‑slackness (kilter) residual**

\[
r_{\text{comp}}^{(s)} :=\bigl|\,\langle x^{(s)},g^{(s)}\rangle \bigr| .
\]

Similarly the **primal feasibility residual** of block \(s\) is

\[
r_{\text{prim}}^{(s)} := \bigl\| (A x-b)_{(s)} \bigr\| .
\]

The **global duality gap** is  

\[
\operatorname{gap}= f(x)-d(\lambda) \;=\;
\sum_{s=1}^{S} r_{\text{comp}}^{(s)} .
\]

> **Key point 1** – *If the whole algorithm has truly converged (the global duality gap is at machine precision and the primal feasibility residual is also tiny), then each block residual is a *measure of how well that block satisfies its own KKT conditions*.*

### 2.2  What does a *large* block residual mean?  

Two mutually exclusive possibilities:

| Situation | What the residual reflects | Typical signature |
|-----------|----------------------------|-------------------|
| **A. Solver not converged** | The iterates have not yet satisfied the KKT system; the error is *algorithmic*. | Residuals of *all* blocks are of comparable magnitude, **and they decay** as the iteration proceeds (often geometrically for PDHG/ADMM). |
| **B. Model‑form error** (miss‑specified physics, wrong constitutive law, wrong interface condition) | The *exact* solution of the *mis‑specified* optimisation problem is **different** from the data you are trying to fit, so even the *exact* KKT system of the *incorrect* model is infeasible with respect to the measurement constraints. | One (or a few) blocks show a *systematically larger* residual **that does not shrink** when the solver is run longer, while the rest of the blocks already sit at machine precision. |

Thus, **the only rigorous way to distinguish A from B is to check the *trend* of each block residual as the algorithm proceeds**.

### 2.3  Formal perturbation view  

Let the *true* (unknown) optimisation problem be  

\[
\min_{x} f^{\star}(x) \quad\text{s.t.}\quad A^{\star}x=b^{\star},\; x\in\mathcal K^{\star}.
\]

You actually solve a *perturbed* problem  

\[
\min_{x} f(x)=f^{\star}(x)+\Delta f(x),\qquad
A =A^{\star}+ \Delta A,\; b=b^{\star}+ \Delta b,\;
\mathcal K=\mathcal K^{\star}+\Delta\mathcal K .
\]

If the perturbations \(\Delta\) are *localized* to block \(s_{0}\) (e.g. you changed only the tissue‑organ constitutive law), then standard **sensitivity analysis** (see e.g. Bonnans‑Shapiro, *Perturbation Analysis of Optimization Problems*) gives

\[
r_{\text{comp}}^{(s)} = \mathcal O\bigl(\|\Delta\| \bigr) \;\;\text{for } s=s_{0},
\qquad
r_{\text{comp}}^{(s)} = \mathcal O\bigl(\|\Delta\|^{2}\bigr) \;\;\text{for } s\neq s_{0}.
\]

In words: *first‑order* changes in the model affect the residual **most strongly** in the block where the model was altered; other blocks feel only a second‑order effect. This is the mathematical justification for *localisation*.

If, however, the iterates are still far from a KKT point, the residual contains a *first‑order term* proportional to the **solver error** \(\varepsilon_{\text{alg}}\) that is *global*:

\[
r_{\text{comp}}^{(s)} = \varepsilon_{\text{alg}} + \mathcal O(\|\Delta\|).
\]

Hence, the *observable* residual is a sum of a *global algorithmic error* plus a *local model error*.

### 2.4  Practical diagnostic workflow  

1. **Run the solver long enough** until the *global* duality gap stabilises at a value comparable to machine precision (or at least below a user‑chosen tolerance).  
   *Plot*: \(\text{gap}_k\) vs. iteration \(k\).  

2. **Record each block’s residual at every iteration**:  
   \(\{r_{\text{comp}}^{(s)}(k)\}_{k=1}^{K}\).  

3. **Analyse the decay**  
   * If **all** residuals decay at the same rate → the problem is *solver‑limited*; no block can be blamed.  
   * If **one** (or a small group) stops decaying while the others reach machine precision → *candidate model‑error block*.

4. **Check primal feasibility** of the interfaces that involve the suspect block.  
   The interface residual  

   \[
   r_{\text{int}}^{(s\leftrightarrow s+1)} = \bigl\|\, (A^{(s)}x^{(s)}+A^{(s+1)}x^{(s+1)}-b^{(s\leftrightarrow s+1)})\bigr\|
   \]

   should also be large if the interface law is miss‑specified.

5. **Perform a *post‑hoc* refinement**:  
   * Freeze the variables of all *other* blocks at their converged values and re‑solve only the suspect block (or a small neighbourhood) with a *different* algorithm (e.g. Newton, interior‑point).  
   * If the residual now drops dramatically, the original large residual was *solver‑related*; if it stays large, the block’s model is indeed inconsistent with the data.

6. **Statistical sanity check** (optional):  
   Treat the residual vector \(\mathbf r=(r_{\text{comp}}^{(1)},\dots ,r_{\text{comp}}^{(S)})\) as a random variable under the hypothesis “solver has converged”. Compute the empirical mean \(\mu\) and standard deviation \(\sigma\) of the *converged* blocks, then flag any block with  

   \[
   r_{\text{comp}}^{(s)} > \mu + 3\sigma
   \]

   as a *significant outlier*.

### 2.5  What the literature says  

| Area | What it contributes to the question |
|------|--------------------------------------|
| **Domain decomposition / FETI‑DP / BDDC** | Provides *block‑wise* equilibrium residuals; they are used to *balance* loads, not to diagnose model error. The theory (e.g. Mandel’s *balancing domain decomposition*) tells us the residual is zero *iff* the global KKT system is satisfied. |
| **A‑posteriori error estimation (finite‑element)** | Splits the total error into element‑wise contributions; the same mathematics (dual‑weighted residual) can be transplanted to optimisation blocks. |
| **Sensitivity / Perturbation analysis of KKT systems** (Bonnans‑Shapiro, Fiacco) | Gives the *first‑order* effect of a local model perturbation on the KKT residuals – exactly the theoretical justification for localisation. |
| **Inexact KKT / Stopping criteria for ADMM/PDHG** (Boyd et al., 2011) | Shows that a *global* tolerance \(\varepsilon\) guarantees \(\|r_{\text{comp}}^{(s)}\|\le\varepsilon\) for *all* blocks. No block‑wise distinction is possible unless you tighten the tolerance further. |
| **Model‑error detection in inverse problems** (Kaipio & Somersalo, 2005) | Uses the *discrepancy principle*: if the data‑misfit residual is larger than the expected noise level, the forward model is suspect. The same idea can be applied to block‑wise KKT residuals. |

In short: **the theory exists, but it tells you that block‑wise residuals can only be interpreted as model‑error indicators *after* the algorithmic error has been driven below the size of the model error**.

### 2.6  Answer to the two concrete questions  

1. **Is there an established theory / practice for using per‑block KKT residuals as a model‑error localiser?**  
   Yes. The theory comes from *perturbation analysis of KKT systems* and from *a‑posteriori error estimation* for decomposed optimisation. The practical practice is to (i) drive the global duality gap to machine precision, (ii) monitor the decay of each block’s residual, and (iii) treat any block whose residual stalls as a candidate model‑error location.

2. **Are there results that let us tell “large residual because the model is wrong” from “large residual because the solver is struggling”?**  
   The distinguishing feature is **temporal behaviour**:  
   * Solver‑induced residuals decay together across all blocks; they vanish at the same rate as the global gap.  
   * Model‑

*Original question: [Can per-block complementary-slackness residuals localize model-form error to a specific scale in a decomposed multi-scale optimization?](https://math.stackexchange.com/questions/5151383/can-per-block-complementary-slackness-residuals-localize-model-form-error-to-a-s) on Mathematics Stack Exchange, licensed CC BY-SA.*

{% endraw %}
