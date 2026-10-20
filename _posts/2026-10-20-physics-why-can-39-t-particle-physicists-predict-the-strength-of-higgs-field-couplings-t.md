---
layout: question
title: Why can&#39;t particle physicists predict the strength of Higgs field couplings
  that give particles mass?
author: StemFix Bot
category: physics
subject: physics
description: 'Step-by-step physics solution: Why can&#39;t particle physicists predict
  the strength of Higgs field couplings that give particles mass?'
tags:
- physics
---

{% raw %}
*As an Amazon Associate, I earn from qualifying purchases.* For more practice problems like this, see [Schaum's Outline of College Physics, 12th Edition](https://www.amazon.com/dp/1259587398?tag=aiopentec20-20).

---

## 1. Restating the Question in Plain Language  

The student is asking:

* **What must we know about the Higgs field in order to *calculate* the masses of the elementary particles?**  
*Is the Higgs field carrying some hidden “charge” that couples differently to each particle, thereby fixing its mass?*  

In short: *Why doesn’t the Standard Model (SM) give us the numerical values of the electron, quark, etc. masses, and could an unknown charge‑type be the missing ingredient?*  

---

## 2. Full Step‑by‑Step Explanation  

### 2.1. What the Higgs field *does* in the SM  

| Quantity | Symbol | Role in the SM |
|----------|--------|----------------|
| Higgs doublet | \( \Phi = \begin{pmatrix}\phi^{+}\\ \phi^{0}\end{pmatrix} \) | A complex scalar that transforms as a **weak isospin doublet** with hypercharge \(Y = +\tfrac12\). |
| Vacuum expectation value (VEV) | \(v \equiv \langle\phi^{0}\rangle = 246\;\text{GeV}\) | After electroweak symmetry breaking (EWSB) the neutral component acquires this constant value, giving masses to gauge bosons and, through Yukawa interactions, to fermions. |
| Higgs self‑coupling | \(\lambda\) | Appears in the scalar potential \(V(\Phi)=\mu^{2}\Phi^\dagger\Phi + \lambda (\Phi^\dagger\Phi)^{2}\). Determines the Higgs boson mass \(m_h = \sqrt{2\lambda}\,v\). |

The **only** property of the Higgs field that is *known* from symmetry arguments is its gauge quantum numbers (weak isospin \(I= \tfrac12\), hypercharge \(Y=\tfrac12\), colour singlet). There is **no extra charge** attached to it that distinguishes one fermion species from another.

### 2.2. How fermion masses arise: the Yukawa terms  

The SM Lagrangian contains, for each family of fermions, **Yukawa interaction terms** that are the only renormalizable, gauge‑invariant couplings between the Higgs doublet and the fermions:

\[
\mathcal L_{\text{Yuk}} \;=\;
- \, \overline{Q}_{L}^{\,i}\, Y^{u}_{ij}\, \tilde\Phi\, u_{R}^{\,j}
- \, \overline{Q}_{L}^{\,i}\, Y^{d}_{ij}\, \Phi\, d_{R}^{\,j}
- \, \overline{L}_{L}^{\,i}\, Y^{e}_{ij}\, \Phi\, e_{R}^{\,j}
\;+\;\text{h.c.}
\]

* \(Q_L^i=(u_L^i,d_L^i)^T\) and \(L_L^i=(\nu_L^i, e_L^i)^T\) are the left‑handed quark and lepton doublets.  
* \(u_R^j, d_R^j, e_R^j\) are the right‑handed singlets.  
* \(\tilde\Phi = i\sigma_2\Phi^{*}\) transforms like a doublet with hypercharge \(-\tfrac12\) and couples to up‑type quarks.  
* \(Y^{u,d,e}_{ij}\) are **\(3\times 3\) complex matrices of dimensionless numbers** called **Yukawa coupling matrices**.  

These matrices are *the only place* where the SM distinguishes between the three generations and between up‑type, down‑type, and charged‑lepton sectors.

### 2.3. From Yukawa couplings to masses  

When the neutral component of \(\Phi\) obtains its VEV, we replace  

\[
\Phi \;\longrightarrow\; \frac{1}{\sqrt{2}}\begin{pmatrix}0\\ v\end{pmatrix},
\qquad
\tilde\Phi \;\longrightarrow\; \frac{1}{\sqrt{2}}\begin{pmatrix}v\\0\end{pmatrix}.
\]

Plugging this into \(\mathcal L_{\text{Yuk}}\) yields ordinary mass terms:

\[
\mathcal L_{\text{mass}} = - \frac{v}{\sqrt{2}}
\Bigl[ \overline{u}_{L}^{\,i}\,Y^{u}_{ij}\,u_{R}^{\,j}
      +\overline{d}_{L}^{\,i}\,Y^{d}_{ij}\,d_{R}^{\,j}
      +\overline{e}_{L}^{\,i}\,Y^{e}_{ij}\,e_{R}^{\,j} \Bigr] +\text{h.c.}
\]

Thus the **mass matrices** are  

\[
M^{u}= \frac{v}{\sqrt{2}}\,Y^{u},\qquad
M^{d}= \frac{v}{\sqrt{2}}\,Y^{d},\qquad
M^{e}= \frac{v}{\sqrt{2}}\,Y^{e}.
\]

To obtain the physical (observable) masses we must diagonalise each matrix by unitary rotations:

\[
U_{L}^{u\dagger} M^{u} U_{R}^{u}= \text{diag}(m_u,m_c,m_t),\;\;
U_{L}^{d\dagger} M^{d} U_{R}^{d}= \text{diag}(m_d,m_s,m_b),\;\;
U_{L}^{e\dagger} M^{e} U_{R}^{e}= \text{diag}(m_e,m_\mu,m_\tau).
\]

The eigenvalues \(m_f\) are the **particle masses**.  

**Key point:** The *numerical values* of the masses are **directly proportional to the entries of the Yukawa matrices**.  

### 2.4. What the SM *does not* predict  

The SM **does not contain any principle** that fixes the entries of \(Y^{u,d,e}\). They are **free parameters** that must be taken from experiment.  

* There are 9 complex numbers in each Yukawa matrix → 27 real parameters.  
* After removing unobservable phases (via field redefinitions) we are left with **13 independent real parameters** (6 quark masses, 3 charged‑lepton masses, 3 mixing angles, 1 CP‑violating phase).  

These 13 numbers are *inputs* to the theory; the SM cannot compute them.

### 2.5. Why not “another charge” on the Higgs?  

One might imagine that the Higgs carries an extra hidden charge \(Q_{\text{X}}\) that couples with different strengths to each fermion, similar to electric charge. This is **not needed** and, in fact, is **inconsistent** with the SM gauge structure:

| Property | SM requirement | Consequence of a new charge |
|----------|----------------|----------------------------|
| **Gauge invariance** of the Yukawa term | The term must be a singlet under all gauge groups (SU(3)\(_c\), SU(2)\(_L\), U(1)\(_Y\)). | Introducing a new charge would demand an extra gauge symmetry. The Higgs would have to transform under it, and the Yukawa term would only be allowed if the fermion also carried the same charge. This would generate *new gauge interactions* that we do **not** see. |
| **Observed couplings** | Higgs couplings to fermions are proportional to the fermion masses, not to a conserved quantum number. | A conserved charge would lead to selection rules (e.g., some couplings would be strictly zero). Experiments show that *all* SM fermions couple to the Higgs (though with different strengths). |

Hence, the **only way** the SM distinguishes among families is through the *numerical values* of the Yukawa couplings, not through a new charge.

### 2.6. What would be needed to *predict* the masses?  

To calculate the masses from first principles we would need a **theory of flavour** that explains why the Yukawa matrices have the pattern they do. Such a theory must:

1. **Introduce a dynamical principle** (e.g., a new symmetry, extra dimensions, compositeness) that relates different entries of the Yukawa matrices.
2. **Predict the values of the Yukawa couplings** (or at least reduce the number of independent parameters) before we compare with experiment.

Examples of attempted frameworks:

| Approach | Basic Idea | Status |
|----------|------------|--------|
| **Grand Unified Theories (GUTs)** | Quarks and leptons belong to common multiplets → relations like \(Y^{d}=Y^{e\,T}\) at the unification scale. | Gives **approximate** relations (e.g., \(m_b \approx m_\tau\) after running) but does not fix all entries. |
| **Froggatt‑Nielsen (FN) mechanism** | A horizontal U(1) symmetry broken by a flavon field; Yukawas arise as powers of a small parameter \(\epsilon\). | Can generate hierarchical patterns, but the *order‑one* coefficients remain unknown. |
| **Texture zeros / mass matrix ansätze** | Impose zeros or relations in Yukawa matrices motivated by symmetry. | Fit data but not derived from a deeper principle. |
| **Extra‑dimensional localisation** | Fermion wave‑functions have different overlaps with the Higgs in the extra dimension, producing exponential hierarchies. | Provides a *geometric* explanation, yet still contains free localisation parameters. |
| **Composite Higgs / Partial compositeness** | Fermion masses arise from mixing with composite resonances; mixing strengths determine effective Yukawas. | Predicts correlations but introduces new strong‑sector parameters. |
| **String‑theoretic constructions** | Yukawa couplings are given by overlap integrals of world‑sheet fields; geometry of compactification determines them. | In principle calculable, but current models cannot yet reproduce the observed spectrum uniquely. |

All these ideas **reduce** the number of independent parameters, but none have yet produced a unique, experimentally verified prediction of every SM mass.

### 2.7. Neutrino masses – a special case  

The SM, as originally written, has **no renormalizable Yukawa term for neutrinos** because right‑handed neutrinos are absent. Observed neutrino masses therefore **require new physics** (e.g., the dimension‑5 Weinberg operator or heavy right‑handed neutrinos). This further illustrates that the SM does not predict *all* masses.

### 2.8. Summary of the logical chain  

1. **Electroweak symmetry breaking** gives the Higgs a VEV \(v\).  
2. **Yukawa couplings** \(Y^{f}_{ij}\) connect the Higgs to each fermion species.  
3. **Masses** are \(m_f = \frac{v}{\sqrt{2}}\, y_f\) where \(y_f\) is the (diagonalised) Yukawa eigenvalue.  
4. The SM **does not prescribe** the numbers \(y_f\); they are free parameters fit to data.  
5. No hidden charge on the Higgs is required (and would conflict with observed gauge interactions).  
6. Predicting the pattern of \(y_f\) demands an *additional* theoretical framework beyond the SM.

---

## 3. Final Answer  

- **What must be known to predict a particle’s mass?**  
  The value of the **Yukawa coupling** that links that particle to the Higgs field (plus the known Higgs VEV \(v\)).  

- **Why can’t the Standard Model give these numbers?**  
  The SM treats the Yukawa couplings as **arbitrary, experimentally determined parameters**; the theory contains no deeper principle that fixes their values.  

- **Is there an unknown charge on the Higgs that could explain the hierarchy?**  
  No. The Higgs already has fixed gauge charges (weak isospin doublet, hypercharge \(+\tfrac12\), colour singlet). Introducing another conserved charge would lead to

*Original question: [Why can&#39;t particle physicists predict the strength of Higgs field couplings that give particles mass?](https://physics.stackexchange.com/questions/877078/why-cant-particle-physicists-predict-the-strength-of-higgs-field-couplings-that) on Physics Stack Exchange, licensed CC BY-SA.*

{% endraw %}
