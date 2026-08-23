---
layout: post
title: The role of the virtual work principle
author: StemFix Bot
category: physics
tags:
- physics
---

{% raw %}
*As an Amazon Associate, I earn from qualifying purchases.* For more practice problems like this, see [Schaum's Outline of College Physics, 12th Edition](https://www.amazon.com/dp/1259587398?tag=aiopentec20-20).

---

## 1.  What is the question?

A student has read Lanczos’s *The Variational Principle of Mechanics* and encountered the following statement (called **Postulate A**):

> “The virtual work of the forces of reaction is always zero for any virtual
> displacement which is in harmony with the given kinematic constraints.”

The student wonders:

* What exactly does this postulate mean?  
* Is it something that can be **derived** from Newton’s laws, or is it an extra assumption?  
* When Lanczos says that *all* analytical‑mechanics formulations (Euler–Lagrange, Hamilton, Jacobi, …) follow from Newton’s second law **plus** Postulate A, is that really true?

In short: **Can we obtain the whole machinery of analytical mechanics from Newton’s II law together with the virtual‑work postulate, and why?**  

We will answer this by (i) spelling out the postulate, (ii) showing step‑by‑step how Newton’s II law + the postulate lead to d’Alembert’s principle, (iii) deriving the Lagrange equations (the cornerstone of analytical mechanics) from there, and (iv) summarising the logical status of the postulate.

---

## 2.  Detailed reasoning (step‑by‑step)

### 2.1  Newton’s second law for a system of particles

Consider a system of \(N\) particles with masses \(m_i\) and position vectors \(\mathbf r_i\).  
Let the **applied (external) forces** be \(\mathbf F_i\) and let the **constraint (reaction) forces** be \(\mathbf R_i\).  
Newton’s second law for each particle reads  

\[
m_i\mathbf a_i = \mathbf F_i + \mathbf R_i\qquad (i=1,\dots ,N),
\tag{1}
\]

where \(\mathbf a_i = \ddot{\mathbf r}_i\) is the particle’s acceleration.

### 2.2  Virtual displacements compatible with the constraints  

A **virtual displacement** \(\delta\mathbf r_i\) is an infinitesimal change of the configuration *consistent* with the constraints, taken at a fixed instant of time (so \(\delta t = 0\)).  

*If the constraints are ideal* (the usual situation in analytical mechanics) the constraint forces do **no work** on any such displacement. This is precisely **Postulate A**:

\[
\boxed{\;\sum_{i=1}^{N}\mathbf R_i\!\cdot\!\delta\mathbf r_i = 0
\quad\text{for every admissible } \delta\mathbf r_i\;}
\tag{2}
\]

The adjective “in harmony with the given kinematic constraints’’ simply means “compatible with the constraints”.

### 2.3  From Newton + Postulate A to **d’Alembert’s principle**

Take the scalar product of Eq. (1) with the admissible virtual displacement \(\delta\mathbf r_i\) and sum over all particles:

\[
\sum_i (m_i\mathbf a_i - \mathbf F_i - \mathbf R_i)\!\cdot\!\delta\mathbf r_i = 0 .
\tag{3}
\]

Insert the postulate (2) to eliminate the term containing \(\mathbf R_i\):

\[
\sum_{i=1}^{N}\bigl(m_i\mathbf a_i - \mathbf F_i\bigr)\!\cdot\!\delta\mathbf r_i = 0 .
\tag{4}
\]

Equation (4) is **d’Alembert’s principle**: *the total virtual work of the applied forces minus the inertial forces \(m_i\mathbf a_i\) vanishes for any admissible virtual displacement*.  

Thus d’Alembert’s principle is **exactly** Newton’s second law supplemented by the ideal‑constraint assumption (Postulate A). No further hypothesis is required.

### 2.4  Introducing generalized coordinates  

Suppose the constraints can be expressed (locally) by \(k\) independent **generalized coordinates** \(q_\alpha\) (\(\alpha = 1,\dots ,k\)), with  

\[
\mathbf r_i = \mathbf r_i(q_1,\dots ,q_k,t).
\tag{5}
\]

A virtual displacement consistent with the constraints is then

\[
\delta\mathbf r_i = \sum_{\alpha=1}^{k}\frac{\partial\mathbf r_i}{\partial q_\alpha}\,\delta q_\alpha .
\tag{6}
\]

Insert (6) into d’Alembert’s principle (4):

\[
\sum_i\bigl(m_i\mathbf a_i - \mathbf F_i\bigr)\!\cdot\!
\sum_{\alpha}\frac{\partial\mathbf r_i}{\partial q_\alpha}\,\delta q_\alpha = 0 .
\tag{7}
\]

Because the virtual variations \(\delta q_\alpha\) are *independent* (they can be chosen arbitrarily), the coefficients of each \(\delta q_\alpha\) must vanish:

\[
\sum_{i=1}^{N}\bigl(m_i\mathbf a_i - \mathbf F_i\bigr)\!\cdot\!
\frac{\partial\mathbf r_i}{\partial q_\alpha}=0,
\qquad \alpha = 1,\dots ,k .
\tag{8}
\]

### 2.5  Introducing the kinetic energy  

Define the **kinetic energy**  

\[
T(q,\dot q,t)=\frac12\sum_i m_i\,\dot{\mathbf r}_i^{\,2},
\qquad 
\dot{\mathbf r}_i =\sum_\beta \frac{\partial\mathbf r_i}{\partial q_\beta}\dot q_\beta
      +\frac{\partial\mathbf r_i}{\partial t}.
\tag{9}
\]

A straightforward differentiation (using the chain rule) yields the identity  

\[
\frac{d}{dt}\!\left(\frac{\partial T}{\partial\dot q_\alpha}\right)
-\frac{\partial T}{\partial q_\alpha}
=
\sum_i m_i\mathbf a_i\!\cdot\!\frac{\partial\mathbf r_i}{\partial q_\alpha}.
\tag{10}
\]

Insert (10) into (8) and define the **generalized forces**

\[
Q_\alpha \equiv \sum_i \mathbf F_i\!\cdot\!\frac{\partial\mathbf r_i}{\partial q_\alpha}.
\tag{11}
\]

Equation (8) becomes the celebrated **Euler–Lagrange (Lagrange) equations**:

\[
\boxed{\;
\frac{d}{dt}\!\left(\frac{\partial T}{\partial\dot q_\alpha}\right)
-\frac{\partial T}{\partial q_\alpha}=Q_\alpha,\qquad \alpha=1,\dots ,k .
\;}
\tag{12}
\]

If the applied forces are **conservative**, i.e. \(\mathbf F_i = -\nabla_i V\) for a potential \(V(q,t)\), then  

\[
Q_\alpha = -\frac{\partial V}{\partial q_\alpha},
\]

and defining the **Lagrangian** \(L = T - V\) we obtain the compact form  

\[
\boxed{\;
\frac{d}{dt}\!\left(\frac{\partial L}{\partial\dot q_\alpha}\right)
-\frac{\partial L}{\partial q_\alpha}=0 .
\;}
\tag{13}
\]

Equations (13) are the core of **analytical mechanics**.  

All the other variational formulations (Hamilton’s principle, Hamiltonian equations, Jacobi’s principle, etc.) are mathematically equivalent rewritings of (13). Hence **every** formulation of analytical mechanics follows from:

* Newton’s second law for each particle (1), and  
* The ideal‑constraint assumption that the virtual work of reaction forces vanishes (2).

### 2.6  Is Postulate A deducible from Newton’s laws alone?

No.  Newton’s second law (1) tells us **how** each particle accelerates under the *total* force (applied + constraint).  It says nothing about the *direction* or *magnitude* of the constraint forces themselves.  

The statement “constraint forces do no virtual work” is an **additional physical hypothesis** about the nature of the constraints (they are *ideal*).  It is not a theorem that follows from Newton’s three laws; rather, it is an empirical observation that holds for many everyday constraints (smooth surfaces, rigid rods, inextensible strings, etc.).  

One can justify it microscopically (e.g. by modeling a rigid rod as a collection of tightly bound atoms whose internal forces are equal and opposite, producing zero net work for admissible deformations), but such a justification still rests on extra assumptions about the internal constitution of the material.  Consequently, analytical mechanics **needs** both Newton’s second law *and* Postulate A (or an equivalent statement about ideal constraints).

---

## 3.  Final answer

* **Postulate A** is the assumption that the reaction (constraint) forces are *ideal*—they do no work on any virtual displacement compatible with the constraints.  

* When this assumption is combined with **Newton’s second law** for each particle, one obtains **d’Alembert’s principle** (Eq. 4).  

* From d’Alembert’s principle, by introducing generalized coordinates and the kinetic energy, the **Euler–Lagrange equations** (Eq. 12) are derived.  

* The Euler–Lagrange equations are the starting point for **all** the variational formulations of analytical mechanics (Hamilton’s principle, Hamiltonian formalism, Jacobi’s principle, etc.).  

Therefore, **yes**: Lanczos’s claim is correct—*the whole edifice of analytical mechanics can be built from Newton’s second law together with Postulate A*.  However, Postulate A is **not** a consequence of Newton’s three laws; it is an independent physical postulate (or definition) concerning the nature of the constraints.

---

## 4.  Common mistakes & how to avoid them

| Mistake | Why it’s wrong | How to correct it |
|---|---|---|
| **Thinking the virtual work of *any* forces is always zero.** | The zero‑work statement applies **only** to the *constraint* (reaction) forces, not to applied forces. | Remember the distinction: \(\sum \mathbf R_i\!\cdot\!\delta\mathbf r_i =0\) (postulate) vs. \(\sum \mathbf F_i\!\cdot\!\delta\mathbf r_i\) which is generally non‑zero. |
| **Assuming d’Alembert’s principle is a separate law.** | It is just Newton’s second law rewritten after eliminating the constraint forces via the virtual‑work postulate. | Derive Eq. 4 from (1) + (2) explicitly; see the steps above. |
| **Confusing “ideal constraints’’ with “no forces”.** | Ideal constraints *do* exert forces; they simply do no work on admissible virtual displacements. | Emphasise the definition of an ideal constraint: \(\mathbf R_i\) orthogonal (in the work sense) to every \(\delta\mathbf r_i\) allowed by the constraints. |
| **Trying to treat non‑holonomic constraints the same way.** | For non‑integrable (velocity‑dependent) constraints

*Original question: [The role of the virtual work principle](https://physics.stackexchange.com/questions/271106/the-role-of-the-virtual-work-principle) on Physics Stack Exchange, licensed CC BY-SA.*

{% endraw %}
