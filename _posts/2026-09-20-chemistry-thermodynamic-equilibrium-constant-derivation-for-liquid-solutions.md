---
layout: question
title: Thermodynamic Equilibrium Constant derivation for liquid solutions
author: StemFix Bot
category: chemistry
subject: chemistry
description: 'Step-by-step chemistry solution: Thermodynamic Equilibrium Constant
  derivation for liquid solutions'
tags:
- chemistry
---

{% raw %}
*As an Amazon Associate, I earn from qualifying purchases.* For more practice problems like this, see [Schaum's Outline of College Chemistry, 10th Edition](https://www.amazon.com/dp/007181082X?tag=aiopentec20-20).

---

## 1.  What the question is asking (in plain language)

The student wants to know **where the equation**

\[
\boxed{\Delta G = \Delta G^{\circ}+RT\ln K_c}
\]

comes from when the reaction takes place in a **liquid solution**.  
In other words:

* How do we go from the fundamental definition of chemical potential to an expression that relates the Gibbs energy change of a reaction to the equilibrium constant written in terms of *concentrations* (or activities) for a solution?  
* The same relation is familiar for gases (using partial pressures, \(K_p\)). The student wonders why the same form also works for liquids, and what approximations are involved.

We will start from the most general thermodynamic statement, introduce activities, define the equilibrium constant for a solution, and finally obtain the desired equation step‑by‑step.



---

## 2.  Full derivation – every step shown  

### 2.1  Chemical potential and activity  

For any component \(i\) in a homogeneous phase (gas, liquid, solid) the **chemical potential** is  

\[
\mu_i = \mu_i^{\circ} + RT\ln a_i \tag{1}
\]

where  

* \(\mu_i^{\circ}\) – standard chemical potential (defined at the chosen standard state)  
* \(a_i\) – **activity** of component \(i\) (dimensionless).  

The activity reduces to the “concentration” or “partial pressure” only when the system behaves ideally:

* For an ideal gas: \(a_i = \dfrac{p_i}{p^{\circ}}\) (with \(p^{\circ}=1\;\text{bar}\)).  
* For a *dilute* liquid solution: \(a_i \approx \dfrac{c_i}{c^{\circ}}\) (with \(c^{\circ}=1\;\text{mol·L}^{-1}\)).  

The approximation \(a_i \approx c_i/c^{\circ}\) follows because the activity coefficient \(\gamma_i\) is close to 1 for sufficiently dilute solutions:

\[
a_i = \gamma_i\frac{c_i}{c^{\circ}},\qquad \gamma_i\approx 1\;\;( \text{ideal solution limit} )
\]

From now on we will keep the notation \(a_i\) but remember that for an ideal (or very dilute) solution we may replace it by the concentration ratio.

---

### 2.2  Reaction Gibbs energy expressed with chemical potentials  

Consider a generic reaction written in stoichiometric form

\[
\sum_{i} \nu_i \, \mathrm{A}_i = 0
\]

where \(\nu_i\) are **stoichiometric numbers** (negative for reactants, positive for products).  
The **Gibbs energy change** of the reaction at any composition is

\[
\Delta G = \sum_i \nu_i \mu_i \tag{2}
\]

Insert Eq. (1) for each \(\mu_i\):

\[
\Delta G = \sum_i \nu_i \bigl[\mu_i^{\circ}+RT\ln a_i \bigr]
        = \underbrace{\sum_i \nu_i \mu_i^{\circ}}_{\displaystyle \Delta G^{\circ}}
          + RT\sum_i \nu_i\ln a_i
\]

Define the **standard Gibbs energy of reaction**

\[
\boxed{\Delta G^{\circ}= \sum_i \nu_i \mu_i^{\circ}} \tag{3}
\]

and use the logarithm property \(\sum \nu_i\ln a_i = \ln\bigl(\prod a_i^{\nu_i}\bigr)\) :

\[
\Delta G = \Delta G^{\circ} + RT\ln\!\left(\prod_i a_i^{\nu_i}\right) \tag{4}
\]

---

### 2.3  Definition of the equilibrium constant for a solution  

At **equilibrium** the reaction Gibbs energy is zero:

\[
\Delta G_{\text{eq}} = 0
\]

Setting \(\Delta G=0\) in Eq. (4) gives

\[
0 = \Delta G^{\circ}+RT\ln\!\left(\prod_i a_i^{\nu_i}\right)_{\!\text{eq}}
\]

Re‑arranging:

\[
-\frac{\Delta G^{\circ}}{RT}= \ln\!\left(\prod_i a_i^{\nu_i}\right)_{\!\text{eq}}
\]

Exponentiating both sides:

\[
\boxed{K \equiv \exp\!\bigl(-\Delta G^{\circ}/RT\bigr)
      = \prod_i a_i^{\nu_i}\Big|_{\text{eq}} } \tag{5}
\]

The quantity \(K\) is the **thermodynamic equilibrium constant**.  
When we choose the **standard state** for a solute to be a 1 mol L\(^{-1}\) solution, the activity reduces to \(a_i = c_i/c^{\circ}\). Consequently

\[
K_c = \prod_i \left(\frac{c_i}{c^{\circ}}\right)^{\nu_i} \qquad (\text{for a liquid solution})
\]

\(K_c\) is the equilibrium constant *expressed in terms of concentrations* (often called the “concentration equilibrium constant”).  

Because \(c^{\circ}=1\;\text{mol·L}^{-1}\) is a unit, the factor \((c^{\circ})^{\sum \nu_i}\) is unity, so we can simply write  

\[
K_c = \prod_i c_i^{\nu_i}\quad\text{(if the solution behaves ideally)}.
\]

---

### 2.4  Final relation between \(\Delta G\) and \(K_c\) for any composition  

Returning to Eq. (4) but **not** forcing equilibrium, keep the product of activities as it appears:

\[
\Delta G = \Delta G^{\circ}+RT\ln\!\left(\prod_i a_i^{\nu_i}\right)
\]

Replace the product of activities by the definition of the *instantaneous* equilibrium constant \(Q\) (the reaction quotient):

\[
Q \equiv \prod_i a_i^{\nu_i}
\]

Thus

\[
\boxed{\Delta G = \Delta G^{\circ}+RT\ln Q } \tag{6}
\]

When the system **is at equilibrium**, \(Q=K\) and Eq. (6) reduces to the earlier result \(\Delta G=0\).

If we are dealing with an *ideal* liquid solution, we may replace activities by concentrations:

\[
Q \;\approx\; \prod_i \left(\frac{c_i}{c^{\circ}}\right)^{\nu_i}
          \equiv K_c
\]

Hence for an ideal (or sufficiently dilute) solution we obtain the familiar expression

\[
\boxed{\displaystyle \Delta G = \Delta G^{\circ}+RT\ln K_c } \tag{7}
\]

Equation (7) is exactly the same form as for gases; the only difference lies in **how** the activities are related to measurable quantities (partial pressures for gases, molar concentrations for liquids).

---

### 2.5  Summary of the logical chain  

| Step | What we used | Result |
|------|--------------|--------|
| 1.   | Chemical potential definition (Eq. 1) | \(\mu_i = \mu_i^{\circ}+RT\ln a_i\) |
| 2.   | Reaction Gibbs energy (Eq. 2) | \(\Delta G = \sum_i \nu_i\mu_i\) |
| 3.   | Insert (1) into (2) → separate standard part | \(\Delta G = \Delta G^{\circ}+RT\ln\!\prod a_i^{\nu_i}\) |
| 4.   | Define reaction quotient \(Q = \prod a_i^{\nu_i}\) | \(\Delta G = \Delta G^{\circ}+RT\ln Q\) |
| 5.   | At equilibrium \(\Delta G=0\) → define \(K = Q_{\text{eq}}\) | \(K = \exp(-\Delta G^{\circ}/RT)\) |
| 6.   | Choose solution standard state (1 M) → activity ≈ concentration | \(K_c = \prod (c_i/c^{\circ})^{\nu_i}\) |
| 7.   | Replace \(Q\) by \(K_c\) for an ideal solution | \(\Delta G = \Delta G^{\circ}+RT\ln K_c\) |

---

## 3.  Final answer  

For a reaction occurring in a **liquid solution** (ideal or sufficiently dilute) the Gibbs free‑energy change at any composition is  

\[
\boxed{\displaystyle \Delta G = \Delta G^{\circ}+RT\ln K_c}
\]

where  

* \(\Delta G^{\circ}\) – standard Gibbs energy change (all solutes at the standard state of 1 mol L\(^{-1}\)).  
* \(K_c\) – equilibrium constant expressed in terms of molar concentrations:  

\[
K_c = \prod_i \left(\frac{c_i}{c^{\circ}}\right)^{\nu_i}\quad\text{with }c^{\circ}=1\;\text{M}
\]

If the solution is not perfectly ideal, the exact form uses **activities**:

\[
\Delta G = \Delta G^{\circ}+RT\ln\!\left(\prod_i a_i^{\nu_i}\right),
\qquad a_i = \gamma_i\frac{c_i}{c^{\circ}}
\]

and the same derivation leads to \(\Delta G = \Delta G^{\circ}+RT\ln K\) with \(K\) defined using activities.

---

## 4.  Common mistakes (and how to avoid them)

| Mistake | Why it’s wrong | How to correct it |
|---------|----------------|-------------------|
| **Treating \(K_c\) as a pure number without the standard‑state reference** | The equilibrium constant is dimensionless; ignoring the 1 M (or 1 bar) reference gives an apparent unit mismatch. | Always write activities as ratios to the standard state: \(a_i = c_i/c^{\circ}\). The factor \(c^{\circ}=1\;\text{M}\) makes \(K_c\) dimensionless. |
| **Using concentrations directly for a non‑ideal solution** | In real solutions the activity coefficient \(\gamma_i\neq 1\); substituting \(c_i\) leads to quantitative error. | Include \(\gamma_i\): \(a_i = \gamma_i c_i/c^{\circ}\). If the solution is sufficiently dilute, \(\gamma_i\approx 1\) and the approximation is justified. |
| **Confusing \(K_c\) with the reaction quotient \(Q\)** | \(K_c\) is the value **at equilibrium**; \(Q\) is the instantaneous ratio of activities. Mixing them obscures the condition \(\Delta G = 0\). | Keep the notation distinct: \(Q = \prod a_i^{\nu_i}\) (any composition), \(K_c = Q_{\text{eq}}\). |
| **Assuming the same derivation works for solids or pure liquids without modification** | Pure phases have activities fixed at 1, so they do not appear in the expression. | Omit pure solids or liquids from the product; they contribute \(\nu_i\mu_i^{\circ}\) to \(\Delta G^{\circ}\) but no concentration term. |
| **Skipping the step where \(\ln(\prod a_i^{\nu_i}) = \sum \nu_i \ln a_i\)** | The logarithm property is essential; forgetting it leads to algebraic errors. | Write the product explicitly, then apply \(\ln(ab)=\ln a + \ln b\) repeatedly, or remember the compact form \(\ln\prod a_i^{\nu_i}\). |
| **Using the gas‑phase standard pressure (1 bar) for a solution** | The standard state for solutes is 1 M, not 1 bar. Mixing standards changes \(\Delta G^{\circ}\). | Keep the standard state consistent: 1 M for solutes, 1 bar for gases, pure liquid/solid = 1. |

By following the derivation step‑by‑step and watching out for these pitfalls, the origin of the equation \(\Delta G = \Delta G^{\circ}+RT\ln K_c\) for liquid solutions becomes clear and fully justified.

*Original question: [Thermodynamic Equilibrium Constant derivation for liquid solutions](https://chemistry.stackexchange.com/questions/195988/thermodynamic-equilibrium-constant-derivation-for-liquid-solutions) on Chemistry Stack Exchange, licensed CC BY-SA.*

{% endraw %}
