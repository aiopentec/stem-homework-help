---
layout: post
title: On the Constant Rank Theorem and the Frobenius Theorem for differential equations.
author: StemFix Bot
category: math
tags:
- math
render_with_liquid: false
---

*As an Amazon Associate, I earn from qualifying purchases.* For more practice problems like this, see [Schaum's Outline of Calculus, 7th Edition](https://www.amazon.com/dp/126425833X?tag=aiopentec20-20).

---

## 1.  What the question is asking (in plain language)

The asker wants to know whether two fundamental local‑existence results in differential geometry are *the same*:

* **Constant‑Rank Theorem (CRT).**  
  If a smooth map \(F : M\to N\) between manifolds has the same rank at every point of a neighbourhood, then there are local coordinates in which \(F\) looks like a projection
  \[
  (x^{1},\dots ,x^{m})\longmapsto (x^{1},\dots ,x^{r}),\qquad r=\operatorname{rank}F .
  \]

* **Frobenius Theorem (FT).**  
  If a smooth distribution \(\mathcal D\subset TM\) (i.e. a choice of a subspace \(\mathcal D_{p}\subset T_{p}M\) at each point) has constant dimension and is **involutive** (closed under Lie brackets), then through every point there is a submanifold whose tangent space equals \(\mathcal D\).  In coordinates the distribution can be written as the span of some coordinate vector fields.

The question is:  

*Does one theorem imply the other?  Are they equivalent?*  

We shall answer this by analysing the logical relationship and giving explicit reasons (and counter‑examples) for why the implication goes only one way.

--------------------------------------------------------------------

## 2.  Detailed analysis

### 2.1  From Constant‑Rank → Frobenius

1. **Kernel of a map.**  
   Let \(F:M\to N\) be a smooth map whose differential has constant rank \(r\) on an open set \(U\subset M\).  
   Define the distribution
   \[
   \mathcal D_{p}:=\ker dF_{p}\subset T_{p}M ,\qquad p\in U .
   \]

2. **Involutivity of the kernel.**  
   If \(X,Y\) are smooth vector fields with \(X_{p},Y_{p}\in\ker dF_{p}\) for every \(p\), then
   \[
   dF([X,Y]) = X(dF(Y)) - Y(dF(X)) = 0 .
   \]
   Hence \([X,Y]_{p}\in\ker dF_{p}\).  Thus the kernel distribution is **automatically involutive**.

3. **Application of Frobenius.**  
   The kernel distribution has constant dimension \(\dim M-\operatorname{rank}F\) (because the rank of \(dF\) is constant).  
   By the Frobenius theorem, through each point there is an \((\dim M-\operatorname{rank}F)\)-dimensional integral submanifold.

4. **Local coordinates from CRT.**  
   The constant‑rank theorem provides coordinates \((x^{1},\dots ,x^{m})\) on a neighbourhood \(U\) such that
   \[
   F(x)=\bigl(x^{1},\dots ,x^{r}\bigr) .
   \]
   In these coordinates the kernel distribution is simply
   \[
   \mathcal D=\operatorname{span}\Bigl\{\frac{\partial}{\partial x^{r+1}},\dots ,\frac{\partial}{\partial x^{m}}\Bigr\},
   \]
   i.e. the distribution described by the Frobenius theorem.  

**Conclusion.**  
Whenever we start with a *given* map of constant rank, the Frobenius theorem can be applied to its kernel.  Thus **CRT ⇒ FT (for the particular distribution that is the kernel of the map).**

---

### 2.2  From Frobenius → Constant‑Rank ?

Now suppose we are given an involutive distribution \(\mathcal D\) of constant dimension \(k\).  
The Frobenius theorem guarantees *locally* the existence of a submersion whose kernel equals \(\mathcal D\):

* There are neighbourhoods \(U\) and smooth functions  
  \[
  \phi=(\phi^{1},\dots ,\phi^{m-k}) : U\longrightarrow \mathbb R^{\,m-k}
  \]
  such that \(\ker d\phi = \mathcal D\) on \(U\).

However, **the Frobenius theorem does **not** give a *single* globally defined map of constant rank whose kernel is \(\mathcal D\).**  

#### Counter‑example showing FT does not imply CRT

Consider the **plane with a line removed**:

\[
M = \mathbb R^{2}\setminus\{(0,0)\},\qquad
\mathcal D_{(x,y)} = \operatorname{span}\{\,x\,\partial_{x}+y\,\partial_{y}\,\}.
\]

* The distribution is one‑dimensional and involutive (any two vector fields tangent to the radial direction have zero Lie bracket).
* By Frobenius, through each point there is an integral curve: the radial line through the origin.

Suppose a smooth map \(F:M\to \mathbb R\) existed with \(\ker dF = \mathcal D\).  
Because the integral curves are the rays, the level sets of \(F\) would have to be the **circles** centred at the origin.  Hence \(F\) would have to be a function of the radius \(r=\sqrt{x^{2}+y^{2}}\) only, say \(F = g(r)\).

But \(r\) is **not smooth at the origin**, and the origin is missing from \(M\).  More importantly, any smooth \(g\) would have **critical points** (where \(g'(r)=0\)), at which the differential \(dF\) drops rank from \(1\) to \(0\).  Consequently, no smooth map on the whole of \(M\) can have constant rank and kernel equal to \(\mathcal D\).

Thus we have an involutive distribution that satisfies the hypotheses of Frobenius, yet **there is no globally defined smooth map of constant rank whose kernel is that distribution**.  Hence **FT does not imply CRT**.

---

### 2.3  Summary of logical relations

| Direction | True? | Reason |
|-----------|-------|--------|
| **CRT ⇒ FT** (for the kernel distribution) | **Yes** | The kernel of a constant‑rank map is automatically involutive and of constant dimension, so Frobenius applies. |
| **FT ⇒ CRT** (as a statement about arbitrary involutive distributions) | **No** | Frobenius only guarantees *local* existence of a submersion; a globally defined constant‑rank map need not exist. Counter‑example: the radial distribution on \(\mathbb R^{2}\setminus\{0\}\). |

Therefore the two theorems are **not equivalent**: the constant‑rank theorem is a special case of the Frobenius theorem (applied to the kernel of a given map), while the Frobenius theorem is strictly more general.

--------------------------------------------------------------------

## 3.  Final answer

*The Constant Rank Theorem and the Frobenius Theorem are **not** equivalent.*

*   **Constant‑Rank ⇒ Frobenius** (for the kernel distribution) because the kernel of a constant‑rank differential is a regular, involutive distribution, and Frobenius guarantees integral manifolds for it.

*   **Frobenius ⇏ Constant‑Rank**.  An involutive distribution may fail to arise as the kernel of any smooth map of constant rank; the radial distribution on \(\mathbb R^{2}\setminus\{0\}\) is a concrete counter‑example.

Thus the Frobenius theorem strictly generalises the constant‑rank situation.

--------------------------------------------------------------------

## 4.  Common mistakes to avoid

| Mistake | Why it is wrong | How to avoid it |
|---------|----------------|-----------------|
| **Assuming any involutive distribution is the kernel of a given map.** | The Frobenius theorem only *produces* a local submersion; it does not guarantee a globally defined one, nor that the original problem supplied such a map. | Remember the statement of FT: *existence* of submanifolds, not existence of a pre‑existing map. |
| **Confusing “constant rank of a map” with “constant dimension of a distribution”.** | A distribution may have constant dimension without coming from a map, and a map may have constant rank but its kernel may be trivial (rank = 0) or full (rank = dim M). | Keep the two objects separate: a map \(F\) gives a distribution \(\ker dF\); a distribution need not be presented as a kernel. |
| **Thinking the constant‑rank theorem follows from Frobenius because both give local coordinates.** | The coordinate change supplied by CRT is *built from the given map*; the coordinates supplied by FT are *built from the distribution* and need not extend to a global map of constant rank. | Check the hypotheses: CRT requires a specific map with constant rank, FT requires involutivity. The presence of one hypothesis does not guarantee the other. |
| **Neglecting the involutivity condition.** | A distribution that is not involutive cannot be the kernel of any smooth map, even if it has constant dimension. | Verify \([X,Y]\in\mathcal D\) for generators \(X,Y\) when trying to relate a distribution to a kernel. |

Keeping these points in mind will prevent the most frequent conceptual errors when comparing the Constant Rank and Frobenius theorems.

*Original question: [On the Constant Rank Theorem and the Frobenius Theorem for differential equations.](https://math.stackexchange.com/questions/427172/on-the-constant-rank-theorem-and-the-frobenius-theorem-for-differential-equation) on Mathematics Stack Exchange, licensed CC BY-SA.*
