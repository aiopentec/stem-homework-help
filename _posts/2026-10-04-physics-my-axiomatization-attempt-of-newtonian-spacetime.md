---
layout: question
title: My axiomatization attempt of Newtonian spacetime
author: StemFix Bot
category: physics
subject: physics
description: 'Step-by-step physics solution: My axiomatization attempt of Newtonian
  spacetime'
tags:
- physics
---

{% raw %}
*As an Amazon Associate, I earn from qualifying purchases.* For more practice problems like this, see [Schaum's Outline of College Physics, 12th Edition](https://www.amazon.com/dp/1259587398?tag=aiopentec20-20).

---

## 1.  What the question is asking (in plain language)

The student wants to **re‑formulate Newtonian space‑time** without introducing an absolute time function \(t:M\to\mathbb R\).  
Instead he proposes:

* a **unit vector field** \(X\) that points “into the future’’,
* a symmetric bilinear form \(g\) on the tangent bundle such that  

\[
g(Y,Y)=g(Y,X)^2\qquad\text{for every vector field }Y .
\]

He then shows (or tries to show) that this forces  

\[
g(Y,Z)=\omega(Y)\,\omega(Z),\qquad\omega:=g(X,\cdot ) .
\]

The problem is to **explain, step by step, why this construction cannot serve as a proper Newtonian space‑time structure** and what the correct axiomatization looks like (the one used by Schuller and the standard Newton‑Cartan formulation).

In short we have to:

1. Derive rigorously the consequence \(g=\omega\otimes\omega\) from the postulated property.
2. Show that such a \(g\) is **degenerate** (rank 1) and therefore cannot give a spatial metric.
3. Explain why the usual Newtonian axioms use a **clock 1‑form** \(dt\) and a **degenerate spatial metric** \(h\) rather than a unit vector field.
4. Summarise the correct set of axioms and why the student’s attempt fails.

---

## 2.  Detailed step‑by‑step solution  

### 2.1  From the “unit‑speed’’ condition to a rank‑1 bilinear form  

**Assumption (A).**  
There exists a smooth vector field \(X\) on \(M\) with  

\[
g(X,X)=1,
\]

and for **every** vector field \(Y\),

\[
\boxed{g(Y,Y)=g(Y,X)^2}. \tag{1}
\]

Define the 1‑form  

\[
\omega(Y):=g(Y,X)\qquad\text{(so } \omega = g(X,\cdot)\text{)}. \tag{2}
\]

We want to prove

\[
g(Y,Z)=\omega(Y)\,\omega(Z) \qquad\forall Y,Z . \tag{3}
\]

---

#### 2.1.1  Polarisation identity for a *quadratic* form

For any symmetric bilinear form \(g\) we have the polarisation identity

\[
2g(Y,Z)=g(Y+Z,Y+Z)-g(Y,Y)-g(Z,Z). \tag{4}
\]

This identity holds **without** any further hypothesis.

---

#### 2.1.2  Use the hypothesis (1) in the polarisation identity  

Insert (1) into (4):

\[
\begin{aligned}
2g(Y,Z)
&=g(Y+Z,Y+Z)-g(Y,Y)-g(Z,Z)\\[2mm]
&=\bigl[g(Y+Z,X)\bigr]^{2}
-\bigl[g(Y,X)\bigr]^{2}
-\bigl[g(Z,X)\bigr]^{2}.
\end{aligned}
\]

Because of the definition (2),

\[
g(Y+Z,X)=\omega(Y+Z)=\omega(Y)+\omega(Z) ,
\]

since \(\omega\) is linear (it is a 1‑form).  Hence

\[
\begin{aligned}
2g(Y,Z)
&=(\omega(Y)+\omega(Z))^{2}-\omega(Y)^{2}-\omega(Z)^{2}\\[2mm]
&=2\,\omega(Y)\,\omega(Z).
\end{aligned}
\]

Dividing by 2 yields exactly (3):

\[
\boxed{g(Y,Z)=\omega(Y)\,\omega(Z)} .
\]

Thus **the only symmetric bilinear form that satisfies (1) is the outer product of a single 1‑form with itself**.

---

### 2.2  Consequences of \(g=\omega\otimes\omega\)

1. **Rank and degeneracy.**  
   For any vector \(V\) that satisfies \(\omega(V)=0\) we have  

   \[
   g(V,\cdot)=\omega(V)\,\omega(\cdot)=0 .
   \]

   Hence the kernel of \(g\) is precisely  

   \[
   \ker g=\{V\in TM\mid \omega(V)=0\},
   \]

   a subbundle of codimension 1. Consequently \(\operatorname{rank} g=1\); the form is **highly degenerate** and cannot be used to measure spatial distances (which require a non‑degenerate metric on the three‑dimensional “space‑like’’ subspaces).

2. **No information about spatial geometry.**  
   In Newtonian physics we need a *spatial metric* that tells us how far apart two simultaneous events are.  
   The tensor \(\omega\otimes\omega\) only measures the component **along** the distinguished direction \(X\) (the “time direction’’).  It says nothing about the geometry **orthogonal** to \(X\).

3. **Incompatibility with a generic force density.**  
   Newton’s second law in the Newton‑Cartan formulation reads  

   \[
   \nabla_{\dot\gamma}\dot\gamma = \frac{1}{m}F ,
   \qquad \text{with } dt(F)=0 .
   \]

   The condition \(dt(F)=0\) means the force is *spatial*: it lives in \(\ker dt\).  
   In the student’s set‑up we have only \(\omega\), no separate “spatial’’ subbundle, so we cannot express the requirement “force has no time component’’ in a coordinate‑free way.

---

### 2.3  Why the standard Newton–Cartan axioms are different  

| Feature | Student’s attempt | Standard Newton–Cartan (Schuller) |
|---|---|---|
| **Temporal structure** | A unit vector field \(X\) (norm 1 w.r.t. \(g\)) | A **clock 1‑form** \(\tau\) (or \(dt\)) with \(\tau\neq0\) everywhere |
| **Metric** | \(g=\omega\otimes\omega\) (rank 1, degenerate) | Two independent objects: <br> • \(\tau\) (temporal 1‑form) <br> • \(h\) (spatial metric) of rank 3, defined on \(\ker\tau\) |
| **Compatibility** | Implicit: \(\nabla\tau=0\) would force \(\nabla X=0\) (very restrictive) | Explicit: \(\nabla\tau=0\) and \(\nabla h=0\) (torsion‑free) give the **Galilean connection** |
| **Physical meaning** | “unit speed into the future’’ is forced, but spatial distances cannot be defined | \(\tau\) tells *how much time passes* between events; \(h\) tells *how far apart* simultaneous events are. |
| **Force condition** | Not expressible | \(dt(F)=0\) (force lives in \(\ker dt\)) |

The **key point** is that in Newtonian physics **time and space are independent**: you have a *one‑form* that selects a preferred foliation (the absolute time slices) and a *spatial metric* on each leaf of the foliation. Trying to encode both pieces of data in a single vector field and a degenerate bilinear form inevitably loses the spatial metric.

---

### 2.4  The correct set of axioms (concise version)

1. **Absolute time**: a nowhere‑vanishing 1‑form \(\tau\) (often written \(dt\)) with \(\tau\wedge d\tau=0\) (so the kernel integrates to a foliation by three‑dimensional slices).

2. **Spatial metric**: a symmetric, positive‑definite tensor \(h\) of rank 3 defined on \(\ker\tau\) (i.e. \(h(\tau,\cdot)=0\)).  

3. **Galilean connection** \(\nabla\): a torsion‑free affine connection satisfying  

   \[
   \nabla\tau =0,\qquad \nabla h =0 .
   \]

4. **Newton’s second law** for a test particle of mass \(m\):  

   \[
   \nabla_{\dot\gamma}\dot\gamma = \frac{1}{m}F ,\qquad \tau(F)=0 .
   \]

These axioms reproduce the familiar Newtonian physics and avoid the pitfalls of the attempted “unit‑vector‑field’’ construction.

---

## 3.  Final answer (summary)

* From the postulated condition \(g(Y,Y)=g(Y,X)^2\) one **must** have  

  \[
  g = \omega\otimes\omega,\qquad \omega:=g(X,\cdot).
  \]

* This tensor is **rank‑1 and degenerate**; it can only measure the component of a vector along the distinguished direction \(X\). It provides **no spatial metric** on the three‑dimensional slices orthogonal to \(X\).

* Consequently the student’s formulation cannot encode Newtonian physics, because Newtonian spacetime requires **both** a temporal 1‑form (absolute time) **and** a non‑degenerate spatial metric on the simultaneity slices.

* The standard Newton‑Cartan (or Schuller) axiomatization uses a **clock 1‑form** \(\tau\) and a **spatial metric** \(h\) together with a torsion‑free connection preserving both. This correctly separates time from space and allows a well‑defined notion of spatial distances and forces orthogonal to the time direction.

Hence, the attempt to replace absolute time by a unit vector field together with a bilinear form satisfying \(g(Y,Y)=g(Y,X)^2\) leads inevitably to a degenerate metric that cannot serve as the spatial geometry of Newtonian spacetime; the correct axioms must keep a separate time 1‑form and a spatial metric.

---

## 4.  Common mistakes in this type of problem  

| Mistake | Why it’s wrong | How to avoid it |
|---|---|---|
| **Treating \(\omega\) as a metric** | A metric must be non‑degenerate; \(\omega\otimes\omega\) has a whole 3‑dimensional kernel. | Always check the rank of the bilinear form; a genuine spatial metric must be invertible on the spatial subbundle. |
| **Assuming \(g(Y+Z,X)=g(Y,X)+g(Z,X)\) without justification** | This uses linearity of the *1‑form* \(\omega\), which follows only after you have defined \(\omega=g(X,\cdot)\). | Define \(\omega\) first and verify its linearity (it is a covector). |
| **Confusing a unit *vector* field with a unit *covector* field** | In Newtonian spacetime the “clock’’ is a covector (1‑form) \(dt\), not a vector; a vector field cannot encode the foliation uniquely. | Remember that a foliation is defined by the kernel of a 1‑form, not by a vector field. |
| **Forgetting the force orthogonality condition** | Newton’s second law requires the force to be spatial (\(dt(F)=0\)). Without a separate time 1‑form this condition cannot be expressed. | Keep a distinct \(\tau\) (or \(dt\)) and impose \(\tau(F)=0\). |
| **Believing that any torsion‑free connection preserving a degenerate metric is “the” Newtonian connection** | There are many connections preserving a rank‑1 form; Newtonian physics imposes *additional* conditions (preserving the spatial metric, curvature constraints). | Use the full set of compatibility conditions \(\nabla\tau=0,\ \nabla h=0\) and the curvature conditions of Newton–Cartan theory. |

---

*Original question: [My axiomatization attempt of Newtonian spacetime](https://physics.stackexchange.com/questions/876422/my-axiomatization-attempt-of-newtonian-spacetime) on Physics Stack Exchange, licensed CC BY-SA.*

{% endraw %}
