---
layout: question
title: Orthogonal projection of point/vector to an affine space
author: StemFix Bot
category: math
subject: math
description: 'Step-by-step mathematics solution: Orthogonal projection of point/vector
  to an affine space'
tags:
- math
---

{% raw %}
*As an Amazon Associate, I earn from qualifying purchases.* For more practice problems like this, see [Schaum's Outline of Calculus, 7th Edition](https://www.amazon.com/dp/126425833X?tag=aiopentec20-20).

---

## Orthogonal projection of a point onto an affine subspace  

### 1.  What the problem is asking (in plain language)

We are given  

* an **affine subspace**  

\[
L \;=\; x_{0}+U\subset\mathbb R^{n},
\]

  where  

  * \(x_{0}\in\mathbb R^{n}\) is a fixed point (the “origin” of the affine space), and  
  * \(U\) is a linear subspace (the **direction space**) of dimension \(k\le n\).

* a point (or a column vector) \(x\in\mathbb R^{n}\).

We want the **orthogonal projection** of \(x\) onto \(L\); that is, the point \(\pi_{L}(x)\in L\) that is **closest** to \(x\) in the Euclidean norm.  
Equivalently, the error vector  

\[
e:=x-\pi_{L}(x)
\]

must be orthogonal to the direction space \(U\):

\[
e\;\perp\;U\qquad\Longleftrightarrow\qquad
\langle e,u\rangle =0\;\;\forall\,u\in U .
\]

The question is: **How can we compute \(\pi_{L}(x)\) in a simple, general way?**  
We will give a formula that works in any basis, using only elementary linear‑algebraic operations.

---

### 2.  Step‑by‑step derivation  

#### 2.1  Choose a matrix that spans the direction space  

Let  

\[
A=\begin{bmatrix}a_{1}&a_{2}&\dots&a_{k}\end{bmatrix}\in\mathbb R^{n\times k}
\]

be a matrix whose columns \(\{a_{1},\dots ,a_{k}\}\) form a basis of \(U\).  
(If the basis is not orthonormal we do **not** need to orthogonalise it; the formula below works for any full‑rank \(A\).)

#### 2.2  Orthogonal projector onto the *linear* subspace \(U\)

The orthogonal projector \(P_{U}:\mathbb R^{n}\to U\) is the unique linear map satisfying  

* \(P_{U}^{2}=P_{U}\) (idempotent)  
* \(\operatorname{Im} P_{U}=U\)  
* \((I-P_{U})\) is orthogonal to \(U\).

When the columns of \(A\) span \(U\) and \(A\) has full column rank, the projector is

\[
\boxed{ \;P_{U}=A\,(A^{\!\top}A)^{-1}A^{\!\top}\; } \tag{1}
\]

*Proof sketch*: for any \(y\in\mathbb R^{n}\) we look for the vector \(u\in U\) that minimises \(\|y-u\|^{2}\).  
Write \(u=A\alpha\) with \(\alpha\in\mathbb R^{k}\).  
The minimiser solves the normal equations  

\[
A^{\!\top}(y-A\alpha)=0 \;\Longrightarrow\; A^{\!\top}A\;\alpha = A^{\!\top}y,
\]

so \(\alpha=(A^{\!\top}A)^{-1}A^{\!\top}y\) and \(u=A\alpha\).  
Hence \(P_{U}y = A(A^{\!\top}A)^{-1}A^{\!\top}y\).

If the columns of \(A\) are already orthonormal (\(A^{\!\top}A=I\)), then \(P_{U}=AA^{\!\top}\).

#### 2.3  From the linear projector to the affine projector  

Any point of the affine space \(L\) can be written as  

\[
x_{0}+u,\qquad u\in U.
\]

The distance from \(x\) to a generic point \(x_{0}+u\) is  

\[
\|x-(x_{0}+u)\|^{2}= \|(x-x_{0})-u\|^{2}.
\]

Thus the problem “project \(x\) onto \(L\)” is exactly the same as “project the vector \(x-x_{0}\) onto the *linear* subspace \(U\)”.  
Therefore  

\[
\boxed{ \;\pi_{L}(x)\;=\;x_{0}+P_{U}\bigl(x-x_{0}\bigr)\; } \tag{2}
\]

Substituting (1) for \(P_{U}\) gives an explicit matrix formula:

\[
\boxed{
\displaystyle 
\pi_{L}(x)=x_{0}+A\,(A^{\!\top}A)^{-1}A^{\!\top}\bigl(x-x_{0}\bigr)
}
\tag{3}
\]

This point lies in \(L\) (by construction) and satisfies  

\[
\bigl(x-\pi_{L}(x)\bigr)\;\perp\;U,
\]

so it is the unique **orthogonal (shortest‑distance) projection**.

#### 2.4  Verifying orthogonality  

Let \(e:=x-\pi_{L}(x)=\bigl(I-P_{U}\bigr)(x-x_{0})\).  
For any \(u\in U\) we can write \(u=A\beta\). Then

\[
\langle e,u\rangle
= \bigl[(I-P_{U})(x-x_{0})\bigr]^{\!\top}A\beta
= (x-x_{0})^{\!\top}(I-P_{U})A\beta .
\]

But \(P_{U}A=A\) (because columns of \(A\) are already in the image of \(P_{U}\)), so  

\[
(I-P_{U})A=0\quad\Longrightarrow\quad \langle e,u\rangle=0 .
\]

Hence \(e\) is orthogonal to every direction of \(U\).

#### 2.5  What if a different inner product is used?  

If the underlying inner product is \(\langle y,z\rangle = y^{\!\top}Gz\) with a symmetric positive‑definite matrix \(G\), replace the ordinary transpose by the \(G\)-transpose:

\[
P_{U}=A\,(A^{\!\top}GA)^{-1}A^{\!\top}G,
\]

and keep formula (2). The derivation is identical, only the normal equations become \(A^{\!\top}G A\,\alpha = A^{\!\top}G\,y\).

---

### 3.  Final answer  

Let  

* \(x_{0}\in\mathbb R^{n}\) be a point on the affine subspace,  
* \(A\in\mathbb R^{n\times k}\) (full column rank) whose columns span the direction space \(U\), and  
* \(x\in\mathbb R^{n}\) the point to be projected.

Then the orthogonal projection of \(x\) onto the affine subspace  

\[
L = x_{0}+U
\]

is

\[
\boxed{\displaystyle
\pi_{L}(x)=x_{0}+A\,(A^{\!\top}A)^{-1}A^{\!\top}\bigl(x-x_{0}\bigr)
}
\]

Equivalently, compute  

1. the **shifted vector** \(y = x-x_{0}\);  
2. the linear orthogonal projector onto \(U\) using (1): \(P_{U}=A(A^{\!\top}A)^{-1}A^{\!\top}\);  
3. the projected point \( \pi_{L}(x)=x_{0}+P_{U}y\).

The error vector \(x-\pi_{L}(x)\) is orthogonal to every direction in \(U\), guaranteeing that \(\pi_{L}(x)\) is the unique closest point of \(L\) to \(x\).

---

### 4.  Common mistakes  

| Mistake | Why it is wrong | How to avoid it |
|---------|----------------|-----------------|
| **Using the projector \(AA^{\!\top}\) when the columns of \(A\) are not orthonormal.** | \(AA^{\!\top}\) is only a projector when \(A^{\!\top}A=I\). Otherwise it does not satisfy \(P^{2}=P\). | Always form \(P_{U}=A(A^{\!\top}A)^{-1}A^{\!\top}\). If you prefer an orthonormal basis, first orthonormalise the columns (e.g., QR factorisation). |
| **Projecting directly onto \(L\) with \(P_{U}x\) and forgetting the shift \(x_{0}\).** | The affine space is not a linear subspace; the origin matters. | First translate: work with \(x-x_{0}\), project, then add back \(x_{0}\). |
| **Assuming the projection is linear in \(x\) for an affine space.** | The map \(x\mapsto\pi_{L}(x)\) is **affine**, not linear (because of the added \(x_{0}\)). | Remember the final formula has a constant term \(x_{0}\). |
| **Neglecting the invertibility of \(A^{\!\top}A\).** | If the columns of \(A\) are linearly dependent, \(A^{\!\top}A\) is singular and the formula breaks down. | Ensure \(A\) has full column rank (i.e., the chosen basis of \(U\) is indeed a basis). If not, first remove dependent columns. |
| **Using the wrong inner product.** | The orthogonality condition depends on the inner product; using the Euclidean formula with a weighted norm leads to errors. | If a non‑standard inner product \(\langle\cdot,\cdot\rangle_{G}\) is intended, replace the transpose by the \(G\)-transpose as noted in §2.5. |
| **Numerical instability when \(A^{\!\top}A\) is ill‑conditioned.** | Inverting a poorly conditioned matrix amplifies round‑off errors. | Use a numerically stable method: solve the normal equations with a Cholesky factorisation, or better, compute the QR factorisation of \(A\) and use \(P_{U}=Q Q^{\!\top}\). |

Keeping these points in mind will help you obtain the correct orthogonal projection onto any affine subspace.

*Original question: [Orthogonal projection of point/vector to an affine space](https://math.stackexchange.com/questions/5151533/orthogonal-projection-of-point-vector-to-an-affine-space) on Mathematics Stack Exchange, licensed CC BY-SA.*

{% endraw %}
