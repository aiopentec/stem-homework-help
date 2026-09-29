---
layout: question
title: Can two bodies be at thermal equilibrium while having different temperatures?
author: StemFix Bot
category: physics
subject: physics
description: 'Step-by-step physics solution: Can two bodies be at thermal equilibrium
  while having different temperatures?'
tags:
- physics
---

{% raw %}
*As an Amazon Associate, I earn from qualifying purchases.* For more practice problems like this, see [Schaum's Outline of College Physics, 12th Edition](https://www.amazon.com/dp/1259587398?tag=aiopentec20-20).

---

## 1. What the question is really asking  

> **Can two bodies be in thermal equilibrium while they have different temperatures?**

In plain language the problem is asking whether the condition “no net heat flows between the bodies” (thermal equilibrium) *must* force the bodies to have the same temperature, or whether there are circumstances in which the heat‑flow condition can be satisfied even though the two objects are at different temperatures.

---

## 2. Step‑by‑step answer  

### 2.1 Define the key concepts  

| Concept | Precise thermodynamic definition |
|---------|-----------------------------------|
| **Temperature** \(T\) | The intensive variable that is the derivative of the internal energy with respect to entropy at fixed volume and particle number: \(\displaystyle \frac{1}{T}= \left(\frac{\partial S}{\partial U}\right)_{V,N}\). For a macroscopic body that is internally equilibrated this number is uniform throughout the body. |
| **Thermal equilibrium (between subsystems)** | Two subsystems are said to be in thermal equilibrium **if, when they are placed in thermal contact, there is no net heat flow between them**. Equivalently, the combined isolated system has reached a state in which all macroscopic observables (including entropy) are stationary. |
| **Isolated composite system** | A set of bodies that together exchange no energy or matter with the outside world. The only possible internal interactions are those that are allowed (e.g., a conducting wall, a perfect insulator, etc.). |

> **Important:** The definition of thermal equilibrium refers to *the situation *that would occur *if* the subsystems were allowed to exchange heat. It does **not** require that they *are* able to exchange heat at the moment.

### 2.2 What happens when heat can be transferred  

If two bodies are placed in direct thermal contact (a conducting interface) then the Second Law tells us that heat will flow from the hotter to the colder body until their temperatures become equal. At that final state the net heat flow is zero, **and** the temperatures are equal:

\[
\text{(conducting contact)} \quad\Longrightarrow\quad T_1 = T_2 .
\]

Thus, *if* the bodies are **thermally coupled**, equality of temperature is a necessary condition for thermal equilibrium.

### 2.3 When heat cannot be transferred  

Consider now a situation in which the two bodies **cannot exchange heat** because of an ideal insulating barrier (or because they are separated by a vacuum with no radiative coupling). The composite system is still **isolated**: no energy can leave or enter the pair of bodies. Inside each body the usual internal processes (collisions, phonon scattering, etc.) quickly bring that body to its own internal equilibrium, giving it a well‑defined temperature \(T_1\) and \(T_2\).

Because the insulating wall forbids any heat flow, the condition “no net heat flow” is automatically satisfied, *regardless of the numerical values of \(T_1\) and \(T_2\)*. Consequently the composite system is already in thermal equilibrium even though the two temperatures differ.

> **Key point:** Thermal equilibrium is a statement about the *absence of a driving force for heat exchange* **if** exchange were possible. If exchange is prohibited by an infinite thermal resistance, the driving force (the temperature difference) cannot act, so equilibrium is reached instantly.

### 2.4 Concrete example  

| Element | Description |
|---------|-------------|
| Body A | A copper block at \(T_A = 300\ \text{K}\). |
| Body B | A glass block at \(T_B = 350\ \text{K}\). |
| Separation | A perfect vacuum gap together with a perfect mirror on each side, so that **no radiative, conductive, or convective heat transfer** can occur. |
| Whole system | Isolated from the environment (adiabatic walls). |

*Each block quickly becomes internally uniform in temperature.*  
*Because the gap is a perfect insulator, the net heat flow between A and B is **identically zero**.*  

Thus the pair (A + B) satisfies the definition of thermal equilibrium even though \(T_A \neq T_B\).

### 2.5 General statement  

- **If the bodies are thermally coupled (finite thermal conductance)** → thermal equilibrium **implies** equal temperatures.  
- **If the bodies are thermally isolated from each other (infinite thermal resistance)** → they can be in thermal equilibrium **with different temperatures**; the temperature difference is simply a *latent* driving force that cannot be expressed because the coupling is absent.

Therefore the answer to the original question is **YES** – two bodies can be in thermal equilibrium while having different temperatures, provided they are not able to exchange heat.

---

## 3. Final answer  

> **Yes.** Two bodies can be in thermal equilibrium while having different temperatures if they are thermally insulated from each other (i.e., there is no path for heat to flow). In that case the condition “no net heat flow” is automatically satisfied, even though the bodies possess distinct temperatures. If a heat‑conducting path exists, thermal equilibrium forces the temperatures to become equal.  

---

## 4. Common Mistakes  

| Mistake | Why it’s wrong | How to avoid it |
|---------|----------------|-----------------|
| **Assuming “thermal equilibrium” automatically means “same temperature”.** | The definition involves *absence of net heat flow* **provided** heat exchange is possible. If the exchange path is blocked, the temperatures may differ. | Explicitly check whether a thermal coupling exists before concluding that temperatures must be equal. |
| **Confusing “isolated system” with “thermally isolated subsystems”.** | An isolated **composite** system can contain subsystems that cannot talk to each other thermally. | Distinguish between (i) the whole system being isolated from the environment, and (ii) the internal thermal conductance between its parts. |
| **Neglecting radiative heat transfer in a vacuum gap.** | Even a vacuum allows heat flow via radiation, so a “perfect” vacuum gap must be idealised as perfectly reflecting to truly block heat. | State the idealisation (perfectly reflecting surfaces, zero emissivity) when using a vacuum gap as an insulating barrier. |
| **Thinking that a temperature difference always drives a heat flow.** | The driving force exists, but if the conductance is zero the flow rate is zero. | Remember the linear law \( \dot Q = G (T_1-T_2) \). If \(G=0\), \(\dot Q = 0\) irrespective of the temperature difference. |
| **Mixing up “thermal equilibrium” with “mechanical equilibrium”.** | Mechanical equilibrium concerns forces/pressures, not heat. | Keep the definitions separate: thermal equilibrium ↔ no net heat flow; mechanical equilibrium ↔ no net force/pressure imbalance. |

By keeping these points in mind you can correctly analyse whether two bodies can share a thermal equilibrium state while maintaining different temperatures.

*Original question: [Can two bodies be at thermal equilibrium while having different temperatures?](https://physics.stackexchange.com/questions/876470/can-two-bodies-be-at-thermal-equilibrium-while-having-different-temperatures) on Physics Stack Exchange, licensed CC BY-SA.*

{% endraw %}
