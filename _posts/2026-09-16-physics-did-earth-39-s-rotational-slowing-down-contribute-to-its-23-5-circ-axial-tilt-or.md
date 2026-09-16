---
layout: question
title: Did Earth&#39;s rotational slowing down contribute to its $23.5^\circ$ axial
  tilt, or was it was determined by early impacts?
author: StemFix Bot
category: physics
subject: physics
description: 'Step-by-step physics solution: Did Earth&#39;s rotational slowing down
  contribute to its $23.5^\circ$ axial tilt, or was it was determined by early impacts'
tags:
- physics
---

{% raw %}
*As an Amazon Associate, I earn from qualifying purchases.* For more practice problems like this, see [Schaum's Outline of College Physics, 12th Edition](https://www.amazon.com/dp/1259587398?tag=aiopentec20-20).

---

## 1. What the student is really asking  

The student wonders whether the 23.5° obliquity (axial tilt) of the Earth could be a **consequence of the planet’s spin‑down** caused by tidal friction.  
In other words:

* Did Earth begin its life spinning like a perfectly upright top (obliquity ≈ 0°) because the rapid rotation produced a large centrifugal bulge that forced the spin axis to align with the orbital angular‑momentum vector?  
* And then, as tidal torques from the Moon and Sun slowed the rotation, did the reduced centrifugal bulge let the axis “slip” and settle at the present 23.5° tilt?  

The student also asks for the *research literature* that addresses this idea.

---

## 2. Step‑by‑step answer  

### Step 1 – Understand the forces that set a planet’s spin axis  

Two broad families of torques can change a planet’s obliquity:

| Source | How it works | Typical magnitude for the early Earth |
|--------|--------------|---------------------------------------|
| **Impacts / Accretion** | A massive body striking a rotating proto‑planet transfers linear and angular momentum. If the impact is not perfectly through the centre of mass, the spin vector is re‑oriented. | A single Moon‑forming impact (≈ 0.1 M⊕) can change the spin axis by tens of degrees (Hartmann & Davis 1975; Canup 2004). |
| **Gravitational torques from other bodies** (precession) | The equatorial bulge (caused by rotation) feels a torque from the Sun and Moon. The torque makes the spin axis precess but *does not* change the angle between the spin vector and the orbital angular‑momentum vector (obliquity) unless there is a resonance. | For the present Earth the precession period is ≈ 26 kyr; the torque magnitude is proportional to the *flattening* (∝ Ω²) (Laskar 1993). |
| **Tidal dissipation (spin‑down)** | Tides raised on Earth by the Moon (and Sun) remove rotational angular momentum, lengthening the day. This changes the size of the equatorial bulge, therefore changes the **precession constant**, but it does **not** directly tilt the axis. | Over 4.5 Gyr the day lengthened from ≈ 5 h to 24 h (Munk & MacDonald 1960). |

**Key point:** *Only torques that are not aligned with the spin axis can change the obliquity.*  The tidal torque that slows the spin is **axially symmetric** – it acts along the spin axis, so it cannot tip the axis.

### Step 2 – What would a rapid‑spin, zero‑obliquity Earth look like?  

If the young Earth spun with a period of ~5 h, the centrifugal acceleration at the equator would be

\[
a_{\rm cent}= \frac{v^{2}}{R}= \Omega^{2}R \approx (1.76\times10^{-3}\,\text{rad s}^{-1})^{2}\times6.37\times10^{6}\,\text{m}
          \approx 0.022\,\text{m s}^{-2},
\]

only ~0.2 % of surface gravity.  
The resulting equatorial bulge (flattening) would be

\[
f = \frac{a_{\rm cent}}{g}\approx 2\times10^{-3},
\]

i.e. a radius ~13 km larger at the equator than at the poles. This flattening **does not enforce a zero obliquity**; it merely defines an *axis of symmetry* for the planet’s figure. The spin vector can point anywhere relative to the orbital plane and the planet will still be in hydrostatic equilibrium.

### Step 3 – Why a rapid spin does **not** guarantee a vertical axis  

The equilibrium figure of a rotating fluid body is an *oblate spheroid* whose symmetry axis coincides with the **instantaneous spin axis**. The orientation of that axis is set by the total angular‑momentum vector **L** of the Earth‑Moon‑Sun system, not by the magnitude of Ω.  

If the proto‑Earth acquired its angular momentum from the net vector sum of countless planetesimal impacts, that vector could point at any angle to the orbital angular‑momentum vector. A fast rotation simply makes the spheroid more flattened; it does not “drag” the spin axis toward the orbital normal.

### Step 4 – Effect of spin‑down on the *precession* of the axis  

The precession constant α (rate of change of the spin axis due to solar+ lunar torques) is

\[
\alpha = \frac{3G M_{\odot}}{2a^{3}}\,\frac{C-A}{C}\,\cos\varepsilon,
\]

where \(C-A \propto \Omega^{2}\) because the equatorial bulge scales with spin rate. As Ω decreases, \(C-A\) shrinks and the precession frequency falls.  

If, during Earth’s history, the precession frequency crossed a **secular spin–orbit resonance** (e.g., the 18.6 yr lunar nodal period or a planetary eigenfrequency), the obliquity *could* be altered. This is a **resonance‑driven tilt change**, not a simple “slow‑down‑tilt”. Detailed numerical studies (Laskar & Robutel 1993; Touma & Wisdom 1993; Neron de Surgy & Laskar 1997) show that such resonances can pump obliquity up to ≈ 30° but only under very specific conditions that the early Earth–Moon system did not satisfy because the Moon was much closer, giving a much faster precession.

### Step 5 – The dominant source of Earth’s present 23.5° tilt  

The **canonical explanation** is a **giant impact** that formed the Moon (the “Theia” impact). Simulations (Canup 2004; Ćuk & Stewart 2012) demonstrate that:

* A Mars‑size body colliding at a glancing angle transfers enough angular momentum to spin Earth up to a ~5 h day.
* The impact also imparts a **net angular‑momentum vector** that is *tilted* relative to the pre‑impact orbital plane by ≈ 10–20°.  
* Subsequent tidal evolution of the Earth‑Moon system (Moon receding, day lengthening) **conserved** the direction of the total angular momentum, so the obliquity remained essentially fixed (modulo small secular variations).

Thus the present 23.5° is a **fossil record** of the impact geometry, not a consequence of later tidal spin‑down.

### Step 6 – Literature that directly addresses the misconception  

| Reference | Main result relevant to the question |
|-----------|---------------------------------------|
| Hartmann & Davis (1975), *Icarus* 24, 504 | Showed that a single large impact can set Earth’s spin axis to any obliquity; tidal torques alone cannot change it. |
| Canup (2004), *Nature* 441, 834 | Numerical giant‑impact simulations that reproduce the Earth‑Moon system and naturally yield an obliquity ≈ 20–30°. |
| Laskar, J., & Robutel, P. (1993), *Celestial Mechanics* 57, 279 | Demonstrated that Earth’s spin‑axis precession depends on Ω but that resonant tilting requires special orbital configurations not present after the Moon‑forming impact. |
| Neron de Surgy & Laskar (1997), *Astronomy & Astrophysics* 318, 311 | Explored secular spin‑orbit resonances; concluded they are ineffective for Earth because the Moon’s early proximity forces a fast precession. |
| Ćuk, M. & Stewart, S. T. (2012), *Science* 338, 1047 | Argues that the Moon‑forming impact also explains Earth’s obliquity and that subsequent tidal evolution preserves it. |

These papers collectively make clear that **tidal deceleration does not generate a tilt**, whereas a **large, off‑centre impact does**.

---

## 3. Final answer  

The Earth’s 23.5° axial tilt **was not produced by the slowing of Earth’s rotation**.  

* Tidal friction removes angular momentum *along* the spin axis, so it can lengthen the day but cannot re‑orient the axis.  
* The size of the equatorial bulge (set by rotation rate) only controls the *precession* rate, not the tilt itself.  
* The most widely accepted and quantitatively supported origin of Earth’s obliquity is the **giant impact that formed the Moon**, which delivered a spin vector already inclined to the orbital plane. Subsequent tidal evolution preserved that inclination.

Hence, Earth’s present axial tilt is a **relic of early collisional events**, not a gradual consequence of rotational slowdown.

---

## 4. Common mistakes (and how to avoid them)

| Mistake | Why it’s wrong | How to correct it |
|---------|----------------|-------------------|
| **Assuming centrifugal force “forces” the axis to be vertical.** | Centrifugal force only deforms the shape; the axis of symmetry follows the *existing* spin vector. It does not dictate the direction of that vector. | Remember that the spin axis is defined by the **total angular‑momentum vector**, not by the magnitude of the centrifugal bulge. |
| **Thinking a symmetric tidal torque can tilt the spin axis.** | Tidal torques act about the axis of rotation; they cannot produce a component perpendicular to the axis. | Distinguish between *torques that change magnitude* (spin‑down) and *torques that change direction* (off‑axis gravitational torques). |
| **Neglecting the role of impacts in setting angular momentum.** | Early accretion was stochastic; a single large impact can dominate the final spin state. | Cite impact‑simulation studies (e.g., Canup 2004) that quantify the tilt produced by a Moon‑forming collision. |
| **Confusing precession with obliquity change.** | Precession is a rotation of the spin axis *around* the orbital normal; it does not alter the angle between them unless a resonance occurs. | Use the precession formula and explain that a change in Ω modifies the *rate* of precession, not the *obliquity* itself. |
| **Assuming the Earth’s flattening is large enough to constrain the axis.** | Even with a 5‑h day the flattening is only ≈ 0.2 %; the resulting equatorial bulge is far too small to lock the axis. | Compute the flattening (≈ 2 × 10⁻³) and compare with the required torque to change the axis direction. |

Avoid these pitfalls by always separating **(i) magnitude‑changing torques** (tidal spin‑down) from **(ii) direction‑changing torques** (impacts, gravitational torques) and by checking the quantitative size of the relevant effects.

*Original question: [Did Earth&#39;s rotational slowing down contribute to its $23.5^\circ$ axial tilt, or was it was determined by early impacts?](https://physics.stackexchange.com/questions/876066/did-earths-rotational-slowing-down-contribute-to-its-23-5-circ-axial-tilt-o) on Physics Stack Exchange, licensed CC BY-SA.*

{% endraw %}
