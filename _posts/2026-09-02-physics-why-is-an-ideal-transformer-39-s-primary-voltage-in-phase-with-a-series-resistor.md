---
layout: question
title: Why is an ideal transformer&#39;s primary voltage in phase with a series resistor
  for a resistive load?
author: StemFix Bot
category: physics
subject: physics
description: 'Step-by-step physics solution: Why is an ideal transformer&#39;s primary
  voltage in phase with a series resistor for a resistive load?'
tags:
- physics
---

{% raw %}
*As an Amazon Associate, I earn from qualifying purchases.* For more practice problems like this, see [Schaum's Outline of College Physics, 12th Edition](https://www.amazon.com/dp/1259587398?tag=aiopentec20-20).

---

## 1.  What the question is really asking  

A student has drawn the following circuit  

```
      Vs ──┬── Rs ──(primary winding)───┬───   (ideal transformer)
           │                         │
           └─────────────────────────┘
```

* The primary winding is part of an **ideal transformer** (no winding resistance, perfect magnetic coupling).  
* The secondary is terminated by a **purely resistive load** \(R_{\text L}\).  
* Because the resistor \(R_s\) is in series with the primary, the student observes that the voltage across the resistor, \(V_R\), is **in phase** with the primary current \(I_1\).  
* The textbook says the primary‑winding voltage \(V_1\) is also in phase with \(I_1\), so that the source voltage is just the scalar sum  

\[
V_s = V_R + V_1 .
\]

The student then wonders:

> A lone inductor always makes its voltage **lead** the current by \(90^{\circ}\) (\(v = L\,\frac{di}{dt}\)).  
> Why doesn’t the primary winding of the transformer behave the same way?

In other words: **Why isn’t the voltage across the primary winding 90° out of phase with the current, even though the winding is an inductor?**  

---

## 2.  Full step‑by‑step analysis  

### 2.1  Basic equations of an ideal transformer  

For an ideal transformer with \(N_1\) primary turns and \(N_2\) secondary turns  

| Quantity | Expression |
|----------|------------|
| **Flux linkage** \(\Phi(t)\) (same for both windings) | — |
| Primary induced emf | \(e_1(t)= N_1\frac{d\Phi}{dt}\) |
| Secondary induced emf | \(e_2(t)= N_2\frac{d\Phi}{dt}\) |
| Voltage–turns ratio (holds for the *induced* emfs) | \(\displaystyle \frac{e_1}{e_2}= \frac{N_1}{N_2}\) |
| Magnetising (no‑load) current | \(I_m = \frac{e_1}{j\omega L_m}\) (lags \(e_1\) by \(90^{\circ}\)) |
| Reflected secondary current | \(I_{\text{ref}} = \frac{N_2}{N_1}\,I_2\) (in phase with the secondary voltage) |

\(L_m\) is the **magnetising inductance** of the core.  
The *total* primary current is the algebraic sum  

\[
I_1 = I_m + I_{\text{ref}} .
\tag{1}
\]

### 2.2  What happens when the secondary is a resistive load  

If the secondary is terminated by a resistor \(R_L\),

\[
I_2 = \frac{e_2}{R_L}, \qquad
e_2 = \frac{N_2}{N_1} e_1 .
\]

Hence the reflected current is  

\[
I_{\text{ref}} = \frac{N_2}{N_1} I_2
                = \frac{N_2}{N_1}\,\frac{e_2}{R_L}
                = \frac{N_2^2}{N_1^2}\,\frac{e_1}{R_L}.
\tag{2}
\]

Notice that **\(I_{\text{ref}}\) is **in phase** with the primary emf \(e_1\)** because the secondary load is purely resistive.

### 2.3  Voltage across the series resistor  

The series resistor sees the **total** primary current \(I_1\).  
Its voltage is therefore  

\[
V_R = I_1 R_s,
\tag{3}
\]

which is **exactly in phase** with the current \(I_1\).

### 2.4  Voltage across the primary winding  

KVL around the source loop gives  

\[
V_s = V_R + V_1 .
\tag{4}
\]

Because the winding itself has **zero ohmic resistance**, the only voltage that can appear across it is the *induced emf* \(e_1\).  
Thus  

\[
V_1 = e_1 .
\tag{5}
\]

Now, what is the phase of \(e_1\) relative to the **total** current \(I_1\)?

From (1) we have two components of current:

* \(I_m\) lags \(e_1\) by \(90^{\circ}\) (purely inductive).
* \(I_{\text{ref}}\) is **in phase** with \(e_1\) (purely resistive).

Consequently the vector sum (1) is **not** 90° out of phase with \(e_1\); its angle is somewhere between \(0^{\circ}\) and \(-90^{\circ}\) depending on how large the load is compared with the magnetising inductance.  

If the load is heavy (large \(I_{\text{ref}}\)), the current is almost in phase with \(e_1\).  
If the load is light (small \(I_{\text{ref}}\)), the current is closer to lagging by 90°.

But **the voltage \(V_1\) itself is always exactly the same as the source voltage (minus the tiny drop across \(R_s\)).**  
Thus the primary voltage is *not* forced to lag the current by 90°; it simply follows whatever the source forces, while the current adjusts (splitting into magnetising and reflected parts) to satisfy both the core flux requirement and the load.

### 2.5  Why the simple “\(v = L\,di/dt\)” rule does **not** apply here  

The relation  

\[
v = L\frac{di}{dt}
\]

describes the voltage **across a *single* series inductance** whose current is the *only* current flowing through it.  
In an ideal transformer the primary winding is **not** a series inductance in that sense:

| Feature | Simple series inductor | Primary winding of ideal transformer |
|---------|------------------------|--------------------------------------|
| Voltage across element | \(v_L = L\frac{di}{dt}\) (leads \(i\) by 90°) | \(v_1 = e_1 = N_1\frac{d\Phi}{dt}\) (set by the applied source) |
| Current through element | The only current in the circuit | Total current = **magnetising + reflected** |
| Phase relationship between *this* voltage and *total* current | Fixed 90° lag | Variable; depends on load |

In other words, the primary winding’s **inductive reactance** is “hidden’’ inside the magnetic core. The **induced emf** (which we call the primary voltage) is *forced* by the source, not by the current through a discrete \(L\). The current reacts to that emf, splitting into two orthogonal components. Therefore the simple 90° rule does **not** dictate the phase between the applied primary voltage and the total primary current.

### 2.6  Putting it all together  

1. The source voltage appears across the series combination of \(R_s\) and the ideal winding.  
2. The resistor voltage \(V_R = I_1 R_s\) is in phase with the *total* current.  
3. The winding voltage \(V_1\) is the induced emf, which is **the same phasor as the source voltage (minus \(V_R\))**.  
4. Because the primary current contains a *load* component that is in phase with \(V_1\), the overall current is **not** 90° out of phase with the voltage.  
5. The classic \(v = L\,di/dt\) lag only applies to a *stand‑alone* inductor with no coupled secondary and no reflected current.

Hence the primary voltage of an ideal transformer **does not lag its current by 90°**; it is essentially in phase with the source, while the current’s phase depends on the balance between magnetising and reflected components.

---

## 3.  Final answer  

- In an ideal transformer the primary voltage is the **induced emf** \(e_1 = N_1 \, d\Phi/dt\).  
- This emf is forced by the source; it is therefore *in phase* with the source voltage (apart from the drop across the series resistor).  
- The primary current is the sum of a **magnetising current** (which lags the emf by 90°) and a **reflected load current** (which is in phase with the emf).  
- Because the reflected component exists whenever the secondary is

*Original question: [Why is an ideal transformer&#39;s primary voltage in phase with a series resistor for a resistive load?](https://physics.stackexchange.com/questions/875575/why-is-an-ideal-transformers-primary-voltage-in-phase-with-a-series-resistor-fo) on Physics Stack Exchange, licensed CC BY-SA.*

{% endraw %}
