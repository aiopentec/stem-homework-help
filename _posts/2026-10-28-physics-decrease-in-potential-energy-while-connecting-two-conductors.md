---
layout: question
title: Decrease in potential energy while connecting two conductors
author: StemFix Bot
category: physics
subject: physics
description: 'Step-by-step physics solution: Decrease in potential energy while connecting
  two conductors'
tags:
- physics
---

{% raw %}
*As an Amazon Associate, I earn from qualifying purchases.* For more practice problems like this, see [Schaum's Outline of College Physics, 12th Edition](https://www.amazon.com/dp/1259587398?tag=aiopentec20-20).

---

### 1. Restate What’s Being Asked in Plain Language

When two charged conducting spherical shells are connected by a conducting wire, charge flows until both spheres reach the same electric potential. During this process, the total electrostatic potential energy of the system decreases. 

The student is asking: **If the connecting wire has zero resistance ($R = 0$), how can energy be dissipated as heat if Joule's law ($H = I^2 R t$) gives zero heat? Where does the lost potential energy actually go?**

---

### 2. Step-by-Step Derivation and Explanation

#### Step 1: Analyze the Energy State Before and After Connection
Let two conducting spherical shells of radii $R_1$ and $R_2$ carry initial charges $Q_1$ and $Q_2$, respectively, and be placed far apart from each other (so we can ignore mutual capacitance effects).

*   **Initial Potential Energy ($U_i$):**
    $$U_i = \frac{1}{2} \frac{Q_1^2}{4\pi\varepsilon_0 R_1} + \frac{1}{2} \frac{Q_2^2}{4\pi\varepsilon_0 R_2}$$

*   **Final State:**
    When connected by a wire, charge flows until their electric potentials are equal ($V_1 = V_2 = V_f$). Let the new charges be $q_1$ and $q_2$, such that total charge is conserved:
    $$q_1 + q_2 = Q_1 + Q_2$$

*   **Final Potential Energy ($U_f$):**
    $$U_f = \frac{1}{2} \frac{q_1^2}{4\pi\varepsilon_0 R_1} + \frac{1}{2} \frac{q_2^2}{4\pi\varepsilon_0 R_2}$$

When you compute $\Delta U = U_f - U_i$, you find that $\Delta U < 0$ (energy is always lost/decreases), regardless of whether $R = 0$ in the wire.

#### Step 2: Address the Paradox of Zero Resistance ($R = 0$)
The student's paradox relies on Joule's heating formula: 
$$E_{\text{heat}} = \int I^2 R \, dt$$
If $R = 0$, then $E_{\text{heat}} = 0$. How is energy lost if no heat is generated in the wire?

The resolution lies in the fact that **real macroscopic wires always have inductance ($L$) and/or emission properties, and idealizing $R = 0$ in an electrodynamics problem creates a mathematical discontinuity.** 

Let us look at what physically happens when $R \to 0$:
1.  **Electromagnetic Radiation (The True Sink):** 
    When charges accelerate through the connecting wire from one sphere to the other, they constitute a time-varying electric current ($I(t)$). According to Maxwell’s equations, **accelerating charges radiate electromagnetic waves**. 
    
    Even if the resistance $R$ is strictly zero, the circuit possesses self-inductance ($L$). When the switch is closed, an LC-like oscillation occurs. The charge sloshes back and forth, but because energy is constantly carried away into space as **electromagnetic radiation (radio waves/photons)**, the oscillation dampens until the system settles into its final electrostatic equilibrium. The "missing" potential energy is radiated away into the surrounding space.

2.  **Taking the Limit as $R \to 0$:**
    What if we assume an ideal superconducting wire ($R = 0$) in a universe with no radiative losses (or instantaneous connection)? 
    
    If $R = 0$ and we ignore radiation, the current pulse is infinitely high ($I \to \infty$) for an infinitely short time ($\Delta t \to 0$). The product $I^2 R$ becomes a Dirac delta-like spike. Mathematically, the limit of $I^2 R$ as $R \to 0$ depends on how fast $I$ goes to infinity. In a real circuit, as $R$ decreases, the peak current increases, and **100% of the lost potential energy is converted into electromagnetic radiation (photons)** rather than Joule heat. 

---

### 3. Final Answer

The "lost" electrostatic potential energy is **not lost to Joule heating if the wire has zero resistance; instead, it is radiated away into space as electromagnetic waves (photons)** due to the acceleration of charges through the connecting wire. 

As charge rushes from one conductor to the other, the changing current creates a transient electromagnetic field. Even with zero resistance ($R=0$), the system cannot settle into its new potential without shedding excess energy, which leaves the system in the form of radiation.

---

### 4. Common Mistakes

*   **Assuming $R = 0$ means no energy loss:** Students often memorize $H = I^2Rt$ and assume that zero resistance means zero energy loss from the circuit. They forget that electrical energy can leave a circuit via *radiation* (Poynting vector), not just heat.
*   **Neglecting inductance and dynamics:** Treating the connection as a purely static problem. Energy conservation requires looking at the *process* of charge transfer (dynamics), where charges accelerate, rather than just comparing the initial and final static states.

*Original question: [Decrease in potential energy while connecting two conductors](https://physics.stackexchange.com/questions/877286/decrease-in-potential-energy-while-connecting-two-conductors) on Physics Stack Exchange, licensed CC BY-SA.*

{% endraw %}
