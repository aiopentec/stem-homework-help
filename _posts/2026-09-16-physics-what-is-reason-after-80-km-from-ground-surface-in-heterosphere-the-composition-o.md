---
layout: question
title: What is reason after 80 km from ground surface in heterosphere the composition
  of air and its ratio changes but not in homosphere?
author: StemFix Bot
category: physics
subject: physics
description: 'Step-by-step physics solution: What is reason after 80 km from ground
  surface in heterosphere the composition of air and its ratio changes but not in
  homos'
tags:
- physics
---

{% raw %}
*As an Amazon Associate, I earn from qualifying purchases.* For more practice problems like this, see [Schaum's Outline of College Physics, 12th Edition](https://www.amazon.com/dp/1259587398?tag=aiopentec20-20).

---

## 1. Restating the question in plain language  

The student is asking:

* **Why does the composition of the atmosphere (the relative amounts of N₂, O₂, Ar, etc.) stay essentially constant up to about 80 km, but above that height the proportions begin to change?**  
* **Is the 80 km “boundary” a theoretical construct, a result of measurements, or both?**  

In short: *What physical processes make the lower 80 km of the atmosphere well‑mixed, and why do they stop being effective higher up?*  

---

## 2. Step‑by‑step explanation  

### 2.1  Define the two regions  

| Region | Approx. altitude | Common name | Main characteristic |
|-------|------------------|-------------|----------------------|
| **Homosphere** | 0 – ~80 km | Homosphere | The major constituents (N₂, O₂, Ar, CO₂) are mixed so thoroughly that their **volume mixing ratios** are essentially constant with height. |
| **Heterosphere** | > ~80 km | Heterosphere | The mixing ratios start to vary with altitude; lighter gases become relatively more abundant with height. |

The transition altitude is not a hard wall but a *transition layer* (roughly 70–100 km) where the dominant transport mechanism changes.

---

### 2.2  How gases are mixed in the lower atmosphere  

Two physical processes keep the gases well mixed:

| Process | What it does | Typical strength in the homosphere |
|---------|--------------|------------------------------------|
| **Turbulent (eddy) diffusion** | Random, chaotic motions of air parcels (e.g., caused by weather, convection, gravity waves) transport molecules vertically. | Eddy diffusivity \(K_{\text{eddy}}\) ≈ 10–10³ m² s⁻¹ in the troposphere, decreasing with height but still > molecular diffusion below ~80 km. |
| **Molecular (Brownian) diffusion** | Random motion of individual molecules colliding with each other. | Diffusivity \(D\) ≈ 0.1–1 m² s⁻¹ for N₂, O₂ at sea level; increases with decreasing pressure but is **much smaller** than eddy diffusion in the homosphere. |

**Key point:** As long as **eddy diffusion dominates** over molecular diffusion, any parcel of air that is displaced vertically quickly becomes mixed back to the background composition. The result is a *uniform mixing ratio* for the major gases.

---

### 2.3  When does eddy diffusion stop dominating?  

The competition between the two diffusion mechanisms can be quantified by comparing their coefficients:

\[
\frac{K_{\text{eddy}}}{D} \gg 1 \quad \Longrightarrow \text{well‑mixed (homosphere)}\\[4pt]
\frac{K_{\text{eddy}}}{D} \lesssim 1 \quad \Longrightarrow \text{diffusive separation (heterosphere)}
\]

- **Eddy diffusivity** drops with altitude because atmospheric density and the sources of turbulence (convection, weather) become weaker. Empirically, \(K_{\text{eddy}}\) falls roughly as \(K_{\text{eddy}} \propto \rho^{-0.5}\) (where \(\rho\) is air density).  
- **Molecular diffusivity** increases with decreasing pressure (roughly \(D \propto 1/\rho\)) because collisions are less frequent, allowing molecules to travel farther between collisions.

The two curves intersect near **70–90 km**. Using typical empirical profiles (e.g., the NRLMSISE‑00 model), the crossover altitude is **≈ 80 km**.  

---

### 2.4  What happens above the crossover?  

When molecular diffusion dominates, each species behaves **independently** under the influence of gravity. The vertical distribution of a constituent *i* follows the **barometric (hydrostatic) formula with its own scale height**:

\[
n_i(z) = n_i(z_0)\,\exp\!\Big[-\frac{z - z_0}{H_i}\Big],
\qquad 
H_i = \frac{k_B T}{m_i g},
\]

where  

* \(n_i\) = number density of species *i*  
* \(k_B\) = Boltzmann constant  
* \(T\) = temperature (≈ 200 K in the mesosphere/thermosphere)  
* \(m_i\) = molecular mass of species *i*  
* \(g\) = acceleration due to gravity (≈ 9.8 m s⁻²)

Because **\(H_i\) depends on the mass**, lighter gases (e.g., H, He) have *larger* scale heights and therefore their relative concentration **increases with altitude**, while heavier gases (N₂, O₂) fall off more rapidly. This creates the **heterosphere** composition gradient.

---

### 2.5  Why is the 80 km value used in textbooks?  

1. **Observational evidence** – Measurements from sounding rockets, satellite drag data, and mass spectrometers (e.g., the Atmosphere Explorer missions) show a clear change in mixing ratios around 70–100 km.  
2. **Modeling convention** – Atmospheric models (e.g., US Standard Atmosphere, NRLMSISE‑00) adopt a *transition altitude* near 80 km because that is where the modeled eddy diffusion coefficient falls below the molecular diffusion coefficient for the major species.  
3. **Practical simplicity** – Using a single number (80 km) gives a convenient “rule of thumb” for the homosphere/heterosphere boundary, even though the real transition is a gradual crossover.

Thus the 80 km figure is **both empirically observed and theoretically justified**, but it should be understood as an approximate, not a strict, dividing line.

---

### 2.6  Summary of the physical picture  

| Altitude | Dominant transport | Resulting composition |
|----------|-------------------|-----------------------|
| 0 – ~70 km | Turbulent (eddy) diffusion \(\gg\) molecular diffusion | Uniform mixing ratios → *homosphere* |
| ~70 – ~100 km | Eddy and molecular diffusion comparable (transition layer) | Gradual onset of separation |
| > ~100 km | Molecular diffusion \(\gg\) eddy diffusion | Species separate by mass → *heterosphere* |

---

## 3. Final answer  

- **Below ~80 km** the atmosphere is called the **homosphere** because vigorous turbulent mixing (eddy diffusion) overwhelms molecular diffusion, keeping the volume mixing ratios of N₂, O₂, Ar, CO₂, etc., essentially constant with height.  
- **Above ~80 km** turbulent mixing becomes weak; molecular diffusion becomes dominant. Each gas then follows its own exponential decline with a scale height that depends on its molecular mass, so lighter gases become relatively more abundant. This region is the **heterosphere**.  
- The **≈ 80 km boundary** is a **practical, observationally supported approximation** that marks where the eddy‑diffusion coefficient drops to the same order as the molecular‑diffusion coefficient for the main atmospheric constituents.

---

## 4. Common mistakes  

| Mistake | Why it’s wrong | Correct approach |
|---------|----------------|------------------|
| **Thinking the 80 km line is a physical “wall.”** | The atmosphere changes continuously; there is no abrupt discontinuity. | Treat the 70–100 km region as a gradual transition where the two diffusion processes become comparable. |
| **Attributing the change solely to temperature.** | Temperature does affect scale heights, but the *dominant* factor for the composition change is the switch from turbulent to molecular diffusion. | Emphasize the relative magnitudes of eddy vs. molecular diffusion coefficients. |
| **Assuming that all gases separate immediately above 80 km.** | Separation proceeds according to each species’ molecular weight; heavy gases still dominate up to several hundred km before becoming negligible. | Use the barometric formula with species‑specific scale heights to see the gradual nature of separation. |
| **Neglecting the role of external sources (e.g., solar UV, meteoric input).** | While photochemistry and meteoric ablation affect trace species, the *overall* change in the major constituent ratios is driven by diffusion. | Mention that for trace species, photochemistry can dominate, but the homosphere/heterosphere distinction concerns the bulk gases. |
| **Using a single value of eddy diffusivity for all altitudes.** | Eddy diffusivity varies by many orders of magnitude with height. | Refer to empirical profiles (e.g., \(K_{\text{eddy}} \approx 10^2\) m² s⁻¹ at 50 km, falling to < 1 m² s⁻¹ near 90 km). |

Keeping these points in mind will help avoid misconceptions when discussing atmospheric layering and composition.

*Original question: [What is reason after 80 km from ground surface in heterosphere the composition of air and its ratio changes but not in homosphere?](https://physics.stackexchange.com/questions/875664/what-is-reason-after-80-km-from-ground-surface-in-heterosphere-the-composition-o) on Physics Stack Exchange, licensed CC BY-SA.*

{% endraw %}
