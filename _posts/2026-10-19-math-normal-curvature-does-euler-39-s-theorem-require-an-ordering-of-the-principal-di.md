---
layout: question
title: 'Normal curvature: does Euler&#39;s theorem require an ordering of the principal
  directions/curvatures?'
author: StemFix Bot
category: math
subject: math
description: 'Step-by-step mathematics solution: Normal curvature: does Euler&#39;s
  theorem require an ordering of the principal directions/curvatures?'
tags:
- math
---

{% raw %}
*As an Amazon Associate, I earn from qualifying purchases.* For more practice problems like this, see [Schaum's Outline of Calculus, 7th Edition](https://www.amazon.com/dp/126425833X?tag=aiopentec20-20).

---

## 1.  What the question is asking (in plain language)

A surface \(M\subset\mathbb R^{3}\) has at each point \(p\)

* two **principal directions** \(\mathbf e_{1},\mathbf e_{2}\) (mutually orthogonal unit tangent vectors) and  
* the corresponding **principal curvatures** \(\kappa_{1},\kappa_{2}\) (the normal curvatures in those directions).

Euler’s theorem says that for any unit tangent vector \(u\) making an angle \(\theta\) with \(\mathbf e_{1}\),

\[
\kappa(u)=\kappa_{1}\cos^{2}\theta+\kappa_{2}\sin^{2}\theta .
\]

The student wonders:

* Must we label the direction with the *largest* curvature as \(\mathbf e_{1}\) (and thus call its curvature \(\kappa_{1}\))?  
* If we do not order them, does the formula still hold?  
* What does “largest” mean when one curvature is negative?

In short: **Is an ordering of the principal directions/curvatures required for Euler’s formula, or is it merely a convenient convention?**



## 2.  Detailed answer – step‑by‑step

### 2.1  Principal directions and the shape operator  

At a point \(p\) the **shape operator** (Weingarten map) is the linear map  

\[
S_p:T_{p}M\longrightarrow T_{p}M,\qquad S_p(v)=-\mathrm dN_{p}(v),
\]

where \(N\) is a chosen unit normal field.  
\(S_p\) is symmetric with respect to the first fundamental form, therefore it can be diagonalised:

\[
S_p(\mathbf e_{i})=\kappa_{i}\,\mathbf e_{i},\qquad i=1,2,
\]

where \(\{\mathbf e_{1},\mathbf e_{2}\}\) is an **orthonormal** basis of eigenvectors (the *principal directions*) and \(\kappa_{1},\kappa_{2}\) are the corresponding eigenvalues (the *principal curvatures*).

*The eigenvalues are just numbers; they can be positive, zero or negative.  No sign restriction is imposed.*

### 2.2  Normal curvature of an arbitrary direction  

Take any unit tangent vector \(u\in T_{p}M\).  Because \(\{\mathbf e_{1},\mathbf e_{2}\}\) is a basis we can write

\[
u=\cos\theta\,\mathbf e_{1}+\sin\theta\,\mathbf e_{2},
\qquad \text{with }\theta\in[0,2\pi).
\]

(The angle \(\theta\) is precisely the oriented angle from \(\mathbf e_{1}\) to \(u\).)

The **normal curvature** of the surface in the direction \(u\) is defined by

\[
\kappa(u)=\langle S_p(u),\,u\rangle .
\]

Insert the decomposition of \(u\):

\[
\begin{aligned}
S_p(u) &= S_p\bigl(\cos\theta\,\mathbf e_{1}+\sin\theta\,\mathbf e_{2}\bigr)
        = \cos\theta\,S_p(\mathbf e_{1})+\sin\theta\,S_p(\mathbf e_{2}) \\
        &= \cos\theta\,\kappa_{1}\mathbf e_{1}+\sin\theta\,\kappa_{2}\mathbf e_{2}.
\end{aligned}
\]

Now take the inner product with \(u\) (remember that \(\mathbf e_{1},\mathbf e_{2}\) are orthonormal):

\[
\begin{aligned}
\kappa(u) &=\big\langle\cos\theta\,\kappa_{1}\mathbf e_{1}+\sin\theta\,\kappa_{2}\mathbf e_{2},
            \; \cos\theta\,\mathbf e_{1}+\sin\theta\,\mathbf e_{2}\big\rangle   \\
          &=\kappa_{1}\cos^{2}\theta+\kappa_{2}\sin^{2}\theta .
\end{aligned}
\]

Thus **Euler’s formula** holds **for every orthonormal pair of principal directions**, no matter how we label them.

### 2.3  What happens if we interchange the labels?

Suppose we decide to call the eigenvector with curvature \(\kappa_{2}\) “\(\mathbf e_{1}\)” and the other “\(\mathbf e_{2}\)”.  
Then the decomposition of the same vector \(u\) becomes

\[
u = \cos\theta'\,\mathbf e_{1}^{\text{new}} + \sin\theta'\,\mathbf e_{2}^{\text{new}},
\]

where \(\theta' = \theta - \frac{\pi}{2}\) (the angle measured from the new \(\mathbf e_{1}\)).  

Applying the same computation gives

\[
\kappa(u)=\kappa_{2}\cos^{2}\theta' + \kappa_{1}\sin^{2}\theta',
\]

which is **exactly the same number**, because \(\cos^{2}\theta' = \sin^{2}\theta\) and \(\sin^{2}\theta' = \cos^{2}\theta\).  
Hence the formula is invariant under swapping the labels; the only thing that changes is the name of the angle \(\theta\).

### 2.4  Why many texts say “largest” and “smallest”

Because the shape operator has **two** eigenvalues, it is customary to order them for ease of reference:

\[
\kappa_{1}\ge \kappa_{2}.
\]

Here “largest” and “smallest” refer to the *numerical* ordering on the real line, **including the sign**.  
Examples:

* If \(\kappa_{1}=5,\;\kappa_{2}=-2\), then \(\kappa_{1}\) is the largest (5 > −2).  
* If \(\kappa_{1}=-1,\;\kappa_{2}=-4\), then the “largest” is \(-1\) (because \(-1>-4\)).  

Ordering is *purely conventional*; the geometry does not depend on which eigenvalue we call \(\kappa_{1}\).  One may also order by absolute value (\(|\kappa_{1}|\ge |\kappa_{2}|\)) if a problem specifically needs “principal curvature of greatest magnitude”, but that is a different convention that must be stated explicitly.

### 2.5  Summary of the answer to the original question  

*Euler’s theorem does **not** require us to label the principal direction with the numerically largest curvature as \(\mathbf e_{1}\).*  
Any orthonormal eigenbasis \(\{\mathbf e_{1},\mathbf e_{2}\}\) together with its eigenvalues \(\kappa_{1},\kappa_{2}\) satisfies

\[
\boxed{\;\kappa(u)=\kappa_{1}\cos^{2}\theta+\kappa_{2}\sin^{2}\theta\;},
\]

where \(\theta\) is the angle from the chosen \(\mathbf e_{1}\) to \(u\).  

If one wishes to adopt a standard naming, the usual convention is to order the eigenvalues so that \(\kappa_{1}\ge\kappa_{2}\).  “Largest” means *greater* in the usual order of real numbers, sign included.  This convention is only for bookkeeping; the formula itself is independent of it.

---

## 3.  Final answer

Euler’s formula holds for **any** orthonormal pair of principal directions, regardless of which one is called \(\mathbf e_{1}\) or \(\mathbf e_{2}\).  
The only requirement is that the curvature \(\kappa_{i}\) attached to \(\mathbf e_{i}\) is the corresponding eigenvalue of the shape operator.  

The common practice of naming \(\kappa_{1}\) the “largest” curvature simply means that we order the two eigenvalues so that \(\kappa_{1}\ge\kappa_{2}\) (numerically, sign included).  This ordering is a convenient convention, not a mathematical necessity for Euler’s theorem.

---

## 4.  Common mistakes

| Mistake | Why it’s wrong | How to avoid it |
|---|---|---|
| **Assuming Euler’s formula fails if \(\kappa_{1}<\kappa_{2}\).** | The derivation uses only the eigen‑pair relationship; the inequality is irrelevant. | Remember the proof: \(\kappa(u)=\langle S(u),u\rangle\). The result is symmetric in the two eigenvalues. |
| **Swapping \(\mathbf e_{1},\mathbf e_{2}\) but keeping the same \(\theta\).** | After swapping, the angle measured from the new \(\mathbf e_{1}\) changes (\(\theta'=\theta-\pi/2\)). | When you relabel the basis, also relabel the angle accordingly. |
| **Confusing “largest” with “largest in absolute value”.** | “Largest” in the usual statement means greater as a real number, not larger magnitude. | State explicitly which ordering you are using; if you need magnitude, write \(|\kappa_{1}|\ge |\kappa_{2}|\). |
| **Using a non‑orthonormal eigenbasis.** | The derivation uses \(\langle\mathbf e_{i},\mathbf e_{j}\rangle=\delta_{ij}\). | Always normalise eigenvectors to unit length before applying the formula. |
| **Ignoring sign of curvature.** | Principal curvatures can be negative; the formula works unchanged. | Keep the signs of \(\kappa_{1},\kappa_{2}\) in the computation; do not replace them by absolute values unless the problem explicitly asks for it. |

By keeping these points in mind, the correct application of Euler’s theorem becomes straightforward.

*Original question: [Normal curvature: does Euler&#39;s theorem require an ordering of the principal directions/curvatures?](https://math.stackexchange.com/questions/5152277/normal-curvature-does-eulers-theorem-require-an-ordering-of-the-principal-dire) on Mathematics Stack Exchange, licensed CC BY-SA.*

{% endraw %}
