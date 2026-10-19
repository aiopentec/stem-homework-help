---
layout: question
title: What is the physical meaning of raising the index of a force covector?
author: StemFix Bot
category: physics
subject: physics
description: 'Step-by-step physics solution: What is the physical meaning of raising
  the index of a force covector?'
tags:
- physics
---

{% raw %}
*As an Amazon Associate, I earn from qualifying purchases.* For more practice problems like this, see [Schaum's Outline of College Physics, 12th Edition](https://www.amazon.com/dp/1259587398?tag=aiopentec20-20).

---

## 1.  What the question is asking – in plain language  

In Lagrangian (geometric) mechanics a **force** is first introduced as a *covector* (a 1‑form)  

\[
F = F_i\,dx^i ,
\]

which tells us how much *work* is done when the system makes an infinitesimal displacement  
\(\mathbf v = v^i\partial_i\):  

\[
\delta W = F(\mathbf v)=F_i v^i .
\]

Because the equations of motion we normally write are  

\[
\mathbf F = m\mathbf a ,
\]

we also need a *vector* that points in the direction of the acceleration.  
The usual way to obtain a vector from the covector is to **raise the index** with a metric \(g\):

\[
F^{i}=g^{ij}F_{j}.
\]

In Cartesian coordinates the components of the covector and of the raised vector happen to be the same numbers, so the distinction looks irrelevant. In a curvilinear coordinate system (e.g. polar coordinates) they are different.  

**The student asks:**  

*What does the metric actually do when it turns the covector \(F_i\) into the vector \(F^{i}\)?  In other words, what physical information is added by the metric, and why do the two sets of components differ?*  

---

## 2.  Detailed answer – step by step  

### 2.1  Vectors vs. covectors on a configuration manifold  

* The **configuration space** \(\mathcal Q\) of a mechanical system is a smooth manifold whose points are the possible positions of the system (e.g. \(\mathbb R^3\) for a particle, or a space of angles for a rigid body).  
* At each point \(q\in\mathcal Q\) we have a **tangent space** \(T_q\mathcal Q\) – the space of possible velocity vectors \(\dot q\).  
* The **cotangent space** \(T_q^{*}\mathcal Q\) consists of linear maps on \(T_q\mathcal Q\).  A covector \(\alpha\in T_q^{*}\mathcal Q\) assigns a number \(\alpha(v)\) to every tangent vector \(v\).  

A **force** that tells us how much work is done by a virtual displacement \(\delta q\) is naturally a covector:  

\[
\delta W = \underbrace{F_q}_{\in T_q^{*}\mathcal Q}(\delta q).
\]

A **mass‑times‑acceleration** term that appears in Newton’s second law lives in the tangent space:  

\[
m\,a_q \in T_q\mathcal Q .
\]

Thus the two objects belong to *different* spaces.  To set them equal we must **identify** the tangent and cotangent spaces.

### 2.2  The metric as the identification map  

A (Riemannian) **metric** is a smooth, symmetric, positive‑definite bilinear form  

\[
g_q : T_q\mathcal Q \times T_q\mathcal Q \longrightarrow \mathbb R .
\]

Because it is non‑degenerate we can use it to turn a covector into a vector and vice‑versa:

* For any covector \(\alpha\) define the **musical isomorphism** (the “flat” map)

\[
\alpha^\sharp \;:\; T_q\mathcal Q \longrightarrow \mathbb R,\qquad 
\alpha^\sharp(v) = g_q^{-1}(\alpha, v) .
\]

In components this is exactly the raising of an index:

\[
\alpha^\sharp = \alpha^{i}\,\partial_i,\qquad 
\alpha^{i}=g^{ij}\alpha_j .
\]

* Conversely the “flat” map \((\cdot)^\flat\) lowers an index:  

\[
v^\flat = g_{ij} v^j\,dx^i .
\]

Hence the **metric supplies the rule that tells us which vector corresponds to a given covector**.  Without a metric there is no canonical way to compare a work‑producing 1‑form with a mass‑times‑acceleration vector.

### 2.3  Physical meaning of the metric in Newtonian mechanics  

In ordinary Newtonian mechanics the configuration space is equipped with the **kinetic‑energy metric**  

\[
g_{ij}(q)=\sum_{\alpha=1}^{N} m_\alpha\,
\frac{\partial \mathbf r_\alpha}{\partial q^i}\!\cdot\!
\frac{\partial \mathbf r_\alpha}{\partial q^j},
\]

where \(\mathbf r_\alpha(q)\) is the Cartesian position of the \(\alpha\)-th particle expressed as a function of the generalized coordinates \(q^i\).  

* **What does this metric contain?**  
  * The **masses** \(m_\alpha\) – it encodes the inertia of each particle.  
  * The **geometry of the coordinate transformation** – the factors \(\partial \mathbf r_\alpha/\partial q^i\) describe how a small change in a generalized coordinate translates into a displacement in ordinary space.  

Therefore the metric tells us *how a virtual displacement in the abstract coordinate space is measured in ordinary Euclidean space* and *how the kinetic energy \(T=\tfrac12 g_{ij}\dot q^i\dot q^j\) is built from those velocities*.  

### 2.4  Why the components differ in curvilinear coordinates  

Consider a simple planar particle of mass \(m\) described in polar coordinates \((r,\theta)\).  

* The Euclidean metric in these coordinates is  

\[
g_{ij}=\begin{pmatrix}
1 & 0\\
0 & r^{2}
\end{pmatrix},\qquad 
g^{ij}=\begin{pmatrix}
1 & 0\\
0 & \dfrac{1}{r^{2}}
\end{pmatrix}.
\]

* Suppose the particle is acted on by a *central* force that does only radial work, i.e. the 1‑form  

\[
F = F_r\,dr \quad\text{with}\quad F_r = -k\,r .
\]

The covector components are \(F_r=-kr\), \(F_\theta =0\).  

* Raising the index gives  

\[
F^{r}=g^{rr}F_r = (-kr),\qquad 
F^{\theta}=g^{\theta\theta}F_\theta = \frac{1}{r^{2}}\cdot 0 =0 .
\]

Here the numerical values happen to be the same because the metric is diagonal with unit entry in the radial direction.  

Now consider a **force that does work in the angular direction**, e.g. a torque \(\tau\) that produces a 1‑form  

\[
F = \tau\,d\theta .
\]

Covector components: \(F_r =0\), \(F_\theta =\tau\).  

Raise the index:

\[
F^{r}=0,\qquad 
F^{\theta}=g^{\theta\theta}F_\theta =\frac{\tau}{r^{2}} .
\]

The vector component \(F^{\theta}\) is **not** equal to the covector component \(\tau\); it is divided by \(r^{2}\).  Physically this is exactly what Newton’s second law predicts for a particle moving on a circle:

\[
m\,a_\theta = m\,r\,\ddot\theta = F^{\theta}
\quad\Longrightarrow\quad
m\,r^{2}\,\ddot\theta = \tau .
\]

The factor \(r^{2}\) is the *moment of inertia* \(I=m r^{2}\).  The metric has supplied precisely this inertial factor, turning the *torque* (a covector that measures work per unit angular displacement) into the *angular component of the force vector* that must equal \(m\,a\).

Thus **the metric encodes the inertia associated with each coordinate direction**.  When the coordinate basis vectors are not orthonormal (as in polar, spherical, or any curvilinear system), the same physical force appears with different numerical components in the covector and vector pictures because the basis vectors have different lengths.

### 2.5  Summary of the physical picture  

| Object | Geometric nature | What it acts on | Physical meaning |
|--------|------------------|-----------------|------------------|
| **Force covector** \(F = F_i\,dx^i\) | 1‑form, lives in \(T_q^{*}\mathcal Q\) | Virtual displacement \(\delta q^i\) | Gives the *infinitesimal work* \(\delta W = F_i\delta q^i\). |
| **Metric** \(g_{ij}\) | Bilinear form on \(T_q\mathcal Q\) | Converts a vector into a covector and vice‑versa | Encodes *inertial properties* (masses, moments of inertia) and the *shape* of the coordinate basis. |
| **Force vector** \(F^{i}=g^{ij}F_j\) | Tangent vector, lives in \(T_q\mathcal Q\) | Acceleration \(a^i\) | Enters Newton’s law \(F^{i}=m a^{i}\). |

The **physical information added by the metric** is therefore the *mass distribution* (or more generally the kinetic‑energy tensor) that tells us how a given amount of work translates into an acceleration in each coordinate direction.  In Cartesian coordinates the basis vectors are orthonormal and the metric is the identity, so raising or lowering an index does nothing numerically.  In any other coordinate system the basis vectors are stretched or compressed, and the metric compensates by scaling the components appropriately.

---

## 3.  Final answer  

*Raising the index of a force covector with the metric does not change the underlying physical force; it merely expresses the same object in the tangent space instead of the cotangent space.  The metric supplies the **inertial conversion factor** that relates work per unit virtual displacement (a covector) to mass‑times‑acceleration (a vector).  In curvilinear coordinates the basis vectors have different lengths, so the numerical components of the covector and of the raised vector differ by the metric components (e.g. factors of \(r\) or \(r^{2}\) in polar/spherical coordinates).  These factors are precisely the moments of inertia that appear in Newton’s second law, showing that the metric encodes the system’s mass distribution and the geometry of the chosen coordinates.*  

---

## 4.  Common mistakes  

| Mistake | Why it’s wrong | How to avoid it |
|---------|----------------|-----------------|
| **Thinking the metric is “just a coordinate change”.** | The metric is *not* a change of coordinates; it is an additional structure that relates vectors and covectors. A coordinate transformation alone does not turn a 1‑form into a vector. | Remember the two distinct spaces (tangent vs. cotangent) and that the metric provides an *isomorphism* between them. |
| **Equating \(F_i\) with the physical component of the force.** | \(F_i\) are components of a covector, which give work for a displacement; the physical *force vector* that appears in \(\mathbf F = m\mathbf a\) is \(F^{i}=g^{ij}F_j\). | Explicitly write the work expression \(\delta W = F_i\delta q^i\) and the Newton expression \(F^{i}=m a^{i}\); note they involve different objects. |
| **Ignoring the mass matrix in generalized coordinates.** | In many mechanical systems the metric \(g_{ij}\) contains the masses (e.g. \(g_{ij}=m\delta_{ij}\) in Cartesian, \(g_{ij}=m\,r^{2}\) for angular coordinates). Dropping it leads to wrong equations of motion. | When working in non‑Cartesian coordinates, always compute the kinetic‑energy metric from the definition \(T=\frac12 g_{ij}\dot q^i\dot q^j\). |
| **Assuming \(F^{i}=F_i\) because the space is Euclidean.** | Euclidean space *as a manifold* still has a non‑trivial metric in curvilinear coordinates; the Euclidean metric expressed in those coordinates is not the identity matrix. | Write the metric explicitly in the chosen coordinates (e.g. polar, spherical) and verify that \(g^{ij}\neq\delta^{ij}\). |
| **Confusing “raising an index” with “taking a derivative”.** | Raising an index is an algebraic operation using the metric; taking a derivative involves the connection (Christoffel symbols). | Keep the two operations distinct: index raising = multiplication by \(g^{ij}\); covariant differentiation = \(\nabla_k\). |

By keeping these points in mind, the distinction between force as a covector and as a vector, and the role of the metric, become clear.

*Original question: [What is the physical meaning of raising the index of a force covector?](https://physics.stackexchange.com/questions/877053/what-is-the-physical-meaning-of-raising-the-index-of-a-force-covector) on Physics Stack Exchange, licensed CC BY-SA.*

{% endraw %}
