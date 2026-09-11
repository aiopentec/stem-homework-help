---
layout: question
title: Breaking a four-vector into orthogonal components
author: StemFix Bot
category: physics
subject: physics
description: 'Step-by-step physics solution: Breaking a four-vector into orthogonal
  components'
tags:
- physics
---

{% raw %}
*As an Amazon Associate, I earn from qualifying purchases.* For more practice problems like this, see [Schaum's Outline of College Physics, 12th Edition](https://www.amazon.com/dp/1259587398?tag=aiopentec20-20).

---

## 1.  What the problem is asking (in plain language)

We have two special four‑vectors that describe the motion of a particle  

* the **four‑velocity** \(U^{\mu}\) (a timelike unit vector, \(U\!\cdot\!U=-1\)),  
* the **four‑acceleration** \(A^{\mu}=dU^{\mu}/d\tau\) (always orthogonal to the velocity, \(U\!\cdot\!A=0\)).

The question is:

*How can we build an orthogonal basis (a “tetrad”) in Minkowski space that contains the velocity direction, and then split the acceleration into three mutually orthogonal spacelike pieces that are also orthogonal to the velocity?*  

In other words we need a systematic way to decompose any four‑vector into a part **parallel** to \(U^{\mu}\) and a part **perpendicular** to \(U^{\mu}\), and then, for the perpendicular part, further split it into three mutually orthogonal spacelike directions.

---

## 2.  Step‑by‑step solution  

### 2.1  Conventions and the Minkowski inner product  

We work with the metric  

\[
\eta_{\mu\nu}= \operatorname{diag}(-1,\; +1,\; +1,\; +1),\qquad
A\!\cdot\!B\equiv \eta_{\mu\nu}A^{\mu}B^{\nu}.
\]

With this signature a **timelike** vector has negative norm, a **spacelike** vector has positive norm, and a **null** vector has zero norm.

The four‑velocity satisfies  

\[
U^{\mu}U_{\mu}= -1 .
\]

The four‑acceleration satisfies  

\[
U^{\mu}A_{\mu}=0 .
\]

---

### 2.2  Projecting onto the direction of the velocity  

Given any four‑vector \(V^{\mu}\) we can separate it into a piece parallel to \(U^{\mu}\) and a piece orthogonal to \(U^{\mu}\).  
Because \(U^{\mu}U_{\mu}=-1\),

\[
\boxed{\;V_{\parallel}^{\mu}=-(U\!\cdot\!V)\;U^{\mu}\;}
\]

is the component **along** the velocity (the minus sign compensates the \(-1\) norm).  

The orthogonal component is obtained with the **spatial projector**

\[
h_{\mu\nu}= \eta_{\mu\nu}+U_{\mu}U_{\nu},
\qquad
\boxed{\;V_{\perp}^{\mu}=h^{\mu}{}_{\nu}V^{\nu}=V^{\mu}+(U\!\cdot\!V)U^{\mu}\; } .
\]

Notice that \(h_{\mu\nu}U^{\nu}=0\) and \(h_{\mu\nu}\) acts like the identity on any vector already orthogonal to \(U^{\mu}\).

*For the four‑acceleration* \(A^{\mu}\) we have \(U\!\cdot\!A=0\), therefore  

\[
A_{\parallel}^{\mu}=0,\qquad A_{\perp}^{\mu}=A^{\mu}.
\]

So the acceleration is already a **purely spatial** vector in the instantaneous rest frame of the particle.

---

### 2.3  Building an orthonormal spacelike triad  

We now need three spacelike unit vectors \(e_{(i)}^{\mu}\;(i=1,2,3)\) that satisfy  

\[
e_{(i)}\!\cdot\!e_{(j)}=\delta_{ij},\qquad
e_{(i)}\!\cdot\!U=0 .
\]

The standard way is to use a **Minkowski‑adapted Gram–Schmidt process**.

---

#### Step 1 – Choose the first spacelike direction

Take the acceleration itself (if it is non‑zero) as the first direction:

\[
e_{(1)}^{\mu}= \frac{A^{\mu}}{\sqrt{A\!\cdot\!A}}\; .
\]

Because \(A\!\cdot\!A>0\) (the acceleration is spacelike), the denominator is real and \(e_{(1)}\) is unit spacelike and already orthogonal to \(U\).

---

#### Step 2 – Choose any other vector not in the span of \(\{U,e_{(1)}\}\)

Pick an arbitrary four‑vector \(B^{\mu}\) that is **not** a linear combination of \(U^{\mu}\) and \(A^{\mu}\).  
A convenient choice is a coordinate basis vector, e.g. \(B^{\mu}=(0,1,0,0)\) in the particle’s instantaneous rest frame (any spatial basis vector works).

First make it orthogonal to the velocity:

\[
\tilde B^{\mu}=B^{\mu}+(U\!\cdot\!B)U^{\mu}\; .
\]

(If \(B^{\mu}\) is already spatial in the rest frame, the extra term vanishes.)

Now remove the component along \(e_{(1)}\):

\[
\tilde B^{\mu}_{\perp}= \tilde B^{\mu}-(e_{(1)}\!\cdot\!\tilde B)\,e_{(1)}^{\mu}.
\]

Normalize:

\[
e_{(2)}^{\mu}= \frac{\tilde B^{\mu}_{\perp}}{\sqrt{\tilde B_{\perp}\!\cdot\!\tilde B_{\perp}}}.
\]

By construction  

\[
e_{(2)}\!\cdot\!U=0,\qquad e_{(2)}\!\cdot\!e_{(1)}=0,\qquad e_{(2)}\!\cdot\!e_{(2)}=+1 .
\]

---

#### Step 3 – The third spacelike direction  

Having two orthonormal spacelike vectors, the third can be obtained with the Levi‑Civita tensor (the Minkowski “cross product”):

\[
e_{(3)}^{\mu}= \frac{1}{\sqrt{-\det h}}\;
\varepsilon^{\mu\nu\rho\sigma}U_{\nu}\,e_{(1)\,\rho}\,e_{(2)\,\sigma},
\]

where  

\[
h \equiv \det\bigl(\eta_{\alpha\beta}+U_{\alpha}U_{\beta}\bigr) = -1
\]

so the prefactor is just a sign. Explicitly,

\[
e_{(3)}^{\mu}= \frac{\varepsilon^{\mu\nu\rho\sigma}U_{\nu}e_{(1)\rho}e_{(2)\sigma}}
{\sqrt{(U\!\cdot\!U)(e_{(1)}\!\cdot\!e_{(1)})(e_{(2)}\!\cdot\!e_{(2)})}}.
\]

Because the Levi‑Civita symbol is totally antisymmetric, the resulting vector is orthogonal to each of the three vectors already in the list and is automatically spacelike. Normalising gives a unit vector.

Now we have the **orthonormal tetrad**

\[
\boxed{\bigl\{\,U^{\mu},\;e_{(1)}^{\mu},\;e_{(2)}^{\mu},\;e_{(3)}^{\mu}\bigr\}} ,
\]

with the required orthogonality relations.

---

### 2.4  Decomposing the acceleration into the orthogonal basis  

Since \(A^{\mu}\) lies entirely in the spatial subspace, its expansion reads

\[
A^{\mu}= \underbrace{0}_{\text{parallel to }U}\;U^{\mu}
          + \underbrace{(A\!\cdot\!e_{(1)})}_{=|A|}\,e_{(1)}^{\mu}
          + (A\!\cdot\!e_{(2)})\,e_{(2)}^{\mu}
          + (A\!\cdot\!e_{(3)})\,e_{(3)}^{\mu}.
\]

Because we chose \(e_{(1)}\) to be **parallel to** the acceleration, the two remaining scalar products vanish:

\[
A\!\cdot\!e_{(2)}=A\!\cdot\!e_{(3)}=0 .
\]

Thus the **final decomposition** is simply

\[
\boxed{ \displaystyle 
A^{\mu}= |A|\,e_{(1)}^{\mu},\qquad 
|A| \equiv \sqrt{A\!\cdot\!A}\; } .
\]

If one wishes to express an *arbitrary* four‑vector \(V^{\mu}\) in the same tetrad, the general formula is

\[
V^{\mu}= -(U\!\cdot\!V)U^{\mu}
        + (V\!\cdot\!e_{(1)})e_{(1)}^{\mu}
        + (V\!\cdot\!e_{(2)})e_{(2)}^{\mu}
        + (V\!\cdot\!e_{(3)})e_{(3)}^{\mu}.
\]

---

## 3.  Final answer  

* The projector onto the subspace orthogonal to the four‑velocity is  

\[
h_{\mu\nu}= \eta_{\mu\nu}+U_{\mu}U_{\nu}.
\]

* For any vector \(V^{\mu}\),

\[
V_{\parallel}^{\mu}=-(U\!\cdot\!V)U^{\mu},\qquad
V_{\perp}^{\mu}=V^{\mu}+(U\!\cdot\!V)U^{\mu}.
\]

* An orthonormal spacelike triad \(\{e_{(i)}^{\mu}\}\) orthogonal to \(U^{\mu}\) can be built by (i) taking \(e_{(1)}^{\mu}=A^{\mu}/\sqrt{A\!\cdot\!A}\); (ii) Gram‑Schmidt‑orthogonalising any other spatial vector to obtain \(e_{(2)}^{\mu}\); (iii) defining  

\[
e_{(3)}^{\mu}= \frac{\varepsilon^{\mu\nu\rho\sigma}U_{\nu}e_{(1)\rho}e_{(2)\sigma}}
{\sqrt{-(U\!\cdot\!U)(e_{(1)}\!\cdot\!e_{(1)})(e_{(2)}\!\cdot\!e_{(2)})}} .
\]

* The acceleration decomposes as  

\[
A^{\mu}=|A|\,e_{(1)}^{\mu},\qquad |A|=\sqrt{A\

*Original question: [Breaking a four-vector into orthogonal components](https://physics.stackexchange.com/questions/875892/breaking-a-four-vector-into-orthogonal-components) on Physics Stack Exchange, licensed CC BY-SA.*

{% endraw %}
