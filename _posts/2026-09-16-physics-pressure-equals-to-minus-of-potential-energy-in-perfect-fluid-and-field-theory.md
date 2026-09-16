---
layout: question
title: Pressure equals to minus of Potential energy in perfect fluid (and field theory)
author: StemFix Bot
category: physics
subject: physics
description: 'Step-by-step physics solution: Pressure equals to minus of Potential
  energy in perfect fluid (and field theory)'
tags:
- physics
---

{% raw %}
*As an Amazon Associate, I earn from qualifying purchases.* For more practice problems like this, see [Schaum's Outline of College Physics, 12th Edition](https://www.amazon.com/dp/1259587398?tag=aiopentec20-20).

---

## 1. What the question is asking (in plain language)

In many papers on cosmological first‑order phase transitions the **energy–momentum tensor** of the early Universe is written as the perfect‑fluid form  

\[
T^{\mu\nu}= (\rho+p)u^{\mu}u^{\nu}-g^{\mu\nu}p ,
\]

and the **pressure** is identified with the **negative of the effective (free‑energy) potential** of a scalar field that drives the transition,

\[
p =-\,V_{\rm eff}(\phi) .
\]

The student wants to re‑derive this relation **directly from the field‑theoretic definition**  

\[
T^{\mu\nu}= (\partial^{\mu}\phi)\,\frac{\partial\mathcal L}{\partial(\partial_{\nu}\phi)}-g^{\mu\nu}\mathcal L ,
\]

for the simple Lagrangian  

\[
\mathcal L=\tfrac12(\partial_{\mu}\phi)(\partial^{\mu}\phi)-V(\phi) .
\]

He/she assumes  

1. the scalar field itself constitutes the fluid,
2. the field is homogeneous (no spatial gradients), and
3. by going to the fluid rest frame the field can be taken as static (\(\dot\phi=0\)).

With these assumptions he/she obtains \(p=-V(\phi)\) and asks:

*Is the derivation correct?  In particular, is assumption 3 legitimate?*  

We shall answer by **deriving the general expressions for \(\rho\) and \(p\) of a scalar field**, then examining the special cases that give \(p=-V\).  

---

## 2. Step‑by‑step derivation

### 2.1 Energy‑momentum tensor of a canonical scalar field  

For  

\[
\mathcal L = \frac12\partial_{\mu}\phi\,\partial^{\mu}\phi - V(\phi)
\]

the canonical (Hilbert) energy‑momentum tensor is  

\[
\boxed{T^{\mu\nu}= \partial^{\mu}\phi\,\partial^{\nu}\phi - g^{\mu\nu}\mathcal L } .
\]

Insert \(\mathcal L\):

\[
T^{\mu\nu}= \partial^{\mu}\phi\,\partial^{\nu}\phi
          - g^{\mu\nu}\!\left[\frac12\partial_{\alpha}\phi\,\partial^{\alpha}\phi - V(\phi)\right].
\]

### 2.2 Components in a generic frame  

Write \(\partial^{0}\phi = \dot\phi\) and \(\partial^{i}\phi = \partial_{i}\phi \equiv (\nabla\phi)_{i}\).  
Using the Minkowski metric \(g^{\mu\nu}= {\rm diag}(+1,-1,-1,-1)\):

* **Energy density** (\(T^{00}\))  

\[
\begin{aligned}
T^{00} &= \dot\phi\,\dot\phi 
        - g^{00}\!\left[\tfrac12(\dot\phi^{2} - (\nabla\phi)^{2})-V\right] \\
       &= \dot\phi^{2} -\Big[\tfrac12(\dot\phi^{2}-(\nabla\phi)^{2})-V\Big] \\
       &= \frac12\dot\phi^{2} + \frac12(\nabla\phi)^{2}+ V .
\end{aligned}
\]

* **Spatial diagonal components** (\(T^{ii}\), no sum over \(i\))  

\[
\begin{aligned}
T^{ii} &= (\partial^{i}\phi)^{2}
        - g^{ii}\!\left[\tfrac12(\dot\phi^{2}-(\nabla\phi)^{2})-V\right] \\
       &= (\partial_{i}\phi)^{2}
        +\Big[\tfrac12(\dot\phi^{2}-(\nabla\phi)^{2})-V\Big] \\
       &= \frac12\dot\phi^{2} - \frac12(\nabla\phi)^{2} - V .
\end{aligned}
\]

Because the metric is diagonal, all three spatial components are equal when the field is isotropic, i.e. when \((\nabla\phi)^{2}= \delta^{ij}\partial_i\phi\,\partial_j\phi\).

### 2.3 Matching to the perfect‑fluid form  

The perfect‑fluid tensor can be written as  

\[
T^{\mu\nu}= (\rho+p)u^{\mu}u^{\nu} - g^{\mu\nu}p ,
\]
with \(u^{\mu}u_{\mu}=+1\).  

In the **fluid rest frame** we have \(u^{\mu}=(1,0,0,0)\). Then

\[
T^{00}= \rho ,\qquad 
T^{ij}= -\,g^{ij}p .
\]

Comparing the scalar‑field components **in a frame where the field is homogeneous** (so that \(\nabla\phi =0\)) we obtain

\[
\boxed{\rho = \frac12\dot\phi^{2}+V(\phi)},
\qquad
\boxed{p    = \frac12\dot\phi^{2}-V(\phi)} .
\]

Thus, for a **generic homogeneous but time‑dependent** scalar field the pressure is **not** simply \(-V\); it contains a kinetic contribution \(\frac12\dot\phi^{2}\).

### 2.4 When does \(p=-V\) hold?  

From the above expression,  

\[
p = -V \quad\Longleftrightarrow\quad \dot\phi =0 .
\]

Therefore the equality \(p=-V\) is true only in the **static limit** where the field sits at a constant value (for example at a minimum of its potential).  

In cosmology this situation occurs:

* **At thermal equilibrium**: after a first‑order phase transition the field has settled in the true vacuum and its time‑derivative vanishes. The *effective potential* \(V_{\rm eff}(\phi,T)\) is the **Gibbs free‑energy density** \(f\). Thermodynamics tells us that the pressure is the negative of the free‑energy density,
  \[
  p = -f = -V_{\rm eff} .
  \]

* **In the slow‑roll regime of inflation** where \(\dot\phi^{2}\ll V\): the kinetic term is negligible, so \(p\simeq -V\) (the equation‑of‑state approaches \(w\equiv p/\rho\approx -1\)).

But **the kinetic term cannot be removed by a Lorentz boost**. The fluid 4‑velocity \(u^{\mu}\) for a scalar field is defined as the timelike eigenvector of \(T^{\mu}{}_{\nu}\),

\[
T^{\mu}{}_{\nu}u^{\nu}= \rho\,u^{\mu}.
\]

When \(\dot\phi\neq 0\) this eigenvector is proportional to \(\partial^{\mu}\phi\). A boost that would set \(\dot\phi\) to zero would also change the field configuration itself, which is not allowed. Hence **assumption 3 is not valid**: you cannot make the field static simply by going to the fluid rest frame.  

Only if the *physical* configuration already has \(\dot\phi=0\) (i.e. the field is truly static) does the rest frame coincide with a static field.

### 2.5 Incorporating the *effective* (finite‑temperature) potential  

At finite temperature the Lagrangian is unchanged, but the **potential** receives thermal corrections, giving the *effective potential* \(V_{\rm eff}(\phi,T)\). The **free‑energy density** of the system is precisely  

\[
f(T,\phi)= V_{\rm eff}(\phi,T) .
\]

When the system is in thermal equilibrium the scalar field sits at the (local) minimum of \(V_{\rm eff}\), so \(\dot\phi=0\). Consequently,

\[
p = -f = -V_{\rm eff}(\phi,T) .
\]

This is the statement used in the literature on cosmic phase transitions.

---

## 3. Final answer (concise)

* For a canonical real scalar field with Lagrangian \(\mathcal L=\tfrac12(\partial\phi)^2-V(\phi)\) the energy‑momentum tensor can be written in perfect‑fluid form with  

\[
\boxed{\rho = \frac12\dot\phi^{2}+V(\phi)},\qquad
\boxed{p    = \frac12\dot\phi^{2}-V(\phi)} .
\]

* **Only** when the field is *static* (\(\dot\phi=0\)) does the pressure reduce to  

\[
p = -V(\phi) .
\]

* In a cosmological first‑order phase transition the field is assumed to have relaxed to a (thermal) equilibrium configuration, i.e. \(\dot\phi=0\) at the minima of the **effective potential** \(V_{\rm eff}(\phi,T)\). The free‑energy density is \(f=V_{\rm eff}\) and thermodynamics gives \(p=-f\), reproducing the relation used in the references.

* Assumption 3 (that one can make \(\dot\phi=0\) by a choice of frame) is **incorrect**; the fluid rest frame is determined by the eigenvector of \(T^{\mu}{}_{\nu}\) and does not, in general, eliminate the time derivative of the scalar field.

---

## 4. Common mistakes for this type of problem  

| Mistake | Why it is wrong | How to avoid it |
|---|---|---|
| **Setting \(\dot\phi=0\) by a Lorentz boost** | The scalar field is a *field*, not a collection of particles; its time derivative is a physical quantity, not a component of a 4‑vector that can be rotated away. | Remember that \(u^{\mu}\) is defined from the eigenvector of \(T^{\mu}{}_{\nu}\). Only when the field configuration itself has \(\dot\phi=0\) does the rest frame coincide with a static field. |
| **Identifying \(p\) with \(-V\) for any homogeneous field** | The pressure also receives a kinetic contribution \(\frac12\dot\phi^{2}\). Ignoring it gives the wrong equation of state (e.g. predicts \(w=-1\) even when the field is rolling). | Write the general expressions for \(\rho\) and \(p\) first, then examine the special limit \(\dot\

*Original question: [Pressure equals to minus of Potential energy in perfect fluid (and field theory)](https://physics.stackexchange.com/questions/875656/pressure-equals-to-minus-of-potential-energy-in-perfect-fluid-and-field-theory) on Physics Stack Exchange, licensed CC BY-SA.*

{% endraw %}
