---
layout: question
title: Can momentum be considered as the resistance of a force
author: StemFix Bot
category: physics
subject: physics
description: 'Step-by-step physics solution: Can momentum be considered as the resistance
  of a force'
tags:
- physics
---

{% raw %}
*As an Amazon Associate, I earn from qualifying purchases.* For more practice problems like this, see [Schaum's Outline of College Physics, 12th Edition](https://www.amazon.com/dp/1259587398?tag=aiopentec20-20).

---

## 1. What the question is really asking  

The student is wondering whether **linear momentum** \( \mathbf p = m\mathbf v \) can be interpreted as “the resistance of a force’’ – i.e. as something that tells us how hard it is for a force to change the motion of an object. In other words:

*Is momentum a measure of an object’s “resistance’’ to being acted on by a force?*  

We have to compare the role of momentum with the more familiar notion of **inertia** (the resistance to acceleration) and see whether the word “resistance of a force’’ is a correct description.

---

## 2. Step‑by‑step analysis  

### 2.1  Definitions  

| Quantity | Symbol | Definition | Units |
|----------|--------|------------|-------|
| Mass (inertia) | \(m\) | Amount of matter; a measure of how much a body resists acceleration | kg |
| Velocity | \(\mathbf v\) | Rate of change of position | m s\(^{-1}\) |
| Linear momentum | \(\mathbf p\) | Product of mass and velocity | kg·m s\(^{-1}\) |
| Force | \(\mathbf F\) | Interaction that changes momentum | N = kg·m s\(^{-2}\) |
| Impulse | \(\mathbf J\) | Time integral of force, \( \mathbf J = \int \mathbf F\,dt \) | N·s = kg·m s\(^{-1}\) |

### 2.2  Newton’s second law in its most general form  

Newton’s second law is **not** \( \mathbf F = m\mathbf a \) (that is a special case). The fundamental statement is  

\[
\boxed{\mathbf F = \frac{d\mathbf p}{dt}}
\]

i.e. a force tells us **how fast the momentum of a body changes**.

If the mass is constant, we can write  

\[
\frac{d\mathbf p}{dt}= \frac{d}{dt}(m\mathbf v)=m\frac{d\mathbf v}{dt}=m\mathbf a,
\]

and the familiar \( \mathbf F = m\mathbf a \) follows. But the *law itself* ties **force** directly to **change of momentum**, not to the momentum itself.

### 2.3  What does “resistance’’ mean?  

In everyday language, “resistance’’ to a force is usually identified with **inertia**: a larger mass means a smaller acceleration for the same applied force. Mathematically:

\[
\mathbf a = \frac{\mathbf F}{m}\quad\Longrightarrow\quad m = \frac{\mathbf F}{\mathbf a}.
\]

Thus **mass** is the proportionality constant that measures how much a given force is *opposed* by the object’s tendency to keep moving at its current velocity.

### 2.4  Momentum vs. inertia  

| Quantity | Depends on | What it tells us |
|----------|------------|------------------|
| Mass \(m\) | Property of the object alone | “How hard it is to accelerate the object” (inertia) |
| Momentum \(\mathbf p\) | Mass **and** the current velocity | “How much motion the object carries” (a state variable) |
| Force \(\mathbf F\) | External agent | “What is trying to change the momentum” |

- **Mass** is a *property* of the object; it is the same regardless of the object's motion.  
- **Momentum** changes when the object’s velocity changes; it is *not* a property that tells us how much a force is opposed, but rather *how much* momentum must be **added or removed** to change the state.

### 2.5  Impulse–momentum theorem  

Integrating Newton’s second law over a finite time interval \([t_1,t_2]\):

\[
\int_{t_1}^{t_2}\mathbf F\,dt = \Delta\mathbf p \equiv \mathbf p_2-\mathbf p_1 .
\]

This tells us:

- A **given impulse** (area under the force‑time curve) produces a **specific change in momentum**.  
- The *size* of the momentum before the impulse does not affect how much impulse is needed to achieve a particular *change*; only the *difference* \(\Delta\mathbf p\) matters.

Hence momentum itself is **not** a resistance; it is the *quantity that is being changed* by the impulse.

### 2.6  Example: Two objects with the same momentum but different masses  

- Object A: \(m_A = 1\; \text{kg},\; v_A = 10\; \text{m/s}\) → \(p_A = 10\; \text{kg·m/s}\).  
- Object B: \(m_B = 10\; \text{kg},\; v_B = 1\; \text{m/s}\) → \(p_B = 10\; \text{kg·m/s}\).

Both have the **same momentum**, yet their **resistance to a force** (i.e. their acceleration under the same force) is very different:

\[
a_A = \frac{F}{1\;\text{kg}}, \qquad a_B = \frac{F}{10\;\text{kg}}.
\]

The heavier object (B) accelerates ten times less for the same force, even though its momentum equals that of A. This demonstrates that *mass* (inertia), not momentum, quantifies resistance.

### 2.7  Summary of the logical chain  

1. **Force** → *causes* **change of momentum** (Newton’s 2nd law).  
2. **Mass** → *determines* how much **acceleration** a given force produces (inertial resistance).  
3. **Momentum** → *records* the current state of motion; it is **not** a property that limits the effect of a force.  

Therefore, **momentum cannot be correctly described as “the resistance of a force’’**. The correct phrase would be:

> *Mass* (or inertia) is the resistance of an object to changes in its motion caused by a force.  
> *Momentum* is the amount of motion that a force must add to or remove from the object.

---

## 3. Final answer  

- **Momentum** \( \mathbf p = m\mathbf v \) is a *state variable* that tells us how much motion an object currently possesses.  
- The *resistance* to a force – the tendency of an object to oppose acceleration – is measured by the **mass** (inertia), not by its momentum.  
- Hence momentum is **not** the resistance of a force; it is the quantity that a force changes.

---

## 4. Common Mistakes  

| Mistake | Why it’s wrong | Correct view |
|---------|----------------|--------------|
| **Equating “hard to change motion’’ with “hard to accelerate’’** | “Hard to change motion” can refer to either changing *velocity* (acceleration) or changing *momentum* (impulse). Confusing the two leads to treating momentum as inertia. | Distinguish: *Mass* quantifies resistance to acceleration; *Momentum* quantifies the current motion that must be altered. |
| **Assuming two bodies with equal momentum have equal resistance** | As shown in the example, equal momentum can arise from very different masses and velocities, giving very different accelerations under the same force. | Check the mass: resistance ∝ \(1/m\); momentum alone tells nothing about resistance. |
| **Using \( \mathbf F = m\mathbf a \) as the definition of force** | This form hides the underlying relationship \( \mathbf F = d\mathbf p/dt\) and obscures the role of momentum. | Remember the fundamental law \( \mathbf F = d\mathbf p/dt \); only the *change* in momentum is directly tied to force. |
| **Thinking that a larger momentum “stores’’ more resistance** | Momentum does not store a property; it is simply the product of mass and velocity at an instant. | Momentum is a bookkeeping quantity; resistance is stored in the mass (inertia). |

Keeping these distinctions clear prevents the misconception that momentum itself resists forces.

*Original question: [Can momentum be considered as the resistance of a force](https://physics.stackexchange.com/questions/875726/can-momentum-be-considered-as-the-resistance-of-a-force) on Physics Stack Exchange, licensed CC BY-SA.*

{% endraw %}
