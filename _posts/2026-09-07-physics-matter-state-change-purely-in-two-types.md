---
layout: question
title: Matter state change purely in two types
author: StemFix Bot
category: physics
subject: physics
description: 'Step-by-step physics solution: Matter state change purely in two types'
tags:
- physics
---

{% raw %}
*As an Amazon Associate, I earn from qualifying purchases.* For more practice problems like this, see [Schaum's Outline of College Physics, 12th Edition](https://www.amazon.com/dp/1259587398?tag=aiopentec20-20).

---

## 1.  What the question is really asking  

The student is wondering whether **gravity alone** can turn a solid (for example a metal rod) into a liquid.  
In other words:

*If a planet has a surface gravity that is millions of times larger than Earth’s, will a piece of metal that is solid on Earth melt and flow like water **without any heating**?*  

We have to decide, using basic physics and real‑world material data, whether a *purely gravitational* pressure can change the phase of a substance.

---

## 2.  Step‑by‑step analysis  

### 2.1  Pressure produced by gravity  

The pressure that gravity can exert on a material comes from the **weight of the material that lies above it**.  
For a horizontal slab of thickness \(h\) and density \(\rho\),

\[
P = \rho \, g \, h .
\]

- \(\rho\) – mass density (kg m⁻³)  
- \(g\) – gravitational acceleration at the planet’s surface (m s⁻²)  
- \(h\) – depth measured vertically (m)  

On the **surface of a planet** the only material sitting on top of a small metal rod is the rod itself.  
If the rod has a cross‑sectional area \(A\) and length \(L\),

\[
\text{stress at the bottom of the rod}= \frac{\text{weight}}{A}= \frac{\rho A L g}{A}= \rho L g .
\]

Thus the pressure that the rod can feel because of its own weight is simply  

\[
P_{\text{self}} = \rho L g .
\]

*Even on a planet with a huge surface gravity, the pressure inside a modest‑size object is limited by its own height.*

---

### 2.2  How large must the pressure be to melt a typical metal?  

Phase diagrams give the relationship between **melting temperature \(T_m\)** and **pressure \(P\)**.  
For a first‑order transition the Clapeyron equation applies:

\[
\frac{dP}{dT}= \frac{\Delta S}{\Delta V}
            = \frac{L_{\text{fusion}}}{T_m \,\Delta V},
\]

where  

* \(L_{\text{fusion}}\) – latent heat of fusion (J kg⁻¹)  
* \(\Delta V = V_{\text{liq}}-V_{\text{sol}}\) – volume change on melting (m³ kg⁻¹, usually *positive* for most metals).

A convenient rule of thumb (derived from tabulated data) is:

| Metal | \(T_{m,\,1\text{atm}}\) (K) | \(\frac{dT_m}{dP}\) (K GPa⁻¹) |
|-------|----------------------------|-------------------------------|
| Iron  | 1809                       | ≈ 15 K GPa⁻¹ |
| Aluminum | 933                    | ≈ 9 K GPa⁻¹ |
| Copper | 1358                     | ≈ 12 K GPa⁻¹ |

These numbers tell us that **raising the pressure by 1 GPa (≈10 000 atm) raises the melting point only by a few × 10 K**.  
Conversely, to *lower* the melting point (as the student imagined) the material would have to **shrink on melting** (negative \(\Delta V\)), which is rare for metals (it happens for water/ice, not for most solids).

**Conclusion from the data:**  
To melt a metal at *room temperature* (≈ 300 K) by pressure alone would require pressures of order **hundreds of gigapascals** – comparable to the pressure at the centre of the Earth (≈ 360 GPa).  

---

### 2.3  How big is the pressure from a gigantic surface gravity?  

Take a “super‑Earth” with surface gravity  

\[
g = 10^6 \, g_{\oplus} = 10^6 \times 9.81\ \text{m s}^{-2}= 9.8\times10^6\ \text{m s}^{-2}.
\]

Assume a metal rod of **density** \(\rho = 8\,000\ \text{kg m}^{-3}\) and **length** \(L = 1\ \text{m}\).

\[
P_{\text{self}} = \rho L g = 8\times10^{3}\,\text{kg m}^{-3}\times 1\ \text{m}\times 9.8\times10^{6}\ \text{m s}^{-2}
                 \approx 8\times10^{10}\ \text{Pa}= 80\ \text{GPa}.
\]

80 GPa is **far below** the several‑hundred‑GPa pressure that would be needed to melt iron at 300 K.  
Even if we make the rod 10 m tall, the pressure only rises to ≈ 800 GPa, which is comparable to the Earth’s core pressure; but a 10‑m rod would collapse under its own weight long before reaching that pressure, and the material would be **compressed and heated** during the collapse.

**Key point:** *The pressure created by gravity at the surface of any realistic object is limited by the object’s own height. To reach the multi‑hundred‑GPa regime you need either enormous depths (planetary interiors) or an external confinement (diamond anvil cell), not just a stronger surface gravity.*

---

### 2.4  What actually happens deep inside massive planets?  

Inside a planet the **hydrostatic pressure** grows with depth:

\[
P(r) = \int_{r}^{R} \rho(r')\, g(r')\, dr'.
\]

At depths of several thousand kilometres the pressure can be **hundreds of GPa**, and the **temperature also rises** (adiabatic compression, radiogenic heating, etc.) to several thousand kelvin.  
Thus in planetary interiors we indeed find **solid iron behaving like a liquid** (the Earth's outer core) – but **both high pressure *and* high temperature** are responsible.  

Pure pressure alone, at a fixed low temperature, would not melt most metals.

---

### 2.5  Summarising the physics  

| Concept | What the student claimed | What physics tells us |
|---------|--------------------------|-----------------------|
| Gravity → pressure on a solid rod | “Millions‑times‑Earth gravity makes the rod melt” | Pressure from self‑weight = \(\rho L g\). Even with \(g =10^6 g_{\oplus}\) and \(L=1\) m we get ≈ 80 GPa, far too low to melt typical metals at room temperature. |
| Pressure → phase change | “Pressure alone can turn solid into liquid” | For most metals, the melting curve has a **positive slope** (higher pressure → higher melting temperature). You need *very* high pressure **and** high temperature to liquefy them. |
| Planetary interiors | “Matter behaves very differently because of gravity” | True, but the difference comes from *both* immense pressure **and** the associated temperature rise, not gravity alone. |

---

## 3.  Final answer  

- **Gravity itself does not change the phase of a material.**  
- A stronger surface gravity only increases the **stress** inside a body proportionally to its height. For realistic sizes this stress is at most a few × 10¹⁰ Pa, far below the hundreds of gigapascals required to melt most metals at ordinary temperatures.  
- In the deep interiors of very massive planets the pressure (and temperature) become high enough to cause solids to behave like liquids, but this is a **combined pressure‑temperature effect**, not a pure “gravity‑only” melting.  

**Therefore, a metal rod on the surface of a planet with a million‑times‑Earth gravity would **not** melt and flow like water purely because of the planet’s gravity.**  

---

## 4.  Common mistakes when tackling this type of problem  

| Mistake | Why it’s wrong | How to avoid it |
|--------|----------------|-----------------|
| **Confusing weight (a force) with pressure (force / area).** | The rod’s weight is \(mg\); the pressure it feels is \(mg/A\). For a thin rod the area is tiny, but the stress is limited by the rod’s own height, not by the planet’s \(g\) alone. | Always write the pressure as \(\rho L g\) (or \( \rho g h\) for a column) and keep track of units. |
| **Assuming that higher pressure always lowers the melting point.** | For most substances, especially metals, the melting curve slopes **upward**: higher pressure raises the melting temperature. Only substances that expand on melting (e.g., water) melt at lower pressures. | Look at a phase diagram or the sign of \(\Delta V\) in the Clapeyron equation. |
| **Neglecting the temperature rise that accompanies compression.** | Compressing a material adiabatically heats it; the temperature in planetary interiors is thousands of kelvin, which together with pressure causes melting. | Remember that the state of matter is a function of *both* pressure **and** temperature. |
| **Thinking that surface gravity directly translates into huge pressures on a small object.** | Surface gravity sets the weight per unit mass, but the pressure a small object experiences is limited by how much material sits above it (its own height). | Use the hydrostatic formula \(P = \rho g h\) and ask “what is \(h\)?” for the object in question. |
| **Using Earth‑sea‑level pressure (1 atm) as a baseline for all planets.** | On a planet with stronger gravity, the ambient atmospheric pressure may be higher, but the *additional* pressure inside a solid comes from overlying material, not from the background atmosphere. | Distinguish between **external** (atmospheric) pressure and **internal** pressure due to self‑weight. |

Keep these pitfalls in mind whenever you evaluate whether gravity can change the phase of a material.

*Original question: [Matter state change purely in two types](https://physics.stackexchange.com/questions/875763/matter-state-change-purely-in-two-types) on Physics Stack Exchange, licensed CC BY-SA.*

{% endraw %}
