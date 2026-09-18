---
layout: question
title: 'Magnetization v/s Polarization: Why are they weirdly dissimilar?'
author: StemFix Bot
category: physics
subject: physics
description: 'Step-by-step physics solution: Magnetization v/s Polarization: Why are
  they weirdly dissimilar?'
tags:
- physics
---

{% raw %}
*As an Amazon Associate, I earn from qualifying purchases.* For more practice problems like this, see [Schaum's Outline of College Physics, 12th Edition](https://www.amazon.com/dp/1259587398?tag=aiopentec20-20).

---

## 1.  What the student is asking (in plain language)

The student sees two pairs of macroscopic fields  

*Electric*: \( \mathbf E,\;\mathbf D\)  
*Magnetic*: \( \mathbf B,\;\mathbf H\)

and the corresponding material responses  

*Polarization*: \(\mathbf P\) and *Magnetization*: \(\mathbf M\).

The textbook formulas read  

\[
\mathbf P =\varepsilon_0\chi_e\mathbf E ,\qquad 
\mathbf M = \chi_m\mathbf H ,
\]

\[
\mathbf D =\varepsilon_0\mathbf E+\mathbf P ,\qquad 
\mathbf H =\frac{\mathbf B}{\mu_0}-\mathbf M .
\]

The student wonders why

* \( \mathbf P\) is written as proportional to the **applied** electric field \(\mathbf E\) while \(\mathbf M\) is written as proportional to the **auxiliary** field \(\mathbf H\);
* we do **not** write \(\mathbf M =\chi_m\mathbf B\) (or \(\mathbf P = \chi_e \mathbf D\));
* the “field produced by the magnetization’’ appears with a factor \(1/\mu_0\) instead of \(1/(\mu_0\chi_m)\);
* the total magnetic induction is written as \(\mathbf B =\mu_0\mathbf H\) (or \(\mu\mathbf H\)) rather than \(\mathbf B = \mu \mathbf B_{\text{applied}}\).

In short: *Why do the electric and magnetic constitutive relations look asymmetrical?*  

The answer lies in **how we define the four macroscopic fields** and in the **separation of free versus bound sources** in Maxwell’s equations.

---

## 2.  Microscopic vs. macroscopic fields

### 2.1 Microscopic Maxwell equations  

At the microscopic level the fields \(\mathbf e(\mathbf r,t)\) and \(\mathbf b(\mathbf r,t)\) obey

\[
\begin{aligned}
\nabla\!\cdot\!\mathbf e &= \frac{\rho_{\text{tot}}}{\varepsilon_0},\\[2pt]
\nabla\!\times\!\mathbf b &= \mu_0\mathbf j_{\text{tot}}+\mu_0\varepsilon_0\frac{\partial\mathbf e}{\partial t},
\end{aligned}
\]

where \(\rho_{\text{tot}}\) and \(\mathbf j_{\text{tot}}\) contain **both** the *free* charges/currents we control and the *bound* charges/currents bound inside atoms and molecules.

### 2.2 Averaging → macroscopic fields  

We smooth (average) the microscopic fields over a volume large compared with atomic dimensions but small compared with the wavelength of interest. The result are the **macroscopic** fields \(\mathbf E,\,\mathbf B\). They obey the same Maxwell equations **if** we also introduce *effective* source densities

\[
\rho_{\text{free}},\quad \mathbf j_{\text{free}}
\]

and define the *bound* sources through the material response:

* **Bound electric charge density**  
  \[
  \rho_{\text{bound}} = -\nabla\!\cdot\!\mathbf P .
  \]

* **Bound current density** (including the “magnetization current’’)  
  \[
  \mathbf j_{\text{bound}} = \nabla\times\mathbf M +\frac{\partial\mathbf P}{\partial t}.
  \]

With these definitions the macroscopic Maxwell equations become

\[
\boxed{
\begin{aligned}
\nabla\!\cdot\!\mathbf D &= \rho_{\text{free}}, &
\mathbf D &\equiv \varepsilon_0\mathbf E+\mathbf P,\\[4pt]
\nabla\!\cdot\!\mathbf B &= 0,\\[4pt]
\nabla\times\mathbf E &= -\frac{\partial\mathbf B}{\partial t},\\[4pt]
\nabla\times\mathbf H &= \mathbf j_{\text{free}}+\frac{\partial\mathbf D}{\partial t}, &
\mathbf H &\equiv \frac{\mathbf B}{\mu_0}-\mathbf M .
\end{aligned}}
\]

**Key point:**  

* \(\mathbf D\) and \(\mathbf H\) are *auxiliary* fields that contain **only the free sources**.  
* \(\mathbf E\) and \(\mathbf B\) contain **both** free and bound contributions.

Because of this definition the equations look “asymmetric’’ when we write the material constitutive relations.

---

## 3.  Linear, isotropic, homogeneous media  

For many common materials the response is linear and direction‑independent:

\[
\mathbf P = \varepsilon_0 \chi_e \mathbf E ,\qquad 
\mathbf M = \chi_m \mathbf H .
\]

These are **definitions** of the electric susceptibility \(\chi_e\) and magnetic susceptibility \(\chi_m\).  
Why does \(\mathbf M\) involve \(\mathbf H\) and not \(\mathbf B\)?

* By definition \(\chi_m\) is the proportionality constant **between the magnetization and the field that would exist if the bound currents were absent**, i.e. the *free‑current* field \(\mathbf H\).  
* If we tried to write \(\mathbf M = \tilde\chi_m\mathbf B\), the constant \(\tilde\chi_m\) would have different dimensions (because \(\mathbf B\) already contains \(\mu_0\)).  The conventional choice keeps \(\mathbf M\) and \(\mathbf H\) having the same units (A m⁻¹), which makes \(\chi_m\) dimensionless, just like \(\chi_e\).

Similarly for the electric case we could write \(\mathbf P = \varepsilon_0\tilde\chi_e \mathbf D\) but that would just introduce an extra factor of \(\varepsilon_0\) and hide the physical meaning of \(\chi_e\).

---

## 4.  Deriving the familiar “\(\mathbf B = \mu \mathbf H\)” relation  

Starting from the definition of \(\mathbf H\),

\[
\mathbf H = \frac{\mathbf B}{\mu_0} - \mathbf M,
\]

and substituting the linear relation \(\mathbf M = \chi_m\mathbf H\),

\[
\mathbf H = \frac{\mathbf B}{\mu_0} - \chi_m\mathbf H
\;\;\Longrightarrow\;\;
\mathbf B = \mu_0(1+\chi_m)\mathbf H \equiv \mu\,\mathbf H .
\]

Thus the *total* magnetic induction \(\mathbf B\) is the sum of two parts:

* **Free‑current part**: \(\mu_0\mathbf H\) (the field that would exist without bound currents);
* **Bound‑current part**: \(\mu_0\mathbf M = \mu_0\chi_m\mathbf H\).

So the *field produced by the magnetization* is **\(\mu_0\mathbf M\)**, not \(\mathbf M/\mu_0\). The textbook formula

\[
\boxed{\mathbf B = \mu_0(\mathbf H + \mathbf M)}
\]

is simply the rearranged version of the definition of \(\mathbf H\).

---

## 5.  Parallel electric formulas  

The electric side works analogously:

\[
\mathbf D = \varepsilon_0\mathbf E + \mathbf P,
\qquad \mathbf P = \varepsilon_0\chi_e\mathbf E,
\]

which gives

\[
\mathbf D = \varepsilon_0(1+\chi_e)\mathbf E \equiv \varepsilon\mathbf E .
\]

Here the **applied** field is \(\mathbf E\) (the field that would exist without bound charge), while \(\mathbf D\) is the auxiliary field that responds only to free charge. The symmetry is thus present; the only difference is the conventional naming of the “applied’’ field:

| Quantity | Applied (free‑source) field | Auxiliary field containing only free sources |
|----------|----------------------------|----------------------------------------------|
| Electric | \(\displaystyle \mathbf E\) | \(\displaystyle \mathbf D\) |
| Magnetic | \(\displaystyle \mathbf H\) | \(\displaystyle \mathbf B\) |

Because \(\mathbf B\) already includes \(\mu_0\), the magnetic auxiliary field is \(\mathbf H\); because \(\mathbf E\) already includes \(\varepsilon_0\), the electric auxiliary field is \(\mathbf D\). This explains the apparent asymmetry.

---

## 6.  Summary of the answers to the explicit questions  

| Question | Answer |
|----------|--------|
| **Why is \(\mathbf M\) proportional to \(\mathbf H\) and not \(\mathbf B\)?** | \(\mathbf H\) is defined as the magnetic field produced **only by free currents**. The susceptibility \(\chi_m\) is defined with respect to that free‑current field, giving a dimensionless constant and keeping \(\mathbf M\) and \(\mathbf H\) in the same units. Writing \(\mathbf M = \chi_m \mathbf B\) would mix free and bound contributions and would require a different (non‑dimensionless) constant. |
| **Why not write \(\mathbf P = \chi_e \mathbf D\)?** | It would be equivalent but would hide the physical meaning of \(\chi_e\). The conventional definition \(\mathbf P = \varepsilon_0\chi_e\mathbf E\) makes \(\chi_e\) dimensionless and directly ties the polarization to the **electric field that would exist without bound charge**. |
| **Why does the “field produced by magnetization’’ have the factor \( \mu_0\) (or \(1/\mu_0\) in the definition of \(\mathbf H\))?** | From \(\mathbf H = \mathbf B/\mu_0 - \mathbf M\) we get \(\mathbf B = \mu_0(\mathbf H + \mathbf M)\). The contribution of the magnetization to \(\mathbf B\) is therefore \(\mu_0\mathbf M\). The factor \(\mu_0\) appears because the magnetic field intensity \(\mathbf H\) was defined to subtract the bound‑current term \(\mathbf M\) from \(\mathbf B/\mu_0\). |
| **Why is the total \(\mathbf B\) written as \(\mu_0\mathbf H\) (or \(\mu\mathbf H\)) and not \(\mu\,\mathbf B_{\text{applied}}\)?** | The “applied’’ magnetic field is \(\mathbf H\); the total induction is \(\mathbf B = \mu \mathbf H\). If you tried to call \(\mathbf B_{\text{applied}}\) the field without magnetization you would actually be referring to \(\mu_0\mathbf H\). The notation already incorporates the material’s permeability \(\mu = \mu_0(1+\chi_m)\). |
| **Is there a hidden symmetry?** | Yes. The electric and magnetic sets of equations are symmetric once you remember that \(\mathbf D

*Original question: [Magnetization v/s Polarization: Why are they weirdly dissimilar?](https://physics.stackexchange.com/questions/876143/magnetization-v-s-polarization-why-are-they-weirdly-dissimilar) on Physics Stack Exchange, licensed CC BY-SA.*

{% endraw %}
