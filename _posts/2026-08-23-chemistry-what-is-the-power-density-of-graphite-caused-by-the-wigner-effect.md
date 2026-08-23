---
layout: post
title: What is the power density of graphite caused by the Wigner effect?
author: StemFix Bot
category: chemistry
tags:
- chemistry
---

{% raw %}
*As an Amazon Associate, I earn from qualifying purchases.* For more practice problems like this, see [Schaum's Outline of College Chemistry, 10th Edition](https://www.amazon.com/dp/007181082X?tag=aiopentec20-20).

---

## 1.  What the question is really asking  

The problem gives a **specific energy** stored in irradiated graphite because of the Wigner effect:

\[
E_{\text{W}} = 2.7\;\text{MJ kg}^{-1}=2.7\times10^{6}\;\text{J kg}^{-1}
\]

The student wants to know the **power density** – i.e. how many watts (J s⁻¹) are produced per unit mass (or per unit volume) when that stored energy is released.  
Power density can be written as  

\[
\dot{q}= \frac{E_{\text{W}}}{\Delta t}
\]

where \(\Delta t\) is the time over which the energy is liberated.  
Since the release time is not given, we must treat it as an unknown and express the answer as a function of \(\Delta t\). We can also give a few realistic “order‑of‑magnitude” estimates based on what actually happened at Windscale.

---

## 2.  Step‑by‑step calculation  

### Step 1 – Write the basic relationship  

\[
\boxed{\dot{q}_{\text{mass}} = \frac{2.7\times10^{6}\;\text{J kg}^{-1}}{\Delta t\;(\text{s})}\;\text{W kg}^{-1}}
\]

If you prefer **volumetric** power density, multiply by the bulk density of graphite.

### Step 2 – Graphite density  

Typical nuclear‑grade graphite has a bulk density  

\[
\rho \approx 1.8\;\text{g cm}^{-3}=1.8\times10^{3}\;\text{kg m}^{-3}
\]

### Step 3 – Convert to volumetric power density  

\[
\dot{q}_{\text{vol}} = \dot{q}_{\text{mass}}\;\rho
                = \frac{2.7\times10^{6}\;\text{J kg}^{-1}}{\Delta t}\;(1.8\times10^{3}\;\text{kg m}^{-3})
\]

\[
\boxed{\dot{q}_{\text{vol}} = \frac{4.86\times10^{9}}{\Delta t\;(\text{s})}\;\text{W m}^{-3}}
\]

### Step 4 – Insert plausible release times  

| Assumed release time \(\Delta t\) | \(\dot{q}_{\text{mass}}\) (W kg⁻¹) | \(\dot{q}_{\text{vol}}\) (W m⁻³) |
|-----------------------------------|-----------------------------------|-----------------------------------|
| 1 s (instantaneous)               | \(2.7\times10^{6}\)               | \(4.9\times10^{9}\)               |
| 1 min (60 s)                      | \(4.5\times10^{4}\)               | \(8.1\times10^{7}\)               |
| 1 h (3600 s)                      | \(7.5\times10^{2}\)               | \(1.35\times10^{6}\)              |
| 10 h (3.6 × 10⁴ s) – approximate Windscale event | \(75\) | \(1.35\times10^{5}\) |
| 1 day (8.64 × 10⁴ s)              | \(31\)                            | \(5.6\times10^{4}\)               |

These numbers illustrate the huge range: the power density can be **megawatts per kilogram** if the energy is dumped in a fraction of a second, but only a few **tens of watts per kilogram** if the release stretches over many hours.

### Step 5 – Relate to the Windscale accident  

During the Windscale fire (October 1957) the graphite core was deliberately heated to ~250 °C to anneal stored Wigner energy. The temperature rise and the subsequent “energy release” lasted on the order of **10 h** before the fire became uncontrolled. Using \(\Delta t\approx 3.6\times10^{4}\) s gives

\[
\dot{q}_{\text{mass}} \approx 75\;\text{W kg}^{-1}
\qquad
\dot{q}_{\text{vol}} \approx 1.3\times10^{5}\;\text{W m}^{-3}
\]

These values are consistent with the observed heat flux that ignited the surrounding fuel channels.

---

## 3.  Final answer  

The **power density** (mass basis) of Wigner‑energy release from graphite is

\[
\boxed{\displaystyle \dot{q}_{\text{mass}} = \frac{2.7\times10^{6}\;\text{J kg}^{-1}}{\Delta t\;(\text{s})}\; \text{W kg}^{-1}}
\]

and, using the bulk density \(\rho = 1.8\times10^{3}\;\text{kg m}^{-3}\),

\[
\boxed{\displaystyle \dot{q}_{\text{vol}} = \frac{4.9\times10^{9}}{\Delta t\;(\text{s})}\; \text{W m}^{-3}}
\]

For the Windscale incident, where the energy was released over roughly **10 h (≈ 3.6 × 10⁴ s)**, the power densities are

\[
\dot{q}_{\text{mass}} \approx 75\;\text{W kg}^{-1},
\qquad
\dot{q}_{\text{vol}} \approx 1.3\times10^{5}\;\text{W m}^{-3}.
\]

---

## 4.  Common Mistakes  

| Mistake | Why it’s wrong | How to avoid it |
|---------|----------------|-----------------|
| **Treating the 2.7 MJ kg⁻¹ as a *power* instead of an *energy*** | Power already includes a time factor; the given number is purely an energy per mass. | Remember that **Power = Energy / Time**; you must introduce a time scale \(\Delta t\). |
| **Using the crystal density of graphite (≈ 2.2 g cm⁻³) instead of the bulk density of the reactor core** | Reactor graphite is porous and has a lower bulk density (~1.8 g cm⁻³). Using the higher value over‑estimates volumetric power density. | Use the actual bulk density of the material in the specific configuration (often supplied in reactor design data). |
| **Assuming the release is instantaneous** | In reality the Wigner energy anneals over minutes to hours; an instantaneous assumption gives absurdly high power densities (MW kg⁻¹) that are not physically realized. | Cite experimental or historical release times (e.g., Windscale ~10 h) and present the result as a function of \(\Delta t\). |
| **Neglecting the fact that only a fraction of the stored energy is released in a single event** | Not all stored Wigner energy may be liberated; some remains trapped after the first anneal. | State the assumption “all 2.7 MJ kg⁻¹ is released” and, if needed, introduce a fraction \(f\) (0 < f ≤ 1) to scale the answer. |
| **Mixing up mass‑ and volume‑based power densities** | Confusing units (W kg⁻¹ vs. W m⁻³) leads to errors in subsequent heat‑transfer calculations. | Keep a clear conversion step: \(\dot{q}_{\text{vol}} = \dot{q}_{\text{mass}} \times \rho\). |

By keeping the time factor explicit and using the correct material density, you obtain a reliable estimate of the power density associated with the Wigner effect in graphite.

*Original question: [What is the power density of graphite caused by the Wigner effect?](https://chemistry.stackexchange.com/questions/152976/what-is-the-power-density-of-graphite-caused-by-the-wigner-effect) on Chemistry Stack Exchange, licensed CC BY-SA.*

{% endraw %}
