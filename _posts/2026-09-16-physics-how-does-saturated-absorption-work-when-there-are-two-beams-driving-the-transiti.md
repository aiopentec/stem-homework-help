---
layout: question
title: How does saturated absorption work when there are two beams driving the transition?
author: StemFix Bot
category: physics
subject: physics
description: 'Step-by-step physics solution: How does saturated absorption work when
  there are two beams driving the transition?'
tags:
- physics
---

{% raw %}
*As an Amazon Associate, I earn from qualifying purchases.* For more practice problems like this, see [Schaum's Outline of College Physics, 12th Edition](https://www.amazon.com/dp/1259587398?tag=aiopentec20-20).

---

## 1.  What the problem is asking (in plain language)

We have a single two‑level atom that is illuminated **simultaneously** by two resonant laser beams that travel in opposite directions  

* Beam A : propagates in the \(+\hat x\) direction, intensity \(I_A = 1000\,I_{\rm sat}\)  
* Beam B : propagates in the \(-\hat x\) direction, intensity \(I_B = 100\,I_{\rm sat}\)

Both beams are exactly on resonance with the atomic transition (no Doppler shift, no Zeeman shift, etc.).  

The question is:  

*What fraction of the total scattering events comes from each beam?*  

In other words, does the atom absorb photons equally from the two beams (Option 1) or does it absorb them in proportion to the beam intensities (Option 2)?

---

## 2.  Step‑by‑step solution  

### 2.1  Model of a driven two‑level atom  

We treat the atom as a closed two‑level system \(|g\rangle \leftrightarrow |e\rangle\) with spontaneous decay rate \(\Gamma\) from \(|e\rangle\) to \(|g\rangle\).  
The atom is driven by classical electric fields; quantum‑optical derivations give the same steady‑state results.

Define the **saturation parameter** for a single beam

\[
s_i \equiv \frac{I_i}{I_{\rm sat}} ,
\qquad
I_{\rm sat}= \frac{\pi h c \Gamma}{3\lambda^{3}} \;(\text{for a closed transition}),
\]

where \(i = A,B\).  
When several resonant beams illuminate the atom, the total **on‑resonance saturation parameter** is simply the sum of the individual ones because the optical Bloch equations contain the total Rabi frequency squared:

\[
s_{\rm tot}= s_A + s_B .
\]

(If the two beams are mutually incoherent – as is the usual situation for independent lasers – there is no interference term.  If they are phase‑locked, a standing‑wave intensity pattern appears, but the **average** over many atoms gives the same result, as shown at the end.)

### 2.2  Steady‑state excited‑state population  

The optical Bloch equations for resonant driving give, in the steady state,

\[
\rho_{ee}^{\;(\text{ss})}= \frac{s_{\rm tot}}{2\bigl(1+s_{\rm tot}\bigr)} .
\]

The **total scattering rate** (number of spontaneously emitted photons per unit time) is

\[
R_{\rm sc}= \Gamma\,\rho_{ee}^{\;(\text{ss})}
           = \Gamma\,\frac{s_{\rm tot}}{2\bigl(1+s_{\rm tot}\bigr)} .
\]

When \(s_{\rm tot}\gg 1\) the factor \(\frac{s_{\rm tot}}{1+s_{\rm tot}}\) approaches 1, so \(R_{\rm sc}\to \Gamma/2\), i.e. the well‑known saturation limit.

### 2.3  How many photons are **absorbed** from each beam?  

Absorption from a given beam is proportional to the product of:

* the intensity (or saturation parameter) of that beam, and  
* the **ground‑state** population \(\rho_{gg}=1-\rho_{ee}= \frac{1}{1+s_{\rm tot}}\).

Thus the **absorption (and consequently the scattering) rate contributed by beam i** is

\[
R_i = \frac{\Gamma}{2}\,
      \frac{s_i}{1+s_{\rm tot}} .
\tag{1}
\]

Notice that the sum of the two contributions reproduces the total rate:

\[
R_A+R_B = \frac{\Gamma}{2}\,\frac{s_A+s_B}{1+s_{\rm tot}}
        = \Gamma\frac{s_{\rm tot}}{2(1+s_{\rm tot})}=R_{\rm sc}.
\]

Equation (1) is the key result: **the fraction of scattering events that originates from a particular beam is simply the ratio of its saturation parameter to the total saturation parameter.**  

\[
\boxed{\displaystyle 
\frac{R_i}{R_{\rm sc}} = \frac{s_i}{s_A+s_B}
}
\tag{2}
\]

### 2.4  Plug in the numbers  

\[
s_A = 1000 ,\qquad s_B = 100 ,\qquad s_{\rm tot}=1100 .
\]

*Total scattering rate*

\[
R_{\rm sc}= \Gamma\frac{1100}{2(1101)}
          \approx 0.4995\,\Gamma \;\approx\; \frac{\Gamma}{2}.
\]

*Scattering from the forward beam (A)*  

\[
R_A = \frac{\Gamma}{2}\,\frac{1000}{1101}
    = \frac{10}{11}\;R_{\rm sc}\; .
\]

*Scattering from the backward beam (B)*  

\[
R_B = \frac{\Gamma}{2}\,\frac{100}{1101}
    = \frac{1}{11}\;R_{\rm sc}\; .
\]

Thus **10/11 of the emitted photons come from the intense \(+\hat x\) beam and 1/11 from the weaker \(-\hat x\) beam**.

### 2.5  Remarks on coherence / standing‑wave effects  

If the two lasers are phase‑locked, the intensity at position \(x\) is

\[
I(x)=I_A+I_B+2\sqrt{I_AI_B}\cos(2kx) .
\]

The **local** saturation parameter varies between \((\sqrt{s_A}\pm\sqrt{s_B})^{2}\).  
An atom at a fixed position would therefore see a position‑dependent scattering fraction given by Eq. (2) with the **local** \(s_i\).  
However, for an ensemble of atoms uniformly distributed over many wavelengths, the spatial average of \(\cos(2kx)\) is zero, and the average fractions reduce exactly to the intensity‑ratio result derived above. Hence the answer is the same for incoherent or mutually coherent beams when we speak about the *average* scattering.

---

## 3.  Final answer  

The atom scatters photons at (essentially) the saturation limit \(\Gamma/2\).  
The **fraction** of those photons that originated from each beam is proportional to the beam’s intensity (its saturation parameter).  

\[
\boxed{
\begin{aligned}
\text{Scattering from }+\hat x\text{ beam} & = \frac{10}{11}\;R_{\rm sc},\\[4pt]
\text{Scattering from }-\hat x\text{ beam} & = \frac{1}{11}\;R_{\rm sc}.
\end{aligned}}
\]

So **Option 2** is the correct description.

---

## 4.  Common Mistakes  

| Mistake | Why it is wrong | Correct reasoning |
|---------|----------------|-------------------|
| **Assuming each beam independently produces a scattering rate of \(\Gamma/2\).** | The atom can be in only one internal state at a time; the excited‑state population is limited by the *total* drive, not by each beam separately. | The total saturation parameter is the sum \(s_A+s_B\); the excited‑state fraction is \(\frac{s_{\rm tot}}{2(1+s_{\rm tot})}\). |
| **Neglecting the depletion of the ground state.** | At high intensity most atoms are already in the excited state, so the absorption probability from any beam is reduced. | Absorption rate from beam \(i\) contains the factor \(\rho_{gg}=1/(1+s_{\rm tot})\). |
| **Thinking the scattered photon “belongs” to the beam that emitted it.** | Spontaneous emission is isotropic and unrelated to the direction of the absorbed photon; only the *absorption* step cares about the beam. | The fraction of absorptions from each beam is given by Eq. (1); the subsequent spontaneous emission does not retain directional memory. |
| **Treating the two beams as a single beam of intensity \(I_A+I_B\) and then dividing the scattering equally.** | The division equally would be true only if the beams had the same intensity; the absorption probability scales with intensity. | The relative contributions follow the intensity ratio, Eq. (2). |
| **Ignoring the possibility of interference (standing wave).** | If the beams are coherent, a standing‑wave pattern does appear, but the *spatial average* over many atoms reproduces the same intensity‑ratio result. | For a single atom at a fixed node/antinode the local rate changes, but the average over a wavelength gives the same fractions as above. |
| **Using photon‑counting intuition (“the atom randomly picks a photon”).** | Photons are not independent classical particles when the atom is saturated; the atom’s transition is driven by the *coherent* field amplitude, not by discrete photon “choices”. | The optical Bloch equations give the correct rates; the result is intensity‑weighted, not a random coin‑flip. |

Keeping these points in mind will prevent the most frequent errors when dealing with saturated absorption in the presence of multiple driving beams.

*Original question: [How does saturated absorption work when there are two beams driving the transition?](https://physics.stackexchange.com/questions/876021/how-does-saturated-absorption-work-when-there-are-two-beams-driving-the-transiti) on Physics Stack Exchange, licensed CC BY-SA.*

{% endraw %}
