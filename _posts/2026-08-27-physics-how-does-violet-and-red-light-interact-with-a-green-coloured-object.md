---
layout: question
title: How does violet and red light interact with a green coloured object?
author: StemFix Bot
category: physics
subject: physics
description: 'Step-by-step physics solution: How does violet and red light interact
  with a green coloured object?'
tags:
- physics
---

{% raw %}
*As an Amazon Associate, I earn from qualifying purchases.* For more practice problems like this, see [Schaum's Outline of College Physics, 12th Edition](https://www.amazon.com/dp/1259587398?tag=aiopentec20-20).

---

## 1.  What is the question?

A student is trying to understand **why a green‑coloured object looks green when it is illuminated by white light**, and specifically what happens to the **vioiolet** and **red** components of that light.  
The student has heard the following (from AI chat‑bots) and wants to know whether it is correct:

| Light colour | Supposed fate in the green object |
|--------------|-----------------------------------|
| **Violet**   | Excites electrons to a higher energy band (electronic transition) |
| **Red**      | Bypasses electrons and makes atoms vibrate (phonons) |
| **Green**    | Is “ignored” and simply bounces back, giving the green colour |

We must explain, using basic optics and solid‑state physics, **what actually happens to violet, red and green photons when they strike a green object** and why we perceive the object as green.

---

## 2.  Step‑by‑step physical picture  

### 2.1  Colour of an object = its **spectral reflectance**

* An object is illuminated by a mixture of wavelengths (white light).  
* Each wavelength is either **absorbed**, **transmitted**, or **reflected/scattered**.  
* The **reflectance spectrum** \(R(\lambda)\) tells us the fraction of incident light at wavelength \(\lambda\) that leaves the surface toward our eye.  
* The colour we see is the *weighted* sum of the reflected wavelengths, after the eye’s photoreceptors have responded.

> **Key point:** A “green” object is one whose reflectance is high in the green part of the spectrum (≈ 500–570 nm) and low elsewhere. Nothing “ignores” green; the green photons are simply **reflected** (or scattered) much more efficiently than the others.

### 2.2  How light couples to matter  

Two main ways a photon can be taken up by a solid:

| Mechanism | Energy range (photon wavelength) | What it does to the material |
|-----------|----------------------------------|------------------------------|
| **Electronic transition** (promotion of an electron from a filled band to an empty band) | Typically visible‑UV (≈ 1.5–4 eV, 300–800 nm) | Creates an excited electron‑hole pair; the photon is *absorbed*. |
| **Vibrational (phonon) excitation** | Infrared (IR) (≈ 0.03–0.5 eV, > 2 µm) | Excites lattice vibrations; photons of *visible* wavelength are *too energetic* to couple directly to a single phonon. |

Thus:

* **Violet photons (≈ 380–440 nm, 2.8–3.3 eV)** have enough energy to trigger many electronic transitions, *if* the material has an allowed transition at that energy.  
* **Red photons (≈ 620–750 nm, 1.65–2.0 eV)** are still in the visible range, so they can also cause electronic transitions, but the probability depends on the material’s electronic band structure.  
* **Green photons (≈ 500–570 nm, 2.2–2.5 eV)** behave the same way—whether they are absorbed or reflected depends on the available electronic states.

### 2.3  What a typical *green pigment* looks like inside  

Most everyday green colours come from **organic dyes** (e.g., chlorophyll, phthalocyanines) or **inorganic pigments** (e.g., copper phthalocyanine, chromium oxide). Their electronic structure can be sketched as:

```
   Conduction band (empty)   ←  higher energy
   ────────────────────────
   Absorption band (strong) ← absorbs blue‑violet & red
   ────────────────────────
   Valence band (filled)    ← lower energy
```

* The **absorption band** is centered around wavelengths *outside* the green region (often in the blue‑violet and sometimes in the red).  
* Photons whose energy falls inside this band are **strongly absorbed** → electrons are promoted to the conduction band (or to an excited molecular orbital).  
* Photons whose energy falls in the **spectral “gap”** (the region where the material has few or no electronic states to jump into) pass through the pigment without being absorbed. In a thin layer they are mostly **reflected** (by the surface and by internal scattering) and therefore reach the eye.

A **simplified picture** of the reflectance curve for a green pigment looks like:

```
R(λ)
 1 ────────\          /─────────────
            \        /
 0 ──────────\______/─────────────────
            400   520   700 (nm)
          violet  green  red
```

*High reflectance* in the green region, *low* elsewhere.

### 2.4  What actually happens to each colour component  

| Incident colour | What the pigment *does* (probability) | Resulting light that reaches the eye |
|-----------------|----------------------------------------|--------------------------------------|
| **Violet (≈ 400 nm)** | Strong electronic absorption (many pigments have a π→π* transition in the blue‑violet). The photon is absorbed; the electron relaxes non‑radiatively or by fluorescence (often outside the visible range). | Very little violet is reflected → we do **not** see violet. |
| **Red (≈ 650 nm)** | Depends on pigment. Many green pigments have a *secondary* absorption band in the red (e.g., copper phthalocyanine absorbs around 620 nm). If such a band exists, red photons are partially absorbed; if not, they are mostly reflected. In most everyday “green” paints, the red band is weak, so a noticeable fraction of red is reflected. | Some red is reflected → the object may look slightly yellow‑ish under pure red illumination, but under white light the dominant reflected colour is still green. |
| **Green (≈ 530 nm)** | The absorption coefficient is minimal in this region → **very little electronic excitation**. The photon is not absorbed; it undergoes elastic scattering/reflection. | Most green photons leave the surface → the eye receives a strong green signal → the object appears green. |

> **Bottom line:** The statement “violet excites electrons, red makes atoms vibrate, green is ignored” is **incorrect**.  
> *Violet* and *red* photons are **absorbed** (or not) according to the pigment’s electronic absorption spectrum; they do **not** directly cause lattice vibrations because visible photons are too energetic for a single phonon. *Green* photons are **reflected** because the material lacks allowed electronic transitions at that energy.

### 2.5  Why the “vibrational” idea is misplaced  

* A photon can only create a phonon if its energy matches a phonon mode **and** momentum conservation can be satisfied (usually through the crystal lattice).  
* Visible photon energies (≈ 2 eV) are **hundreds of times larger** than typical optical phonon energies (≈ 0.03–0.1 eV).  
* Therefore a single visible photon cannot be absorbed by exciting a single phonon; instead it must involve electronic states.  

The only way red light could be “converted into heat” is via **non‑radiative relaxation** of an excited electron: the photon is absorbed, the electron is promoted, then it relaxes by transferring its energy to many phonons (heat). This is true for both violet and red photons that are absorbed.

### 2.6  Summary of the physical process

1. **White light** hits the surface.  
2. For each wavelength λ, the pigment has an **absorption coefficient** α(λ).  
3. The intensity that emerges (reflected + scattered) is \(I_{\text{out}}(\lambda)=I_{\text{in}}(\lambda)\,e^{-\alpha(\lambda) d}\) (Beer‑Lambert law) where *d* is the effective optical path through the pigment layer.  
4. Where α(λ) is large (violet, often red), the exponential term is tiny → almost all those photons are **absorbed** → their energy ends up as excited electrons → quickly turned into heat.  
5. Where α(λ) is small (green), the exponential term ≈ 1 → most photons are **reflected** → our eyes receive green light → we perceive the object as green.

---

## 3.  Final answer (concise)

* A **green object** appears green because its material **reflects green‑wavelength photons** much more efficiently than photons of other colours.  
* **Violet photons** usually have enough energy to be **absorbed electronically** (they promote electrons to higher energy states), and their energy is eventually turned into heat or re‑emitted at other wavelengths (fluorescence).  
* **Red photons** may also be **absorbed electronically** if the pigment has an absorption band in the red; otherwise they are largely reflected like green. They do **not** directly cause atomic vibrations because visible photons are far too energetic for a single phonon.  
* **Green photons** are **not “ignored”**; they simply **pass through the material without being absorbed** (or are elastically scattered) and thus dominate the reflected light that reaches our eyes.

Therefore the AI‑generated description mixes correct ideas (violet can cause electronic excitation) with inaccurate ones (red “bypasses electrons” and directly makes atoms vibrate; green is ignored). The correct picture is governed by the material’s **spectral absorption (or reflectance) curve**, not by a colour‑by‑colour rule.

---

## 4.  Common Mistakes  

| Mistake | Why it’s wrong | Correct view |
|--------|----------------|--------------|
| **“Red light cannot excite electrons because it is low‑energy.”** | Visible photons (including red) still have enough energy (~2 eV) to bridge many band gaps or molecular orbital gaps. | Whether red is absorbed depends on the *specific* electronic states of the pigment, not on a generic “too low” rule. |
| **“Vibrational excitation happens directly from visible photons.”** | Phonon energies are ≈ 10–100 meV, far smaller than visible photon energies (≈ 2 eV). | Visible photons are absorbed electronically; the resulting excited electrons can relax non‑radiatively, transferring energy to many phonons (heat). |
| **“Green photons are ignored by the material.”** | Ignoring would imply no interaction; in reality the material *reflects* (or scatters) them because it lacks an allowed absorption transition at that energy. | Green light is reflected because the pigment’s absorption coefficient is low in that wavelength range. |
| **“All colours are either absorbed or reflected, never both.”** | Real pigments have wavelength‑dependent absorption; a single wavelength can be partially absorbed and partially reflected depending on thickness and surface roughness. | The reflected intensity follows Beer‑Lambert’s exponential law; the fraction reflected plus the fraction absorbed (plus any transmission) sums to the incident intensity. |
| **“Fluorescence is the main reason we see colour.”** | Fluorescence is usually a weak, secondary process; the dominant colour we see comes from *elastic* reflection/scattering. | Fluorescence can add subtle tints (e.g., a faint red glow under UV), but the perceived colour of a green object under white light is set by its reflectance spectrum. |

---

*Original question: [How does violet and red light interact with a green coloured object?](https://physics.stackexchange.com/questions/875417/how-does-violet-and-red-light-interact-with-a-green-coloured-object) on Physics Stack Exchange, licensed CC BY-SA.*

{% endraw %}
