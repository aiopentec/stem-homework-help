---
layout: question
title: Is the surrogate isothermal flash for an adiabatic flash unique?
author: StemFix Bot
category: chemistry
subject: chemistry
description: 'Step-by-step chemistry solution: Is the surrogate isothermal flash for
  an adiabatic flash unique?'
tags:
- chemistry
---

{% raw %}
*As an Amazon Associate, I earn from qualifying purchases.* For more practice problems like this, see [Schaum's Outline of College Chemistry, 10th Edition](https://www.amazon.com/dp/007181082X?tag=aiopentec20-20).

---

## 1.  What the question is really asking  

You have two inlet streams, **S₁** and **S₂**, that are mixed adiabatically (no heat is added or removed) at a common pressure **P**.  
The mixture leaves the mixer as a single stream **S′** that will later “flash’’ into a vapor stream **V** and a liquid stream **L** while staying at the same pressure **P**.

Because the mixer is adiabatic, the only way to determine the final thermodynamic state of **S′** is to satisfy **both**

* the **Rachford–Rice equation (RRE)** – which tells you, for any guessed temperature **T**, what vapor fraction **β(T)** would be in equilibrium at that **T** and **P**, **and**
* the **overall energy balance** – which forces the enthalpy of the equilibrium split (liquid + vapor) to equal the total enthalpy that entered the mixer.

The usual engineering practice is therefore an **iterative “isothermal‑flash surrogate’’**:

1. Guess a temperature **T**.  
2. Solve the RRE at (**P**, **T**) → obtain **β(T)**.  
3. Compute the enthalpy of the split streams (using β(T) and the K‑values).  
4. Compare that enthalpy with the known inlet enthalpy; adjust **T** and repeat.

The **core question** is:

> **Does this procedure always converge to a *single* (unique) solution, or could there be two different temperatures (and thus two different equilibrium splits) that both satisfy the energy balance?**  

In other words: *Is the surrogate isothermal flash for an adiabatic flash unique?*  

---

## 2.  Full step‑by‑step analysis  

Below we work under the standard assumptions stated in the problem:

* Ideal‑gas vapor phase and ideal‑solution liquid phase.  
* Constant pressure **P** throughout the flash.  
* Known overall mole fractions **zᵢ** (obtained by mixing the two inlet streams).  
* Known overall enthalpy **H\_in** (sum of the enthalpies of the two inlet streams).  
* Known temperature‑dependent K‑values **Kᵢ(T)** (e.g. from Wilson, NRTL, etc.).  

### 2.1  Write the two governing equations  

1. **Rachford–Rice (mass‑balance) equation** – for any temperature **T**  

   \[
   f(T,\beta)=\sum_{i=1}^{N}\frac{z_i\bigl(K_i(T)-1\bigr)}{1+\bigl(K_i(T)-1\bigr)\beta}=0
   \tag{1}
   \]

   For a fixed **T**, (1) is a *monotonic* function of **β** that has a single root in the interval \([0,1]\) (provided at least one component is more volatile than the other). Hence for every **T** we obtain a **unique** vapor fraction **β(T)**.

2. **Energy‑balance equation** – the enthalpy of the equilibrium split must equal the inlet enthalpy  

   \[
   H_{\text{calc}}(T) \equiv \beta(T) H_V(T) + \bigl[1-\beta(T)\bigr] H_L(T) = H_{\text{in}}
   \tag{2}
   \]

   where  

   \[
   H_V(T)=\sum_i y_i(T) \, \bar h_i^{\,V}(T) ,\qquad 
   H_L(T)=\sum_i x_i(T) \, \bar h_i^{\,L}(T)
   \]

   and the equilibrium compositions are  

   \[
   y_i(T)=\frac{K_i(T)z_i}{1+\bigl(K_i(T)-1\bigr)\beta(T)},\qquad
   x_i(T)=\frac{z_i}{1+\bigl(K_i(T)-1\bigr)\beta(T)} .
   \]

   The molar enthalpies \(\bar h_i^{\,V},\; \bar h_i^{\,L}\) are smooth, monotonic functions of **T** for ideal phases (they are linear in **T** if constant‑Cp is assumed).

### 2.2  Reduce the problem to a single scalar function  

Define a **residual function** that measures the mismatch between the calculated and the known enthalpy:

\[
\Phi(T) \equiv H_{\text{calc}}(T) - H_{\text{in}} .
\tag{3}
\]

Finding the adiabatic flash state is therefore equivalent to solving  

\[
\boxed{\Phi(T)=0}
\]

with **T** the only unknown.  

All the other quantities (β, xᵢ, yᵢ, H\_V, H\_L) are *functions of T* obtained from the steps above.

### 2.3  Prove that \(\Phi(T)\) is monotonic  

We need to show that **Φ(T)** is strictly monotonic (either always increasing or always decreasing) over the physically relevant temperature range \([T_{\min},T_{\max}]\). If that holds, the equation \(\Phi(T)=0\) can have at most one root → uniqueness.

#### 2.3.1  Derivative of β(T)  

From the implicit function theorem applied to (1):

\[
\frac{d\beta}{dT}= -\frac{\partial f/\partial T}{\partial f/\partial \beta}.
\]

*The denominator* \(\partial f/\partial \beta\) is **negative** because each term in (1) has the form  

\[
\frac{z_i (K_i-1)}{\bigl[1+(K_i-1)\beta\bigr]^2}
\]

which is positive; the sum multiplied by a minus sign gives a negative denominator.  

*The numerator* \(\partial f/\partial T\) contains \(\partial K_i/\partial T\). For most real components, the K‑value **decreases with temperature** (the more volatile component becomes relatively less volatile as temperature rises). Hence \(\partial K_i/\partial T <0\) for the lighter components and \(>0\) for the heavier ones, but the net sum is **negative** for a typical binary or multicomponent mixture that actually flashes. Consequently  

\[
\frac{d\beta}{dT}>0 .
\]

*Interpretation*: As the guessed temperature rises, the equilibrium vapor fraction **β** also rises.

#### 2.3.2  Derivative of the enthalpy term  

Write (2) as  

\[
H_{\text{calc}}(T)=\beta(T) \sum_i y_i(T) \bar h_i^{V}(T) 
               + \bigl[1-\beta(T)\bigr] \sum_i x_i(T) \bar h_i^{L}(T).
\]

Both \(\bar h_i^{V}(T)\) and \(\bar h_i^{L}(T)\) are **increasing** functions of **T** (positive heat capacities). The compositions \(x_i, y_i\) are also smooth functions of **T** (through K‑values and β). Differentiating \(H_{\text{calc}}(T)\) gives three positive contributions:

1. **Direct temperature rise of the pure‑component enthalpies** → positive.  
2. **Increase of β with T** → more vapor (usually higher enthalpy) → positive.  
3. **Shift of compositions toward the more volatile species** (because K‑values move) → also raises the mixture enthalpy (vapor is richer in low‑boiling, high‑enthalpy species).  

Hence  

\[
\frac{d H_{\text{calc}}}{dT} \;>\; 0 \qquad\text{for all } T\text{ in the flashing region}.
\]

Since \(H_{\text{in}}\) is a constant,  

\[
\frac{d\Phi}{dT}= \frac{d H_{\text{calc}}}{dT}>0 .
\]

Thus **Φ(T) is strictly increasing**.

### 2.4  Existence of a root  

Because the mixture is **adiabatically mixed**, the inlet enthalpy **H\_in** must lie between the enthalpy of the *all‑liquid* state (β = 0) and the *all‑vapor* state (β = 1) evaluated at the same pressure. Define  

\[
\Phi_{\text{liq}} \equiv H_{\text{calc}}(T_{\text{liq}})-H_{\text{in}},\qquad
\Phi_{\text{vap}} \equiv H_{\text{calc}}(T_{\text{vap}})-H_{\text{in}},
\]

where \(T_{\text{liq}}\) is the temperature at which the RRE gives β = 0 (the bubble‑point temperature for the overall composition) and \(T_{\text{vap}}\) the temperature at which β = 1 (the dew‑point temperature).  

* At **T = T\_liq** we have β = 0 ⇒ \(H_{\text{calc}} = H_L\). Since the inlet mixture contains some vapor‑forming energy, \(H_{\text{in}} > H_L\) and therefore \(\Phi_{\text{liq}} < 0\).  
* At **T = T\_vap** we have β = 1 ⇒ \(H_{\text{calc}} = H_V\). Because the inlet mixture cannot have more enthalpy than a fully vaporized stream at the same pressure, \(H_{\text{in}} < H_V\) and \(\Phi_{\text{vap}} > 0\).

Consequently  

\[
\Phi(T_{\text{liq}}) < 0 < \Phi(T_{\text{vap}}).
\]

A continuous, strictly increasing function that changes sign must cross zero **exactly once** (Intermediate Value Theorem).  

Hence **there exists a unique temperature T\* that satisfies Φ(T\*) = 0**, and the corresponding β\* and equilibrium compositions are unique as well.

### 2.5  Summary of the logical chain  

| Step | What we prove | Consequence |
|------|---------------|-------------|
| 1.   | For any fixed T, the RRE (1) has a single root β(T) in [0,1] | Vapor fraction is a well‑defined function of T |
| 2.   | β(T) is monotonic increasing with T (dβ/dT > 0) | Higher temperature → more vapor |
| 3.   | The mixture enthalpy \(H_{\text{calc}}(T)\) is strictly increasing with T | The residual Φ(T) is monotonic |
| 4.   | Φ(T) is negative at the bubble‑point temperature and positive at the dew‑point temperature | Φ(T) must cross zero |
| 5.   | Because Φ(T) is continuous and monotonic, the crossing occurs **once** | **Unique solution** for the adiabatic flash |

---

## 3.  Final answer  

**Yes.**  
Under the usual assumptions of ideal liquid/vapor phases, known K‑values, and a single pressure, the surrogate isothermal‑flash iteration converges to a **single, unique** thermodynamic state for the adiabatic flash. The uniqueness follows from:

* the Rachford–Rice equation giving a unique vapor fraction for each temperature,
* the monotonic increase of the calculated equilibrium enthalpy with temperature, and
* the fact that the inlet enthalpy always lies between the enthalpy of the all‑liquid and all‑vapor limits.

Therefore the pair \((T^\*,\beta^\*)\) that satisfies both the RRE and the overall energy balance is unique; no second temperature can produce the same total enthalpy while also meeting phase‑equilibrium constraints.

---

## 4.  Common mistakes when tackling this type of problem  

| Mistake | Why it is wrong | How to avoid it |
|---------|----------------|-----------------|
| **Assuming β is independent of T.** | β is defined by the RRE; it changes with temperature because K‑values change. | Always solve the RRE for β *after* picking a temperature; treat β(T) as a function. |
| **Treating the enthalpy balance as linear in T.** | The enthalpy of a mixture involves both temperature‑dependent pure‑component enthalpies and composition changes (via K‑values). | Keep the full expression (2) and differentiate it; note the three positive contributions to dH/dT. |
| **Neglecting the sign of ∂f/∂β.** | A wrong sign leads to an incorrect conclusion about monotonicity of β(T). | Write out ∂f/∂β explicitly; it is negative because each term is a positive fraction divided by a squared denominator. |
| **Checking only one temperature limit (e.g., only bubble point).** | You need both limits to guarantee that Φ changes sign. | Evaluate Φ at both the bubble‑point (β = 0) and the dew‑point (β = 1) temperatures. |
| **Assuming ideal‑gas heat capacities are zero.** |

*Original question: [Is the surrogate isothermal flash for an adiabatic flash unique?](https://chemistry.stackexchange.com/questions/195939/is-the-surrogate-isothermal-flash-for-an-adiabatic-flash-unique) on Chemistry Stack Exchange, licensed CC BY-SA.*

{% endraw %}
