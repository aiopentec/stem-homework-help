---
layout: question
title: How does relativistic proper time dilation ($\Delta\tau = 0$ for lightlike
  paths) affect spontaneous wavefunction collapse rates?
author: StemFix Bot
category: physics
subject: physics
description: 'Step-by-step physics solution: How does relativistic proper time dilation
  ($\Delta\tau = 0$ for lightlike paths) affect spontaneous wavefunction collapse
  r'
tags:
- physics
---

{% raw %}
*As an Amazon Associate, I earn from qualifying purchases.* For more practice problems like this, see [Schaum's Outline of College Physics, 12th Edition](https://www.amazon.com/dp/1259587398?tag=aiopentec20-20).

---

## 1.  What the question is really asking  

| Question |Plain‑language restatement|
|---|---|
|**Parameterisation**|When we write a spontaneous‑collapse law (e.g. “the wavefunction collapses after a time \(T\)”), should the “clock’’ that measures \(T\) be the laboratory coordinate time \(t\) (the time used by an external observer) or the proper time \(\tau\) that ticks along the particle’s world‑line?|
|**Time‑dilation effect**|If the collapse law is written in terms of the particle’s own proper time, then for a particle moving at (or very close to) the speed of light \(\Delta\tau\to0\). Does this make the collapse time \(\to\infty\) – i.e. does the superposition never collapse?|
|**Photon paradox**|Does this mean that mass‑less particles (photons) or any system that experiences extreme time dilation can never undergo an intrinsic spontaneous collapse unless something else (a massive “clock’’) forces it?|
|**How do modern relativistic collapse models solve the apparent clash between relativistic kinematics (proper‑time) and the notion of a universal collapse rate?**|  

In short: **Do relativistic collapse theories use the particle’s proper time, the laboratory time, or something else?** And **what happens for light‑like world‑lines?**  

---

## 2.  Step‑by‑step answer  

### 2.1  Collapse models in non‑relativistic quantum mechanics  

1. **CSL (Continuous Spontaneous Localization)**  
   - The stochastic modification of the Schrödinger equation is written as  

\[
d|\psi_t\rangle = \Bigl[-\frac{i}{\hbar}H\,dt
     +\sqrt{\lambda}\int d^3x\,(M(\mathbf x)-\langle M(\mathbf x)\rangle_t )\,dW_t(\mathbf x) 
     -\frac{\lambda}{2}\int d^3x\,(M(\mathbf x)-\langle M(\mathbf x)\rangle_t )^2dt\Bigr]|\psi_t\rangle .
\]

   - **\(t\)** is the *Newtonian* (global) time that all observers in the laboratory share.  
   - The **collapse rate \(\lambda\)** has dimensions of *inverse time* (typically \(\lambda\sim 10^{-16}\,{\rm s}^{-1}\) for a nucleon).  

2. **Penrose’s gravity‑induced collapse**  
   - The lifetime of a superposition is estimated as  

\[
\tau_{\rm Penrose}\simeq \frac{\hbar}{\Delta E_G},
\]

   where \(\Delta E_G\) is the gravitational self‑energy of the difference between the two mass distributions.  
   - No explicit “clock’’ appears; the *time* that enters is just the inverse of an energy, i.e. a *coordinate‑time* scale defined by the observer’s frame.

Both models are **non‑relativistic**: they assume a single universal time parameter.

---

### 2.2  What breaks when we try to use a particle’s proper time?  

For a massive particle moving with 4‑velocity \(u^\mu\),

\[
d\tau = \sqrt{g_{\mu\nu}u^\mu u^\nu}\, dt .
\]

If we *re‑write* the CSL equation with \(d\tau\) instead of \(dt\), the stochastic term would be multiplied by \(\sqrt{d\tau}\). For a particle that approaches the speed of light, \(d\tau\to0\) and the noise would *vanish*: the wavefunction would never randomise.  

That is **not** what any relativistic collapse theory does, because it would lead to the absurd conclusion that photons are perfectly immune to collapse.

---

### 2.3  Relativistic extensions – the correct “clock’’  

The modern way to make collapse models compatible with relativity is to **anchor the stochastic dynamics to a Lorentz‑scalar spacetime volume element**, *not* to a particle’s proper time.  

#### 2.3.1  Relativistic CSL (RCSL) – a sketch  

*Reference: Tumulka (2006), Bedingham (2011), Pearle & Squires (1994)*  

1. **Field‑theoretic formulation** – The wavefunction is replaced by a quantum field state \(|\Psi\rangle\) on a Cauchy surface \(\Sigma\).  
2. **Noise field** – A classical scalar random field \(w(x)\) is defined on spacetime, with correlation  

\[
\mathbb{E}\bigl[w(x)w(y)\bigr] = \lambda\,\delta^{(4)}(x-y) .
\]

   The delta function is *four‑dimensional*; its argument is a Lorentz invariant spacetime separation.  
3. **Modified Tomonaga–Schwinger equation**  

\[
\frac{\delta |\Psi(\Sigma)\rangle}{\delta \Sigma(x)} 
   = \Bigl[-\frac{i}{\hbar}\mathcal H(x) 
          + \sqrt{\lambda}\,\bigl(\mathcal M(x)-\langle\mathcal M(x)\rangle_\Sigma\bigr) w(x)
          -\frac{\lambda}{2}\bigl(\mathcal M(x)-\langle\mathcal M(x)\rangle_\Sigma\bigr)^2\Bigr] |\Psi(\Sigma)\rangle ,
\]

   where \(\mathcal M(x)\) is a *mass‑density operator* (or, more generally, any Lorentz scalar operator).  

4. **What plays the role of “time’’?**  
   - The **infinitesimal advance of the hypersurface** \(\Sigma\) is measured by the **four‑volume element** \(d^4x\).  
   - The collapse *rate per unit four‑volume* is the constant \(\lambda\).  
   - Consequently, **any world‑line, massive or massless, experiences the same average number of collapses per unit spacetime volume that it traverses**.

#### 2.3.2  Consequences for light‑like trajectories  

* For a photon travelling along a null line, the *proper time* along that line is indeed zero, **but the four‑volume swept out by the photon’s world‑tube is not zero**.  
* In the field picture the photon is described by a *wave‑packet* with a finite spatial extension. As the packet moves, it occupies a region of spacetime of volume  

\[
dV_{\rm tube}=A_\perp\,c\,dt,
\]

   where \(A_\perp\) is the transverse cross‑section of the packet. The stochastic field \(w(x)\) acts everywhere in that tube, so the photon’s quantum state is subject to collapse at the same *coordinate‑time* rate \(\lambda\) (converted to a per‑unit‑proper‑time rate by dividing by the Lorentz factor, which for a null line diverges, cancelling the zero proper time).  

* The **expected number of collapse events** that the photon experiences while it propagates for a laboratory time \(\Delta t\) is  

\[
\langle N_{\rm collapse}\rangle = \lambda\,\Delta V = \lambda\, A_\perp\,c\,\Delta t .
\]

   If we make the packet arbitrarily narrow in the transverse direction, \(A_\perp\to0\) and the rate goes to zero – this reproduces the well‑known fact that CSL couples to **mass density**, and a single photon (zero rest mass) has a *very tiny* coupling.  

* In practice, for realistic optical photons the collapse effect predicted by relativistic CSL is **far below any observable level**, but it is *finite*; it does **not** become infinite because of \(\Delta\tau=0\).

#### 2.3.3  Penrose‑type models  

Penrose’s proposal does **not** invoke a time parameter at all. The collapse time is set by the *gravitational self‑energy* \(\Delta E_G\) of the difference between the two mass distributions. For a photon (or any system with negligible rest mass) \(\Delta E_G\) is essentially zero, so the model predicts an *extremely long* lifetime – but **not an infinite one**; any tiny mass distribution (e.g. the energy of the photon contributes to the stress‑energy tensor) yields a non‑zero \(\Delta E_G\).  

Hence, the “photon paradox’’ is resolved by noting that Penrose’s formula is *frame‑independent*; it does not rely on proper time.

---

### 2.4  Summary of the answer to each sub‑question  

| Sub‑question |Answer (concise)|
|---|---|
|**Parameterisation**|Relativistic collapse models use a **Lorentz‑invariant spacetime volume element** (or equivalently a global foliation) as the clock, not the particle’s proper time.|
|**Time‑dilation effect**|Because the collapse rate is defined per unit *four‑volume*, extreme time dilation does **not** freeze the collapse. For a null trajectory the proper‑time factor disappears, leaving a finite rate proportional to the laboratory time and the spatial extent of the wave‑packet.|
|**Photon paradox**|Photons (and other massless excitations) are **not immune** to spontaneous collapse; the collapse strength is simply extremely small because CSL couples to mass density, and Penrose’s energy‑based estimate is also tiny but finite.|
|**Reconciliation in modern theories**|Relativistic CSL, Tomonaga–Schwinger‑type collapse, and “flash” models (e.g. Tumulka’s relativistic GRW‑f) all embed the stochastic dynamics in a covariant way, ensuring that the collapse law is the same for all observers and does not depend on a particle’s proper time.|

---

## 3.  Final answer  

* In relativistic extensions of spontaneous‑collapse theories the **collapse “clock’’ is a Lorentz‑scalar spacetime volume element**, not the particle’s proper time.  
* Consequently, a light‑like world‑line (where \(\Delta\tau=0\)) does **not** make the superposition last forever; the stochastic field still acts on the photon’s wave‑packet as it sweeps out a non‑zero four‑volume, giving a finite (though usually negligible) collapse probability per unit laboratory time.  
* Penrose’s gravity‑induced collapse likewise yields a finite lifetime that depends on the gravitational self‑energy of the superposed stress‑energy, independent of proper time.  
* Modern relativistic collapse models (relativistic CSL, relativistic GRW‑flash, Tomonaga–Schwinger formulations) therefore **reconcile the apparent mismatch** by making the collapse law covariant, ensuring all observers agree on the rate, and avoiding any paradox associated with \(\Delta\tau=0\) for massless particles.

---

## 4.  Common Mistakes  

| Mistake |Why it’s wrong|How to avoid it|
|---|---|---|
|1. **Using the particle’s proper time as the collapse parameter**|Proper time vanishes for null paths, which would imply zero collapse for photons – contradicts all covariant formulations.|Remember that relativistic collapse models are built from *field* operators; the stochastic coupling is defined per unit **four‑volume**, not per proper time.|
|2. **Assuming CSL works unchanged for photons because the equation contains a mass‑density operator**|The CSL coupling constant \(\lambda\) multiplies the *mass density*; a photon has zero rest mass, so the coupling is extremely weak but not zero (it scales with the energy‑density of the field).|Use the relativistic version where the collapse operator is a Lorentz scalar (e.g. the stress‑energy trace) that also acts on electromagnetic fields.|
|3. **Thinking that time dilation “stretches’’ the collapse time linearly**|Time dilation is a *relative* effect between frames; a covariant collapse law must give the same predictions in all frames.|Check that the collapse rate is expressed as a scalar (e.g. \(\lambda\,d^4x\)), which is invariant under Lorentz transformations.|
|4. **Confusing the “collapse time’’ \(\tau_{\rm Penrose}\) with a proper‑time interval**|Penrose’s formula uses the inverse of a gravitational self‑energy; it is a *coordinate‑time* scale, not a proper‑time measurement.|Identify the dimensional origin of each quantity: energy \(\to\) inverse time in any inertial frame.|
|5. **Neglecting the spatial extension of a photon wave‑packet**|A point‑like null line has zero four‑volume, leading to the illusion of no collapse. Real photons are described by finite‑size wave‑packets, giving a non‑zero spacetime volume.|Always consider the field’s support (cross‑section) when estimating collapse probabilities for massless particles.|

---

*Original question: [How does relativistic proper time dilation ($\Delta\tau = 0$ for lightlike paths) affect spontaneous wavefunction collapse rates?](https://physics.stackexchange.com/questions/876097/how-does-relativistic-proper-time-dilation-delta-tau-0-for-lightlike-paths) on Physics Stack Exchange, licensed CC BY-SA.*

{% endraw %}
