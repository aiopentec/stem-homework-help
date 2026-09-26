---
layout: question
title: Where did Frames go in the geometric formulation of Newton&#39;s laws? (Schuller)
author: StemFix Bot
category: physics
subject: physics
description: 'Step-by-step physics solution: Where did Frames go in the geometric
  formulation of Newton&#39;s laws? (Schuller)'
tags:
- physics
---

{% raw %}
*As an Amazon Associate, I earn from qualifying purchases.* For more practice problems like this, see [Schaum's Outline of College Physics, 12th Edition](https://www.amazon.com/dp/1259587398?tag=aiopentec20-20).

---

## 1. What the question is really asking  

The student has learned Newton’s laws in the **usual textbook way**:  

* “A particle that is not acted on by a net force moves with constant velocity.”  
* The law is written in a particular **inertial reference frame** as  

\[
\mathbf F_{\text{net}} = m\frac{d^{2}\mathbf x}{dt^{2}}\;,
\qquad \mathbf F_{AB}= -\,\mathbf F_{BA}.
\]

In the **geometric (coordinate‑free) formulation** used by Schuller the laws are written as  

\[
\nabla_{\mathbf u}\mathbf u = \mathbf F,\qquad 
\mathbf F_{AB}= -\,\mathbf F_{BA},
\]

where \(\mathbf u\) is the particle’s 4‑velocity and \(\nabla\) is a covariant derivative on Newtonian (Galilean) space‑time.  
There is **no explicit mention of “inertial frames”**.  

> **Question:** *Where did the notion of reference frames (especially inertial frames) go in this geometric picture? How do we recover the usual textbook statements?*  

---

## 2. Step‑by‑step answer  

### 2.1  Newtonian (Galilean) space‑time as a geometric object  

1. **Manifold** \(\mathcal M\): a 4‑dimensional smooth manifold whose points are *events* \((t,\mathbf x)\).  

2. **Absolute time**: a closed 1‑form \(\tau\) (often written \(dt\)) that assigns a time value to each event. Its kernel \(\ker\tau\) consists of the three‑dimensional spatial directions.  

3. **Spatial metric** \(h\): a symmetric, positive‑definite bilinear form defined on \(\ker\tau\); it measures spatial distances but does **not** raise a time component.  

4. **Connection \(\nabla\)**: a torsion‑free affine connection satisfying  

   \[
   \nabla \tau =0,\qquad \nabla h =0.
   \]

   These two compatibility conditions encode the idea that **time is the same for all observers** and that **spatial distances are preserved by parallel transport**.

The quadruple \((\mathcal M,\tau,h,\nabla)\) is called **Galilean (Newtonian) space‑time**.

### 2.2  World‑lines, velocity and acceleration  

* A particle’s **world‑line** is a curve \(\gamma : \mathbb R \to \mathcal M\) with \(\tau(\dot\gamma)=1\); the parameter is the absolute time \(t\).  

* The **4‑velocity** is the tangent vector \(\mathbf u = \dot\gamma\).  

* The **covariant derivative along the curve** gives the (coordinate‑free) acceleration:  

  \[
  \mathbf a \equiv \nabla_{\mathbf u}\mathbf u .
  \]

In any coordinate system \((t,x^i)\) that respects the structure (\(\tau = dt\)), the components read  

\[
\bigl(\nabla_{\mathbf u}\mathbf u\bigr)^i = \frac{d^{2}x^{i}}{dt^{2}} + \Gamma^{i}{}_{jk}\frac{dx^{j}}{dt}\frac{dx^{k}}{dt} + 2\Gamma^{i}{}_{0j}\frac{dx^{j}}{dt} + \Gamma^{i}{}_{00},
\]

where indices \(0\) refer to the time coordinate.

### 2.3  **Free** particle ⇒ geodesic  

The geometric version of Newton’s first law is  

\[
\nabla_{\mathbf u}\mathbf u = 0 .
\tag{1}
\]

Equation (1) says *the acceleration vanishes with respect to the connection \(\nabla\)*; i.e. the world‑line is a **geodesic** of \(\nabla\).

### 2.4  Where are *inertial frames*?  

An **inertial frame** is simply a coordinate chart \((t,x^i)\) that makes the connection coefficients vanish:

\[
\Gamma^{\mu}{}_{\nu\rho}=0 .
\tag{2}
\]

Because \(\nabla\tau=0\) and \(\nabla h=0\), the condition (2) can be satisfied **globally** on a *flat* Galilean space‑time (the one used in Newtonian physics). The coordinates satisfying (2) are called **affine (Galilean) coordinates**.  

* In such a chart, (1) reduces to  

  \[
  \frac{d^{2}x^{i}}{dt^{2}} = 0 ,
  \]

  which is exactly the textbook statement “a free particle moves with constant velocity”.  

* Any other chart related to an affine chart by a **Galilean transformation**  

  \[
  t' = t + t_{0},\qquad
  \mathbf x' = \mathbf R\mathbf x + \mathbf v\,t + \mathbf a,
  \]

  also has \(\Gamma^{\mu}{}_{\nu\rho}=0\); thus *all Galilean transformations map inertial frames to inertial frames*.

Consequently, **the notion of an inertial frame has not disappeared**; it is encoded in the *choice of coordinates for which the affine connection looks trivial*. In the coordinate‑free language we simply *do not have to mention the frame* because the law is written directly in terms of geometric objects that are independent of any particular chart.

### 2.5  Adding forces  

When external forces act, the geometric law becomes  

\[
\nabla_{\mathbf u}\mathbf u = \frac{1}{m}\,\mathbf F .
\tag{3}
\]

* \(\mathbf F\) is a spatial vector field (i.e. \(\tau(\mathbf F)=0\)) defined along the world‑line.  

* In an inertial chart where \(\Gamma^{\mu}{}_{\nu\rho}=0\), (3) reads  

  \[
  m\frac{d^{2}x^{i}}{dt^{2}} = F^{i},
  \]

  which is the familiar Newton’s second law.

The **action‑reaction principle** remains untouched because it is a statement about the *force vectors themselves*:  

\[
\mathbf F_{AB} = -\,\mathbf F_{BA},
\]

which is a coordinate‑free equality and therefore holds in any frame.

### 2.6  Summary of the correspondence  

| Textbook formulation | Geometric formulation | How frames appear |
|----------------------|-----------------------|-------------------|
| Inertial frame → coordinates with no “fictitious” terms | Covariant derivative \(\nabla\) (torsion‑free, compatible) | Inertial frames are precisely the affine charts where \(\Gamma^{\mu}{}_{\nu\rho}=0\) |
| \(\displaystyle \frac{d^{2}\mathbf x}{dt^{2}} = 0\) for a free particle | \(\displaystyle \nabla_{\mathbf u}\mathbf u = 0\) | No explicit frame needed; the equation is valid in any chart; in inertial charts it reduces to the textbook form |
| \(m\mathbf a = \mathbf F\) | \(\displaystyle \nabla_{\mathbf u}\mathbf u = \frac{1}{m}\mathbf F\) | Same reduction as above |
| \(\mathbf F_{AB} = -\mathbf F_{BA}\) | Same equality of spatial vectors | Frame‑independent, so unchanged |

---

## 3. Final answer  

*In the geometric (coordinate‑free) formulation the reference‑frame language is hidden inside the affine connection \(\nabla\). An **inertial frame** is any coordinate system that makes the connection coefficients vanish; in such a frame the covariant‑derivative equation \(\nabla_{\mathbf u}\mathbf u = \mathbf F/m\) reduces exactly to the textbook Newtonian equations. Thus frames have not disappeared; they are simply encoded by the choice of coordinates that trivialise the connection.*  

---

## 4. Common mistakes when dealing with this topic  

| Mistake | Why it’s wrong | How to avoid it |
|---------|----------------|-----------------|
| **Thinking that “no frames appear → frames are unnecessary.”** | The geometric law is *frame‑independent*, but to recover the familiar \(d^{2}\mathbf x/dt^{2}\) you must choose an inertial chart. | Remember that any tensor equation holds in all frames; only when you write components do you need a frame. |
| **Assuming any coordinate system is inertial.** | Only those for which the Galilean connection coefficients vanish are inertial. Accelerating or rotating coordinates introduce extra terms (Coriolis, centrifugal). | Check the connection coefficients \(\Gamma^{\mu}{}_{\nu\rho}\); if they are non‑zero, the frame is non‑inertial. |
| **Confusing the Newtonian connection with the Levi‑Civita connection of a Lorentzian metric.** | Newtonian space‑time has a degenerate spatial metric and a separate absolute‑time 1‑form; its compatible connection is not the same as the relativistic one. | Keep the structure \((\tau,h,\nabla)\) in mind; the compatibility conditions are \(\nabla\tau=0,\ \nabla h=0\). |
| **Treating \(\mathbf F\) as a 4‑vector with a time component.** | In Galilean space‑time forces are spatial; the time component of \(\mathbf F\) is forced to be zero by \(\tau(\mathbf F)=0\). | Explicitly project forces onto \(\ker\tau\) or state “\(\mathbf F\) is spatial”. |
| **Dropping the torsion‑free condition on \(\nabla\).** | Torsion would introduce extra “force‑like” terms even for free particles, violating Newton’s first law. | Always require \(\nabla\) to be torsion‑free when modelling Newtonian mechanics. |

---

*Original question: [Where did Frames go in the geometric formulation of Newton&#39;s laws? (Schuller)](https://physics.stackexchange.com/questions/876401/where-did-frames-go-in-the-geometric-formulation-of-newtons-laws-schuller) on Physics Stack Exchange, licensed CC BY-SA.*

{% endraw %}
