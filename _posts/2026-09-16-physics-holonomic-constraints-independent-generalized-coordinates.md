---
layout: question
title: Holonomic constraints, independent generalized coordinates
author: StemFix Bot
category: physics
subject: physics
description: 'Step-by-step physics solution: Holonomic constraints, independent generalized
  coordinates'
tags:
- physics
---

{% raw %}
*As an Amazon Associate, I earn from qualifying purchases.* For more practice problems like this, see [Schaum's Outline of College Physics, 12th Edition](https://www.amazon.com/dp/1259587398?tag=aiopentec20-20).

---

## 1.  What the statement means in plain language  

We have a collection of \(N\) point particles, each with three Cartesian coordinates.  
Altogether we start with a **configuration space**  

\[
\mathcal C=\mathbb R^{3N}\; .
\]

The particles are not completely free: they must satisfy \(p\) **holonomic constraints**

\[
g_{v}(\mathbf r_{1},\dots ,\mathbf r_{N},t)=0,\qquad v=1,\dots ,p .
\]

For a *fixed* instant \(t=t_{0}\) the constraints define a subset  

\[
M_{t_{0}}:=\Bigl\{ \mathbf r\in\mathbb R^{3N}\; \big|\; g_{v}(\mathbf r,t_{0})=0,\;v=1,\dots ,p\Bigr\}.
\]

The textbooks claim that the *current* shape of the system can be described by
\(3N-p\) numbers \(q^{1},\dots ,q^{3N-p}\) (the **generalised coordinates**) and that
these numbers are **independent**, i.e. there is **no** relation  

\[
F\bigl(q^{1},\dots ,q^{3N-p}\bigr)=0
\]

apart from the trivial one \(F\equiv 0\).

Our goal is to **prove** this claim rigorously.

---

## 2.  Assumptions (regularity of the constraints)

The proof works under the standard regularity hypothesis for holonomic constraints:

> **Regularity (independence) of the constraints** –  
> At every point \(\mathbf r\in M_{t_{0}}\) the Jacobian matrix  

\[
J(\mathbf r)=\Bigl[\;\partial_{r_{i}}g_{v}(\mathbf r,t_{0})\Bigr]_{\;v=1..p}^{\;i=1..3N}
\]

has full rank \(p\) (i.e. the rows are linearly independent).

This is exactly the condition that the constraints are *independent* and
*holonomic*; it guarantees that the constraints cut out a smooth submanifold
of the expected dimension.

---

## 3.  Step‑by‑step proof  

### 3.1  The constraint surface is a \((3N-p)\)-dimensional manifold  

Define  

\[
\mathbf g(\mathbf r)=\bigl(g_{1}(\mathbf r,t_{0}),\dots ,g_{p}(\mathbf r,t_{0})\bigr):
\mathbb R^{3N}\longrightarrow\mathbb R^{p}.
\]

Because each \(g_{v}\) is smooth, \(\mathbf g\) is a smooth map.
The regularity hypothesis says that \(\mathbf 0\in\mathbb R^{p}\) is a **regular value** of \(\mathbf g\) :

\[
\operatorname{rank}\, D\mathbf g(\mathbf r)=p \qquad\forall \mathbf r\in\mathbf g^{-1}(\mathbf 0)=M_{t_{0}} .
\]

The **Regular Value Theorem** (also called the pre‑image theorem) then tells us that  

\[
M_{t_{0}}=\mathbf g^{-1}(\mathbf 0)
\]

is an embedded submanifold of \(\mathbb R^{3N}\) whose dimension is  

\[
\dim M_{t_{0}}=3N-p .
\]

Thus the set of admissible configurations at the instant \(t_{0}\) is a smooth
\((3N-p)\)-dimensional manifold.

---

### 3.2  Existence of local coordinates on the manifold  

Pick an arbitrary point \(\mathbf r^{*}\in M_{t_{0}}\).
Because the Jacobian \(J(\mathbf r^{*})\) has rank \(p\), there exists a
\(p\times p\) sub‑determinant that is non‑zero.
Without loss of generality we may relabel the Cartesian coordinates so that the
sub‑determinant involves the last \(p\) coordinates
\((x^{3N-p+1},\dots ,x^{3N})\).  
(If the non‑zero minor involves a different set of coordinates we simply reorder
the list of coordinates; the physics is unchanged.)

Write the full coordinate vector as  

\[
\mathbf x=(x^{1},\dots ,x^{3N-p},\,x^{3N-p+1},\dots ,x^{3N}) .
\]

Now apply the **Implicit Function Theorem** to the equations  

\[
g_{v}(\mathbf x)=0,\qquad v=1,\dots ,p .
\]

Because the matrix  

\[
\Bigl[\partial_{x^{3N-p+k}}g_{v}(\mathbf r^{*})\Bigr]_{v,k=1}^{p}
\]

is invertible, the theorem guarantees that, in a neighbourhood \(U\) of
\(\mathbf r^{*}\), the last \(p\) coordinates can be expressed uniquely as smooth
functions of the first \(3N-p\) coordinates:

\[
x^{3N-p+k}=h_{k}\bigl(x^{1},\dots ,x^{3N-p}\bigr),\qquad k=1,\dots ,p .
\]

Consequently every point of \(M_{t_{0}}\cap U\) is uniquely determined by the
tuple  

\[
\mathbf q:=(q^{1},\dots ,q^{3N-p})\;:=\;(x^{1},\dots ,x^{3N-p}) .
\]

Define  

\[
\Phi:U\cap M_{t_{0}}\longrightarrow \mathbb R^{3N-p},\qquad
\Phi(\mathbf r)=\bigl(q^{1},\dots ,q^{3N-p}\bigr) .
\]

Because the inverse map  

\[
\Phi^{-1}(q^{1},\dots ,q^{3N-p})=
\bigl(q^{1},\dots ,q^{3N-p},\,
h_{1}(\mathbf q),\dots ,h_{p}(\mathbf q)\bigr)
\]

is also smooth, \(\Phi\) is a **diffeomorphism** between the neighbourhood
\(U\cap M_{t_{0}}\) and an open set \(V\subset\mathbb R^{3N-p}\).

Thus the numbers \(\mathbf q=(q^{1},\dots ,q^{3N-p})\) are legitimate **local
coordinates** on the constraint manifold.

---

### 3.3  Independence of the coordinates  

By definition of a coordinate system on a manifold, the coordinate functions
\(q^{i}:U\cap M_{t_{0}}\to\mathbb R\) have linearly independent differentials.
Indeed, the Jacobian matrix of the map \(\Phi\),

\[
\frac{\partial (q^{1},\dots ,q^{3N-p})}{\partial (x^{1},\dots ,x^{3N})}
=
\begin{pmatrix}
I_{3N-p} & 0
\end{pmatrix},
\]

has full rank \(3N-p\).  

Suppose there existed a non‑trivial smooth function \(F:\mathbb R^{3N-p}\to\mathbb R\)
such that  

\[
F\bigl(q^{1}(\mathbf r),\dots ,q^{3N-p}(\mathbf r)\bigr)=0
\quad\text{for every }\mathbf r\in U\cap M_{t_{0}} .
\]

Differentiating this identity gives  

\[
\sum_{i=1}^{3N-p}\frac{\partial F}{\partial q^{i}}( \mathbf q )\,
dq^{i}=0 .
\]

Because the differentials \(dq^{i}\) are linearly independent, each coefficient
must vanish:

\[
\frac{\partial F}{\partial q^{i}}(\mathbf q)=0,\qquad i=1,\dots ,3N-p .
\]

Hence the gradient of \(F\) is zero on the open set \(V=\Phi(U\cap M_{t_{0}})\).
A smooth function with vanishing gradient on a connected open set is constant,
and because \(F\) vanishes somewhere (take any point of \(V\)), that constant is
zero. Therefore \(F\equiv 0\).

Thus **no non‑trivial functional relation** among the \(q^{i}\) can hold locally.
The coordinates are independent in the sense required by the textbooks.

---

### 3.4  Global picture  

The argument above works at every point of the constraint surface.
Consequently the whole admissible configuration space  

\[
\mathcal Q:=\bigcup_{t}\;M_{t}
\]

is a smooth manifold of dimension \(3N-p\).  
A manifold is, by definition, covered by a collection of such local charts,
each providing a set of \(3N-p\) independent generalized coordinates.
If the constraints are simple (e.g. a single rigid body) a single global chart
exists; in general several overlapping charts may be needed, but the *number*
of independent coordinates never exceeds \(3N-p\).

---

## 4.  Final answer  

*Under the regularity (independence) assumption on the holonomic constraints,
the set of admissible configurations at any fixed time is a smooth
\((3N-p)\)-dimensional submanifold of \(\mathbb R^{3N}\).  
The implicit‑function theorem provides, in a neighbourhood of any admissible
configuration, a diffeomorphism onto an open subset of \(\mathbb R^{3N-p}\).  
The image coordinates \((q^{1},\dots ,q^{3N-p})\) are therefore **independent**
(their differentials are linearly independent, and no non‑trivial relation
\(F(q^{1},\dots ,q^{3N-p})=0\) can hold).  

Hence a system of \(3N\) particles subject to \(p\) independent holonomic
constraints can be described locally (and, after patching charts, globally) by
exactly \(3N-p\) independent generalized coordinates.*

---

## 5.  Common mistakes to avoid  

| Mistake | Why it is wrong | How to avoid it |
|---|---|---|
| **Assuming the constraints are independent without checking the Jacobian rank.** | If the Jacobian loses rank somewhere, the constraint surface may have a lower dimension or singular points, and the count \(3N-p\) fails. | Explicitly require \(\operatorname{rank} D\mathbf g = p\) at every point (regular value condition). |
| **Believing a *single* global set of \(q^{i}\) always exists.** | Some configuration manifolds (e.g. a sphere) cannot be covered by one chart; you need an atlas of overlapping charts. | State the result locally; mention that a global chart exists only for special topologies. |
| **Treating time as a coordinate and counting it among the \(3N\) variables.** | The constraints are *holonomic*: they involve only the spatial coordinates at a fixed time; time is an external parameter. | Fix a time \(t_{0}\) when applying the theorem; treat \(t\) separately. |
| **Confusing “no functional relation” with “no algebraic relation”.** | Independence must hold for *smooth* functions, not only polynomials. | Use the differential argument (linear independence of \(dq^{i}\)). |
| **Using the implicit function theorem without verifying the invertible sub‑matrix.** | The theorem requires a specific set of coordinates whose partial derivatives form an invertible matrix. | Reorder the Cartesian coordinates so that a non‑zero \(p\times p\) minor appears, then apply the theorem. |

Keeping these points in mind yields a clean and rigorous justification of the
textbook statement.

*Original question: [Holonomic constraints, independent generalized coordinates](https://physics.stackexchange.com/questions/876002/holonomic-constraints-independent-generalized-coordinates) on Physics Stack Exchange, licensed CC BY-SA.*

{% endraw %}
