---
layout: question
title: Confusion about upper and lower indices
author: StemFix Bot
category: physics
subject: physics
description: 'Step-by-step physics solution: Confusion about upper and lower indices'
tags:
- physics
---

{% raw %}
*As an Amazon Associate, I earn from qualifying purchases.* For more practice problems like this, see [Schaum's Outline of College Physics, 12th Edition](https://www.amazon.com/dp/1259587398?tag=aiopentec20-20).

---

## 1.  What the student is asking  

The student wants to compute the components of the product  

\[
X^{T}\,g ,
\]

where  

* \(X\) is a (1,1)‑type tensor (a matrix) with components \(X^{\mu}{}_{\nu}\);
* \(g\) is the metric tensor with components \(g_{\mu\nu}=g_{\nu\mu}\) (or its inverse \(g^{\mu\nu}\));
* The superscript **T** denotes the **matrix transpose**, i.e. \((X^{T})^{\mu}{}_{\nu}=X_{\nu}{}^{\mu}\) when the metric is used to raise/lower the indices.

The student tried two different ways of “expanding” the product, obtained  

\[
X_{\nu}{}^{\mu}\qquad\text{and}\qquad X^{\nu}{}_{\mu},
\]

and wonders which step is illegal and why the two results differ.

---

## 2.  Detailed, step‑by‑step solution  

### 2.1  Conventions we will use  

| Symbol | Meaning |
|--------|---------|
| \(X^{\mu}{}_{\nu}\) | components of a (1,1) tensor (a linear map) |
| \(g_{\mu\nu}\) | metric (covariant) – lowers an index: \(V_{\mu}=g_{\mu\nu}V^{\nu}\) |
| \(g^{\mu\nu}\) | inverse metric – raises an index: \(V^{\mu}=g^{\mu\nu}V_{\nu}\) |
| \(\delta^{\mu}{}_{\nu}\) | Kronecker delta, the identity matrix |
| \((X^{T})\) | matrix transpose **with respect to the metric**: \((X^{T})^{\mu}{}_{\nu}=X_{\nu}{}^{\mu}\) .  In index‑free language, the transpose is the adjoint defined by \(g(Xu,v)=g(u,X^{T}v)\). |

*Important:* Raising or lowering an index **must be done with the metric**, never by simply swapping the position of an index. In other words, \(X^{\mu\nu}\neq X^{\nu\mu}\) unless the tensor is already symmetric; you have to insert a metric (or its inverse) to move an index from up to down.

### 2.2  Write the product with explicit index contractions  

The matrix product \((X^{T}g)^{\mu}{}_{\nu}\) means

\[
(X^{T}g)^{\mu}{}_{\nu}= (X^{T})^{\mu}{}_{\rho}\,g^{\rho}{}_{\nu}\; ,
\]

or, equivalently (because the metric can be written with both indices down),

\[
(X^{T}g)^{\mu}{}_{\nu}= (X^{T})^{\mu\rho}\,g_{\rho\nu}.
\]

Both forms are correct; they are related by \(g^{\rho}{}_{\nu}=g^{\rho\lambda}g_{\lambda\nu}\).  
**The key point:** the index that is summed over (the *dummy* index) must appear **once up and once down** in each factor.  

### 2.3  Insert the definition of the transpose  

By definition of the transpose with respect to the metric,

\[
(X^{T})^{\mu}{}_{\rho}=X_{\rho}{}^{\mu}=g_{\rho\alpha}X^{\alpha\mu}\; .
\]

If we prefer the version with both indices up,

\[
(X^{T})^{\mu\rho}=X^{\rho\mu}=g^{\rho\alpha}X_{\alpha}{}^{\mu}.
\]

Both are legitimate; they just use different positions for the metric that performs the index‑raising/lowering.

### 2.4  Compute the product using the **first** convenient form  

Take  

\[
(X^{T}g)^{\mu}{}_{\nu}= (X^{T})^{\mu\rho}\,g_{\rho\nu}.
\]

Insert \((X^{T})^{\mu\rho}=X^{\rho\mu}\):

\[
\begin{aligned}
(X^{T}g)^{\mu}{}_{\nu}
      &= X^{\rho\mu}\,g_{\rho\nu}\\[2pt]
      &= \bigl(g^{\rho\alpha}X_{\alpha}{}^{\mu}\bigr) g_{\rho\nu}\\[2pt]
      &= X_{\alpha}{}^{\mu}\,\underbrace{g^{\rho\alpha}g_{\rho\nu}}_{\delta^{\alpha}{}_{\nu}}\\[2pt]
      &= X_{\nu}{}^{\mu}.
\end{aligned}
\]

**Result 1:**  

\[
\boxed{(X^{T}g)^{\mu}{}_{\nu}=X_{\nu}{}^{\mu}}.
\]

### 2.5  Compute the product using the **second** convenient form  

Now start from  

\[
(X^{T}g)^{\mu}{}_{\nu}= (X^{T})^{\mu}{}_{\rho}\,g^{\rho}{}_{\nu}.
\]

Insert the transpose with one index down:

\[
\begin{aligned}
(X^{T}g)^{\mu}{}_{\nu}
      &= X_{\rho}{}^{\mu}\,g^{\rho}{}_{\nu}\\[2pt]
      &= X_{\rho}{}^{\mu}\,g^{\rho\lambda}g_{\lambda\nu}\\[2pt]
      &= \underbrace{g^{\rho\lambda}X_{\rho}{}^{\mu}}_{X^{\lambda\mu}}\,g_{\lambda\nu}\\[2pt]
      &= X^{\lambda\mu}g_{\lambda\nu}\\[2pt]
      &= X_{\nu}{}^{\mu}.
\end{aligned}
\]

Again we obtain \(X_{\nu}{}^{\mu}\).  
The step where the student wrote  

\[
X^{\rho}{}_{\mu}\,\delta^{\rho}{}_{\nu}=X^{\rho}{}_{\mu}\,\delta^{\nu}{}_{\rho}=X^{\nu}{}_{\mu}
\]

is **illegal** because the Kronecker delta \(\delta^{\rho}{}_{\nu}\) can only be used to **replace the dummy index** \(\rho\) by \(\nu\) **when the index positions match** (upper‑to‑lower). Changing the order of the delta as \(\delta^{\nu}{}_{\rho}\) swaps the positions of the free indices, which is not allowed without an accompanying metric.

### 2.6  Where the student made the mistake  

Let us pinpoint the exact illegal step in the second chain:

\[
\begin{aligned}
(X^{T}g)^{\mu}{}_{\nu}
      &= (X^{T})^{\mu}{}_{\rho} g^{\rho}{}_{\nu}\\
      &= X^{\rho}{}_{\mu} g^{\rho}{}_{\nu}\quad\text{(transpose definition)}\\
      &= X^{\rho}{}_{\mu}\,\delta^{\rho}{}_{\nu}\qquad\text{(since }g^{\rho}{}_{\nu}= \delta^{\rho}{}_{\nu}\text{)}\\
      &= X^{\rho}{}_{\mu}\,\delta^{\nu}{}_{\rho}\quad\color{red}{\text{illegal}}\\
      &= X^{\nu}{}_{\mu}\; .
\end{aligned}
\]

The equality \(\delta^{\rho}{}_{\nu}= \delta^{\nu}{}_{\rho}\) **holds**, but you cannot then replace the *dummy* index \(\rho\) by the *free* index \(\nu\) **in the opposite position**. The dummy index must be eliminated **exactly** as it appears in the delta:

\[
X^{\rho}{}_{\mu}\,\delta^{\rho}{}_{\nu}=X^{\nu}{}_{\mu}\quad\text{(correct)}.
\]

If you rewrite the delta as \(\delta^{\nu}{}_{\rho}\), the summed index is now \(\rho\) **in the lower position**, so the contraction would give \(X^{\nu}{}_{\mu}\) **only if** the free index \(\nu\) were *lower*, i.e. \(X_{\nu\mu}\). Because the index positions are mismatched, the step is not allowed.  

In short: **Never move a free index from an upper to a lower (or vice‑versa) position without inserting the metric**. The Kronecker delta alone cannot change the variance of an index.

---

## 3.  Final answer  

Using the proper definition of the transpose and the rule that a dummy index must appear once up and once down in each factor, the product of the transpose of \(X\) with the metric is

\[
\boxed{(X^{T}g)^{\mu}{}_{\nu}=X_{\nu}{}^{\mu}} .
\]

Both of the student's expansion routes give the same result **provided** the index‑raising/lowering is performed correctly. The erroneous step was the replacement  

\[
X^{\rho}{}_{\mu}\,\delta^{\rho}{}_{\nu}\;\longrightarrow\; X^{\rho}{}_{\mu}\,\delta^{\nu}{}_{\rho},
\]

which swaps the position of the free index without a metric and therefore changes the variance of the index illegally.

---

## 4.  Common Mistakes in this type of problem  

| Mistake | Why it is wrong | How to avoid it |
|---------|----------------|-----------------|
| **Swapping the position of a free index inside a Kronecker delta** (e.g. \(\delta^{\rho}{}_{\nu}\to\delta^{\nu}{}_{\rho}\)) and then using it to replace the dummy index. | The delta only identifies *the same* index with the *same* variance. Changing its order changes the variance of the free index, which is not allowed. | Keep the delta exactly as it appears; perform the contraction directly: \(A^{\rho} \delta_{\rho}^{\ \nu}=A^{\nu}\). |
| **Treating raising/lowering as a mere “move” of the index** (writing \(X^{\mu\nu}=X^{\nu\mu}\) or \(X_{\mu}{}^{\nu}=X^{\nu}{}_{\mu}\)). | Raising/lowering requires the metric: \(X_{\mu}{}^{\nu}=g_{\mu\alpha}X^{\alpha\nu}\). Without the metric the equality is not guaranteed. | Whenever you need to change the position of an index, insert \(g_{\alpha\beta}\) or \(g^{\alpha\beta}\) explicitly. |
| **Using the metric as the identity matrix without checking index positions** (writing \(g^{\rho}{}_{\nu}= \delta^{\rho}{}_{\nu}\) and then treating the delta as if it had opposite variance). | The identity property holds only when the metric contracts a *raised* with a *lowered* index. | Remember: \(g^{\rho}{}_{\nu}= \delta^{\rho}{}_{\nu}\) **only** when the first index is up and the second is down. |
| **Confusing the transpose with the simple index swap** \((X^{T})^{\mu}{}_{\nu}=X^{\nu\mu}\). | The transpose is defined via the metric: \((X^{T})^{\mu}{}_{\nu}=X_{\nu}{}^{\mu}=g_{\nu\alpha}X^{\alpha\mu}\). | Write the definition of the transpose explicitly in terms of the metric before manipulating components. |
| **Leaving a dummy index appearing twice in the same position** (e.g. \(X^{\mu}{}_{\mu}\) without a sum). | Dummy indices must be summed; they cannot appear twice in the same variance position because the Einstein summation convention requires one up and one down. | Use distinct dummy letters, e.g. \(X^{\mu}{}_{\nu}\,g^{\nu\rho}\). |

By respecting these conventions, index gymnastics become reliable and free of contradictions.

*Original question: [Confusion about upper and lower indices](https://physics.stackexchange.com/questions/876551/confusion-about-upper-and-lower-indices) on Physics Stack Exchange, licensed CC BY-SA.*

{% endraw %}
