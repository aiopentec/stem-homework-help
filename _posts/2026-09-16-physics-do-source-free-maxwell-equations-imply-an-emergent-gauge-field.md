---
layout: question
title: Do source-free Maxwell equations imply an emergent gauge field?
author: StemFix Bot
category: physics
subject: physics
description: 'Step-by-step physics solution: Do source-free Maxwell equations imply
  an emergent gauge field?'
tags:
- physics
---

{% raw %}
*As an Amazon Associate, I earn from qualifying purchases.* For more practice problems like this, see [Schaum's Outline of College Physics, 12th Edition](https://www.amazon.com/dp/1259587398?tag=aiopentec20-20).

---

## 1.  What the question is asking (in plain language)

A low‑energy theory produces two vector fields **E**(x,t) and **B**(x,t) that, *on the solutions we look at*, obey the four vacuum Maxwell equations  

\[
\begin{aligned}
\nabla\!\cdot\!\mathbf B &=0 , &
\nabla\!\times\!\mathbf E+\partial_t\mathbf B &=0 ,\\[2mm]
\nabla\!\cdot\!\mathbf E &=0 , &
\nabla\!\times\!\mathbf B-\frac1{c^{2}}\partial_t\mathbf E &=0 .
\end{aligned}
\]

Does this automatically mean that the low‑energy sector is an **emergent U(1) gauge field** (i.e. a photon‑like degree of freedom)?  

If not, what extra pieces of structure must the underlying theory possess so that we can legitimately call the emergent object a gauge field? In particular, do we have to demand an explicit gauge redundancy and the presence of exactly two mass‑less transverse modes, rather than merely obtaining fields that happen to satisfy the source‑free Maxwell equations on a special class of configurations?

---

## 2.  Step‑by‑step answer  

Below we proceed systematically:

| Step | Goal | What we do |
|------|------|------------|
| 1 | Show that the four equations are *not* enough to guarantee a gauge field. | Exhibit a counter‑example (a free massless spin‑1 field without gauge invariance). |
| 2 | Identify the *minimal* extra ingredients that turn the equations into a genuine Maxwell gauge theory. | Discuss potentials, gauge redundancy, constraints, and the counting of physical degrees of freedom. |
| 3 | Summarise the complete set of conditions that must be met for an emergent **U(1) gauge field**. | List them in a concise checklist. |
| 4 | Explain why each item is necessary. | Use Hamiltonian/lagrangian arguments and examples from condensed‑matter realizations. |
| 5 | Provide a short “Common Mistakes” table. | Highlight pitfalls students often fall into. |

---

### Step 1 – Why the four equations alone are insufficient  

1. **The equations are *only* a subset of the full Maxwell system.**  
   The homogeneous equations  

   \[
   \nabla\!\cdot\!\mathbf B =0,\qquad 
   \nabla\!\times\!\mathbf E +\partial_t\mathbf B =0
   \]

   are automatically satisfied if we **define** a vector potential \(\mathbf A\) and a scalar potential \(\phi\) by  

   \[
   \mathbf B=\nabla\times\mathbf A,\qquad 
   \mathbf E=-\nabla\phi-\partial_t\mathbf A .
   \tag{2.1}
   \]

   But (2.1) is *a definition*, not a dynamical statement. Any pair of fields that can be written as (2.1) will satisfy the homogeneous equations, regardless of whether a gauge symmetry exists.

2. **The inhomogeneous equations**  

   \[
   \nabla\!\cdot\!\mathbf E =0,\qquad 
   \nabla\!\times\!\mathbf B-\frac{1}{c^{2}}\partial_t\mathbf E =0
   \tag{2.2}
   \]

   are equivalent to the wave equations  

   \[
   \Box \mathbf E =0,\qquad \Box \mathbf B =0 .
   \tag{2.3}
   \]

   A **massless spin‑1 field** described by a *vector* \(A_\mu\) with the Lagrangian  

   \[
   \mathcal L = -\frac12 (\partial_\mu A_\nu)(\partial^\mu A^\nu)
   \tag{2.4}
   \]

   also gives \(\Box A_\mu =0\). If we *identify* \(\mathbf E = -\partial_t\mathbf A\) and \(\mathbf B = \nabla\times\mathbf A\) (i.e. we set \(\phi=0\)), then (2.2) holds **on‑shell**, but the theory (2.4) has **four** propagating components, not the two required for a photon. The extra longitudinal and time‑like components are *not* removed by any gauge redundancy because the Lagrangian (2.4) is not gauge invariant.

   Hence a theory can produce fields that satisfy (2.2) on its solutions **without** being a gauge theory.

3. **Counter‑example:**  
   Take a free *Proca* field with a tiny mass \(m\). When \(m\to0\) the equations of motion reduce to (2.3) plus the Proca constraint \(\partial_\mu A^\mu =0\). The constraint removes one degree of freedom, leaving **three** polarizations (two transverse + one longitudinal). In the strict \(m=0\) limit the longitudinal mode becomes nondynamical, but the theory still lacks the **first‑class constraint** (Gauss law) that generates a gauge symmetry. Thus the mere satisfaction of the source‑free Maxwell equations does **not** guarantee a gauge field.

---

### Step 2 – What extra structure *does* guarantee an emergent U(1) gauge field?

| Requirement | Why it matters |
|-------------|----------------|
| **(a) Existence of potentials** \(A_\mu = (\phi,\mathbf A)\) such that \(\mathbf B = \nabla\times\mathbf A\) and \(\mathbf E = -\nabla\phi-\partial_t\mathbf A\). | Guarantees the homogeneous equations automatically. |
| **(b) Gauge redundancy** \(A_\mu\to A_\mu+\partial_\mu\chi\) (or, in Hamiltonian language, a **first‑class constraint**). | Removes the unphysical longitudinal and time‑like components, leaving exactly two physical helicities. |
| **(c) Gauss‑law constraint** \(\nabla\!\cdot\!\mathbf E =0\) (or \(\partial_i \Pi^i \approx 0\) in canonical language) that holds **as a constraint on every state**, not only on a particular solution. | Implements the *source‑free* condition as a *kinematical* restriction, i.e. it is generated by the gauge symmetry rather than being a dynamical equation of motion. |
| **(d) Linear, Lorentz‑invariant action** \(S = -\frac14\int d^4x\,F_{\mu\nu}F^{\mu\nu}\) (or any action that is gauge‑invariant and yields the same equations). | Ensures the equations are true for *all* field configurations, not just a selected subset; guarantees the wave‑dispersion relation \(\omega = c|\mathbf k|\). |
| **(e) Exactly two massless transverse propagating modes** (helicity \(\pm1\)). | The hallmark of a photon; follows automatically from (b)–(d) but must be checked explicitly when the emergent description is derived from a microscopic model. |
| **(f) Existence of a conserved U(1) charge** (or a topological conservation law) that can couple to \(A_\mu\). | Gives the gauge field a *meaning* as the mediator of a long‑range interaction; distinguishes a genuine gauge field from a “pure” free wave that never couples to anything. |

**How the pieces fit together**

1. **From (a) to (b).**  
   If we can write \(\mathbf E,\mathbf B\) as in (2.1), the potentials are *not* uniquely defined: adding the gradient of an arbitrary scalar \(\chi(x,t)\) changes \(\phi,\mathbf A\) but leaves \(\mathbf E,\mathbf B\) invariant. That non‑uniqueness is precisely a **gauge redundancy**.  

2. **From (b) to (c).**  
   In the Hamiltonian formulation the canonical momentum conjugate to \(A_0\) vanishes identically,
   \[
   \Pi^0 \equiv \frac{\partial\mathcal L}{\partial\dot A_0}=0,
   \]
   a **primary first‑class constraint**. Consistency under time evolution generates the **Gauss‑law secondary constraint**
   \[
   \partial_i \Pi^i =0 \quad\Longleftrightarrow\quad \nabla\!\cdot\!\mathbf E =0 .
   \]
   First‑class constraints generate gauge transformations; therefore (c) is not an extra equation of motion but a consequence of the gauge symmetry.

3. **Degree‑of‑freedom count.**  
   Start with four components \(A_\mu\).  
   - Primary constraint \(\Pi^0=0\) removes 1.  
   - Gauge freedom \(A_\mu\to A_\mu+\partial_\mu\chi\) removes another 1.  
   - The Gauss constraint removes a third component (the longitudinal mode).  
   Leaving **two** independent phase‑space variables → **two transverse photon polarizations**.

4. **Lorentz invariance & linearity** ensure that the dispersion relation is the relativistic one \(\omega = c|\mathbf k|\) and that the theory is stable (no ghosts).  

5. **Coupling to matter** (requirement (f)) is what distinguishes a *gauge* field from a free spin‑1 wave that never interacts. In condensed‑matter contexts the “charge” is often a topological defect (e.g. a monopole in spin ice) or a conserved lattice‑spin current.

---

### Step 3 – Checklist: When can we call the low‑energy sector an *emergent Maxwell U(1) gauge field*?

A low‑energy description **qualifies** as an emergent U(1) gauge theory **iff** all of the following hold:

1. **Potential representation**: There exist fields \(A_\mu\) such that \(\mathbf B = \nabla\times\mathbf A\) and \(\mathbf E = -\nabla\phi-\partial_t\mathbf A\).

2. **Gauge invariance**: The effective action (or Hamiltonian) is invariant under \(A_\mu\rightarrow A_\mu+\partial_\mu\chi\) for an arbitrary smooth function \(\chi\).

3. **Gauss‑law as a constraint**: \(\nabla\!\cdot\!\mathbf E =0\) (or its operator version) is a **first‑class constraint** that holds on the whole Hilbert space, not just on a subset of solutions.

4. **Linear, Lorentz‑invariant dynamics**: The equations of motion follow from the gauge‑invariant action \(S=-\frac14\!\int\!F_{\mu\nu}F^{\mu\nu}\) (or an equivalent low‑energy expansion).  

5. **Two

*Original question: [Do source-free Maxwell equations imply an emergent gauge field?](https://physics.stackexchange.com/questions/875901/do-source-free-maxwell-equations-imply-an-emergent-gauge-field) on Physics Stack Exchange, licensed CC BY-SA.*

{% endraw %}
