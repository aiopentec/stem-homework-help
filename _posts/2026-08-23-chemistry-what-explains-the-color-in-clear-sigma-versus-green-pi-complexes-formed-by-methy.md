---
layout: post
title: What explains the color in clear sigma versus green pi complexes formed by
  methylbenzene?
author: StemFix Bot
category: chemistry
tags:
- chemistry
render_with_liquid: false
---

*As an Amazon Associate, I earn from qualifying purchases.* For more practice problems like this, see [Schaum's Outline of College Chemistry, 10th Edition](https://www.amazon.com/dp/007181082X?tag=aiopentec20-20).

---

## 1. What the question is asking (in plain language)

The textbook says that when **toluene (methylbenzene)** is treated  

* with **HCl alone** → a *σ‑complex* (the usual Wheland intermediate) is formed and the mixture stays **colourless**.  

* with **HCl + AlCl₃** (a Lewis‑acid catalyst) → a *π‑complex* of toluene with AlCl₃ is formed and the mixture turns **green**.  

**We have to explain why the two reactions give different colours.**  
In particular, does the green colour come from the π‑complex, and if so, what electronic process is responsible for it?

---

## 2. Step‑by‑step explanation  

### Step 1 – Identify the two species that are actually present  

| Reaction condition | Species that is generated (major) | Structural picture |
|--------------------|-----------------------------------|---------------------|
| **HCl only** (no Lewis acid) | **σ‑complex** (also called the Wheland intermediate) – a cyclohexadienyl cation where the aromatic ring has temporarily lost aromaticity because H⁺ has added to one carbon. | ![σ‑complex] (a benzene ring with one sp³‑hybridised carbon bearing a H⁺) |
| **HCl + AlCl₃** | **π‑complex** – AlCl₃ coordinates to the *π‑electron cloud* of the aromatic ring, giving a “Lewis‑acid/π‑base” adduct. The aromatic system stays planar; AlCl₃ sits above the ring. | ![π‑complex] (toluene with AlCl₃ above the ring) |

*The σ‑complex is a **carbocation** that is strongly localized and does not involve any new metal‑ligand orbitals. The π‑complex, on the other hand, involves a **metal‑to‑π charge‑transfer interaction**.*

---

### Step 2 – What colours do we normally expect from these species?

| Species | Typical electronic transitions | Position of absorption | Observed colour |
|---------|-------------------------------|------------------------|-----------------|
| Uncomplexed benzene/toluene | **π → π\*** (UV, ~260 nm) | Far‑UV, outside the visible range | Colourless |
| σ‑complex (cyclohexadienyl cation) | Mostly **σ → σ\*** and **π → π\*** but still high‑energy (UV) because the conjugation is broken | UV, < 350 nm | Colourless |
| π‑complex (aryl‑AlCl₃) | **Charge‑transfer (CT) transition**: donation of electron density from the aromatic π system to the empty Al 3p orbital (π → Al) | **Visible region (≈ 500–560 nm)** | **Green** (the complementary colour of the absorbed red‑orange light) |

*Why does a CT band appear only for the π‑complex?*  

AlCl₃ is a strong Lewis acid; it possesses an empty 3p orbital that can accept electron density. When the aromatic ring sits over AlCl₃, the π electrons are partially transferred into this orbital, creating a **π → Al charge‑transfer excited state**. This transition costs less energy than the ordinary π → π\* transition, so its absorption is shifted from the UV into the visible part of the spectrum. The band lies roughly at 550 nm, which removes red/orange light and makes the solution appear green.

---

### Step 3 – Sketch of the electronic picture

```
   π electrons of toluene   →   empty Al 3p orbital (Lewis‑acid)
   ------------------------------------------------------------
   Ground state:   π (filled)   |   Al 3p (empty)
   Excited state:  π (partially empty) | Al 3p (partially filled)
```

The energy gap (ΔE) for this CT transition is:

\[
\Delta E = h\nu \approx \frac{hc}{\lambda}
\]

Taking λ ≈ 540 nm (green‑absorbing red/orange),

\[
\Delta E \approx \frac{(6.626\times10^{-34}\,\text{J·s})(3.00\times10^{8}\,\text{m·s}^{-1})}{5.40\times10^{-7}\,\text{m}}
\approx 3.68\times10^{-19}\,\text{J} \approx 2.3\,\text{eV}
\]

This is much lower than the ≈ 5 eV required for a typical π → π\* transition in benzene, confirming that the AlCl₃‑π interaction creates a low‑energy, visible‑region transition.

---

### Step 4 – Why the σ‑complex stays colourless  

The σ‑complex does **not** involve a metal centre with low‑lying empty orbitals. Its electronic spectrum is dominated by localized σ‑bond transitions and the broken aromatic π system. The lowest‑energy allowed transition remains in the UV, so no visible light is absorbed → the solution looks colourless.

---

### Step 5 – Summarise the answer to the original question  

*Yes, the green colour is directly caused by the formation of the π‑complex between toluene and AlCl₃.*  
The colour originates from a **π → Al charge‑transfer transition** that absorbs red/orange light, leaving the transmitted light green. The σ‑complex formed with HCl alone lacks such a metal‑centred acceptor and therefore does not absorb visible light, remaining colourless.

---

## 3. Final answer

- The **σ‑complex** (Wheland intermediate) formed with HCl alone absorbs only in the UV; it is colourless.  
- The **π‑complex** formed when AlCl₃ is present coordinates to the aromatic π‑system, creating a **metal‑to‑π charge‑transfer interaction**. This interaction introduces an electronic transition in the visible region (≈ 500–560 nm), which removes red/orange light and makes the solution appear **green**.  

Thus, the observed colour difference is indeed due to the formation of the π‑complex, specifically the π → Al charge‑transfer band it introduces.

---

## 4. Common mistakes for this type of problem  

| Mistake | Why it’s wrong | How to avoid it |
|---------|----------------|-----------------|
| **Assuming the colour comes from the HCl itself** | HCl is a colourless gas; it does not generate visible‑range absorptions. | Focus on the *complex* formed, not on the reagent. |
| **Attributing the green colour to a simple “chlorination” product** | Electrophilic chlorination of toluene gives p‑/o‑chloro‑toluene, which are also colourless. | Remember the question is about *complexes* (intermediates), not the final substitution product. |
| **Confusing σ‑complex with a σ‑bonded AlCl₃ adduct** | σ‑complex refers to the carbocation intermediate, not a metal‑bound species. | Keep the definitions clear: σ‑complex = Wheland (C–H σ bond formed), π‑complex = Lewis‑acid/π‑base adduct. |
| **Neglecting the role of charge‑transfer transitions** | Colour in many organometallic/π‑complexes arises from CT bands, not from π → π\* alone. | Explicitly consider whether an empty orbital on a metal (AlCl₃) can accept electron density from the aromatic π system. |
| **Thinking the colour must be “green because of AlCl₃”** | Not every AlCl₃ complex is green; the colour depends on the energy of the CT transition. | Relate colour to the wavelength of the absorbed light, not just the identity of the metal. |

By keeping these points in mind, you can correctly diagnose colour changes in aromatic Lewis‑acid complexes.

*Original question: [What explains the color in clear sigma versus green pi complexes formed by methylbenzene?](https://chemistry.stackexchange.com/questions/95845/what-explains-the-color-in-clear-sigma-versus-green-pi-complexes-formed-by-methy) on Chemistry Stack Exchange, licensed CC BY-SA.*
