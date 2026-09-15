---
layout: question
title: How to formally show that the choice of a coordinate system in a physical system
  can be arbitrary?
author: StemFix Bot
category: physics
subject: physics
description: 'Step-by-step physics solution: How to formally show that the choice
  of a coordinate system in a physical system can be arbitrary?'
tags:
- physics
---

{% raw %}
*As an Amazon Associate, I earn from qualifying purchases.* For more practice problems like this, see [Schaum's Outline of College Physics, 12th Edition](https://www.amazon.com/dp/1259587398?tag=aiopentec20-20).

---

## 1.  What the question is really asking  

> *“Why does it not matter which coordinate system I use to describe a physical system?  How can we prove, in a clean and rigorous way, that the conclusions we draw (the equations of motion, measured quantities, etc.) are the same no matter what coordinates we pick?”*

In plain language the problem is asking for a **coordinate‑independent** (or *covariant*) formulation of physics and a proof that any two admissible coordinate charts give the same physical predictions.  
The proof must work for **arbitrary** smooth changes of coordinates – not only rotations, but translations, scalings, curvilinear maps, etc.

---

## 2.  Step‑by‑step proof  

The proof is most transparent in the language of **differential geometry**.  
We will treat a classical mechanical system; the same ideas carry over to field theory, relativity, and quantum mechanics.

### 2.1  The setting  

* Let \(\mathcal{M}\) be the **configuration space** of the system (e.g. \(\mathbb R^{3N}\) for \(N\) point particles).  
* A **coordinate chart** is a smooth bijection  

\[
\phi : U\subset\mathcal{M}\longrightarrow V\subset \mathbb R^{n},\qquad 
x =\phi(p)
\]

that assigns to each point \(p\in U\) an ordered \(n\)-tuple of numbers \(x^{i}\) (the coordinates).  
* Any other admissible chart \(\tilde\phi\) is related to \(\phi\) by a **smooth change of coordinates**

\[
\tilde{x}^{i}= \tilde{\phi}^{i}\bigl(\phi^{-1}(x)\bigr)\equiv f^{i}(x),\qquad 
\text{with } f:V\to\tilde V\text{ a diffeomorphism.}
\]

Thus the Jacobian matrix  

\[
J^{i}{}_{j}(x)=\frac{\partial \tilde{x}^{i}}{\partial x^{j}}
\]

is invertible everywhere on the overlap of the two charts.

### 2.2  Physical quantities are geometric objects  

The key physical principle is:

> **Principle of Coordinate Independence** –  *All measurable (or “real”) quantities are geometric objects on \(\mathcal{M}\) that do not depend on the choice of coordinates.*  

Geometric objects are precisely those that transform under a change of coordinates according to a **tensorial rule**.  
Examples:

| Geometric object | Coordinate components | Transformation rule |
|------------------|----------------------|----------------------|
| Scalar \(S\) | \(S(x)\) | \( \tilde S(\tilde x)=S(x) \) (no change) |
| Vector \(V\) | \(V^{i}(x)\) | \(\tilde V^{i}(\tilde x)=J^{i}{}_{j}(x)\,V^{j}(x)\) |
| Covector (1‑form) \(\alpha\) | \(\alpha_{i}(x)\) | \(\tilde\alpha_{i}(\tilde x)= (J^{-1})^{j}{}_{i} \,\alpha_{j}(x)\) |
| Rank‑\(k\) tensor \({T^{i_{1}\dots i_{p}}_{j_{1}\dots j_{q}}}\) | … | product of \(J\)’s and \((J^{-1})\)’s |

Anything that can be written **only with tensors** (contractions, sums, exterior derivatives, etc.) has the same value in any chart because the Jacobian factors cancel.

### 2.3  The action is a scalar  

In Lagrangian mechanics the dynamics is encoded in the **action functional**

\[
S[\gamma]=\int_{t_{1}}^{t_{2}} L\bigl(q(t),\dot q(t),t\bigr)\,dt .
\]

* \(q(t)\) are the coordinates of a path \(\gamma\) in \(\mathcal{M}\).  
* The Lagrangian \(L\) is required to be a **scalar function** on the tangent bundle \(T\mathcal{M}\times\mathbb R\).  

If we change coordinates \(q\to\tilde q=f(q)\) then  

\[
\dot{\tilde q}^{\,i}= \frac{d}{dt}\tilde q^{i}=J^{i}{}_{j}(q)\,\dot q^{j},
\]

and the new Lagrangian \(\tilde L\) is defined by  

\[
\tilde L(\tilde q,\dot{\tilde q},t)\equiv L\bigl(q,\dot q,t\bigr).
\]

Because \(L\) is a scalar, the numerical value of the integrand does **not** change:

\[
L\bigl(q,\dot q,t\bigr)=\tilde L\bigl(\tilde q,\dot{\tilde q},t\bigr).
\]

Hence the **action functional itself is invariant** under any smooth coordinate change.

### 2.4  Euler–Lagrange equations are covariant  

Varying the action in any chart gives the Euler–Lagrange equations

\[
\frac{d}{dt}\Bigl(\frac{\partial L}{\partial \dot q^{i}}\Bigr)-\frac{\partial L}{\partial q^{i}}=0 .
\]

Apply a coordinate transformation. Using the chain rule and the Jacobian relations above one finds

\[
\frac{d}{dt}\Bigl(\frac{\partial \tilde L}{\partial \dot{\tilde q}^{\,k}}\Bigr)-\frac{\partial \tilde L}{\partial \tilde q^{k}}
= J^{i}{}_{k}\Bigl[\frac{d}{dt}\Bigl(\frac{\partial L}{\partial \dot q^{i}}\Bigr)-\frac{\partial L}{\partial q^{i}}\Bigr] .
\]

Since the Jacobian matrix \(J^{i}{}_{k}\) is invertible, the set of equations in the new chart is *exactly equivalent* to the original set.  

Thus **the equations of motion are covariant**: a solution curve \(\gamma(t)\) expressed in coordinates \(q^{i}(t)\) satisfies the EL equations in the \(q\)-chart **iff** the transformed curve \(\tilde q^{k}(t)=f^{k}(q(t))\) satisfies the EL equations in the \(\tilde q\)-chart.

### 2.5  Observables are coordinate‑independent  

Physical observables are functions of the geometric state of the system:

* **Position of a particle** – the point \(p\in\mathcal{M}\) itself, not its coordinate numbers.  
* **Distance between two particles** – a scalar built from the metric tensor \(g\): \(d=\sqrt{g_{ij}\,\Delta q^{i}\Delta q^{j}}\).  
* **Energy** – \(E = \dot q^{i}p_{i} - L\) is a scalar because \(p_{i}=\partial L/\partial \dot q^{i}\) transforms as a covector.

Because each observable is a scalar (or a contraction of tensors), its numerical value is unchanged when we replace \(q\) by any \(\tilde q\).

### 2.6  General statement  

Let \(\phi\) and \(\tilde\phi\) be any two admissible coordinate charts on the part of configuration space where the motion occurs.  

1. **Geometric objects** (scalars, vectors, tensors, differential forms, etc.) have components that are related by the appropriate Jacobian factors.  
2. **Fundamental equations** (Newton’s law, Euler–Lagrange, Maxwell’s equations, Schrödinger equation written in covariant form) are *tensor equations*: each term is a tensor of the same type, so the whole equation is invariant under any smooth change of coordinates.  
3. **Solutions** of the equations map to each other by the coordinate transformation: if \(\gamma(t)\) solves the equations in one chart, then \(\tilde\gamma(t)=\tilde\phi\!\bigl(\phi^{-1}(\gamma(t))\bigr)\) solves them in the other.  
4. **Measured quantities** (numbers that an experiment can read) are scalars obtained by contracting tensors; therefore their values are identical in every chart.

Consequently **the choice of coordinate system is completely arbitrary**: it is a matter of convenience, not of physics.

---

## 3.  Final answer  

**The rigorous proof** consists of three logical steps:

1. **Identify physical quantities as geometric objects (tensors).**  
2. **Show that the fundamental action (or field functional) is a scalar, so it is unchanged by any smooth diffeomorphism of the coordinates.**  
3. **Derive the equations of motion from the invariant action; because they are tensor equations, they retain exactly the same form under any coordinate change, and solutions are carried into each other by the coordinate map.**  

Since all observable predictions are built from these tensors, the numerical outcomes are independent of the coordinate chart. Hence we may **choose any admissible coordinate system**—rotated, translated, curvilinear, or otherwise—and obtain the same physical conclusions.

---

## 4.  Common Mistakes  

| Mistake | Why it is wrong | How to avoid it |
|---------|----------------|-----------------|
| **Confusing “invariance under a specific symmetry” with “invariance under any coordinate change.”** | Rotational invariance is a symmetry of a particular *physical law*; coordinate invariance is a *general property* of the mathematical description. | Emphasise the tensor nature of quantities; a symmetry is a special case where the transformation also leaves the *form* of the law unchanged. |
| **Treating the coordinates themselves as physical objects.** | Coordinates are merely labels; only geometric objects (points, vectors, scalars) have physical meaning. | When you write an equation, check that each term is a tensor of the same type; if a term is just a list of numbers, it is not physical. |
| **Neglecting the Jacobian when transforming derivatives.** | Forgetting the factor \(J^{i}{}_{j}\) leads to apparent “extra terms” that look like a change in the physics. | Use the chain rule explicitly: \(\dot{\tilde q}^{\,i}=J^{i}{}_{j}\dot q^{j}\), and for second derivatives include the time derivative of the Jacobian. |
| **Assuming the Lagrangian must be unchanged point‑wise.** | The Lagrangian is a scalar *function*; its value at a point is the same, but its expression in new coordinates may look different. | Remember: \(L(q,\dot q)=\tilde L(\tilde q,\dot{\tilde q})\). The functional form may change, but the numerical value does not. |
| **Thinking that non‑linear coordinate changes break Newton’s law.** | Newton’s second law written as a vector equation is covariant; the components change, but the geometric equation \( \mathbf{F}=m\mathbf{a}\) stays true. | Write Newton’s law using vectors (or covariant derivatives) rather than component‑wise equations. |
| **Forgetting about the domain of the charts (overlap).** | Two charts might not cover the whole configuration space; invariance only needs to be shown on the overlap where both are defined. | State explicitly that the proof works on \(U\cap\tilde U\); extend by covering the whole space with a collection of overlapping charts. |

By keeping these points in mind, one can avoid the usual pitfalls and present a clean, mathematically rigorous argument that **the physics does not depend on the coordinate system we happen to use**.

*Original question: [How to formally show that the choice of a coordinate system in a physical system can be arbitrary?](https://physics.stackexchange.com/questions/876047/how-to-formally-show-that-the-choice-of-a-coordinate-system-in-a-physical-system) on Physics Stack Exchange, licensed CC BY-SA.*

{% endraw %}
