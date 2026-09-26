---
layout: question
title: Mutual Pressure Between Gases at Different Pressure
author: StemFix Bot
category: chemistry
subject: chemistry
description: 'Step-by-step chemistry solution: Mutual Pressure Between Gases at Different
  Pressure'
tags:
- chemistry
---

{% raw %}
*As an Amazon Associate, I earn from qualifying purchases.* For more practice problems like this, see [Schaum's Outline of College Chemistry, 10th Edition](https://www.amazon.com/dp/007181082X?tag=aiopentec20-20).

---

## 1.  What the question is really asking  

We have two **different** gases (or the same gas at different conditions) that are initially kept apart by a rigid wall.  
* Gas 1 occupies a volume \(V_{1}\) and exerts a pressure \(p_{1}\).  
* Gas 2 occupies a volume \(V_{2}\) and exerts a pressure \(p_{2}\).

The wall is suddenly taken away, so the two samples can inter‑mix.  
The student wants to know:

*“When the two gases are in direct contact, what pressure does each gas feel from the other?  How can that ‘mutual pressure’ be expressed in terms of the original pressures \(p_{1}\) and \(p_{2}\)?”*  

In other words: after the wall disappears, what is the pressure of the **combined** system (the pressure that each side exerts on the other) in terms of the initial data?

---

## 2.  Step‑by‑step solution  

### 2.1  What is pressure, really?

*Pressure* \(p\) is defined as **force per unit area** that a gas exerts on a **physical surface** (or on an imaginary surface that we choose to analyse).  
It is a **scalar** quantity – it has magnitude but no direction.  
Newton’s third law tells us that the force the left side of an interface exerts on the right side is equal in magnitude and opposite in direction to the force the right side exerts on the left side.  
Because the forces act on the same area, the **pressures on the two sides of any chosen surface are equal at any instant**.

Therefore the “mutual pressure’’ we are looking for is simply the **pressure that exists at the interface after the gases have had time to equilibrate**.

### 2.2  What happens when the wall is removed?

1. **Immediately after removal** the two sides still have their original pressures. The higher‑pressure side pushes a compression (or shock) wave into the lower‑pressure side, while a rarefaction wave travels the other way.  
   - During this transient stage the pressure is not uniform; it varies with position and time.  
   - The force on each side is \((p_{\text{high}}-p_{\text{low}})A\), where \(A\) is the cross‑sectional area of the interface.

2. **After a short time** (a few sound‑travel times across the container) the waves have reflected from the container walls and the gas mixture settles into a **uniform, static state**.  
   - In that final equilibrium state the pressure is the same everywhere, and each infinitesimal surface inside the gas feels the same pressure from its neighbours.  
   - This uniform pressure is the “mutual pressure’’ the problem asks for.

### 2.3  Use the ideal‑gas law to obtain the equilibrium pressure  

Assume (as is customary for textbook problems) that both gases behave **ideally** and that the temperature \(T\) remains unchanged during the mixing (the container is thermally insulated and the mixing is rapid, so no heat is exchanged with the surroundings).  

| Quantity | Gas 1 | Gas 2 |
|----------|-------|-------|
| Initial pressure | \(p_{1}\) | \(p_{2}\) |
| Initial volume   | \(V_{1}\) | \(V_{2}\) |
| Number of moles  | \(n_{1}= \displaystyle\frac{p_{1}V_{1}}{RT}\) | \(n_{2}= \displaystyle\frac{p_{2}V_{2}}{RT}\) |

After the wall is gone the total volume is  

\[
V = V_{1}+V_{2}
\]

and the total amount of gas is  

\[
n = n_{1}+n_{2}= \frac{p_{1}V_{1}+p_{2}V_{2}}{RT}.
\]

Because the temperature is the same for the whole mixture, the **ideal‑gas equation** applied to the combined system gives

\[
p_{\text{mutual}} V = nRT.
\]

Insert the expression for \(n\):

\[
p_{\text{mutual}} (V_{1}+V_{2}) = 
\frac{p_{1}V_{1}+p_{2}V_{2}}{RT}\;RT
      = p_{1}V_{1}+p_{2}V_{2}.
\]

Finally, solve for the uniform pressure after mixing:

\[
\boxed{\,p_{\text{mutual}}=
\frac{p_{1}V_{1}+p_{2}V_{2}}{V_{1}+V_{2}}\, } \qquad\text{(Eq. 1)}
\]

#### Special cases  

* **Equal initial volumes** (\(V_{1}=V_{2}=V/2\))  

  \[
  p_{\text{mutual}} = \frac{p_{1}+p_{2}}{2}\quad\text{(simple arithmetic mean).}
  \]

* **One side occupies a much larger volume** (e.g. \(V_{2}\gg V_{1}\))  

  The term with the larger volume dominates, so the final pressure approaches the pressure that originally existed in the larger region.

* **If the gases are different species but at the same temperature**, Eq. 1 is still valid because the ideal‑gas law does not depend on chemical identity—only on total mole number.

### 2.4  Why the “max’’ you observed in a 1‑D simulation?

A naïve 1‑D code that updates the pressure on each cell by simply copying the larger of the two neighbour values will produce a pressure that looks like the **maximum** of the two initial pressures.  
That algorithm is **not** solving the physical equations (continuity, momentum, energy, and the equation of state); it is only imposing a rule that mimics a *shock moving into the low‑pressure side*.  
In a real gas the pressure behind the shock quickly relaxes to the uniform value given by Eq. 1, not to the initial high pressure.

---

## 3.  Final answer  

When two gases initially at pressures \(p_{1}\) and \(p_{2}\) and occupying volumes \(V_{1}\) and \(V_{2}\) are allowed to mix (no heat exchange, temperature unchanged), the **uniform pressure that each gas exerts on the other after equilibrium is reached** is  

\[
\boxed{p_{\text{mutual}}=
\frac{p_{1}V_{1}+p_{2}V_{2}}{V_{1}+V_{2}} }.
\]

If the two volumes are equal, this reduces to the simple arithmetic mean \((p_{1}+p_{2})/2\).  

The pressure is *not* the maximum of the two initial pressures, nor is it a vector sum; it is the weighted average dictated by the total number of moles and the total volume.

---

## 4.  Common Mistakes  

| Mistake | Why it’s wrong | How to avoid it |
|---------|----------------|-----------------|
| **Treating pressure as a vector** and adding the two pressures like forces. | Pressure is a scalar; only the *force* on a surface is a vector (force = pressure × area). | Remember “pressure = force per unit area”; only the forces on opposite sides of a chosen surface are opposite, not the pressures themselves. |
| **Taking the arithmetic mean regardless of volumes**. | The final pressure depends on how many moles each side contributes, i.e. on both pressure *and* volume. | Use the weighted average in Eq. 1; only when \(V_{1}=V_{2}\) does it become a simple mean. |
| **Assuming the pressure stays at the higher initial value**. | After the wall is removed a compression wave propagates, but the system relaxes to a uniform pressure lower than the original high pressure (unless the low‑pressure side is negligible). | Recognise that equilibrium pressure follows from conservation of mass (and energy) together with the equation of state. |
| **Ignoring temperature changes**. | Mixing can be adiabatic; if the two sides have different temperatures, the final temperature (and thus pressure) will differ from the initial values. | State the temperature assumption explicitly; if temperatures differ, solve the energy balance together with the ideal‑gas law. |
| **Using a 1‑D “max‑copy’’ update rule in a simulation**. | That rule does not satisfy the fluid‑dynamic equations; it artificially forces the pressure to stay at the larger value. | Implement the full set of Navier–Stokes (or at least the Euler) equations with an appropriate equation of state. |

Keeping these points in mind will help you correctly predict the pressure that the two gases exert on each other after the separator is removed.

*Original question: [Mutual Pressure Between Gases at Different Pressure](https://chemistry.stackexchange.com/questions/196017/mutual-pressure-between-gases-at-different-pressure) on Chemistry Stack Exchange, licensed CC BY-SA.*

{% endraw %}
